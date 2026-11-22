# frozen_string_literal: true

# Build-time Mermaid prerendering.
#
# The Markdown source keeps normal ```mermaid fences. During the build:
#
#   1. a Generator collects every Mermaid block and asks the Node renderer to
#      produce one SVG per theme (light/dark) in assets/img/mermaid;
#   2. a :post_convert hook replaces the rendered <pre><code> block with a
#      <figure> containing the two SVGs.
#
# The Node renderer is `tools/mermaid/render.mjs`. It uses a single headless
# Chromium instance and caches each SVG by a hash of its source.

require 'cgi'
require 'digest'
require 'fileutils'
require 'json'
require 'open3'
require 'tempfile'

module MermaidPrerender
  MANIFEST_KEY = 'mermaid_prerender_manifest'
  OUT_DIR = File.join('assets', 'img', 'mermaid')
  SCRIPT = File.expand_path('../tools/mermaid/render.mjs', __dir__)

  FENCE_RE = /^```mermaid[ \t]*\r?\n(.*?)^```[ \t]*$/m
  HTML_RE = %r{<pre><code class="language-mermaid">(.*?)</code></pre>}m

  module_function

  def enabled?
    ENV['MERMAID_RENDER'] != '0'
  end

  def render_all(site)
    return unless enabled?

    blocks = collect_blocks(site)

    if blocks.empty?
      site.config[MANIFEST_KEY] = {}
      return
    end

    Jekyll.logger.info 'Mermaid:', "Rendering #{blocks.length} diagram(s)..."
    manifest = invoke_renderer(site, blocks)
    site.config[MANIFEST_KEY] = manifest
    register_static_files(site, manifest)
    Jekyll.logger.info 'Mermaid:', "Done (#{manifest.length} diagram(s))."
  rescue StandardError => e
    handle_failure(e, site)
  end

  def collect_blocks(site)
    blocks = []
    seen = {}

    site.posts.docs.each do |post|
      next unless post.content

      post.content.scan(FENCE_RE) do |match|
        code = normalize(match[0])
        next if code.empty?

        id = digest(code)
        next if seen[id]

        seen[id] = true
        blocks << { 'id' => id, 'code' => code }
      end
    end

    blocks
  end

  def invoke_renderer(site, blocks)
    unless File.file?(SCRIPT)
      raise "renderer not found: #{SCRIPT}"
    end

    out_dir = File.join(site.source, OUT_DIR)
    FileUtils.mkdir_p(out_dir)

    input = Tempfile.new(['mermaid-input', '.json'])
    output = Tempfile.new(['mermaid-manifest', '.json'])

    begin
      input.write(JSON.generate('blocks' => blocks))
      input.close
      output.close

      node = ENV['MERMAID_NODE'] || 'node'
      cmd = [
        node,
        SCRIPT,
        '--input', input.path,
        '--manifest', output.path,
        '--out', out_dir
      ]

      stdout, stderr, status = Open3.capture3(*cmd, chdir: File.dirname(SCRIPT))
      Jekyll.logger.debug 'Mermaid:', stdout unless stdout.empty?

      unless status.success?
        raise "renderer exited #{status.exitstatus}: #{stderr.strip[0, 4000]}"
      end

      JSON.parse(File.read(output.path))
    ensure
      input.close! unless input.closed?
      output.close! unless output.closed?
    end
  end

  def register_static_files(site, manifest)
    rel_dir = OUT_DIR.tr('\\', '/')

    manifest.each_value do |entry|
      entry.each_value do |info|
        name = info['file']
        next unless name

        generated_path = File.join(site.source, rel_dir, name)
        next if site.static_files.any? { |file| file.path == generated_path }

        site.static_files << Jekyll::StaticFile.new(
          site,
          site.source,
          rel_dir,
          name
        )
      end
    end
  end

  def replace(post)
    manifest = post.site.config[MANIFEST_KEY]
    return if manifest.nil? || manifest.empty?

    baseurl = post.site.baseurl.to_s.chomp('/')
    post.content = post.content.gsub(HTML_RE) do
      raw = Regexp.last_match(1)
      code = normalize(CGI.unescapeHTML(raw))
      id = digest(code)
      entry = manifest[id]

      unless entry
        raise "missing manifest entry for #{post.relative_path} (#{id})"
      end

      light = entry['light']
      dark = entry['dark']
      raise "missing light SVG for #{id}" unless light
      raise "missing dark SVG for #{id}" unless dark

      alt = alt_text(code)
      light_src = "#{baseurl}/#{OUT_DIR.tr('\\', '/')}/#{light['file']}"
      dark_src = "#{baseurl}/#{OUT_DIR.tr('\\', '/')}/#{dark['file']}"

      <<~HTML
        <figure class="mermaid-diagram">
          <img class="mermaid-light" src="#{CGI.escapeHTML(light_src)}" alt="#{CGI.escapeHTML(alt)}" width="#{light['width']}" height="#{light['height']}" loading="lazy" decoding="async">
          <img class="mermaid-dark" src="#{CGI.escapeHTML(dark_src)}" alt="#{CGI.escapeHTML(alt)}" width="#{dark['width']}" height="#{dark['height']}" loading="lazy" decoding="async">
        </figure>
      HTML
    end
  rescue StandardError => e
    raise Jekyll::Errors::FatalException,
          "Mermaid prerender failed for #{post.relative_path}: #{e.message}"
  end

  def normalize(code)
    code.to_s.gsub("\r\n", "\n").strip
  end

  def digest(code)
    Digest::SHA256.hexdigest(code)[0, 16]
  end

  def alt_text(code)
    code[/^\s*accTitle:\s*(.+)$/i, 1]&.strip || 'Mermaid diagram'
  end

  def handle_failure(error, site)
    message = "Mermaid prerender failed: #{error.message}"

    if Jekyll.env == 'production'
      raise Jekyll::Errors::FatalException, message
    end

    Jekyll.logger.warn(
      'Mermaid:',
      "#{message} (development build; diagrams stay as code blocks)"
    )
    site.config[MANIFEST_KEY] = {}
  end
end

class MermaidPrerenderGenerator < Jekyll::Generator
  safe true
  priority :low

  def generate(site)
    MermaidPrerender.render_all(site)
  end
end

Jekyll::Hooks.register :posts, :post_convert do |post|
  MermaidPrerender.replace(post)
end

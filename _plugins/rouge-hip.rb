# -*- coding: utf-8 -*- #
# frozen_string_literal: true

# Custom Rouge lexer for HIP (ROCm).
#
# HIP is a CUDA-compatible, single-source C++ kernel language maintained by
# AMD. It intentionally reuses the CUDA language extensions (`__global__`,
# `<<<...>>>` kernel launches, ...) so this lexer subclasses Rouge's `CUDA`
# lexer and only adds the AMD/ROCm-specific pieces:
#   * qualifiers   e.g. `__launch_bounds__`, `__no_patch__`, `__grid_constant__`
#   * types        e.g. `half`, `hipStream_t`, `hipLaunchParm`, ...
#   * launch APIs  e.g. `hipLaunchKernelGGL`, `hipLaunchKernel`, ...
#   * coordinate   e.g. `hipThreadIdx_x`, `hipBlockDim_y`, ... (ROCm 7+)
# builtins            and the CUDA-compatible `threadIdx`, `blockIdx`, ...
#
# Reference: https://rocm.docs.amd.com/projects/HIP/en/latest/ (HIP C++ language extensions)

require 'set'
require 'rouge'
require 'rouge/lexers/cuda'

module Rouge
  module Lexers
    class Hip < CUDA
      title 'HIP'
      desc 'HIP: Heterogeneous-Compute Interface for Portability (ROCm GPU programming)'

      tag 'hip'
      aliases 'hipcpp'
      filenames '*.hip', '*.hip.cpp', '*.hip.cc', '*.hip.hpp', '*.hip.inl'

      # __host__/__device__/__global__/__shared__/... are inherited from CUDA;
      # these are the qualifiers HIP layers on top.
      def self.keywords
        @keywords ||= super + Set.new(%w(
          __launch_bounds__ __no_patch__ __grid_constant__
        ))
      end

      # HIP builtin scalar, vector and API-handle types.
      def self.keywords_type
        @keywords_type ||= super + Set.new(%w(
          half __half __half2 __nv_bfloat16 __nv_bfloat162
          hipLaunchParm
          hipCtx_t hipDevice_t hipDeviceptr_t hipFunction_t hipModule_t
          hipStream_t hipEvent_t hipError_t hipMemcpyKind hipMemoryType
          hipSharedMemConfig hipFuncCache hipDeviceProp_t hipPointerProp_t
          hipGridGeometry hipWorkGeometry
        ))
      end

      # HIP launch macros and built-in coordinate variables. NB: inherited
      # `builtins` is an Array, so concatenate with [], not Set.
      def self.builtins
        @builtins ||= super + %w(
          hipLaunchKernelGGL hipLaunchKernel
          HIP_KERNEL_NAME HIP_DYNAMIC_SHARED
          hipThreadIdx_x hipThreadIdx_y hipThreadIdx_z
          hipBlockIdx_x hipBlockIdx_y hipBlockIdx_z
          hipBlockDim_x hipBlockDim_y hipBlockDim_z
          hipGridDim_x hipGridDim_y hipGridDim_z
          hipWorkDim_x hipWorkDim_y hipWorkDim_z
          hipMaxWorkDim
          threadIdx blockIdx blockDim gridDim warpSize
        )
      end
    end
  end
end
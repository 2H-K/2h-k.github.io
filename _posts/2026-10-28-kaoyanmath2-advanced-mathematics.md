---
title: "数二 · 高等数学笔记"
description: 无
date: 2026-10-28 19:30:00 +0800
categories: ["数学二", "高数"]
math: true
---

> 适用范围：数二（高数 + 线代）。数二高数不考：空间解析几何、三重积分、曲线/曲面积分、无穷级数。
> 每章结构：定义定理 → 判定流程 → 例题 → 易错点。速查表只留三处：极限选法（§1.5.2）、定积分应用（§3.4.1）、二重积分（§5.5）；公式汇总见附录。
> 用法：第一遍读定义和判定流程；做题卡住时查对应速查表；考前只看绿色结论和章末易错点。

> 全文颜色约定：<span class="hl-red">红色 = 符号 / 易错</span>，<span class="hl-orange">橙色 = 条件 / 区别</span>，<span class="hl-green">绿色 = 结论 / 必背</span>，<span class="hl-blue">蓝色 = 定义 / 基本关系</span>。

---

## 第一章 函数、极限、连续

### 1.1 函数

**定义**：设数集 $D\subset\mathbb{R}$，若存在对应法则 $f$，使每个 $x\in D$ 都有唯一确定的 $y$ 与之对应，则称 $f:D\to\mathbb{R}$ 为定义在 $D$ 上的函数，记 $y=f(x)$。$D$ 为定义域，$$f(D)=\{f(x)\mid x\in D\}$$ 为值域。

**几个特殊函数**：

- 绝对值函数：$$\lvert x\rvert =\begin{cases}x,&x\ge0\\-x,&x<0\end{cases}$$
- 符号函数：$$\operatorname{sgn}x=\begin{cases}1,&x>0\\0,&x=0\\-1,&x<0\end{cases}$$，有 $x=\lvert x\rvert \operatorname{sgn}x$
- 取整函数：$[x]$（不超过 $x$ 的最大整数），有 $x-1<[x]\le x$，$[x+n]=[x]+n$

**函数的四种特性**（判定流程见 §1.1.1，结论见 §1.1.2，例题见 §1.1.3）：

| 特性 | 定义 | 判定动作 |
|---|---|---|
| 有界性 | $\exists M>0$，使 $\lvert f(x)\rvert \le M,\ \forall x\in X$；否则无界 | 找"危险点"：区间端点、间断点、$x\to\infty$ 的行为 |
| 单调性 | 单增：$x_1<x_2\Rightarrow f(x_1)<f(x_2)$；单减：$x_1<x_2\Rightarrow f(x_1)>f(x_2)$ | 定义法（取两点比）/ 导数法 $f'\gtrless0$（§2.5） |
| 奇偶性 | 定义域关于原点对称；$f(-x)=f(x)$ 为偶，$f(-x)=-f(x)$ 为奇 | <span class="hl-orange">先查定义域</span>，再算 $f(-x)$ 并化简比较 |
| 周期性 | $\exists T>0$，$f(x+T)=f(x),\ \forall x\in D$ | 找"平移不变"结构；证"不是周期"时比较 $f(x+T)$ 与 $f(x)$ |

> **【大纲定位】** 数二大纲对四性的要求是"<span class="hl-orange">了解</span>"：直接考多是选择/填空里的"性质判断题"，更多时候是作为**解题工具**出现在证明题与计算题中（什么时候该想到它，见 §1.1.2）。

#### 1.1.1 判定流程：Step 0–4

**Step 0 · 先看定义域**：定义域是一切判定的地基。
- 定义域不关于原点对称 ⇒ 直接出局"奇/偶"（如 $\ln x$、$y=\frac{1}{x-1}$）；
- 定义域有"洞"（$\tan x$、$\frac{1}{x}$）⇒ 先看洞附近是否 $\to\pm\infty$，这直接决定有界性。

**Step 1 · 奇偶（最快、结论最硬）**：定义域对称 + 化简 $f(-x)$。
- $f(-x)=f(x)$ ⇒ 偶；$f(-x)=-f(x)$ ⇒ 奇；都不满足 ⇒ 非奇非偶；
- <span class="hl-red">$f\equiv0$ 既奇又偶</span>；奇函数必有 $f(0)=0$（若 $0\in D$）。

**Step 2 · 周期**：找"加上同一个数后不变"的结构。
- 直接成立：$f(x+T)=f(x)$；
- 变号型：$f(x+a)=-f(x)\Rightarrow 2a$ 是周期；
- 取倒数型：$f(x+a)=\frac{1}{f(x)}\Rightarrow 2a$ 是周期；
- 平移加常数型：$f(x+a)=f(x)+b\ (b\ne0)\Rightarrow$ <span class="hl-red">无周期</span>；
- <span class="hl-orange">证"不是周期函数"的严格写法</span>：假设存在周期 $T>0$，把 $f(x+T)$ 算出来与 $f(x)$ 比；若含 $x$ 这类非周期因子，比系数会逼出 $T=0$，矛盾（例 1）。

**Step 3 · 单调**：三选一。
- 定义法：取 $x_1<x_2$ 比较 $f(x_1),f(x_2)$（适合分段函数、选择题）；
- 导数法：$f'(x)>0$（$<0$）⇒ 单调增（减）（§2.5）；
- 复合保序：内增外增得增、内增外减得减、内减外增得减、内减外减得增；
- <span class="hl-orange">与奇偶联动</span>：奇函数在关于原点对称的两个区间上单调性<span class="hl-green">相同</span>，偶函数<span class="hl-orange">相反</span>。

**Step 4 · 有界**：先找"危险点"，再看三类有界源。
- 危险点：区间端点、间断点、$x\to\infty$ 的行为（$\tan x$ 型）；
- 有界源：$\lvert\sin x\rvert\le1$、$\lvert\operatorname{arctan}x\rvert\le\frac{\pi}{2}$、<span class="hl-green">闭区间上连续 ⇒ 有界</span>（§1.6）、<span class="hl-green">有界 × 无穷小 = 0</span>（§1.5）；
- <span class="hl-orange">证无界的标准写法</span>：构造 $x_k\to\infty$（或趋近间断点），使 $\lvert f(x_k)\rvert\to\infty$。

#### 1.1.2 必背结论

1. 奇函数：$f(0)=0$（若 $0\in D$）；在关于原点对称的区间上单调性相同。偶函数单调性相反。<span class="hl-red">$f\equiv0$ 既奇又偶</span>。
2. 周期 + 单调 ⇒ 常函数；周期 + 连续 ⇒ 在 $\mathbb{R}$ 上有界；周期函数在无穷远处极限存在 ⇒ 常函数（例 3）。
3. 周期函数积分：$\int_a^{a+T}f=\int_0^T f$，每个周期上的积分相等。
4. 严格单调 ⇒ 单射 ⇒ 有反函数；$f$ 与 $f^{-1}$ 单调性相同，图像关于 $y=x$ 对称。
5. 偶函数在 $0$ 处可导 ⇒ $f'(0)=0$；<span class="hl-orange">奇函数不一定</span>（§1.7 表 A），但奇函数处处可导时 $f'$ 是偶函数。
6. 奇函数若在 $0$ 处取极值且可导，则 $f'(0)=0$（费马引理，§2.4）。
7. $f$ 奇 ⇒ $\int_0^x f(t)dt$ 偶；$f$ 偶 ⇒ $\int_0^x f(t)dt$ 奇（2024 数二选择题）。
8. 闭区间上连续 ⇒ 有界，且取得最大值最小值（§1.6）。
9. 有界 × 无穷小 $=0$；无穷大 ÷ 有界（极限非 $0$）$=$ 无穷大。
10. 证明方程有唯一解 $=$ <span class="hl-green">连续给存在，单调给唯一</span>（例 4）。

**用到哪去找**：对称区间定积分、二重积分对称性见 §3.2、§5.3；单调有界准则见 §1.2；极值与不等式证明见 §2.5。

#### 1.1.3 例题：四性怎么用

**例 1 · 四性判断（选择题的逐项排除法）**：设 $f(x)=x\tan x\cdot e^{\sin x}$，则 $f$ 是（　）　A. 偶函数　B. 无界函数　C. 周期函数　D. 单调函数

<span class="hl-blue">信号识别</span>：四个选项正好对应四性 ⇒ <span class="hl-green">逐项排除</span>，顺序按 Step 1→4。

- **A（偶）**：$f(-x)=(-x)\tan(-x)e^{-\sin x}=x\tan x\,e^{-\sin x}\ne f(x)$ ⇒ 非偶 ⇒ A 错。
- **C（周期）**：设 $T>0$ 为周期。由 $f(0)=0=f(T)$ 且 $T>0$ 得 $\tan T=0$，即 $T=k\pi$（$k\ge1$）。于是 $\tan(x+T)=\tan x$、$\sin(x+T)=\sin x$，代入 $f(x+T)=f(x)$ 得 $(x+T)e^{\sin x}=xe^{\sin x}$ ⇒ $T=0$，与 $T>0$ 矛盾 ⇒ 非周期 ⇒ C 错。
- **D（单调）**：取 $x_1=\frac{\pi}{4}<x_2=\frac{3\pi}{4}$，有 $f(x_1)>0>f(x_2)$，与单增矛盾；再取 $x_1=\frac{3\pi}{4}<x_2=\frac{5\pi}{4}$，有 $f(x_1)<0<f(x_2)$，与单减矛盾 ⇒ 非单调 ⇒ D 错。
- **B（无界）**：取 $x_k=2k\pi+\frac{\pi}{2}\to+\infty$，$\tan x_k\to+\infty$，$x_ke^{\sin x_k}\to\infty$，故 $\lvert f(x_k)\rvert\to\infty$ ⇒ 无界。

答案：<span class="hl-green">B</span>。

**例 2 · 有界性判定（只看危险点）**：$f(x)=\frac{\lvert x\rvert\sin(x-2)}{x(x-1)(x-2)^2}$ 在下列哪个区间内有界（　）　A. $(-1,0)$　B. $(0,1)$　C. $(1,2)$　D. $(2,3)$

<span class="hl-blue">信号识别</span>："在某区间是否有界" ⇒ 区间内部连续 ⇒ 只需检查**端点与间断点邻域**（局部有界性，§1.3）。

- B：$x\to1^{-}$ 时分子 $\to\sin(-1)\ne0$、分母 $\to0$ ⇒ $\lvert f\rvert\to\infty$ ⇒ 无界；
- C、D：$x\to2$ 时 $\sin(x-2)\sim-(x-2)$，分母含 $(x-2)^2$，故 $f\sim-\frac{1}{x-2}$ ⇒ 无界；
- A：唯一危险点 $x\to0^{-}$：$f=\frac{\lvert x\rvert}{x}\cdot\frac{\sin(x-2)}{(x-1)(x-2)^2}\to(-1)\cdot\frac{-\sin2}{-4}=-\frac{\sin2}{4}$，有限 ⇒ 有界。

答案：<span class="hl-green">A</span>。

**例 3 · 周期性 → 常函数（极限型）**：设 $f$ 是以 $T>0$ 为周期的连续函数，且 $\lim_{x\to+\infty}f(x)=A$ 存在，证明 $f(x)\equiv A$。

证明：任取 $x\in\mathbb{R}$，令 $x_n=x+nT\to+\infty$。由周期性 $f(x_n)=f(x)$（与 $n$ 无关）；由极限存在 $f(x_n)\to A$。由数列极限唯一性，$f(x)=A$。

<span class="hl-orange">对照</span>：$\sin x$、$\tan x$ 有周期但无穷远处极限不存在——"周期 + 无穷远极限"这个组合本身就是强信号。

**例 4 · 单调 + 连续 → 唯一解（证明题模板）**：证明方程 $x-\sin x-1=0$ 在 $[0,\pi]$ 上有唯一解。

- 存在性：$F(x)=x-\sin x-1$ 在 $[0,\pi]$ 上连续，$F(0)=-1<0$，$F(\pi)=\pi-1>0$ ⇒ 零点定理（§1.6）；
- 唯一性：$F'(x)=1-\cos x\ge0$ ⇒ $F$ 单调不减 ⇒ $F$ 至多有一个零点 ⇒ 唯一。

<span class="hl-green">套路</span>："证明方程有唯一解" = <span class="hl-green">连续性给存在，单调性给唯一</span>，两个关键词缺一不可。

**例 5 · 奇偶性 → 定积分化简**：设 $f$ 在 $[-1,1]$ 上连续且为奇函数，求 $\int_{-1}^{1}f(x)dx$；若 $f$ 为偶函数呢？

- 奇：$\int_{-1}^{1}f=0$（对称区间上奇函数的积分为 $0$，§3.2）；
- 偶：$\int_{-1}^{1}f=2\int_{0}^{1}f$。

变上限版本（2024 数二真题）：设 $f(x)=\int_{0}^{\sin x}\sin^{3}t\,dt$，$g(x)=\int_{0}^{x}f(t)\,dt$，判断 $f,g$ 的奇偶性。

- $\sin^{3}t$ 是奇函数 ⇒ $h(x)=\int_{0}^{x}\sin^{3}t\,dt$ 是偶函数；
- $f(x)=h(\sin x)$：偶函数复合 $\sin$ 仍是偶函数；
- $f$ 偶 ⇒ $g(x)=\int_{0}^{x}f(t)dt$ 是奇函数。

答案：<span class="hl-green">$f$ 偶、$g$ 奇</span>。

**反函数**：$y=f(x)$ 单射（如单调）才有反函数 $x=f^{-1}(y)$，习惯写成 $y=f^{-1}(x)$。$f$ 与 $f^{-1}$ 图像关于 $y=x$ 对称，单调性相同（见 §1.1.2 第 4 条）。

**复合函数**：$y=f(u),\ u=g(x)$，$y=f[g(x)]$。

**基本初等函数**：幂函数、指数函数、对数函数、三角函数、反三角函数。

**三角函数恒等式**：

$$\sin^2x+\cos^2x=1,\quad 1+\tan^2x=\sec^2x,\quad 1+\cot^2x=\csc^2x$$

$$\sin 2x=2\sin x\cos x,\quad \cos2x=\cos^2x-\sin^2x=2\cos^2x-1=1-2\sin^2x$$

$$\sin x+\sin y=2\sin\frac{x+y}{2}\cos\frac{x-y}{2},\quad \sin x-\sin y=2\cos\frac{x+y}{2}\sin\frac{x-y}{2}$$

$$\cos x+\cos y=2\cos\frac{x+y}{2}\cos\frac{x-y}{2},\quad \cos x-\cos y=-2\sin\frac{x+y}{2}\sin\frac{x-y}{2}$$

**反三角函数**：

$$\arcsin x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right],\quad \arccos x\in[0,\pi],\quad \arctan x\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$$

$$\arcsin x+\arccos x=\frac{\pi}{2},\quad \arctan x+\operatorname{arccot}x=\frac{\pi}{2}$$

### 1.2 数列极限

**定义（$\varepsilon$-$N$）**：$\lim_{n\to\infty}x_n=a\iff \forall\varepsilon>0,\ \exists N\in\mathbb{N}^+$，当 $n>N$ 时，$\lvert x_n-a\rvert <\varepsilon$。

**收敛数列的性质**：

1. 极限唯一；
2. 有界性：收敛数列必有界（无界必发散）；
3. 保号性：若 $\lim x_n=a>0$（或 $<0$），则 $\exists N$，$n>N$ 时 $x_n>0$（或 $<0$）；
4. 收敛数列的子列也收敛，且极限相同。

**推论**：若有两个子列收敛于不同值，则数列发散（常用于判断含 $(-1)^n$、分段数列）。改变数列的有限项不影响其极限。若 $\lim_{n\to\infty}\frac{x_{n+1}}{x_n}=1$，<span class="hl-red">不能推出数列收敛</span>（反例：$x_n=n$）。

**存在准则**：

- 单调有界准则：单调有界数列必有极限；
- 夹逼准则：$y_n\le x_n\le z_n$，且 $\lim y_n=\lim z_n=a$，则 $\lim x_n=a$。

> **【理解】** 递推数列用单调有界准则时，单调性三条路并列：作差 $x_{n+1}-x_n$、作商 $\frac{x_{n+1}}{x_n}$、<span class="hl-green">单调中介</span>。第三条：$g$ 在取值范围内严格单调，则比较 $x_{n+1}$ 与 $x_n$ 等价于比较 $g(x_{n+1})$ 与 $g(x_n)$（$g$ 严格增则不等号同向，严格减则反向）。$g$ 从题面读——$x_n>0$ 且递推含 $e^{x}$，取 $g(x)=e^x$；含 $\ln x$ 取 $\ln x$；含 $\arctan x$ 取 $\arctan x$。例如证 $x_{n+1}<x_n$，改证 $e^{x_{n+1}}<e^{x_n}$，把递推代入后指数自己消掉。这就是用一个明显单调的函数当桥梁，原数列的单调性跟着过来。

### 1.3 函数极限

**定义**：$\lim_{x\to x_0}f(x)=A\iff \forall\varepsilon>0,\ \exists\delta>0$，当 $0<\lvert x-x_0\rvert <\delta$ 时，$\lvert f(x)-A\rvert <\varepsilon$。

- 左极限 $f(x_0^-)$、右极限 $f(x_0^+)$；
- 极限存在 $\iff$ 左右极限都存在且相等。

**性质**：唯一性、局部有界性、局部保号性。

**函数极限与数列极限的关系**：

- 若 $\lim_{x\to x_0}f(x)=A$，则对任意 $x_n\to x_0$（$x_n\ne x_0$），都有 $\lim f(x_n)=A$；
- 若能找到两个趋于 $x_0$ 的数列使 $f(x_n)$ 极限不同，则 $\lim f(x)$ 不存在。

**两个重要极限**：

<div class="hl-green" markdown="1">

$$\lim_{x\to0}\frac{\sin x}{x}=1,\qquad \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e\ \left(\text{即}\ \lim_{x\to0}(1+x)^{1/x}=e\right)$$

</div>

### 1.4 无穷小与无穷大

**无穷小**：极限为 $0$ 的变量。无穷小与函数极限的关系：$\lim f(x)=A\iff f(x)=A+\alpha$，其中 $\alpha\to0$。

**无穷大**：绝对值无限增大（$\forall M>0,\ \exists\delta,\ 0<\lvert x-x_0\rvert <\delta$ 时 $\lvert f(x)\rvert >M$）。无穷大与无穷小：在同一极限过程中，无穷大的倒数为无穷小；非零无穷小的倒数为无穷大。

**无穷小的比较**（设 $\alpha,\beta\to0$，且 $\lim\frac{\beta}{\alpha}=c$）：

- $c=0$：$\beta$ 是 $\alpha$ 的高阶无穷小，记 $\beta=o(\alpha)$；
- $c\ne0$：同阶无穷小；
- $c=1$：等价无穷小，记 $\alpha\sim\beta$；
- $\lim\frac{\beta}{\alpha^k}=c\ne0$：$\beta$ 是 $\alpha$ 的 $k$ 阶无穷小。

**等价无穷小替换定理**：$\alpha\sim\alpha',\ \beta\sim\beta'$，且 $\lim\frac{\beta'}{\alpha'}$ 存在，则 $\lim\frac{\beta}{\alpha}=\lim\frac{\beta'}{\alpha'}$。

> 注意：等价无穷小只能用于**乘除因子**，<span class="hl-red">加减中不能直接替换</span>（加减需用泰勒展开）。→ 什么信号下必须改用泰勒，见 §1.5.2。

**常用等价无穷小（$x\to0$）**：

$$\sin x\sim\tan x\sim\arcsin x\sim\arctan x\sim x,\quad e^x-1\sim x,\quad a^x-1\sim x\ln a$$

$$\ln(1+x)\sim x,\quad 1-\cos x\sim\frac12x^2,\quad (1+x)^a-1\sim ax$$

$$\sqrt{1+x}-1\sim\frac12x,\quad x-\sin x\sim\frac16x^3,\quad x-\tan x\sim-\frac13x^3$$

$$\sqrt{1+x^2}-1\sim\frac12x^2$$

$$\tan x-x\sim\frac13x^3,\quad x-\arcsin x\sim-\frac16x^3,\quad x-\arctan x\sim\frac13x^3$$

$$\sec x-1\sim\frac12x^2,\quad x-\ln(1+x)\sim\frac12x^2$$

> **【理解】** 高阶等价无穷小由泰勒展开直接得到，不必单独记：$\sin x=x-\frac{x^3}{6}+o(x^3)$，故 $x-\sin x\sim\frac{x^3}{6}$；$\tan x=x+\frac{x^3}{3}+o(x^3)$，故 $\tan x-x\sim\frac{x^3}{3}$。（各函数的完整展开见 §1.5.3 泰勒展开表）

### 1.5 极限计算方法（七种未定式）

> 本节两层：<span class="hl-green">1.5.1–1.5.2 选工具</span>（看信号定方法），1.5.3 是逐型手册，1.5.4 单独展开中值定理法。表中的"第一反应"是应试归纳的顺序，不是定理。

#### 1.5.1 选法总则：先化简 → 再定型 → 后选工具

**总原则**：<span class="hl-green">先化简 → 再定型 → 后选工具</span>。

1. **无害化简**：有理化、通分、提非零因子、变量代换、取对数——不改变极限本质，但能把式子压成标准未定式，直接缩小选法范围；
2. **定型是选法的前提**：$0/0$、$\infty/\infty$、$0\cdot\infty$、$\infty-\infty$、$1^\infty$、$0^0$、$\infty^0$ 七型的工具池完全不同，<span class="hl-red">不先定型就套洛必达是最高频的错源</span>；
3. **优先级不是绝对的**：等价无穷小最快，但只在**乘除结构**中无条件安全；加减结构要满足"代换后不抵消"，否则改用泰勒；<span class="hl-red">洛必达是备选方案，不是首选方案</span>；
4. **泰勒展开到第几阶由分母决定**：分子分母同阶时，展开到"相减不为 $0$、且能与分母约掉"的最低阶即可。

#### 1.5.2 选法速查

拿到题第一步永远是<span class="hl-green">判断未定式类型</span>，类型决定第一优先方法。九种工具的去向：基本极限、等价无穷小、有理运算、洛必达、泰勒见 §1.5.3；夹逼、单调有界、定积分定义见下表后半；中值定理见 §1.5.4。

| 看到的信号 | 第一反应 | 关键判据 / 陷阱 | 对应 |
|---|---|---|---|
| $0/0$ 型，分子分母都是简单初等函数 | 等价无穷小 → 洛必达 → 泰勒 | <span class="hl-green">等价代换最快</span>；代换后仍是未定式再换工具 | §1.5.3 方法一 |
| $0/0$ 型，分子或分母含 $\sin x-x$、$x-\ln(1+x)$ 等"经典差" | 泰勒公式 | <span class="hl-red">等价代换会把差项消成 $0$</span>，必须展到非零的最低阶（$\sin x-x\sim-\frac{x^3}{6}$） | §1.4、§1.5.3 |
| $\infty/\infty$ 型，$x\to\infty$，分子分母为多项式或幂函数 | 抓大头 / 有理运算法则 | 指数增长 $>$ 幂函数 $>$ 对数；<span class="hl-orange">只有乘除结构可直接抓，加减结构不能直接丢低阶项</span> | §1.5.3 方法二 |
| $\infty-\infty$ 型，分式差 | 通分 | 化为 $0/0$ 或 $\infty/\infty$ 再选工具 | §1.5.3 方法四 |
| $\infty-\infty$ 型，根式差 | 有理化 | $\sqrt A-\sqrt B$ 有理化后，分母常趋于非零常数或无穷 | §1.5.3 方法四 |
| $0\cdot\infty$ 型 | 下放或上提 | 化 $0/0$ 或 $\infty/\infty$ | §1.5.3 方法三 |
| 幂指型 $1^\infty$、$0^0$、$\infty^0$ | 取对数 / 凑重要极限 | $u^v=e^{v\ln u}$；$1^\infty$ 型也可用"三部曲"直接写 | §1.5.3 方法五、六、七 |
| 含变上限积分 $\int_a^x f(t)dt$ | 洛必达法则 | 求导消去积分号；一次求导后仍是未定式可继续求导（<span class="hl-orange">数二了解层级</span>） | §1.5.3 洛必达 |
| 含根式但不是根式差（如 $\frac{\sqrt{1+x}-1}{x}$） | 有理化 或 等价无穷小 | $\sqrt{1+x}-1\sim\frac x2$，优先等价 | §1.4 |
| 非零因子与另一部分相乘 / 相除 | 先求出非零因子的极限 | 极限非零的因子可以先算出来，简化剩余部分 | — |
| 求无穷小的阶数 | 等价无穷小 / 泰勒 | 展开到第一个非零项 | §1.4 |
| 差商型 $\frac{f(A(x))-f(B(x))}{A(x)-B(x)}$，$A,B\to$ 同一点 $a$ | 中值定理（拉格朗日 / 柯西） | $\to f'(a)$；<span class="hl-green">能凑成商时中值定理是主力</span> | §1.5.4 |
| 裸的 $f(A)-f(B)$，$A,B\to a$（不除以 $A-B$） | 和差化积（$\cos$、$\sin$）或泰勒 | <span class="hl-red">中值定理只能定阶，给不出精确系数</span> | §1.5.4 |
| $\frac1x\int_0^x f(t)dt$，或 $\int f\cdot g$ | 积分中值定理 | $f$ 被"提出"积分号，$\to f(0)$ | §3.2、§1.5.4 |

**数列极限**（重点看 $n$ 项和、$n$ 项连乘、递推三种结构）：

| 看到的信号 | 第一反应 | 关键判据 / 陷阱 |
|---|---|---|
| $n$ 项和 $\sum_{i=1}^n a_i$，变化部分相对主体是次量级 | 夹逼准则 | 放缩后左右两端极限必须相等；若两端不等说明"夹不住"，换招 |
| $n$ 项和，变化部分与主体同量级，能提出 $\frac1n$ 并写成 $f\left(\frac in\right)$ | 定积分定义 | 与夹逼的判据就是"同量级还是次量级"；提 $\frac1n$ 后再定被积函数与积分区间 |
| $n$ 项连乘 | 取对数化为 $n$ 项和 | 化完再按上面两条选 |
| 递推关系 $x_{n+1}=f(x_n)$ | 单调有界准则 | 先证单调 + 有界，再令极限为 $A$ 代入递推式求 $A$；证单调三条路见 §1.2 |
| 通项是函数型 $a_n=f(n)$ 且 $f$ 可导 | 转化为函数极限 | <span class="hl-red">大题中不能直接对 $n$ 用洛必达</span>：先把 $n$ 换成 $x$ 求函数极限，再离散化回数列 |
| $\sqrt[n]{a_1^n+\cdots+a_m^n}$ | 基本极限结论 | 直接得 $\max a_i$ |

#### 1.5.3 七种未定式的逐型处理

未定式共七种：$\frac00$、$\frac{\infty}{\infty}$、$0\cdot\infty$、$\infty-\infty$、$1^\infty$、$\infty^0$、$0^0$。

**方法一：$\frac00$ 型**

1. 因式分解、通分、利用已知极限消去"零因子"；
2. 洛必达法则或泰勒展开；
3. 等价无穷小替换；
4. 根式有理化。

**方法二：$\frac{\infty}{\infty}$ 型**

1. 洛必达法则；
2. 同除最大项（抓大头）；
3. 无穷大比较：$x\to+\infty$ 时 $\ln x\ll x^a\ll e^x$（$a>0$）。

$$\lim_{x\to\infty}\frac{a_mx^m+\cdots+a_0}{b_nx^n+\cdots+b_0}=\begin{cases}\infty,&m>n\\[2pt]\dfrac{a_m}{b_n},&m=n\\[4pt]0,&m<n\end{cases}$$

**方法三：$0\cdot\infty$ 型**：取倒数化为 $\frac00$ 或 $\frac{\infty}{\infty}$。

**方法四：$\infty-\infty$ 型**：有分母通分（化 $\frac00$）；有根式有理化（化 $\frac{\infty}{\infty}$）。

**方法五：$1^\infty$ 型**：用公式

<div class="hl-green" markdown="1">

$$\lim f(x)^{g(x)}=e^{\lim [f(x)-1]g(x)}$$

</div>

**方法六、七：$\infty^0$、$0^0$ 型**：幂指函数对数化 $u(x)^{v(x)}=e^{v(x)\ln u(x)}$。

**洛必达法则**：若满足：<span class="hl-red">① $\lim f(x)=\lim F(x)=0$（或 $\infty$）</span>；<span class="hl-red">② 在去心邻域内 $f',F'$ 存在且 $F'\ne0$</span>；<span class="hl-red">③ $\lim\frac{f'}{F'}$ 存在（或为 $\infty$）</span>，则

$$\lim\frac{f(x)}{F(x)}=\lim\frac{f'(x)}{F'(x)}$$

<span class="hl-red">③ 的极限不存在且不为 $\infty$</span> ⇒ 原极限<span class="hl-orange">不适合用洛必达</span>，<span class="hl-red">不代表原极限不存在</span>。

<span class="hl-red">数列极限（离散变量）不能直接用洛必达</span>：洛必达只用于连续型变量。大题中先把 $n$ 换成 $x$ 求函数极限，再离散化回数列（§1.5.2）。

> 注意：含 $\sin\infty$、$\cos\infty$（如 $\lim_{x\to\infty}\frac{x+\sin x}{x}$）不能用洛必达，应直接用极限性质或夹逼。

**数列极限的定积分定义**（夹逼、单调有界见 §1.2，选法见 §1.5.2）：

$$\lim_{n\to\infty}\frac1n\sum_{i=1}^n f\left(\frac{i}{n}\right)=\int_0^1 f(x)\,dx$$

**常用泰勒（麦克劳林）展开（$x\to0$，统一展开到 4 阶及以上）**：

$$e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+o(x^4)$$

$$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5)$$

$$\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+o(x^4)$$

$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+o(x^4)$$

$$(1+x)^a=1+ax+\frac{a(a-1)}{2}x^2+\frac{a(a-1)(a-2)}{6}x^3+\frac{a(a-1)(a-2)(a-3)}{24}x^4+o(x^4)$$

$$\sqrt{1+x^2}=1+\frac{1}{2}x^2-\frac{1}{8}x^4+o(x^4)$$

$$\tan x=x+\frac{x^3}{3}+\frac{2x^5}{15}+o(x^5)$$

$$\arcsin x=x+\frac{x^3}{6}+\frac{3x^5}{40}+o(x^5)$$

$$\arctan x=x-\frac{x^3}{3}+\frac{x^5}{5}+o(x^5)$$

> **【理解】** $e^x$ 的导数等于自身，第 $n$ 项系数须为 $1/n!$，求导后才降为前一项；$\sin$ 只含奇次、$\cos$ 只含偶次、符号交替，由奇偶性决定；<span class="hl-orange">奇函数的 4 阶项恒为 $0$，所以 $\sin x$、$\tan x$、$\arcsin x$、$\arctan x$ 的"4 阶及以上"只能展到 5 阶</span>；<span class="hl-blue">$\sqrt{1+x^2}$ 是偶函数，$x^3$ 项为 $0$，表中只写非零项</span>。

#### 1.5.4 中值定理法求极限（第 9 种方法）

**定位**：中值定理是<span class="hl-green">与前八种并列</span>的第 9 种工具，不是夹逼准则的附属品。它的作用是**结构化简**——把 $f(A)-f(B)$ 型变成导数型、把被积函数提出积分号；夹逼的作用是**估值与界定**。两者常配合（<span class="hl-orange">中值定理先行化简，夹逼准则后续收尾</span>），但目的不同。定理本身见 §2.4（微分）、§3.2（积分）。

**三条核心公式**

<div class="hl-green" markdown="1">

$$f(A)-f(B)=f'(\xi)(A-B),\quad \xi\in(A,B)\quad\text{（拉格朗日）}$$

$$\frac{f(A)-f(B)}{g(A)-g(B)}=\frac{f'(\xi)}{g'(\xi)}\quad\text{（柯西）}$$

$$\int_a^b f(x)g(x)dx=f(\xi)\int_a^b g(x)dx\quad\text{（积分中值定理）}$$

</div>

> <span class="hl-red">前提</span>：本节把差商化归为导数的两条（拉格朗日、柯西）都以 $f$ 在 $a$ 可导（或区间内可导）为前提，属于**计算工具**；积分中值定理的条件是 $f$ 连续。用它们去"由极限式反判可导"会构成循环论证，判定路线见 §2.1.2。

**触发条件（信号 → 结论）**

| 看到的信号 | 用哪条 | 结论 |
|---|---|---|
| $\frac{f(A(x))-f(B(x))}{A(x)-B(x)}$，且 $A,B\to$ 同一点 $a$ | 拉格朗日 / 柯西 | $\to f'(a)$；<span class="hl-green">这是中值定理的主场</span> |
| 裸的 $f(A)-f(B)$，$A,B\to a$（不除以 $A-B$） | 拉格朗日 | $=f'(\xi)(A-B)$，<span class="hl-orange">只能定"是几阶零点"</span>，<span class="hl-red">系数拿不到</span> |
| $\frac1x\int_0^x f(t)dt$，或 $\int f\cdot g$ | 积分中值定理 | $f$ 被提出积分号，$\to f(0)$ |
| 要证 $f$ 在区间上单调（再接单调有界准则） | 拉格朗日 | $f'>0\Rightarrow$ 单调 |
| 要证不等式（如 $\cos x<\frac{\sin x}{x}<1$） | 拉格朗日 | 构造辅助函数取极值 |

**案例：$\cos(\sin x)-\cos x$**

<span class="hl-blue">信号识别</span>：$f(A)-f(B)$ 型，$f=\cos$，$A=\sin x$，$B=x$。注意 $A-B=\sin x-x$ 是<span class="hl-orange">高阶小量</span>，不是一阶。

路线一（中值定理）：只定阶，给不出系数

设 $\xi$ 介于 $\sin x$ 与 $x$ 之间，则

$$\cos(\sin x)-\cos x=-\sin\xi\,(\sin x-x)$$

由 $\lvert\sin\xi\rvert\le\lvert\xi\rvert\le\lvert x\rvert$、$\sin x-x=O(x^3)$，得 $\cos(\sin x)-\cos x=O(x^4)$。

<span class="hl-red">但 $\xi$ 的位置只知道在 $(\sin x,x)$ 内，系数 $\frac16$ 拿不到</span>——中值定理在这里只是"定阶工具"。

路线二（和差化积 + 等价无穷小）：拿精确值

$$\cos(\sin x)-\cos x=-2\sin\frac{\sin x+x}{2}\,\sin\frac{\sin x-x}{2}$$

其中

$$\sin\frac{\sin x+x}{2}\sim\frac{\sin x+x}{2}\sim x,\qquad \sin\frac{\sin x-x}{2}\sim\frac{\sin x-x}{2}\sim-\frac{x^3}{12}$$

故

$$\cos(\sin x)-\cos x\sim-2\cdot x\cdot\left(-\frac{x^3}{12}\right)=\frac{x^4}{6},\qquad \lim_{x\to0}\frac{\cos(\sin x)-\cos x}{x^4}=\frac16$$

路线三（泰勒）：也能拿，但要展两层

$$\sin^2x=x^2-\frac{x^4}{3}+O(x^6),\quad \sin^4x=x^4+O(x^6)$$

$$\cos(\sin x)=1-\frac{\sin^2x}{2!}+\frac{\sin^4x}{4!}+o(x^4)=1-\frac{x^2}{2}+\frac{5x^4}{24}+o(x^4)$$

$$\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+o(x^4)$$

两式相减得 $\frac{x^4}{6}+o(x^4)$，与路线二一致。

**结论**

- <span class="hl-green">$f(A)-f(B)$ 能凑成商 $\frac{f(A)-f(B)}{A-B}$ → 中值定理直接给 $f'(a)$，此时它是主力</span>；
- <span class="hl-red">裸的差 → 中值定理只给阶，精确值交给和差化积 / 泰勒</span>；
- <span class="hl-orange">$\cos A-\cos B$、$\sin A-\sin B$ 是"两函数值之差"的特例：先和差化积再等价无穷小，是这类题的固定套路</span>。

### 1.6 函数的连续性

**定义**：$f(x)$ 在 $x_0$ 连续 $\iff \lim_{x\to x_0}f(x)=f(x_0)\iff \lim_{\Delta x\to0}\Delta y=0$。

**间断点分类**：

| 类型 | 条件 |
|---|---|
| 可去间断点 | 左右极限都存在且相等，但不等于 $f(x_0)$ 或 $f(x_0)$ 无定义 |
| 跳跃间断点 | 左右极限都存在但不相等 |
| 无穷间断点 | 至少一侧极限为 $\infty$ |
| 振荡间断点 | 至少一侧极限振荡不存在（如 $\sin\frac1x$ 在 $x=0$） |

- 第一类间断点：可去、跳跃（左右极限都存在）；
- 第二类间断点：无穷、振荡等。

含 $x^n$ 或 $x^{2n}$ 的分段函数，分段点处优先盯 $x=\pm1$：$x=1$ 分子分母通常均不为零，可直接代入求左右极限；$x=-1$ 分母可能为零，盯奇偶导致的符号变化或无定义；$x<-1$ 提取最高阶项，并看正负号及振荡。

**连续函数运算**：连续函数的和、差、积、商（分母不为零）、复合仍连续；基本初等函数在定义域内连续；初等函数在定义区间内连续。

> **【理解】** 极限、连续、可导在四则运算里用同一套「好 / 坏」口诀（极限：好 = 存在；连续：好 = 连续；可导：好 = 可导）。加法：好 ± 好 = 好；<span class="hl-red">好 ± 坏 = 必坏</span>（反证）；坏 ± 坏 = 不一定（$\frac1x+(-\frac1x)=0$，表 B、表 D）。乘法：好 × 好 = 好；好 × 坏 = 不一定，看「好」的那个在该点是否为零（$x\sin\frac1x$）；坏 × 坏 = 不一定。可导同一套，展开见 §2.1。

**闭区间上连续函数的性质**：

1. 有界性与最大值最小值定理；
2. 零点定理：$f(a)f(b)<0$，则 $\exists\xi\in(a,b)$ 使 $f(\xi)=0$；
3. 介值定理：$f$ 在 $[a,b]$ 连续，$f(a)=A,\ f(b)=B$，则对 $A,B$ 间任一值 $C$，$\exists\xi,\ f(\xi)=C$。

**例题**：求 $\lim_{x\to0}\frac{\tan x-x}{x^2\ln(1+2x)}$。

$$\text{原式}=\lim_{x\to0}\frac{\frac13x^3}{x^2\cdot 2x}=\frac16$$

> **【信号拆解】** 分子分母都趋于 $0$（$0/0$ 型）；但分子 $\tan x-x$ 是"经典差"，<span class="hl-red">直接等价代换会把差项消成 $0$</span>，所以取**高阶等价无穷小** $\tan x-x\sim\frac{x^3}{3}$（等价于泰勒展到 3 阶），分母 $x^2\ln(1+2x)\sim x^2\cdot 2x$。→ 对照 §1.5.2 第 2 行。

### 1.7 选择题：命题否定与反例搜索

> 本节是<span class="hl-green">检索表</span>：给定命题「$A\Rightarrow B$」，要造出 $A$ 成立且 $B$ 失败的 $f$。判定某个给定 $f$ 的四性，仍走 §1.1。每个格子只给函数名，展开见回链。

**下手顺序**（按构造成本从低到高，搜到就停）：

1. <span class="hl-green">初等函数库</span>：$x$、$x^2$、$\sin x$、$\tan x$、$\operatorname{arctan}x$、$e^x$、$\ln x$、$1/x$；
2. <span class="hl-green">章首特殊函数</span>：$\lvert x\rvert$、$\operatorname{sgn}x$、$[x]$、$\{x\}$；
3. <span class="hl-green">振荡型</span>：$\sin\frac1x$、$x\sin\frac1x$、$(-1)^n$；
4. <span class="hl-green">分段函数</span>：左右各写一截，或只改单点函数值；
5. <span class="hl-green">乘积 / 平移破坏</span>：周期 $\times$ 多项式、周期 $+$ 线性（样板：§1.1.3 例 1 的 $x\tan x$）；
6. <span class="hl-green">定义域 / 区间类型</span>：定义域不对称、开区间对闭区间、一点挖洞。

数二极少需要 Dirichlet；有理/无理分段点到为止。

**对着选项的口诀**：

- 推翻周期：乘一个 $x$，或加一个 $x$；
- 推翻单调：让函数过零变号，或分段先升后降；
- 推翻有界：往间断点或无穷远处走一列 $x_k$；
- 推翻极限存在：造两条路径（左右、奇偶项、$\sin\frac1x$ 的峰与谷）；
- 推翻连续：改单点函数值，或左右公式不同；
- 推翻奇偶：先动定义域；定义域对称再分段破坏 $f(-x)$。

**表 A · 四性互推**（$A$ 成立、$B$ 失败）

| 要保留的 $A$ | 要推翻的 $B$ | 母例 |
|---|---|---|
| 有界 | 极限存在 | $\sin x$ |
| 有界 | 单调 | $\sin x$ |
| 有界 | 周期 | $\operatorname{arctan}x$ |
| 单调 | 有界 | $\tan x$ 在 $(-\frac{\pi}{2},\frac{\pi}{2})$，或 $e^x$ |
| 周期 | 有界 | $\tan x$（连续周期才有界，§1.1.3 第 4 条） |
| 周期 | 连续 | $\{x\}$ 或 $\tan x$ |
| 奇 | $f'(0)=0$ | $f(x)=x$（偶且可导则必有 $f'(0)=0$，§1.1.3 第 10 条） |
| 周期外观 | 真周期 | $x\tan x$（周期被 $x$ 乘坏，§1.1.3 例 1） |
| 定义域不对称 | 奇偶 | $\ln x$、$\frac{1}{x-1}$（§1.1.1 Step 0） |

**表 B · 极限代数**

| 命题 | 母例 |
|---|---|
| $f+g$ 极限存在，各自不存在 | $f=\sin\frac1x$、$g=-\sin\frac1x$；或 $(-1)^n$ 与 $-(-1)^n$ |
| $fg$ 极限存在，各自不存在 | $f=(-1)^n$、$g=(-1)^n$ |
| 两条子列极限不同 ⇒ 极限不存在 | $(-1)^n$；Heine：$\sin\frac1x$ 取峰与谷（§1.2、§1.3） |
| 洛必达结论不存在，原极限存在 | $\dfrac{x+\sin x}{x}$（$x\to\infty$，§1.5.3） |
| 有界 $\times$ 无穷小 $=0$ | $\dfrac{\sin x}{x}$（$x\to\infty$），极限是 $0$ 不是 $1$ |
| 有界 ⇏ 收敛 | $(-1)^n$（§1.2、§1.8 第 5 条） |

**表 C · 连续与闭区间性质**（缺一条就垮）

| 缺的条件 | 母例 |
|---|---|
| 连续 ⇏ 可导 | $\lvert x\rvert$ 在 $0$（§2.1） |
| 开区间连续有界，取不到最值 | $x$ 在 $(0,1)$；或 $\operatorname{arctan}x$ 在 $\mathbb{R}$ |
| 有界 ⇏ 有最值 | 同上 |
| 取到中间值 ⇏ 连续 | $\sin\frac1x$（补 $f(0)=0$）：含 $0$ 的区间上能取遍 $[-1,1]$，在 $0$ 不连续 |
| 外连续、内极限不存在，复合仍可能有极限 | $g=\operatorname{sgn}x$（$x\to0$ 极限不存在），$f(u)=u^2$，$f(g(x))=1$（$x\neq0$） |
| 零点定理缺条件 | 缺连续：$\operatorname{sgn}x$ 在 $[-1,1]$，$f(-1)f(1)<0$ 无零点；缺闭区间：$\frac1x$ 在 $(0,1)$ |

**表 D · 和 / 积还带不带原间断点**

选择题常给两个函数各自的间断点，问 $f\pm g$、$fg$ 在这些点还间断不断。先看是<span class="hl-green">同一点</span>还是<span class="hl-orange">两点</span>，再分和、积。

| 情形 | 结论 | 母例 |
|---|---|---|
| 同点：两函数都间断 | 和可以连续 | $\operatorname{sgn}x+(-\operatorname{sgn}x)=0$；$\frac1x+(-\frac1x)=0$ |
| 同点：两函数都间断 | 积可以连续 | 左 $1$ 右 $0$ 的阶跃 $\times$ 左 $0$ 右 $1$ 的阶跃，积恒 $0$ |
| 异点：只 $f$ 在 $a$ 间断，$g$ 在 $a$ 连续 | 和在 $a$ 仍间断 | 连续项消不掉 $f$ 的间断 |
| 异点：只 $f$ 在 $a$ 间断，$g$ 连续且 $g(a)=0$ | 积可以在 $a$ 连续 | $\operatorname{sgn}x\cdot x=\lvert x\rvert$ |
| 异点：只 $f$ 在 $a$ 间断，$g$ 连续且 $g(a)\ne0$ | 积在 $a$ 仍间断 | 非零连续因子把 $f$ 的间断原样留下 |

**表 E · 导数概念反例**（差商极限存在，仍推不出可导；细节与题面结构见 §2.1.2）

| 命题 | 母例 |
|---|---|
| 差商极限存在 ⇏ 可导 | $\lvert x\rvert$ 配 $f(h^2)-f(0)$ 型单侧增量 |
| 缺基准点的极限存在 ⇏ 可导 | $\lvert x\rvert$ 在 $0$，$\frac{f(h)-f(-h)}{2h}\to0$ |
| $\frac{f(x)}{g(x)}\to0$、$g$ 低阶 ⇏ 可导 | $\lvert x\rvert^{2/3}$ 配 $g=x^{1/3}$（同一条件下 $\lvert x\rvert^{4/3}$ 却可导） |
| 单侧导数存在 ⇏ 可导 | $\lvert x\rvert$ 在 $0$，右导数为 $1$、左导数为 $-1$ |

### 1.8 本章易错点

1. $\lim_{x\to\infty}\frac{\sin x}{x}=0$（不是 $1$，用有界乘无穷小）；
2. 等价无穷小只在乘除替换，加减中误用是最高频错误；
3. 极限 $\lim_{x\to\infty}(1+\frac1x)^x=e$ 与 $\lim_{x\to0}(1+x)^{1/x}=e$ 别混淆；
4. 判断间断点要先看左右极限是否都存在，再分类；
5. 数列 $\{x_n\}$ 有界不一定收敛，但收敛一定有界；
6. 洛必达先验三个条件，结果不存在不代表原极限不存在；<span class="hl-red">它是备选不是首选</span>，$0/0$ 型先试等价无穷小，含"经典差"才上泰勒（§1.5.1）；
7. 抓大头只能在乘除结构用，<span class="hl-red">加减结构不能直接丢低阶项</span>；
8. $n$ 项和到底用夹逼还是定积分定义，判据是"变化部分与主体同量级还是次量级"（见 §1.5.2）。
9. <span class="hl-red">中值定理给的是"阶"不是"系数"</span>：差商型 $\frac{f(A)-f(B)}{A-B}$ 可直接用中值定理得 $f'(a)$，但裸的 $f(A)-f(B)$ 只能定阶，精确值要靠和差化积 / 泰勒（见 §1.5.4）。
10. 选择题不会下手造反例 → 见 §1.7 搜索顺序与表 A–D。

---

## 第二章 一元函数微分学

### 2.1 导数概念

**定义**：函数 $f(x)$ 在 $x_0$ 处的导数

$$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$

> <span class="hl-orange">这个定义有两个使用方向</span>：正向是已知可导、求导数（§2.1.4）；逆向是从给定的极限结构反判是否可导（§2.1.1–§2.1.3）。数二选择题多数考逆向。

**左右导数**：

$$f'_-(x_0)=\lim_{h\to0^-}\frac{f(x_0+h)-f(x_0)}h,\quad f'_+(x_0)=\lim_{h\to0^+}\frac{f(x_0+h)-f(x_0)}h$$

$$f'(x_0)\text{ 存在}\iff f'_-(x_0)=f'_+(x_0)$$

**可导与连续的关系**：<span class="hl-green">可导 ⇒ 连续 ⇒ 极限存在</span>（连续见 §1.6）；反之均不成立。连续 ⇏ 可导的母例：$\lvert x\rvert$（尖点）、$\sqrt[3]{x}$（切线垂直）、$x\sin\frac1x$（导数振荡，可导性需单独分析）。

**导数的几何意义**：$f'(x_0)$ 是曲线 $y=f(x)$ 在 $(x_0,f(x_0))$ 处切线斜率。

- 切线：$y-y_0=f'(x_0)(x-x_0)$；
- 法线：$y-y_0=-\frac{1}{f'(x_0)}(x-x_0)$。

**物理意义**：瞬时速度 $v=s'(t)$，加速度 $a=v'(t)=s''(t)$。

#### 2.1.1 三要素与像集覆盖

> 定位：本节回答"为什么一个极限存在，能或不能说明 $f$ 在 $x_0$ 可导"。这是定义的逆向使用，也是数二选择题的高频考法。

标准差商 $\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ 由三件事共同确定，任何一件被换掉，"极限存在"就不再等价于"可导"：

| 要素 | 在定义里的作用 | 被破坏后 |
|---|---|---|
| 基准点 $f(x_0)$ | 提供纵向参照，固定从哪个高度起算 | 极限只约束两点之差，$f(x_0)$ 可随意改动 |
| 增量 $\Delta x$ 双向趋于 $0$ | 让差商同时采样左右两侧 | 只能得到单侧导数 |
| 分母 $=\Delta x$ | 分母是同一个横向增量，比值才是割线斜率 | 比值不再是割线斜率，须做阶数换算（§2.1.3） |

统一原理：<span class="hl-green">极限只是沿增量 $\alpha$ 采样</span>。式子 $\dfrac{f(x_0+\alpha)-f(x_0)}{\alpha}$ 只用到 $f$ 在 $\alpha$ 的像集上的值；像集没覆盖到的地方，$f$ 怎么变都不影响这个极限。

由此得到两层：

- <span class="hl-green">充分条件（考试够用）</span>：$h\to0$ 时 $\alpha\to0$，且 $\alpha$ 在 $0$ 的两侧各自连续严格单调、分母就是 $\alpha$（如 $\alpha=h,\ \sin h,\ e^h-1$）。这时 $\alpha$ 是去心邻域之间的连续一一换元，$h\to0\iff\alpha\to0$，差商只是重编号，<span class="hl-green">"极限存在 ⇔ 可导"</span>。
- <span class="hl-orange">必要条件</span>：$\alpha$ 的像集要覆盖 $0$ 的一个去心邻域，只取单侧（$x^2$、$1-\cos h$）一定不满足。注意"两侧都有"只是这条判据的一半：$\alpha$ 只取 $\pm\frac1n$ 时两侧都有、像集却漏掉无穷多点，此时把 $f$ 造得在这些点取 $0$、其余取 $2y$，沿 $\alpha$ 的差商恒为 $0$，而漏掉点处差商为 $2$，<span class="hl-red">极限存在却不可导</span>。

一句话：<span class="hl-green">单调换元保等价，单侧增量只给单侧导数</span>。双侧离散采样这一层超出数二主流，知道"双侧趋近"不是充分判据即可。

#### 2.1.2 反判四问与反例库

判定题（"下列条件能否推出 $f$ 在 $x_0$ 可导"）按序过四问，<span class="hl-red">任一问不过就停</span>：

1. **基准点在场吗？** 式中有没有 $f(x_0)$？没有（如 $f(x_0+h)-f(x_0-h)$）就不能直接判可导。
2. **增量的像集覆盖双侧吗？** 看 $\alpha$ 的取值是否包含 $0$ 的一个去心邻域：双向趋于 $0$ 才算；恒非负（$x^2$、$1-\cos h$）或恒非正都只给单侧。
3. **分母与增量一致吗？** 不一致就做恒等变形，把分母凑成真实增量，再看多出的因子趋于 $0$、有限数还是 $\infty$（§2.1.3）。
4. **还原成标准差商后极限是有限数吗？** 存在且有限（含 $0$）才可导；出现 $0\cdot\infty$、$\infty$、振荡，都不能判。

**导数概念反例库**（每条都满足左边题面的极限，却在 $x_0=0$ 不可导）

| 题面结构 | 破坏的要素 | 反例（$x_0=0$） | 题面极限 | 实际 |
|---|---|---|---|---|
| $\dfrac{f(h^2)-f(0)}{h}$ | 增量单侧 + 分母不一致 | $f(x)=\lvert x\rvert$ | $0$ | 不可导 |
| $\dfrac{f(1-\cos h)}{h^2}$ | 增量单侧 | $f(x)=\lvert x\rvert$ | $\frac12$ | 不可导 |
| $\dfrac{f(h)-f(-h)}{2h}$ | 缺基准点 | $f(x)=\lvert x\rvert$ | $0$ | 不可导 |
| $\dfrac{f(2h)-f(h)}{h}$ | 缺基准点 | $f(0)=1,\ f(x)=x\ (x\ne0)$ | $1$ | 不可导（在 $0$ 间断） |
| $\lim_{x\to0}\dfrac{f(x)}{x^{1/3}}=0$ | 分母低阶 | $f(x)=\lvert x\rvert^{2/3}$ | $0$ | 不可导 |

> <span class="hl-orange">缺基准点的两行要分开看</span>：第 4 行 $\frac{f(2h)-f(h)}{h}$ 的反例依赖 $f$ 在 $x_0$ 不连续，补上"$f$ 在 $x_0$ 连续"后，这个条件确实能推出可导（教材固定题型，沿 $h\to h/2$ 迭代即可）。第 3 行对称差商则不同，$\lvert x\rvert$ 在 $0$ 连续、该比值恒为 $0$，加了连续性依旧不可导。<span class="hl-red">结论按结构逐题判，不能套模板</span>。

**绝对值型真题**：2018 数二第 2 题直接问"下列函数在 $x=0$ 处不可导的是"，四个选项为 $\lvert x\rvert\sin\lvert x\rvert$、$\lvert x\rvert\sin\sqrt{\lvert x\rvert}$、$\cos\lvert x\rvert$、$\cos\sqrt{\lvert x\rvert}$，答案为 $\cos\sqrt{\lvert x\rvert}$。统一做法是回到定义算 $\lim_{x\to0}\frac{f(x)-f(0)}{x}$：前三个的差商都趋于 $0$，可导；$\cos\sqrt{\lvert x\rvert}\approx1-\frac{\lvert x\rvert}{2}$，差商在 $x\to0^+$ 时趋于 $-\frac12$、在 $x\to0^-$ 时趋于 $+\frac12$，左右不等，故不可导。

**判定型与计算型分流**（<span class="hl-red">这是最容易被混用的一步</span>）

| 类型 | 已知 | 可用工具 | 禁用 |
|---|---|---|---|
| 判定型（能否推可导） | 只有极限式 | 定义、左右导数、反例 | 中值定理、等价替换（以可导为前提，会循环论证） |
| 计算型（求 $f'(x_0)$） | 已知 $f$ 在 $x_0$ 可导 | 定义、中值定理、泰勒、等价替换、拆项 | 拆项前未验证各部分极限存在 |

> <span class="hl-red">复合增量替换同理</span>：$f(x_0+\alpha)-f(x_0)\sim f'(x_0)\alpha$ 只有在 $f'(x_0)$ 已知时才是化简工具，不能反过来当作可导的判据。

#### 2.1.3 阶数换算：比值趋于零时能否可导

**主判据：看 $f$ 相对增量 $\alpha=x-x_0$ 的阶。** 设 $f$ 在 $x_0$ 连续、$f(x_0)=0$，要判的就是 $\dfrac{f(x)}{\alpha}$，阶数直接决定结局：

| $f$ 相对 $\alpha$ 的阶 | 写法 | $\dfrac{f(x)}{\alpha}$ | 结论 |
|---|---|---|---|
| 高阶（比 $\alpha$ 更快趋于 $0$） | $f=o(\alpha)$，如 $x^2$、$\lvert x\rvert^{3/2}$ | $\to0$ | 可导，$f'(x_0)=0$ |
| 同阶 / 等价 | $f\sim A\alpha\ (A\ne0)$，如 $3x$、$\sin x$ | $\to A$ | 可导，$f'(x_0)=A\ne0$ |
| 低阶（比 $\alpha$ 慢） | $\dfrac{f}{\alpha}\to\infty$，如 $\lvert x\rvert^{1/2}$ | 无穷 | 不可导 |
| 差商振荡、无极限 | 如 $f=x\sin\frac1x$ | 不存在 | 不可导 |

> <span class="hl-green">这条主判据一句话说清</span>：$f$ 与 $\alpha$ 同阶或等价 ⇒ 导数有限非零，$f$ 比 $\alpha$ 高阶 ⇒ 导数为 $0$，$f$ 低阶或差商振荡 ⇒ 不可导。导数的值就是 $\alpha$ 的系数。

<span class="hl-orange">"无法判定"只出现在信息不足时</span>：只要 $f$ 相对 $\alpha$ 的阶被确定，结论就唯一。真正判不出来的是下面这种——题目只约束了辅助函数 $g$ 的阶，没约束 $f$ 自己的阶，此时差商落成 $0\cdot\infty$。

**题型常给辅助比值 $\dfrac{f(x)}{g(x)}\to0$，要换算过去。** 做一步恒等变形：

$$\frac{f(x)}{\alpha}=\underbrace{\frac{f(x)}{g(x)}}_{\to0}\cdot\underbrace{\frac{g(x)}{\alpha}}_{\text{由 }g\text{ 的阶决定}}$$

第一个因子已经趋于 $0$，结局由第二个因子决定：

| $g$ 相对 $\alpha$ 的阶 | $\dfrac{g(x)}{\alpha}$ | 乘积 | 结论 |
|---|---|---|---|
| 高阶（如 $x^2$） | $\to0$ | $\to0$ | 可导，$f'(x_0)=0$ |
| 同阶（如 $\sin x$、$\ln(1+x)$） | 有限非零 | $\to0$ | 可导，$f'(x_0)=0$ |
| 低阶（如 $x^{1/3}$、$x^{2/3}$） | $\to\infty$ | $0\cdot\infty$ | <span class="hl-red">无法判定</span> |

> <span class="hl-red">关键：$0\cdot\infty$ 是未定式，照样判不出可导性</span>。只凭 $\frac{f}{g}\to0$ 加上"$g$ 低阶"这两个条件，可导与不可导两种结局都能造出来，必须回到主判据看 $f$ 自己的阶。

**例**：$\lim_{x\to0}\dfrac{f(x)}{x^{1/3}}=0$（$g=x^{1/3}$ 是低阶，正落在 $0\cdot\infty$）。取 $f(x)=\lvert x\rvert^{2/3}$，则 $\frac{f}{g}=\lvert x\rvert^{1/3}\to0$，但 $\frac{f}{\alpha}=\dfrac{\lvert x\rvert^{2/3}}{x}$ 两侧分别趋于 $\pm\infty$，不可导；取 $f(x)=\lvert x\rvert^{4/3}$，同一极限仍为 $0$，而 $\frac{f}{\alpha}\to0$，$f'(0)=0$。同一条件下两种结局都有，可见 $0\cdot\infty$ 时条件不足。

> <span class="hl-red">易错</span>：当 $g$ 与 $\alpha$ 同阶时，给的 $\frac{f}{g}\to0$ 说明 $f$ 比 $g$ 高阶，导出的是 $f'(x_0)=0$，<span class="hl-orange">并非非零导数</span>。"$f/g\to0$ ⇒ 有限非零导数"是错误表述；想要非零导数，得 $f$ 本身与 $\alpha$ 同阶，即 $\frac{f}{g}\to A\ne0$ 且 $g\sim c\alpha$，此时 $f'(x_0)=A\cdot c$。

#### 2.1.4 计算型两步：先定函数值，再凑定义

已知可导性、要求 $f'(x_0)$ 的题（解答题最常见）走两步：

1. <span class="hl-green">先定函数值</span>：分母趋于 $0$ 且极限存在 ⇒ 分子趋于 $0$；配合连续性得到 $f(x_0)$ 的确定值。
2. <span class="hl-green">拆项凑定义</span>：把目标式写成若干个 $\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ 的线性组合，套用已知的 $f'(x_0)$。<span class="hl-red">拆项前逐项确认极限存在</span>，否则拆分不合法。

**例 1（先定值，再换分母）**：设 $f$ 在 $x=0$ 连续，且 $\lim_{x\to0}\dfrac{f(x)}{\sin x}=3$，求 $f(0)$ 与 $f'(0)$。

$\sin x\to0$ 且比值有极限 ⇒ $f(x)\to0$；连续 ⇒ $f(0)=0$。换分母凑定义：

$$\frac{f(x)}{x}=\frac{f(x)}{\sin x}\cdot\frac{\sin x}{x}\to3\cdot1=3$$

故 $f'(0)=3$。<span class="hl-orange">这里的 $\dfrac{\sin x}{x}\to1$ 是关键换算因子</span>；若题面改成 $\lim\dfrac{f(x)}{1-\cos x}=2$，则 $\dfrac{1-\cos x}{x}\to0$，得到 $f'(0)=0$。

**例 2（拆项）**：设 $f$ 在 $x=0$ 可导，求 $\lim_{x\to0}\dfrac{f(x)-f(2x)}{x}$。

拆成两个差商：

$$\frac{f(x)-f(2x)}{x}=\frac{f(x)-f(0)}{x}-2\cdot\frac{f(2x)-f(0)}{2x}\to f'(0)-2f'(0)=-f'(0)$$

两项分别存在，拆分合法。<span class="hl-orange">不要用"$\frac{f(x)-f(2x)}{x-2x}=f'(\xi)\to f'(0)$"来收尾</span>：这条链要求 $f'$ 在 $0$ 连续，而题面只给了 $f$ 在 $0$ 可导。直接拆项不依赖这个假设。

### 2.2 求导法则

**基本初等函数导数公式**：

$$(C)'=0,\quad (x^\mu)'=\mu x^{\mu-1},\quad (a^x)'=a^x\ln a,\quad (e^x)'=e^x$$

$$(\log_a x)'=\frac1{x\ln a},\quad (\ln x)'=\frac1x$$

$$(\sin x)'=\cos x,\quad (\cos x)'=-\sin x,\quad (\tan x)'=\sec^2x,\quad (\cot x)'=-\csc^2x$$

$$(\sec x)'=\sec x\tan x,\quad (\csc x)'=-\csc x\cot x$$

$$(\arcsin x)'=\frac1{\sqrt{1-x^2}},\quad (\arccos x)'=-\frac1{\sqrt{1-x^2}}$$

$$(\arctan x)'=\frac1{1+x^2},\quad (\operatorname{arccot}x)'=-\frac1{1+x^2}$$

**四则运算**：

$$(u\pm v)'=u'\pm v',\quad (uv)'=u'v+uv',\quad \left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$$

**反函数求导**：$\frac{dy}{dx}=\frac{1}{\frac{dx}{dy}}$。

**复合函数求导（链式法则）**：$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$。

### 2.3 高阶导数与微分

**高阶导数**：$f''(x)=\lim_{\Delta x\to0}\frac{f'(x+\Delta x)-f'(x)}{\Delta x}$。

**常用高阶导数**：

$$(e^x)^{(n)}=e^x,\quad (a^x)^{(n)}=a^x(\ln a)^n$$

$$(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}{2}\right),\quad (\cos x)^{(n)}=\cos\left(x+\frac{n\pi}{2}\right)$$

$$[\ln(1+x)]^{(n)}=(-1)^{n-1}\frac{(n-1)!}{(1+x)^n},\quad (x^\mu)^{(n)}=\mu(\mu-1)\cdots(\mu-n+1)x^{\mu-n}$$

**莱布尼茨公式**：

$$(uv)^{(n)}=\sum_{k=0}^n C_n^k u^{(k)}v^{(n-k)}$$

**微分**：$\Delta y=A\Delta x+o(\Delta x)$，则 $dy=f'(x)\Delta x=f'(x)dx$。

**微分形式不变性**：$y=f(u)$，无论 $u$ 是自变量还是中间变量，都有 $dy=f'(u)du$。

### 2.4 微分中值定理

**费马引理**：若 $f(x)$ 在 $x_0$ 可导且取得极值，则 $f'(x_0)=0$。

**罗尔定理**：$f$ 在 $[a,b]$ 连续、$(a,b)$ 可导、$f(a)=f(b)$，则 $\exists\xi\in(a,b)$，$f'(\xi)=0$。

**拉格朗日中值定理**：$f$ 在 $[a,b]$ 连续、$(a,b)$ 可导，则 $\exists\xi\in(a,b)$：

<div class="hl-green" markdown="1">

$$f(b)-f(a)=f'(\xi)(b-a)$$

</div>

有限增量形式：$f(x+\Delta x)-f(x)=f'(x+\theta\Delta x)\Delta x$。

> **【用途】** 中值定理求极限（求极限的第 9 种方法）见 §1.5.4。

**柯西中值定理**：$f,F$ 在 $[a,b]$ 连续、$(a,b)$ 可导且 $F'(x)\ne0$，则 $\exists\xi$：

$$\frac{f(b)-f(a)}{F(b)-F(a)}=\frac{f'(\xi)}{F'(\xi)}$$

> **【理解】** 证明 $f'(\xi)+P(\xi)f(\xi)=0$ 时，构造辅助函数 $F=e^{\int P\,dx}f$，因 $F'=e^{\int P\,dx}(f'+Pf)$，对 $F$ 用罗尔定理即可。

**泰勒公式**：

$$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+R_n(x)$$

- 拉格朗日余项：$R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$；
- 佩亚诺余项：$R_n(x)=o((x-x_0)^n)$。

### 2.5 导数应用

**单调性**：$f'(x)>0$（$<0$）则 $f$ 单调增加（减少）。

**极值判别（"1+3"）**：

- 必要条件：$f$ 在 $x_0$ 可导且为极值点 $\Rightarrow f'(x_0)=0$；
- 第一充分条件：$f'(x_0)=0$（或 $f$ 在 $x_0$ 连续），看左右邻域导数符号：
  - 左负右正 → 极小值；左正右负 → 极大值；
- 第二充分条件：$f'(x_0)=0,\ f''(x_0)\ne0$：
  - $f''(x_0)<0$ 取极大值；$f''(x_0)>0$ 取极小值；
- 第三充分条件：$f'(x_0)=\cdots=f^{(n)}(x_0)=0,\ f^{(n+1)}(x_0)\ne0$，$n$ 为奇数时，$f^{(n+1)}<0$ 取极大、$>0$ 取极小。

**最值**：① 确定区间、算端点值；② 求所有驻点和不可导点函数值；③ 比较得最值。

**曲线凹凸性**：$f''(x)>0$ 凹（凹向上）；$f''(x)<0$ 凸。

**拐点**：凹凸性改变的点（必要条件 $f''(x_0)=0$ 或不存在，再看两侧 $f''$ 变号）。

**渐近线**：

- 水平：$\lim_{x\to\infty}f(x)=A$，$y=A$；
- 垂直：$\lim_{x\to x_0}f(x)=\infty$，$x=x_0$；
- 斜：$a=\lim_{x\to\infty}\frac{f(x)}x,\ b=\lim_{x\to\infty}[f(x)-ax]$，$y=ax+b$。

**曲率**（数二要求）：

$$K=\frac{|y''|}{(1+y'^2)^{3/2}},\quad \text{曲率半径}\ \rho=\frac1K$$

**例题**：设 $f(x)$ 二阶可导，满足 $f'(x)+x^2f(x)=xe^x$，且 $x=0$ 为极值点，判断极大/极小。

解：$f'(0)=0$；两边求导 $f''(x)+2xf(x)+x^2f'(x)=(x+1)e^x$，代入 $x=0$ 得 $f''(0)=1>0$，故 $x=0$ 为极小值点。

### 2.6 相关变化率

> **【定位】** 已知某个量对时间的变化率，求另一个量的变化率。核心不是积分，而是<span class="hl-green">关系式两边对 $t$ 求导</span>。2010、2016、2018、2021 都考过。

**三步流程**：

1. **写关系式**：用勾股、相似、面积、体积公式把待求量与已知量连起来；
2. **对 $t$ 求导**：所有变量都是 $t$ 的函数，用链式法则；<span class="hl-red">先代数值再求导是高频错误</span>；
3. **代瞬时值**：把该时刻的数值代入，解出待求变化率。

**常见关系式**：

| 题面信号 | 关系式 | 求导后 |
|---|---|---|
| 长方形边长变化，问对角线 | $l^2=a^2+b^2$ | $l\,l'=a\,a'+b\,b'$ |
| 圆柱半径、高同时变 | $V=\pi r^2h$ | $V'=\pi(2rh\,r'+r^2h')$ |
| 圆柱表面积 | $S=2\pi r^2+2\pi rh$ | $S'=2\pi(2r\,r'+r'h+rh')$ |
| 曲线上动点到原点距离 | $d^2=x^2+y^2,\ y=f(x)$ | $d\,d'=x+y\,y'$ |
| 区域面积随上限变 | $S(t)=\int_{a(t)}^{b(t)}f(x)dx$ | 变限积分求导（§3.2） |
| 旋转体体积随参数变 | $V(t)=\pi\int_a^{b(t)}f^2dx$ | $V'=\pi f^2[b(t)]b'(t)$ |

**例 1（圆柱）**：圆柱半径 $r=2$、高 $h=5$，$r$ 以 $1/\text{s}$ 增大、$h$ 以 $2/\text{s}$ 减小，求体积与表面积的变化率。

$$V'=\pi(2rh\,r'+r^2h')=\pi(2\cdot2\cdot5\cdot1+4\cdot(-2))=12\pi$$

$$S'=2\pi(2r\,r'+r'h+rh')=2\pi(4+5-4)=10\pi$$

**例 2（面积随上限变）**：曲线 $y=x^2$、$x$ 轴与直线 $x=t$ 围成面积 $S(t)$，若 $t$ 以 $2\,\text{cm/s}$ 增长，求 $t=1$ 时 $S$ 的变化率。

$$S(t)=\int_0^t x^2dx=\frac{t^3}{3},\qquad \frac{dS}{dt}=S'(t)\cdot t'=t^2\cdot2$$

$t=1$ 时 $\dfrac{dS}{dt}=2\,\text{cm}^2/\text{s}$。

> **【易错】** 关系式里有多个变量时，<span class="hl-red">不能把"瞬时值"先代进去再求导</span>；必须先对 $t$ 求导，再代瞬时值。否则所有变化率都会变成 $0$。

### 2.7 本章易错点

1. 分段函数在分段点处必须用左右导数定义求，不能直接求导后代入；
2. 可导必连续，但连续不一定可导；
3. $f'(x_0)=0$ 不一定是极值点（如 $x^3$ 在 $0$ 处）；
4. 拐点是曲线上的点，要写坐标 $(x_0,f(x_0))$，不是只写 $x_0$；
5. 中值定理条件（连续、可导）缺一不可；
6. 极值点可以是不可导点（如 $\lvert x\rvert $ 在 $0$），第一充分条件可判导数不存在的情形；
7. <span class="hl-red">判定题不能借用中值定理、等价替换</span>：它们以可导为前提，用来"证明"可导就是循环论证（§2.1.2 分流表）；
8. <span class="hl-red">增量是 $x^2$、$1-\cos h$ 这类非负结构时只能得单侧导数</span>，即使极限存在也不能判可导；
9. <span class="hl-red">$f(x_0+h)-f(x_0-h)$ 型缺基准点</span>：已知可导时它等于 $f'(x_0)$，反过来推不出可导（$\lvert x\rvert$ 在 $0$）；
10. 拆项凑导数前先验证每一部分极限存在，否则拆分本身不合法（§2.1.2）；
11. 阶数判可导看两件事：$f$ 与 $\alpha$ 同阶/等价 ⇒ 导数有限非零，$f$ 高阶 ⇒ 导数为 $0$，$f$ 低阶 ⇒ 不可导；只给 $\frac{f(x)}{g(x)}\to0$ 且 $g$ 低阶时是 $0\cdot\infty$，条件不足（§2.1.3）。

---

## 第三章 一元函数积分学

### 3.1 不定积分

**原函数**：若 $F'(x)=f(x)$，则 $F(x)$ 是 $f(x)$ 的一个原函数。

**不定积分**：$\int f(x)dx=F(x)+C$。

**性质**：$\int[f(x)\pm g(x)]dx=\int f\,dx\pm\int g\,dx$；$\int kf(x)dx=k\int f\,dx$。拆成两项时，原积分前的常系数乘进拆开后的每一项（定积分、二重积分同此）。

**基本积分公式**：

$$\int x^\mu dx=\frac{x^{\mu+1}}{\mu+1}+C\ (\mu\ne-1),\quad \int\frac1x dx=\ln|x|+C$$

$$\int a^x dx=\frac{a^x}{\ln a}+C,\quad \int e^x dx=e^x+C$$

$$\int\sin x\,dx=-\cos x+C,\quad \int\cos x\,dx=\sin x+C$$

$$\int\sec^2x\,dx=\tan x+C,\quad \int\csc^2x\,dx=-\cot x+C$$

$$\int\sec x\tan x\,dx=\sec x+C,\quad \int\csc x\cot x\,dx=-\csc x+C$$

$$\int\sec x\,dx=\ln\lvert\sec x+\tan x\rvert+C,\quad \int\csc x\,dx=\ln\lvert\csc x-\cot x\rvert+C$$

> **【理解】** $\sec$ 常与 $\tan$ 成对、$\csc$ 常与 $-\cot$ 成对：导数里 $(\sec x)'=\sec x\tan x$、$(\csc x)'=-\csc x\cot x$；积分里也按这对来记。这两个不好推，直接背。

$$\int\frac{dx}{1+x^2}=\arctan x+C,\quad \int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C$$

$$\int\frac{dx}{a^2+x^2}=\frac1a\arctan\frac xa+C,\quad \int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac xa+C$$

$$\int\frac{dx}{a^2-x^2}=\frac1{2a}\ln\left|\frac{a+x}{a-x}\right|+C,\quad \int\frac{dx}{\sqrt{x^2\pm a^2}}=\ln\left|x+\sqrt{x^2\pm a^2}\right|+C$$

**积分方法**：

1. **第一类换元法（凑微分）**：$\int f[\varphi(x)]\varphi'(x)dx=\int f(u)du$。
2. **第二类换元法**：令 $x=\varphi(t)$。
   - 三角代换：$\sqrt{a^2-x^2}$ 令 $x=a\sin t$；$\sqrt{a^2+x^2}$ 令 $x=a\tan t$；$\sqrt{x^2-a^2}$ 令 $x=a\sec t$；
   - 倒代换：$x=\frac1t$（处理分母次数高的情形）；
   - 根式代换：$t=\sqrt[n]{ax+b}$。
3. **分部积分法**：

$$\int u\,dv=uv-\int v\,du$$

**分部积分表格法**：对需多次分部的积分，一列反复求导（$u$ 及其导数），一列反复积分（$dv$ 及其积分），按"正、负、正、负"交替相乘相加，直到导数列为 $0$。

**万能代换**：$t=\tan\frac x2$，则 $\sin x=\frac{2t}{1+t^2},\ \cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2}{1+t^2}dt$。

**常用凑微分**：

$$\frac1{\sqrt x}dx=2\,d\sqrt x,\quad x\,dx=\frac12 d(x^2),\quad \frac1x dx=d\ln x,\quad e^x dx=d(e^x)$$

### 3.2 定积分

**定义**：

$$\int_a^b f(x)dx=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$$

**规定**：$\int_a^b f\,dx=-\int_b^a f\,dx$；$\int_a^a f\,dx=0$。

**可积条件**：

- 必要条件：$f$ 在 $[a,b]$ 上有界；
- 充分条件（任一）：$f$ 连续；或有界且只有有限个间断点；或单调。

> **【理解】** 可积（定积分存在）与有原函数是两个概念。$f$ 连续时两者都成立，变上限积分 $\Phi(x)=\int_a^x f(t)dt$ 就是原函数。若 $f$ 有第一类间断点，则仍可积（如 $\operatorname{sgn}x$ 在 $[-1,1]$ 可积），但没有原函数，因为导函数不能有第一类间断点；此时 $\Phi(x)$ 存在且连续，但在间断点处 $\Phi'(x)\ne f(x)$，故 $\Phi$ 是积分、不是原函数。

**性质**：

$$\int_a^b f\,dx=\int_a^c f\,dx+\int_c^b f\,dx$$

$$\int_a^b[f\pm g]dx=\int_a^b f\,dx\pm\int_a^b g\,dx,\quad \int_a^b kf\,dx=k\int_a^b f\,dx$$

**积分中值定理**：$f$ 在 $[a,b]$ 连续，则 $\exists\xi\in[a,b]$：

$$\int_a^b f(x)dx=f(\xi)(b-a)$$

> **【用途】** 把被积函数提出积分号求极限，见 §1.5.4。

**变限积分求导**：

$$\Phi(x)=\int_a^x f(t)dt\ (f\text{ 连续})\Rightarrow \Phi'(x)=f(x)$$

$$\frac{d}{dx}\int_{\psi(x)}^{\varphi(x)}f(t)dt=f[\varphi(x)]\varphi'(x)-f[\psi(x)]\psi'(x)$$

> **【理解】** 变上限积分在下限处为 $0$：$\Phi(a)=\int_a^a f=0$。求导丢掉积分常数，把下限代回**求导前的原式**就能读出初值。典型动作：原式含 $\int_0^x$，两边令 $x=0$，积分消失，直接得到 $f(0)$（或 $y(0)$）。下限本身就是约束，这就是隐初值。

**牛顿-莱布尼茨公式**：$F'(x)=f(x)$，则

<div class="hl-green" markdown="1">

$$\int_a^b f(x)dx=F(b)-F(a)$$

</div>

**定积分换元法**：换元必换限，$\int_a^b f(x)dx=\int_\alpha^\beta f[\varphi(t)]\varphi'(t)dt$。

**定积分分部积分**：$\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du$。

**常用结论（对称区间、华里士公式）**：

<div class="hl-orange" markdown="1">

$$\int_{-a}^a f(x)dx=\begin{cases}2\int_0^a f\,dx,&f\text{ 为偶}\\0,&f\text{ 为奇}\end{cases}$$

</div>

<div class="hl-green" markdown="1">

$$\int_0^\pi xf(\sin x)dx=\frac{\pi}{2}\int_0^\pi f(\sin x)dx$$

</div>

<div class="hl-green" markdown="1">

$$\int_0^{\pi/2}\sin^n x\,dx=\int_0^{\pi/2}\cos^n x\,dx=\begin{cases}\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdots\dfrac12\cdot\dfrac{\pi}{2},&n\text{ 为偶}\\[4pt]\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdots\dfrac23\cdot1,&n\text{ 为奇}\end{cases}$$

</div>

### 3.3 反常积分

**无穷限反常积分**：

$$\int_a^{+\infty}f(x)dx=\lim_{b\to+\infty}\int_a^b f\,dx,\quad \int_{-\infty}^b f\,dx=\lim_{a\to-\infty}\int_a^b f\,dx$$

**无界函数（瑕积分）**：$a$ 为瑕点时 $\int_a^b f\,dx=\lim_{\varepsilon\to0^+}\int_{a+\varepsilon}^b f\,dx$。

**常见敛散性结论**：

$$\int_1^{+\infty}\frac{dx}{x^p}\begin{cases}p>1&\text{收敛}\\p\le1&\text{发散}\end{cases},\qquad \int_0^1\frac{dx}{x^p}\begin{cases}p<1&\text{收敛}\\p\ge1&\text{发散}\end{cases}$$

$$\int_2^{+\infty}\frac{dx}{x(\ln x)^p}\begin{cases}p>1&\text{收敛}\\p\le1&\text{发散}\end{cases}$$

> **【理解】** 由 $\int x^{-p}dx=\frac{x^{1-p}}{1-p}$：无穷远处需 $1-p<0$（$p>1$）；$0$ 点处需 $1-p>0$（$p<1$）。

### 3.4 定积分应用

> **【定位】** 所有模型共用一条流水线：<span class="hl-green">分割 → 近似 → 求和 → 取极限</span>（微元法）。做题先回答三个问题：**沿哪个变量积分、微元是什么形状、微元的量怎么表示**。公式只是这条流水线的结论。

**微元法四步**

1. **分割**：把所求量对应的区域/物体切成 $n$ 个小块，第 $i$ 块记作 $\Delta_i$；
2. **近似**：在 $\Delta_i$ 上取一点，把小块近似成规则图形（窄条、薄片、细棒、薄层），写出 $\Delta Q_i\approx q(\xi_i)\Delta x_i$；
3. **求和**：$Q\approx\sum_{i=1}^n q(\xi_i)\Delta x_i$；
4. **取极限**：令 $\lambda=\max\Delta x_i\to0$，得 $Q=\int_a^b q(x)dx$。

<span class="hl-green">选型三问</span>：

- **沿谁积分？** 图形竖着切对 $x$ 积分，横着切对 $y$ 积分；旋转体绕 $x$ 轴通常对 $x$，绕 $y$ 轴可用柱壳对 $x$ 或圆盘对 $y$。
- **微元是什么？** 面积题是窄条，体积题是薄片/薄壳，弧长题是小弧段，物理题是薄层/微元质量。
- **微元的量怎么表示？** 面积 $=$ 长 $\times$ 宽，体积 $=$ 底面积 $\times$ 高，功 $=$ 力 $\times$ 位移，压力 $=$ 压强 $\times$ 面积。

#### 3.4.1 信号速查：看到什么 → 用什么模型

| 题面信号 | 模型 | 第一动作 | 核心公式 |
|---|---|---|---|
| 两曲线围成区域，求面积 | 直角坐标面积 | 求交点、画图定上下边界 | $S=\int_a^b\lvert f-g\rvert dx$ |
| 极坐标曲线围成区域 | 极坐标面积 | 定 $\theta$ 范围，看对称性 | $S=\frac12\int_\alpha^\beta r^2d\theta$ |
| 区域绕 $x$ 轴 | 圆盘 / 垫圈 | 定内外半径 | $V=\pi\int_a^b(f^2-g^2)dx$ |
| 区域绕 $y$ 轴 | 柱壳 / 圆盘 | $y=f(x)$ 用柱壳，$x=g(y)$ 用圆盘 | $V=2\pi\int_a^b xf\,dx$ 或 $\pi\int_c^d x^2dy$ |
| 绕 $y=c$ 或 $x=c$ | 平移半径 | 半径改成到轴的距离 | $\pi\int(f-c)^2dx$ 或 $2\pi\int\lvert x-c\rvert h\,dx$ |
| 已知平行截面面积 | 截面积分 | 写 $A(x)$ | $V=\int_a^b A(x)dx$ |
| 求曲线长度 | 弧长 | 看曲线给的是直角/参数/极坐标 | $\int ds$ |
| 曲线绕轴转，求曲面面积 | 旋转曲面 | 半径 $\times$ 弧长微元 | $S=2\pi\int r\,ds$ |
| 给线密度/面密度 | 质心 | 静矩 $/$ 质量 | $\bar x=\frac{1}{m}\int x\,dm$ |
| 抽水、变力推物体 | 做功 | 取薄层/微元，定提升距离 | $W=\int F\,dx$ |
| 平板铅直挡水 | 水压力 | 深度 $h$ 处取水平窄条 | $dF=\rho gh\cdot L(h)dh$ |
| 细棒吸引质点 | 引力 | 微元当质点，先分解再积分 | $dF=\frac{Gm\,dm}{r^2}$ |
| 积分上限为 $+\infty$ 或有瑕点 | 反常积分 | 先判收敛，再分段算 | $\lim_{b\to\infty}\int_a^b$ |
| 结果含参数，问最值 | 积分后求最值 | 先算出 $V(a)$，再求导 | $V'(a)=0$ |

#### 3.4.2 平面图形的面积

**直角坐标**：若 $f(x)\ge g(x)$，

$$S=\int_a^b[f(x)-g(x)]dx$$

<span class="hl-red">不满足 $f\ge g$ 时必须加绝对值</span>：$S=\int_a^b\lvert f-g\rvert dx$，并在交点处分段。下面这个 $e^{-x}\sin x$ 就是典型：曲线在 $x$ 轴上下交替，必须按零点分段。

**极坐标**：

$$S=\frac12\int_\alpha^\beta r^2(\theta)d\theta$$

先由曲线方程或交点定 $\theta$ 范围；图形关于极轴对称时可算一半再乘 $2$。

**参数方程**：$x=x(t),y=y(t)$，则

$$S=\int_a^b y\,dx=\int_{t_1}^{t_2}y(t)x'(t)dt$$

若 $x'(t)$ 变号，同样要分段并取绝对值。

<span class="hl-orange">边界含未知切点时</span>：先设切点 $(a,f(a))$，写出切线 $y-f(a)=f'(a)(x-a)$，用"过定点/斜率/截距"条件解出 $a$，再定积分限（2012 数二第 18 题）。

> **【例 · 面积要加绝对值（分段）】** 求曲线 $y=e^{-x}\sin x$ 在 $[0,2\pi]$ 上与 $x$ 轴围成的面积。
>
> 曲线在 $[0,\pi]$ 上为正、在 $[\pi,2\pi]$ 上为负，按零点分段并加绝对值：
>
> $$\int_0^\pi e^{-x}\sin x\,dx=\frac{1+e^{-\pi}}{2},\qquad \int_\pi^{2\pi}e^{-x}\lvert\sin x\rvert dx=e^{-\pi}\cdot\frac{1+e^{-\pi}}{2}$$
>
> 故
>
> $$S=\frac{1+e^{-\pi}}{2}\left(1+e^{-\pi}\right)=\frac{(1+e^{-\pi})^2}{2}$$

<span class="hl-orange">关键是先加绝对值再分段</span>；直接积 $e^{-x}\sin x$ 得到的是代数和，正负会抵消。无穷区间上的同类计算要借助级数，超出数二范围，这里不展开。

#### 3.4.3 旋转体体积

**绕坐标轴与任意直线的统一表**：

| 旋转轴 | 区域给法 | 方法 | 公式 |
|---|---|---|---|
| $x$ 轴 | $y=f(x)\ge g(x)\ge0$ | 圆盘 / 垫圈 | $V=\pi\int_a^b[f^2(x)-g^2(x)]dx$ |
| $y$ 轴 | $y=f(x)$，$x\ge0$ | 柱壳 | $V=2\pi\int_a^b x f(x)dx$ |
| $y$ 轴 | $x=g(y)$ | 圆盘 | $V=\pi\int_c^d g^2(y)dy$ |
| $y=c$ | $y=f(x)$，$f\ge c$ | 垫圈（半径 $f-c$） | $V=\pi\int_a^b(f-c)^2dx$ |
| $x=c$ | $y=f(x)$，$x\ge c$ | 柱壳（半径 $x-c$） | $V=2\pi\int_a^b(x-c)f(x)dx$ |

<span class="hl-green">选法口诀</span>：<span class="hl-green">绕 $x$ 轴竖切用圆盘，绕 $y$ 轴竖切用柱壳；轴一平移，半径就改成"到轴的距离"</span>。区域与轴相交时，先拆成轴两侧分别算；区域有内边界（空心）时，绕 $y=c$ 的公式把 $(f-c)^2$ 换成 $(f-c)^2-(g-c)^2$，绕 $x=c$ 且 $x<c$ 时半径写 $c-x$。

> **【例 · 绕 $y=-1$ 旋转】** 区域由 $y=x^2$ 与 $y=1$ 围成，绕 $y=-1$ 旋转，求体积。
>
> 到轴的距离：上边界 $1-(-1)=2$，下边界 $x^2-(-1)=x^2+1$。故
>
> $$V=\pi\int_{-1}^1\left[2^2-(x^2+1)^2\right]dx=\pi\int_{-1}^1(3-2x^2-x^4)dx=\frac{64\pi}{15}$$

> **【例 · 圆锥 + 反常积分拼接】** 曲线 $y=\frac{1}{1+x^2}$ 的拐点为 $M\left(\frac1{\sqrt3},\frac34\right)$，无界区域由曲线、线段 $OM$、$x$ 轴围成，绕 $x$ 轴旋转，求体积。
>
> 边界在 $x=\frac1{\sqrt3}$ 处换：左边下边界是 $OM$，右边下边界是 $x$ 轴。$OM$ 的斜率 $m=\frac{3\sqrt3}{4}$，故
>
> $$V=\pi\int_0^{1/\sqrt3}\left[\frac{1}{(1+x^2)^2}-m^2x^2\right]dx+\pi\int_{1/\sqrt3}^{+\infty}\frac{dx}{(1+x^2)^2}$$
>
> 用 $\int\frac{dx}{(1+x^2)^2}=\frac12\left(\frac{x}{1+x^2}+\arctan x\right)$，得
>
> $$V=\pi\left(\frac{\pi}{4}-\frac{\sqrt3}{16}\right)$$
>
> <span class="hl-orange">要点</span>：规则体（圆锥）与积分体分开算，反常积分先确认收敛（$x\to\infty$ 时被积函数 $\sim x^{-4}$）。

> **【例 · 积分后再求最值】** 曲线 $y=\sqrt{x}e^{-x}$ 与 $x$ 轴、直线 $x=t$ 围成区域绕 $x$ 轴旋转，体积 $V(t)=\pi\int_0^t xe^{-2x}dx$，求 $V(t)$ 的上确界。
>
> $$V'(t)=\pi t e^{-2t}>0\quad(t>0)$$
>
> 故 $V(t)$ 在 $(0,+\infty)$ 上单调增，没有最大值，上确界在 $t\to+\infty$ 处取到：
>
> $$\sup V(t)=\lim_{t\to\infty}V(t)=\pi\int_0^\infty xe^{-2x}dx=\frac{\pi}{4}$$

<span class="hl-orange">这里同时考了"积分上限函数求导"和"反常积分"</span>；先算 $V(t)$ 再求导，不要对 $t$ 直接套圆盘公式。

> **【例 · 同一区域绕两轴】** 区域由 $y=A\sin x$（$0\le x\le\frac{\pi}{2}$，$A>0$）与 $x$ 轴围成，绕 $x$ 轴、$y$ 轴所得体积分别为 $V_1,V_2$，若 $V_1=V_2$，求 $A$。
>
> 绕 $x$ 轴用圆盘，绕 $y$ 轴用柱壳：
>
> $$V_1=\pi A^2\int_0^{\pi/2}\sin^2x\,dx=\frac{\pi^2A^2}{4}$$
>
> $$V_2=2\pi A\int_0^{\pi/2}x\sin x\,dx=2\pi A$$
>
> 由 $V_1=V_2$ 且 $A>0$，得 $A=\frac{8}{\pi}$。
>
> <span class="hl-orange">同一区域绕两轴，通常一个用圆盘、一个用柱壳；先分别列式再令相等</span>。

#### 3.4.4 弧长与旋转曲面面积

**弧长微元 $ds$（三种给法）**：

$$y=f(x):\quad ds=\sqrt{1+y'^2}\,dx$$

$$x=x(t),y=y(t):\quad ds=\sqrt{x'^2(t)+y'^2(t)}\,dt$$

$$r=r(\theta):\quad ds=\sqrt{r^2+r'^2}\,d\theta$$

**弧长**：$L=\int ds$。

**旋转曲面面积**：曲线绕轴旋转，半径 $r$ 是曲线到轴的距离，

$$S=2\pi\int r\,ds$$

绕 $x$ 轴时 $r=\lvert y\rvert$，绕 $y$ 轴时 $r=\lvert x\rvert$。<span class="hl-red">半径漏绝对值或把 $ds$ 写成 $dx$ 是高频错误</span>。

> **【例 · 变限积分曲线弧长】** $y=\int_0^x\tan t\,dt$，$0\le x\le\frac{\pi}{4}$，求弧长。
>
> $y'=\tan x$，$\sqrt{1+y'^2}=\sqrt{1+\tan^2x}=\sec x$，故
>
> $$L=\int_0^{\pi/4}\sec x\,dx=\ln(\sqrt2+1)$$

> **【例 · 根号自动化简】** $y=\int_{-\sqrt3}^x\sqrt{3-t^2}\,dt$，求弧长。
>
> $y'=\sqrt{3-x^2}$，$\sqrt{1+y'^2}=\sqrt{4-x^2}$，积分限为 $[-\sqrt3,\sqrt3]$：
>
> $$L=\int_{-\sqrt3}^{\sqrt3}\sqrt{4-x^2}\,dx=\sqrt3+\frac{4\pi}{3}$$

> **【例 · 参数方程旋转面】** 圆 $x=\cos t,y=\sin t$（$0\le t\le\pi$）绕 $x$ 轴旋转，求曲面面积。
>
> $ds=\sqrt{\sin^2t+\cos^2t}\,dt=dt$，$r=y=\sin t$，故
>
> $$S=2\pi\int_0^\pi\sin t\,dt=4\pi$$

#### 3.4.5 质心与形心

**平面图形**（均匀密度，$S$ 为面积）：

$$\bar{x}=\frac{1}{S}\int_a^b x[f(x)-g(x)]dx,\qquad \bar{y}=\frac{1}{S}\int_a^b\frac12[f^2(x)-g^2(x)]dx$$

**平面曲线**（弧长 $L$）：

$$\bar{x}=\frac{1}{L}\int x\,ds,\qquad \bar{y}=\frac{1}{L}\int y\,ds$$

**旋转体**（绕 $x$ 轴，$V$ 为体积）：

$$\bar{x}=\frac{1}{V}\int_a^b\pi x f^2(x)dx,\qquad \bar{y}=0$$

**细棒**（线密度 $\rho(x)$）：

$$m=\int_a^b\rho(x)dx,\qquad \bar{x}=\frac{1}{m}\int_a^b x\rho(x)dx$$

> **【理解】** 质心 $=$ 静力矩 $/$ 质量。均匀密度时把 $\rho$ 提出去，用 $S$、$L$、$V$ 代替质量；<span class="hl-red">变密度细棒不能套平面图形公式</span>。形心就是均匀密度时的质心。

> **【例 · 平面图形形心】** 区域由 $y=x$ 与 $y=x^2$ 围成，求形心。
>
> $$S=\int_0^1(x-x^2)dx=\frac16$$
>
> $$\bar{x}=6\int_0^1x(x-x^2)dx=6\cdot\frac1{12}=\frac12$$
>
> $$\bar{y}=6\int_0^1\frac12(x^2-x^4)dx=3\cdot\frac2{15}=\frac25$$

> **【例 · 细棒质心（2014 数二填空）】** 细棒位于 $x$ 轴 $[0,1]$，线密度 $\rho(x)=-x^2+2x+1$，求 $\bar{x}$。
>
> $$m=\int_0^1\rho(x)dx=\frac53,\qquad \int_0^1x\rho(x)dx=\frac{11}{12}$$
>
> $$\bar{x}=\frac{11/12}{5/3}=\frac{11}{20}$$

#### 3.4.6 物理应用

**（1）做功**

- 变力沿直线：$W=\int_a^bF(x)dx$；
- 抽水：在高度 $y$ 处取厚度 $dy$ 的水平薄层，体积 $A(y)dy$，重量 $\rho gA(y)dy$，提升距离 $H-y$，

$$W=\rho g\int A(y)(H-y)dy$$

> **【例 · 半球形容器抽水】** 半径 $R$ 的半球形容器装满水，把水全部抽到容器口，求功。
>
> 以容器底为原点、向上为 $y$ 轴，容器口在 $y=R$，球心在 $(0,R)$。高度 $y$ 处截面半径满足 $x^2=R^2-(y-R)^2=2Ry-y^2$，故 $A(y)=\pi(2Ry-y^2)$，提升距离 $R-y$：
>
> $$W=\rho g\pi\int_0^R(2Ry-y^2)(R-y)dy=\rho g\pi\int_0^R(2R^2y-3Ry^2+y^3)dy=\frac{\rho g\pi R^4}{4}$$

<span class="hl-orange">2011 数二第 20 题的容器由两段圆弧拼成</span>：截面半径 $x(y)$ 要按两段圆弧分别写出，提升距离仍是"容器口高度 $-y$"，在拼接点处把积分拆成两段即可。

> **【例 · 变力做功】** 单位质点 $P$ 从 $(0,0)$ 沿 $x$ 轴移到 $(1,0)$，质点 $Q$ 固定在 $(0,1)$，质量 $m$，求克服引力做的功。
>
> 距离 $r=\sqrt{x^2+1}$，引力沿 $x$ 轴的分力为 $\frac{Gmx}{(x^2+1)^{3/2}}$，故
>
> $$W=\int_0^1\frac{Gmx}{(x^2+1)^{3/2}}dx=Gm\left(1-\frac1{\sqrt2}\right)$$

**（2）水压力**

深度 $h$ 处取水平窄条，面积 $L(h)dh$，压强 $\rho gh$，

$$dF=\rho gh\cdot L(h)dh$$

> **【例 · 三角形平板（2020 数二填空第 12 题）】** 等腰直角三角形平板铅直沉入水中，斜边与水面齐平，斜边长 $2a$，求一侧所受水压力。
>
> 顶点在斜边下方 $a$ 处。深度 $h$ 处窄条长度 $L(h)=2(a-h)$，故
>
> $$F=\rho g\int_0^a2h(a-h)dh=\rho g\left[ah^2-\frac{2h^3}{3}\right]_0^a=\frac{\rho g a^3}{3}$$

**（3）引力**

微元质量 $dm=\rho ds$ 当质点，$dF=\frac{Gm\,dm}{r^2}$，再沿坐标轴分解，<span class="hl-green">对称方向先抵消，只积剩下的分量</span>。

> **【例 · 细棒对质点】** 线密度为 $1$ 的细棒位于 $x$ 轴 $[-1,1]$，质量 $m$ 的质点位于 $(0,1)$，求细棒对质点的引力。
>
> 在 $x$ 处取 $dm=dx$，$r=\sqrt{x^2+1}$；水平分量左右对称抵消，只剩竖直分量，方向余弦 $\frac{1}{r}$：
>
> $$F=\int_{-1}^1\frac{Gm}{(1+x^2)^{3/2}}dx=2Gm\int_0^1\frac{dx}{(1+x^2)^{3/2}}=\sqrt2\,Gm$$
>
> 其中 $\int_0^1\frac{dx}{(1+x^2)^{3/2}}=\frac{x}{\sqrt{1+x^2}}\Big|_0^1=\frac1{\sqrt2}$。

**（4）容器油量（截面面积积分）**

柱体体积 $=$ 截面面积 $\times$ 柱长，核心是用定积分求不规则截面面积。

> **【例 · 椭圆柱贮油罐】** 椭圆柱贮油罐平放，椭圆截面长轴 $2a$、短轴 $2b$，油面高度 $\frac{3b}{2}$，求油的质量（罐长 $l$，油密度 $\rho$）。
>
> 以椭圆中心为原点，油面从 $y=-b$ 到 $y=\frac b2$。截面油面积
>
> $$S=\int_{-b}^{b/2}2a\sqrt{1-\frac{y^2}{b^2}}\,dy$$
>
> 令 $y=b\sin t$，$t\in[-\frac\pi2,\frac\pi6]$：
>
> $$S=2ab\int_{-\pi/2}^{\pi/6}\cos^2t\,dt=ab\left(\frac{2\pi}{3}+\frac{\sqrt3}{4}\right)$$
>
> 故 $m=\rho lS=\rho lab\left(\frac{2\pi}{3}+\frac{\sqrt3}{4}\right)$。

**（5）牛顿冷却定律**

$$\frac{dT}{dt}=-k(T-T_{\text{环境}})$$

可分离变量，解为 $T=T_{\text{环境}}+Ce^{-kt}$；用两个时刻的温度定 $C,k$，再预测。方程解法见 §6.2。<span class="hl-orange">这类题落点在微分方程，不在积分微元</span>。

#### 3.4.7 反常积分与含参几何量

**固定流程**：

1. **找异常点**：积分上限 $+\infty$，或被积函数在端点无界（瑕点）；
2. **先判收敛**：用 §3.3 的 $p$ 积分结论或比较判别；
3. **分段计算**：瑕点处拆成 $\lim_{\varepsilon\to0^+}\int_{a+\varepsilon}^b$；
4. **含参再求最值**：先算出 $V(a)$，再对 $a$ 求导、令 $V'(a)=0$。

> **【例 · 无界区域面积与体积】** 曲线 $y=\frac{1}{x\sqrt{1+x^2}}$（$x\ge1$）与 $x$ 轴围成无界区域，求面积 $S$ 及绕 $x$ 轴旋转的体积 $V$。
>
> 先判收敛：$x\to\infty$ 时 $y\sim x^{-2}$，面积收敛；$y^2\sim x^{-4}$，体积也收敛。
>
> 令 $x=\tan t$，$t\in[\frac\pi4,\frac\pi2)$：
>
> $$S=\int_1^\infty\frac{dx}{x\sqrt{1+x^2}}=\int_{\pi/4}^{\pi/2}\csc t\,dt=\ln(\sqrt2+1)$$
>
> $$V=\pi\int_1^\infty\frac{dx}{x^2(1+x^2)}=\pi\int_1^\infty\left(\frac1{x^2}-\frac1{1+x^2}\right)dx=\pi\left(1-\frac\pi4\right)$$

> **【例 · 含参体积求最小值】** 无界区域由 $y=\sqrt{x}\,a^{-x/(2a)}$、$x$ 轴及 $y$ 轴围成，绕 $x$ 轴旋转，体积记为 $V(a)$，求 $V(a)$ 的最小值（$a>1$）。
>
> 先算
>
> $$V(a)=\pi\int_0^\infty x a^{-x/a}dx=\pi\int_0^\infty xe^{-x\ln a/a}dx=\frac{\pi a^2}{(\ln a)^2}$$
>
> 令 $g(a)=\frac{a}{\ln a}$，则 $g'(a)=\frac{\ln a-1}{(\ln a)^2}$，驻点 $a=e$。故
>
> $$V_{\min}=V(e)=\pi e^2$$
>
> <span class="hl-orange">这类题的标准动作是"先积分（含参），再求最值"</span>，不要先代特殊值。

#### 3.4.8 低频模型（了解）

**函数平均值**：

$$\bar f=\frac{1}{b-a}\int_a^b f(x)dx$$

几何意义：与曲线围成等面积的矩形的高。

**平面薄板质心**：均匀密度时与平面图形质心公式相同；变面密度 $\sigma(x,y)$ 时

$$m=\iint_D\sigma(x,y)\,d\sigma,\qquad \bar x=\frac{1}{m}\iint_D x\sigma\,d\sigma,\qquad \bar y=\frac{1}{m}\iint_D y\sigma\,d\sigma$$

（二重积分计算见第五章。）

**转动惯量**：微元法 $I=\int r^2dm$，$r$ 是微元到转轴的距离。数二近 20 年未单独考；若你的考纲列出，记住"$r^2dm$"这个微元即可，不必背具体图形的结果。

### 3.5 本章易错点

1. 变限积分求导前先检查被积函数是否含 $x$，含 $x$ 要先提出或换元；
2. 可积不等于有原函数；变上限积分只有在 $f$ 连续时才是原函数，$f$ 有第一类间断点时它只是积分；
3. 定积分换元必须同时换上下限，不必回代；
4. 反常积分要先找瑕点，分段计算，<span class="hl-red">不能直接用牛莱公式</span>；
5. 奇偶性结论<span class="hl-orange">只适用于对称区间</span>；
6. 分部积分选 $u$ 顺序：反、对、幂、三、指（排在前的作 $u$）；
7. $\int\frac1x dx=\ln\lvert x\rvert +C$，<span class="hl-red">绝对值不能漏</span>；
8. 拆分积分时，原积分前的常系数要乘进拆开后的两项；
9. 面积、旋转体：先画图定边界；$f,g$ 上下不确定就加绝对值；旋转轴不在坐标轴上时，半径一律写"到轴的距离"（§3.4.2–3.4.3）；
10. 旋转曲面 $S=2\pi\int r\,ds$：$r$ 带绝对值，$ds$ 不能漏根号（§3.4.4）；
11. 无界区域先判收敛再算；物理题先取微元：抽水看提升距离，压力看深度，引力先分解（§3.4.6–3.4.7）。

---

## 第四章 多元函数微分学

### 4.1 基本概念

**平面点集**：邻域 $$U(P_0,\delta)=\{P\mid \lvert PP_0\rvert <\delta\}$$；内点、边界点、开集、区域。

**二元函数**：$z=f(x,y),\ (x,y)\in D$。

**二重极限**：

$$\lim_{(x,y)\to(x_0,y_0)}f(x,y)=A\iff \forall\varepsilon>0,\ \exists\delta>0,\ 0<\sqrt{(x-x_0)^2+(y-y_0)^2}<\delta\Rightarrow |f(x,y)-A|<\varepsilon$$

> 注意：点 $(x,y)$ 以**任意方式**趋于 $(x_0,y_0)$ 极限都为 $A$，若沿两条不同路径极限不同，则二重极限不存在。

**连续**：$\lim_{(x,y)\to(x_0,y_0)}f(x,y)=f(x_0,y_0)$。

**多元连续函数性质**：有界闭区域上连续函数有最大值最小值定理、介值定理。

### 4.2 偏导数与全微分

**偏导数**：

$$f_x(x_0,y_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}$$

$$f_y(x_0,y_0)=\lim_{\Delta y\to0}\frac{f(x_0,y_0+\Delta y)-f(x_0,y_0)}{\Delta y}$$

**高阶偏导**：$f_{xx},f_{xy},f_{yx},f_{yy}$。若混合偏导连续，则 $f_{xy}=f_{yx}$。

**全微分**：

$$dz=f_x(x,y)dx+f_y(x,y)dy$$

**可微、可导、连续的关系**（数二高频考点）：

- 偏导数连续 $\Rightarrow$ 可微；
- 可微 $\Rightarrow$ 连续、可微 $\Rightarrow$ 偏导数存在；
- <span class="hl-red">偏导数存在 $\not\Rightarrow$ 可微、偏导数存在 $\not\Rightarrow$ 连续</span>；
- <span class="hl-red">连续 $\not\Rightarrow$ 偏导数存在</span>。

**可微判别**：计算

$$\lim_{(\Delta x,\Delta y)\to(0,0)}\frac{\Delta z-f_x\Delta x-f_y\Delta y}{\sqrt{\Delta x^2+\Delta y^2}}$$

极限为 $0$ 则可微，否则不可微。

> **【理解】** 偏导数只沿 $x,y$ 两轴取值。例：$f(x,y)=\frac{xy}{x^2+y^2}$ 在原点两偏导均为 $0$，但沿 $y=kx$ 趋于 $0$ 得 $\frac{k}{1+k^2}$，极限不存在，故不连续、不可微。

### 4.3 多元复合函数求导

**链式法则**：设 $u=u(x,y),\ v=v(x,y)$，$z=f(u,v)$：

$$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x},\qquad \frac{\partial z}{\partial y}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}$$

**方法**：画树状图（$z$ 为根，中间变量为枝，自变量为叶），"沿线相乘、分线相加"。

**记号**：对第一个中间变量求导记 $f_1'$，对第二个记 $f_2'$；二阶记 $f_{11}'',f_{12}'',f_{22}''$，且 $f_{12}''=f_{21}''$。

**一自变量抽象复合**（$y=f\bigl(u(x),v(x)\bigr)$，题干写"$f$ 具有二阶连续偏导数"）：

$$\frac{dy}{dx}=f_1'\,u'+f_2'\,v'$$

求二阶时把 $f_1',f_2'$ 再当复合函数：对 $x$ 求导用乘积法则，并对 $f_1',f_2'$ 再套一次链式法则（各乘 $u',v'$）。结果是 $f_1',f_{11}''$ 等在特定点的取值。先写通式再代入；特殊点上大量交叉项会消失（如 $x=0$ 时 $\sin0=0$）。

**全微分形式不变性**：$dz=f_u du+f_v dv$。

### 4.4 隐函数求导

**一个方程 $F(x,y)=0$**：

$$\frac{dy}{dx}=-\frac{F_x}{F_y}\quad (F_y\ne0)$$

**$F(x,y,z)=0$ 确定 $z=z(x,y)$**：

$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},\qquad \frac{\partial z}{\partial y}=-\frac{F_y}{F_z}\quad (F_z\ne0)$$

### 4.5 多元函数极值与最值

**无条件极值（"1+1"）**：

- 必要条件：$z=f(x,y)$ 在 $(x_0,y_0)$ 可导且为极值点 $\Rightarrow f_x=0,\ f_y=0$；
- 充分条件：令 $A=f_{xx}(x_0,y_0),\ B=f_{xy},\ C=f_{yy}$：
  - $AC-B^2>0$：有极值，$A>0$ 极小、$A<0$ 极大；
  - $AC-B^2<0$：无极值；
  - $AC-B^2=0$：无法判定。

**条件极值（拉格朗日乘数法）**：求 $f(x,y)$ 在 $\varphi(x,y)=0$ 下的极值，构造

$$L(x,y,\lambda)=f(x,y)+\lambda\varphi(x,y)$$

解方程组 $L_x=0,\ L_y=0,\ L_\lambda=0$。

**有界闭区域上最值**：先求区域内无条件极值，再求边界上条件极值，最后比较。

### 4.6 本章易错点

1. 偏导数存在函数不一定连续，也不一定可微（三者关系要画清）；
2. 求二重极限不能只验证直线路径，两条路径极限不同只用于证明不存在；
3. 抽象复合求二阶：$f_1',f_2'$ 仍是同结构的复合函数，要继续用链式法则；一自变量时答案落在点上的符号（如 $f_1'(1,1)$），先通式再代入；
4. 隐函数求导公式带负号，且分母偏导不为 $0$；
5. 拉格朗日函数中 $\lambda$ 是辅助变量，求出后要回代比较；
6. 极值判别式 $AC-B^2$ 符号记反是高频错误。

---

## 第五章 二重积分

### 5.1 概念与性质

**定义**：

$$\iint_D f(x,y)d\sigma=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta\sigma_i$$

**几何意义**：$f(x,y)\ge0$ 时为曲顶柱体体积；$f\equiv1$ 时 $\iint_D d\sigma=S_D$（区域面积）。

**性质**：线性、可加性、比较性、估值定理、积分中值定理（$\exists(\xi,\eta),\ \iint_D f\,d\sigma=f(\xi,\eta)S_D$）。

### 5.2 二重积分计算

**直角坐标**：

$$\iint_D f(x,y)d\sigma=\iint_D f(x,y)dx\,dy$$

- X 型区域（$a\le x\le b,\ \varphi_1(x)\le y\le\varphi_2(x)$）：

$$\int_a^b dx\int_{\varphi_1(x)}^{\varphi_2(x)} f(x,y)\,dy$$

- Y 型区域（$c\le y\le d,\ \psi_1(y)\le x\le\psi_2(y)$）：

$$\int_c^d dy\int_{\psi_1(y)}^{\psi_2(y)} f(x,y)\,dx$$

**极坐标**：$x=r\cos\theta,\ y=r\sin\theta,\ d\sigma=r\,dr\,d\theta$：

$$\iint_D f(x,y)d\sigma=\iint_D f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$

> 适用：区域为圆、圆环、扇形，或被积函数含 $x^2+y^2$、$\frac yx$、$\frac xy$。

**积分区域由参数方程给出**（2018 数二第 17 题考法）：

边界为单参数曲线 $x=x(t),\ y=y(t)\ (\alpha\le t\le\beta)$、另一边界为某坐标轴时，按三步走：

1. 先化成直角坐标累次积分（通常是 X 型）：$a\le x\le b,\ 0\le y\le y(x)$；
2. 内层对 $y$ 积分到底，结果只含 $x$，如 $\int_0^{y(x)}(x+2y)\,dy=x\,y(x)+y(x)^2$；
3. 外层再代参数：$x=x(t)$、$y(x)=y(t)$、$dx=x'(t)\,dt$，积分限换成 $t:\alpha\to\beta$。

<span class="hl-red">顺序不能颠倒</span>：内层若提前把 $y$ 当作 $t$ 的函数塞进去，$dy$ 就无法处理。

**例（2018 数二 17）**：$D$ 由摆线一拱 $x=t-\sin t,\ y=1-\cos t\ (0\le t\le 2\pi)$ 与 $x$ 轴围成，求

$$I=\iint_D(x+2y)\,dx\,dy$$

区域写成 X 型：$0\le x\le 2\pi,\ 0\le y\le y(x)$，其中 $y(x)=1-\cos t$ 由 $x=t-\sin t$ 隐式确定。

$$I=\int_0^{2\pi}dx\int_0^{y(x)}(x+2y)\,dy=\int_0^{2\pi}\big[x\,y(x)+y(x)^2\big]dx$$

外层代参：$dx=(1-\cos t)\,dt$，$y(x)=1-\cos t$：

$$I=\int_0^{2\pi}\big[(t-\sin t)(1-\cos t)+(1-\cos t)^2\big](1-\cos t)\,dt=\underbrace{\int_0^{2\pi}(t-\sin t)(1-\cos t)^2dt}_{3\pi^2}+\underbrace{\int_0^{2\pi}(1-\cos t)^3dt}_{5\pi}$$

其中 $\int_0^{2\pi}\sin t(1-\cos t)^2dt=0$。故

<div class="hl-green" markdown="1">

$$I=3\pi^2+5\pi$$

</div>

<span class="hl-orange">**拓展：一般换元与雅可比**</span>（超出数二大纲主流，覆盖线性换元类技巧题）。若 $x=x(u,v),\ y=y(u,v)$ 把 $uv$ 平面区域 $D'$ 一一映到 $xy$ 平面区域 $D$，且

$$J=\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}x_u & x_v\\ y_u & y_v\end{vmatrix}\ne0$$

则

$$\iint_D f(x,y)\,dx\,dy=\iint_{D'} f\big(x(u,v),y(u,v)\big)\,\lvert J\rvert\,du\,dv$$

被积函数整体换成 $f(x(u,v),y(u,v))$，面积元素换成 $\lvert J\rvert\,du\,dv$。极坐标即 $x=r\cos\theta,\ y=r\sin\theta$ 时 $J=r$ 的特例。线性换元例：$x=u+v,\ y=u-v$，此时 $J=-2$，$dx\,dy=2\,du\,dv$。

### 5.3 对称性

**普通对称性**：

- $D$ 关于 $y$ 轴（$x=0$）对称：

$$\iint_D f\,d\sigma=\begin{cases}2\iint_{D_1} f\,d\sigma,&f(-x,y)=f(x,y)\ (\text{关于 }x\text{ 偶})\\0,&f(-x,y)=-f(x,y)\ (\text{关于 }x\text{ 奇})\end{cases}$$

- $D$ 关于 $x$ 轴（$y=0$）对称：同理，看 $f$ 关于 $y$ 的奇偶；
- 关于 $x=a$、$y=a$ 对称：用 $f(2a-x,y)$ 判别；
- 关于原点对称：用 $f(-x,-y)$ 判别。

**轮换对称性**：若 $x,y$ 对调后区域 $D$ 不变（$D$ 关于 $y=x$ 对称），则

$$\iint_D f(x,y)d\sigma=\iint_D f(y,x)d\sigma$$

若 $f(x,y)+f(y,x)=a$，则

<div class="hl-green" markdown="1">

$$I=\frac12\iint_D[f(x,y)+f(y,x)]d\sigma=\frac a2 S_D$$

</div>

### 5.4 交换积分次序

**步骤**：① 由原累次积分上下限画出区域 $D$；② 重新确定另一类型区域的上下限。

**例题**：$\int_0^1 dy\int_0^{y^2} y\sin(1-x)^2 dx$（对 $x$ 积分不好算，换序）。

$$\text{原式}=\int_0^1 dx\int_{\sqrt x}^1 y\sin(1-x)^2 dy=\int_0^1 \sin(1-x)^2\left(\frac12y^2\Big|_{\sqrt x}^1\right) dx=\frac12\int_0^1(1-x)\sin(1-x)^2 dx$$

**坐标系互换**：与换序同理，本质是同一个积分换一种描述。<span class="hl-green">区域边界是圆弧、或被积函数含 $x^2+y^2$、$\frac yx$</span> 时倾向极坐标；<span class="hl-green">边界是直线围成的多边形、被积函数为多项式</span> 时倾向直角坐标。互换前先画图，避免 $\theta$ 与 $r$ 的定限混乱。

### 5.5 题型信号速查

| 题面信号 | 想到 | 立刻能做什么 |
|---|---|---|
| 区域是圆 / 圆环 / 扇形 / 偏心圆，或含 $x^2+y^2$、$\frac yx$ | 极坐标 | 画射线定 $\theta$ 范围，由边界解出 $r$ 上下限，<span class="hl-red">别漏 $r$</span> |
| 累次积分内层积不出（如 $\sin(1-x)^2$、$e^{x^2}$） | 交换次序 | 由原上下限画区域，重定另一型边界 |
| 区域关于坐标轴、$x=a$、$y=a$、原点对称 | 普通对称性 | 先验区域对称，再配 $f$ 相应奇偶（§5.3） |
| 区域关于 $y=x$ 对称 | 轮换对称性 | 用 $\iint f(x,y)=\iint f(y,x)$；$f+f=a$ 时 $I=\frac a2S_D$ |
| 被积函数含 $\lvert\cdot\rvert$、$\max$、$\min$、分段定义 | 分块计算 | 按符号分界把 $D$ 拆成几块分别积 |
| 边界形如 $x=x(t),\ y=y(t)$，另一边界是坐标轴 | 参数区域 | 化 X 型 → 内层积 $y$ → 外层代 $t$，$dx=x'(t)dt$（§5.2） |
| 出现线性变换、椭圆域 $x^2/a^2+y^2/b^2\le1$ | 一般换元 | 求 $J$，面积元素乘 $\lvert J\rvert$（§5.2 拓展） |
| 积分上限含参、结果含参 | 含参综合 | 先对区域积完，再对参数求导（§5.6） |
| 比较两个二重积分大小或估计值 | 估值 / 中值 | 比较被积函数，或用估值定理、积分中值定理（§5.1） |

### 5.6 综合与证明套路

**含参积分求导**：积分上限（或结果）含参数 $x$ 时，先把对 $y$ 的积分积完得到一个关于 $x$ 的表达式，再对 $x$ 求导。若求导后出现 $f'(x)$ 与 $f(x)$ 的方程，就是与微分方程联立（第六章）的典型综合题。

**积分不等式**：常用两条路——① 比较被积函数大小（如 $x^2\le x$ 在 $[0,1]$ 上），由比较性直接放缩；② 先用估值定理或积分中值定理把积分化为 $f(\xi,\eta)S_D$，再把问题转成一元函数的最值。

### 5.7 本章易错点

1. 极坐标下面积元素是 <span class="hl-red">$r\,dr\,d\theta$</span>，$r$ 不能漏；
2. 用对称性前必须先验证区域对称性，且被积函数奇偶性要对应；
3. 交换次序要先画区域，不能直接改上下限；
4. 极坐标下 $\theta$ 范围与 $r$ 范围要根据图形确定；
5. 分段函数（含绝对值、max、min）要先分区域去符号；
6. 区域由参数方程给出时，<span class="hl-red">只对外层 $x$ 换元</span>，内层 $y$ 必须用直角坐标积到底；
7. 一般换元必须乘 $\lvert J\rvert$ 并取绝对值，注意换元须一一对应；
8. 轮换对称要求 <span class="hl-orange">区域 $D$ 关于 $y=x$ 对称</span>，仅有被积函数对称不够；
9. 含参求导前先确认可积可导，别把积分变量与参数混淆。

### 5.8 本章速查

**直角坐标**：$\displaystyle\iint_D f\,d\sigma=\int_a^b dx\int_{\varphi_1(x)}^{\varphi_2(x)}f\,dy=\int_c^d dy\int_{\psi_1(y)}^{\psi_2(y)}f\,dx$

**极坐标**：$\displaystyle\iint_D f\,d\sigma=\iint_{D'}f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$

**一般换元**：$\displaystyle\iint_D f\,dxdy=\iint_{D'}f(x(u,v),y(u,v))\,\lvert J\rvert\,dudv,\quad J=\frac{\partial(x,y)}{\partial(u,v)}$

**对称性**：$D$ 关于 $y$ 轴对称，$f$ 关于 $x$ 奇则积分为 $0$，偶则为 $2\iint_{D_1}f$；关于 $x$ 轴同理。

**轮换对称**：$D$ 关于 $y=x$ 对称 $\Rightarrow \iint_D f(x,y)=\iint_D f(y,x)$，且 $f(x,y)+f(y,x)=a$ 时 $I=\frac a2S_D$。

**面积**：$\displaystyle\iint_D d\sigma=S_D$。

---

## 第六章 常微分方程

### 6.1 基本概念

**微分方程**：含未知函数导数（或微分）的方程。阶数（最高阶导数阶数）、解、通解（含独立常数个数等于阶数）、特解、初值条件。

> **【理解】** 综合题常由积分关系求导得到微分方程，通解里的 $C$ 要回原式定。变上限积分的隐初值见 §3.2。

#### 6.1.1 几何条件 → 微分方程（建模链）

> **【定位】** 数二压轴题常走这条链：先由几何条件列微分方程，解出曲线，再回答弧长、面积或最值。第一步不是积分，而是把几何语言翻译成 $y,y'$ 的方程。

**三个高频翻译**：

| 几何条件 | 翻译 | 后续 |
|---|---|---|
| 切线在 $y$ 轴上的截距 | $Y-y=y'(X-x)$，令 $X=0$：$b=y-xy'$ | 与定点/距离列方程 |
| 法线在 $x$ 轴上的截距 | 法线斜率 $-\frac1{y'}$，令 $Y=0$：$a=x+yy'$ | 截距相等/成比例 |
| 面积、体积、弧长条件 | $S(x)=\int_a^x f(t)dt$ 等 | 对 $x$ 求导，化微分方程 |

**固定流程**：

1. 设曲线上点为 $(x,y)$，写出切线/法线/面积表达式；
2. 用题给条件列方程，消去辅助变量；
3. 整理成标准一阶方程（可分离/齐次/线性），求解；
4. 用曲线过的定点定 $C$（定 $C$ 常回到原几何式，别只用通解）；
5. 再算题目要的弧长、面积、体积或最值。

**例 · 切线截距**：曲线上任一点 $P(x,y)$ 到 $y$ 轴的距离等于该点处切线在 $y$ 轴上的截距，且曲线过 $(1,1)$，求曲线方程。

- 点到 $y$ 轴距离为 $x$（$x>0$）；切线在 $y$ 轴截距为 $y-xy'$；
- 条件：$x=y-xy'$，即 $y'-\frac1x y=-1$；
- 积分因子 $\frac1x$：$\left(\frac yx\right)'=-\frac1x$，故 $\frac yx=C-\ln x$，$y=x(C-\ln x)$；
- 代入 $y(1)=1$ 得 $C=1$，所以 $y=x(1-\ln x)$。

**例 · 侧面积等于体积的 2 倍**：设 $f(x)>0$，曲线 $y=f(x)$ 在 $[0,x]$ 上与 $x$ 轴围成的区域绕 $x$ 轴旋转，侧面积恒等于体积的 $2$ 倍，且 $f(0)=1$，求 $f(x)$。

- 侧面积 $S(x)=2\pi\int_0^x f(t)\sqrt{1+f'^2(t)}dt$，体积 $V(x)=\pi\int_0^x f^2(t)dt$；
- 条件 $S=2V$：$2\pi\int f\sqrt{1+f'^2}=2\pi\int f^2$，两边对 $x$ 求导得 $f\sqrt{1+f'^2}=f^2$；
- $f>0$ 约去 $f$：$\sqrt{1+f'^2}=f$，即 $f'^2=f^2-1$；
- 取正支（负支由对称性给同一结果），$\dfrac{df}{\sqrt{f^2-1}}=dx$，积分得 $\operatorname{arcosh}f=x+C$；
- $f(0)=1$ 得 $C=0$，故 $f(x)=\cosh x$。

> **【易错】** 面积条件含变限积分时，先令 $x=a$ 读出 $f(a)$（隐初值，§3.2），再求导；只求导不定初值，$C$ 会错。

### 6.2 一阶微分方程

**可分离变量**：$\frac{dy}{dx}=f(x)g(y)$，则 $\int\frac{dy}{g(y)}=\int f(x)dx$。

**齐次方程**：$\frac{dy}{dx}=\varphi\left(\frac yx\right)$，令 $u=\frac yx$（$y=ux,\ y'=u+xu'$）。

**一阶线性微分方程**：$y'+P(x)y=Q(x)$，通解

<div class="hl-green" markdown="1">

$$y=e^{-\int P\,dx}\left[\int Q(x)e^{\int P\,dx}dx+C\right]$$

</div>

**伯努利方程**：$y'+P(x)y=Q(x)y^n\ (n\ne0,1)$，令 $z=y^{1-n}$，化为 $z'+(1-n)Pz=(1-n)Q$。

### 6.3 可降阶的高阶方程

**$y^{(n)}=f(x)$ 型**：连续积分 $n$ 次。

**$y''=f(x,y')$ 型（不显含 $y$）**：令 $p=y'$，则 $y''=p'$，化为 $p'=f(x,p)$。

**$y''=f(y,y')$ 型（不显含 $x$）**：令 $p=y'$，则 $y''=p\frac{dp}{dy}$，化为 $p\frac{dp}{dy}=f(y,p)$。

### 6.4 高阶线性微分方程

**线性方程解的结构**：

$$y''+P(x)y'+Q(x)y=f(x)$$

- 齐次 $y''+Py'+Qy=0$：两个线性无关解 $y_1,y_2$（$\frac{y_1}{y_2}\ne$ 常数），通解 $Y=C_1y_1+C_2y_2$；
- 非齐次：通解 $$y=Y+y^*$$（$$y^*$$ 为一个特解）；
- 叠加原理：$f=f_1+f_2$ 时分别求特解相加。

**二阶常系数齐次**：$y''+py'+qy=0$，特征方程 $r^2+pr+q=0$：

| 特征根 | 通解 |
|---|---|
| 两不等实根 $r_1\ne r_2$ | $y=C_1e^{r_1x}+C_2e^{r_2x}$ |
| 两相等实根 $r_1=r_2=r$ | $y=(C_1+C_2x)e^{rx}$ |
| 一对共轭复根 $r=\alpha\pm i\beta$ | $y=e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$ |

**二阶常系数非齐次**：

- $f(x)=e^{\lambda x}P_m(x)$：设 $y^*=x^k e^{\lambda x}Q_m(x)$，其中 <span class="hl-red">$k$ 是 $\lambda$ 作为特征根的重数</span>（$0,1,2$）；
- $f(x)=e^{\lambda x}[P_l(x)\cos\omega x+P_n(x)\sin\omega x]$：设

$$y^*=x^k e^{\lambda x}[R_m(x)\cos\omega x+S_m(x)\sin\omega x],\quad m=\max(l,n)$$

$k$ 为 $\lambda+i\omega$ 是否为特征根（$0$ 或 $1$）。

### 6.5 微分算子法（快速求特解）

**算子定义**：$D=\frac{d}{dx}$，$D^2=\frac{d^2}{dx^2}$，方程 $y''+py'+qy=f(x)$ 写成

$$(D^2+pD+q)y=f(x)\quad\Rightarrow\quad y^*=\frac{1}{D^2+pD+q}f(x)=F(D)^{-1}f(x)$$

**基本规则**：

1. $\frac1{D-a}f(x)=e^{ax}\int e^{-ax}f(x)dx$；
2. $\frac1{F(D)}e^{kx}=\frac{e^{kx}}{F(k)}$（$F(k)\ne0$），$F(k)=0$ 时提 $x$：$\frac1{F(D)}e^{kx}=x\frac{e^{kx}}{F'(k)}$（$k$ 为单根），二重根再提 $x$；
3. $\frac1{F(D^2)}\sin ax=\frac{\sin ax}{F(-a^2)}$（$F(-a^2)\ne0$），为零则提 $x$，且 $\frac1{D^2+a^2}\sin ax=-\frac{x}{2a}\cos ax$；
4. $\frac1{F(D)}x^n$：将 $\frac1{F(D)}$ 展开为 $D$ 的幂级数（到 $D^n$ 项）后逐项作用。

### 6.6 本章易错点

1. 一阶线性方程通解公式中 $e^{\int P\,dx}$ 与 $e^{-\int P\,dx}$ 别用反；
2. 齐次方程（可分离变量的"齐次"）与齐次线性方程是两个概念；
3. 可降阶方程中，不显含 $y$ 令 $p=y'$ 用 $p'$；不显含 $x$ 用 $p\frac{dp}{dy}$；
4. 设特解时 $x^k$ 的 $k$ 由 $\lambda$ 与特征根关系确定，<span class="hl-red">漏乘 $x$ 是高频错误</span>；
5. 特征根为复根时通解是 $e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$，不要写 $e^{i\beta x}$；
6. 通解中常数个数必须等于方程阶数。

---

## 附录：一页速查

**等价无穷小（$x\to0$）**

$$\sin x\sim\tan x\sim\arcsin x\sim\arctan x\sim x,\quad e^x-1\sim x,\quad \ln(1+x)\sim x$$

$$1-\cos x\sim\frac{x^2}{2},\quad (1+x)^a-1\sim ax,\quad x-\sin x\sim\frac{x^3}{6},\quad \tan x-x\sim\frac{x^3}{3}$$

**泰勒前几项**

$$e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+o(x^3),\qquad \sin x=x-\frac{x^3}{6}+o(x^3)$$

$$\cos x=1-\frac{x^2}{2}+\frac{x^4}{24}+o(x^4),\qquad \ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3)$$

**积分**

$$\int\frac{dx}{1+x^2}=\arctan x+C,\quad \int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C,\quad \int\sec x\,dx=\ln\lvert\sec x+\tan x\rvert+C$$

$$\int_0^{\pi/2}\sin^n x\,dx=\int_0^{\pi/2}\cos^n x\,dx=\begin{cases}\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdots\dfrac12\cdot\dfrac{\pi}{2},&n\text{ 为偶}\\[4pt]\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdots\dfrac23\cdot1,&n\text{ 为奇}\end{cases}$$

**旋转体与曲线**

$$V_x=\pi\int_a^b(f^2-g^2)dx,\qquad V_y=2\pi\int_a^b x f\,dx,\qquad S=2\pi\int r\,ds,\qquad L=\int ds$$

**微分方程**

$$y'+P(x)y=Q(x)\ \Rightarrow\ y=e^{-\int P\,dx}\left[\int Q(x)e^{\int P\,dx}dx+C\right]$$

特征根 $r_1\ne r_2$：$C_1e^{r_1x}+C_2e^{r_2x}$；$r_1=r_2=r$：$(C_1+C_2x)e^{rx}$；$\alpha\pm i\beta$：$e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$。

**索引**：极限选法 §1.5.2；中值定理法 §1.5.4；反例库 §1.7；定积分应用 §3.4.1；二重积分选法 §5.5；几何条件建模 §6.1.1。

**题型分布**：极限计算（选择/填空高频）、中值定理证明、一元积分计算与应用、多元偏导/全微分、二重积分、微分方程。定积分应用重点：旋转体体积、弧长与旋转面、质心，以及做功/水压力/引力三类物理微元（§3.4）。

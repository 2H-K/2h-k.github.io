---
title: "数二 · 高等数学笔记"
description: 无
date: 2026-10-28 19:30:00 +0800
categories: ["数学二", "高数"]
math: true
---

> 适用范围：数二（高数 + 线代）。数二高数不考：空间解析几何、三重积分、曲线/曲面积分、无穷级数。
> 每章结构：知识框架 → 定义定理 → 题型方法 → 易错点 → 公式速查。

> 全文颜色约定：<span class="hl-red">红色 = 符号 / 易错</span>，<span class="hl-orange">橙色 = 条件 / 区别</span>，<span class="hl-green">绿色 = 结论 / 必背</span>，<span class="hl-blue">蓝色 = 定义 / 基本关系</span>。

---

## 第一章 函数、极限、连续

### 1.1 函数

**定义**：设数集 $D\subset\mathbb{R}$，若存在对应法则 $f$，使每个 $x\in D$ 都有唯一确定的 $y$ 与之对应，则称 $f:D\to\mathbb{R}$ 为定义在 $D$ 上的函数，记 $y=f(x)$。$D$ 为定义域，$$f(D)=\{f(x)\mid x\in D\}$$ 为值域。

**几个特殊函数**：

- 绝对值函数：$$\lvert x\rvert =\begin{cases}x,&x\ge0\\-x,&x<0\end{cases}$$
- 符号函数：$$\operatorname{sgn}x=\begin{cases}1,&x>0\\0,&x=0\\-1,&x<0\end{cases}$$，有 $x=\lvert x\rvert \operatorname{sgn}x$
- 取整函数：$[x]$（不超过 $x$ 的最大整数），有 $x-1<[x]\le x$，$[x+n]=[x]+n$

**函数的四种特性**：

| 特性 | 定义 |
|---|---|
| 有界性 | $\exists M>0$，使 $\lVert f(x)\rVert \le M,\ \forall x\in X$；否则无界 |
| 单调性 | 单增：$f(x_1)<f(x_2)$；单减：$f(x_1)>f(x_2)$（$x_1<x_2$） |
| 奇偶性 | 定义域关于原点对称；$f(-x)=f(x)$ 为偶，$f(-x)=-f(x)$ 为奇 |
| 周期性 | $\exists T>0$，$f(x+T)=f(x),\ \forall x\in D$ |

**反函数**：$y=f(x)$ 单射（如单调）才有反函数 $x=f^{-1}(y)$，习惯写成 $y=f^{-1}(x)$。$f$ 与 $f^{-1}$ 图像关于 $y=x$ 对称。

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

**推论**：若有两个子列收敛于不同值，则数列发散（常用于判断含 $(-1)^n$、分段数列）。

**存在准则**：

- 单调有界准则：单调有界数列必有极限；
- 夹逼准则：$y_n\le x_n\le z_n$，且 $\lim y_n=\lim z_n=a$，则 $\lim x_n=a$。

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

> 注意：等价无穷小只能用于**乘除因子**，<span class="hl-red">加减中不能直接替换</span>（加减需用泰勒展开）。

**常用等价无穷小（$x\to0$）**：

$$\sin x\sim\tan x\sim\arcsin x\sim\arctan x\sim x,\quad e^x-1\sim x,\quad a^x-1\sim x\ln a$$

$$\ln(1+x)\sim x,\quad 1-\cos x\sim\frac12x^2,\quad (1+x)^a-1\sim ax$$

$$\sqrt{1+x}-1\sim\frac12x,\quad x-\sin x\sim\frac16x^3,\quad x-\tan x\sim-\frac13x^3$$

$$\tan x-x\sim\frac13x^3,\quad x-\arcsin x\sim-\frac16x^3,\quad x-\arctan x\sim\frac13x^3$$

$$\sec x-1\sim\frac12x^2,\quad x-\ln(1+x)\sim\frac12x^2$$

> **【理解】** 高阶等价无穷小由泰勒展开直接得到，不必单独记：$\sin x=x-\frac{x^3}{6}+o(x^3)$，故 $x-\sin x\sim\frac{x^3}{6}$；$\tan x=x+\frac{x^3}{3}+o(x^3)$，故 $\tan x-x\sim\frac{x^3}{3}$。

### 1.5 极限计算方法（七种未定式）

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

**洛必达法则**：若满足：① $\lim f(x)=\lim F(x)=0$（或 $\infty$）；② 在去心邻域内 $f',F'$ 存在且 $F'\ne0$；③ $\lim\frac{f'}{F'}$ 存在（或为 $\infty$），则

$$\lim\frac{f(x)}{F(x)}=\lim\frac{f'(x)}{F'(x)}$$

> 注意：含 $\sin\infty$、$\cos\infty$（如 $\lim_{x\to\infty}\frac{x+\sin x}{x}$）不能用洛必达，应直接用极限性质或夹逼。

**数列极限三大招**：

1. **夹逼准则**：含 $n$ 项求和、放缩；
2. **单调有界**：递推数列 $x_{n+1}=f(x_n)$，先证有界、再证单调；
3. **定积分定义**：$\lim_{n\to\infty}\frac1n\sum_{i=1}^n f\left(\frac{i}{n}\right)=\int_0^1 f(x)\,dx$。

**常用泰勒（麦克劳林）展开（$x\to0$）**：

$$e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+o(x^3)$$

$$\sin x=x-\frac{x^3}{3!}+o(x^3),\quad \cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+o(x^4)$$

$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3)$$

$$(1+x)^a=1+ax+\frac{a(a-1)}{2}x^2+o(x^2)$$

$$\tan x=x+\frac{x^3}{3}+o(x^3),\quad \arcsin x=x+\frac{x^3}{6}+o(x^3),\quad \arctan x=x-\frac{x^3}{3}+o(x^3)$$

> **【理解】** $e^x$ 的导数等于自身，第 $n$ 项系数须为 $1/n!$，求导后才降为前一项；$\sin$ 只含奇次、$\cos$ 只含偶次、符号交替，由奇偶性决定。

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

**连续函数运算**：连续函数的和、差、积、商（分母不为零）、复合仍连续；基本初等函数在定义域内连续；初等函数在定义区间内连续。

**闭区间上连续函数的性质**：

1. 有界性与最大值最小值定理；
2. 零点定理：$f(a)f(b)<0$，则 $\exists\xi\in(a,b)$ 使 $f(\xi)=0$；
3. 介值定理：$f$ 在 $[a,b]$ 连续，$f(a)=A,\ f(b)=B$，则对 $A,B$ 间任一值 $C$，$\exists\xi,\ f(\xi)=C$。

**例题**：求 $\lim_{x\to0}\frac{\tan x-x}{x^2\ln(1+2x)}$。

$$\text{原式}=\lim_{x\to0}\frac{\frac13x^3}{x^2\cdot 2x}=\frac16$$

### 1.7 本章易错点

1. $\lim_{x\to\infty}\frac{\sin x}{x}=0$（不是 $1$，用有界乘无穷小）；
2. 等价无穷小只在乘除替换，加减中误用是最高频错误；
3. 极限 $\lim_{x\to\infty}(1+\frac1x)^x=e$ 与 $\lim_{x\to0}(1+x)^{1/x}=e$ 别混淆；
4. 判断间断点要先看左右极限是否都存在，再分类；
5. 数列 $$\{x_n\}$$ 有界不一定收敛，但收敛一定有界；
6. 洛必达使用前必须验证三个条件，且结果不存在不代表原极限不存在。

---

## 第二章 一元函数微分学

### 2.1 导数概念

**定义**：函数 $f(x)$ 在 $x_0$ 处的导数

$$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$

**左右导数**：

$$f'_-(x_0)=\lim_{h\to0^-}\frac{f(x_0+h)-f(x_0)}h,\quad f'_+(x_0)=\lim_{h\to0^+}\frac{f(x_0+h)-f(x_0)}h$$

$f'(x_0)$ 存在 $\iff f'_-(x_0)=f'_+(x_0)$。

**可导与连续的关系**：可导必连续；<span class="hl-red">连续不一定可导</span>（如 $\lvert x\rvert $ 在 $x=0$ 连续但不可导）。

**导数的几何意义**：$f'(x_0)$ 是曲线 $y=f(x)$ 在 $(x_0,f(x_0))$ 处切线斜率。

- 切线：$y-y_0=f'(x_0)(x-x_0)$；
- 法线：$y-y_0=-\frac{1}{f'(x_0)}(x-x_0)$。

**物理意义**：瞬时速度 $v=s'(t)$，加速度 $a=v'(t)=s''(t)$。

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

### 2.6 本章易错点

1. 分段函数在分段点处必须用左右导数定义求，不能直接求导后代入；
2. 可导必连续，但连续不一定可导；
3. $f'(x_0)=0$ 不一定是极值点（如 $x^3$ 在 $0$ 处）；
4. 拐点是曲线上的点，要写坐标 $(x_0,f(x_0))$，不是只写 $x_0$；
5. 中值定理条件（连续、可导）缺一不可；
6. 极值点可以是不可导点（如 $\lvert x\rvert $ 在 $0$），第一充分条件可判导数不存在的情形。

---

## 第三章 一元函数积分学

### 3.1 不定积分

**原函数**：若 $F'(x)=f(x)$，则 $F(x)$ 是 $f(x)$ 的一个原函数。

**不定积分**：$\int f(x)dx=F(x)+C$。

**性质**：$\int[f(x)\pm g(x)]dx=\int f\,dx\pm\int g\,dx$；$\int kf(x)dx=k\int f\,dx$。

**基本积分公式**：

$$\int x^\mu dx=\frac{x^{\mu+1}}{\mu+1}+C\ (\mu\ne-1),\quad \int\frac1x dx=\ln|x|+C$$

$$\int a^x dx=\frac{a^x}{\ln a}+C,\quad \int e^x dx=e^x+C$$

$$\int\sin x\,dx=-\cos x+C,\quad \int\cos x\,dx=\sin x+C$$

$$\int\sec^2x\,dx=\tan x+C,\quad \int\csc^2x\,dx=-\cot x+C$$

$$\int\sec x\tan x\,dx=\sec x+C,\quad \int\csc x\cot x\,dx=-\csc x+C$$

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

**变限积分求导**：

$$\Phi(x)=\int_a^x f(t)dt\ (f\text{ 连续})\Rightarrow \Phi'(x)=f(x)$$

$$\frac{d}{dx}\int_{\psi(x)}^{\varphi(x)}f(t)dt=f[\varphi(x)]\varphi'(x)-f[\psi(x)]\psi'(x)$$

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

**平面图形面积**：

- 直角坐标：$S=\int_a^b[\,f(x)-g(x)\,]dx$；
- 极坐标：$S=\frac12\int_\alpha^\beta r^2(\theta)d\theta$。

**旋转体体积**：

- 绕 $x$ 轴：$V=\pi\int_a^b f^2(x)dx$；
- 绕 $y$ 轴（柱壳法）：$V=2\pi\int_a^b x\,f(x)dx$。

**平行截面面积已知的立体体积**：$V=\int_a^b A(x)dx$。

**平面曲线弧长**：

$$L=\int_a^b\sqrt{1+y'^2}\,dx,\quad L=\int_\alpha^\beta\sqrt{r^2+r'^2}\,d\theta$$

**旋转曲面面积**：$S=2\pi\int_a^b y\sqrt{1+y'^2}\,dx$。

### 3.5 本章易错点

1. 变限积分求导前先检查被积函数是否含 $x$，含 $x$ 要先提出或换元；
2. 可积不等于有原函数；变上限积分只有在 $f$ 连续时才是原函数，$f$ 有第一类间断点时它只是积分；
3. 定积分换元必须同时换上下限，不必回代；
4. 反常积分要先找瑕点，分段计算，<span class="hl-red">不能直接用牛莱公式</span>；
5. 奇偶性结论<span class="hl-orange">只适用于对称区间</span>；
6. 分部积分选 $u$ 顺序：反、对、幂、三、指（排在前的作 $u$）；
7. $\int\frac1x dx=\ln\lvert x\rvert +C$，<span class="hl-red">绝对值不能漏</span>。

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
3. 抽象复合函数求二阶偏导时，$f_1',f_2'$ 仍是同结构的复合函数，要继续用链式法则；
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

### 5.5 本章易错点

1. 极坐标下面积元素是 <span class="hl-red">$r\,dr\,d\theta$</span>，$r$ 不能漏；
2. 用对称性前必须先验证区域对称性，且被积函数奇偶性要对应；
3. 交换次序要先画区域，不能直接改上下限；
4. 极坐标下 $\theta$ 范围与 $r$ 范围要根据图形确定；
5. 分段函数（含绝对值、max、min）要先分区域去符号。

---

## 第六章 常微分方程

### 6.1 基本概念

**微分方程**：含未知函数导数（或微分）的方程。阶数（最高阶导数阶数）、解、通解（含独立常数个数等于阶数）、特解、初值条件。

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

- $f(x)=e^{\lambda x}P_m(x)$：设 $$y^*=\textcolor{#e05252}{x^k} e^{\lambda x}Q_m(x)$$，$k$ 为 $\lambda$ 作为特征根的重数（$0,1,2$）；
- $f(x)=e^{\lambda x}[P_l(x)\cos\omega x+P_n(x)\sin\omega x]$：设

$$y^*=\textcolor{#e05252}{x^k} e^{\lambda x}[R_m(x)\cos\omega x+S_m(x)\sin\omega x],\quad m=\max(l,n)$$

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

## 附录：高数常用公式速查

**重要极限**：$\frac{\sin x}{x}\to1$；$\left(1+\frac1x\right)^x\to e$。

**等价无穷小（$x\to0$）**：见 1.4。

**泰勒展开**：见 1.5。

**积分公式**：见 3.1。

**方程通解**：见 6.4。

**数二高数题型分布提示**：极限计算（选择/填空高频）、中值定理证明、一元积分计算与应用、多元偏导/全微分、二重积分、微分方程（常与其他章节综合）。

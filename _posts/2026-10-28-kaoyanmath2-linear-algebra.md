---
title: "数二 · 线性代数笔记"
description: 无
date: 2026-10-28 19:30:00 +0800
categories: ["数学二", "线代"]
math: true
---
> 数二线代范围：行列式、矩阵、向量、线性方程组、特征值与特征向量、二次型。
> 每章结构：知识框架 → 定义定理 → 题型方法 → 易错点 → 公式速查。
> 做题前先过开篇两张表：**表 1 把题干翻译成数学语言，表 2 决定第一笔写什么**。

> 全文颜色约定：<span class="hl-red">红色 = 符号 / 易错</span>，<span class="hl-orange">橙色 = 条件 / 区别</span>，<span class="hl-green">绿色 = 结论 / 必背</span>，<span class="hl-blue">蓝色 = 定义 / 基本关系</span>。

---

## 开篇 · 先翻译，再落笔

> 大题卡住，多半不是题型没见过，是**题干那句话没翻译成数学语言**，翻译完了又**不知道第一笔写什么**。
> 所以做题的顺序是：查表 1 定性 → 查表 2 落笔 → 再算。

### 表 1 · 措辞翻译表

| 题干出现 | 翻译成 | 立刻能写 | 别搞混 |
|---|---|---|---|
| A 可经初等**行**变换化为 B | 存在可逆 P，$PA=B$ | $r(A)=r(B)$（必要） | 同秩还不够，行空间也要相同 |
| A 可经初等**列**变换化为 B | 存在可逆 P，$AP=B$ | $r(A)=r(B)$（必要） | 同秩还不够，列空间也要相同；不是相似 |
| A 与 B 等价 | 同上（行、列变换都可以） | $r(A)=r(B)$（同型同秩即可） | 只保秩 |
| A 与 B 相似 | 存在可逆 P，$P^{-1}AP=B$ | 特征值相同（双方可对角化时） | 特征值相同 $\not\Rightarrow$ 相似 |
| A 与 B 合同 | 存在可逆 C，$C^TAC=B$ | 正负惯性指数相同 | 与相似是另一回事 |
| A 与 B 有相同的行空间 | 行向量组等价 | 互相线性表出 | 列空间相同是另一回事 |
| 求满足 $AP=B$ 的**可逆** P | 矩阵方程 | 解 $AX=B$ | A 奇异时不能写 $P=A^{-1}B$ |
| $AX=B$ 有解 | $B=AX$ | $r(A)=r(A\mid B)$ | 光有 $r(A)=r(B)$ 不够 |
| B 的列可由 A 的列表出 | $B=AX$ | X 就是矩阵方程的解 | 行方向反过来是 $A=YB$ |
| $A\sim B$ 必然有 | $A,B$ 相似 | $\lvert A\rvert=\lvert B\rvert$，$\operatorname{tr}(A)=\operatorname{tr}(B)$，$r(A)=r(B)$，特征值相同 | 全是必要条件 |
| $A^T=-A$ | 反对称 | 主对角线全 0，奇数阶 $\lvert A\rvert=0$ | |
| $A^TA=E$ | 正交矩阵 | $A^{-1}=A^T$，$\lvert A\rvert=\pm1$ | |

**行、列别搞反**：

- 初等**行**变换 $=$ 左乘可逆阵：$PA=B$，动的是行，**行空间**保持不变；
- 初等**列**变换 $=$ 右乘可逆阵：$AP=B$，动的是列，**列空间**保持不变。

题干写"列变换"，手上却做行变换，$P$ 的形式会全错。

### 表 2 · 起手式表

| 题面信号 | 第一笔写什么 | 拿到什么 | 陷阱 |
|---|---|---|---|
| 秩、初等变换、矩阵等价、伴随、逆矩阵 | 对 $A$ 做初等行变换化阶梯形，数非零行 | $r(A)$ | 别用列变换 |
| 求逆 | $(A\mid E)\xrightarrow{\text{行变换}}(E\mid A^{-1})$ | $A^{-1}$ | 行、列不能混用 |
| 矩阵方程 $AX=B$ | 写 $(A\mid B)$ 行变换；或把那串列变换的矩阵乘积记下来 | $X$ | A 奇异时 $P$ 不唯一 |
| 方程组 $Ax=b$ | 写增广矩阵行变换，比 $r(A)$ 与 $r(A,b)$ | 有解性与通解 | 自由变量 $n-r(A)$ 个 |
| 含参方程组 | 先看参数在哪：增广列 / 系数阵 / 常数列 | 见 §4.6 | 别一上来求通解 |
| 特征值 | 先写 $\lvert\lambda E-A\rvert=0$，再按降幂展开 | 特征值 | 三阶手算容易漏项 |
| 特征向量 | 解 $(\lambda_iE-A)x=0$，自由变量取 1 | 基础解系 | 特征向量不能取零 |
| 对角化 | 先分重数：代数重数 vs $n-r(\lambda_iE-A)$ | 能否对角化 | 特征值相同不等于相似 |
| 实对称矩阵 | 求特征值 → 不同特征值的向量已经正交 → 只对重根做正交化 | 正交矩阵 $Q$ | 单根只需单位化 |
| 二次型 | 先写对称矩阵 $A$（交叉项系数除 2） | $f=x^TAx$ | $A$ 必须对称 |
| 化标准形 | 正交变换看特征值；配方法要记下变换矩阵 | 标准形、规范形 | 配方法的系数不是特征值 |
| 正定 | 顺序主子式全大于 0，或特征值全大于 0 | 判定 | 只看 $\lvert A\rvert>0$ 不够 |

> 表 2 的用法：命中哪行就照"第一笔"列写，**别跳过第一笔直接想结论**。2018 数二那道题就是卡在没写行变换上——条件想对了，工具没落笔。

---

## 第一章 行列式

### 1.1 行列式的概念

**先备一个工具：排列与逆序数**（定义里那堆正负号全来自这里）

把 $1,2,\dots,n$ 排成一列 $j_1j_2\cdots j_n$，称为一个 $n$ 元**排列**，共有 $n!$ 个。若排列中前面的数大于后面的数，即 $j_s>j_t\ (s<t)$，就说它们构成一个**逆序**；一个排列中逆序的总个数称为**逆序数**，记作 <span class="hl-blue">$\tau(j_1j_2\cdots j_n)$</span>。逆序数为偶数的叫偶排列，为奇数的叫奇排列。

$$\tau(123)=0\ (\text{偶}),\qquad \tau(213)=1\ (\text{奇}),\qquad \tau(321)=3\ (\text{奇})$$

> **【理解】** $\tau$ 只数"大小顺序错了几对"，从左往右逐个往后数即可：$312$ 中 $3>1,\ 3>2$，其余 $1<2$，故 $\tau(312)=2$，是偶排列。
> **对换改变奇偶性**：交换排列中任意两个数，逆序数的奇偶性必然改变——这正是后面"互换两行（列）行列式变号"的根源。

**二阶、三阶**：

$$\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}=a_{11}a_{22}-a_{12}a_{21}$$

三阶展开时，每一项正负号也由列标排列决定：$a_{11}a_{22}a_{33}$ 对应 $123$（$\tau=0$）取正，$a_{12}a_{23}a_{31}$ 对应 $231$（$\tau=2$）取正，$a_{13}a_{22}a_{31}$ 对应 $321$（$\tau=3$）取负。

**$n$ 阶行列式定义**：

$$D=\begin{vmatrix}a_{11}&\cdots&a_{1n}\\\vdots&&\vdots\\a_{n1}&\cdots&a_{nn}\end{vmatrix}=\sum_{j_1j_2\cdots j_n}\textcolor{#e05252}{(-1)^{\tau(j_1j_2\cdots j_n)}}a_{1j_1}a_{2j_2}\cdots a_{nj_n}$$

即取自不同行不同列的 $n$ 个元素乘积的代数和，共 $n!$ 项。逐项拆开看：

| 记号 | 含义 |
| --- | --- |
| <span class="hl-blue">$\sum\limits_{j_1j_2\cdots j_n}$</span> | 对列标 $1,2,\dots,n$ 的全部 $n!$ 个排列求和（行标固定为 $1,2,\dots,n$） |
| <span class="hl-orange">$a_{1j_1}a_{2j_2}\cdots a_{nj_n}$</span> | 第 $i$ 行取第 $j_i$ 列，故每行每列各取一个元素，共 $n$ 个因子 |
| <span class="hl-blue">$\tau(j_1j_2\cdots j_n)$</span> | 列标排列的逆序数 |
| <span class="hl-red">$(-1)^{\tau}$</span> | 该项的符号：$\tau$ 取偶数得 $+1$，取奇数得 $-1$ |

> **【理解】** 定义里只在列标上写 $\tau$，换成按行标数逆序数结果也一样——因为两个排列互为逆排列，逆序数奇偶性相同。这也是 <span class="hl-green">$\lvert A^T\rvert =\lvert A\rvert $</span> 的直观来源。
> 记忆口诀：**"每行每列各取一个，再看列标逆序数定正负"**。<span class="hl-red">$(-1)^{\tau}$</span> 不是"负一的多少次方"这么随意，它是一个由排列奇偶性决定的符号。

### 1.2 行列式的性质

1. 行列式与转置行列式相等：$\lvert A^T\rvert =\lvert A\rvert $；
2. 互换两行（列），行列式变号；
3. 提公因子：$\lvert kA\rvert =k^n\lvert A\rvert $（某一行（列）提 $k$，$kA$ 是所有元素乘 $k$）；
4. 两行（列）成比例（含相同），行列式为 $0$；
5. 若某行（列）元素都是两数之和，可拆成两个行列式之和；
6. 某行（列）的 $k$ 倍加到另一行（列），行列式不变。

### 1.3 展开定理

**余子式**：划去 $a_{ij}$ 所在行、列后剩下的 $n-1$ 阶行列式，记 $M_{ij}$；**代数余子式**：<span class="hl-red">$A_{ij}=\textcolor{#e05252}{(-1)^{i+j}}M_{ij}$</span>。

**展开定理**：

$$D=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in}\quad(\text{按第 }i\text{ 行})$$

$$D=a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj}\quad(\text{按第 }j\text{ 列})$$

**异乘变零**：某行（列）元素与另一行（列）对应代数余子式乘积之和为 $0$。

### 1.4 特殊行列式

**对角、上（下）三角**：

$$\begin{vmatrix}a_{11}&&0\\&\ddots&\\0&&a_{nn}\end{vmatrix}=a_{11}a_{22}\cdots a_{nn}$$

**副对角**：

$$\begin{vmatrix}0&&a_{1n}\\&\ddots&\\a_{n1}&&0\end{vmatrix}=\textcolor{#e05252}{(-1)^{\frac{n(n-1)}2}}a_{1n}a_{2,n-1}\cdots a_{n1}$$

> **【理解】** 指数 $\frac{n(n-1)}2$ 就是列标排列 $n,n-1,\dots,1$ 的<span class="hl-blue">逆序数</span>（$n-1+n-2+\cdots+1$），正好把 1.1 的定义落地。

**拉普拉斯（分块）行列式**：

$$\begin{vmatrix}A_{m\times m}&O\\O&B_{n\times n}\end{vmatrix}=|A||B|,\quad \begin{vmatrix}O&A_{m\times m}\\B_{n\times n}&O\end{vmatrix}=\textcolor{#e05252}{(-1)^{mn}}|A||B|$$

> **【理解】** 副对角分块相当于把 $B$ 的 $n$ 行整体跨过 $A$ 的 $m$ 行，共做 $mn$ 次相邻对换，每次改一次奇偶，故符号为 <span class="hl-red">$(-1)^{mn}$</span>。

**范德蒙行列式**：

$$D_n=\begin{vmatrix}1&1&\cdots&1\\x_1&x_2&\cdots&x_n\\x_1^2&x_2^2&\cdots&x_n^2\\\vdots&\vdots&&\vdots\\x_1^{n-1}&x_2^{n-1}&\cdots&x_n^{n-1}\end{vmatrix}=\prod_{1\le i<j\le n}(x_j-x_i)$$

**递推法**（三对角型等结构）：这类行列式阶数不定，目标是把它化成**只含 $D_{n-1},D_{n-2}$ 的递推式**，再解特征方程求通项。常用手段：按首行（或末行）展开，或用性质 6（某行的倍数加到另一行）把多余项消掉。

以三对角型为例：

$$D_n=\begin{vmatrix}a&b&0&0\\b&a&b&0\\0&b&a&b\\0&0&b&a\end{vmatrix}\quad(n\text{ 阶同理})$$

按第一行展开（$M_{12}=bD_{n-2}$，$A_{12}=-bD_{n-2}$）得

$$D_n=aD_{n-1}-b^2D_{n-2},\qquad D_1=a,\quad D_2=a^2-b^2$$

**特征方程** $\lambda^2-a\lambda+b^2=0$，根 $\lambda_{1,2}=\dfrac{a\pm\sqrt{a^2-4b^2}}2$；再用 $D_1,D_2$ 定出常数 $c_1,c_2$，得通项 $D_n=c_1\lambda_1^n+c_2\lambda_2^n$。

> **【例】** $a=2,b=1$：特征方程 $(\lambda-1)^2=0$ 为重根 $\lambda=1$，故 $D_n=c_1+c_2n$；由 $D_1=2,D_2=3$ 得 $c_1=c_2=1$，即 $D_n=n+1$。
> $a=3,b=1$：$r=\dfrac{3+\sqrt5}2,\ s=\dfrac{3-\sqrt5}2$，则 $D_n=\dfrac{r^{n+1}-s^{n+1}}{\sqrt5}$（$D_1,\dots,D_6=3,8,21,55,144,377$）。

### 1.5 重要结论

<div class="hl-green" markdown="1">

$$|A^T|=|A|,\quad |kA|=k^n|A|,\quad |AB|=|A||B|,\quad |A^{-1}|=|A|^{-1}$$

$$|A^*|=|A|^{n-1},\quad |A|=\prod_{i=1}^n\lambda_i$$

</div>

**爪形（箭形）行列式**：

$$D_n=\begin{vmatrix}a&b&\cdots&b\\b&a&\cdots&b\\\vdots&\vdots&&\vdots\\b&b&\cdots&a\end{vmatrix}=[a+(n-1)b](a-b)^{n-1}$$

**行和相等的行列式**：若 $n$ 阶行列式每行元素之和都等于 $k$，$A_{ij}$ 为元素 $a_{ij}$ 的代数余子式，则

$$|A| = k\left(A_{11}+A_{21}+\cdots+A_{n1}\right)$$

> **【理解】** 把第 $2,3,\dots,n$ 列都加到第 $1$ 列（行列式不变），第 $1$ 列元素全为 $k$；再按第 $1$ 列展开，此时各行的代数余子式与原来相同，得上式。
> 推论：<span class="hl-green">$k$ 是 $A$ 的特征值，特征向量为 $(1,\dots,1)^T$</span>（见 §5.2）。

### 1.6 本章易错点

1. <span class="hl-red">$\lvert kA\rvert =k^n\lvert A\rvert $</span>，不是 $k\lvert A\rvert $；
2. 行列式互换两行变号，展开式代数余子式 <span class="hl-red">$A_{ij}=(-1)^{i+j}M_{ij}$</span> 符号别漏；
3. 拉普拉斯副对角分块带 <span class="hl-red">$(-1)^{mn}$</span>（$mn$ 次对换），副对角行列式的指数是 <span class="hl-red">$\frac{n(n-1)}2$</span>（逆序数），都别数错；
4. 范德蒙是"列标对应元素、大减小"，顺序看清楚；
5. 抽象行列式先化为 $\lvert A\rvert $ 或特征值的形式，不要硬算。

---

## 第二章 矩阵

### 2.1 矩阵的概念与运算

**矩阵**：$m\times n$ 数表 $A=(a_{ij})_{m\times n}$。

**线性运算**：加法（同型矩阵对应元素相加）、数乘（每元素乘 $k$）。

**矩阵乘法**：$A_{m\times s}B_{s\times n}=C_{m\times n}$，其中

$$c_{ij}=\sum_{k=1}^s a_{ik}b_{kj}$$

注意：

- 矩阵乘法**不满足交换律**：$AB\ne BA$（一般）；
- 不满足消去律：$AB=AC\ \not\Rightarrow\ B=C$；
- $AB=O\ \not\Rightarrow\ A=O$ 或 $B=O$；
- 满足结合律、分配律；
- 若 $AB=BA$，则 <span class="hl-green">$A^kB=BA^k$、$AB^k=BA^k$</span>（可交换矩阵的幂可与对方换位），常用来处理 $A^nB$ 这类式子。

**转置**：$(A^T)^T=A,\ (A+B)^T=A^T+B^T,\ (kA)^T=kA^T$，<span class="hl-red">$(AB)^T=B^TA^T$</span>。

**方阵的幂**：$A^k=A\cdots A$（$k$ 个），$A^kA^l=A^{k+l},\ (A^k)^l=A^{kl}$。

**方阵的行列式**：$\lvert AB\rvert =\lvert A\rvert \lvert B\rvert =\lvert BA\rvert $。

**矩阵的迹**：$\operatorname{tr}(A)=\sum_{i=1}^{n}a_{ii}$（方阵对角线元素之和）。

- $\operatorname{tr}(kA)=k\operatorname{tr}(A)$，$\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$；
- $\operatorname{tr}(AB)=\operatorname{tr}(BA)$（<span class="hl-orange">$A,B$ 同阶方阵</span>）；
- <span class="hl-red">一般 $\operatorname{tr}(AB)\ne\operatorname{tr}(A)\operatorname{tr}(B)$</span>（例 $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$，$B=\begin{pmatrix}1&2\\3&4\end{pmatrix}$：$\operatorname{tr}(AB)=17$，$\operatorname{tr}(A)\operatorname{tr}(B)=25$）；
- $\operatorname{tr}(A^T)=\operatorname{tr}(A)$。

### 2.2 逆矩阵

**定义**：$AB=BA=E$，则 $A$ 可逆，$B=A^{-1}$。

**可逆充要条件**：$\lvert A\rvert \ne0$（即非奇异、满秩）。

**伴随矩阵法**（需 <span class="hl-orange">$\lvert A\rvert \ne0$</span>）：

<div class="hl-green" markdown="1">

$$A^{-1}=\frac{1}{|A|}A^*$$

</div>

**伴随矩阵性质**（$(A^*)^*$、$(A^*)^{-1}$ 两条需 <span class="hl-orange">$\lvert A\rvert \ne0$</span>）：

<div class="hl-green" markdown="1">

$$AA^*=A^*A=|A|E,\quad |A^*|=|A|^{n-1},\quad (A^*)^*=|A|^{n-2}A,\quad (A^*)^{-1}=\frac{A}{|A|}$$

</div>

> **【理解】** 由 $$AA^*=\lvert A\rvert E$$ 两边取行列式：$$\lvert A\rvert \lvert A^*\rvert =\lvert A\rvert ^n$$，故 $$\lvert A^*\rvert =\lvert A\rvert ^{n-1}$$。

**伴随矩阵的秩（三段式，$A$ 为 $n$ 阶）**：

<div class="hl-green" markdown="1">

$$r(A^*)=\begin{cases}n,&r(A)=n\\[2pt]1,&r(A)=n-1\\[2pt]0,&r(A)\le n-2\end{cases}$$

</div>

> **【理解】** $r(A)=n$ 时 $A^*$ 可逆，满秩；$r(A)=n-1$ 时 $AA^*=O$，由 $r(A)+r(A^*)\le n$ 得 $r(A^*)\le1$，又此时至少有一个 $n-1$ 阶非零子式，故 $r(A^*)=1$；$r(A)\le n-2$ 时所有 $n-1$ 阶子式全为 $0$，$A^*=O$。

**可逆矩阵性质**：

$$(A^{-1})^{-1}=A,\quad (kA)^{-1}=\frac1kA^{-1},\quad \textcolor{#e05252}{(AB)^{-1}=B^{-1}A^{-1}},\quad (A^T)^{-1}=(A^{-1})^T,\quad |A^{-1}|=\frac1{|A|}$$

> 注意：$(A+B)^{-1}\ne A^{-1}+B^{-1}$。

**初等变换法**：

$$(A\mid E)\xrightarrow{\text{初等行变换}}(E\mid A^{-1})$$

### 2.3 初等变换与初等矩阵

**初等行（列）变换**：① 互换两行；② 非零数乘某行；③ 某行倍数加到另一行。

**初等矩阵**：单位矩阵经一次初等变换得到的矩阵。

**初等矩阵性质**：

- 初等矩阵均可逆，其逆仍是同类型初等矩阵：

$$E_{ij}^{-1}=E_{ij},\quad E_i^{-1}(k)=E_i\left(\frac1k\right),\quad E_{ij}^{-1}(k)=E_{ij}(-k)$$

- 左乘初等矩阵 $=$ 行变换，右乘 $=$ 列变换；
- 矩阵可逆 $\iff$ 可表示为若干初等矩阵乘积。

**矩阵等价**：$A$ 经有限次初等变换化为 $B$，记 $A\cong B$。充要条件：同型且秩相等（$r(A)=r(B)$）。

### 2.4 矩阵的秩

**定义**：$A$ 中最高阶非零子式的阶数，记 $r(A)$。

**求法**：初等行变换化为行阶梯形，非零行数即为秩。

**秩的公式**：

$$r(A)\le\min\{m,n\}$$

<div class="hl-blue" markdown="1">

$$r(AB)\le\min\{r(A),r(B)\}$$

</div>

$$r(A)+r(B)-n\le r(AB)\le\min\{r(A),r(B)\}$$

<span class="hl-orange">其中 $n$ 为 $A$ 的列数（也是 $B$ 的行数）：设 $A$ 为 $m\times n$，$B$ 为 $n\times p$。</span>

$$r(A+B)\le r(A)+r(B)$$

<div class="hl-blue" markdown="1">

$$r(A)=r(A^T)=r(AA^T)=r(A^TA)$$

</div>

$$r(kA)=r(A)\ (k\ne0)$$

<div class="hl-green" markdown="1">

$$AB=O\Rightarrow r(A)+r(B)\le n$$

</div>

<span class="hl-orange">$n$ 为 $A$ 的列数（也是 $B$ 的行数）</span>。

**满秩**：$r(A)=n$（方阵即可逆）。

> **【理解】** $AB=O$ 时，$B$ 的列向量都在 $Ax=0$ 的解空间中，其维数为 $n-r(A)$，故 $r(B)\le n-r(A)$，即 $r(A)+r(B)\le n$。

### 2.5 分块矩阵

**分块对角**：

$$\begin{pmatrix}A&O\\O&B\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&O\\O&B^{-1}\end{pmatrix}$$

$$\begin{pmatrix}O&A\\B&O\end{pmatrix}^{-1}=\begin{pmatrix}O&B^{-1}\\A^{-1}&O\end{pmatrix}$$

**分块转置**：

$$\begin{pmatrix}A&B\\C&D\end{pmatrix}^T=\begin{pmatrix}A^T&C^T\\B^T&D^T\end{pmatrix}$$

### 2.6 矩阵高次幂（五个思路）

1. **秩 1 矩阵**：$A=\alpha\beta^T$，则 $A^n=[\operatorname{tr}(A)]^{n-1}A$；
2. **分解法**：$A=kE+B$（$B$ 为幂零或秩 1），$A^n=(kE+B)^n$ 用二项式展开；
3. **分块对角**：$$A=\begin{pmatrix}B&O\\O&C\end{pmatrix}$$，$$A^n=\begin{pmatrix}B^n&O\\O&C^n\end{pmatrix}$$；
4. **相似对角化**：$A=P\Lambda P^{-1}$，$A^n=P\Lambda^nP^{-1}$；
5. **找规律**：先算 $A^2,A^3$ 找递推关系。

### 2.7 本章易错点

1. 矩阵乘法不满足交换律、消去律；
2. 伴随矩阵 $$A^*$$ 元素是"代数余子式按列排列"，注意转置；
3. 求逆只能用初等行变换（不能行列混用）；
4. 抽象矩阵求逆优先用定义 $AB=E$ 或因式分解；
5. 秩的不等式中 <span class="hl-red">$AB=O\Rightarrow r(A)+r(B)\le n$</span> 是高频考点，$n$ 是 $B$ 的行数（也是 $A$ 的列数）；
6. 三组"推不出"必须记牢：<span class="hl-red">$A^2=0\not\Rightarrow A=0$</span>（$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$）；<span class="hl-red">$A^2=B^2\not\Rightarrow A=B$</span>（$A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$、$B=-A$，两者平方都是 $E$）；<span class="hl-red">$\lvert A\rvert=\lvert B\rvert\not\Rightarrow A\sim B$</span>。

---

## 第三章 向量

### 3.1 向量的概念与线性组合

**$n$ 维向量**：$\alpha=(a_1,a_2,\cdots,a_n)^T$（列向量）。

**线性组合**：$k_1\alpha_1+k_2\alpha_2+\cdots+k_s\alpha_s$。

**线性表示**：$\beta=k_1\alpha_1+\cdots+k_s\alpha_s$（有解）。

### 3.2 线性相关与线性无关

**定义**：

- 线性相关：存在一组不全为 $0$ 的 $k_1,\cdots,k_s$，使 $k_1\alpha_1+\cdots+k_s\alpha_s=0$；
- 线性无关：上式成立当且仅当 $k_1=\cdots=k_s=0$。

**判别**：

- $m$ 个 $n$ 维向量 $\alpha_1,\cdots,\alpha_m$：
  - $m>n$：<span class="hl-red">必线性相关</span>；
  - $m=n$：行列式 <span class="hl-green">$\lvert \alpha_1\cdots\alpha_n\rvert =0$</span> 相关，$\ne0$ 无关；
  - $m<n$：求秩，$r(A)<m$ 相关，$r(A)=m$ 无关。
- 用定义：设 $k_1\alpha_1+\cdots+k_s\alpha_s=0$，恒等变形推出 $k_i$ 是否全为 $0$。

**重要结论**：

1. 含零向量的向量组必相关；
2. <span class="hl-red">部分相关 $\Rightarrow$ 整体相关；整体无关 $\Rightarrow$ 部分无关</span>；
3. 低维无关 $\Rightarrow$ 高维无关；高维相关 $\Rightarrow$ 低维相关；
4. $\alpha_1,\cdots,\alpha_s$ 无关，$\alpha_1,\cdots,\alpha_s,\beta$ 相关，则 $\beta$ 可由 $\alpha_1,\cdots,\alpha_s$ 唯一表示；
5. 若向量组可由更少向量的向量组线性表示，则该向量组相关。

### 3.3 向量组的秩

**极大线性无关组**：向量组中一个部分组线性无关，且每个向量都能由它表示。

**向量组的秩**：极大无关组所含向量个数。

**矩阵秩 = 行秩 = 列秩**。

**求极大无关组**：初等行变换（不改变列向量线性关系），主元所在列即为极大无关组，其余向量用其表示。

### 3.4 向量组的等价

**定义**：设 $\alpha_1,\dots,\alpha_s$ 与 $\beta_1,\dots,\beta_t$ 是两组 $n$ 维向量，若 $\alpha_1,\dots,\alpha_s$ 均可由 $\beta_1,\dots,\beta_t$ 线性表示，且 $\beta_1,\dots,\beta_t$ 也均可由 $\alpha_1,\dots,\alpha_s$ 线性表示，则称两组向量**等价**，记 $\alpha\cong\beta$。

**判定定理**：

$$\alpha\cong\beta\iff r(\alpha)=r(\beta)=r(\alpha,\beta)$$

其中 $r(\alpha,\beta)$ 指把两组向量拼成一个矩阵所得的秩。

**三条关系**：

1. 等价 $\Rightarrow$ 秩相等；<span class="hl-red">秩相等不一定等价</span>——秩只管"最多能表示出几个"，不管"能不能互相表示"；
2. <span class="hl-green">向量组等价 $\Rightarrow$ 矩阵等价</span>（<span class="hl-orange">两组向量个数相同</span>时才谈得上同型，此时秩也相等）；<span class="hl-red">矩阵等价 $\not\Rightarrow$ 向量组等价</span>——矩阵等价只保证秩相等；
3. 当 $A=(\alpha_1,\dots,\alpha_n)$、$B=(\beta_1,\dots,\beta_n)$ 都是 $n$ 阶可逆矩阵时：<span class="hl-green">$A,B$ 的列向量组等价 $\iff$ 存在可逆矩阵 $P$ 使 $B=PA\iff A,B$ 矩阵等价</span>（左乘关系，见 §2.3）。

> **【理解】** "向量组等价"是**双向**的（互相可表示），"矩阵等价"只是"秩相等"，单向可达：向量组等价 $\Rightarrow$ 矩阵等价，反之不行。
> <span class="hl-orange">别把"左乘"当"相似"</span>：$B=PA$ 是**矩阵等价**（只保秩），$A\sim B$ 是**相似**（§5.3，保特征值），二者不是一回事。反例 $A=E$，$B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$：取 $P=B$ 即 $B=PA$，但 $E$ 与 $B$ 不相似（$B$ 不可对角化）。
> 三种关系一句话：<span class="hl-orange">等价保秩，相似保特征值（行列式、迹），合同保正负惯性指数</span>（合同见 §6.4）。

### 3.5 向量空间（数二了解）

- 基、维数、坐标；
- 过渡矩阵：基变换 $(\beta_1,\cdots,\beta_n)=(\alpha_1,\cdots,\alpha_n)P$；
- 内积：$(\alpha,\beta)=\alpha^T\beta$；正交：$(\alpha,\beta)=0$；
- 规范正交基：两两正交、单位长度。

### 3.6 本章易错点

1. 相关/无关判别要先看向量个数与维数关系；
2. 线性表示对应方程组有解，相关对应齐次有非零解；
3. 求极大无关组用行变换，<span class="hl-red">不能用列变换</span>；
4. 抽象证明优先用定义，"同乘""重组"是常用手法；
5. 两个向量组等价与矩阵等价<span class="hl-orange">不是一回事</span>（见 §3.4）：<span class="hl-green">向量组等价 $\Rightarrow$ 矩阵等价</span>，反向不成立。

---

## 第四章 线性方程组

### 4.1 齐次线性方程组 $Ax=0$

**有解判定**（$A$ 为 $m\times n$）：

- 只有零解 $\iff r(A)=n$；
- 有非零解 $\iff r(A)<n$。

**解的性质**：

- $\xi_1,\xi_2$ 是解 $\Rightarrow \xi_1+\xi_2$ 是解；
- $\xi$ 是解 $\Rightarrow k\xi$ 是解。

**基础解系**：解空间的一组基，含 <span class="hl-green">$n-r(A)$</span> 个线性无关解。

**通解**：

<div class="hl-green" markdown="1">

$$x=k_1\xi_1+k_2\xi_2+\cdots+k_{n-r}\xi_{n-r}$$

</div>

**求通解步骤**：① 行变换化行阶梯；② 写同解方程组、定自由变量；③ 自由变量依次取 $1$（其余为 $0$）求基础解系；④ 写通解。

### 4.2 非齐次线性方程组 $Ax=b$

**有解判定**：

<div class="hl-orange" markdown="1">

$$\begin{cases}\text{无解}\iff r(A)<r(A,b)\\[2pt]\text{唯一解}\iff r(A)=r(A,b)=n\\[2pt]\text{无穷多解}\iff r(A)=r(A,b)<n\end{cases}$$

</div>

**解的性质**：

- $\eta_1,\eta_2$ 是 $Ax=b$ 的解 $\Rightarrow \eta_1-\eta_2$ 是 $Ax=0$ 的解；
- $\xi$ 是 $Ax=0$ 的解、$\eta$ 是 $Ax=b$ 的解 $\Rightarrow \xi+\eta$ 是 $Ax=b$ 的解。

**通解**：

$$x=k_1\xi_1+\cdots+k_{n-r}\xi_{n-r}+\eta^*$$

**推广**：$\eta_1,\cdots,\eta_s$ 是 $Ax=b$ 的解，则 $\sum k_i\eta_i$ 是：

- $Ax=0$ 的解 $\iff \sum k_i=0$；
- $Ax=b$ 的解 $\iff \sum k_i=1$。

### 4.3 矩阵方程 $AX=B$

$A$ 是 $m\times n$，$X$ 是 $n\times p$，$B$ 是 $m\times p$。把 $AX=B$ 按列拆开，就是 $n$ 个右端不同的方程组 $Ax=b_j$。

**有解判定**：

<div class="hl-green" markdown="1">

$$AX=B\ \text{有解}\iff r(A)=r(A\mid B)$$

</div>

也就是 B 的列向量组能由 A 的列向量组线性表出。

<span class="hl-red">光有 $r(A)=r(B)$ 不够</span>：取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$、$B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$，两者秩都是 1，但 B 的第一列 $(0,1)^T$ 不在 A 的列空间 $\mathrm{span}\{(1,0)^T\}$ 里，无解。

**解法一（通用）**：对增广矩阵 $(A\mid B)$ 做初等行变换，系数部分化阶梯形后逐列解，或者通过化简后的两个矩阵的秩依然相等，来求一些参数的值，比如某行必须全0，必须非0等。

- $A$ 可逆：$X=A^{-1}B$，唯一解；
- $A$ 不可逆但有解：解不唯一，通解写成 $X=X_0+NZ$，$X_0$ 是任一组特解，$N$ 的列取自 $Ax=0$ 的基础解系，$Z$ 任意。

**解法二（题干说"可经初等列变换化为 B"时最快）**：

初等列变换就是右乘初等矩阵，所以那串列变换做完后

$$B=A\cdot E_1E_2\cdots E_k=A\cdot P$$

$P=E_1E_2\cdots E_k$ 可逆，**$P$ 本身就是要找的答案**，连方程组都不用解。

**易错点**：

1. $A$ 不可逆时不能写 $P=A^{-1}B$，也不能"除以 $A$"；
2. 题目要"**可逆**矩阵 $P$"时，通解写出来还要**回代验 $\lvert P\rvert\ne0$**；
3. 用解法二时记牢是**列**变换的矩阵之积，写成行的就全错了。

**例 · 2018 数二**

$$A=\begin{pmatrix}1&2&a\\1&3&0\\2&7&-a\end{pmatrix},\qquad B=\begin{pmatrix}1&a&2\\0&1&1\\-1&1&1\end{pmatrix}$$

(1) 求 $a$，使 A 可经初等列变换化为 B。

翻译：初等列变换 $=$ 右乘可逆阵，所以 $B=AP$（$P$ 可逆），$P$ 可逆则 $\lvert B\rvert=\lvert A\rvert\lvert P\rvert$，于是

$$r(A)=r(B)\quad(\text{必要条件})$$

先算 $r(A)$：

$$A\xrightarrow{\text{行变换}}\begin{pmatrix}1&2&a\\0&1&-a\\0&3&-3a\end{pmatrix}\xrightarrow{r_3-3r_2}\begin{pmatrix}1&2&a\\0&1&-a\\0&0&0\end{pmatrix}$$

$r(A)=2$，与 $a$ 无关；于是要 $r(B)=2$，即 $\lvert B\rvert=0$：

$$\lvert B\rvert=1(1-1)-a(0+1)+2(0+1)=2-a=0\ \Rightarrow\ a=2$$

$a=2$ 确实做得到：第 (2) 问求出的 $P$ 可逆且 $AP=B$，而 $P$ 本身能拆成初等矩阵，$B=AP$ 就是那串列变换。

(2) 求可逆矩阵 $P$，使 $AP=B$。

此时 $A$ 奇异，$P$ 不唯一，只能解矩阵方程。增广矩阵行变换：

$$\begin{array}{ccc|ccc}1&2&2&1&2&2\\1&3&0&0&1&1\\2&7&-2&-1&1&1\end{array}\ \xrightarrow{\text{行变换}}\ \begin{array}{ccc|ccc}1&0&6&3&4&4\\0&1&-2&-1&-1&-1\\0&0&0&0&0&0\end{array}$$

设 $P$ 第 $j$ 列第三个元为 $c_j$，回代得

$$P=\begin{pmatrix}3-6c_1&4-6c_2&4-6c_3\\-1+2c_1&-1+2c_2&-1+2c_3\\c_1&c_2&c_3\end{pmatrix}$$

再由 $P$ 可逆定 $c$：第一行加 6 倍第三行、第二行减 2 倍第三行（不改变行列式），得

$$\lvert P\rvert=\begin{vmatrix}3&4&4\\-1&-1&-1\\c_1&c_2&c_3\end{vmatrix}=c_3-c_2\ne0$$

取 $c_1=c_2=0,\ c_3=1$：

$$P=\begin{pmatrix}3&4&-2\\-1&-1&1\\0&0&1\end{pmatrix},\qquad \lvert P\rvert=1\ne0$$

> **【理解】** 两问各考一样东西：(1) 考"初等列变换 $=$ 矩阵等价 $=$ 同秩"，(2) 考"矩阵方程 $AX=B$ $=$ 拿增广矩阵做行变换"。两问都是老套路，坑在 (1) 的措辞——"列变换"这个词平时几乎不出现，翻译成 $AP=B$、$r(A)=r(B)$ 之后就没什么了。

### 4.4 克拉默法则

$n$ 个方程 $n$ 个未知数，<span class="hl-orange">$\lvert A\rvert \ne0$</span> 时唯一解 $x_j=\dfrac{D_j}{D}$，其中 $D_j$ 为 $D$ 中第 $j$ 列换为常数项。

### 4.5 同解与公共解

**$Ax=0$ 与 $Bx=0$ 同解**（等价条件）：

1. $A$ 经初等行变换化为 $B$；
2. $A,B$ 行向量组等价；
3. $$r(A)=r(B)=r\begin{pmatrix}A\\B\end{pmatrix}$$（三秩相等）；
4. 两方程组解集相同；
5. 存在可逆矩阵 $P$，$PA=B$。

**同解方程组**：<span class="hl-green">$Ax=0$ 与 $A^TAx=0$ 同解</span>（因为 $x^TA^TAx=\lVert Ax\rVert^2=0\iff Ax=0$）。

<span class="hl-red">$Ax=0$ 与 $AA^Tx=0$ 一般不同解</span>：$AA^Tx=0\iff A^Tx=0$，说的是 $A^T$ 的核，只有当 $\ker A=\ker A^T$（如 $A$ 对称）时才与 $Ax=0$ 同解。反例 $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$：$Ax=0\Rightarrow x_1=-x_2$，而 $AA^T=\begin{pmatrix}2&0\\0&0\end{pmatrix}\Rightarrow x_1=0$，两者解集不同。

**公共解**：联立 $$\begin{pmatrix}A\\B\end{pmatrix}x=0$$。

- <span class="hl-green">有非零公共解 $\iff r\begin{pmatrix}A\\B\end{pmatrix}<n$</span>；
- 只有零公共解 $\iff r\begin{pmatrix}A\\B\end{pmatrix}=n$。

**解集的包含关系**：$Ax=0$ 的解**都是** $Bx=0$ 的解（即 $\ker A\subseteq\ker B$），<span class="hl-orange">充要条件是</span>

$$r\begin{pmatrix}A\\B\end{pmatrix}=r(A)$$

（此时必有 $r(A)\ge r(B)$）。

> **【理解】** $\ker A=(\text{A 的行空间})^\perp$，故 $\ker A\subseteq\ker B$ 等价于"B 的行向量组被 A 的行向量组张成"，即 $r\begin{pmatrix}A\\B\end{pmatrix}=r(A)$。与"同解"的 $r(A)=r(B)=r\begin{pmatrix}A\\B\end{pmatrix}$ 对照记忆：**同解要两边都含，包含只要一头含**。

### 4.6 题型：含参线性方程组的讨论

**目标**：求参数 $t$ 的取值，使 $Ax=b$ 无解 / 唯一解 / 无穷多解。

**情形一：增广矩阵含参（参数在常数列或增广列）**

1. 对增广矩阵 $(A\mid b)$ 只做**行**变换，把含参的列一起变过去，令参数为 $t$；
2. 看末行：出现 $0=c\ne0$（恒不成立）→ <span class="hl-red">恒无解</span>；出现 $0=k(t)$ → 解 $k(t)=0$ 得"无解"的临界值；
3. 剩下的 $t$ 值再按 $r(A)$ 与 $r(A,b)$ 分类：<span class="hl-green">相等 $\Rightarrow$ 有解</span>，不等 $\Rightarrow$ 无解；
4. 若 $r(A)=r(A,b)<n$ → 无穷多解（自由变量 $n-r(A)$ 个）；若 $r(A)=r(A,b)=n$ → 唯一解。

**情形二：系数矩阵含参（参数在 $A$ 中、$b$ 不含参）**

1. 先算 $\Delta(t)=|A(t)|$：<span class="hl-green">$\Delta(t)\ne0$ 时一律唯一解</span>（对一切使 $\Delta\ne0$ 的 $t$）；
2. 只需再讨论 $\Delta(t)=0$ 的那些 $t$：此时按 $r(A)=r(A,b)$ 判有解性。

**情形三：参数在常数列的"加方程"技巧**

把 $Ax=b+tC$ 改写成两个方程组的联立：

$$\begin{cases}Ax=b\\Cy=-t\end{cases}$$

于是 $Ax=b+tC$ 有解 $\iff$ 联立方程组有解 $\iff r\begin{pmatrix}A\\C\end{pmatrix}=r\begin{pmatrix}A&\mid&b\\C&\mid&-t\end{pmatrix}$。

> **【理解】** 参数在常数列时不要去算 $|A|$，而是把参数"搬"成另一个方程，与原方程组联立后比秩——"比秩"就变成了"方程个数与解的关系"，这是含参方程组最省力的入口。

### 4.7 本章易错点

1. 判定有解看 $r(A)$ 与 $r(A,b)$，<span class="hl-red">不能只看 $r(A)$</span>；
2. 基础解系个数是 <span class="hl-red">$n-r(A)$</span>，不是 $m-r(A)$；
3. 非齐次通解 = 齐次通解 + 一个特解；
4. 同解、公共解、包含关系三类题要分清（见 §4.5）；
5. 若 $Ax=0$ 的解都是 $Bx=0$ 的解，则 $r(A)\ge r(B)$；<span class="hl-orange">充要条件是 $r\begin{pmatrix}A\\B\end{pmatrix}=r(A)$</span>；
6. 含参方程组<span class="hl-red">先比秩、再按 $\Delta(t)$ 分情况</span>，别一上来就求通解（见 §4.6）；
7. <span class="hl-red">$Ax=0$ 只与 $A^TAx=0$ 同解</span>，与 $AA^Tx=0$ <span class="hl-red">一般不同解</span>（后者 $\iff A^Tx=0$）；
8. 矩阵方程 $AX=B$：<span class="hl-red">$A$ 奇异时不能写 $P=A^{-1}B$</span>，解出通解后还要回代验 $\lvert P\rvert\ne0$（见 §4.3）。

---

## 第五章 特征值与特征向量

### 5.1 特征值与特征向量

**定义**：$A\alpha=\lambda\alpha$（$\alpha\ne0$），$\lambda$ 为特征值，$\alpha$ 为特征向量。

**特征方程**：$\lvert \lambda E-A\rvert =0$。

**求法**：① 解 $\lvert \lambda E-A\rvert =0$ 得特征值；② 解 $(\lambda_i E-A)x=0$ 得特征向量。

**性质**：

<div class="hl-green" markdown="1">

$$\sum_{i=1}^n\lambda_i=\sum_{i=1}^n a_{ii}=\operatorname{tr}(A),\qquad \prod_{i=1}^n\lambda_i=|A|$$

$$\sum_{i=1}^n\lambda_i^k=\operatorname{tr}(A^k)\quad (k=1,2,3,\dots)$$

</div>

- 不同特征值对应的特征向量线性无关；
- $k$ 重特征值对应线性无关特征向量不超过 $k$ 个。

**可逆性与特征值**：<span class="hl-green">$A$ 可逆 $\iff$ $A$ 没有零特征值</span>；等价地，<span class="hl-green">$\lvert A\rvert=0\iff A$ 至少有一个特征值 $0$</span>。因为 $\lvert A\rvert=\prod\lambda_i$，只要有一个 $\lambda_i=0$ 行列式就为零。

### 5.2 各种矩阵的特征值

| 矩阵 | $A$ | $A^T$ | $A^{-1}$ | $A^*$ | $A^k$ | $A+kE$ | $f(A)$ | $P^{-1}AP$ |
|---|---|---|---|---|---|---|---|---|
| 特征值 | $\lambda$ | $\lambda$ | $\dfrac1\lambda$ | $\dfrac{\lvert A\rvert }\lambda$ | $\lambda^k$ | $\lambda+k$ | $f(\lambda)$ | $\lambda$ |
| 特征向量 | $\alpha$ | / | $\alpha$ | $\alpha$ | $\alpha$ | $\alpha$ | $\alpha$ | $P^{-1}\alpha$ |

> **【理解】** 均由 $A\alpha=\lambda\alpha$ 推出：左乘 $A^{-1}$ 得 $A^{-1}\alpha=\frac1\lambda\alpha$；左乘 $A^{k-1}$ 得 $A^k\alpha=\lambda^k\alpha$；加 $kE$ 得 $(A+kE)\alpha=(\lambda+k)\alpha$。
> <span class="hl-orange">条件</span>：$A^{-1}$、$A^*$ 两列需 $A$ 可逆（$\lambda\ne0$）；$A^T$ 的特征向量与 $A$ 无确定关系（表中"/"）。

**矩阵函数的行列式**：若 $f$ 是多项式（$f(A)$ 指把 $A$ 代入 $f$ 得到的矩阵，如 $f(A)=A^2-3A+2E$），$f(A)$ 的特征值为 $f(\lambda_i)$，故

<div class="hl-green" markdown="1">

$$|f(A)|=\prod_{i=1}^n f(\lambda_i)$$

</div>

特别地 $|A+kE|=\prod_{i=1}^n(\lambda_i+k)$、$|A^k|=|A|^k$。

- 若 $B=P^{-1}AP$，$A$ 的特征向量为 $\alpha$，则 $B$ 的特征向量为 $P^{-1}\alpha$；
- 若 $A=PBP^{-1}$，$B$ 的特征向量为 $\alpha$，则 $A$ 的特征向量为 $P\alpha$。

**特殊情形**：

- $A$ 每行元素之和为 $a$：$$A\begin{pmatrix}1\\\vdots\\1\end{pmatrix}=a\begin{pmatrix}1\\\vdots\\1\end{pmatrix}$$，即特征值 $a$、特征向量 $(1,\cdots,1)^T$；
- $AB=O$：$B$ 的非零列向量是 $A$ 特征值 $0$ 的特征向量。
- <span class="hl-green">$AB$ 与 $BA$ 有相同的非零特征值</span>（$A$ 为 $m\times n$、$B$ 为 $n\times m$，不一定同阶；零特征值的个数可能不同）；
- <span class="hl-green">$f(A)=O\Rightarrow A$ 的任一特征值都满足 $f(\lambda)=0$</span>；<span class="hl-red">反之不成立</span>（特征值都满足 $f(\lambda)=0$ 推不出 $f(A)=O$，还需可对角化等条件）。

### 5.3 相似矩阵

**定义**：$P^{-1}AP=B$（$P$ 可逆），称 $A\sim B$。相似是等价关系（反身、对称、传递）。

**充要条件**（以下任一）：

1. 存在可逆矩阵 $P$，使 <span class="hl-green">$P^{-1}AP=B$</span>（定义本身）；
2. $A$、$B$ 是同一线性变换在两组基下的矩阵；
3. <span class="hl-orange">双方均可对角化时</span>：特征值相同（含重数），即 $|\lambda E-A|=|\lambda E-B|$；实对称矩阵必可对角化，故只需特征值相同；
4. <span class="hl-orange">一般情形</span>（数一了解）：有相同的 Jordan 标准形（或初等因子相同）。

> **【理解】** $|A|=|B|$、$\operatorname{tr}(A)=\operatorname{tr}(B)$、$r(A)=r(B)$、特征多项式相同、特征值相同，都只是<span class="hl-red">必要非充分</span>。反例：$E$ 与 $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ 特征值全为 $1$，前者可对角化、后者不可，故不相似。

**性质**：

$$|A|=|B|,\quad \operatorname{tr}(A)=\operatorname{tr}(B),\quad r(A)=r(B),\quad |\lambda E-A|=|\lambda E-B|$$

- 特征值相同只是必要，<span class="hl-red">不足以判定相似</span>；
- $A^T\sim B^T,\ A^k\sim B^k,\ A^{-1}\sim B^{-1},\ f(A)\sim f(B)$。

**题型：含参矩阵求参数使 $A\sim B$**（$A$、$B$ 至少一方含未知参数）

相似 $\Rightarrow$ 特征多项式相同，故先用必要条件列方程求出候选值，再回代验证充分性。

1. <span class="hl-green">$\lvert A\rvert=\lvert B\rvert$</span>，得第一个含参等式（恒可用）；
2. 再补第二个等式，两条路二选一：
   - **迹**：<span class="hl-green">$\operatorname{tr}(A)=\operatorname{tr}(B)$</span>。参数出现在对角线上时这个等式才含未知数，优先用；
   - **特征多项式比系数**：分别算 $\lvert\lambda E-A\rvert$、$\lvert\lambda E-B\rvert$，按 $\lambda$ 的降幂展开，对应系数相等。2 阶时 $\lvert\lambda E-A\rvert=\lambda^2-\operatorname{tr}(A)\lambda+\lvert A\rvert$，故行列式 + 迹已穷尽全部系数；3 阶还要再比 $\lambda$ 的一次项（主子式之和）。
3. 解出候选参数后<span class="hl-red">必须回代</span>：双方均可对角化（或实对称）时，特征多项式相同即相似；有一方不可对角化时，还要看几何重数 / Jordan 块是否一致，必要时直接找可逆 $P$ 使 $P^{-1}AP=B$。

> **【理解】** 行列式、迹是特征多项式的两个系数，不是两套独立理论。参数不在对角就别硬用迹，改展开比系数。求得的是必要条件下的候选值，<span class="hl-orange">不回代就当答案会漏掉不相似的情形</span>。

### 5.4 矩阵对角化

**可对角化条件**：

- 充要条件：$A$ 有 $n$ 个线性无关特征向量；
- 充要条件：每个 $k_i$ 重特征值 $\lambda_i$ 满足 <span class="hl-green">$n-r(\lambda_i E-A)=k_i$</span>（即 $r(\lambda_i E-A)=n-k_i$）；
- 充分条件：$A$ 有 $n$ 个不同特征值。

**代数重数与几何重数**：特征值 $\lambda_i$ 在特征方程中的重数叫**代数重数**（即 $k_i$），对应特征子空间的维数叫**几何重数**，即

$$g_i=\dim\ker(\lambda_iE-A)=n-r(\lambda_iE-A)$$

<span class="hl-green">恒有 $1\le g_i\le k_i$</span>（几何重数不超过代数重数）。于是"可对角化"可改述为：<span class="hl-green">每个特征值的几何重数等于代数重数</span>。$g_i<k_i$ 时称 $\lambda_i$ **亏损**，矩阵不可对角化。

**对角化步骤**：

1. 求特征值 $\lambda_1,\cdots,\lambda_n$；
2. 求特征向量 $\alpha_1,\cdots,\alpha_n$；
3. 令 $P=(\alpha_1,\cdots,\alpha_n)$，则 $P^{-1}AP=\Lambda=\operatorname{diag}(\lambda_1,\cdots,\lambda_n)$。

### 5.5 实对称矩阵

**性质**：

1. 特征值全为实数；
2. 不同特征值对应特征向量正交；
3. 必可对角化，且可正交对角化：存在正交矩阵 $Q$，<span class="hl-green">$Q^{-1}AQ=Q^TAQ=\Lambda$</span>。

**正交矩阵 $Q$ 步骤**：

1. 求特征值；
2. 求特征向量；
3. 重根对应的特征向量施密特正交化；
4. 全部单位化；
5. 拼 $Q=(\eta_1,\cdots,\eta_n)$。

**施密特正交化**：

$$\beta_1=\alpha_1$$

$$\beta_2=\alpha_2-\frac{(\alpha_2,\beta_1)}{(\beta_1,\beta_1)}\beta_1$$

$$\beta_3=\alpha_3-\frac{(\alpha_3,\beta_1)}{(\beta_1,\beta_1)}\beta_1-\frac{(\alpha_3,\beta_2)}{(\beta_2,\beta_2)}\beta_2$$

### 5.6 本章易错点

1. 特征向量必须是非零向量；
2. 相似矩阵特征值相同，但特征向量要经过 <span class="hl-red">$P^{-1}$ 变换</span>；两方阵相似的充要<span class="hl-red">不是</span>特征值相同，只有双方都可对角化（含实对称）时才是；含参求值时 $\lvert A\rvert=\lvert B\rvert$ 与 $\operatorname{tr}(A)=\operatorname{tr}(B)$ 只给候选，<span class="hl-red">必须回代</span>；
3. 可对角化判定要看每个特征值的线性无关特征向量个数是否等于重数；
4. 实对称矩阵不同特征值特征向量"正交"，普通矩阵只是<span class="hl-orange">"无关"</span>；
5. 正交化只需对重根特征向量进行，单根特征向量只需单位化。

---

## 第六章 二次型

### 6.1 二次型及其矩阵

**二次型**：

$$f(x_1,\cdots,x_n)=\sum_{i,j}a_{ij}x_ix_j=\textcolor{#3f8fd6}{x^TAx}$$

其中 $A$ 为对称矩阵（$A^T=A$），$a_{ii}$ 为平方项系数，$a_{ij}=a_{ji}$ 为交叉项系数的一半。

**矩阵表示**：$f=x^TAx$，$A$ 唯一，$r(A)$ 为二次型秩。

> **【理解】** $x^TAx$ 中交叉项 $a_{ij}x_ix_j$ 被 $(i,j)$、$(j,i)$ 两处计入，故写矩阵时交叉项系数除以 $2$。

### 6.2 标准形与规范形

**标准形**：只含平方项 $f=d_1y_1^2+\cdots+d_ny_n^2$。

**规范形**：系数为 $1,-1,0$：$f=z_1^2+\cdots+z_p^2-z_{p+1}^2-\cdots-z_r^2$（从标准形提成规范形的步骤见 §6.3 第 6 步）。

**惯性定理**：可逆线性变换下，正、负平方项个数（正惯性指数 $p$、负惯性指数 $q$）不变。

### 6.3 化标准形

**正交变换法**：$x=Qy$，则

<div class="hl-green" markdown="1">

$$f=\lambda_1y_1^2+\lambda_2y_2^2+\cdots+\lambda_ny_n^2$$

</div>

系数即 $A$ 的特征值。

**配方法**：不算特征值，直接对变量配方；标准形的系数是**顺序主子式之比**。

**步骤**：

1. **配 $x_1$**：把含 $x_1$ 的项全收进一个平方

$$f=a_{11}\left(x_1+\frac{a_{12}}{a_{11}}x_2+\cdots+\frac{a_{1n}}{a_{11}}x_n\right)^2+\{\text{不含 }x_1\text{ 的二次式}\}$$

（要 $a_{11}\ne0$）

2. **换元**：令 $y_1=x_1+\frac{a_{12}}{a_{11}}x_2+\cdots+\frac{a_{1n}}{a_{11}}x_n$，剩下的部分记成 $f_1(y_2,\dots,y_n)$；
3. 对 $f_1$ 重复第 1、2 步，依次配出 $y_2,y_3,\dots,y_n$；
4. **记代换**：最后把 $x$ 用 $y$ 反解出来，写成 $x=P_1y$，这个 $P_1$ 就是配方用的变换矩阵（§6.6 搭桥法要用）；
5. 得到标准形 $f=d_1y_1^2+\cdots+d_ny_n^2$，其中 $d_k=\dfrac{\Delta_k}{\Delta_{k-1}}$，$\Delta_k$ 是 $A$ 的 $k$ 阶顺序主子式，$\Delta_0=1$；
6. **提规范形**：$d_i$ 分三堆——正的留下、负的带负号、零的丢掉，再缩放 $z_i=\sqrt{\lvert d_i\rvert}y_i$：

$$f=z_1^2+\cdots+z_p^2-z_{p+1}^2-\cdots-z_r^2$$

$p$ 是正惯性指数，$r-p$ 是负惯性指数。

> **【理解】** 第 5 步的 $d_k=\Delta_k/\Delta_{k-1}$，就是配方剩下那部分（$A$ 的 Schur 补）的对角元。所以**一旦某个 $\Delta_k=0$，这一步就配不下去**（系数为 0），得先用一次合同变换换主元，或调整变量顺序。

**例**：$f=x_1^2+2x_1x_2+2x_1x_3+2x_2^2+4x_2x_3+3x_3^2$，即 $A=\begin{pmatrix}1&1&1\\1&2&2\\1&2&3\end{pmatrix}$。

配 $x_1$：

$$f=(x_1+x_2+x_3)^2+x_2^2+2x_2x_3+2x_3^2$$

再配 $x_2$：

$$f=(x_1+x_2+x_3)^2+(x_2+x_3)^2+x_3^2$$

令 $y_1=x_1+x_2+x_3,\ y_2=x_2+x_3,\ y_3=x_3$，反解得 $x=P_1y$：

$$P_1=\begin{pmatrix}1&-1&0\\0&1&-1\\0&0&1\end{pmatrix},\qquad f=y_1^2+y_2^2+y_3^2$$

回头看顺序主子式：$\Delta_1=1,\ \Delta_2=\begin{vmatrix}1&1\\1&2\end{vmatrix}=1,\ \Delta_3=1$，于是 $d_1=d_2=d_3=1$，与配方结果对得上；规范形为 $z_1^2+z_2^2+z_3^2$，三正，$f$ 正定。

**两种方法怎么挑**：

| | 正交变换法 | 配方法 |
|---|---|---|
| 标准形系数 | $A$ 的特征值 | 顺序主子式之比 $\Delta_k/\Delta_{k-1}$ |
| 代价 | 要算特征值，三阶以上比较烦 | 逐步配方，但**变换矩阵要写出来** |
| 什么时候用 | 要求正交矩阵 $Q$；实对称矩阵 | 合同、正定、惯性指数、搭桥法 |

### 6.4 合同

**定义**：存在可逆矩阵 $C$，$C^TAC=B$，称 $A$ 与 $B$ 合同。

**性质**：

- 合同 $\Rightarrow$ 秩相等、正负惯性指数相同；
- 实对称矩阵合同 $\iff$ 正负惯性指数相同（特征值正负个数相同）。

> **【理解】** <span class="hl-orange">等价保秩，相似保特征值（含行列式、迹），合同保正负惯性指数</span>。

**相似、合同、等价关系**：

- 相似一定等价，合同一定等价；
- 实对称矩阵相似一定合同（特征值相同则正负性相同）；
- 普通矩阵相似与合同没有必然关系。

### 6.5 正定二次型

**定义**：设 $A$ 为<span class="hl-orange">实对称矩阵</span>，若对任意 $x\ne0$，都有 $x^TAx>0$，则称 $A$（及二次型 $f=x^TAx$）**正定**。

> 定义里的实对称前提不能省：非对称矩阵的 $x^TAx$ 只用到了对称部分 $\frac{A+A^T}2$，讨论正定前要先对称化。

**充要条件（任一）**：

1. <span class="hl-green">特征值全为正</span>；
2. 正惯性指数 $p=n=r(A)$；
3. 与单位矩阵合同：$P^TAP=E$；
4. 存在可逆矩阵 $P$，$A=P^TP$；
5. <span class="hl-green">各阶顺序主子式全大于 $0$</span>。

**必要条件**：$a_{ii}>0$；$\lvert A\rvert >0$。

**正定的运算性质**：若 $A$ 正定，则 <span class="hl-green">$A^{-1}$、$A^T$、$kA\ (k>0)$ 都正定</span>；$A,B$ 均正定时 $A+B$ 正定；$A$ 可逆时 $A^TA$ 正定（$x^TA^TAx=\lVert Ax\rVert^2>0,\ x\ne0$）。

**负定**：对任意 $x\ne0$，$x^TAx<0$。等价于 <span class="hl-green">特征值全为负</span>，也等价于 $-A$ 正定。判定用顺序主子式时<span class="hl-orange">符号交替</span>：

$$\Delta_1<0,\ \Delta_2>0,\ \Delta_3<0,\ \cdots,\ (-1)^k\Delta_k>0$$

即奇数阶顺序主子式为负、偶数阶为正。

**半正定**：对任意 $x\ne0$，$x^TAx\ge0$。等价于特征值全 $\ge0$。若进一步存在 $x\ne0$ 使 $x^TAx=0$（此时 $\lvert A\rvert=0$、$A$ 不可逆），称为非严格半正定。<span class="hl-red">各阶顺序主子式全 $\ge0$ 只是半正定的必要条件，不能作为充分判定</span>。

### 6.6 三种搭桥法

**搭桥法 1**：求可逆矩阵 $P$ 使 $P^{-1}AP=B$（两非对角矩阵相似）。

- 分别对角化：$P_1^{-1}AP_1=\Lambda,\ P_2^{-1}BP_2=\Lambda$（$P_1$ 的列是 $A$ 的特征向量）；
- 则 $P=P_1P_2^{-1}$。

**搭桥法 2**：求正交矩阵 $Q$ 使一个二次型变为另一个（合同+正交）。

- 分别正交对角化：$Q_1^TAQ_1=\Lambda,\ Q_2^TBQ_2=\Lambda$；
- 则 $Q=Q_1Q_2^T$。

**搭桥法 3**：求可逆矩阵 $P$ 使 $P^TAP=B$（合同，非正交）。

- 两边都用**配方法**化到**同一个标准形**（系数完全一样；或两边都化到**规范形**，系数只剩 $1,-1,0$，最省事）；
- 记下配方的代换：$x=P_1y$（$f$ 的）、$x=P_2z$（$g$ 的）；
- 则 $P=P_1P_2^{-1}$；
- 两个标准形只差一个正比例时（$g$ 的是 $f$ 的 $\lambda$ 倍），再乘个缩放：$P=\sqrt\lambda\,P_1P_2^{-1}$；
- <span class="hl-red">前置检查</span>：惯性指数（正、负系数个数）必须相同，否则两型不合同，这样的 $P$ 压根不存在。

> **【理解】** 三个 $P$ 的来源不一样：法 1 的 $P_1$ 用**特征向量**拼（配合 $P_1^{-1}AP_1=\Lambda$），法 3 的 $P_1$ 是**配方代换**（$x=P_1y$），别把两者的 $P_1$ 混用；法 2 那个 $Q_1Q_2^T$ 多一个转置，正交阵要正交着拼。

### 6.7 二次型几何应用（数一了解，数二可略）

特征值三正：椭球面；两正一负：单叶双曲面；一正两负：双叶双曲面等。

### 6.8 本章易错点

1. 二次型矩阵必须对称，交叉项系数一半写在对称位置；
2. 正交变换标准形系数是特征值，<span class="hl-orange">配方法不是</span>；
3. <span class="hl-orange">合同看正负惯性指数，相似看特征值</span>；
4. 正定判定顺序主子式是"各阶"都大于零，不是只看 $\lvert A\rvert $；
5. 搭桥法中乘法顺序（<span class="hl-red">$P_1P_2^{-1}$</span> 或 <span class="hl-red">$Q_1Q_2^T$</span>）不能反；
6. 配方法要把变换矩阵 <span class="hl-orange">$x=P_1y$</span> 写出来（§6.6 搭桥法 3 靠它拼 $P$），配到某个 $\Delta_k=0$ 配不下去时要换主元；
7. 合同题先比惯性指数，正负个数不同就没有 $P$（§6.6）；
8. 负定的顺序主子式是<span class="hl-red">符号交替</span>（奇数阶 $<0$、偶数阶 $>0$），别照搬正定的全大于 $0$；
9. 半正定看特征值全 $\ge0$ 且 $\lvert A\rvert=0$，<span class="hl-orange">顺序主子式全 $\ge0$ 只是必要</span>；正定定义要先有实对称前提。

---

## 附录：线代思维定势速查

**"看到……就想到……"**：

1. 看到 $AB=O$：$r(A)+r(B)\le n$（$n$ 为 $A$ 的列数、$B$ 的行数）；$B$ 的列向量是 $Ax=0$ 的解；<span class="hl-orange">$A,B$ 为 $n$ 阶方阵时</span>，$A$ 有特征值 $0$；
2. 看到 $AB=C$：$C$ 的列向量可由 $A$ 的列向量表示，$C$ 的行向量可由 $B$ 的行向量表示；
3. 看到 $AB=E$：$A,B$ 均可逆，$A^{-1}=B,\ B^{-1}=A$；
4. 看到 $A$ 为正交矩阵：$A^{-1}=A^T$，<span class="hl-red">$\lvert A\rvert =\pm1$</span>，特征值 $\pm1$，行列向量两两正交且单位化；
5. 看到 $A^T=-A$（反对称）：主对角线为 $0$，奇数阶时 $\lvert A\rvert =0$；
6. 看到秩 1：$A=\alpha\beta^T$，$A^n=[\operatorname{tr}(A)]^{n-1}A$，特征值 $\operatorname{tr}(A),0,\cdots,0$；
7. 看到 $AA^T$、$A^TA$：必为对称阵，与 $A$ 同秩，非零特征值相同；<span class="hl-green">$A^TAx=0\iff Ax=0$</span>（与 $Ax=0$ 同解），<span class="hl-red">但 $AA^Tx=0\iff A^Tx=0$</span>，一般不与 $Ax=0$ 同解；
8. 看到每行元素之和为 $a$：特征值 $a$、特征向量 $(1,\cdots,1)^T$；
9. 看到 $A\sim B$：行列式、迹、秩、特征值全相等；
10. 看到实对称矩阵：特征值实数、特征向量正交、必可正交对角化；
11. 看到二次型：先写对称矩阵，正交变换看特征值，合同看正负惯性指数，正定看顺序主子式；
12. 看到伴随 $A^*$：先判 $r(A)$，$n$、$n-1$、$\le n-2$ 对应 $r(A^*)=n,1,0$；特征值 $\frac{\lvert A\rvert}{\lambda}$（$A$ 可逆）；
13. 看到 $f(A)=O$：特征值都满足 $f(\lambda)=0$；
14. 看到 $AB$、$BA$：非零特征值相同。

**秩的核心公式**：

$$r(A)=r(A^T)=r(AA^T)=r(A^TA),\quad r(AB)\le\min\{r(A),r(B)\}$$

$$r(A)+r(B)-n\le r(AB),\quad AB=O\Rightarrow r(A)+r(B)\le n$$

$$r(A^*)=\begin{cases}n,&r(A)=n\\1,&r(A)=n-1\\0,&r(A)\le n-2\end{cases}$$

**数二线代题型分布提示**：行列式/矩阵小题、向量相关性、方程组求解（大题高频）、特征值与对角化（大题高频）、二次型标准形与正定（常与特征值综合）。

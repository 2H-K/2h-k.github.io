---
title: "数二 · 线性代数笔记"
description: 无
date: 2026-10-28 19:30:00 +0800
categories: ["数学二", "线代"]
math: true
---
> 数二线代范围：行列式、矩阵、向量、线性方程组、特征值与特征向量、二次型。
> 每章结构：知识框架 → 定义定理 → 题型方法 → 易错点 → 公式速查。

---

## 第一章 行列式

### 1.1 行列式的概念

**二阶、三阶**：

$$\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}=a_{11}a_{22}-a_{12}a_{21}$$

**$n$ 阶行列式定义**：

$$D=\begin{vmatrix}a_{11}&\cdots&a_{1n}\\\vdots&&\vdots\\a_{n1}&\cdots&a_{nn}\end{vmatrix}=\sum_{j_1j_2\cdots j_n}(-1)^{\tau(j_1j_2\cdots j_n)}a_{1j_1}a_{2j_2}\cdots a_{nj_n}$$

即取自不同行不同列的 $n$ 个元素乘积的代数和，共 $n!$ 项。

### 1.2 行列式的性质

1. 行列式与转置行列式相等：$\lvert A^T\rvert =\lvert A\rvert $；
2. 互换两行（列），行列式变号；
3. 提公因子：$\lvert kA\rvert =k^n\lvert A\rvert $（某一行（列）提 $k$，$kA$ 是所有元素乘 $k$）；
4. 两行（列）成比例（含相同），行列式为 $0$；
5. 若某行（列）元素都是两数之和，可拆成两个行列式之和；
6. 某行（列）的 $k$ 倍加到另一行（列），行列式不变。

### 1.3 展开定理

**余子式**：划去 $a_{ij}$ 所在行、列后剩下的 $n-1$ 阶行列式，记 $M_{ij}$；**代数余子式**：$A_{ij}=(-1)^{i+j}M_{ij}$。

**展开定理**：

$$D=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in}\quad(\text{按第 }i\text{ 行})$$

$$D=a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj}\quad(\text{按第 }j\text{ 列})$$

**异乘变零**：某行（列）元素与另一行（列）对应代数余子式乘积之和为 $0$。

### 1.4 特殊行列式

**对角、上（下）三角**：

$$\begin{vmatrix}a_{11}&&0\\&\ddots&\\0&&a_{nn}\end{vmatrix}=a_{11}a_{22}\cdots a_{nn}$$

**副对角**：

$$\begin{vmatrix}0&&a_{1n}\\&\ddots&\\a_{n1}&&0\end{vmatrix}=(-1)^{\frac{n(n-1)}2}a_{1n}a_{2,n-1}\cdots a_{n1}$$

**拉普拉斯（分块）行列式**：

$$\begin{vmatrix}A_{m\times m}&O\\O&B_{n\times n}\end{vmatrix}=|A||B|,\quad \begin{vmatrix}O&A_{m\times m}\\B_{n\times n}&O\end{vmatrix}=(-1)^{mn}|A||B|$$

**范德蒙行列式**：

$$D_n=\begin{vmatrix}1&1&\cdots&1\\x_1&x_2&\cdots&x_n\\x_1^2&x_2^2&\cdots&x_n^2\\\vdots&\vdots&&\vdots\\x_1^{n-1}&x_2^{n-1}&\cdots&x_n^{n-1}\end{vmatrix}=\prod_{1\le i<j\le n}(x_j-x_i)$$

### 1.5 重要结论

$$|A^T|=|A|,\quad |kA|=k^n|A|,\quad |AB|=|A||B|,\quad |A^{-1}|=|A|^{-1}$$

$$|A^*|=|A|^{n-1},\quad |A|=\prod_{i=1}^n\lambda_i$$

**爪形（箭形）、行和相等行列式**：

$$D_n=\begin{vmatrix}a&b&\cdots&b\\b&a&\cdots&b\\\vdots&\vdots&&\vdots\\b&b&\cdots&a\end{vmatrix}=[a+(n-1)b](a-b)^{n-1}$$

### 1.6 本章易错点

1. $\lvert kA\rvert =k^n\lvert A\rvert $，不是 $k\lvert A\rvert $；
2. 行列式互换两行变号，展开式代数余子式 $A_{ij}=(-1)^{i+j}M_{ij}$ 符号别漏；
3. 拉普拉斯副对角分块带 $(-1)^{mn}$；
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
- 满足结合律、分配律。

**转置**：$(A^T)^T=A,\ (A+B)^T=A^T+B^T,\ (kA)^T=kA^T,\ (AB)^T=B^TA^T$。

**方阵的幂**：$A^k=A\cdots A$（$k$ 个），$A^kA^l=A^{k+l},\ (A^k)^l=A^{kl}$。

**方阵的行列式**：$\lvert AB\rvert =\lvert A\rvert \lvert B\rvert =\lvert BA\rvert $。

### 2.2 逆矩阵

**定义**：$AB=BA=E$，则 $A$ 可逆，$B=A^{-1}$。

**可逆充要条件**：$\lvert A\rvert \ne0$（即非奇异、满秩）。

**伴随矩阵法**：

$$A^{-1}=\frac{1}{|A|}A^*$$

**伴随矩阵性质**：

$$AA^*=A^*A=|A|E,\quad |A^*|=|A|^{n-1},\quad (A^*)^*=|A|^{n-2}A,\quad (A^*)^{-1}=\frac{A}{|A|}$$

> **【理解】** 由 $AA^*=\lvert A\rvert E$ 两边取行列式：$\lvert A\rvert \lvert A^*\rvert =\lvert A\rvert ^n$，故 $\lvert A^*\rvert =\lvert A\rvert ^{n-1}$。

**可逆矩阵性质**：

$$(A^{-1})^{-1}=A,\quad (kA)^{-1}=\frac1kA^{-1},\quad (AB)^{-1}=B^{-1}A^{-1},\quad (A^T)^{-1}=(A^{-1})^T,\quad |A^{-1}|=\frac1{|A|}$$

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

$$r(AB)\le\min\{r(A),r(B)\}$$

$$r(A)+r(B)-n\le r(AB)\le\min\{r(A),r(B)\}$$

$$r(A+B)\le r(A)+r(B)$$

$$r(A)=r(A^T)=r(AA^T)=r(A^TA)$$

$$r(kA)=r(A)\ (k\ne0)$$

$$AB=O\Rightarrow r(A)+r(B)\le n$$

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
2. 伴随矩阵 $A^*$ 元素是"代数余子式按列排列"，注意转置；
3. 求逆只能用初等行变换（不能行列混用）；
4. 抽象矩阵求逆优先用定义 $AB=E$ 或因式分解；
5. 秩的不等式中 $AB=O\Rightarrow r(A)+r(B)\le n$ 是高频考点。

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
  - $m>n$：必线性相关；
  - $m=n$：行列式 $\lvert \alpha_1\cdots\alpha_n\rvert =0$ 相关，$\ne0$ 无关；
  - $m<n$：求秩，$r(A)<m$ 相关，$r(A)=m$ 无关。
- 用定义：设 $k_1\alpha_1+\cdots+k_s\alpha_s=0$，恒等变形推出 $k_i$ 是否全为 $0$。

**重要结论**：

1. 含零向量的向量组必相关；
2. 部分相关 $\Rightarrow$ 整体相关；整体无关 $\Rightarrow$ 部分无关；
3. 低维无关 $\Rightarrow$ 高维无关；高维相关 $\Rightarrow$ 低维相关；
4. $\alpha_1,\cdots,\alpha_s$ 无关，$\alpha_1,\cdots,\alpha_s,\beta$ 相关，则 $\beta$ 可由 $\alpha_1,\cdots,\alpha_s$ 唯一表示；
5. 若向量组可由更少向量的向量组线性表示，则该向量组相关。

### 3.3 向量组的秩

**极大线性无关组**：向量组中一个部分组线性无关，且每个向量都能由它表示。

**向量组的秩**：极大无关组所含向量个数。

**矩阵秩 = 行秩 = 列秩**。

**求极大无关组**：初等行变换（不改变列向量线性关系），主元所在列即为极大无关组，其余向量用其表示。

### 3.4 向量空间（数二了解）

- 基、维数、坐标；
- 过渡矩阵：基变换 $(\beta_1,\cdots,\beta_n)=(\alpha_1,\cdots,\alpha_n)P$；
- 内积：$(\alpha,\beta)=\alpha^T\beta$；正交：$(\alpha,\beta)=0$；
- 规范正交基：两两正交、单位长度。

### 3.5 本章易错点

1. 相关/无关判别要先看向量个数与维数关系；
2. 线性表示对应方程组有解，相关对应齐次有非零解；
3. 求极大无关组用行变换，不能用列变换；
4. 抽象证明优先用定义，"同乘""重组"是常用手法；
5. 两个向量组等价与矩阵等价不是一回事。

---

## 第四章 线性方程组

### 4.1 齐次线性方程组 $Ax=0$

**有解判定**（$A$ 为 $m\times n$）：

- 只有零解 $\iff r(A)=n$；
- 有非零解 $\iff r(A)<n$。

**解的性质**：

- $\xi_1,\xi_2$ 是解 $\Rightarrow \xi_1+\xi_2$ 是解；
- $\xi$ 是解 $\Rightarrow k\xi$ 是解。

**基础解系**：解空间的一组基，含 $n-r(A)$ 个线性无关解。

**通解**：

$$x=k_1\xi_1+k_2\xi_2+\cdots+k_{n-r}\xi_{n-r}$$

**求通解步骤**：① 行变换化行阶梯；② 写同解方程组、定自由变量；③ 自由变量依次取 $1$（其余为 $0$）求基础解系；④ 写通解。

### 4.2 非齐次线性方程组 $Ax=b$

**有解判定**：

$$\begin{cases}\text{无解}\iff r(A)<r(A,b)\\[2pt]\text{唯一解}\iff r(A)=r(A,b)=n\\[2pt]\text{无穷多解}\iff r(A)=r(A,b)<n\end{cases}$$

**解的性质**：

- $\eta_1,\eta_2$ 是 $Ax=b$ 的解 $\Rightarrow \eta_1-\eta_2$ 是 $Ax=0$ 的解；
- $\xi$ 是 $Ax=0$ 的解、$\eta$ 是 $Ax=b$ 的解 $\Rightarrow \xi+\eta$ 是 $Ax=b$ 的解。

**通解**：

$$x=k_1\xi_1+\cdots+k_{n-r}\xi_{n-r}+\eta^*$$

**推广**：$\eta_1,\cdots,\eta_s$ 是 $Ax=b$ 的解，则 $\sum k_i\eta_i$ 是：

- $Ax=0$ 的解 $\iff \sum k_i=0$；
- $Ax=b$ 的解 $\iff \sum k_i=1$。

### 4.3 克拉默法则

$n$ 个方程 $n$ 个未知数，$\lvert A\rvert \ne0$ 时唯一解 $x_j=\dfrac{D_j}{D}$，其中 $D_j$ 为 $D$ 中第 $j$ 列换为常数项。

### 4.4 同解与公共解

**$Ax=0$ 与 $Bx=0$ 同解**（等价条件）：

1. $A$ 经初等行变换化为 $B$；
2. $A,B$ 行向量组等价；
3. $$r(A)=r(B)=r\begin{pmatrix}A\\B\end{pmatrix}$$（三秩相等）；
4. 两方程组解集相同；
5. 存在可逆矩阵 $P$，$PA=B$。

**同解方程组**：$Ax=0$ 与 $A^TAx=0$ 同解；$Ax=0$ 与 $AA^Tx=0$ 同解。

**公共解**：联立 $$\begin{pmatrix}A\\B\end{pmatrix}x=0$$。

### 4.5 本章易错点

1. 判定有解看 $r(A)$ 与 $r(A,b)$，不能只看 $r(A)$；
2. 基础解系个数是 $n-r(A)$，不是 $m-r(A)$；
3. 非齐次通解 = 齐次通解 + 一个特解；
4. 同解、公共解、包含关系三类题要分清；
5. 若 $Ax=0$ 的解都是 $Bx=0$ 的解，则 $r(A)\ge r(B)$。

---

## 第五章 特征值与特征向量

### 5.1 特征值与特征向量

**定义**：$A\alpha=\lambda\alpha$（$\alpha\ne0$），$\lambda$ 为特征值，$\alpha$ 为特征向量。

**特征方程**：$\lvert \lambda E-A\rvert =0$。

**求法**：① 解 $\lvert \lambda E-A\rvert =0$ 得特征值；② 解 $(\lambda_i E-A)x=0$ 得特征向量。

**性质**：

$$\sum_{i=1}^n\lambda_i=\sum_{i=1}^n a_{ii}=\operatorname{tr}(A),\qquad \prod_{i=1}^n\lambda_i=|A|$$

- 不同特征值对应的特征向量线性无关；
- $k$ 重特征值对应线性无关特征向量不超过 $k$ 个。

### 5.2 各种矩阵的特征值

| 矩阵 | $A$ | $A^T$ | $A^{-1}$ | $A^*$ | $A^k$ | $A+kE$ | $f(A)$ | $P^{-1}AP$ |
|---|---|---|---|---|---|---|---|---|
| 特征值 | $\lambda$ | $\lambda$ | $\dfrac1\lambda$ | $\dfrac{\lvert A\rvert }\lambda$ | $\lambda^k$ | $\lambda+k$ | $f(\lambda)$ | $\lambda$ |
| 特征向量 | $\alpha$ | / | $\alpha$ | $\alpha$ | $\alpha$ | $\alpha$ | $\alpha$ | $P^{-1}\alpha$ |

> **【理解】** 均由 $A\alpha=\lambda\alpha$ 推出：左乘 $A^{-1}$ 得 $A^{-1}\alpha=\frac1\lambda\alpha$；左乘 $A^{k-1}$ 得 $A^k\alpha=\lambda^k\alpha$；加 $kE$ 得 $(A+kE)\alpha=(\lambda+k)\alpha$。

- 若 $B=P^{-1}AP$，$A$ 的特征向量为 $\alpha$，则 $B$ 的特征向量为 $P^{-1}\alpha$；
- 若 $A=PBP^{-1}$，$B$ 的特征向量为 $\alpha$，则 $A$ 的特征向量为 $P\alpha$。

**特殊情形**：

- $A$ 每行元素之和为 $a$：$$A\begin{pmatrix}1\\\vdots\\1\end{pmatrix}=a\begin{pmatrix}1\\\vdots\\1\end{pmatrix}$$，即特征值 $a$、特征向量 $(1,\cdots,1)^T$；
- $AB=O$：$B$ 的非零列向量是 $A$ 特征值 $0$ 的特征向量。

### 5.3 相似矩阵

**定义**：$P^{-1}AP=B$（$P$ 可逆），称 $A\sim B$。

**性质**：

$$|A|=|B|,\quad \operatorname{tr}(A)=\operatorname{tr}(B),\quad r(A)=r(B),\quad |\lambda E-A|=|\lambda E-B|$$

- 特征值相同（$A\sim B$）；
- $A^T\sim B^T,\ A^k\sim B^k,\ A^{-1}\sim B^{-1},\ f(A)\sim f(B)$。

### 5.4 矩阵对角化

**可对角化条件**：

- 充要条件：$A$ 有 $n$ 个线性无关特征向量；
- 充要条件：每个 $k_i$ 重特征值 $\lambda_i$ 满足 $n-r(\lambda_i E-A)=k_i$（即 $r(\lambda_i E-A)=n-k_i$）；
- 充分条件：$A$ 有 $n$ 个不同特征值。

**对角化步骤**：

1. 求特征值 $\lambda_1,\cdots,\lambda_n$；
2. 求特征向量 $\alpha_1,\cdots,\alpha_n$；
3. 令 $P=(\alpha_1,\cdots,\alpha_n)$，则 $P^{-1}AP=\Lambda=\operatorname{diag}(\lambda_1,\cdots,\lambda_n)$。

### 5.5 实对称矩阵

**性质**：

1. 特征值全为实数；
2. 不同特征值对应特征向量正交；
3. 必可对角化，且可正交对角化：存在正交矩阵 $Q$，$Q^{-1}AQ=Q^TAQ=\Lambda$。

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
2. 相似矩阵特征值相同，但特征向量经过 $P^{-1}$ 变换；
3. 可对角化判定要看每个特征值的线性无关特征向量个数是否等于重数；
4. 实对称矩阵不同特征值特征向量"正交"，普通矩阵只是"无关"；
5. 正交化只需对重根特征向量进行，单根特征向量只需单位化。

---

## 第六章 二次型

### 6.1 二次型及其矩阵

**二次型**：

$$f(x_1,\cdots,x_n)=\sum_{i,j}a_{ij}x_ix_j=x^TAx$$

其中 $A$ 为对称矩阵（$A^T=A$），$a_{ii}$ 为平方项系数，$a_{ij}=a_{ji}$ 为交叉项系数的一半。

**矩阵表示**：$f=x^TAx$，$A$ 唯一，$r(A)$ 为二次型秩。

> **【理解】** $x^TAx$ 中交叉项 $a_{ij}x_ix_j$ 被 $(i,j)$、$(j,i)$ 两处计入，故写矩阵时交叉项系数除以 $2$。

### 6.2 标准形与规范形

**标准形**：只含平方项 $f=d_1y_1^2+\cdots+d_ny_n^2$。

**规范形**：系数为 $1,-1,0$：$f=z_1^2+\cdots+z_p^2-z_{p+1}^2-\cdots-z_r^2$。

**惯性定理**：可逆线性变换下，正、负平方项个数（正惯性指数 $p$、负惯性指数 $q$）不变。

### 6.3 化标准形

**正交变换法**：$x=Qy$，则

$$f=\lambda_1y_1^2+\lambda_2y_2^2+\cdots+\lambda_ny_n^2$$

系数即 $A$ 的特征值。

**配方法**：依次对变量配方，得到可逆线性变换（配方法标准形系数一般不是特征值）。

### 6.4 合同

**定义**：存在可逆矩阵 $C$，$C^TAC=B$，称 $A$ 与 $B$ 合同。

**性质**：

- 合同 $\Rightarrow$ 秩相等、正负惯性指数相同；
- 实对称矩阵合同 $\iff$ 正负惯性指数相同（特征值正负个数相同）。

> **【理解】** 等价保秩，相似保特征值（含行列式、迹），合同保正负惯性指数。

**相似、合同、等价关系**：

- 相似一定等价，合同一定等价；
- 实对称矩阵相似一定合同（特征值相同则正负性相同）；
- 普通矩阵相似与合同没有必然关系。

### 6.5 正定二次型

**定义**：对任意 $x\ne0$，$x^TAx>0$。

**充要条件（任一）**：

1. 特征值全为正；
2. 正惯性指数 $p=n=r(A)$；
3. 与单位矩阵合同：$P^TAP=E$；
4. 存在可逆矩阵 $P$，$A=P^TP$；
5. 各阶顺序主子式全大于 $0$。

**必要条件**：$a_{ii}>0$；$\lvert A\rvert >0$。

### 6.6 三种搭桥法

**搭桥法 1**：求可逆矩阵 $P$ 使 $P^{-1}AP=B$（两非对角矩阵相似）。

- 分别对角化：$P_1^{-1}AP_1=\Lambda,\ P_2^{-1}BP_2=\Lambda$；
- 则 $P=P_1P_2^{-1}$。

**搭桥法 2**：求正交矩阵 $Q$ 使一个二次型变为另一个（合同+正交）。

- 分别正交对角化：$Q_1^TAQ_1=\Lambda,\ Q_2^TBQ_2=\Lambda$；
- 则 $Q=Q_1Q_2^T$。

**搭桥法 3**：求可逆矩阵 $P$ 使一个二次型变为另一个（合同，非正交）。

- 两二次型都用配方法化到**相同标准形**（第一个写标准形、第二个写非标准形）；
- 则 $P=P_1P_2^{-1}$。

### 6.7 二次型几何应用（数一了解，数二可略）

特征值三正：椭球面；两正一负：单叶双曲面；一正两负：双叶双曲面等。

### 6.8 本章易错点

1. 二次型矩阵必须对称，交叉项系数一半写在对称位置；
2. 正交变换标准形系数是特征值，配方法不是；
3. 合同看正负惯性指数，相似看特征值；
4. 正定判定顺序主子式是"各阶"都大于零，不是只看 $\lvert A\rvert $；
5. 搭桥法中乘法顺序（$P_1P_2^{-1}$ 或 $Q_1Q_2^T$）不能反。

---

## 附录：线代思维定势速查

**"看到……就想到……"**：

1. 看到 $AB=O$：$r(A)+r(B)\le n$；$B$ 的列向量是 $Ax=0$ 的解；$A$ 有特征值 $0$；
2. 看到 $AB=C$：$C$ 的列向量可由 $A$ 的列向量表示，$C$ 的行向量可由 $B$ 的行向量表示；
3. 看到 $AB=E$：$A,B$ 均可逆，$A^{-1}=B,\ B^{-1}=A$；
4. 看到 $A$ 为正交矩阵：$A^{-1}=A^T$，$\lvert A\rvert =\pm1$，特征值 $\pm1$，行列向量两两正交且单位化；
5. 看到 $A^T=-A$（反对称）：主对角线为 $0$，奇数阶时 $\lvert A\rvert =0$；
6. 看到秩 1：$A=\alpha\beta^T$，$A^n=[\operatorname{tr}(A)]^{n-1}A$，特征值 $\operatorname{tr}(A),0,\cdots,0$；
7. 看到 $AA^T$、$A^TA$：必为对称阵，与 $A$ 同秩，与 $Ax=0$ 同解，非零特征值相同；
8. 看到每行元素之和为 $a$：特征值 $a$、特征向量 $(1,\cdots,1)^T$；
9. 看到 $A\sim B$：行列式、迹、秩、特征值全相等；
10. 看到实对称矩阵：特征值实数、特征向量正交、必可正交对角化；
11. 看到二次型：先写对称矩阵，正交变换看特征值，合同看正负惯性指数，正定看顺序主子式。

**秩的核心公式**：

$$r(A)=r(A^T)=r(AA^T)=r(A^TA),\quad r(AB)\le\min\{r(A),r(B)\}$$

$$r(A)+r(B)-n\le r(AB),\quad AB=O\Rightarrow r(A)+r(B)\le n$$

**数二线代题型分布提示**：行列式/矩阵小题、向量相关性、方程组求解（大题高频）、特征值与对角化（大题高频）、二次型标准形与正定（常与特征值综合）。

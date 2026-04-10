---
layout: default
title: "index"
---

# Notation and Simple Matrix Algebra
# 표기법 및 간단한 행렬 대수

Choosing notation for a textbook is always a difficult task.
교과서의 표기법을 선택하는 것은 항상 어려운 작업입니다.
For the most part we adopt the same notational conventions as ESL.
대부분의 경우 우리는 ESL과 동일한 표기 규칙을 채택합니다.

We will use $n$ to represent the number of distinct data points, or observations, in our sample.
우리는 샘플에서 고유한 데이터 포인트 또는 관찰(측정) 값의 수를 나타내기 위해 $n$을 사용할 것입니다.
We will let $p$ denote the number of variables that are available for use in making predictions.
우리는 예측 공간을 만드는 데 사용할 수 있는 변수의 수를 나타내기 위해 $p$를 둘 것입니다.
For example, the `Wage` data set consists of 11 variables for 3,000 people, so we have $n = 3,000$ observations and $p = 11$ variables (such as year, age, race, and more).
예를 들어 `Wage` 데이터 세트는 3,000명에 대한 11개의 변수로 구성되므로, 우리에겐 관찰값 $n = 3,000$과 변수 $p = 11$(연도, 나이, 인종 등)개가 있습니다.
Note that throughout this book, we indicate variable names using colored font: `Variable Name`.
이 책 전체에 걸쳐 색상이 지정된 글꼴을 사용하여 변수 이름을 나타냅니다: `Variable Name`.

In some examples, $p$ might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.
일부 예에서 $p$는 수천 또는 수백만 단위와 같이 상당히 클 수 있습니다. 이러한 상황은 예를 들면 최신의 생물학적 데이터 또는 웹 기반 광고 데이터를 분석할 때 꽤 자주 발생합니다.

In general, we will let $x_{ij}$ represent the value of the $j$th variable for the $i$th observation, where $i = 1, 2, \dots , n$ and $j = 1, 2, \dots , p$.
일반적으로 우리는 $x_{ij}$가 $i$번째 관찰에 대한 $j$번째 변수의 값을 나타내게 할 것이며, 여기서 $i = 1, 2, \dots , n$ 이고 $j = 1, 2, \dots , p$ 입니다.
Throughout this book, $i$ will be used to index the samples or observations (from 1 to $n$) and $j$ will be used to index the variables (from 1 to $p$).
이 책을 통틀어 $i$는 샘플 또는 관찰값(1에서 $n$까지)을 인덱싱하는 데 사용되고 $j$는 변수(1에서 $p$까지)를 인덱싱하는 데 사용됩니다.
We let $\mathbf{X}$ denote an $n \times p$ matrix whose $(i, j)$th element is $x_{ij}$. That is,
우리가 $(i, j)$번째 요소가 $x_{ij}$인 $n \times p$차원의 행렬 $\mathbf{X}$를 표시할 때, 즉:

$$
\mathbf{X} = 
\begin{pmatrix}
x_{11} & x_{12} & \dots & x_{1p} \\
x_{21} & x_{22} & \dots & x_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
x_{n1} & x_{n2} & \dots & x_{np}
\end{pmatrix}.
$$

For readers who are unfamiliar with matrices, it is useful to visualize $\mathbf{X}$ as a spreadsheet of numbers with $n$ rows and $p$ columns.
행렬에 익숙하지 않은 독자의 경우, $\mathbf{X}$를 $n$개의 행과 $p$개의 열로 구성된 숫자의 스프레드시트로 시각화하면 유용합니다.

At times we will be interested in the rows of $\mathbf{X}$, which we write as $x_1, x_2, \dots , x_n$.
때때로 우리는 $x_1, x_2, \dots , x_n$으로 작성하는 $\mathbf{X}$의 행에 관심을 가질 것입니다.
Here $x_i$ is a vector of length $p$, containing the $p$ variable measurements for the $i$th observation. That is,
여기서 $x_i$는 해당 $i$번째 단일 관찰값에 대해 $p$개 변수로 구성된 길이 $p$의 벡터입니다. 즉:

$$
x_i = 
\begin{pmatrix}
x_{i1} \\
x_{i2} \\
\vdots \\
x_{ip}
\end{pmatrix}. \quad \text{(1.1)}
$$

(Vectors are by default represented as columns.)
(벡터는 기본적으로 열로 표현됩니다.)
For example, for the `Wage` data, $x_i$ is a vector of length 11, consisting of year, age, race, and other values for the $i$th individual.
예를 들어 `Wage` 데이터의 경우, $x_i$는 $i$번째 개인의 연도, 나이, 인종 및 기타 값들로 구성된 길이가 11인 벡터입니다.
At other times we will instead be interested in the columns of $\mathbf{X}$, which we write as $\mathbf{x}_1, \mathbf{x}_2, \dots , \mathbf{x}_p$.
또 다른 때에 우리는 $\mathbf{x}_1, \mathbf{x}_2, \dots , \mathbf{x}_p$와 같이 표기하는 대신 $\mathbf{X}$의 열에 관심을 가질 것입니다.
Each is a vector of length $n$. That is,
각각은 길이 $n$의 벡터입니다. 즉:

$$
\mathbf{x}_j = 
\begin{pmatrix}
x_{1j} \\
x_{2j} \\
\vdots \\
x_{nj}
\end{pmatrix}.
$$

For example, for the `Wage` data, $\mathbf{x}_1$ contains the $n = 3,000$ values for `year`.
예를 들어 `Wage` 데이터의 경우, $\mathbf{x}_1$은 `year`에 대한 $n = 3,000$개의 모든 값을 포함합니다.

Using this notation, the matrix $\mathbf{X}$ can be written as
이 표기법을 사용하면 행렬 $\mathbf{X}$는 다음과 같이 쓸 수 있습니다:

$$
\mathbf{X} = \begin{pmatrix} \mathbf{x}_1 & \mathbf{x}_2 & \dots & \mathbf{x}_p \end{pmatrix},
$$

or
또는,

$$
\mathbf{X} = 
\begin{pmatrix}
x_1^T \\
x_2^T \\
\vdots \\
x_n^T
\end{pmatrix}.
$$

The $^T$ notation denotes the transpose of a matrix or vector. So, for example,
$^T$ 표기는 행렬 또는 벡터의 전치를 나타냅니다. 따라서 예를 들어:

$$
\mathbf{X}^T = 
\begin{pmatrix}
x_{11} & x_{21} & \dots & x_{n1} \\
x_{12} & x_{22} & \dots & x_{n2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1p} & x_{2p} & \dots & x_{np}
\end{pmatrix},
$$

while
반면에,

$$
x_i^T = \begin{pmatrix} x_{i1} & x_{i2} & \dots & x_{ip} \end{pmatrix}.
$$

We use $y_i$ to denote the $i$th observation of the variable on which we wish to make predictions, such as wage.
우리는 나중의 예측 수행을 희망하는 목적 변수의 $i$번째 관찰(예: wage)을 나타내기 위해 $y_i$를 사용합니다.
Hence, we write the set of all $n$ observations in vector form as
따라서 관찰된 모든 $n$개의 데이터 집합을 다음과 같이 벡터 형태로 나타냅니다:

$$
\mathbf{y} = 
\begin{pmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{pmatrix}.
$$

Then our observed data consists of $\{(x_1, y_1), (x_2, y_2), \dots , (x_n, y_n)\}$, where each $x_i$ is a vector of length $p$. (If $p = 1$, then $x_i$ is simply a scalar.)
그러면 관측된 데이터 세트는 $\{(x_1, y_1), (x_2, y_2), \dots , (x_n, y_n)\}$로 구성되며, 여기서 각 $x_i$는 앞서 언급한 길이 $p$의 벡터입니다. ($p = 1$이면 $x_i$는 단순한 1차원의 스칼라입니다.)

In this text, a vector of length $n$ will always be denoted in lower case bold; e.g.
이 책에서 길이 $n$의 벡터는 항상 소문자 볼드체로 표시됩니다. e.g.

$$
\mathbf{a} = 
\begin{pmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{pmatrix}.
$$

However, vectors that are not of length $n$ (such as feature vectors of length $p$, as in (1.1)) will be denoted in lower case normal font, e.g. $a$.
그러나 $n$의 길이가 아닌 벡터들(예: 앞의 (1.1)에서와 같이 변수 피처의 길이 $p$인 벡터)은 일반 소문자 글꼴(예: $a$)로 표시됩니다.
Scalars will also be denoted in lower case normal font, e.g. $a$.
스칼라 또한 일반 소문자(예: $a$)로 나타냅니다.
In the rare cases in which these two uses for lower case normal font lead to ambiguity, we will clarify which use is intended.
이러한 두 가지 일반 소문자 사용이 모호함을 유발하는 드문 경우, 우리가 의도한 바를 명확하게 다시 설명할 것입니다.
Matrices will be denoted using bold capitals, such as $\mathbf{A}$.
행렬은 볼드체 대문자를 사용하여 나타냅니다(예: $\mathbf{A}$).
Random variables will be denoted using capital normal font, e.g. $A$, regardless of their dimensions.
랜덤 확률 변수는 해당 변수의 차원(dimension)과 관계없이 일반 대문자(예: $A$)를 사용하여 나타냅니다.

Occasionally we will want to indicate the dimension of a particular object.
가끔 특정 객체의 차원을 직접 표시하고 싶을 때가 있습니다.
To indicate that an object is a scalar, we will use the notation $a \in \mathbb{R}$.
객체가 단일한 차원의 스칼라임을 나타내기 위해 식 $a \in \mathbb{R}$을 사용합니다.
To indicate that it is a vector of length $k$, we will use $a \in \mathbb{R}^k$ (or $a \in \mathbb{R}^n$ if it is of length $n$).
길이가 $k$인 벡터임을 나타내기 위해 식 $a \in \mathbb{R}^k$(길이가 $n$인 경우 $a \in \mathbb{R}^n$)를 사용합니다.
We will indicate that an object is an $r \times s$ matrix using $\mathbf{A} \in \mathbb{R}^{r \times s}$.
그리고 객체가 $r \times s$ 특성을 가지는 행렬임을 나타내기 위해 $\mathbf{A} \in \mathbb{R}^{r \times s}$를 사용합니다.

We have avoided using matrix algebra whenever possible.
우리는 이 책을 집필하면서 가능한 한 행렬 대수를 사용하는 것을 피했습니다.
However, in a few instances it becomes too cumbersome to avoid it entirely.
그러나 소수의 몇몇 경우에는 행렬 대수를 완전히 피하는 것이 너무 번거롭고 성가신 일이 될 수 있습니다.
In these rare instances it is important to understand the concept of multiplying two matrices.
이처럼 드문 경우 두 행렬의 곱셈에 대한 주요 개념을 이해하는 것이 중요합니다.
Suppose that $\mathbf{A} \in \mathbb{R}^{r \times d}$ and $\mathbf{B} \in \mathbb{R}^{d \times s}$.
$\mathbf{A} \in \mathbb{R}^{r \times d}$ 이고 $\mathbf{B} \in \mathbb{R}^{d \times s}$ 라고 가정해 봅니다.
Then the product of $\mathbf{A}$ and $\mathbf{B}$ is denoted $\mathbf{AB}$.
그러면 두 $\mathbf{A}$ 와 $\mathbf{B}$ 행렬의 곱은 $\mathbf{AB}$로 표시됩니다.
The $(i, j)$th element of $\mathbf{AB}$ is computed by multiplying each element of the $i$th row of $\mathbf{A}$ by the corresponding element of the $j$th column of $\mathbf{B}$.
$\mathbf{AB}$의 $(i, j)$번째 요소는 $\mathbf{A}$의 $i$번째 행의 각 요소에 대응되는 $\mathbf{B}$의 $j$번째 열의 각 요소를 각각 곱하여 계산됩니다.
That is, $(\mathbf{AB})_{ij} = \sum_{k=1}^d a_{ik}b_{kj}$.
즉 이를 수식으로 하면 $(\mathbf{AB})_{ij} = \sum_{k=1}^d a_{ik}b_{kj}$ 입니다.
As an example, consider
하나의 예로서 다음을 생각해 봅니다:

$$
\mathbf{A} = 
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\quad \text{and} \quad
\mathbf{B} = 
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}.
$$

Then
그러면 두 행렬의 곱셈은 다음의 연산 과정을 거치게 됩니다:

$$
\mathbf{AB} = 
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
= 
\begin{pmatrix}
1 \times 5 + 2 \times 7 & 1 \times 6 + 2 \times 8 \\
3 \times 5 + 4 \times 7 & 3 \times 6 + 4 \times 8
\end{pmatrix}
=
\begin{pmatrix}
19 & 22 \\
43 & 50
\end{pmatrix}.
$$

Note that this operation produces an $r \times s$ matrix.
위의 이 연산은 결과로 $r \times s$ 크기의 행렬을 생성한다는 점에 유의해야 합니다.
It is only possible to compute $\mathbf{AB}$ if the number of columns of $\mathbf{A}$ is the same as the number of rows of $\mathbf{B}$.
행렬 곱 연산은 $\mathbf{A}$ 행렬 열의 수와 $\mathbf{B}$ 행렬 행의 수가 정확히 동일한 경우에만 $\mathbf{AB}$를 계산할 수 있습니다.

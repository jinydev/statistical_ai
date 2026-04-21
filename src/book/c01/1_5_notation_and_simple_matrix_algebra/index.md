---
layout: default
title: "index"
---

[< 1.4 Who Should Read This Book](../1_4_who_should_read_this_book/index.html) | [1.6 Organization Of This Book >](../1_6_organization_of_this_book/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Notation and Simple Matrix Algebra

Choosing notation for a textbook is always a difficult task. For the most part we adopt the same notational conventions as ESL.

We will use $n$ to represent the number of distinct data points, or observations, in our sample. We will let $p$ denote the number of variables that are available for use in making predictions. For example, the `Wage` data set consists of 11 variables for 3,000 people, so we have $n = 3,000$ observations and $p = 11$ variables (such as year, age, race, and more). Note that throughout this book, we indicate variable names using colored font: `Variable Name`.

In some examples, $p$ might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.

In general, we will let $x_{ij}$ represent the value of the $j$th variable for the $i$th observation, where $i = 1, 2, \dots , n$ and $j = 1, 2, \dots , p$. Throughout this book, $i$ will be used to index the samples or observations (from 1 to $n$) and $j$ will be used to index the variables (from 1 to $p$).

We let $\mathbf{X}$ denote an $n \times p$ matrix whose $(i, j)$th element is $x_{ij}$. That is,

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

At times we will be interested in the rows of $\mathbf{X}$, which we write as $x_1, x_2, \dots , x_n$. Here $x_i$ is a vector of length $p$, containing the $p$ variable measurements for the $i$th observation. That is,

$$

x_i =
\begin{pmatrix}
x_{i1} \\
x_{i2} \\
\vdots \\
x_{ip}
\end{pmatrix}. \quad \text{(1.1)}

$$

(Vectors are by default represented as columns.) For example, for the `Wage` data, $x_i$ is a vector of length 11, consisting of year, age, race, and other values for the $i$th individual.

At other times we will instead be interested in the columns of $\mathbf{X}$, which we write as $\mathbf{x}_1, \mathbf{x}_2, \dots , \mathbf{x}_p$. Each is a vector of length $n$. That is,

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

Using this notation, the matrix $\mathbf{X}$ can be written as

$$

\mathbf{X} = \begin{pmatrix} \mathbf{x}_1 & \mathbf{x}_2 & \dots & \mathbf{x}_p \end{pmatrix},

$$

or

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

$$

x_i^T = \begin{pmatrix} x_{i1} & x_{i2} & \dots & x_{ip} \end{pmatrix}.

$$

We use $y_i$ to denote the $i$th observation of the variable on which we wish to make predictions, such as wage. Hence, we write the set of all $n$ observations in vector form as

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

In this text, a vector of length $n$ will always be denoted in lower case bold; e.g.

$$

\mathbf{a} =
\begin{pmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{pmatrix}.

$$

However, vectors that are not of length $n$ (such as feature vectors of length $p$, as in (1.1)) will be denoted in lower case normal font, e.g. $a$. Scalars will also be denoted in lower case normal font, e.g. $a$. In the rare cases in which these two uses for lower case normal font lead to ambiguity, we will clarify which use is intended.

Matrices will be denoted using bold capitals, such as $\mathbf{A}$. Random variables will be denoted using capital normal font, e.g. $A$, regardless of their dimensions.

Occasionally we will want to indicate the dimension of a particular object. To indicate that an object is a scalar, we will use the notation $a \in \mathbb{R}$. To indicate that it is a vector of length $k$, we will use $a \in \mathbb{R}^k$ (or $a \in \mathbb{R}^n$ if it is of length $n$). We will indicate that an object is an $r \times s$ matrix using $\mathbf{A} \in \mathbb{R}^{r \times s}$.

We have avoided using matrix algebra whenever possible. However, in a few instances it becomes too cumbersome to avoid it entirely. In these rare instances it is important to understand the concept of multiplying two matrices. Suppose that $\mathbf{A} \in \mathbb{R}^{r \times d}$ and $\mathbf{B} \in \mathbb{R}^{d \times s}$. Then the product of $\mathbf{A}$ and $\mathbf{B}$ is denoted $\mathbf{AB}$. The $(i, j)$th element of $\mathbf{AB}$ is computed by multiplying each element of the $i$th row of $\mathbf{A}$ by the corresponding element of the $j$th column of $\mathbf{B}$. That is, $(\mathbf{AB})_{ij} = \sum_{k=1}^d a_{ik}b_{kj}$. As an example, consider

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

Note that this operation produces an $r \times s$ matrix. It is only possible to compute $\mathbf{AB}$ if the number of columns of $\mathbf{A}$ is the same as the number of rows of $\mathbf{B}$.

---

## Sub-Chapters


[< 1.4 Who Should Read This Book](../1_4_who_should_read_this_book/index.html) | [1.6 Organization Of This Book >](../1_6_organization_of_this_book/index.html)

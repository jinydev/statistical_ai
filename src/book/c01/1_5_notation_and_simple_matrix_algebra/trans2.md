---
layout: default
title: "trans2"
---

[< 1.4 Who Should Read This Book](../1_4_who_should_read_this_book/trans2.html) | [1.6 Organization Of This Book >](../1_6_organization_of_this_book/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Notation and Simple Matrix Algebra
# 표기법 및 간단한 행렬 대수 (외계어 징크스 타파하기)

Choosing notation for a textbook is always a difficult task.
교과서를 쓰면서 독자들에게 "이 숫자는 이렇게 부르자!" 하고 기호(표기법)를 정하는 건 늘 골머리 앓는 빡센 작업입니다.

For the most part we adopt the same notational conventions as ESL.
그래도 잔머리를 좀 굴려서, 대부분의 기호들은 그 꼰대 같은 벽돌책 형님(ESL)이 정해둔 룰(표기 규칙)을 양심 없이 그대로 훔쳐 와서(채택해서) 쓰기로 했습니다.

We will use $n$ to represent the number of distinct data points, or observations, in our sample.
자, 첫 번째 외계어입니다! 우린 앞으로 우리가 긁어모은 데이터 샘플 안에서 "도대체 사람(또는 물건) 몇 명을 조사했냐?" 하는 그 머릿수(관찰값의 수)를 **'$n$'** 이라는 알파벳으로 뭉뚱그려 부를 겁니다.

We will let $p$ denote the number of variables that are available for use in making predictions.
두 번째! 미래를 점치는 데(예측) 써먹을 수 있는 힌트들! 즉 "나이, 학벌, 성별 같은 힌트 종류가 몇 개나 되냐?" 하는 변수의 개수는 **'$p$'** 라는 놈으로 퉁칠 겁니다.

For example, the `Wage` data set consists of 11 variables for 3,000 people, so we have $n = 3,000$ observations and $p = 11$ variables (such as year, age, race, and more).
예를 들어 볼까요? 앞서 배운 `월급(Wage)` 장난감 데이터는 아저씨 3,000명을 호구 조사해서 11가지 힌트를 캐냈죠. 그러니까 이 경우엔 사람 머릿수 **$n = 3,000$**, 힌트 종류수 **$p = 11$**(연도, 나이, 인종 등등)이 되는 겁니다!

Note that throughout this book, we indicate variable names using colored font: `Variable Name`.
아, 참고로 이 책에서는 눈알 빠지지 말라고 `이렇게 색깔 칠해진 글씨(Variable Name)`가 나오면 무조건 "아, 이건 변수 이름이구나!" 하고 눈치채시면 됩니다.

In some examples, $p$ might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.
어떤 미친 예제에선 이 힌트 개수 $p$ 가 수천 개, 심지어 수백만 개 단위로 뻥튀기되기도 합니다. 요즘 같은 시대엔 암세포 유전자(생물학적 데이터)나 여러분이 인터넷에서 어디 광클했는지(웹 광고 데이터) 추적할 때 아주 흔해 빠지게 일어나는 호러 상황이죠.

In general, we will let $x_{ij}$ represent the value of the $j$th variable for the $i$th observation, where $i = 1, 2, \dots , n$ and $j = 1, 2, \dots , p$.
이제 본격적인 외계어! 일반적으로 **$x_{ij}$** 라는 기호를 쓰면, 이건 "전체 명부에서 **$i$** 번째 줄에 서있는 아저씨의 **$j$** 번째 힌트 값이 뭐냐?"를 가리키는 겁니다. 여기서 $i$ 는 사람 등번호($1$부터 $n$명까지), $j$ 는 힌트 번호($1$부터 $p$개까지)를 나타내죠.

Throughout this book, $i$ will be used to index the samples or observations (from 1 to $n$) and $j$ will be used to index the variables (from 1 to $p$).
그러니까 이 책을 덮을 때까지 **$i$** 라는 알파벳이 보이면 무조건 "아, 이건 사람 숫자 매기는 꼬리표(인덱스)구나!", **$j$** 가 보이면 "이건 힌트 종류 세는 꼬리표구나!" 라고 머리에 박아두세요.

We let $\mathbf{X}$ denote an $n \times p$ matrix whose $(i, j)$th element is $x_{ij}$. That is,
자, 이 자잘한 $x_{ij}$ 찌끄러기들을 다 긁어모아서 거대한 표 지도로 합쳐버리면, 가로 세로가 $n \times p$ 모양인 거대한 뚱땡이 대문자 행렬 **$\mathbf{X}$** 가 탄생합니다. 그림으로 쫙 풀어보면 이렇습니다.

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
행렬 기호만 보면 구역질이 나는 수포자 독자분들! 그냥 마음을 비우고 저 $\mathbf{X}$ 를 우리가 매일 야근하며 보는 가로줄 $n$개(행), 세로줄 $p$개(열) 짜리 '평범한 엑셀(스프레드시트) 창'이라고 머릿속에 그림을 그리세요. 아주 마음이 편해집니다.

At times we will be interested in the rows of $\mathbf{X}$, which we write as $x_1, x_2, \dots , x_n$.
가끔 우리는 그 거대한 엑셀 표에서 '가로 한 줄'만 쏙 빼서 염탐하고 싶어집니다. 이 가로줄들을 편하게 $x_1, x_2, \dots , x_n$ 이라고 부릅시다.

Here $x_i$ is a vector of length $p$, containing the $p$ variable measurements for the $i$th observation. That is,
여기서 $x_i$ 라는 놈은 $i$ 번째 아저씨 한 명의 호구 조사 정보(힌트 $p$개)가 나란히 적힌 길이가 $p$인 한 줄짜리 숫자의 묶음(벡터)입니다. 즉:

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
(주의: 수학쟁이들 똥고집 때문에, 벡터를 빈 종이에 쓸 때는 가로가 아니라 꼬치구이처럼 무조건 '세로 줄(열)'로 길게 늘어뜨려 적는 게 국룰입니다.)

For example, for the `Wage` data, $x_i$ is a vector of length 11, consisting of year, age, race, and other values for the $i$th individual.
방금 배운 걸 써먹어볼까요? `월급` 데이터에서 $x_i$ 는 $i$번째 아저씨 한 명의 나이, 인종, 연도 등 11개 스펙이 세로로 쫙 꽂혀있는 길이가 11짜리 벡터 묶음입니다.

At other times we will instead be interested in the columns of $\mathbf{X}$, which we write as $\mathbf{x}_1, \mathbf{x}_2, \dots , \mathbf{x}_p$.
또 어떤 날에는 반대로 "모든 아저씨들의 나이만 한 번에 뽑아보자!" 하면서 엑셀 표의 '세로 세로줄 한 뭉탱이'만 뽑아 쓰고 싶을 텐데, 이놈들은 특별히 두꺼운 뚱땡이 글씨로 $\mathbf{x}_1, \mathbf{x}_2, \dots , \mathbf{x}_p$ 라고 적습니다.

Each is a vector of length $n$. That is,
이 세로줄 봉은 전체 아저씨 수($n$명)만큼 길쭉하니까 '길이가 $n$인 벡터'가 되겠죠. 열어보면 이렇습니다.

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
아까 그 `월급` 데이터에서 예를 들자면 뚱땡이 $\mathbf{x}_1$ 안에는 3,000명 분의 `연도(year)` 숫자가 징그럽게 3,000개나($n=3,000$) 꽉꽉 채워져 있는 겁니다.

Using this notation, the matrix $\mathbf{X}$ can be written as
지금까지 배운 이 세로줄 몽둥이(벡터)들을 장작 개비 묶듯 옆으로 차곡차곡 이어 붙이면 원래의 거대한 $\mathbf{X}$ 표기법을 이렇게 폼나게 쓸 수 있죠.

$$
\mathbf{X} = \begin{pmatrix} \mathbf{x}_1 & \mathbf{x}_2 & \dots & \mathbf{x}_p \end{pmatrix},
$$

or
아니면 아까 배운 가로줄 $x_i$ (한 명 한 명의 정보) 벡터들을 위에서 아래로 벽돌 쌓듯 층층이 포개서 쓸 수도 있습니다.

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
오잉? 갑자기 우측 상단에 붙은 조그만 $^T$ 딱지는 뭐냐고요? 이건 세로로 긴 걸 가로로 냅다 눕혀버리거나(전치), 가로를 세로로 세워버리는 '마법의 뒤집개' 기호입니다. 그래서 뒤집어보면,

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
반면에, 원래 세로로 꼿꼿하게 서 있던 아저씨 한 명의 정보($x_i$)에 뒤집개($^T$)를 갖다 대면 이렇게 가로로 발라당 누워버립니다.

$$
x_i^T = \begin{pmatrix} x_{i1} & x_{i2} & \dots & x_{ip} \end{pmatrix}.
$$

We use $y_i$ to denote the $i$th observation of the variable on which we wish to make predictions, such as wage.
자, 이제 정답지 나갑니다! 우리가 최종적으로 맞추고 싶어 안달이 난 타겟 정답(예: 월급 액수)은 **$y_i$** 라는 기호로 부릅니다. "$i$번째 아저씨의 진짜 월급 정답"이라는 뜻이죠.

Hence, we write the set of all $n$ observations in vector form as
마찬가지로 이 $n$명 치의 빛나는 정답지 쪼가리들을 쭉 세로로 모아서 벡터 뭉탱이로 만들면 이렇게 뚱땡이 **$\mathbf{y}$** 로 쓸 수 있습니다.

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
그러면 최종적으로 우리가 가진 전체 엑셀 데이터의 정체는 뭠니까? 바로 $n$명의 아저씨마다 **(힌트 뭉탱이, 진짜 정답)** 쌍으로 묶인 $\{(x_1, y_1), (x_2, y_2), \dots , (x_n, y_n)\}$ 과일 바구니 세트인 겁니다. (물론 힌트가 고작 1개($p=1$)뿐이면 $x_i$ 도 벡터가 아니라 그냥 알랑방구 같은 숫자 1개, 즉 스칼라가 되겠죠.)

In this text, a vector of length $n$ will always be denoted in lower case bold; e.g.
이 책의 약속 하나 더! 길이가 아저씨 전체 머릿수인 $n$만큼 징그럽게 길쭉한 벡터는 항상 **'두껍고 뚱뚱한 소문자(볼드체)'** 로 표시합니다. 예컨대 이렇게요.

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
하지만 그딴 거 없이 힌트 개수 $p$ 길이밖에 안 되는 앙증맞은 피처 벡터들(예: 앞서 본 (1.1) 식)은 그냥 다이어트 성공한 날씬한 '일반 소문자(예: $a$)'로 대충 적어버릴 겁니다.

Scalars will also be denoted in lower case normal font, e.g. $a$.
웃긴 건 벡터도 아닌 그냥 맹물 같은 숫자 한 알(스칼라)도 일반 소문자(예: $a$)로 똑같이 표기합니다. 

In the rare cases in which these two uses for lower case normal font lead to ambiguity, we will clarify which use is intended.
"아니 그럼 저게 날씬한 벡터인지 스칼라인지 어떻게 구분함?" 걱정 마세요. 진짜 미치도록 헷갈릴 거 같은 똥망 상황이 간혹 오면, 저희가 그땐 친절하게 텍스트로 "야! 이건 벡터다!" 하고 짚어드릴 테니까요.

Matrices will be denoted using bold capitals, such as $\mathbf{A}$.
명심하세요. 거대한 표 덩어리인 행렬은 무조건 에누리 없이 **'두껍고 뚱뚱한 대문자(예: $\mathbf{A}$)'** 로만 씁니다.

Random variables will be denoted using capital normal font, e.g. $A$, regardless of their dimensions.
반면 통계학에서 제비 뽑기 할 때 나오는 그 신비로운 '확률 변수(Random variable)'라는 놈은 크기(차원)가 어떻든 상관없이 무조건 **다이어트한 얇은 대문자(예: $A$)** 로만 고집합니다. 

Occasionally we will want to indicate the dimension of a particular object.
수포자들 뒷목 잡는 얘기긴 하지만, 가끔은 우리가 눈앞에 있는 이 알파벳 녀석이 "길이가 몇이냐? 행렬이냐 스칼라냐?" 하고 친절하게(혹은 과시용으로) 꼬리표를 달아 차원을 인증해야 할 때가 생깁니다. 

To indicate that an object is a scalar, we will use the notation $a \in \mathbb{R}$.
"이 녀석은 그냥 보잘것없는 실수 숫자 한 개(스칼라)입니다!"라고 티를 내고 싶을 땐 허세 가득하게 $a \in \mathbb{R}$ 이라는 엘프어(수식)를 씁니다.

To indicate that it is a vector of length $k$, we will use $a \in \mathbb{R}^k$ (or $a \in \mathbb{R}^n$ if it is of length $n$).
"오, 요놈은 길이가 무려 $k$짜리인 긴 벡터 꼬치구이입니다!"라고 자랑하려면 $a \in \mathbb{R}^k$ (길이가 $n$이면 $a \in \mathbb{R}^n$) 처럼 머리통에 숫자를 달아줍니다.

We will indicate that an object is an $r \times s$ matrix using $\mathbf{A} \in \mathbb{R}^{r \times s}$.
그리고 "이 뚱뚱한 놈은 가로 $r$번, 세로 $s$번 쪼개진 엑셀 괴물(행렬)이다!"라고 낙인찍으려면 $\mathbf{A} \in \mathbb{R}^{r \times s}$ 처럼 곱하기 기호를 박아버리죠.

We have avoided using matrix algebra whenever possible.
저자로서 다시 한번 피의 맹세를 합니다. 저희는 여러분 뇌가 터지는 걸 막기 위해 책을 쓰는 내내 그 지긋지긋한 '행렬 대수' 외계어를 어떻게든 안 쓰려고 요리조리 피해 다녔습니다.

However, in a few instances it becomes too cumbersome to avoid it entirely.
하지만... 정말 극소수의 상황에서는 행렬을 안 쓰고 설명하려다 보니 오히려 말이 수천 줄로 길어지며 개똥같이(너무 번거롭게) 꼬여버리는 지옥을 맛봤습니다.

In these rare instances it is important to understand the concept of multiplying two matrices.
그래서 이 미치고 팔짝 뛰는 몇몇 희귀한 순간만큼은, 여러분이 '두 행렬을 곱하는 마법(곱셈 개념)' 딱 하나만이라도 제발 이해해 주길 구걸하는 바입니다.

Suppose that $\mathbf{A} \in \mathbb{R}^{r \times d}$ and $\mathbf{B} \in \mathbb{R}^{d \times s}$.
자, 최면을 걸어봅시다. 당신 눈앞에 $\mathbf{A} \in \mathbb{R}^{r \times d}$ 뚱땡이와 $\mathbf{B} \in \mathbb{R}^{d \times s}$ 뚱땡이가 서 있습니다.

Then the product of $\mathbf{A}$ and $\mathbf{B}$ is denoted $\mathbf{AB}$.
둘이 박치기해서 교배(곱셈)시킨 결과물은 심플하게 **$\mathbf{AB}$** 라고 적습니다.

The $(i, j)$th element of $\mathbf{AB}$ is computed by multiplying each element of the $i$th row of $\mathbf{A}$ by the corresponding element of the $j$th column of $\mathbf{B}$.
이 박치기 괴물 $\mathbf{AB}$ 의 몸집에서 $(i, j)$ 번째 속살 세포 하나가 어떻게 태어나느냐? 앞놈 $\mathbf{A}$ 의 **$i$번째 가로줄**을 통째로 뜯어내고, 뒷놈 $\mathbf{B}$ 의 **$j$번째 세로줄**을 통째로 뜯어서, 그 요소들을 순서대로 쪽쪽 곱한 다음 다 터프하게 더해버리면(계산) 됩니다. 

That is, $(\mathbf{AB})_{ij} = \sum_{k=1}^d a_{ik}b_{kj}$.
이걸 토 나오는 수학 기호로 구겨 넣으면 $(\mathbf{AB})_{ij} = \sum_{k=1}^d a_{ik}b_{kj}$ 가 되는 거죠.

As an example, consider
자, 못 믿겠으면 구구단 수준의 예시 하나 들어봅시다. 

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
이 두 꼬맹이 행렬을 박치기시켜 볼까요? 곱셈 연산 발동!

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
짜잔! 곱하기의 끔찍한 혼종 연산이 끝나니까 신기하게도 $r \times s$ 크기의 아주 반듯하고 통통한 새 행렬이 탄생했죠?

It is only possible to compute $\mathbf{AB}$ if the number of columns of $\mathbf{A}$ is the same as the number of rows of $\mathbf{B}$.
근데 마지막 주의 사항 하나! 아무나 데려다가 곱해서 교배시킬 수 있는 게 아닙니다. 가로로 뜯은 앞놈 $\mathbf{A}$ 표의 열 개수와, 세로로 뜯은 뒷놈 $\mathbf{B}$ 표의 행 개수가 **"귀신같이 똑같은 숫자(쌍)"** 일 때만 이 박치기 연산이 허락됩니다! 다르면 에러 뱉고 시위하니까 절대 주의하세요! 

---

## Sub-Chapters (하위 목차)

[< 1.4 Who Should Read This Book](../1_4_who_should_read_this_book/trans2.html) | [1.6 Organization Of This Book >](../1_6_organization_of_this_book/trans2.html)

---
layout: default
title: "trans1"
---

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/trans1.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/trans1.html)

# 3.1.2 Assessing the Accuracy of the Coefficient Estimates

# 3.1.2 계수 추정치의 정확도 평가

Recall from (2.1) that we assume that the _true_ relationship between $X$ and $Y$ takes the form $Y = f(X) + \epsilon$ for some unknown function $f$, where $\epsilon$ is a mean-zero random error term.

(2.1)에서 살펴보았듯이, 우리는 $X$ 와 $Y$ 사이의 _실제(true)_ 관계가 어떤 미지의 함수 $f$ 에 대해 $Y = f(X) + \epsilon$ 의 형태를 띤다고 가정하며, 여기서 $\epsilon$ 은 평균이 0인 무작위 오차항입니다.

If $f$ is to be approximated by a linear function, then we can write this relationship as

만약 $f$ 가 선형 함수로 근사될 수 있다면, 우리는 이 관계를 다음과 같이 쓸 수 있습니다.

$$
Y = \beta_0 + \beta_1 X + \epsilon \quad (3.5)
$$

Here $\beta_0$ is the intercept term—that is, the expected value of $Y$ when $X = 0$, and $\beta_1$ is the slope—the average increase in $Y$ associated with a one-unit increase in $X$.

여기서 $\beta_0$ 는 절편 항입니다—즉 $X = 0$ 일 때 기대되는 $Y$ 의 값입니다, 그리고 $\beta_1$ 은 기울기입니다— $X$ 가 1단위 증가할 때 연관된 $Y$ 의 평균적인 증가량입니다.

The error term is a catch-all for what we miss with this simple model: the true relationship is probably not linear, there may be other variables that cause variation in $Y$, and there may be measurement error.

오차항은 이 단순한 모델에서 우리가 놓치는 모든 것을 포괄합니다: 실제 관계는 아마 선형이 아닐 것이고, $Y$ 에 변동을 유발하는 다른 변수들이 있을 수 있으며, 측정 오차가 존재할 수도 있습니다.

We typically assume that the error term is independent of $X$.

우리는 일반적으로 오차항이 $X$ 와 독립이라고 가정합니다.

**==> picture [284 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 6 7 8 9 β 0 β 1<br>β 0<br> 2.2<br> 2.3<br> 2.15<br> 2.5<br> 2.5<br> 2.11<br> 3<br> 3<br>RSS<br>0.06<br>β 1 0.05<br>0.04<br>0.03<br>**----- End of picture text -----**<br>

**FIGURE 3.2.** _Contour and three-dimensional plots of the RSS on the_ `Advertising` _data, using_ `sales` _as the response and_ `TV` _as the predictor. The red dots correspond to the least squares estimates $\hat{\beta}_0$ and $\hat{\beta}_1$, given by (3.4)._

**FIGURE 3.2.** `Advertising` _데이터에 대한 RSS(잔차 제곱합)의 등고선 및 3차원 플롯이며,_ `sales` _를 응답 변수로,_ `TV` _를 예측 변수로 사용했습니다. 붉은 점들은 (3.4) 식에 의해 주어지는 최소 제곱 추정치 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 에 해당합니다._

The model given by (3.5) defines the _population regression line_, which is the best linear approximation to the true relationship between $X$ and $Y$.$^1$

(3.5) 차식으로 주어지는 모델은 _모집단 회귀선(population regression line)_ 을 정의하며, 이는 $X$ 와 $Y$ 사이의 실제 관계에 대한 가장 훌륭한 선형 근사치입니다.$^1$

The least squares regression coefficient estimates (3.4) characterize the _least squares line_ (3.2).

최소 제곱 회귀 계수 추정치 (3.4) 식은 _최소 제곱선(least squares line)_ 인 (3.2) 식을 특징짓습니다.

The left-hand panel of Figure 3.3 displays these two lines in a simple simulated example.

그림 3.3의 왼쪽 패널은 간단한 시뮬레이션 예제 안에서 이 두 선을 보여줍니다.

We created 100 random $X$s, and generated 100 corresponding $Y$s from the model

우리는 100개의 무작위 $X$ 들을 생성했고, 다음 모델로부터 상응하는 100개의 $Y$ 들을 생성했습니다.

$$
Y = 2 + 3X + \epsilon \quad (3.6)
$$

where $\epsilon$ was generated from a normal distribution with mean zero.

여기서 $\epsilon$ 은 평균이 0인 정규 분포로부터 생성되었습니다.

The red line in the left-hand panel of Figure 3.3 displays the _true_ relationship, $f(X) = 2 + 3X$, while the blue line is the least squares estimate based on the observed data.

그림 3.3의 왼쪽 패널에 있는 붉은 선은 $f(X) = 2 + 3X$ 이라는 _실제(true)_ 관계를 보여주며, 반면 파란 선은 관측된 데이터를 바탕으로 한 최소 제곱 추정치입니다.

The true relationship is generally not known for real data, but the least squares line can always be computed using the coefficient estimates given in (3.4).

실제 관계는 일반적으로 실제 데이터에 대해서는 알려져 있지 않지만, 최소 제곱선은 (3.4) 식에 주어진 계수 추정치를 사용하여 언제나 계산될 수 있습니다.

In other words, in real applications, we have access to a set of observations from which we can compute the least squares line; however, the population regression line is unobserved.

다시 말해, 실제 응용에서는 최소 제곱선을 계산할 수 있는 일련의 관측 집합에 접근할 수 있습니다; 하지만, 모집단 회귀선은 관측되지 않습니다.

In the right-hand panel of Figure 3.3 we have generated ten different data sets from the model given by (3.6) and plotted the corresponding ten least squares lines.

그림 3.3의 오른쪽 패널에서는 식 (3.6) 에 주어진 모델로부터 10개의 다른 데이터 세트를 생성하고 해당되는 10개의 최소 제곱선을 그렸습니다.

Notice that different data sets generated from the same true model result in slightly different least squares lines, but the unobserved population regression line does not change.

동일하게 참인 모델에서 생성된 서로 다른 데이터 세트들은 약간씩 다른 최소 제곱선을 초래하지만, 관측되지 않는 모집단 회귀선은 변하지 않는다는 점에 주목하십시오.

At first glance, the difference between the population regression line and the least squares line may seem subtle and confusing.

언뜻 보기에, 모집단 회귀선과 최소 제곱선 사이의 차이는 미묘하고 혼란스러워 보일 수 있습니다.

We only have one data set, and so what does it mean that two different lines describe the relationship between the predictor and the response?

우리는 데이터 세트를 오직 하나만 가지고 있는데, 그렇다면 두 개의 서로 다른 선이 예측 변수와 응답 변수 간의 관계를 묘사한다는 것은 무엇을 의미할까요?

Fundamentally, the concept of these two lines is a natural extension of the standard statistical approach of using information from a sample to estimate characteristics of a large population.

근본적으로, 이 두 선의 개념은 표본으로부터 얻은 정보를 사용하여 거대한 모집단의 특성을 추정하는 표준 통계적 접근법의 자연스러운 확장입니다.

For example, suppose that we are interested in knowing

예를 들어, 우리가 알고 싶은 것이 있다고 가정해 봅시다.

> 1The assumption of linearity is often a useful working model.

> 1선형성이라는 가정은 종종 유용한 실무 모델입니다.

> However, despite what many textbooks might tell us, we seldom believe that the true relationship is linear.

> 하지만, 많은 교과서들이 우리에게 말해주는 바에도 불구하고, 우리는 실제 참인 관계가 선형일 것이라고 거의 믿지 않습니다.

**==> picture [315 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
−2 −1 0 1 2 −2 −1 0 1 2<br>X X<br>10 10<br>5 5<br>Y Y<br>0 0<br>−5 −5<br>−10 −10<br>**----- End of picture text -----**<br>

**FIGURE 3.3.** _A simulated data set._ Left: _The red line represents the true relationship, f(X) = 2 + 3X, which is known as the population regression line. The blue line is the least squares line; it is the least squares estimate for f(X) based on the observed data, shown in black._ Right: _The population regression line is again shown in red, and the least squares line in dark blue. In light blue, ten least squares lines are shown, each computed on the basis of a separate random set of observations. Each least squares line is different, but on average, the least squares lines are quite close to the population regression line._

**FIGURE 3.3.** _시뮬레이션된 데이터 세트._ 왼쪽: _붉은 선은 실제 관계 $f(X) = 2 + 3X$ 를 나타내며, 이는 모집단 회귀선으로 알려져 있습니다. 파란 선은 최소 제곱선입니다; 이것은 관측된 데이터(검은색으로 표시됨)를 바탕으로 한 $f(X)$ 의 최소 제곱 추정치입니다._ 오른쪽: _모집단 회귀선이 다시 붉은색으로 표시되고, 최소 제곱선이 짙은 파란색으로 표시됩니다. 밝은 파란색으로는, 각기 분리된 무작위 관측 세트를 기반으로 각각 계산된 10개의 최소 제곱선이 표시됩니다. 각각의 최소 제곱선은 다르지만, 평균적으로 볼 때 최소 제곱선들은 모집단 회귀선에 꽤 가깝습니다._

the population mean $\mu$ of some random variable $Y$.

어떤 확률 변수 $Y$ 의 모집단 평균 $\mu$ 가 그 예시입니다.

Unfortunately, $\mu$ is unknown, but we do have access to $n$ observations from $Y$, $y_1, \dots, y_n$, which we can use to estimate $\mu$.

불행히도 $\mu$ 는 알려져 있지 않지만, 우리는 이를 추정하는 데 사용할 수 있는 $Y$ 로부터 온 $n$ 개의 관측치인 $y_1, \dots, y_n$ 에 접근 가능한 상태입니다.

A reasonable estimate is $\hat{\mu} = \bar{y}$, where $\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$ is the sample mean.

타당한 추정치는 $\hat{\mu} = \bar{y}$ 이며, 여기서 $\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$ 는 표본 평균입니다.

The sample mean and the population mean are different, but in general the sample mean will provide a good estimate of the population mean.

표본 평균과 모집단 평균은 다르지만, 일반적으로 표본 평균은 모집단 평균에 대한 훌륭한 추정치를 제공할 것입니다.

In the same way, the unknown coefficients $\beta_0$ and $\beta_1$ in linear regression define the population regression line.

같은 방식으로, 선형 회귀에 있는 미지의 계수 $\beta_0$ 와 $\beta_1$ 는 모집단 회귀선을 정의합니다.

We seek to estimate these unknown coefficients using $\hat{\beta}_0$ and $\hat{\beta}_1$ given in (3.4).

우리는 식 (3.4) 에 주어진 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 값을 사용하여 이 미지의 계수들을 추정하고자 노력합니다.

These coefficient estimates define the least squares line.

이러한 계수 추정치들이 곧장 최소 제곱선을 정의힙니다.

The analogy between linear regression and estimation of the mean of a random variable is an apt one based on the concept of _bias_.

선형 회귀와 무작위 변수의 평균 추정 사이의 비유는 _편향(bias)_ 개념에 기반을 둔 적절한 비유 중 하나입니다.

If we use the sample mean $\hat{\mu}$ to estimate $\mu$, this estimate is _unbiased_, in the sense that on average, we expect $\hat{\mu}$ to equal $\mu$.

우리가 $\mu$ 를 추정하기 위해 표본 평균 $\hat{\mu}$ 를 쓴다면, 이 추정치는 평균적으로 우리가 $\hat{\mu}$ 가 $\mu$ 와 같아질 것이라고 기대한다는 측면에서 _불편향적(unbiased)_ 입니다.

What exactly does this mean?

이것이 정확히 무엇을 의미할까요?

It means that on the basis of one particular set of observations $y_1, \dots, y_n$, $\hat{\mu}$ might overestimate $\mu$, and on the basis of another set of observations, $\hat{\mu}$ might underestimate $\mu$.

그 뜻은 $y_1, \dots, y_n$ 의 한정된 기저 관점 하에서 $\hat{\mu}$ 는 $\mu$ 를 과대평가할 수 있고, 다른 관측치 세트의 기저 관점에서는 $\hat{\mu}$ 가 $\mu$ 를 과소평가할 수 있다는 뜻입니다.

But if we could average a huge number of estimates of $\mu$ obtained from a huge number of sets of observations, then this average would _exactly_ equal $\mu$.

하지만 만일 수많은 관측치 세트들로부터 얻어진 방대한 $\mu$ 의 추정치들을 모아 평균을 낼 수 있다면, 이 평균은 _정확하게(exactly)_ $\mu$ 와 같아질 것입니다.

Hence, an unbiased estimator does not _systematically_ over- or under-estimate the true parameter.

따라서, 불편향 추정치는 참된 매개변수를 _체계적으로(systematically)_ 과대평가 하거나 과소평가하지 않습니다.

The property of unbiasedness holds for the least squares coefficient estimates given by (3.4) as well: if we estimate $\beta_0$ and $\beta_1$ on the basis of a particular data set, then our estimates won’t be exactly equal to $\beta_0$ and $\beta_1$.

불편향성의 속성은 식 (3.4) 로 주어지는 최소 제곱 계수 추정치들에 대해서도 동일하게 성립합니다: 우리가 특정 단면 데이터 세트를 근거 삼아 $\beta_0$ 와 $\beta_1$ 를 추정한다면, 우리의 추정치는 결코 $\beta_0$ 및 $\beta_1$ 과 완벽하게 같지는 않을 것입니다.

But if we could average the estimates obtained over a huge number of data sets, then the average of these estimates would be spot on!

하지만 우리가 수많은 방대한 데이터 세트에 걸쳐 획득한 추정치들을 전부 함께 모아들여 평균을 낼 수 있다면, 이 추정치들의 평균은 정확히 들어맞을 것입니다!

In fact, we can see from the righthand panel of Figure 3.3 that the average of many least squares lines, each estimated from a separate data set, is pretty close to the true population regression line.

실제로, 우리는 앞선 그림 3.3의 오른쪽 패널 도식을 통해, 분리된 개별 데이터 세트에서 각각 추정된 수많은 단위 최소 제곱선들의 평균 치세가 진짜 참된 모집단 회귀선 본 궤도 위치에 꽤 상당히 근접함을 두 눈으로 볼 수 있습니다.

We continue the analogy with the estimation of the population mean $\mu$ of a random variable $Y$.

무작위 변수 $Y$ 의 모집단 평균 $\mu$ 추정에 관한 비유를 계속해서 이어 나갑니다.

A natural question is as follows: how accurate is the sample mean $\hat{\mu}$ as an estimate of $\mu$?

한 가지 자연스런 의문사항이 다음과 같이 따릅니다: 표본 평균 $\hat{\mu}$ 은 $\mu$ 의 추정치로서 얼마나 정확할까요?

We have established that the average of $\hat{\mu}$'s over many data sets will be very close to $\mu$, but that a single estimate $\hat{\mu}$ may be a substantial underestimate or overestimate of $\mu$.

우리는 많은 데이터 집합에 걸쳐서 취합된 무수한 $\hat{\mu}$ 의 평균은 거의 $\mu$ 와 무척 가까울 것이라 정립했지만, 단일 추정 기록 단편 $\hat{\mu}$ 만큼은 자칫 본연 $\mu$ 치수에 대해 상당한 수치의 과소평가 혹은 과대평가 결과물이 오롯이 될 수 있음을 확립해 두었습니다.

How far off will that single estimate of $\hat{\mu}$ be?

저 단일 추정치 $\hat{\mu}$ 값은 (진짜 평균값에서부터)얼마나 이탈하게 될까요?

In general, we answer this question by computing the _standard error_ of $\hat{\mu}$, written as $\text{SE}(\hat{\mu})$.

일반적으로 우리는 $\text{SE}(\hat{\mu})$ 라고 표기되는 $\hat{\mu}$ 의 _표준 오차(standard error)_ 를 산출 계산함으로써 이 의문사항 질문에 대해 대답합니다.

We have the well-known formula:

우리에겐 이러한 익히 잘 알려져 있는 도출 공식이 마련되어 있습니다:

$$
\text{Var}(\hat{\mu}) = \text{SE}(\hat{\mu})^2 = \frac{\sigma^2}{n} \quad (3.7)
$$

where $\sigma$ is the standard deviation of each of the realizations $y_i$ of $Y$.$^2$

위 기재 공식 구조에서 표지 기수 $\sigma$ 는 단위 $Y$ 가 발현된 편린 조각들인 $y_i$ 조각 개개인 하나하나가 각각 기여 조달하는 표준 편차 모치입니다.$^2$

Roughly speaking, the standard error tells us the average amount that this estimate $\hat{\mu}$ differs from the actual value of $\mu$.

대략적으로 무사히 말해 두자면, 이 기조 표준 오차 단위는 추정 수치값 $\hat{\mu}$ 결단 본단이 기존 실제 모수 평균 본값 $\mu$ 수치와 엇갈려 동떨어져 있는 평균적인 편차 폭의 크기가 산술 어느 정도 통단 수준인지를 곧장 우리에게 알려 전해 줍니다.

Equation 3.7 also tells us how this deviation shrinks with $n$—the more observations we have, the smaller the standard error of $\hat{\mu}$.

식 3.7 단위 등식은 또한 이러한 빗나가는 단별 편차가 지수 $n$ 치수에 맞물려 기조 어떻게 그 넓이 크기가 축소 감면되는지도 알려줍니다—우리가 가진 통치 관측치 표단 수가 거대 더 방대히 많아질수록, 표지 $\hat{\mu}$ 에 배당 적용되는 표준 수리 오차 본결 산치 단위는 더 작아집니다.

In a similar vein, we can wonder how close $\hat{\beta}_0$ and $\hat{\beta}_1$ are to the true values $\beta_0$ and $\beta_1$.

비슷한 맥락이 부여된 상황에서, 우리는 $\hat{\beta}_0$ 와 표수 $\hat{\beta}_1$ 수치가 본연 참값 모치 $\beta_0$ 와 지지 $\beta_1$ 단위에 대해 도달 과연 어떻게 수리적으로 일치 및 근접한 파지 모구 표본 상태일지 궁금증을 해 볼 제지 조달 수가 있습니다.

To compute the standard errors associated with $\hat{\beta}_0$ and $\hat{\beta}_1$, we use the following formulas:

$\hat{\beta}_0$ 기치 및 모도 투합 $\hat{\beta}_1$ 측치에 단기 연루 관련된 계도 모치 표준 산치 오차들을 결결 연산 계산해 도찰 내기 부단 위하여, 우리는 도단 다음 단결 공식을 도집 의거 조단 사용합니다:

$$
\text{SE}(\hat{\beta}_0)^2 = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right], \quad \text{SE}(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \quad (3.8)
$$

where $\sigma^2 = \text{Var}(\epsilon)$.

여기 구조 공식 내에서 표제 $\sigma^2 = \text{Var}(\epsilon)$ 단위와 동등 합일 무치 부단 기치 연합 편의 일치합니다.

For these formulas to be strictly valid, we need to assume that the errors $\epsilon_i$ for each observation have common variance $\sigma^2$ and are uncorrelated.

이러한 모치 기재 공식들이 통구 엄격하게 합치 타당성을 정오 조단 가지기 기위 본단 위해서, 결단 우리는 지단 각각의 개별 배단 관측치 조단 오차항 지오 $\epsilon_i$ 가 통상적인 공통 분산 단면 $\sigma^2$ 를 구지 모구 가지고 서로 지조 비상관적인 무상관 구도 상관관계가 나타나지 않음에 필연 필단 의거 가정 도치 부합 단결 해야만 합니다.

This is clearly not true in Figure 3.1, but the formula still turns out to be a good approximation.

이는 모자 단결 그림 3.1 에서는 단수 명확히 수리 전제 참이 지위 부설 도달 아님이 분명하지만, 지지 도조 이 전제 공식은 단도 여전히 부도 도합 통결 훌륭한 산당 근사치로 지지 도결 증명 판명 조지 기리 전제 도출됩니다.

Notice in the formula that $\text{SE}(\hat{\beta}_1)$ is smaller when the $x_i$ are more spread out; intuitively we have more _leverage_ to estimate a slope when this is the case.

수식에서 $x_i$ 가 더 넓게 퍼져 있을수록 $\text{SE}(\hat{\beta}_1)$ 가 더 작아진다는 점에 주목하십시오; 직관적으로 볼 때 이러한 경우 우리는 기울기를 추정할 수 있는 더 많은 _지렛대(leverage)_ 를 가지게 됩니다.

We also see that $\text{SE}(\hat{\beta}_0)$ would be the same as $\text{SE}(\hat{\mu})$ if $\bar{x}$ were zero (in which case $\hat{\beta}_0$ would be equal to $\bar{y}$).

만약 $\bar{x}$ 가 0이라면 (이 경우 $\hat{\beta}_0$ 는 $\bar{y}$ 와 같을 것입니다) $\text{SE}(\hat{\beta}_0)$ 는 $\text{SE}(\hat{\mu})$ 와 같을 것이라는 점도 알 수 있습니다.

In general, $\sigma^2$ is not known, but can be estimated from the data.

일반적으로 $\sigma^2$ 는 알려져 있지 않지만 데이터로부터 추정할 수 있습니다.

This estimate of $\sigma$ is known as the _residual standard error_, and is given by the formula $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$.

$\sigma$ 에 대한 이 추정치는 _잔차 표준 오차(residual standard error)_ 라고 알려져 있으며, $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$ 수식에 의해 주어집니다.


Strictly speaking, when $\sigma^2$ is estimated from the data we should write $\widehat{\text{SE}}(\hat{\beta}_1)$ to indicate that an estimate has been made, but for simplicity of notation we will drop this extra “hat”.

엄밀히 말해서, $\sigma^2$ 이 데이터로부터 추정될 때 우리는 추정이 이루어졌음을 나타내기 위해 $\widehat{\text{SE}}(\hat{\beta}_1)$ 로 적어야만 하지만 표기의 단순화를 위해 이 추가적인 "햇(hat)" 을 생략할 것입니다.

That is, there is approximately a 95% chance that the interval

즉, 다음 구간이

$$
\left[ \hat{\beta}_1 - 2 \cdot \text{SE}(\hat{\beta}_1), \, \hat{\beta}_1 + 2 \cdot \text{SE}(\hat{\beta}_1) \right] \quad (3.10)
$$

will contain the true value of $\beta_1$.$^3$

(위의 국문 문장에 결합 완료)

Similarly, a confidence interval for $\beta_0$ approximately takes the form

유사하게, $\beta_0$ 에 대한 신뢰 구간(confidence interval)은 대략적으로 다음과 같은 형태를 취합니다.

$$
\hat{\beta}_0 \pm 2 \cdot \text{SE}(\hat{\beta}_0) \quad (3.11)
$$

In the case of the advertising data, the 95% confidence interval for $\beta_0$ is $[6.130, 7.935]$ and the 95% confidence interval for $\beta_1$ is $[0.042, 0.053]$.

광고 데이터 예제의 경우, $\beta_0$ 에 대한 95% 신뢰 구간은 $[6.130, 7.935]$ 이고 $\beta_1$ 에 대한 95% 신뢰 구간은 $[0.042, 0.053]$ 입니다.

Therefore, we can conclude that in the absence of any advertising, sales will, on average, fall somewhere between 6,130 and 7,935 units.

따라서, 우리는 어떤 광고도 없는 상황에서 판매량은 평균적으로 6,130 단위와 7,935 단위 사이 어딘가로 떨어질 것이라고 결론 내릴 수 있습니다.

Furthermore, for each $\$1,000$ increase in television advertising, there will be an average increase in sales of between 42 and 53 units.

나아가, 텔레비전 광고에서 1,000 달러가 증가할 때마다 42 단위와 53 단위 사이 구간의 판매량 평균 증가가 있을 것입니다.

Standard errors can also be used to perform _hypothesis tests_ on the coefficients.

표준 오차는 계수에 대한 _가설 검정(hypothesis tests)_ 을 수행하는 데에도 사용될 수 있습니다.

The most common hypothesis test involves testing the _null hypothesis_ of

가장 일반적인 가설 검정은 다음과 같은 _귀무가설(null hypothesis)_ 을 검정하는 작업과 관련이 있습니다.

$$
H_0 : \beta_1 = 0 \quad (3.12)
$$

versus the _alternative hypothesis_

이에 반대되는 _대립가설(alternative hypothesis)_ 은 다음과 같습니다.

$$
H_a : \beta_1 \neq 0 \quad (3.13)
$$

Mathematically, this corresponds to testing

수학적으로, 이는 다음을 테스트하는 것과 대응됩니다.

$$
H_0 : \text{There is no relationship between } X \text{ and } Y
$$

versus

이에 반대되는 상황은:

$$
H_a : \text{There is some relationship between } X \text{ and } Y
$$

since if $\beta_1 = 0$ then the model (3.5) reduces to $Y = \beta_0 + \epsilon$, and $X$ is not associated with $Y$.

왜냐하면 만약 $\beta_1 = 0$ 이라면 모델 (3.5) 제식은 $Y = \beta_0 + \epsilon$ 로 축소될 것이며, $X$ 는 $Y$ 와 연관되지 않게 되기 때문입니다.

To test the null hypothesis, we need to determine whether $\hat{\beta}_1$, our estimate for $\beta_1$, is sufficiently far from zero that we can be confident that $\beta_1$ is non-zero.

이 귀무가설을 검정하기 위해, 우리는 $\beta_1$ 에 대한 우리의 추정치인 $\hat{\beta}_1$ 이 $\beta_1$ 이 0이 아니라고 확신할 수 있을 만큼 충분히 0에서 멀리 떨어져 있는지 결정해야 합니다.

How far is far enough?

얼마나 멀어야 충분할까요?

This of course depends on the accuracy of $\hat{\beta}_1$—that is, it depends on $\text{SE}(\hat{\beta}_1)$.

이것은 물론 $\hat{\beta}_1$ 의 정확도에—즉 $\text{SE}(\hat{\beta}_1)$ 에 달려 있습니다.

If $\text{SE}(\hat{\beta}_1)$ is small, then even relatively small values of $\hat{\beta}_1$ may provide strong evidence that $\beta_1 \neq 0$, and hence that there is a relationship between $X$ and $Y$.

만약 $\text{SE}(\hat{\beta}_1)$ 이 작다면, 상대적으로 작은 $\hat{\beta}_1$ 값이라도 $\beta_1 \neq 0$ 임을, 나아가 $X$ 와 $Y$ 사이에 관계가 존재한다는 것을 반증하는 강력한 증거를 제공할 수 있습니다.

In contrast, if $\text{SE}(\hat{\beta}_1)$ is large, then $\hat{\beta}_1$ must be large in absolute value in order for us to reject the null hypothesis.

반대로 $\text{SE}(\hat{\beta}_1)$ 가 크다면, 우리가 귀무가설을 기각하기 위해서 $\hat{\beta}_1$ 의 절대값은 무조건 커야만 합니다.

In practice, we compute a _$t$-statistic_, given by

실제로는 다음과 같이 주어지는 _$t$-통계량($t$-statistic)_ 을 계산합니다.

$$
t = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{\beta}_1)} \quad (3.14)
$$

> $^3$ _Approximately_ for several reasons.

> $^3$ 몇 가지 이유에서 _대략적으로(Approximately)_ 라고 표현했습니다.

> Equation 3.10 relies on the assumption that the errors are Gaussian.

> 식 3.10 은 오차들이 가우시안 확률 분포를 가진다는 가정에 의존합니다.

> Also, the factor of 2 in front of the $\text{SE}(\hat{\beta}_1)$ term will vary slightly depending on the number of observations $n$ in the linear regression.

> 또한 $\text{SE}(\hat{\beta}_1)$ 항 앞에 있는 계수 2는 선형 회귀의 관측치 $n$ 수에 따라 미세하게 다를 수 있습니다.

> To be precise, rather than the number 2, (3.10) should contain the 97.5% quantile of a $t$-distribution with $n-2$ degrees of freedom.

> 정확히 말해, (3.10) 수식은 2 보다는 $n-2$ 자유도를 취한 $t$-분포의 97.5% 분위수를 두어야 맞습니다.

> Details of how to compute the 95% confidence interval precisely in `R` will be provided later in this chapter.

> 이 장의 후반부에서 `R` 안에서 95% 신뢰 구간을 아주 정교하게 계산해 내는 세부 방식을 제공할 것입니다.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 7.0325 | 0.4578 | 15.36 | $< 0.0001$ |
| `TV` | 0.0475 | 0.0027 | 17.67 | $< 0.0001$ |

**TABLE 3.1.** _For the_ `Advertising` _data, coefficients of the least squares model for the regression of number of units sold on TV advertising budget. An increase of_ $\$1,000$ _in the TV advertising budget is associated with an increase in sales by around 50 units. (Recall that the_ `sales` _variable is in thousands of units, and the_ `TV` _variable is in thousands of dollars.)_

**TABLE 3.1.** `Advertising` _데이터에 대한 표본 도표로, TV 광고 예산을 근거로 한 제품 판매 단위 회귀를 위한 최소 제곱 모델의 계수. TV 광고 예산의_ $\$1,000$ _증가는 대략 판매량 50 단위의 상승 결과와 연관되어 있습니다. (_`sales` _변수가 수천 단위이며,_ `TV` _변수 단위 역시 수천 달러라는 점을 상기하십시오.)_

which measures the number of standard deviations that $\hat{\beta}_1$ is away from 0.

이는 $\hat{\beta}_1$ 이 0에서부터 벗어난 표준 편차 숫자를 측정합니다.

If there really is no relationship between $X$ and $Y$, then we expect that (3.14) will have a $t$-distribution with $n - 2$ degrees of freedom.

만일 실제로 아무 관계가 없다면 우리는 식 (3.14) 수식이 $n - 2$ 자유도의 $t$-분포 모델을 띨 것이라 기대합니다.

The $t$-distribution has a bell shape and for values of $n$ greater than approximately 30 it is quite similar to the standard normal distribution.

$t$-분포는 종(bell) 형태를 취하며 값 $n$ 이 대략 30보다 클 경우 표준 정규 분포와 매우 유사합니다.

Consequently, it is a simple matter to compute the probability of observing any number equal to $|t|$ or larger in absolute value, assuming $\beta_1 = 0$.

결론적으로 $\beta_1 = 0$ 이라 가정하고 살펴볼 때 표본의 절대값이 $|t|$ 와 같거나 큰 관측 확률을 따지는 계산은 무척 간단한 문제입니다.

We call this probability the _$p$-value_.

우리는 이 확률을 _$p$-값($p$-value)_ 이라고 부릅니다.

Roughly speaking, we interpret the $p$-value as follows: a small $p$-value indicates that it is unlikely to observe such a substantial association between the predictor and the response due to chance, in the absence of any real association between the predictor and the response.

대략적으로 말해, 우리는 $p$-값을 다음과 같이 해석합니다: 작은 $p$-값은 예측 변수와 응답 변수 단독 사이에 어떠한 실제 연관성이 없는 상태에서 오직 우연 발생적인 확률로 인해 예측 변수와 응답 변수 사이의 실질적인 연대성을 관측하게 될 객관적인 요율이 사실상 굉장히 낮음을 시사합니다.

Hence, if we see a small $p$-value, then we can infer that there is an association between the predictor and the response.

따라서, 작은 $p$-값을 보게 된다면 예측 변수와 응답 변수 사이엔 명확한 어떤 연관성이 있다고 추정할 수 있습니다.

We _reject the null hypothesis_—that is, we declare a relationship to exist between $X$ and $Y$—if the $p$-value is small enough.

만일 도출된 확률 $p$-값이 단지 충분히 작다면 저희는 귀무 가설 자체를 과감히 기각(_reject the null hypothesis_)하고—즉 $X$ 와 $Y$ 편 사이엔 분명한 동반 공존적 인과 관계가 실재 존재한다고 선언합니다.

Typical $p$-value cutoffs for rejecting the null hypothesis are 5% or 1%, although this topic will be explored in much greater detail in Chapter 13.

이런 기각 결정의 컷오프(cutoff) 판단 통상 지점들은 전형적으로 수리 비율 5% 이나 혹 1% 로 상정됩니다, 비록 이 화두 쟁점 주제는 다가올 제 13장에서 한결 보다 깊은 심층 상세 논의로 추후 다루어 지겠지만 말입니다.

When $n = 30$, these correspond to $t$-statistics (3.14) of around 2 and 2.75, respectively.

기준 단위를 $n = 30$ 치수로 삼아 본다면, 해당 컷오프 점들은 방정식 (3.14) 수치 안의 $t$-통계량 기준상 대략 각각 숫자 2 와 2.75 수치 비율로 대치 대응되어 일치 성립합니다.

Table 3.1 provides details of the least squares model for the regression of number of units sold on TV advertising budget for the `Advertising` data.

표 3.1 에서는 해당 `Advertising` 모델 데이터 위에서 산립된 TV 기반 예산 자본의 제품 유닛 판매 숫자 회귀를 위한 편향 최소 제곱 치수 모델에 대한 세부 항목 단위들을 제시합니다.

Notice that the coefficients for $\hat{\beta}_0$ and $\hat{\beta}_1$ are very large relative to their standard errors, so the $t$-statistics are also large; the probabilities of seeing such values if $H_0$ is true are virtually zero.

관측 기록 항목상 투여된 $\hat{\beta}_0$ 요소 및 $\hat{\beta}_1$ 수치들의 단편 계수가 당해 단입 본연 표준 오차 비율 요소들과 견주어 보았을 상황 적에 상당한 상대 폭으로 크고 거대함을 주목하십시오, 나아가 도달 산출의 이 여파로 동반 결집 통계치인 $t$-통계량 치표들도 그와 같이 똑같이 큰 상태를 유지합니다; 이 말은 즉, 본연 기저 당사 가설 기반치 $H_0$ 가 진짜 실존하는 명백한 참(true) 이었을 시 기조 상태상에서, 이처럼 기조상 동종의 값들을 오롯이 관측 직견 발견 보게 될 우연적 상황 확률이 사실상 0(zero) 수렴 기반과 전무 다름없다는 귀결 결과를 말합니다.

Hence we can conclude that $\beta_0 \neq 0$ and $\beta_1 \neq 0$.$^4$

고로 결론적으로, 우리는 $\beta_0 \neq 0$ 임과 단도직입적으로 $\beta_1 \neq 0$ 이라는 결론을 도외시 내릴 수 있는 확증 단계에 놓이게 됩니다.$^4$

## Sub-Chapters

This is the document for 3.1.2 Assessing the Accuracy of the Coefficient Estimates.

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/trans1.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/trans1.html)

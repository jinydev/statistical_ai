---
layout: default
title: "trans1"
---

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

[< 3.1 Simple Linear Regression](../trans1.html) | [3.1.2 Assessing the Accuracy of the Coefficient Estimates >](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans1.html)

# 3.1.1 Estimating the Coefficients
# 3.1.1 계수 추정

In practice, $\beta_0$ and $\beta_1$ are unknown.
실제로는, $\beta_0$와 $\beta_1$은 알려져 있지 않습니다.

So before we can use (3.1) to make predictions, we must use data to estimate the coefficients.
그래서 우리가 예측을 하기 위해 (3.1)을 사용하기 전에, 우리는 계수를 추정하기 위해 데이터를 사용해야 합니다.

Let
다음을

$$
(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)
$$

represent $n$ observation pairs, each of which consists of a measurement of $X$ and a measurement of $Y$.
각각이 $X$의 측정값과 $Y$의 측정값으로 구성된 $n$개의 관측치 쌍을 나타낸다고 합시다.

In the `Advertising` example, this data set consists of the TV advertising budget and product sales in $n = 200$ different markets.
`Advertising` 예제에서, 이 데이터셋은 $n = 200$개의 서로 다른 시장에서의 TV 광고 예산과 제품 판매량으로 구성됩니다.

(Recall that the data are displayed in Figure 2.1.)
(데이터가 그림 2.1에 표시되어 있다는 것을 상기하십시오.)

Our goal is to obtain coefficient estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ such that the linear model (3.1) fits the available data well—that is, so that $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ for $i = 1, \dots, n$.
우리의 목표는 선형 모델 (3.1)이 가용한 데이터에 잘 맞도록—즉, $i = 1, \dots, n$에 대해 $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$가 되도록—계수 추정치 $\hat{\beta}_0$와 $\hat{\beta}_1$을 얻는 것입니다.

In other words, we want to find an intercept $\hat{\beta}_0$ and a slope $\hat{\beta}_1$ such that the resulting line is as close as possible to the $n = 200$ data points.
다시 말해, 우리는 결과로 나오는 선이 $n = 200$개의 데이터 포인트들에 가능한 한 가깝게 되도록 절편 $\hat{\beta}_0$와 기울기 $\hat{\beta}_1$을 찾기를 원합니다.

There are a number of ways of measuring _closeness_.
*가까움*을 측정하는 여러 방법들이 존재합니다.

However, by far the most common approach involves minimizing the _least squares_ criterion, and we take that approach in this chapter.
하지만, 단연코 가장 흔한 접근법은 *최소 제곱* 기준을 최소화하는 것을 포함하며, 우리는 이 챕터에서 그 접근법을 취합니다.

Alternative approaches will be considered in Chapter 6.
대안적인 접근 방식들은 6장에서 다루어질 것입니다.

Let $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the prediction for $Y$ based on the $i$th value of $X$.
$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$를 $X$의 $i$번째 값에 기반한 $Y$에 대한 예측값이라고 합시다.

Then $e_i = y_i - \hat{y}_i$ represents the $i$th _residual_—this is the difference between the $i$th observed response value and the $i$th response value that is predicted by our linear model.
그러면 $e_i = y_i - \hat{y}_i$는 $i$번째 *잔차*를 나타냅니다—이것은 $i$번째로 관측된 응답값과 우리의 선형 모델에 의해 예측된 $i$번째 응답값 사이의 차이입니다.

We define the _residual sum of squares_ (RSS) as
우리는 *잔차 제곱합* (RSS)을 다음과 같이 정의합니다

$$
\text{RSS} = e_1^2 + e_2^2 + \dots + e_n^2
$$

or equivalently as $$
\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1 x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1 x_2)^2 + \dots + (y_n - \hat{\beta}_0 - \hat{\beta}_1 x_n)^2 \quad (3.3)
$$
또는 동등하게 다음과 같습니다 $$
\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1 x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1 x_2)^2 + \dots + (y_n - \hat{\beta}_0 - \hat{\beta}_1 x_n)^2 \quad (3.3)
$$

The least squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS.
최소 제곱 접근법은 RSS를 최소화하기 위해 $\hat{\beta}_0$와 $\hat{\beta}_1$을 선택합니다.

Using some calculus, one can show that the minimizers are
약간의 미적분학을 사용하면, 최소화하는 값들은 다음과 같음을 보여줄 수 있습니다.

$$
\begin{align*}
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x}
\end{align*} \quad (3.4)
$$

**FIGURE 3.1.** _For the_ `Advertising` _data, the least squares fit for the regression of_ `sales` _onto_ `TV` _is shown._
**그림 3.1.** `Advertising` 데이터에 대해, `TV`에 대한 `sales` 회귀의 최소 제곱 적합이 표시됩니다.

_The fit is found by minimizing the residual sum of squares._
적합은 잔차 제곱합을 최소화함으로써 찾아집니다.

_Each grey line segment represents a residual._
각각의 회색 선분은 잔차를 나타냅니다.

_In this case a linear fit captures the essence of the relationship, although it overestimates the trend in the left of the plot._
이 경우 선형 적합은 플롯의 왼쪽 부분에서 추세를 과대 추정하기는 하지만, 관계의 핵심을 포착합니다.

where $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ and $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ are the sample means.
여기서 $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$와 $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$는 표본 평균들입니다.

In other words, (3.4) defines the _least squares coefficient estimates_ for simple linear regression.
다시 말해, (3.4)는 단순 선형 회귀에 대한 *최소 제곱 계수 추정치*를 정의합니다.

Figure 3.1 displays the simple linear regression fit to the `Advertising` data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$.
그림 3.1은 `Advertising` 데이터에 단순 선형 회귀를 적합한 것을 표시하며, 여기서 $\hat{\beta}_0 = 7.03$ 이고 $\hat{\beta}_1 = 0.0475$ 입니다.

In other words, according to this approximation, an additional $\$1,000$ spent on TV advertising is associated with selling approximately 47.5 additional units of the product.
다시 말해, 이 근사에 따르면, TV 광고에 소비된 추가적인 $\$1,000$는 제품의 대략 47.5개의 추가 단위를 판매하는 것과 연관되어 있습니다.

In Figure 3.2, we have computed RSS for a number of values of $\beta_0$ and $\beta_1$, using the advertising data with `sales` as the response and `TV` as the predictor.
그림 3.2에서, 우리는 `sales`를 반응 변수로 하고 `TV`를 예측 변수로 하여 광고 데이터를 사용해 여러 $\beta_0$와 $\beta_1$ 값들에 대해 RSS를 계산했습니다.

In each plot, the red dot represents the pair of least squares estimates $(\hat{\beta}_0, \hat{\beta}_1)$ given by (3.4).
각 플롯에서, 빨간 점은 (3.4)에 의해 주어진 최소 제곱 추정치 쌍 $(\hat{\beta}_0, \hat{\beta}_1)$을 나타냅니다.

These values clearly minimize the RSS.
이 값들은 명확하게 RSS를 최소화합니다.

[< 3.1 Simple Linear Regression](../trans1.html) | [3.1.2 Assessing the Accuracy of the Coefficient Estimates >](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans1.html)

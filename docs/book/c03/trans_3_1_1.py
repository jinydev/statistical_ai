import sys
import re

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_1_simple_linear_regression\3_1_1_estimating_the_coefficients\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"""In practice, $\beta_0$ and $\beta_1$ are unknown. So before we can use (3.1) to make predictions, we must use data to estimate the coefficients. Let

실제로 $\beta_0$ 와 $\beta_1$ 는 미지수입니다. 따라서 예측을 위해 (3.1) 식을 사용하기 전에, 우리는 반드시 데이터를 사용하여 계수를 추정해야 합니다. 다음과 같이 가정합시다.""":
    r"""In practice, $\beta_0$ and $\beta_1$ are unknown.

실제로 $\beta_0$ 와 $\beta_1$ 는 미지수입니다.

So before we can use (3.1) to make predictions, we must use data to estimate the coefficients.

따라서 예측을 위해 (3.1) 식을 사용하기 전에, 우리는 반드시 데이터를 사용하여 계수를 추정해야 합니다.

Let

다음과 같이 가정합시다.""",

    r"""represent $n$ observation pairs, each of which consists of a measurement of $X$ and a measurement of $Y$. In the `Advertising` example, this data set consists of the TV advertising budget and product sales in $n = 200$ different markets. (Recall that the data are displayed in Figure 2.1.) Our goal is to obtain coefficient estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ such that the linear model (3.1) fits the available data well—that is, so that $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ for $i = 1, \dots, n$. In other words, we want to find an intercept $\hat{\beta}_0$ and a slope $\hat{\beta}_1$ such that the resulting line is as close as possible to the $n = 200$ data points. There are a number of ways of measuring _closeness_. However, by far the most common approach involves minimizing the _least squares_ criterion, and we take that approach in this chapter. Alternative approaches will be considered in Chapter 6.

이는 $X$ 의 측정값과 $Y$ 의 측정값으로 구성된 $n$ 쌍의 관측치를 나타냅니다. `Advertising` 예제에서 이 데이터 세트는 $n = 200$ 개의 다른 시장에서의 TV 광고 예산과 제품 판매량으로 구성됩니다. (이러한 데이터가 그림 2.1 에 표시되었다는 점을 떠올려 보십시오.) 우리의 목표는 선형 모델 (3.1) 이 가용한 데이터에 잘 맞도록, 즉 $i = 1, \dots, n$ 에 대해 $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ 가 될 수 있는 계수 추정치 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 를 얻는 것입니다. 다시 말해, 우리는 결과로 나오는 선이 $n = 200$ 개의 데이터 포인트에 최대한 가까워지도록 하는 절편 $\hat{\beta}_0$ 와 기울기 $\hat{\beta}_1$ 를 찾고자 합니다. _근접성(closeness)_ 을 측정하는 방법에는 여러 가지가 있습니다. 하지만 지금까지 가장 보편적인 접근법은 _최소 제곱(least squares)_ 기준을 최소화하는 것이며, 우리는 이 장에서 그 접근 방식을 취합니다. 대안적인 접근법은 6장에서 다룰 것입니다.""":
    r"""represent $n$ observation pairs, each of which consists of a measurement of $X$ and a measurement of $Y$.

이는 $X$ 의 측정값과 $Y$ 의 측정값으로 구성된 $n$ 쌍의 관측치 쌍을 나타냅니다.

In the `Advertising` example, this data set consists of the TV advertising budget and product sales in $n = 200$ different markets.

`Advertising` 예제에서 이 데이터 세트는 $n = 200$ 개의 다른 시장에서의 TV 광고 예산과 제품 판매량으로 구성됩니다.

(Recall that the data are displayed in Figure 2.1.)

(이러한 데이터가 그림 2.1 에 표시되었다는 점을 떠올려 보십시오.)

Our goal is to obtain coefficient estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ such that the linear model (3.1) fits the available data well—that is, so that $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ for $i = 1, \dots, n$.

우리의 목표는 선형 모델 (3.1) 이 가용한 데이터에 잘 맞도록, 즉 $i = 1, \dots, n$ 에 대해 $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ 가 될 수 있도록 하는 계수 추정치 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 를 얻는 것입니다.

In other words, we want to find an intercept $\hat{\beta}_0$ and a slope $\hat{\beta}_1$ such that the resulting line is as close as possible to the $n = 200$ data points.

다시 말해, 우리는 결과로 나오는 선이 $n = 200$ 개의 데이터 포인트에 최대한 가까워지도록 하는 절편 $\hat{\beta}_0$ 와 기울기 $\hat{\beta}_1$ 를 찾고자 합니다.

There are a number of ways of measuring _closeness_.

_근접성(closeness)_ 을 측정하는 방법에는 여러 가지가 있습니다.

However, by far the most common approach involves minimizing the _least squares_ criterion, and we take that approach in this chapter.

하지만 지금까지 가장 보편적인 접근법은 _최소 제곱(least squares)_ 기준을 최소화하는 것이며, 우리는 이 장에서 그 접근 방식을 취합니다.

Alternative approaches will be considered in Chapter 6.

대안적인 접근법은 6장에서 다룰 것입니다.""",

    r"""Let $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the prediction for $Y$ based on the $i$th value of $X$. Then $e_i = y_i - \hat{y}_i$ represents the $i$th _residual_—this is the difference between the $i$th observed response value and the $i$th response value that is predicted by our linear model. We define the _residual sum of squares_ (RSS) as

$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ 를 $X$ 의 $i$ 번째 값을 기반으로 한 $Y$ 예측값이라 합시다. 그러면 $e_i = y_i - \hat{y}_i$ 는 $i$ 번째 _잔차(residual)_ 를 나타냅니다. 이는 관측된 $i$ 번째 응답값과 우리의 선형 모델에 의해 예측된 $i$ 번째 응답 예측값 사이의 차이입니다. 우리는 _잔차 제곱합(residual sum of squares, RSS)_ 을 다음과 같이 정의합니다.""":
    r"""Let $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the prediction for $Y$ based on the $i$th value of $X$.

$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ 를 $X$ 의 $i$ 번째 값을 기반으로 한 $Y$ 예측값이라 합시다.

Then $e_i = y_i - \hat{y}_i$ represents the $i$th _residual_—this is the difference between the $i$th observed response value and the $i$th response value that is predicted by our linear model.

그러면 $e_i = y_i - \hat{y}_i$ 는 $i$ 번째 _잔차(residual)_ 를 나타냅니다—이는 관측된 $i$ 번째 응답값과 우리의 선형 모델에 의해 예측된 $i$ 번째 응답값 사이의 차이입니다.

We define the _residual sum of squares_ (RSS) as

우리는 _잔차 제곱합(residual sum of squares, RSS)_ 을 다음과 같이 정의합니다.""",

    r"""The least squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS. Using some calculus, one can show that the minimizers are

최소 제곱 접근법은 이 RSS 를 최소화하기 위해 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 를 선택합니다. 미적분학을 사용하면, 이것을 최소로 만드는 값들이 다음과 같음을 증명할 수 있습니다.""":
    r"""The least squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS.

최소 제곱 접근법은 이 RSS 를 최소화하기 위해 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 를 선택합니다.

Using some calculus, one can show that the minimizers are

약간의 미적분학을 사용하면, 이것을 최소화하는 값들이 다음과 같음을 보일 수 있습니다.""",

    r"""where $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ and $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ are the sample means. In other words, (3.4) defines the _least squares coefficient estimates_ for simple linear regression. 

여기서 $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ 와 $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ 는 표본의 평균값입니다. 다시 말해, (3.4) 식은 단순 선형 회귀 통계에 쓰이는 _최소 제곱 계수 추정치(least squares coefficient estimates)_ 를 정의합니다.""":
    r"""where $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ and $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ are the sample means.

여기서 $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ 와 $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ 는 표본 평균입니다.

In other words, (3.4) defines the _least squares coefficient estimates_ for simple linear regression. 

다시 말해, (3.4) 식은 단순 선형 회귀를 위한 _최소 제곱 계수 추정치(least squares coefficient estimates)_ 를 정의합니다.""",

    r"""Figure 3.1 displays the simple linear regression fit to the `Advertising` data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$. In other words, according to this approximation, an additional $\$1,000$ spent on TV advertising is associated with selling approximately 47.5 additional units of the product. In Figure 3.2, we have computed RSS for a number of values of $\beta_0$ and $\beta_1$, using the advertising data with `sales` as the response and `TV` as the predictor. In each plot, the red dot represents the pair of least squares estimates $(\hat{\beta}_0, \hat{\beta}_1)$ given by (3.4). These values clearly minimize the RSS. 

그림 3.1 은 `Advertising` 데이터에 통계 적합된 단순 선형 회귀 모형을 표시하며, 그 추산은 절편 $\hat{\beta}_0 = 7.03$ , 기울기 $\hat{\beta}_1 = 0.0475$ 로 판명됩니다. 다시 말해 이 근사치에 따르면, TV 광고비 항목에 추가로 투자한 $\$1,000$ 의 비용 예산이 대략 47.5 개의 추가 판매량을 달성하는 것과 연관되어 있음을 의미합니다. 그림 3.2 에서 우리는 예측 변수로 투입된 `TV` 와 응답 변수로 설정된 `sales` 데이터를 사용하여 여러 $\beta_0$ 와 $\beta_1$ 값에 대한 RSS 를 계산했습니다. 각 플롯 안에서, 붉은 점은 (3.4) 식을 통해 계산된 _최소 제곱 적합 쌍(pair of least squares estimates)_ 인 $(\hat{\beta}_0, \hat{\beta}_1)$ 위치를 나타냅니다. 이 값들이 분명히 RSS 를 최소화합니다.""":
    r"""Figure 3.1 displays the simple linear regression fit to the `Advertising` data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$.

그림 3.1 은 `Advertising` 데이터에 대한 단순 선형 회귀 적합을 표시하며, 여기서 $\hat{\beta}_0 = 7.03$ 이고 $\hat{\beta}_1 = 0.0475$ 입니다.

In other words, according to this approximation, an additional $\$1,000$ spent on TV advertising is associated with selling approximately 47.5 additional units of the product.

다시 말해, 이 근사치에 따르면, TV 광고에 추가로 쓴 $\$1,000$ 는 약 47.5개의 제품을 추가로 판매하는 것과 연관이 있습니다.

In Figure 3.2, we have computed RSS for a number of values of $\beta_0$ and $\beta_1$, using the advertising data with `sales` as the response and `TV` as the predictor.

그림 3.2 에서, 우리는 응답 변수로 `sales` 를 그리고 예측 변수로 `TV` 를 사용한 광고 데이터를 이용하여, 수많은 $\beta_0$ 와 $\beta_1$ 값 쌍들에 대한 RSS 를 계산했습니다.

In each plot, the red dot represents the pair of least squares estimates $(\hat{\beta}_0, \hat{\beta}_1)$ given by (3.4).

각 플롯에서, 빨간 점은 (3.4) 식으로 주어지는 최소 제곱 추정치 쌍 $(\hat{\beta}_0, \hat{\beta}_1)$ 을 나타냅니다.

These values clearly minimize the RSS. 

이 값들은 명확하게 RSS 를 최소화합니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")

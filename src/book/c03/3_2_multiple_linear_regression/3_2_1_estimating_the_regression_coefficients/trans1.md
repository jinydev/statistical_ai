---
layout: default
title: "trans1"
---

[< 3.2 Multiple Linear Regression](../trans1.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.2.1 Estimating the Regression Coefficients_

# _3.2.1 회귀 계수 추정 (Estimating the Regression Coefficients)_

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula

단순 선형 회귀 설정의 경우와 마찬가지로, 식 (3.19) 의 회귀 계수 $\beta_0, \beta_1, \dots, \beta_p$ 는 미지수이므로 추정해야만 합니다. 주어진 추정치 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 에 대해, 우리는 다음 공식을 사용하여 예측할 수 있습니다.

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals

이 파라미터들은 단순 선형 회귀의 맥락에서 살펴보았던 것과 동일한 최소 제곱 접근법을 사용하여 추정됩니다. 우리는 잔차 제곱합을 최소화하도록 $\beta_0, \beta_1, \dots, \beta_p$ 를 선택합니다.

$$
\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)
$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4

(3.22) 를 최소화하는 값 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 가 다중 최소 제곱 회귀 계수 추정치입니다. (3.4) 의 단순 선형 회귀 추정치들과 달리, 다중 회귀 계수 추정치는 행렬 대수학을 사용하여 가장 쉽게 표현할 수 있는 다소 복잡한 형태를 갖습니다. 이러한 이유로, 우리는 여기서 그 공식들을 제공하지 않습니다. 어떠한 통계 소프트웨어 패키지든 이러한 계수 추정치를 계산하는 데 사용할 수 있으며, 이 장의 후반부에서 우리는 `R` 에서 이를 어떻게 수행하는지 보여줄 것입니다. 그림 3.4 는

<br>

<p align="center">

<img src="./img/3_4.png" alt="In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.">

</p>

<br>

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._



**FIGURE 3.4.** _두 개의 예측 변수와 한 개의 응답 변수가 있는 3차원 설정에서, 최소 제곱 회귀선은 평면이 됩니다. 이 평면은 각 관측치(빨간색으로 표시됨)와 평면 사이의 수직 거리 제곱합을 최소화하도록 선택됩니다._



illustrates an example of the least squares fit to a toy data set with $p=2$ predictors.

$p=2$ 예측 변수가 있는 장난감 데이터 세트에 대한 최소 제곱 적합의 예를 보여줍니다.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data.

표 3.4는 `Advertising` 데이터를 활용하여 제품 판매량을 예측할 목적으로 TV, 라디오, 그리고 신문 매체의 광고 예산을 사용했을 때 산출되는 다중 회귀 계수 추정치들을 보여줍니다.

We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales.

우리는 이러한 결과를 다음과 같이 해석합니다. TV 와 신문 광고 예산 수준이 고정되어 있을 때, 라디오 광고에 1,000 달러를 추가 지출하는 것은 대략 189 개 판매 단위의 매출 증가와 연관이 있습니다.

Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates.

이 추정치들을 표 3.1 과 3.3 의 수치들과 비교하면, `TV` 와 `radio` 에 대한 다중 회귀 모델의 계수들이 단순 선형 회귀의 수치값들과 상당히 유사하다는 점을 알 수 있습니다.

However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86.

하지만 표 3.3에서 `newspaper` 선형 회귀 계수 추정치는 유의미하게 0이 아니었으나, 다중 회귀 기법에서의 `newspaper` 계수는 0에 극히 근접하며 해당하는 $p$-값은 0.86 수치 주위를 맴돌며 더는 유의미하지 않게 되었습니다.

This illustrates that the simple and multiple regression coefficients can be quite different.

이 사례는 단순 회귀 계수와 다중 모형 회귀의 예측 계수가 꽤 상이할 수 있음을 보여줍니다.

This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`.

이런 극명한 차이는 단순 회귀의 경우 기울기 척도가 `TV` 와 `radio` 등 타 변수를 무시한 채, 오직 신문 지면 부문 1,000달러 증가와 연관된 평균 판매액 증가치만 보여주기 때문에 발생합니다.

By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.

이와 상반되게, 다중 회귀 맥락 환경에서 `newspaper` 측정 척도는 `TV` 나 `radio` 부문 예측값을 고정한 채, 신문 매체 광고 지출을 1,000달러 증가시킬 때 연관되는 일어날 평균적인 매출 상승폭을 나타냅니다.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the opposite?

단순 선형 회귀에선 상반되는 결과를 암시했던 반면, 이 다중 회귀에서는 `sales` 와 `newspaper` 사이에 아무런 관계조차 시사하지 않는 것이 과연 타당한 이치일까요?

In fact it does.

사실 이는 타당합니다.

Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5.

표 3.5 에 나타난 3개의 예측 변수와 응답 변수에 대한 상관관계 행렬을 고려해 보십시오.

| | Coefficient | Std. error | $t$-statistic | $p$-value |

| :--- | :--- | :--- | :--- | :--- |

| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |

| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |

| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |

| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | $0.8599$ |

**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._

**TABLE 3.4.** `Advertising` _데이터의 경우, 이 표는 TV, 라디오 및 신문 광고 예산에 따른 판매 단위 수에 대한 다중 선형 회귀의 최소 제곱 계수 추정치를 보여줍니다._

| | `TV` | `radio` | `newspaper` | `sales` |

| :--- | :--- | :--- | :--- | :--- |

| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |

| `radio` | 0.0548 | 1.0000 | 0.3541 | 0.5762 |

| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |

| `sales` | 0.7822 | 0.5762 | 0.2283 | 1.0000 |

**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._

**TABLE 3.5.** `Advertising` _데이터를 위한_ `TV` _,_ `radio` _,_ `newspaper` _, 그리고_ `sales` _간의 상관관계 행렬입니다._

Notice that the correlation between `radio` and `newspaper` is 0.35.

여기서 `radio` 와 `newspaper` 간 상관관계가 대략 0.35 임을 주목하십시오.

This indicates that markets with high newspaper advertising tend to also have high radio advertising.

이는 신문 광고비 투입이 높은 시장일수록 라디오 광고비도 많은 경향이 있음을 나타냅니다.

Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales.

이제 다중 회귀 모델이 옳고, 신문 광고는 매출과 무관하지만 라디오 광고는 매출과 관련이 있다고 가정해 봅시다.

Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets.

그렇다면 우리가 라디오 부문에 비용을 더 많이 지출하는 시장들에서 상품 판매량이 덩달아 높아질 것이고, 앞선 상관 행렬이 보여주듯 우린 해당 시장들에서 종종 신문 광고에도 더 많은 투자를 하는 경향이 있습니다.

Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales.

결과적으로, 오직 `sales` 대 `newspaper` 양측만을 대조해 보는 단순 선형 회귀에선, 신문 광고가 매출 파급과 직접 결부되어 있지 않음에도 불구하고 높은 `newspaper` 수치가 더 높은 `sales` 와 연관성이 있다는 결과(가짜 관계)를 관측하게 될 공산이 큽니다.

So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` .

즉, `newspaper` 신문 광고비는 사실 `radio` 라디오 광고비를 짚어내는 대리인(surrogate) 역할을 한 것이며; `newspaper` 가 `radio` 부문이 일군 매출 기여의 "공로(credit)"를 가로채 덧쓴 양상입니다.

This slightly counterintuitive result is very common in many real life situations.

이러한 약간 직관에 반하는 역설적 양상은 많은 실생활 현장에서 매우 흔히 발현합니다.

Consider an absurd example to illustrate the point.

이 관점을 쉽게 이해할 수 있는 조금 우스꽝스러운 예시 한 가지를 살펴봅시다.

Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper` .

어느 해변 마을에서 일정 기간 수집된 '상어 습격 횟수' 대 '아이스크림 판매량' 데이터를 회귀 분석해 보면, 앞서 `sales` 와 `newspaper` 부문에 나타난 것과 유사한 양(+) 의 상관관계를 보여줄 것입니다.

Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks.

물론 상어 습격을 줄이기 위해 해변에서 아이스크림 판매를 금지해야 한다고 주장하는 사람은 (아직) 없습니다.

In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks.

실제로 기온이 오르면 더 많은 사람들이 해변을 방문하게 되며, 이는 자연스레 더 많은 아이스크림 판매량 증가와 (해수욕 인파 증가로 인한) 상어 습격 빈도를 동시에 증가시킵니다.

A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.

상어 습격 횟수를 아이스크림 판매량과 온도라는 총 두 변수에 맞춰 다중 회귀 분석해 보면, 우리의 직관이 암시하듯 온도를 고려하여 기준을 조정한 후엔 아이스크림 판매가 더 이상 유의미한 예측 변수가 아님이 밝혀집니다.

---


현재 3.2.1 회귀 계수 추정 소속 문서입니다.
[상위 경로(Multiple Linear Regression)로 돌아가기](../trans1.html)

---

## Sub-Chapters (하위 목차)


[< 3.2 Multiple Linear Regression](../trans1.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/trans1.html)

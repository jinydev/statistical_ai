---
layout: default
title: "trans1"
---

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans1.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/trans1.html)

# 3.1.3 Assessing the Accuracy of the Model

# 3.1.3 모델의 정확도 평가

Once we have rejected the null hypothesis (3.12) in favor of the alternative hypothesis (3.13), it is natural to want to quantify _the extent to which the model fits the data_. The quality of a linear regression fit is typically assessed using two related quantities: the _residual standard error_ (RSE) and the $$R^2$$ statistic.

대립가설 (3.13) 을 지지하여 귀무가설 (3.12) 를 기각하고 나면, _모델이 데이터에 적합한 정도_ 를 정량화하고자 하는 것은 자연스러운 일입니다. 선형 회귀 적합의 품질은 일반적으로 두 가지 관련 수치를 사용하여 평가됩니다: _잔차 표준 오차(residual standard error, RSE)_ 와 $$R^2$$ 통계량입니다.

> $^4$ In Table 3.1, a small $p$-value for the intercept indicates that we can reject the null hypothesis that $\beta_0 = 0$, and a small $p$-value for `TV` indicates that we can reject the null hypothesis that $\beta_1 = 0$. Rejecting the latter null hypothesis allows us to conclude that there is a relationship between `TV` and `sales`. Rejecting the former allows us to conclude that in the absence of `TV` expenditure, `sales` are non-zero.

> $^4$ 표 3.1에서 절편에 대한 작은 $p$-값은 $\beta_0 = 0$ 이라는 귀무가설을 기각할 수 있음을 나타내며, `TV` 에 대한 작은 $p$-값은 $\beta_1 = 0$ 이라는 귀무가설을 기각할 수 있음을 나타냅니다. 후자의 귀무가설을 기각하면 `TV` 와 `sales` 간에 관계가 있다고 결론 내릴 수 있습니다. 전자의 귀무가설을 기각하면 `TV` 광고가 없을 때에도 `sales` 가 0이 아니라는 단론을 내릴 수 있습니다.

| Quantity | Value |

| :--- | :--- |

| Residual standard error | 3.26 |

| $$R^2$$ | 0.612 |

| $F$-statistic | 312.1 |

**TABLE 3.2.** _For the_ `Advertising` _data, more information about the least squares model for the regression of number of units sold on TV advertising budget._

**TABLE 3.2.** `Advertising` _데이터에 대한, TV 광고 예산에 따른 판매 단위 수 회귀 추정을 위한 최소 제곱 모델의 추가 정보입니다._

Table 3.2 displays the RSE, the $$R^2$$ statistic, and the $F$-statistic (to be described in Section 3.2.2) for the linear regression of number of units sold on TV advertising budget.

표 3.2는 TV 광고 예산에 따른 판매 단위 수의 선형 회귀에 대한 RSE, $$R^2$$ 통계량, 그리고 $F$-통계량(3.2.2절에서 설명됨)을 보여줍니다.

## Residual Standard Error

## 잔차 표준 오차 (Residual Standard Error)

Recall from the model (3.5) that associated with each observation is an error term $\epsilon$. Due to the presence of these error terms, even if we knew the true regression line (i.e. even if $\beta_0$ and $\beta_1$ were known), we would not be able to perfectly predict $Y$ from $X$. The RSE is an estimate of the standard deviation of $\epsilon$. Roughly speaking, it is the average amount that the response will deviate from the true regression line. It is computed using the formula

모델 (3.5) 에서 각 관측치에는 오차항 $\epsilon$ 이 수반됨을 떠올려 보십시오. 이러한 오차항의 존재로 인해, 설령 우리가 진짜 회귀선(즉, $\beta_0$ 와 $\beta_1$ 값)을 안다 해도 $X$ 로부터 $Y$ 를 완벽히 예측할 수는 없습니다. RSE 는 $\epsilon$ 의 표준 편차에 대한 추정치입니다. 대략적으로 말해, 이는 응답 변수가 진짜 회귀선으로부터 벗어날 평균적인 양입니다. 이는 다음 공식을 사용하여 계산됩니다.

$$
\text{RSE} = \sqrt{\frac{1}{n-2}\text{RSS}} = \sqrt{\frac{1}{n-2}\sum_{i=1}^n(y_i-\hat{y}_i)^2} \quad (3.15)
$$

Note that RSS was defined in Section 3.1.1, and is given by the formula

RSS 는 앞서 3.1.1 절에서 정의되었으며, 다음 공식으로 주어짐에 유의하십시오.

$$
\text{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad (3.16)
$$

In the case of the advertising data, we see from the linear regression output in Table 3.2 that the RSE is 3.26. In other words, actual sales in each market deviate from the true regression line by approximately 3,260 units, on average. Another way to think about this is that even if the model were correct and the true values of the unknown coefficients $\beta_0$ and $\beta_1$ were known exactly, any prediction of sales on the basis of TV advertising would still be off by about 3,260 units on average. Of course, whether or not 3,260 units is an acceptable prediction error depends on the problem context. In the advertising data set, the mean value of `sales` over all markets is approximately 14,000 units, and so the percentage error is $3,260 / 14,000 = 23\%$.

광고 데이터 예제의 경우, 우리는 표 3.2 의 선형 회귀 출력에서 RSE 가 3.26 임을 알 수 있습니다. 다시 말해, 각 시장의 실제 판매량은 진짜 회귀선에서 평균적으로 약 3,260 개 단위만큼 벗어납니다. 다르게 생각해 보면, 설령 모델이 옳고 모르는 계수 $\beta_0$ 와 $\beta_1$ 의 참값을 정확히 안다 하더라도, TV 광고를 기반으로 한 판매량 예측값은 여전히 평균적으로 약 3,260 개가량 어긋나게 될 것이라는 의미입니다. 물론 3,260 개 단위가 수용 가능한 예측 오차인지 여부는 문제의 맥락에 달려 있습니다. 광고 데이터 세트에서 전체 시장에 대한 `sales` 의 평균값은 대략 14,000 단위이므로, 퍼센티지 오차는 $3,260 / 14,000 = 23\%$ 에 해당합니다.

The RSE is considered a measure of the _lack of fit_ of the model (3.5) to the data. If the predictions obtained using the model are very close to the true outcome values—that is, if $y_i \approx \hat{y}_i$ for $i = 1, \dots, n$—then (3.15) will be small, and we can conclude that the model fits the data very well. On the other hand, if $\hat{y}_i$ is very far from $y_i$ for one or more observations, then the RSE may be quite large, indicating that the model doesn’t fit the data well.

RSE 는 모델 (3.5) 가 데이터에 _적합하지 않은 정도(lack of fit)_ 를 측정하는 척도로 여겨집니다. 만약 모델을 사용하여 얻은 예측치가 진짜 결과값에 무척 가깝다면—즉 $i = 1, \dots, n$ 에 대해 $y_i \approx \hat{y}_i$ 라면—(3.15) 는 작아질 것이고, 우리는 이 모델이 데이터에 아주 잘 맞는다고 결론 내릴 수 있습니다. 그와 반대로, 하나 이상의 관측치에서 예측치 $\hat{y}_i$ 가 결과값 $y_i$ 에서 아주 멀리 동떨어져 있다면 RSE 는 꽤 커질 수 있으며, 이는 모델이 데이터에 잘 맞지 않음을 나타냅니다.

## $$R^2$$ Statistic

## $$R^2$$ 통계량 ($$R^2$$ Statistic)

The RSE provides an absolute measure of lack of fit of the model (3.5) to the data. But since it is measured in the units of $Y$, it is not always clear what constitutes a good RSE. The $$R^2$$ statistic provides an alternative measure of fit. It takes the form of a _proportion_—the proportion of variance explained—and so it always takes on a value between 0 and 1, and is independent of the scale of $Y$.

RSE 는 모델 (3.5) 가 데이터에 적합하지 않은 정도를 절대적인 척도로 제공합니다. 그러나 이는 $Y$ 의 단위로 측정되기 때문에 항상 어느 정도가 좋은 RSE 인지 명확하지는 않습니다. $$R^2$$ 통계량은 모델 적합성의 대안적인 척도를 제공합니다. 이는 설명된 분산의 비율이라는 _비율(proportion)_ 형태를 취하므로, 항상 0 에서 1 사이의 값을 가지며 $Y$ 의 스케일과 무관합니다.

To calculate $$R^2$$, we use the formula

$$R^2$$ 를 계산하기 위해 다음 공식을 사용합니다.
$$

R^2 = \frac{\text{TSS} - \text{RSS}}{\text{TSS}} = 1 - \frac{\text{RSS}}{\text{TSS}} \quad (3.17)

$$
where $\text{TSS} = \sum (y_i - \bar{y})^2$ is the _total sum of squares_, and $\text{RSS}$ is defined in (3.16). $\text{TSS}$ measures the total variance in the response $Y$, and can be thought of as the amount of variability inherent in the response before the regression is performed. In contrast, $\text{RSS}$ measures the amount of variability that is left unexplained after performing the regression. Hence, $\text{TSS} - \text{RSS}$ measures the amount of variability in the response that is explained (or removed) by performing the regression, and $$R^2$$ measures the _proportion of variability in $Y$ that can be explained using $X$_. An $$R^2$$ statistic that is close to 1 indicates that a large proportion of the variability in the response is explained by the regression. A number near 0 indicates that the regression does not explain much of the variability in the response; this might occur because the linear model is wrong, or the error variance $\sigma^2$ is high, or both. In Table 3.2, the $$R^2$$ was 0.61, and so just under two-thirds of the variability in `sales` is explained by a linear regression on `TV`.
여기서 $\text{TSS} = \sum (y_i - \bar{y})^2$ 는 _총 제곱합(total sum of squares)_ 이고, $\text{RSS}$ 는 (3.16) 에서 정의되었습니다. $\text{TSS}$ 는 응답 $Y$ 의 총 분산을 측정하며, 회귀가 수행되기 전에 응답에 내재된 변동성의 양으로 간주될 수 있습니다. 대조적으로 $\text{RSS}$ 는 회귀를 수행한 후에 설명되지 않은 채로 남겨진 변동성의 양을 측정합니다. 그러므로 $\text{TSS} - \text{RSS}$ 는 회귀를 수행함으로써 설명된(혹은 제거된) 응답의 변동성을 측정하며, $$R^2$$ 는 _$X$ 를 사용하여 설명할 수 있는 $Y$ 의 변동성 비율_ 을 측정합니다. 1에 가까운 $$R^2$$ 통계량은 응답 변동성의 큰 비율이 회귀에 의해 설명됨을 뜻합니다. 0에 가까운 숫자는 회귀가 응답의 변동성을 그다지 설명하지 못함을 나타내며; 이는 아마도 선형 모델이 틀렸거나, 오차 분산 $\sigma^2$ 가 높거나, 아니면 두 가지 모두 해당하기 때문일 수 있습니다. 표 3.2 에서, $$R^2$$ 는 0.61 이었으며, 따라서 `sales` 변위성의 대략 3분의 2 조금 못 미치는 수치가 `TV` 의 선형 회귀에 의해 설명됩니다.
The $$R^2$$ statistic (3.17) has an interpretational advantage over the RSE (3.15), since unlike the RSE, it always lies between 0 and 1. However, it can still be challenging to determine what is a _good $$R^2$$_ value, and in general, this will depend on the application. For instance, in certain problems in physics, we may know that the data truly comes from a linear model with a small residual error. In this case, we would expect to see an $$R^2$$ value that is extremely close to 1, and a substantially smaller $$R^2$$ value might indicate a serious problem with the experiment in which the data were generated. On the other hand, in typical applications in biology, psychology, marketing, and other domains, the linear model (3.5) is at best an extremely rough approximation to the data, and residual errors due to other unmeasured factors are often very large. In this setting, we would expect only a very small proportion of the variance in the response to be explained by the predictor, and an $$R^2$$ value well below 0.1 might be more realistic!
$$R^2$$ 통계량 (3.17) 은 RSE 와 달리 항상 0 과 1 사이에 수치가 존재하므로 RSE (3.15) 보다 해석에 이점이 있습니다. 그러나 여전히 어떤 지표가 _좋은 $$R^2$$_ 값인지 결정하는 것은 어려울 수 있으며, 보편적으로 이는 적용되는 분야에 따라 달라질 것입니다. 예를 들어, 물리학 연구의 특정 문제에서는 데이터가 작은 잔차 오차를 가진 선형 모델에서 나옴을 이미 알 수 있습니다. 이 경우 우리는 $$R^2$$ 값이 1에 극히 가까울 것으로 예상하게 되며, 이보다 현저히 작은 $$R^2$$ 값은 데이터가 생성된 당초 실험에 심각한 문제가 있음을 나타내는 반증일 수 있습니다. 반면 생물학, 심리학, 마케팅 및 다른 분야의 일반적인 활용에서는, 선형 모델 (3.5) 이 기껏해야 데이터에 대한 극히 거친 근삿값에 그치며, 파악되지 않은 다른 요소로 인한 잔차 오차가 무척 큰 경우가 빈번합니다. 이런 환경에서라면 우리는 예측 변수에 의해 설명되는 응답 분산이 아주 적은 비율 수준일 것으로 기대해야 하고, 0.1 을 훨씬 밑도는 $$R^2$$ 값이 오히려 더 현실적일 수 있습니다!

The $$R^2$$ statistic is a measure of the linear relationship between $X$ and $Y$. Recall that _correlation_, defined as

$$R^2$$ 통계량은 $X$ 와 $Y$ 사이의 선형 관계를 측정하는 척도입니다. 다음과 같이 정의되는 _상관(correlation)_ 계수를 상기해 보십시오.
$$

r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}} \quad (3.18)

$$
is also a measure of the linear relationship between $X$ and $Y$.$^5$ This suggests that we might be able to use $r = \text{Cor}(X, Y)$ instead of $$R^2$$ in order to assess the fit of the linear model. In fact, it can be shown that in the simple
이 상관 계수 역시 $X$ 와 $Y$ 사이 선형 관계의 척도입니다.$^5$ 이는 우리가 선형 모델의 부합성을 평가하기 위해 $$R^2$$ 대신 $r = \text{Cor}(X, Y)$ 를 사용할 수도 있음을 뜻합니다. 사실 단순
> $^5$ We note that in fact, the right-hand side of (3.18) is the sample correlation; thus, it would be more correct to write $\widehat{\text{Cor}}(X, Y)$; however, we omit the "hat" for ease of notation.
> $^5$ 참고로 (3.18) 공식의 우변은 표본 상관입니다; 따라서 $\widehat{\text{Cor}}(X, Y)$ 라고 쓰는 편이 더 정확할 것입니다; 그러나 여기서 표기의 편의를 위해 "햇(hat, 모자 기호)" 을 생략합니다.
80 3. Linear Regression
<br>
**Simple regression of `sales` on `radio`**
<p align="center"><b>`radio` 지출에 대한 `sales` 의 단순 회귀</b></p>
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 9.312 | 0.563 | 16.54 | $< 0.0001$ |
| `radio` | 0.203 | 0.020 | 9.92 | $< 0.0001$ |
**Simple regression of `sales` on `newspaper`**
<p align="center"><b>`newspaper` 지출에 대한 `sales` 의 단순 회귀</b></p>
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 12.351 | 0.621 | 19.88 | $< 0.0001$ |
| `newspaper` | 0.055 | 0.017 | 3.30 | $0.00115$ |
**TABLE 3.3.** _More simple linear regression models for the_ `Advertising` _data. Coefficients of the simple linear regression model for number of units sold on_ Top: _radio advertising budget and_ Bottom: _newspaper advertising budget. A $\$1,000$ _increase in spending on radio advertising is associated with an average increase in sales by around 203 units, while the same increase in spending on newspaper advertising is associated with an average increase in sales by around 55 units. (Note that the_ `sales` _variable is in thousands of units, and the_ `radio` _and_ `newspaper` _variables are in thousands of dollars.)_
**TABLE 3.3.** `Advertising` _데이터에 대한 또 다른 단순 선형 모델입니다. 다음은 판매된 제품 단위 수에 대한 단순 선형 회귀 모델의 계수들입니다._ 위쪽 표: _라디오 광고 예산의 경우, 그리고_ 아래쪽 표: _신문 광고 예산의 경우입니다. 라디오 광고에 대한 $\$1,000$ 지출 증가는 평균적으로 약 203 개 단위의 매출 증가와 연관이 있는 반면, 신문 광고에 대한 동일한 예산 증가는 약 55 개 단위의 평균 매출 증가와 연관되어 있습니다. (앞서 언급했듯_ `sales` _변수는 수천 단위 묶음이고, 변수_ `radio` _와_ `newspaper` _수치는 수천 달러 단위임을 유의하십시오.)_
linear regression setting, $$R^2$$ = $r^2$. In other words, the squared correlation and the $$R^2$$ statistic are identical. However, in the next section we will discuss the multiple linear regression problem, in which we use several predictors simultaneously to predict the response. The concept of correlation between the predictors and the response does not extend automatically to this setting, since correlation quantifies the association between a single pair of variables rather than between a larger number of variables. We will see that $$R^2$$ fills this role.
선형 회귀 설정에서는 $$R^2 = r^2$$ 입니다. 다시 말해, 상관계수의 제곱과 $$R^2$$ 통계량은 동일합니다. 하지만 다음 절에서 우리는 다중 선형 회귀 문제를 논의할 것이며, 여기서는 응답을 예측하기 위해 여러 개의 예측 변수를 동시에 사용할 것입니다. 예측 변수들과 응답 사이의 상관(correlation) 개념은 이러한 설정으로 자동으로 연장되지 않습니다. 왜냐하면 상관은 다수의 변수들 간의 연관성보다는 단일 변수 쌍 간의 연관성을 정량화하기 때문입니다. 우리는 앞으로 $$R^2$$ 가 이러한 역할을 채우는 것을 보게 될 것입니다.
## Sub-Chapters

This is the document for 3.1.3 Assessing the Accuracy of the Model.

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans1.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/trans1.html)

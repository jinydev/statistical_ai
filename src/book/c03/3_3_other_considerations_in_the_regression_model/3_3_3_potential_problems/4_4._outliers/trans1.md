---
layout: default
title: "trans1"
---

[< 3 3. Non-Constant Variance Of Error Terms](../3_3._non-constant_variance_of_error_terms/trans1.html) | [6 6. Collinearity >](../6_6._collinearity/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4. Outliers

# 네 번째 잠재적 문제점: 이상치(Outliers)

An _outlier_ is a point for which $y_i$ is far from the value predicted by the model.

_이상치(outlier)_ 란 관측치 $y_i$ 가 모델에 의해 예측된 값에서 멀리 떨어진 점을 의미합니다.

**==> picture [321 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20 20<br>−2 −1 0 1 2 −2 0 2 4 6 −2 0 2 4 6<br>X Fitted Values Fitted Values<br>6<br>6 4<br>4 3 4<br>Y 2 2 2<br>0 Residuals 1<br>−2 0 Studentized Residuals 0<br>−1<br>−4<br>**----- End of picture text -----**<br>


**FIGURE 3.12.** Left: _The least squares regression line is shown in red, and the regression line after removing the outlier is shown in blue._ Center: _The residual plot clearly identifies the outlier._ Right: _The outlier has a  residual of_ 6 _; typically we expect values between −_ 3 _and_ 3 _._

Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.
이상치는 데이터 수집 과정에서 관측치가 잘못 기록된 경우 등 다양한 이유로 발생할 수 있습니다.

The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier.
그림 3.12 의 왼쪽 패널에 있는 붉은 점(관측치 20)은 전형적인 이상치를 예시합니다.

The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier.
붉은 실선은 최소 제곱 회귀 적합선이며, 푸른 점선은 이 이상치를 제거한 뒤 얻은 최소 제곱 적합선입니다.

In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept.
이 경우 이상치를 제거하는 것은 최소 제곱선에 거의 영향을 미치지 않습니다: 기울기엔 거의 변동이 없고 절편에서 미세한 감소만을 이끌었습니다.

It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit.
이처럼 예측 변숫값이 특이하지 않은 이상치는 대체로 최소 제곱 적합에 별다른 영향을 미치지 않는 것이 전형적입니다.

However, even if an outlier does not have much effect on the least squares fit, it can cause other problems.
하지만 이상치가 당장의 회귀 최소 제곱 적합에 큰 영향을 주지 않더라도, 다른 문제들을 야기할 수 있습니다.

For instance, in this example, the RSE is $1.09$ when the outlier is included in the regression, but it is only $0.77$ when the outlier is removed.
예를 들어 이 사례에서 이상치를 회귀 묶음에 포함했을 때 잔차 표준 오차(RSE)는 $1.09$ 이지만, 제거했을 땐 $0.77$ 로 줄어듭니다.

Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit.
RSE 는 모든 신뢰 구간과 $p$-값을 계산하는 데 사용되므로, 단일 데이터 점으로 인한 이 극적인 증가는 결과적으로 모델 적합을 해석하는 데 시사점을 가질 수 있습니다.

Similarly, inclusion of the outlier causes the $R^2$ to decline from $0.892$ to $0.805$.
비슷하게, 이상치를 포함하는 것은 결괏값 $R^2$ 를 $0.892$ 에서 $0.805$ 로 감소시키는 원인이 됩니다.

Residual plots can be used to identify outliers.
흔히 이상치를 식별하는 데 잔차 플롯을 사용할 수 있습니다.

In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12.
이 예제에서 그림 3.12 의 중앙 패널에 묘사된 잔차 플롯을 보면 이상치를 분명하게 확인할 수 있습니다.

But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier.
그러나 실제로는 수치가 어느 정도나 커져야 어떤 관측치를 이상치로 간주할 수 있을지 결정하기 어려울 수 있습니다.

To address this problem, instead of plotting the residuals, we can plot the _ residuals_, computed by dividing each residual $e_i$ by its estimated standard error.
이러한 문제를 다루기 위해 단순히 모델의 잔차를 플롯하는 대신, 각 잔차 $e_i$ 를 해당 추정된 표준 오차로 나누어 계산한 _스튜던트화 잔차( residuals)_ 표본 무리를 도해로 플로팅할 수 있습니다.

Observations whose  residuals are greater than 3 in absolute value are possible outliers.
통상 스튜던트화 잔차의 절댓값이 3 보다 큰 관측치는 잠재적인 이상치일 가능성이 큽니다.

In the right-hand panel of Figure 3.12, the outlier's  residual exceeds 6, while all other observations have  residuals between -2 and 2.
그림 3.12 오른쪽 국면을 보면 이상치의 스튜던트화 잔차 치수는 6 을 벗어나는 반면, 다른 모든 관측치는 -2 와 2 사이 대역 범위 내에 있습니다.

If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation.
만약 이상치가 데이터 수집 측면이나 단순 기록상의 오류로 인해 초래된 것이라고 확신한다면, 한 가지 제일 쉬운 해결책은 해당 관측치를 아예 삭제해 버리는 조치입니다.

However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.
그러나 예측 변수가 누락된 경우처럼, 이상치는 되려 전반적인 모델 자체의 결함을 일러주는 결함 지표일 수도 있으므로 주의를 기울여야 합니다.

# 5. High Leverage Points
# 다섯 번째 잠재적 문제점: 높은 레버리지(High Leverage) 점

We just saw that outliers are observations for which the response $y_i$ is unusual given the predictor $x_i$.
방금 전 우리는 이상치가 예측 변수 $x_i$ 대비 비정상적으로 튀는 관측 응답치 $y_i$ 를 가진 관측 사항임을 살펴보았습니다.

In contrast, observations with _high _ have an unusual value for $x_i$.
이와 대조적으로 _높은 레버리지(high )_ 를 가진 관측치들은 오히려 예측 변수 $x_i$ 자체가 아주 기이한 값을 품고 있습니다.

For example, observation 41 in the left-hand





**==> picture [318 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
41 20<br>41<br>20<br>−2 −1 0 1 2 3 4 −2 −1 0 1 2 0.00 0.05 0.10 0.15 0.20 0.25<br>X X1 Leverage<br>2 5<br>4<br>10 1<br>3<br>Y 5 X2 0 2<br>1<br>−1<br>0 Studentized Residuals 0<br>−2 −1<br>**----- End of picture text -----**<br>


**FIGURE 3.13.** Left: _Observation 41 is a high  point, while 20 is not. The red line is the fit to all the data, and the blue line is the fit with observation 41 removed._ Center: _The red observation is not unusual in terms of its X_ 1 _value or its X_ 2 _value, but still falls outside the bulk of the data, and hence has high ._ Right: _Observation_ 41 _has a high  and a high residual._

panel of Figure 3.13 has high , in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high  observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high  observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high  observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high  observations.

In a simple linear regression, high  observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$. Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high  point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.

In order to quantify an observation’s , we compute the _ statistic_ . A large value of this indicates an observation with high  . For a simple linear regression,

**==> picture [220 x 26] intentionally omitted <==**





**==> picture [318 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
2000 4000 6000 8000 12000 2000 4000 6000 8000 12000<br>Limit Limit<br>80<br>800<br>70<br>60 600<br>Age<br>Rating<br>50<br>400<br>40<br>30 200<br>**----- End of picture text -----**<br>


**FIGURE 3.14.** _Scatterplots of the observations from the_ `Credit` _data set._ Left: _A plot of_ `age` _versus_ `limit` _. These two variables are not collinear._ Right: _A plot of_ `rating` _versus_ `limit` _. There is high collinearity._

It is clear from this equation that _hi_ increases with the distance of x_i from ¯ _x_ . There is a simple extension of _hi_ to the case of multiple predictors, though we do not provide the formula here. The  _hi_ is always between 1 _/n_ and 1, and the average  for all the observations is always equal to ( $p$ + 1) _/n_ . So if a given observation has a  that greatly exceeds ( $p$ +1) _/n_ , then we may suspect that the corresponding point has high .

The right-hand panel of Figure 3.13 provides a plot of the  residuals versus _hi_ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high  as well as a high  residual. In other words, it is an outlier as well as a high  observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low .

---

## Sub-Chapters (하위 목차)


[< 3 3. Non-Constant Variance Of Error Terms](../3_3._non-constant_variance_of_error_terms/trans1.html) | [6 6. Collinearity >](../6_6._collinearity/trans1.html)

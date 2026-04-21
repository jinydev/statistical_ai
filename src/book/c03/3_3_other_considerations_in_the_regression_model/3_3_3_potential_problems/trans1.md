---
layout: default
title: "trans1"
---

[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/trans1.html) | [2 2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.3.3 Potential Problems_



When we fit a linear regression model to a particular data set, many problems may occur. Most common among these are the following:

1. _Non-linearity of the response-predictor relationships._

2. _Correlation of error terms._

3. _Non-constant variance of error terms._

4. _Outliers._

5. _High-leverage points._

6. _Collinearity._

In practice, identifying and overcoming these problems is as much an art as a science. Many pages in countless books have been written on this topic. Since the linear regression model is not our primary focus here, we will provide only a brief summary of some key points.

1. Non-linearity of the Data



**==> picture [318 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Residual Plot for Linear Fit Residual Plot for Quadratic Fit<br>323 334<br>330 323<br>334<br>155<br>5 10 15 20 25 30 15 20 25 30 35<br>Fitted values Fitted values<br>20<br>15<br>15<br>10<br>10<br>5<br>5<br>0<br>0<br>Residuals Residuals<br>−5<br>−5<br>−10<br>−10<br>−15<br>−15<br>**----- End of picture text -----**<br>


**FIGURE 3.9.** _Plots of residuals versus predicted (or fitted) values for the_ `Auto` _data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend._ Left: _A linear regression of_ `mpg` _on_ `horsepower` _. A strong pattern in the residuals indicates non-linearity in the data._ Right: _A linear regression of_ `mpg` _on_ `horsepower` _and_ `horsepower`[2] _. There is little pattern in the residuals._

The linear regression model assumes that there is a straight-line relationship between the predictors and the response. If the true relationship is far from linear, then virtually all of the conclusions that we draw from the fit are suspect. In addition, the prediction accuracy of the model can be significantly reduced.

_Residual plots_ are a useful graphical tool for identifying non-linearity. residual plot Given a simple linear regression model, we can plot the residuals, _ei_ =

3.3 Other Considerations in the Regression Model 101

ˆ _yi − yi_ , versus the predictor x_i . In the case of a multiple regression model, since there are multiple predictors, we instead plot the residuals versus ˆ the predicted (or _fitted_ ) values y_i . Ideally, the residual plot will show no fitted discernible pattern. The presence of a pattern may indicate a problem with some aspect of the linear model.

The left panel of Figure 3.9 displays a residual plot from the linear regression of `mpg` onto `horsepower` on the `Auto` data set that was illustrated in Figure 3.8. The red line is a smooth fit to the residuals, which is displayed in order to make it easier to identify any trends. The residuals exhibit a clear U-shape, which provides a strong indication of non-linearity in the data. In contrast, the right-hand panel of Figure 3.9 displays the residual plot that results from the model (3.36), which contains a quadratic term. There appears to be little pattern in the residuals, suggesting that the quadratic term improves the fit to the data.

If the residual plot indicates that there are non-linear associations in the data, then a simple approach is to use non-linear transformations of the predictors, such as log X , _√X_ , and X[2] , in the regression model. In the later chapters of this book, we will discuss other more advanced non-linear approaches for addressing this issue.

---



### 2. Correlation of Error Terms (오차 항의 상관관계)

오차 항들은 서로 독립이어야 한다는 기본 전제가 깨졌을 때 발생하는 표준 오차 산정의 치명적인 오류를 다룹니다.
이로 인해 발생하는 가설 검정 결함 및 p-value의 신뢰성 하락을 설명합니다.

### 3. Non-constant Variance of Error Terms (오차 항의 비일관적 분산)

데이터의 반응 변수 값이 커짐에 따라 오차의 편차가 커지는 이분산성(Heteroscedasticity) 문제를 분석합니다.
로그 함수와 같은 반응 변수 변환(Transformation)으로 오차 분산을 안정화하는 기법을 배웁니다.

### 4. Outliers (이상치)

일반 예측치를 크게 벗어난 관측값인 이상치가 잔차 표준 오차 및 모델 적합도(R²)에 어떤 치명적인 영향을 끼치는지 파악합니다.
스튜던트화 잔차(Studentized Residual)를 사용한 진단과 대응을 다룹니다.

### 6. Collinearity (다중공선성)

입력 변수들이 서로 높은 상관성을 띠어 각 계수 추정의 분산을 팽창시키는 다중공선성의 위험 패턴을 분석합니다.
분산 팽창 인수(VIF)를 계산하여 문제를 감지하고 대응책을 세우는 법을 안내합니다.

---

## Sub-Chapters (하위 목차)


[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/trans1.html) | [2 2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/trans1.html)

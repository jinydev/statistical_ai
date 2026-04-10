---
layout: default
title: "index"
---

# _3.2.1 Estimating the Regression Coefficients_ 
# _3.2.1 회귀 계수 추정 (Estimating the Regression Coefficients)_

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula

단순 선형 회귀 모의 환경에서의 경우와 동일하게 본 식 (3.19) 내에 존재하는 단편 회귀 계수 $\beta_0, \beta_1, \dots, \beta_p$ 단항 수치들은 전부 도출 미지수이며 단락 필수적으로 모델 추정이 동반되어야 도합 합니다. 단수 추정치 단위들로 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 이 주어졌을 때 우리는 다음의 수식을 사용해 예측을 내릴 수 있습니다.

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals 

이 변수 파라미터들은 앞선 단순 선형 회귀 단락의 맥락에서 우리가 다루었던 것과 모종 동일한 최소 제곱 접근 방식을 사용하여 단도 추정 산출됩니다. 우리는 응당 잔차 단위 제곱합을 최소로 수렴 파기하기 도단 위해 $\beta_0, \beta_1, \dots, \beta_p$ 치수를 모구 고안 선택합니다.

$$
\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)
$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4

본 수식 단락 (3.22) 의 모델 제곱합을 최소로 부합 분산시키는 추정 계수 산수 값 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 수치들이 곧 다중 최소 제곱 회귀 계수 산수 추정치들입니다. (3.4) 식에 기재된 단순 모델 선형 모의 회귀 도출 추정치들과는 지극히 상이하게, 이러한 다중 모델 회귀 계수 추정의 결과치들은 통상 행렬 대수학 산식을 직결 사용해야 지수 도출이 무난 타당할 만큼 구조가 사뭇 꽤나 복잡한 체계의 폼을 단위 띱니다. 이러한 연유 탓에, 우리는 통계 본서 내에 그 실 수식을 굳이 제출 전면 기재하지는 통지 않겠습니다. 어떠한 종단 통계 분석용 소프트웨어 단지 패키지 프로그램이든 가뿐히 결단 이 계수 산수 추정치 산출을 전부 문제없이 계산해 규명 도출할 수 있으며, 이 장 후반부 결락 내용에선 구체적으로 통계 패키지 `R` 수단을 투사하여 이것들을 수월히 처리 계산하는 활용 방법을 시연 포괄 보여드릴 것입니다. 이어지는 그림 3.4 모델 도표는

<br>
<p align="center">
  <img src="./img/3_4.png" alt="In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.">
</p>
<br>

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._

**FIGURE 3.4.** _단일 두 개의 독립 예측 요인과 오직 단 한 개의 응답 종속 단위를 지닌 통칭 3차원 공간 단면 모델 설정에서 볼 때, 최소 체계 제곱 적합 모델의 회귀선은 평면 투사선이 됩니다. 이 평면 기준은 매 개별 관측단 단위(적색 점선 붉은 점 표시 단형)와 모델 해당 투사 평면 사이의 각각 분할 수직 거리의 도달 최고 제곱합을 철저히 최소 치수로 통단 축소 단일하기 위해 표본 선택 도단 결지 모구 도출됩니다._

illustrates an example of the least squares fit to a toy data set with $p=2$ predictors.

$p=2$ 개수의 다단 예측 변수를 지닌 소형 장난감 연습용 모델 토이 데이터 분석 세트에 무단 투입 적용해 본 전단 최소 제곱 체계 예측 회귀선상 적합 사례를 예시로 삽입 조립 보여줍니다.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data. We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales. Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates. However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86. This illustrates that the simple and multiple regression coefficients can be quite different. This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`. By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the

3.2 Multiple Linear Regression 83 

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |
| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |
| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |
| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | $0.8599$ |



**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._ 

| | `TV` | `radio` | `newspaper` | `sales` |
| :--- | :--- | :--- | :--- | :--- |
| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |
| `radio` | 0.0548 | 1.0000 | 0.3541 | 0.5762 |
| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |
| `sales` | 0.7822 | 0.5762 | 0.2283 | 1.0000 |



**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._ 

opposite? In fact it does. Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5. Notice that the correlation between `radio` and `newspaper` is 0.35. This indicates that markets with high newspaper advertising tend to also have high radio advertising. Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales. Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets. Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales. So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` . 

This slightly counterintuitive result is very common in many real life situations. Consider an absurd example to illustrate the point. Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper` . Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks. In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks. A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature. 

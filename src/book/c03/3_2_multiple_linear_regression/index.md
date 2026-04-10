---
layout: default
title: "index"
---

# 3.2 Multiple Linear Regression 

Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the `Advertising` data, we have examined the relationship between sales and TV advertising. We also have data for the amount of money spent advertising on the radio and in newspapers, and we may want to know whether either of these two media is associated with sales. How can we extend our analysis of the advertising data in order to accommodate these two additional predictors? 

One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the amount spent on radio advertisements. Results are shown in Table 3.3 (top table). We find that a $\$1,000$ increase in spending on radio advertising is associated with an increase in sales of around 203 units. Table 3.3 (bottom table) contains the least squares coefficients for a simple linear regression of sales onto newspaper advertising budget. A $\$1,000$ increase in newspaper advertising budget is associated with an increase in sales of approximately 55 units. 

3.2 Multiple Linear Regression 81 

However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertising media budgets, since each of the budgets is associated with a separate regression equation. Second, each of the three regression equations ignores the other two media in forming estimates for the regression coefficients. We will see shortly that if the media budgets are correlated with each other in the 200 markets in our data set, then this can lead to very misleading estimates of the association between each media budget and sales. 

Instead of fitting a separate simple linear regression model for each predictor, a better approach is to extend the simple linear regression model (3.5) so that it can directly accommodate multiple predictors. We can do this by giving each predictor a separate slope coefficient in a single model. In general, suppose that we have $p$ distinct predictors. Then the multiple linear regression model takes the form 

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon \quad (3.19)
$$

where $X_j$ represents the $j$th predictor and $$\beta_j$$ quantifies the association between that variable and the response. We interpret $$\beta_j$$ as the _average_ effect on $Y$ of a one unit increase in $X_j$, _holding all other predictors fixed_. In the advertising example, (3.19) becomes

$$
\text{sales} = \beta_0 + \beta_1 \times \text{TV} + \beta_2 \times \text{radio} + \beta_3 \times \text{newspaper} + \epsilon \quad (3.20)
$$

---

## Sub-Chapters (하위 목차)

### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)
* [문서로 이동하기](./3_2_1_estimating_the_regression_coefficients/)

여러 개의 설명 변수를 모두 포함한 다차원 공간에서 평균 잔차 제곱합을 최소화하는 하이퍼플레인을 찾는 과정을 배웁니다.
단순 회귀 때와 비교해 계수의 의미가 어떻게 변하는지 확인합니다.

### 3.2.2 Some Important Questions (중요한 질문들)
* [문서로 이동하기](./3_2_2_some_important_questions/)

다중 선형 회귀 모델을 사용할 때 답해야 하는 주요 질문(변수들의 유의성, 모델 적합도, 예측)들을 제기합니다.
이후의 소단원들을 통해 해당 질문들에 대한 단계적 통계 검증 프로세스를 다룹니다.

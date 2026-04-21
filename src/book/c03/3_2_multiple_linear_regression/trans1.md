---
layout: default
title: "trans1"
---

[< 3.1.3 Assessing The Accuracy Of The Model](../3_1_simple_linear_regression/3_1_3_assessing_the_accuracy_of_the_model/trans1.html) | [3.2.1 Estimating The Regression Coefficients >](3_2_1_estimating_the_regression_coefficients/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 3.2 Multiple Linear Regression

# 3.2 다중 선형 회귀 (Multiple Linear Regression)

Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the `Advertising` data, we have examined the relationship between sales and TV advertising. We also have data for the amount of money spent advertising on the radio and in newspapers, and we may want to know whether either of these two media is associated with sales. How can we extend our analysis of the advertising data in order to accommodate these two additional predictors?

단순 선형 회귀는 단일 예측 변수를 기반으로 응답을 예측하는 유용한 접근법입니다. 하지만 실제로는 둘 이상의 예측 변수를 갖는 경우가 빈번합니다. 예를 들어, `Advertising` 데이터에서 우리는 판매량과 TV 광고 간의 관계를 살펴보았습니다. 우리는 또한 라디오와 신문 광고에 지출된 비용에 대한 데이터도 가지고 있으며, 이 두 매체 중 하나라도 판매량과 연관되어 있는지 알고 싶을 수 있습니다. 이 두 개의 추가 파라미터를 수용하기 위해 광고 데이터 분석을 어떻게 확장할 수 있을까요?

One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the amount spent on radio advertisements. Results are shown in Table 3.3 (top table). We find that a $\$1,000$ increase in spending on radio advertising is associated with an increase in sales of around 203 units. Table 3.3 (bottom table) contains the least squares coefficients for a simple linear regression of sales onto newspaper advertising budget. A $\$1,000$ increase in newspaper advertising budget is associated with an increase in sales of approximately 55 units.

한 가지 옵션은 서로 다른 광고 매체를 예측 변수로 사용하는 세 번의 별개 단순 선형 회귀를 실행하는 것입니다. 예를 들어, 라디오 광고 지출액을 바탕으로 판매량을 예측하도록 단순 선형 회귀 모델을 적합할 수 있습니다. 결과는 표 3.3 (위쪽 표) 에 나와 있습니다. 우리는 라디오 광고 지출이 $\$1,000$ 증가할 때마다 매출이 약 203 단위 증가하는 것과 관련이 있음을 발견했습니다. 표 3.3 (아래쪽 표) 은 판매량을 신문 광고 예산에 대해 단순 선형 회귀를 돌린 최소 제곱 계수들을 포함합니다. 신문 광고 예산의 $\$1,000$ 증가는 약 55 단위의 판매량 증가와 연관이 있습니다.

However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertising media budgets, since each of the budgets is associated with a separate regression equation. Second, each of the three regression equations ignores the other two media in forming estimates for the regression coefficients. We will see shortly that if the media budgets are correlated with each other in the 200 markets in our data set, then this can lead to very misleading estimates of the association between each media budget and sales.

하지만 매 예측 변수마다 별개의 단순 선형 모델을 여러 번 각각 적합시키는 접근법은 전적으로 만족스럽지가 못합니다. 무엇보다도 세 매체 광고 예산이 주어졌을 때 이를 기반으로 어떻게 단일한 판매 예측치를 도출할지가 불분명한데, 그 이유는 각각의 예산이 분리된 별개의 회귀 방정식과 묶여 있기 때문입니다. 둘째로, 세 개의 각 예측 회귀 방정식들이 자가 회귀 계수를 형성 산출할 때 나머지 다른 두 매체는 철저히 무시하게 됩니다. 만약 우리 200개 규모의 데이터 세트 시장 내에서 다른 매체별 예산들이 피차 서로 밀접하게 상관관계를 지니고 있을 경우, 이러한 접근법이 매체별 예산과 판매량 간의 결부 관계 분석에 관해 매우 심각하게 오도된 추정치를 초래할 수 있음을 잠시 후 확인하게 될 것입니다.

Instead of fitting a separate simple linear regression model for each predictor, a better approach is to extend the simple linear regression model (3.5) so that it can directly accommodate multiple predictors. We can do this by giving each predictor a separate slope coefficient in a single model. In general, suppose that we have $p$ distinct predictors. Then the multiple linear regression model takes the form

매번 각 개별 요인마다 분리된 선형 모델을 단독 적합시키는 것보다 차라리 더 나은 접근법은 선형 회귀 모델 (3.5) 체계 자체를 크게 확장하여 다수의 예측 변수를 직접 통째로 한 번에 수용할 수 있게 고치는 길입니다. 우리는 하나의 단일 모델 내에서 각 예측 변수마다 독립적인 개별 기울기 계수를 제공해 주며 이 작업을 원활히 진행할 수 있습니다. 일반적으로, 우리에게 서로 구별되는 독립된 $p$ 개의 예측 변수가 있다고 설정합시다. 그렇다면 다중 선형 회귀 모의 방식은 필연적으로 다음과 같은 형태를 띱니다.

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon \quad (3.19)
$$

where $X_j$ represents the $j$th predictor and $$\beta_j$$ quantifies the association between that variable and the response. We interpret $$\beta_j$$ as the _average_ effect on $Y$ of a one unit increase in $X_j$, _holding all other predictors fixed_. In the advertising example, (3.19) becomes

여기서 $X_j$ 는 $j$번째 예측 변수를 나타내며 $\beta_j$ 는 해당 변수와 응답 사이의 연관성을 정량화합니다. 우리는 $\beta_j$ 를 _나머지 모든 예측 변수들이 고정되어 있을 때_ $X_j$ 의 1 단위 증가가 $Y$ 에 미치는 _평균적인_ 효과로 해석합니다. 광고 데이터 예제로 볼 때, (3.19) 식은 다음과 같이 됩니다.

$$
\text{sales} = \beta_0 + \beta_1 \times \text{TV} + \beta_2 \times \text{radio} + \beta_3 \times \text{newspaper} + \epsilon \quad (3.20)
$$

---


### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)

여러 개의 설명 변수를 모두 포함한 다차원 공간에서 평균 잔차 제곱합을 최소화하는 하이퍼플레인을 찾는 과정을 배웁니다.
단순 회귀 때와 비교해 계수의 의미가 어떻게 변하는지 확인합니다.

### 3.2.2 Some Important Questions (중요한 질문들)

다중 선형 회귀 모델을 사용할 때 답해야 하는 주요 질문(변수들의 유의성, 모델 적합도, 예측)들을 제기합니다.
이후의 소단원들을 통해 해당 질문들에 대한 단계적 통계 검증 프로세스를 다룹니다.

---

## Sub-Chapters (하위 목차)


[< 3.1.3 Assessing The Accuracy Of The Model](../3_1_simple_linear_regression/3_1_3_assessing_the_accuracy_of_the_model/trans1.html) | [3.2.1 Estimating The Regression Coefficients >](3_2_1_estimating_the_regression_coefficients/trans1.html)

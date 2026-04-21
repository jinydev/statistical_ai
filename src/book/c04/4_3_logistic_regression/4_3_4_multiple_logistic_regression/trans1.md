---
layout: default
title: "trans1"
---

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans1.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.4 Multiple Logistic Regression
# 4.3.4. 다중 로지스틱 회귀 (Multiple Logistic Regression)

We now consider the problem of predicting a binary response using multiple predictors.
우리는 이제 다수의 예측 변수를 사용하여 이진 응답을 예측하는 문제를 고려합니다.

By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:
3장의 단순 선형 회귀에서 다중 선형 회귀로의 확장에 유추하여, 우리는 식 (4.4)를 다음과 같이 일반화할 수 있습니다:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.6)
$$

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.7)
$$

Just as in Section 4.3.2, we use the maximum likelihood method to estimate $\beta_0, \beta_1, \dots, \beta_p$.
4.3.2 절에서와 마찬가지로, 우리는 $\beta_0, \beta_1, \dots, \beta_p$를 추정하기 위해 최대 우도법을 사용합니다.

Table 4.3 shows the coefficient estimates for a logistic regression model that uses `balance` , `income` (in thousands of dollars), and `student` status to predict probability of `default`.
표 4.3은 `default` 확률을 예측하기 위해 `balance`, `income`(천 달러 단위), 그리고 `student` 상태를 사용하는 로지스틱 회귀 모델에 대한 계수 추정치를 보여줍니다.

There is a surprising result here.
여기에 놀라운 결과가 있습니다.

The _p_-values associated with `balance` and the dummy variable for `student` status are very small, indicating that each of these variables is associated with the probability of `default`.
`balance` 및 `student` 상태에 대한 더미 변수와 관련된 *p*-값이 매우 작으며, 이는 이 변수들 각각이 `default` 확률과 연관되어 있음을 나타냅니다.

However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than nonstudents.
그러나 더미 변수의 계수는 음수이며, 이는 학생들이 학생이 아닌 사람들보다 체납할 가능성이 낮음을 나타냅니다.

In contrast, the coefficient for the dummy variable is positive in Table 4.2.
이와는 대조적으로, 표 4.2에서 해당 더미 변수의 계수는 양수입니다.

How is it possible for student status to be associated with an _increase_ in probability of default in Table 4.2 and a _decrease_ in probability of default in Table 4.3?
학생 상태가 표 4.2에서는 연체 확률의 **증가**와 연관되고 표 4.3에서는 연체 확률의 **감소**와 연관되는 것이 어떻게 가능할까요?

The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox.
그림 4.3의 왼쪽 패널은 이 명백해 보이는 역설을 그래픽으로 설명해 줍니다.

The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance.
주황색 및 파란색 실선은 각각 학생과 비학생에 대한 평균 연체율을 신용 카드 잔고의 함수로 보여줍니다.

The negative coefficient for `student` in the multiple logistic regression indicates that _for a fixed value of_ `balance` _and_ `income`, a student is less likely to default than a non-student.
다중 로지스틱 회귀 결과에서 `student` 변수의 부정적인(음의) 계수는, `balance`와 `income`의 **값이 고정되어 있을 때**, 학생이 학생이 아닌 사람보다 파산할 가능성이 낮다는 것을 의미합니다.

Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of `balance`.
제로, 그림 4.3의 왼쪽 패널에서 우리는 모든 `balance` 값에 대해 학생 체납률이 비학생 체납률과 같거나 그 아래에 위치하는 것을 관찰할 수 있습니다.

But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of `balance` and `income`, suggest the opposite effect: the overall student default rate is higher than the non-student default rate.
그러나 모든 `balance` 및 `income` 값에 대해 평균화된 학생 및 비학생의 파산 비율을 보여주는 플롯 바닥 근처의 수평 파선들은 정반대의 효과를 시사합니다: 즉 전체적인 학생 연체율이 더 높습니다.

Consequently, there is a positive coefficient for `student` in the single variable logistic regression output shown in Table 4.2.
결과적으로 표 4.2에 표시된 단일 변수 로지스틱 회귀 결과에는 `student`에 대한 양의 계수가 존재합니다.

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy.
그림 4.3의 오른쪽 패널은 이런 불일치에 대한 설명을 제공합니다.

The variables `student` and `balance` are correlated.
`student`와 `balance` 변수는 상관관계가 있습니다.

Students tend to hold higher levels of debt, which is in turn associated with higher probability of default.
학생들은 더 높은 수준의 부채를 보유하는 경향이 있으며, 이는 결국 더 높은 파산 확률과 연관됩니다.

In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates.
다시 말해, 학생들은 거대한 신용 카드 잔고를 가질 가능성이 더 높으며, 우리가 그림 4.3의 왼쪽 패널에서 알 수 있듯이 이는 높은 연체율로 이어지는 경향이 있습니다.

Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students.
따라서, 특정 신용 카드 잔고가 주어진 개별 학생이 **동일한** 신용 카드 잔고를 가진 비학생보다 파산 확률이 낮은 경향이 있을지라도, 전체적으로 학생들이 더 높은 신용 카드 잔고를 갖는 경향이 있다는 사실은 전체적으로 학생들이 비학생보다 더 높은 비율로 위약하는 경향이 있음을 의미합니다.

This is an important distinction for a credit card company that is trying to determine to whom they should offer credit.
이것은 누구에게 신용 카드를 제공해야 할지 결정하려는 신용 카드 회사에게 중요한 구별입니다.

A student is riskier than a non-student if no information about the student’s credit card balance is available.
만약 해당 학생의 신용 카드 잔고에 대해 확인할 수 있는 정보가 전혀 없다면 학생은 학생이 아닌 사람보다 더 위험합니다.

However, that student is less risky than a non-student _with the same credit card balance_!
그러나 **동일한 신용 카드 잔고를 가진** 비학생보다는 그 학생이 덜 위험합니다!

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant.
이 간단한 예제는 여러 다른 예측 변수들도 같이 연관될 수 있을 때 오직 단일 예측 변수만 포함한 회귀 분석을 수행하는 것과 관련된 위험성과 미묘함을 잘 보여줍니다.

As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors.
선형 회귀 설정에서와 마찬가지로, 오직 한 개의 예측 변수만을 사용하여 얻은 결과는 여러 개의 예측 변수를 사용하여 얻은 결과와 매우 다를 수 있으며, 특히 예측 변수들 사이에 상관관계가 존재할 때 그렇습니다.

In general, the phenomenon seen in Figure 4.3 is known as _confounding_.
일반적으로, 이 그림 4.3에서 목격된 이러한 현상을 **교란(confounding)** 이라고 부릅니다.

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions.
표 4.3에서 얻은 회귀 계수에 대한 추정치들을 식 (4.7)에 대입함으로써 우리는 예측을 수행할 수 있습니다.

For example, a student with a credit card balance of $1,500 and an income of $40,000 has an estimated probability of default of
예를 들어, 신용 카드 잔고가 \$1,500이고 소득이 \$40,000인 한 학생의 추정된 파산 확률은 다음과 같습니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}} = 0.058
$$

A non-student with the same balance and income has an estimated probability of default of
위와 동일한 잔고와 수입을 가진 어떤 비학생(non-student)에 대한 파산 추정 확률은 다음과 같이 산출됩니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}} = 0.105
$$

(Here we multiply the `income` coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with `income` measured in units of $1,000.)
(여기서 우리는 수입 40,000을 넣는 대신 식에서 표 4.3의 `income` 계수 추정치에 단지 40만을 곱하게 되는데, 왜냐하면 그 해당 표에서 모형 적합 시 `income`의 단위가 \$1,000 였기 때문입니다.)

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters (하위 목차)

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans1.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans1.html)

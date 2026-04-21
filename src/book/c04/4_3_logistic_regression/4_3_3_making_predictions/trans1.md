---
layout: default
title: "trans1"
---

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans1.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.3 Making Predictions
# 4.3.3 예측하기 (Making Predictions)

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a `balance` of $1,000 is
일단 $\beta$ 계수들이 정상적으로 추정되고 나면, 우리는 주어진 그 어떠한 임의의 신용카드 잔고에 대해서도 체납(`default`) 확률을 곧바로 계산해 낼 수 있습니다. 예를 들어, 표 4.1의 방정식에 세팅된 계수 산출물들을 이용 시, 잔고가 \$1,000 인 특정 개인의 파산 확률은 다음과 같이 예측됩니다.

$$
\hat{p}(X) = \frac{e^{-10.6513 + 0.0055 \times 1000}}{1 + e^{-10.6513 + 0.0055 \times 1000}} = 0.00576
$$

which is below 1%. In contrast, the predicted probability of default for an individual with a `balance` of $2,000 is much higher, and equals 0.586 or 58.6%.
계산 결과 $0.00576$ 이 나왔으며, 이는 1%도 채 안 되는 매우 낮은 수치입니다. 이와는 정반대로, 잔고 계좌에 \$2,000 이 들어있는 개인의 예상 파산 확률 수치는 훨씬 더 치솟으며 0.586, 퍼센트로 환산 시 무려 58.6% 에 육박하게 됩니다.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the `Default` data set contains the qualitative variable `student` . To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students.
우리는 3.3.1 단원에서 배웠던 **더미 변수(Dummy Variable)** 0/1 스위치 접근법을 가져와서 로지스틱 회귀 모델에 '질적(문자형)' 예측 변수를 얼마든지 밀어 넣을 수 있습니다. 일례로 본 `Default` 실습 데이터셋은 학생이냐 아니냐를 나타내는 질적 변수 `student` 를 포함하고 있습니다. 오직 학생 여부만을 예측 변수로 삼아 구동되는 확률 모델을 훈련하기 위해서는, 단순히 학생이면 1 값으로 불이 켜지고 학생이 아니면 0 이 들어가는 더미 변수를 하나 창조해 내기만 하면 됩니다.

The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated _p_-value is statistically significant. This indicates that students tend to have higher default probabilities than non-students:
오직 이 단일한 학생 신분 변수를 통해 채무 불이행 파산율을 예측해 낸 로지스틱 모형의 결과표는 책의 표 4.2에서 확인하실 수 있습니다. 저 '학생 여부 더미 변수' 자리에 할당된 계수는 양수(Positive, +)이며 연달아 붙어있는 _p_-값은 통계적으로 심각하게 유의미한 수준입니다. 이것은 명확하게 **학생 신분인 사람의 그룹이 일반인보다 파산할 확률이 평균적으로 훨씬 더 높은 경향**이 있다는 것을 우리에게 지목합니다:

$$
\begin{align*}
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{Yes}) &= \frac{e^{-3.5041 + 0.4049 \times 1}}{1 + e^{-3.5041 + 0.4049 \times 1}} = 0.0431 \\
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{No})  &= \frac{e^{-3.5041 + 0.4049 \times 0}}{1 + e^{-3.5041 + 0.4049 \times 0}} = 0.0292
\end{align*}
$$

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans1.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans1.html)

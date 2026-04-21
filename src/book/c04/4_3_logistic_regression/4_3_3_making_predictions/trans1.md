---
layout: default
title: "trans1"
---

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans1.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.3 Making Predictions
# 4.3.3. 예측하기 (Making Predictions)

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance.
일단 계수들이 추정되고 나면, 우리는 상정된 임의의 신용카드 잔고에 대해 파산(`default`) 확률을 계산할 수 있습니다.

For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a `balance` of $1,000 is
예를 들어, 표 4.1에 주어진 계수 추정치를 사용하면 잔고가 $1,000인 개인의 체납 확률을 다음과 같이 예측합니다:

$$
\hat{p}(X) = \frac{e^{-10.6513 + 0.0055 \times 1000}}{1 + e^{-10.6513 + 0.0055 \times 1000}} = 0.00576
$$

which is below 1%.
이는 1% 미만입니다.

In contrast, the predicted probability of default for an individual with a `balance` of $2,000 is much higher, and equals 0.586 or 58.6%.
이와는 대조적으로, 잔고가 $2,000인 개인의 예측 체납 확률은 훨씬 더 높으며, 0.586 즉 58.6%입니다.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1.
Section 3.3.1의 더미 변수(dummy variable) 접근법을 사용하면 로지스틱 회귀 모델에 정성적(질적) 예측 변수를 사용할 수 있습니다.

As an example, the `Default` data set contains the qualitative variable `student` .
예를 들어, `Default` 데이터셋에는 질적 변수인 `student`가 포함되어 있습니다.

To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students.
학생 신분을 예측 변수로 사용하는 모델을 피팅하기 위해, 우리는 학생의 경우 값이 1이 되고 학생이 아닌 경우 값이 0이 되는 더미 변수를 단순하게 생성합니다.

The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2.
학생의 상태로부터 체납 확률을 예측한 결과인 로지스틱 회귀 모형은 표 4.2에서 볼 수 있습니다.

The coefficient associated with the dummy variable is positive, and the associated _p_-value is statistically significant.
더미 변수와 관련된 계수는 양수이며, 결과적인 *p*-값은 통계적으로 유의미합니다.

This indicates that students tend to have higher default probabilities than non-students:
이 수치는 학생들이 학생이 아닌 사람들보다 더 높은 체납 확률을 가지는 경향이 있음을 나타냅니다:

$$
\begin{align*}
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{Yes}) &= \frac{e^{-3.5041 + 0.4049 \times 1}}{1 + e^{-3.5041 + 0.4049 \times 1}} = 0.0431 \\
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{No})  &= \frac{e^{-3.5041 + 0.4049 \times 0}}{1 + e^{-3.5041 + 0.4049 \times 0}} = 0.0292
\end{align*}
$$

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters (하위 목차)

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans1.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans1.html)

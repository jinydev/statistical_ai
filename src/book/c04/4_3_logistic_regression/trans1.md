---
layout: default
title: "trans1"
---

[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/trans1.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3 Logistic Regression
# 4.3. 로지스틱 회귀 (Logistic Regression)

Consider again the `Default` data set, where the response `default` falls into one of two categories, `Yes` or `No`.
종속 변수 `default`(체납 여부)가 `Yes` 와 `No` 라는 두 범주 중 하나에 속하는 `Default` 데이터셋을 다시 생각해 보겠습니다.

Rather than modeling this response $Y$ directly, logistic regression models the _probability_ that $Y$ belongs to a particular category.
로지스틱 회귀는 이런 반응 변수 $Y$를 직접적으로 모델링하는 대신에, $Y$가 특정 카테고리에 속하게 될 **확률(Probability)** 자체를 모델링합니다.

For the `Default` data, logistic regression models the probability of default.
`Default` 데이터의 경우, 로지스틱 회귀는 파산할 확률을 수식으로 짭니다.

For example, the probability of default given `balance` can be written as
예를 들어 잔고(`balance`)가 주어졌을 때 파산할 확률은 다음과 같이 작성할 수 있습니다:

$$
p(\text{balance}) = \text{Pr}(\text{default} = \text{Yes} \mid \text{balance})
$$

The values of Pr(`default` = `Yes` $\mid$ `balance`), which we abbreviate $p(\text{balance})$, will range between 0 and 1.
우리가 짧게 $p(\text{balance})$ 라고 줄여서 부를 $\text{Pr}(\text{default} = \text{Yes} \mid \text{balance})$ 의 값은 언제나 0과 1 사이에서만 변동하게 될 것입니다.

Then for any given value of `balance` , a prediction can be made for `default`.
그러면 어떤 특정한 `balance` 값이 주어지든 우리는 `default` 에 대한 예측을 내릴 수 있습니다.

For example, one might predict default = Yes for any individual for whom $p(\text{balance}) > 0.5$.
예를 들어, 어떤 카드사는 $p(\text{balance}) > 0.5$ (50%)가 넘어가는 모든 개인에 대해 체납할 것이라고 예측할 수 있습니다.

Alternatively, if a company wishes to be conservative in predicting individuals who are at risk for default, then they may choose to use a lower threshold, such as $p(\text{balance}) > 0.1$.
반면 만약 카드사가 체납 위험자를 잡아내는 데 매우 보수적이고 엄격하고 싶다면, 그들은 $p(\text{balance}) > 0.1$ (10%) 와 같은 훨씬 더 낮은 커트라인 기준치(Threshold)를 사용하는 것을 대안으로 선택할 수도 있습니다.

---

### 4.3.1 The Logistic Model (로지스틱 모형)

### 4.3.2 Estimating the Regression Coefficients (회귀 계수 추정)

### 4.3.3 Making Predictions (예측하기)

### 4.3.4 Multiple Logistic Regression (다중 로지스틱 회귀)

### 4.3.5 Multinomial Logistic Regression (다항 로지스틱 회귀)

---

## Sub-Chapters (하위 목차)

[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/trans1.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/trans1.html)

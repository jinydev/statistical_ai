---
layout: default
title: "index"
---

[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/index.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.3 Logistic Regression

Consider again the `Default` data set, where the response `default` falls into one of two categories, `Yes` or `No`. Rather than modeling this response $Y$ directly, logistic regression models the _probability_ that $Y$ belongs to a particular category.

For the `Default` data, logistic regression models the probability of default. For example, the probability of default given `balance` can be written as

$$
p(\text{balance}) = \text{Pr}(\text{default} = \text{Yes} \mid \text{balance})
$$

The values of Pr(`default` = `Yes` $\mid$ `balance`), which we abbreviate $p(\text{balance})$, will range between 0 and 1. Then for any given value of `balance` , a prediction can be made for `default`. For example, one might predict default = Yes for any individual for whom $p(\text{balance}) > 0.5$. Alternatively, if a company wishes to be conservative in predicting individuals who are at risk for default, then they may choose to use a lower threshold, such as $p(\text{balance}) > 0.1$.

---

### 4.3.1 The Logistic Model

### 4.3.2 Estimating the Regression Coefficients

### 4.3.3 Making Predictions

### 4.3.4 Multiple Logistic Regression

### 4.3.5 Multinomial Logistic Regression

---

## Sub-Chapters


[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/index.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/index.html)

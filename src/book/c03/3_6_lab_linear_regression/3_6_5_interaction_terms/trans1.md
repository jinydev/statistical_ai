---
layout: default
title: "trans1"
---

[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/trans1.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.6.5 Interaction Terms_

# 3.6.5 상호 작용 항 실습

It is easy to include interaction terms in a linear model using `ModelSpec()`.

이처럼 기본 `ModelSpec()` 도구를 차용하면 선형 모델 체제 속에 다변수 간의 상호 작용 항(interaction terms) 지표를 거뜬히 손쉽게(easy) 포함해 설계 삽입해 넣을 수 있습니다. Including a tuple `("lstat", "age")` tells the model matrix builder to include an interaction term between `lstat` and `age`.

예컨대 튜플 묶음 형태인 `("lstat", "age")` 조각을 연산식에 명시 귀속(Including)해 주면, 이는 행렬 조합기(builder) 측에게 두 변수 `lstat` 과 `age` 사이를 매개하는 실질적 상호 작용 항을 산입 포함하라는 명확한 지시(tells)로 작동합니다.

```
In [31]: X = MS(['lstat',
                'age',
                ('lstat', 'age')]).fit_transform(Boston)
model2 = sm.OLS(y, X)
summarize(model2.fit())
```

```
Out[31]:           coef  std err       t  P>|t|
intercept 36.0885   1.470  24.553  0.000
lstat     -1.3921   0.167  -8.313  0.000
age       -0.0007   0.020  -0.036  0.971
lstat:age  0.0042   0.002   2.244  0.025
```

---

## Sub-Chapters (하위 목차)


[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/trans1.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/trans1.html)

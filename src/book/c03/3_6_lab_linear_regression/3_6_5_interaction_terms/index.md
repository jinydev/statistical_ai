---
layout: default
title: "index"
---

[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/index.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.5 Interaction Terms_

It is easy to include interaction terms in a linear model using `ModelSpec()`.

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

## Sub-Chapters


[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/index.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/index.html)

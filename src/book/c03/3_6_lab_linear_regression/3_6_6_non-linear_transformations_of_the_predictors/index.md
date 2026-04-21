---
layout: default
title: "index"
---

[< 3.6.5 Interaction Terms](../3_6_5_interaction_terms/index.html) | [3.6.6.1 In 33 Anovalmresults1 Results3 >](3_6_6_1_in_33_anovalmresults1_results3/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.6 Non-linear Transformations of the Predictors_

The model matrix builder can include terms beyond just column names and interactions.

```
In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston)
model3 = sm.OLS(y, X)
results3 = model3.fit()
summarize(results3)
```

```
Out[32]:
```

|**`Out[32]:`**|`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|
|`intercept`|`17.7151`|`0.781`|`22.681`|`0.000`|
|`poly(lstat, degree=2)[0]`|`-179.2279`|`6.733`|`-26.620`|`0.000`|
|`poly(lstat, degree=2)[1]`|`72.9908`|`5.482`|`13.315`|`0.000`|
|`age`|`0.0703`|`0.011`|`6.471`|`0.000`|

The effectively zero $p$-value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.

By default, `poly()` creates a basis matrix for inclusion in the model matrix whose columns are _orthogonal polynomials_ , which are designed for sta- orthogonal ble least squares computations. [13]

---

---

## Sub-Chapters


[< 3.6.5 Interaction Terms](../3_6_5_interaction_terms/index.html) | [3.6.6.1 In 33 Anovalmresults1 Results3 >](3_6_6_1_in_33_anovalmresults1_results3/index.html)

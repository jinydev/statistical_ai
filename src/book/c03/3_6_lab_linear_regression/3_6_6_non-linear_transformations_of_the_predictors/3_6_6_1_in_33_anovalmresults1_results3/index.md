---
layout: default
title: "index"
---

[< 3.6.6 Non-Linear Transformations Of The Predictors](../index.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# **`In [33]:`** `anova_lm(results1, results3)`

|**`Out[33]:`**|`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|
|`0`|`503.0`|`19168.13`|`0.0`|`NaN`|`NaN`|`NaN`|
|`1`|`502.0`|`14165.61`|`1.0`|`5002.52`|`177.28`|`7.47e-35`|

Here `results1` represents the linear submodel containing predictors `lstat` and `age`, while `results3` corresponds to the larger model above with a quadratic term in `lstat`.

126 3. Linear Regression

The function `anova_lm()` can take more than two nested models as input, in which case it compares every successive pair of models.

```
In [34]: ax = subplots(figsize=(8, 8))[1]
ax.scatter(results3.fittedvalues, results3.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')
```

We see that when the quadratic term is included in the model, there is little discernible pattern in the residuals.

---

## Sub-Chapters


[< 3.6.6 Non-Linear Transformations Of The Predictors](../index.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/index.html)

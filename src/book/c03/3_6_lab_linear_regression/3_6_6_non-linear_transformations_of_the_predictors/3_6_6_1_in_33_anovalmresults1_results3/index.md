---
layout: default
title: "index"
---

# **`In [33]:`** `anova_lm(results1, results3)` 

|**`Out[33]:`**||`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|---|
||`0`|`503.0`|`19168.13`|`0.0`|`NaN`|`NaN`|`NaN`|
||`1`|`502.0`|`14165.61`|`1.0`|`5002.52`|`177.28`|`7.47e-35`|



Here `results1` represents the linear submodel containing predictors `lstat` and `age` , while `results3` corresponds to the larger model above with a quadratic term in `lstat` . The `anova_lm()` function performs a hypothesis test comparing the two models. The null hypothesis is that the quadratic term in the bigger model is not needed, and the alternative hypothesis is that the bigger model is superior. Here the $F$-statistic is 177.28 and the associated $p$-value is zero. In this case the $F$-statistic is the square of the $t$-statistic for the quadratic term in the linear model summary for `results3` — a consequence of the fact that these nested models differ by one degree of 

> 13Actually, `poly()` is a wrapper for the workhorse and standalone function `Poly()` that does the work in building the model matrix. 

126 3. Linear Regression 

freedom. This provides very clear evidence that the quadratic polynomial in `lstat` improves the linear model. This is not surprising, since earlier we saw evidence for non-linearity in the relationship between `medv` and `lstat` . 

The function `anova_lm()` can take more than two nested models as input, in which case it compares every successive pair of models. That also explains why their are `NaN` s in the first row above, since there is no previous model with which to compare the first. 

```
In [34]:ax=subplots(figsize=(8,8))[1]
ax.scatter(results3.fittedvalues ,results3.resid)
ax.set_xlabel('Fittedvalue')
ax.set_ylabel('Residual')
ax.axhline(0,c='k',ls='--')
```

We see that when the quadratic term is included in the model, there is little discernible pattern in the residuals. In order to create a cubic or higher-degree polynomial fit, we can simply change the degree argument to `poly()` . 

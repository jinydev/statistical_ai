---
layout: default
title: "index"
---

# **`In [9]:`** `summarize(M)` 

```
Out[9]:
```

|||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
|`intercept`||`111.7036`|`0.729`|`153.283`|`0.000`|
|`poly(age, `|`degree=4)[0]`|`447.0679`|`39.915`|`11.201`|`0.000`|
|`poly(age, `|`degree=4)[1] `|`-478.3158`|`39.915`|`-11.983`|`0.000`|
|`poly(age, `|`degree=4)[2]`|`125.5217`|`39.915`|`3.145`|`0.002`|
|`poly(age, `|`degree=4)[3]`|`-77.9112`|`39.915`|`-1.952`|`0.051`|



Notice that the p-values are the same, and in fact the square of the t-statistics are equal to the F-statistics from the `anova_lm()` function; for example: 

```
In [10]:(-11.983)**2
```

---
layout: default
title: "index"
---

# **`Out[27]:`** `20.04` 

The test set $\text{MSE}$ is 20.04; this indicates that random forests did somewhat worse than bagging in this case. Extracting the `feature_importances_` values from the fitted model, we can view the importance of each variable. 

8.3 Lab: Tree-Based Methods 361 

```
In [28]:feature_imp=pd.DataFrame(
{'importance':RF_boston.feature_importances_},
index=feature_names)
feature_imp.sort_values(by='importance',ascending=False)
```

```
Out[28]:
```

||`importance`|
|---|---|
|`lstat`|`0.368683`|
|`rm`|`0.333842`|
|`ptratio`|`0.057306`|
|`indus`|`0.053303`|
|`crim`|`0.052426`|
|`dis`|`0.042493`|
|`nox`|`0.034410`|
|`age`|`0.024327`|
|`tax`|`0.022368`|
|`rad`|`0.005048`|
|`zn`|`0.003238`|
|`chas`|`0.002557`|



This is a relative measure of the total decrease in node impurity that results from splits over that variable, averaged over all trees (this was plotted in Figure 8.9 for a model fit to the `Heart` data). 

The results indicate that across all of the trees considered in the random forest, the wealth level of the community ( `lstat` ) and the house size ( `rm` ) are by far the two most important variables. 

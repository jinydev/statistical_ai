---
layout: default
title: "index"
---

# **`Out[53]:`** `204139.31` 

The `explained_variance_ratio_` attribute of our `PCA` object provides the _percentage of variance explained_ in the predictors and in the response using different numbers of components. This concept is discussed in greater detail in Section 12.2. 

```
In [54]:pipe.named_steps['pca'].explained_variance_ratio_
```

```
Out[54]:array([0.3831424,0.21841076])
```

Briefly, we can think of this as the amount of information about the predictors that is captured using _M_ principal components. For example, setting _M_ = 1 only captures 38.31% of the variance, while _M_ = 2 captures an additional 21.84%, for a total of 60.15% of the variance. By _M_ = 6 it increases to 88.63%. Beyond this the increments continue to diminish, until we use all _M_ = _p_ = 19 components, which captures all 100% of the variance. 

Partial Least Squares 

Partial least squares (PLS) is implemented in the `PLSRegression()` function. `PLS` 

```
In [55]:pls=PLSRegression(n_components=2,
scale=True)
pls.fit(X,Y)
```

```
Regression()
```

As was the case in PCR, we will want to use CV to choose the number of components. 

```
In [56]:param_grid={'n_components':range(1,20)}
grid=skm.GridSearchCV(pls,
param_grid,
cv=kfold,
scoring='neg_mean_squared_error')
grid.fit(X,Y)
```

As for our other methods, we plot the MSE. 

```
In [57]:pls_fig,ax=subplots(figsize=(8,8))
n_comp=param_grid['n_components']
ax.errorbar(n_comp,
-grid.cv_results_['mean_test_score'],
grid.cv_results_['std_test_score']/np.sqrt(K))
ax.set_ylabel('Cross-validatedMSE',fontsize=20)
ax.set_xlabel('#principalcomponents',fontsize=20)
ax.set_xticks(n_comp[::2])
ax.set_ylim([50000,250000]);
```

CV error is minimized at 12, though there is little noticable difference between this point and a much lower number like 2 or 3 components. 

6.6 Exercises 283 

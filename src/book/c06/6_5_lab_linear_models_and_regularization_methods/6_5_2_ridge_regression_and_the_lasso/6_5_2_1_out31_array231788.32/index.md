---
layout: default
title: "index"
---

# **`Out[31]:`** `array([231788.32])` 

Obviously choosing _λ_ = 0 _._ 01 is arbitrary, so we will use cross-validation or the validation-set approach to choose the tuning parameter _λ_ . The object `GridSearchCV()` allows exhaustive grid search to choose such a parameter. We first use the validation set method to choose _λ_ . 

```
Grid
SearchCV()
```

```
In [32]:param_grid={'ridge__alpha':lambdas}
grid=skm.GridSearchCV(pipe,
param_grid ,
cv=validation,
scoring='neg_mean_squared_error')
grid.fit(X,Y)
grid.best_params_['ridge__alpha']
grid.best_estimator_
```

```
Out[32]:Pipeline(steps=[('scaler',StandardScaler()),
```

```
('ridge',ElasticNet(alpha=0.005899,l1_ratio=0))])
```

6.5 Lab: Linear Models and Regularization Methods 

277 

Alternatively, we can use 5-fold cross-validation. 

```
In [33]:grid=skm.GridSearchCV(pipe,
param_grid,
cv=kfold,
scoring='neg_mean_squared_error')
grid.fit(X,Y)
grid.best_params_['ridge__alpha']
grid.best_estimator_
```

Recall we set up the `kfold` object for 5-fold cross-validation on page 271. We now plot the cross-validated $\text{MSE}$ as a function of _−_ log( _λ_ ), which has shrinkage decreasing from left to right. 

```
In [34]:ridge_fig,ax=subplots(figsize=(8,8))
ax.errorbar(-np.log(lambdas),
-grid.cv_results_['mean_test_score'],
yerr=grid.cv_results_['std_test_score']/np.sqrt(K))
ax.set_ylim([50000,250000])
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
ax.set_ylabel('Cross-validatedMSE',fontsize=20);
```

One can cross-validate different metrics to choose a parameter. The default metric for `skl.ElasticNet()` is test _R_[2] . Let’s compare _R_[2] to $\text{MSE}$ for cross-validation here. 

```
In [35]:grid_r2=skm.GridSearchCV(pipe,
param_grid ,
cv=kfold)
grid_r2.fit(X,Y)
```

Finally, let’s plot the results for cross-validated _R_[2] . 

```
In [36]:r2_fig,ax=subplots(figsize=(8,8))
ax.errorbar(-np.log(lambdas),
grid_r2.cv_results_['mean_test_score'],
yerr=grid_r2.cv_results_['std_test_score']/np.sqrt(K)
)
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
ax.set_ylabel('Cross-validated$R^2$',fontsize=20);
```

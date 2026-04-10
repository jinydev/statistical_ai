---
layout: default
title: "index"
---

# The Lasso 

We saw that ridge regression with a wise choice of _λ_ can outperform least squares as well as the null model on the `Hitters` data set. We now ask whether the lasso can yield either a more accurate or a more interpretable model than ridge regression. In order to fit a lasso model, we once again use the `ElasticNetCV()` function; however, this time we use the argument `l1_ratio=1` . Other than that change, we proceed just as we did in fitting a ridge model. 

```
In [43]:lassoCV=skl.ElasticNetCV(n_alphas=100,
l1_ratio=1,
cv=kfold)
pipeCV=Pipeline(steps=[('scaler',scaler),
('lasso',lassoCV)])
pipeCV.fit(X,Y)
tuned_lasso=pipeCV.named_steps['lasso']
tuned_lasso.alpha_
```

```
Out[43]:3.147
```

|**`In [44]:`**|`lambdas, soln_array = skl.Lasso.path(Xs,`|
|---|---|
||`Y,`|
||`l1_ratio=1,`|
||`n_alphas=100)[:2]`|
||`soln_path = pd.DataFrame(soln_array.T,`|
||`columns=D.columns,`|
||`index=-np.log(lambdas))`|



We can see from the coefficient plot of the standardized coefficients that depending on the choice of tuning parameter, some of the coefficients will be exactly equal to zero. 

280 6. Linear Model Selection and Regularization 

```
In [45]:path_fig,ax=subplots(figsize=(8,8))
soln_path.plot(ax=ax,legend=False)
ax.legend(loc='upperleft')
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
ax.set_ylabel('Standardizedcoefficiients',fontsize=20);
```

The smallest cross-validated error is lower than the test set $\text{MSE}$ of the null model and of least squares, and very similar to the test $\text{MSE}$ of 115526.71 of ridge regression (page 278) with _λ_ chosen by cross-validation. 

```
In [46]:np.min(tuned_lasso.mse_path_.mean(1))
```

```
Out[46]:114690.73
```

Let’s again produce a plot of the cross-validation error. 

```
In [47]:lassoCV_fig ,ax=subplots(figsize=(8,8))
ax.errorbar(-np.log(tuned_lasso.alphas_),
tuned_lasso.mse_path_.mean(1),
yerr=tuned_lasso.mse_path_.std(1)/np.sqrt(K))
ax.axvline(-np.log(tuned_lasso.alpha_),c='k',ls='--')
ax.set_ylim([50000,250000])
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
ax.set_ylabel('Cross-validatedMSE',fontsize=20);
```

However, the lasso has a substantial advantage over ridge regression in that the resulting coefficient estimates are sparse. Here we see that 6 of the 19 coefficient estimates are exactly zero. So the lasso model with _λ_ chosen by cross-validation contains only 13 variables. 

```
In [48]:tuned_lasso.coef_
```

```
Out[48]:array([-210.01008773,243.4550306,0.,0.,
0.,97.69397357,-41.52283116,-0.,
0.,39.62298193,205.75273856,124.55456561,
-126.29986768,15.70262427,-59.50157967,75.24590036,
21.62698014,-12.04423675,-0.])
```

As in ridge regression, we could evaluate the test error of cross-validated lasso by first splitting into test and training sets and internally running cross-validation on the training set. We leave this as an exercise. 

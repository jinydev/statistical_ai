---
layout: default
title: "index"
---

# Ridge Regression 

We will use the function `skl.ElasticNet()` to fit both ridge and the lasso. To fit a _path_ of ridge regressions models, we use `skl.ElasticNet.path()` , which can fit both ridge and lasso, as well as a hybrid mixture; ridge regression corresponds to `l1_ratio=0` . It is good practice to standardize the columns of `X` in these applications, if the variables are measured in different units. Since `skl.ElasticNet()` does no normalization, we have to take care of that ourselves. Since we standardize first, in order to find coefficient estimates on the original scale, we must _unstandardize_ the coefficient estimates. The parameter $\lambda$ in (6.5) and (6.7) is called `alphas` in `sklearn` . In order to be consistent with the rest of this chapter, we use `lambdas` rather than `alphas` in what follows.[^10] 

[^10]: At the time of publication, ridge fits like the one in code chunk [22] issue unwarranted convergence warning messages; we expect these to disappear as this package matures. 

274 6. Linear Model Selection and Regularization 

```
In [22]:Xs=X-X.mean(0)[None,:]
X_scale=X.std(0)
Xs=Xs/X_scale[None,:]
lambdas=10**np.linspace(8,-2,100)/Y.std()
soln_array=skl.ElasticNet.path(Xs,
Y,
l1_ratio=0.,
alphas=lambdas)[1]
soln_array.shape
```

```
Out[22]:(19,100)
```

Here we extract the array of coefficients corresponding to the solutions along the regularization path. By default the `skl.ElasticNet.path` method fits a path along an automatically selected range of $\lambda$ values, except for the case when `l1_ratio=0` , which results in ridge regression (as is the case here).[^11] So here we have chosen to implement the function over a grid of values ranging from $\lambda = 10^8$ to $\lambda = 10^{-2}$ scaled by the standard deviation of $y$ , essentially covering the full range of scenarios from the null model containing only the intercept, to the least squares fit. 

Associated with each value of $\lambda$ is a vector of ridge regression coefficients, that can be accessed by a column of `soln_array` . In this case, `soln_array` is a 19 _×_ 100 matrix, with 19 rows (one for each predictor) and 100 columns (one for each value of $\lambda$ ). 

We transpose this matrix and turn it into a data frame to facilitate viewing and plotting. 

```
In [23]:
```

```
soln_path=pd.DataFrame(soln_array.T,
columns=D.columns,
index=-np.log(lambdas))
soln_path.index.name='negativelog(lambda)'
soln_path
```

|**`Out[23]:`**||`AtBat`|`Hits`|`HmRun`|`Runs`|`...`|
|---|---|---|---|---|---|---|
||`negative`||||||
||`log(lambda)`||||||
||`-12.310855`|`0.000800`|`0.000889`|`0.000695`|`0.000851`|`...`|
||`-12.078271`|`0.001010`|`0.001122`|`0.000878`|`0.001074`|`...`|
||`-11.845686`|`0.001274`|`0.001416`|`0.001107`|`0.001355`|`...`|
||`-11.613102`|`0.001608`|`0.001787`|`0.001397`|`0.001710`|`...`|
||`-11.380518`|`0.002029`|`0.002255`|`0.001763`|`0.002158`|`...`|
||`...`|`...`|`...`|`...`|`...`|`...`|
||`100 rows × 19 columns`||||||



We plot the paths to get a sense of how the coefficients vary with $\lambda$ . To control the location of the legend we first set `legend` to `False` in the plot method, adding it afterward with the `legend()` method of `ax` . 

```
In [24]:path_fig,ax=subplots(figsize=(8,8))
soln_path.plot(ax=ax,legend=False)
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
```

> 11The reason is rather technical; for all models except ridge, we can find the smallest value of $\lambda$ for which all coefficients are zero. For ridge this value is _∞_ . 

6.5 Lab: Linear Models and Regularization Methods 

275 

```
ax.set_ylabel('Standardizedcoefficients',fontsize=20)
ax.legend(loc='upperleft');
```

(We have used `latex` formatting in the horizontal label, in order to format the Greek $\lambda$ appropriately.) We expect the coefficient estimates to be much smaller, in terms of $\ell_2$ norm, when a large value of $\lambda$ is used, as compared to when a small value of $\lambda$ is used. (Recall that the $\ell_2$ norm is the square root of the sum of squared coefficient values.) We display the coefficients at the 40th step, where $\lambda$ is 25.535. 

```
In [25]:beta_hat=soln_path.loc[soln_path.index[39]]
lambdas[39],beta_hat
```

|**`Out[25]:`**|`(25.535,`||
|---|---|---|
||`AtBat`|`5.433750`|
||`Hits`|`6.223582`|
||`HmRun`|`4.585498`|
||`Runs`|`5.880855`|
||`RBI`|`6.195921`|
||`Walks`|`6.277975`|
||`Years`|`5.299767`|
||`...`|`...`|



Let’s compute the $\ell_2$ norm of the standardized coefficients. 

```
In [26]:np.linalg.norm(beta_hat)
```

```
Out[26]:24.17
```

In contrast, here is the $\ell_2$ norm when $\lambda$ is 2.44e-01. Note the much larger $\ell_2$ norm of the coefficients associated with this smaller value of $\lambda$ . 

```
In [27]:beta_hat=soln_path.loc[soln_path.index[59]]
lambdas[59],np.linalg.norm(beta_hat)
```

```
Out[27]:(0.2437,160.4237)
```

Above we normalized `X` upfront, and fit the ridge model using `Xs` . The `Pipeline()` object in `sklearn` provides a clear way to separate feature normalization from the fitting of the ridge model itself. 

```
In [28]:ridge=skl.ElasticNet(alpha=lambdas[59],l1_ratio=0)
scaler=StandardScaler(with_mean=True,with_std=True)
pipe=Pipeline(steps=[('scaler',scaler),('ridge',ridge)])
pipe.fit(X,Y)
```

We show that it gives the same $\ell_2$ norm as in our previous fit on the standardized data. 

```
In [29]:np.linalg.norm(ridge.coef_)
```

```
Out[29]:160.4237
```

Notice that the operation `pipe.fit(X, Y)` above has changed the `ridge` object, and in particular has added attributes such as `coef_` that were not there before. 

276 6. Linear Model Selection and Regularization 

Estimating Test Error of Ridge Regression 

Choosing an _a priori_ value of $\lambda$ for ridge regression is difficult if not impossible. We will want to use the validation method or cross-validation to select the tuning parameter. The reader may not be surprised that the `Pipeline()` approach can be used in `skm.cross_validate()` with either a validation method (i.e. `validation` ) or _k_ -fold cross-validation. 

We fix the random state of the splitter so that the results obtained will be reproducible. 

```
In [30]:validation=skm.ShuffleSplit(n_splits=1,
test_size=0.5,
random_state=0)
ridge.alpha=0.01
results=skm.cross_validate(ridge,
X,
Y,
scoring='neg_mean_squared_error',
cv=validation)
-results['test_score']
```

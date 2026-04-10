---
layout: default
title: "index"
---

# **`Out[4]:`** `(263, 20)` 

We first choose the best model using forward selection based on _Cp_ (6.2). This score is not built in as a metric to `sklearn` . We therefore define a function to compute it ourselves, and use it as a scorer. By default, `sklearn` tries to maximize a score, hence our scoring function computes the negative _Cp_ statistic. 

```
In [5]:defnCp(sigma2,estimator,X,Y):
"NegativeCpstatistic"
n,p=X.shape
Yhat=estimator.predict(X)
RSS=np.sum((Y-Yhat)**2)
return-(RSS+2*p*sigma2)/n
```

6.5 Lab: Linear Models and Regularization Methods 269 

We need to estimate the residual variance _σ_[2] , which is the first argument in our scoring function above. We will fit the biggest model, using all the variables, and estimate _σ_[2] based on its MSE. 

```
In [6]:design=MS(Hitters.columns.drop('Salary')).fit(Hitters)
Y=np.array(Hitters['Salary'])
X=design.transform(Hitters)
sigma2=OLS(Y,X).fit().scale
```

The function `sklearn_selected()` expects a scorer with just three arguments — the last three in the definition of `nCp()` above. We use the function `partial()` first seen in Section 5.3.3 to freeze the first argument with our estimate of _σ_[2] . 

```
In [7]:neg_Cp=partial(nCp,sigma2)
```

We can now use `neg_Cp()` as a scorer for model selection. Along with a score we need to specify the search strategy. This is done through the object `Stepwise()` in the `ISLP.models` package. The method `Stepwise.first_peak()` runs forward stepwise until any further additions to the model do not result in an improvement in the evaluation score. Similarly, the method `Stepwise.fixed_steps()` runs a fixed number of steps of stepwise search. 

```
In [8]:strategy=Stepwise.first_peak(design,
```

```
direction='forward',
max_terms=len(design.terms))
```

We now fit a linear regression model with `Salary` as outcome using forward selection. To do so, we use the function `sklearn_selected()` from the `sklearn_ ISLP.models` package. This takes a model from `statsmodels` along with a search strategy and selects a model with its `fit` method. Without specifying a `scoring` argument, the score defaults to MSE, and so all 19 variables will be selected (output not shown). 

```
selected()
```

```
In [9]:hitters_MSE=sklearn_selected(OLS,
hitters_MSE.fit(Hitters,Y)
hitters_MSE.selected_state_
```

```
strategy)
```

Using `neg_Cp` results in a smaller model, as expected, with just 10 variables selected. 

```
In [10]:hitters_Cp=sklearn_selected(OLS,
strategy,
scoring=neg_Cp)
hitters_Cp.fit(Hitters,Y)
hitters_Cp.selected_state_
```

```
Out[10]:('Assists',
'AtBat',
'CAtBat',
'CRBI',
'CRuns',
'CWalks',
'Division',
```

270 6. Linear Model Selection and Regularization 

```
'Hits',
'PutOuts',
'Walks')
```

Choosing Among Models Using the Validation Set Approach and Cross-Validation 

As an alternative to using _Cp_ , we might try cross-validation to select a model in forward selection. For this, we need a method that stores the full path of models found in forward selection, and allows predictions for each of these. This can be done with the `sklearn_selection_path()` estima- `sklearn_` tor from `ISLP.models` . The function `cross_val_predict()` from `ISLP.models` computes the cross-validated predictions for each of the models along the `path()` path, which we can use to evaluate the cross-validated $\text{MSE}$ along the path. Here we define a strategy that fits the full forward selection path. While `predict()` there are various parameter choices for `sklearn_selection_path()` , we use the defaults here, which selects the model at each step based on the biggest reduction in RSS. 

```
selection_
path()
cross_val_
predict()
```

```
In [11]:strategy=Stepwise.fixed_steps(design,
```

```
len(design.terms),
direction='forward')
full_path=sklearn_selection_path(OLS,strategy)
```

We now fit the full forward-selection path on the `Hitters` data and compute the fitted values. **`In [12]:`** `full_path.fit(Hitters, Y) Yhat_in = full_path.predict(Hitters) Yhat_in.shape` 

```
Out[12]:(263,20)
```

This gives us an array of fitted values — 20 steps in all, including the fitted mean for the null model — which we can use to evaluate in-sample MSE. As expected, the in-sample $\text{MSE}$ improves each step we take, indicating we must use either the validation or cross-validation approach to select the number of steps. We fix the y-axis to range from 50,000 to 250,000 to compare to the cross-validation and validation set $\text{MSE}$ below, as well as other methods such as ridge regression, lasso and principal components regression. 

```
In [13]:mse_fig,ax=subplots(figsize=(8,8))
insample_mse=((Yhat_in-Y[:,None])**2).mean(0)
n_steps=insample_mse.shape[0]
ax.plot(np.arange(n_steps),
insample_mse ,
'k',#colorblack
label='In-sample')
ax.set_ylabel('MSE',
fontsize=20)
ax.set_xlabel('#stepsofforwardstepwise',
fontsize=20)
ax.set_xticks(np.arange(n_steps)[::2])
ax.legend()
```

6.5 Lab: Linear Models and Regularization Methods 

271 

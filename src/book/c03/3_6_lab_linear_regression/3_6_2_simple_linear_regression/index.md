---
layout: default
title: "index"
---

[< 3.6.1 Importing Packages](../3_6_1_importing_packages/index.html) | [3.6.2.1 Out24 374 >](3_6_2_1_out24_374/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.2 Simple Linear Regression_

In this section we will construct model matrices (also called design matrices) using the `ModelSpec()` transform from `ISLP.models`.

We will use the `Boston` housing data set, which is contained in the `ISLP` package.

The `Boston` dataset records `medv` (median house value) for 506 neighborhoods around Boston.

We will build a regression model to predict `medv` using 13 predictors such as `rmvar` (average number of rooms per house), `age` (proportion of owner-occupied units built prior to 1940), and `lstat` (percent of households with low socioeconomic status).

We will use `statsmodels` for this task, a `Python` package that implements several commonly used regression methods.

We have included a simple loading function `load_data()` in the `ISLP` package:

```
In [8]: Boston = load_data("Boston")
Boston.columns
```

```
Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'],
dtype='object')
```

Type `Boston?` to find out more about these data.

We start by using the `sm.OLS()` function to fit a simple linear regression model.

Our response will be `medv` and `lstat` will be the single predictor.

For this model, we can create the model matrix by hand.

```
In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]),
'lstat': Boston['lstat']})
X[:4]
```

```
Out[9]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

We extract the response, and fit the model.

```
In [10]: y = Boston['medv']
model = sm.OLS(y, X)
results = model.fit()
```

Note that `sm.OLS()` does not fit the model; it specifies the model, and then `model.fit()` does the actual fitting.

Our `ISLP` function `summarize()` produces a simple table of the parameter estimates, their standard errors, $t$-statistics and p-values.

The function takes a single argument, such as the object `results` returned here by the `fit` method, and returns such a summary.

```
In [11]: summarize(results)
```

```
Out[11]:
```

||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|
|`intercept`|`34.5538`|`0.563`|`61.415`|`0.0`|
|`lstat`|`-0.9500`|`0.039 `|`-24.528`|`0.0`|

Before we describe other methods for working with fitted models, we outline a more useful and general framework for constructing a model matrix `X`.

A transform is an object that is created with some parameters as arguments.

The object has two main methods: `fit()` and ``.

```
.fit()
.
```

We provide a general approach for specifying models and constructing the model matrix through the transform `ModelSpec()` in the `ISLP` library.

`ModelSpec()` (renamed `MS()` in the preamble) creates a transform object, and then a pair of methods `` and `fit()` are used to construct a corresponding model matrix.

```
In [12]: design = MS(['lstat'])
design = design.fit(Boston)
X = design.transform(Boston)
X[:4]
```

```
Out[12]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

In this simple case, the `fit()` method does very little; it simply checks that the variable `'lstat'` specified in `design` exists in `Boston`.

Then `` constructs the model matrix with two columns: an `intercept` and the variable `lstat`.

These two operations can be combined with the `fit_` method.

```
In [13]: design = MS(['lstat'])
X = design.fit_transform(Boston)
X[:4]
```

```

```

```
Out[13]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

Note that, as in the previous code chunk when the two steps were done separately, the `design` object is changed as a result of the `fit()` operation.

The power of this pipeline will become clearer when we fit more complex models that involve interactions and transformations.

Let’s return to our fitted regression model.

The object `results` has several methods that can be used for inference.

We already presented a function `summarize()` for showing the essentials of the fit.

For a full and somewhat exhaustive summary of the fit, we can use the `summary()` method (output not shown).

```
In [14]: results.summary()
```

The fitted coefficients can also be retrieved as the `params` attribute of `results`.

```
In [15]: results.params
```

```
Out[15]:
```

```
intercept34.553841
lstat-0.950049
dtype:float64
```

The `get_prediction()` method can be used to obtain predictions, and produce confidence intervals and prediction intervals for the prediction of `medv` for given values of `lstat`.

```
In [16]: new_df = pd.DataFrame({'lstat': [5, 10, 15]})
newX = design.transform(new_df)
newX
```

```
Out[16]:    intercept  lstat
0        1.0     5.0
1        1.0    10.0
2        1.0    15.0
```

Next we compute the predictions at `newX`, and view them by extracting the `predicted_mean` attribute.

```
In [17]: new_predictions = results.get_prediction(newX)
new_predictions.predicted_mean
```

```
Out[17]: array([29.80359411, 25.05334734, 20.30310057])
```

We can produce confidence intervals for the predicted values.

```
In [18]: new_predictions.conf_int(alpha=0.05)
```

```
Out[18]: array([[29.00741194, 30.59977628],
       [24.47413202, 25.63256267],
       [19.73158815, 20.87461299]])
```

Prediction intervals are computing by setting `obs=True`:

```
In [19]: new_predictions.conf_int(obs=True, alpha=0.05)
```

```
Out[19]: array([[17.56567478, 42.04151344],
       [12.82762635, 37.27906833],
       [8.0777421 , 32.52845905]])
```

For instance, the 95% confidence interval associated with an `lstat` value of 10 is (24.47, 25.63), and the 95% prediction interval is (12.82, 37.28).

As expected, the confidence and prediction intervals are centered around the same point (a predicted value of 25.05 for `medv` when `lstat` equals 10), but the latter are substantially wider.

Next we will plot `medv` and `lstat` using `DataFrame.plot.scatter()`, and wish to add the regression line to the resulting plot.

3.6 Lab: Linear Regression 121

```
In [20]: def abline(ax, b, m):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim)
```

A few things are illustrated above.

First we see the syntax for defining a function: `def funcname(...)`.

The function has arguments `ax, b, m` where `ax` is an axis object for an exisiting plot, `b` is the intercept and `m` is the slope of the desired line.

Other plotting options can be passed on to `ax.plot` by including additional optional arguments as follows:

```
In [21]: def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs)
```

The addition of `*args` allows any number of non-named arguments to `abline`, while `*kwargs` allows any number of named arguments (such as `linewidth=3`) to `abline`.

In our function, we pass these arguments verbatim to `ax.plot` above.

Readers interested in learning more about functions are referred to the section on defining functions in docs.python.org/tutorial.

Let’s use our new function to add this regression line to a plot of `medv` vs. `lstat`.

```
In [22]: ax = Boston.plot.scatter('lstat', 'medv')
abline(ax,
       results.params[0],
       results.params[1],
       'r--',
       linewidth=3)
```

Thus, the final call to `ax.plot()` is `ax.plot(xlim, ylim, 'r--', linewidth=3)`.

We have used the argument `'r--'` to produce a red dashed line, and added an argument to make it of width 3.

There is some evidence for non-linearity in the relationship between `lstat` and `medv`.

We will explore this issue later in this lab.

As mentioned above, there is an existing function to add a line to a plot — `ax.axline()` — but knowing how to write such functions empowers us to create more expressive displays.

Next we examine some diagnostic plots, several of which were discussed in Section 3.3.3.

We can find the fitted values and residuals of the fit as attributes of the `results` object.

Various influence measures describing the regression model are computed with the `get_influence()` method.

As we will not use the `fig` component returned as the first value from `subplots()`, we simply capture the second returned value in `ax` below.

```
In [23]: ax = subplots(figsize=(8, 8))[1]
```

```
ax.scatter(results.fittedvalues, results.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')
```

We add a horizontal line at 0 for reference using the `ax.axhline()` method, indicating it should be black (`c='k'`) and have a dashed linestyle (`ls='--'`).

On the basis of the residual plot (not shown), there is some evidence of non-linearity.

Leverage statistics can be computed for any number of predictors using the `hat_matrix_diag` attribute of the value returned by the `get_influence()` method.

```
In [24]: infl = results.get_influence()
ax = subplots(figsize=(8, 8))[1]
ax.scatter(np.arange(X.shape[0]), infl.hat_matrix_diag)
ax.set_xlabel('Index')
ax.set_ylabel('Leverage')
np.argmax(infl.hat_matrix_diag)
```

---

---

---

## Sub-Chapters


[< 3.6.1 Importing Packages](../3_6_1_importing_packages/index.html) | [3.6.2.1 Out24 374 >](3_6_2_1_out24_374/index.html)

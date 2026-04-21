---
layout: default
title: "index"
---

[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/index.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.3 Multiple Linear Regression_

In order to fit a multiple linear regression model using least squares, we again use the `ModelSpec()` transform to construct the required model matrix and response.

```
In [25]: X = MS(['lstat', 'age']).fit_transform(Boston)
model1 = sm.OLS(y, X)
results1 = model1.fit()
summarize(results1)
```

```
Out[25]:
```

```
           coef  std err       t  P>|t|
intercept 33.2228   0.731 45.458  0.000
lstat     -1.0321   0.048 -21.416 0.000
age        0.0345   0.012  2.826  0.005
```

Notice how we have compacted the first line into a succinct expression describing the construction of `X`.

The `Boston` data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors.

```
In [26]: terms = Boston.columns.drop('medv')
terms
```

```
.columns.
drop()
```

```
Out[26]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
       'rad', 'tax', 'ptratio', 'lstat'],
      dtype='object')
```

We can now fit the model with all the variables in `terms` using the same model matrix builder.

```
In [27]: X = MS(terms).fit_transform(Boston)
model = sm.OLS(y, X)
results = model.fit()
summarize(results)
```

|**`Out[27]:`**|`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|
|`intercept`|`41.6173`|`4.936`|`8.431`|`0.000`|
|`crim`|`-0.1214`|`0.033`|`-3.678`|`0.000`|
|`zn`|`0.0470`|`0.014`|`3.384`|`0.001`|
|`indus`|`0.0135`|`0.062`|`0.217`|`0.829`|
|`chas`|`2.8400`|`0.870`|`3.264`|`0.001`|
|`nox`|`-18.7580`|`3.851`|`-4.870`|`0.000`|
|`rm`|`3.6581`|`0.420`|`8.705`|`0.000`|
|`age`|`0.0036`|`0.013`|`0.271`|`0.787`|
|`dis`|`-1.4908`|`0.202`|`-7.394`|`0.000`|
|`rad`|`0.2894`|`0.067`|`4.325`|`0.000`|
|`tax`|`-0.0127`|`0.004`|`-3.337`|`0.001`|
|`ptratio`|`-0.9375`|`0.132`|`-7.091`|`0.000`|
|`lstat`|`-0.5520`|`0.051`|`-10.897 `|`0.000`|

What if we would like to perform a regression using all of the variables but one?

```
In [28]: minus_age = Boston.columns.drop(['medv', 'age'])
Xma = MS(minus_age).fit_transform(Boston)
model1 = sm.OLS(y, Xma)
summarize(model1.fit())
```

---

## Sub-Chapters


[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/index.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/index.html)

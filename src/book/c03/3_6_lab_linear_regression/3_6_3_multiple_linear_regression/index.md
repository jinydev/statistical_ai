---
layout: default
title: "index"
---

# _3.6.3 Multiple Linear Regression_ 

In order to fit a multiple linear regression model using least squares, we again use the `ModelSpec()` transform to construct the required model matrix and response. The arguments to `ModelSpec()` can be quite general, but in this case a list of column names suffice. We consider a fit here with the two variables `lstat` and `age` . 

```
In [25]:X=MS(['lstat','age']).fit_transform(Boston)
model1=sm.OLS(y,X)
results1=model1.fit()
summarize(results1)
```

```
Out[25]:
```

```
coefstderrtP>|t|
intercept33.22280.73145.4580.000
lstat-1.03210.048-21.4160.000
age0.03450.0122.8260.005
```

Notice how we have compacted the first line into a succinct expression describing the construction of `X` . 

The `Boston` data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors. Instead, we can use the following short-hand: 

```
In [26]:terms=Boston.columns.drop('medv')
terms
```

```
.columns.
drop()
```

3.6 Lab: Linear Regression 

```
Out[26]:Index(['crim','zn','indus','chas','nox','rm','age','dis',
'rad','tax','ptratio','lstat'],
dtype='object')
```

We can now fit the model with all the variables in `terms` using the same model matrix builder. 

```
In [27]:X=MS(terms).fit_transform(Boston)
model=sm.OLS(y,X)
results=model.fit()
summarize(results)
```

|**`Out[27]:`**||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`41.6173`|`4.936`|`8.431`|`0.000`|
||`crim`|`-0.1214`|`0.033`|`-3.678`|`0.000`|
||`zn`|`0.0470`|`0.014`|`3.384`|`0.001`|
||`indus`|`0.0135`|`0.062`|`0.217`|`0.829`|
||`chas`|`2.8400`|`0.870`|`3.264`|`0.001`|
||`nox`|`-18.7580`|`3.851`|`-4.870`|`0.000`|
||`rm`|`3.6581`|`0.420`|`8.705`|`0.000`|
||`age`|`0.0036`|`0.013`|`0.271`|`0.787`|
||`dis`|`-1.4908`|`0.202`|`-7.394`|`0.000`|
||`rad`|`0.2894`|`0.067`|`4.325`|`0.000`|
||`tax`|`-0.0127`|`0.004`|`-3.337`|`0.001`|
||`ptratio`|`-0.9375`|`0.132`|`-7.091`|`0.000`|
||`lstat`|`-0.5520`|`0.051`|`-10.897 `|`0.000`|



What if we would like to perform a regression using all of the variables but one? For example, in the above regression output, `age` has a high $p$-value. So we may wish to run a regression excluding this predictor. The following syntax results in a regression using all predictors except `age` (output not shown). 

```
In [28]:minus_age=Boston.columns.drop(['medv','age'])
Xma=MS(minus_age).fit_transform(Boston)
model1=sm.OLS(y,Xma)
summarize(model1.fit())
```

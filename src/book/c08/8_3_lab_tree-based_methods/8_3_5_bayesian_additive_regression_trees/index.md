---
layout: default
title: "index"
---

# _8.3.5 Bayesian Additive Regression Trees_ 

In this section we demonstrate a `Python` implementation of BART found in the `ISLP.bart` package. We fit a model to the `Boston` housing data set. This `BART()` estimator is designed for quantitative outcome variables, though `BART()` other implementations are available for fitting logistic and probit models to categorical outcomes. 

```
In [33]:bart_boston=BART(random_state=0,burnin=5,ndraw=15)
bart_boston.fit(X_train,y_train)
```

```
Out[33]:BART(burnin=5,ndraw=15,random_state=0)
```

On this data set, with this split into test and training, we see that the test error of BART is similar to that of random forest. 

```
In [34]:yhat_test=bart_boston.predict(X_test.astype(np.float32))
np.mean((y_test-yhat_test)**2)
```

```
Out[34]:20.92
```

We can check how many times each variable appeared in the collection of trees. This gives a summary similar to the variable importance plot for boosting and random forests. 

8.4 Exercises 363 

```
In [35]:var_inclusion=pd.Series(bart_boston.variable_inclusion_.mean(0),
index=D.columns)
var_inclusion
```

|**`Out[35]:`**|`crim`|`25.333333`|
|---|---|---|
||`zn`|`27.000000`|
||`indus`|`21.266667`|
||`chas`|`20.466667`|
||`nox`|`25.400000`|
||`rm`|`32.400000`|
||`age`|`26.133333`|
||`dis`|`25.666667`|
||`rad`|`24.666667`|
||`tax`|`23.933333`|
||`ptratio`|`25.000000`|
||`lstat`|`31.866667`|
||`dtype: `|`float64`|



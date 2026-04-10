---
layout: default
title: "index"
---

# **`Out[30]:`** `array([134214.0])` 

The test $\text{MSE}$ is 1.342e+05. Note that if we had instead simply fit a model with just an intercept, we would have predicted each test observation using the mean of the training observations. We can get the same result by fitting a ridge regression model with a _very_ large value of _λ_ . Note that `1e10` means 10[10] . 

```
In [31]:ridge.alpha=1e10
results=skm.cross_validate(ridge,
X,
Y,
scoring='neg_mean_squared_error',
cv=validation)
-results['test_score']
```

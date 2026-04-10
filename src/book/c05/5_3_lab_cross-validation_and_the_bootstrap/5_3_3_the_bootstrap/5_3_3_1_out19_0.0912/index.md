---
layout: default
title: "index"
---

# **`Out[19]:`** `0.0912` 

The final output shows that the bootstrap estimate for SE(ˆ _α_ ) is 0 _._ 0912. 

Estimating the Accuracy of a Linear Regression Model 

The bootstrap approach can be used to assess the variability of the coefficient estimates and predictions from a statistical learning method. Here we use the bootstrap approach in order to assess the variability of the 

222 5. Resampling Methods 

estimates for _β_ 0 and _β_ 1, the intercept and slope terms for the linear regression model that uses `horsepower` to predict `mpg` in the `Auto` data set. We will compare the estimates obtained using the bootstrap to those obtained using the formulas for SE( _β_[ˆ] 0) and SE( _β_[ˆ] 1) described in Section 3.1.2. 

To use our `boot_SE()` function, we must write a function (its first argument) that takes a data frame `D` and indices `idx` as its only arguments. But here we want to bootstrap a specific regression model, specified by a model formula and data. We show how to do this in a few simple steps. 

We start by writing a generic function `boot_OLS()` for bootstrapping a regression model that takes a formula to define the corresponding regression. We use the `clone()` function to make a copy of the formula that can `clone()` be refit to the new dataframe. This means that any derived features such as those defined by `poly()` (which we will see shortly), will be re-fit on the resampled data frame. 

```
In [20]:defboot_OLS(model_matrix ,response,D,idx):
D_=D.loc[idx]
Y_=D_[response]
X_=clone(model_matrix).fit_transform(D_)
returnsm.OLS(Y_,X_).fit().params
```

This is not quite what is needed as the first argument to `boot_SE()` . The first two arguments which specify the model will not change in the bootstrap process, and we would like to _freeze_ them. The function `partial()` from the `partial() functools` module does precisely this: it takes a function as an argument, and freezes some of its arguments, starting from the left. We use it to freeze the first two model-formula arguments of `boot_OLS()` . 

```
In [21]:hp_func=partial(boot_OLS,MS(['horsepower']),'mpg')
```

Typing `hp_func?` will show that it has two arguments `D` and `idx` — it is a version of `boot_OLS()` with the first two arguments frozen — and hence is ideal as the first argument for `boot_SE()` . 

The `hp_func()` function can now be used in order to create bootstrap estimates for the intercept and slope terms by randomly sampling from among the observations with replacement. We first demonstrate its utility on 10 bootstrap samples. 

```
In [22]:rng=np.random.default_rng(0)
np.array([hp_func(Auto,
rng.choice(392,
392,
replace=True))for_inrange(10)])
```

```
Out[22]:array([[39.8806,-0.1568],
[38.733,-0.147],
[38.3173,-0.1444],
[39.9145,-0.1578],
[39.4335,-0.1507],
[40.3663,-0.1591],
[39.6233,-0.1545],
[39.0581,-0.1495],
[38.6669,-0.1452],
[39.6428,-0.1556]])
```

5.3 Lab: Cross-Validation and the Bootstrap 223 

Next, we use the `boot_SE()` function to compute the standard errors of 1,000 bootstrap estimates for the intercept and slope terms. 

```
In [23]:hp_se=boot_SE(hp_func,
Auto,
B=1000,
seed=10)
hp_se
Out[23]:intercept0.8488
horsepower0.0074
dtype:float64
```

This indicates that the bootstrap estimate for SE( _β_[ˆ] 0) is 0.85, and that the bootstrap estimate for SE( _β_[ˆ] 1) is 0.0074. As discussed in Section 3.1.2, standard formulas can be used to compute the standard errors for the regression coefficients in a linear model. These can be obtained using the `summarize()` function from `ISLP.sm` . 

```
In [24]:hp_model.fit(Auto,Auto['mpg'])
model_se=summarize(hp_model.results_)['stderr']
model_se
```

```
Out[24]:intercept0.717
horsepower0.006
Name:stderr,dtype:float64
```

The standard error estimates for _β_[ˆ] 0 and _β_[ˆ] 1 obtained using the formulas from Section 3.1.2 are 0.717 for the intercept and 0.006 for the slope. Interestingly, these are somewhat different from the estimates obtained using the bootstrap. Does this indicate a problem with the bootstrap? In fact, it suggests the opposite. Recall that the standard formulas given in Equation 3.8 on page 75 rely on certain assumptions. For example, they depend on the unknown parameter _σ_[2] , the noise variance. We then estimate _σ_[2] using the RSS. Now although the formula for the standard errors do not rely on the linear model being correct, the estimate for _σ_[2] does. We see in Figure 3.8 on page 99 that there is a non-linear relationship in the data, ˆ and so the residuals from a linear fit will be inflated, and so will _σ_[2] . Secondly, the standard formulas assume (somewhat unrealistically) that the _xi_ are fixed, and all the variability comes from the variation in the errors _ϵi_ . The bootstrap approach does not rely on any of these assumptions, and so it is likely giving a more accurate estimate of the standard errors of _β_[ˆ] 0 and _β_[ˆ] 1 than the results from `sm.OLS` . 

Below we compute the bootstrap standard error estimates and the standard linear regression estimates that result from fitting the quadratic model to the data. Since this model provides a good fit to the data (Figure 3.8), there is now a better correspondence between the bootstrap estimates and the standard estimates of SE( _β_[ˆ] 0), SE( _β_[ˆ] 1) and SE( _β_[ˆ] 2). 

```
In [25]:quad_model=MS([poly('horsepower',2,raw=True)])
quad_func=partial(boot_OLS,
quad_model,
'mpg')
boot_SE(quad_func,Auto,B=1000)
```

224 5. Resampling Methods 

```
Out[25]:
```

```
intercept2.067840
poly(horsepower ,2,raw=True)[0]0.033019
poly(horsepower ,2,raw=True)[1]0.000120
dtype:float64
```

We compare the results to the standard errors computed using `sm.OLS()` . 

```
In [26]:M=sm.OLS(Auto['mpg'],
```

```
quad_model.fit_transform(Auto))
summarize(M.fit())['stderr']
```

```
Out[26]:intercept1.800
poly(horsepower ,2,raw=True)[0]0.031
poly(horsepower ,2,raw=True)[1]0.000
Name:stderr,dtype:float64
```

---
layout: default
title: "index"
---

# _Cp_ , AIC, BIC, and Adjusted _R_[2] 

We show in Chapter 2 that the training set $\text{MSE}$ is generally an underestimate of the test MSE. (Recall that $\text{MSE}$ = RSS _/n_ .) This is because when we fit a model to the training data using least squares, we specifically estimate the regression coefficients such that the training RSS (but not the test RSS) is as small as possible. In particular, the training error will decrease as more variables are included in the model, but the test error may not. Therefore, training set RSS and training set _R_[2] cannot be used to select from among a set of models with different numbers of variables. 

However, a number of techniques for _adjusting_ the training error for the model size are available. These approaches can be used to select among a set of models with different numbers of variables. We now consider four such approaches: _criterion_ (BIC), and _Cp_ , _Akaike information adjusted R_[2] . Figure _criterion_ 6.2 displays (AIC), _C Bayesian informationp_ , BIC, and adjusted _Cp R_[2] for the best model of each size produced by best subset selection on the `Credit` data set. 

Akaike information criterion Bayesian information criterion adjusted _R_[2] 

For a fitted least squares model containing _d_ predictors, the _Cp_ estimate of test $\text{MSE}$ is computed using the equation

$$
C_p = \frac{1}{n} (\text{RSS} + 2 d \hat{\sigma}^2) \quad (6.2)
$$

where _σ_ ˆ[2] is an estimate of the variance of the error _ϵ_ associated with each response measurement in (6.1).[4] Typically _σ_ ˆ[2] is estimated using the full model containing all predictors. Essentially, the _Cp_ statistic adds a penalty of 2 _dσ_ ˆ[2] to the training RSS in order to adjust for the fact that the training error tends to underestimate the test error. Clearly, the penalty increases as the number of predictors in the model increases; this is intended to adjust 

> 4Mallow’s _Cp_ is sometimes defined as _Cp′_[=][RSS] _[/][σ]_[ˆ][2][+ 2] _[d][ −][n]_[.][This][is][equivalent][to] the definition given above in the sense that _Cp_ = _n_[1] _[σ]_[ˆ][2][(] _[C] p[′]_[+] _[ n]_[)][,][and][so][the][model][with] smallest _Cp_ also has smallest _Cp[′]_[.] 

6.1 Subset Selection 237 

![Figure 6.2](./img/6_2.png)

**FIGURE 6.2.** _Cp, BIC, and adjusted R_[2] _are shown for the best models of each size for the_ `Credit` _data set (the lower frontier in Figure 6.1). Cp and BIC are estimates of test MSE. In the middle plot we see that the BIC estimate of test error shows an increase after four variables are selected. The other two plots are rather flat after four variables are included._ 

for the corresponding decrease in training RSS. Though it is beyond the scope of this book, one can show that if _σ_ ˆ[2] is an unbiased estimate of _σ_[2] in (6.2), then _Cp_ is an unbiased estimate of test MSE. As a consequence, the _Cp_ statistic tends to take on a small value for models with a low test error, so when determining which of a set of models is best, we choose the model with the lowest _Cp_ value. In Figure 6.2, _Cp_ selects the six-variable model containing the predictors `income` , `limit` , `rating` , `cards` , `age` and `student` . 

The AIC criterion is defined for a large class of models fit by maximum likelihood. In the case of the model (6.1) with Gaussian errors, maximum likelihood and least squares are the same thing. In this case AIC is given by

$$
\text{AIC} = \frac{1}{n \hat{\sigma}^2} (\text{RSS} + 2 d \hat{\sigma}^2) \quad (6.3)
$$

where, for simplicity, we have omitted irrelevant constants.[5] Hence for least squares models, _Cp_ and AIC are proportional to each other, and so only _Cp_ is displayed in Figure 6.2. 

BIC is derived from a Bayesian point of view, but ends up looking similar to _Cp_ (and AIC) as well. For the least squares model with _d_ predictors, the BIC is, up to irrelevant constants, given by

$$
\text{BIC} = \frac{1}{n} (\text{RSS} + \log(n) d \hat{\sigma}^2) \quad (6.4)
$$

Like _Cp_ , the BIC will tend to take on a small value for a model with a low test error, and so generally we select the model that has the lowest BIC value. Notice that BIC replaces the 2 _dσ_ ˆ[2] used by _Cp_ with a log( _n_ ) _dσ_ ˆ[2] term, where _n_ is the number of observations. Since log _n >_ 2 for any _n >_ 7, 

> 5There are two formulas for AIC for least squares regression. The formula that we provide here requires an expression for _σ_[2] , which we obtain using the full model containing all predictors. The second formula is appropriate when _σ_[2] is unknown and we do not want to explicitly estimate it; that formula has a log(RSS) term instead of an RSS term. Detailed derivations of these two formulas are outside of the scope of this book. 

238 6. Linear Model Selection and Regularization 

the BIC statistic generally places a heavier penalty on models with many variables, and hence results in the selection of smaller models than _Cp_ . In Figure 6.2, we see that this is indeed the case for the `Credit` data set; BIC chooses a model that contains only the four predictors `income` , `limit` , `cards` , and `student` . In this case the curves are very flat and so there does not appear to be much difference in accuracy between the four-variable and six-variable models. 

The adjusted _R_[2] statistic is another popular approach for selecting among a set of models that contain different numbers of variables. Recall from Chapter 3 that the usual _R_[2] is defined as 1 _−_ RSS _/_ TSS, where TSS = �( _yi −_ ~~_y_~~ )[2] is the _total sum of squares_ for the response. Since RSS always decreases as more variables are added to the model, the _R_[2] always increases as more variables are added. For a least squares model with _d_ variables, the adjusted _R_[2] statistic is calculated as

$$
\text{Adjusted } R^2 = 1 - \frac{\text{RSS} / (n - d - 1)}{\text{TSS} / (n - 1)} \quad (6.5)
$$

Unlike _Cp_ , AIC, and BIC, for which a _small_ value indicates a model with a low test error, a _large_ value of adjusted _R_[2] indicates a model with a small test error. Maximizing the adjusted _R_[2] is equivalent to minimizing RSS _n−d−_ 1[. While RSS always decreases as the number of variables in the model] increases, _n−_ RSS _d−_ 1[may][increase][or][decrease,][due][to][the][presence][of] _[d]_[in][the] denominator. 

The intuition behind the adjusted _R_[2] is that once all of the correct variables have been included in the model, adding additional _noise_ variables will lead to only a very small decrease in RSS. Since adding noise variables leads to an increase in _d_ , such variables will lead to an increase in _n−_ RSS _d−_ 1[,] and consequently a decrease in the adjusted _R_[2] . Therefore, in theory, the model with the largest adjusted _R_[2] will have only correct variables and no noise variables. Unlike the _R_[2] statistic, the adjusted _R_[2] statistic _pays a price_ for the inclusion of unnecessary variables in the model. Figure 6.2 displays the adjusted _R_[2] for the `Credit` data set. Using this statistic results in the selection of a model that contains seven variables, adding `own` to the model selected by _Cp_ and AIC. 

_Cp_ , AIC, and BIC all have rigorous theoretical justifications that are beyond the scope of this book. These justifications rely on asymptotic arguments (scenarios where the sample size _n_ is very large). Despite its popularity, and even though it is quite intuitive, the adjusted _R_[2] is not as well motivated in statistical theory as AIC, BIC, and _Cp_ . All of these measures are simple to use and compute. Here we have presented their formulas in the case of a linear model fit using least squares; however, AIC and BIC can also be defined for more general types of models. 

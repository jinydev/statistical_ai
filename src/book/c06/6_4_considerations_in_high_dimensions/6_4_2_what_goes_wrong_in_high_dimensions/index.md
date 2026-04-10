---
layout: default
title: "index"
---

# _6.4.2 What Goes Wrong in High Dimensions?_ 

In order to illustrate the need for extra care and specialized techniques for regression and classification when _p > n_ , we begin by examining what can go wrong if we apply a statistical technique not intended for the highdimensional setting. For this purpose, we examine least squares regression. But the same concepts apply to logistic regression, linear discriminant analysis, and other classical statistical approaches. 

When the number of features _p_ is as large as, or larger than, the number of observations _n_ , least squares as described in Chapter 3 cannot (or rather, _should not_ ) be performed. The reason is simple: regardless of whether or not there truly is a relationship between the features and the response, least squares will yield a set of coefficient estimates that result in a perfect fit to the data, such that the residuals are zero. 

An example is shown in Figure 6.22 with _p_ = 1 feature (plus an intercept) in two cases: when there are 20 observations, and when there are only two observations. When there are 20 observations, _n > p_ and the least squares regression line does not perfectly fit the data; instead, the regression line seeks to approximate the 20 observations as well as possible. On the other hand, when there are only two observations, then regardless of the values of those observations, the regression line will fit the data exactly. This is problematic because this perfect fit will almost certainly lead to overfitting of the data. In other words, though it is possible to perfectly fit the training data in the high-dimensional setting, the resulting linear model will perform extremely poorly on an independent test set, and therefore does not constitute a useful model. In fact, we can see that this happened in Figure 6.22: the least squares line obtained in the right-hand panel will perform very poorly on a test set comprised of the observations in the lefthand panel. The problem is simple: when _p > n_ or _p ≈ n_ , a simple least squares regression line is too _flexible_ and hence overfits the data. 

Figure 6.23 further illustrates the risk of carelessly applying least squares when the number of features _p_ is large. Data were simulated with _n_ = 20 observations, and regression was performed with between 1 and 20 features, 

264 6. Linear Model Selection and Regularization 

![Figure 6.22](./img/6_22.png)

**FIGURE 6.22.** Left: _Least squares regression in the low-dimensional setting._ Right: _Least squares regression with n_ = 2 _observations and two parameters to be estimated (an intercept and a coefficient)._ 

![Figure 6.23](./img/6_23.png)

**FIGURE 6.23.** _On a simulated example with n_ = 20 _training observations, features that are completely unrelated to the outcome are added to the model._ Left: _The R_[2] _increases to 1 as more features are included._ Center: _The training set $\text{MSE}$ decreases to 0 as more features are included._ Right: _The test set $\text{MSE}$ increases as more features are included._ 

each of which was completely unrelated to the response. As shown in the figure, the model _R_[2] increases to 1 as the number of features included in the model increases, and correspondingly the training set $\text{MSE}$ decreases to 0 as the number of features increases, _even though the features are completely unrelated to the response_ . On the other hand, the $\text{MSE}$ on an _independent test set_ becomes extremely large as the number of features included in the model increases, because including the additional predictors leads to a vast increase in the variance of the coefficient estimates. Looking at the test set MSE, it is clear that the best model contains at most a few variables. However, someone who carelessly examines only the _R_[2] or the training set $\text{MSE}$ might erroneously conclude that the model with the greatest number of variables is best. This indicates the importance of applying extra care when analyzing data sets with a large number of variables, and of always evaluating model performance on an independent test set. 

6.4 Considerations in High Dimensions 265 

![Figure 6.24](./img/6_24.png)

**FIGURE 6.24.** _The lasso was performed with n_ = 100 _observations and three values of p, the number of features. Of the p features, 20 were associated with the response. The boxplots show the test MSEs that result using three different values of the tuning parameter λ in (6.7). For ease of interpretation, rather than reporting λ, the_ degrees of freedom _are reported; for the lasso this turns out to be simply the number of estimated non-zero coefficients. When p_ = 20 _, the lowest test $\text{MSE}$ was obtained with the smallest amount of regularization. When p_ = 50 _, the lowest test $\text{MSE}$ was achieved when there is a substantial amount of regularization. When p_ = 2 _,_ 000 _the lasso performed poorly regardless of the amount of regularization, due to the fact that only 20 of the 2,000 features truly are associated with the outcome._ 

In Section 6.1.3, we saw a number of approaches for adjusting the training set RSS or _R_[2] in order to account for the number of variables used to fit a least squares model. Unfortunately, the _Cp_ , AIC, and BIC approaches are not appropriate in the high-dimensional setting, because estimating _σ_ ˆ[2] is problematic. (For instance, the formula for _σ_ ˆ[2] from Chapter 3 yields an estimate _σ_ ˆ[2] = 0 in this setting.) Similarly, problems arise in the application of adjusted _R_[2] in the high-dimensional setting, since one can easily obtain a model with an adjusted _R_[2] value of 1. Clearly, alternative approaches that are better-suited to the high-dimensional setting are required. 

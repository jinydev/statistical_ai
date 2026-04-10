---
layout: default
title: "index"
---

# _5.1.2 Leave-One-Out Cross-Validation_ 

_Leave-one-out cross-validation_ (LOOCV) is closely related to the validation leave-oneset approach of Section 5.1.1, but it attempts to address that method’s out drawbacks. 

out crossvalidation 

Like the validation set approach, LOOCV involves splitting the set of observations into two parts. However, instead of creating two subsets of comparable size, a single observation ( _x_ 1 _, y_ 1) is used for the validation set, and the remaining observations _{_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ ) _}_ make up the training set. The statistical learning method is fit on the _n −_ 1 training observations, and a prediction _y_ ˆ1 is made for the excluded observation, using its value _x_ 1. Since ( _x_ 1 _, y_ 1) was not used in the fitting process, $\text{MSE}_1$ = ( _y_ 1 _− y_ ˆ1)[2] provides an approximately unbiased estimate for the test error. But even though $\text{MSE}_1$ is unbiased for the test error, it is a poor estimate because it is highly variable, since it is based upon a single observation ( _x_ 1 _, y_ 1). 

We can repeat the procedure by selecting ( _x_ 2 _, y_ 2) for the validation data, training the statistical learning procedure on the _n −_ 1 observations ˆ _{_ ( _x_ 1 _, y_ 1) _,_ ( _x_ 3 _, y_ 3) _, . . . ,_ ( _xn, yn_ ) _}_ , and computing $\text{MSE}_2$ = ( _y_ 2 _−y_ 2)[2] . Repeating this approach _n_ times produces _n_ squared errors, $\text{MSE}_1$ _, . . . ,_ MSE _n_ . The LOOCV estimate for the test MSE is the average of these _n_ test error estimates: 

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{MSE}_i \quad (5.1)
$$

5.1 Cross-Validation 205 

**FIGURE 5.3.** _A schematic display of LOOCV. A set of n data points is repeatedly split into a training set (shown in blue) containing all but one observation, and a validation set that contains only that observation (shown in beige). The test error is then estimated by averaging the n resulting MSEs. The first training set contains all but observation 1, the second training set contains all but observation 2, and so forth._ 

A schematic of the LOOCV approach is illustrated in Figure 5.3. 

LOOCV has a couple of major advantages over the validation set approach. First, it has far less bias. In LOOCV, we repeatedly fit the statistical learning method using training sets that contain _n −_ 1 observations, almost as many as are in the entire data set. This is in contrast to the validation set approach, in which the training set is typically around half the size of the original data set. Consequently, the LOOCV approach tends not to overestimate the test error rate as much as the validation set approach does. Second, in contrast to the validation approach which will yield different results when applied repeatedly due to randomness in the training/validation set splits, performing LOOCV multiple times will always yield the same results: there is no randomness in the training/validation set splits. 

We used LOOCV on the `Auto` data set in order to obtain an estimate of the test set MSE that results from fitting a linear regression model to predict `mpg` using polynomial functions of `horsepower` . The results are shown in the left-hand panel of Figure 5.4. 

LOOCV has the potential to be expensive to implement, since the model has to be fit _n_ times. This can be very time consuming if _n_ is large, and if each individual model is slow to fit. With least squares linear or polynomial regression, an amazing shortcut makes the cost of LOOCV the same as that of a single model fit! The following formula holds: 

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2 \quad (5.2)
$$

206 5. Resampling Methods 

![Figure 5.4](./img/5_4.png)

**FIGURE 5.4.** _Cross-validation was used on the_ `Auto` _data set in order to estimate the test error that results from predicting_ `mpg` _using polynomial functions of_ `horsepower` _._ Left: _The LOOCV error curve._ Right: 10 _-fold CV was run nine separate times, each with a different random split of the data into ten parts. The figure shows the nine slightly different CV error curves._ 

where _y_ ˆ _i_ is the _i_ th fitted value from the original least squares fit, and _hi_ is the leverage defined in (3.37) on page 105.[1] This is like the ordinary MSE, except the _i_ th residual is divided by 1 _− hi_ . The leverage lies between 1 _/n_ and 1, and reflects the amount that an observation influences its own fit. Hence the residuals for high-leverage points are inflated in this formula by exactly the right amount for this equality to hold. 

LOOCV is a very general method, and can be used with any kind of predictive modeling. For example we could use it with logistic regression or linear discriminant analysis, or any of the methods discussed in later chapters. The magic formula (5.2) does not hold in general, in which case the model has to be refit _n_ times. 

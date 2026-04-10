---
layout: default
title: "index"
---

# An Application to the Credit Data 

In Figure 6.4, the ridge regression coefficient estimates for the `Credit` data set are displayed. In the left-hand panel, each curve corresponds to the ridge regression coefficient estimate for one of the ten variables, plotted as a function of _λ_ . For example, the black solid line represents the ridge regression estimate for the `income` coefficient, as _λ_ is varied. At the extreme left-hand side of the plot, _λ_ is essentially zero, and so the corresponding ridge coefficient estimates are the same as the usual least squares estimates. But as _λ_ increases, the ridge coefficient estimates shrink towards zero. When _λ_ is extremely large, then all of the ridge coefficient estimates are basically zero; this corresponds to the _null model_ that contains no predictors. In this plot, the `income` , `limit` , `rating` , and `student` variables are displayed in distinct colors, since these variables tend to have by far the largest coefficient estimates. While the ridge coefficient estimates tend to decrease in aggregate as _λ_ increases, individual coefficients, such as `rating` and `income` , may occasionally increase as _λ_ increases. 

242 6. Linear Model Selection and Regularization 

The right-hand panel of Figure 6.4 displays the same ridge coefficient estimates as the left-hand panel, but instead of displaying _λ_ on the _x_ -axis, we now display _∥β_[ˆ] _λ[R][∥]_[2] _[/][∥][β]_[ˆ] _[∥]_[2][,][where] _[β]_[ˆ][denotes][the][vector][of][least][squares] coefficient estimates. The notation _∥β∥_ 2 denotes the _ℓ_ 2 _norm_ (pronounced _ℓ_ 2 norm “ell 2”) of a vector, and is defined as _∥β∥_ 2 = ~~��~~ _pj_ =1 _[β][j]_ 2. It measures the distance of _β_ from zero. As _λ_ increases, the _ℓ_ 2 norm of _β_[ˆ] _λ[R]_[will] _[always]_ decrease, and so will _∥β_[ˆ] _λ[R][∥]_[2] _[/][∥][β]_[ˆ] _[∥]_[2][. The latter quantity ranges from 1 (when] _λ_ = 0, in which case the ridge regression coefficient estimate is the same as the least squares estimate, and so their _ℓ_ 2 norms are the same) to 0 (when _λ_ = _∞_ , in which case the ridge regression coefficient estimate is a vector of zeros, with _ℓ_ 2 norm equal to zero). Therefore, we can think of the _x_ -axis in the right-hand panel of Figure 6.4 as the amount that the ridge regression coefficient estimates have been shrunken towards zero; a small value indicates that they have been shrunken very close to zero. 

The standard least squares coefficient estimates discussed in Chapter 3 are _scale equivariant_ : multiplying _Xj_ by a constant _c_ simply leads to a scale scaling of the least squares coefficient estimates by a factor of 1 _/c_ . In other words, regardless of how the _j_ th predictor is scaled, _Xjβ_[ˆ] _j_ will remain the same. In contrast, the ridge regression coefficient estimates can change _substantially_ when multiplying a given predictor by a constant. For instance, consider the `income` variable, which is measured in dollars. One could reasonably have measured income in thousands of dollars, which would result in a reduction in the observed values of `income` by a factor of 1,000. Now due to the sum of squared coefficients term in the ridge regression formulation (6.5), such a change in scale will not simply cause the ridge regression coefficient estimate for `income` to change by a factor of 1,000. In other words, _Xjβ_[ˆ] _j,λ[R]_[will depend not only on the value of] _[ λ]_[, but also on the scaling of the] _j_ th predictor. In fact, the value of _Xjβ_[ˆ] _j,λ[R]_[may][even][depend][on][the][scaling] of the _other_ predictors! Therefore, it is best to apply ridge regression after _standardizing the predictors_ , using the formula

$$
\tilde{x}_{ij} = \frac{x_{ij}}{\sqrt{\frac{1}{n} \sum_{i=1}^n (x_{ij} - \bar{x}_j)^2}} \quad (6.6)
$$

so that they are all on the same scale. In (6.6), the denominator is the estimated standard deviation of the _j_ th predictor. Consequently, all of the standardized predictors will have a standard deviation of one. As a result the final fit will not depend on the scale on which the predictors are measured. In Figure 6.4, the _y_ -axis displays the standardized ridge regression coefficient estimates—that is, the coefficient estimates that result from performing ridge regression using standardized predictors. 

Why Does Ridge Regression Improve Over Least Squares? 

Ridge regression’s advantage over least squares is rooted in the _bias-variance trade-off_ . As _λ_ increases, the flexibility of the ridge regression fit decreases, leading to decreased variance but increased bias. This is illustrated in the left-hand panel of Figure 6.5, using a simulated data set containing _p_ = 45 predictors and _n_ = 50 observations. The green curve in the left-hand panel 

6.2 Shrinkage Methods 243 

![Figure 6.5](./img/6_5.png)

**FIGURE 6.5.** _Squared bias (black), variance (green), and test mean squared error (purple) for the ridge regression predictions on a simulated data set, as a function of λ and ∥β_[ˆ] _λ[R][∥]_[2] _[/][∥][β]_[ˆ] _[∥]_[2] _[. The horizontal dashed lines indicate the minimum] possible MSE. The purple crosses indicate the ridge regression models for which the $\text{MSE}$ is smallest._ 

of Figure 6.5 displays the variance of the ridge regression predictions as a function of _λ_ . At the least squares coefficient estimates, which correspond to ridge regression with _λ_ = 0, the variance is high but there is no bias. But as _λ_ increases, the shrinkage of the ridge coefficient estimates leads to a substantial reduction in the variance of the predictions, at the expense of a slight increase in bias. Recall that the test mean squared error (MSE), plotted in purple, is closely related to the variance plus the squared bias. For values of _λ_ up to about 10, the variance decreases rapidly, with very little increase in bias, plotted in black. Consequently, the $\text{MSE}$ drops considerably as _λ_ increases from 0 to 10. Beyond this point, the decrease in variance due to increasing _λ_ slows, and the shrinkage on the coefficients causes them to be significantly underestimated, resulting in a large increase in the bias. The minimum $\text{MSE}$ is achieved at approximately _λ_ = 30. Interestingly, because of its high variance, the $\text{MSE}$ associated with the least squares fit, when _λ_ = 0, is almost as high as that of the null model for which all coefficient estimates are zero, when _λ_ = _∞_ . However, for an intermediate value of _λ_ , the $\text{MSE}$ is considerably lower. 

The right-hand panel of Figure 6.5 displays the same curves as the lefthand panel, this time plotted against the _ℓ_ 2 norm of the ridge regression coefficient estimates divided by the _ℓ_ 2 norm of the least squares estimates. Now as we move from left to right, the fits become more flexible, and so the bias decreases and the variance increases. 

In general, in situations where the relationship between the response and the predictors is close to linear, the least squares estimates will have low bias but may have high variance. This means that a small change in the training data can cause a large change in the least squares coefficient estimates. In particular, when the number of variables _p_ is almost as large as the number of observations _n_ , as in the example in Figure 6.5, the least squares estimates will be extremely variable. And if _p > n_ , then the least squares estimates do not even have a unique solution, whereas ridge regression can still perform well by trading off a small increase in bias for a 

244 6. Linear Model Selection and Regularization 

large decrease in variance. Hence, ridge regression works best in situations where the least squares estimates have high variance. 

Ridge regression also has substantial computational advantages over best subset selection, which requires searching through 2 _[p]_ models. As we discussed previously, even for moderate values of _p_ , such a search can be computationally infeasible. In contrast, for any fixed value of _λ_ , ridge regression only fits a single model, and the model-fitting procedure can be performed quite quickly. In fact, one can show that the computations required to solve (6.5), _simultaneously for all values of λ_ , are almost identical to those for fitting a model using least squares. 

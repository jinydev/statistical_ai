---
layout: default
title: "index"
---

# The Principal Components Regression Approach 

The _principal components regression_ (PCR) approach involves construct- principal ing the first _M_ principal components, _Z_ 1 _, . . . , ZM_ , and then using these components as the predictors in a linear regression model that is fit usregression ing least squares. The key idea is that often a small number of principal components suffice to explain most of the variability in the data, as well as the relationship with the response. In other words, we assume that _the_ 

components regression 

258 6. Linear Model Selection and Regularization 

![Figure 6.17](./img/6_17.png)

**FIGURE 6.17.** _Plots of the second principal component scores zii_ 2 _versus_ `pop` _and_ `ad` _. The relationships are weak._ 

**FIGURE 6.18.** _PCR was applied to two simulated data sets. In each panel, the horizontal dashed line represents the irreducible error._ Left: _Simulated data from Figure 6.8._ Right: _Simulated data from Figure 6.9._ 

_directions in which X_ 1 _, . . . , Xp show the most variation are the directions that are associated with Y_ . While this assumption is not guaranteed to be true, it often turns out to be a reasonable enough approximation to give good results. 

If the assumption underlying PCR holds, then fitting a least squares model to _Z_ 1 _, . . . , ZM_ will lead to better results than fitting a least squares model to _X_ 1 _, . . . , Xp_ , since most or all of the information in the data that relates to the response is contained in _Z_ 1 _, . . . , ZM_ , and by estimating only _M ≪ p_ coefficients we can mitigate overfitting. In the advertising data, the first principal component explains most of the variance in both `pop` and `ad` , so a principal component regression that uses this single variable to predict some response of interest, such as `sales` , will likely perform quite well. 

Figure 6.18 displays the PCR fits on the simulated data sets from Figures 6.8 and 6.9. Recall that both data sets were generated using _n_ = 50 observations and _p_ = 45 predictors. However, while the response in the first data set was a function of all the predictors, the response in the second data set was generated using only two of the predictors. The curves are plotted as a function of _M_ , the number of principal components used as predictors in the regression model. As more principal components are used 

6.3 Dimension Reduction Methods 259 

![Figure 6.19](./img/6_19.png)

**FIGURE 6.19.** _PCR, ridge regression, and the lasso were applied to a simulated data set in which the first five principal components of X contain all the information about the response Y . In each panel, the irreducible error_ Var( _ϵ_ ) _is shown as a horizontal dashed line._ Left: _Results for PCR._ Right: _Results for lasso (solid) and ridge regression (dotted). The x-axis displays the shrinkage factor of the coefficient estimates, defined as the ℓ_ 2 _norm of the shrunken coefficient estimates divided by the ℓ_ 2 _norm of the least squares estimate._ 

in the regression model, the bias decreases, but the variance increases. This results in a typical U-shape for the mean squared error. When _M_ = _p_ = 45, then PCR amounts simply to a least squares fit using all of the original predictors. The figure indicates that performing PCR with an appropriate choice of _M_ can result in a substantial improvement over least squares, especially in the left-hand panel. However, by examining the ridge regression and lasso results in Figures 6.5, 6.8, and 6.9, we see that PCR does not perform as well as the two shrinkage methods in this example. 

The relatively worse performance of PCR in Figure 6.18 is a consequence of the fact that the data were generated in such a way that many principal components are required in order to adequately model the response. In contrast, PCR will tend to do well in cases when the first few principal components are sufficient to capture most of the variation in the predictors as well as the relationship with the response. The left-hand panel of Figure 6.19 illustrates the results from another simulated data set designed to be more favorable to PCR. Here the response was generated in such a way that it depends exclusively on the first five principal components. Now the bias drops to zero rapidly as _M_ , the number of principal components used in PCR, increases. The mean squared error displays a clear minimum at _M_ = 5. The right-hand panel of Figure 6.19 displays the results on these data using ridge regression and the lasso. All three methods offer a significant improvement over least squares. However, PCR and ridge regression slightly outperform the lasso. 

We note that even though PCR provides a simple way to perform regression using _M < p_ predictors, it is _not_ a feature selection method. This is because each of the _M_ principal components used in the regression is a linear combination of all _p_ of the _original_ features. For instance, in (6.19), _Z_ 1 was a linear combination of both `pop` and `ad` . Therefore, while PCR often performs quite well in many practical settings, it does not result in the 

260 6. Linear Model Selection and Regularization 

![Figure 6.20](./img/6_20.png)

**FIGURE 6.20.** Left: _PCR standardized coefficient estimates on the_ `Credit` _data set for different values of M ._ Right: _The ten-fold cross-validation_ $\text{MSE}$ _obtained using PCR, as a function of M ._ 

development of a model that relies upon a small set of the original features. In this sense, PCR is more closely related to ridge regression than to the lasso. In fact, one can show that PCR and ridge regression are very closely related. One can even think of ridge regression as a continuous version of PCR![8] 

In PCR, the number of principal components, _M_ , is typically chosen by cross-validation. The results of applying PCR to the `Credit` data set are shown in Figure 6.20; the right-hand panel displays the cross-validation errors obtained, as a function of _M_ . On these data, the lowest cross-validation error occurs when there are _M_ = 10 components; this corresponds to almost no dimension reduction at all, since PCR with _M_ = 11 is equivalent to simply performing least squares. 

When performing PCR, we generally recommend _standardizing_ each predictor, using (6.6), prior to generating the principal components. This standardization ensures that all variables are on the same scale. In the absence of standardization, the high-variance variables will tend to play a larger role in the principal components obtained, and the scale on which the variables are measured will ultimately have an effect on the final PCR model. However, if the variables are all measured in the same units (say, kilograms, or inches), then one might choose not to standardize them. 

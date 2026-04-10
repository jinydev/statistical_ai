---
layout: default
title: "index"
---

# _6.3.2 Partial Least Squares_ 

The PCR approach that we just described involves identifying linear combinations, or _directions_ , that best represent the predictors _X_ 1 _, . . . , Xp_ . These directions are identified in an _unsupervised_ way, since the response _Y_ is not used to help determine the principal component directions. That is, the response does not _supervise_ the identification of the principal components. Consequently, PCR suffers from a drawback: there is no guarantee 

> 8More details can be found in Section 3.5 of _The Elements of Statistical Learning_ by Hastie, Tibshirani, and Friedman. 

6.3 Dimension Reduction Methods 261 

![Figure 6.21](./img/6_21.png)

**FIGURE 6.21.** _For the advertising data, the first PLS direction (solid line) and first PCR direction (dotted line) are shown._ 

that the directions that best explain the predictors will also be the best directions to use for predicting the response. Unsupervised methods are discussed further in Chapter 12. 

We now present _partial least squares_ (PLS), a _supervised_ alternative to PCR. Like PCR, PLS is a dimension reduction method, which first identifies partialsquaresleast a new set of features _Z_ 1 _, . . . , ZM_ that are linear combinations of the original features, and then fits a linear model via least squares using these _M_ new features. But unlike PCR, PLS identifies these new features in a supervised way—that is, it makes use of the response _Y_ in order to identify new features that not only approximate the old features well, but also that _are related to the response_ . Roughly speaking, the PLS approach attempts to find directions that help explain both the response and the predictors. 

We now describe how the first PLS direction is computed. After standardizing the _p_ predictors, PLS computes the first direction _Z_ 1 by setting each _φj_ 1 in (6.16) equal to the coefficient from the simple linear regression of _Y_ onto _Xj_ . One can show that this coefficient is proportional to the correlation between _Y_ and _Xj_ . Hence, in computing _Z_ 1 =[�] _[p] j_ =1 _[φ][j]_[1] _[X][j]_[,][PLS] places the highest weight on the variables that are most strongly related to the response. 

Figure 6.21 displays an example of PLS on a synthetic dataset with Sales in each of 100 regions as the response, and two predictors; Population Size and Advertising Spending. The solid green line indicates the first PLS direction, while the dotted line shows the first principal component direction. PLS has chosen a direction that has less change in the `ad` dimension per unit change in the `pop` dimension, relative to PCA. This suggests that `pop` is more highly correlated with the response than is `ad` . The PLS direction does not fit the predictors as closely as does PCA, but it does a better job explaining the response. 

To identify the second PLS direction we first _adjust_ each of the variables for _Z_ 1, by regressing each variable on _Z_ 1 and taking _residuals_ . These residuals can be interpreted as the remaining information that has not been explained by the first PLS direction. We then compute _Z_ 2 using this _or-_ 

262 6. Linear Model Selection and Regularization 

_thogonalized_ data in exactly the same fashion as _Z_ 1 was computed based on the original data. This iterative approach can be repeated _M_ times to identify multiple PLS components _Z_ 1 _, . . . , ZM_ . Finally, at the end of this procedure, we use least squares to fit a linear model to predict _Y_ using _Z_ 1 _, . . . , ZM_ in exactly the same fashion as for PCR. 

As with PCR, the number _M_ of partial least squares directions used in PLS is a tuning parameter that is typically chosen by cross-validation. We generally standardize the predictors and response before performing PLS. 

PLS is popular in the field of chemometrics, where many variables arise from digitized spectrometry signals. In practice it often performs no better than ridge regression or PCR. While the supervised dimension reduction of PLS can reduce bias, it also has the potential to increase variance, so that the overall benefit of PLS relative to PCR is a wash. 

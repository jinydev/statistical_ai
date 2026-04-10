---
layout: default
title: "index"
---

# _5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation_ 

We mentioned in Section 5.1.3 that _k_ -fold CV with _k < n_ has a computational advantage to LOOCV. But putting computational issues aside, a less obvious but potentially more important advantage of _k_ -fold CV is that it often gives more accurate estimates of the test error rate than does LOOCV. This has to do with a bias-variance trade-off. 

It was mentioned in Section 5.1.1 that the validation set approach can lead to overestimates of the test error rate, since in this approach the training set used to fit the statistical learning method contains only half the observations of the entire data set. Using this logic, it is not hard to see 

5.1 Cross-Validation 209 

that LOOCV will give approximately unbiased estimates of the test error, since each training set contains _n −_ 1 observations, which is almost as many as the number of observations in the full data set. And performing _k_ -fold CV for, say, _k_ = 5 or _k_ = 10 will lead to an intermediate level of bias, since each training set contains approximately ( _k −_ 1) _n/k_ observations— fewer than in the LOOCV approach, but substantially more than in the validation set approach. Therefore, from the perspective of bias reduction, it is clear that LOOCV is to be preferred to _k_ -fold CV. 

However, we know that bias is not the only source for concern in an estimating procedure; we must also consider the procedure’s variance. It turns out that LOOCV has higher variance than does _k_ -fold CV with _k < n_ . Why is this the case? When we perform LOOCV, we are in effect averaging the outputs of _n_ fitted models, each of which is trained on an almost identical set of observations; therefore, these outputs are highly (positively) correlated with each other. In contrast, when we perform _k_ -fold CV with _k < n_ , we are averaging the outputs of _k_ fitted models that are somewhat less correlated with each other, since the overlap between the training sets in each model is smaller. Since the mean of many highly correlated quantities has higher variance than does the mean of many quantities that are not as highly correlated, the test error estimate resulting from LOOCV tends to have higher variance than does the test error estimate resulting from _k_ -fold CV. 

To summarize, there is a bias-variance trade-off associated with the choice of _k_ in _k_ -fold cross-validation. Typically, given these considerations, one performs _k_ -fold cross-validation using _k_ = 5 or _k_ = 10, as these values have been shown empirically to yield test error rate estimates that suffer neither from excessively high bias nor from very high variance. 

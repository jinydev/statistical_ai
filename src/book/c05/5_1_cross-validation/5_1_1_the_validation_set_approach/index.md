---
layout: default
title: "index"
---

# _5.1.1 The Validation Set Approach_ 

Suppose that we would like to estimate the test error associated with fitting a particular statistical learning method on a set of observations. The _validation set approach_ , displayed in Figure 5.1, is a very simple strategy validation for this task. It involves randomly dividing the available set of observaset tions into two parts, a _training set_ and a _validation set_ or _hold-out set_ . The validation model is fit on the training set, and the fitted model is used to predict the set responses for the observations in the validation set. The resulting validation hold-out set error rate—typically assessed using MSE in the case of a quantitative response—provides an estimate of the test error rate. 

set approach 

set hold-out set 

We illustrate the validation set approach on the `Auto` data set. Recall from Chapter 3 that there appears to be a non-linear relationship between `mpg` and `horsepower` , and that a model that predicts `mpg` using `horsepower` and `horsepower`[2] gives better results than a model that uses only a linear term. It is natural to wonder whether a cubic or higher-order fit might provide even better results. We answer this question in Chapter 3 by looking at the p-values associated with a cubic term and higher-order polynomial terms in a linear regression. But we could also answer this question using the validation method. We randomly split the 392 observations into two 

5.1 Cross-Validation 203 

����������������������������������������������������������������������������������������������������������������������������������� ��������������������������������������������������������������������������������������������������������������������������������� 

**FIGURE 5.1.** _A schematic display of the validation set approach. A set of n observations are randomly split into a training set (shown in blue, containing observations 7, 22, and 13, among others) and a validation set (shown in beige, and containing observation 91, among others). The statistical learning method is fit on the training set, and its performance is evaluated on the validation set._ 

sets, a training set containing 196 of the data points, and a validation set containing the remaining 196 observations. The validation set error rates that result from fitting various regression models on the training sample and evaluating their performance on the validation sample, using MSE as a measure of validation set error, are shown in the left-hand panel of Figure 5.2. The validation set MSE for the quadratic fit is considerably smaller than for the linear fit. However, the validation set MSE for the cubic fit is actually slightly larger than for the quadratic fit. This implies that including a cubic term in the regression does not lead to better prediction than simply using a quadratic term. 

Recall that in order to create the left-hand panel of Figure 5.2, we randomly divided the data set into two parts, a training set and a validation set. If we repeat the process of randomly splitting the sample set into two parts, we will get a somewhat different estimate for the test MSE. As an illustration, the right-hand panel of Figure 5.2 displays ten different validation set MSE curves from the `Auto` data set, produced using ten different random splits of the observations into training and validation sets. All ten curves indicate that the model with a quadratic term has a dramatically smaller validation set MSE than the model with only a linear term. Furthermore, all ten curves indicate that there is not much benefit in including cubic or higher-order polynomial terms in the model. But it is worth noting that each of the ten curves results in a different test MSE estimate for each of the ten regression models considered. And there is no consensus among the curves as to which model results in the smallest validation set MSE. Based on the variability among these curves, all that we can conclude with any confidence is that the linear fit is not adequate for this data. 

The validation set approach is conceptually simple and is easy to implement. But it has two potential drawbacks: 

1. As is shown in the right-hand panel of Figure 5.2, the validation estimate of the test error rate can be highly variable, depending on precisely which observations are included in the training set and which observations are included in the validation set. 

2. In the validation approach, only a subset of the observations—those that are included in the training set rather than in the validation set—are used to fit the model. Since statistical methods tend to perform worse when trained on fewer observations, this suggests that the 

204 5. Resampling Methods 

![Figure 5.2](./img/5_2.png)

**FIGURE 5.2.** _The validation set approach was used on the_ `Auto` _data set in order to estimate the test error that results from predicting_ `mpg` _using polynomial functions of_ `horsepower` _._ Left: _Validation error estimates for a single split into training and validation data sets._ Right: _The validation method was repeated ten times, each time using a different random split of the observations into a training set and a validation set. This illustrates the variability in the estimated test MSE that results from this approach._ 

validation set error rate may tend to _overestimate_ the test error rate for the model fit on the entire data set. 

In the coming subsections, we will present _cross-validation_ , a refinement of the validation set approach that addresses these two issues. 

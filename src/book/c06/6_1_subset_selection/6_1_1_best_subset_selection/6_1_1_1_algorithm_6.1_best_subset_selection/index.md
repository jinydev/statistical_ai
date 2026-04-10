---
layout: default
title: "index"
---

# **Algorithm 6.1** _Best subset selection_ 

1. Let _M_ 0 denote the _null model_ , which contains no predictors. This model simply predicts the sample mean for each observation. 

2. For _k_ = 1 _,_ 2 _, . . . p_ : 

   - (a) Fit all � _kp_ � models that contain exactly _k_ predictors. (b) Pick the best among these � _kp_ � models, and call it _Mk_ . Here _best_ is defined as having the smallest RSS, or equivalently largest _R_[2] . 

3. Select a single best model from among _M_ 0 _, . . . , Mp_ using using the prediction error on a validation set, _Cp_ (AIC), BIC, or adjusted _R_[2] . Or use the cross-validation method. 

In Algorithm 6.1, Step 2 identifies the best model (on the training data) for each subset size, in order to reduce the problem from one of 2 _[p]_ possible models to one of _p_ + 1 possible models. In Figure 6.1, these models form the lower frontier depicted in red. 

Now in order to select a single best model, we must simply choose among these _p_ + 1 options. This task must be performed with care, because the RSS of these _p_ + 1 models decreases monotonically, and the _R_[2] increases monotonically, as the number of features included in the models increases. Therefore, if we use these statistics to select the best model, then we will always end up with a model involving all of the variables. The problem is that a low RSS or a high _R_[2] indicates a model with a low _training_ error, whereas we wish to choose a model that has a low _test_ error. (As shown in Chapter 2 in Figures 2.9–2.11, training error tends to be quite a bit smaller than test error, and a low training error by no means guarantees a low test error.) Therefore, in Step 3, we use the error on a validation set, _Cp_ , BIC, or adjusted _R_[2] in order to select among _M_ 0 _, M_ 1 _, . . . , Mp_ . If cross-validation is used to select the best model, then Step 2 is repeated on each training fold, and the validation errors are averaged to select the best value of _k_ . 

232 6. Linear Model Selection and Regularization 

![Figure 6.1](./img/6_1.png)

**FIGURE 6.1.** _For each possible model containing a subset of the ten predictors in the_ `Credit` _data set, the RSS and R_[2] _are displayed. The red frontier tracks the_ best _model for a given number of predictors, according to RSS and R_[2] _. Though the data set contains only ten predictors, the x-axis ranges from_ 1 _to_ 11 _, since one of the variables is categorical and takes on three values, leading to the creation of two dummy variables._ 

Then the model _Mk_ fit on the full training set is delivered for the chosen _k_ . These approaches are discussed in Section 6.1.3. 

An application of best subset selection is shown in Figure 6.1. Each plotted point corresponds to a least squares regression model fit using a different subset of the 10 predictors in the `Credit` data set, discussed in Chapter 3. Here the variable `region` is a three-level qualitative variable, and so is represented by two dummy variables, which are selected separately in this case. Hence, there are a total of 11 possible variables which can be included in the model. We have plotted the RSS and _R_[2] statistics for each model, as a function of the number of variables. The red curves connect the best models for each model size, according to RSS or _R_[2] . The figure shows that, as expected, these quantities improve as the number of variables increases; however, from the three-variable model on, there is little improvement in RSS and _R_[2] as a result of including additional predictors. 

Although we have presented best subset selection here for least squares regression, the same ideas apply to other types of models, such as logistic regression. In the case of logistic regression, instead of ordering models by RSS in Step 2 of Algorithm 6.1, we instead use the _deviance_ , a measure deviance that plays the role of RSS for a broader class of models. The deviance is negative two times the maximized log-likelihood; the smaller the deviance, the better the fit. 

While best subset selection is a simple and conceptually appealing approach, it suffers from computational limitations. The number of possible models that must be considered grows rapidly as _p_ increases. In general, there are 2 _[p]_ models that involve subsets of _p_ predictors. So if _p_ = 10, then there are approximately 1,000 possible models to be considered, and if _p_ = 20, then there are over one million possibilities! Consequently, best subset selection becomes computationally infeasible for values of _p_ greater than 

6.1 Subset Selection 233 

**Algorithm 6.2** _Forward stepwise selection_ 

1. Let _M_ 0 denote the _null_ model, which contains no predictors. 

2. For _k_ = 0 _, . . . , p −_ 1: 

   - (a) Consider all _p − k_ models that augment the predictors in _Mk_ with one additional predictor. 

   - (b) Choose the _best_ among these _p − k_ models, and call it _Mk_ +1. Here _best_ is defined as having smallest RSS or highest _R_[2] . 

3. Select a single best model from among _M_ 0 _, . . . , Mp_ using the prediction error on a validation set, _Cp_ (AIC), BIC, or adjusted _R_[2] . Or use the cross-validation method. 

around 40, even with extremely fast modern computers. There are computational shortcuts—so called branch-and-bound techniques—for eliminating some choices, but these have their limitations as _p_ gets large. They also only work for least squares linear regression. We present computationally efficient alternatives to best subset selection next. 

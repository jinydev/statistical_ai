---
layout: default
title: "index"
---

# Validation and Cross-Validation 

As an alternative to the approaches just discussed, we can directly estimate the test error using the validation set and cross-validation methods discussed in Chapter 5. We can compute the validation set error or the cross-validation error for each model under consideration, and then select 

6.1 Subset Selection 239 

![Figure 6.3](./img/6_3.png)

**FIGURE 6.3.** _For the_ `Credit` _data set, three quantities are displayed for the best model containing d predictors, for d ranging from_ 1 _to_ 11 _. The overall_ best _model, based on each of these quantities, is shown as a blue cross._ Left: _Square root of BIC._ Center: _Validation set errors._ Right: _Cross-validation errors._ 

the model for which the resulting estimated test error is smallest. This procedure has an advantage relative to AIC, BIC, _Cp_ , and adjusted _R_[2] , in that it provides a direct estimate of the test error, and makes fewer assumptions about the true underlying model. It can also be used in a wider range of model selection tasks, even in cases where it is hard to pinpoint the model degrees of freedom (e.g. the number of predictors in the model) or hard to estimate the error variance _σ_[2] . Note that when cross-validation is used, the sequence of models _Mk_ in Algorithms 6.1–6.3 is determined separately for each training fold, and the validation errors are averaged over all folds for each model size _k_ . This means, for example with best-subset regression, that _Mk_ , the best subset of size _k_ , can differ across the folds. Once the best size _k_ is chosen, we find the best model of that size on the full data set. 

In the past, performing cross-validation was computationally prohibitive for many problems with large _p_ and/or large _n_ , and so AIC, BIC, _Cp_ , and adjusted _R_[2] were more attractive approaches for choosing among a set of models. However, nowadays with fast computers, the computations required to perform cross-validation are hardly ever an issue. Thus, crossvalidation is a very attractive approach for selecting from among a number of models under consideration. 

Figure 6.3 displays, as a function of _d_ , the BIC, validation set errors, and cross-validation errors on the `Credit` data, for the best _d_ -variable model. The validation errors were calculated by randomly selecting three-quarters of the observations as the training set, and the remainder as the validation set. The cross-validation errors were computed using _k_ = 10 folds. In this case, the validation and cross-validation methods both result in a six-variable model. However, all three approaches suggest that the four-, five-, and six-variable models are roughly equivalent in terms of their test errors. 

In fact, the estimated test error curves displayed in the center and righthand panels of Figure 6.3 are quite flat. While a three-variable model clearly has lower estimated test error than a two-variable model, the estimated test errors of the 3- to 11-variable models are quite similar. Furthermore, if we 

240 6. Linear Model Selection and Regularization 

repeated the validation set approach using a different split of the data into a training set and a validation set, or if we repeated cross-validation using a different set of cross-validation folds, then the precise model with the lowest estimated test error would surely change. In this setting, we can select a model using the _one-standard-error rule_ . We first calculate the onestandard error of the estimated test $\text{MSE}$ for each model size, and then select the smallest model for which the estimated test error is within one error standard error of the lowest point on the curve. The rationale here is that rule if a set of models appear to be more or less equally good, then we might as well choose the simplest model—that is, the model with the smallest number of predictors. In this case, applying the one-standard-error rule to the validation set or cross-validation approach leads to selection of the three-variable model. 

standarderror rule 

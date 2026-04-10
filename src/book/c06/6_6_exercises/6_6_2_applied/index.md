---
layout: default
title: "index"
---

# _Applied_ 

8. In this exercise, we will generate simulated data, and will then use this data to perform forward and backward stepwise selection. 

   - (a) Create a random number generator and use its `normal()` method to generate a predictor _X_ of length _n_ = 100, as well as a noise vector _ϵ_ of length _n_ = 100. 

   - (b) Generate a response vector _Y_ of length _n_ = 100 according to the model

$$
Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \epsilon
$$

where _β_ 0, _β_ 1, _β_ 2, and _β_ 3 are constants of your choice. 

- (c) Use forward stepwise selection in order to select a model containing the predictors _X, X_[2] _, . . . , X_[10] . What is the model obtained according to _Cp_ ? Report the coefficients of the model obtained. 

- (d) Repeat (c), using backwards stepwise selection. How does your answer compare to the results in (c)? 

- (e) Now fit a lasso model to the simulated data, again using _X, X_[2] _, . . . , X_[10] as predictors. Use cross-validation to select the optimal value of _λ_ . Create plots of the cross-validation error as a function of _λ_ . Report the resulting coefficient estimates, and discuss the results obtained. 

- (f) Now generate a response vector _Y_ according to the model

$$
Y = \beta_0 + \beta_7 X^7 + \epsilon
$$

and perform forward stepwise selection and the lasso. Discuss the results obtained. 

9. In this exercise, we will predict the number of applications received using the other variables in the `College` data set. 

   - (a) Split the data set into a training set and a test set. 

   - (b) Fit a linear model using least squares on the training set, and report the test error obtained. 

   - (c) Fit a ridge regression model on the training set, with _λ_ chosen by cross-validation. Report the test error obtained. 

   - (d) Fit a lasso model on the training set, with _λ_ chosen by crossvalidation. Report the test error obtained, along with the number of non-zero coefficient estimates. 

   - (e) Fit a PCR model on the training set, with _M_ chosen by crossvalidation. Report the test error obtained, along with the value of _M_ selected by cross-validation. 

   - (f) Fit a PLS model on the training set, with _M_ chosen by crossvalidation. Report the test error obtained, along with the value of _M_ selected by cross-validation. 

6.6 Exercises 287 

   - (g) Comment on the results obtained. How accurately can we predict the number of college applications received? Is there much difference among the test errors resulting from these five approaches? 

10. We have seen that as the number of features used in a model increases, the training error will necessarily decrease, but the test error may not. We will now explore this in a simulated data set. 

   - (a) Generate a data set with _p_ = 20 features, _n_ = 1 _,_ 000 observations, and an associated quantitative response vector generated according to the model 

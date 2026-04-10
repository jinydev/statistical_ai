---
layout: default
title: "index"
---

# Additional Details 

The discussion of Cox’s proportional hazards model glossed over a few subtleties: 

- There is no intercept in (11.14) nor in the equations that follow, because an intercept can be absorbed into the baseline hazard _h_ 0( _t_ ). 

- We have assumed that there are no tied failure times. In the case of ties, the exact form of the partial likelihood (11.16) is a bit more complicated, and a number of computational approximations must be used. 

- (11.16) is known as the _partial_ likelihood because it is not exactly a likelihood. That is, it does not correspond exactly to the probability of the data under the assumption (11.14). However, it is a very good approximation. 

- We have focused only on estimation of the coefficients _β_ = ( _β_ 1 _, . . . , βp_ ) _[T]_ . However, at times we may also wish to estimate the baseline hazard _h_ 0( _t_ ), for instance so that we can estimate the survival curve _S_ ( _t|x_ ) for an individual with feature vector _x_ . The details are beyond the scope of this book. Estimation of _h_ 0( _t_ ) is implemented in the `lifelines` package in `Python` , which we will see in Section 11.8. 

482 11. Survival Analysis and Censored Data 

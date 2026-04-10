---
layout: default
title: "index"
---

# Pros and Cons of GAMs 

Before we move on, let us summarize the advantages and limitations of a GAM. 

- L GAMs allow us to fit a non-linear _fj_ to each _Xj_ , so that we can automatically model non-linear relationships that standard linear regression will miss. This means that we do not need to manually try out many different transformations on each variable individually. 

- L The non-linear fits can potentially make more accurate predictions for the response _Y_ . 

- L Because the model is additive, we can examine the effect of each _Xj_ on _Y_ individually while holding all of the other variables fixed. 

- L The smoothness of the function _fj_ for the variable _Xj_ can be summarized via degrees of freedom. 

- N The main limitation of GAMs is that the model is restricted to be additive. With many variables, important interactions can be missed. However, as with linear regression, we can manually add interaction terms to the GAM model by including additional predictors of the form _Xj × Xk_ . In addition we can add low-dimensional interaction functions of the form _fjk_ ( _Xj, Xk_ ) into the model; such terms can be fit using two-dimensional smoothers such as local regression, or two-dimensional splines (not covered here). 

For fully general models, we have to look for even more flexible approaches such as random forests and boosting, described in Chapter 8. GAMs provide a useful compromise between linear and fully nonparametric models. 

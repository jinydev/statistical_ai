---
layout: default
title: "index"
---

# _11.7.1 Area Under the Curve for Survival Analysis_ 

In Chapter 4, we introduced the area under the ROC curve — often referred to as the “AUC” — as a way to quantify the performance of a two-class classifier. Define the _score_ for the _i_ th observation to be the classifier’s estimate of Pr( _Y_ = 1 _|X_ = _xi_ ). It turns out that if we consider all pairs consisting of one observation in Class 1 and one observation in Class 2, then the AUC is the fraction of pairs for which the score for the observation in Class 1 exceeds the score for the observation in Class 2. 

This suggests a way to generalize the notion of AUC to survival analˆ ysis. We calculate an estimated risk score, _ηi_ = _β_[ˆ] 1 _xi_ 1 + _· · ·_ + _β_[ˆ] _pxip_ , for ˆ ˆ _i_ = 1 _, . . . , n_ , using the Cox model coefficients. If _ηi′ > ηi_ , then the model predicts that the _i[′]_ th observation has a larger hazard than the _i_ th observation, and thus that the survival time _ti_ will be _greater_ than _ti′_ . Thus, it is tempting to try to generalize AUC by computing the proportion of obˆ ˆ servations for which _ti > ti′_ and _ηi′ > ηi_ . However, things are not quite so easy, because recall that we do not observe _t_ 1 _, . . . , tn_ ; instead, we observe 

11.7 Additional Topics 487 

**FIGURE** _compute tertiles of “risk” in the test set using coefficients estimated on the training_ **11.8.** _For the_ `Publication` _data introduced in Section 11.5.4, we set. There is clear separation between the resulting survival curves._ 

the (possibly-censored) times _y_ 1 _, . . . , yn_ , as well as the censoring indicators _δ_ 1 _, . . . , δn_ . 

Therefore, _Harrell’s concordance index_ (or _C-index_ ) computes the proˆ ˆ Harrell’s portion of observation pairs for which _ηi′ > ηi_ and _yi > yi′_ :

concordance index

$$
C = \frac{ \sum_{i, i'} I(y_i > y_{i'}, \delta_{i'} = 1) I(\hat{\eta}_{i'} > \hat{\eta}_i) }{ \sum_{i, i'} I(y_i > y_{i'}, \delta_{i'} = 1) } \quad (11.18)
$$

where the indicator variable _I_ (ˆ _ηi′ > ηi_ ) equals one if _ηi′ > ηi_ , and equals zero otherwise. The numerator and denominator are multiplied by the status indicator _δi′_ , since if the _i[′]_ th observation is uncensored (i.e. if _δi′_ = 1), then _yi > yi′_ implies that _ti > ti′_ . By contrast, if _δi′_ = 0, then _yi > yi′_ does not imply that _ti > ti′_ . 

We fit a Cox proportional hazards model on the training set of the `Publication` data, and computed the _C_ -index on the test set. This yielded _C_ = 0 _._ 733. Roughly speaking, given two random papers from the test set, the model can predict with 73.3% accuracy which will be published first. 

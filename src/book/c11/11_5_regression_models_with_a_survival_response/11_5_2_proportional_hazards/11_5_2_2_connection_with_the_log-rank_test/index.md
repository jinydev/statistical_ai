---
layout: default
title: "index"
---

# Connection With The Log-Rank Test 

Suppose we have just a single predictor ( _p_ = 1), which we assume to be binary, i.e. _xi ∈{_ 0 _,_ 1 _}_ . In order to determine whether there is a difference between the survival times of the observations in the group _{i_ : _xi_ = 0 _}_ and those in the group _{i_ : _xi_ = 1 _}_ , we can consider taking two possible approaches: 

_Approach #1:_ Fit a Cox proportional hazards model, and test the null hypothesis _H_ 0 : _β_ = 0. (Since _p_ = 1, _β_ is a scalar.) 

_Approach #2:_ Perform a log-rank test to compare the two groups, as in Section 11.4. 

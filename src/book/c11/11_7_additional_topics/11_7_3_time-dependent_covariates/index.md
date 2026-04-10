---
layout: default
title: "index"
---

# _11.7.3 Time-Dependent Covariates_ 

A powerful feature of the proportional hazards model is its ability to handle _time-dependent covariates_ , predictors whose value may change over time. For example, suppose we measure a patient’s blood pressure every week over the course of a medical study. In this case, we can think of the blood pressure for the _i_ th observation not as _xi_ , but rather as _xi_ ( _t_ ) at time _t_ . 

Because the partial likelihood in (11.16) is constructed sequentially in time, dealing with time-dependent covariates is straightforward. In particular, we simply replace _xij_ and _xi′j_ in (11.16) with _xij_ ( _yi_ ) and _xi′j_ ( _yi_ ), respectively; these are the current values of the predictors at time _yi_ . By contrast, time-dependent covariates would pose a much greater challenge within the context of a traditional parametric approach, such as (11.13). 

One example of time-dependent covariates appears in the analysis of data from the Stanford Heart Transplant Program. Patients in need of a heart transplant were put on a waiting list. Some patients received a transplant, but others died while still on the waiting list. The primary objective of the analysis was to determine whether a transplant was associated with longer patient survival. 

A naïve approach would use a fixed covariate to represent transplant status: that is, _xi_ = 1 if the _i_ th patient ever received a transplant, and _xi_ = 0 otherwise. But this approach overlooks the fact that patients had to live long enough to get a transplant, and hence, on average, healthier patients received transplants. This problem can be solved by using a time-dependent covariate for transplant: _xi_ ( _t_ ) = 1 if the patient received a transplant by time _t_ , and _xi_ ( _t_ ) = 0 otherwise. 

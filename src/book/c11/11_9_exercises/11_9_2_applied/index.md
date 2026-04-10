---
layout: default
title: "index"
---

# _Applied_ 

10. This exercise focuses on the brain tumor data, which is included in the `ISLP` library. 

   - (a) Plot the Kaplan-Meier survival curve with _±_ 1 standard error bands, using the `KaplanMeierFitter()` estimator in the `lifelines` package. 

   - (b) Draw a bootstrap sample of size _n_ = 88 from the pairs ( _yi, δi_ ), and compute the resulting Kaplan-Meier survival curve. Repeat this process _B_ = 200 times. Use the results to obtain an estimate of the standard error of the Kaplan-Meier survival curve at each timepoint. Compare this to the standard errors obtained in (a). 

   - (c) Fit a Cox proportional hazards model that uses all of the predictors to predict survival. Summarize the main findings. 

   - (d) Stratify the data by the value of `ki` . (Since only one observation has `ki==40` , you can group that observation together with the observations that have `ki==60` .) Plot Kaplan-Meier survival curves for each of the five strata, adjusted for the other predictors. 

11. This exercise makes use of the data in Table 11.4. 

   - (a) Create two groups of observations. In Group 1, _X <_ 2, whereas in Group 2, _X ≥_ 2. Plot the Kaplan-Meier survival curves corresponding to the two groups. Be sure to label the curves so that it is clear which curve corresponds to which group. By eye, does there appear to be a difference between the two groups’ survival curves? 

   - (b) Fit Cox’s proportional hazards model, using the group indicator as a covariate. What is the estimated coefficient? Write a sentence providing the interpretation of this coefficient, in terms of the hazard or the instantaneous probability of the event. Is there evidence that the true coefficient value is non-zero? 

   - (c) Recall from Section 11.5.2 that in the case of a single binary covariate, the log-rank test statistic should be identical to the score statistic for the Cox model. Conduct a log-rank test to determine whether there is a difference between the survival curves for the two groups. How does the _p_ -value for the log-rank test statistic compare to the _p_ -value for the score statistic for the Cox model from (b)? 

12 Unsupervised Learning 

Most of this book concerns _supervised learning_ methods such as regression and classification. In the supervised learning setting, we typically have access to a set of _p_ features _X_ 1 _, X_ 2 _, . . . , Xp_ , measured on _n_ observations, and a response _Y_ also measured on those same _n_ observations. The goal is then to predict _Y_ using _X_ 1 _, X_ 2 _, . . . , Xp_ . 

This chapter will instead focus on _unsupervised learning_ , a set of statistical tools intended for the setting in which we have only a set of features _X_ 1 _, X_ 2 _, . . . , Xp_ measured on _n_ observations. We are not interested in prediction, because we do not have an associated response variable _Y_ . Rather, the goal is to discover interesting things about the measurements on _X_ 1 _, X_ 2 _, . . . , Xp_ . Is there an informative way to visualize the data? Can we discover subgroups among the variables or among the observations? Unsupervised learning refers to a diverse set of techniques for answering questions such as these. In this chapter, we will focus on two particular types of unsupervised learning: _principal components analysis_ , a tool used for data visualization or data pre-processing before supervised techniques are applied, and _clustering_ , a broad class of methods for discovering unknown subgroups in data. 

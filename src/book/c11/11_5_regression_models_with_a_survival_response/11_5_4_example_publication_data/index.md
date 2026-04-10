---
layout: default
title: "index"
---

# _11.5.4 Example: Publication Data_ 

Next, we consider the dataset `Publication` involving the time to publication of journal papers reporting the results of clinical trials funded by the National Heart, Lung, and Blood Institute.[14] For 244 trials, the time in months until publication is recorded. Of the 244 trials, only 156 were published during the study period; the remaining studies were censored. The covariates include whether the trial focused on a clinical endpoint ( `clinend` ), whether the trial involved multiple centers ( `multi` ), the funding mechanism within the National Institutes of Health ( `mech` ), trial sample size ( `sampsize` ), budget ( `budget` ), impact ( `impact` , related to the number of citations), and whether the trial produced a positive (significant) result ( `posres` ). The last covariate is particularly interesting, as a number of studies have suggested that positive trials have a higher publication rate. 

> 14This dataset is described in the following paper: Gordon et al. (2013) Publication of trials funded by the National Heart, Lung, and Blood Institute. New England Journal of Medicine, 369(20):1926–1934. 

11.5 Regression Models With a Survival Response 483 

![Figure 11.5](./img/11_5.png)

**FIGURE 11.5.** _Survival curves for time until publication for the_ `Publication` _data described in Section 11.5.4, stratified by whether or not the study produced a positive result._ 

Figure 11.5 shows the Kaplan–Meier curves for the time until publication, stratified by whether or not the study produced a positive result. We see slight evidence that time until publication is lower for studies with a positive result. However, the log-rank test yields a very unimpressive _p_ -value of 0 _._ 36. 

We now consider a more careful analysis that makes use of all of the available predictors. The results of fitting Cox’s proportional hazards model using all of the available features are shown in Table 11.3. We find that the chance of publication of a study with a positive result is _e_[0] _[.]_[55] = 1 _._ 74 times higher than the chance of publication of a study with a negative result at any point in time, holding all other covariates fixed. The very small _p_ -value associated with `posres` in Table 11.3 indicates that this result is highly significant. This is striking, especially in light of our earlier finding that a log-rank test comparing time to publication for studies with positive versus negative results yielded a _p_ -value of 0 _._ 36. How can we explain this discrepancy? The answer stems from the fact that the log-rank test did not consider any other covariates, whereas the results in Table 11.3 are based on a Cox model using all of the available covariates. In other words, after we adjust for all of the other covariates, then whether or not the study yielded a positive result is highly predictive of the time to publication. 

In order to gain more insight into this result, in Figure 11.6 we display estimates of the survival curves associated with positive and negative results, adjusting for the other predictors. To produce these survival curves, we estimated the underlying baseline hazard _h_ 0( _t_ ). We also needed to select representative values for the other predictors; we used the mean value for each predictor, except for the categorical predictor `mech` , for which we used the most prevalent category ( `R01` ). Adjusting for the other predictors, we now see a clear difference in the survival curves between studies with positive versus negative results. 

Other interesting insights can be gleaned from Table 11.3. For example, studies with a clinical endpoint are more likely to be published at any given point in time than those with a non-clinical endpoint. The funding 

484 11. Survival Analysis and Censored Data 

||Coefcient|Std. error|_z_-statistic|_p_-value|
|---|---|---|---|---|
|`posres[Yes]`|0.55|0.18|3.02|0.00|
|`multi[Yes]`|0.15|0.31|0.47|0.64|
|`clinend[Yes]`|0.51|0.27|1.89|0.06|
|`mech[K01]`|1.05|1.06|1.00|0.32|
|`mech[K23]`|-0.48|1.05|-0.45|0.65|
|`mech[P01]`|-0.31|0.78|-0.40|0.69|
|`mech[P50]`|0.60|1.06|0.57|0.57|
|`mech[R01]`|0.10|0.32|0.30|0.76|
|`mech[R18]`|1.05|1.05|0.99|0.32|
|`mech[R21]`|-0.05|1.06|-0.04|0.97|
|`mech[R24,K24]`|0.81|1.05|0.77|0.44|
|`mech[R42]`|-14.78|3414.38|-0.00|1.00|
|`mech[R44]`|-0.57|0.77|-0.73|0.46|
|`mech[RC2]`|-14.92|2243.60|-0.01|0.99|
|`mech[U01]`|-0.22|0.32|-0.70|0.48|
|`mech[U54]`|0.47|1.07|0.44|0.66|
|`sampsize`|0.00|0.00|0.19|0.85|
|`budget`|0.00|0.00|1.67|0.09|
|`impact`|0.06|0.01|8.23|0.00|



**TABLE 11.3.** _Results for Cox’s proportional hazards model fit to the_ `Publication` _data, using all of the available features. The features_ `posres` _,_ `multi` _, and_ `clinend` _are binary. The feature_ `mech` _is qualitative with 14 levels; it is coded so that the baseline level is_ `Contract` _._ 

mechanism did not appear to be significantly associated with time until publication. 

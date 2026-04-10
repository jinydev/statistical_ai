---
layout: default
title: "index"
---

# _11.5.3 Example: Brain Cancer Data_ 

Table 11.2 shows the result of fitting the proportional hazards model to the `BrainCancer` data, which was originally described in Section 11.3. The coefficient column displays _β_[ˆ] _j_ . The results indicate, for instance, that the estimated hazard for a male patient is _e_[0] _[.]_[18] = 1 _._ 2 times greater than for a female patient: in other words, with all other features held fixed, males have a 1.2 times greater chance of dying than females, at any point in time. However, the _p_ -value is 0 _._ 61, which indicates that this difference between males and females is not significant. 

As another example, we also see that each one-unit increase in the Karnofsky index corresponds to a multiplier of exp( _−_ 0 _._ 05) = 0 _._ 95 in the instantaneous chance of dying. In other words, the higher the Karnofsky index, the lower the chance of dying at any given point in time. This effect is highly significant, with a _p_ -value of 0 _._ 0027. 

||Coefcient|Std. error|_z_-statistic|_p_-value|
|---|---|---|---|---|
|`sex[Male]`|0.18|0.36|0.51|0.61|
|`diagnosis[LG Glioma]`|0.92|0.64|1.43|0.15|
|`diagnosis[HG Glioma]`|2.15|0.45|4.78|0.00|
|`diagnosis[Other]`|0.89|0.66|1.35|0.18|
|`loc[Supratentorial]`|0.44|0.70|0.63|0.53|
|`ki`|-0.05|0.02|-3.00|_<_0.01|
|`gtv`|0.03|0.02|1.54|0.12|
|`stereo[SRT]`|0.18|0.60|0.30|0.77|



**TABLE 11.2.** _Results for Cox’s proportional hazards model fit to the_ `BrainCancer` _data, which was first described in Section 11.3. The variable_ `diagnosis` _is qualitative with four levels: meningioma, LG glioma, HG glioma, or other. The variables_ `sex` _,_ `loc` _, and_ `stereo` _are binary._ 

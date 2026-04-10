---
layout: default
title: "index"
---

# _11.7.2 Choice of Time Scale_ 

In the examples considered thus far in this chapter, it has been fairly clear how to define _time_ . For example, in the `Publication` example, _time zero_ for each paper was defined to be the calendar time at the end of the study, and the failure time was defined to be the number of months that elapsed from the end of the study until the paper was published. 

However, in other settings, the definitions of time zero and failure time may be more subtle. For example, when examining the association between risk factors and disease occurrence in an epidemiological study, one might use the patient’s age to define time, so that time zero is the patient’s date of birth. With this choice, the association between age and survival cannot be measured; however, there is no need to adjust for age in the analysis. When examining covariates associated with disease-free survival (i.e. the 

488 11. Survival Analysis and Censored Data 

amount of time elapsed between treatment and disease recurrence), one might use the date of treatment as time zero. 

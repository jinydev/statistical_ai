---
layout: default
title: "index"
---

# _6.4.1 High-Dimensional Data_ 

Most traditional statistical techniques for regression and classification are intended for the _low-dimensional_ setting in which _n_ , the number of ob- lowservations, is much greater than _p_ , the number of features. This is due in part to the fact that throughout most of the field’s history, the bulk of scientific problems requiring the use of statistics have been low-dimensional. For instance, consider the task of developing a model to predict a patient’s blood pressure on the basis of his or her age, sex, and body mass index (BMI). There are three predictors, or four if an intercept is included in the model, and perhaps several thousand patients for whom blood pressure and age, sex, and BMI are available. Hence _n ≫ p_ , and so the problem is low-dimensional. (By dimension here we are referring to the size of _p_ .) 

dimensional 

In the past 20 years, new technologies have changed the way that data are collected in fields as diverse as finance, marketing, and medicine. It is now commonplace to collect an almost unlimited number of feature measurements ( _p_ very large). While _p_ can be extremely large, the number of observations _n_ is often limited due to cost, sample availability, or other considerations. Two examples are as follows: 

1. Rather than predicting blood pressure on the basis of just age, sex, and BMI, one might also collect measurements for half a million _single nucleotide polymorphisms_ (SNPs; these are individual DNA mutations that are relatively common in the population) for inclusion in the predictive model. Then _n ≈_ 200 and _p ≈_ 500 _,_ 000. 

2. A marketing analyst interested in understanding people’s online shopping patterns could treat as features all of the search terms entered by users of a search engine. This is sometimes known as the “bag-ofwords” model. The same researcher might have access to the search histories of only a few hundred or a few thousand search engine users who have consented to share their information with the researcher. For a given user, each of the _p_ search terms is scored present (0) or 

6.4 Considerations in High Dimensions 263 

absent (1), creating a large binary feature vector. Then _n ≈_ 1 _,_ 000 and _p_ is much larger. 

Data sets containing more features than observations are often referred to as _high-dimensional_ . Classical approaches such as least squares linear highregression are not appropriate in this setting. Many of the issues that arise in the analysis of high-dimensional data were discussed earlier in this book, since they apply also when _n > p_ : these include the role of the bias-variance trade-off and the danger of overfitting. Though these issues are always relevant, they can become particularly important when the number of features is very large relative to the number of observations. 

dimensional 

We have defined the _high-dimensional setting_ as the case where the number of features _p_ is larger than the number of observations _n_ . But the considerations that we will now discuss certainly also apply if _p_ is slightly smaller than _n_ , and are best always kept in mind when performing supervised learning. 

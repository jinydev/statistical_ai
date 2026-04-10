---
layout: default
title: "index"
---

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing. However, this result is misleading because we trained and tested the model on the same set of 1,250 observations. In other words, 100 _−_ 52 _._ 2 = 47 _._ 8% is the _training_ error rate. As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate. In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data. This will yield a more realistic error rate, in the sense that in practice we will be interested in our model’s performance not on the data that we used to fit the model, but rather on days in the future for which the market’s movements are unknown. 

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004. We then use this vector to create a held out data set of observations from 2005. 

**`In [14]:`** `train = (Smarket.Year < 2005) Smarket_train = Smarket.loc[train] Smarket_test = Smarket.loc[` _∼_ `train] Smarket_test.shape` 

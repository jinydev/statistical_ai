---
layout: default
title: "index"
---

# **`In [8]:`** `results.params` 

|**`Out[8]:`**|`intercept`|`-0.126000`|
|---|---|---|
||`Lag1`|`-0.073074`|
||`Lag2`|`-0.042301`|
||`Lag3`|`0.011085`|
||`Lag4`|`0.009359`|
||`Lag5`|`0.010313`|
||`Volume`|`0.135441`|
||`dtype: float64`||



Likewise we can use the `pvalues` attribute to access the _p_ -values for the coefficients (not shown). 

```
In [9]:results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors. This method returns predictions on the probability scale. If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model. As with linear regression, one can pass an optional `exog` argument consistent with a design matrix if desired. Here we have printed only the first ten probabilities. 

```
In [10]:probs=results.predict()
probs[:10]
```

```
Out[10]:array([0.5070841,0.4814679,0.4811388,0.5152223,0.5107812,
0.5069565,0.4926509,0.5092292,0.5176135,0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down` . The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5. 

```
In [11]:labels=np.array(['Down']*1250)
labels[probs >0.5]="Up"
```

176 4. Classification 

The `confusion_table()` function from the `ISLP` package summarizes these `confusion_` predictions, showing how many observations were correctly or incorrectly `table()` classified. Our function, which is adapted from a similar function in the module `sklearn.metrics` , transposes the resulting matrix and includes row and column labels. The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels. 

```
In [12]:confusion_table(labels,Smarket.Direction)
```

|**`Out[12]:`**|`Truth`|`Down`|`Up`|
|---|---|---|---|
||`Predicted`|||
||`Down`|`145`|`141`|
||`Up`|`457`|`507`|



The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions. Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions. The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct. In this case, logistic regression correctly predicted the movement of the market 52.2% of the time. 

```
In [13]:(507+145)/1250,np.mean(labels==Smarket.Direction)
```

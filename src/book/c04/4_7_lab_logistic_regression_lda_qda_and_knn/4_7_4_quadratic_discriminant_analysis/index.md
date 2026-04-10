---
layout: default
title: "index"
---

# _4.7.4 Quadratic Discriminant Analysis_ 

We will now fit a QDA model to the `Smarket` data. QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we ab- `Quadratic` breviate to `QDA()` . The syntax is very similar to `LDA()` . 

```
Discriminant
Analysis()
```

```
In [33]:qda=QDA(store_covariance=True)
qda.fit(X_train,L_train)
```

```
Out[33]:QuadraticDiscriminantAnalysis(store_covariance=True)
```

The `QDA()` function will again compute `means_` and `priors_` . 

```
In [34]:qda.means_,qda.priors_
```

```
Out[34]:(array([[0.04279022,0.03389409],
[-0.03954635,-0.03132544]]),
array([0.49198397,0.50801603]))
```

The `QDA()` classifier will estimate one covariance per class. Here is the estimated covariance in the first class: 

```
In [35]:qda.covariance_[0]
```

```
Out[35]:array([[1.50662277,-0.03924806],
[-0.03924806,1.53559498]])
```

The output contains the group means. But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors. The `predict()` function works in exactly the same fashion as for LDA. 

182 4. Classification 

```
In [36]:qda_pred=qda.predict(X_test)
confusion_table(qda_pred,L_test)
```

```
Out[36]:TruthDownUp
Predicted
Down3020
Up81121
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model. 

```
In [37]:np.mean(qda_pred==L_test)
```

```
Out[37]:0.599
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately. This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression. However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market! 

_4.7.5 Naive Bayes_ 

Next, we fit a naive Bayes model to the `Smarket` data. The syntax is similar to that of `LDA()` and `QDA()` . By default, this implementation `GaussianNB()` of the naive Bayes classifier models each quantitative feature using a Gaussian `GaussianNB()` distribution. However, a kernel density method can also be used to estimate the distributions. 

```
In [38]:NB=GaussianNB()
NB.fit(X_train,L_train)
```

```
Out[38]:GaussianNB()
```

The classes are stored as `classes_` . 

```
In [39]:NB.classes_
```

```
Out[39]:array(['Down','Up'],dtype='<U4')
```

The class prior probabilities are stored in the `class_prior_` attribute. 

```
In [40]:NB.class_prior_
```

```
Out[40]:array([0.49,0.51])
```

The parameters of the features can be found in the `theta_` and `var_` attributes. The number of rows is equal to the number of classes, while the number of columns is equal to the number of features. We see below that the mean for feature `Lag1` in the `Down` class is 0.043. 

```
In [41]:NB.theta_
```

```
Out[41]:array([[0.043,0.034],
[-0.040,-0.031]])
```

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 183 

Its variance is 1.503. 

```
In [42]:NB.var_
```

```
Out[42]:array([[1.503,1.532],
[1.514,1.487]])
```

How do we know the names of these attributes? We use `NB?` (or `?NB` ). We can easily verify the mean computation: 

```
In [43]:X_train[L_train=='Down'].mean()
```

```
Out[43]:Lag10.042790
Lag20.033894
dtype:float64
```

Similarly for the variance: 

```
In [44]:X_train[L_train=='Down'].var(ddof=0)
```

```
Out[44]:Lag11.503554
Lag21.532467
dtype:float64
```

The `GaussianNB()` function calculates variances using the 1 _/n_ formula.[6] Since `NB()` is a classifier in the `sklearn` library, making predictions uses the same syntax as for `LDA()` and `QDA()` above. 

```
In [45]:nb_labels=NB.predict(X_test)
confusion_table(nb_labels,L_test)
```

```
Out[45]:TruthDownUp
Predicted
Down2920
Up82121
```

Naive Bayes performs well on these data, with accurate predictions over 59% of the time. This is slightly worse than QDA, but much better than LDA. 

As for `LDA` , the `predict_proba()` method estimates the probability that each observation belongs to a particular class. 

```
In [46]:NB.predict_proba(X_test)[:5]
```

```
Out[46]:array([[0.4873,0.5127],
[0.4762,0.5238],
[0.4653,0.5347],
[0.4748,0.5252],
[0.4902,0.5098]])
```

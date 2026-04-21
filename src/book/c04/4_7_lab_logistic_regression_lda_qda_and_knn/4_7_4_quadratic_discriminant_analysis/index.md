---
layout: default
title: "index"
---

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/index.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/index.html)


# _4.7.4 Quadratic Discriminant Analysis_ 

We will now fit a QDA model to the `Smarket` data. QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we abbreviate to `QDA()`. The syntax is very similar to `LDA()`. 

```python
In [33]: qda = QDA(store_covariance=True)
qda.fit(X_train, L_train)
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True)
```

The `QDA()` function will again compute `means_` and `priors_`. 

```python
In [34]: qda.means_, qda.priors_
```

```python
Out[34]: (array([[ 0.04279022,  0.03389409],
                 [-0.03954635, -0.03132544]]),
          array([0.49198397, 0.50801603]))
```

The `QDA()` classifier will estimate one covariance per class. Here is the estimated covariance in the first class: 

```python
In [35]: qda.covariance_[0]
```

```python
Out[35]: array([[ 1.50662277, -0.03924806],
                [-0.03924806,  1.53559498]])
```

The output contains the group means. But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors. The `predict()` function works in exactly the same fashion as for LDA. 

```python
In [36]: qda_pred = qda.predict(X_test)
confusion_table(qda_pred, L_test)
```

```python
Out[36]: Truth      Down   Up
Predicted            
Down         30   20
Up           81  121
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model. 

```python
In [37]: np.mean(qda_pred == L_test)
```

```python
Out[37]: 0.5992063492063492
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately. This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression. However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market!

---

## Sub-Chapters


[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/index.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/index.html)

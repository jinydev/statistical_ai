---
layout: default
title: "index"
---

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/index.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/index.html)


# _4.7.3 Linear Discriminant Analysis_ 

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()`, which we have abbreviated `LDA()`. We fit the model using only the observations before 2005.

```python
In [22]: lda = LDA(store_covariance=True)
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test`. We can also directly use the labels rather than the Boolean vectors `y_train`. 

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept']) for M in [X_train, X_test]]
lda.fit(X_train, L_train)
```

```python
Out[23]: LinearDiscriminantAnalysis(store_covariance=True)
```

Here we have used the list comprehensions introduced in Section 3.6.4. Looking at our first line above, we see that the right-hand side is a list of length two. This is because the code `for M in [X_train, X_test]` iterates over a list of length two. While here we loop over a list, the list comprehension method works when looping over any iterable object. We then apply the `drop()` method to each element in the iteration, collecting the result in a list. The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test`. Of course, this overwrites the previous values of `X_train` and `X_test`. 

Having fit the model, we can extract the means in the two classes with the `means_` attribute. These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_k$. These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines. 

```python
In [24]: lda.means_
```

```python
Out[24]: array([[ 0.0426,  0.0338],
                [-0.0395, -0.0313]])
```

The estimated prior probabilities are stored in the `priors_` attribute. The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method. We can be sure of which entry corresponds to which label by looking at the `classes_` attribute. 

```python
In [25]: lda.classes_
```

```python
Out[25]: array(['Down', 'Up'], dtype='<U4')
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$. 

```python
In [26]: lda.priors_
```

```python
Out[26]: array([0.49198397, 0.50801603])
```

The linear discriminant vectors can be found in the `scalings_` attribute: 

```python
In [27]: lda.scalings_
```

```python
Out[27]: array([[-0.64201906],
                [-0.51352928]])
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule. In other words, these are the multipliers of the elements of $X = x$ in (4.24). If $-0.642 	imes Lag1 - 0.513 	imes Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline. 

```python
In [28]: lda_pred = lda.predict(X_test)
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical. 

```python
In [29]: confusion_table(lda_pred, L_test)
```

```python
Out[29]: Truth      Down   Up
Predicted            
Down         35   35
Up           76  106
```

We can also estimate the probability of each class for each point in a training set. Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in `lda_pred`. 

```python
In [30]: lda_prob = lda.predict_proba(X_test)
np.all(
    np.where(lda_prob[:,1] >= 0.5, 'Up','Down') == lda_pred
)
```

```python
Out[30]: True
```

Above, we used the `np.where()` function that creates an array with value `'Up'` for indices where the second column of `lda_prob` (the estimated posterior probability of `'Up'`) is greater than 0.5. For problems with more than two classes the labels are chosen as the class whose posterior probability is highest:

```python
In [31]: np.all(
    [lda.classes_[i] for i in np.argmax(lda_prob, 1)] == lda_pred
)
```

---

---

## Sub-Chapters


[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/index.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/index.html)

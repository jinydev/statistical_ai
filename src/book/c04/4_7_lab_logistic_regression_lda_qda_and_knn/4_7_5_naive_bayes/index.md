---
layout: default
title: "index"
---

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/index.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/index.html)


# _4.7.5 Naive Bayes_ 

Next, we fit a naive Bayes model to the `Smarket` data. The syntax is similar to that of `LDA()` and `QDA()`. By default, this implementation of the naive Bayes classifier models each quantitative feature using a Gaussian distribution. However, a kernel density method can also be used to estimate the distributions. 

```python
In [38]: NB = GaussianNB()
NB.fit(X_train, L_train)
```

```python
Out[38]: GaussianNB()
```

The classes are stored as `classes_`. 

```python
In [39]: NB.classes_
```

```python
Out[39]: array(['Down', 'Up'], dtype='<U4')
```

The class prior probabilities are stored in the `class_prior_` attribute. 

```python
In [40]: NB.class_prior_
```

```python
Out[40]: array([0.49198397, 0.50801603])
```

The parameters of the features can be found in the `theta_` and `var_` attributes. The number of rows is equal to the number of classes, while the number of columns is equal to the number of features. We see below that the mean for feature `Lag1` in the `Down` class is $0.043$. 

```python
In [41]: NB.theta_
```

```python
Out[41]: array([[ 0.04279022,  0.03389409],
                [-0.03954635, -0.03132544]])
```

Its variance is $1.503$. 

```python
In [42]: NB.var_
```

```python
Out[42]: array([[1.50355424, 1.53246652],
                [1.51397116, 1.4870335 ]])
```

How do we know the names of these attributes? We use `NB?` (or `?NB`). We can easily verify the mean computation: 

```python
In [43]: X_train[L_train == 'Down'].mean()
```

```python
Out[43]: Lag1    0.042790
         Lag2    0.033894
         dtype: float64
```

Similarly for the variance: 

```python
In [44]: X_train[L_train == 'Down'].var(ddof=0)
```

```python
Out[44]: Lag1    1.503554
         Lag2    1.532467
         dtype: float64
```

The `GaussianNB()` function calculates variances using the $1/n$ formula. Since `NB()` is a classifier in the `sklearn` library, making predictions uses the same syntax as for `LDA()` and `QDA()` above. 

```python
In [45]: nb_labels = NB.predict(X_test)
confusion_table(nb_labels, L_test)
```

```python
Out[45]: Truth      Down   Up
Predicted            
Down         29   20
Up           82  121
```

Naive Bayes performs well on these data, with accurate predictions over 59% of the time. This is slightly worse than QDA, but much better than LDA. 

As for `LDA`, the `predict_proba()` method estimates the probability that each observation belongs to a particular class. 

```python
In [46]: NB.predict_proba(X_test)[:5]
```

```python
Out[46]: array([[0.48732444, 0.51267556],
                [0.47620455, 0.52379545],
                [0.46526732, 0.53473268],
                [0.47481179, 0.52518821],
                [0.49015096, 0.50984904]])
```

---

## Sub-Chapters


[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/index.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/index.html)

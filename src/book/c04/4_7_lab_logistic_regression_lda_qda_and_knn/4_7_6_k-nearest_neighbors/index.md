---
layout: default
title: "index"
---

[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/index.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/index.html)


# _4.7.6 K-Nearest Neighbors_ 

We will now perform KNN using the `KNeighborsClassifier()` function. This function works similarly to the other model-fitting functions that we have encountered thus far. 

As is the case for LDA and QDA, we fit the classifier using the `fit` method. New predictions are formed using the `predict` method of the object returned by `fit()`. 

```python
In [47]: knn1 = KNeighborsClassifier(n_neighbors=1)
knn1.fit(X_train, L_train)
knn1_pred = knn1.predict(X_test)
confusion_table(knn1_pred, L_test)
```

```python
Out[47]: Truth      Down   Up
Predicted            
Down         43   58
Up           68   83
```

The results using $K=1$ are not very good, since only 50% of the observations are correctly predicted. Of course, it may be that $K=1$ results in an overly-flexible fit to the data. 

```python
In [48]: (83+43)/252, np.mean(knn1_pred == L_test)
```

```python
Out[48]: (0.5, 0.5)
```

We repeat the analysis below using $K=3$. 

```python
In [49]: knn3 = KNeighborsClassifier(n_neighbors=3)
knn3_pred = knn3.fit(X_train, L_train).predict(X_test)
np.mean(knn3_pred == L_test)
```

```python
Out[49]: 0.5317460317460317
```

The results have improved slightly. But increasing $K$ further provides no further improvements. It appears that for these data, and this train/test split, QDA gives the best results of the methods that we have examined so far. 

KNN does not perform well on the `Smarket` data, but it often does provide impressive results. As an example we will apply the KNN approach to the `Caravan` data set, which is part of the `ISLP` library. This data set includes 85 predictors that measure demographic characteristics for 5,822 individuals. The response variable is `Purchase`, which indicates whether or not a given individual purchases a caravan insurance policy. In this data set, only 6% of people purchased caravan insurance. 

```python
In [50]: Caravan = load_data('Caravan')
Purchase = Caravan.Purchase
Purchase.value_counts()
```

```python
Out[50]: No     5474
         Yes     348
         Name: Purchase, dtype: int64
```

```python
In [51]: 348 / 5822
```

```python
Out[51]: 0.05977327378907592
```

Our features will include all columns except `Purchase`. 

```python
In [52]: feature_df = Caravan.drop(columns=['Purchase'])
```

Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. 

A good way to handle this problem is to _standardize_ the data so that all variables are given a mean of zero and a standard deviation of one. Then all variables will be on a comparable scale. This is accomplished using the `StandardScaler()` transformation. 

```python
In [53]: scaler = StandardScaler(with_mean=True,
                                 with_std=True,
                                 copy=True)
scaler.fit(feature_df)
X_std = scaler.transform(feature_df)
```

Now every column of `feature_std` below has a standard deviation of one and a mean of zero. 

```python
In [56]: (X_train, X_test, y_train, y_test) = train_test_split(X_std, Purchase, test_size=1000, random_state=0)
```

We fit a KNN model on the training data using $K=1$, and evaluate its performance on the test data. 

```python
In [57]: knn1 = KNeighborsClassifier(n_neighbors=1)
knn1_pred = knn1.fit(X_train, y_train).predict(X_test)
np.mean(y_test != knn1_pred), np.mean(y_test != "No")
```

```python
Out[57]: (0.111, 0.067)
```

It turns out that KNN with $K=1$ does far better than random guessing among the customers that are predicted to buy insurance. Among 62 such customers, 9, or 14.5%, actually do purchase insurance. This is double the rate that one would obtain from random guessing. 

```python
In [59]: 9 / (53 + 9)
```

```python
Out[59]: 0.14516129032258066
```

---

## Sub-Chapters


[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/index.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/index.html)

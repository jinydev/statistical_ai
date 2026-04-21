---
layout: default
title: "index"
---

[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

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

Likewise we can use the `pvalues` attribute to access the _p_-values for the coefficients (not shown). 

```python
In [9]: results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors. This method returns predictions on the probability scale. If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model. Here we have printed only the first ten probabilities.

```python
In [10]: probs = results.predict()
probs[:10]
```

```python
Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812,
                0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down`. The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5. 

```python
In [11]: labels = np.array(['Down']*1250)
labels[probs > 0.5] = "Up"
```

The `confusion_table()` function from the `ISLP` package summarizes these predictions, showing how many observations were correctly or incorrectly classified. The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels.

```python
In [12]: confusion_table(labels, Smarket.Direction)
```

|**`Out[12]:`**|`Truth`|`Down`|`Up`|
|---|---|---|---|
||`Predicted`|||
||`Down`|`145`|`141`|
||`Up`|`457`|`507`|

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions. Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions. The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct. In this case, logistic regression correctly predicted the movement of the market 52.2% of the time. 

```python
In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)
```

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing. However, this result is misleading because we trained and tested the model on the same set of 1,250 observations. In other words, 100 − 52.2 = 47.8% is the _training_ error rate. As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate. In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data. 

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004. We then use this vector to create a held out data set of observations from 2005.

```python
In [14]: train = (Smarket.Year < 2005)
Smarket_train = Smarket.loc[train]
Smarket_test = Smarket.loc[~train]
Smarket_test.shape
```

# **`Out[14]:`** `(252, 9)` 

The object `train` is a boolean array, since its elements are `True` and `False`. Therefore, `Smarket.loc[~train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False`. The output above indicates that there are 252 such observations. 

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005. We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005. 

```python
In [15]: X_train, X_test = X.loc[train], X.loc[~train]
y_train, y_test = y.loc[train], y.loc[~train]
glm_train = sm.GLM(y_train,
                   X_train,
                   family=sm.families.Binomial())
results = glm_train.fit()
probs = results.predict(exog=X_test)
```

Notice that we have trained and tested our model on two completely separate data sets: training was performed using only the dates before 2005, and testing was performed using only the dates in 2005.

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period. We will first store the test and training labels (recall `y_test` is binary).

```python
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train]
```

Now we threshold the fitted probability at 50% to form our predicted labels.

```python
In [17]: labels = np.array(['Down']*252)
labels[probs > 0.5] = 'Up'
confusion_table(labels, L_test)
```

```python
Out[17]: Truth      Down  Up
Predicted
Down         77    97
Up           34    44
```

The test accuracy is about 48% while the error rate is about 52%.

```python
In [18]: np.mean(labels == L_test), np.mean(labels != L_test)
```

```python
Out[18]: (0.4802, 0.5198)
```

The `!=` notation means _not equal to_, and so the last command computes the test set error rate. The results are rather disappointing: the test error rate is 52%, which is worse than random guessing! Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days’ returns to predict future market performance. (After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)

We recall that the logistic regression model had very underwhelming _p_-values associated with all of the predictors. Using predictors that have no relationship with the response tends to cause a deterioration in the test error rate, and so removing such predictors may in turn yield an improvement. Below we refit the logistic regression using just `Lag1` and `Lag2`, which seemed to have the highest predictive power in the original model.

```python
In [19]: model = MS(['Lag1', 'Lag2']).fit(Smarket)
X = model.transform(Smarket)
X_train, X_test = X.loc[train], X.loc[~train]
glm_train = sm.GLM(y_train,
                   X_train,
                   family=sm.families.Binomial())
results = glm_train.fit()
probs = results.predict(exog=X_test)
labels = np.array(['Down']*252)
labels[probs > 0.5] = 'Up'
confusion_table(labels, L_test)
```

```python
Out[19]: Truth      Down  Up
Predicted
Down         35    35
Up           76   106
```

Let’s evaluate the overall accuracy as well as the accuracy within the days when logistic regression predicts an increase.

```python
In [20]: (35+106)/252, 106/(106+76)
```

```python
Out[20]: (0.5595, 0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted. Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach. However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate. This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted.

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2`. We want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8. We do this using the `predict()` function.

```python
In [21]: newdata = pd.DataFrame({'Lag1':[1.2, 1.5],
'Lag2':[1.1, -0.8]});
newX = model.transform(newdata)
results.predict(newX)
```

```python
Out[21]:
0    0.4791
1    0.4961
dtype: float64
```

---

## Sub-Chapters


[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/index.html)

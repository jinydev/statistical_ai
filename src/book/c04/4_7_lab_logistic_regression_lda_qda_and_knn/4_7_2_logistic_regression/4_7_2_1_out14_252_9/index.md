---
layout: default
title: "index"
---

# **`Out[14]:`** `(252, 9)` 

The object `train` is a vector of 1,250 elements, corresponding to the observations in our data set. The elements of the vector that correspond to observations that occurred before 2005 are set to `True` , whereas those that correspond to observations in 2005 are set to `False` . Hence `train` is a _boolean_ array, since its elements are `True` and `False` . Boolean arrays can be used to obtain a subset of the rows or columns of a data frame using the 

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 177 

`loc` method. For instance, the command `Smarket.loc[train]` would pick out a submatrix of the stock market data set, corresponding only to the dates before 2005, since those are the ones for which the elements of `train` are `True` . The _∼_ symbol can be used to negate all of the elements of a Boolean vector. That is, _∼_ `train` is a vector similar to `train` , except that the elements that are `True` in `train` get swapped to `False` in _∼_ `train` , and vice versa. Therefore, `Smarket.loc[` _∼_ `train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False` . The output above indicates that there are 252 such observations. 

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005. We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005. 

**`In [15]:`** `X_train, X_test = X.loc[train], X.loc[` _∼_ `train] y_train, y_test = y.loc[train], y.loc[` _∼_ `train] glm_train = sm.GLM(y_train, X_train, family=sm.families.Binomial()) results = glm_train.fit() probs = results.predict(exog=X_test)` 

Notice that we have trained and tested our model on two completely separate data sets: training was performed using only the dates before 2005, and testing was performed using only the dates in 2005. 

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period. We will first store the test and training labels (recall `y_test` is binary). 

```
In [16]:D=Smarket.Direction
```

`L_train, L_test = D.loc[train], D.loc[` _∼_ `train]` 

Now we threshold the fitted probability at 50% to form our predicted labels. 

```
In [17]:labels=np.array(['Down']*252)
labels[probs >0.5]='Up'
confusion_table(labels,L_test)
```

```
Out[17]:TruthDownUp
Predicted
Down7797
Up3444
```

The test accuracy is about 48% while the error rate is about 52% 

```
In [18]:np.mean(labels==L_test),np.mean(labels!=L_test)
```

```
Out[18]:(0.4802,0.5198)
```

The `!=` notation means _not equal to_ , and so the last command computes `!=` the test set error rate. The results are rather disappointing: the test error rate is 52%, which is worse than random guessing! Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days’ returns to predict future market performance. (After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.) 

178 4. Classification 

We recall that the logistic regression model had very underwhelming _p_ - values associated with all of the predictors, and that the smallest _p_ -value, though not very small, corresponded to `Lag1` . Perhaps by removing the variables that appear not to be helpful in predicting `Direction` , we can obtain a more effective model. After all, using predictors that have no relationship with the response tends to cause a deterioration in the test error rate (since such predictors cause an increase in variance without a corresponding decrease in bias), and so removing such predictors may in turn yield an improvement. Below we refit the logistic regression using just `Lag1` and `Lag2` , which seemed to have the highest predictive power in the original logistic regression model. 

**`In [19]:`** `model = MS(['Lag1', 'Lag2']).fit(Smarket) X = model.transform(Smarket) X_train, X_test = X.loc[train], X.loc[` _∼_ `train] glm_train = sm.GLM(y_train, X_train, family=sm.families.Binomial()) results = glm_train.fit() probs = results.predict(exog=X_test) labels = np.array(['Down']*252) labels[probs >0.5] = 'Up' confusion_table(labels, L_test)` 

```
Out[19]:TruthDownUp
Predicted
Down3535
Up76106
```

Let’s evaluate the overall accuracy as well as the accuracy within the days when logistic regression predicts an increase. 

```
In [20]:(35+106)/252,106/(106+76)
```

```
Out[20]:(0.5595,0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted. It is worth noting that in this case, a much simpler strategy of predicting that the market will increase every day will also be correct 56% of the time! Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach. However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate. This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted. Of course one would need to investigate more carefully whether this small improvement was real or just due to random chance. 

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2` . In particular, we want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1 _._ 2 and 1 _._ 1, respectively, and on a day when they equal 1 _._ 5 and _−_ 0 _._ 8. We do this using the `predict()` function. 

```
In [21]:newdata=pd.DataFrame({'Lag1':[1.2,1.5],
'Lag2':[1.1,-0.8]});
```

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 

179 

```
newX=model.transform(newdata)
results.predict(newX)
```

```
Out[21]:
```

```
00.4791
10.4961
dtype:float64
```

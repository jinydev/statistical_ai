---
layout: default
title: "index"
---

# _4.7.3 Linear Discriminant Analysis_ 

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()` , which we have abbreviated `LDA()` . We fit `Linear` the model using only the observations before 2005. 

```
Discriminant
Analysis()
```

```
In [22]:lda=LDA(store_covariance=True)
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test` . We can also directly use the labels rather than the Boolean vectors `y_train` . 

```
In [23]:X_train,X_test=[M.drop(columns=['intercept'])
forMin[X_train,X_test]]
lda.fit(X_train,L_train)
```

```
Out[23]:LinearDiscriminantAnalysis(store_covariance=True)
```

Here we have used the list comprehensions introduced in Section 3.6.4. Looking at our first line above, we see that the right-hand side is a list of length two. This is because the code `for M in [X_train, X_test]` iterates over a list of length two. While here we loop over a list, the list comprehension method works when looping over any iterable object. We then apply the `drop()` method to each element in the iteration, collecting the result `.drop()` in a list. The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test` . Of course, this overwrites the previous values of `X_train` and `X_test` . 

Having fit the model, we can extract the means in the two classes with the `means_` attribute. These are the average of each predictor within each class, and are used by LDA as estimates of _µk_ . These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines. 

```
In [24]:lda.means_
```

```
Out[24]:array([[0.04,0.03],
[-0.04,-0.03]])
```

The estimated prior probabilities are stored in the `priors_` attribute. The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method. We can be sure of which entry corresponds to which label by looking at the `classes_` attribute. 

```
In [25]:lda.classes_
```

```
Out[25]:array(['Down','Up'],dtype='<U4')
```

180 4. Classification 

The LDA output indicates that _π_ ˆDown = 0 _._ 492 and _π_ ˆUp = 0 _._ 508. 

```
In [26]:lda.priors_
```

```
Out[26]:array([0.492,0.508])
```

The linear discriminant vectors can be found in the `scalings_` attribute: 

```
In [27]:lda.scalings_
```

```
Out[27]:array([[-0.642],
```

```
[-0.513]])
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule. In other words, these are the multipliers of the elements of $X$= _x_ in (4.24). If _−_ 0 _._ 64 _×_ Lag1 _−_ 0 _._ 51 _×_ Lag2 is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline. 

```
In [28]:lda_pred=lda.predict(X_test)
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical. 

```
In [29]:confusion_table(lda_pred,L_test)
```

**`Out[29]:`** `Truth Down Up Predicted Down 35 35 Up 76 106` We can also estimate the probability of each class for each training set. Applying a 50% threshold to the posterior probabilities ing in class one allows us to recreate the predictions contained in **`In [30]:`** `lda_prob = lda.predict_proba(X_test) np.all( np.where(lda_prob[:,1] >= 0.5, 'Up','Down') == lda_pred )` 

We can also estimate the probability of each class for each point in a training set. Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in `lda_pred` . 

```
Out[30]:True
```

Above, we used the `np.where()` function that creates an array with value `np.where() 'Up'` for indices where the second column of `lda_prob` (the estimated posterior probability of `'Up'` ) is greater than 0.5. For problems with more than two classes the labels are chosen as the class whose posterior probability is highest: 

```
In [31]:np.all(
[lda.classes_[i]foriinnp.argmax(lda_prob,1)]==
lda_pred
)
```

---

## Sub-Chapters (하위 목차)

### 사전 확률 점검 (Jupyter Notebook Output)
* [문서로 이동하기](./4_7_3_1_out31_true/)

LDA 실행 후 도출된 집단 사전 확률 및 로직이 타당한지 간단한 불 값(True/False) 출력 테스트를 점검합니다.

---
layout: default
title: "index"
---

# _8.3.3 Bagging and Random Forests_ 

Here we apply bagging and random forests to the `Boston` data, using the `RandomForestRegressor()` from the `sklearn.ensemble` package. Recall that `RandomForest` bagging is simply a special case of a random forest with _m_ = _p_ . Therefore, `Regressor()` the `RandomForestRegressor()` function can be used to perform both bagging `sklearn.` and random forests. We start with bagging. `ensemble` 

```
In [24]:bag_boston=RF(max_features=X_train.shape[1],random_state=0)
bag_boston.fit(X_train,y_train)
```

```
Out[24]:RandomForestRegressor(max_features=12,random_state=0)
```

The argument `max_features` indicates that all 12 predictors should be considered for each split of the tree — in other words, that bagging should be done. How well does this bagged model perform on the test set? 

```
In [25]:ax=subplots(figsize=(8,8))[1]
y_hat_bag=bag_boston.predict(X_test)
ax.scatter(y_hat_bag,y_test)
np.mean((y_test-y_hat_bag)**2)
```

```
Out[25]:14.63
```

The test set $\text{MSE}$ associated with the bagged regression tree is 14.63, about half that obtained using an optimally-pruned single tree. We could change the number of trees grown from the default of 100 by using the `n_estimators` argument: 

```
In [26]:bag_boston=RF(max_features=X_train.shape[1],
n_estimators=500,
random_state=0).fit(X_train,y_train)
y_hat_bag=bag_boston.predict(X_test)
np.mean((y_test-y_hat_bag)**2)
```

```
Out[26]:14.61
```

There is not much change. Bagging and random forests cannot overfit by increasing the number of trees, but can underfit if the number is too small. Growing a random forest proceeds in exactly the same way, except that we use a smaller value of the `max_features` argument. By default, `RandomForestRegressor()` uses _p_ variables when building a random forest of regression trees (i.e. it defaults to bagging), and `RandomForestClassifier()` uses _[√] p_ variables when building a random forest of classification trees. Here we use `max_features=6` . 

```
In [27]:RF_boston=RF(max_features=6,
random_state=0).fit(X_train,y_train)
y_hat_RF=RF_boston.predict(X_test)
np.mean((y_test-y_hat_RF)**2)
```

---

## Sub-Chapters (하위 목차)

### Jupyter Notebook Output (앙상블 모형 편차 스코어 결과)
* [문서로 이동하기](./8_3_3_1_out27_20.04/)

포레스트 트리 군락이 형성한 평균 오차율이 단일 트리를 얼마나 압도적으로 넘어서는지 로그로 확인힙니다.

---
layout: default
title: "index"
---

# _8.3.4 Boosting_ 

Here we use `GradientBoostingRegressor()` from `sklearn.ensemble` to fit `Gradient` boosted regression trees to the `Boston` data set. For classification we would `Boosting` use `GradientBoostingClassifier()` . The argument `n_estimators=5000` indicates that we want 5000 trees, and the option `max_depth=3` limits the depth `Gradient` of each tree. The argument `learning_rate` is the _λ_ mentioned earlier in the `Boosting` description of boosting. 

```
Boosting
Regressor()
Gradient
Boosting
Classifier()
```

```
In [29]:boost_boston=GBR(n_estimators=5000,
learning_rate=0.001,
max_depth=3,
random_state=0)
boost_boston.fit(X_train,y_train)
```

We can see how the training error decreases with the `train_score_` attribute. To get an idea of how the test error decreases we can use the `staged_predict()` method to get the predicted values along the path. 

```
In [30]:test_error=np.zeros_like(boost_boston.train_score_)
foridx,y_inenumerate(boost_boston.staged_predict(X_test)):
test_error[idx]=np.mean((y_test-y_)**2)
plot_idx=np.arange(boost_boston.train_score_.shape[0])
ax=subplots(figsize=(8,8))[1]
ax.plot(plot_idx,
boost_boston.train_score_ ,
'b',
label='Training')
```

362 8. Tree-Based Methods 

```
ax.plot(plot_idx,
test_error,
'r',
label='Test')
ax.legend();
```

We now use the boosted model to predict `medv` on the test set: 

```
In [31]:y_hat_boost=boost_boston.predict(X_test);
np.mean((y_test-y_hat_boost)**2)
```

```
Out[31]:14.48
```

The test $\text{MSE}$ obtained is 14.48, similar to the test $\text{MSE}$ for bagging. If we want to, we can perform boosting with a different value of the shrinkage parameter _λ_ in (8.10). The default value is 0.001, but this is easily modified. Here we take _λ_ = 0 _._ 2. 

```
In [32]:boost_boston=GBR(n_estimators=5000,
learning_rate=0.2,
max_depth=3,
random_state=0)
boost_boston.fit(X_train,
y_train)
y_hat_boost=boost_boston.predict(X_test);
np.mean((y_test-y_hat_boost)**2)
```

---

## Sub-Chapters (하위 목차)

### Jupyter Notebook Output (부스팅 반환 점검)
* [문서로 이동하기](./8_3_4_1_out32_14.50/)

느린 속도로 학습률을 올린 부스팅 모델의 단단한 테스트 예측력을 수치 스코어로 파악합니다.

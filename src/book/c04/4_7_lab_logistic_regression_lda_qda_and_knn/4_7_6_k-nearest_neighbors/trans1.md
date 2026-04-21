---
layout: default
title: "trans1"
---

[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/trans1.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.6 K-Nearest Neighbors
# 4.7.6 K-최근접 이웃 (KNN)

We will now perform KNN using the `KNeighborsClassifier()` function. This function works similarly to the other model-fitting functions that we have encountered thus far. 
우리는 이제 `KNeighborsClassifier()` 함수를 사용하여 KNN을 수행할 것입니다. 이 함수는 지금까지 우리가 만났던 다른 모델 피팅(model-fitting) 함수들과 유사하게 작동합니다.

As is the case for LDA and QDA, we fit the classifier using the `fit` method. New predictions are formed using the `predict` method of the object returned by `fit()`. 
LDA 및 QDA의 경우와 마찬가지로, 우리는 `fit` 메서드를 사용하여 분류기를 피팅합니다. 새로운 예측은 `fit()` 에 의해 반환된 객체의 `predict` 메서드를 사용하여 형성됩니다.

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
관측치의 50% 만 정확하게 예측되었기 때문에 $K=1$ 을 사용한 결과는 별로 좋지 않습니다. 물론 $K=1$ 이 데이터에 대해 지나치게 유연한(overly-flexible) 피팅을 초래했을 수도 있습니다.

```python
In [48]: (83+43)/252, np.mean(knn1_pred == L_test)
```

```python
Out[48]: (0.5, 0.5)
```

We repeat the analysis below using $K=3$. 
아래에서 $K=3$ 을 사용하여 분석을 반복합니다.

```python
In [49]: knn3 = KNeighborsClassifier(n_neighbors=3)
knn3_pred = knn3.fit(X_train, L_train).predict(X_test)
np.mean(knn3_pred == L_test)
```

```python
Out[49]: 0.5317460317460317
```

The results have improved slightly. But increasing $K$ further provides no further improvements. It appears that for these data, and this train/test split, QDA gives the best results of the methods that we have examined so far. 
결과가 약간 개선되었습니다. 그러나 $K$ 를 더 극대화해도 추가적인 개선이 제공되지는 않습니다. 이 데이터와 이 훈련/테스트 분할(train/test split) 에서는 QDA가 지금까지 검토한 방법 중에서 가장 좋은 결과를 제공하는 것으로 보입니다.

KNN does not perform well on the `Smarket` data, but it often does provide impressive results. As an example we will apply the KNN approach to the `Caravan` data set, which is part of the `ISLP` library. This data set includes 85 predictors that measure demographic characteristics for 5,822 individuals. The response variable is `Purchase`, which indicates whether or not a given individual purchases a caravan insurance policy. In this data set, only 6% of people purchased caravan insurance. 
KNN은 `Smarket` 데이터에서는 잘 작동하지 않지만, 종종 인상적인 결과를 제공합니다. 한 예로 우리는 그 모델을 `ISLP` 라이브러리의 일부인 `Caravan` 데이터 세트에 KNN 접근 방식을 적용할 것입니다. 이 데이터 세트에는 5,822명의 개인에 대한 인구통계학적 특성을 측정하는 85개의 예측 변수가 포함되어 있습니다. 반응 변수(response variable)는 `Purchase` 이며, 이는 주어진 개인이 캐러밴 보험 정책을 구매하는지 여부를 나타냅니다. 이 데이터 세트에서는 오직 6%의 사람들만이 캐러밴 보험을 구매했습니다.

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
우리의 특성(features)에는 `Purchase` 를 제외한 모든 열이 포함됩니다.

```python
In [52]: feature_df = Caravan.drop(columns=['Purchase'])
```

Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. 
KNN 분류기는 주어진 테스트 관측치에 가장 가까운 관측치들을 식별함으로써 클래스를 예측하기 때문에, 변수들의 척도(scale)가 중요합니다.

A good way to handle this problem is to _standardize_ the data so that all variables are given a mean of zero and a standard deviation of one. Then all variables will be on a comparable scale. This is accomplished using the `StandardScaler()` transformation. 
이 문제를 처리하는 좋은 방법은 모든 변수에 대해 평균이 0이고 표준 편차가 1이 되도록 데이터를 _표준화(standardize)_ 하는 것입니다. 그러면 모든 변수가 비교 가능한 척도를 갖게 됩니다. 이것은 `StandardScaler()` 변환을 사용하여 수행됩니다.

```python
In [53]: scaler = StandardScaler(with_mean=True,
                                 with_std=True,
                                 copy=True)
scaler.fit(feature_df)
X_std = scaler.transform(feature_df)
```

Now every column of `feature_std` below has a standard deviation of one and a mean of zero. 
이제 아래의 `feature_std` 의 모든 열은 변형되어 표준 편차가 1이고 평균이 0이 됩니다.

```python
In [56]: (X_train, X_test, y_train, y_test) = train_test_split(X_std, Purchase, test_size=1000, random_state=0)
```

We fit a KNN model on the training data using $K=1$, and evaluate its performance on the test data. 
우리는 $K=1$ 을 사용하여 훈련 데이터에 KNN 모델을 피팅하고 예측된 결과에 대해 테스트 데이터에서의 성능을 평가합니다.

```python
In [57]: knn1 = KNeighborsClassifier(n_neighbors=1)
knn1_pred = knn1.fit(X_train, y_train).predict(X_test)
np.mean(y_test != knn1_pred), np.mean(y_test != "No")
```

```python
Out[57]: (0.111, 0.067)
```

It turns out that KNN with $K=1$ does far better than random guessing among the customers that are predicted to buy insurance. Among 62 such customers, 9, or 14.5%, actually do purchase insurance. This is double the rate that one would obtain from random guessing. 
보험을 구매할 것으로 예측된 고객들 사이에서 $K=1$ 인 KNN은 무작위 예측보다 훨씬 더 나은 성과를 내는 것으로 밝혀졌습니다. 그러한 62명의 고객 중 9명, 즉 14.5% 가 실제로 보험을 구매합니다. 이것은 무작위 예측(random guessing)으로부터 얻을 수 있는 비율의 두 배입니다.

```python
In [59]: 9 / (53 + 9)
```

```python
Out[59]: 0.14516129032258066
```

---

## Sub-Chapters

[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/trans1.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/trans1.html)

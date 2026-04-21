---
layout: default
title: "trans1"
---

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans1.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.3 Linear Discriminant Analysis
# 4.7.3 선형 판별 분석

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()`, which we have abbreviated `LDA()`. We fit the model using only the observations before 2005.
우리는 축약하여 `LDA()` 로 명명한 `LinearDiscriminantAnalysis()` 함수를 사용하여 `Smarket` 데이터에 대한 LDA를 수행하는 것으로 시작합니다. 우리는 2005년 이전의 관측치만을 사용하여 모델을 피팅합니다.

```python
In [22]: lda = LDA(store_covariance=True)
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test`. We can also directly use the labels rather than the Boolean vectors `y_train`. 
`LDA` 추정기(estimator)는 자동으로 절편(intercept)을 추가하므로, 우리는 `X_train` 및 `X_test` 모두에서 절편에 해당하는 열을 제거해야 합니다. 또한 부울 벡터 `y_train` 대신 레이블을 직접 사용할 수도 있습니다.

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept']) for M in [X_train, X_test]]
lda.fit(X_train, L_train)
```

```python
Out[23]: LinearDiscriminantAnalysis(store_covariance=True)
```

Here we have used the list comprehensions introduced in Section 3.6.4. Looking at our first line above, we see that the right-hand side is a list of length two. This is because the code `for M in [X_train, X_test]` iterates over a list of length two. While here we loop over a list, the list comprehension method works when looping over any iterable object. We then apply the `drop()` method to each element in the iteration, collecting the result in a list. The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test`. Of course, this overwrites the previous values of `X_train` and `X_test`. 
여기서 우리는 Section 3.6.4 에 도입된 리스트 컴프리헨션(list comprehensions)을 사용했습니다. 위의 첫 번째 줄을 보면, 우변이 길이 2의 리스트임을 알 수 있습니다. 이는 `for M in [X_train, X_test]` 코드가 길이가 2인 리스트에 대해 반복하기 때문입니다. 여기서는 리스트에 대해 루프(loop)를 돌리지만, 리스트 컴프리헨션 방법은 반복 가능한(iterable) 객체에 대해 루프를 돌릴 때 작동합니다. 그런 다음 반복(iteration) 내의 각 요소에 `drop()` 메서드를 적용하여 그 결과를 리스트에 수집합니다. 좌변은 이 길이 2의 리스트를 언패킹(unpack)하여 요소들을 `X_train` 과 `X_test` 변수에 할당하라고 `Python` 에게 지시합니다. 물론, 이것은 `X_train` 과 `X_test` 의 이전 값을 덮어씁니다.

Having fit the model, we can extract the means in the two classes with the `means_` attribute. These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_k$. These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines. 
모델을 피팅한 후 우리는 `means_` 속성을 사용하여 두 클래스의 평균을 추출할 수 있습니다. 이것들은 각 클래스 내 각 예측 변수의 평균이며, LDA에 의해 $\mu_k$ 에 대한 추정치로 사용됩니다. 이것들은 시장이 상승하는 날에는 이전 2일간의 수익률이 음수인 경향이 있고, 시장이 하락하는 날에는 이전 날들의 수익률이 양수인 경향이 있음을 시사합니다.

```python
In [24]: lda.means_
```

```python
Out[24]: array([[ 0.0426,  0.0338],
                [-0.0395, -0.0313]])
```

The estimated prior probabilities are stored in the `priors_` attribute. The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method. We can be sure of which entry corresponds to which label by looking at the `classes_` attribute. 
추정된 사전 확률(prior probabilities)은 `priors_` 속성에 저장됩니다. `sklearn` 패키지는 일반적으로 `fit()` 메서드를 사용할 때 추정된 수량을 나타내기 위해 후행(trailing) `_` 를 사용합니다. 우리는 `classes_` 속성을 봄으로써 어느 항목이 어떤 레이블에 해당하는지 확신할 수 있습니다.

```python
In [25]: lda.classes_
```

```python
Out[25]: array(['Down', 'Up'], dtype='<U4')
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$. 
LDA 출력은 $\hat{\pi}_{Down} = 0.492$ 및 $\hat{\pi}_{Up} = 0.508$ 임을 나타냅니다.

```python
In [26]: lda.priors_
```

```python
Out[26]: array([0.49198397, 0.50801603])
```

The linear discriminant vectors can be found in the `scalings_` attribute: 
선형 판별 벡터(linear discriminant vectors)는 `scalings_` 속성에서 찾을 수 있습니다:

```python
In [27]: lda.scalings_
```

```python
Out[27]: array([[-0.64201906],
                [-0.51352928]])
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule. In other words, these are the multipliers of the elements of $X = x$ in (4.24). If $-0.642 \times Lag1 - 0.513 \times Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline. 
이러한 값들은 LDA 결정 규칙(decision rule)을 형성하는 데 사용되는 `Lag1` 과 `Lag2` 의 선형 결합을 제공합니다. 즉, 이것들은 (4.24)에서 $X = x$ 요소들의 승수(multipliers)입니다. 만약 $-0.642 \times Lag1 - 0.513 \times Lag2$ 가 크면 LDA 분류기는 시장 상승을 예측할 것이고, 만약 작으면 LDA 분류기는 시장 하락을 예측할 것입니다.

```python
In [28]: lda_pred = lda.predict(X_test)
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical. 
분류 방법의 비교(Section 4.5)에서 관찰했듯이, LDA와 로지스틱 회귀 예측은 거의 동일(identical)합니다.

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
우리는 훈련 세트의 각 점에 대해 각 클래스의 확률을 추정할 수도 있습니다. 클래스 1에 속할 사후 확률(posterior probabilities)에 50% 임계값(threshold)을 적용하면 `lda_pred` 에 포함된 예측을 재현할 수 있습니다.

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
위에서 우리는 `lda_prob` 의 두 번째 열(`'Up'` 의 추정된 사후 확률)이 0.5보다 큰 인덱스에 대해 값 `'Up'` 을 가진 배열을 생성하는 `np.where()` 함수를 사용했습니다. 클래스가 두 개 이상인 문제의 경우 사후 확률이 가장 높은 클래스로 레이블이 선택됩니다:

```python
In [31]: np.all(
    [lda.classes_[i] for i in np.argmax(lda_prob, 1)] == lda_pred
)
```

---

## Sub-Chapters

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans1.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans1.html)

---
layout: default
title: "trans1"
---

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/trans1.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.5 Naive Bayes
# 4.7.5 나이브 베이즈

Next, we fit a naive Bayes model to the `Smarket` data. The syntax is similar to that of `LDA()` and `QDA()`. By default, this implementation of the naive Bayes classifier models each quantitative feature using a Gaussian distribution. However, a kernel density method can also be used to estimate the distributions. 
다음으로, 우리는 `Smarket` 데이터에 나이브 베이즈(naive Bayes) 모델을 피팅합니다. 구문은 `LDA()` 및 `QDA()` 의 구문과 유사합니다. 기본적으로, 나이브 베이즈 분류기의 이 구현은 가우시안 분포(Gaussian distribution)를 사용하여 각 정량적 특성(quantitative feature)을 모델링합니다. 그러나 분포를 추정하기 위해 커널 밀도(kernel density) 방법이 사용될 수도 있습니다.

```python
In [38]: NB = GaussianNB()
NB.fit(X_train, L_train)
```

```python
Out[38]: GaussianNB()
```

The classes are stored as `classes_`. 
클래스들은 `classes_` 에 저장됩니다.

```python
In [39]: NB.classes_
```

```python
Out[39]: array(['Down', 'Up'], dtype='<U4')
```

The class prior probabilities are stored in the `class_prior_` attribute. 
클래스 사전 확률(class prior probabilities)은 `class_prior_` 속성에 저장됩니다.

```python
In [40]: NB.class_prior_
```

```python
Out[40]: array([0.49198397, 0.50801603])
```

The parameters of the features can be found in the `theta_` and `var_` attributes. The number of rows is equal to the number of classes, while the number of columns is equal to the number of features. We see below that the mean for feature `Lag1` in the `Down` class is $0.043$. 
특성의 매개변수는 `theta_` 및 `var_` 속성에서 찾을 수 있습니다. 행의 수는 클래스의 수와 같고, 열의 수는 특성의 수와 같습니다. 우리는 아래에서 `Down` 클래스에 있는 `Lag1` 특성의 평균이 $0.043$ 임을 알 수 있습니다.

```python
In [41]: NB.theta_
```

```python
Out[41]: array([[ 0.04279022,  0.03389409],
                [-0.03954635, -0.03132544]])
```

Its variance is $1.503$. 
그 분산(variance)은 $1.503$ 입니다.

```python
In [42]: NB.var_
```

```python
Out[42]: array([[1.50355424, 1.53246652],
                [1.51397116, 1.4870335 ]])
```

How do we know the names of these attributes? We use `NB?` (or `?NB`). We can easily verify the mean computation: 
우리가 이러한 속성들의 이름을 어떻게 알 수 있을까요? 우리는 `NB?` (또는 `?NB`)를 사용합니다. 우리는 평균 계산을 쉽게 검증(verify)할 수 있습니다:

```python
In [43]: X_train[L_train == 'Down'].mean()
```

```python
Out[43]: Lag1    0.042790
         Lag2    0.033894
         dtype: float64
```

Similarly for the variance: 
분산에 대해서도 유사합니다:

```python
In [44]: X_train[L_train == 'Down'].var(ddof=0)
```

```python
Out[44]: Lag1    1.503554
         Lag2    1.532467
         dtype: float64
```

The `GaussianNB()` function calculates variances using the $1/n$ formula. Since `NB()` is a classifier in the `sklearn` library, making predictions uses the same syntax as for `LDA()` and `QDA()` above. 
`GaussianNB()` 함수는 $1/n$ 공식을 사용하여 분산을 계산합니다. `NB()` 는 `sklearn` 라이브러리의 분류기이므로, 예측을 수행하는 것은 위의 `LDA()` 및 `QDA()` 에 대한 것과 동일한 구문을 사용합니다.

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
나이브 베이즈는 59% 이상의 정답률(accurate predictions)로 이 데이터에서 잘 수행됩니다. 이는 QDA보다는 약간 나쁘지만, LDA보다는 훨씬 좋습니다.

As for `LDA`, the `predict_proba()` method estimates the probability that each observation belongs to a particular class. 
`LDA` 와 마찬가지로 `predict_proba()` 메서드는 각 관측치가 특정 클래스에 속할 확률을 추정합니다.

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

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/trans1.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/trans1.html)

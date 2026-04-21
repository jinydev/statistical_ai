---
layout: default
title: "trans1"
---

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans1.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.7 Linear and Poisson Regression on the Bikeshare Data
# 4.7.7 자전거 공유 데이터에 대한 선형 및 푸아송 회귀

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6. The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012. 
여기서 우리는 Section 4.6에서 설명한 바와 같이 `Bikeshare` 데이터에 선형 및 푸아송 회귀 모델을 피팅합니다. 반응 변수 `bikers` 는 2010-2012년 기간 동안 워싱턴 DC의 시간당 자전거 대여 수를 측정합니다.

```python
In [64]: Bike = load_data('Bikeshare')
```

Let’s have a peek at the dimensions and names of the variables in this dataframe. 
이 데이터프레임에 있는 변수들의 차원(dimensions)과 이름을 살짝 엿보겠습니다(peek).

```python
In [65]: Bike.shape, Bike.columns
```

```python
Out[65]: ((8645, 15),
          Index(['season', 'mnth', 'day', 'hr', 'holiday', 'weekday',
                 'workingday', 'weathersit', 'temp', 'atemp', 'hum',
                 'windspeed', 'casual', 'registered', 'bikers'],
                dtype='object'))
```

Linear Regression 
선형 회귀

We begin by fitting a linear regression model to the data. 
우리는 데이터에 선형 회귀 모델을 피팅하는 것으로 시작합니다.

```python
In [66]: X = MS(['mnth',
                 'hr',
                 'workingday',
                 'temp',
                 'weathersit']).fit_transform(Bike)
Y = Bike['bikers']
M_lm = sm.OLS(Y, X).fit()
summarize(M_lm)
```

```python
Out[66]:
```

| | `coef` | `std err` | `t` | `P>|t|` |
|---|---|---|---|---|
| `intercept` | `-68.6317` | `5.307` | `-12.932` | `0.000` |
| `mnth[Feb]` | `6.8452` | `4.287` | `1.597` | `0.110` |
| `mnth[March]` | `16.5514` | `4.301` | `3.848` | `0.000` |
| `mnth[April]` | `41.4249` | `4.972` | `8.331` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

There are 24 levels in `hr` and 40 rows in all, so we have truncated the summary. In `M_lm`, the first levels `hr[0]` and `mnth[Jan]` are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines. For example, the Feb coefficient of $6.845$ signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January. Similarly there are about 16.5 more riders in March than in January. 
`hr` 에는 24개의 수준(levels)이 있고 총 40개의 행이 있으므로 요약을 잘라냈습니다(truncated). `M_lm` 에서 첫 번째 수준인 `hr[0]` 와 `mnth[Jan]` 은 베이스라인 값으로 취급되므로 이들에 대한 계수 추정치는 제공되지 않습니다. 암묵적으로(implicitly), 이들의 계수 추정치는 0이며, 다른 모든 수준들은 이러한 베이스라인에 상대적으로 측정됩니다. 예를 들어, 2월(Feb) 계수 $6.845$ 는 다른 모든 변수를 일정하게 유지할 때 1월보다 2월에 평균적으로 약 7명의 라이더가 더 많다는 것을 의미합니다(signifies). 유사하게 1월보다 3월에 약 16.5명의 라이더가 더 많습니다.

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth`, as follows: 
Section 4.6.1에서 본 결과는 다음과 같이 변수 `hr` 및 `mnth` 의 약간 다른 코딩(coding)을 사용했습니다:

```python
In [67]: hr_encode = contrast('hr', 'sum')
mnth_encode = contrast('mnth', 'sum')
```

Refitting again: 
다시 피팅(Refitting):

```python
In [68]: X2 = MS([mnth_encode,
                  hr_encode,
                  'workingday',
                  'temp',
                  'weathersit']).fit_transform(Bike)
M2_lm = sm.OLS(Y, X2).fit()
S2 = summarize(M2_lm)
S2
```

```python
Out[68]:
```

| | `coef` | `std err` | `t` | `P>|t|` |
|---|---|---|---|---|
| `intercept` | `73.5974` | `5.132` | `14.340` | `0.000` |
| `mnth[Jan]` | `-46.0871` | `4.085` | `-11.281` | `0.000` |
| `mnth[Feb]` | `-39.2419` | `3.539` | `-11.088` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

What is the difference between the two codings? In `M2_lm`, a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth`. Importantly, in `M2_lm`, the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels. Similarly, in `M2_lm`, the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels. This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can 단be interpreted as the difference from the mean level. For example, the coefficient for January of $-46.087$ indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average. 
두 코딩의 차이점은 무엇일까요? `M2_lm` 에서는 `hr` 의 수준 `23` 과 `mnth` 의 수준 `Dec` 를 제외한 모든 수준에 대해 계수 추정치가 보고됩니다. 중요하게도, `M2_lm` 에서 `mnth` 의 마지막 수준에 대한 (보고되지 않은) 계수 추정치는 0이 아닙니다: 대신, 그것은 다른 모든 수준에 대한 계수 추정치 합의 음수와 같습니다. 유사하게, `M2_lm` 에서 `hr` 의 마지막 수준에 대한 계수 추정치는 다른 모든 수준에 대한 계수 추정치 합의 음수입니다. 이는 `M2_lm` 에서 `hr` 과 `mnth` 의 계수들의 합이 항상 0이 됨을 의미하며, 평균 수준으로부터의 차이로 해석될(interpreted) 수 있습니다. 예를 들어, 1월 계수 $-46.087$ 은 다른 모든 변수를 일정하게 유지할 때 연간 평균에 비해 1월의 라이더 수가 일반적으로 46명 더 적음을 나타냅니다.

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used. For example, we see that the predictions from the linear model are the same regardless of coding: 
사용된 코딩에 비추어 모델 출력을 정확하게 해석하기만 한다면, 코딩의 선택은 실제로 중요하지 않다는 것을 깨닫는 것이 중요합니다. 예를 들어, 선형 모델의 예측은 코딩에 관계없이 동일함을 알 수 있습니다:

```python
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2)
```

```python
Out[69]: 5.166710408544458e-09
```

---

## Sub-Chapters

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans1.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans1.html)

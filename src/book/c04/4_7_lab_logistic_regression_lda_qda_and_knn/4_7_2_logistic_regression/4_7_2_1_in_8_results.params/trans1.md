---
layout: default
title: "trans1"
---

[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# **`In [8]:`** `results.params` 

| **`Out[8]:`** | `intercept` | `-0.126000` |
|---|---|---|
| | `Lag1` | `-0.073074` |
| | `Lag2` | `-0.042301` |
| | `Lag3` | `0.011085` |
| | `Lag4` | `0.009359` |
| | `Lag5` | `0.010313` |
| | `Volume` | `0.135441` |
| | `dtype: float64` | |

Likewise we can use the `pvalues` attribute to access the _p_-values for the coefficients (not shown).
이와 마찬가지로 우리는 계수들에 대한 p-값들에 접근하기 위해 `pvalues` 속성을 사용할 수 있습니다 (여기 표시되지는 않음).

```python
In [9]: results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors.
`results` 의 `predict()` 메서드는 예측 변수들의 값들을 주어졌을 때 시장이 상승할 확률을 예측하는 데 사용될 수 있습니다.

This method returns predictions on the probability scale.
이 메서드는 확률 척도(probability scale)에서의 예측들을 반환합니다.

If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model.
만약 분석 데이터 세트가 `predict()` 함수에 전혀 공급되지 않으면, 로지스틱 회귀 모델을 적합시키는 데 사용되었던 원래의 훈련 데이터에 대해서 확률들이 계산됩니다.

Here we have printed only the first ten probabilities.
여기서 우리는 단지 처음 10개의 확률들만을 출력했습니다.

```python
In [10]: probs = results.predict()
probs[:10]
```

```python
Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812,
                0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down`.
특정 날짜에 주식 시장이 상승할지 또는 하락할지에 관한 단일 예측을 내리기 위해, 우리는 이러한 예측된 확률값 숫자들을 `Up` 또는 `Down` 이라는 클래스 레이블 문자로 변환해야만 합니다.

The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5.
다음의 두 명령어들은 시장 상승의 예측된 확률이 산술 조건 0.5보다 큰지 또는 작은지 여부에 기초하여 클래스 분류 예측 레이블의 벡터를 생성해 줍니다.

```python
In [11]: labels = np.array(['Down']*1250)
labels[probs > 0.5] = "Up"
```

The `confusion_table()` function from the `ISLP` package summarizes these predictions, showing how many observations were correctly or incorrectly classified.
`ISLP` 패키지의 `confusion_table()` (혼동 행렬표) 기능은 이러한 라벨 예측들을 깔끔히 요약하며, 얼마나 많은 관측치들이 올바르게 또는 잘못 분류되었는지를 보여줍니다.

The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels.
`confusion_table()` 함수는 첫 번째 인자로 우리가 도출한 예측된 레이블들을, 그리고 두 번째 인자로 실제 정답 데이터인 참의 레이블(true labels)들을 취합니다.

```python
In [12]: confusion_table(labels, Smarket.Direction)
```

| **`Out[12]:`** | `Truth` | `Down` | `Up` |
|---|---|---|---|
| | `Predicted` | | |
| | `Down` | `145` | `141` |
| | `Up` | `457` | `507` |

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions.
혼동 행렬(confusion matrix) 내의 중심 대각선 방향(diagonal)의 요소들은 올바른 예측들을 명확히 나타내며, 반면 비대각선 주변 요소들은 잘못된 예측들을 나타냅니다.

Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions.
따라서 우리의 생성 모델은 시장이 507일 동안 상승하고 145일 동안 하락할 것이라는 기상 현상을 올바르게 예측했으며, 총 507 + 145 = 652개의 올바른 예측들을 얻었습니다.

The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct.
`np.mean()` (평균값 함수) 기능은 도출된 예측이 맞았던 날짜들의 분수 비율(fraction)을 손쉽게 계산하는 데 사용될 수 있습니다.

In this case, logistic regression correctly predicted the movement of the market 52.2% of the time.
이 경우, 로지스틱 회귀는 전체 시간의 52.2% 동안 시장의 움직임 방향을 올바르게 예측했습니다.

```python
In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)
```

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing.
언뜻 보기에(At first glance), 이 도출된 로지스틱 회귀 모델이 단순히 추측(random guessing)하는 것보다는 약간 더 잘 작동하고 있는 것처럼 보입니다.

However, this result is misleading because we trained and tested the model on the same set of 1,250 observations.
그러나 우리는 애초에 1,250개의 다 동일한 단일 세트의 관측치 자료에 대해 똑같이 모델을 훈련시키고(trained) 동시에 그것을 테스트했기(tested) 때문에 이 결과는 매우 오해의 소지가 있습니다(misleading).

In other words, 100 − 52.2 = 47.8% is the _training_ error rate.
다시 말해, 통계 분석 100 − 52.2 = 47.8%는 단지 **훈련(training) 오차율** 일 뿐입니다.

As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate.
우리가 이전에 확인했던 바와 같이, 단일 훈련의 오차율은 데이터 속성상 종종 지나치게 낙관적인(overly optimistic) 경향이 있습니다 — 그것은 대개 테스트 오차율을 심각하게 과소평가(underestimate) 하는 편향을 지닙니다.

In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data.
현재의 이 설정 환경 안에서 도출 모델의 판별 정확도를 더 잘 평가하기 위해, 우리는 모든 데이터의 일부만을 사용하여 훈련 모델을 적합시키고, 그런 다음 그것이 남겨둔(held out) 데이터를 얼마나 잘 예측하는지 검토 실험할 수 있습니다.

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004.
이 전략을 구현 수행하기 위해, 우리는 제일 먼저 2001년부터 2004년 기간에 해당하는 데이터 관측치에 대응하는 부울(Boolean) 논리 벡터를 계산 생성합니다.

We then use this vector to create a held out data set of observations from 2005.
우리는 그다음에 논리 기반 체계 이 벡터를 이용하여 2005년도 해당하는 관측치들의 유지된 '남겨 둔(held out)' 데이터 세트를 선별 분리 생성합니다.

```python
In [14]: train = (Smarket.Year < 2005)
Smarket_train = Smarket.loc[train]
Smarket_test = Smarket.loc[~train]
Smarket_test.shape
```

# **`Out[14]:`** `(252, 9)` 

The object `train` is a boolean array, since its elements are `True` and `False`.
지정된 객체 `train` 은 배열 안의 요소들이 `True` 와 `False` 이기 때문에, 이것은 부울 배열(boolean array) 체계 자료형입니다.

Therefore, `Smarket.loc[~train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False`.
따라서, 연산된 결과물 `Smarket.loc[~train]` 은 논리 분류 기준 `train` 이 `False` 인, 그 관측치들만을 따로 추출해 포함하는 주식 시장 데이터 프레임의 부분 집합(subset) 행들을 산출 생산합니다.

The output above indicates that there are 252 such observations.
위에 표기된 산출 결과 출력물은 이러한 추출 관측치들이 총 252개 존재함을 나타냅니다.

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005.
우리는 이제 2005년 전 날짜에 해당하는 자료 관측치들의 이 부분 집합(subset) 만을 사용하여 로지스틱 회귀 모형을 적합시킵니다.

We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005.
그런 다음 우리는 우리의 검정 세트(test set) — 즉, 2005년의 일자 — 의 각 요일에 대해 주식 시장이 상승할 예측 확률값들을 확보 산출해 얻습니다.

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
주목할 점은 우리가 예측 모델을 완전히 서로 분리된 두 개의 데이터 세트들 상에서 서로 훈련(trained)시키고 테스트(tested)했다는 사실입니다: 훈련은 오직 2005년 이전 날짜 데이터만을 사용하여 수행되었고, 테스팅은 오직 2005년 내의 날짜 데이터들만을 사용하여 수행되었습니다.

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period.
마지막으로 도출된 대미 결말로, 우리는 2005년 데이터의 모형 예측값들을 해당 시간 기간 동안 벌어진 실제 시장 동향 움직임 변동 지표들과 비교합니다.

We will first store the test and training labels (recall `y_test` is binary).
우리는 제일 먼저 테스트와 훈련 용 판별 라벨들을 단편 저장할 것입니다 (지시 확률값 `y_test` 가 이진(binary) 변수임을 회상하십시오).

```python
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train]
```

Now we threshold the fitted probability at 50% to form our predicted labels.
이제 우리는 우리의 훈련 완성된 예측 라벨 결과물을 확립 형성하기 위해 모형 산출물인 적합된 확률을 50% 의 고정된 임계치(threshold)로 설정 산정합니다.

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
진짜 시험 테스트 결과 판별 정확도는 약 48% 인 반면 역오류율은 약 52% 에 달합니다.

```python
In [18]: np.mean(labels == L_test), np.mean(labels != L_test)
```

```python
Out[18]: (0.4802, 0.5198)
```

The `!=` notation means _not equal to_, and so the last command computes the test set error rate.
여기서 `!=` 표기 부호 문법은 **같지 않다(not equal to)**를 의미하며, 역으로 위 명령어는 테스트 세트 오류율을 파악 산출 도출 계산합니다.

The results are rather disappointing: the test error rate is 52%, which is worse than random guessing!
결과들은 꽤 실망스럽습니다(disappointing): 테스트 오류율이 52%인데, 이것은 단순히 요행 추측(random guessing)으로 나오는 무작위 결괏값보다 더 나쁩니다(worse)!

Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days’ returns to predict future market performance.
물론 특정 개인이 단순히 이전 날들의 지표 수익률을 모조리 사용해서 미래 시장 성과를 단번에 예측해 낼 수 있을 것이라고 도저히 대개 기대하진 않을 것이라는 한계점을 고려하면, 이 처참한 결과가 그리 크게 놀라운 수치는 아닙니다.

(After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)
(생각해보면, 만약 진정 그렇게 예측하는 것이 가능했다면, 이 책의 저자들은 지루한 통계학 교재를 집필하고 있기보다는 그 시간에 이미 큰돈을 벌어 벼락부자(striking it rich)가 되어있었을 것입니다.)

We recall that the logistic regression model had very underwhelming _p_-values associated with all of the predictors.
우리는 여기서 다시 로지스틱 회귀 모델이 각 예측 변수들과 관련하여 연관성이 매우 약한 실망스러운(underwhelming) 낮은 _p_-값들을 가졌었다는 첫 사실을 씁쓸하게 기억을 회상(recall)합니다.

Using predictors that have no relationship with the response tends to cause a deterioration in the test error rate, and so removing such predictors may in turn yield an improvement.
타깃 반응 변수와 아무런 연관 관계성도 없는 불량 데이터 예측 변수들을 사용하는 체계는 테스트 오차율 분석 결과의 질적 악화(deterioration) 결함을 심각하게 야기하는 경향성이 있으며, 따라서 역으로 그러한 예측 변수들을 제거하면 결과적으로 반대의 점수 개선 향상(improvement) 을 도출 산출해 낼 수도 있습니다.

Below we refit the logistic regression using just `Lag1` and `Lag2`, which seemed to have the highest predictive power in the original model.
아래에서 우리는 원래 모델 안에서 단적으로 가장 높은 정밀 예측력(predictive power)을 가진 것으로 보였던 제한된 `Lag1` 그리고 `Lag2` 두 예측 지표들 만을 골라 사용하여 로지스틱 회귀를 재차 다시 한번 재적합(refit) 할 것입니다.

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
우리가 얻은 분석 데이터의 전반적인 정확도(overall accuracy), 그리고 로지스틱 회귀 모형이 단독적으로 특수한 시장 상승(increase)을 찍어 예측한 특정 발생 날들 내 기간의 예측 특정 정확도 수치를 명확하게 모조리 동시 평가해 봅시다.

```python
In [20]: (35+106)/252, 106/(106+76)
```

```python
Out[20]: (0.5595, 0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted.
이제 테스트 결과 데이터 수치가 이전에 비해서는 약간 조금 다소 나아 개선된 것처럼 보입니다: 일별 시장 일일 움직임의 약 56% 체계 확률이 요번엔 올바르게 예측되었습니다.

Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach.
분석의 총괄 수치상 (전체 오차율 측면에서) 볼 때, 이 로지스틱 회귀 방법 단일 모델의 산출 성능 확률은 원시적 단순 나이브(naive) 도박 접근법 추측 보다는 그나마 지표상 여전히 그다지 썩 대단히 나아 보이는 큰 수준 차이는 없습니다.

However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate.
그럼에도 불구하고 이 표의 특이상황 혼동 행렬 결괏값의 분석 체계가 보여주듯이 오직 로지스틱 로직 파악이 기계적으로 해당 주식 판세 시장의 극적인 '상승(increase)' 지표 방향을 콕 단일 특정 예측 집어낸 특정 상황 작동 환경의 도출된 요일 특정 날짜(days) 들 내에서만큼 한에서는, 모형은 약 58% 예측 적중 확률 정확도 비율 달성 수치 도달 성적 점수를 달성 기록 보여줍니다.

This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted.
이 기계 분석 데이터 수치 기반 도출 지표는 만약 어떤 매매 대상 특정 모형 장세가 예측 상향(increasing market) 시장 예측 환경 조건을 시그널 알릴 시 특정 날들에 자산 종목 재산을 매수(buying) 하고, 그 반작용 이면 반대로 하락 붕괴 떨어질 시그널 장이 예상 특정되는 날들에는 모조리 회피하여 관전 자재 보류 포지션만 유지 관망하는 (avoiding trades) 특정 기계 기반 매매 규칙 투기 거래 전략(trading strategy) 형성 창출 기능 발동 성립 아이디어 기초 지식 가능성 성립 신봉 단서 가능성을 확실히 시사 가능성 뒷받침 도출합니다.

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2`.
가정하여, 만약 우리가 특정한 `Lag1` 그리고 `Lag2` 시계열 단서 값들과 연결되어 파생하는 관련된 특정 결과 목표 지표 수익률(returns) 의 계산 산출 결과를 예측 투입 도출해 내고 싶다고 지정 상상 상정 가정해 봅시다.

We want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8.
우리는 목표 단서 변수 `Lag1` 과 `Lag2` 값 지표 점수 가 각각 따로 동일하게 특수 순차적으로 산술 1.2 그리고 1.1 결괏값 계수와 대응 매칭하는 동일 부합하는 특정 상황 일자의 날과, 동일 조건 반대 조합 쌍 점수로서 각각 산술 수식 1.5 지표 결괏값 과 무너지는 대칭 -0.8 점수 결과 단절 부합과 완전히 평행 동일 일치 동일 등식 부합 일치 작동 조건하는 또 다른 발생 특수 관전 날짜 데이터 요건을 지정 대치 입력 설정하여, 그 속의 반응 결과 모형 `Direction` 상승 하락 도출 여부를 기계적으로 판별 강제 예측 지시 발동 확인해 얻고 싶습니다.

We do this using the `predict()` function.
우리는 앞선 통계 기계의 내부 구조인 `predict()` 모형 예측 산출 발판 모델 함수 명령 체계를 호출 사용하여 이 강제 목표 투입 예측 산술 연산 결과를 최종 강제 도출 작동 명령 완수 처리합니다.

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

[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans1.html)

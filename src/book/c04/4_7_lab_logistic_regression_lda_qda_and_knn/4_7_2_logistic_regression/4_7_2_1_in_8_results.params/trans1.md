---
layout: default
title: "trans1"
---

[< 4.7.2 Logistic Regression](../trans1.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

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
마찬가지로 우리는 계수에 대한 _p_-value에 접근하기 위해 `pvalues` 속성을 사용할 수 있습니다 (표시되지 않음). 

```python
In [9]: results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors. This method returns predictions on the probability scale. If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model. Here we have printed only the first ten probabilities.
`results` 의 `predict()` 메서드는 예측 변수의 값이 주어졌을 때 시장이 상승할 확률을 예측하는 데 사용할 수 있습니다. 이 메서드는 확률 척도(probability scale)로 예측을 반환합니다. `predict()` 함수에 데이터 세트가 제공되지 않으면, 로지스틱 회귀 모델을 피팅하는 데 사용된 훈련 데이터(training data)에 대해 확률이 계산됩니다. 여기서는 처음 10개의 확률만 출력했습니다.

```python
In [10]: probs = results.predict()
probs[:10]
```

```python
Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812,
                0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down`. The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5. 
특정 날짜에 시장이 상승할지 하락할지 예측하려면, 이러한 예측 확률을 `Up` 또는 `Down` 이라는 클래스 레이블로 변환해야 합니다. 다음 두 명령은 시장 상승의 예측 확률이 0.5보다 큰지 작은지에 기반하여 클래스 예측 벡터를 생성합니다. 

```python
In [11]: labels = np.array(['Down']*1250)
labels[probs > 0.5] = "Up"
```

The `confusion_table()` function from the `ISLP` package summarizes these predictions, showing how many observations were correctly or incorrectly classified. The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels.
`ISLP` 패키지의 `confusion_table()` 함수는 이러한 예측을 요약하여 얼마나 많은 관측치가 정확하거나 잘못 분류되었는지 보여줍니다. `confusion_table()` 함수는 첫 번째 인수로 예측된 레이블을 취하고, 두 번째 인수로 실제(true) 레이블을 취합니다.

```python
In [12]: confusion_table(labels, Smarket.Direction)
```

|**`Out[12]:`**|`Truth`|`Down`|`Up`|
|---|---|---|---|
||`Predicted`|||
||`Down`|`145`|`141`|
||`Up`|`457`|`507`|

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions. Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions. The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct. In this case, logistic regression correctly predicted the movement of the market 52.2% of the time. 
혼동 행렬(confusion matrix)의 대각선 요소는 올바른 예측을 나타내며, 비대각선(off-diagonals)은 잘못된 예측을 나타냅니다. 따라서 우리 모델은 시장이 507일 동안 상승하고 145일 동안 하락할 것이라고 정확하게 예측하여, 총 507 + 145 = 652 번의 정확한 예측을 수행했습니다. 예측이 정확했던 날짜의 비율을 계산하기 위해 `np.mean()` 함수를 사용할 수 있습니다. 이 경우, 로지스틱 회귀는 52.2% 의 빈도로 시장의 움직임을 올바르게 예측했습니다.

```python
In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)
```

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing. However, this result is misleading because we trained and tested the model on the same set of 1,250 observations. In other words, 100 − 52.2 = 47.8% is the _training_ error rate. As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate. In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data. 
언뜻 보기에 로지스틱 회귀 모델은 무작위 추측(random guessing)보다 약간 더 잘 작동하는 것처럼 보입니다. 그러나 이 결과는 모델을 훈련하고 동일한 1,250개의 관측치 세트에서 테스트했기 때문에 오해의 소지가 있습니다(misleading). 다시 말해, 100 - 52.2 = 47.8% 는 _훈련_ 오류율(training error rate)입니다. 이전에 본 바와 같이, 훈련 오류율은 종종 지나치게 낙관적입니다 - 테스트 오류율(test error rate)을 과소평가하는 경향이 있습니다. 이 설정에서 로지스틱 회귀 모델의 정확도를 더 잘 평가하기 위해, 우리는 데이터의 일부를 사용하여 모델을 피팅한 다음 보류된(held out) 데이터를 얼마나 잘 예측하는지 검토할 수 있습니다. 

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004. We then use this vector to create a held out data set of observations from 2005.
이 전략을 구현하기 위해 먼저 2001년부터 2004년까지의 관측치에 해당하는 불리언(Boolean) 벡터를 생성합니다. 그런 다음 이 벡터를 사용하여 2005년 관측치로 구성된 보류 데이터 세트를 만듭니다.

```python
In [14]: train = (Smarket.Year < 2005)
Smarket_train = Smarket.loc[train]
Smarket_test = Smarket.loc[~train]
Smarket_test.shape
```

# **`Out[14]:`** `(252, 9)` 

The object `train` is a boolean array, since its elements are `True` and `False`. Therefore, `Smarket.loc[~train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False`. The output above indicates that there are 252 such observations. 
객체 `train` 은 요소가 `True` 및 `False` 이므로 부울 배열(boolean array)입니다. 따라서 `Smarket.loc[~train]` 은 `train` 이 `False` 인 관측치만 포함하는 주식 시장 데이터 데이터 프레임 행의 하위 집합을 생성합니다. 위의 출력은 이러한 관측치가 252개 있음을 나타냅니다. 

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005. We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005. 
이제 2005년 이전 날짜에 해당하는 데이터의 부분 집합만 사용하여 로지스틱 회귀 모델을 피팅합니다. 그런 다음 테스트 세트의 각 날짜(즉, 2005년의 날짜)에 대해 주식 시장이 상승할 예측 확률을 얻습니다. 

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
모델을 두 개의 완전히 분리된 데이터 세트에서 훈련하고 테스트했음에 주목하십시오: 훈련은 2005년 이전 날짜만 사용하여 수행되었고, 테스트는 2005년 날짜만 사용하여 수행되었습니다.

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period. We will first store the test and training labels (recall `y_test` is binary).
마지막으로, 우리는 2005년의 예측을 해당 기간 동안 시장의 실제 움직임과 비교합니다. 우리는 먼저 테스트 및 훈련 레이블을 저장할 것입니다(`y_test` 가 이진 데이터(binary)임을 상기하십시오).

```python
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train]
```

Now we threshold the fitted probability at 50% to form our predicted labels.
이제 예측된 레이블을 형성하기 위해 적합된 확률에 대해 50% 에서 임계값(threshold)을 적용합니다.

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
테스트 정확도는 약 48% 인 반면 오류율은 약 52% 입니다.

```python
In [18]: np.mean(labels == L_test), np.mean(labels != L_test)
```

```python
Out[18]: (0.4802, 0.5198)
```

The `!=` notation means _not equal to_, and so the last command computes the test set error rate. The results are rather disappointing: the test error rate is 52%, which is worse than random guessing! Of course this result is not all that surprising, given that one 성would not generally expect to be able to use previous days’ returns to predict future market performance. (After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)
`!=` 표기법은 _같지 않음(not equal to)_ 을 의미하며, 따라서 마지막 명령은 테스트 세트 오류율을 계산합니다. 결과는 다소 실망스럽습니다: 테스트 오류율이 52% 로 무작위 추측보다 더 나쁩니다! 물론 이전 날의 수익률을 사용하여 미래의 시장 성과를 예측할 수 있을 것이라고 일반적으로 기대하지 않는다는 점을 감안할 때 이 결과가 그리 놀라운 것은 아닙니다. (만약 그것이 가능했다면, 이 책의 저자들도 통계학 교과서를 쓰는 대신 큰돈을 벌고 있었을 것입니다.)

We recall that the logistic regression model had very underwhelming _p_-values associated with all of the predictors. Using predictors that have no relationship with the response tends to cause a deterioration in the test error rate, and so removing such predictors may in turn yield an improvement. Below we refit the logistic regression using just `Lag1` and `Lag2`, which seemed to have the highest predictive power in the original model.
우리는 로지스틱 회귀 모델이 모든 예측 변수와 연관되어 매우 실망스러운 _p_-value를 가졌음을 상기합니다. 반응 변수와 연관성이 없는 예측 변수를 사용하면 테스트 오류율이 저하되는 경향이 있으므로 이러한 예측 변수를 제거하면 결과적으로 모델이 개선될 수 있습니다. 아래에서는 원래 모델에서 가장 높은 예측력을 가지고 있는 것처럼 보였던 `Lag1` 과 `Lag2` 만을 사용하여 로지스틱 회귀를 다시 피팅합니다.

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
로지스틱 회귀가 시장 상승을 예측한 날에 대한 정확도뿐만 아니라 전반적인 정확도도 평가해 보겠습니다.

```python
In [20]: (35+106)/252, 106/(106+76)
```

```python
Out[20]: (0.5595, 0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted. Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach. However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate. This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted.
이제 결과가 약간 나아 보입니다: 매일 움직임의 56%가 올바르게 예측되었습니다. 그러므로 전체 오류율의 측면에서 로지스틱 회귀 방법은 나이브한(순진한) 접근 방식보다 나을 것이 없습니다. 그러나 혼동 행렬은 로지스틱 회귀가 시장의 상승을 예측한 날에는 58% 의 정확도를 갖는다는 것을 보여줍니다. 이는 모델이 상승장을 예측하는 날에는 매수를 하고, 하락장이 예측되는 날에는 거래를 피하는 가능성 있는 트레이딩 전략을 시사합니다.

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2`. We want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8. We do this using the `predict()` function.
특정한 `Lag1` 및 `Lag2` 값과 관련된 수익을 예측하고 싶다고 가정해 봅시다. 우리는 `Lag1` 과 `Lag2` 가 각각 1.2와 1.1인 날과 1.5와 -0.8인 날에 주식 시장의 방향(`Direction`)을 예측하고자 합니다. `predict()` 함수를 사용하여 이를 수행합니다.

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

[< 4.7.2 Logistic Regression](../trans1.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans1.html)

---
layout: default
title: "trans2"
---

[< 4.7.2 Logistic Regression](../trans2.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

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
이와 똑같은 야매 해킹 스킬로, 엑기스 계수 파편들인 `params` 대신 아예 그 계수들의 통계적 목숨 신용등급인 _p_-value 수치들만 쏙 빼먹고 싶다면 `pvalues` 속성을 때려 박으면 됩니다. (너무 뻔해서 화면엔 생략했습니다). 

```python
In [9]: results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors. This method returns predictions on the probability scale. If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model. Here we have printed only the first ten probabilities.
자, 이제 피팅을 마친 결과물 `results` 깡통에다가 `predict()` 라는 살벌한 미래 예언 마법 주문을 스킬로 꽂아 넣으면, 컴퓨터가 알아서 과연 "내일 시장 호가가 상승 폭발(Up) 할 것인가?" 에 대한 배팅 확률 결과를 도출해 냅니다. 이 도구는 기본적으로 0부터 1 사이를 요동치는 '당첨 로또 확률 도수(probability scale)' 모드로 숫자를 뱉어냅니다. 만약 `predict()` 함수 부품 안에다 "새로운 내일의 $X$ 데이터" 를 우겨 넣지 않고 그냥 무식하게 뻥 빈 괄호로 때리면, 모델은 훈련하며 씹어 먹었던 과거 자신이 학습용으로 썼던 오리지널 훈련용 과거 데이터들을 그대로 재활용해 자기 확신성 확률 채점으로 뱉어버립니다. 맛보기로 딱 앞쪽 주가 10일 치의 떡상 확률 예측 스코어들만 출력해 보았습니다.

```python
In [10]: probs = results.predict()
probs[:10]
```

```python
Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812,
                0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down`. The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5. 
하지만 결국 우리가 손에 쥐어야 할 진짜 대박 과실은 저런 애매모호한 0.507 같은 확률 숫자가 아니라, 그래서 "오늘 살까(`Up`) 팔까(`Down`)?" 를 결정짓는 확실한 이분법 막도장 지시 레이블(Class Label)입니다. 이걸 쟁취하기 위해, 다음의 단 2줄짜리 파이썬 칼날 명령어 코딩으로 우리는 저 흐리멍덩한 확률 게이지가 **"50% (0.5) 반반 무 많이" 커트라인** 위를 아슬아슬하게 넘겼느냐, 아니면 밑으로 꺼졌느냐를 기계적으로 판단하여 강제로 `Up` 과 `Down` 이란 과녁 문자 벡터판으로 변환 수술을 갈겨버립니다. 

```python
In [11]: labels = np.array(['Down']*1250)
labels[probs > 0.5] = "Up"
```

The `confusion_table()` function from the `ISLP` package summarizes these predictions, showing how many observations were correctly or incorrectly classified. The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels.
자 이제 진짜 잔인한 채점 시간입니다. 우리가 방금 전 `ISLP` 특급 보급품 무기고에서 쌔벼온 `confusion_table()` (혼동 행렬표) 심판 함수를 작동시키면, 그동안 우리 모델이 얼마나 헛발질을 하고 얼마나 뒷걸음질 치다 쥐를 잡았는지(올바른 분류와 틀린 분류 횟수)를 낱낱이 표로 박제해 요약해 줍니다. 이 `confusion_table()` 심판관 녀석은 첫 번째 입력 아가리에 "기계가 예측한 팻말" 을 물리고, 두 번째 투입구엔 세상에 숨길 수 없는 진짜 정답인 "해딩 날 주가의 찐 성적 팻말" 을 집어넣어 구동시킵니다.

```python
In [12]: confusion_table(labels, Smarket.Direction)
```

|**`Out[12]:`**|`Truth`|`Down`|`Up`|
|---|---|---|---|
||`Predicted`|||
||`Down`|`145`|`141`|
||`Up`|`457`|`507`|

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions. Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions. The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct. In this case, logistic regression correctly predicted the movement of the market 52.2% of the time. 
출력된 এই 기괴한 '혼동 행렬(confusion matrix)' 십자가 표의 한가운데 대각선 조각 숫자들이 바로 "야호 빙고! 정답!" 을 외치는 극강의 승리 횟수 타점이며, 가장자리 대각선 바깥(off-diagonals) 에 널린 지뢰 숫자들은 예측이 삐끗해서 빗나가 헛발 폭망한 횟수 타격 오답을 의미합니다. 결론적으로 우리 로지스틱 확률 머신은, 주식이 떡상(`Up`) 할 거란걸 507일 날짜 동안 정확히 저격 예측했고, 주식이 나락(`Down`) 으로 갈 거란 걸 145일 날짜 동안 귀신같이 때려 맞춰서, 도합 **507 + 145 = 총 652번의 정답 홈런 타격**을 쳐냈습니다! 이 복잡한 타율 계산을 파이썬 깡패 무기 `np.mean()` 함수에 맡기면 자기가 알아서 정답 명중률 게이지를 분수율로 산출 뻥튀기해 줍니다. 결과적으로 까보니, 이 대단하신 로지스틱 회귀 모델의 족집게 확률 점수는 시장 방향을 찍어 맞춘 역대 승률 타율 **절반을 아주 쥐꼬리만큼 넘긴 52.2%** 의 승률 적중 파워를 내뿜었습니다. 

```python
In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)
```

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing. However, this result is misleading because we trained and tested the model on the same set of 1,250 observations. In other words, 100 − 52.2 = 47.8% is the _training_ error rate. As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate. In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data. 
언뜻 속아 넘어가기 쉬운 겉모습! "오? 아무것도 모르고 눈감고 50% 확률 동전 던지기로 찍는 것보단 52.2% 니까 모델 스킬 쓰길 훨씬 낫네 ㅋ" 라고 혹해서 기뻐할지 모릅니다. 하지만 명심하십시오! 이것은 통계판의 끔찍한 조작 환상 극의 기만(misleading) 함정 거미줄 늪입니다!! 왜냐고요? 우린 방금 전 이 모델 멍청이에게 **시험문제(1,250개 과거치)를 갖다 바치며 가르친(Train) 뒤, 평가할 때(Test) 놀랍게도 같은 시험문제를 그대로 또 던져줘서 오픈북 컨닝**을 시켰기 때문입니다! 다시 말하자면 지금 계산된 100 - 52.2 = 47.8% 오답률 불량 지표 수치는 실전 야생 모의고사인 테스트 폭망 점수가 아니라, 답안지 다 외운 연습장 **'훈련(Training)' 오차율 점수**에 불과합니다. 우리가 전에도 뼈저리게 뒤통수 맞았듯 겪었지만, 이 연습장 훈련 에러 점수는 항상 우릴 꼬시기 위해 세상 편한 장밋빛 초-긍정 낙관 망상에 빠진 뻥카 수치일 뿐입니다 — 늘 진짜로 겪게 될 야생 수능 당일 실전인 "테스트 에러율(Test Error)" 거탑의 매운맛 난이도를 아주 한참 깎아내려 무시하고 과소평가(underestimate) 하는 교활한 사기꾼 치부 경향이 있죠. 우린 이제 이런 사기극을 뒤집어엎고, 진짜 피비린내 나는 주식판 세팅에서 모델 실력을 멱살 잡고 털기 위해! 과감하게 주어진 데이터의 생살을 찢어 발라 훈련용 일부분으로만 빡세게 공부 세팅 피팅 시킨 뒤, 모델이 태어나 단 한 번도 본 적 없는 철저히 창고에 감춰둔 뒷주머니 비밀 무기 데이터(held out) 를 시험지로 던져줘 얼마나 기가 막히게 내일의 미래를 예언하는지 그 실전 야생 적중력 타격 감각 성능을 시험 극렬 테스트할 것입니다! 

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004. We then use this vector to create a held out data set of observations from 2005.
이 악랄한 살 떨리는 실전 테스트 분리 찢기 전략을 수행 구현하기 위해, 우린 파이썬 코딩 흑마법을 써서 우선 2001년 초부터 2004년 연말 구역까지의 훈련 전용 과거 잡동사니 일자 기록 조각들만 쏙쏙 타겟 추출하는 스위치 제어 불리언(Boolean `True/False`) 기폭장치 벡터를 빚어냅니다. 그런 다음, 이 스위치 조작 벡터 방패를 방패막이 분단 트리거로 역 이용 발동시켜서, 기계가 결코 곁눈질할 수 없었던 최신 따끈따끈한 **2005년 미래판 신상 데이터 파편들**만을 싹 긁어 분리 보류 인양 격리(held out)하여 모의고사용 살육 시험대 데이터 장치판 타격 진입 세팅을 준비 조작해 구축해 무장시켜 버립니다.

```python
In [14]: train = (Smarket.Year < 2005)
Smarket_train = Smarket.loc[train]
Smarket_test = Smarket.loc[~train]
Smarket_test.shape
```

# **`Out[14]:`** `(252, 9)` 

The object `train` is a boolean array, since its elements are `True` and `False`. Therefore, `Smarket.loc[~train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False`. The output above indicates that there are 252 such observations. 
방금 선언해 조작한 `train` 객체판 덩이는 조각 속살이 온통 오직 예/아니오 두 편 가르기 표식 `True(참)` 랑 `False(거짓)` 꼬리표 딱지로만 뒤집어 씌워진 스위치 불리언 지뢰 배열판입니다. 따라서 저기 판다스 킬러 인덱싱 `Smarket.loc[~train]` 물결 `~` 부정 폭탄 무기 꺾기 조작은 곧, "그 기조 조건이 `train` 이 절대 뒤집어진 완전 개방구 `False(아니다)` 에 결박 타격 기표되는 나머지 찌꺼기 몫" 이란 기상천외 반전 스위치 색출 추출을 선언 폭발 타격하며, 결과적으로 Smarket 몸통 구조에서 순전히 시험대에 오를 불쌍한 영혼 파편들만 잔인 조작 추출 찢어서 새로운 쪼그라든 부분집합 데이터 표 덩이를 짜 맞추어 발 굴 조 진 무마 창설하게 됩니다. 맨 마지막 위 뱉어진 무 조작 전리품 크기 수치를 보면 그 잔혹 발탁 모의고사 타깃 시험지 타깃 관측치 희생양 머릿수 몫이 **정확히 252 마리 개수** 분량만큼 남아 도 열해 진 배치 대기 탑재 전열 포진되어 있음을 지표 선 폭 타격 증명합니다. 

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005. We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005. 
자, 이제 피의 훈련장이다! 우린 모델녀석의 머슬 메모리에 오직 딱 **2005년 이전에 발생했던 먼지 쌓인 옛날 과거 훈련 일지 파편** 쪼가리 데이터 부분집합 만을 가혹하게 먹여 단련 훈련 강제 주입 주입 억지 훈련 시켜 버립니다 (피팅 fit). 그리고 나선 그 훈련 뽕에 취한 기계에게 드디어 칼을 쥐여주고 우리가 뒷주머니에 꽁꽁 훔쳐 모셔 숨겨둔 "테스트 전장 전장 세트판", 즉 미증유의 영역 **2005년 미래 타겟** 일자 하나하나를 표적으로 "내일 오를 거 같냐?"(확률) 예측 스코어를 무자비 단 전 폭 갈겨 타 투 투 하 방 터 무 찍어 뽑아 내 발사 강 제 획득 착수 진단 폭 취를 구 형 감 행 합니다 .

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
소름 돋는 분리 조작 기술력을 다시 한번 주목 각인 기 상 타 관 찰 돌 립 하십 시오: 지금 이 순간 우리는 불쌍한 로봇 기계 머신을 **두 줄기 완전히 평행 우주처럼 철저히 동 떨 어 지 고 차 단 찢 기 폐 쇄 단 절 무결 전 단 된 분리 데이터 벽 영 역 공간 덩 어 리들 구 형 지 형 세트 판** 에서 훈련 피를 뽑고 실전을 갈궜습니다! 즉, 땀 흘린 도장 '훈련 무 대' 는 오직 무 조 전 2005년 문턱 이 십 전 파 편 과 거 력 옛 흔 적 사료 만 갈아 먹였고 반면 수능 모 의 고 사 심판 결계 "테 스트 타격 평가 도 마 형 장" 은 기계가 단 한 줄도 맛볼 여 지 수 결 무 차 부 무 허 참 당 무결 못 했 던 무 상 청 정 구 조 **잔혹 실 전 미래 2005년 년 도 일 바 파편 무기** 표 적 일 들 로만 기 무결 수 구 형 덮 타 단 조 타 집 결 지 단 전 참 돌 조 발 무 마 갈 통 수 타 격 포 단 구 돌 폭 도 막 구 기 형 정 차 형 동 타 부 전 집 구 시 무단 켰 답 통 니다!

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period. We will first store the test and training labels (recall `y_test` is binary).
드디어 숨 막히는 마지막 채점의 장! 우린 저 기계 놈이 미친 듯 내뱉은 **눈먼 2005년도 떡상 예측 스코어**들과, 실제로 그 해 거대한 시장 판 덩어리가 피도 눈물도 없이 어떻게 널 뛰고 발작해 미쳐 돌아 움직였는지 '그 잔혹한 실제 진또배기 움직임 운명(실제 정답)' 의 방향 곡선을 도마 위에 올려두고 처절 압 살 단 도 마 비교 피 튀 채점 결 과 폭 검 거 검증 을 관 전 거 전 결 수행 타 격 결 단 파 차 겠 구 수 발 습 다! 이 피 검사 형 전 작업 피 튀 교 조 사전 워밍업 예 비 로, 우리는 일단 시험판과 훈련판 과녁 표식 과 녁 정답 진 과녁판 표식 레 이블 판때기들을 창 고 안 구 통 무 도 창 고 로 임시 전 분 전 편 압 보 조 저장 수 기 갈 수 결 단 차 장 전 투 보 부 기 킵 해 다 거 조 모 두 조 포 겠 포 발 다 (아 참, 저기 정 답 타 깃 `y_test` 는 0 아 님 1 지 통 쪼 갈 무 거 부 전 타 쪼 개 던 저 거 거 단 극 단 적 이진(binary) 모 듈 총 전 포 발 로 구성 돼 도 투 전 장 단 포 파 되 전 있다는 사실 참 진 동 기 단 관 차 상 하 도 비 참 전 차 단 기 부 차 십 조 시 동 오 보).

```python
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train]
```

Now we threshold the fitted probability at 50% to form our predicted labels.
이제 드디어 컴퓨터가 애매모호하게 소수점으로 뱉싸지른 저 훈련 피팅 잔류 **예측 '확률(probability)' 조각 숫자** 무더기 더미 들 위 에 다 가, 잔인한 단 두 동 강 토막 절 단 결 단 선 극악 커트라인 **임계점(threshold) 작두 칼날 지표율 반반 50% 폭격 무 잣대 선** 을 시 퍼 렇게 번 쩍 갈 폭 기 꽂 기 위 전 수 꽂 아 투 차 무결 발 탕 박 터 내려 찢 꽂 구 분 찍 보 구 무 다 결 정 타 어 넣 단 치 고, 최종적으로 이 쪽 "Up(떡상) 이냐 저쪽 "Down(나락) 이냐" 를 멱살 단 단 낙 전 찢 무 결 통 명 명 구 지 어 갈라 버린 **"궁 극 기 조 명 포 진 압 참 포 구 예측 징 지 팻 말 레이블 딱 치(predicted labels)" 무 조 성 차 성 배 구 형 조 집 구 제 단 위 치 지 형 타 극 결 동 창 립 구 축 형 배 조 자 수 거** 할 모 보 셋 돌 치 참 지 겠 습 치 파 다 니다.

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
야생 전투 실전 모의고사 수능 채점 결과, 승리 **테스트 적중 정확도(test accuracy)** 점수는 겨우 발 기 무 보 참 꼴 랑 찢 **약 48%** 선에서 짐 싸 추락 돌 다 나 락 부 구 단 참 결 고, 틀 려 먹 고 빗나가 오발 폭발 무 기 치 오 전 오 참 차 조 헛 치 결 나 폭 타 수 지 참 오 차 낸 삽 질 에러 오 답 율 폭 발 에 러 점 수 모 오 형(error rate) 기 참 수 는 **빌 어 발 무 참 차 비 무 단 단 대 략 절 반 이 상 비 치 참 약 52%** 의 비 부 수 타 부 참 전 무 지 진 무결 전 구 극 나 형 막 구 단 모 조 수 를 찍 나 지 구 모 내 참 참 터 발 구 뿜 었 지 진 습 부 다 단 니 냐 모 차 전다.

The `!=` notation means _not equal to_, and so the last command computes the test set error rate. The results are rather disappointing: the test error rate is 52%, which is worse than random guessing! Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days’ returns to predict future market performance. (After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)
방금 윗 파이썬 코드에서 쓰인 `!=` 특수 기호는 **_결코 똑같지 않다(not equal to)! 틀렸다!_** 란 의미의 판정을 내립니다. 따라서 맨 마지막 시점의 명령줄은 이 모의고사(테스트 세트)가 얼마나 개판이었는지, 즉 오답을 낸 삑사리인 **에러율(error rate)** 을 뼈아프게 계산해 냅니다. 그 결과는 그야말로 처참하고 실망스럽습니다: 모의고사 폭구 오답률은 무려 **52%** 로, 이것은 아무 생각 없이 눈감고 50 대 50 동전 던지기로 찍는 무작위 찍기(random guessing) 방식보다도 훨씬 더 멍청한 바닥을 치는 성적입니다! 물론, 어제그제 주식 수익률 나부랭이 데이터 따위를 가지고 감히 내일의 거대한 주식 시장 떡상/떡락 방향성을 다 꿰뚫어 볼 수 있다고 거만하게 기대하는 것 자체가 미친 짓이므로, 이런 참담한 폭망 결과가 통계학적으로 그리 놀라운 일도 아닙니다. (솔직히 말해, 만약 그 옛날 주식 데이터 쪼가리로 미래의 황금 주가를 백발백중 족집게처럼 때려 맞추는 게 진짜 가능했다면, 이 책의 저자 양반들도 골치 아프게 통계학 교과서나 쓰고 앉아있지 않고 진작에 월스트리트 쌍끌이로 떼돈을 쓸어 담아 갑부가 되어 날아갔을 것입니다!)

We recall that the logistic regression model had very underwhelming _p_-values associated with all of the predictors. Using predictors that have no relationship with the response tends to cause a deterioration in the test error rate, and so removing such predictors may in turn yield an improvement. Below we refit the logistic regression using just `Lag1` and `Lag2`, which seemed to have the highest predictive power in the original model.
정신을 챙기고 뼈 아픈 반성 타임을 가져봅시다! 아까 저 위쪽에서 우리가 간과했던 팩트 진실 하나를 서늘하게 끄집어 회상(recall) 해 봅시다. 그 잘났던 로지스틱 회귀 모델 머신이 왜 똥볼을 찼을까요? 당연합니다! 처음 모델 훈련 때 장착했던 힌트 부품(예측 변수)들이 몽땅 다 하나같이 **터무니없이 불량한 _p_-value(p-값) 계급장**을 달고 있었음을 우린 직시했습니다. 어차피 정답 과녁(반응 변수)과 실질적인 상관관계의 생명줄이 하나도 없는 이런 잡동사니 쓰레기 힌트 예측 변수들까지 좋다고 박박 긁어모아 기계에 쑤셔 넣으면, 그 노이즈 간섭 때문에 실전 모의고사 테스트 에러율이 미친 듯이 박살 나고 오염되어 저하(deterioration) 되는 끔찍한 부작용 병목 현상만 유발할 뿐입니다. 따라서 아예 이런 불량 파츠 변수들을 과감히 칼날로 도려내 제거해 버리는 것이 종종 모델의 컨디션을 확 끌어올려 성능 향상의 대박 결과(improvement) 를 낳습니다. 그리하여 바로 아래 파이썬 코드에서는, 그나마 아까 첫 번째 잡동사니 원본 모델에서 눈곱만큼이라도 제일 예측력 파워가 높아 보였던 에이스 후보 `Lag1` 과 `Lag2`, 단 두 놈의 정예 멤버만 차출해서 로지스틱 회귀 머신을 가볍고 날카롭게 다시 피팅 세팅(refit) 해 볼 것입니다.

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
과연 이번엔 로봇이 좀 쓸만해졌을까요? 로지스틱 회귀가 시장 상승세에 올라타 "가즈아, 오를 거다 떡상!" 을 예측한 날들의 핀포인트 적중도 명중률은 물론이고, 이런저런 것 다 합친 판 전체의 총 종합 명중 정확도 스펙(overall accuracy)까지 모조리 계산기로 탈탈 털어 해부 평가 폭격을 갈겨보겠습니다.

```python
In [20]: (35+106)/252, 106/(106+76)
```

```python
Out[20]: (0.5595, 0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted. Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach. However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate. This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted.
오호라, 드디어 피를 깎는 다이어트(변수 제거)의 쾌감! 결과가 전보다 약간 살아난 듯 보입니다! 매일 요동치는 야생 주가 널뛰기 무브먼트의 **약 56%** 나 되는 흐름을 기계 녀석이 올바르게 요격 예측해 잡아냈습니다. 하지만 잠깐, 이 판 전체의 총합 오답 에러율(overall error rate) 관점이라는 싸늘한 잣대로 다시 쑤셔보면, 56% 승률은 그저 반반 무 많이 찍기나 다름없는 뇌 빼기 동전 던지기식 나이브(naive) 전략보다 그닥 압도적으로 더 위대하다고 칭송할 수준은 결코 못 됩니다. 그러나! 우리의 채점판 표인 혼동 행렬(confusion matrix) 속살을 살짝 파헤쳐 보면 아주 구미가 당기는 기가 막힌 통계 하나가 숨어 있습니다: **로지스틱 회귀 머신이 "오늘은 무조건 주식 시장이 떡상(increase) 한다!" 라고 신호를 뿜어낸 날짜들만 쏙쏙 골라서 채점해 보면, 그 적중 명중률이 무려 58% 까지 솟구친다는 꿀 팩트가 발굴됩니다.** 이것은 우리에게 아주 짜릿하고 달콤한 작전 지시, 즉 "모델 녀석이 오를 거라고 신호를 깜빡이는 날에만 영혼을 끌어모아 베팅(buying) 해 매수하고, 이 자식이 떨어질 거라고 경고하는 찝찝한 날엔 주식 매매 거래를 싹 중단하고 관망 도피 피신하라!" 라는 승률 58% 짜리 실전 야생 트레이딩 전투 전략(trading strategy)을 강력히 속삭이며 설계 시사해 줍니다.

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2`. We want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8. We do this using the `predict()` function.
이 기고만장해진 확률 머신에게 마지막 극한 킬러 테스트 상상 퀘스트를 하나 줘볼까요? 만약 우리가 특정 수치로 기이하게 비틀어 맞춘 `Lag1` 및 `Lag2` 의 가상의 돌연변이 수치 상황에서 터져 나올 수익 반응 타율을 조준 예측하고 싶다고 상상(Suppose) 해 보십시오. 구체적 작전 상황 세팅! 우리는 두 가지 완전히 다른 날의 미래 운명 방향(`Direction`)을 꿰뚫고 싶습니다: 하루는 어제(`Lag1`) 1.2%, 엊그제(`Lag2`) 1.1% 씩 양일 모두 상승 펌핑을 친 불장 훈훈한 날이고, 또 다른 날은 어젠 무려 1.5% 급등했지만 엊그젠 -0.8% 로 처박혀 널뛰기 발작을 한 기괴한 날입니다. 우리는 다시 한번 우리의 영특한 수정 구슬 도구인 `predict()` 예언 함수 마법을 소환 구동하여 이 두 가상 상황의 미래 스코어를 뽑아냅니다.

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

[< 4.7.2 Logistic Regression](../trans2.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans2.html)

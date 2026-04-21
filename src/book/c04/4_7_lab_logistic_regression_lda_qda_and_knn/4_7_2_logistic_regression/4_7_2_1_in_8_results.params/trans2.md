---
layout: default
title: "trans2"
---

[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# **`In [8]:`** `results.params` 

| **`Out[8]:`** | `intercept` (조준점) | `-0.126000` |
|---|---|---|
| | `Lag1` (어제의 피바람) | `-0.073074` |
| | `Lag2` (그제의 광기) | `-0.042301` |
| | `Lag3` | `0.011085` |
| | `Lag4` | `0.009359` |
| | `Lag5` | `0.010313` |
| | `Volume` (어제 거래량 덩치)| `0.135441` |
| | `dtype: float64` | |

Likewise we can use the `pvalues` attribute to access the _p_-values for the coefficients (not shown).
이와 똑같은 꼼수 원리로, 만약 우리가 가중치 점수가 아니라 "이 힌트가 진짜인지 가짜인지 판별해 주는 거짓말 탐지기 확률(p-value)" 수치만 쏙! 빼내고 싶다면, 방금 전 `.params` 대신 이번엔 `.pvalues` 라는 속성 버튼을 똑딱 눌러주면 됩니다. (코드가 너무 길어져서 위 표기에는 생략했습니다.)

```python
In [9]: results.pvalues
```

The `predict()` method of `results` can be used to predict the probability that the market will go up, given values of the predictors.
자, 기계 학습 훈련이 다 끝났다면 이 `results` 로켓 엔진에 달린 궁극의 발사 버튼, **`predict()` 메서드**를 누를 차례입니다. 이 버튼을 누르면 우리가 챙겨둔 탄환 힌트(예측 변수들)를 기계가 집어삼킨 다음, "음... 오늘 주식 시장이 위로 솟구쳐 오를 확률은 말이야..." 라며 기막힌 상승 확률 예측 점수를 토해냅니다.

This method returns predictions on the probability scale.
물론 로지스틱 기계답게 다짜고짜 "오른다!(Up)" "내린다!(Down)" 문자를 던지는 성격 급한 짓은 안 합니다. 대신 아주 냉정하게 `0.8(80%)`, `0.3(30%)` 같은 확률 스케일 스코어로 예언 퍼센티지를 쏴줍니다.

If no data set is supplied to the `predict()` function, then the probabilities are computed for the training data that was used to fit the logistic regression model.
그런데 주의할 점! 이 `predict()` 입구 구멍에다가 '미래에 쓸 새로운 데이터'를 안 넣어주고 그냥 뻥 비워둔 채 발사 버튼을 누르면 이 기계는 대체 어떻게 할까요? 멍청하게도 얘가 예전에 훈련할 때 이미 씹고 뜯고 맛봤던 **그 기존의 훈련 데이터(과거 기출문제)를 꺼내서 자기 자신의 실력을 셀프 확인**하는 확률 점검 예측을 시작합니다. 

Here we have printed only the first ten probabilities.
일단 그렇게 기출문제 점검으로 얻어낸 확률 스코어들 중, 기계가 뱉어낸 맨 처음 파편 10개만 슬쩍 먼저 출력해서 구경해 보겠습니다.

```python
In [10]: probs = results.predict()
probs[:10]
```

```python
Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812,
                0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])
```

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, `Up` or `Down`.
보이시나요? 저렇게 `0.507...`, `0.481...` 식으로 확률만 던져주면 도박장에선 배팅을 내릴 수가 없습니다. 따라서 우리는 저 모호한 확률 수치 고깃덩어리들을 **진짜 올라갈 팀(`Up`)** 인지 아니면 떡락할 **내려갈 팀(`Down`)** 인지 명확한 흑백 문자 클래스 라벨(label) 이름표로 강제 변환, 도축 작업을 무자비하게 해줘야만 합니다!

The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5.
아래 두 줄의 코드가 바로 그 도축 작업입니다. 쿨하게 **0.5 (50% 활률)** 을 커트라인 임계점(컷오프) 무기로 설정해서, 확률 스코어가 이 데스라인을 넘으면 "넌 상승(Up) 팀!" 이라고 낙인을 박아버리고, 넘지 못하고 찌그러지면 "넌 하락(Down) 팀!" 이라고 잔혹하게 이분법 라벨 도장을 팡팡 찍어 흑백 벡터 수레를 만드는 거죠. 

```python
In [11]: labels = np.array(['Down']*1250) # 우선 1,250개 밑장 빼고 전부 다 쫄아서 하락(Down) 도장으로 1차 초벌 낙인!
labels[probs > 0.5] = "Up" # 확률 스코어 0.5 넘는 놈들 머리 끄덩이만 잡아서 상승(Up) 합격 명패로 바꿔치기 강제 수정!
```

The `confusion_table()` function from the `ISLP` package summarizes these predictions, showing how many observations were correctly or incorrectly classified.
이 잔혹한 심사의 끝에 남은 건 기계의 예측 결과가 원래 정답과 진짜 얼마나 팩트로 맞아떨어졌나 채점을 해보는 겁니다. `ISLP` 공구함에서 가져온 **`confusion_table()` (혼동 행렬 폭로판)** 기능이 이 채점을 대신해 줍니다. 이 녀석이 바로, 이 깡패 기계가 몇 건이나 똥볼을 찼는지(오류), 혹은 몇 건이나 신들린 듯 정답을 맞혔는지 그 성적표를 한 장의 요약표 칠판에 적나라하게 폭로시켜 줍니다.

The `confusion_table()` function takes as first argument the predicted labels, and second argument the true labels.
선생님이 이 `confusion_table()` 폭로판 채점기를 돌릴 때 넣어야 할 규칙은 간단합니다: 첫 번째 넣을 놈은 기계가 찍어 제출한 짝퉁 답안지(predicted labels), 그리고 두 번째로 넣을 놈은 진짜 숨겨둔 황금 팩트 정답지(true labels)입니다.

```python
In [12]: confusion_table(labels, Smarket.Direction)
```

| **`Out[12]:`** | `Truth` (진짜 정답 팩트) | `Down` | `Up` |
|---|---|---|---|
| | `Predicted` (기계가 낸 짝퉁 예측) | | |
| | `Down` (기계가 예측) | `145` (정답 일치!) | `141` |
| | `Up` (기계가 예측) | `457` | `507` (정답 일치!) |

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions.
짜잔! 폭로판이 떴습니다. 이 네모난 칠판 한가운데를 비스듬히 가로지르는 대각선(diagonal) 자리에 박힌 숫자 `145`와 `507`은 기계가 정답 팩트와 완벽히 찰떡궁합으로 맞아떨어진 영광의 **축배(정답 타점)** 를 의미합니다. 반대로 대각선 밖으로 삐져나간 찌그러진 구석의 쓰레기 숫자(`141`, `457`)들은 기계가 똥볼을 거하게 차버린 슬픈 **오류 삽질** 횟수를 나타내죠.

Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of 507 + 145 = 652 correct predictions.
고로 이 폭로판 성적을 읽어볼까요? 우리의 깡패 로지스틱 기계는 "음, 507번은 시장이 뛸 것이고, 145번은 시장이 꼬라박을 거야!"라고 쪽집게같이 맞췄다는 뜻입니다. 합쳐서 총 507 + 145 = 652 번이라는 나름 영광스러운 신들린 촉의 과제를 당당히 올바르게 맞춰 도출 달성했습니다!

The `np.mean()` function can be used to compute the fraction of days for which the prediction was correct.
이 귀찮은 더하기 덧셈을 코드 한방에 퍼센티지(클래스 분류 정확률 확률 점수) 체계로 날려버리고 싶다면, 파이썬 넘파이 공구 중 아주 유용한 **`np.mean()` (평균 내라!) 함수** 톱니를 사용하면 단숨에 정답 점유 분수 비율 타점 수치를 뿜어냅니다.

In this case, logistic regression correctly predicted the movement of the market 52.2% of the time.
그렇게 굴려본 결과, 우리의 로지스틱 회귀 기계는 수많은 1250번의 도박 시간 중 약 절반에 해당하는 **52.2% 의 시간** 동안 도박장 주식 시장의 상하 화살표 움직임 방향 정답 확률 타깃을 귀신같이 올바르게 맞춰 냈습니다. 오호? 선방했는데요?

```python
In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)
```

# **`Out[13]:`** `(0.5216, 0.5216)` 

At first glance, it appears that the logistic regression model is working a little better than random guessing.
오호? 이 겉보기 숫자(At first glance) 스코어 점수 52.2%만 얼핏 보고 있자니, 우리의 위대한 로지스틱 기계가 그냥 눈 감고 원숭이가 동전 50:50 반반 던지는 무식한 찍기 추측 확률(random guessing) 보다는 미세하긴 하지만 어쨌건 2.2%나 약간은 더 돈을 잘 따는 천재 작동 메커니즘인 것처럼 우리 눈을 속이며 대견해 보입니다.

However, this result is misleading because we trained and tested the model on the same set of 1,250 observations.
**하지만, 정신 차리세요! 이건 엄청난 함정이자 사기극(misleading)입니다!** 왜냐하면 우린 엄청난 금기를 깼거든요. 우리는 아까 이 깡패 기계한테 1,250개의 '과거 기출문제 정답지 데이터'를 주면서 똑같이 훈련(trained) 시켜놓고선, 시험 칠 때도 뻔뻔하게 그 자신이 이미 달달 외워본 똑! 같! 은! 1,250개의 중복 데이터 세트 문제지 관측치를 내밀고서 셀프 시험판 채점 테스트(tested)를 돌려 우려먹었기 때문입니다!

In other words, 100 − 52.2 = 47.8% is the _training_ error rate.
다시 말해, 저기서 얻은 자랑스러운 52.2% 정답률의 이면에 도출된 통계 분석 에러 오답 확률치 인 100 − 52.2 = 47.8% 쓰레기 점수는, 진짜 야생에서 통할 실전 생존 팩트 에러율이 아니라 단지 지 혼자 공부하고 치른 방구석 챔피언 결과물, **훈련(training) 오차율** 에 불과하다는 끔찍한 실태 전제입니다 반복 조립 통계.

As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate.
우리가 이론 병법서 2장에서 수없이 귀에 못이 박이게 이론으로 배웠던 바와 똑같이, 훈련지 방구석에서 지 혼자 풀어낸 저 단일 반복 훈련 오차율 점수는 데이터 속성 메커니즘 특성상 종종 지 주제를 모르고 지나치게 과도하게 나르시시즘에 빠져 터무니없는 비정상 낙관적인(overly optimistic) 오만경향을 띱니다 — 그 쓰레기 스코어 점수 결과 지표 구조는 대개 우리가 찐으로 목숨을 걸어야 할 실전 테스트 시험 검정 지표 오차율(test error rate) 을 수치적으로 심각하게 얕잡아보고 기만해서 낮잡아 과소평가(underestimate) 하는 근본적 불량 편향 한계 기저 구도를 지니어 갖습니다.

In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the _held out_ data.
그럼 어쩌라고요? 그래서 우리는 지금의 이 불량 작동 테스트 설정 세팅 환경 안에서 도출된 이 기계 모델의 판별 스코어 오차 정확도 허상을 까부수고 단연코 더 제대로 칼같이 잘 조립 성능 평가하기 위해 절단 수술을 감행할 것입니다. 바로 우리는 우리가 쥐고 있는 전체 데이터를 칼로 쪼개어 일부만 잘라 던져줘서 훈련 모델을 적합(fit)시키고 적응 적합을 완료 시키고, 그런 다음 녀석은 평생 한 번도 보지 못한, 우리가 몰래 장롱에 **남겨 숨겨둔 순수(held out) 찐 실전 시험 데이터**를 이놈 얼굴에 투척해 얼마나 그것을 소름 돋게 잘 맞추고 유지 예측하는지 진짜 그 본 성능 밑바닥을 냉정하게 검토 검사 검증 실험할 수 있는 모의 테스트 실험법 구축이 필수입니다.

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004.
이 분리 검증 전략을 엄수 단행 구현 수행하기 위해, 우리는 이 주식 시장 시간표 상에서 제일 먼저 2001년부터 2004년 기간 과거 훈련용 시계에 해당하는 데이터 관측치에 1:1로만 작동 판별되어 대응하는 부울(Boolean) True/False 논리 벡터 거름망을 먼저 계산하여 날조 생성 짜 맞춥니다.

We then use this vector to create a held out data set of observations from 2005.
우리는 그다음에 그 생성한 논리 기반 체계 인계선인 이 기준 벡터를 이용하여 2005년 미래 정답의 해당하는 관측치들의 순수하게 숨겨 유지된 '따로 실전 테스트용 남겨 둔(held out)' 미래 가상 데이터 세트를 분리 선별 창출 생성 모의실험 세팅 분리 도출 해 냅니다.

```python
In [14]: train = (Smarket.Year < 2005) # 2004년 이전 옛날 데이터만 True로 쾅쾅 낙인찍는 부울망 걸쇠 생성!
Smarket_train = Smarket.loc[train] # True로 찍힌 놈들만 쓸어 담아서 훈련소 캠프(train)로 직행!
Smarket_test = Smarket.loc[~train] # 이건 반대! 물결표(~) 기호로 2005년 미래 관측치만 싹 쓸어 담아서 지옥의 시험장(test)으로 격리 이송!
Smarket_test.shape
```

# **`Out[14]:`** `(252, 9)` 

The object `train` is a boolean array, since its elements are `True` and `False`.
저 방금 코드에서 지정 생성한 통계 객체 `train` 이란 놈은, 그 거름망 배열 안의 구성 요소들이 온통 1과 0 인 `True` 와 `False` 데이터들로만 도배되어 있기 때문에, 이 녀석의 정체는 파이썬에서 흔히 쓰는 부울 배열(boolean array) 체계형 그물망 자료형입니다.

Therefore, `Smarket.loc[~train]` yields a subset of the rows of the data frame of the stock market data containing only the observations for which `train` is `False`.
따라서, 그물을 반대로 뒤집어 연산한 코드 연산된 결과물인 `Smarket.loc[~train]` 은 논리 분류 기준 거름망 `train` 에서 탈락해 `False` 낙인이 찍힌, 즉 2005년 이후에 터진 그 최신 미래 테스트 관측치들만을 따로 알뜰하게 추출해 모아 포함 구축하는 오리지널 주식 시장 데이터 프레임의 분리 파편적인 해당 행 부분 집합(subset) 행 그룹 단위 객체 들을 최종적으로 산출 생산 출산 분리 시켜 냅니다.

The output above indicates that there are 252 such observations.
위에 표기된 산출 결과의 스펙 출력물 지표 값은 파편 이 이러한 분리되어 추출 도출된 2005년 실전 테스트 관측치들이 총 252개라는 방대한 양으로 존재 유지 발현함을 여지없이 나타냅니다 수치 보여 줍니다.

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005.
우리는 이제 실전 시험 준비 돌입! 오직 이 모든 데이터 속에서 정답 시험지를 버리고 2005년 **전 과거 날짜** 시간표에 정확히 해당하는 자료 관측치들의 이 훈련용 파편 부분 집합(subset) 지식 만을 기계 뇌 속에 주입 사용 장전하여 로지스틱 회귀 기계 모형을 시험 스파링 훈련 적합을 강제로 무자비하게 뺑뺑이 시킵니다 적응 시 적합!

We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005.
그런 다음 훈련이 끝난 기계 놈을 끌고 와서 우리는 우리의 지옥의 시험 검정 세팅 세트(test set) — 즉, 얘가 한 번도 본 적 없는 **미래 2005년의 일자 날짜**— 의 각 시계열 시간 날 요일 날에 대한 관측 단서를 주고 주식 시장이 지표가 오를 예측 상향 확률값 예언값 들을 최종 마지막으로 확보 수집 산출해 시험장 테스트 결과물 판별 획득해 내어 결과를 얻어 빼냅니다!

```python
In [15]: X_train, X_test = X.loc[train], X.loc[~train] # 탄환(X)들도 과거 훈련/미래 정답으로 쪼개기
y_train, y_test = y.loc[train], y.loc[~train] # 과녁(y)들도 훈련/미래 실전용으로 쪼개버리기!
glm_train = sm.GLM(y_train,
                   X_train,
                   family=sm.families.Binomial()) # 로지스틱 기동!
results = glm_train.fit() # 이번엔 모든 데이터가 아니라 'X_train(과거)' 만 던져줘서 스파링 훈련 돌림!!!
probs = results.predict(exog=X_test) # 스파링 끝난 기계한테 'X_test(미래의 2005년 데이터)' 를 던져서 실전 시험 평가 사격 발동 도출!!
```

Notice that we have trained and tested our model on two completely separate data sets: training was performed using only the dates before 2005, and testing was performed using only the dates in 2005.
우리가 이 시점에서 조립에서 절대 망각하지 말고 명확히 필히 주목해야만 할 경악스런 차이점 하나는 우리가 지금 우리가 기른 로지스틱 예측 모델을 완전히 물과 기름처럼 서로 분열되고 독립적으로 나뉘어 교집합 분리된 두 개의 개별 독집 분리 데이터 세트들 상에서 모델을 각각 격리하여 훈련(trained)시키고 그것을 분리 실전 테스트(tested)했다는 매우 통계적 의미가 큰 유의미한 시사적 사실 팩트 구동입니다: 모형 훈련 육성 조립은 완전히 오직 2005년도 시간표 이전의 과거 날짜 방구석 관측 자료 데이터 지식만을 토대로 통하여 사용하여 전산 구축 수행되었고, 그리고 기능 실전 시험 판별 적중률 테스트는 정반대로 얘가 눈곱만큼 도 아예 본 적도 없는 오직 온전히 2005년 시간표 내의 한정 분리 독립된 신규 날짜 관측 자료 데이터들만을 기반 무기 사용하여 도출 실험 실행 모의 판별 테스트 수행되었습니다.

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period.
마침내 수확의 대미 결말로 도래, 우리는 오만방자한 기계가 뱉은 2005년 미래 데이터의 모형 실전 테스트 예측값 타점들을 해당 지정 시간 기간 전체 구간 동안 세상에 발동 벌어진 모의 세계 예측 주식 시장 동향 장세 데이터 팩트 상황판의 실제 진짜 황금 답안지 정답 움직임 팩트 변동 지표들과 수치적으로 결합 융합 비교 심문 채점을 실행 돌입합니다!

We will first store the test and training labels (recall `y_test` is binary).
우리는 표 산출 출력 제일 먼저 과정 으로서 지정 융합 분류 훈련용 과 그 에 상응하는 테스트 결과 오리지널 황금 비교 판별 정답 라벨들을 단편 저장 그릇에 따로 스코어 할 것입니다 (지시 변수 `y_test` 자체가 `Up/Down` 두 종류 값인 이진 데이터 산출물(binary)임 속성 이었다는 사실을 환기 구조적 회상하십시오).

```python
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train]
```

Now we threshold the fitted probability at 50% to form our predicted labels.
이제 우리는 우리의 치열했던 실전 훈련 파편 완성된 예측 라벨 결과물을 정답 채점지에 쓸 수 있는 언어로 확립 통계 형성 조립하기 위해, 기계에서 산출 반환된 적중 적합 확률값을 앞서 했던 똑같은 방식인 50%를 커트라인 고정된 마지노선 흑백 임계치(threshold)로 설정 산정 절단 낙인찍습니다!

```python
In [17]: labels = np.array(['Down']*252)
labels[probs > 0.5] = 'Up'  # 확률 0.5가 넘은 시험 답안지만 Up으로 예언 강제 판별 정답 교체 처리!
confusion_table(labels, L_test) # 채점표 발동 발사!!
```

```python
Out[17]: Truth      Down  Up  (이거 정답지)
Predicted (이건 기계가 낸 시험답안지)
Down         77    97
Up           34    44
```

The test accuracy is about 48% while the error rate is about 52%.
충격적인 진짜 시험 성적! 혼동 판별 채점 폭로판이 보여주는 기계의 진짜 실전 시험 테스트 결과 판별 영광스러운 정확도 타점은 겨우 **약 48% 참담한 수준**이며, 반면 시험을 거하게 망쳐버린 역산출 오류 똥볼 오답률은 오답률 약 52% 로 오만방자하게 달합니다.

```python
In [18]: np.mean(labels == L_test), np.mean(labels != L_test)
```

```python
Out[18]: (0.4802, 0.5198)
```

The `!=` notation means _not equal to_, and so the last command computes the test set error rate.
설명 참견: 여기서 `!=` 이 기괴한 파이썬 표기 부호 표시는 **같지 않다, 즉 짝퉁 틀렸어!(not equal to)**를 직관 의미하며, 그래서 저 위 코드 블록 안의 저 마지막 명령줄 `np.mean` 판별 체계 코드는 바로 기계가 틀려버린 오답 횟수의 평균, 즉 시험 오류 테스트 세트 오차 오답률 을 단숨 파악 집계 산출 도출 평균 연산 계산합니다!

The results are rather disappointing: the test error rate is 52%, which is worse than random guessing!
이 테스트 산출 획득 결과들은 그야말로 오히려 꽤 눈물이 날 만큼 실망스럽습니다(disappointing): 치열하게 쪼개서 계산된 실전 지옥의 테스트 오답 오류율이 52% 절반을 초과해 버리는데, 이 끔찍한 오답 조작 수치는 차라리 머리 비우고 눈 감고 아무렇게나 단순히 두꺼비집 동전 던지기의 **원숭이 무작위 찍기 추측(random guessing)으로 나오는 아주 원초적인 동전 확률 50% 우연 도박 결과값보다 조차도 수치상 그 뻘쭘 확률 성능이 통계 파악 도출 결과 상 무참히 더 나쁩니다 등신(worse)!** 쓰레기라는 뜻이죠!

Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days’ returns to predict future market performance.
물론 통계 현실 상식 도박판 주식의 세계가 늘 그렇듯, 만약 특정 도박꾼 개인이 무모하게 단순히 차트의 흘러 지나간 거품 과거나 어제 전날들의 일일 증시 과거 상승 하락 변동 수익률 수치만을 모조리 집어다 긁어모아 전적으로 모조리 무기 인양 의존 사용해서 이 지독하고 도무지 변덕스럽고 파악 불가 예측 엇나가는 변덕쟁이 한 치 앞도 분간 모를 미래의 복잡한 요물 주식 시장 짐승 변동 차트 미래 수익 변동 성과를 마스터하여 단번에 얌전하게 콕 도출 예측해 낼 수 있을 것이라고 도저히 대개 기대하진 상상도 기만조차 안 할 것이라는 상식을 합당하게 고려 전제해 보면, এই 무참하게 짓밟혀 산산이 부서진 데이터 실패의 처참한 깡통 결과가 그리 크게 다 모두 충격적이거나 소름 돋게 전례 없이 유별나게 놀라운 대참사 수준 결과 통계는 결코 아닙니다.

(After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)
(결국 까놓고 따져보면 상식적으로 만약 진짜로 그런 타임머신 어긋난 도박 부자 행위들이 데이터 쪼가리 함수 코딩 따위 나부랭이로 실제로 백발백중 가능하게 세상만사 존재했다면, 빌어먹을 이 똑똑하신 척 대단한 통계학 교재의 저술 나부랭이 저작 교수 저자 양반들은 이런 답답하고 구질구질한 연구실 방구석에서 지루한 이딴 통계학 교재나 기술 종이나 타이핑 작성 집필하고 앉아 있기보다는, 그 시간에 진즉에 이미 컴퓨터 기동 프로그램 조작해서 밖 길거리 금융 월가 증권가에 나아가 주식 도박 코인 장판에서 조 단위로 쓸어 담아 큰돈을 벌고 요트 타며 떼돈을 번 무적의 졸부 벼락 대박 억만장자 부자(striking it rich)가 편하게 되어있었을 것입니다. 현실이 말해주죠.)

We recall that the logistic regression model had very underwhelming _p_-values associated with all of the predictors.
우리는 여기서 이 처참한 실패 결과 패인을 따져보며, 아까 앞 단원 표에서 이 야심 차게 산출된 로지스틱 회귀 모델 기판이 그 내부 부품 예측 투입 후보 변수들 목록 모두와 지지고 볶고 통찰력 연계 없이 너무나도 단순히 허접하게 엮여서 거의 쓰레기 급의 아주 초라하고 나약한 한심한 수준치(underwhelming)의 낮은 의미 없는 바닥 치는 확률 신뢰도 _p_-값 도출 데이터 점수 통계 조각들을 안타깝게 우글우글 가졌었다는 처참한 첫 오류 팩트 훈련 조립 부품 하자 사실을 슬프고 씁쓸하게 다시 복기하여 환기 떠올립니다(recall).

Using predictors that have no relationship with the response tends to cause a deterioration in the test error rate, and so removing such predictors may in turn yield an improvement.
통계 예측 모델 엔진 기판 회로 설계 조립 과정 속에서 정작 자기가 타격해야 할 타깃 과녁 응답 방향 목표 반응 도출 지표 움직임 모형 방향 계산 과정과 유의미한 아무런 연관 끈 연계성 논리도, 아예 하등 수학적 의미 관계도 아예 존재하지 않는 노이즈 쓰레기 불량 맹탕 데이터 예측 부품 변수들을 버젓이 구동 주입 연료 재료로 억지로 구겨 끼워 넣고 사용하는 헛된 강행 무지성 훈련 주입 행위 작동 체계는 곧 결과적으로 기계 자체의 전체 테스트 오차율 분석 결과 조립 점수의 심각한 총체적 질적인 붕괴 오염 타락 기능 지표 하락 악화 맹종 오차 붕괴(deterioration) 치명 결함을 가중 심각하게 유발 야기 확장 초래하는 고질적 최악 나쁜 주요 악영향 질환 원인이 되며 증폭시킵니다. 따라서 이런 고물 논리에 따라 역발상 지표로 그러한 뇌동매매 무관 연계 불필요한 독성 쓰레기 불량 잡음 노이즈 교란 오염 과잉 예측 부품 파편 변수 덩어리들을 기판에서 싹 다 뽑아버려 추출 단절 제거하면 차례적으로 이번엔 오히려 기계 본연 결괏값의 불량이 도리어 상쇄 반대로 덜어지며 결과 회로 점수들의 득점 지표 성능 항샹 이라는 타점 전폭적 향상 진보(improvement) 스탯 상승 기적을 재점화 긍정 역 도출 개선 산출해 낼 수도 있는 법입니다.

Below we refit the logistic regression using just `Lag1` and `Lag2`, which seemed to have the highest predictive power in the original model.
아래에서 우리는 아까 보았던 저 절망의 파편 본래 오리지널 무기 기본 모델 그 불량 부품 무더기 성적표 안에서 그나마 유일하게 썩은 무더기 속에서 상대적으로 가장 타당한 그나마 눈곱만큼 나은 스코어, 즉 가장 지대한 독보적 기여도의 높은 기능 연산 정밀 생존 타격 예측력 잠재성(predictive power)을 작게나마 가진 예측 최고 득점 유망주 지표인 것으로 간주 분석 추정 보였던 `Lag1` 그리고 `Lag2` 딱 요 2개 부품 알짜 지표들 조각 소스 단서 데이터 파편 기판 만을 알뜰하게 조합 단독 엄선 모의 사용하여 전면 재편 축소 분리 모델링으로 다시 한번 로지스틱 회귀 로켓 엔진을 대대적 축소 조립 재점화 다지기 재적합 구동(refit) 할 것입니다.

```python
In [19]: model = MS(['Lag1', 'Lag2']).fit(Smarket) # 쓰레기 힌트 싹 버리고 제일 그나마 똑똑한 Lag1, Lag2 두 놈만 도면에 장착!
X = model.transform(Smarket) 
X_train, X_test = X.loc[train], X.loc[~train] # 똑같이 훈련용, 시험용으로 쪼개고
glm_train = sm.GLM(y_train,
                   X_train,
                   family=sm.families.Binomial())
results = glm_train.fit() # 가벼워진 몸집으로 다시 뺑뺑이 재훈련 적중 발진!!
probs = results.predict(exog=X_test) # 미래 시험지로 재평가 타격!!
labels = np.array(['Down']*252)
labels[probs > 0.5] = 'Up'
confusion_table(labels, L_test) # 성적 폭로판 재발동! 두구두구!
```

```python
Out[19]: Truth      Down  Up  (정답)
Predicted (두 개의 부품으로 다시 치른 시험답안지 기계 예측)
Down         35    35
Up           76   106
```

Let’s evaluate the overall accuracy as well as the accuracy within the days when logistic regression predicts an increase.
과연 잡다한 쓰레기를 버리고 날렵해진 우리 기계의 성적은 어떨까요? 우리가 얻은 재시험 전체 결과 데이터상의 전반적 전체 총칭 포괄 적중 명중 판별 정확도(overall accuracy), 그리고 한 걸음 더 나아가 좀 더 깊이 로지스틱 회귀 모형 기계가 꽤 독단 단독적으로 확신에 차 오직 주식 시장 자체 차트의 폭발적 기상 상승(increase) 징후 만을 찍어 상승 타점 예측한 콕 집은 발생 날짜 기간 일수 내에서의 오직 그 기간만의 부분 특화 분리 독립 상승 국소 단위 적중률 예측 특수 특정 정확도 수치를 명확히 함께 모두 동시에 수치 계산 산술 평가 검증 전개 도출해 봅시다.

```python
In [20]: (35+106)/252, 106/(106+76) # (대각선 합 / 전체 시험 문제 수) = 전체 정확도, (Up 찍어서 진짜 Up 맞춘 수 / 기계가 Up이라고 찍은 총수) = 분리 상승 전용 정확도
```

```python
Out[20]: (0.5595, 0.5824)
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted.
이제 테스트 재도전 산출 결과 데이터 수치가 이전에 깡통 차던 48% 악몽에 비해서는 약간 극적인 기사회생 갱생 아주 조금 다소 꽤나 나아 호전 개선된 도출 양상 인스피레이션 스코어 진단 향상으로 보입니다: 전체 기동 총망라 분석 산술 일별 하루하루 주식 시장 변동 일일 오르락내리락 파동 움직임 방향 전개 방향성의 평균 대략 절반을 훌쩍 넘는 약 56% 체계 생존 확률 전조 확률이 요번엔 거짓 상실 오류 헛발질 없이 아주 기특하게 판정 도출 올바르게 무사히 안착 예측 도달 확인 증명되었습니다.

Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach.
분석의 총괄 종합 전산망 수치상 (전체 모형의 치명타 오차율 점수 지표 파악 측면에서 구조 파악) 덜어내 볼 때, 이 쓰레기를 치운 날렵한 로지스틱 회귀 회로 방법 기법의 단일 기계 모델의 종합 산출 판정 성능 승률 베팅 성공 도출 확률은 극단적으로 표현하면 원숭이가 동전 굴려 찍는 원시적 본능 무지성 단순 나이브(naive) 무도 맹신 돌격 맹목 도박 접근법 확률인 50 찍기 모의 추측 확률 스코어 시스템 판별 무구 보다는 통계적으로 계산해 보면 지표상 여전히 그다지 썩 판도를 뒤집게 가시적으로 우월 대단히 월등 나아 초월해 이기고 우승해 보이는 혁신적 큰 무결성 스텝 도달 신뢰 등급업 성능 압살의 거대한 진보 진척 수준 격차 혁신 차이는 아닙니다. 그냥 약간 더 운이 좋았다 정도.

However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate.
그럼에도 불구하고 이 표의 특이상황 기이 지표, 즉 혼동 행렬 결괏값 폭로 도표의 세부 분석 체계가 여실히 극명 보여주듯이 맹점 발견 포인트는, 오직 로지스틱 시스템 두뇌 기계 회로 파악 모형이 아주 기계적으로 확고하게 해당 특정 당일 주식 요주의 판세 시장 도박장의 극적인 국지적 한정 변동 장세인 '상승 곡선 화살표(increase)' 반발 지표 단일 방향만을 콕 하나로 단일 특정 집어 상승 예측을 특정 상황 발동해 베팅 찍어낸 아주 특이 특정 상황 발동 환경의 도출 구역 지정 요일 특정 날짜 제한(days) 들 내에서 만큼 이란 특정 전제 조건 한에서는, 이 로켓 로지스틱 회귀 모의 모형은 절반의 동전 치기를 가뿐히 비웃으며 극적으로 약 무려 대략 대거 58% 신들린 수준의 특권 국지 상승 예측 적중 신뢰 확률 단일 정확도 타점 달성 승률 비율 달성 수치 우월 도달 성적 점수를 신묘하게도 달성 구축 기록해 발휘 방출하여 우리에게 그 위력 지문을 놀랍게도 부분 보여줍니다.

This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted.
이 기계 분석 극적 발견 국소 데이터 수치 기반 도출 시사 지표는, 영악한 트레이더에게 만약 어떤 매매 운용 주체 대상이 이 특정 모형 장세가 예측 모델 통계 예측 점쟁이 로봇이 상향 불기둥(increasing market) 시장 예측 발동 환경 조건을 시그널 알릴 시 강력 발생 타점 특정 발동 날들에만 용감하게 맹신하여 시장 해당 주식 재고 현물 보유 자산 종목 몰빵 재산을 풀배수 풀매수 진입(buying) 하여 과감히 오름차순 도박 배팅을 긁어먹고! 그리고 그 외 그 반작용 파멸 우려 이면 반대로 하향 하락 곡선 붕괴 수치 짐작 떨어질 시그널 절망의 하락 늪이 도출 예상 예측 특정 징후 발현 장이 예상 세팅되는 우울 폭격 무너지는 파멸 단층의 모든 하락 예측 기동 오류 날들에는 미련 없이 패를 던지고 모조리 매매 접근 회피하여 아무것도 안 하고 놀면서 현금 관전 자재 보류 관망 쉼 포지션만 영리하게 안전 도피 지대 유지 관망 영위하는 (avoiding trades) 특정 기계 시그널 의존 기반 얌체 매매 베팅 규칙 스탑 투기 거래 타점 공략 전략(trading strategy) 형성 시스템 창출 모의 전술 기동 기능 발동 확정 성립 아이디어 기초 지식 실현 이득 가능성 수익 전략 성립 신봉 구사 단서 승률 배팅 가능성을 꽤 솔깃하게 확실하고 치명적으로 긍정 시사 이면 지시 가능성 확률 파편을 아주 은밀히 뒷받침 무언적 제공 공조 도출 제시합니다.

Suppose that we want to predict the returns associated with particular values of `Lag1` and `Lag2`.
마지막 유희. 한번 더 상상을 확장 가정하여, 만약 우리가 애초에 특정한 지표 수치 단서인 이 짱짱한 예측 부품 `Lag1` 과 그리고 `Lag2` 두 시계열 무적 무기 단서 값들과 끈끈히 역학 연결되어 파생하는 관련된 특정 결과 후행 목표 방향 지표 확률 상승 수익률 변환(returns) 단절 의 특정 목표 모의 계산 파악 산출 결과를 강제로 예측 렌더링 주입 모델 입력 조작하여 내가 원하는 파편 값에 해당하는 그 수치를 최종 도출해 알아내고 싶다고 억지 지정 꼬집어 상상 세팅 상정 기만 가정해 봅시다.

We want to predict `Direction` on a day when `Lag1` and `Lag2` equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8.
우리는 두 가지 날을 상상합니다. 하나는 최근 목표 선행 단서 변수 `Lag1` 과 이어서 `Lag2` 값 지표 점수 기판이 차례대로 순차 쌍을 이뤄 각각 따로따로 동일하게 특수 쌍 구조로 강제 수치 산술 1.2 상승 스탯 그리고 이어서 연속 1.1 결괏값 계수 스탯과 완전 대응 매치 매칭하는 동일 기상 부합하는 특정 조작 일자의 한 개의 날(장세)과, 두 번째 세팅으로 동일 작동 조건의 완전히 반대 구성 조합 쌍 배틀 점수 지표로서 각각 단서 배열이 산술 수식 1.5 지표 단기 고 상승폭 결괏값 상승 기록 과 그 뒤를 이어 하루 지나 무참히 뒤통수 꺾인 무너지는 대칭 -0.8 떡락 단절 점수 결과 단절 붕괴 점수 판 판락과 완벽 동일하게 짝패를 이뤄 완전 동일 세트 일치 하강 부합 일치 연속 작용 작동 조건하는 또 다른 두 번째 발동 발생 가정 특수 모의 관전 상상 날짜 데이터 시험 요건을 모델에 임의 지표 강제 지시 주입 쑤셔 넣어 지정 대치 인계 입력 강요 설정하여, 그 조작된 상황 모의 속 가상의 반응 판결 결과 판도 모형 주가 상승 장세 `Direction` 이 미친 듯 상승할지 도적 파멸 하락할지 도출 발현 여부를 기계 고유 논리적으로 판독하여 판별 억지 강제 예측 확률 지시 명령 발동 기동 확인해 그 값을 토해 얻어 뽑아내고 싶습니다.

We do this using the `predict()` function.
우리는 아주 간단하게 통계 모델 기계의 본질 내부 로켓 구조 스위치 트리거 인 파이썬 머신 러닝 `predict()` 단조 강력 추론 반환 함수 구문 발사 수식 을 그대로 발사 도달 스위치 온 활용 호출 사용 조작하여 이 강요 무적 모의 단타 계산 목적 판결 타점 목표 변수 투입 산술 연산 예측 판별 사격 결과치 추출을 최종 반박 불가 강제 강압 도출 지표 추출 작동 계산 명령 수행 계산 강행 도출 완수 성과 강행 처리 수행 마감 짓습니다.

```python
In [21]: newdata = pd.DataFrame({'Lag1':[1.2, 1.5],
'Lag2':[1.1, -0.8]}); # 내가 만든 내 멋대로 억지 가짜 상상 주가 날짜 2개 만들기
newX = model.transform(newdata) 
results.predict(newX) # 기계야, 이 상상의 날에 주식이 오를 확률은 몇이냐?! 발사!
```

```python
Out[21]:
0    0.4791 # 첫 번째 날은 47% 확률로 오르네요. (떡락각!)
1    0.4961 # 두 번째 날은 49% 확률로 오르네요. (이것도 떡락각!)
dtype: float64
```

---

## Sub-Chapters

[< 4.7.2 Logistic Regression](../index.html) | [4.7.3 Linear Discriminant Analysis >](../../4_7_3_linear_discriminant_analysis/trans2.html)

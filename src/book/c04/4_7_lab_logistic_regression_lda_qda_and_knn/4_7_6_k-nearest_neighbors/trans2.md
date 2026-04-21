---
layout: default
title: "trans2"
---

[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/trans2.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.6 K-Nearest Neighbors
# 4.7.6 K-최근접 이웃 (KNN): 묻지 마 다수결, 내 주변 놈들이 내 운명!

We will now perform KNN using the `KNeighborsClassifier()` function. This function works similarly to the other model-fitting functions that we have encountered thus far. 
드디어 소문만 무성했던 깡패 알고리즘, 내 주변 이웃들의 쪽수로 내 운명을 결정짓는 무지성 다수결 머신 **K-최근접 이웃(KNN)** 을 돌려볼 시간입니다! 파이썬 소환 마법진 이름은 `KNeighborsClassifier()` 인데요, 이거 구동하는 맛은 지금까지 우리가 지겹게 마르고 닳도록 맛본 타 분류기 로봇들의 스위치 조작법과 소름 돋게 똑같습니다. 

As is the case for LDA and QDA, we fit the classifier using the `fit` method. New predictions are formed using the `predict` method of the object returned by `fit()`. 
앞서 뛰었던 LDA나 QDA 조상님들과 마찬가집니다! 기계 배때지에 `.fit()` 먹방 주걱으로 데이터를 때려 박아 훈련시키고 나면, 그 결과물로 진화한 훈련종료 머신에게 냅다 `.predict()` 발사 방아쇠를 땡겨 미지의 미래 타겟 예측 샷을 갈겨 대는 똑같은 콤보 매커니즘이죠.

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
일단 몸풀기로 **$K=1$**, 즉 가장 가까운 이웃 딱 1명 한 놈만의 의견을 맹신하는 극단적 1인 독재 KNN을 돌려봤는데... 성적표 꼬라지가 처참합니다! 고작해야 모의고사 정답 타율이 반토막 50% 수준에 머무는 폭망 수준입니다. 뭐 당연한 결과이기도 합니다. $K=1$ 이란 극단적 세팅은 주변 잡소리에 너무 펄떡펄떡 휘둘려서 거대한 짐승의 뱃살처럼 너무 과하게 출렁거리며 데이터에 억지 끼워 맞춰지는 심각한 부작용(overly-flexible fit, 과대적합) 을 일으키기 딱 좋은 위험한 짓이거든요.

```python
In [48]: (83+43)/252, np.mean(knn1_pred == L_test)
```

```python
Out[48]: (0.5, 0.5)
```

We repeat the analysis below using $K=3$. 
그래서 정신 차리고 이웃 쪽수를 3배로 늘려, 이번엔 3명의 이웃과 다수결 투표를 붙이는 **$K=3$** 모드로 세팅을 조율해 재도전 불꽃을 튀겨보겠습니다.

```python
In [49]: knn3 = KNeighborsClassifier(n_neighbors=3)
knn3_pred = knn3.fit(X_train, L_train).predict(X_test)
np.mean(knn3_pred == L_test)
```

```python
Out[49]: 0.5317460317460317
```

The results have improved slightly. But increasing $K$ further provides no further improvements. It appears that for these data, and this train/test split, QDA gives the best results of the methods that we have examined so far. 
짜잔, 다행히 명중 타율 점수가 53.1% 로 코딱지만큼(slightly) 쥐꼬리 상향을 맛봤습니다. 하지만 안타깝게도 $K$ 쪽수를 이보다 더 펌핑해서 올려봐야 헛수고일 뿐 점수판엔 아무런 메리트 업그레이드(improvements) 가 터지지 않습니다. 결론적으로 이 구역의 막장스러운 `Smarket` 주식 데이터 판과 우리가 이번에 짜 둔 훈련/시험 분할 그라운드 배틀 세팅 안에서는, 지금까지 달려본 선수들 중 **이차 곡선 뱀파이어 QDA 머신 녀석이 뱉은 성적표가 제일 우주 최고 스코어 갑(best results)** 이었던 것으로 판명 납니다.

KNN does not perform well on the `Smarket` data, but it often does provide impressive results. As an example we will apply the KNN approach to the `Caravan` data set, which is part of the `ISLP` library. This data set includes 85 predictors that measure demographic characteristics for 5,822 individuals. The response variable is `Purchase`, which indicates whether or not a given individual purchases a caravan insurance policy. In this data set, only 6% of people purchased caravan insurance. 
이 주식판 데이터에서 삽질했다고 KNN 녀석을 개무시하지 마십시오! KNN은 종종 소름 돋게 멱살 잡는 꿀 성적표를 뿜어내기도 합니다. 그 증거를 체감하기 위해 그 무대를 확 바꿔서, 이번엔 `ISLP` 무기고 서랍 구석에 잠들어있던 **`Caravan` (캐러밴 보험 구매)** 데이터 사냥터로 KNN 용병을 파견시켜 볼 겁니다. 이 소름 끼치는 신규 데이터 속엔 5,822명의 인간들 신상 정보를 탈탈 턴 인구통계학적 스펙(나이, 수입 등등 무려 85개짜리 힌트 조각) 들이 도배되어 있습니다. 우리가 최종 저격해 맞출 정답 타겟(반응 변수) 은 과연 이 호갱이 '캐러밴 캠핑카 보험' 에 돈을 꼴아박고 샀(Purchase) 느냐 마느냐를 나타내는데, 사실 이 시장은 졸라 협소해서 전체 호갱 타기팅 중 **꼴랑 6% 인간들만 지갑을 열고 보험을 산** 극악 무도 불균형 사막 데이터입니다.

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
자 결승선 타겟인 통장 결제 여부 `Purchase` 딱지표 기둥만 쏙 도려내 빼놓은 나머지 모든 스펙 기둥들을 우리 공격용 힌트 총알(features) 로 장전합시다.

```python
In [52]: feature_df = Caravan.drop(columns=['Purchase'])
```

Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. 
주의 집중!! 극강의 경고 타임입니다! KNN 녀석은 눈 뜬 장님처럼 철저히 공간상의 "거리(distance)" 하나만 맹신하며 자신과 가장 찰싹 달라붙어 가까운 이웃 놈들의 신분을 베껴 예측하는 무지성 카피캣입니다. **그러므로 예측 변수들이 갖는 숫자 크기 덩치표(스케일 scale) 가 목숨줄처럼 중요(matters) 해집니다!** (예를 들어 '연봉 5000만 원' 과 '나이 30살' 은 숫자 스케일 덩치 차이가 넘사벽이라서, KNN 공간에선 연봉 변수가 거리를 다 씹어먹고 군림해 버립니다!)

A good way to handle this problem is to _standardize_ the data so that all variables are given a mean of zero and a standard deviation of one. Then all variables will be on a comparable scale. This is accomplished using the `StandardScaler()` transformation. 
이 막장 스케일 격차 사태를 해결할 사이다 같은 비법은, 85개 잡동사니 모든 스펙 변수에 강제로 다이어트와 성형을 감행해 **'평균은 무조건 한가운데 0, 흩어진 널뛰기 폭빵 표준편차는 무조건 공평하게 1' 로 맞춰 버리는 표준화(standardize) 마력의 평탄화 스킬**을 먹이는 겁니다. 그러면 연봉이든 나이든 전부 다 평등하고 쫄깃하게 비빌 수 있는 수준급(comparable scale) 도토리 키 재기로 억지 변환 개조됩니다. 이때 쓰는 마법의 파이썬 마술봉이 바로 거친 야생마도 순한 양으로 갈아 넣는 `StandardScaler()` 규격화 변환기입니다!

```python
In [53]: scaler = StandardScaler(with_mean=True,
                                 with_std=True,
                                 copy=True)
scaler.fit(feature_df)
X_std = scaler.transform(feature_df)
```

Now every column of `feature_std` below has a standard deviation of one and a mean of zero. 
짜잔! 파이썬 코딩 분쇄기를 거쳐 탄생한 이 새로 깔끔해진 `feature_std` 판때기의 모든 기둥 라인 숫자들은 완벽 공산품처럼 찍혀서, 오차 널뛰기 1, 중앙 스코어 0이란 평등한 스펙으로 무장 탈바꿈했습니다! 

```python
In [56]: (X_train, X_test, y_train, y_test) = train_test_split(X_std, Purchase, test_size=1000, random_state=0)
```

We fit a KNN model on the training data using $K=1$, and evaluate its performance on the test data. 
우린 다시 이 갓 빚어낸 순수 평화 통일 스케일 훈련 데이터를 갈아 넣고, 미친 독불장군 이웃 **$K=1$** 짜리 KNN 모델을 세팅(피팅) 해 뒷주머니 타겟 테스트 데이터에다 냅다 모의고사 스코어를 채점(evaluate) 저격해 보았습니다.

```python
In [57]: knn1 = KNeighborsClassifier(n_neighbors=1)
knn1_pred = knn1.fit(X_train, y_train).predict(X_test)
np.mean(y_test != knn1_pred), np.mean(y_test != "No")
```

```python
Out[57]: (0.111, 0.067)
```

It turns out that KNN with $K=1$ does far better than random guessing among the customers that are predicted to buy insurance. Among 62 such customers, 9, or 14.5%, actually do purchase insurance. This is double the rate that one would obtain from random guessing. 
오 마이 갓, 결과창 까보니 신박한 비밀이 하나 까발려집니다! 모델 녀석이 "이 호갱님들은 백퍼 보험 삽니다!" 라고 점을 찍은 타겟 고객 명단을 까보니 조잡한 무지성 찍기(random guessing) 에 비해 그 성취율이 미치도록 월등해진 쾌거(far better) 가 터집니다! 이 KNN 녀석이 작두 타며 픽한 구매 예측 예정 고객 62마리 중에서, 무려 9명(비율로 치면 **14.5%**) 의 인간들이 지갑을 열고 실전에서 진짜로 보험을 사 주었습니다! 이건 애초에 전체 데이터 구매 지분 눈감고 찍었을 때 터질 확률(겨우 6%) 에 비하면 무배에 떡상하는 놀라운 마법과 같은 타격 효율의 대혁명입니다!

```python
In [59]: 9 / (53 + 9)
```

```python
Out[59]: 0.14516129032258066
```

---

## Sub-Chapters

[< 4.7.5 Naive Bayes](../4_7_5_naive_bayes/trans2.html) | [4.7.7 Linear And Poisson Regression On The Bikeshare Data >](../4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/trans2.html)

---
layout: default
title: "trans2"
---

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans2.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.7 Linear and Poisson Regression on the Bikeshare Data
# 4.7.7 자전거 대여 데이터: 선형 회귀와 푸아송 회귀의 쌍끌이 출격!

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6. The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012. 
자, 지루했던 분류(떡상/떡락) 게임은 여기서 리셋! 우린 파트 4.6 챕터에서 영혼까지 털렸던 그 문제의 **`Bikeshare` 자전거 대여량** 데이터 배틀장으로 다시 뛰어듭니다. 이번엔 밋밋하게 선형 회귀를 돌려보고, 그다음 푸아송 회귀 콤보까지 더블로 피팅을 갈길 겁니다. 여기서 우리의 타깃 과녁(반응 변수 `bikers`) 은 2010~2012년 동안 워싱턴 DC 길바닥에서 1시간마다 빌려간 자전거 대여 '명수(카운트 숫자)' 입니다.

```python
In [64]: Bike = load_data('Bikeshare')
```

Let’s have a peek at the dimensions and names of the variables in this dataframe. 
일단 이 자전거 데이터프레임 덩치가 얼마나 살벌한지, 안에 어떤 장비품(변수 이름) 들이 숨겨져 있는지 살짝 엿보고(peek) 스캐닝해 보시죠.

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
선형 회귀 (Linear Regression): 일직선 무지성 막대기 꽂기!

We begin by fitting a linear regression model to the data. 
시작은 클래식하게! 데이터의 속살에다 무식한 1차원 직선 막대기를 꽂아 피팅하는 **선형 회귀(Linear Regression)** 로 몸을 풉니다.

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
출력된 요약표를 보면, 시간(`hr`) 꼬리표가 무려 24단계나 되고 전체 행이 40개나 돼서 너무 길어 뒷부분을 칼같이 잘라버렸(truncated) 습니다. 여기서 `M_lm` 모델의 영악한 속셈을 파헤쳐 보죠! 이 녀석은 첫 번째 떨거지 단계인 '자정 시간(`hr[0]`)' 과 '1월달(`mnth[Jan]`)' 을 아무 의미 없는 0짜리 투명인간 **'기준 바닥점(baseline)'** 으로 뭉개버립니다. 그래서 표를 눈을 씻고 찾아봐도 1월이나 자정에 대한 폭발력(계수 추정치) 스코어는 안 보입니다. 암묵적으로(implicitly) 얘네는 0점 처리된 거고, 나머지 다른 달과 시간들은 전부 **"이 기준점(1월/자정) 에 비해서 얼마나 더 대박 났냐?"** 라는 식의 오름차순/내림차순 차액 스코어로 측정된 겁니다. 
예를 들어 볼까요? 2월 달력(`mnth[Feb]`) 녀석의 파워 스코어가 $6.845$ 죠? 이 말인즉슨, 다른 날씨나 온도 조건이 다 똑같이 묶여 세팅장(constant) 되어 있다면, 최소한 2월 달이 1월(기준점) 대비 평균적으로 매시간 대략 7명(반올림) 의 호갱 자전거 라이더를 더 끌어모아 태웠다는 아주 직관적(signifies) 팩트입니다. 같은 논리로 3월은 1월 대비 평균 16.5명의 자전거 피플이 불어난 거죠.

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth`, as follows: 
근데 기억나십니까? 저 과거 Section 4.6.1 에선 `hr` 랑 `mnth` 를 파이썬 회로에 구겨 넣을 때 지금과는 미묘하게 다른 변태적인 코딩 꼼수 인코딩(coding) 세팅을 걸었었죠! 바로 아래처럼 말입니다:

```python
In [67]: hr_encode = contrast('hr', 'sum')
mnth_encode = contrast('mnth', 'sum')
```

Refitting again: 
이 변태 코딩을 우겨넣어 다시 한번 매운맛 피팅 리트라이(Refitting)!

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

What is the difference between the two codings? In `M2_lm`, a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth`. Importantly, in `M2_lm`, the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels. Similarly, in `M2_lm`, the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels. This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can be interpreted as the difference from the mean level. For example, the coefficient for January of $-46.087$ indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average. 
아니 대체 뭐가 다른 건가요 팩트 폭격 갑니다! 두 번째 도구인 `M2_lm` 결과판에선, 아까 1번 타자 1월(`Jan`) 이 투명인간 0점 취급 된 거랑 정 반대로, 이번엔 맨 마지막 찌꺼기 꼬리칸인 밤 11시(`hr 23`) 와 12월(`Dec`) 녀석들의 스코어만 쏙 빠져있습니다. 근데 진짜 개호러 반전 포인트(Importantly)는! 이 빠진 12월 녀석의 파워 스코어가 아까처럼 만만한 '0점 처리' 가 절대 절대 아니라는 겁니다! 이 녀석의 진짜 숨겨진 점수 채점 룰은 **"나머지 11개월 오합지졸 형제들의 파워 점수를 모조리 싸그리 다 더한 뒤, 거기다 자비 없이 마이너스(negative) 쇠고랑 거울 부호를 강제로 때려 박은 값"** 이 되어버립니다. `hr` 시간 대의 마지막 밤 11시 녀석도 다른 시간 조무래기 형제 스코어를 다 더한 값에 마이너스 부호를 폭격 맞은 처지죠.
이 변태 룰의 결론이 뭘까요? `M2_lm` 방 안의 `hr` 24개 조각 점수와 `mnth` 12개 조각 점수를 싹 다 끌어모아 덧셈을 갈기면 1원도 안 남고 **100% 무조건 "0" 으로 폭파 상쇄 수렴(sum to zero)** 되어 버립니다! 그렇기 때문에 이런 코딩 환경에서 뱉어진 각 달의 스코어는 "1월 기준점 대비 대비 차액" 따위가 아니라, 아예 **"1년 전체 평타(평균 수준 mean level) 랑 맞짱 떴을 때 얘는 얼마나 혼자 돌출/하강했냐?"** 라는 '평균 중심 폭격 해석' 기법으로 찰지게 재해석(interpreted) 됩니다.
예를 꽂아보죠! 1월(`Jan`) 스펙에 박힌 눈물의 마이너스 $-46.087$ 숫자는 무슨 뜻일까요? 다른 변수들을 다 자물쇠로 잠가 평등하게 세팅할 때, 빌어먹게 추운 1월은 **1년 평균 자전거 대여 평타 실적 궤도 대비, 일반적으로 약 46명의 라이더가 덜렁 증발하고 팍 줄어 꺾이는 폭망 비수기 달**이라는 처절한 현실을 적나라하게 대변(indicates) 하는 아주 날카로운 스코어입니다.

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used. For example, we see that the predictions from the linear model are the same regardless of coding: 
자 여기서 현탐 시간! "아 짜증나 복잡해! 1번 세팅 써 2번 세팅 써?!" 하고 분노하신다면, **"어떤 코딩 세팅을 후려 패 쓰든 내 맘이지만, 결국 당신이 그 튀어나온 숫자 결괏값의 의미 본질(기준점 중심이냐 평균 타격 중심이냐) 만 헷갈리지 않고 정확히 뇌 속에서 번역(interpret) 해 내기만 한다면 1도 상관 안 한다(does not matter)!"** 는 대서사시를 깨닫는 게 초특급 기브 앤 테이크입니다. 사실 뒤에서 벌어지는 미래 예측 게임에선 아무 짝에 쓸모없는 논란입니다. 아래 코드 검증을 보면, 어떤 미친 코딩 옷을 입혔든 결국 선형 모델이 내놓는 "그래서 내일 몇 명 탄다고?" 란 최종 예측 결과치 꼬라지는 수천 년이 지나도(regardless) 그 나물에 그 밥인 100% 거울 속 도플갱어급 판박이(the same) 결과라는 걸 속 시원히 두 눈으로 목도할 수 있으니까요!

```python
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2)
```

```python
Out[69]: 5.166710408544458e-09
```

---

## Sub-Chapters

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans2.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans2.html)

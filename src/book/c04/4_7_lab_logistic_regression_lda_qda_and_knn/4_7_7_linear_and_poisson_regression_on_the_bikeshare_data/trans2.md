---
layout: default
title: "trans2"
---

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans2.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.7 Linear and Poisson Regression on the Bikeshare Data
# 4.7.7 자전거 대박 날짜를 맞춰라! 자전거 대여 데이터 대상 선형 & 포아송 회귀 폭격

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6.
분위기를 확 바꿔서 이번엔 주식 도박판을 떠나 평화로운 자전거 대여소로 갑시다! 4.6단원에서 구구절절 이론을 풀었던 그 `Bikeshare` (자전거 공유) 데이터에다가 무식한 직선인 제일 친숙한 '선형 회귀' 기계와, 개수 세기에 특화된 '포아송 회귀' 쌍끌이 통계 모델을 모두 쑤셔 박아 돌려볼(fit) 겁니다.

The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012.
타깃 목표는 아주 명확합니다. 우리의 예측 과녁 정답지 열인 힌트 변수 `bikers`(자전거 대여 수) 열기둥엔 2010년에서 2012년 사이, 꿀 보직 워싱턴 DC에서 시간당 자전거가 몇 대나 팔려 나갔고 대여됐는지 발생 횟수(number)가 아주 적나라하게 그득그득 카운트되어 통계 측정 보존 기록(measures) 되어 있습니다.

```python
In [64]: Bike = load_data('Bikeshare') # 워싱턴 DC 자전거 장부 털어오기!
```

Let’s have a peek at the dimensions and names of the variables in this dataframe.
이 자전거 장부 데이터 프레임 덩치가 대체 얼마나 큰 지 차원 볼륨(dimensions), 또 날씨나 공휴일 같은 어떤 꿀 힌트 변수 리스트들(names)이 숨어있나 살짝 훔쳐보기 스캔(have a peek at) 분석을 해봅시다.

```python
In [65]: Bike.shape, Bike.columns # 장부 사이즈랑, 힌트 리스트 기둥 이름 다 까봐!
```

```python
Out[65]: ((8645, 15), # 8,645시간 분량의 기록! 힌트 기둥은 총 15개!
          Index(['season', 'mnth', 'day', 'hr', 'holiday', 'weekday',
                 'workingday', 'weathersit', 'temp', 'atemp', 'hum',
                 'windspeed', 'casual', 'registered', 'bikers'], # 계절, 달, 요일, 공휴일, 날씨, 기온, 습도... ㄷㄷ
                dtype='object'))
```

Linear Regression
가장 원시적인 공격: 선형 회귀 (Linear Regression) 발진

We begin by fitting a linear regression model to the data.
우선은 무식하지만 가장 직관적인 아날로그 몽둥이, **선형 회귀 기계(linear regression model)** 로 데이터를 미친 듯이 패서 훈련 적합을 강제 시키며 굴려 보는 것으로(begin by) 분석 포문을 엽니다.

```python
In [66]: X = MS(['mnth', # 월(month)
                 'hr', # 시간(hour)
                 'workingday', # 평일이냐 휴일이냐!
                 'temp', # 온도
                 'weathersit']).fit_transform(Bike) # 힌트 5개만 골라내 타깃 X로 조립 세팅!
Y = Bike['bikers'] # 과녁은 자전거 대여 수량!
M_lm = sm.OLS(Y, X).fit() # 무식한 선형 회귀 기계(OLS)로 무차별 훈련 격발!!
summarize(M_lm) # "야 기계야, 성적표 요약해서(summarize) 보고해 롸이 나우!"
```

```python
Out[66]:
```

| | `coef` (기울기 타점 득점) | `std err` | `t` | `P>|t|` (오류 확률) |
|---|---|---|---|---|
| `intercept` (시작 영점 기준) | `-68.6317` | `5.307` | `-12.932` | `0.000` |
| `mnth[Feb]` (2월 버프) | `6.8452` | `4.287` | `1.597` | `0.110` |
| `mnth[March]` (3월 버프) | `16.5514` | `4.301` | `3.848` | `0.000` |
| `mnth[April]` (4월 버프) | `41.4249` | `4.972` | `8.331` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

There are 24 levels in `hr` and 40 rows in all, so we have truncated the summary.
표를 보니 눈이 안 돌아가시나요? 시간(`hr`) 변수가 하루 24시간을 다 쪼개놨기 때문에, 레벨 항목만 총 40개가 넘어가서 다 보여주면 종이가 모자라니 중간에 확 가위로 잘라버렸(truncated) 습니다.

In `M_lm`, the first levels `hr[0]` and `mnth[Jan]` are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines.
이 무식한 `M_lm` 결과표를 읽을 때 초보가 가장 많이 당하는 함정 팩트! 잘 찾다 보면 첫 빠따 수준인 `hr[0]`(밤 12시)이나 `mnth[Jan]`(1월 쌩 겨울) 항목 점수 행 자체가 표에서 증발해 사라져 안 보일 겁니다! 기계 에러가 아닙니다! 이 첫 빠따 항목들은 뭣도 없는 기계 기준선, 이른바 디폴트 **기저 0점 세팅 영점 과녁(baseline values)** 으로 기계가 취급해 버립니다(treated). 그래서 "야 어차피 얘네 점수는 0(zero)이야 바보야!" 하고 생략해서 점수표에 표기를 안 해버리죠. 그리고 나머지 2월, 3월, 1시, 2시 등의 모든 통계 점수들은 이 '1월 자정(0점 기준선) 대비 상대적으로 플러스(+)냐 마이너스(-)냐'의 상대성 점수로만 비교 퉁쳐서 점수가 측정(measured relative to) 반영되어 뜹니다!

For example, the Feb coefficient of $6.845$ signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January.
표 보는 법 꿀팁: 예컨대 조작 투사, 표에서 `mnth[Feb]` (2월) 타점 점수가 6.845 라고 덩그러니 표기되어 있죠? 이건 날씨, 공휴일 등 일체의 딴 조건 다 그대로 똑같이 무기한 얼려두고(holding constant), 오직 달력만 딱 넘어가면, 제일 춥고 우울한 **1월(점수 0의 기준선)보다 그나마 2월에 자전거 렌트 손님이 통계 평균상 대략 7명이나 더 몰려들어 증가한다**는 기가 막힌 통계 수익 상승 버프 팩트 점수 차이를 고발 의미(signifies) 합니다!

Similarly there are about 16.5 more riders in March than in January.
똑같은 원단 논리 구조로 동일하게(Similarly) 찍어서 쭉쭉 적용해 볼까요? 봄바람 부는 3월(March) 점수 `16.55`는 뭔 뜻? 아하! 1월의 암흑기 빙하기 대비 3월에는 평균 약 16.5명의 렌탈족 라이더들이 초과 등판해서 매장에 더 나타단다는 통계상 수익 진리 파생 지표 차이의 산출이죠!

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth`, as follows:
하지만 잠깐! 옛날 저 먼 앞 단원 4.6.1 절에서 우리가 이론 공부할 때 보여준 칠판상의 결론 표는 똑같은 데이터인데 점수가 방금 본 표랑 좀 요상하게 달랐었죠? 그건 그때 쓴 코딩 데이터 조작 방식이 아까 0점 기준 잡기(더미 코딩 방법론) 같은 게 아니라 기저 데이터 세팅 값이 밑장 빼기처럼 약간 조작 이질 구조로 다르게(slightly different coding) 장난 세팅을 했기 때문입니다 다음과 같이요:

```python
In [67]: hr_encode = contrast('hr', 'sum') # "야 파이썬, 시간(hr) 변수 점수 기준 방식을 전부 다 더하면 0(sum)이 되는 희한한 코딩 방식으로 꼬아 놔라!"
mnth_encode = contrast('mnth', 'sum') # 월(mnth) 변수도 똑같이 기저 세팅을 조작해!!
```

Refitting again:
기준 룰을 조작 바꿨으니 다시 재적합해서 뺑뺑이 돌려 비교해 봅시다(Refitting again):

```python
In [68]: X2 = MS([mnth_encode, # 아까 코딩 방식 조작한 이질적 놈으로 교체!
                  hr_encode, # 얘도 교체!
                  'workingday',
                  'temp',
                  'weathersit']).fit_transform(Bike)
M2_lm = sm.OLS(Y, X2).fit() # 신상 기계(M2_lm) 발진 격발!
S2 = summarize(M2_lm)
S2 # "새 규칙 모델 성적표 나와라 뚝딱!"
```

```python
Out[68]:
```

| | `coef` (점수) | `std err` | `t` | `P>|t|` |
|---|---|---|---|---|
| `intercept` (새로운 영점 기준) | `73.5974` | `5.132` | `14.340` | `0.000` |
| `mnth[Jan]` (오, 1월이 살아 돌아왔다!) | `-46.0871` | `4.085` | `-11.281` | `0.000` |
| `mnth[Feb]` (2월 점수 폭락!?) | `-39.2419` | `3.539` | `-11.088` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

What is the difference between the two codings?
자, 두 코딩 방식 조작 구조 간의 이 기괴 파생 차이점 룰 변환(difference) 의 숨겨진 팩트 통계 진실 은 대체 본질이 뭘까요? 왜 아까는 1월이 안 보이고 2월 점수가 +6 이었는데, 이젠 1월 점수가 부활하고 2월 점수가 느닷없이 -39 막장 마이너스 도출 나락으로 폭락 표기된 걸까요?!

In `M2_lm`, a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth`.
새로운 신규 체제 모델인 `M2_lm` 결과 출력 진영 내에서는 아까하곤 반대로, 시간(`hr`)의 가장 극단 끄트머리 꼬리인 밤 11시(`23`) 와 달(`mnth`)의 꼬리표 마지막 제일 끝 레벨인 12월(`Dec`) 기둥 둘 다 딱 한 개씩만 빼고, 나머지 앞선 모든 월, 시간 레벨의 투사 계수 산점 추정치(coefficient estimate) 스탯 자체가 표면상 표에 모조리 아주 빼곡하게 확연 노출 표기 보고(reported) 됩니다!

Importantly, in `M2_lm`, the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels.
이게 진짜 중대 반전 팩트 논리입니다(Importantly)! 이 두 번째 특수 옵션 코딩 기판 `M2_lm` 룰 잣대 안에서는, 표에서 안 보이는 그 미보고 은닉된(unreported) 12월(`Dec`)의 점수가 아까 무식하게 '그냥 스탯 수치 0 처리'로 묻어버리는 게 절대(not zero) 아닙니다! 대신(instead) 아주 기가 막힌 보존의 마술 수학 연산으로, **나머지 1월부터 11월까지 보여준 모든 점수를 모조리 합산(sum) 한 수치 값에 강제로 부호 역전 변환 마이너스 음수 기호 조작(negative) 을 딱! 부착 치환 적용한 뒤집힌 파편 값**과 이 표에 없는 12월 점수가 수치상 완벽하게 일치상성(equals) 된다는 수학 기계 공식을 가집니다.

Similarly, in `M2_lm`, the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels.
마찬가지 똑같은 동일 소름 돋는 원단 로직으로(Similarly), 시간(`hr`) 계급표의 맨 마지막 안 보이는 꼬리인 23시 요금 점수 파편 할당 계수 투사 추정치는, 표에 보이는 나머지 시간 때 (0~22시) 계수 파편 결괏값 들을 죄다 끌어모은 융합 덩어리 도출 수치(sum) 의 단절 부호 반전 역 역전 음수 수치 덩어리(negative) 로 치환 도출 산입되어, 표를 안 봐도 알아서 계산하게 만들어 숨겨논 겁니다.

This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can be interpreted as the difference from the mean level.
이 미친 복잡 산단 논리 방식 조작 구조 패턴이 대체 뭐가 좋아서 쓰는 걸까요? 이렇게 꼬아 버리면 `M2_lm` 진영 기판의 월(`mnth`)들과 시간(`hr`) 파편 쪼가리 점수들을 한 달 치 혹은 하루 치 전부 다 긁어모아 더 해보면 그 합산 결과 파이가 무조건 강제적으로 **영락없이 0 (sum to zero)** 점으로 오차 없이 귀결 소멸해 버립니다. 덕분에 기준점 자체가 '1월' 이나 '0시' 같은 편파적 특정 타점 시점이 아니라, 아주 객관화된 범용 **"연간 혹은 하루 총체적 연 평균 종합 수준 타점 표본 척도(mean level)"** 라는 포괄 기점 자체가 객관 영점 거점 기준선이 되어 버립니다! 고로 나온 득점들은 그 평균 거점 바닥으로부터 파생되어 통계적으로 격차 이탈 단절 벌어진 더 높냐, 더 낮냐 식의 아주 객관적인 차이점(difference) 점유 지표로 아주 공평하게 치환 비교 해석 판독 관측(interpreted) 구조 논리 분석 가능하게 되는 마술의 의미 맹점 분석 수치를 뜻합니다.

For example, the coefficient for January of $-46.087$ indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average.
이걸 알면 이제 확증 통계 수치 표가 달라 보입니다! 예를 들어 표에 찍힌 새로운 1월 점수 **$-46.087$** 에 담긴 깊은 의미는? 이전처럼 '딴 달보다 기분 나쁨' 이딴 이상한 단순 비교가 아니라, "모든 조작 날씨 요건을 통제하고(holding constant) 얼렸을 때, 이 1년 치 '전체 일일 연간 평균(yearly average)' 객관 잣대의 하루 평균 자전거 이용객 수치 스탯과 비교선(relative to) 을 들이밀어 보면 1월은 평균의 기준 치보다 대략 **46명씩이나 모자라고 안 팔리고 비는 더 적은 라이더들(fewer riders)** 이라는 대대적 적자 감소 타격 지분 손실" 이 난다는 아주 극명하고 객관적 스탯 부피 손실 지표 팩트를 가리키고 저격(indicates) 판단 표지 하는 겁니다.

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used.
이 대목 단락 전제에서 우리가 통찰 분석가로써 반드시 통계 확고히 깨달아야(realize) 만 하는 가장 중대 논리 팩트는 제발 쫄지 말라는 겁니다! 사용자가 어떤 종류 복잡한 파이썬 기저 코딩 입력 옵션 방식 구조(coding used) 를 가져다 치환하든 돌려가며 쓰건 간에, 우리가 그냥 그 각 방식의 논리 규칙성만 제대로 머릿속에 장착 이해하고 도출 해석(interpret) 해 낼 수 있는 뇌만 보장 조건 성립(provided that) 된다면! 머신러닝 분석 판에서 **코딩 변환 양식 방식 선택 채택 유무(choice of coding) 기법 조작 그 자체 따위**는 기계 예측을 파괴하거나 전체 성능 구조 모의 타점에 타격 치명적 악 영향 문제 결과 오류 기점상 체계를 정말 하등 일절 단 1도 발생 오류 조작 치명 타격을 주지 않는다(does not matter) 는 사실의 깨달음 진단 통계 통찰입니다. 표현만 다를 뿐 팩트는 같습니다!

For example, we see that the predictions from the linear model are the same regardless of coding:
위 말이 못 미더우신가요? 조작 데이터 증거를 보세요. 우리가 표기 룰 코딩 변환을 아무리 꼬아서 코딩 지지고 볶고 난리를 치더라도(regardless of), 첫 번째 무식한 선형 모델(`M_lm`) 기계가 내뱉은 예측 정답지랑, 복잡하게 평균을 비틀어버린 두 번째 기계(`M2_lm`) 의 궁극의 최종 도달 예측 도박 스코어 도출 산출량 예측값들(predictions) 자체는 오차 하나 없이 항상 **귀신같이 절대 표본 데칼코마니 동일 불변 복제 융합 복사본(same)** 으로 일치한다는 통계 진리 사실 팩트를 다음과 같이 수학 에러 계산 연산 도출 증명(0으로 떴죠!) 으로 눈앞에 들이댈 증명 목격(see) 할 수 있습니다. 코딩에 속지 말고 데이터 본질을 보세요!

```python
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2) # "의심되면 첫 번째 구형 모델 결론 값이랑 두 번째 신형 모델 결론 값 빼기 해서 확인해 덧셈해봐라!!"
```

```python
Out[69]: 5.166710408544458e-09 # "뼛속까지 싹 다 빼도 결과는 0 (소수점 9자리 뒤에나 붙은 0, 즉 파이썬 컴퓨터 기계 계산 오류일 뿐 사실상 완벽한 0)! 둘의 결론은 똑같다!"
```

---

## Sub-Chapters

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans2.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans2.html)

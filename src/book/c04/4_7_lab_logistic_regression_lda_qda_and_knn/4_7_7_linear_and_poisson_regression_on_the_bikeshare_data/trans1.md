---
layout: default
title: "trans1"
---

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans1.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.7 Linear and Poisson Regression on the Bikeshare Data
# 4.7.7 자전거 대여 데이터에 대한 선형 및 포아송 회귀

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6.
여기서 우리는 단원 4.6 장에서 이미 묘사 설명되었던(described) 바와 같이, `Bikeshare` 종속 데이터 세트에 대해 선형 회귀 통계 모델 및 포아송 결합 회귀 모델들을 공용 적합(fit)시킵니다.

The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012.
관측 응답 지표 변수인 단서 `bikers` 측정치 항목은 기점 연도 2010–2012년이라는 특정 기간(period) 내의 특수 구역 Washington, DC 의 지정 시간당(per hour) 단절 자전거 렌탈 상품 대여 발생 횟수(number) 발생 치를 통계 측정(measures) 기록합니다.

```python
In [64]: Bike = load_data('Bikeshare')
```

Let’s have a peek at the dimensions and names of the variables in this dataframe.
우리 분석을 위해 이 로드된 외부 데이터 프레임(dataframe) 집단 내부의 배열 차원 크기들(dimensions) 그리고 그 속 변수 속성들의 개별 이름들(names) 열람을 잠깐 훔쳐 살펴보도록(have a peek at) 합시다.

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
선형 회귀 (Linear Regression)

We begin by fitting a linear regression model to the data.
우리는 제일 먼저 주입 데이터를 이용해 기초적 선형 회귀 모델(linear regression model) 을 적합 강제 훈련 시키며 시작(begin by) 합니다.

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

There are 24 levels in `hr` and 40 rows in all, so we have truncated the summary.
변수 `hr` 범위 내에는 시간상 24개의 세분된 독립 수준 분류 레벨들(levels) 이 파편 존재하며 전표 내에 모두 총합(in all) 결과 40개의 행(rows) 들이 있으므로, 그래서 우리는 부득이 출력 요약표(summary) 배열을 조작 중간 단절 잘라냈습니다(truncated).

In `M_lm`, the first levels `hr[0]` and `mnth[Jan]` are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines.
적합 기판인 `M_lm` 결과 테이블 내에서, 시간상 첫 수준인 표본 부품 항목 `hr[0]` 지표 그리고 `mnth[Jan]` 월 지표는 분석상 기저 디폴트인 기준 기준선 값들(baseline values) 로서 지정 작동 취급(treated) 되며, 그래서 그것 자체들 에 대해서는 어떠한 도출 판점 가중치 계수 추정치들(coefficient estimates) 조차도 화면상 제공 산출 표기 되지(provided for) 않습니다: 통계 암묵적으로(implicitly), 그들의 자체 할당 계수 산출 추정치들은 수치 0(zero) 으로 취급 은닉 되어지며, 그리고 나머지 뒤이은 일체의 모든 다른 종속 수준치 들은 모두 상대적으로 이 오리지널 기초 기준선들 지표들에 상대하여 파생 대비 도출 상대적으로 산출 측정 연산 측정(measured relative to) 반영 됩니다.

For example, the Feb coefficient of $6.845$ signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January.
예를 들면 특정 설명으로, 2월(Feb)의 판별 투사 가중치 계수 스코어 수치 인 $6.845$ 도출 스탯은, 다른 일체의 예측 변수들 조건 치수들을 전적으로 단 한치의 변동 없는 고정 상수 상태로 유지 가정 시킨 채로(holding all other variables constant), 통계 평균치 전제상(on average) 1월(January) 보다도 2월 달 내에 측정상 대략 계산 통계 7명의 자전거 초과 렌탈 이용자 가 더 산술 초과 발생 증대 존재 한다는 통계상 지표 팩트를 상징 의미(signifies) 전언 합니다.

Similarly there are about 16.5 more riders in March than in January.
유사하게 동일 원리 지표 비교(Similarly) 단절 로 유추하면, 산점 평균 측정상 1월 달 대비 기준 단절 비교 시 상대적으로 3월(March) 달 기간 내에는 약 16.5명의 추가 이용 렌트 발생 라이더 들이 결론 단적으로 더 통계 파생 초과 존재 상승 합니다.

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth`, as follows:
우리가 과거 단원 챕터 4.6.1 절 본문 내에서 주의 목격했던 결과 도표들은 변수 `hr` 파편 과 `mnth` 파편 배열 값들에 대해 다음과 같이 약간 이질 구조적인 다른 기저 코딩(coding) 투입 처리 방식을 구조 사용했습니다:

```python
In [67]: hr_encode = contrast('hr', 'sum')
mnth_encode = contrast('mnth', 'sum')
```

Refitting again:
모델 기계 구조 변경 재적합 작동 지시(Refitting again):

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

What is the difference between the two codings?
이 상호 분리 전개된 투 코딩 기점들(two codings) 배열 전극 간의 핵심 파생 구조 이면 차이(difference) 극명 점 은 대체 본질적으로 수리 무엇일까요?

In `M2_lm`, a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth`.
통계 산출 변수 배열 `M2_lm` 덩어리 전개 내에서는, 오직 특징 `hr` 변수의 제일 마지막 꼬리 레벨 등급 꼬리 스탯 인 단위 `23` 수치 와 속성 `mnth` 지표 그룹의 역시 기저 꼬리표 마지막 계급 레벨 표본 인 그룹 꼬리표 `Dec` 수치 둘 특정 개체 를 제외한 일관 전부 모든 단별 단절 파편 들에 대해서 표기 종속 계수 산점 추정치(coefficient estimate) 스탯 이 확연 표기 도출되어 화면상 보고 통계(reported) 수렴 됩니다.

Importantly, in `M2_lm`, the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels.
중요하게도 핵심 전제(Importantly), 이 치환 `M2_lm` 기판 구조 배정 환경 내에서는, 지표 `mnth` 구역의 은닉된 최후 수치 제일 마지막 계층 레벨 지표에 대한 산점 투사 계수 산출 추출 추정 타점 스탯 (결과표 도출상 미보고 은닉된, unreported) 은 0 제로 치 값(not zero) 이 아닙니다: 그 대신(instead) 대체 은닉값으로, 그 은닉 도출 결과 수치는 표면상 나타난 나머지 파생된 그 모든 다른 선행 수준 레벨들에 대한 도출 확증 분리된 나머지 전부 통계 계수 추정치들 의 총 합산 배당 누적 총계(sum) 단위 치에 역전 수리 마이너스 부호 음수(negative) 지표를 단절 강제 적용 부착한 뒤집힌 파편 수치 값과 산술상 전면 일치(equals) 계산 도출 합니다.

Similarly, in `M2_lm`, the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels.
매우 유사하게 논리 일치 단절 작동 원리상(Similarly), 기판 `M2_lm` 제 체제 데이터 안에서, 기판 `hr` 조작에 대한 콘솔상 미보고 은닉 된 가장 마지막 은닉 레벨 지표 파편의 종속 할당 계수 결괏값 도출 투사 추정치는, 나머지 선행 표기된 일체의 그 외 선행 모든 계층 레벨들 배당 계수 판정 추정 파편 결괏값 들의 전체 융합 총계값 도출 수치(sum) 의 단절 산술 부호 반전 역 역전 음수 수치 값(negative) 배열 로 치환 배당 산입 도출됩니다.

This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can be interpreted as the difference from the mean level.
이 전위된 치명적 단절 논리 구조가 의미 상징 전위 하는 것은, 파편 `M2_lm` 내부 집군 투사 타깃된 개체 추출 `hr` 산단 속성과 개체 산단 `mnth` 속성의 할당 배열 파편 고유 도출 계수들(coefficients) 은 결과상 전체 집단 합산 집계 시 항상 불변 합산 제로 기점 0 수치 (sum to zero) 로 강제 궤멸 수렴 귀결할 것이며, 그리고 본연 통계적 적으로는 거시적 집계 연간 기준 종합 평균 수준 도래 그룹 총기점 단위 레벨 척도(mean level) 로부터 양과 음으로 발생 파생 이격된 통계 잔여 파편 격차 단절 분기 차이점(difference) 지점 파편 그 자체 지표 로 치환 해석 판별될 수(interpreted) 있다는 논리 기반 맹점을 통과 의미(means) 파생 합니다.

For example, the coefficient for January of $-46.087$ indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average.
특정 투사 전극 예를 들어 설명하면, 확증 표기 통계 수치상 1월 표기 부착 변수에 대한 계수 수치 $-46.087$ 마커 스탯 지표의 지시 의미는, 시스템 기판의 투입 나머지 일체의 다른 종속 예측 힌트 투입 수치 변수들의 산출 조건 스펙 척도를 일절 침범 유동 불변 없는 상태의 항상 고정 결박 조건으로 단절 유지 지시 통제(holding constant) 시켰을 때, 단연 지어 연간 전체 집계 종합 도출 평균(yearly average) 점 스탯 척도 기준선 대비 상대 배분(relative to) 비교상 1월(January) 특정 분단에는 오직 평균적으로 파생 통상 대략 통계(typically) 도출 46명 정도 비교 더 적은 마이너스 비율의 부족 거치된 렌탈 이용자 라이더들(fewer riders) 이 단위 통계 타결 감소 발현 파생 결론 도출 존재 수립 한다는 극단적 통계 팩트 산포 구조를 여지없이 지시 가리킵니다(indicates).

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used.
이 대목 단락 전제에서 우리가 통계 조작 지휘 분석가로서 필히 확고히 깨닫고 견지(realize) 해야만 하는 가장 중대 맹점 사항 단서는, 기동 극단적 관점에서 돌이켜 보면 만약 우리 인간 코딩 조작 사용자가 임의 사용 조작 투입 조작된 기저 배열 특정 코딩 기술 논리 관점 전제 구조(coding used) 패턴 방식의 배경 잣대 토대 비추어 고찰 빛(in light of) 테두리 한계 안에서, 산출 기틀 통계 기동 모델 도출 출력물 산점 이면 은닉 논리를 엇나가지 않고 산술 논리 온전히 올바르게 지시 진단 해석해 낼(interpret) 수만 있는 지식이 전제 보장 조건(provided that) 수립 된다면, 사실상 데이터 전단 코딩 변환의 양식 선택 채택 방법(choice of coding) 도출 기법 조작 양식 그 자체는 실질적으로 단연 조작상 전체적 거대 구조 모의 거시 예측 통계치에 미치는 결과상 정말 아무런 조작 지장 이나 어떠한 치명적 악 영향 구조 문제 발생 전개조차 일절 무구하게 발생 파생 역 일으키지 기점 조작 치명 않는다(does not matter) 는 핵심 극명한 진단 통계 사실 단절 팩트의 통찰력 깊은 조명입니다.

For example, we see that the predictions from the linear model are the same regardless of coding:
수치 결론 파생 조작 예를 들어 산점 도출 계산, 우리는 유입 코딩 방식 제단 데이터 기법 선택 재현 구조에 코딩 전적으로 일괄 상관없이 전혀 무관하게(regardless of) 산출 선형 모델 연산 장치 코딩 기능에서 산술 파생 도달 획득한 기계의 궁극의 결론 도달 예측치들 추론 산출 예측 확증 도출(predictions) 투사 타점 점수 지표 결과 객체 자체는 확증 항상 절대적 표본 동일 복제 치환 확증(same) 일치한다는 불변의 사실 팩트를 다음과 같이 코딩 연산 단절 도출로 눈앞에 결과 산점 도출 목격 봅니다(see) 증명합니다:

```python
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2)
```

```python
Out[69]: 5.166710408544458e-09
```

---

## Sub-Chapters

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/trans1.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/trans1.html)

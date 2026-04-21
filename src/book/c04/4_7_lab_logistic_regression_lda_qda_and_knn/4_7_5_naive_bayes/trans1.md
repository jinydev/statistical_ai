---
layout: default
title: "trans1"
---

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/trans1.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.5 Naive Bayes
# 4.7.5 나이브 베이즈

Next, we fit a naive Bayes model to the `Smarket` data.
다음 차례로, 우리는 `Smarket` 관측 데이터 표본 집단에 나이브 베이즈(naive Bayes) 예측 확률 모의 모델을 모의 강압 적합시킵니다.

The syntax is similar to that of `LDA()` and `QDA()`.
파이썬 언어 기동 구동 조작 구문(syntax) 코딩 사용 방식은 이전의 `LDA()` 모델 작동과 직전의 기동 모델인 `QDA()` 구동 체제의 구문 제식 규격과 거의 매우 동일하게 똑같이 일치 유사합니다.

By default, this implementation of the naive Bayes classifier models each quantitative feature using a Gaussian distribution.
파이썬 패키지 내부 코드 작동 기본 조작 설정 체제(By default)상으로, 해당 이 나이브 베이즈 통계 분류기 기전 모형의 전산 시스템 구현체(implementation) 기능 모듈은, 분석 투입된 각 개별 낱개의 변수 단위 정량적 예측 특징(quantitative feature) 변수 데이터 개별 모형 무더기들을 수학적 속성 인 가우시안 확률 정규 분포(Gaussian distribution) 통계 곡선을 각각 임의 사용하여 내부적으로 강압 모델링합니다.

However, a kernel density method can also be used to estimate the distributions.
그러나, 통계 변수 내부 곡선 분포 모형을 추산 획득 및 확률 추정(estimate) 판단 작동 변환 하기 위한 프로그래머 조작의 다른 내부 대안 옵션 세팅 기동 지시 구동으로서 수학적 산점 인 커널 밀도 추정 방법(kernel density method) 로직 도구 구동 또한 얼마든지 조작 교체 사용될 수 있습니다.

```python
In [38]: NB = GaussianNB()
NB.fit(X_train, L_train)
```

```python
Out[38]: GaussianNB()
```

The classes are stored as `classes_`.
분류 추론 대상 추출된 단절 기점 타깃 종속 확률 판정 반환 클래스들 통계 범주 정보 표상 정보 기록은 기계 내부에 `.classes_` 란 이름의 내부 은닉 속성 객체 기능 인덱스 단편 공간으로 파편 백업 분류 저장됩니다(stored).

```python
In [39]: NB.classes_
```

```python
Out[39]: array(['Down', 'Up'], dtype='<U4')
```

The class prior probabilities are stored in the `class_prior_` attribute.
해당 그룹 단원 고유 그룹 전면 클래스들의 분류 출현 통계 사전 확률들(prior probabilities) 의 몫 비 데이터 백업 값들은 모형 내부에 보존 은닉된 개별 특수 조작 확인 속성 저장고 `.class_prior_` 독립 속성 구조 탭 공간 안에 은닉 분리 저장 백업됩니다.

```python
In [40]: NB.class_prior_
```

```python
Out[40]: array([0.49198397, 0.50801603])
```

The parameters of the features can be found in the `theta_` and `var_` attributes.
개입 투입된 조작 단서 투입 특징(features) 징후 변수 파편 파라미터 값들은 `.theta_` (각 관측 특성 그룹의 산술 평균) 통계 단편 속성 와 `.var_` (각 관측 단서 특성의 자체 분산) 이라는 기판 통계 2가지 속성값 들의 단편 메모리 열람 공간 안에서 분석가가 모두 단적으로 분명히 기록 확증 파악 개별 발견 탐색될 수 있습니다.

The number of rows is equal to the number of classes, while the number of columns is equal to the number of features.
이 출력 결과 표에서 2차원 배열 행(rows) 방향의 숫자 기록 카운트 나열 층 개수는 단말 산출 목표 지목 도출 팀의 타깃 클래스들의 도출 분류 전체수와 일치 상응 수치 크기가 동일(equal) 한 반면, 이와 반대로 가로 단절 배열 종속 구조 열(columns)의 길이 인덱스 수식 숫자는 관측 단서 속성 변동 개입 투입 타깃 특징(features) 단일 변수 개수 숫자 길이와 완벽히 일치 쌍으로 동일 대응합니다.

We see below that the mean for feature `Lag1` in the `Down` class is $0.043$.
아래 계산 관측 표 산출 데이터에서 우리는 하락 도출 상징 그룹 `Down` 종속 분류 클래스 팀 영역 안에서 투입단 관측 투입 조작 계산 종속 투입 지표 예측 단서 변형 변수 단편 계산 부품인 `Lag1` 변수의 수학적 독립 도출 속성 단위 분리 평균(mean) 이 대략적 계산 결과 산술상 도출 부품 데이터 $0.043$ 수치 파편 값임을 관측 확인해 살펴봅니다.

```python
In [41]: NB.theta_
```

```python
Out[41]: array([[ 0.04279022,  0.03389409],
                [-0.03954635, -0.03132544]])
```

Its variance is $1.503$.
그것 대상의 해당 개별 독립 그룹 단일 집단 종속 공분산 개체인 확률 분산 결괏값(variance) 수치 통계 기록 편차 치는 대략적으로 $1.503$ 스탯으로 측정 연산 계산됩니다.

```python
In [42]: NB.var_
```

```python
Out[42]: array([[1.50355424, 1.53246652],
                [1.51397116, 1.4870335 ]])
```

How do we know the names of these attributes?
우리가 대체 프로그램 내부적으로 컴파일 되어 은닉된 이러한 파이썬 기계 내부 내장 파편 부품 은닉 속성 데이터 객체 변수명 들의 은닉된 숨은 이름들(names) 열람을 외부 단에서 이토록 전격 편하게 어떻게 모조리 다 호출 단어로 알 길이 있을까요?

We use `NB?` (or `?NB`).
대답은, 우리는 파이썬 특수 헬프 쿼리 명령 구문인 명령줄 변형 호출 도움말 호출 단축 명령 규격인 `NB?` (혹은 뒤집은 명령형 `?NB`) 를 조작 강제 투입 대단히 도출 호출 강압 사용합니다.

We can easily verify the mean computation:
우리는 시스템 기계 모델이 폐쇄 내부 은닉된 도출 작동 산술로 독립적 자체 처리 이행 수행 판단한 이러한 블랙박스 내부 수동 평균 추산 계산법 연산 측정(computation) 기작 구조 출력 이력을 통계 패키지 기능 없이 아주 쉽게 독자적으로 외부적으로 임의 교차 증명 계산하여 단독 수동 검증(verify) 입증 확인 일치 연산 교차 대조 증명해 낼 수 있습니다:

```python
In [43]: X_train[L_train == 'Down'].mean()
```

```python
Out[43]: Lag1    0.042790
         Lag2    0.033894
         dtype: float64
```

Similarly for the variance:
유사하게 매우 완벽 동일 원리 작동(Similarly) 패턴으로써 통계 집단 증명인 분산(variance) 데이터 스탯 확증 측정 측면 조작 방식 에 대해서도 개별 독립 입증 산술 도출 수동 조작을 단절 증명 검증 합니다:

```python
In [44]: X_train[L_train == 'Down'].var(ddof=0)
```

```python
Out[44]: Lag1    1.503554
         Lag2    1.532467
         dtype: float64
```

The `GaussianNB()` function calculates variances using the $1/n$ formula.
확인 결과, 측정에 쓰인 베이즈 확률 통계 모형 측정 함수 도구 개체인 `GaussianNB()` 기능 추출 함수 패키지는 통계상 수학적으로 표본 보정이 아닌 모수 단절 편차 산술 추정용 $1/n$ 표본 분산 정칙 산술 추정 계산 도출 정립 공식(formula) 계산 체제 구조를 본질적으로 우선 단독 사용하여 파편 은닉 데이터 속성 타깃 그룹 간의 분산들(variances) 을 독자적 단독 독립 계산 산출 자체 파악 계산해 산출합니다(calculates).

Since `NB()` is a classifier in the `sklearn` library, making predictions uses the same syntax as for `LDA()` and `QDA()` above.
소개 작동 투입된 주 기동 베이즈 확률 통계 작동인 `NB()` 무기 파편 통계 모델 장비 객체가 저 거대 통합 모음인 `sklearn` 도구 라이브러리 연장 패키지 덤불 속에 부품 공용 보급 존재하는 거대 표준 분류기(classifier) 장비의 거대 상속된 여러 부품 의 거시 연장 한 계열 이라는 전제 공통 호환성 인 관점 근거 기동 지향적 성격이므로, 미래 투입된 단서 타점 단서 도출 예측들 산출 도출(predictions) 추론 행동 판결 계산 발포 사격 구동은 맨 위 선조립 이전 방식인 구기동 체제 `LDA()` 모델 조작 그리고 이전 타 단원의 장비 `QDA()` 무기 작동에서 확립 사용 대입된 단일 구조 방식과 소름 돋게 일치 똑같은 무구 호환 동일 코딩 구조 구문 규칙(syntax) 조작 제식 명령 틀을 단지 이질감 없이 단일 통합 재사용 호환성 높게 공유해 확고히 대입 투입 실현 지시 구동 사용합니다(uses).

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

Naive Bayes performs well on these data, with accurate predictions over 59% of the time.
가장 확률적 기반의 약한 맹신을 기반하는 역설의 나이브 베이즈(Naive Bayes) 통계 예측 도출 시스템 장비는 이 해당 목표 복잡 난해 혼동의 특수 주가 거대 도박판 데이터 표본 전개 극단적 시계열 파편 묶음 들 위에서 실전 테스트 파편 모의 분석 투사 결과, 전체 가동 시간 중 실전 명중 타점 예측 달성 명중 도달 타점 퍼센티지 수치 약 59% 이상의 실전 도달 기록 시간 적중 비율을 아득히 넘어서며 아주 꽤 상당히 날카롭게 예후 정확한 조준 성능 예측 일치 판별 적중 타점 적중 예측 도출 결과들을 의외로 훌륭하게 단숨에 만들어 기록 내며 결과적으로 상당히 매우 압도적으로 뛰어난 단단히 우수한 확률 성능 지향 타격 우성 생존 성능(performs well) 적중 타점 전선 스탯 판별 방어력을 실전 필드에서 능히 도출 증명 구축 발휘합니다.

This is slightly worse than QDA, but much better than LDA.
단 하나 꼬집어 객관적으로 보여준 방금 도출 산출 이 베이즈 단일 결과 산출물 타격 기능 기록 지표 스코어의 무결성 수치는, 직전 단원 전 도출 고차 거대 투입 비교 비교 체제 비교군 인 유연한 뱀 같은 구조체 QDA 기법의 도출 기록 명중 달성 득점 보다는 통계상 극히 아주 살짝 근소한 소수점 단위로 미세하게 약간 단절 하락 기점 약화 안 좋게 기록 성능이 조금 파생 열위 추락 하락 지배당해 성능이 나쁘지만(worse), 그전의 아주 초장기 훨씬 구식 기법인 극단 단순 경직 LDA 모델 기계 기동 기록 성적 판도 스탯 수치 보다는 결코 단언코 아주 비교 불가 수준으로 훨씬 극비 한 극단적 대단 한 초격차 월등히 우위 우성 비교 우위(better) 맹목 성과 기점 더 생존율이 아주 단단하고 우수 성능 명중 성적 성능 타점 생존율 지표를 적나라하게 과시 측정 타점 도출합니다.

As for `LDA`, the `predict_proba()` method estimates the probability that each observation belongs to a particular class.
이전 조작 관행 투입된 초기 직선 구식 기동 방식 구형 선형 분리기 모델 체제였던 `LDA` 기법의 전산 통계 작동 방식 파운데이션 절차 작동 전개 기능 작동 수행 연산 절차 패턴 룰 방식과 전혀 이질 다름없는 완벽 모의 마찬가지 같은 통일 규격 제식 작동 호환 체제 원리 구성 조작 로(As for), 부속 사후 소속 분배 예측 확률 결괏값 판별 계산 도출 배점 사격 전산 버튼 투입 명령 전용 호출 장치 표본 부품인 백분율 확률 예측 할당 메서드 작동 조작 스위치 `predict_proba()` 사격 발진 확률 도출 분류 확률 연산 산출 조작 메서드 톱니바퀴는 통계 판별 산단 추출 파편 각 미립 세부 낱개 단일 개별 관서 테스트 추출 관측 단서치(observation) 낱낱 요소 테스트 요소 표본 낱낱 개체 들이 제각각 파편 분열되어 흑백 선택지 중 대체 어느 지정 상응 대응된 팀 소속 판별 한정된 부류 특수 지정 예측 확률 목표 최종 타겟 후보군 낙인 속성 소속 종속 진영 분류 그룹 단일 진영 특정 팀 클래스(particular class) 도출 속성에 최종 적으로 더 우위로 도래 속성 도달 확률로 여부로 낙인 지목 소속 속할지에 편향 치 대한 매우 치밀하고 세밀한 배정 해당 통계 소속 합산 확률 백분율 배당 예측치 소속 지분 배정 확률 퍼센트 표본 데이터 산술 도출량 스코어 수치(probability) 데이터 묶음 도표 리스트 를 모조리 하나하나 모조리 남김없이 통계 모두 개별 핀포인트 세세히 일련 추적 분리 확률 백분위 계산 산술 내부 단절 연산 추정 분단 판별 통계 연산 측정 추출 계산 결판 추출 도달 산출(estimates) 분출 덤핑 측정 해 분리 반환 출력 해 제공 표출 해 보여 줍니다.

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

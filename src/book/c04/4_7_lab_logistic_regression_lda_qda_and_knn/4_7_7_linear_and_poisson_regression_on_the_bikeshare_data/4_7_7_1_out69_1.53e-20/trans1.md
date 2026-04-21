---
layout: default
title: "trans1"
---

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans1.html) | [4.7.7.2 Poisson Regression >](../4_7_7_1_poisson_regression/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.7.1 Out69 1.53E-20

The sum of squared differences is zero.
두 비교 검증 모델 간의 각 파생된 산출 예측치 차이의 제곱 연산 도출 결과 총합(sum of squared differences) 수치는 시스템상 완벽한 0(zero) 으로 수렴 계산 도출됩니다.

We can also see this using the `np.allclose()` function:
우리는 데이터 패키지 또한 파이썬 통계 검증 도구인 `np.allclose()` 기능 함수 교차 스위치를 전면 구동 사용(using) 함으로써 이 수학적 논리 일치 사실 통계 팩트를 여실히 교차 검증 목격(see) 할 수 있습니다:

```python
In [70]: np.allclose(M_lm.fittedvalues, M2_lm.fittedvalues)
```

```python
Out[70]: True
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with `mnth`.
본문 도표 Figure 4.13의 시각 지표 좌측 편(left-hand side) 지표 표출 영역을 다시 우리가 스스로 코딩으로 독자 재생산 기동 도출(reproduce) 하기 위해서, 우리는 반드시 가장 우선적 선결 조작 조건으로서 변수 대상 `mnth` 파편과 직접 연관 결합(associated with) 되어 묶여 있는 해당 타깃 투사 계수 산점 추정치 배열들(coefficient estimates) 을 개별 독립 분리하여 모조리 온전하게 획득 단독 추출 도출(obtain) 해야만 합니다.

The coefficients for January through November can be obtained directly from the `M2_lm` object.
특정 추출 1월(January) 시작 지표부터 11월(November) 지표 단락까지 연계 거치기 위한 해당 연속 소속 표상 배열 계수 파편들은 기판 변수 파편 `M2_lm` 결과 객체 배열(object) 의 표면 기저로부터 아무 추가 연산 왜곡 작동 없이 곧바로 단독 직접 완전 획득 분리 도출(obtained directly) 확증 추출 될 수 있습니다.

The coefficient for December must be explicitly computed as the negative sum of all the other months.
마지막 절단 누락된 기판 12월(December) 지표에 단절 대한 해당 누락 파편 은닉 계수 단일 수치는, 반드시 논리적으로 그 외 모든 다른 전체 산출 월별 그룹 도출 수치들(all the other months) 의 결과 도출된 총합 부분(sum) 에 대한 마이너스 음수 부호 역 반전(negative) 이면 산점 역산 기법 조작 절차로 명시적으로 단절 직접 프로그래머가 계산 도출 연산 조작 지정(explicitly computed) 되어 강제 산출 도출 복원 회수 되어야만 합니다.

We first extract all the coefficients for month from the coefficients of `M2_lm`.
우리는 연산 과정에서 제일 통계 먼저 가장 우선하여 조작 `M2_lm` 결과 기판의 배열 파편 혼합 계수들 무더기 더미 속으로부터, 특정 분단되어 있는 모든 온전한 추출 월별(month) 기간 한정 계수 표상 파편 들만 을 따로 조건 지정 조작하여 우선 별도 스캔 추출 단절 분리(extract) 처리 해냅니다.

```python
In [71]: coef_month = S2[S2.index.str.contains('mnth')]['coef']
         coef_month
```

```python
Out[71]: mnth[Jan]    -46.0871
         mnth[Feb]    -39.2419
         mnth[March]  -29.5357
         mnth[April]   -4.6622
         mnth[May]     26.4700
         mnth[June]    21.7317
         mnth[July]    -0.7626
         mnth[Aug]      7.1560
         mnth[Sept]    20.5912
         mnth[Oct]     29.7472
         mnth[Nov]     14.2229
         Name: coef, dtype: float64
```

Next, we append `Dec` as the negative of the sum of all other months.
다음 통계 연산 이행 단계로(Next), 우리는 위 나머지 단편 산출 모든 거시 타 척도 월들(all other months) 계수 추출 결과 도출 배열의 총합산 산술 결과(sum) 수치 표면에, 마이너스 역전 부호 음수 기점 조작(negative) 을 가한 강제 산술 확증 값 데이터를 단절 은닉된 타점 `Dec`(12월) 지표 명칭 꼬리표 항목으로써 배열 기판의 맨 하단 끝에 수동 덧대기 병합 결합 꼬리 추가 결합(append) 구조 조작합니다.

```python
In [72]: months = Bike['mnth'].dtype.categories
         coef_month = pd.concat([
             coef_month,
             pd.Series([-coef_month.sum()],
                       index=['mnth[Dec]'])
         ])
         coef_month
```

```python
Out[72]: mnth[Jan]    -46.0871
         mnth[Feb]    -39.2419
         mnth[March]  -29.5357
         mnth[April]   -4.6622
         mnth[May]     26.4700
         mnth[June]    21.7317
         mnth[July]    -0.7626
         mnth[Aug]      7.1560
         mnth[Sept]    20.5912
         mnth[Oct]     29.7472
         mnth[Nov]     14.2229
         mnth[Dec]      0.3705
         Name: coef, dtype: float64
```

Finally, to make the plot neater, we’ll just use the first letter of each month, which is the 6th entry of each of the labels in the index.
마지막 단절 시각 데이터 조작 절차로(Finally), 최종 결과 출력 도출 시각화 시점 그래프(plot) 패널 판을 화면상 좀 더 단절 산뜻하게 외형 미관상 더 깔끔하게 구축 구성 생성 복구(make neater) 하기 임의 지시 위해서, 우리는 그냥 축약 표기상 각 분리 개별 파편 월(month) 명칭 지정 글자의 제일 기점 첫 번째 개별 문자 낱단 항목(first letter) 마킹 요소만 을 단독 분리 선택 조작 사용(use) 할 것인데, 이것 규칙은 해당 단절 추출 문자 배열 이 파이썬 문자열 표기 인덱스 속성에 위치한 기저 내부 라벨들 정보 배열(labels in the index) 문자열 단어 덩어리 문자 하나 하나 열 마다 기판 내부 배열 적으로 배열 순서 6번째 단절 기록 색인 항목(6th entry) 순번 자리에 고정 위치 점유하고 있는 색인 개체 팩트 지표 입니다.

```python
In [73]: 
fig_month, ax_month = subplots(figsize=(8, 8))
x_month = np.arange(coef_month.shape[0])
ax_month.plot(x_month, coef_month, marker='o', ms=10)
ax_month.set_xticks(x_month)
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20)
ax_month.set_xlabel('Month', fontsize=20)
ax_month.set_ylabel('Coefficient', fontsize=20);
```

Reproducing the right-hand plot in Figure 4.13 follows a similar process.
앞서 보여준 본문 도표 Figure 4.13 의 우측 편 시각 조작 도출 연개 그래프(right-hand plot) 영역을 다시 시각 프로그래밍 결과 재생산 단절 도출(reproducing) 코드로 구현해 내는 지시 절차 작동 방식 역시 위와 기능상 완벽 전격 상응하는 상호 유사한 코딩 구조 패턴 체제 절차들(similar process) 조작 논리를 동일 단절 수반 추적(follows) 병용 전개합니다.

```python
In [74]: 
coef_hr = S2[S2.index.str.contains('hr')]['coef']
coef_hr = coef_hr.reindex(['hr[{0}]'.format(h) for h in range(23)])
coef_hr = pd.concat([
    coef_hr,
    pd.Series([-coef_hr.sum()], index=['hr[23]'])
])
```

We now make the hour plot.
우리는 전면 확정된 통합 시간 데이터 결과 도출 스펙 치로 이제 시각화 최종 목적 시간 도출 연계 그래프(hour plot) 도표 패널 을 전면 단독 생성 확립 생성 구축 단절(make) 산점 도출합니다.

```python
In [75]: 
fig_hr, ax_hr = subplots(figsize=(8, 8))
x_hr = np.arange(coef_hr.shape[0])
ax_hr.plot(x_hr, coef_hr, marker='o', ms=10)
ax_hr.set_xticks(x_hr[::2])
ax_hr.set_xticklabels(range(24)[::2], fontsize=20)
ax_hr.set_xlabel('Hour', fontsize=20)
ax_hr.set_ylabel('Coefficient', fontsize=20);
```

---

## Sub-Chapters

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans1.html) | [4.7.7.2 Poisson Regression >](../4_7_7_1_poisson_regression/trans1.html)

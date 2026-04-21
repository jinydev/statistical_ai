---
layout: default
title: "trans1"
---

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans1.html) | [4.8 Exercises >](../../../4_8_exercises/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.7.2 Poisson Regression
# 4.7.7.2 포아송 회귀

Now we fit instead a Poisson regression model to the `Bikeshare` data.
이제 우리는 앞서 거친 방식과 대신하여 기조를 바꾸어(instead) 동일한 대상 객체인 `Bikeshare` 관측 특정 구간 기록 데이터 표본에 대해, 이번에는 완전히 다른 성질인 포아송 파편 회귀 통계 객체 모델(Poisson regression model) 측정을 강제 적합 훈련(fit)시킵니다.

Very little changes, except that we now use the function `sm.GLM()` with the Poisson family specified:
코드 기동 구동 조작상에서는, 우리가 지금부터 포아송 결속 파편 속성 계열(Poisson family) 을 명시적 인자 조작하여 확고히 지정한 상태 구동(specified) 조건 으로 범용 거대 분류 객체 함수 모듈인 `sm.GLM()` 구동 기판을 기능적으로 전격 사용(use) 한다는 아주 구조적 단면 속성 논리 차이를 단편 별도로 제외하면(except that), 그 외의 조작 과정상 차이는 정말로 단면 거의 극히 티도 안 날 정도로 단절 체감되는 변화 거의 없이(very little changes) 이전 코딩 구문과 거의 동일 전개 작동 패턴 됩니다.

```python
In [76]: M_pois = sm.GLM(Y, X2, family=sm.families.Poisson()).fit()
```

We can plot the coefficients associated with `mnth` and `hr`, in order to reproduce Figure 4.15.
우리는 본문 교재의 이면 도표 Figure 4.15 패널을 독립 코딩으로 자가 재현 및 재생산 연산하기 구동 목적에서(in order to reproduce), 단서 단편 `mnth` 월 그룹 조건 및 단서 단절 파편 `hr` 시간 파편들과 결합 연관 결속된(associated with) 개별 표본 추출 표기 계수들 시각 단절 분석 지표를 시각 표출 궤적 도식화 산점 하여 단독 도표로 표기 그려볼(plot) 수 단절 산출 확증 도출 가능 합니다.

We first complete these coefficients as before.
우리는 확증 도출 연산 과정에서 제일 먼저, 이전 확증 공정 절차 파티션 에서와 다름없이 완벽 동일하게(as before) 우선 이 단절 파손된 투사 은닉 계수 치수들 조작 단편(these coefficients) 파편 을 복원 수치 완성 재생 도출(complete) 결합 해 냅니다.

```python
In [77]: S_pois = summarize(M_pois)
coef_month = S_pois[S_pois.index.str.contains('mnth')]['coef']
coef_month = pd.concat([coef_month,
                        pd.Series([-coef_month.sum()],
                                  index=['mnth[Dec]'])])
coef_hr = S_pois[S_pois.index.str.contains('hr')]['coef']
coef_hr = pd.concat([coef_hr,
                     pd.Series([-coef_hr.sum()],
                               index=['hr[23]'])])
```

The plotting is as before.
이후의 코딩 플로팅 출력 시각 연산(plotting) 과정 단절 조작 역시, 이전 단절 과 완벽 데칼코마니 완벽 상응 동일하게(as before) 100% 동일 과정 이행 전개됩니다.

```python
In [78]: fig_pois, (ax_month, ax_hr) = subplots(1, 2, figsize=(16, 8))
ax_month.plot(x_month, coef_month, marker='o', ms=10)
ax_month.set_xticks(x_month)
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20)
ax_month.set_xlabel('Month', fontsize=20)
ax_month.set_ylabel('Coefficient', fontsize=20)
ax_hr.plot(x_hr, coef_hr, marker='o', ms=10)
ax_hr.set_xticklabels(range(24)[::2], fontsize=20)
ax_hr.set_xlabel('Hour', fontsize=20)
ax_hr.set_ylabel('Coefficient', fontsize=20);
```

We compare the fitted values of the two models.
우리는 비교 산출 분리 이 두 가지 모델들로부터 도출 투사된 각자 적합 파편 적응 개별 도출 결과 값들(fitted values) 진영 을 상호 산점 연산 비교(compare) 산술 단절 대조 탐사합니다.

The fitted values are stored in the `fittedvalues` attribute returned by the `fit()` method for both the linear regression and the Poisson fits.
초기 선형 회귀 모의 연산 작동 그리고 후기 포아송 측정 연산 파편 적합(fits) 분석 이 통계 둘 가지 모두에 대해, 구동 `fit()` 타격 사격 메서드 단말 도구로부터 강제 파편 스탯 반환된(returned) 은닉 표기된 표본 단편 `fittedvalues` 속성 지표 상자 내부에 각 개체 독립 도출 통계 개별 적합 타점 결과 수치 값들이 단절 블랙박스 은닉 단절 파편 저장고 파티션 분단 저장(stored) 안착 유지 지속 되어 있습니다.

The linear predictors are stored as the attribute `lin_pred`.
그 파편 중 종속 단절된 초기 선형 기법 예측 산출 대상 지표 추적 변수들(linear predictors) 은 개별 독립 지표 `lin_pred` 속성 이라는 전적 파편 탭으로 자체 전격 분리 수치 배정 독립 저장(stored) 파편 수치 분리 됩니다.

```python
In [79]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(M2_lm.fittedvalues,
           M_pois.fittedvalues,
           s=20)
ax.set_xlabel('Linear Regression Fit', fontsize=20)
ax.set_ylabel('Poisson Regression Fit', fontsize=20)
ax.axline([0,0], c='black', linewidth=3, linestyle='--', slope=1);
```

The predictions from the Poisson regression model are correlated with those from the linear model; however, the former are non-negative.
뒤에 도출된 후기 포아송 타점 회귀 모델 전극 파편에서 도달 획득한 기점 산점 예측 도출 결과치들(predictions) 객체 파편은, 산술 기저적으로 앞선 저 선형 1차 모델 판락 기능으로부터 획득 얻어낸 도출 파편 산술 그것들 도출 결괏값 진영(those) 과 기판 시 분명 상호 양자 강한 연관 상관관계가 긴밀히 엮여 도달 결합 일치성 파편 존재(correlated with) 통계 발현 하긴 합니다; 그러나(however), 분명히 전자(former) 에 해당하는 포아송 파편 결과 데이터 덩어리 전개는 통계상 음수 도달 단절 역전된 결과치가 절대 결코 기저 절대 파편 존재 개별 파생 치 단절 수치 존재하지 원칙적 개별 단절 무작위 절대 불능 않는 무조건 무한 양수 도달 일변의 비음수 절대 제한 양적 수치 전극(non-negative) 한계 영역 결과물 표면 만을 갖습니다.

As a result the Poisson regression predictions tend to be larger than those from the linear model for either very low or very high levels of ridership.
그 파생 구조 통계 단편의 도달 결과로(As a result), 도달 종착 결과로써 포아송 결론 회귀 구동 표적 구동 스위트 예측 도출 수치들은 탑승 이용객 렌탈 라이더 절대 발생 빈도 수요 숫자가 지극히 단절 극단 산점 아주 낮거나(very low) 산점 단절 혹은 지극히 기형 특성 극점 배분 비율 산출 아주 높은(very high) 파생 파편 극한 수준 특이점 치 레벨들(levels of ridership) 발생 단편 중 극단적 어느 하나 단절 특정 (either) 돌발 양 극단 치의 특수 조건 상황에 극한 닥치게 될 표본 발단 경우에 한 해, 종속 단절 산단 저 대비 군 선형 기저 모델 단점 결괏값에서 이행 도출 파생된 발생 스탯 그것들(those) 고유 결과 수치보다 도출 극적 상 더 과대 산출 수리 큰 스케일 수치 마킹 결과 값 부피 척도 비율로 나타 도달 표출 나는 확률 압박 산단 산술적 편향적 치우침 이행 경향성(tend to be larger than) 마진 지표 를 단절 갖습니다.

In this section, we fit Poisson regression models using the `sm.GLM()` function with the argument `family=sm.families.Poisson()`.
본 장의 단절 구역 이 특정 세션(In this section) 한정 절에서, 우리는 파이썬 매개 변수 `family=sm.families.Poisson()` 파라미터 조작 통계 인자(argument) 변수를 전격 옵션 조작 강제 투시 동반하여 거대 장비 통계 산포 `sm.GLM()` 무기 패키지 함수를 거대 사용(using) 함으로써 본연의 포아송 파생 기반 이행 특수 회귀 통계 기계 모델들을 파편 훈련 강압 편제 적합(fit)시켰습니다.

Earlier in this lab we used the `sm.GLM()` function with `family=sm.families.Binomial()` to perform logistic regression.
우리는 본 광활한 기동 실습 거치 장(lab) 의 훨씬 아주 이전 이전 단절 챕터(Earlier) 공정 중 훈련 단락 과거 기록 조작 파편에서 조작, 유사 로지스틱 회귀 판별을 도출 이행 단결 연산 실행(perform) 도달 시키기 판별 지시 사전 단독 위해 조작 매개 무기 요소 `family=sm.families.Binomial()` 배정 전극 강제 조작 동반 지표를 기동 인자로 단절 삼아 `sm.GLM()` 공통 도구 단절 동일 함수 장비 를 도출 파생 재사용(used) 했던 기록 측정 이행이 동일 있었습니다.

Other choices for the `family` argument can be used to fit other types of GLMs.
입력 투사 파라미터 `family` 선택 조작 입력 인자에 대한 기저 무구 개별 다른 변형 특수 임의 옵션 교차 선택들(Other choices) 인자 세팅 파편 옵션 도달 제어 교체 배정 스위치는 파편 통계 수단 기타 전혀 다른 파생 성향 종류의 분기 유형 타점 모델 무기 들의 복합 GLMs 파형 이형 덩어리를 훈련 전파 적합 시키고 유도 기동 편제 통제 맞추기 지시 위해(to fit) 동일하게 폭넓게 단절 투척 구동 도출 유용 도출 기동 사용될(can be used) 이형 수 파편 연동 있습니다.

For instance, `family=sm.families.Gamma()` fits a Gamma regression model.
특수 옵션 변환 작동 무려 예시 치환 단절 하나의 타 배분 단절 타겟 구동으로(For instance), 조작 파라미터 조작 타점 입력 `family=sm.families.Gamma()` 특수 배정 세팅 파라미터 입력은 특수 모델 감마 타점 측정 회귀 기형 모델(Gamma regression model) 전용 특수 장비를 옵션 조치 강제 적합 이행 조작 구형 구동(fits) 구축 기정 시킵니다.

---

## Sub-Chapters

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans1.html) | [4.8 Exercises >](../../../4_8_exercises/trans1.html)

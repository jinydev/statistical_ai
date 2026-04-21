---
layout: default
title: "trans2"
---

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans2.html) | [4.8 Exercises >](../../../4_8_exercises/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.7.2 Poisson Regression
# 4.7.7.2 마이너스는 참을 수 없어! 양수 전용기 포아송 회귀(Poisson Regression)

Now we fit instead a Poisson regression model to the `Bikeshare` data.
자, 계속해서 자전거 대여 데이터를 분석합니다! 방금 전까지 무식한 일직선 몽둥이인 '선형 모델'로 자전거가 몇 대 대여될지 때려 맞췄다면, 이번에는 작전을 영리하게 바꿔서(instead) 자전거 수 같은 '개수 카운팅'에 아주 최적화 특화된 통계 병기, **포아송 회귀 통계 모델(Poisson regression model)** 이라는 신무기를 꺼내와 강제 훈련(fit) 적합 시켜 보겠습니다.

Very little changes, except that we now use the function `sm.GLM()` with the Poisson family specified:
코드 기동 구동 조작상에서는 놀랍게도 여러분이 새로 외울 코드는 맹세코 거의 없습니다! 단지 범용 기관총인 `sm.GLM()` 모듈에다가 탄창 옵션 스위치로 포아송 패밀리 계열(`family=sm.families.Poisson()`) 총알을 써라! 하고 단어 하나 명시적 옵션 칩을 끼워 지정(specified) 조작해 주는 사소한 변화(except that) 차이를 빼면 그 외의 조작 과정상 차이는 정말로 티도 안 날 정도로 아주 사소하게 거의 없이(very little changes) 이전 무기들과 똑같은 조작 버튼으로 아주 편하게 호환 작동 됩니다. 짜잔!

```python
In [76]: M_pois = sm.GLM(Y, X2, family=sm.families.Poisson()).fit() # "야 파이썬! 이번엔 GLM 모델에다가 포아송(Poisson) 무기 세팅해서 훈련 개시해!!"
```

We can plot the coefficients associated with `mnth` and `hr`, in order to reproduce Figure 4.15.
자, 그럼 포아송 무기가 내놓은 결괏값을 눈으로 검토해 볼 시간입니다! 우리는 앞서 본문의 이론 설명란 도표 Figure 4.15에서 봤던 그 멋진 그래프 패널을 코딩으로 직접 쌍둥이 재현 연산하기 목적(in order to reproduce)으로, 저 포아송 기계가 뱉어낸 월(`mnth`) 영향력 힌트와 시간(`hr`) 힌트 점수표를 뽑아 통계 시각 도식화 하여 도표로 그려볼(plot) 겁니다.

We first complete these coefficients as before.
먼저, 저번 챕터 선형 모델 때 시간과 월 점수를 요리조리 복원했던 짜증 나는 그 노가다 스킬! 그 점수 복원 마스터 조립(complete) 작업을 똑같이(as before) 이 무기 점수표에서도 그대로 데칼코마니 반복해 줍니다. 

```python
In [77]: S_pois = summarize(M_pois)
coef_month = S_pois[S_pois.index.str.contains('mnth')]['coef']
coef_month = pd.concat([coef_month,
                        pd.Series([-coef_month.sum()],
                                  index=['mnth[Dec]'])]) # 아까 했던 '증발한 12월 점수 마이너스로 꼬리에 덧붙여 부활시키기' 신공 작전! 전격 이행!!
coef_hr = S_pois[S_pois.index.str.contains('hr')]['coef']
coef_hr = pd.concat([coef_hr,
                     pd.Series([-coef_hr.sum()],
                               index=['hr[23]'])]) # 아까 했던 '증발한 23시 점수 마이너스로 꼬리에 덧붙여 부활시키기' 신공 작전! 똑같이 이행!!
```

The plotting is as before.
당연히 엑스축 맞추고 라벨 붙이는 그래프 출력 시각 연산(plotting) 코딩 과정도, 직전 모델과 그림판 캔버스 크기(16x8) 만 좀 크게 바꾼 거 빼고는 완벽하게 100% 동일하게 긁어붙이기 무한 재탕(as before) 이행 전개됩니다. 

```python
In [78]: fig_pois, (ax_month, ax_hr) = subplots(1, 2, figsize=(16, 8)) # "이번엔 도화지 좀 큰 걸로(16x8) 두 장 나란히 붙여서 세팅해!"
ax_month.plot(x_month, coef_month, marker='o', ms=10) # 1~12월 점수 때려박고!
ax_month.set_xticks(x_month) 
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20) # 촌스러운 영단어 짜르고 첫 글자만 스펠링 이쁘게 박고!
ax_month.set_xlabel('Month', fontsize=20)
ax_month.set_ylabel('Coefficient', fontsize=20)
ax_hr.plot(x_hr, coef_hr, marker='o', ms=10) # 0~23시 점수 때려박고 굵은 점으로 빡!
ax_hr.set_xticklabels(range(24)[::2], fontsize=20) # 짝수 시간만 점프 띄어쓰기해서 라벨 이쁘게 박아!
ax_hr.set_xlabel('Hour', fontsize=20)
ax_hr.set_ylabel('Coefficient', fontsize=20); # 완성!!
```

We compare the fitted values of the two models.
결과가 나왔습니다! 이제 우리의 도마 위에 오른 아주 무식한 구닥다리 모델(선형 선배)과 영리한 신형 모델(포아송 후배)! 이 두 라이벌 가지 머신들이 데이터를 보고 각각 뱉어낸 '상상 예측 점수 값들(fitted values)' 간에 무슨 치명적인 차이가 있는지 멱살 잡고 상호 산점 연산 비교(compare) 단절 대조 매치업 결투를 시켜보겠습니다.

The fitted values are stored in the `fittedvalues` attribute returned by the `fit()` method for both the linear regression and the Poisson fits.
기계가 뽑은 이 '상상 예측 점수' 파일 장부는 두 모델 기계 놈들 다 똑같이 훈련(fit)이 끝나면 무상 제공(returned)으로 뽑아주는, 기계 내장 디폴트 블랙박스 조수석 서랍통인 `.fittedvalues` 속성 지표 상자 안에 차곡차곡 예쁘게 결과 점수가 다 백업 파편 저장(stored) 안착 유지되어 있습니다! 꺼내오면 됩니다!

The linear predictors are stored as the attribute `lin_pred`.
참고로 TMI지만, 그 예측 점수들이 나오기 직전의 내부 선형 추적 뼈대 부품 변수 통계치(linear predictors)는 `.lin_pred` 속성이라는 다른 서랍 탭으로 기계가 알아서 자체 전격 분리 수치 배정 독립 저장(stored) 해 둡니다. (이건 나중에 심심하면 꺼내 보세요!)

```python
In [79]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(M2_lm.fittedvalues, # 가로축: ము식한 선형 회귀 기계가 찍은 정답 예측치!
           M_pois.fittedvalues, # 세로축: 최신식 포아송 회귀 기계가 찍은 정답 예측치! 크로스!
           s=20)
ax.set_xlabel('Linear Regression Fit', fontsize=20)
ax.set_ylabel('Poisson Regression Fit', fontsize=20)
ax.axline([0,0], c='black', linewidth=3, linestyle='--', slope=1); # 정가운데 기준선 대각선(y=x) 그려서 비교판 깔아라!!
```

The predictions from the Poisson regression model are correlated with those from the linear model; however, the former are non-negative.
도표를 보시면! 포아송 기계가 찍은 정답 스코어 결과치들(predictions)과 무식한 선형 기계의 도출 결괏값 들은 크게 보면 서로 비슷하게 얼추 비슷하게 같이 비례하면서 상호 똑같이 증감하는 강한 연관 상관관계 경향성 궤도를 분명 띠면서 결합 존재(correlated with) 하긴 합니다; 그러나(however), 기막힌 가장 치명적인 약점 차이 발생 반전 팩트가 이 지표 도표에서 폭로 드러납니다! 그림을 자세히 보십쇼! 전자(former) 에 해당하는 포아송 마술 무기 파편의 결과 데이터 점들 덩어리는 스탯 통계상 아예 마이너스 음수 바닥 아래로는 단 하나도 절대로 파편 존재 뚫지 못하고 떨어지지 않는 아주 기막힌 무조건 **비음수(non-negative)** 마지노선 배수진 한계 방어막 절대 영역 0 이상의 표면 위에서만 놀고 있습니다! 왜? 포아송은 카운트 세는 무기고 자전거 판매 수는 음수가 없으니까요! 반면 선형 기계는 멍청하게 "손님 마이너스 20명요!" 이러고 있죠! 

As a result the Poisson regression predictions tend to be larger than those from the linear model for either very low or very high levels of ridership.
그 기막힌 로직의 파생 구조 통계 도달 결과로(As a result)! 수요가 완전 폭망한 새벽(자전거 대여 수량이 아주 개박살 극저 단절 극단 산단으로 낮은 수준, very low) 구간 이나 눈코 뜰 새 없이 바쁜 파생 극한 정점 피크 러시 타임 극단 비율 산출(대여량이 아주 기형 특성 극점 폭풍 비율로 높은, very high) 두 극단 한계 특정 레벨의 날들 치 특이점 레벨(levels of ridership) 발생 단편 중 극단적 어느 상황 한 곳(either) 에 맞닥뜨리게 될 표본 경우엔! 포아송 회귀 표적 구동 예측치들은 무식한 아날로그 1차 선배 선형 모델 스탯 결괏값의 한 마디 도출 수치(those) 견적 보다도 훨씬 자기주장이 세게 좀 더 양적으로 과대 산출 수리 큰 숫자의 아주 과감한 타점 척도 스케일 결과 값 숫자로 불러 나타나는 극한 압박 확률 스텝 산단 편향적 치우침 이행 경향성 엑셀 파워(tend to be larger than) 지표 징후군 꼬리표를 팩트 단절로 아주 맹렬히 보여 갖게 됩니다! (마이너스를 쳐내는 포아송 탓에 극한점에 오면 오차가 확 불어나는 특성 팩트죠!)

In this section, we fit Poisson regression models using the `sm.GLM()` function with the argument `family=sm.families.Poisson()`.
자, 본 장의 통계 정리 요약 타임 이 특정 세션(In this section)! 우리는 여태 파이썬 매개 변수 칩인 옵션 포아송 탄창 `family=sm.families.Poisson()` 파라미터 조작 통계 인자(argument) 변수를 전격 옵션 조작 장착 투시 동반하여 저 거대 만능 장비포 통계 산포 무관 `sm.GLM()` 무기 패키지 함수를 거대 사용(using) 함으로써 본연의 이 멋진 카운팅 전문 무기인 포아송 파생 기반 이행 특수 회귀 통계 기계 모델들을 파편 훈련 강압 폼나게 편제 적합(fit)시켰습니다.

Earlier in this lab we used the `sm.GLM()` function with `family=sm.families.Binomial()` to perform logistic regression.
돌이켜 보세요! 우리는 본 광활한 기동 실습 거치 장(lab) 의 훨씬 아득한 아주 초반, 분류의 꽃이 로지스틱을 다루던 시절 이전 옛 단절 챕터(Earlier) 공정 중 훈련 단락 과거 기록 조작 파편에서도, 사실 모형 훈련 시 칩 만 `family=sm.families.Binomial()`(이항 분포 탄창 칩!) 으로 살짝 이빨만 갈아 끼워 조작 동반 지표를 기동 매개 변주 모델 인자로 단절 삼아서 방금 쓴 이 거대 몸통 본체인 공통 무식 범용 도구 단절 동일 함수 장비 `sm.GLM()` 기기를 사용해 로지스틱 회귀 판별을 도출 이행 단결 연산 실행(perform) 도달 시키기 위해 아주 다재다능하게 도출 파생 재사용(used) 우려먹었던 기록 이행이 동일 하게 존재 있었습니다. 이래서 패키지 함수 하나 잘 다루면 파생 이득 꿀을 엄청 납니다! 

Other choices for the `family` argument can be used to fit other types of GLMs.
이 이면 구조 시스템 맹점은 무엇? 즉, 입력 투사 파라미터 탄창 칩 장비인 `family` 옵션 선택 조작 입력 인자에 대한 기저 무구 개별 다양한 다른 변형 특수 임의 옵션 교차 스위치를 알아서 상황 맞춰 교체 배정 선택(Other choices) 변경 세팅 칩 교환 파편 제어 교체를 자유자재로 해 주면! 우리는 저 어마어마한 파편 통계 수단 거대 몸통 기능 한대로, 기타 아예 전혀 다른 파생 성향 종류의 미친 듯이 다양한 분기 유형 타점 모델 복합 GLM 머신 모델 통계 전파 적합 유도 기동 구축 편제들을 통제 맞추기 지시 위해(to fit) 동일하게 한 기계 몸통으로 아주 폭넓게 우려먹어 무한 폭격 단절 투척 구동 도출 유용 융합 기동 무한 생성 응용 도출해 사용할(can be used) 이형 파편 지표 연동 가능성이 무궁무진 뻥 뚫려 있다는 대단한 시스템 조작 팩트 뜻이 됩니다!

For instance, `family=sm.families.Gamma()` fits a Gamma regression model.
무한 응용 특수 변환 확장 작동 팁 투사 예시를 하나만 더 투척 치환해 주자면(For instance)! 조작 엔진 함수 파라미터 조작 타점에 입력 세팅을 `family=sm.families.Gamma()` 특수 배정 세팅 파라미터 부품으로 끼워 넣고 스위치를 켜면? 당신은 즉시 아무 코딩 개조 없이 순식간에 아주 심오한 통계 기형적 특수 전진 감마 모델 타점 측정 **감마 회귀 치수 판별 모델(Gamma regression model)** 전용 특수 분석 장비 로보트로 옵션 조치 강압 적합 이행 모델 개조 마법 조작 구형 장비가 변신 구동(fits) 구축 기정 파생 촉발 작동 시킬 수 있습니다! 대단하죠? 이상 실험실 실습 무기 활용 코딩 해설을 마칩니다!

---

## Sub-Chapters

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans2.html) | [4.8 Exercises >](../../../4_8_exercises/trans2.html)

---
layout: default
title: "trans2"
---

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans2.html) | [4.8 Exercises >](../../../4_8_exercises/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# Poisson Regression 
# 푸아송 회귀(Poisson Regression): "마이너스 수요가 어딨어?" 현실 반영 폭격 모델!

Now we fit instead a Poisson regression model to the `Bikeshare` data. Very little changes, except that we now use the function `sm.GLM()` with the Poisson family specified: 
밋밋한 선형 회귀는 집어치우고, 드디어 **개수/카운트 측정의 절대 존엄 깡패, '푸아송 회귀(Poisson regression)'** 모델을 자전거 투기판에 박아 넣을 차례입니다. 기존의 로지스틱 회귀 쓸 때랑 다른 점은 거의 없습니다(Very little changes). 그냥 뼈대 함수인 `sm.GLM()` 소환진을 그릴 때, 옵션(family) 칸에다 "아, 맞다. 나 이번엔 푸아송 종족(Poisson family) 파벌 쓸래~" 라고 이름표만 스윽 꽂아(specified) 구동시키면 끝입니다.

```python
In [76]: M_pois = sm.GLM(Y, X2, family=sm.families.Poisson()).fit()
```

We can plot the coefficients associated with `mnth` and `hr`, in order to reproduce Figure 4.15. We first complete these coefficients as before. 
푸아송이 토해낸 녀석들로, 아까처럼 Figure 4.15(푸아송 버전 스코어 도표) 를 간지나게 복제해 그려보겠습니다. 그리기 전에 일단 `mnth` 와 `hr` 꼬리 칸에 아까처럼 "나머지 다 더해서 마이너스 곱박" 편법으로 숨겨진 스코어를 우겨넣어 퍼즐을 완성합니다(complete).

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
그림 그리는 붓질(plotting) 타임은 아까 선형 회귀 때 했던 짓거리랑 복붙 수준으로 징그럽게 똑같습니다.

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

We compare the fitted values of the two models. The fitted values are stored in the `fittedvalues` attribute returned by the `fit()` method for both the linear regression and the Poisson fits. The linear predictors are stored as the attribute `lin_pred`. 
과연 두 기계의 뇌구조는 어떻게 다를까요? 1차원 선형 회귀 막대기랑 카운트 괴물 푸아송 녀석이 각각 토해낸 예측 결과(적합값 fitted values) 를 맞짱 배틀 비교해 봅니다. 두 녀석 다 훈련(`fit()`) 을 참 잘 끝마치면, 언제나처럼 친절하게 `fittedvalues` 란 금고 속에 자기만의 예측 답안지 번호표들을 곱게 접어 저장해 줍니다 (참고로, 선형 예측 부품 덩어리는 `lin_pred` 란 방에 몰래 처박혀 있습니다).

```python
In [79]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(M2_lm.fittedvalues,
           M_pois.fittedvalues,
           s=20)
ax.set_xlabel('Linear Regression Fit', fontsize=20)
ax.set_ylabel('Poisson Regression Fit', fontsize=20)
ax.axline([0,0], c='black', linewidth=3, linestyle='--', slope=1);
```

The predictions from the Poisson regression model are correlated with those from the linear model; however, the former are non-negative. As a result the Poisson regression predictions tend to be larger than those from the linear model for either very low or very high levels of ridership. 
저 위 그래프 산점도를 째려보면, 푸아송 머신이 찍은 예측 타점들과 선형 막대기 머신이 찍은 타점들은 서로 꽤 죽이 잘 맞아 올라가는 상관관계(correlated) 를 보여줍니다. **하지만 여기서 존엄한 차이! 푸아송 녀석(전자) 은 절대 네버 "음수(마이너스값 non-negative)" 따위의 헛소리를 예측표로 토해내지 않습니다!!** (상식적으로 오늘 자전거빌린 놈이 마이너스 5명입니다! 란 게 말이 안 되잖아요?). 이 미친 현실 고증의 결과로, 거리의 자전거 인간들이 씨가 말라 미치도록 쪼그라든 핵 비수기(very low ridership) 라거나 반대로 수요가 미친 듯이 터져버린 초극강 성수기 구간(very high) 에 진입했을 때, 이 푸아송 예측선이 바닥으로 꺼지는 일직선 막대기 선형 모델의 예측 수치보다 항상 좀 더 뻥튀기 되어 큰(larger) 쪽으로 날뛰게 되는 보정 곡선을 그리는 경향이 심해집니다.

In this section, we fit Poisson regression models using the `sm.GLM()` function with the argument `family=sm.families.Poisson()`. Earlier in this lab we used the `sm.GLM()` function with `family=sm.families.Binomial()` to perform logistic regression. Other choices for the `family` argument can be used to fit other types of GLMs. For instance, `family=sm.families.Gamma()` fits a Gamma regression model.
정리 한 스푼! 우린 이번 판에서 `sm.GLM()` 함수 몸통의 가족 증명서(argument) 칸에다 떡하니 `family=sm.families.Poisson()` 파벌 이름을 때려 박음으로써 강력한 카운터 푸아송 마법을 시전했습니다. 아까 이 랩장 초반에 떡상/떡락 분류하던 그 시절엔 가문 이름을 `Binomial()` (이항 분포 파벌) 로 바꿔치기해서 로지스틱 회귀를 돌렸었죠? 이처럼 이 거대한 **GLM(일반화 선형 모델)** 용병 시스템은 저 `family` 가문 칸에다 무슨 부족 명판을 갈아 끼우느냐에 따라 각양각색의 돌연변이 괴물 회귀 머신들을 공장처럼 찍어냅니다. 덤으로 꿀팁 하나 더 주자면 저따가 심심하면 `family=sm.families.Gamma()` 감마 가문 명찰을 붙여서 감마(Gamma) 파벌 회귀 모델도 막막 빚어 돌릴 수 있습니다! (이게 바로 뷔페식 파이썬 코딩의 권력이죠!)

---

## Sub-Chapters

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans2.html) | [4.8 Exercises >](../../../4_8_exercises/trans2.html)

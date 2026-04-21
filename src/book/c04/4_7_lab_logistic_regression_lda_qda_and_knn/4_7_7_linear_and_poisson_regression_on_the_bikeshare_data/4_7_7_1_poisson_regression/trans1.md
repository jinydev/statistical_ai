---
layout: default
title: "trans1"
---

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans1.html) | [4.8 Exercises >](../../../4_8_exercises/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# Poisson Regression 
# 푸아송 회귀

Now we fit instead a Poisson regression model to the `Bikeshare` data. Very little changes, except that we now use the function `sm.GLM()` with the Poisson family specified: 
이제 우리는 대신 `Bikeshare` 데이터에 푸아송 회귀(Poisson regression) 모델을 피팅합니다. 이제 푸아송 패밀리(Poisson family)가 지정된 `sm.GLM()` 함수를 사용한다는 점을 제외하면 변하는 것은 거의 없습니다(Very little changes):

```python
In [76]: M_pois = sm.GLM(Y, X2, family=sm.families.Poisson()).fit()
```

We can plot the coefficients associated with `mnth` and `hr`, in order to reproduce Figure 4.15. We first complete these coefficients as before. 
우리는 Figure 4.15를 재현하기 위해 `mnth` 및 `hr` 와 관련된 계수 도표를 그릴(plot) 수 있습니다. 우리는 먼저 이전과 같이 이러한 계수들을 완성합니다.

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
도표 그리기(plotting)는 이전과 같습니다.

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
두 모델의 적합값(fitted values)을 비교합니다. 수집 적합값은 선형 회귀 및 푸아송 회귀 피팅 모두에 대해 `fit()` 메서드에 의해 반환된 `fittedvalues` 속성에 저장됩니다. 선형 예측 변수(linear predictors)는 `lin_pred` 속성으로 저장됩니다.

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
푸아송 회귀 모델의 예측은 선형 모델의 예측과 상관관계(correlated)가 있습니다. 그러나 전자(푸아송)는 음수가 아닙니다(non-negative). 그 결과 푸아송 회귀 예측은 이용자 수(ridership)가 매우 낮거나 매우 높은 수준에 대해 선형 모델의 예측보다 더 큰(larger) 경향이 있습니다.

In this section, we fit Poisson regression models using the `sm.GLM()` function with the argument `family=sm.families.Poisson()`. Earlier in this lab we used the `sm.GLM()` function with `family=sm.families.Binomial()` to perform logistic regression. Other choices for the `family` argument can be used to fit other types of GLMs. For instance, `family=sm.families.Gamma()` fits a Gamma regression model.
이 절(section)에서 우리는 `family=sm.families.Poisson()` 인수를 가진 `sm.GLM()` 함수를 사용하여 푸아송 회귀 모델을 피팅했습니다. 이 랩(lab)의 앞부분에서 우리는 로지스틱 회귀를 수행하기 위해 `family=sm.families.Binomial()` 과 함께 `sm.GLM()` 함수를 사용했습니다. `family` 인수에 대한 다른 선택들은 다른 유형의 GLM을 피팅하는 데 사용될 수 있습니다. 예를 들어, `family=sm.families.Gamma()` 는 감마(Gamma) 회귀 모델을 피팅합니다.

---

## Sub-Chapters

[< 4.7.7.1 Out69 1.53E-20](../4_7_7_1_out69_1.53e-20/trans1.html) | [4.8 Exercises >](../../../4_8_exercises/trans1.html)

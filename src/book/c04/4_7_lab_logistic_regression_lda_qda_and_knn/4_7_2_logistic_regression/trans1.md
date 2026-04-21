---
layout: default
title: "trans1"
---

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans1.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.2 Logistic Regression
# 4.7.2 로지스틱 회귀

Next, we will fit a logistic regression model in order to predict `Direction` using `Lag1` through `Lag5` and `Volume`.
다음으로, 우리는 `Lag1` 부터 `Lag5` 까지 그리고 `Volume`을 예측 변수로 사용하여 `Direction`을 예측하기 위해 최우선적으로 로지스틱 회귀 모델을 적합시킬 것입니다.

The `sm.GLM()` function fits _generalized linear models_, a class of models that includes logistic regression.
`sm.GLM()` 함수는 로지스틱 회귀를 포함하는 모델들의 한 클래스 부류인 **일반화 선형 모델(generalized linear models)**을 적합시킵니다.

Alternatively, the function `sm.Logit()` fits a logistic regression model directly.
대안적으로, `sm.Logit()` 함수는 다른 과정 없이 로지스틱 회귀 모델을 직접적으로 적합시킵니다.

The syntax of `sm.GLM()` is similar to that of `sm.OLS()`, except that we must pass in the argument `family=sm.families.Binomial()` in order to tell `statsmodels` to run a logistic regression rather than some other type of generalized linear model.
`sm.GLM()` 의 구문(syntax)은 `sm.OLS()` 의 구문과 유사하지만, 우리는 `statsmodels` 모듈 측에 다른 유형의 일반화 선형 모델이 아닌 바로 로지스틱 회귀를 실행하라고 알려주기 위해 `family=sm.families.Binomial()` 이라는 매개변수 인자(argument)를 강제적으로 전달해야만 한다는 점이 예외적으로 다릅니다.

```python
In [7]: allvars = Smarket.columns.drop(['Today', 'Direction', 'Year'])
        design = MS(allvars)
        X = design.fit_transform(Smarket)
        y = Smarket.Direction == 'Up'
        glm = sm.GLM(y,
                     X,
                     family=sm.families.Binomial())
        results = glm.fit()
        summarize(results)
```

```python
Out[7]:
```

| | `coef` | `std err` | `z` | `P>\|z\|` |
|---|---|---|---|---|
| `intercept` | `-0.1260` | `0.241` | `-0.523` | `0.601` |
| `Lag1` | `-0.0731` | `0.050` | `-1.457` | `0.145` |
| `Lag2` | `-0.0423` | `0.050` | `-0.845` | `0.398` |
| `Lag3` | `0.0111` | `0.050` | `0.222` | `0.824` |
| `Lag4` | `0.0094` | `0.050` | `0.187` | `0.851` |
| `Lag5` | `0.0103` | `0.050` | `0.208` | `0.835` |
| `Volume` | `0.1354` | `0.158` | `0.855` | `0.392` |

The smallest _p_-value here is associated with `Lag1`.
얻어낸 결과 엑셀 표에서 가장 작은 **p-값(_p_-value)**은 가장 최근 시간차 단서인 `Lag1` 과 연관되어 있습니다.

The negative coefficient for this predictor suggests that if the market had a positive return yesterday, then it is less likely to go up today.
이 예측 변수(`Lag1`) 자체에 찍혀 나온 음수(negative)의 계수는 만약 다루는 관측 주식 시장이 바로 전날 어제 긍정적인(positive) 상승 수익률을 기록했다면, 그 반작용으로써 정작 오늘 그것이 올라가 상승할(go up) 가능성이 더 낮아질 것이라는 통계 패턴 점을 시사합니다.

However, at a value of 0.15, the _p_-value is still relatively large, and so there is no clear evidence of a real association between `Lag1` and `Direction`.
그러나 안타깝게도 0.15라는 값 수치에서, 그 p-값은 수학적으로 보았을 때 여전히 절대치로 상대적으로 큰 수준이며, 따라서 겉보기와 달리 `Lag1` 과 `Direction` 방향성 변성 사이의 진짜 팩트 실질적인 연관성(association)에 대한 통계상 명확한 증거 규칙성 자체는 이 자료상 전혀 없습니다 나타나지 않습니다.

We use the `params` attribute of `results` in order to access just the coefficients for this fitted model.
우리는 이 도출 적합된 모델에 대해 단지 계수 숫자 부품들에게만 따로따로 접근해 떼어보기 위해 추후 분석에서 `results` 판정 결과 객체 의 내부 속성인 `params` 속성을 사용합니다.

---

## Sub-Chapters

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans1.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans1.html)

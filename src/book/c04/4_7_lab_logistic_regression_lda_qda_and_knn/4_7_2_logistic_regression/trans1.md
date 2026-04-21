---
layout: default
title: "trans1"
---

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans1.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.2 Logistic Regression
# 4.7.2 로지스틱 회귀

Next, we will fit a logistic regression model in order to predict `Direction` using `Lag1` through `Lag5` and `Volume` . The `sm.GLM()` function fits _generalized linear models_ , a class of models that includes logistic regression. Alternatively, the function `sm.Logit()` fits a logistic regression model directly. The syntax of `sm.GLM()` is similar to that of `sm.OLS()` , except that we must pass in the argument `family=sm.families.Binomial()` in order to tell `statsmodels` to run a logistic regression rather than some other type of generalized linear model. 
다음으로, 우리는 `Lag1` 부터 `Lag5` 및 `Volume` 을 사용하여 `Direction` 을 예측하기 위해 로지스틱 회귀 모델을 피팅할 것입니다. `sm.GLM()` 함수는 로지스틱 회귀를 포함하는 모델의 클래스인 _일반화 선형 모델(generalized linear models)_ 을 피팅합니다. 대안으로, `sm.Logit()` 함수는 로지스틱 회귀 모델을 직접 피팅합니다. `sm.GLM()` 의 구문(syntax)은 `sm.OLS()` 의 구문과 유사하지만, 다른 유형의 일반화 선형 모델이 아닌 로지스틱 회귀를 실행하도록 `statsmodels` 에 지시하기 위해 `family=sm.families.Binomial()` 인수를 전달해야 한다는 점이 다릅니다.

```python
In [7]:allvars=Smarket.columns.drop(['Today','Direction','Year'])
design=MS(allvars)
X=design.fit_transform(Smarket)
y=Smarket.Direction=='Up'
glm=sm.GLM(y,
X,
family=sm.families.Binomial())
results=glm.fit()
summarize(results)
```

```python
Out[7]:
```

||`coef`|`std err`|`z`|`P>|z|`|
|---|---|---|---|---|
|`intercept `|`-0.1260`|`0.241`|`-0.523`|`0.601`|
|`Lag1`|`-0.0731`|`0.050`|`-1.457`|`0.145`|
|`Lag2`|`-0.0423`|`0.050`|`-0.845`|`0.398`|
|`Lag3`|`0.0111`|`0.050`|`0.222`|`0.824`|
|`Lag4`|`0.0094`|`0.050`|`0.187`|`0.851`|
|`Lag5`|`0.0103`|`0.050`|`0.208`|`0.835`|
|`Volume`|`0.1354`|`0.158`|`0.855`|`0.392`|

The smallest _p_-value here is associated with `Lag1` . The negative coefficient for this predictor suggests that if the market had a positive return yesterday, then it is less likely to go up today. However, at a value of 0.15, the _p_-value is still relatively large, and so there is no clear evidence of a real association between `Lag1` and `Direction` . 
여기서 가장 작은 _p_-value는 `Lag1` 과 연관되어 있습니다. 이 예측 변수에 대한 음의 계수는 어제 시장 수익률이 양수였다면 오늘 시장이 상승할 가능성이 적음을 시사합니다. 그러나 0.15의 값에서 _p_-value는 여전히 상대적으로 크며, 따라서 `Lag1` 과 `Direction` 사이의 실질적인 연관성에 대한 명확한 증거(evidence)는 없습니다.

We use the `params` attribute of `results` in order to access just the coefficients for this fitted model. 
우리는 이 피팅된 모델에 대한 계수에만 접근하기 위해 `results` 의 `params` 속성을 사용합니다.

---

## Sub-Chapters

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans1.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans1.html)

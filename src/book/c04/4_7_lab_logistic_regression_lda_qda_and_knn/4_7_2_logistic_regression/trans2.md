---
layout: default
title: "trans2"
---

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans2.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.2 Logistic Regression
# 4.7.2 로지스틱 회귀 분석: 확률 배팅의 꽃, 시장의 오르내림을 맞춰라!

Next, we will fit a logistic regression model in order to predict `Direction` using `Lag1` through `Lag5` and `Volume` . The `sm.GLM()` function fits _generalized linear models_ , a class of models that includes logistic regression. Alternatively, the function `sm.Logit()` fits a logistic regression model directly. The syntax of `sm.GLM()` is similar to that of `sm.OLS()` , except that we must pass in the argument `family=sm.families.Binomial()` in order to tell `statsmodels` to run a logistic regression rather than some other type of generalized linear model. 
자, 다음 스테이지입니다! 이번엔 전설의 타짜 머신, **로지스틱 회귀 모델**을 등판시켜서 어제그제 시장 지표인 `Lag1` 부터 `Lag5` 까지의 힌트 변수들과 거래 덩치 `Volume` 을 모조리 불태워 오늘 주식이 떡상할지(`Up`) 떡락할지(`Down`) 결정 짓는 팻말 변수 `Direction` 을 족집게처럼 예측하는 세팅을 맞춰보겠습니다. 파이썬 마법 주문인 `sm.GLM()` 함수는 이 구역의 지배자, **일반화 선형 모델(Generalized Linear Models, GLM)** 이라는 거대 폭격기 클래스를 통째로 장착하는 무기입니다. (당연히 로지스틱 회귀도 이 GLM 가문 소속입니다.) 귀찮으면 아예 직빵으로 로지스틱 회귀 모델 전용 타격기인 `sm.Logit()` 함수를 빼 들어 찍어 눌러도 됩니다. 우리가 쓸 `sm.GLM()` 파이썬 코딩 주문의 문법 구조(syntax) 자체는 옛날 3장에서 지겹게 치던 평범한 회귀 `sm.OLS()` 때와 완전 붕어빵처럼 똑같습니다. 단, 차이가 딱 하나 있다면 치명적인 괄호 안의 옵션 암호! 반드시 `family=sm.families.Binomial()` 이라는 베르누이 마법의 가문 동전 던지기 인수를 던져 넣어서 파이썬 `statsmodels` 엔진 녀석에게 "어이 멍청아, 다른 GLM 모델 말고 로지스틱 회귀로 피가 튀게 굴려라!" 라고 멱살 잡고 정확히 강제 지시해야 한다는 점입니다.

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
이 처참한 살육의 성적표(회귀 결과 표)를 볼까요? 여기서 가장 숫자가 바닥을 기는 제일 작은 _p_-value(통계적 신용도 척도) 점수는 `Lag1` 녀석이 차지했습니다. 근데 이 녀석 앞에 붙은 계수 표식(`coef`) 숫자가 기분 나쁜 **음수(-0.0731)** 임을 똑똑히 눈여겨보십시오! 이게 뭘 뜻하느냐? "만약 어제 시장 분위기가 뜨끈하게 불장(+) 상승세를 탔다면, 반대로 오늘 시장 지수는 위로 치고 올라갈 확률이 오히려 꼬꾸라진다(less likely)!" 라는 냉정한 반전 심리를 시사합니다. 하지만 떡 줄 사람은 생각도 않는데 김칫국 마시지 마시길! 저 p-value 수치가 아무리 꼴찌라도 무려 **0.15** 라는 크고 비대한 뚱보 덩치를 자랑하고 있습니다! (보통 0.05 이하는 돼야 와 진짜다 믿죠). 팩트 체킹! 결과적으로 이 0.15란 숫자는 여전히 터무니없이 큰 오차 덤탱이 확률이므로, 어제 수익률(`Lag1`)과 오늘의 장 방향성(`Direction`) 사이에 뭔가 대단한 진짜 영적인 끈끈한 현실 연관성이 존재한다는 확실하고 뼈 때리는 물증(evidence) 따위는 눈을 씻고 찾아봐도 없다는 허무한 결론이 폭발합니다.

We use the `params` attribute of `results` in order to access just the coefficients for this fitted model. 
참고로 위에 쏟아진 번잡한 쓰레기 텍스트 말고 엑기스인 요 계수(coefficient) 숫자 부품 타깃만 깔끔하게 털어서 주머니에 넣고 싶다면, 피팅된 결과물 `results` 뭉치에다가 `params` 라는 속성 해킹 도구를 꽂아 넣어 바로 접근 추출하면 그만입니다.

---

## Sub-Chapters

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans2.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans2.html)

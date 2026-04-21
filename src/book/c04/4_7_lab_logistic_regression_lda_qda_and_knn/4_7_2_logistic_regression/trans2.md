---
layout: default
title: "trans2"
---

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans2.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.2 Logistic Regression
# 4.7.2 전투기 발진: 스피드 깡패 로지스틱 회귀 가동

Next, we will fit a logistic regression model in order to predict `Direction` using `Lag1` through `Lag5` and `Volume`.
주식 시장 관찰이 대충 끝났으니, 이제 가장 기본적이고 만만한 스피드 깡패 무기, **로지스틱 회귀(Logistic Regression)** 모델을 조립해서 투입해 봅시다. 이 녀석의 미션은 과거 5일 치 기록인 `Lag1` ~ `Lag5`, 그리고 지난 거래량 `Volume` 이라는 탄창 힌트들을 이용해, 오늘의 주식 방향이 상승할지 하락할지 도박 결과를 치는 `Direction` 과녁을 정확히 맞추는 겁니다!

The `sm.GLM()` function fits _generalized linear models_, a class of models that includes logistic regression.
이때 파이썬의 `statsmodels` 공구함에서 꺼내 쓰는 핵심 망치가 바로 `sm.GLM()` 함수입니다. 얘는 앞서 우리가 배운 '일반화 선형 모델(GLM)' 이라는 거대한 시스템 자체를 굴리는 만능 조종석이죠! 당연히 조폭 같은 로지스틱 회귀도 이 거대한 모델 클래스의 식구 중 하나 소속이기 때문에 이 망치로 때려 맞출 수 있습니다.

Alternatively, the function `sm.Logit()` fits a logistic regression model directly.
뭐, 이게 귀찮으면 그냥 묻고 따지지도 않고 대놓고 "로지스틱 전용 망치!"인 `sm.Logit()` 함수를 직접 휘둘러서 다이렉트로 때려 맞추는 방법도 있긴 합니다. 

The syntax of `sm.GLM()` is similar to that of `sm.OLS()`, except that we must pass in the argument `family=sm.families.Binomial()` in order to tell `statsmodels` to run a logistic regression rather than some other type of generalized linear model.
만능 GLM 조종석인 `sm.GLM()` 을 조종하는 방법은 예전에 통나무 선형 회귀에서 썼던 `sm.OLS()` 구문과 뼈대가 판박이처럼 쏙 빼닮아 아주 다루기 친숙합니다. 단, 한 가지 주의할 치명적 예외가 있죠. GLM은 '우주 만능 기계'라서, 우리가 굳이 수식 맨 끝에 **`family=sm.families.Binomial()` (베르누이 도박 가문 코인)** 이라는 비밀 치트키 암호(argument)를 입력해 줘야만 기계가 "아항~ 다른 이상한 기동이 아니라, 지금 당장 동전 뒤집기 확률 싸움인 '로지스틱 회귀'로 변신해서 세팅을 굴리라는 뜻이구나!" 하고 찰떡같이 알아먹고 실행을 칩니다.

```python
In [7]: allvars = Smarket.columns.drop(['Today', 'Direction', 'Year']) # 쓸데없는 과녁판(정답, 년도) 힌트는 싹 빼고 찐 단서 탄환만 장전!
        design = MS(allvars) # 모델 조립 도면 그리기
        X = design.fit_transform(Smarket) # 도면에 맞춰 장전물(X) 장착!
        y = Smarket.Direction == 'Up' # 과녁판(Y)은 '올라간다(Up)'를 맞추면 1(True)!
        glm = sm.GLM(y,
                     X,
                     family=sm.families.Binomial()) # 베르누이 코인을 꽂아서 로지스틱 변신! 발사!
        results = glm.fit() # 훈련장에 던져 넣고 뺑뺑이 돌리기 
        summarize(results) # 기계가 토해낸 전투 성적표 요약하기
```

```python
Out[7]:
```

| | `coef` (가중치 계수 파워) | `std err` | `z` | `P>\|z\|` (거짓말 확률 p-value) |
|---|---|---|---|---|
| `intercept` (기본 세팅 점수 타점) | `-0.1260` | `0.241` | `-0.523` | `0.601` |
| `Lag1` (어제 주가) | `-0.0731` | `0.050` | `-1.457` | `0.145` |
| `Lag2` (그제 주가) | `-0.0423` | `0.050` | `-0.845` | `0.398` |
| `Lag3` | `0.0111` | `0.050` | `0.222` | `0.824` |
| `Lag4` | `0.0094` | `0.050` | `0.187` | `0.851` |
| `Lag5` | `0.0103` | `0.050` | `0.208` | `0.835` |
| `Volume` | `0.1354` | `0.158` | `0.855` | `0.392` |

The smallest _p_-value here is associated with `Lag1`.
자, 기계가 뱉어낸 이 무시무시한 성적표(계수표)에서 가장 중요한 건 오른쪽 끝에 있는 거짓말 확률(p-value)을 나타내는 **`P>|z|`** 열입니다. 숫자가 눈곱만치 작을수록 그 힌트(변수)가 진또배기라는 뜻인데, 여기서 제일 숫자가 작은 에이스 타자는 바로 어제 주가 정보인 `Lag1` (0.145) 로 판명 났습니다.

The negative coefficient for this predictor suggests that if the market had a positive return yesterday, then it is less likely to go up today.
이 예측 변수 `Lag1` 옆에 찍힌 가중치 `coef` 값이 오싹하게도 마이너스 영하권(`-0.0731`) 결괏값 계수인 것에 주목해 볼까요? 이 통계 기계는 무시무시한 패턴의 의미를 꼬집고 있습니다. "만약 어쩌다 주식 시장이 '어제' 미친 듯이 긍정적 단서로 상승 불기둥 수익(positive)을 뿜었다면, 정작 그 이면의 패턴 역풍으로 '오늘' 또 연속으로 상승 연타(go up)를 칠 확률은 오히려 바닥으로 확 고꾸라진다!" 라는 냉혹한 주식장 심리 역설 징조를 시사해 분석한 겁니다. 어제 먹었으면 오늘은 토해낸다는 거죠!

However, at a value of 0.15, the _p_-value is still relatively large, and so there is no clear evidence of a real association between `Lag1` and `Direction`.
**하지~만!** 뼈를 스치는 진리가 숨어있습니다. 그 '제일 작은' p-값이라 치켜세웠던 놈조차 수치가 0.15 언저리에서 놀고 있습니다. 통계 바닥에서 이 정도 수치는 "응, 그냥 이거 어쩌다 다 운빨 뽀록이야~" 라고 취급될 만큼 여전히 엄청 뚱뚱하고 상대적으로 멍청하게 큰 불량 수치(large)입니다. 따라서, 현실 팩트로 까놓고 보면 `Lag1`(어제 주가) 정보를 가지고 `Direction`(오늘 오를지 내릴지) 방향성 변수 짝짝꿍을 진짜 맞출 수 있다는 그 어떠한 명확한 증거(clear evidence)도 이 데이터표 상엔 존재하지 않습니다. 쓰레기 데이터 파편이라는 겁니다.

We use the `params` attribute of `results` in order to access just the coefficients for this fitted model.
나중에 뒷단 코딩에서 우리가 이 훈련된 깡패 기계 모델의 성적표 중 저 복잡한 표를 다 버리고 오직 엑기스인 "가중치 부품(계수)" 스코어 점수판만 쏙! 빼내오고 싶을 때, 우리는 쿨하게 `results` 객체 옆구리에 점 찍고 붙어있는 `.params` 라는 추출 속성(attribute) 버튼을 눌러 꺼내 쓸 수 있습니다. 아주 유용하죠!

---

## Sub-Chapters

[< 4.7.1 The Stock Market Data](../4_7_1_the_stock_market_data/trans2.html) | [4.7.2.1 In 8 Results.Params >](4_7_2_1_in_8_results.params/trans2.html)

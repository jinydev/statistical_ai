---
layout: default
title: "trans2"
---

[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/trans2.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3 Logistic Regression
# 4.3. 로지스틱 회귀 (확률을 구부려 맞히는 마법)

Consider again the `Default` data set, where the response `default` falls into one of two categories, `Yes` or `No`.
아까 봤던 카드 빚 체납 모의실험 `Default` 데이터셋을 다시 거듭 째려보며 생각해 보겠습니다. 여기서 우리가 맞혀야 할 표적 범인, 즉 종속 반응 변수 `default`(체납 여부)는 `Yes(배 짼다)` 와 `No(잘 갚는다)` 라는 극단적인 두 가지 카테고리 중 단연 하나로 칼같이 떨어져 꽂힙니다(falls into).

Rather than modeling this response $Y$ directly, logistic regression models the _probability_ that $Y$ belongs to a particular category.
**로지스틱 회귀(Logistic Regression)** 마법의 핵심 비결은 이렇습니다: 무식하게 직선을 그어 반응 변수 $Y$ 자체를 "1번이다, 2번이다" 직접적으로 딱 부러지게 모델링 시뮬레이션하려는 멍청한 시도를 버리는 대신, $Y$가 특정 범죄 카테고리에 속하게 될 **'확률(Probability)'** 그 자체의 게이지를 교묘하게 모델링하고 구부려 맞춰냅니다.

For the `Default` data, logistic regression models the probability of default.
이 `Default` 카드 빚 데이터의 경우, 로지스틱 회귀 요원은 타깃이 파산할 '확률' 자체를 하나의 수식 함수로 유연하게 짭니다.

For example, the probability of default given `balance` can be written as
예를 들어, 탐문 조사된 어떤 이의 현재 잔고(`balance`) 스펙이 주어졌을 때 이 녀석이 파산할 치명적 확률은 다음과 같이 수려하게 작성될 공산을 가집니다:

$$
p(\text{balance}) = \text{Pr}(\text{default} = \text{Yes} \mid \text{balance})
$$

The values of Pr(`default` = `Yes` $\mid$ `balance`), which we abbreviate $p(\text{balance})$, will range between 0 and 1.
우리가 너무 기니까 짧게 가오 살려 $p(\text{balance})$ 라고 줄여서 부를 이 수치 지표, 즉 '잔고를 털어보니 체납(`default`)이 `Yes`일 확률' 결과값 부분은, 이제 미친 듯이 치솟지 않고 언제나 안전하게 0(0%)과 1(100%)이라는 상식적인 확률 박스 구간 사이에서만 안착해 얌전히 변동(range)하게 될 것입니다.

Then for any given value of `balance` , a prediction can be made for `default`.
그러면 이제 어떤 특정한 고객의 `balance` 조달 거액 값이 떡 하니 주어지든, 우리는 확률 수위를 보고 체납 폭탄 `default` 여부에 대한 족집게 예측을 시원하게 내릴 무기를 갖게 될 수 있습니다.

For example, one might predict default = Yes for any individual for whom $p(\text{balance}) > 0.5$.
예를 들어 깡다구가 있는 어떤 카드사는 단지 $p(\text{balance}) > 0.5$ (50%)를 감지 차단벽으로 넘나드는 모든 타깃 개인들에 대해서 "이놈은 파산 = Yes 다!" 라고 화끈하게 쳐내어 예측할 수 있습니다.

Alternatively, if a company wishes to be conservative in predicting individuals who are at risk for default, then they may choose to use a lower threshold, such as $p(\text{balance}) > 0.1$.
한편 반대 대안으로, 만약 어떤 쫄보 카드 회사가 파산 위험군 블랙 대상 개인들을 모조리 솎아내 예측하는 방면에서 지극히 보수적이고 엄청 엄격하게 굴길 단연 간절 원한다면 어떨까요? 그들은 아마도 $p(\text{balance}) > 0.1$ (고작 10% 위험만 있어도 아웃!) 와 같은 훨씬 더 가혹하고 낮은 차원의 커트라인 감시망 기준치(Threshold) 장벽을 내걸고 구태 사냥 사용하는 특단 조치를 취하려 선택 조처할 수도 있습니다.

---

### 4.3.1 The Logistic Model (로지스틱 모형)

### 4.3.2 Estimating the Regression Coefficients (회귀 계수 추정)

### 4.3.3 Making Predictions (예측하기)

### 4.3.4 Multiple Logistic Regression (다중 로지스틱 회귀)

### 4.3.5 Multinomial Logistic Regression (다항 로지스틱 회귀)

---

## Sub-Chapters

[< 4.2 Why Not Linear Regression](../4_2_why_not_linear_regression/trans2.html) | [4.3.1 The Logistic Model >](4_3_1_the_logistic_model/trans2.html)

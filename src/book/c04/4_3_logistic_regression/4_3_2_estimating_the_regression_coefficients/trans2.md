---
layout: default
title: "trans2"
---

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans2.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.2 Estimating the Regression Coefficients
# 4.3.2. 회귀 계수 추정 (정답 찾아 맞추기 게임)

The coefficients $\beta_0$ and $\beta_1$ in (4.2) are unknown, and must be estimated based on the available training data.
아까 보았던 거대한 로지스틱 함수 식 (4.2)의 동력원인 계수 $\beta_0$ 번과 $\beta_1$ 번은, 현재 우리가 정체를 완전히 알 수 없는 미지의 블랙박스 값이며 어떻게든 오로지 주어진 훈련 데이터를 요리조리 분석하여 역으로 찾아내(추정해) 맞춰야만 하는 과제입니다.

In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients.
지난 3장 시절, 우리는 직선의 선형 회귀에 숨어있던 범인 계수를 추적하기 위해 '최소 제곱법'이라는 오차 줄이기 마법 기술을 사용했었습니다.

Although we could use (non-linear) least squares to fit the model (4.4), the more general method of _maximum likelihood_ is preferred, since it has better statistical properties.
여기 곡선의 세계(4.4)에서도 (비선형) 최소 제곱법을 억지로 우겨넣어 빙빙 돌릴 순 있겠지만 통계학자들은 단연코 기각합니다. 대신 **최대 우도법(maximum likelihood)** 이라는 훨씬 더 범용적이고 우아한 통계적 방어력을 지닌 대체 기법을 무기로 삼아 선호하는 편입니다.

The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_0$ and $\beta_1$ such that the predicted probability $\hat{p}(x_i)$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status.
이 거창한 '최대 우도법'을 로지스틱 회귀에 끼워 맞추는 뒤편의 기본 아이디어 직관은 아주 상식적이고 심플합니다: 우리는 $\beta_0$ 와 $\beta_1$ 퍼즐 조각을 찾을 때, 식 (4.2)를 통해 내놓은 수학적 예측 파산 확률 $\hat{p}(x_i)$ 가, 내 눈앞에 앉은 그 환자의 진짜 파산 여부 상태 (관측값) 와 영혼의 단짝처럼 최고로 완벽하게 딱 달라붙도록 만들 궁리를 하는 겁니다.

In other words, we try to find $\hat{\beta}_0$ and $\hat{\beta}_1$ such that plugging these estimates into the model for $p(X)$, given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not.
즉 대놓고 말해서, 이 추정치 퍼즐 조각들을 (4.2) 모형 기계 $p(X)$ 에 무더기로 쑤셔 넣었을 때, 진짜로 파산 늪에 빠진 우울한 고객들에게는 "1(100%)"에 미친 듯 가깝게 숫자를 토해내고, 멀쩡하게 빚을 잘 갚은 평화로운 사람들에겐 "0(0%)"에 바닥을 기게 숫자를 뱉어내게 만드는, 그 마법의 황금비율 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 을 기어코 샅샅이 뒤져 찾아내고자 시도하는 것입니다.

This intuition can be formalized using a mathematical equation called a _likelihood function_:
이 상식적인 직관 욕심은, 두통을 유발하는 **우도 함수(likelihood function)** 라는 다음과 같은 수식 기호를 통해 엄숙하게 공식화됩니다:

$$
\ell(\beta_0, \beta_1) = \prod_{i: y_i=1} p(x_i) \prod_{i^{\prime}: y_{i^{\prime}}=0} (1 - p(x_{i^{\prime}})) \quad (4.5)
$$

The estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ are chosen to _maximize_ this likelihood function.
우리의 주인공 예측 추정치 모자 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 은, 오로지 이 거대한 우도 함수의 총결산 수치를 우주 끝까지 멱살 잡고 끌어올려 **최대화(maximize)** 시켜버리는 챔피언 값으로 채택 결정됩니다.

Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book.
최대 우도 추정법은 이 책 내내 우리를 괴롭힐 숱하게 등장하는 수많은 비선형 굴곡진 모델들을 냅다 데이터에 피팅해버릴 때 전천후로 쓰이는 매우 일반적인 국밥 같은 접근법입니다.

In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood.
비밀을 폭로하자면, 3장 선형 회귀 동네에서 썼던 그 잘난 최소 제곱법조차도, 사실 알고 보면 이 거대한 '최대 우도법'의 아주 쪼그만 하위 특별 케이스(special case) 잔가지 하나에 불과합니다.

The mathematical details of maximum likelihood are beyond the scope of this book.
하지만 안심하십시오. 이 최대 우도를 손으로 직접 미적분해 갈라치는 끔찍한 수학적 세부 증명은, 다행히도 이 교재가 감당할 한계 범위를 아득히 벗어납니다.

However, in general, logistic regression and other models can be easily fit using statistical software such as `R` or `Python`, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.
요즘 세상에선 로지스틱 회귀든 머신러닝 모델이든 `R`이나 `Python(파이썬)` 같은 천재적인 통계 소프트웨어에 데이터만 던져주면 명령어 한 줄로 1초 만에 내부적으로 손쉽게 돌아가 피팅되기 때문에, 우리는 굳이 뒷단의 최대 우도 수학 연산 적합 절차에 지레 겁먹고 속을 끓일 하등의 염려 필요가 없습니다.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the `Default` data in order to predict the probability of `default = Yes` using `balance` .
표 4.1의 성적표는 지갑 잔고(`balance`) 정보만을 가지고 불길한 파산 `default = Yes` 확률을 예측하려는 목적으로 `Default` 모의 데이터에 로지스틱 모형을 신나게 돌려본 뒤 얻어낸 최종 계수 결괏값 추정치 및 그 주변 신상 통계 정보들을 줄줄이 보여줍니다.

We see that $\hat{\beta}_1 = 0.0055$; this indicates that an increase in `balance` is associated with an increase in the probability of `default`.
여기서 $\hat{\beta}_1 = 0.0055$ 로 떴습니다. 양수죠? 즉, 내 통장 빚 잔고(`balance`)가 한 푼 두 푼 늘어날수록 통계학적으로 얄짤없이 파산(`default`) 확률도 가파르게 증가하는 죽음의 늪 양상과 연관되어 있음을 덤덤히 지시해 줍니다. 

To be precise, a one-unit increase in `balance` is associated with an increase in the log odds of `default` by 0.0055 units.
수식적으로 현미경을 들이대서 극도로 정확히 꼬집자면, 잔고가 1달러 1단위 증가할 때 우리의 파산 확률 자체가 오르는 게 아니라 파산의 **로그 오즈(log odds)** 지수가 0.0055 단위 치수만큼 스멀스멀 늘어나는 기계 메커니즘과 연동된다는 뜻입니다.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3.
놀랍게도 표 4.1에 출력된 로지스틱 패널 표의 상당수 검증 항목 지표들은, 과거 3장에서 줄기차게 봤던 친숙한 선형 회귀 성적표 아웃풋 모양새와 거의 판박이처럼 유사합니다.

For example, we can measure the accuracy of the coefficient estimates by computing their standard errors.
예를 들면, 추정치 옆에 껌딱지처럼 늘 붙어 다니는 표준 오차(SE)를 측정 계산해서, 이 계수 수치가 얼마나 믿을만한지 흔들림 정확도를 가늠해 보는 짓도 그대로 할 수 있습니다.

The _z_-statistic in Table 4.1 plays the same role as the _t_-statistic in the linear regression output.
표 4.1 중간에 떡 하니 박혀있는 **z-통계량(z-statistic)** 은, 선형 회귀 출력표에서 심판관 역할을 했던 **t-통계량(t-statistic)** 과 완벽히 영혼의 투톱 쌍둥이 역할을 수행합니다.

For instance, the _z_-statistic associated with $\beta_1$ is equal to $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$, and so a large (absolute) value of the _z_-statistic indicates evidence against the null hypothesis $H_0 : \beta_1 = 0$.
단순하게 $\beta_1$ 에 붙어있는 z-통계량 심판 점수는 자기 값 나누기 표준오차 $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$ 를 투박하게 한 수치이며, 이게 (부호를 떼고 절댓값으로 봐도) 무지무지하게 거대한 값이라는 것은, 속 터지는 억지 주장인 귀무 가설 $H_0 : \beta_1 = 0$ (즉 "잔고랑 파산은 아무 상관없다!"는 헛소리)을 가차 없이 산산조각 낼 강력 발언 증거가 된다는 걸 뜻합니다.

This null hypothesis implies that the probability of `default` does not depend on `balance` .
(이 답답한 귀무 가설 녀석의 속뜻은 파산(`default`) 확률이 지갑(`balance`) 두께 따위에는 전혀 1도 의존하지 않는다고 우기는 것입니다).

Since the _p_-value associated with `balance` in Table 4.1 is tiny, we can reject $H_0$.
다행히도 표 4.1에서 `balance` 에 뜬 *p*-값이 소수점 한참 아래인 코딱지만큼(tiny) 매우 무시무시하게 작게 떴기 때문에, 우리는 속 시원히 이 망상가 $H_0$ 를 발로 차서 기각(reject)해 버릴 수 있습니다.

In other words, we conclude that there is indeed an association between `balance` and probability of `default`.
속되게 한 줄로 요약하면, 통장 빚 잔고 지표(`balance`)와 파산 멸망(`default`) 확률 간에는 변명의 여지 없는 실제 연관 관계가 단단히 결속되어 있다는 결론 도장에 마침내 쾅 쐐기를 박는 순간입니다.

The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).
추가로, 표 상단에 박힌 추정된 절편(intercept) 상수 수치 자체는 보통 과학자들의 이목과 관심 밖 찌꺼기 영역입니다. 요 녀석의 존재 이유는 그저 데이터를 쫙 펼쳤을 때 예측 모델의 한가운데 평균 적합도를 진짜 원본 데이터 내 파산자 전체 퍼센티지(여기서는 전체 고객 3% 파산율 기초 기준점) 비율과 엇비슷하게 영점 튜닝 사격하여 끼워 맞추는 조정 용도일 뿐입니다.

This is the document for this topic.
이것은 폭발적인 주제에 대한 문서입니다.

---

## Sub-Chapters

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans2.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans2.html)

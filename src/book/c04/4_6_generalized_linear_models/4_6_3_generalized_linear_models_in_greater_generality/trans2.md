---
layout: default
title: "trans2"
---

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.3 Generalized Linear Models in Greater Generality
# 4.6.3 더 넓은 우주로의 확장: 궁극의 변신 로봇 '일반화 선형 모델 (GLM)'의 모든 것

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics:
자, 지금까지 우리는 험난한 통계 전장을 구르며 선형 회귀, 로지스틱 회귀, 그리고 아까 막 등장한 포아송 회귀라는 세 가지 막강한 예측 병기들을 다뤄봤습니다. 겉보기엔 각자 노는 세계(연속된 숫자, 사과/배 찍기, 개수 카운트)가 전혀 달라 보이지만, 놀랍게도 이 세 용사들의 뼛속 DNA 구조를 뜯어보면 아주 소름 끼치게 동일한 평행 이론 공통점들을 공유하고 있습니다:

1. Each approach uses predictors $X_1, \dots, X_p$ to predict a response $Y$. We assume that, conditional on $X_1, \dots, X_p$, $Y$ belongs to a certain family of distributions. For linear regression, we typically assume that $Y$ follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$ follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$ follows a Poisson distribution.
1. 세 녀석 모두 입력 힌트(예측 변수) $X_1, \dots, X_p$ 총알들을 장전해서 무조건 타깃 정답 $Y$ 를 추적 격추(예측)한다는 본질적 미션이 똑같습니다. 단지 그들이 적을 조준할 때, 조건부 $X$ 힌트를 깔고 봤을 때 저 $Y$ 녀석이 "어떤 종특(분포 가문)의 피가 흐르는가?" 에 대한 신앙만 달랐을 뿐이죠. **선형 회귀**는 "내 적 $Y$ 는 무조건 우산 모양의 가우시안(정규 분포) 고상한 가문 출신이야!" 라고 우기고, **로지스틱 회귀**는 "웃기지 마, $Y$ 는 0 아니면 1을 찍는 살벌한 동전 던지기 베르누이 가문 출신이야!" 라며, 마지막으로 **포아송 회귀**는 "뭔 소리, $Y$ 는 대가리를 세는 양수 덩어리 포아송 가문의 핏줄이야!" 라고 각자 믿고 총을 쏩니다.
2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form
2. 게다가 세 녀석 모조리 타깃 과녁 $Y$ 의 **정중앙 코어(평균, Mean) 지표**를 힌트 예측 변수 군단들의 조립 함수 형태로 스케치한다는 전략이 동일합니다. 선형 회귀에서 과녁 $Y$ 의 정중앙 평균 코어는 너무나 뻔하고 뻣뻣한 일자 형태의 조립식을 띱니다:

$$
\text{E}(Y \mid X_1, \dots, X_p) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form
즉, 힌트 수치들을 곱하고 더해서 일자로 쭉 이어 붙인 '직선(선형) 함수' 뼈대 그 자체죠. 반면 동전 던지기 도박사인 **로지스틱 회귀** 용사는 이 일자 뼈대를 구부려 다음과 같은 기괴한 S자 곡선 평균 형태를 취합니다:

$$
\text{E}(Y \mid X_1, \dots, X_p) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form
그리고 갓 등장한 대가리 카운터 **포아송 회귀** 용사는 그 평균을 다음과 같이 날아오르는 지수 펌프 형태로 폭발시킵니다:

$$
\text{E}(Y \mid X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_, $\eta$, which applies a transformation to $E(Y \mid X_1, \dots, X_p)$ so that the transformed mean is a linear function of the predictors. That is,
어질어질하시죠? 하지만 이 제각각인 변태 같은 세 조각의 수식 (4.39)–(4.41) 은 모두 **_연결 함수(link function)_** $\eta$ (에타)라는 마법의 본드로 한 큐에 묶여 설명될 수 있습니다! 이 $\eta$ 연결 함수는 제 아무리 구부러지고 폭발하는 복잡한 평균 코어 $E(Y \mid X_1, \dots, X_p)$ 일지라도, 변환 수술을 통해 무조건 저 우직하고 평범한 $X$ 변수들의 단순 합체 **일자 뼈대(선형 함수)** 로 강제 펴서 맵핑 연결해 버리는 미친 강제력 변환 장치입니다. 즉!

$$
\eta(\text{E}(Y \mid X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, and $\eta(\mu) = \log(\mu)$, respectively.
이 마법의 연결 장치 규격을 까보면: 선형 회귀에 쓰였던 투명 연결 함수는 있는 그대로 통과시키는 $\eta(\mu) = \mu$ (아무것도 안 함) 이고, 로지스틱 회귀에서 $X$ 들을 선형으로 쭉 펴버린 무적의 연결 함수는 전설의 확률 배틀 승률비 함수인 로그 오즈 $\eta(\mu) = \log(\mu / (1 - \mu))$ 이며, 포아송 회귀를 펴준 연결 함수 요술 지팡이는 아까 봤던 $\eta(\mu) = \log(\mu)$ 로그 씌우기 장치입니다.

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_. Other well-known members of this family are the _exponential_ distribution, the _Gamma_ distribution, and the _negative binomial_ distribution. In general, we can perform a regression by modeling the response $Y$ as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via (4.42). Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM). Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs. Other examples not covered here include _Gamma regression_ and _negative binomial regression_.
사실 이 가우시안(정규), 베르누이, 포아송 이 세 종특 가문들은 훨씬 더 거대하고 위대한 우주 혈통인 **_지수 계열 족속 혈통(exponential family)_** 에 속하는 친척 형제들입니다. 이 명문 지수 족속 계보에는 덩달아 _지수(exponential) 분포, 감마(Gamma) 분포_, 횟수 카운터의 깡패인 _음이항(negative binomial) 분포_ 같은 빵빵한 엘리트 친척들이 바글바글합니다. 요약하자면, 우리가 맞춰야 할 타깃 $Y$ 가 이 거대 지수 혈통 가문 출신 중 아무 놈팽이나 하나 걸려있다고 판이 깔렸을 때, 그 $Y$ 의 정중앙 평균 덩어리에다가 저 무적의 식 (4.42) 요술 **연결 함수(link function $\eta$)** 를 냅다 씌워 변환해서, 힌트 $X$ 들의 단순한 일자 수학 덧셈 결합(선형 함수) 모형으로 쫙쫙 다려 펴 맞춰 버릴 수 있다는 대통일 이론이 성립합니다! 바로 이 무시무시한 대통합 레시피 룰을 따르는 세상의 모든 회귀 분파 무리들을 몽땅 엮어서 그 유명한 **_일반화 선형 모델(Generalized Linear Model, 즉 GLM)_** 이라는 칭호로 부릅니다. 고로, 선형 회귀, 로지스틱 회귀, 포아송 회귀 녀석들은 이 우주적 위대함을 지닌 GLM 거대 제국의 구역 원탑 3대장 예시일 뿐입니다. 우리 책이 귀찮아서 덮어둔 나머지 은둔 고수 친척 형제들로는 _감마 회귀(Gamma regression) 전투 로봇_ 이나 _음이항 회귀(negative binomial regression) 폭격기_ 등등이 수두룩하게 대기하고 있습니다!

---

## Sub-Chapters

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans2.html)

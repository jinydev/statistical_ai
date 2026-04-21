---
layout: default
title: "trans1"
---

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6.3 Generalized Linear Models in Greater Generality
# 4.6.3 더 포괄적인 일반화 선형 모델

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics:
우리는 지금까지 선형, 로지스틱, 그리고 포아송이라는 세 가지 유형의 회귀 모델들에 대해 논의했습니다. 이 접근법들은 다음과 같은 공통된 특성들을 공유합니다:

1. Each approach uses predictors $X_1, \dots, X_p$ to predict a response $Y$. We assume that, conditional on $X_1, \dots, X_p$, $Y$ belongs to a certain family of distributions. For linear regression, we typically assume that $Y$ follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$ follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$ follows a Poisson distribution.
1. 각 접근법은 예측 변수 $X_1, \dots, X_p$ 를 사용하여 반응 변수 $Y$를 예측합니다. 우리는 변수 $X_1, \dots, X_p$ 가 주어진 조건 하에서, $Y$가 특정 분포 패밀리(family of distributions)에 속한다고 가정합니다. 선형 회귀의 경우에는 예측 타깃 $Y$가 정규(normal) 분포 또는 가우시안 분포를 따른다고 일반적으로 가정합니다. 로지스틱 회귀의 경우, 우리는 $Y$가 베르누이(Bernoulli) 분포를 따른다고 가정합니다. 마지막으로 다룬 포아송 회귀에 대해, 우리는 $Y$가 포아송 분포를 따른다고 가정합니다.

2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form
2. 각 접근법은 $Y$의 예측 타깃 평균을 입력 예측 변수들의 산출 함수형으로 모델링합니다. 통상 선형 회귀에서, $Y$의 평균값은 다음 계산 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form
즉, 그것은 예측 변수들에 대한 가장 단순한 직선 선형 함수입니다. 반면 로지스틱 회귀의 경우, 도출 평균값 지표는 그 대신 다음과 같은 분수 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form
한편 바로 직전의 포아송 회귀 모델의 경우 평균 지표는 다음과 같은 지수 함수 형태를 취하게 됩니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_, $\eta$, which applies a transformation to $E(Y \mid X_1, \dots, X_p)$ so that the transformed mean is a linear function of the predictors. That is,
공식 (4.39)–(4.41)은 예측 모델이 계산하여 도출한 타깃 평균이 예측 변수들의 직선 선형 1차 함수로 유지되도록 $E(Y \mid X_1, \dots, X_p)$ 값 자체에 변환을 가해 적용하는 **연결 함수(link function)**, 즉 기호 $\eta$ 단위 식을 사용하여 한방에 요약 표현될 수 있습니다. 즉 다시 말해 다음의 식으로 통합 대체됩니다,

$$
\eta(\text{E}(Y \mid X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, and $\eta(\mu) = \log(\mu)$, respectively.
이 경우 적용되는 앞선 선형 모델, 로지스틱 모델 그리고 포아송 회귀의 각 매개 연결 함수(link functions) 부품들은 차례로 $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, 그리고 $\eta(\mu) = \log(\mu)$ 입니다.

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_.
우리가 앞에서 언급한 가우시안 분산 분포, 베르누이 단일 분포, 그리고 포아송 분산 분포 확률 도면 기법들은 모두 통틀어서, 알려진 이름인 거대 **지수 족(exponential family)** 이라고 불리는 더 방대하고 광범위한 거상 클래스 분포 패밀리의 한 속한 하부 종속 계층 일원 구성 멤버 무리들입니다.

Other well-known members of this family are the _exponential_ distribution, the _Gamma_ distribution, and the _negative binomial_ distribution.
이 거대 집단 패밀리 내에 포함되는 학계에 잘 알려진 여타 다른 멤버 무리들로는 특정 **지수(exponential) 분포**, **감마(Gamma) 분포**, 그리고 **음이항(negative binomial) 분포** 등이 자리 위치해 있습니다.

In general, we can perform a regression by modeling the response $Y$ as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via (4.42).
일반적으로 보편 통틀어 취합하여, 우리는 평가 반응 변수 수치 $Y$가 저 거대 지수 족 패밀리에 속하는 어느 특정 분파 멤버 부류 무리에서 기원 도출되어 파생 나온다고 넓게 묶어 가정 모델링 한 다음, (4.42) 매개 연결 공식을 거쳐 산출된 반응 변수의 타깃 예측 평균값이 그대로 바로 최초 입력 예측 단서 변수들의 단조 1차 선형 함수 뼈대 형태로 직결 연결되어 매개되도록 산술 수식을 치환 변형시킴으로써 아주 포괄적인 광범위 회귀 기계 도출 시스템을 통합 수행해낼 수 있습니다.

Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM).
이러한 매우 넓게 포괄적인 범용 수학적 절차 규칙 조립 설계 방식 절차(recipe) 레시피를 기반으로 채택해 따르고 작동 수용하며 순응하는 그 어떠한 기계 회귀 예측 접근법 방법 등은 모두 거대 총칭하여 **일반화 선형 모델(generalized linear model, GLM)** 이라는 포괄 이름표 규범으로 하나로 묶여 칭해 부르며 알려져 통용됩니다.

Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs.
따라서 최상위 관점으로 볼 때, 우리가 앞서 다뤘던 통나무 선형 회귀, 스피드 깡패 로지스틱 회귀, 그리고 이번 카운트 폭격기 포아송 예측 회귀 모델 등은 근본적으로 모두 저 거대 GLM 상위 범주에 속한 세 가지 대표적인 파편 모델 하위 특정 예시 가지 사례 부속 모형들일 뿐입니다.

Other examples not covered here include _Gamma regression_ and _negative binomial regression_.
이 단원에서 우리가 자세하게 다루어 보지 못한 확장 진영 다른 가지 예시들로는 동종 분파에 속하는 **감마 회귀(Gamma regression)** 장비와 **음이항 회귀(negative binomial regression)** 모델 따위 등이 있습니다.

---

## Sub-Chapters

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans1.html)

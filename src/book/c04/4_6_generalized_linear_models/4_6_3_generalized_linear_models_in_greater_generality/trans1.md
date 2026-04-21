---
layout: default
title: "trans1"
---

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6.3 Generalized Linear Models in Greater Generality
# 4.6.3 더 넓은 일반성의 일반화 선형 모델

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics:
우리는 이제 세 가지 유형의 회귀 모델, 즉 선형, 로지스틱 및 포아송에 대해 논의했습니다. 이러한 접근법들은 몇 가지 공통적인 특성을 공유합니다:

1. Each approach uses predictors $X_1, \dots, X_p$ to predict a response $Y$. We assume that, conditional on $X_1, \dots, X_p$, $Y$ belongs to a certain family of distributions. For linear regression, we typically assume that $Y$ follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$ follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$ follows a Poisson distribution.
1. 각 접근법은 예측 변수 $X_1, \dots, X_p$ 를 사용하여 반응 변수 $Y$ 를 예측합니다. 우리는 $X_1, \dots, X_p$ 를 조건으로 하여 $Y$ 가 특정 분포 계열(family of distributions)에 속한다고 가정합니다. 선형 회귀의 경우, 전형적으로 $Y$ 가 가우시안(Gaussian) 또는 정규 분포를 따른다고 가정합니다. 로지스틱 회귀의 경우, $Y$ 가 베르누이(Bernoulli) 분포를 따른다고 가정합니다. 마지막으로 포아송 회귀의 경우, $Y$ 가 포아송 분포를 따른다고 가정합니다.
2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form
2. 각 접근법은 $Y$ 의 평균을 예측 변수의 함수로 모델링합니다. 선형 회귀에서 $Y$ 의 평균은 다음과 같은 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form
즉, 예측 변수의 선형 함수입니다. 로지스틱 회귀의 경우 평균은 대신 다음과 같은 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form
반면 포아송 회귀의 경우 다음과 같은 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_, $\eta$, which applies a transformation to $E(Y \mid X_1, \dots, X_p)$ so that the transformed mean is a linear function of the predictors. That is,
식 (4.39)–(4.41)은 변환된 평균이 예측 변수의 선형 함수가 되도록 $E(Y \mid X_1, \dots, X_p)$ 에 변환을 적용하는 _연결 함수(link function)_, $\eta$ 를 사용하여 표현할 수 있습니다. 즉,

$$
\eta(\text{E}(Y \mid X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, and $\eta(\mu) = \log(\mu)$, respectively.
선형, 로지스틱 및 포아송 회귀의 연결 함수는 각각 $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, 그리고 $\eta(\mu) = \log(\mu)$ 입니다.

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_. Other well-known members of this family are the _exponential_ distribution, the _Gamma_ distribution, and the _negative binomial_ distribution. In general, we can perform a regression by modeling the response $Y$ as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via (4.42). Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM). Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs. Other examples not covered here include _Gamma regression_ and _negative binomial regression_.
가우시안, 베르누이 및 포아송 분포는 모두 _지수 계열(exponential family)_ 로 알려진 더 광범위한 분포 클래스의 구성원입니다. 이 계열의 다른 잘 알려진 구성원으로는 _지수(exponential)_ 분포, _감마(Gamma)_ 분포, 그리고 _음이항(negative binomial)_ 분포가 있습니다. 일반적으로, 우리는 반응 변수 $Y$ 가 지수 계열의 특정 구성원으로부터 파생된다고 모델링한 다음, 변환된 평균이 (4.42)를 통해 예측 변수의 선형 함수가 되도록 반응의 평균을 변환함으로써 회귀를 수행할 수 있습니다. 이 매우 일반적인 레시피를 따르는 모든 회귀 접근법을 _일반화 선형 모델(generalized linear model, GLM)_ 이라고 합니다. 따라서 선형 회귀, 로지스틱 회귀 및 포아송 회귀는 GLM의 세 가지 예입니다. 여기에서 다루지 않은 다른 예로는 _감마 회귀(Gamma regression)_ 와 _음이항 회귀(negative binomial regression)_ 가 있습니다.

---

## Sub-Chapters

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans1.html)

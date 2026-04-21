---
layout: default
title: "trans1"
---

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans1.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.2 Estimating the Regression Coefficients
# 4.3.2 회귀 계수 추정 (Estimating the Regression Coefficients)

The coefficients $\beta_0$ and $\beta_1$ in (4.2) are unknown, and must be estimated based on the available training data. In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients. Although we could use (non-linear) least squares to fit the model (4.4), the more general method of _maximum likelihood_ is preferred, since it has better statistical properties.
이 수식 (4.2) 안에 있는 계수 $\beta_0$ 와 $\beta_1$ 은 우리가 알 수 없는 미지의 값이며, 우리는 주어진 훈련 데이터를 바탕으로 이 값들을 찍어 맞춰야(추정해야) 합니다. 3단원에서 우리는 선형 회귀의 미지수를 맞추기 위해 '최소 제곱법'을 썼습니다. 비록 여기서도 (비선형) 최소 제곱법을 써서 (4.4) 모형을 욱여넣을 순 있겠지만, 여기서는 **최대 우도 추정법(Maximum Likelihood Estimation)** 이라는 더 보편적이고 일반적인 방식이 훨씬 통계적 속성이 뛰어나기 때문에 이 방법을 선호합니다.

The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_0$ and $\beta_1$ such that the predicted probability $\hat{p}(x_i)$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status.
로지스틱 회귀 모델을 맞추기 위해 최대 우도법을 동원하는 가장 기본적인 직관은 이렇습니다: (4.2)번 식을 통과시켜 내놓은 각각의 개인별 파산 예측 확률 $\hat{p}(x_i)$ 가, 눈앞에 있는 그 사람의 '진짜 파산 상태(관측값)'에 최대한 완벽하게 들러붙어 일치하도록 만드는 $\beta_0$ 와 $\beta_1$ 추정치를 찾는 것입니다.

In other words, we try to find $\hat{\beta}_0$ and $\hat{\beta}_1$ such that plugging these estimates into the model for $p(X)$, given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not.
다시 말해, 우리는 (4.2) 식의 $p(X)$ 에 이 추정치들을 쑤셔 넣었을 때, 진짜로 파산한 녀석들에게는 1에 가까운 확률 숫자를 뱉어내고 파산하지 않은 녀석들에게는 0에 가까운 숫자를 뱉어내게 만드는 완벽한 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 을 찾아내려고 시도하는 것입니다.

This intuition can be formalized using a mathematical equation called a _likelihood function_:
이러한 직관은 **우도 함수(Likelihood Function)** 라고 불리는 다음 수학 공식을 통해 공식화할 수 있습니다:

$$
\ell(\beta_0, \beta_1) = \prod_{i: y_i=1} p(x_i) \prod_{i^{\prime}: y_{i^{\prime}}=0} (1 - p(x_{i^{\prime}})) \quad (4.5)
$$

The estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ are chosen to _maximize_ this likelihood function. Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood. The mathematical details of maximum likelihood are beyond the scope of this book. However, in general, logistic regression and other models can be easily fit using statistical software such as `R` or `Python`, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.
추정치 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 은 이 우도 함수 결과를 **가장 최대로 끌어올리게(최대화, Maximize)** 만들도록 선택됩니다. 최대 우도 추정은 이 책 전반에서 우리가 조사하게 될 수많은 비선형 모델들을 피팅할 때 전천후로 쓰이는 매우 일반적인 접근법입니다. 사실 선형 회귀에서 썼던 최소 제곱법도 따지고 보면 이 최대 우도의 아주 특수한 형태일 뿐입니다. 최대 우도법의 복잡한 미적분 수학 디테일은 이 책의 범위를 벗어납니다. 다행히도 로지스틱 회귀와 다른 모델들은 파이썬이나 R 같은 통계 소프트웨어로 순식간에 적합시킬 수 있으므로, 우리가 저 무서운 최대 최소 적합 절차를 손으로 직접 풀며 걱정할 필요는 없습니다.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the `Default` data in order to predict the probability of `default = Yes` using `balance` . We see that $\hat{\beta}_1 = 0.0055$; this indicates that an increase in `balance` is associated with an increase in the probability of `default`. To be precise, a one-unit increase in `balance` is associated with an increase in the log odds of `default` by 0.0055 units.
표 4.1은 통장 잔고(`balance`)를 사용해 `default=Yes` 임을 예측하는 로지스틱 모형을 돌리고 나서 얻은 계수 추정치 등의 성적표입니다. 우리는 $\hat{\beta}_1 = 0.0055$ 임을 볼 수 있습니다; 이것은 잔고가 늘어나면 파산할 확률도 덩달아 상승한다는 뜻입니다. 더 정확히 말하자면, 잔고가 1 단위 늘어날 때마다 파산의 '로그 오즈(Log-odds)' 값이 0.0055 단위만큼 늘어난다는 뜻입니다.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3. For example, we can measure the accuracy of the coefficient estimates by computing their standard errors. The _z_-statistic in Table 4.1 plays the same role as the _t_-statistic in the linear regression output. For instance, the _z_-statistic associated with $\beta_1$ is equal to $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$, and so a large (absolute) value of the _z_-statistic indicates evidence against the null hypothesis $H_0 : \beta_1 = 0$. This null hypothesis implies that the probability of `default` does not depend on `balance` . Since the _p_-value associated with `balance` in Table 4.1 is tiny, we can reject $H_0$. In other words, we conclude that there is indeed an association between `balance` and probability of `default`. The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).
표 4.1에 표시된 회귀 분석 결과표를 보면 3장 선형 회귀 성적표와 굉장히 유사한 측면이 많습니다. 예를 들면, 표준 오차(SE)를 계산해서 추정치가 널뛰는 정확도를 평가할 수 있었습니다. 특히 표 4.1 하단의 **z-통계량(z-statistic)** 은 3장 직선 회귀에서 썼던 t-통계량(t-statistic)과 완전히 똑같은 심판 역할을 합니다. $\beta_1$ 에 붙은 z-통계량은 단순히 $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$ 를 계산한 값이며, 이 (절댓값) 심판 점수가 엄청 거대하다는 것은 자명하게 '잔고와 파산은 관련 없다!'고 억지를 부리는 귀무 가설 $H_0: \beta_1 = 0$ 을 기각할 반박 근거가 된다는 뜻입니다. 표 4.1에서 `balance` 에 뜬 p-값이 코딱지만큼 작게 떴기 때문에, 우리는 당당하게 $H_0$를 기각할 수 있습니다. 즉, 잔고와 파산 확률 사이에는 빼도 박도 못하는 연관성이 존재한다고 결론 내릴 수 있습니다. 표 4.1의 절편(Intercept) 추정치 수치 자체는 보통 우리의 관심사가 아닙니다; 절편은 그저 평균 피팅 확률들이 데이터 전체의 타겟 비율(여기선 3% 파산율 전체)과 균형을 맞추도록 영점을 튜닝하는 부품 역할만 수행합니다.

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans1.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans1.html)

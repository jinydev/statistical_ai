---
layout: default
title: "index"
---

# 3.1 Simple Linear Regression 

_Simple linear regression_ lives up to its name: it is a very straightforward approach for predicting a quantitative response $Y$ on the basis of a single predictor variable $X$. It assumes that there is approximately a linear relationship between $X$ and $Y$. Mathematically, we can write this linear relationship as

$$
Y \approx \beta_0 + \beta_1 X \quad (3.1)
$$

You might read "$\approx$" as _"is approximately modeled as"_. We will sometimes describe (3.1) by saying that we are _regressing $Y$ on $X$_ (or _$Y$ onto $X$_).

For example, $X$ may represent `TV` advertising and $Y$ may represent `sales`. Then we can regress `sales` onto `TV` by fitting the model

$$
\text{sales} \approx \beta_0 + \beta_1 \times \text{TV} \quad (3.2)
$$

In Equation 3.1, $\beta_0$ and $\beta_1$ are two unknown constants that represent the _intercept_ and _slope_ terms in the linear model. Together, $\beta_0$ and $\beta_1$ are known as the model _coefficients_ or _parameters_. Once we have used our training data to produce estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ for the model coefficients, we can predict future sales on the basis of a particular value of TV advertising by computing

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x \quad (3.3)
$$

where $\hat{y}$ indicates a prediction of $Y$ on the basis of $X = x$. Here we use a _hat_ symbol, $\hat{ }$, to denote the estimated value for an unknown parameter or coefficient, or to denote the predicted value of the response.

---

## Sub-Chapters (하위 목차)

### 3.1.1 Estimating the Coefficients (계수 추정)
* [문서로 이동하기](./3_1_1_estimating_the_coefficients/)

주어진 훈련 데이터를 가장 잘 설명하는 회귀 계수를 추정하기 위해 최소 제곱법(Least Squares)을 사용하는 과정을 살펴봅니다.
잔차(Residual)의 개념과 잔차 제곱합(RSS)을 최소화하는 수학적 직관을 다룹니다.

### 3.1.2 Assessing the Accuracy of the Coefficient Estimates (계수 추정치의 정확도 평가)
* [문서로 이동하기](./3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/)

추정한 회귀 계수가 실제 모집단 계수와 얼마나 가까운지(표준 오차, 신뢰 구간) 통계적으로 검증하는 방법을 배웁니다.
가설 검정(Hypothesis Testing)과 p-값(p-value)을 통해 변수의 유의성을 판단하는 법을 다룹니다.

### 3.1.3 Assessing the Accuracy of the Model (모델의 정확도 평가)
* [문서로 이동하기](./3_1_3_assessing_the_accuracy_of_the_model/)

적합된 선형 회귀 모델이 전체 데이터의 변동성을 얼마나 잘 설명하는지 R²(결정계수) 통계량 등으로 측정합니다.
또한 잔차 표준 오차(RSE)를 통해 실제 예측값이 모델 적합선과 차이나는 절대적 오차를 파악합니다.

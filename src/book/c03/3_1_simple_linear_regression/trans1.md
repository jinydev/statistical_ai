---
layout: default
title: "trans1"
---

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

[< 3. Linear Regression](../trans1.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/trans1.html)

# 3.1 Simple Linear Regression

# 3.1 단순 선형 회귀 (Simple Linear Regression)

_Simple linear regression_ lives up to its name: it is a very straightforward approach for predicting a quantitative response $Y$ on the basis of a single predictor variable $X$. It assumes that there is approximately a linear relationship between $X$ and $Y$. Mathematically, we can write this linear relationship as

_단순 선형 회귀(Simple linear regression)_ 는 그 이름 그대로입니다: 단일 예측 변수 $X$ 를 바탕으로 양적 응답 $Y$ 를 예측하기 위한 매우 직관적인 접근법입니다. 이 기법은 $X$ 와 $Y$ 사이에 대략적인 선형 관계가 존재한다고 가정합니다. 수학적으로, 이러한 선형 관계는 다음과 같이 작성할 수 있습니다:

$$
Y \approx \beta_0 + \beta_1 X \quad (3.1)
$$

You might read "$\approx$" as _"is approximately modeled as"_. We will sometimes describe (3.1) by saying that we are _regressing $Y$ on $X$_ (or _$Y$ onto $X$_).

기호 "$\approx$" 는 _"~로 대략 모델링된다"_ 라고 읽을 수 있습니다. 때때로 우리는 식 (3.1) 을 가리켜 _'$Y$ 를 $X$ 에 대해 회귀시킨다(regressing $Y$ on $X$)'_ (혹은 _'$X$ 위로 $Y$ 를 회귀시킨다'_ ) 라고 표현하기도 합니다.

For example, $X$ may represent `TV` advertising and $Y$ may represent `sales`. Then we can regress `sales` onto `TV` by fitting the model

예를 들어, 판단 요인 $X$ 가 `TV` 광고비를 나타내고 그로 인한 결과 지표 $Y$ 가 `sales` (판매량) 을 나타낼 수 있습니다. 그런 다음 우리는 다음과 같은 모델을 적합함으로써 `sales` 변수를 `TV` 기준 상에 회귀시킬 수 있습니다:

$$
\text{sales} \approx \beta_0 + \beta_1 \times \text{TV} \quad (3.2)
$$

In Equation 3.1, $\beta_0$ and $\beta_1$ are two unknown constants that represent the _intercept_ and _slope_ terms in the linear model. Together, $\beta_0$ and $\beta_1$ are known as the model _coefficients_ or _parameters_. Once we have used our training data to produce estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ for the model coefficients, we can predict future sales on the basis of a particular value of TV advertising by computing

방정식 3.1 에서 $\beta_0$ 와 $\beta_1$ 은 선형 모델에서 _절편(intercept)_ 과 _기울기(slope)_ 항을 나타내는 두 미지 상수입니다. 두 상수를 묶어, $\beta_0$ 와 $\beta_1$ 은 모델 _계수(coefficients)_ 또는 _파라미터(parameters)_ 라고 알려져 있습니다. 일단 훈련 데이터를 사용하여 모델 계수에 대한 추정치 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 를 생성하고 나면, 우리는 다음을 계산하여 특정한 TV 광고 예산 값을 바탕으로 미래의 판매량을 예측할 수 있습니다:

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x \quad (3.3)
$$

where $\hat{y}$ indicates a prediction of $Y$ on the basis of $X = x$. Here we use a _hat_ symbol, $\hat{ }$, to denote the estimated value for an unknown parameter or coefficient, or to denote the predicted value of the response.

여기서 $\hat{y}$ 는 $X = x$ 값에 기초한 결괏값 $Y$ 의 예측값을 나타냅니다. 여기서 우리는 알지 못하는 파라미터나 계수에 대한 추정치를 표시하거나, 혹은 응답 변수의 예측값을 나타내기 위해 _햇(hat)_ 기호인 $\hat{ }$ 모양을 사용합니다.

---

## Sub-Chapters (하위 목차)

### 3.1.1 Estimating the Coefficients (계수 추정)
* [문서로 이동하기](./3_1_1_estimating_the_coefficients/trans1.html)

주어진 훈련 데이터를 가장 잘 설명하는 회귀 계수를 추정하기 위해 최소 제곱법(Least Squares)을 사용하는 과정을 살펴봅니다.
잔차(Residual)의 개념과 잔차 제곱합(RSS)을 최소화하는 수학적 직관을 다룹니다.

### 3.1.2 Assessing the Accuracy of the Coefficient Estimates (계수 추정치의 정확도 평가)
* [문서로 이동하기](./3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans1.html)

추정한 회귀 계수가 실제 모집단 계수와 얼마나 가까운지(표준 오차, 신뢰 구간) 통계적으로 검증하는 방법을 배웁니다.
가설 검정(Hypothesis Testing)과 p-값(p-value)을 통해 변수의 유의성을 판단하는 법을 다룹니다.

### 3.1.3 Assessing the Accuracy of the Model (모델의 정확도 평가)
* [문서로 이동하기](./3_1_3_assessing_the_accuracy_of_the_model/trans1.html)

적합된 선형 회귀 모델이 전체 데이터의 변동성을 얼마나 잘 설명하는지 R²(결정계수) 통계량 등으로 측정합니다.
또한 잔차 표준 오차(RSE)를 통해 실제 예측값이 모델 적합선과 차이나는 절대적 오차를 파악합니다.

[< 3. Linear Regression](../trans1.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/trans1.html)

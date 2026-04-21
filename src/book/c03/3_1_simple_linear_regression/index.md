---
layout: default
title: "index"
---

> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

[< 3. Linear Regression](../index.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/index.html)

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

---

## Sub-Chapters

### 3.1.1 Estimating the Coefficients
* [Go to Document](./3_1_1_estimating_the_coefficients/)

### 3.1.2 Assessing the Accuracy of the Coefficient Estimates
* [Go to Document](./3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/)

### 3.1.3 Assessing the Accuracy of the Model
* [Go to Document](./3_1_3_assessing_the_accuracy_of_the_model/index.html)

[< 3. Linear Regression](../index.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/index.html)

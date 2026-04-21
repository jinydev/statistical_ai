---
layout: default
title: "trans1"
---

[< 3.7.1 Conceptual](../3_7_1_conceptual/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _Applied_
# 응용

8. This question involves the use of simple linear regression on the `Auto` data set.
8. 이 질문은 `Auto` 데이터셋에 단순 선형 회귀를 사용하는 것을 포함합니다.

- (a) Use the `sm.OLS()` function to perform a simple linear regression with `mpg` as the response and `horsepower` as the predictor.
- (a) `mpg`를 반응 변수로 하고 `horsepower`를 예측 변수로 하여 단순 선형 회귀를 수행하기 위해 `sm.OLS()` 함수를 사용하십시오.

Use the `summarize()` function to print the results.
결과를 출력하기 위해 `summarize()` 함수를 사용하십시오.

Comment on the output.
출력에 대해 논평하십시오.

For example:
예를 들어:

- i. Is there a relationship between the predictor and the response?
- i. 예측 변수와 반응 변수 사이에 관계가 있습니까?

- ii. How strong is the relationship between the predictor and the response?
- ii. 예측 변수와 반응 변수 사이의 관계는 얼마나 강합니까?

- iii. Is the relationship between the predictor and the response positive or negative?
- iii. 예측 변수와 반응 변수 사이의 관계는 양의 관계입니까 아니면 음의 관계입니까?

- iv. What is the predicted `mpg` associated with a `horsepower` of 98?
- iv. 98의 `horsepower`와 연관된 예측된 `mpg`는 무엇입니까?

What are the associated 95 % confidence and prediction intervals?
연관된 95% 신뢰 구간과 예측 구간은 무엇입니까?

- (b) Plot the response and the predictor in a new set of axes `ax` .
- (b) 새로운 축 세트 `ax`에 반응 변수와 예측 변수를 플롯하십시오.

Use the `ax.axline()` method or the `abline()` function defined in the lab to display the least squares regression line.
최소 제곱 회귀선을 표시하기 위해 랩에서 정의된 `ax.axline()` 메서드 또는 `abline()` 함수를 사용하십시오.

- (c) Produce some of diagnostic plots of the least squares regression fit as described in the lab.
- (c) 랩에 설명된 대로 최소 제곱 회귀 적합의 몇 가지 진단 플롯을 생성하십시오.

Comment on any problems you see with the fit.
적합에서 보이는 문제에 대해 논평하십시오.

9. This question involves the use of multiple linear regression on the `Auto` data set.
9. 이 질문은 `Auto` 데이터셋에 다중 선형 회귀를 사용하는 것을 포함합니다.

- (a) Produce a scatterplot matrix which includes all of the variables in the data set.
- (a) 데이터셋의 모든 변수를 포함하는 산점도 행렬을 생성하십시오.

- (b) Compute the matrix of correlations between the variables using the `DataFrame.corr()` method.
- (b) `DataFrame.corr()` 메서드를 사용하여 변수들 사이의 상관관계 행렬을 계산하십시오.

- (c) Use the `sm.OLS()` function to perform a multiple linear regression with `mpg` as the response and all other variables except `name` as the predictors.
- (c) `mpg`를 반응 변수로 하고 `name`을 제외한 모든 다른 변수를 예측 변수로 하여 다중 선형 회귀를 수행하기 위해 `sm.OLS()` 함수를 사용하십시오.

Use the `summarize()` function to print the results.
결과를 출력하기 위해 `summarize()` 함수를 사용하십시오.

Comment on the output.
출력에 대해 논평하십시오.

For instance:
예를 들어:

- i. Is there a relationship between the predictors and the response?
- i. 예측 변수들과 반응 변수 사이에 관계가 있습니까?

Use the `anova_lm()` function from `statsmodels` to answer this question.
이 질문에 답하기 위해 `statsmodels`의 `anova_lm()` 함수를 사용하십시오.

- ii. Which predictors appear to have a statistically significant relationship to the response?
- ii. 어느 예측 변수들이 반응 변수와 통계적으로 유의미한 관계가 있는 것으로 보입니까?

- iii. What does the coefficient for the `year` variable suggest?
- iii. `year` 변수의 계수는 무엇을 시사합니까?

- (d) Produce some of diagnostic plots of the linear regression fit as described in the lab.
- (d) 랩에 설명된 대로 선형 회귀 적합의 몇 가지 진단 플롯을 생성하십시오.

Comment on any problems you see with the fit.
적합에서 보이는 문제에 대해 논평하십시오.

Do the residual plots suggest any unusually large outliers?
잔차 플롯들이 유난히 큰 이상치들을 시사합니까?

Does the leverage plot identify any observations with unusually high leverage?
레버리지 플롯이 유난히 높은 레버리지를 가진 관측치들을 식별합니까?

- (e) Fit some models with interactions as described in the lab.
- (e) 랩에 설명된 대로 상호작용 항이 있는 몇몇 모델들을 적합하십시오.

Do any interactions appear to be statistically significant?
어떤 상호작용들이 통계적으로 유의미해 보입니까?

- (f) Try a few different transformations of the variables, such as $\log(X)$, $\sqrt{X}$, $X^2$.
- (f) $\log(X)$, $\sqrt{X}$, $X^2$와 같이 변수들의 몇 가지 다른 변환들을 시도해 보십시오.

Comment on your findings.
당신의 발견에 대해 논평하십시오.

10. This question should be answered using the `Carseats` data set.
10. 이 질문은 `Carseats` 데이터셋을 사용하여 답해져야 합니다.

- (a) Fit a multiple regression model to predict `Sales` using `Price` , `Urban` , and `US` .
- (a) `Price`, `Urban`, 그리고 `US`를 사용하여 `Sales`를 예측하기 위한 다중 회귀 모델을 적합하십시오.

- (b) Provide an interpretation of each coefficient in the model.
- (b) 모델의 각 계수에 대한 해석을 제공하십시오.

Be careful—some of the variables in the model are qualitative!
주의하십시오—모델의 변수들 중 일부는 질적 변수입니다!

- (c) Write out the model in equation form, being careful to handle the qualitative variables properly.
- (c) 질적 변수들을 적절히 처리하도록 주의하면서, 모델을 방정식 형태로 작성하십시오.

- (d) For which of the predictors can you reject the null hypothesis $H_0 : \beta_j = 0$?
- (d) 어느 예측 변수들에 대해 귀무 가설 $H_0 : \beta_j = 0$을 기각할 수 있습니까?

- (e) On the basis of your response to the previous question, fit a smaller model that only uses the predictors for which there is evidence of association with the outcome.
- (e) 이전 질문에 대한 당신의 응답을 바탕으로, 결과와 연관성에 대한 증거가 있는 예측 변수들만을 사용하는 더 작은 모델을 적합하십시오.

- (f) How well do the models in (a) and (e) fit the data?
- (f) (a)와 (e)의 모델들이 데이터를 얼마나 잘 적합합니까?

- (g) Using the model from (e), obtain 95 % confidence intervals for the coefficient(s).
- (g) (e)의 모델을 사용하여, 계수(들)에 대한 95% 신뢰 구간들을 얻으십시오.

- (h) Is there evidence of outliers or high leverage observations in the model from (e)?
- (h) (e)의 모델에서 이상치들이나 높은 레버리지 관측치들의 증거가 있습니까?

11. In this problem we will investigate the $t$-statistic for the null hypothesis $H_0 : \beta = 0$ in simple linear regression without an intercept.
11. 이 문제에서 우리는 절편이 없는 단순 선형 회귀에서 귀무 가설 $H_0 : \beta = 0$에 대한 $t$-통계량을 조사할 것입니다.

To begin, we generate a predictor `x` and a response `y` as follows.
시작하기 위해, 우리는 다음과 같이 예측 변수 `x`와 반응 변수 `y`를 생성합니다.

```python
rng = np.random.default_rng(1)
x = rng.normal(size=100)
y = 2 * x + rng.normal(size=100)
```

- (a) Perform a simple linear regression of `y` onto `x` , _without_ an intercept.
- (a) 절편 _없이_, `y`를 `x`에 대해 단순 선형 회귀를 수행하십시오.

Report the coefficient estimate $\hat{\beta}$ , the standard error of this coefficient estimate, and the $t$-statistic and $p$-value associated with the null hypothesis $H_0 : \beta = 0$.
계수 추정치 $\hat{\beta}$, 이 계수 추정치의 표준 오차, 그리고 귀무 가설 $H_0 : \beta = 0$과 연관된 $t$-통계량과 $p$-값을 보고하십시오.

Comment on these results.
이러한 결과들에 대해 논평하십시오.

(You can perform regression without an intercept using the keywords argument `intercept=False` to `ModelSpec()` .)
(당신은 `ModelSpec()`에 대한 키워드 인수 `intercept=False`를 사용하여 절편 없이 회귀를 수행할 수 있습니다.)

- (b) Now perform a simple linear regression of `x` onto `y` without an intercept, and report the coefficient estimate, its standard error, and the corresponding $t$-statistic and $p$-values associated with the null hypothesis $H_0 : \beta = 0$.
- (b) 이제 절편 없이 `x`를 `y`에 대해 단순 선형 회귀를 수행하고, 계수 추정치, 그것의 표준 오차, 그리고 귀무 가설 $H_0 : \beta = 0$과 연관된 상응하는 $t$-통계량과 $p$-값들을 보고하십시오.

Comment on these results.
이러한 결과들에 대해 논평하십시오.

- (c) What is the relationship between the results obtained in (a) and (b)?
- (c) (a)와 (b)에서 얻은 결과들 사이의 관계는 무엇입니까?

- (d) For the regression of Y onto X without an intercept, the $t$-statistic for $H_0 : \beta = 0$ takes the form $\hat{\beta} / \text{SE}(\hat{\beta})$, where $\hat{\beta}$ is given by (3.38), and where
- (d) 절편이 없는 Y의 X에 대한 회귀에서, $H_0 : \beta = 0$에 대한 $t$-통계량은 $\hat{\beta} / \text{SE}(\hat{\beta})$의 형태를 취하며, 여기서 $\hat{\beta}$는 (3.38)에 의해 주어지고, 여기서

**==> picture [133 x 31] intentionally omitted <==**
**==> picture [133 x 31] intentionally omitted <==**

(These formulas are slightly different from those given in Sections 3.1.1 and 3.1.2, since here we are performing regression without an intercept.)
(이러한 공식들은 섹션 3.1.1과 3.1.2에서 주어진 것들과 약간 다른데, 왜냐하면 여기에서 우리는 절편 없는 회귀를 수행하고 있기 때문입니다.)

Show algebraically, and confirm numerically in `Python` , that the $t$-statistic can be written as
대수적으로 보여주고, `Python`에서 수치적으로 확인하여, $t$-통계량이 다음과 같이 쓰여질 수 있음을 보여주십시오.

**==> picture [181 x 32] intentionally omitted <==**
**==> picture [181 x 32] intentionally omitted <==**

- (e) Using the results from (d), argue that the $t$-statistic for the regression of `y` onto `x` is the same as the $t$-statistic for the regression of `x` onto `y` .
- (e) (d)로부터의 결과들을 사용하여, `y`의 `x`에 대한 회귀의 $t$-통계량이 `x`의 `y`에 대한 회귀의 $t$-통계량과 동일하다고 주장하십시오.

- (f) In `Python` , show that when regression is performed _with_ an intercept, the $t$-statistic for $H_0 : \beta_1 = 0$ is the same for the regression of `y` onto `x` as it is for the regression of `x` onto `y` .
- (f) `Python`에서, 만약 회귀가 절편과 _함께_ 수행될 때, $H_0 : \beta_1 = 0$에 대한 $t$-통계량은 `y`의 `x`에 대한 회귀에서의 경우와 `x`의 `y`에 대한 회귀에서의 경우가 동일함을 보여주십시오.

12. This problem involves simple linear regression without an intercept.
12. 이 문제는 절편이 없는 단순 선형 회귀를 포함합니다.

- (a) Recall that the coefficient estimate $\hat{\beta}$ for the linear regression of Y onto X without an intercept is given by (3.38).
- (a) 절편 없는 Y의 X에 대한 선형 회귀를 위한 계수 추정치 $\hat{\beta}$가 (3.38)에 의해 주어진다는 것을 상기하십시오.

Under what circumstance is the coefficient estimate for the regression of X onto Y the same as the coefficient estimate for the regression of Y onto X?
어떤 상황 하에서 X의 Y에 대한 회귀의 계수 추정치가 Y의 X에 대한 회귀의 계수 추정치와 동일해집니까?

- (b) Generate an example in `Python` with $n = 100$ observations in which the coefficient estimate for the regression of X onto Y is _different from_ the coefficient estimate for the regression of Y onto X .
- (b) `Python`에서 X의 Y에 대한 회귀의 계수 추정치가 Y의 X에 대한 회귀의 계수 추정치와 _다른_ $n = 100$ 관측치를 갖는 예시를 생성하십시오.

- (c) Generate an example in `Python` with $n = 100$ observations in which the coefficient estimate for the regression of X onto Y is _the same as_ the coefficient estimate for the regression of Y onto X .
- (c) `Python`에서 X의 Y에 대한 회귀의 계수 추정치가 Y의 X에 대한 회귀의 계수 추정치와 _동일한_ $n = 100$ 관측치를 갖는 예시를 생성하십시오.

13. In this exercise you will create some simulated data and will fit simple linear regression models to it.
13. 이 연습문제에서 당신은 약간의 시뮬레이션된 데이터를 생성할 것이며 단순 선형 회귀 모델들을 그것에 적합시킬 것입니다.

Make sure to use the default random number generator with seed set to 1 prior to starting part (a) to ensure consistent results.
일관된 결과를 보장하기 위해 파트 (a)를 시작하기 전에 시드가 1로 설정된 기본 난수 생성기를 사용하도록 확인하십시오.

- (a) Using the `normal()` method of your random number generator, create a vector, `x` , containing 100 observations drawn from a $N(0, 1)$ distribution.
- (a) 난수 생성기의 `normal()` 메서드를 사용하여, $N(0, 1)$ 분포에서 추출된 100개의 관측치들을 포함하는 벡터 `x`를 생성하십시오.

This represents a feature, X .
이것은 특성 X를 나타냅니다.

- (b) Using the `normal()` method, create a vector, `eps` , containing 100 observations drawn from a $N(0, 0.25)$ distribution—a normal distribution with mean zero and variance $0.25$.
- (b) `normal()` 메서드를 사용하여, 평균이 0이고 분산이 $0.25$인 정규 분포인 $N(0, 0.25)$ 분포에서 추출된 100개의 관측치들을 포함하는 벡터 `eps`를 생성하십시오.

- (c) Using `x` and `eps` , generate a vector `y` according to the model
- (c) `x`와 `eps`를 사용하여, 이 모델에 따라 벡터 `y`를 생성하십시오.

**==> picture [182 x 11] intentionally omitted <==**
**==> picture [182 x 11] intentionally omitted <==**

What is the length of the vector `y` ?
벡터 `y`의 길이는 무엇입니까?

What are the values of $\beta_0$ and $\beta_1$ in this linear model?
이 선형 모델에서 $\beta_0$와 $\beta_1$의 값들은 무엇입니까?

- (d) Create a scatterplot displaying the relationship between `x` and `y` .
- (d) `x`와 `y` 사이의 관계를 표시하는 산점도를 생성하십시오.

Comment on what you observe.
당신이 관찰하는 것에 대해 논평하십시오.

- (e) Fit a least squares linear model to predict `y` using `x` .
- (e) `x`를 사용하여 `y`를 예측하기 위한 최소 제곱 선형 모델을 적합하십시오.

Comment on the model obtained.
얻어진 모델에 대해 논평하십시오.

How do $\hat{\beta}_0$ and $\hat{\beta}_1$ compare to $\beta_0$ and $\beta_1$?
$\hat{\beta}_0$와 $\hat{\beta}_1$은 $\beta_0$ 및 $\beta_1$과 비교하여 어떻습니까?

- (f) Display the least squares line on the scatterplot obtained in (d).
- (f) (d)에서 얻은 산점도에 최소 제곱 선형을 표시하십시오.

Draw the population regression line on the plot, in a different color.
다른 색상으로 플롯에 모집단 회귀선을 그리십시오.

Use the `legend()` method of the axes to create an appropriate legend.
적절한 범례를 생성하기 위해 축의 `legend()` 메서드를 사용하십시오.

- (g) Now fit a polynomial regression model that predicts `y` using `x` and $x^2$ .
- (g) 이제 `x`와 $x^2$를 사용하여 `y`를 예측하는 다항 회귀 모델을 적합하십시오.

Is there evidence that the quadratic term improves the model fit?
이차 항이 모델의 적합도를 향상시킨다는 증거가 있습니까?

Explain your answer.
당신의 답변을 설명하십시오.

- (h) Repeat (a)–(f) after modifying the data generation process in such a way that there is _less_ noise in the data.
- (h) 데이터에 잡음이 _적도록_ 데이터 생성 과정을 수정한 후 (a)-(f)를 반복하십시오.

The model (3.39) should remain the same.
모델 (3.39)은 동일하게 유지되어야 합니다.

You can do this by decreasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b).
당신은 (b)에서 오차 항 $\epsilon$을 생성하기 위해 사용된 정규 분포의 분산을 감소시킴으로써 이를 수행할 수 있습니다.

Describe your results.
당신의 결과들을 설명하십시오.

- (i) Repeat (a)–(f) after modifying the data generation process in such a way that there is _more_ noise in the data.
- (i) 데이터에 잡음이 _많도록_ 데이터 생성 과정을 수정한 후 (a)-(f)를 반복하십시오.

The model (3.39) should remain the same.
모델 (3.39)은 동일하게 유지되어야 합니다.

You can do this by increasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b).
당신은 (b)에서 오차 항 $\epsilon$을 생성하기 위해 사용된 정규 분포의 분산을 증가시킴으로써 이를 수행할 수 있습니다.

Describe your results.
당신의 결과들을 설명하십시오.

- (j) What are the confidence intervals for $\beta_0$ and $\beta_1$ based on the original data set, the noisier data set, and the less noisy data set?
- (j) 원래 데이터셋, 잡음이 더 많은 데이터셋, 그리고 잡음이 더 적은 데이터셋을 기반으로 한 $\beta_0$와 $\beta_1$에 대한 신뢰 구간들은 무엇입니까?

Comment on your results.
당신의 결과들에 대해 논평하십시오.

14. This problem focuses on the _collinearity_ problem.
14. 이 문제는 _공선성(collinearity)_ 문제에 초점을 맞춥니다.

- (a) Perform the following commands in `Python` :
- (a) `Python`에서 다음 명령들을 수행하십시오:

```python
rng = np.random.default_rng(10)
x1 = rng.uniform(0, 1, size=100)
x2 = 0.5 * x1 + rng.normal(size=100) / 10
y = 2 + 2 * x1 + 0.3 * x2 + rng.normal(size=100)
```

The last line corresponds to creating a linear model in which `y` is a function of `x1` and `x2` .
마지막 줄은 `y`가 `x1`과 `x2`의 함수인 선형 모델을 생성하는 것에 해당합니다.

Write out the form of the linear model.
선형 모델의 형태를 작성하십시오.

What are the regression coefficients?
회귀 계수들은 무엇입니까?

- (b) What is the correlation between `x1` and `x2` ?
- (b) `x1`과 `x2` 사이의 상관관계는 무엇입니까?

Create a scatterplot displaying the relationship between the variables.
변수들 사이의 관계를 표시하는 산점도를 생성하십시오.

- (c) Using this data, fit a least squares regression to predict `y` using `x1` and `x2` .
- (c) 이 데이터를 사용하여, `x1`과 `x2`를 사용하여 `y`를 예측하기 위한 최소 제곱 회귀를 적합하십시오.

Describe the results obtained.
얻어진 결과들을 설명하십시오.

What are $\hat{\beta}_0$, $\hat{\beta}_1$, and $\hat{\beta}_2$?
$\hat{\beta}_0$, $\hat{\beta}_1$, 및 $\hat{\beta}_2$는 무엇입니까?

How do these relate to the true $\beta_0$, $\beta_1$, and $\beta_2$?
이것들은 실제 $\beta_0$, $\beta_1$, 및 $\beta_2$와 어떻게 연관됩니까?

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
귀무 가설 $H_0 : \beta_1 = 0$을 기각할 수 있습니까?

How about the null hypothesis $H_0 : \beta_2 = 0$?
귀무 가설 $H_0 : \beta_2 = 0$은 어떻습니까?

- (d) Now fit a least squares regression to predict `y` using only `x1` .
- (d) 이제 `x1`만을 사용하여 `y`를 예측하기 위한 최소 제곱 회귀를 적합하십시오.

Comment on your results.
당신의 결과들에 대해 논평하십시오.

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
귀무 가설 $H_0 : \beta_1 = 0$을 기각할 수 있습니까?

- (e) Now fit a least squares regression to predict `y` using only `x2` .
- (e) 이제 `x2`만을 사용하여 `y`를 예측하기 위한 최소 제곱 회귀를 적합하십시오.

Comment on your results.
당신의 결과들에 대해 논평하십시오.

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
귀무 가설 $H_0 : \beta_1 = 0$을 기각할 수 있습니까?

- (f) Do the results obtained in (c)–(e) contradict each other?
- (f) (c)–(e)에서 얻어진 결과들이 서로 모순됩니까?

Explain your answer.
당신의 답변을 설명하십시오.

- (g) Suppose we obtain one additional observation, which was unfortunately mismeasured.
- (g) 불행히도 잘못 측정된 하나의 추가적인 관측치를 우리가 얻었다고 가정하십시오.

We use the function `np.concatenate()` to add this additional observation to each of `x1` , `x2` and `y` .
우리는 `np.concatenate()` 함수를 사용하여 이 추가적인 관측치를 `x1`, `x2` 그리고 `y`의 각각에 더합니다.

```python
x1 = np.concatenate([x1, [0.1]])
x2 = np.concatenate([x2, [0.8]])
y = np.concatenate([y, [6]])
```

Re-fit the linear models from (c) to (e) using this new data.
이 새로운 데이터를 사용하여 (c)부터 (e)까지의 선형 모델들을 재적합하십시오.

What effect does this new observation have on the each of the models?
이 새로운 관측치가 각각의 모델들에 어떠한 영향을 미칩니까?

In each model, is this observation an outlier?
각각의 모델에서, 이 관측치가 이상치입니까?

A high-leverage point?
높은 레버리지 지점입니까?

Both?
둘 다입니까?

Explain your answers.
당신의 답변들을 설명하십시오.

15. This problem involves the `Boston` data set, which we saw in the lab for this chapter.
15. 이 문제는 이 장을 위한 랩에서 우리가 보았던 `Boston` 데이터셋을 포함합니다.

We will now try to predict per capita crime rate using the other variables in this data set.
우리는 이제 이 데이터셋 내의 다른 변수들을 사용하여 1인당 범죄율을 예측하려고 시도할 것입니다.

In other words, per capita crime rate is the response, and the other variables are the predictors.
다시 말해, 1인당 범죄율이 반응 변수이고, 다른 변수들은 예측 변수들입니다.

- (a) For each predictor, fit a simple linear regression model to predict the response.
- (a) 각각의 예측 변수에 대해, 반응 변수를 예측하기 위한 단순 선형 회귀 모델을 적합하십시오.

Describe your results.
당신의 결과들을 설명하십시오.

In which of the models is there a statistically significant association between the predictor and the response?
어느 모델들에서 예측 변수와 반응 변수 사이에 통계적으로 유의미한 연관성이 있습니까?

Create some plots to back up your assertions.
당신의 주장들을 뒷받침할 만한 몇몇 플롯들을 생성하십시오.

- (b) Fit a multiple regression model to predict the response using all of the predictors.
- (b) 모든 예측 변수들을 사용하여 반응 변수를 예측하기 위한 다중 회귀 모델을 적합하십시오.

Describe your results.
당신의 결과들을 설명하십시오.

For which predictors can we reject the null hypothesis $H_0 : \beta_j = 0$?
우리가 어느 예측 변수들에 대해 귀무 가설 $H_0 : \beta_j = 0$을 기각할 수 있습니까?

- (c) How do your results from (a) compare to your results from (b)?
- (c) (a)로부터의 당신의 결과들이 (b)로부터의 결과들과 어떻게 비교됩니까?

Create a plot displaying the univariate regression coefficients from (a) on the _x_ -axis, and the multiple regression coefficients from (b) on the _y_ -axis.
(a)로부터의 단변량 회귀 계수들을 _x_-축에, 그리고 (b)로부터의 다중 회귀 계수들을 _y_-축에 표시하는 플롯을 생성하십시오.

That is, each predictor is displayed as a single point in the plot.
즉, 각각의 예측 변수가 플롯에서 단일 점으로 표시됩니다.

Its coefficient in a simple linear regression model is shown on the _x_ -axis, and its coefficient estimate in the multiple linear regression model is shown on the _y_ -axis.
단순 선형 회귀 모델에서의 그것의 계수는 _x_-축에 보여지고, 다중 선형 회귀 모델에서의 계수 추정치는 _y_-축에 보여집니다.

- (d) Is there evidence of non-linear association between any of the predictors and the response?
- (d) 어떤 예측 변수들과 반응 변수 사이에 비선형 연관성의 증거가 있습니까?

To answer this question, for each predictor X , fit a model of the form
이 질문에 답하기 위해, 각각의 예측 변수 X에 대해 이러한 형태의 모델을 적합하십시오

**==> picture [154 x 11] intentionally omitted <==**
**==> picture [154 x 11] intentionally omitted <==**

---

## Sub-Chapters (하위 목차)

[< 3.7.1 Conceptual](../3_7_1_conceptual/trans1.html)

---
layout: default
title: "index"
---

[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/index.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3.2.2 Some Important Questions

When we perform multiple linear regression, we usually are interested in answering a few important questions.

1. _Is at least one of the predictors $X_1, X_2, \dots, X_p$ useful in predicting the response?_

2. _Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?_

3. _How well does the model fit the data?_

4. _Given a set of predictor values, what response value should we predict, and how accurate is our prediction?_

We now address each of these questions in turn.

## One: Is There a Relationship Between the Response and Predictors?

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$.

In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \dots = \beta_p = 0$.

As in the simple linear regression setting, we use a hypothesis test to answer this question.

We test the null hypothesis,

$$

H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad (3.23)

$$

versus the alternative

$$

H_a : \text{at least one } \beta_j \text{ is non-zero.}

$$

This hypothesis test is performed by computing the _F -statistic_ ,

$$

F = \frac{(\text{TSS} - \text{RSS}) / p}{\text{RSS} / (n - p - 1)} \quad (3.24)

$$

where, as with simple linear regression, $\text{TSS} = \sum (y_i - \bar{y})^2$ and $\text{RSS} = \sum (y_i - \hat{y}_i)^2$.

If the linear model assumptions are correct, one can show that

$$

E\{\text{RSS} / (n - p - 1)\} = \sigma^2

$$

and that, provided $H_0$ is true,

$$

E\{(\text{TSS} - \text{RSS}) / p\} = \sigma^2

$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1.

On the other hand, if $H_a$ is true, then $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$, so we expect $F$ to be greater than 1.

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6.

In this example the $F$-statistic is 570.

Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$.

In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`.

However, what if the $F$-statistic had been closer to 1?

| Quantity | Value |

| Residual standard error | 1.69 |

| $F$-statistic | 570 |

$$

H_0 : \beta_{p-q+1} = \beta_{p-q+2} = \dots = \beta_p = 0

$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables _except_ those last $q$. Suppose that the residual sum of squares for that model is $\text{RSS}_0$. Then the appropriate $F$-statistic is

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$ . However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the _F_ - statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as _forward selection_ , can be used. This _high-dimensional_ setting is discussed in greater detail in Chapter 6.

---

---

### One: Is There a Relationship Between the Response and Predictors?

### Two: Deciding on Important Variables

### Three: Model Fit

### Four: Predictions

---

## Sub-Chapters


[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/index.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/index.html)

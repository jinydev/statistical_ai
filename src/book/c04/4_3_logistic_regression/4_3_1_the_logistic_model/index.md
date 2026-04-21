---
layout: default
title: "index"
---

[< 4.3 Logistic Regression](../index.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.3.1 The Logistic Model

How should we model the relationship between $p(X) = \text{Pr}(Y=1 \mid X)$ and $X$? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent these probabilities:

$$
p(X) = \beta_0 + \beta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance`, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1. These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1. This problem is not unique to the credit default data. Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of $X$ and $p(X) > 1$ for others (unless the range of $X$ is limited).

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of $X$. Many functions meet this description. In logistic regression, we use the _logistic function_,

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \quad (4.2)
$$

To fit the model (4.2), we use a method called _maximum likelihood_, which we discuss in the next section. The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the `Default` data. Notice that for low balances we now predict the probability of default as close to, but never below, zero. Likewise, for high balances we predict a default probability close to, but never above, one. The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction. We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot. The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.

After a bit of manipulation of (4.2), we find that

$$
\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X} \quad (4.3)
$$

The quantity $p(X) / [1 - p(X)]$ is called the _odds_, and can take on any value between 0 and $\infty$. Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively. For example, on average 1 in 5 people with an odds of $1/4$ will default, since $p(X) = 0.2$ implies an odds of $0.2 / (1 - 0.2) = 1/4$. Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X) = 0.9$ implies an odds of $0.9 / (1 - 0.9) = 9$. Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.

By taking the logarithm of both sides of (4.3), we arrive at

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_. We see that the logistic regression model (4.2) has a logit that is linear in $X$.

Recall from Chapter 3 that in a linear regression model, $\beta_1$ gives the average change in $Y$ associated with a one-unit increase in $X$. By contrast, in a logistic regression model, increasing $X$ by one unit changes the log odds by $\beta_1$ (4.4). Equivalently, it multiplies the odds by $e^{\beta_1}$ (4.3). However, because the relationship between $p(X)$ and $X$ in (4.2) is not a straight line, $\beta_1$ does _not_ correspond to the change in $p(X)$ associated with a one-unit increase in $X$. The amount that $p(X)$ changes due to a one-unit change in $X$ depends on the current value of $X$. But regardless of the value of $X$, if $\beta_1$ is positive then increasing $X$ will be associated with increasing $p(X)$, and if $\beta_1$ is negative then increasing $X$ will be associated with decreasing $p(X)$.

---

## Sub-Chapters


[< 4.3 Logistic Regression](../index.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/index.html)

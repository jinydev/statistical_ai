---
layout: default
title: "index"
---

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/index.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/index.html)

> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3.1.2 Assessing the Accuracy of the Coefficient Estimates

Recall from (2.1) that we assume that the _true_ relationship between $X$ and $Y$ takes the form $Y = f(X) + \epsilon$ for some unknown function $f$, where $\epsilon$ is a mean-zero random error term.

If $f$ is to be approximated by a linear function, then we can write this relationship as

$$

Y = \beta_0 + \beta_1 X + \epsilon \quad (3.5)

$$

Here $\beta_0$ is the intercept term—that is, the expected value of $Y$ when $X = 0$, and $\beta_1$ is the slope—the average increase in $Y$ associated with a one-unit increase in $X$.

The error term is a catch-all for what we miss with this simple model: the true relationship is probably not linear, there may be other variables that cause variation in $Y$, and there may be measurement error.

We typically assume that the error term is independent of $X$.

**==> picture [284 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 6 7 8 9 β 0 β 1<br>β 0<br> 2.2<br> 2.3<br> 2.15<br> 2.5<br> 2.5<br> 2.11<br> 3<br> 3<br>RSS<br>0.06<br>β 1 0.05<br>0.04<br>0.03<br>**----- End of picture text -----**<br>

**FIGURE 3.2.** _Contour and three-dimensional plots of the RSS on the_ `Advertising` _data, using_ `sales` _as the response and_ `TV` _as the predictor. The red dots correspond to the least squares estimates $\hat{\beta}_0$ and $\hat{\beta}_1$, given by (3.4)._

The model given by (3.5) defines the _population regression line_, which is the best linear approximation to the true relationship between $X$ and $Y$.$^1$

The least squares regression coefficient estimates (3.4) characterize the _least squares line_ (3.2).

The left-hand panel of Figure 3.3 displays these two lines in a simple simulated example.

We created 100 random $X$s, and generated 100 corresponding $Y$s from the model

$$
Y = 2 + 3X + \epsilon \quad (3.6)
$$

where $\epsilon$ was generated from a normal distribution with mean zero.

The red line in the left-hand panel of Figure 3.3 displays the _true_ relationship, $f(X) = 2 + 3X$, while the blue line is the least squares estimate based on the observed data.

The true relationship is generally not known for real data, but the least squares line can always be computed using the coefficient estimates given in (3.4).

In other words, in real applications, we have access to a set of observations from which we can compute the least squares line; however, the population regression line is unobserved.

In the right-hand panel of Figure 3.3 we have generated ten different data sets from the model given by (3.6) and plotted the corresponding ten least squares lines.

Notice that different data sets generated from the same true model result in slightly different least squares lines, but the unobserved population regression line does not change.

At first glance, the difference between the population regression line and the least squares line may seem subtle and confusing.

We only have one data set, and so what does it mean that two different lines describe the relationship between the predictor and the response?

Fundamentally, the concept of these two lines is a natural extension of the standard statistical approach of using information from a sample to estimate characteristics of a large population.

For example, suppose that we are interested in knowing

> 1The assumption of linearity is often a useful working model.

> However, despite what many textbooks might tell us, we seldom believe that the true relationship is linear.

**==> picture [315 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
−2 −1 0 1 2 −2 −1 0 1 2<br>X X<br>10 10<br>5 5<br>Y Y<br>0 0<br>−5 −5<br>−10 −10<br>**----- End of picture text -----**<br>

**FIGURE 3.3.** _A simulated data set._ Left: _The red line represents the true relationship, f(X) = 2 + 3X, which is known as the population regression line. The blue line is the least squares line; it is the least squares estimate for f(X) based on the observed data, shown in black._ Right: _The population regression line is again shown in red, and the least squares line in dark blue. In light blue, ten least squares lines are shown, each computed on the basis of a separate random set of observations. Each least squares line is different, but on average, the least squares lines are quite close to the population regression line._

the population mean $\mu$ of some random variable $Y$.

Unfortunately, $\mu$ is unknown, but we do have access to $n$ observations from $Y$, $y_1, \dots, y_n$, which we can use to estimate $\mu$.

A reasonable estimate is $\hat{\mu} = \bar{y}$, where $\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$ is the sample mean.

The sample mean and the population mean are different, but in general the sample mean will provide a good estimate of the population mean.

In the same way, the unknown coefficients $\beta_0$ and $\beta_1$ in linear regression define the population regression line.

We seek to estimate these unknown coefficients using $\hat{\beta}_0$ and $\hat{\beta}_1$ given in (3.4).

These coefficient estimates define the least squares line.

The analogy between linear regression and estimation of the mean of a random variable is an apt one based on the concept of _bias_.

If we use the sample mean $\hat{\mu}$ to estimate $\mu$, this estimate is _unbiased_, in the sense that on average, we expect $\hat{\mu}$ to equal $\mu$.

What exactly does this mean?

It means that on the basis of one particular set of observations $y_1, \dots, y_n$, $\hat{\mu}$ might overestimate $\mu$, and on the basis of another set of observations, $\hat{\mu}$ might underestimate $\mu$.

But if we could average a huge number of estimates of $\mu$ obtained from a huge number of sets of observations, then this average would _exactly_ equal $\mu$.

Hence, an unbiased estimator does not _systematically_ over- or under-estimate the true parameter.

The property of unbiasedness holds for the least squares coefficient estimates given by (3.4) as well: if we estimate $\beta_0$ and $\beta_1$ on the basis of a particular data set, then our estimates won’t be exactly equal to $\beta_0$ and $\beta_1$.

But if we could average the estimates obtained over a huge number of data sets, then the average of these estimates would be spot on!

In fact, we can see from the righthand panel of Figure 3.3 that the average of many least squares lines, each estimated from a separate data set, is pretty close to the true population regression line.

We continue the analogy with the estimation of the population mean $\mu$ of a random variable $Y$.

A natural question is as follows: how accurate is the sample mean $\hat{\mu}$ as an estimate of $\mu$?

We have established that the average of $\hat{\mu}$'s over many data sets will be very close to $\mu$, but that a single estimate $\hat{\mu}$ may be a substantial underestimate or overestimate of $\mu$.

How far off will that single estimate of $\hat{\mu}$ be?

In general, we answer this question by computing the _standard error_ of $\hat{\mu}$, written as $\text{SE}(\hat{\mu})$.

We have the well-known formula:

$$
\text{Var}(\hat{\mu}) = \text{SE}(\hat{\mu})^2 = \frac{\sigma^2}{n} \quad (3.7)
$$

where $\sigma$ is the standard deviation of each of the realizations $y_i$ of $Y$.$^2$

Roughly speaking, the standard error tells us the average amount that this estimate $\hat{\mu}$ differs from the actual value of $\mu$.

Equation 3.7 also tells us how this deviation shrinks with $n$—the more observations we have, the smaller the standard error of $\hat{\mu}$.

In a similar vein, we can wonder how close $\hat{\beta}_0$ and $\hat{\beta}_1$ are to the true values $\beta_0$ and $\beta_1$.

To compute the standard errors associated with $\hat{\beta}_0$ and $\hat{\beta}_1$, we use the following formulas:

$$
\text{SE}(\hat{\beta}_0)^2 = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right], \quad \text{SE}(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \quad (3.8)
$$

where $\sigma^2 = \text{Var}(\epsilon)$.

For these formulas to be strictly valid, we need to assume that the errors $\epsilon_i$ for each observation have common variance $\sigma^2$ and are uncorrelated.

This is clearly not true in Figure 3.1, but the formula still turns out to be a good approximation.

Notice in the formula that $\text{SE}(\hat{\beta}_1)$ is smaller when the $x_i$ are more spread out; intuitively we have more _leverage_ to estimate a slope when this is the case.

We also see that $\text{SE}(\hat{\beta}_0)$ would be the same as $\text{SE}(\hat{\mu})$ if $\bar{x}$ were zero (in which case $\hat{\beta}_0$ would be equal to $\bar{y}$).

In general, $\sigma^2$ is not known, but can be estimated from the data.

This estimate of $\sigma$ is known as the _residual standard error_, and is given by the formula $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$.

Strictly speaking, when $\sigma^2$ is estimated from the data we should write $\widehat{\text{SE}}(\hat{\beta}_1)$ to indicate that an estimate has been made, but for simplicity of notation we will drop this extra “hat”.

That is, there is approximately a 95% chance that the interval

$$
\left[ \hat{\beta}_1 - 2 \cdot \text{SE}(\hat{\beta}_1), \, \hat{\beta}_1 + 2 \cdot \text{SE}(\hat{\beta}_1) \right] \quad (3.10)
$$

will contain the true value of $\beta_1$.$^3$

Similarly, a confidence interval for $\beta_0$ approximately takes the form

$$
\hat{\beta}_0 \pm 2 \cdot \text{SE}(\hat{\beta}_0) \quad (3.11)
$$

In the case of the advertising data, the 95% confidence interval for $\beta_0$ is $[6.130, 7.935]$ and the 95% confidence interval for $\beta_1$ is $[0.042, 0.053]$.

Therefore, we can conclude that in the absence of any advertising, sales will, on average, fall somewhere between 6,130 and 7,935 units.

Furthermore, for each $\$1,000$ increase in television advertising, there will be an average increase in sales of between 42 and 53 units.

Standard errors can also be used to perform _hypothesis tests_ on the coefficients.

The most common hypothesis test involves testing the _null hypothesis_ of

$$
H_0 : \beta_1 = 0 \quad (3.12)
$$

versus the _alternative hypothesis_

$$
H_a : \beta_1 \neq 0 \quad (3.13)
$$

Mathematically, this corresponds to testing

$$
H_0 : \text{There is no relationship between } X \text{ and } Y
$$

versus

$$
H_a : \text{There is some relationship between } X \text{ and } Y
$$

since if $\beta_1 = 0$ then the model (3.5) reduces to $Y = \beta_0 + \epsilon$, and $X$ is not associated with $Y$.

To test the null hypothesis, we need to determine whether $\hat{\beta}_1$, our estimate for $\beta_1$, is sufficiently far from zero that we can be confident that $\beta_1$ is non-zero.

How far is far enough?

This of course depends on the accuracy of $\hat{\beta}_1$—that is, it depends on $\text{SE}(\hat{\beta}_1)$.

If $\text{SE}(\hat{\beta}_1)$ is small, then even relatively small values of $\hat{\beta}_1$ may provide strong evidence that $\beta_1 \neq 0$, and hence that there is a relationship between $X$ and $Y$.

In contrast, if $\text{SE}(\hat{\beta}_1)$ is large, then $\hat{\beta}_1$ must be large in absolute value in order for us to reject the null hypothesis.

In practice, we compute a _$t$-statistic_, given by

$$
t = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{\beta}_1)} \quad (3.14)
$$

> $^3$ _Approximately_ for several reasons.

> Equation 3.10 relies on the assumption that the errors are Gaussian.

> Also, the factor of 2 in front of the $\text{SE}(\hat{\beta}_1)$ term will vary slightly depending on the number of observations $n$ in the linear regression.

> To be precise, rather than the number 2, (3.10) should contain the 97.5% quantile of a $t$-distribution with $n-2$ degrees of freedom.

> Details of how to compute the 95% confidence interval precisely in `R` will be provided later in this chapter.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 7.0325 | 0.4578 | 15.36 | $< 0.0001$ |
| `TV` | 0.0475 | 0.0027 | 17.67 | $< 0.0001$ |

**TABLE 3.1.** _For the_ `Advertising` _data, coefficients of the least squares model for the regression of number of units sold on TV advertising budget. An increase of_ $\$1,000$ _in the TV advertising budget is associated with an increase in sales by around 50 units. (Recall that the_ `sales` _variable is in thousands of units, and the_ `TV` _variable is in thousands of dollars.)_

which measures the number of standard deviations that $\hat{\beta}_1$ is away from 0.

If there really is no relationship between $X$ and $Y$, then we expect that (3.14) will have a $t$-distribution with $n - 2$ degrees of freedom.

The $t$-distribution has a bell shape and for values of $n$ greater than approximately 30 it is quite similar to the standard normal distribution.

Consequently, it is a simple matter to compute the probability of observing any number equal to $|t|$ or larger in absolute value, assuming $\beta_1 = 0$.

We call this probability the _$p$-value_.

Roughly speaking, we interpret the $p$-value as follows: a small $p$-value indicates that it is unlikely to observe such a substantial association between the predictor and the response due to chance, in the absence of any real association between the predictor and the response.

Hence, if we see a small $p$-value, then we can infer that there is an association between the predictor and the response.

We _reject the null hypothesis_—that is, we declare a relationship to exist between $X$ and $Y$—if the $p$-value is small enough.

Typical $p$-value cutoffs for rejecting the null hypothesis are 5% or 1%, although this topic will be explored in much greater detail in Chapter 13.

When $n = 30$, these correspond to $t$-statistics (3.14) of around 2 and 2.75, respectively.

Table 3.1 provides details of the least squares model for the regression of number of units sold on TV advertising budget for the `Advertising` data.

Notice that the coefficients for $\hat{\beta}_0$ and $\hat{\beta}_1$ are very large relative to their standard errors, so the $t$-statistics are also large; the probabilities of seeing such values if $H_0$ is true are virtually zero.

Hence we can conclude that $\beta_0 \neq 0$ and $\beta_1 \neq 0$.$^4$

---

---



## Sub-Chapters

This is the document for 3.1.2 Assessing the Accuracy of the Coefficient Estimates.

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/index.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/index.html)

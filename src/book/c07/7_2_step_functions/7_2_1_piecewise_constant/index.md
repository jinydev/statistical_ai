---
layout: default
title: "index"
---

# **Piecewise Constant** 

![Figure 7.2](./img/7_2.png)

**FIGURE 7.2.** _The_ `Wage` _data._ Left: _The solid curve displays the fitted value from a least squares regression of_ `wage` _(in thousands of dollars) using step functions of_ `age` _. The dashed curves indicate an estimated 95 % confidence interval._ Right: _We model the binary event_ `wage>250` _using logistic regression, again using step functions of_ `age` _. The fitted posterior probability of_ `wage` _exceeding_ $250 _,_ 000 _is shown, along with an estimated 95 % confidence interval._ 

be interpreted as the mean value of _Y_ for _X < c_ 1. By comparison, (7.5) predicts a response of _β_ 0+ _βj_ for _cj ≤ X < cj_ +1, so _βj_ represents the average increase in the response for _X_ in _cj ≤ X < cj_ +1 relative to _X < c_ 1. 

An example of fitting step functions to the `Wage` data from Figure 7.1 is shown in the left-hand panel of Figure 7.2. We also fit the logistic regression model

$$
\Pr(y_i > 250 \mid x_i) = \frac{\exp(\beta_0 + \beta_1 C_1(x_i) + \dots + \beta_K C_K(x_i))}{1 + \exp(\beta_0 + \beta_1 C_1(x_i) + \dots + \beta_K C_K(x_i))} \quad (7.6)
$$

in order to predict the probability that an individual is a high earner on the basis of `age` . The right-hand panel of Figure 7.2 displays the fitted posterior probabilities obtained using this approach. 

Unfortunately, unless there are natural breakpoints in the predictors, piecewise-constant functions can miss the action. For example, in the lefthand panel of Figure 7.2, the first bin clearly misses the increasing trend of `wage` with `age` . Nevertheless, step function approaches are very popular in biostatistics and epidemiology, among other disciplines. For example, 5-year age groups are often used to define the bins. 

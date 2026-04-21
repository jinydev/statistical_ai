---
layout: default
title: "index"
---

[< 3.2 Multiple Linear Regression](../index.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.2.1 Estimating the Regression Coefficients_

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula

$$

\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)

$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals

$$

\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)

$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4

<br>

<p align="center">

<img src="./img/3_4.png" alt="In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.">

</p>

<br>

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._

illustrates an example of the least squares fit to a toy data set with $p=2$ predictors.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data.

We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales.

Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates.

However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86.

This illustrates that the simple and multiple regression coefficients can be quite different.

This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`.

By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the opposite?

In fact it does.

Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5.

| | Coefficient | Std. error | $t$-statistic | $p$-value |

| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |

| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |

**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._

| | `TV` | `radio` | `newspaper` | `sales` |

| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |

| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |

**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._

Notice that the correlation between `radio` and `newspaper` is 0.35.

This indicates that markets with high newspaper advertising tend to also have high radio advertising.

Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales.

Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets.

Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales.

So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` .

This slightly counterintuitive result is very common in many real life situations.

Consider an absurd example to illustrate the point.

Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper` .

Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks.

In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks.

A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.

---

---

---

## Sub-Chapters


[< 3.2 Multiple Linear Regression](../index.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/index.html)

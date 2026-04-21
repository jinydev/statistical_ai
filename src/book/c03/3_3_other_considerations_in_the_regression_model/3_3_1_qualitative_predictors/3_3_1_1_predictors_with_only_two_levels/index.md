---
layout: default
title: "index"
---

[< 3.3.1 Qualitative Predictors](../index.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Predictors with Only Two Levels

Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don’t, ignoring the other variables for the moment.

If a qualitative predictor (also known as a _factor_) only has two _levels_, or possible values, then incorporating it into a regression model is very simple.

We simply create an indicator or _dummy variable_ that takes on two possible numerical values.[10]

For example, based on the `own` variable, we can create a new variable that takes the form

$$

x_i = \begin{cases}
1 & \text{if } i\text{th person owns house} \\
0 & \text{if } i\text{th person does not own house}
\end{cases}

$$

and use this variable as a predictor in the regression equation.

This results in the model

$$

y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{th person owns house} \\
\beta_0 + \epsilon_i & \text{if } i\text{th person does not own house}
\end{cases} \quad (3.27)

$$

Now \beta_0 can be interpreted as the average credit card balance among those who do not own, \beta_0 + \beta_1 as the average credit card balance among those who do own their house, and \beta_1 as the average difference in credit card balance between owners and non-owners.

> [10] In the machine learning community, the creation of dummy variables to handle qualitative predictors is known as "one-hot encoding".

**==> picture [300 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 40 60 80 100 5 10 15 20 2000 8000 14000<br>Balance<br>Age<br>Cards<br>Education<br>Income<br>Limit<br>Rating<br>0 500 1500 2 4 6 8 50 100 150 200 600 1000<br>1500<br>500<br>0<br>100<br>80<br>60<br>40<br>20<br>8<br>6<br>4<br>2<br>20<br>15<br>10<br>5<br>150<br>100<br>50<br>14000<br>8000<br>2000<br>1000<br>600<br>200<br>**----- End of picture text -----**<br>

**FIGURE 3.6.** _The_ `Credit` _data set contains information about_ `balance` _,_ `age` _,_ `cards` _,_ `education` _,_ `income` _,_ `limit` _, and_ `rating` _for a number of potential customers._

notice that the $p$-value for the dummy variable is very high. This indicates that there is no statistical evidence of a difference in average credit card balance based on house ownership.

The decision to code owners as $1$ and non-owners as $0$ in (3.27) is arbitrary, and has no effect on the regression fit, but does alter the interpretation of the coefficients.

If we had coded non-owners as $1$ and owners as $0$, then the estimates for $\beta_0$ and $\beta_1$ would have been $529.53$ and $-19.73$, respectively, leading once again to a prediction of credit card debt of $\$529.53 - \$19.73 = \$509.80$ for non-owners and a prediction of $\$529.53$ for owners.

Alternatively, instead of a $0 / 1$ coding scheme, we could create a dummy variable

$$
x_i = \begin{cases}
1 & \text{if } i\text{th person owns house} \\
-1 & \text{if } i\text{th person does not own house}
\end{cases}
$$

and use this variable in the regression equation.

This results in the model

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{th person owns house} \\
\beta_0 - \beta_1 + \epsilon_i & \text{if } i\text{th person does not own house}
\end{cases} \quad (3.28)
$$

3.3 Other Considerations in the Regression Model 93

|3.3 Other Considerations in the Regression Model|3.3 Other Considerations in the Regression Model|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`own[Yes]`|509.80<br>33.13<br>15.389<br>_<_0_._0001<br>19.73<br>46.05<br>0.429<br>0.6690|

**TABLE 3.7.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `own` _in the_ `Credit` _data set. The linear model is given in (3.27). That is, ownership is encoded as a dummy variable, as in (3.26)._

Now $\beta_0$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_1$ is the amount by which house owners and non-owners have credit card balances that are above and below the average, respectively.[11]

In this example, the estimate for $\beta_0$ is $\$519.665$, halfway between the non-owner and owner averages of $\$509.80$ and $\$529.53$.

The estimate for $\beta_1$ is $\$9.865$, which is half of $\$19.73$, the average difference between owners and non-owners.

It is important to note that the final predictions for the credit balances of owners and non-owners will be identical regardless of the coding scheme used.

The only difference is in the way that the coefficients are interpreted.

Qualitative Predictors with More than Two Levels

When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values.

In this situation, we can create additional dummy variables.

For example, for the `region` variable we create two dummy variables. The first could be

**==> picture [268 x 31] intentionally omitted <==**

and the second could be

**==> picture [267 x 31] intentionally omitted <==**

Then both of these variables can be used in the regression equation, in order to obtain the model

**==> picture [294 x 39] intentionally omitted <==**

(3.30)

Now $\beta_0$ can be interpreted as the average credit card balance for individuals from the East, $\beta_1$ can be interpreted as the difference in the average balance between people from the South versus the East, and $\beta_2$ can be interpreted as the difference in the average balance between those from the West versus the East.

There will always be one fewer dummy variable than the number of levels.

The level with no dummy variable — East in this example — is known as the __.

> [11] Technically $\beta_0$ is half the sum of the average debt for house owners and the average debt for non-house owners. Hence, $\beta_0$ is exactly equal to the overall average only if the two groups have an equal number of members.

94 3. Linear Regression

|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`region[South]`<br>`region[West]`|531.00<br>46.32<br>11.464<br>_<_0_._0001<br>_−_12.50<br>56.68<br>_−_0.221<br>0.8260<br>_−_18.69<br>65.02<br>_−_0.287<br>0.7740|

**TABLE 3.8.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `region` _in the_ `Credit` _data set. The linear model is given in (3.30). That is, region is encoded via two dummy variables (3.28) and (3.29)._

From Table 3.8, we see that the estimated `balance` for the , East, is $531 _._ 00. It is estimated that those in the South will have $18 _._ 69 less debt than those in the East, and that those in the West will have $12 _._ 50 less debt than those in the East. However, the $p$-values associated with the coefficient estimates for the two dummy variables are very large, suggesting no statistical evidence of a real difference in average credit card balance between South and East or between West and East.[12] Once again, the level selected as the  category is arbitrary, and the final predictions for each group will be the same regardless of this choice. However, the coefficients and their $p$-values do depend on the choice of dummy variable coding. Rather than rely on the individual coefficients, we can use an _F_ -test to test $H_0$ : \beta_1 = \beta_2 = 0; this does not depend on the coding. This _F_ -test has a $p$-value of 0 _._ 96, indicating that we cannot reject the null hypothesis that there is no relationship between `balance` and `region` .

Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors.

For example, to regress `balance` on both a quantitative variable such as `income` and a qualitative variable such as `student`, we must simply create a dummy variable for `student` and then fit a multiple regression model using `income` and the dummy variable as predictors for credit card balance.

There are many different ways of coding qualitative variables besides the dummy variable approach taken here.

All of these approaches lead to equivalent model fits, but the coefficients are different and have different interpretations, and are designed to measure particular _contrasts_.

This topic is beyond the scope of the book.

---

## Sub-Chapters


[< 3.3.1 Qualitative Predictors](../index.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/index.html)

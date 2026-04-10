---
layout: default
title: "index"
---

# _4.3.4 Multiple Logistic Regression_ 

We now consider the problem of predicting a binary response using multiple predictors. By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows: 

$$
\log\left(
rac{p(X)}{1 - p(X)}
ight) = eta_0 + eta_1 X_1 + \dots + eta_p X_p \quad (4.6)
$$

$$
p(X) = 
rac{e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p}}{1 + e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p}} \quad (4.7)
$$

4.3 Logistic Regression 143 

||Coefcient|Std. error|_z_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|_−_10.8690|0.4923|_−_22.08|_<_0.0001|
|`balance`|0.0057|0.0002|24.74|_<_0.0001|
|`income`|0.0030|0.0082|0.37|0.7115|
|`student[Yes]`|_−_0.6468|0.2362|_−_2.74|0.0062|



**TABLE 4.3.** _For the_ `Default` _data, estimated coefficients of the logistic regression model that predicts the probability of_ `default` _using_ `balance` _,_ `income` _, and student status. Student status is encoded as a dummy variable_ `student[Yes]` _, with a value of_ 1 _for a student and a value of_ 0 _for a non-student. In fitting this model,_ `income` _was measured in thousands of dollars._ 

Just as in Section 4.3.2, we use the maximum likelihood method to estimate _β_ 0 _, β_ 1 _, . . . , βp_ . 

Table 4.3 shows the coefficient estimates for a logistic regression model that uses `balance` , `income` (in thousands of dollars), and `student` status to predict probability of `default` . There is a surprising result here. The _p_ - values associated with `balance` and the dummy variable for `student` status are very small, indicating that each of these variables is associated with the probability of `default` . However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than nonstudents. In contrast, the coefficient for the dummy variable is positive in Table 4.2. How is it possible for student status to be associated with an _increase_ in probability of default in Table 4.2 and a _decrease_ in probability of default in Table 4.3? The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox. The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance. The negative coefficient for `student` in the multiple logistic regression indicates that _for a fixed value of_ `balance` _and_ `income` , a student is less likely to default than a non-student. Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of `balance` . But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of `balance` and `income` , suggest the opposite effect: the overall student default rate is higher than the non-student default rate. Consequently, there is a positive coefficient for `student` in the single variable logistic regression output shown in Table 4.2. 

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy. The variables `student` and `balance` are correlated. Students tend to hold higher levels of debt, which is in turn associated with higher probability of default. In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates. Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students. This is an important distinction for a credit card company that is trying to determine to whom they should offer credit. A student is riskier than a non-student if no information about the student’s credit card 

144 4. Classification 

![Figure 4.3](./img/4_3.png)

**FIGURE 4.3.** _Confounding in the_ `Default` _data._ Left: _Default rates are shown for students (orange) and non-students (blue). The solid lines display default rate as a function of_ `balance` _, while the horizontal broken lines display the overall default rates._ Right: _Boxplots of_ `balance` _for students (orange) and non-students (blue) are shown._ 

balance is available. However, that student is less risky than a non-student _with the same credit card balance_ ! 

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant. As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors. In general, the phenomenon seen in Figure 4.3 is known as _confounding_ . 

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions. For example, a student with a credit card balance of $1,500 and an income of $40,000 has an estimated probability of default of 

$$
\hat{p}(X) = 
rac{e^{-10.869 + 0.00574 	imes 1500 + 0.003 	imes 40 - 0.6468 	imes 1}}{1 + e^{-10.869 + 0.00574 	imes 1500 + 0.003 	imes 40 - 0.6468 	imes 1}} = 0.058
$$

A non-student with the same balance and income has an estimated probability of default of 

$$
\hat{p}(X) = 
rac{e^{-10.869 + 0.00574 	imes 1500 + 0.003 	imes 40 - 0.6468 	imes 0}}{1 + e^{-10.869 + 0.00574 	imes 1500 + 0.003 	imes 40 - 0.6468 	imes 0}} = 0.105
$$

(Here we multiply the `income` coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with `income` measured in units of $1 _,_ 000.) 

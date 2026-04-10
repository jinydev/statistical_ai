---
layout: default
title: "index"
---

# 6. Collinearity 

_Collinearity_ refers to the situation in which two or more predictor variables collinearity are closely related to one another. The concept of collinearity is illustrated in Figure 3.14 using the `Credit` data set. In the left-hand panel of Figure 3.14, the two predictors `limit` and `age` appear to have no obvious relationship. In contrast, in the right-hand panel of Figure 3.14, the predictors `limit` and `rating` are very highly correlated with each other, and we say that they are _collinear_ . The presence of collinearity can pose problems in the regression context, since it can be difficult to separate out the individual effects of collinear variables on the response. In other words, since `limit` and `rating` tend to increase or decrease together, it can be difficult to determine how each one separately is associated with the response, `balance` . 

Figure 3.15 illustrates some of the difficulties that can result from collinearity. The left-hand panel of Figure 3.15 is a contour plot of the RSS (3.22) associated with different possible coefficient estimates for the regression of `balance` on `limit` and `age` . Each ellipse represents a set of coefficients 

3.3 Other Considerations in the Regression Model 107 

**==> picture [319 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.16 0.17 0.18 0.19 −0.1 0.0 0.1 0.2<br>βLimit βLimit<br> 21.8<br> 21.5<br> 21.25<br> 21.8<br> 21.5<br>5<br>0<br>4<br>−1<br>3<br>Age −2<br>β Rating 2<br>β<br>−3<br>1<br>−4<br>0<br>−5<br>**----- End of picture text -----**<br>


**FIGURE 3.15.** _Contour plots for the RSS values as a function of the parameters β for various regressions involving the_ `Credit` _data set. In each plot, the black dots represent the coefficient values corresponding to the minimum RSS._ Left: _A contour plot of RSS for the regression of_ `balance` _onto_ `age` _and_ `limit` _. The minimum value is well defined._ Right: _A contour plot of RSS for the regression of_ `balance` _onto_ `rating` _and_ `limit` _. Because of the collinearity, there are many pairs_ ( _β_ Limit _, β_ Rating) _with a similar value for RSS._ 

that correspond to the same RSS, with ellipses nearest to the center taking on the lowest values of RSS. The black dots and associated dashed lines represent the coefficient estimates that result in the smallest possible RSS—in other words, these are the least squares estimates. The axes for `limit` and `age` have been scaled so that the plot includes possible coefficient estimates that are up to four standard errors on either side of the least squares estimates. Thus the plot includes all plausible values for the coefficients. For example, we see that the true `limit` coefficient is almost certainly somewhere between 0 _._ 15 and 0 _._ 20. 

In contrast, the right-hand panel of Figure 3.15 displays contour plots of the RSS associated with possible coefficient estimates for the regression of `balance` onto `limit` and `rating` , which we know to be highly collinear. Now the contours run along a narrow valley; there is a broad range of values for the coefficient estimates that result in equal values for RSS. Hence a small change in the data could cause the pair of coefficient values that yield the smallest RSS—that is, the least squares estimates—to move anywhere along this valley. This results in a great deal of uncertainty in the coefficient estimates. Notice that the scale for the `limit` coefficient now runs from roughly _−_ 0 _._ 2 to 0 _._ 2; this is an eight-fold increase over the plausible range of the `limit` coefficient in the regression with `age` . Interestingly, even though the `limit` and `rating` coefficients now have much more individual uncertainty, they will almost certainly lie somewhere in this contour valley. For example, we would not expect the true value of the `limit` and `rating` coefficients to be _−_ 0 _._ 1 and 1 respectively, even though such a value is plausible for each coefficient individually. 

Since collinearity reduces the accuracy of the estimates of the regression coefficients, it causes the standard error for \hat{\beta} _j_ to grow. Recall that the $t$-statistic for each predictor is calculated by dividing \hat{\beta} _j_ by its standard 

108 3. Linear Regression 

|108<br>3. Linear Regression|108<br>3. Linear Regression|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>Model 1<br>`age`<br>`limit`|_−_173.411<br>43.828<br>_−_3.957<br>_<_0_._0001<br>_−_2.292<br>0.672<br>_−_3.407<br>0_._0007<br>0.173<br>0.005<br>34.496<br>_<_0_._0001|
|`Intercept`<br>Model 2<br>`rating`<br>`limit`|_−_377.537<br>45.254<br>_−_8.343<br>_<_0_._0001<br>2.202<br>0.952<br>2.312<br>0.0213<br>0.025<br>0.064<br>0.384<br>0.7012|



**TABLE 3.11.** _The results for two multiple regression models involving the_ `Credit` _data set are shown. Model 1 is a regression of_ `balance` _on_ `age` _and_ `limit` _, and Modelβ_ ˆlimit _increases2 a regression12-fold ofin_ `balance` _the secondonregression,_ `rating` _anddue_ `limit` _to collinearity.. The standard error of_ 

error. Consequently, collinearity results in a decline in the $t$-statistic. As a result, in the presence of collinearity, we may fail to reject $H_0$ : $\beta_j$ = 0. This means that the _power_ of the hypothesis test—the probability of correctly power detecting a _non-zero_ coefficient—is reduced by collinearity. 

Table 3.11 compares the coefficient estimates obtained from two separate multiple regression models. The first is a regression of `balance` on `age` and `limit` , and the second is a regression of `balance` on `rating` and `limit` . In the first regression, both `age` and `limit` are highly significant with very small $p$-values. In the second, the collinearity between `limit` and `rating` has caused the standard error for the `limit` coefficient estimate to increase by a factor of 12 and the $p$-value to increase to 0 _._ 701. In other words, the importance of the `limit` variable has been masked due to the presence of collinearity. To avoid such a situation, it is desirable to identify and address potential collinearity problems while fitting the model. 

A simple way to detect collinearity is to look at the correlation matrix of the predictors. An element of this matrix that is large in absolute value indicates a pair of highly correlated variables, and therefore a collinearity problem in the data. Unfortunately, not all collinearity problems can be detected by inspection of the correlation matrix: it is possible for collinearity to exist between three or more variables even if no pair of variables has a particularly high correlation. We call this situation _multicollinearity_ . multiInstead of inspecting the correlation matrix, a better way to assess multicollinearity is to compute the _variance inflation factor_ (VIF). The VIF is variance the ratio of the variance of \hat{\beta} _j_ when fitting the full model divided by the inflation variance of \hat{\beta} _j_ if fit on its own. The smallest possible value for VIF is 1, factor which indicates the complete absence of collinearity. Typically in practice there is a small amount of collinearity among the predictors. As a rule of thumb, a VIF value that exceeds 5 or 10 indicates a problematic amount of collinearity. The VIF for each variable can be computed using the formula 

collinearity variance inflation factor 

**==> picture [108 x 26] intentionally omitted <==**

where _RX_[2] _j |X−j_[is][the] _[R]_[2][from][a][regression][of] _[X][j]_[onto][all][of][the][other] predictors. If _RX_[2] _j |X−j_[is][close][to][one,][then][collinearity][is][present,][and][so] the VIF will be large. 

3.4 The Marketing Plan 109 

In the `Credit` data, a regression of `balance` on `age` , `rating` , and `limit` indicates that the predictors have VIF values of 1.01, 160.67, and 160.59. As we suspected, there is considerable collinearity in the data! 

When faced with the problem of collinearity, there are two simple solutions. The first is to drop one of the problematic variables from the regression. This can usually be done without much compromise to the regression fit, since the presence of collinearity implies that the information that this variable provides about the response is redundant in the presence of the other variables. For instance, if we regress `balance` onto `age` and `limit` , without the `rating` predictor, then the resulting VIF values are close to the minimum possible value of 1, and the $R^2$ drops from 0 _._ 754 to 0 _._ 75. So dropping `rating` from the set of predictors has effectively solved the collinearity problem without compromising the fit. The second solution is to combine the collinear variables together into a single predictor. For instance, we might take the average of standardized versions of `limit` and `rating` in order to create a new variable that measures _credit worthiness_ . 

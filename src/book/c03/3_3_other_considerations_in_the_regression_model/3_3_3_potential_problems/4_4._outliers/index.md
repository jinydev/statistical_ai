---
layout: default
title: "index"
---

# 4. Outliers 

An _outlier_ is a point for which y_i is far from the value predicted by the outlier 

104 3. Linear Regression 

**==> picture [321 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20 20<br>−2 −1 0 1 2 −2 0 2 4 6 −2 0 2 4 6<br>X Fitted Values Fitted Values<br>6<br>6 4<br>4 3 4<br>Y 2 2 2<br>0 Residuals 1<br>−2 0 Studentized Residuals 0<br>−1<br>−4<br>**----- End of picture text -----**<br>


**FIGURE 3.12.** Left: _The least squares regression line is shown in red, and the regression line after removing the outlier is shown in blue._ Center: _The residual plot clearly identifies the outlier._ Right: _The outlier has a studentized residual of_ 6 _; typically we expect values between −_ 3 _and_ 3 _._ 

model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection. 

The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier. The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier. In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept. It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit. However, even if an outlier does not have much effect on the least squares fit, it can cause other problems. For instance, in this example, the RSE is 1 _._ 09 when the outlier is included in the regression, but it is only 0 _._ 77 when the outlier is removed. Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit. Similarly, inclusion of the outlier causes the $R^2$ to decline from 0 _._ 892 to 0 _._ 805. 

Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier. To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_ , computed by dividing each residual _ei_ by its estimated standard studentized error. Observations whose studentized residuals are greater than 3 in absoresidual lute value are possible outliers. In the right-hand panel of Figure 3.12, the outlier’s studentized residual exceeds 6, while all other observations have studentized residuals between _−_ 2 and 2. 

If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation. However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor. 

5. High Leverage Points 

We just saw that outliers are observations for which the response y_i is unusual given the predictor x_i . In contrast, observations with _high leverage_ high have an unusual value for x_i . For example, observation 41 in the left-hand 

leverage 

3.3 Other Considerations in the Regression Model 105 

**==> picture [318 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
41 20<br>41<br>20<br>−2 −1 0 1 2 3 4 −2 −1 0 1 2 0.00 0.05 0.10 0.15 0.20 0.25<br>X X1 Leverage<br>2 5<br>4<br>10 1<br>3<br>Y 5 X2 0 2<br>1<br>−1<br>0 Studentized Residuals 0<br>−2 −1<br>**----- End of picture text -----**<br>


**FIGURE 3.13.** Left: _Observation 41 is a high leverage point, while 20 is not. The red line is the fit to all the data, and the blue line is the fit with observation 41 removed._ Center: _The red observation is not unusual in terms of its X_ 1 _value or its X_ 2 _value, but still falls outside the bulk of the data, and hence has high leverage._ Right: _Observation_ 41 _has a high leverage and a high residual._ 

panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high leverage observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high leverage observations. 

In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$. Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously. 

In order to quantify an observation’s leverage, we compute the _leverage statistic_ . A large value of this statistic indicates an observation with high leverage leverage. For a simple linear regression, 

**==> picture [220 x 26] intentionally omitted <==**

statistic 

106 3. Linear Regression 

**==> picture [318 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
2000 4000 6000 8000 12000 2000 4000 6000 8000 12000<br>Limit Limit<br>80<br>800<br>70<br>60 600<br>Age<br>Rating<br>50<br>400<br>40<br>30 200<br>**----- End of picture text -----**<br>


**FIGURE 3.14.** _Scatterplots of the observations from the_ `Credit` _data set._ Left: _A plot of_ `age` _versus_ `limit` _. These two variables are not collinear._ Right: _A plot of_ `rating` _versus_ `limit` _. There is high collinearity._ 

It is clear from this equation that _hi_ increases with the distance of x_i from ¯ _x_ . There is a simple extension of _hi_ to the case of multiple predictors, though we do not provide the formula here. The leverage statistic _hi_ is always between 1 _/n_ and 1, and the average leverage for all the observations is always equal to ( $p$ + 1) _/n_ . So if a given observation has a leverage statistic that greatly exceeds ( $p$ +1) _/n_ , then we may suspect that the corresponding point has high leverage. 

The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus _hi_ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage. 

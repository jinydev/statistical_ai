---
layout: default
title: "index"
---

[< 3.3.3 Potential Problems](../index.html) | [3 3. Non-Constant Variance Of Error Terms >](../3_3._non-constant_variance_of_error_terms/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2. Correlation of Error Terms

An important assumption of the linear regression model is that the error terms, $\epsilon_1, \epsilon_2, \dots, \epsilon_n$, are uncorrelated.

What does this mean?

For instance, if the errors are uncorrelated, then the fact that $\epsilon_i$ is positive provides little or no information about the sign of $\epsilon_{i+1}$.

The standard errors that are computed for the estimated regression coefficients or the fitted values are based on the assumption of uncorrelated error terms.

If in fact there is correlation among the error terms, then the estimated standard errors will tend to underestimate the true standard errors.

As a result, confidence and prediction intervals will be narrower than they should be.

For example, a $95\%$ confidence interval may in reality have a much lower probability than $0.95$ of containing the true value of the parameter.

In addition, $p$-values associated with the model will be lower than they should be; this could cause us to erroneously conclude that a parameter is statistically significant.

In short, if the error terms are correlated, we may have an unwarranted sense of confidence in our model.

As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs.

If we ignored this, our standard error calculations would be as if we had a sample of size $2n$, when in fact we have only $n$ samples.

Our estimated parameters would be the same for the $2n$ samples as for the $n$ samples, but the confidence intervals would be narrower by a factor of $\sqrt{2}$!

Why might correlations among the error terms occur?

Such correlations frequently occur in the context of _time series_ data, which consists of observations for which measurements are obtained at discrete points in time.

In many cases, observations that are obtained at adjacent time points will have positively correlated errors.

In order to determine if this is the case for a given data set, we can plot the residuals from our model as a function of time.

If the errors are uncorrelated, then there should be no discernible pattern.

**==> picture [317 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ =0.0<br>0 20 40 60 80 100<br>ρ =0.5<br>0 20 40 60 80 100<br>ρ =0.9<br>0 20 40 60 80 100<br>Observation<br>3<br>2<br>1<br>0<br>Residual −1<br>−3<br>2<br>1<br>0<br>Residual<br>−2<br>−4<br>1.5<br>0.5<br>Residual −0.5<br>−1.5<br>**----- End of picture text -----**<br>

**FIGURE 3.10.** _Plots of residuals from simulated time series data sets generated with differing levels of correlation ρ between error terms for adjacent time points._

On the other hand, if the error terms are positively correlated, then we may see _tracking_ in the residuals — that is, adjacent residuals may have similar values.

Figure 3.10 provides an illustration.

In the top panel, we see the residuals from a linear regression fit to data generated with uncorrelated errors.

There is no evidence of a time-related trend in the residuals.

In contrast, the residuals in the bottom panel are from a data set in which adjacent errors had a correlation of $0.9$.

Now there is a clear pattern in the residuals — adjacent residuals tend to take on similar values.

Finally, the center panel illustrates a more moderate case in which the residuals had a correlation of $0.5$.

There is still evidence of tracking, but the pattern is less clear.

Many methods have been developed to properly take account of correlations in the error terms in time series data.

Correlation among the error terms can also occur outside of time series data.

For instance, consider a study in which individuals' heights are predicted from their weights.

The assumption of uncorrelated errors could be violated if some of the individuals in the study are members of the same family, eat the same diet, or have been exposed to the same environmental factors.

In general, the assumption of uncorrelated errors is extremely important for linear regression as well as for other statistical methods, and good experimental design is crucial in order to mitigate the risk of such correlations.

3.3 Other Considerations in the Regression Model 103

**==> picture [315 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Response Y Response log(Y)<br>998<br>975<br>845<br>605<br>671<br>437<br>10 15 20 25 30 2.4 2.6 2.8 3.0 3.2 3.4<br>Fitted values Fitted values<br>15<br>0.4<br>10 0.2<br>5 0.0<br>0<br>Residuals Residuals −0.2<br>−5 −0.4<br>−10 −0.6<br>−0.8<br>**----- End of picture text -----**<br>

**FIGURE 3.11.** _Residual plots. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. The blue lines track the outer quantiles of the residuals, and emphasize patterns._ Left: _The funnel shape indicates heteroscedasticity._ Right: _The response has been log transformed, and there is now no evidence of heteroscedasticity._

---

## Sub-Chapters


[< 3.3.3 Potential Problems](../index.html) | [3 3. Non-Constant Variance Of Error Terms >](../3_3._non-constant_variance_of_error_terms/index.html)

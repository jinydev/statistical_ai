---
layout: default
title: "index"
---

[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/index.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Three: Model Fit

Two of the most common numerical measures of model fit are the RSE and $R^2$, the fraction of variance explained.

These quantities are computed and interpreted in the same fashion as for simple linear regression.

Recall that in simple regression, $R^2$ is the square of the correlation of the response and the variable.

In multiple linear regression, it turns out that it equals $\text{Cor}(Y, \hat{Y})^2$, the square of the correlation between the response and the fitted linear model; in fact one property of the fitted linear model is that it maximizes this correlation among all possible linear models.

An $R^2$ value close to 1 indicates that the model explains a large portion of the variance in the response variable.

As an example, we saw in Table 3.6 that for the `Advertising` data, the model that uses all three advertising media to predict `sales` has an $R^2$ of $0.8972$.

On the other hand, the model that uses only `TV` and `radio` to predict `sales` has an $R^2$ value of $0.89719$.

In other words, there is a _small_ increase in $R^2$ if we include newspaper advertising in the model that already contains TV and radio advertising, even though we saw earlier that the $p$-value for newspaper advertising in Table 3.4 is not significant.

It turns out that $R^2$ will always increase when more variables are added to the model, even if those variables are only weakly associated with the response.

This is due to the fact that adding another variable always results in a decrease in the residual sum of squares on the training data (though not necessarily the testing data).

Thus, the $R^2$ statistic, which is also computed on the training data, must increase.

The fact that adding newspaper advertising to the model containing only TV and radio advertising leads to just a tiny increase in $R^2$ provides additional evidence that `newspaper` can be dropped from the model.

Essentially, `newspaper` provides no real improvement in the model fit to the training samples, and its inclusion will likely lead to poor results on independent test samples due to overfitting.

By contrast, the model containing only `TV` as a predictor had an $R^2$ of $0.61$ (Table 3.2).

Adding `radio` to the model leads to a substantial improvement in $R^2$.

This implies that a model that uses TV and radio expenditures to predict sales is substantially better than one that uses only TV advertising.

We could further quantify this improvement by looking at the $p$-value for the `radio` coefficient in a model that contains only `TV` and `radio` as predictors.

The model that contains only `TV` and `radio` as predictors has an RSE of 1.681, and the model that also contains `newspaper` as a predictor has an RSE of 1.686 (Table 3.6).

In contrast, the model that contains only `TV` has an RSE of $3.26$ (Table 3.2).

This corroborates our previous conclusion that a model that uses TV and radio expenditures to predict sales is much more accurate (on the training data) than one that only uses TV spending.

Furthermore, given that TV and radio expenditures are used as predictors, there is no point in also using newspaper spending as a predictor in the model.

The observant reader may wonder how RSE can increase when `newspaper` is added to the model given that RSS must decrease. In general RSE is defined as

$$

\text{RSE} = \sqrt{\frac{1}{n-p-1} \text{RSS}} \quad (3.26)

$$

**==> picture [230 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sales<br>TV<br>Radio<br>**----- End of picture text -----**<br>

**FIGURE 3.5.** _For the_ `Advertising` _data, a linear regression fit to_ `sales` _using_ `TV` _and_ `radio` _as predictors. From the pattern of the residuals, we can see that there is a pronounced non-linear relationship in the data. The positive residuals (those visible above the surface), tend to lie along the 45-degree line, where TV and Radio budgets are split evenly. The negative residuals (most not visible), tend to lie away from this line, where budgets are more lopsided._

which simplifies to (3.15) for a simple linear regression.

Thus, models with more variables can have higher RSE if the decrease in RSS is small relative to the increase in $p$.

In addition to looking at the RSE and $R^2$ statistics just discussed, it can be useful to plot the data.

Graphical summaries can reveal problems with a model that are not visible from numerical statistics.

For example, Figure 3.5 displays a three-dimensional plot of `TV` and `radio` versus `sales`.

We see that some observations lie above and some observations lie below the least squares regression plane.

In particular, the linear model seems to overestimate `sales` for instances in which most of the advertising money was spent exclusively on either `TV` or `radio`.

It underestimates `sales` for instances where the budget was split between the two media.

This pronounced non-linear pattern suggests a _synergy_ or _interaction_ effect between the advertising media, whereby combining the media together results in a bigger boost to sales than using any single medium.

In Section 3.3.2, we will discuss extending the linear model to accommodate such synergistic effects through the use of interaction terms.

---

## Sub-Chapters


[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/index.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/index.html)

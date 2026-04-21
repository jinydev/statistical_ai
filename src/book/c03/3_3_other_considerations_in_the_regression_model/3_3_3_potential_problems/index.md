---
layout: default
title: "index"
---

[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/index.html) | [2 2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.3.3 Potential Problems_

When we fit a linear regression model to a particular data set, many problems may occur. Most common among these are the following:

1. _Non-linearity of the response-predictor relationships._

3. _Non-constant variance of error terms._

5. _High-leverage points._

In practice, identifying and overcoming these problems is as much an art as a science. Many pages in countless books have been written on this topic. Since the linear regression model is not our primary focus here, we will provide only a brief summary of some key points.

1. Non-linearity of the Data

**==> picture [318 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Residual Plot for Linear Fit Residual Plot for Quadratic Fit<br>323 334<br>330 323<br>334<br>155<br>5 10 15 20 25 30 15 20 25 30 35<br>Fitted values Fitted values<br>20<br>15<br>15<br>10<br>10<br>5<br>5<br>0<br>0<br>Residuals Residuals<br>−5<br>−5<br>−10<br>−10<br>−15<br>−15<br>**----- End of picture text -----**<br>

**FIGURE 3.9.** _Plots of residuals versus predicted (or fitted) values for the_ `Auto` _data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend._ Left: _A linear regression of_ `mpg` _on_ `horsepower` _. A strong pattern in the residuals indicates non-linearity in the data._ Right: _A linear regression of_ `mpg` _on_ `horsepower` _and_ `horsepower`[2] _. There is little pattern in the residuals._

The linear regression model assumes that there is a straight-line relationship between the predictors and the response. If the true relationship is far from linear, then virtually all of the conclusions that we draw from the fit are suspect. In addition, the prediction accuracy of the model can be significantly reduced.

_Residual plots_ are a useful graphical tool for identifying non-linearity. residual plot Given a simple linear regression model, we can plot the residuals, _ei_ =

3.3 Other Considerations in the Regression Model 101

ˆ _yi − yi_ , versus the predictor x_i . In the case of a multiple regression model, since there are multiple predictors, we instead plot the residuals versus ˆ the predicted (or _fitted_ ) values y_i . Ideally, the residual plot will show no fitted discernible pattern. The presence of a pattern may indicate a problem with some aspect of the linear model.

The left panel of Figure 3.9 displays a residual plot from the linear regression of `mpg` onto `horsepower` on the `Auto` data set that was illustrated in Figure 3.8. The red line is a smooth fit to the residuals, which is displayed in order to make it easier to identify any trends. The residuals exhibit a clear U-shape, which provides a strong indication of non-linearity in the data. In contrast, the right-hand panel of Figure 3.9 displays the residual plot that results from the model (3.36), which contains a quadratic term. There appears to be little pattern in the residuals, suggesting that the quadratic term improves the fit to the data.

If the residual plot indicates that there are non-linear associations in the data, then a simple approach is to use non-linear transformations of the predictors, such as log X , _√X_ , and X[2] , in the regression model. In the later chapters of this book, we will discuss other more advanced non-linear approaches for addressing this issue.

---

---

### 1. Non-linearity of the Data

### 2. Correlation of Error Terms

### 3. Non-constant Variance of Error Terms

### 4. Outliers

### 5. High Leverage Points

### 6. Collinearity

---

## Sub-Chapters


[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/index.html) | [2 2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/index.html)

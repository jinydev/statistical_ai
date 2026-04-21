---
layout: default
title: "index"
---

[< 2 2. Correlation Of Error Terms](../2_2._correlation_of_error_terms/index.html) | [4 4. Outliers >](../4_4._outliers/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3. Non-constant Variance of Error Terms

Another important assumption of the linear regression model is that the error terms have a constant variance, $\text{Var}(\epsilon_i) = \sigma^2$.

The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption.

Unfortunately, it is often the case that the variances of the error terms are non-constant.

For instance, the variances of the error terms may increase with the value of the response.

One can identify non-constant variances in the errors, or _hetero_, from the presence of a _funnel shape_ in the residual plot.

An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values.

When faced with this problem, one possible solution is to transform the response $Y$ using a concave function such as $\log Y$ or $\sqrt{Y}$.

Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in hetero.

The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using $\log Y$.

The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data.

Sometimes we have a good idea of the variance of each response.

For example, the $i$th response could be an average of $n_i$ raw observations.

If each of these raw observations is uncorrelated with variance $\sigma^2$, then their average has variance $\sigma_i^2 = \sigma^2 / n_i$.

In this case, a simple remedy is to fit our model by _weighted least squares_, with weights proportional to the inverse variances — i.e. $w_i = n_i$ in this case.

Most linear regression software allows for observation weights.

---

## Sub-Chapters


[< 2 2. Correlation Of Error Terms](../2_2._correlation_of_error_terms/index.html) | [4 4. Outliers >](../4_4._outliers/index.html)

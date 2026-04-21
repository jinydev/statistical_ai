---
layout: default
title: "index"
---

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/index.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.3.3 Making Predictions

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a `balance` of $1,000 is

$$
\hat{p}(X) = \frac{e^{-10.6513 + 0.0055 \times 1000}}{1 + e^{-10.6513 + 0.0055 \times 1000}} = 0.00576
$$

which is below 1%. In contrast, the predicted probability of default for an individual with a `balance` of $2,000 is much higher, and equals 0.586 or 58.6%.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the `Default` data set contains the qualitative variable `student` . To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students. The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated _p_-value is statistically significant. This indicates that students tend to have higher default probabilities than non-students:

$$
\begin{align*}
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{Yes}) &= \frac{e^{-3.5041 + 0.4049 \times 1}}{1 + e^{-3.5041 + 0.4049 \times 1}} = 0.0431 \\
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{No})  &= \frac{e^{-3.5041 + 0.4049 \times 0}}{1 + e^{-3.5041 + 0.4049 \times 0}} = 0.0292
\end{align*}
$$

---

## Sub-Chapters


[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/index.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/index.html)

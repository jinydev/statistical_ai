---
layout: default
title: "index"
---

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/index.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.3.5 Multinomial Logistic Regression

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure`. However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable.

It turns out that it is possible to extend the two-class logistic regression approach to the setting of $K > 2$ classes. This extension is sometimes known as _multinomial logistic regression_. To do this, we first select a single class to serve as the _baseline_; without loss of generality, we select the $K$th class for this role. Then we replace the model (4.7) with the model

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and

$$
\text{Pr}(Y = K \mid X = x) = \frac{1}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$,

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = \beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p \quad (4.11)
$$

Notice that (4.11) is quite similar to (4.6). Equation 4.11 indicates that once again, the log odds between any pair of classes is linear in the features.

It turns out that in (4.9)–(4.11), the decision to treat the $K$th class as the baseline is unimportant. For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline. The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline. For example, if we set `epileptic seizure` to be the baseline, then we can interpret $\beta_{\text{stroke}0}$ as the log odds of `stroke` versus `epileptic seizure`, given that $x_1 = \dots = x_p = 0$. Furthermore, a one-unit increase in $X_j$ is associated with a $\beta_{\text{stroke}j}$ increase in the log odds of `stroke` over `epileptic seizure`. Stated another way, if $X_j$ increases by one unit, then the ratio increases by $e^{\beta_{\text{stroke}j}}$.

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding. The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding. But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it. In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k = 1, \dots, K$,

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.13)
$$

Thus, rather than estimating coefficients for $K - 1$ classes, we actually estimate coefficients for all $K$ classes. It is not hard to see that as a result of (4.13), the log odds ratio between the $k$th and $k'$th classes equals

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = k' \mid X = x)} \right) = (\beta_{k0} - \beta_{k'0}) + (\beta_{k1} - \beta_{k'1}) x_1 + \dots + (\beta_{kp} - \beta_{k'p}) x_p \quad (4.14)
$$

---

## Sub-Chapters


[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/index.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/index.html)

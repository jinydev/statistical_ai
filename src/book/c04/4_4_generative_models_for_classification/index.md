---
layout: default
title: "index"
---

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/index.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.4 Generative Models for Classification

Logistic regression involves directly modeling $\text{Pr}(Y = k \mid X = x)$ using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$. We now consider an alternative and less direct approach to estimating these probabilities. In this new approach, we model the distribution of the predictors $X$ separately in each of the response classes (i.e. for each value of $Y$). We then use Bayes’ theorem to flip these around into estimates for $\text{Pr}(Y = k \mid X = x)$. When the distribution of $X$ within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.

Why do we need another method, when we have logistic regression? There are several reasons:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.
- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.
- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \ge 2$. In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values. Let $\pi_k$ represent the overall or _prior_ probability that a randomly chosen observation comes from the $k$th class. Let $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ denote the _density function_ of $X$ for an observation that comes from the $k$th class. In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$th class has $X \approx x$, and $f_k(x)$ is small if it is very unlikely that an observation in the $k$th class has $X \approx x$. Then _Bayes’ theorem_ states that

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)} \quad (4.15)
$$

In accordance with our earlier notation, we will use the abbreviation $p_k(x) = \text{Pr}(Y = k \mid X = x)$; this is the _posterior_ probability that an observation $X = x$ belongs to the $k$th class. That is, it is the probability that the observation belongs to the $k$th class, _given_ the predictor value for that observation.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers. In the following sections, we discuss three classifiers that use different estimates of $f_k(x)$ in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_.

---

### 4.4.1 Linear Discriminant Analysis for p = 1

### 4.4.2 Linear Discriminant Analysis for p > 1

### 4.4.3 Quadratic Discriminant Analysis

### 4.4.4 Naive Bayes

---

## Sub-Chapters


[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/index.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/index.html)

---
layout: default
title: "index"
---

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/index.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.4.4 Naive Bayes

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers. Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier.

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability $p_k(x) = \text{Pr}(Y = k \mid X = x)$ in terms of $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. To use (4.15) in practice, we need estimates for $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. As we saw in previous sections, estimating the prior probabilities $\pi_k$ is typically straightforward: we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$th class. 

However, estimating $f_1(x), \dots, f_K(x)$ is more subtle. Recall that $f_k(x)$ is the $p$-dimensional density function for an observation in the $k$th class. In general, estimating a $p$-dimensional density function is challenging. In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and shared covariance matrix $\mathbf{\Sigma}$. By contrast, in QDA, we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and class-specific covariance matrix $\mathbf{\Sigma}_k$. By making these very strong assumptions, we are able to replace the very challenging problem of estimating $K 	imes p$-dimensional density functions with the much simpler problem of estimating means and covariance matrices.

The naive Bayes classifier takes a different tack for estimating $f_1(x), \dots, f_K(x)$. Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single, sweeping assumption:

**Within the $k$th class, the $p$ predictors are independent.**

Stated mathematically, this assumption means that for $k = 1, \dots, K$,

$$
f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p) \quad (4.29)
$$

where $f_{kj}$ is the one-dimensional density function of the $j$th predictor among observations in the $k$th class.

Why is this assumption so powerful? Essentially, estimating a $p$-dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors. In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix. However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate. But by assuming that the $p$ covariates are independent within each class, we completely eliminate the need to worry about the association between the $p$ predictors, because we have simply assumed that there is _no_ association between the predictors!

Do we really believe the naive Bayes assumption that the $p$ covariates are independent within each class? In most settings, we do not. But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where $n$ is not large enough relative to $p$ for us to effectively estimate the joint distribution of the predictors within each class. In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings. Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability,

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k \times f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p)}{\sum_{l=1}^{K} \pi_l \times f_{l1}(x_1) \times f_{l2}(x_2) \times \dots \times f_{lp}(x_p)} \quad (4.30)
$$

for $k = 1, \dots, K$.

To estimate the one-dimensional density function $f_{kj}$ using training data, we have a few options:
- If $X_j$ is quantitative, we can assume it follows a univariate normal distribution, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- Alternatively, we can use a non-parametric estimate like a histogram or a kernel density estimator.
- If $X_j$ is qualitative, we simply count the proportion of training observations corresponding to each class instance.

---

## Sub-Chapters


[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/index.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/index.html)

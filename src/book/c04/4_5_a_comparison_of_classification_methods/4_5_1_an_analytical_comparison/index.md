---
layout: default
title: "index"
---

[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.5.1 An Analytical Comparison

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression. We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes $\text{Pr}(Y = k \mid X = x)$. Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) \quad (4.31)
$$

for $k = 1, \dots, K$. Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j \quad (4.32)
$$

where $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ and $b_{kj}$ is the $j$th component of $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$. Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$. Using similar calculations, in the QDA setting (4.31) becomes

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j + \sum_{j=1}^{p} \sum_{l=1}^{p} c_{kjl} x_j x_l \quad (4.33)
$$

where $a_k, b_{kj}$, and $c_{kjl}$ are functions of $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ and $\mathbf{\Sigma}_K$. Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in $x$.

Finally, we examine (4.31) in the naive Bayes setting. Recall that in this setting, $f_k(x)$ is modeled as a product of $p$ one-dimensional functions $f_{kj}(x_j)$ for $j = 1, \dots, p$. Hence,

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} g_{kj}(x_j) \quad (4.34)
$$

where $a_k = \log (\pi_k / \pi_K)$ and $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$. Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_, a topic that is discussed further in Chapter 7.

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:
- LDA is a special case of QDA with $c_{kjl} = 0$.
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj} x_j$. In particular, this means that LDA is a special case of naive Bayes!
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj}, \sigma_j^2)$, naive Bayes is actually a special case of LDA with $\mathbf{\Sigma}$ restricted to be a diagonal matrix.
- Neither QDA nor naive Bayes is a special case of the other. QDA includes multiplicative terms of the form $c_{kjl} x_j x_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important.

How does logistic regression tie into this story? This is identical to the linear form of LDA (4.32). In LDA, the coefficients in this linear function are functions of estimates obtained by assuming that $X$ follow a normal distribution. By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary.
- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that $n$ is very large and $p$ is small.
- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors.
- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients.

---

## Sub-Chapters


[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/index.html)

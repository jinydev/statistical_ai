---
layout: default
title: "index"
---

[< 4.4 Generative Models For Classification](../index.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.4.1 Linear Discriminant Analysis for p = 1

For now, assume that $p = 1$—that is, we have only one predictor. We would like to obtain an estimate for $f_k(x)$ that we can plug into (4.15) in order to estimate $p_k(x)$. We will then classify an observation to the class for which $p_k(x)$ is greatest. To estimate $f_k(x)$, we will first make some assumptions about its form.

In particular, we assume that $f_k(x)$ is _normal_ or _Gaussian_. In the one-dimensional setting, the normal density takes the form

$$
f_k(x) = \frac{1}{\sqrt{2 \pi} \sigma_k} \exp \left( -\frac{1}{2 \sigma_k^2} (x - \mu_k)^2 \right) \quad (4.16)
$$

where $\mu_k$ and $\sigma_k^2$ are the mean and variance parameters for the $k$th class. For now, let us further assume that $\sigma_1^2 = \dots = \sigma_K^2$: that is, there is a shared variance term across all $K$ classes, which for simplicity we can denote by $\sigma^2$. Plugging (4.16) into (4.15), we find that

$$
p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_k)^2 \right)}{\sum_{l=1}^{K} \pi_l \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_l)^2 \right)} \quad (4.17)
$$

The Bayes classifier involves assigning an observation $X = x$ to the class for which (4.17) is largest. Taking the log of (4.17) and rearranging the terms, it is not hard to show that this is equivalent to assigning the observation to the class for which

$$
\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2 \sigma^2} + \log(\pi_k) \quad (4.18)
$$

is largest. For instance, if $K = 2$ and $\pi_1 = \pi_2$, then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$, and to class 2 otherwise. The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$; one can show that this amounts to

$$
x = \frac{\mu_1^2 - \mu_2^2}{2(\mu_1 - \mu_2)} = \frac{\mu_1 + \mu_2}{2} \quad (4.19)
$$

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\sigma^2$. The _linear discriminant analysis_ (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k, \mu_k$, and $\sigma^2$ into (4.18). In particular, the following estimates are used:

$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i: y_i = k} x_i \\
\hat{\sigma}^2 = \frac{1}{n - K} \sum_{k=1}^{K} \sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2 \quad (4.20)
$$

where $n$ is the total number of training observations, and $n_k$ is the number of training observations in the $k$th class. The estimate for $\mu_k$ is simply the average of all the training observations from the $k$th class, while $\hat{\sigma}^2$ can be seen as a weighted average of the sample variances for each of the $K$ classes. In the absence of any additional information, LDA estimates $\pi_k$ using the proportion of the training observations that belong to the $k$th class. In other words,

$$
\hat{\pi}_k = \frac{n_k}{n} \quad (4.21)
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which 

$$
\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2 \hat{\sigma}^2} + \log(\hat{\pi}_k) \quad (4.22)
$$

is largest. The word _linear_ in the classifier’s name stems from the fact that the _discriminant functions_ $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$).

---

## Sub-Chapters


[< 4.4 Generative Models For Classification](../index.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/index.html)

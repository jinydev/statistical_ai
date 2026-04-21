---
layout: default
title: "trans1"
---

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans1.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.4.4 Naive Bayes
# 4.4.4 나이브 베이즈

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers. Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier.
이전 섹션에서 우리는 베이즈 정리 (4.15)를 사용하여 LDA 및 QDA 분류기를 개발했습니다. 여기에서는 베이즈 정리를 사용하여 널리 사용되는 _나이브 베이즈_ 분류기의 동기를 부여합니다.

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability $p_k(x) = \text{Pr}(Y = k \mid X = x)$ in terms of $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. To use (4.15) in practice, we need estimates for $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. As we saw in previous sections, estimating the prior probabilities $\pi_k$ is typically straightforward: we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$th class. 
베이즈 정리 (4.15)가 $\pi_1, \dots, \pi_K$ 및 $f_1(x), \dots, f_K(x)$의 관점에서 사후 확률 $p_k(x) = \text{Pr}(Y = k \mid X = x)$에 대한 표현을 제공함을 상기하십시오. 실전에서 (4.15)를 사용하려면 $\pi_1, \dots, \pi_K$ 및 $f_1(x), \dots, f_K(x)$에 대한 추정치가 필요합니다. 이전 섹션에서 보았듯이 사전 확률 $\pi_k$를 추정하는 것은 일반적으로 간단합니다: $\hat{\pi}_k$를 $k$번째 클래스에 속하는 훈련 관측치의 비율로 추정할 수 있습니다.

However, estimating $f_1(x), \dots, f_K(x)$ is more subtle. Recall that $f_k(x)$ is the $p$-dimensional density function for an observation in the $k$th class. In general, estimating a $p$-dimensional density function is challenging. In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and shared covariance matrix $\mathbf{\Sigma}$. By contrast, in QDA, we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and class-specific covariance matrix $\mathbf{\Sigma}_k$. By making these very strong assumptions, we are able to replace the very challenging problem of estimating $K \times p$-dimensional density functions with the much simpler problem of estimating means and covariance matrices.
그러나 $f_1(x), \dots, f_K(x)$를 추정하는 것은 더 미묘합니다. $f_k(x)$가 $k$번째 클래스 관측치에 대한 $p$-차원 밀도 함수임을 상기하십시오. 일반적으로 $p$-차원 밀도 함수를 추정하는 것은 어렵습니다. LDA에서 우리는 작업을 크게 단순화하는 매우 강력한 가정을 만듭니다: $f_k$가 클래스 고유 평균 $\mu_k$와 공유 공분산 행렬 $\mathbf{\Sigma}$를 갖는 다변량 정규 확률 변수에 대한 밀도 함수라고 가정합니다. 대조적으로, QDA에서는 $f_k$가 클래스 고유 평균 $\mu_k$와 클래스 고유 공분산 행렬 $\mathbf{\Sigma}_k$를 갖는 다변량 정규 확률 변수에 대한 밀도 함수라고 가정합니다. 이러한 매우 강력한 가정을 함으로써, 우리는 $K \times p$-차원 밀도 함수를 추정하는 매우 까다로운 문제를 평균 및 공분산 행렬을 추정하는 훨씬 단순한 문제로 대체할 수 있습니다.

The naive Bayes classifier takes a different tack for estimating $f_1(x), \dots, f_K(x)$. Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single, sweeping assumption:
나이브 베이즈 분류기는 $f_1(x), \dots, f_K(x)$를 추정하기 위해 다른 방향(tack)을 취합니다. 이러한 함수가 특정 분포군(예: 다변량 정규 분포)에 속한다고 가정하는 대신, 단일한, 전면적인 가정을 합니다:

**Within the $k$th class, the $p$ predictors are independent.**
**$k$번째 클래스 내에서 $p$개의 예측 변수는 독립적이다.**

Stated mathematically, this assumption means that for $k = 1, \dots, K$,
수학적으로 말하자면, 이 가정은 $k = 1, \dots, K$에 대해 다음을 의미합니다.

$$
f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p) \quad (4.29)
$$

where $f_{kj}$ is the one-dimensional density function of the $j$th predictor among observations in the $k$th class.
여기서 $f_{kj}$는 $k$번째 클래스의 관측치 중 $j$번째 예측 변수의 1차원 밀도 함수입니다.

Why is this assumption so powerful? Essentially, estimating a $p$-dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors. In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix. However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate. But by assuming that the $p$ covariates are independent within each class, we completely eliminate the need to worry about the association between the $p$ predictors, because we have simply assumed that there is _no_ association between the predictors!
왜 이 가정이 그렇게 강력할까요? 본질적으로 $p$-차원 밀도 함수를 추정하는 것이 까다로운 이유는 각 예측 변수의 _주변 분포(marginal distribution)_ - 즉, 자체적인 각 예측 변수의 분포 - 뿐만 아니라, 예측 변수들의 _결합 분포(joint distribution)_ - 즉, 서로 다른 예측 변수들 간의 연관성 - 도 고려해야 하기 때문입니다. 다변량 정규 분포의 경우, 서로 다른 예측 변수 간의 연관성은 공분산 행렬의 비대각선(off-diagonal) 성분으로 요약됩니다. 그러나 일바적으로 이러한 연관성은 구조화하기가 매우 어려울 수 있고, 추정하기가 대단히 까다로울 수 있습니다. 하지만 $p$개의 공변량이 각 클래스 내에서 독립적이라고 가정함으로써, $p$개의 예측 변수 간의 연관성에 대해 걱정할 필요성을 완전히 제거합니다. 왜냐하면 우리는 단순히 예측 변수들 사이에 어떠한 연관성도 _없다_ 고 가정했기 때문입니다!

Do we really believe the naive Bayes assumption that the $p$ covariates are independent within each class? In most settings, we do not. But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where $n$ is not large enough relative to $p$ for us to effectively estimate the joint distribution of the predictors within each class. In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings. Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.
우리가 실제로 각 클래스 내에서 $p$개의 공변량이 독립적이라는 나이브 베이즈 가정을 믿을까요? 대부분의 설정에서 그렇지 않습니다. 하지만 මෙම 모델링 가정이 편의를 위해 만들어졌다 하더라도, 특히 $n$이 각 클래스 내에서 예측 변수의 결합 분포를 효과적으로 추정하기 비해 $p$에 비대 충분히 크지 않은 설정에서는 꽤 괜찮은 결과로 이어지는 경우가 많습니다. 사실 결합 분포를 추정하는 데 막대한 양의 데이터가 필요하므로, 나이브 베이즈는 광범위한 설정에서 좋은 선택입니다. 본질적으로, 나이브 베이즈 가정은 약간의 편향을 도입하지만 분산을 감소시켜 편향-분산 절충(bias-variance trade-off)의 결과로 실전에서 꽤 잘 작동하는 분류기를 만들어 냅니다.

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability,
나이브 베이즈 가정을 만들고 나면, (4.29)를 (4.15)에 대입하여 사후 확률에 대한 표현을 얻을 수 있습니다.

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k \times f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p)}{\sum_{l=1}^{K} \pi_l \times f_{l1}(x_1) \times f_{l2}(x_2) \times \dots \times f_{lp}(x_p)} \quad (4.30)
$$

for $k = 1, \dots, K$.
($k = 1, \dots, K$ 에 대하여)

To estimate the one-dimensional density function $f_{kj}$ using training data, we have a few options:
훈련 데이터를 사용하여 1차원 밀도 함수 $f_{kj}$를 추정하기 위해, 몇 가지 옵션이 있습니다:

- If $X_j$ is quantitative, we can assume it follows a univariate normal distribution, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- $X_j$가 정량적(quantitative)인 경우, 단변량 정규 분포를 따른다고 가정할 수 있습니다, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- Alternatively, we can use a non-parametric estimate like a histogram or a kernel density estimator.
- 대안적으로, 히스토그램이나 커널 밀도 추정기(kernel density estimator)와 같은 비모수적(non-parametric) 추정을 사용할 수 있습니다.
- If $X_j$ is qualitative, we simply count the proportion of training observations corresponding to each class instance.
- $X_j$가 정성적(qualitative)인 경우, 각 클래스 인스턴스에 해당하는 훈련 관측치의 비율을 단순히 계산합니다.

---

## Sub-Chapters

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans1.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans1.html)

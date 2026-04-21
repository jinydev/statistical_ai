---
layout: default
title: "trans1"
---

[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.5.1 An Analytical Comparison
# 4.5.1 분석적 비교

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression.
우리는 이제 LDA, QDA, 나이브 베이즈, 그리고 로지스틱 회귀에 대한 **분석적(analytical)** (또는 수학적) 비교를 수행합니다.

We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes $\text{Pr}(Y = k \mid X = x)$.
우리는 관측치를 $\text{Pr}(Y = k \mid X = x)$가 최대화되는 클래스에 할당하도록, $K$개의 클래스가 있는 설정에서 이러한 접근법들을 고려합니다.

Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes
동등하게, 우리는 클래스 $K$를 **기준(baseline)** 클래스로 설정하고 관측치를 다음을 최대화하는 클래스에 할당할 수 있습니다.

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) \quad (4.31)
$$

for $k = 1, \dots, K$. Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.
(여기서 $k = 1, \dots, K$.) 각 방법에 대한 (4.31)의 특정 형태를 조사하면, 그것들의 유사성과 차이점에 대한 명확한 이해를 제공합니다.

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that
먼저, LDA의 경우, 베이즈 정리 (4.15)와 함께 각 클래스의 예측 변수들이 클래스별 평균 및 공통 공분산 행렬을 지닌 다변량 정규 밀도 (4.23)에서 도출된다는 가정을 활용하여 다음을 보여줄 수 있습니다.

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j \quad (4.32)
$$

where $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ and $b_{kj}$ is the $j$th component of $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$.
여기서 $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 이며 $b_{kj}$는 $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$의 $j$번째 성분입니다.

Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$.
따라서 LDA는 로지스틱 회귀와 마찬가지로 사후 확률의 로그 오즈가 $x$에 대해 선형적이라고 가정합니다.

Using similar calculations, in the QDA setting (4.31) becomes
유사한 계산을 사용하여, QDA 설정에서 (4.31)은 다음과 같아집니다.

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j + \sum_{j=1}^{p} \sum_{l=1}^{p} c_{kjl} x_j x_l \quad (4.33)
$$

where $a_k, b_{kj}$, and $c_{kjl}$ are functions of $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ and $\mathbf{\Sigma}_K$.
여기서 $a_k, b_{kj}$, 그리고 $c_{kjl}$은 $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ 및 $\mathbf{\Sigma}_K$의 함수들입니다.

Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in $x$.
다시 말해, 이름이 시사하듯이, QDA는 사후 확률의 로그 오즈가 $x$에 대해 2차 형태를 가진다고 가정합니다.

Finally, we examine (4.31) in the naive Bayes setting.
마지막으로, 나이브 베이즈 설정에서 (4.31)을 살펴봅니다.

Recall that in this setting, $f_k(x)$ is modeled as a product of $p$ one-dimensional functions $f_{kj}(x_j)$ for $j = 1, \dots, p$. Hence,
이 설정에서 $f_k(x)$는 $j = 1, \dots, p$에 대한 $p$개의 1차원 함수 $f_{kj}(x_j)$의 곱(product)으로 모델링됨을 상기하십시오. 따라서,

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} g_{kj}(x_j) \quad (4.34)
$$

where $a_k = \log (\pi_k / \pi_K)$ and $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$.
여기서 $a_k = \log (\pi_k / \pi_K)$이고 $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$입니다.

Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_, a topic that is discussed further in Chapter 7.
따라서, (4.34)의 우변은 **일반화 가법 모델(generalized additive model)**의 형태를 취하며, 이는 7장에서 더 논의될 주제입니다.

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:
(4.32), (4.33), 그리고 (4.34)를 살펴보면 LDA, QDA, 그리고 나이브 베이즈에 관한 다음과 같은 관찰 결과를 얻을 수 있습니다.

- LDA is a special case of QDA with $c_{kjl} = 0$.
- LDA는 $c_{kjl} = 0$인 QDA의 특수 사례입니다.
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj} x_j$. In particular, this means that LDA is a special case of naive Bayes!
- 선형 결정 경계를 가진 분류기는 $g_{kj}(x_j) = b_{kj} x_j$인 나이브 베이즈의 특수 사례입니다. 특히, 이는 LDA가 나이브 베이즈의 특수 사례임을 의미합니다!
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj}, \sigma_j^2)$, naive Bayes is actually a special case of LDA with $\mathbf{\Sigma}$ restricted to be a diagonal matrix.
- 나이브 베이즈 분류기에서 1차원 가우시안 분포 $N(\mu_{kj}, \sigma_j^2)$를 사용하여 $f_{kj}(x_j)$를 모델링한다면, 나이브 베이즈는 대각 행렬로 제한된 $\mathbf{\Sigma}$를 갖는 LDA의 특수 사례가 됩니다.
- Neither QDA nor naive Bayes is a special case of the other. QDA includes multiplicative terms of the form $c_{kjl} x_j x_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important.
- QDA와 나이브 베이즈는 둘 다 서로의 특수 사례가 아닙니다. QDA는 $c_{kjl} x_j x_l$ 형태의 곱항을 포함합니다. 따라서 QDA는 예측 변수 간의 상호 작용이 중요한 설정에서 더 정확할 가능성이 있습니다.

How does logistic regression tie into this story? This is identical to the linear form of LDA (4.32).
로지스틱 회귀는 이 이야기에 어떻게 연결될까요? 이는 LDA의 선형 형태 (4.32)와 동일합니다.

In LDA, the coefficients in this linear function are functions of estimates obtained by assuming that $X$ follow a normal distribution.
LDA에서는 이 선형 함수의 계수들이 $X$가 정규 분포를 따른다고 가정하여 얻은 추정치의 함수입니다.

By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5).
반대로, 로지스틱 회귀에서는 우도 함수 (4.5)를 최대화하도록 계수들이 선택됩니다.

Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.
따라서 정규성 가정이 대략적으로 성립할 때는 LDA가 로지스틱 회귀를 능가할 것으로 예상하며, 성립하지 않을 때는 로지스틱 회귀가 더 잘 작동할 것으로 예상합니다.

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2.
2장에서 소개된 **K-최근접 이웃(KNN)**에 대한 간단한 논의로 마무리합니다.

Recall that KNN takes a completely different approach from the classifiers seen in this chapter. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary.
KNN은 이 장에서 본 분류기들과는 완전히 다른 접근법을 취한다는 것을 상기하십시오. 따라서 KNN은 완전히 비모수적인 접근법입니다: 결정 경계의 형태에 관해 어떠한 가정도 하지 않습니다.

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that $n$ is very large and $p$ is small.
- KNN은 완전히 비모수적이므로, $n$이 매우 크고 $p$가 작다는 조건 하에, 결정 경계가 매우 비선형적일 때 LDA 및 로지스틱 회귀보다 우수할 것으로 예상할 수 있습니다.
- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors.
- 정확한 분류를 제공하기 위해, KNN은 예측 변수 수에 비해 **많은** 관측치를 필요로 합니다.
- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients.
- 로지스틱 회귀와 달리, KNN은 어떤 예측 변수가 중요한지 알려주지 않습니다: 계수 테이블을 얻을 수 없습니다.

---

## Sub-Chapters

[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans1.html)

---
layout: default
title: "trans1"
---

[< 4.5 A Comparison Of Classification Methods](../trans1.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.5.1 An Analytical Comparison
# 4.5.1 분석적 비교

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression. We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes $\text{Pr}(Y = k \mid X = x)$. Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes
이제 우리는 LDA, QDA, 나이브 베이즈 및 로지스틱 회귀에 대한 _분석적_(또는 수학적) 비교를 수행합니다. 우리는 $K$개의 클래스가 있는 설정에서 이러한 접근법들을 고려하며, $\text{Pr}(Y = k \mid X = x)$를 최대화하는 클래스에 관측치를 할당합니다. 동등하게, 우리는 $K$를 _기준(baseline)_ 클래스로 설정하고 다음을 최대화하는 클래스에 관측치를 할당할 수 있습니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) \quad (4.31)
$$

for $k = 1, \dots, K$. Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.
$k = 1, \dots, K$ 에 대하여. 각 방법에 대한 (4.31)의 특정 형태를 조사하면 이들의 유사성과 차이점을 명확하게 이해할 수 있습니다.

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that
첫째, LDA의 경우 베이즈 정리 (4.15)와 각 클래스 내의 예측 변수가 클래스 고유 평균 및 공유 공분산 행렬을 갖는 다변량 정규 밀도 (4.23)로부터 도출된다는 가정을 활용하여 다음을 보여줄 수 있습니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j \quad (4.32)
$$

where $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ and $b_{kj}$ is the $j$th component of $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$. Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$. Using similar calculations, in the QDA setting (4.31) becomes
여기서 $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 이고 $b_{kj}$는 $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$의 $j$번째 성분입니다. 따라서 LDA는 로지스틱 회귀와 마찬가지로 사후 확률의 로그 오즈가 $x$에 대해 선형이라고 가정합니다. 유사한 계산을 사용하면, QDA 설정에서 (4.31)은 다음과 같이 됩니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j + \sum_{j=1}^{p} \sum_{l=1}^{p} c_{kjl} x_j x_l \quad (4.33)
$$

where $a_k, b_{kj}$, and $c_{kjl}$ are functions of $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ and $\mathbf{\Sigma}_K$. Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in $x$.
여기서 $a_k, b_{kj}$, 그리고 $c_{kjl}$는 $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ 및 $\mathbf{\Sigma}_K$의 함수입니다. 다시 말해, 이름에서 알 수 있듯이 QDA는 사후 확률의 로그 오즈가 $x$에 대해 이차(quadratic)라고 가정합니다.

Finally, we examine (4.31) in the naive Bayes setting. Recall that in this setting, $f_k(x)$ is modeled as a product of $p$ one-dimensional functions $f_{kj}(x_j)$ for $j = 1, \dots, p$. Hence,
마지막으로, 나이브 베이즈 설정에서 (4.31)을 조사합니다. 이 설정에서 $f_k(x)$는 $j = 1, \dots, p$에 대해 $p$개의 1차원 함수 $f_{kj}(x_j)$의 곱으로 모델링됨을 기억하십시오. 따라서,

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} g_{kj}(x_j) \quad (4.34)
$$

where $a_k = \log (\pi_k / \pi_K)$ and $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$. Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_, a topic that is discussed further in Chapter 7.
여기서 $a_k = \log (\pi_k / \pi_K)$ 이고 $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$ 입니다. 그러므로, (4.34)의 우변은 제 7장에서 더 자세히 논의될 주제인 _일반화 가법 모델(generalized additive model)_ 의 형태를 취합니다.

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:
(4.32), (4.33) 및 (4.34)를 검사하면 LDA, QDA 및 나이브 베이즈에 대해 다음과 같은 관찰 결과를 얻을 수 있습니다:

- LDA is a special case of QDA with $c_{kjl} = 0$.
- LDA는 $c_{kjl} = 0$ 인 QDA의 특수한 경우입니다.
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj} x_j$. In particular, this means that LDA is a special case of naive Bayes!
- 선형 결정 경계를 가진 모든 분류기는 $g_{kj}(x_j) = b_{kj} x_j$ 인 나이브 베이즈의 특수한 경우입니다. 특히, 이는 LDA가 나이브 베이즈의 특수한 경우임을 의미합니다!
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj}, \sigma_j^2)$, naive Bayes is actually a special case of LDA with $\mathbf{\Sigma}$ restricted to be a diagonal matrix.
- 나이브 베이즈 분류기에서 1차원 가우시안 분포 $N(\mu_{kj}, \sigma_j^2)$를 사용하여 $f_{kj}(x_j)$를 모델링한다면, 나이브 베이즈는 실제로 $\mathbf{\Sigma}$ 가 대각 행렬(diagonal matrix)로 국한된 LDA의 특수한 경우가 됩니다.
- Neither QDA nor naive Bayes is a special case of the other. QDA includes multiplicative terms of the form $c_{kjl} x_j x_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important.
- QDA와 나이브 베이즈는 어느 한 쪽도 다른 쪽의 특수한 경우가 아닙니다. QDA는 $c_{kjl} x_j x_l$ 형태의 곱셈 항을 포함합니다. 그러므로 예측 변수 간의 상호작용이 중요한 설정에서 QDA가 잠재적으로 더 정확할 가능성이 있습니다.

How does logistic regression tie into this story? This is identical to the linear form of LDA (4.32). In LDA, the coefficients in this linear function are functions of estimates obtained by assuming that $X$ follow a normal distribution. By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.
로지스틱 회귀는 이 이야기와 어떻게 연결될까요? 이는 LDA의 선형 형태 (4.32)와 동일합니다. LDA에서 이 선형 함수의 계수는 $X$가 정규 분포를 따른다고 가정하여 얻은 추정치의 함수입니다. 대조적으로, 로지스틱 회귀에서 계수는 우도 함수(likelihood function) (4.5)를 최대화하도록 선택됩니다. 따라서 정규성 가정이 (대략적으로) 성립할 때 LDA가 로지스틱 회귀보다 더 나은 성능을 발휘할 것으로 예상하며, 성립하지 않을 때는 로지스틱 회귀가 더 잘 수행될 것으로 예상합니다.

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary.
제 2장에서 소개된 _K-최근접 이웃_ (KNN)에 대한 간단한 논의로 마무리하겠습니다. KNN은 이 장에서 본 분류기들과 완전히 다른 접근 방식을 취한다는 점을 상기하십시오. 즉, KNN은 결정 경계의 형태에 대해 어떠한 가정도 하지 않는 완전히 비모수적인 접근 방식입니다.

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that $n$ is very large and $p$ is small.
- KNN은 완전히 비모수적이므로, $n$이 매우 크고 $p$가 작다는 전제하에 결정 경계가 매우 비선형적일 때 이 접근법이 LDA 및 로지스틱 회귀를 압도할 것으로 예상할 수 있습니다.
- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors.
- 정확한 분류를 제공하기 위해, KNN은 예측 변수의 수에 비해 _매우 많은(a lot)_ 관측치를 필요로 합니다.
- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients.
- 로지스틱 회귀와 달리, KNN은 우리에게 어떤 예측 변수가 중요한지 알려주지 않습니다: 우리는 계수 표를 얻지 못합니다.

---

## Sub-Chapters

[< 4.5 A Comparison Of Classification Methods](../trans1.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans1.html)

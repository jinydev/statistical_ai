---
layout: default
title: "trans1"
---

[< 4.4.2.1 Roc Curve](../4_4_2_linear_discriminant_analysis_for_p_1/4_4_2_1_roc_curve/trans1.html) | [4.4.4 Naive Bayes >](../4_4_4_naive_bayes/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.4.3 Quadratic Discriminant Analysis
# 4.4.3 이차 판별 분석

As we have discussed, LDA assumes that the observations within each class are drawn from a multivariate Gaussian distribution with a class-specific mean vector and a covariance matrix that is common to all $K$ classes. _Quadratic discriminant analysis_ (QDA) provides an alternative approach. Like LDA, the QDA classifier results from assuming that the observations from each class are drawn from a Gaussian distribution, and plugging estimates for the parameters into Bayes’ theorem in order to perform prediction. However, unlike LDA, QDA assumes that each class has its own covariance matrix. That is, it assumes that an observation from the $k$th class is of the form $X \sim N(\mu_k, \mathbf{\Sigma}_k)$, where $\mathbf{\Sigma}_k$ is a covariance matrix for the $k$th class. Under this assumption, the Bayes classifier assigns an observation $X = x$ to the class for which
우리가 논의했듯이, LDA는 각 클래스 내의 관측치가 클래스-특정 평균 벡터와 모든 $K$ 클래스에 공통인 공분산 행렬을 갖는 다변량 가우시안 분포로부터 도출된다고 가정합니다. _이차 판별 분석_ (QDA)은 대안적인 접근 방식을 제공합니다. LDA와 마찬가지로, QDA 분류기는 각 클래스의 관측치가 가우시안 분포로부터 도출된다고 가정하고, 예측을 수행하기 위해 매개변수에 대한 추정치를 베이즈 정리에 대입한 결과입니다. 그러나 LDA와 달리 QDA는 각 클래스가 고유한 공분산 행렬을 갖는다고 가정합니다. 즉, $k$번째 클래스의 관측치가 $X \sim N(\mu_k, \mathbf{\Sigma}_k)$의 형태를 갖는다고 가정하며, 여기서 $\mathbf{\Sigma}_k$는 $k$번째 클래스에 대한 공분산 행렬입니다. 이러한 가정 하에서, 베이즈 분류기는 관측치 $X = x$를 다음 값이 최대가 되는 클래스에 할당합니다.

$$
\delta_k(x) = -\frac{1}{2} (x - \mu_k)^T \mathbf{\Sigma}_k^{-1} (x - \mu_k) - \frac{1}{2} \log |\mathbf{\Sigma}_k| + \log \pi_k \quad (4.28)
$$

is largest. So the QDA classifier involves plugging estimates for $\mathbf{\Sigma}_k$, $\mu_k$, and $\pi_k$ into (4.28), and then assigning an observation $X = x$ to the class for which this quantity is largest. Unlike in (4.24), the quantity $x$ appears as a _quadratic_ function in (4.28). This is where QDA gets its name.
결과적으로 QDA 분류기는 $\mathbf{\Sigma}_k$, $\mu_k$, 및 $\pi_k$에 대한 추정치를 (4.28)에 대입한 다음, 이 양이 최대인 클래스에 관측치 $X = x$를 할당하는 것을 포함합니다. (4.24)와 달리 양 $x$는 (4.28)에서 _이차_ 함수로 나타납니다. 이것이 QDA가 그 이름을 얻은 이유입니다.

Why does it matter whether or not we assume that the $K$ classes share a common covariance matrix? In other words, why would one prefer LDA to QDA, or vice-versa? The answer lies in the bias-variance trade-off. When there are $p$ predictors, then estimating a covariance matrix requires estimating $p(p+1)/2$ parameters. QDA estimates a separate covariance matrix for each class, for a total of $K p(p+1)/2$ parameters. With 50 predictors this is some multiple of 1,275, which is a lot of parameters. By instead assuming that the $K$ classes share a common covariance matrix, the LDA model becomes linear in $x$, which means there are $K p$ linear coefficients to estimate. Consequently, LDA is a much less flexible classifier than QDA, and so has substantially lower variance. This can potentially lead to improved prediction performance. But there is a trade-off: if LDA’s assumption that the $K$ classes share a common covariance matrix is badly off, then LDA can suffer from high bias. Roughly speaking, LDA tends to be a better bet than QDA if there are relatively few training observations and so reducing variance is crucial. In contrast, QDA is recommended if the training set is very large, so that the variance of the classifier is not a major concern, or if the assumption of a common covariance matrix for the $K$ classes is clearly untenable.
$K$ 클래스가 공통의 공분산 행렬을 공유한다고 가정하는지 여부가 왜 중요할까요? 즉, 왜 누군가는 QDA보다 LDA를 선호하거나, 또는 그 반대로 선호할까요? 그 답은 편향-분산 절충(trade-off)에 있습니다. $p$개의 예측 변수가 있을 때, 공분산 행렬을 추정하려면 $p(p+1)/2$개의 매개변수를 추정해야 합니다. QDA는 각 클래스에 대해 별도의 공분산 행렬을 추정하므로, 총 $K p(p+1)/2$개의 매개변수가 필요합니다. 50개의 예측 변수가 있는 경우 이는 1,275의 배수에 해당하며, 매우 많은 매개변수입니다. 대신 $K$ 클래스가 공통 공분산 행렬을 공유한다고 가정함으로써, LDA 모델은 $x$에 대해 선형이 되며, 이는 추정해야 할 선형 계수가 $K p$개임을 의미합니다. 결과적으로 LDA는 QDA보다 훨씬 덜 유연한 분류기이며, 따라서 실질적으로 더 낮은 분산을 가집니다. 이는 잠재적으로 개선된 예측 성능으로 이어질 수 있습니다. 그러나 절충(trade-off)이 있습니다: 만약 $K$ 클래스가 공통 공분산 행렬을 공유한다는 LDA의 가정이 심하게 틀린다면, LDA는 높은 편향으로 고통받을 수 있습니다. 대략적으로 말하자면, 훈련 관측치가 상대적으로 적어서 분산을 줄이는 것이 매우 중요한 경우 QDA보다는 LDA가 더 나은 선택이 되는 경향이 있습니다. 대조적으로, 훈련 세트가 매우 커서 분류기의 분산이 주요 관심사가 아니거나, $K$ 클래스에 대해 공통 공분산 행렬의 가정이 명백히 지지될 수 없는 경우에는 QDA가 권장됩니다.

---

## Sub-Chapters

[< 4.4.2.1 Roc Curve](../4_4_2_linear_discriminant_analysis_for_p_1/4_4_2_1_roc_curve/trans1.html) | [4.4.4 Naive Bayes >](../4_4_4_naive_bayes/trans1.html)

---
layout: default
title: "trans1"
---

[< 4.4 Generative Models For Classification](../trans1.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4.1 Linear Discriminant Analysis for p = 1
# 4.4.1. p = 1인 단일 예측 변수에 대한 선형 판별 분석

For now, assume that $p = 1$—that is, we have only one predictor.
당분간, $p = 1$이라고 가정해 보겠습니다. 즉, 우리는 오직 단 하나의 예측 변수만을 가지고 있습니다.

We would like to obtain an estimate for $f_k(x)$ that we can plug into (4.15) in order to estimate $p_k(x)$.
우리는 $p_k(x)$를 추정하기 위해 식 (4.15)에 대입할 수 있는 $f_k(x)$ 에 대한 추정치를 얻고 싶습니다.

We will then classify an observation to the class for which $p_k(x)$ is greatest.
그러고 나서 우리는 $p_k(x)$가 가장 큰 클래스로 관측치를 분류할 것입니다.

To estimate $f_k(x)$, we will first make some assumptions about its form.
$f_k(x)$를 추정하기 위해, 우리는 먼저 그 형태에 대한 몇 가지 가정을 세울 것입니다.

In particular, we assume that $f_k(x)$ is _normal_ or _Gaussian_.
구체적으로, 우리는 $f_k(x)$가 **정규(normal)** 또는 **가우시안(Gaussian)** 분포라고 가정합니다.

In the one-dimensional setting, the normal density takes the form
1차원 설정에서, 정규 밀도 함수는 다음과 같은 형태를 취합니다:

$$
f_k(x) = \frac{1}{\sqrt{2 \pi} \sigma_k} \exp \left( -\frac{1}{2 \sigma_k^2} (x - \mu_k)^2 \right) \quad (4.16)
$$

where $\mu_k$ and $\sigma_k^2$ are the mean and variance parameters for the $k$th class.
여기서 $\mu_k$와 $\sigma_k^2$는 $k$번째 클래스에 대한 평균과 분산 파라미터입니다.

For now, let us further assume that $\sigma_1^2 = \dots = \sigma_K^2$: that is, there is a shared variance term across all $K$ classes, which for simplicity we can denote by $\sigma^2$.
당장은 $\sigma_1^2 = \dots = \sigma_K^2$라고 추가적으로 가정해 봅시다. 즉, 모든 $K$개의 클래스에 걸쳐 공유되는 분산 항이 존재하며, 편의상 이를 $\sigma^2$로 나타낼 수 있습니다.

Plugging (4.16) into (4.15), we find that
수식 (4.16)을 (4.15)에 대입하면, 다음과 같은 결과를 얻습니다:

$$
p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_k)^2 \right)}{\sum_{l=1}^{K} \pi_l \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_l)^2 \right)} \quad (4.17)
$$

The Bayes classifier involves assigning an observation $X = x$ to the class for which (4.17) is largest.
베이즈 분류기는 식 (4.17)이 가장 커지는 클래스에 관측치 $X = x$를 할당하는 과정을 포함합니다.

Taking the log of (4.17) and rearranging the terms, it is not hard to show that this is equivalent to assigning the observation to the class for which
(4.17)의 로그를 취하고 항을 재배열하면, 이것이 다음 수식이 가장 큰 클래스에 관측치를 할당하는 것과 동치임을 보여주는 것은 어렵지 않습니다:

$$
\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2 \sigma^2} + \log(\pi_k) \quad (4.18)
$$

is largest.
(마지막 문장과 결합)

For instance, if $K = 2$ and $\pi_1 = \pi_2$, then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$, and to class 2 otherwise.
예를 들어, 만약 $K = 2$이고 $\pi_1 = \pi_2$라면, 베이즈 분류기는 $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$일 경우 관측치를 1번 클래스로 할당하고, 그렇지 않을 경우에는 2번 클래스로 할당합니다.

The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$; one can show that this amounts to
베이즈 결정 경계(Bayes decision boundary)는 $\delta_1(x) = \delta_2(x)$가 되는 지점이며; 다음 수식에 해당함을 보여줄 수 있습니다:

$$
x = \frac{\mu_1^2 - \mu_2^2}{2(\mu_1 - \mu_2)} = \frac{\mu_1 + \mu_2}{2} \quad (4.19)
$$

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\sigma^2$.
실제로는, 만약 우리가 각 클래스 내에서 $X$가 가우시안 분포로부터 추출되었다는 가정에 대해 상당히 확신한다고 하더라도, 베이즈 분류기를 적용하기 위해 우리는 여전히 $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, 그리고 $\sigma^2$ 파라 파라미터들을 추정해야만 합니다.

The _linear discriminant analysis_ (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k, \mu_k$, and $\sigma^2$ into (4.18).
**선형 판별 분석(linear discriminant analysis, LDA)** 방법은 $\pi_k, \mu_k$, 그리고 $\sigma^2$에 대한 추정치를 식 (4.18)에 대입하여 베이즈 분류기를 근사합니다.

In particular, the following estimates are used:
특히, 다음과 같은 추정치들이 사용됩니다:

$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i: y_i = k} x_i \\
\hat{\sigma}^2 = \frac{1}{n - K} \sum_{k=1}^{K} \sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2 \quad (4.20)
$$

where $n$ is the total number of training observations, and $n_k$ is the number of training observations in the $k$th class.
여기서 $n$은 전체 훈련 관측치의 개수이고, $n_k$는 $k$번째 클래스에 있는 훈련 관측치의 수입니다.

The estimate for $\mu_k$ is simply the average of all the training observations from the $k$th class, while $\hat{\sigma}^2$ can be seen as a weighted average of the sample variances for each of the $K$ classes.
$\mu_k$에 대한 추정치는 단순히 $k$번째 클래스에 속한 모든 훈련 관측치들의 평균치일 뿐이며 반면 $\hat{\sigma}^2$는 $K$개의 각 클래스에 대한 표본 분산들의 가중 평균으로 볼 수 있습니다.

In the absence of any additional information, LDA estimates $\pi_k$ using the proportion of the training observations that belong to the $k$th class.
아무런 추가적인 정보가 부재할 경우, LDA는 $k$번째 클래스에 속하는 훈련 관측치의 비율을 사용하여 $\pi_k$를 추정하게 됩니다.

In other words,
다른 말로,

$$
\hat{\pi}_k = \frac{n_k}{n} \quad (4.21)
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which 
LDA 분류기는 식 (4.20)과 (4.21)에 주어진 추정치들을 식 (4.18)에 대입하고, 다음 수식이 가장 큰 클래스에 관측치 $X = x$를 할당합니다:

$$
\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2 \hat{\sigma}^2} + \log(\hat{\pi}_k) \quad (4.22)
$$

is largest.
(마지막 문장과 결합)

The word _linear_ in the classifier’s name stems from the fact that the _discriminant functions_ $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$).
해당 분류기 이름 중 분별에 사용된 **선형(linear)** 이라는 단어는, 식 (4.22)에 있는 **판별 함수(discriminant functions)** 인 $\hat{\delta}_k(x)$가 ($x$의 더 복잡한 곡선 함수가 아니라) $x$에 대한 1차 선형 함수라는 사실에서 유래합니다.

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters

[< 4.4 Generative Models For Classification](../trans1.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans1.html)

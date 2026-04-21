---
layout: default
title: "trans1"
---

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans1.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4 Generative Models for Classification
# 4.4. 분류를 위한 생성 모델 (Generative Models for Classification)

Logistic regression involves directly modeling $\text{Pr}(Y = k \mid X = x)$ using the logistic function, given by (4.7) for the case of two response classes.
로지스틱 회귀는 두 개의 반응 클래스인 경우, 수식 (4.7)로 주어지는 로지스틱 함수를 사용하여 $\text{Pr}(Y = k \mid X = x)$를 직접적으로 모델링하는 것을 포함합니다.

In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$.
통계학적 전문 용어로 말해, 우리는 예측 변수 $X$가 주어졌을 때 반응 변수 $Y$의 조건부 분포를 모델링합니다.

We now consider an alternative and less direct approach to estimating these probabilities.
우리는 이제 이러한 확률들을 추정하기 위한, 보다 간접적이고 대안적인 접근 방식을 고려합니다.

In this new approach, we model the distribution of the predictors $X$ separately in each of the response classes (i.e. for each value of $Y$).
이 새로운 접근법에서, 우리는 각 반응 클래스 내에서 분리하여(즉, $Y$의 각 값에 대해) 예측 변수 $X$의 분포를 별도로 모델링합니다.

We then use Bayes’ theorem to flip these around into estimates for $\text{Pr}(Y = k \mid X = x)$.
그런 다음 우리는 베이즈 정리(Bayes' theorem)를 사용하여 이를 뒤집어 $\text{Pr}(Y = k \mid X = x)$에 대한 확률 추정치로 변환합니다.

When the distribution of $X$ within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.
각 클래스 내에서 $X$의 분포가 정규 분포라고 가정될 때, 이 모델은 결과적으로 로지스틱 회귀와 형태가 매우 유사함이 밝혀집니다.

Why do we need another method, when we have logistic regression? There are several reasons:
로지스틱 회귀가 이미 있는 마당에 왜 우리는 다른 대안 방법이 필요할까요? 여기에는 여러 가지 이유가 있습니다:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.
- 두 클래스 사이에 상당한 수준의 분리(separation) 구역이 존재할 때, 로지스틱 회귀 모델의 파라미터 추정치들은 놀라울 정도로 불안정해집니다. 우리가 이번 절에서 고려할 방법들은 이러한 문제로부터 자유롭습니다.

- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.
- 만약 예측 변수 $X$의 분포가 각각의 클래스 내에서 대략적으로 정규 분포를 따르며 데이터 샘플 크기가 작다면, 이 절의 접근법들이 로지스틱 회귀보다 더 정확할 수 있습니다.

- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)
- 이 절의 방법들은 자연스럽게 반응 클래스가 세 개 이상인 다중 클래스 경우로 연장 확장될 수 있습니다. (반응 클래스가 세 개 이상인 다항 범주일 경우, 우리는 섹션 4.3.5에서 다룬 다항 로지스틱 회귀 역시 사용할 수도 있습니다.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \ge 2$.
우리가 관측치를 $K \ge 2$인 상황의 $K$개 클래스 중 하나로 분류하고자 한다고 가정해 보겠습니다.

In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values.
다시 말해, 정성적 반응 변수 $Y$는 순서가 없는 구별되는 $K$개의 가질수 있는 값을 취할 수 있습니다.

Let $\pi_k$ represent the overall or _prior_ probability that a randomly chosen observation comes from the $k$th class.
$\pi_k$가 전체적인 확률 또는 무작위로 추출된 관측치가 $k$번째 클래스에서 나왔을 **사전(prior)** 확률을 나타낸다고 합시다.

Let $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ denote the _density function_ of $X$ for an observation that comes from the $k$th class.
$f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$가 $k$번째 클래스에서 나온 관측치에 대한 $X$의 **밀도 함수(density function)** 를 표기한다고 합시다.

In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$th class has $X \approx x$, and $f_k(x)$ is small if it is very unlikely that an observation in the $k$th class has $X \approx x$.
다른 말로 표현하자면, $k$번째 클래스에 있는 관측치가 $X \approx x$를 가질 확률이 높다면 $f_k(x)$는 상대적으로 큰 값을 가지며, $k$번째 클래스의 관측치가 $X \approx x$를 가질 가능성이 아주 적다면 $f_k(x)$는 작은 값을 나타냅니다.

Then _Bayes’ theorem_ states that
그러면 **베이즈 정리(Bayes’ theorem)** 에 따라 다음의 성질이 성립합니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)} \quad (4.15)
$$

In accordance with our earlier notation, we will use the abbreviation $p_k(x) = \text{Pr}(Y = k \mid X = x)$; this is the _posterior_ probability that an observation $X = x$ belongs to the $k$th class.
초기 표기법에 따라서, 우리는 약어 $p_k(x) = \text{Pr}(Y = k \mid X = x)$를 사용할 것이며; 이는 한 관측치 $X = x$가 $k$번째 범주에 속할 **사후(posterior)** 확률을 의미합니다.

That is, it is the probability that the observation belongs to the $k$th class, _given_ the predictor value for that observation.
즉, 그 특정 관측치에 대해 주어지는 예측 변수 단서들이 **주어졌을 때**, 그 관측치가 $k$번째 번호가 적힌 방 클래스에 속할 확률을 뜻합니다.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers.
우리는 이미 2장에서 관측치 변수 $x$를 $p_k(x)$ 확률값이 제일 최대로 나오는 클래스 쪽으로 분류해 버리는 베이즈 분류기(Bayes classifier)가 다른 현존하는 모든 분류기들 중 가장 낮은 오류율을 보장한다는 것을 알고 있습니다.

In the following sections, we discuss three classifiers that use different estimates of $f_k(x)$ in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_.
다음으로 이어질 섹션들에서 우리는 위 식 (4.15) 안의 $f_k(x)$를 구하기 위하여 추정치의 결을 다르게 사용하여 이 이상적인 베이즈 분류기를 근사적으로 흉내 내는 세 가지 분류기 체계를 논의합니다: 즉 **선형 판별 분석(linear discriminant analysis)**, **이차 판별 분석(quadratic discriminant analysis)**, 그리고 **나이브 베이즈(naive Bayes)** 입니다.

---

### 4.4.1 Linear Discriminant Analysis for p = 1

### 4.4.2 Linear Discriminant Analysis for p > 1

### 4.4.3 Quadratic Discriminant Analysis

### 4.4.4 Naive Bayes

---

## Sub-Chapters (하위 목차)

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans1.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans1.html)

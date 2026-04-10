---
layout: default
title: "index"
---

# 4.4 Generative Models for Classification 

Logistic regression involves directly modeling Pr( $Y=$ _k|X_ = _x_ ) using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$. We now consider an alternative and less direct approach to estimating these probabilities. In this new approach, we model the distribution of the predictors $X$separately in each of the response classes (i.e. for each value of $Y$). We then use Bayes’ theorem to flip these around into estimates for Pr( $Y=$ _k|X_ = _x_ ). When the distribution of $X$within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression. 

Why do we need another method, when we have logistic regression? There are several reasons: 

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem. 

- If the distribution of the predictors $X$is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression. 

- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.) 

Suppose that we wish to classify an observation into one of $K$ classes, where _K ≥_ 2. In other words, the qualitative response variable $Y$can take on $K$ possible distinct and unordered values. Let _πk_ represent the overall or _prior_ probability that a randomly chosen observation comes from the prior $k$ th class. Let _fk_ ( $X$) _≡_ Pr( _X|Y_ = $k$ )[1] denote the _density function_ of $X$for an observation that comes from the $k$ th class. In other words, _fk_ ( _x_ ) is relatively large if there is a high probability that an observation in the $k$ th class has _X ≈ x_ , and _fk_ ( _x_ ) is small if it is very unlikely that an observation in the $k$ th class has _X ≈ x_ . Then _Bayes’ theorem_ states that 

density function 

Bayes’ theorem 

> 1Technically, this definition is only correct if $X$is a qualitative random variable. If $X$is quantitative, then _fk_ ( _x_ ) _dx_ corresponds to the probability of $X$falling in a small region _dx_ around _x_ . 

4.4 Generative Models for Classification 147 



In accordance with our earlier notation, we will use the abbreviation _pk_ ( _x_ ) = Pr( $Y=$ _k|X_ = _x_ ); this is the _posterior_ probability that an observation posterior $X$= _x_ belongs to the $k$ th class. That is, it is the probability that the observation belongs to the $k$ th class, _given_ the predictor value for that observation. 

Equation 4.15 suggests that instead of directly computing the posterior probability _pk_ ( _x_ ) as in Section 4.3.1, we can simply plug in estimates of _πk_ and _fk_ ( _x_ ) into (4.15). In general, estimating _πk_ is easy if we have a random sample from the population: we simply compute the fraction of the training observations that belong to the $k$ th class. However, estimating the density function _fk_ ( _x_ ) is much more challenging. As we will see, to estimate _fk_ ( _x_ ), we will typically have to make some simplifying assumptions. 

We know from Chapter 2 that the Bayes classifier, which classifies an observation _x_ to the class for which _pk_ ( _x_ ) is largest, has the lowest possible error rate out of all classifiers. (Of course, this is only true if all of the terms in (4.15) are correctly specified.) Therefore, if we can find a way to estimate _fk_ ( _x_ ), then we can plug it into (4.15) in order to approximate the Bayes classifier. 

In the following sections, we discuss three classifiers that use different estimates of _fk_ ( _x_ ) in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_ . 

---

## Sub-Chapters (하위 목차)

### 4.4.1 Linear Discriminant Analysis for p = 1 (p=1인 경우의 선형 판별 분석)
* [문서로 이동하기](./4_4_1_linear_discriminant_analysis_for_p_1/)

예측 변수가 단 1개일 때 정규 분포 기반으로 각 클래스의 평균과 통일된 분산을 추정하여 집단을 판별(LDA)하는 과정입니다.

### 4.4.2 Linear Discriminant Analysis for p > 1 (p>1인 경우의 선형 판별 분석)
* [문서로 이동하기](./4_4_2_linear_discriminant_analysis_for_p_1/)

여러 개의 차원 특성이 존재할 때 다변량 정규 분포를 가정하여, 클래스 간 선형 경계를 세우는 보편적 LDA 확장 파트입니다.

### 4.4.3 Quadratic Discriminant Analysis (이차 판별 분석)
* [문서로 이동하기](./4_4_3_quadratic_discriminant_analysis/)

각 클래스가 공통된 행렬이 아닌 고유한 개별 분산/공분산 행렬을 가진다고 가정함으로써, 경계를 다소 유연한 2차 곡선(QDA)으로 유도합니다.

### 4.4.4 Naive Bayes (나이브 베이즈)
* [문서로 이동하기](./4_4_4_naive_bayes/)

모든 차원의 변수들이 클래스 내에서 서로 완벽히 독립적이라는 강력한 가정하에 곱 확률로 쉽고 빠르게 연산하는 고전 분류기입니다.

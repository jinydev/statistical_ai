---
layout: default
title: "trans1"
---

[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/trans1.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.1.2 How Do We Estimate _f_?

# 2.1.2 우리는 어떻게 _f_ 를 측정하는가?

Throughout this book, we explore many linear and non-linear approaches for estimating _f_.

이 책 전반에 걸쳐서, 우리는 _f_ 를 측정하기 위한 많은 선형 및 비선형 접근법들을 탐구합니다.

However, these methods generally share certain characteristics. We provide an overview of these shared characteristics in this section.

그러나 이러한 방식들은 일반적으로 특정한 특징들을 공유합니다. 우리는 이 섹션에서 이러한 공유된 특징들의 개요를 제공합니다.

We will always assume that we have observed a set of _n_ different data points.

우리는 항상 _n_ 개의 다른 데이터 포인트 세트를 관측했다고 가정할 것입니다.

For example in Figure 2.2 we observed _n_ = 30 data points.

예를 들어 그림 2.2에서 우리는 _n_ = 30 개의 데이터 포인트를 관측했습니다.

These observations are called the _training data_ because we will use these training observations to train, or teach, our method how to estimate _f_.

우리는 이 관측된 데이터들을 사용하여 우리의 방법에게 _f_ 를 측정하는 방법을 훈련시키거나 가르칠 것이기 때문에 이러한 관찰 대상들은 _훈련 데이터(training data)_ 라고 부릅니다.

Let $x_{ij}$ represent the value of the _j_ th predictor, or input, for observation _i_, where $i = 1, 2, \dots, n$ and $j = 1, 2, \dots, p$. Correspondingly, let $y_i$ represent the response variable for the _i_ th observation.

$x_{ij}$ 를 관측치 _i_ 에 대한 _j_ 번째 예측 변수나 입력의 값이라고 합시다. 여기서 $i = 1, 2, \dots, n$ 이고 $j = 1, 2, \dots, p$ 입니다. 대응하여, $y_i$ 를 _i_ 번째 관측치에 대한 반응 변수라고 합시다.

Then our training data consist of $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ where $x_i = (x_{i1}, x_{i2}, \dots, x_{ip})^T$.

그러면 우리의 훈련 데이터는 $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ 로 구성되며, 여기서 $x_i = (x_{i1}, x_{i2}, \dots, x_{ip})^T$ 입니다.

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function _f_.

우리의 목표는 미지의 함수인 _f_ 를 추정하기 위해 훈련 데이터에 통계적 학습 기법을 적용하는 것입니다.

In other words, we want to find a function $\hat{f}$ such that $Y pprox \hat{f}(X)$ for any observation $(X, Y)$.

다시 말해서, 우리는 임의의 관측값 $(X, Y)$ 에 대하여 $Y pprox \hat{f}(X)$ 가 되는 함수 $\hat{f}$ 를 찾기를 원합니다.

Broadly speaking, most statistical learning methods for this task can be characterized as either _parametric_ or _non-parametric_.

크게 말해, 이 작업을 위한 대부분의 통계적 학습 방법들은 _모수적(parametric)_ 이거나 _비모수적(non-parametric)_ 인 것으로 특징지어질 수 있습니다.

We now briefly discuss these two types of approaches.

우리는 이제 이 두 가지 유형의 접근법에 대해 간략히 논의할 것입니다.

---

### Parametric Methods (모수적 방법론)

먼저 함수의 형태(Shape)를 가정(예: 선형성)하고 한정된 파라미터를 추정하여 모델을 적합시키는 방법입니다.
계산이 빠르고 해석이 쉬운 장점이 있지만 실제 데이터의 형태와 가정된 형태가 크게 다를 수 있다는 단점을 지닙니다.

### Non-Parametric Methods (비모수적 방법론)

함수 $f$의 형태에 특별한 가정을 두지 않고, 데이터 점들에 최대한 근접하도록 적합을 진행하는 방법론들입니다.
데이터를 매우 유연하게 묘사할 수 있으나 유의미한 분석을 위해선 훨씬 방대한 양의 데이터가 필요함을 배웁니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/trans1.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/trans1.html)

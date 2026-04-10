---
layout: default
title: "index"
---

# 2.1.2 How Do We Estimate f ? 
# 2.1.2 어떻게 f를 추정하는가?

Throughout this book, we explore many linear and non-linear approaches for estimating _f_ .

이 책 전반에 걸쳐 우리는 _f_ 를 추정하기 위한 다양한 선형 및 비선형 접근 방식을 탐구합니다.

However, these methods generally share certain characteristics.

그러나 일반적으로 이러한 방법들은 몇 가지 핵심적인 특정 특성을 서로 공유합니다.

We provide an overview of these shared characteristics in this section.

이 섹션에서는 이렇게 공유되는 특성들에 대한 개요를 자세히 제공합니다.

We will always assume that we have observed a set of _n_ different data points.

우리는 항상 _n_ 개의 서로 다른 데이터 요소 관측치 세트를 이미 관찰하고 확보했다고 가정할 것입니다.

For example in Figure 2.2 we observed _n_ = 30 data points.

대표적인 예로, 이전 그림 2.2에서 우리는 총 _n_ = 30개의 데이터 포인트를 정확히 관찰했습니다.

These observations are called the _training data_ because we will use these training observations to train, or teach, our method how to estimate _f_ .

이러한 관찰 집합은 우리가 미래에 함수 _f_ 를 어떻게 추정해야 하는지 그 방법을 시스템에 훈련하거나 가르치기 위해(teach) 사용하는 요소이므로 이들을 _훈련 데이터(training data)_ 라고 부릅니다.

Let $x_{ij}$ represent the value of the _j_ th predictor, or input, for observation _i_ , where _i_ = 1 _,_ 2 _, . . . , n_ and _j_ = 1 _,_ 2 _, . . . , p_ .

이제 $x_{ij}$ 를 관측치 번호 _i_ 에 대한 훈련 구성 요소 중 _j_ 번째 대응하는 예측 변수 또는 입력의 값이라 정립합시다, 이때 요소 _i_ = 1 _,_ 2 _, . . . , n_ 이고 _j_ = 1 _,_ 2 _, . . . , p_ 입니다.

Correspondingly, let $y_i$ represent the response variable for the _i_ th observation.

여기에 상응하여 구조적으로 $y_i$ 로 하여금 _i_ 번째 관측치 관찰 요인에 대응하는 측정 결과치 응답 변수를 나타내게 합시다.

Then our training data consist of $\{(x_1, y_1), (x_2, y_2), . . . , (x_n, y_n)\}$ where $x_i = (x_{i1}, x_{i2}, . . . , x_{ip})^T$.

그러면 궁극적인 우리의 전체 훈련 데이터 모델 형태 구조는 $\{(x_1, y_1), (x_2, y_2), . . . , (x_n, y_n)\}$ 로 복합되어 구성되며 여기서 내부 입력 모형 $x_i = (x_{i1}, x_{i2}, . . . , x_{ip})^T$ 가 됩니다.

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function _f_ .

분석 구조의 우리의 명확한 목표는 그 형태가 아직 파악되지 않은 미지의 함수 _f_ 를 거꾸로 추적해 추정하기 위해 주어진 모형 훈련 데이터들에 가장 알맞은 특권 통계 학습 기술 방법론을 직접 적용하는 것입니다.

In other words, we want to find a function $\hat{f}$ such that $Y \approx \hat{f}(X)$ for any observation $(X, Y)$.

다른 관점의 말로 다시 요약하면, 우리는 확보된 임의의 모든 $(X, Y)$ 에 대한 다중 관측치 형태 모형에 대하여, 이 결과 _Y_ 값 쌍들이 도달치 $Y \approx \hat{f}(X)$ 형태 공식 구조 결과를 도출하여 이루는 가장 근접한 근사 함수 모델 $\hat{f}$ 을 도출해 내어 찾고자 합니다.

Broadly speaking, most statistical learning methods for this task can be characterized as either _parametric_ or _non-parametric_ .

넓은 분석 관점에서 분류하여 말하자면, 이러한 추론 고안 목표 탐색 과제를 수행하는 현존하는 거의 대다수의 통계적 학습의 많은 기법 등 방법론은 두 가지 커다란 특징 갈래 축인 _모수적(parametric)_ 또는 _비모수적(non-parametric)_ 기법 중 한 형태로 크게 특징지어 나눌 수 있습니다.

We now briefly discuss these two types of approaches.

이제 우리는 이 양극을 띠는 두 가지 주요 유형적인 접근 방식의 본질에 대해 각각 간략하게 논의를 전개하겠습니다.

---

## Sub-Chapters (하위 목차)

### Parametric Methods (모수적 방법론)
* [문서로 이동하기](./2_1_2_1_parametric_methods/)

먼저 함수의 형태(Shape)를 가정(예: 선형성)하고 한정된 파라미터를 추정하여 모델을 적합시키는 방법입니다.
계산이 빠르고 해석이 쉬운 장점이 있지만 실제 데이터의 형태와 가정된 형태가 크게 다를 수 있다는 단점을 지닙니다.

### Non-Parametric Methods (비모수적 방법론)
* [문서로 이동하기](./2_1_2_2_non-parametric_methods/)

함수 $f$의 형태에 특별한 가정을 두지 않고, 데이터 점들에 최대한 근접하도록 적합을 진행하는 방법론들입니다.
데이터를 매우 유연하게 묘사할 수 있으나 유의미한 분석을 위해선 훨씬 방대한 양의 데이터가 필요함을 배웁니다.

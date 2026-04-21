---
layout: default
title: "trans1"
---

[< 2.1.2 How Do We Estimate F](../trans1.html) | [2.1.2.2 Non-Parametric Methods >](../2_1_2_2_non-parametric_methods/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Parametric Methods

# 모수적 방법론

Parametric methods involve a two-step model-based approach.

모수적 방법은 모델 기반의 2단계 접근 방식을 포함합니다.

1. First, we make an assumption about the functional form, or shape, of _f_.

1. 첫째, 우리는 _f_ 의 함수적 형태 또는 모양에 대해 가정을 합니다.

For example, one very simple assumption is that _f_ is linear in _X_:

예를 들어 한 가지 매우 간단한 가정은 _f_ 가 _X_ 에 대해 선형이라는 것입니다:

$$ f(X) \approx \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \tag{2.4} $$

This is a _linear model_, which will be discussed extensively in Chapter 3.

이것은 _선형 모델(linear model)_ 인데, 3장에서 광범위하게 논의될 것입니다.

Once we have assumed that _f_ is linear, the problem of estimating _f_ is greatly simplified.

일단 우리가 _f_ 가 선형이라고 가정하고 나면, _f_ 를 추정하는 문제는 크게 단순화됩니다.

Instead of having to estimate an entirely arbitrary _p_-dimensional function _f_(_X_), one only needs to estimate the _p_ + 1 coefficients $\beta_0, \beta_1, \dots, \beta_p$.

전적으로 임의적인 _p_ 차원 함수 _f_(_X_) 를 추정해야 하는 대신, 단지 _p_ + 1 개의 계수 $\beta_0, \beta_1, \dots, \beta_p$ 만 추정하면 됩니다.

2. After a model has been selected, we need a procedure that uses the training data to _fit_ or _train_ the model.

2. 모델이 선택된 후, 우리는 훈련 데이터를 사용하여 모델을 _적합(fit)_ 하거나 _훈련(train)_ 시키는 절차가 필요합니다.

In the case of the linear model fit (2.4), we need to estimate the parameters $\beta_0, \beta_1, \dots, \beta_p$.

선형 모델 적합 (2.4) 의 경우 우리는 파라미터 $\beta_0, \beta_1, \dots, \beta_p$ 를 추정해야 합니다.

That is, we want to find values of these parameters such that

즉 우리는 다음과 같이 되는 이들 파라미터의 값들을 찾기를 원합니다:

$$ Y \approx \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p \tag{2.5} $$

The most common approach to fitting the model (2.4) is referred to as _(ordinary) least squares_, which we discuss in Chapter 3.

모델 (2.4) 를 적합시키는 가장 일반적인 접근법은 _(최상) 최소제곱법((ordinary) least squares)_ 이라 불리며, 우리는 이를 3장에서 논의합니다.

However, least squares is one of many possible ways to fit the linear model.

하지만 최소제곱법은 선형 모델을 적합시키는 가능한 많은 방법들 중 하나일 뿐입니다.

In Chapter 6, we discuss other approaches for estimating the parameters in (2.4).

6장에서 우리는 2.4 의 파라미터를 추정하기 위한 다른 접근법들을 토의합니다.

The model-based approach just described is referred to as _parametric_; it reduces the problem of estimating $f$ down to one of estimating a set of parameters.

방금 설명한 모델 기반 접근법은 _모수적(parametric)_ 이라 일컬어집니다; 이것은 $f$ 를 추정하는 문제를 파라미터 세트를 추정하는 문제 중 하나로 줄입니다.

Assuming a parametric form for $f$ simplifies the problem of estimating $f$ because it is generally much easier to estimate a set of parameters, such as $\beta_0, \beta_1, \dots, \beta_p$ in the linear model (2.4), than it is to fit an entirely arbitrary function $f$.

$f$ 에 대한 모수적 형태를 가정하는 것은 일반적으로 완전히 임의적인 함수 $f$ 를 적합시키는 것보다 선형 모델 (2.4) 내의 $\beta_0, \beta_1, \dots, \beta_p$ 와 같은 파라미터 세트를 추정하는 것이 훨씬 쉽기 때문에 $f$ 추정의 문제를 단순화시킵니다.

The potential disadvantage of a parametric approach is that the model we choose will usually not match the true unknown form of $f$.

모수적 접근법의 잠재적인 단점은 일반적으로 우리가 선택한 모델이 미지의 진짜 $f$ 형태와 일치하지 않을 것이란 점입니다.

If the chosen model is too far from the true $f$, then our estimate will be poor.

만약 선택된 모델이 진짜 $f$ 로부터 너무 멀다면 우리의 추정치는 형편없을 것입니다.

We can try to address this problem by choosing _flexible_ models that can fit many different possible functional forms for $f$.

우리는 $f$ 의 다양하게 다른 여러 가능한 함수 형태들에 맞출 수 있는 _유연한(flexible)_ 모형을 선택함으로써 이 문제를 해결 시도할 수 있습니다.

But in general, fitting a more flexible model requires estimating a greater number of parameters.

하지만 일반적으로 더 유연한 모델을 적합시키기 위해선 더 많은 수량의 파라미터들 추정이 요구됩니다.

These more complex models can lead to a phenomenon known as _overfitting_ the data, which essentially means they follow the errors, or _noise_, too closely.

이러한 특성의 복잡한 모델들은 데이터의 _과적합(overfitting)_ 으로 알려진 현상에 도달할 수 있는데, 이것은 본질적으로 그 모형들이 오류 혹은 _노이즈(noise)_ 를 너무 밀접하게 따라간다는 것을 뜻합니다.

These issues are discussed throughout this book.

이러한 문제들은 이 책 전체에 걸쳐 논의됩니다.

Figure 2.4 shows an example of the parametric approach applied to the `Income` data from Figure 2.3.

그림 2.4는 그림 2.3으로부터의 `Income` 데이터 단면에 적용된 파라미터식 접근 방식 예를 보여줍니다.

We have fit a linear model of the form

우리는 다음과 같은 형태 구조를 가진 선형 모델을 적합시켰습니다:

$$ \text{income} \approx \beta_0 + \beta_1 \times \text{education} + \beta_2 \times \text{seniority} $$

![Figure 2.4](./img/Image_018.png)

**FIGURE 2.4.** _A linear model fit by least squares to the_ `Income` _data from Figure 2.3. The observations are shown in red, and the yellow plane indicates the least squares fit to the data._

**그림 2.4.** _그림 2.3의_ `Income` _데이터에 최소제곱법으로 적합된 선형 모델. 관측치들은 빨간색으로 표시되며, 노란 평면은 데이터에 대한 최소제곱값 적합 모형을 나타냅니다._

**FIGURE 2.5.** _A smooth thin-plate spline fit to the_ `Income` _data from Figure 2.3 is shown in yellow; the observations are displayed in red. Splines are discussed in Chapter 7._

**그림 2.5.** _그림 2.3의_ `Income` _데이터에 맞춰진 부드러운 얇은 판 스플라인(thin-plate spline) 적합 구성이 노란색으로 나타납니다; 관측치들은 빨간색으로 볼 수 있습니다. 스플라인 적합 요소들은 7장에서 토론됩니다._

Since we have assumed a linear relationship between the response and the two predictors, the entire fitting problem reduces to estimating $\beta_0, \beta_1$, and $\beta_2$, which we do using least squares linear regression.

반응과 두 예측 변수 간의 선형 관계를 가정하였기 때문에, 전체 모형 적합 문제는 우리가 최소제곱 선형 회귀 모형들을 사용해 수행하게 될 단지 상수 $\beta_0, \beta_1$, 및 $\beta_2$ 를 추정하는 문제로 감소합니다.

Comparing Figure 2.3 to Figure 2.4, we can see that the linear fit given in Figure 2.4 is not quite right: the true _f_ has some curvature that is not captured in the linear fit.

그림 2.3과 그림 2.4를 비교하여 보면 그림 2.4에 나타난 선형 적합이 전적으로 옳지는 않음을 우리는 인지할 수 있습니다: 실제 진정한 _f_ 는 선형 적합으로 잡히지 않는 얼마 간의 약간의 곡률을 보유합니다.

However, the linear fit still appears to do a reasonable job of capturing the positive relationship between `years of education` and `income`, as well as the slightly less positive relationship between `seniority` and `income`.

그러나 그 해당 선형 적합은 여전히 `seniority` 와 `income` 간의 덜 긍정적인 관계성 측정치 뿐만 아니라 `years of education` 과 `income` 사이의 긍정적 측면 관계성 또한 파악하는 데 제법 훌륭한 합리적인 작업을 해내는 것으로 전제됩니다.

It may be that with such a small number of observations, this is the best we can do.

과연 이처럼 적은 숫자의 관측치 수로선, 아마 이것이 우리가 이행 가능한 최고일지도 모릅니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.2 How Do We Estimate F](../trans1.html) | [2.1.2.2 Non-Parametric Methods >](../2_1_2_2_non-parametric_methods/trans1.html)

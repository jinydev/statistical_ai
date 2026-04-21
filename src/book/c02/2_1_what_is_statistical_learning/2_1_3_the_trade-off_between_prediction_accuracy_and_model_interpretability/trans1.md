---
layout: default
title: "trans1"
---

[< 2.1.2.2 Non-Parametric Methods](../2_1_2_how_do_we_estimate_f/2_1_2_2_non-parametric_methods/trans1.html) | [2.1.4 Supervised Versus Unsupervised Learning >](../2_1_4_supervised_versus_unsupervised_learning/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

# 2.1.3 예측 정확도와 모델 해석력 간의 상충 관계

Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate _f_.

이 책에서 우리가 살펴보는 많은 방법들 중, 일부는 _f_ 를 추정하기 위해 단지 상대적으로 작은 범위의 모양만을 생성할 수 있다는 점에서 덜 유연하거나 더 제한적입니다.

For example, linear regression is a relatively inflexible approach, because it can only generate linear functions such as the lines shown in Figure 2.1 or the plane shown in Figure 2.4.

예를 들어, 선형 회귀는 그림 2.1에 나타난 선들이나 그림 2.4에 표시된 평면과 같은 선형 함수만을 생성할 수 있기 때문에 상대적으로 유연하지 않은 접근법입니다.

Other methods, such as the thin plate splines shown in Figures 2.5 and 2.6, are considerably more flexible because they can generate a much wider range of possible shapes to estimate _f_.

그림 2.5와 2.6에 표시된 얇은 판 스플라인과 같은 다른 방법들은 _f_ 를 추정하기 위해 훨씬 더 광범위한 가능 모형 형태를 생성할 수 있기 때문에 상당히 더 유연합니다.

![Figure 2.7](./img/Image_021.png)

**FIGURE 2.7.** _A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases._

**그림 2.7.** _서로 다른 통계적 학습 방법들을 사용한, 유연성과 해석력 간의 상충 관계에 대한 표현. 일반적으로 한 방법의 유연성이 증가할수록 그것의 해석력은 감소합니다._

One might reasonably ask the following question: _why would we ever choose to use a more restrictive method instead of a very flexible approach?_

누군가는 타당하게 다음과 같은 질문을 던질 수 있습니다: _왜 우리가 매우 유연한 접근법 대신에 더 제한적인 방법을 선택하려는 것일까?_

There are several reasons that we might prefer a more restrictive model.

우리가 더 제한적인 모델을 선호할 수 있는 몇 가지 이유가 있습니다.

If we are mainly interested in inference, then restrictive models are much more interpretable.

만약 우리가 주로 추론에 관심이 있다면, 제한적인 모델들이 훨씬 더 해석하기 쉽습니다.

For instance, when inference is the goal, the linear model may be a good choice since it will be quite easy to understand the relationship between _Y_ and $X_1, X_2, \dots, X_p$.

예를 들어, 추론이 목표일 때, 선형 모델은 _Y_ 와 $X_1, X_2, \dots, X_p$ 사이의 관계를 이해하기 꽤 쉬울 것이기 때문에 좋은 선택이 될 수 있습니다.

In contrast, very flexible approaches, such as the splines discussed in Chapter 7 and displayed in Figures 2.5 and 2.6, and the boosting methods discussed in Chapter 8, can lead to such complicated estimates of _f_ that it is difficult to understand how any individual predictor is associated with the response.

반대로 7장에서 논의되고 그림 2.5 및 2.6에 표시된 스플라인, 그리고 8장에서 논의된 부스팅 방법과 같은 매우 유연한 접근법들은 개별 예측 변수가 응답과 어떻게 연관되는지 이해하기 어려울 정도로 복잡한 _f_ 의 추정치들로 이어질 수 있습니다.

Figure 2.7 provides an illustration of the trade-off between flexibility and interpretability for some of the methods that we cover in this book.

그림 2.7은 우리가 이 책에서 다루는 몇몇 방법들에 대한 유연성과 해석력 간의 상충 관계에 대한 설명을 제공합니다.

Least squares linear regression, discussed in Chapter 3, is relatively inflexible but is quite interpretable.

3장에서 논의된 최소 제곱 선형 회귀는 비교적 유연하지 않지만 꽤 해석 가능합니다.

The _lasso_, discussed in Chapter 6, relies upon the linear model (2.4) but uses an alternative fitting procedure for estimating the coefficients $\beta_0, \beta_1, \dots, \beta_p$.

6장에서 논의된 _라쏘(lasso)_ 는 선형 모델 (2.4) 에 의존하지만, 계수 $\beta_0, \beta_1, \dots, \beta_p$ 를 추정하기 위한 대안적인 적합 절차를 사용합니다.

The new procedure is more restrictive in estimating the coefficients, and sets a number of them to exactly zero.

이 새로운 절차는 계수들을 추정하는 데 더 제한적이고, 그것들 중 다수를 정확히 0으로 설정합니다.

Hence in this sense the lasso is a less flexible approach than linear regression.

그러므로 이러한 의미에서 라쏘는 선형 회귀보다 덜 유연한 접근법입니다.

It is also more interpretable than linear regression, because in the final model the response variable will only be related to a small subset of the predictors—namely, those with nonzero coefficient estimates.

최종 모델에서 응답 변수는 오직 예측 변수들의 작은 부분집합—즉, 0이 아닌 계수 추정치들을 가진 것들—과만 관련될 것이기 때문에, 이는 선형 회귀보다도 더 해석하기 쉽습니다.

_Generalized additive models_ (GAMs), discussed in Chapter 7, instead extend the linear model (2.4) to allow for certain non-linear relationships.

7장에서 논의된 _일반화 가법 모델(Generalized additive models, GAMs)_ 은 특정 비선형적 관계들을 허용하기 위해 대신 선형 모델 (2.4) 를 확장합니다.

Consequently, GAMs are more flexible than linear regression.

결과적으로, GAMs는 선형 회귀보다 더 유연합니다.

They are also somewhat less interpretable than linear regression, because the relationship between each predictor and the response is now modeled using a curve.

각 예측 변수와 응답 간의 관계가 이제 곡선을 사용하여 모델링되기 때문에 그것들은 또한 선형 회귀보다 다소 덜 해석 가능합니다.

Finally, fully non-linear methods such as _bagging_, _boosting_, _support vector machines_ with non-linear kernels, and _neural networks_ (deep learning), discussed in Chapters 8, 9, and 10, are highly flexible approaches that are harder to interpret.

마지막으로 8, 9, 10장에서 논의된 _배깅(bagging)_, _부스팅(boosting)_, 비선형 커널을 가지는 _서포트 벡터 머신(support vector machines)_, 그리고 _신경망(neural networks, 딥러닝)_ 과 같은 완전히 비선형적인 방법들은 해석하기 더 어려운 매우 유연한 접근법들입니다.

We have established that when inference is the goal, there are clear advantages to using simple and relatively inflexible statistical learning methods.

우리는 추론이 목표일 때, 단순하고 비교적 유연하지 않은 통계적 학습 방법들을 사용하는 편이 명확한 이점들이 있다는 것을 확립했습니다.

In some settings, however, we are only interested in prediction, and the interpretability of the predictive model is simply not of interest.

그러나 특정한 환경에서는, 우리는 오직 예측에만 관심이 있으며, 예측 모델의 해석력은 그저 관심사가 아닙니다.

For instance, if we seek to develop an algorithm to predict the price of a stock, our sole requirement for the algorithm is that it predict accurately— interpretability is not a concern.

예를 들어, 만약 우리가 어느 주식의 가격을 예측하는 알고리즘을 개발하고자 한다면, 해당 알고리즘에 대한 우리의 유일한 요구사항은 그것이 정확하게 예측한다는 것이며—해석력은 관심사가 아닙니다.

In this setting, we might expect that it will be best to use the most flexible model available.

이러한 환경에서, 우리는 이용 가능한 가장 유연한 모델을 사용하는 것이 최선일 것이라 기대할지도 모릅니다.

Surprisingly, this is not always the case!

놀랍게도, 이것이 항상 사실은 아닙니다!

We will often obtain more accurate predictions using a less flexible method.

우리는 종종 덜 유연한 방법을 사용하여 더 정확한 예측을 얻을 것입니다.

This phenomenon, which may seem counterintuitive at first glance, has to do with the potential for overfitting in highly flexible methods.

얼핏 보기에 반직관적으로 보일 수 있는 이 현상은 고도로 유연한 방법들에서의 과적합 가능성과 관련이 있습니다.

We saw an example of overfitting in Figure 2.6.

우리는 그림 2.6에서 과적합의 예를 보았습니다.

We will discuss this very important concept further in Section 2.2 and throughout this book.

우리는 2.2절 및 이 책 전반에 걸쳐 이 매우 중요한 개념에 대해 추가로 논의할 것입니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.2.2 Non-Parametric Methods](../2_1_2_how_do_we_estimate_f/2_1_2_2_non-parametric_methods/trans1.html) | [2.1.4 Supervised Versus Unsupervised Learning >](../2_1_4_supervised_versus_unsupervised_learning/trans1.html)

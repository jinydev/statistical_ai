---
layout: default
title: "trans1"
---

[< 2.1.2.1 Parametric Methods](../2_1_2_1_parametric_methods/trans1.html) | [2.1.3 The Trade-Off Between Prediction Accuracy And Model Interpretability >](../../2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Non-Parametric Methods

# 비모수적 방법론

![Figure 2.5](./img/Image_019.png)

**FIGURE 2.5.** _A smooth thin-plate spline fit to the_ `Income` _data from Figure 2.3 is shown in yellow; the observations are displayed in red. Splines are discussed in Chapter 7._

**그림 2.5.** _그림 2.3의_ `Income` _데이터에 맞춰진 부드러운 얇은 판 스플라인(thin-plate spline) 적합이 노란색으로 보여집니다; 관측치들은 빨간색으로 표시됩니다. 스플라인은 7장에서 논의됩니다._

Non-parametric methods do not make explicit assumptions about the functional form of _f_.

비모수적 방법들은 _f_ 의 함수적 형태에 대해 명시적인 가정을 하지 않습니다.

Instead they seek an estimate of _f_ that gets as close to the data points as possible without being too rough or wiggly.

대신 그들은 너무 거칠거나 구불거리지 않으면서 가능한 한 데이터 점들에 가깝게 가는 _f_ 의 추정치를 찾습니다.

Such approaches can have a major advantage over parametric approaches: by avoiding the assumption of a particular functional form for _f_, they have the potential to accurately fit a wider range of possible shapes for _f_.

이러한 접근법들은 모수적 방법들에 비해 한 가지 주요 이점을 가질 수 있습니다: _f_ 에 대한 특정한 함수 형태의 가정을 피함으로써 그들은 _f_ 의 다양히 더 넓은 범위의 가능한 모양들을 정확히 적합시킬 잠재력을 가집니다.

Any parametric approach brings with it the possibility that the functional form used to estimate _f_ is very different from the true _f_, in which case the resulting model will not fit the data well.

어떠한 모수적 접근법이든 _f_ 를 추정하기 위해 사용된 함수 형태가 진짜 _f_ 와 매우 다를 수 있다는 가능성을 가져오며 이 경우 결과 모델은 데이터에 잘 적합되지 않을 것입니다.

In contrast, non-parametric approaches completely avoid this danger, since essentially no assumption about the form of _f_ is made.

이와 대조적으로 비모수적 접근법들은 _f_ 의 형태에 대해 본질적으로 어떠한 가정도 하지 않으므로 이러한 위험을 완전히 피합니다.

But non-parametric approaches do suffer from a major disadvantage: since they do not reduce the problem of estimating _f_ to a small number of parameters, a very large number of observations (far more than is typically needed for a parametric approach) is required in order to obtain an accurate estimate for _f_.

하지만 비모수적 접근법들은 한 가지 주요한 단점을 겪습니다: 그들은 _f_ 의 추정 문제를 소수의 파라미터들로 줄이지 않기 때문에, _f_ 의 정확한 추정치를 얻기 위해서는 (모수적 접근법에서 전형적으로 요구되는 것보다 훨씬 많은) 아주 방대한 수의 관측치들이 요구됩니다.

An example of a non-parametric approach to fitting the `Income` data is shown in Figure 2.5.

`Income` 데이터를 적합시키는 비모수적 접근법의 예시가 그림 2.5에 보여집니다.

A _thin-plate spline_ is used to estimate _f_.

_얇은 판 스플라인(thin-plate spline)_ 이 _f_ 를 추정하기 위해 사용됩니다.

This approach does not impose any pre-specified model on _f_.

이 접근법은 _f_ 에 어떤 사전 지정된 모델도 부과하지 않습니다.

It instead attempts to produce an estimate for _f_ that is as close as possible to the observed data, subject to the fit—that is, the yellow surface in Figure 2.5—being _smooth_.

그 대신 적합—그림 2.5의 노란색 표면—이 _부드러운(smooth)_ 지에 종속된 상태로 그것은 관측된 데이터에 가능한 한 가까운 _f_ 에 대한 추정치를 만들려 시도합니다.

![Figure 2.6](./img/Image_020.png)

**FIGURE 2.6.** _A rough thin-plate spline fit to the_ `Income` _data from Figure 2.3. This fit makes zero errors on the training data._

**그림 2.6.** _그림 2.3의_ `Income` _데이터에 맞춘 거친 얇은 판 스플라인 적합. 이 적합은 훈련 데이터에서 오차를 0으로 만듭니다._

In this case, the non-parametric fit has produced a remarkably accurate estimate of the true _f_ shown in Figure 2.3.

이 경우 비모수적 적합은 그림 2.3에 묘사된 진정한 _f_ 에 대해 놀랍도록 정확한 추정치를 산출해 냈습니다.

In order to fit a thin-plate spline, the data analyst must select a level of smoothness.

얇은 판 스플라인을 적합시키려면 데이터 분석가는 매끄러움의 수준을 선택해야 합니다.

Figure 2.6 shows the same thin-plate spline fit using a lower level of smoothness, allowing for a rougher fit.

그림 2.6은 거친 적합을 허용하면서 더 낮은 강도의 매끄러움을 사용하는 같은 얇은 판 스플라인 적합을 보여줍니다.

The resulting estimate fits the observed data perfectly!

결과적인 이 추정 모델은 관측 데이터들에 완벽하게 맞습니다!

However, the spline fit shown in Figure 2.6 is far more variable than the true function _f_, from Figure 2.3.

하지만 그림 2.6에 지정된 스플라인 적합은 그림 2.3으로부터의 진짜 함수 _f_ 보다 훨씬 더 가변적입니다.

This is an example of overfitting the data, which we discussed previously.

이것은 우리가 이전에 논의했던 데이터의 과적합에 대한 예제입니다.

It is an undesirable situation because the fit obtained will not yield accurate estimates of the response on new observations that were not part of the original training data set.

얻어진 그 해당 적합이 본래 훈련 데이터 세트의 일부가 아니던 새 관측 지표들에 대해서 해당 응답의 정확한 추정치들을 산출해 내지 못할 것이기 때문에 이것은 바람직하지 않은 경우입니다.

We discuss methods for choosing the _correct_ amount of smoothness in Chapter 5.

우리는 측정 상의 _올바른_ 매끄러움 양을 선택하기 위한 방법들을 5장에서 논의합니다.

Splines are discussed in Chapter 7.

스플라인들은 7장에서 논의됩니다.

As we have seen, there are advantages and disadvantages to parametric and non-parametric methods for statistical learning.

우리가 보았듯이 통계적 학습의 모수적 및 비모수적 방법에는 장점과 단점이 존재합니다.

We explore both types of methods throughout this book.

우리는 이 책 전체를 통하여 이 두 가지 유형의 방법을 모두 탐구합니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.2.1 Parametric Methods](../2_1_2_1_parametric_methods/trans1.html) | [2.1.3 The Trade-Off Between Prediction Accuracy And Model Interpretability >](../../2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/trans1.html)

---
layout: default
title: "trans1"
---

# _5.1.1 The Validation Set Approach_ 
# _5.1.1 검증 세트 접근법_

Suppose that we would like to estimate the test error associated with fitting a particular statistical learning method on a set of observations.
관측치 세트에 특정 통계적 학습 방법을 적합시킬 때 수반되는 시험 오차를 우리가 추정하고자 한다고 가정해 보자.

The _validation set approach_ , displayed in Figure 5.1, is a very simple strategy validation for this task.
그림 5.1에 표시된 _검증 세트 접근법(validation set approach)_ 은 이 과업을 위한 매우 단순한 전략이다.

It involves randomly dividing the available set of observations into two parts, a _training set_ and a _validation set_ or _hold-out set_ .
이는 가용한 관측치 세트를 무작위로 두 부분, 즉 _훈련 세트(training set)_ 와 _검증 세트(validation set)_ 혹은 _보류 세트(hold-out set)_ 로 나누는 과정을 포함한다.

The validation model is fit on the training set, and the fitted model is used to predict the responses for the observations in the validation set.
검증 모델은 훈련 세트 위에서 훈련(fit)되며, 이 훈련된 모델은 이후 검증 세트에 속한 관측치들의 응답을 예측하는 데 사용된다.

The resulting validation set error rate—typically assessed using MSE in the case of a quantitative response—provides an estimate of the test error rate. 
결과적으로 도출된 검증 세트 오차율(통상적으로 정량적 응답의 경우 MSE를 사용하여 평가됨)은 실전 시험 오차율에 대한 하나의 추정치를 제공한다.

We illustrate the validation set approach on the `Auto` data set.
우리는 `Auto` 데이터 세트에서 이 검증 세트 접근법을 시연해 보겠다.

Recall from Chapter 3 that there appears to be a non-linear relationship between `mpg` and `horsepower` , and that a model that predicts `mpg` using `horsepower` and `horsepower`[2] gives better results than a model that uses only a linear term.
3장에서 `mpg`와 `horsepower` 사이에 비선형적인 관계가 나타난다는 점, 그리고 오직 선형 항만을 사용하는 모델보다 `horsepower`와 `horsepower`의 제곱항을 함께 사용하여 `mpg`를 예측하는 모델이 더 나은 결과를 제공한다는 점을 상기해 보라.

It is natural to wonder whether a cubic or higher-order fit might provide even better results.
여기서 3차 항 혹은 그보다 더 고차원의 적합을 사용하면 훨씬 더 나은 결과를 제공하지 않을까 의문을 갖는 것은 지극히 자연스럽다.

We answer this question in Chapter 3 by looking at the p-values associated with a cubic term and higher-order polynomial terms in a linear regression.
우리는 3장에서 선형 회귀 모형 내의 3차 항 및 기타 고차 다항식 항들의 p-값을 살펴봄으로써 이 질문에 이미 답한 바 있다.

But we could also answer this question using the validation method.
하지만 우리는 이 검증 방식을 사용해서도 동일한 질문에 충분히 답할 수 있다.

We randomly split the 392 observations into two sets, a training set containing 196 of the data points, and a validation set containing the remaining 196 observations.
우리는 무작위로 392개의 관측치를 두 세트로 쪼갠다. 즉 196개의 데이터 포인트를 포함하는 훈련 세트 하나와, 나머지 196개의 관측치를 포함하는 검증 세트 하나로 분할한다.

The validation set error rates that result from fitting various regression models on the training sample and evaluating their performance on the validation sample, using MSE as a measure of validation set error, are shown in the left-hand panel of Figure 5.2.
훈련 샘플에 여러 회귀 모델들을 각각 훈련시키고 검증 샘플에 대고 MSE를 검증 세트 오차 척도로 사용하여 그 성능을 평가함으로써 도출된 각각의 검증 세트 오차율이 그림 5.2의 왼쪽 패널에 나타나 있다.

The validation set MSE for the quadratic fit is considerably smaller than for the linear fit.
2차식(quadratic) 적합 라인이 보여주는 검증 세트 MSE 수치는 1차 선형(linear) 적합이 거둔 것보다 대폭 더 작다(더 성능이 좋다).

However, the validation set MSE for the cubic fit is actually slightly larger than for the quadratic fit.
하지만, 3차식(cubic) 적합의 검증 세트 MSE는 도리어 정작 2차식 적합 때보다 아주 살짝 더 크게 나타난다.

This implies that including a cubic term in the regression does not lead to better prediction than simply using a quadratic term. 
이는 회귀 내에 고차원 3차 항을 굳이 포함시키는 것이 단순하게 2차 항만을 사용하는 것보다 더 나은 예측력으로 이어지지는 않는다는 사실을 강하게 시사한다.

Recall that in order to create the left-hand panel of Figure 5.2, we randomly divided the data set into two parts, a training set and a validation set.
다시 상기해 보라. 저 그림 5.2의 좌측 패널을 구성해 내기 위해, 우리는 데이터 세트 전체를 무작위로 훈련 세트와 검증 세트라는 두 조각으로 분할했었다.

If we repeat the process of randomly splitting the sample set into two parts, we will get a somewhat different estimate for the test MSE.
만약 우리가 샘플 세트를 이등분으로 무작위 분할하는 이 과정을 지속적으로 반복한다면, 매번 테스트 MSE에 대해 다소간 차이가 있는 엇갈린 추정 수치들을 얻게 될 것이다.

As an illustration, the right-hand panel of Figure 5.2 displays ten different validation set MSE curves from the `Auto` data set, produced using ten different random splits of the observations into training and validation sets.
본보기 차원으로, 그림 5.2의 오른쪽 패널은 `Auto` 데이터 세트 내 관측치들을 훈련 및 검증 세트로 각기 무작위로 10차례 다르게 분할하여 도출한 총 10개의 서로 다른 검증 세트 MSE 곡선들을 전시해 보여준다.

All ten curves indicate that the model with a quadratic term has a dramatically smaller validation set MSE than the model with only a linear term.
열 개의 곡선 모두는 한결같이, 2차 항을 내장한 모델이 오직 선형 항만을 탑재한 모델에 비해 엄청나게 더 작은 검증 세트 MSE 에러를 낳는다는 것을 의미한다.

Furthermore, all ten curves indicate that there is not much benefit in including cubic or higher-order polynomial terms in the model.
나아가, 열 개의 곡선들은 모두 다 모델 내에 3차 혹은 그 이상의 고차원 다항식 항들을 들이미는 것에 딱히 더 큰 실익이 남아있지 않다는 사실 또한 알려준다.

But it is worth noting that each of the ten curves results in a different test MSE estimate for each of the ten regression models considered.
그러나 여기서 주목해야 할 점은, 해당 10개의 곡선 각각이 투입된 10종의 회귀 모델들에 대해 매번 서로 다른 테스트 MSE 추정치를 내뱉는다는 것이다.

And there is no consensus among the curves as to which model results in the smallest validation set MSE.
게다가 그 곡선들 사이에서는 정확히 "어떤 모델이 가장 최저의 약점 없는 검증 세트 MSE를 도출해 냈는지" 에 대해 단 한 점의 합의(consensus) 도 존재하지 않는다.

Based on the variability among these curves, all that we can conclude with any confidence is that the linear fit is not adequate for this data. 
이 곡선들 사이에 나타난 극심한 편차와 변동성(variability) 에 근거해 볼 때, 우리가 조금의 확신이라도 가지고 내릴 수 있는 유일한 결론은 선형 적합 라인이 이 데이터엔 도무지 걸맞지 않다(적절하지 않다)는 점 단 한 가지뿐이다.

The validation set approach is conceptually simple and is easy to implement.
검증 세트 접근법은 개념 면에서 직관적일 뿐만 아니라 구현하기도 굉장히 쉽다.

But it has two potential drawbacks: 
그렇지만 이 접근법은 잠재적으로 2개의 결함을 지닌다.

1. As is shown in the right-hand panel of Figure 5.2, the validation estimate of the test error rate can be highly variable, depending on precisely which observations are included in the training set and which observations are included in the validation set. 
첫째(1.), 바로 위에서 그림 5.2의 우측 패널이 적나라하게 보여주듯, 시험 오차율을 유추해낸 검증 추정치는 정확히 어떤 관측치들이 훈련 세트에 포함되었고 다른 어떤 녀석들이 검증에 들어갔는지 운에 따라 엄청나게 높은 변동성(highly variable)을 수반할 수 있다.

2. In the validation approach, only a subset of the observations—those that are included in the training set rather than in the validation set—are used to fit the model. Since statistical methods tend to perform worse when trained on fewer observations, this suggests that the validation set error rate may tend to _overestimate_ the test error rate for the model fit on the entire data set. 
둘째(2.), 검증 접근법 체계에선, 관측치들의 딱 절반인 일부분(검증 세트 대신 훈련 세트로 뽑혀 들어간 무리들) 만이 모델 적합에 사용된다. 통계적 기법들은 대체로 학습 수련 관측치의 규모가 터무니없이 적을 때 한층 더 형편없는 성능을 내는 경향이 짙기에, 이는 결국 검증 세트 추정 에러율이라는 값이 실제론 전체 데이터 세트를 다 먹고 훈련한 제대로 된 모델이 가질 실전 오차율보다 훨씬 에러가 클 것으로 대폭 과대평가(overestimate) 해버리는 왜곡된 경향성을 띠게 됨을 시사한다.

In the coming subsections, we will present _cross-validation_ , a refinement of the validation set approach that addresses these two issues. 
다가올 하위 단원에서는 바로 이 두 가지 약점 이슈를 완벽하게 보완 해결하는 검증 세트 접근 방식의 궁극적 개선안인 _교차 검증(cross-validation)_ 파훼법을 정식으로 등판시킬 것이다.

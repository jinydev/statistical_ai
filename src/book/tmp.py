import os

text = """---
layout: default
title: "index"
---

# 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

# 2.1.3 예측 정확도와 모델 해석력 간의 상충 관계

Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate _f_.

이 책 안에서 우리가 조사하는 많은 방법들 중, 일부 방법은 _f_ 를 추정하기 위해 상대적으로 좁은 범위의 모양만을 생성해 낼 수 있다는 점에서 덜 유연하거나 혹은 더 제한적인 속성을 갖습니다.

For example, linear regression is a relatively inflexible approach, because it can only generate linear functions such as the lines shown in Figure 2.1 or the plane shown in Figure 2.4.

예를 들어 선형 회귀는 그림 2.1에 나타난 선이나 그림 2.4에 표시된 평면과 같은 선형적인 함수만을 생성할 수 있기 때문에 상대적으로 덜 유연한 접근법입니다.

Other methods, such as the thin plate splines shown in Figures 2.5 and 2.6, are considerably more flexible because they can generate a much wider range of possible shapes to estimate _f_. 

그림 2.5 및 그림 2.6에 표시된 얇은 보강판 스플라인 모형 같은 여타 방법들은, 그 모형들이 _f_ 를 추정하기 위해 훨씬 더 광범위하게 넓은 폭 범위의 가능 모형을 도출할 수 있기 때문에 상당히 더 유연합니다.

![Figure 2.7](./img/Image_021.png)

**FIGURE 2.7.** _A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases._ 

**그림 2.7.** _서로 다른 각종 통계적 기계 학습 방법들을 이용하여 나타낸, 부분 유연성 측면과 직관 해석 모델력 간의 상충 관계에 대한 일련 표상. 일반적으로 특정 방법이 갖는 유연성 척도가 증가할수록 해당 구조 해석력은 감소합니다._

One might reasonably ask the following question: _why would we ever choose to use a more restrictive method instead of a very flexible approach?_ 

사람들은 아주 논리 합당하게 다음과 같이 일련의 질문을 던져 물을 수 있습니다: _대체 왜 우린 매우 유연한 접근법 대신에 더 제한적인 방법을 선택하는 걸까?_

There are several reasons that we might prefer a more restrictive model. 

우리가 좀 더 제한적인 제약 모형 방식 모델을 선호하는 몇몇 이유들이 있습니다.

If we are mainly interested in inference, then restrictive models are much more interpretable. 

만일 우리가 주로 결과 추론 예측에 집중된 쪽에 관심을 갖게 된다면, 결과적으로 제약적인 제한 모델 방법이 오히려 수단 해석에 있어 본래 훨씬 더 낫게 쉽게 직관 해석이 잘 됩니다.

For instance, when inference is the goal, the linear model may be a good choice since it will be quite easy to understand the relationship between _Y_ and $X_1, X_2, \dots, X_p$. 

단적인 예로서 추론 자체가 목표가 될 경우엔 단연 _Y_ 결과와 예측 변수 기조인 $X_1, X_2, \dots, X_p$ 예측 척도 사이의 상호 관련성을 직관 이해하는 과정 자체가 사실 매우 쉽기 때문에 이런 선형 지표 구조 모형은 좋은 선택일 수 있습니다.

In contrast, very flexible approaches, such as the splines discussed in Chapter 7 and displayed in Figures 2.5 and 2.6, and the boosting methods discussed in Chapter 8, can lead to such complicated estimates of _f_ that it is difficult to understand how any individual predictor is associated with the response. 

반면에 제7장에서 논의되고 그림 2.5 및 2.6에 나타난 스플라인이나 제8장에서 논의되는 부스팅 방법과 같은 매우 유연한 접근법들은 어떻게 개별 예측 변수가 응답과 연관되는지 이해하기 어려울 정도로 매우 복잡한 _f_ 의 추정치로 이어질 수 있습니다.

Figure 2.7 provides an illustration of the trade-off between flexibility and interpretability for some of the methods that we cover in this book. 

그림 2.7은 우리가 이 책에서 다루는 방법들 가운데 몇몇 모형들에 대한 유연성과 해석력 간의 상충 관계(trade-off) 설명을 제공합니다.

Least squares linear regression, discussed in Chapter 3, is relatively inflexible but is quite interpretable. 

제3장에서 논의된 최소 제곱 선형 회귀는 비교적 덜 유연하지만 꽤 직관적으로 해석이 가능합니다.

The _lasso_, discussed in Chapter 6, relies upon the linear model (2.4) but uses an alternative fitting procedure for estimating the coefficients $\\beta_0, \\beta_1, \\dots, \\beta_p$. 

제6장에서 논의되는 _라쏘(lasso)_ 는 선형 모델 식 (2.4) 에 의존하지만, 그 매개 파라미터 계수 값들인 $\\beta_0, \\beta_1, \\dots, \\beta_p$ 를 추정하기 위해서 대안적인 적합 절차를 사용합니다.

The new procedure is more restrictive in estimating the coefficients, and sets a number of them to exactly zero. 

이 새로운 평가 절차는 계수들을 추정하는 데 있어서 한층 더 엄격히 제한적이며, 그들 중 다수를 정확히 0으로 설정합니다.

Hence in this sense the lasso is a less flexible approach than linear regression. 

그러므로 이러한 의미에서 라쏘 모형은 기존 선형 회귀보다 덜 유연한 접근법입니다.

It is also more interpretable than linear regression, because in the final model the response variable will only be related to a small subset of the predictors—namely, those with nonzero coefficient estimates. 

또한 이것은 선형 회귀분석보다 해석하기 쉬운데, 그 이유는 최종 모델에서 응답 변수가 오직 예측 변수들의 아주 작은 하위 집합—즉, 0이 아닌 계수 추정치를 지닌 것들—하고만 관련될 것이기 때문입니다.

_Generalized additive models_ (GAMs), discussed in Chapter 7, instead extend the linear model (2.4) to allow for certain non-linear relationships. 

제7장에서 서술되는 _일반화 가법 모델(Generalized additive models, GAMs)_ 은 그 대신 특정 비선형적 관계들을 허용하기 위해 기존 선형 모델 식 (2.4) 를 확장합니다.

Consequently, GAMs are more flexible than linear regression. 

결과적으로, GAMs 모델은 선형 회귀 방식보다 모델 차원에서 더 유연합니다.

They are also somewhat less interpretable than linear regression, because the relationship between each predictor and the response is now modeled using a curve. 

각 예측 변수 요소와 응답 간의 관계가 이제 곡선을 사용하여 수치 모델화되기 때문에 이 방식 수단들 또한 선형 회귀 모델보다 다소 덜 쉽게 해석될 수 있습니다.

Finally, fully non-linear methods such as _bagging_, _boosting_, _support vector machines_ with non-linear kernels, and _neural networks_ (deep learning), discussed in Chapters 8, 9, and 10, are highly flexible approaches that are harder to interpret. 

마지막으로 제8, 9, 10장에서 논의되는 _배깅(bagging)_, _부스팅(boosting)_, 비선형 평가 커널을 수반하는 _서포트 벡터 머신(support vector machines)_, 또 _신경망(neural networks, 딥러닝)_ 등과 같은 완전히 비선형인 방식들은 해석하기가 더욱 어려운 고도로 유연한 접근법들입니다.

We have established that when inference is the goal, there are clear advantages to using simple and relatively inflexible statistical learning methods. 

우리는 측정 결과 추론 자체가 목표인 경우 단순하고 비교적 덜 유연한 단편 방식의 측정 통계 방식 수단 방법을 쓰는 것에 분명한 이점들이 존재함을 확립해 왔습니다.

In some settings, however, we are only interested in prediction, and the interpretability of the predictive model is simply not of interest. 

하지만 특정한 환경 수준에서는 우리는 예측 결과론 하나에만 집중해 흥미를 가지고 해당 예측 도출 모형 예측 모델 속 모델의 단편 해석 자체의 부분 해석 역량은 단순히 어떤 일말의 흥미 대상 요소가 단 전연 아닙니다.

For instance, if we seek to develop an algorithm to predict the price of a stock, our sole requirement for the algorithm is that it predict accurately— interpretability is not a concern. 

예를 들어, 만약 우리가 수시 특정 주식의 훗날 시세를 측정하는 척도 알고리즘을 구축 개발하길 단 모색한다면, 그 일련 알고리즘에 모형에 기인된 우리의 절대적인 요구 한 가지 기준 조건 사항은 그것이 결과 치를 명백 단연코 매우 정확하게 수치 예측해 측정해 수행 산출할 역량을 지닐 것인가 전제 하나에 달린 일이며—모형의 내부 구조석 해석 역량 파악 가능성은 어떤 관심 우려 결론의 고려 대상 사안 요소 결 기 결 도결 전혀 아닙니다.

In this setting, we might expect that it will be best to use the most flexible model available. 

이러한 설정 하에서 우리는 이용 가능한 가장 유연한 모델을 사용하는 것이 최선일 것이라 기대할지도 모릅니다.

Surprisingly, this is not always the case! 

놀랍게도, 이것이 항상 사실인 것은 아닙니다!

We will often obtain more accurate predictions using a less flexible method. 

우리는 종종 덜 유연한 방식을 사용하여 더 정확한 예측을 얻게 될 것입니다.

This phenomenon, which may seem counterintuitive at first glance, has to do with the potential for overfitting in highly flexible methods. 

얼핏 보기에 본 모형 예측 직관에 완전 상반 배반되어 역행되어 보이는 이 특수 역 모순 단면 현상은 극도로 유연한 방법에서의 과적합 가능성과 관련이 매우 높습니다.

We saw an example of overfitting in Figure 2.6. 

우리는 그림 2.6에서 이런 과적합 모형 분석의 한 가지 예를 보았습니다.

We will discuss this very important concept further in Section 2.2 and throughout this book. 

우리는 해당 심도 매우 중대한 개념 기조를 2.2절 및 책 교재 내내 지속해 논의 진행해 갈 것입니다.
"""

path = r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability\index.md'
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('done')

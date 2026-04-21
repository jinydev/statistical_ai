---
layout: default
title: "trans1"
---

[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/trans1.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 3.5 Comparison of Linear Regression with $K$-Nearest Neighbors

# 3.5 선형 회귀와 $K$-최근접 이웃 간의 비교

As discussed in Chapter 2, linear regression is an example of a _parametric_ approach because it assumes a linear functional form for $f(X)$.

제2장에서 논의했듯, 선형 회귀는 본질적으로 $f(X)$ 항목을 향해 선형적인 함수 형태를 가정한다는 측면에서 _모수적(parametric)_ 접근법의 한 가지 좋은 일례를 보여줍니다.

Parametric methods have several advantages.

이러한 모수적 방법론은 여러 가지 강점 이점들을 안고 있습니다.

They are often easy to fit, because one need estimate only a small number of coefficients.

무엇보다도 추정에 소요되는 대상 계수 파편들의 수가 아주 적기 때문에 대개 모델 적합이 한결 쉽습니다.

In the case of linear regression, the coefficients have simple interpretations, and tests of statistical significance can be easily performed.

특히 선형 회귀의 경우에는 각 계수들의 산출 해석 과정이 매우 단순 명료하며, 덤으로 부수적인 통계적 유의성 검정도 몹시 수월하게 병행 조달해 낼 수 있습니다.

But parametric methods do have a disadvantage: by construction, they make strong assumptions about the form of $f(X)$.

하지만 모수적 접근법들 역시 치명적인 단점 맹점을 내포합니다: 구조 태생적으로, 모델이 시종일관 $f(X)$ 의 근본 구조 형태에 관하여 극히 너무 엄격하고 강한 기저 잣대 전제를 가정 고집해 버립니다.

If the specified functional form is far from the truth, and prediction accuracy is our goal, then the parametric method will perform poorly.

만약 우리 예측 정확도가 최우선 목표인 상황에서 그렇게 설정 투입된 기저 함수 구조가 정작 실제 본연의 참인 양태 구조와 아주 동떨어져 비껴간 경우라면 모수적 예측 모델의 성과는 아주 형편없는 궤도 성적으로 전락할 수밖에 없습니다.

For instance, if we assume a linear relationship between X and Y but the true relationship is far from linear, then the resulting model will provide a poor fit to the data, and any conclusions drawn from it will be suspect.

가령 우리가 $X$ 와 $Y$ 사이 관계를 임의로 선형적일 거라 전제 가설을 세웠건만 실상 참인 관계가 결코 전혀 비선형적인 양태라면, 결과 도출 모델은 데이터와 엇박자를 낼 뿐 아니라 그걸 토대로 내린 모든 최종 도출 결론 자체마저 여지없이 큰 의구심에 직면하게 될 것입니다.

In contrast, _non-parametric_ methods do not explicitly assume a parametric form for $f(X)$, and thereby provide an alternative and more flexible approach for performing regression.

이와 대조적으로 _비모수적(non-parametric)_ 방법론은 $f(X)$ 파트에 대해 어떤 특정한 모수적 틀 형태를 별도로 명시 고집 전제하지 않으며, 이로 인해 한결 더 낫고 유연한 대체 회귀 분석 조달 수단 및 접근법을 풍부하게 제공해 냅니다.

We discuss various non-parametric methods in this book.

앞으로 이 책 전반에서 우리는 이같이 다채로운 비모수적 접근 방법론 무리들을 다방면으로 논의 다룰 것입니다.

Here we consider one of the simplest and best-known non-parametric methods, _K-nearest neighbors regression_ ().

여기 당장 우리 측은 비모수적 수단 중에서도 가장 간결하고 또 가장 대중 널리 잘 알려진 대표 형태인 _K-최근접 이웃 회귀(K-nearest neighbors regression, )_ 에 눈을 돌려 집중 고찰해 봅니다.

The  method is closely related to the KNN classifier discussed in Chapter 2.

이 KNN 회귀 방식 자체는 사실 이전 제2장에서 살펴 다룬 분류 판별 분야의 KNN 분류기(classifier)와 본질적으로 몹시 밀착 친척 관계를 갖습니다.

Given a value for $K$ and a prediction point $x_0$,  first identifies the $K$ training observations that are closest to $x_0$, represented by $N_0$.

임의의 수치 $K$ 와 목푯값 관측 타점 예측 변수 $x_0$ 잣대가 주어졌을 시, 제일 먼저 제반 KNN 회귀는 대상 $x_0$ 에 가장 가까이 맞닿은 주변 $K$ 개의 훈련 관측치들 이웃 무리를 선별 식별해 내는데, 흔히 이를 일컬어 지표 묶음 $N_0$ 로 칭하고 대변 표상합니다.

It then estimates $f(x_0)$ using the average of all the training responses in $N_0$. In other words,

이윽고 모델은 바로 이 $N_0$ 이웃 단위 무리 내부에 포함된 전체 총 훈련 응답 결괏값들의 평균 잣대를 활용해 목표 타점 $f(x_0)$ 요건을 추정해 냅니다. 달리 연산 수식 측면으로 다시 말해 설명하면 아래와 같이 기술합니다:

**==> picture [87 x 27] intentionally omitted <==**

Figure 3.16 illustrates two KNN fits on a data set with $p=2$ predictors.
그림 3.16 은 단 2개의 예측 변수 조각 $p=2$ 인자로 묶인 구조의 데이터 단면에 조달 맞춰 구동한 2편의 개별 KNN 결괏값 적합 도면을 각각 예시해 모사합니다.

The fit with $K=1$ is shown in the left-hand panel, while the right-hand panel corresponds to $K=9$.
좌측 해당 패널 도면에 투사된 것은 인자 $K=1$ 조건에 동반 맞춰 나온 결괏값 선이고, 한편 같은 선상의 오른쪽 패널 전경 도면 단면은 $K=9$ 단위 기준일 때 파생 적합된 궤적에 응답 일치합니다.

We see that when $K=1$, the KNN fit perfectly interpolates the training observations, and consequently takes the form of a step function.
우리는 여기서 $K=1$ 단위일 땐, 도출 KNN 모델 전개가 당초 모든 훈련 관측 점 타점 점들을 일점 가감 없이 곡예 보간(interpolates)하여 전부 그 자취를 흡수 그대로 이어나가며, 결과적으로 계단식 함수(step function) 형태의 극단 외관 굴곡 외양 궤도를 띄고 전락함을 적나라하게 목도합니다.

When $K=9$, the KNN fit still is a step function, but averaging over nine observations results in much smaller regions of constant prediction, and consequently a smoother fit.
반면 $K=9$ 편일 적의 KNN 단면 궤선은 비록 여전히 계단식 편린 형태 기조 잔재를 온전히 간직하고 있긴 하나, 무려 9개의 광범위 주변 관측 점들을 대거 아울러 평탄 상쇄 통산 평균 내린 탓에, 예측 단선이 곧은 상수 지위로 국한 제한 도출 국면 차지하는 영역 폭 자체가 훨씬 더 대거 줄어들어 쪼그라들고 결국 그 이음 결과론적으로 아주 더 많이 부드러운 매끈한 표면 양태 궤적 적합선으로 탈바꿈 조달 귀결되는 것을 볼 수 있습니다.

In general, the optimal value for $K$ will depend on the _bias-variance tradeoff_, which we introduced in Chapter 2.
통상 이러한 $K$ 값을 결정지을 최적 최고 효율 잣대 지표는, 우리가 앞선 챕터 제2장에서 논의 소환 소개했던 _편향-분산 상충 관계 상쇄 교환(bias-variance tradeoff)_ 대목 기조 논리에 전수 상당수 전적 의존 결정 따질 것입니다.

A small value for $K$ provides the most flexible fit, which will have low bias but high variance.
일례로 $K$ 지수가 몹시 작고 소규모 수치로 한정 국한되면 비록 아주 고도의 막강 유연한 변형 결괏값을 허여 제공해 내어 편향(bias)의 양은 줄이겠지만 동시에 극대 분산(variance)의 여파 곤경 널뛰 현상을 고스란히 끌어 안기 마련입니다.

This variance is due to the fact that the prediction in a given region is entirely dependent on just one observation.
여기서 치솟는 분산 요건은 당면 예측 영역 내 도출 궤도가 오로지 국한된 단 하나의 개별 훈련 관측치 점에 전적으로 온통 심하게 치우쳐 의존한 까닭에서 기인 비롯된 현상인 것입니다.



**==> picture [311 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
y<br>y y<br>x1 x1<br>x2 x2<br>y y<br>**----- End of picture text -----**<br>


**FIGURE 3.16.** _Plots of f_[ˆ] ( X ) _using  on a two-dimensional data set with_ 64 _observations (orange dots)._ Left: _K_ = 1 _results in a rough step function fit._ Right: _K_ = 9 _produces a much smoother fit._

In contrast, larger values of _K_ provide a smoother and less variable fit; the prediction in a region is an average of several points, and so changing one observation has a smaller effect. However, the smoothing may cause bias by masking some of the structure in $f(X)$. In Chapter 5, we introduce several approaches for estimating test error rates. These methods can be used to identify the optimal value of _K_ in .

In what setting will a parametric approach such as least squares linear regression outperform a non-parametric approach such as ? The answer is simple: _the parametric approach will outperform the nonparametric approach if the parametric form that has been selected is close to the true form of f_ . Figure 3.17 provides an example with data generated from a one-dimensional linear regression model. The black solid lines represent $f(X)$, while the blue curves correspond to the KNN fits using _K_ = 1 and _K_ = 9. In this case, the _K_ = 1 predictions are far too variable, while the smoother _K_ = 9 fit is much closer to $f(X)$. However, since the true relationship is linear, it is hard for a non-parametric approach to compete with linear regression: a non-parametric approach incurs a cost in variance that is not offset by a reduction in bias. The blue dashed line in the lefthand panel of Figure 3.18 represents the linear regression fit to the same data. It is almost perfect. The right-hand panel of Figure 3.18 reveals that linear regression outperforms KNN for this data. The green solid line, plotted as a function of 1 _/K_ , represents the test set mean squared error (MSE) for KNN. The KNN errors are well above the black dashed line, which is the test MSE for linear regression. When the value of _K_ is large, then KNN performs only a little worse than least squares regression in terms of MSE. It performs far worse when _K_ is small.

In practice, the true relationship between X and Y is rarely exactly linear. Figure 3.19 examines the relative performances of least squares regression and KNN under increasing levels of non-linearity in the relationship between X and Y . In the top row, the true relationship is nearly linear. In this case we see that the test MSE for linear regression is still superior

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors

**==> picture [315 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 −1.0 −0.5 0.0 0.5 1.0<br>x x<br>4<br>4<br>3 3<br>y 2 y 2<br>1 1<br>**----- End of picture text -----**<br>


**FIGURE 3.17.** _Plots of f_[ˆ] ( X ) _using  on a one-dimensional data set with_ 50 _observations. The true relationship is given by the black solid line._ Left: _The blue curve corresponds to K_ = 1 _and interpolates (i.e. passes directly through) the training data._ Right: _The blue curve corresponds to K_ = 9 _, and represents a smoother fit._

**==> picture [316 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>4<br>0.15<br>3<br>y 0.10<br>2<br>Mean Squared Error<br>0.05<br>1<br>0.00<br>**----- End of picture text -----**<br>


**FIGURE 3.18.** _The same data set shown in Figure 3.17 is investigated further._ Left: _The blue dashed line is the least squares fit to the data. Since f_ ( X ) _is in fact linear (displayed as the black line), the least squares regression line provides a very good estimate of f_ ( X ) _._ Right: _The dashed horizontal line represents the least squares test set MSE, while the green solid line corresponds to the MSE for KNN as a function of_ 1 _/K (on the log scale). Linear regression achieves a lower test MSE than does , since f_ ( X ) _is in fact linear. For , the best results occur with a very large value of K, corresponding to a small value of_ 1 _/K._

114 3. Linear Regression

**==> picture [318 x 301] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>3.5 0.08<br>3.0<br>0.06<br>2.5<br>y<br>2.0 0.04<br>1.5 Mean Squared Error<br>0.02<br>1.0<br>0.5 0.00<br>0.15<br>3.5<br>3.0<br>0.10<br>2.5<br>y<br>2.0<br>Mean Squared Error 0.05<br>1.5<br>1.0<br>0.00<br>**----- End of picture text -----**<br>


**FIGURE 3.19.** Top Left: _In a setting with a slightly non-linear relationship between X and Y (solid black line), the KNN fits with K_ = 1 _(blue) and K_ = 9 _(red) are displayed._ Top Right: _For the slightly non-linear data, the test set MSE for least squares regression (horizontal black) and KNN with various values of_ 1 _/K (green) are displayed._ Bottom Left and Bottom Right: _As in the top panel, but with a strongly non-linear relationship between X and Y ._

to that of KNN for low values of _K_ . However, for _K ≥_ 4, KNN outperforms linear regression. The second row illustrates a more substantial deviation from linearity. In this situation, KNN substantially outperforms linear regression for all values of _K_ . Note that as the extent of non-linearity increases, there is little change in the test set MSE for the non-parametric KNN method, but there is a large increase in the test set MSE of linear regression.

Figures 3.18 and 3.19 display situations in which KNN performs slightly worse than linear regression when the relationship is linear, but much better than linear regression for nonlinear situations. In a real life situation in which the true relationship is unknown, one might suspect that KNN should be favored over linear regression because it will at worst be slightly inferior to linear regression if the true relationship is linear, and may give substantially better results if the true relationship is non-linear. But in reality, even when the true relationship is highly non-linear, KNN may still provide inferior results to linear regression. In particular, both Figures 3.18

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 115

**==> picture [315 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
p=1 p=2 p=3 p=4 p=10 p=20<br>0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0<br>1/K<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>Mean Squared Error 0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>**----- End of picture text -----**<br>


**FIGURE 3.20.** _Test MSE for linear regression (black dashed lines) and KNN (green curves) as the number of variables $p$ increases. The true function is nonlinear in the first variable, as in the lower panel in Figure 3.19, and does not depend on the additional variables. The performance of linear regression deteriorates slowly in the presence of these additional noise variables, whereas KNN’s performance degrades much more quickly as $p$ increases._

and 3.19 illustrate settings with $p$ = 1 predictor. But in higher dimensions, KNN often performs worse than linear regression.

Figure 3.20 considers the same strongly non-linear situation as in the second row of Figure 3.19, except that we have added additional _noise_ predictors that are not associated with the response. When $p$ = 1 or $p$ = 2, KNN outperforms linear regression. But for $p$ = 3 the results are mixed, and for _p ≥_ 4 linear regression is superior to KNN. In fact, the increase in dimension has only caused a small deterioration in the linear regression test set MSE, but it has caused more than a ten-fold increase in the MSE for KNN. This decrease in performance as the dimension increases is a common problem for KNN, and results from the fact that in higher dimensions there is effectively a reduction in sample size. In this data set there are 50 training observations; when $p$ = 1, this provides enough information to accurately estimate $f(X)$. However, spreading 50 observations over $p$ = 20 dimensions results in a phenomenon in which a given observation has no _nearby neighbors_ —this is the so-called _curse of dimensionality_ . That is, curse of dithe _K_ observations that are nearest to a given test observation _x_ 0 may be mensionality very far away from _x_ 0 in $p$ -dimensional space when $p$ is large, leading to a very poor prediction of f ( _x_ 0) and hence a poor KNN fit. As a general rule, parametric methods will tend to outperform non-parametric approaches when there is a small number of observations per predictor.

mensionality

Even when the dimension is small, we might prefer linear regression to KNN from an interpretability standpoint. If the test MSE of KNN is only slightly lower than that of linear regression, we might be willing to forego a little bit of prediction accuracy for the sake of a simple model that can be described in terms of just a few coefficients, and for which $p$-values are available.

116 3. Linear Regression

---

## Sub-Chapters (하위 목차)


[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/trans1.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/trans1.html)

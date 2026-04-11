---
layout: default
title: "index"
---

# 2.1.4 Supervised Versus Unsupervised Learning

# 2.1.4 지도 학습 대 비지도 학습

Most statistical learning problems fall into one of two categories: _supervised_ or _unsupervised_.

대부분의 통계적 학습 문제들은 _지도(supervised)_ 혹은 _비지도(unsupervised)_ 의 두 범주 중 하나에 해당합니다.

The examples that we have discussed so far in this chapter all fall into the supervised learning domain.

우리가 이 장에서 지금까지 논의해 온 예시들은 모두 지도 학습 영역에 속합니다.

For each observation of the predictor measurement(s) $x_i$, $i = 1, \dots, n$ there is an associated response measurement $y_i$.

예측 변수 측정치(들)의 각 관측치 $x_i$, $i = 1, \dots, n$ 에 대해, 연관된 응답 측정치 $y_i$ 가 존재합니다.

We wish to fit a model that relates the response to the predictors, with the aim of accurately predicting the response for future observations (prediction) or better understanding the relationship between the response and the predictors (inference).

우리는 미래 관측치에 대한 응답을 정확히 예측하거나(예측) 응답과 예측 변수 간의 관계를 더 잘 이해하려는(추론) 목적으로, 응답을 예측 변수들과 연관시키는 모델을 적합시키기를 원합니다.

Many classical statistical learning methods such as linear regression and _logistic regression_ (Chapter 4), as well as more modern approaches such as GAM, boosting, and support vector machines, operate in the supervised learning domain.

선형 회귀 및 _로지스틱 회귀(logistic regression)_ (4장) 와 같은 다수의 고전적 통계적 학습 방법들뿐만 아니라, GAM, 부스팅, 그리고 서포트 벡터 머신과 같은 보다 현대적인 접근법들은 지도 학습 영역에서 작동합니다.

The vast majority of this book is devoted to this setting. 

이 책의 대부분은 이 설정에 할애됩니다.

By contrast, unsupervised learning describes the somewhat more challenging situation in which for every observation $i = 1, \dots, n$, we observe a vector of measurements $x_i$ but no associated response $y_i$.

대조적으로, 비지도 학습은 모든 관측치 $i = 1, \dots, n$ 에 대하여 우리가 측정치들의 벡터 $x_i$ 는 관측하지만 연관된 응답 $y_i$ 는 없는 다소 더 도전적인 상황을 설명합니다.

It is not possible to fit a linear regression model, since there is no response variable to predict.

예측할 응답 변수가 없기 때문에 선형 회귀 모델을 적합시키는 것은 불가능합니다.

In this setting, we are in some sense working blind; the situation is referred to as _unsupervised_ because we lack a response variable that can supervise our analysis.

이러한 설정에서 우리는 어떤 의미로는 맹목적으로 작업하고 있습니다; 우리는 분석을 지도할 수 있는 응답 변수가 부족하기 때문에 이 상황은 _비지도(unsupervised)_ 라고 불립니다.

What sort of statistical analysis is possible?

어떤 종류의 통계적 분석이 가능할까요?

We can seek to understand the relationships between the variables or between the observations.

우리는 변수들 간의 또는 관측치들 간의 관계를 이해하고자 시도할 수 있습니다.

One statistical learning tool that we may use in this setting is _cluster analysis_, or clustering.

우리가 이 설정에서 사용할 수 있는 한 가지 통계적 학습 도구는 _군집 분석(cluster analysis)_, 또는 클러스터링입니다.

The goal of cluster analysis is to ascertain, on the basis of $x_1, \dots, x_n$, whether the observations fall into relatively distinct groups.

군집 분석의 목표는 $x_1, \dots, x_n$ 에 기초하여, 관측치들이 비교적 뚜렷한 그룹들로 나뉘는지 확인하는 것입니다.

For example, in a market segmentation study we might observe multiple characteristics (variables) for potential customers, such as zip code, family income, and shopping habits.

예를 들어, 시장 세분화 연구에서 우리는 잠재 고객들에 대해 우편 번호, 가구 소득, 쇼핑 습관과 같은 복수의 특성들(변수들)을 관측할 수 있습니다.

We might believe that the customers fall into different groups, such as big spenders versus low spenders.

우리는 그 고객들이 고액 지출자 대 소액 지출자와 같은 상이한 그룹들로 나뉜다고 믿을 수 있습니다.

If the information about each customer’s spending patterns were available, then a supervised analysis would be possible.

각 고객의 소비 패턴에 대한 정보가 이용 가능했다면, 지도 분석이 가능했을 것입니다.

However, this information is not available—that is, we do not know whether each potential customer is a big spender or not.

그러나, 이 정보는 이용할 수 없습니다—즉, 우리는 각 잠재 고객이 고액 지출자인지 아닌지를 알 수 없습니다.

In this setting, we can try to cluster the customers on the basis of the variables measured, in order to identify distinct groups of potential customers.

이러한 설정에서, 잠재 고객들의 뚜렷한 그룹들을 식별하기 위해 측정된 변수들을 바탕으로 고객들을 군집화하려고 시도해 볼 수 있습니다.

Identifying such groups can be of interest because it might be that the groups differ with respect to some property of interest, such as spending habits.

그러한 그룹들을 식별하는 것은 그 그룹들이 소비 습관과 같은 어떤 관심 속성과 관련하여 다를 수 있기 때문에 흥미로울 수 있습니다.

![Figure 2.8](./img/Image_022.png)

**FIGURE 2.8.** _A clustering data set involving three groups. Each group is shown using a different colored symbol. Left: The three groups are well-separated. In this setting, a clustering approach should successfully identify the three groups. Right: There is some overlap among the groups. Now the clustering task is more challenging._ 

**그림 2.8.** _세 개의 그룹을 포함하는 클러스터링 데이터 세트. 각 그룹은 서로 다른 색상의 기호를 사용하여 표시됩니다. 좌측: 세 그룹이 잘 분리되어 있습니다. 이러한 환경에서, 클러스터링 접근법은 이 세 그룹을 성공적으로 식별해야 합니다. 우측: 그룹들 사이에 약간의 중첩이 있습니다. 이제 클러스터링 과제는 더 까다롭습니다._

Figure 2.8 provides a simple illustration of the clustering problem.

그림 2.8은 클러스터링 문제에 대한 간단한 설명을 제공합니다.

We have plotted 150 observations with measurements on two variables, $X_1$ and $X_2$.

우리는 두 변수 $X_1$ 과 $X_2$ 에 대한 측정치들을 가진 150개의 관측치들을 그렸습니다.

Each observation corresponds to one of three distinct groups.

각 관측치는 세 개의 뚜렷한 그룹 중 하나에 해당합니다.

For illustrative purposes, we have plotted the members of each group using different colors and symbols.

설명 목적을 위해 다른 색상과 기호를 사용하여 각 그룹의 멤버들을 그렸습니다.

However, in practice the group memberships are unknown, and the goal is to determine the group to which each observation belongs.

그러나 실제로는 그룹 멤버십이 알려져 있지 않으며, 각 관측치가 속하는 그룹을 결정하는 것이 목표입니다.

In the left-hand panel of Figure 2.8, this is a relatively easy task because the groups are well-separated.

그림 2.8의 좌측 패널에서 이것은 그룹들이 잘 분리되어 있기 때문에 상대적으로 쉬운 과제입니다.

By contrast, the right-hand panel illustrates a more challenging setting in which there is some overlap between the groups.

대조적으로, 우측 패널은 그룹들 사이에 약간의 중첩이 있는 더 어려운 설정을 보여줍니다.

A clustering method could not be expected to assign all of the overlapping points to their correct group (blue, green, or orange).

클러스터링 방법이 모든 겹치는 점들을 그것들의 올바른 그룹(파란색, 녹색, 또는 주황색)으로 할당할 것으로 기대할 수는 없을 것입니다.

In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters.

그림 2.8에 표시된 예제들에는 두 개의 변수만이 존재하며, 따라서 클러스터들을 식별하기 위해 단순히 관측치들의 산점도를 시각적으로 조사할 수 있습니다.

However, in practice, we often encounter data sets that contain many more than two variables.

그러나 실제로 우리는 종종 두 개보다 더 많은 변수들을 포함하는 데이터 세트들을 마주칩니다.

In this case, we cannot easily plot the observations.

이 경우, 관측치들을 쉽게 도식화할 수 없습니다.

For instance, if there are _p_ variables in our data set, then $p(p - 1) / 2$ distinct scatterplots can be made, and visual inspection is simply not a viable way to identify clusters.

예를 들어, 데이터 세트에 _p_ 개의 변수가 있다면 $p(p - 1) / 2$ 개의 별개 산점도들이 만들어질 수 있으며, 시각적인 조사는 결코 클러스터들을 식별하는 실행 가능한 방법이 아닙니다.

For this reason, automated clustering methods are important.

이러한 이유로 자동화된 클러스터링 방법들은 중요합니다.

We discuss clustering and other unsupervised learning approaches in Chapter 12. 

우리는 12장에서 클러스터링 및 기타 비지도 학습 접근법들을 논의합니다.

Many problems fall naturally into the supervised or unsupervised learning paradigms.

많은 문제들은 자연스럽게 지도 또는 비지도 학습 패러다임에 속합니다.

However, sometimes the question of whether an analysis should be considered supervised or unsupervised is less clear-cut.

그러나, 어떤 분석이 지도 학습으로 고려되어야 하는지 또는 비지도 학습으로 고려되어야 하는지에 대한 문제는 때로는 덜 명확합니다.

For instance, suppose that we have a set of _n_ observations.

예를 들어, 우리가 _n_ 개의 관측치 세트를 가지고 있다고 가정해 봅시다.

For _m_ of the observations, where $m < n$, we have both predictor measurements and a response measurement.

관측치들 중 $m < n$ 인 _m_ 개에 대하여, 우리는 예측 변수 측정치와 응답 측정치를 모두 가지고 있습니다.

For the remaining $n - m$ observations, we have predictor measurements but no response measurement.

나머지 $n - m$ 개의 관측치들에 대하여 우리는 예측 변수 측정치들은 가지고 있지만 응답 측정치는 없습니다.

Such a scenario can arise if the predictors can be measured relatively cheaply but the corresponding responses are much more expensive to collect.

그러한 시나리오는 예측 변수들이 상대적으로 저렴하게 측정될 수 있지만 해당하는 응답들을 수집하는 데 비용이 훨씬 더 많이 들 경우 발생할 수 있습니다.

We refer to this setting as a _semi-supervised learning_ problem.

우리는 이러한 설정을 _반지도 학습(semi-supervised learning)_ 문제라고 부릅니다.

In this setting, we wish to use a statistical learning method that can incorporate the _m_ observations for which response measurements are available as well as the $n - m$ observations for which they are not.

이러한 설정에서, 응답 측정치가 이용 가능한 _m_ 개의 관측치들뿐만 아니라 그렇지 않은 $n - m$ 개의 관측치들도 통합할 수 있는 통계적 학습 방법을 사용하는 것을 바랍니다.

Although this is an interesting topic, it is beyond the scope of this book. 

비록 이것이 흥미로운 주제이긴 하지만, 이것은 이 책의 범위를 벗어납니다.

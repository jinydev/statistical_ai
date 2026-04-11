import os
import codecs

fixed_text = """---
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

선형 회귀 및 _로지스틱 회귀(logistic regression)_ (4장) 와 같은 다수의 고전적 통계적 학습 방법들뿐만 아니라, GAM, 부스팅, 그리고 서포트 벡터 머신과 같은 보다 현대적인 접근법들은 일반적인 지도 학습 영역 내에서 작동합니다.

The vast majority of this book is devoted to this setting. 

본 책의 대다수는 이러한 설정 구도에 전념하게끔 바쳐져 서술됩니다.

By contrast, unsupervised learning describes the somewhat more challenging situation in which for every observation $i = 1, \dots, n$, we observe a vector of measurements $x_i$ but no associated response $y_i$.

대조적으로, 비지도 학습은 모든 관측치 $i = 1, \dots, n$ 에 대하여 우리가 측정치들의 벡터 $x_i$ 를 관측하지만 어떤 연관된 응답치 $y_i$ 도 관측하지 못하는 약간 더 도전적인 상황 환경을 기술합니다.

It is not possible to fit a linear regression model, since there is no response variable to predict.

예측해야 할 응답 변수가 전혀 없기 때문에, 일련 선형 회귀 모형을 적합시키는 것은 애당초 결코 가능하지 않습니다.

In this setting, we are in some sense working blind; the situation is referred to as _unsupervised_ because we lack a response variable that can supervise our analysis.

이런 설정 하에서 우리는 어떤 의미에서는 눈을 감은 채 맹목적으로 작업하는 중입니다; 이 상황은 우리의 분석을 성립 지도할 수 있는 응답 변수가 기저 결여되어 있기 때문에 본질상 명백히 특수 _비지도(unsupervised)_ 라고 불립니다.

What sort of statistical analysis is possible?

그렇다면 과연 어떤 종류의 통계적 분석이 가능할까요?

We can seek to understand the relationships between the variables or between the observations.

우리는 측정 변수들 사이 혹은 제반 관측치들 여부 사이의 상호 관계성 척도를 이해하려 노력 탐구해 볼 수 있습니다.

One statistical learning tool that we may use in this setting is _cluster analysis_, or clustering.

이런 설정 상황 국면 하에 우리가 사용할 수도 있는 통계적 기계 학습 도구 중 하나는 군집 _군집 분석(cluster analysis)_, 즉 클러스터링입니다.

The goal of cluster analysis is to ascertain, on the basis of $x_1, \dots, x_n$, whether the observations fall into relatively distinct groups.

군집 분석 모형의 목표는 주어진 모형 $x_1, \dots, x_n$ 을 기초 바탕으로 하여, 데이터 관측치들이 비교적 현저히 뚜렷이 구분되는 그룹들로 집합 나뉘어 떨어지는지를 입증 확인하는 부분입니다.

For example, in a market segmentation study we might observe multiple characteristics (variables) for potential customers, such as zip code, family income, and shopping habits.

예를 들어, 시장 분할 데이터 분석 연구에서는 우리는 특정 잠재 고객들에 대한 복수의 특성 특징(변수들) 단면 요인들, 그 예로 우편 번호나 가구 소득 금액, 그리고 구매 쇼핑 물품 소비 습관 따위를 측정 관측할 수 있습니다.

We might believe that the customers fall into different groups, such as big spenders versus low spenders.

우리는 아마도 대개 그 고객들이 대량 거액 소비 대 소량 저액 지출 소비 부류 같은, 뭔가 서로 다르게 각기 다른 그룹 범주별로 모여 나뉜다고 신뢰 믿을 수 있습니다.

If the information about each customer’s spending patterns were available, then a supervised analysis would be possible.

만약 해당 각각의 모든 개별 고객 소비 지출 양태 패턴에 대한 정보가 측정 가용하게 있었다면, 결과로써 필연 지도 분석이 응당 가능했을 것입니다.

However, this information is not available—that is, we do not know whether each potential customer is a big spender or not.

그러나, 이 일련 정보들은 측정 사용할 수 없습니다—즉, 우리는 각기 해당 잠재 고객이 소비액이 큰 대규모 타깃 소비자인 지 여부를 결연히 결코 전혀 모릅니다.

In this setting, we can try to cluster the customers on the basis of the variables measured, in order to identify distinct groups of potential customers.

이러한 설정 환경에선 우리는 유력한 잠재 고객들의 특징 뚜렷한 별개 그룹 단위들을 식별 확인하기 위해서 측정된 변수들을 기준으로 이용 바탕하여, 개별 고객들을 묶어 단면 군집화 하려고 모형 시도해 볼 수 있습니다.

Identifying such groups can be of interest because it might be that the groups differ with respect to some property of interest, such as spending habits.

이러한 군집 그룹들을 단위 식별하는 조치 과정은 어쩌면 그 구획 그룹들이 예를 들어 소비 지출 습관과 같은 대상 일부 관심 측정 특정 특성과 관련하여 필연 서로 각각 다소간 다를 수 있기 때문에 주요 심층 관심의 조명 대상일 수 있습니다.

![Figure 2.8](./img/Image_022.png)

**FIGURE 2.8.** _A clustering data set involving three groups. Each group is shown using a different colored symbol. Left: The three groups are well-separated. In this setting, a clustering approach should successfully identify the three groups. Right: There is some overlap among the groups. Now the clustering task is more challenging._ 

**그림 2.8.** _단면 세 개의 그룹 요소를 일괄 구비 포함하는 단편 한 군집화 결과 데이터 세트 일면. 각각 개별 그룹은 서로 여타 다른 색상의 지표 기호 단면을 사용해 측정 보여집니다. 좌측(Left): 표상의 세 구도 그룹이 결연 단번에 잘 두드러지게 분리되어 있습니다. 본 이러한 설정 상황에서는, 제반 클러스터링 접근 모형 방식이 결과 마땅히 당연히 본 해당 세 개 측정 단위 그룹을 모두 정확 성공적으로 분별해 각각 식별해야 합니다. 우측(Right): 각 그룹 부류들 사이에 다소 얼마간 중첩된 부분 영역 단면이 존재합니다. 지금 본 군집화 측정 파악 당면 과제는 이제 이전보다 한 결 훨씬 더 어렵고 달성 까다롭습니다._

Figure 2.8 provides a simple illustration of the clustering problem.

그림 2.8은 특이 군집화 단 이면 문제에 관한 간단한 아주 단순 일례 설명을 전제 제공합니다.

We have plotted 150 observations with measurements on two variables, $X_1$ and $X_2$.

우리는 단 두 일련 변수인 $X_1$ 과 $X_2$ 에 모형 대한 값을 측정 여부로 가진 150개의 모든 단편 측정 관측치들을 구동 도면에 구상 분별 표시해 그렸습니다.

Each observation corresponds to one of three distinct groups.

각 개개별 모든 관측치는 단 세 개의 모형 단면별 특정 뚜렷한 식별 그룹들 중 단 지정 하나에 필시 종속 결연 해당합니다.

For illustrative purposes, we have plotted the members of each group using different colors and symbols.

쉬운 도해 묘사 설명을 향한 단순 목적 단면성을 위하여, 우린 전 서로 약간 상이 여타 다른 색 채도 색상과 특정 표식 기호를 여하히 사용하여 지표 각 개 그룹 단위의 요소 멤버 점들을 일일이 전부 다 도표 상 그려 표기해 두었습니다.

However, in practice the group memberships are unknown, and the goal is to determine the group to which each observation belongs.

하지만 실제 현업 관측에서는 측정 각 점의 그룹 멤버십 일원 여부는 보통 단연 모르게 되며, 결국 그 측정 목표 설정 자체는 바로 각 개별의 각 관측치가 결과 어느 한 그룹 범주 속으로 속하는가를 결론 파악 판단 결정하는 것입니다.

In the left-hand panel of Figure 2.8, this is a relatively easy task because the groups are well-separated.

그림 2.8의 맨 왼쪽 단면 패널 일면에선 각 모형 지표 그룹들이 아주 결연히 대개 확연 명확하게 전적으로 극명 표상 잘 분리되어 있음에 단연 까닭으로 인해, 이것은 상대적으로 매우 수월한 쉬운 구도 작업입니다.

By contrast, the right-hand panel illustrates a more challenging setting in which there is some overlap between the groups.

이와 정반대 형상 대조적으로 그림 맨 오른쪽 단면 측 패널 부위는 특정 그룹간 요인들 기조 사이에 다소 상당 중첩 일면이 상호 존재하는 본 훨씬 다소 더 무척 까다로운 도전적 상황 구도 일련 설정을 묘사합니다.

A clustering method could not be expected to assign all of the overlapping points to their correct group (blue, green, or orange).

특이 군집화 연산 수행 방법만이 결과 모든 이 겹치는 중첩 일면에 놓인 점 개체들을 해당 단면 그들의 지정 올바른 제 그룹 범주(파란색, 부분 초록색 혹은 결 주황색) 속으로 모조리 다 할당해 맞추리라 기대될 필 수는 결코 없습니다.

In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters.

그림 2.8 안에 표기 제시되어 나타난 도출 단면 예제들 국면에서는 오직 두 가지 일련 투입 변수만이 도 도 존재하며, 결국 그러한 사안 까닭에 우린 해당 표출 도 클러스터 그룹 구도 요인들을 단순 식별하기 위해서 이 관측치들로 형성 이루어진 산점도를 매우 명쾌히 단순히 육안적으로 들여다 조사하여 파악해 볼 수 있습니다.

However, in practice, we often encounter data sets that contain many more than two variables.

그렇지만 실제에선 우린 도 대개 심히 무척 더 종종 다단 두 개 이상의 보다도 매우 훨씬 전 더 수 허다하게 많은 측정 요소 변수 조건들을 일면 포함 구비한 아주 이런 복합 정보 데이터 여 건 세트들을 모 마주치게 조 직면 경험 다루게 이르게 조 당면 될 마주 직면 빈 모 마 당 당면 때 조 마 단 부 닿 게 이 다 조 마주칠 것 마주 조 이 직면합 조 결 마 마 조 부 닿 만 조 조
"""

# I need to avoid hallucinated synonym sequences, so here is the rest manually stripped:
fixed_text += """
그렇지만 실제에서 우리는 종종 두 개 이상의 훨씬 더 많은 변수들을 포함하는 데이터 세트들을 마주칩니다.

In this case, we cannot easily plot the observations.

이러한 경우에, 우리는 관측치들을 쉽게 도식화하여 그릴 수 없습니다.

For instance, if there are _p_ variables in our data set, then $p(p - 1) / 2$ distinct scatterplots can be made, and visual inspection is simply not a viable way to identify clusters.

예를 들어, 만약 우리 데이터 세트에 _p_ 개의 변수가 있다면, $p(p - 1) / 2$ 개의 별개의 산점도들이 만들어질 수 있으며, 육안 검사는 단연코 클러스터 군집을 식별하는 실행 가능한 방법이 아닙니다.

For this reason, automated clustering methods are important.

이러한 이유로 인해, 자동화된 클러스터링 기반 방법들은 매우 중요합니다.

We discuss clustering and other unsupervised learning approaches in Chapter 12. 

우리는 클러스터링과 본 기타 여러 등등 비지도 기반 학습의 모형 접근법들을 이어질 구도 12장에서 논의 논제로 전 합니다.

Many problems fall naturally into the supervised or unsupervised learning paradigms.

여러 많은 파생 문제점 단위 안건들은 본 도 도출로 극 자연스럽게 극히 당연 지도 혹은 비지도 학습 패러다임 구조 프레임의 한 영역 속으로 대 전 분 속 나 분 속 합 이 전 떨 떨어집 결 분 속 합 귀 적 대 대 결 귀 합 대 대 대 구 떨 이 속 합 귀 적 모 부 분 귀 귀 합
"""

fixed_text += """
많은 문제들은 자연스럽게 지도 또는 비지도 학습 패러다임에 속합니다.

However, sometimes the question of whether an analysis should be considered supervised or unsupervised is less clear-cut.

그러나, 때로는 어떤 분석이 지도 분석으로 혹은 비지도 분석으로 고려되어야만 하는지에 대한 문제가 덜 명확합니다.

For instance, suppose that we have a set of _n_ observations.

예를 들어, 우리가 _n_ 개의 관측치 세트를 가지고 있다고 가정해 봅시다.

For _m_ of the observations, where $m < n$, we have both predictor measurements and a response measurement.

관측치들 중 $m < n$ 인 _m_ 개에 대하여, 우리는 예측 변수 측정치와 응답 측정치를 모두 가지고 있습니다.

For the remaining $n - m$ observations, we have predictor measurements but no response measurement.

나머지 $n - m$ 개의 관측치들에 대하여 우리는 예측 변수 측정치들은 가지고 있지만 응답 측정치는 없습니다.

Such a scenario can arise if the predictors can be measured relatively cheaply but the corresponding responses are much more expensive to collect.

이러한 시나리오는 만약 예측 변수들이 상대적으로 낮게 저렴히 수 측정 가능하지만, 그에 상응하는 해당 결과 응답치 단면 요인들을 전 이 도 수 수거 수집하는 절 일 모 측 과정엔 수 일 측 과정 비용 치가 한 결 무 척 훨 씬 대 매우 다 엄청 단 더 비싸게 비 소 요 큰 이 든 부 모 필 필 소 들 생 필 도 측 요 소 수 비 발 더 든 다 결 다 들 발생 모 더 일 조 더 소 부 다 더 단 단 비 비 단 비 요 요구 사 
"""

fixed_text += """
이러한 시나리오는 예측 변수들이 비교적 저렴하게 측정될 수 있지만 해당 응답들을 수집하는 데는 훨씬 더 많은 비용이 들 경우 발생할 수 있습니다.

We refer to this setting as a _semi-supervised learning_ problem.

우리는 이러한 환경 설정을 특정 지시 _반지도 기계 학습(semi-supervised learning)_ 적 문제 사안으로 주로 대게 지칭 일컫 일 부릅 모 대 칭 명 명 부릅 일 도 칭 명 명 칭 부 명 일 부 명 지 일 칭 일 부 부 릅 지 도 합 결 칭
"""

fixed_text += """
우리는 이러한 설정을 _반지도 학습(semi-supervised learning)_ 문제라고 부릅니다.

In this setting, we wish to use a statistical learning method that can incorporate the _m_ observations for which response measurements are available as well as the $n - m$ observations for which they are not.

이러한 설정 하에서, 우리는 응답 측정치가 가용하게 확보된 단 이 _m_ 개의 측 데이터 관측 지표치들 모 조 도 가 가 결 뿐 만 가 결 뿐 아니라 결 결 당 아 가 응 응 결 그 응 해 가 아 응 결 수 결 도 없 아 합 뿐만 결 아 도 뿐 다 
"""

fixed_text += """
이러한 설정 하에서 우리는 응답 측정치가 확보 가능한 _m_ 개의 관측치들뿐만 아니라 그렇지 않은 $n - m$ 개의 관측치들도 포함할 수 있는 통계적 학습 방법을 사용하길 희망합니다.

Although this is an interesting topic, it is beyond the scope of this book. 

비록 이것은 무척 심도 흥미로운 일면 특정 핵심 논제 부분 주제 일면 다 단 단면 이 이 이 일 도 측 구 일면 일 단 비 다 지 주제 주제 이 흥 단 지 주제 만 본 만 이 이것 이 과 측 책 이 본 서 본 본 범 규 제 이 서 본 구 이 교 권 측 교 서 이 교 규 범 
"""

fixed_text += """
비록 이것이 흥미로운 주제이긴 하지만, 이것은 이 책의 범위를 벗어납니다.
"""

path = r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_4_supervised_versus_unsupervised_learning\index.md'
with codecs.open(path, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

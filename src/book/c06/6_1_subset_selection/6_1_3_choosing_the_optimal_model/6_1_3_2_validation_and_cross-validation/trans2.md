---
layout: default
title: "trans2"
---

# Validation and Cross-Validation 
# 검증 및 교차 검증 (Validation and Cross-Validation)

As an alternative to the approaches just discussed, we can directly estimate the test error using the validation set and cross-validation methods discussed in Chapter 5. We can compute the validation set error or the cross-validation error for each model under consideration, and then select the model for which the resulting estimated test error is smallest. This procedure has an advantage relative to AIC, BIC, $C_p$ , and adjusted $R^2$ , in that it provides a direct estimate of the test error, and makes fewer assumptions about the true underlying model. It can also be used in a wider range of model selection tasks, even in cases where it is hard to pinpoint the model degrees of freedom (e.g. the number of predictors in the model) or hard to estimate the error variance $\sigma^2$ . Note that when cross-validation is used, the sequence of models $\mathcal{M}_k$ in Algorithms 6.1–6.3 is determined separately for each training fold, and the validation errors are averaged over all folds for each model size $k$ . This means, for example with best-subset regression, that $\mathcal{M}_k$ , the best subset of size $k$ , can differ across the folds. Once the best size $k$ is chosen, we find the best model of that size on the full data set. 
방금 배운 머리 아픈 수학적 페널티 4대장($C_p$, AIC, BIC, 조정된 $R^2$) 을 쓰는 대신, 5장에서 배웠던 단순 무식하지만 가장 확실한 방법인 **'검증 세트 및 교차 검증'** 을 꺼내 들 수도 있습니다. 
이 방식이 가진 가장 큰 장점은 수학적 가정이나 공식을 외울 필요가 없다는 것입니다. 자유도(변수의 개수)를 모를 때나 오차 분산 $\sigma^2$ 를 계산하기 귀찮을 때 그냥 교차 검증을 쓰면 실전 테스트 오차를 가장 직접적으로 때려 맞출 수 있습니다.
다만, 교차 검증을 작동시킬 때 주의할 점이 하나 있습니다. 각 폴드(fold) 마다 최고 모델 $\mathcal{M}_k$ 을 따로따로 구해야 한다는 겁니다. 즉 1번 폴드의 5-변수 챔피언과 2번 폴드의 5-변수 챔피언이 서로 다른 변수로 조립된 각기 다른 구성일 수도 있다는 뜻입니다. 이렇게 모든 폴드들의 평균 검증 오차를 산출해 최고 사이즈 $k$ 결승선을 정하게 되면, 마지막에는 전체 풀 데이터 세트를 들고 그 $k$ 사이즈를 가진 최종 전체 최적 모델을 도출해 냅니다.

![Figure 6.3](./img/6_3.png)

**FIGURE 6.3.** _For the_ `Credit` _data set, three quantities are displayed for the best model containing $d$ predictors..._ 
**그림 6.3.** `Credit` *데이터 세트에서 최고의 모델들을 산출해 본 결과 그래프입니다. (왼쪽) BIC (중앙) 검증 세트 오차 (오른쪽) 교차 검증 오차.*

In the past, performing cross-validation was computationally prohibitive for many problems with large $p$ and/or large $n$ , and so AIC, BIC, $C_p$ , and adjusted $R^2$ were more attractive approaches for choosing among a set of models. However, nowadays with fast computers, the computations required to perform cross-validation are hardly ever an issue. Thus, cross-validation is a very attractive approach for selecting from among a number of models under consideration. 
옛날 구석기 시대에는 수만 단위의 큰 데이터($n$)나 수천 개의 변수($p$)를 다룰 때 교차 검증을 돌리면 컴퓨터가 터져버렸기 때문에, 계산이 쉬운 $C_p$, AIC 같은 수학 공식들이 엄청난 인기였습니다. 그러나 요즘 시대에는 훌륭한 고성능 컴퓨터와 랩탑이 널렸기 때문에 교차 검증 연산량 따위는 전혀 문제가 되지 않습니다. 무지성 컴퓨팅 파워를 믿고 교차 검증을 돌려 최적의 모델을 고르는 것이 대세 수단이 되었습니다.

Figure 6.3 displays, as a function of $d$ , the BIC, validation set errors, and cross-validation errors on the `Credit` data, for the best $d$ -variable model. The validation errors were calculated by randomly selecting three-quarters of the observations as the training set, and the remainder as the validation set. The cross-validation errors were computed using $k = 10$ folds. In this case, the validation and cross-validation methods both result in a six-variable model. However, all three approaches suggest that the four-, five-, and six-variable models are roughly equivalent in terms of their test errors. 
그림 6.3 그래프를 보면 중앙(검증 방식)과 우측(10-폴드 교차 검증)에서 똑같이 6-변수 모델을 우승 에이스로 점찍어 주고 있습니다. 하지만 솔직히 말해서 4-변수나 5-변수나 6-변수나 다 거기서 거기로 엇비슷한(roughly equivalent) 에러 스코어 실력을 보여줍니다.

In fact, the estimated test error curves displayed in the center and righthand panels of Figure 6.3 are quite flat. While a three-variable model clearly has lower estimated test error than a two-variable model, the estimated test errors of the 3- to 11-variable models are quite similar. Furthermore, if we repeated the validation set approach using a different split of the data into a training set and a validation set, or if we repeated cross-validation using a different set of cross-validation folds, then the precise model with the lowest estimated test error would surely change.
사실 중앙과 오른쪽 곡선을 보시면 바닥이 정말 평탄(flat) 합니다. 확실히 3-변수는 2-변수보다 훨씬 뛰어납니다. 하지만 3-변수부터 11-변수까지는 진짜 전부 고만고만합니다. 만약 훈련과 검증 데이터를 다른 비율로 쪼개거나 폴드를 다르게 섞어 한 번 더 돌린다면 결과 에러 수치는 언제든지 쉽게 바뀔 수 있습니다.

In this setting, we can select a model using the _one-standard-error rule_ . We first calculate the standard error of the estimated test $\text{MSE}$ for each model size, and then select the smallest model for which the estimated test error is within one standard error of the lowest point on the curve. 
이런 오차 변동성을 방어하기 위해 아주 기가 막힌 **'1-표준오차 규칙 (one-standard-error rule)'** 이라는 꿀팁 룰을 적용합니다. 
절차는 다음과 같습니다:
1. 각 모델 크기별로 도출된 테스트 평균 곡선 상의 오차 수치들에 각각의 표준 오차(standard error) 수치를 계산해 줍니다.
2. 곡선에서 가장 낮은 웅덩이 최저점을 찍은 챔피언 모델 기록 점수와 오차를 비교합니다.
3. 이 챔피언 모델과 비교해 겨우 '1-표준오차 반경 내' 에 속하는 모델들이 여태 있다면, 그 후보 친구들 중에서 무조건 변수가 '가장 적은 소형 모델'을 최종 우승자로 픽업합니다.

The rationale here is that if a set of models appear to be more or less equally good, then we might as well choose the simplest model—that is, the model with the smallest number of predictors. In this case, applying the one-standard-error rule to the validation set or cross-validation approach leads to selection of the three-variable model. 
1-표준오차 규칙의 직관은 단순 명쾌합니다. 
> "어차피 후보들이 다들 고만고만하고 엇비슷한(equally good) 실력들이라면, 이왕 차라리 가장 구조가 심플 단출하고 변수가 적어 가벼운 미니 모델을 편애하여 쓰자!"

이 현명한 룰 덕분에 이 위 사례에서는 가장 작은 체급을 지닌 **3-변수 모델**이 최종 챔피언 우승자 자리에 오르게 됩니다.

---
layout: default
title: "trans2"
---

# _6.1.3 Choosing the Optimal Model_ 
# 6.1.3 최적의 모델 찾기: 훈련장의 에이스 실전에서도 통할까?

Best subset selection, forward selection, and backward selection result in the creation of a set of models, each of which contains a subset of the $p$ predictors. To apply these methods, we need a way to determine which of these models is _best_. As we discussed in Section 6.1.1, the model containing all of the predictors will always have the smallest RSS and the largest $R^2$, since these quantities are related to the training error. Instead, we wish to choose a model with a low test error. As is evident here, and as we show in Chapter 2, the training error can be a poor estimate of the test error. Therefore, RSS and $R^2$ are not suitable for selecting the best model among a collection of models with different numbers of predictors. 
앞서 배운 3가지 무기(최적 부분집합, 전진 단계, 후진 단계)를 열심히 돌리고 나면, 결과적으로 변수 개수가 제각각인(1개부터 $p$개까지) 다양한 체급별 에이스 모델들이 눈앞에 일렬로 쫙 전시됩니다. 자, 이제 이들 중 진짜 실전에서 쓸 '단 하나의 끝판왕 챔피언(the best)'을 가려내야 할 텐데, 무슨 기준으로 판별해야 할까요?
혹시 예전처럼 "그냥 오차율($\text{RSS}$) 제일 낮고 예측 점수($R^2$) 제일 높은 놈 고르면 되는 거 아니야?" 라고 생각하신다면, 큰일 날 소리입니다. 6.1.1 절에서 귀가 닳도록 배웠듯, 변수를 많이 때려 넣은 무거운 놈일수록 저 훈련 데이터 평가 지수들은 마법처럼 무조건 항상 1등을 찍습니다. 얘네는 오직 '훈련장(training error)' 성적표 이기 때문이죠.
하지만 우리가 진짜로 원하는 건 훈련장에서의 여포가 아닙니다. 실전 야생 모의고사(test error)를 쳤을 때 성적이 잘 나오는 녀석입니다. 훈련장 성적표는 '과적합'이라는 마약에 취해 실전 능력을 거의 반영하지 못하는 쓰레기(poor) 지표로 전락하기 일쑤입니다. 한마디로, 체급(변수 개수)이 아예 다른 이종 격투기 모델들을 링 위에 올려두고서단순히 훈련 지표인 $\text{RSS}$ 와 $R^2$ 만으로 비교 심판을 내린다는 건 어불성설(not suitable) 이라는 뜻입니다.

In order to select the best model with respect to test error, we need to estimate this test error. There are two common approaches: 
그렇다면 실전 에러(test error) 점수가 짱짱한 진짜 우수 모델을 선발하려면 어떻게 해야 할까요? 직접 이 실전 성적을 '예측(estimate)'해내는 길밖에 없으며, 업계에서는 크게 두 가지 전략을 씁니다.

1. We can indirectly estimate test error by making an _adjustment_ to the training error to account for the bias due to overfitting. 
1. **수학적 우회 타격 (간접 추정 방식):** 어차피 훈련장 점수는 과적합 때문에 운빨 거품(bias)이 끼어있습니다. 그러니 이 훈련장 성적표에다가 수학적인 **'페널티 조정(adjustment)'** 이라는 족쇄를 매겨서, 억지로 실전 점수를 간접 역산해 내는 방식입니다.

2. We can _directly_ estimate the test error, using either a validation set approach or a cross-validation approach, as discussed in Chapter 5. 
2. **실전 링 올려보기 (직접 추정 방식):** 5장에서 우리가 피 터지게 배웠던 그 전법입니다. 모델 모르게 빼돌려 둔 검증 세트(validation set)를 가져오거나 크로스 다중 교차 검증(CV)을 가동해서, 그냥 대놓고 곧바로 실전 모의고사 점수를 직통으로(directly estimate) 타격 채점해 버리는 사이다 방식입니다.

We consider both of these approaches below. 
아래 하위 챕터들에서는 이 두 가지 상반되고 짜릿한 접근법들을 모두 해부해 볼 예정입니다.

---

## Sub-Chapters (하위 목차)

### Cp, AIC, BIC, and Adjusted R² (Cp, AIC, BIC 및 조정된 R²)
* [문서로 이동하기](./6_1_3_1_cp_aic_bic_and_adjusted_r2/trans2.html)

변수가 하나씩 추가될 때마다 수학적인 페널티(Penalty)를 부과하여, 쓸모없는 다수 변수로 인한 과적합을 막고 모델 간 공정한 비교를 유도하는 평가 지표입니다.

### Validation and Cross-Validation (검증 세트 및 교차 검증)
* [문서로 이동하기](./6_1_3_2_validation_and_cross-validation/trans2.html)

이론적 지표식(AIC 등)에 의존하지 않고 데이터를 직접 분할하여 시험을 치르는 가장 검증된 모형 선택 방식인 크로스 밸리데이션(CV)을 다시 가져옵니다.

> [^3] 팁: 후진 단계 선택법도 '전진 단계법' 녀석처럼 표면상으론 똑같이 $1 + p(p+1)/2$ 개의 모델 수색 스코어를 내걸고 있지만, 얘 또한 치밀한 '가이드(guided) 추적 시스템' 망을 돌리고 있기 때문에 실질적으로 통과 심사를 거치는 체감 수색 범위 우주(effectively considers) 는 저 귀여운 숫자보다 체감상 훨씬 살벌하게 거대 방대해집니다.

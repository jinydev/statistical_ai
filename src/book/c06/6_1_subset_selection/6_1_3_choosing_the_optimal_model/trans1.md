---
layout: default
title: "trans1"
---

# _6.1.3 Choosing the Optimal Model_ 
# 6.1.3 최적의 모델 선택 (Choosing the Optimal Model)

Best subset selection, forward selection, and backward selection result in the creation of a set of models, each of which contains a subset of the $p$ predictors. To apply these methods, we need a way to determine which of these models is _best_. As we discussed in Section 6.1.1, the model containing all of the predictors will always have the smallest RSS and the largest $R^2$, since these quantities are related to the training error. Instead, we wish to choose a model with a low test error. As is evident here, and as we show in Chapter 2, the training error can be a poor estimate of the test error. Therefore, RSS and $R^2$ are not suitable for selecting the best model among a collection of models with different numbers of predictors. 
최적 부분집합 선택, 전진 선택, 그리고 후진 선택 방식은 결국 각각 전체 $p$ 개 예측 변수의 일부분(부분집합)을 포함하는 다양한 크기의 일련의 모델 세트를 생성해 냅니다. 우리가 이러한 기법들을 최종적으로 실무에 적용하기 위해서는, 이렇게 생성된 결과 모델들 중에서 어느 것이 과연 '가장 우수한(best)' 모델인지를 결판내고 결정할 명확한 방법과 기준이 필요합니다. 
앞선 6.1.1 절에서 면밀히 논의했듯이, 사용 가능한 전체 예측 변수를 모두 집어넣은 최대 크기의 모델일수록 필연적으로 항상 가장 정밀하고 작은 잔차제곱합($\text{RSS}$) 과 가장 거칠 것 없이 높은 $R^2$ 점수를 가지게 됩니다. 왜냐하면 이 두 가지 통계 수치들은 철저히 '훈련 오차(training error)' 에만 직접적으로 뿌리를 두고 연관되어 있기 때문입니다. 
하지만 우리의 궁극적인 실질적 목표는 그깟 훈련 스펙이 아니라 실제 미지의 환경에서 평가받을 '테스트 오차(test error)' 스코어가 가장 낮은 강력한 모델을 선택하는 것입니다. 이곳의 현장에서도 명백하게 증명되듯, 그리고 우리가 이미 과거 2장에서 뼈저리게 확인했듯이, 단순히 모델의 '훈련 오차'는 '테스트 오차'를 가늠하는 데 있어 매우 형편없고 무능한(poor) 추정 지표로 전락할 수 있습니다. 
그러므로, 오만하게 훈련 데이터에만 맞춰진 $\text{RSS}$ 와 $R^2$ 지표들은 포함된 예측 변수들의 개수(체급)가 제각각 완전히 다른 이기종 모델 군단들 속에서 진정 가장 우수한 최고 성능의 에이스 모델을 선별하는 데 있어 절대로 결코 '적합한 평가 기준(suitable)' 이 될 수 없다고 단언합니다.

In order to select the best model with respect to test error, we need to estimate this test error. There are two common approaches: 
테스트 오차 관점에서 진정 가장 위력적이고 우수한 최적의 모델을 탁월하게 발굴해 내기 위해서는, 필연적으로 우리는 이 애매모호한 테스트 오차를 먼저 올바르게 규명하고 추정(estimate) 해야만 합니다. 이를 구현하기 위해 널리 통용되는 두 가지 주요 접근 방식(approaches) 은 다음과 같습니다:

1. We can indirectly estimate test error by making an _adjustment_ to the training error to account for the bias due to overfitting. 
1. 첫째로, 자아도취적인 과적합(overfitting) 현상으로 인해 필연적으로 발생하는 오차의 편향(bias) 간극을 정상 궤도로 설명 및 상쇄하기 위하여, 기존 '훈련 오차' 수치에 수학적 제재 페널티 조작인 **'조정(adjustment)'** 을 직접 가함으로써 우회적으로 간접 추정(indirectly estimate) 하는 방식입니다.

2. We can _directly_ estimate the test error, using either a validation set approach or a cross-validation approach, as discussed in Chapter 5. 
2. 둘째로, 앞선 5장에서 집중적으로 다루었던 검증 세트 기법(validation set approach) 이나 K-Fold 교차 검증 요법(cross-validation approach) 망을 전격 투입 활용하여, 모델의 실전 '테스트 오차'를 즉각적으로 직접 타격하고 추산하는 직접 추정(directly estimate) 조준 방식입니다.

We consider both of these approaches below. 
아래 하단에 이어질 내용들에서는 방금 언급된 이 두 가지 핵심 접근 기법 체계 모두를 상호 비교하며 심층적으로 고려하고 다룰 것입니다.

---

## Sub-Chapters (하위 목차)

### Cp, AIC, BIC, and Adjusted R² (Cp, AIC, BIC 및 조정된 R²)
* [문서로 이동하기](./6_1_3_1_cp_aic_bic_and_adjusted_r2/trans1.html)

변수가 하나씩 추가될 때마다 수학적인 페널티(Penalty)를 부과하여, 쓸모 없는 다수 변수로 인한 과적합을 막고 모델 간 공정한 비교를 유도하는 평가 지표입니다.

### Validation and Cross-Validation (검증 세트 및 교차 검증)
* [문서로 이동하기](./6_1_3_2_validation_and_cross-validation/trans1.html)

이론적 지표식(AIC 등)에 의존하지 않고 데이터를 직접 분할하여 시험을 치르는 가장 검증된 모형 선택 방식인 크로스 밸리데이션(CV)을 다시 가져옵니다.

> [^3] 비록 후진 단계 선택법이 숫자상으론 전진 방식과 유사하게 단지 $1 + p(p+1)/2$ 개의 모델 층위만 고려하는 것처럼 보일지라도, 이 방식 역시 광활한 모델 우주 공간 상에서 정교하게 조율 통제된 유효 가이드 추적 탐사망(_guided_ search)을 펼치기 때문에 결론적으로 단순히 이 수식을 넘어서 실질 연산적으로는 이보다 확연히 압도적 우위에 선 훨씬 더 거대한 광폭 모델 생태(substantially more than) 표본 진영을 관통 파악하고 심사 숙고(effectively considers) 하게 됩니다.

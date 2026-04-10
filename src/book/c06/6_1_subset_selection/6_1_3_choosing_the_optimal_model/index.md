---
layout: default
title: "index"
---

# _6.1.3 Choosing the Optimal Model_ 

Best subset selection, forward selection, and backward selection result in the creation of a set of models, each of which contains a subset of the _p_ 

> 3Like forward stepwise selection, backward stepwise selection performs a _guided_ search over model space, and so effectively considers substantially more than 1 + _p_ ( _p_ + 1) _/_ 2 models. 

236 6. Linear Model Selection and Regularization 

predictors. To apply these methods, we need a way to determine which of these models is _best_ . As we discussed in Section 6.1.1, the model containing all of the predictors will always have the smallest RSS and the largest _R_[2] , since these quantities are related to the training error. Instead, we wish to choose a model with a low test error. As is evident here, and as we show in Chapter 2, the training error can be a poor estimate of the test error. Therefore, RSS and _R_[2] are not suitable for selecting the best model among a collection of models with different numbers of predictors. 

In order to select the best model with respect to test error, we need to estimate this test error. There are two common approaches: 

1. We can indirectly estimate test error by making an _adjustment_ to the training error to account for the bias due to overfitting. 

2. We can _directly_ estimate the test error, using either a validation set approach or a cross-validation approach, as discussed in Chapter 5. 

We consider both of these approaches below. 

---

## Sub-Chapters (하위 목차)

### Cp, AIC, BIC, and Adjusted R² (Cp, AIC, BIC 및 조정된 R²)
* [문서로 이동하기](./6_1_3_1_cp_aic_bic_and_adjusted_r2/)

변수가 하나씩 추가될 때마다 수학적인 페널티(Penalty)를 부과하여, 쓸모 없는 다수 변수로 인한 과적합을 막고 모델 간 공정한 비교를 유도하는 평가 지표입니다.

### Validation and Cross-Validation (검증 세트 및 교차 검증)
* [문서로 이동하기](./6_1_3_2_validation_and_cross-validation/)

이론적 지표식(AIC 등)에 의존하지 않고 데이터를 직접 분할하여 시험을 치르는 가장 검증된 모형 선택 방식인 크로스 밸리데이션(CV)을 다시 가져옵니다.

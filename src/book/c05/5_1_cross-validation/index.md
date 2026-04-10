---
layout: default
title: "index"
---

# 5.1 Cross-Validation 

In Chapter 2 we discuss the distinction between the _test error rate_ and the _training error rate_ . The test error is the average error that results from using a statistical learning method to predict the response on a new observation— that is, a measurement that was not used in training the method. Given a data set, the use of a particular statistical learning method is warranted if it results in a low test error. The test error can be easily calculated if a designated test set is available. Unfortunately, this is usually not the case. In contrast, the training error can be easily calculated by applying the statistical learning method to the observations used in its training. But as we saw in Chapter 2, the training error rate often is quite different from the test error rate, and in particular the former can dramatically underestimate the latter. 

In the absence of a very large designated test set that can be used to directly estimate the test error rate, a number of techniques can be used to estimate this quantity using the available training data. Some methods make a mathematical adjustment to the training error rate in order to estimate the test error rate. Such approaches are discussed in Chapter 6. In this section, we instead consider a class of methods that estimate the test error rate by _holding out_ a subset of the training observations from the fitting process, and then applying the statistical learning method to those held out observations. 

In Sections 5.1.1–5.1.4, for simplicity we assume that we are interested in performing regression with a quantitative response. In Section 5.1.5 we consider the case of classification with a qualitative response. As we will see, the key concepts remain the same regardless of whether the response is quantitative or qualitative. 

---

## Sub-Chapters (하위 목차)

### 5.1.1 The Validation Set Approach (검증 세트 접근법)
* [문서로 이동하기](./5_1_1_the_validation_set_approach/)

가장 단순하게 전체 데이터를 절반은 훈련용(Train), 나머지 절반은 검증용(Validation)으로 단 1번 쪼개는 고전적인 분할 방식입니다.
구현하기 무척 쉽지만 관측치 낭비가 크고, 분할 시드에 따라 검증 결과가 심하게 요동치는 치명적인 단점을 살펴봅니다.

### 5.1.2 Leave-One-Out Cross-Validation (단일 관측치 제외 교차 검증, LOOCV)
* [문서로 이동하기](./5_1_2_leave-one-out_cross-validation/)

단 1개의 관측치만 검증 폴드로 빼두고 나머지 수많은 데이터 전체를 훈련에 쏟아붓는 완전형 교차 검증법 수식 체계입니다.
편향 이슈는 거의 해결되나, N번씩 전체 모델을 계속 훈련해야 하므로 연산 비용이 천문학적일 수 있음을 논의합니다.

### 5.1.3 k-Fold Cross-Validation (k-폴드 교차 검증)
* [문서로 이동하기](./5_1_3_k-fold_cross-validation/)

전체 데이터를 균등하게 K개(통상 5~10)의 파티션으로 조각내어 순차적으로 돌아가며 교차 검증하는 최적의 타협안입니다.
LOOCV 대비 연산 소모 구간을 획기적으로 줄여주며, 적정한 분산과 편향 보정 능력을 거두는 기법을 경험합니다.

### 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation (k-폴드에서의 편향-분산 트레이드오프)
* [문서로 이동하기](./5_1_4_bias-variance_trade-off_for_k-fold_cross-validation/)

데이터를 나누는 K 갯수에 따라 편향(Bias) 제어와 예측 분산(Variance) 상승이 어떻게 서로 대치되는지 수리적으로 따져봅니다.
왜 많은 학자들과 현업에서 K=10 혹은 K=5를 압도적인 기본값으로 선택하는지 이론적 이유를 분석합니다.

### 5.1.5 Cross-Validation on Classification Problems (분류 문제에서의 교차 검증)
* [문서로 이동하기](./5_1_5_cross-validation_on_problems_classification/)

그동안 회귀분야 연속 변수(MSE 측도 중심)에서 관찰했던 CV 사이클 테크닉을, 이산적이고 범주형인 오분류율(Error Rate) 척도에 동일하게 전파합니다.
분류 모델들의 초매개변수를 튜닝하고 우수성을 비교하는 통계적 실증 분석입니다.

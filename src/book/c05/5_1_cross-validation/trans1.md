---
layout: default
title: "trans1"
---

# 5.1 Cross-Validation 
# 5.1 교차 검증

In Chapter 2 we discuss the distinction between the _test error rate_ and the _training error rate_ . The test error is the average error that results from using a statistical learning method to predict the response on a new observation— that is, a measurement that was not used in training the method. Given a data set, the use of a particular statistical learning method is warranted if it results in a low test error. The test error can be easily calculated if a designated test set is available. Unfortunately, this is usually not the case. In contrast, the training error can be easily calculated by applying the statistical learning method to the observations used in its training. But as we saw in Chapter 2, the training error rate often is quite different from the test error rate, and in particular the former can dramatically underestimate the latter. 
Chapter 2에서 우리는 _테스트 에러율(test error rate)_ 과 _훈련 에러율(training error rate)_ 간의 차이(distinction)에 대해 논의했습니다. 테스트 에러는 방법론을 훈련하는 데 사용되지 않은 측정값인 새로운 관측치(new observation)에 대한 반응을 예측하기 위해 통계적 학습 방법을 사용한 결과로 나타나는 평균 오차입니다. 데이터 세트가 주어졌을 때, 특정 통계적 학습 방법의 사용은 그것이 낮은 테스트 에러를 초래할 경우에 정당화됩니다(warranted). 지정된 테스트 세트를 이용할 수 있다면 테스트 에러를 쉽게 계산할 수 있습니다. 불행하게도 이는 일반적으로 사실이 아닙니다(not the case). 이와 대조적으로 훈련 에러는 통계적 학습 방법을 해당 훈련에 사용된 관측치들에 적용함으로써 쉽게 계산될 수 있습니다. 그러나 Chapter 2에서 보았듯이 훈련 에러율은 종종 테스트 에러율과 상당히 다르며, 특히 전자는 후자를 극적으로(dramatically) 과소평가(underestimate)할 수 있습니다.

In the absence of a very large designated test set that can be used to directly estimate the test error rate, a number of techniques can be used to estimate this quantity using the available training data. Some methods make a mathematical adjustment to the training error rate in order to estimate the test error rate. Such approaches are discussed in Chapter 6. In this section, we instead consider a class of methods that estimate the test error rate by _holding out_ a subset of the training observations from the fitting process, and then applying the statistical learning method to those held out observations. 
테스트 에러율을 직접적으로 추정하는 데 사용할 수 있는 매우 큰 지정된 테스트 세트가 부재(absence)할 경우, 이용 가능한 훈련 데이터를 활용하여 이 양(quantity)을 추정하는 몇 가지 기술을 사용할 수 있습니다. 몇몇 방법들은 테스트 에러율을 추정하기 위해 훈련 에러율에 대해 수학적인 조정(mathematical adjustment)을 가합니다. 그러한 접근법들은 Chapter 6에서 논의됩니다. 본 절(section)에서 우리는 대신 피팅 과정(fitting process)에서 훈련 관측치의 하위 집합(subset)을 _제외(holding out)_ 하고, 그 제외된 관측치에 통계적 학습 방법을 적용함으로써 테스트 에러율을 추정하는 부류의 방법론을 고려합니다.

In Sections 5.1.1–5.1.4, for simplicity we assume that we are interested in performing regression with a quantitative response. In Section 5.1.5 we consider the case of classification with a qualitative response. As we will see, the key concepts remain the same regardless of whether the response is quantitative or qualitative. 
단순성을 위해 Sections 5.1.1–5.1.4에서는 우리가 정량적인 반응(quantitative response)으로 회귀를 수행하는 데 관심이 있다고 가정할 것입니다. Section 5.1.5에서는 정성적인 반응(qualitative response)으로 분류하는 경우를 고려할 것입니다. 우리가 보게 되겠지만, 핵심 개념(key concepts)은 반응이 정량적인지 정성적인지와 무관하게(regardless) 동일하게 유지됩니다.

---

## Sub-Chapters (하위 목차)

### 5.1.1 The Validation Set Approach (검증 세트 접근법)
* [문서로 이동하기](./5_1_1_the_validation_set_approach/trans1.html)

### 5.1.2 Leave-One-Out Cross-Validation (단일 관측치 제외 교차 검증, LOOCV)
* [문서로 이동하기](./5_1_2_leave-one-out_cross-validation/trans1.html)

### 5.1.3 k-Fold Cross-Validation (k-폴드 교차 검증)
* [문서로 이동하기](./5_1_3_k-fold_cross-validation/trans1.html)

### 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation (k-폴드에서의 편향-분산 트레이드오프)
* [문서로 이동하기](./5_1_4_bias-variance_trade-off_for_k-fold_cross-validation/trans1.html)

### 5.1.5 Cross-Validation on Classification Problems (분류 문제에서의 교차 검증)
* [문서로 이동하기](./5_1_5_cross-validation_on_problems_classification/trans1.html)

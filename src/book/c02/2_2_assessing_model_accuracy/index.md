---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach. Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method? _There is no free lunch in statistics:_ no one method dominates all others over all possible data sets. On a particular data set, one specific method may work 


best, but some other method may work better on a similar but different data set. Hence it is an important task to decide for any given set of data which method produces the best results. Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set. As the book progresses, we will explain how the concepts presented here can be applied in practice. 

---

## Sub-Chapters (하위 목차)

### 2.2.1 Measuring the Quality of Fit (적합성 품질 측정)
* [문서로 이동하기](./2_2_1_measuring_the_quality_of_fit/)

회귀 환경에서 모형의 우수성을 평가할 때 가장 보편적으로 사용되는 척도인 평균 제곱 오차(MSE, Mean Squared Error)를 설명합니다.
단순히 학습 데이터만 잘 맞추는 것보다는 낯선 시험 데이터에도 좋은 성능을 발휘하는 일반화(Generalization)의 중요성을 강조합니다.

### 2.2.2 The Bias-Variance Trade-Off (편향-분산 트레이드오프)
* [문서로 이동하기](./2_2_2_the_bias-variance_trade-off/)

시험 데이터의 오차를 구성하는 본질적인 요소인 편향(Bias)과 분산(Variance) 간의 복잡한 상관관계를 다룹니다.
모델의 유연성이 증가함에 따라 분산은 커지고 편향은 서서히 줄어드는 U자형 검증 곡선(U-Shape)을 수학적으로 탐구합니다.

### 2.2.3 The Classification Setting (분류 환경에서의 평가)
* [문서로 이동하기](./2_2_3_the_classification_setting/)

이산적인 클래스 결과를 예측해야 하는 모델 환경에서 성능을 비교하기 위한 비율 지표인 오분류율(Error Rate)을 도입합니다.
주어진 데이터 공간 내에서 최적의 예측을 수행하여 최소 한계를 규정하는 베이즈 에러율(Bayes Error Rate)을 학습합니다.

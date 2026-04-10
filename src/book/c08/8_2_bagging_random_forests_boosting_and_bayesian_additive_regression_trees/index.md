---
layout: default
title: "index"
---

# 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

An _ensemble_ method is an approach that combines many simple “building ensemble block” models in order to obtain a single and potentially very powerful model. These simple building block models are sometimes known as _weak learners_ , since they may lead to mediocre predictions on their own. 

weak learners 

We will now discuss bagging, random forests, boosting, and Bayesian additive regression trees. These are ensemble methods for which the simple building block is a regression or a classification tree. 

---

## Sub-Chapters (하위 목차)

### 8.2.1 Bagging (배깅)
* [문서로 이동하기](./8_2_1_bagging/)

훈련 데이터에서 부트스트랩 샘플을 여러 개 생성하고, 각 샘플마다 깊게 파고든 개별 트리들을 만들어 평균을 냄으로써 분산을 획기적으로 줄이는 기초 앙상블 기법입니다.

### 8.2.2 Random Forests (랜덤 포레스트)
* [문서로 이동하기](./8_2_2_random_forests/)

배깅의 단점(트리들끼리 상관성이 높아지는 병목)을 극복하고자, 분기 지점마다 무작위로 일부 변수만 추출하여 트리의 다양성을 높이는 초강력 모델입니다.

### 8.2.3 Boosting (부스팅)
* [문서로 이동하기](./8_2_3_boosting/)

트리들을 독립적으로 만들지 않고, 이전 트리가 범한 잔차(오류)를 다음 트리가 집중적으로 순차 보완해나가는 방식의 느슨하지만 정교한 학습법입니다.

### 8.2.4 Bayesian Additive Regression Trees (베이지안 가법 회귀 트리, BART)
* [문서로 이동하기](./8_2_4_bayesian_additive_regression_trees/)

베이즈 사전 분포 개념을 도입해 이전 트리의 조합에 새로운 트리를 더하는 방식을 통계적으로 확률화한 현대적인 머신러닝 최신 기법을 다룹니다.

### 8.2.5 Summary of Tree Ensemble Methods (트리 앙상블 기법들의 종합 요약)
* [문서로 이동하기](./8_2_5_summary_of_tree_ensemble_methods/)

배깅, 랜덤 포레스트, 부스팅, BART가 각각 편향 분산을 어떻게 조절하며 어떠한 튜닝 파라미터를 갖는지 서로 대조하여 맵핑합니다.

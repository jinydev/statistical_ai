---
layout: default
title: "8. Tree-Based Methods"
---

# 8. Tree-Based Methods (트리 기반 방법론)

데이터 공간을 여러 의미 있는 사각형 구역으로 계층적으로 쪼개어 예측하는 의사결정 트리(Decision Tree)와 그 파생 모델들을 다루는 8장입니다.
설명력이 높은 단일 트리 모델부터, 예측력을 극적으로 향상시키는 배깅, 랜덤 포레스트, 부스팅 등 앙상블 기법을 배웁니다.

## 8.1 The Basics of Decision Trees (의사결정 트리의 기초)
* [문서로 이동하기](./8_1_the_basics_of_decision_trees/)

단일 나무 형태의 지도를 따라가며 공간을 분할(Segmentation)하여 회귀 및 분류를 수행하는 베이스 알고리즘을 소개합니다.
조건부 분기(Split)를 통해 예측값을 찾아내는 직관적인 과정을 배웁니다.

### 8.1.1 Regression Trees (회귀 트리)
* [문서로 이동하기](./8_1_the_basics_of_decision_trees/8_1_1_regression_trees/)

연속형 변수를 예측할 때 RSS(잔차 제곱합)를 최소화하는 방향으로 공간을 사각형으로 쪼개는 하향식 탐욕 경로(Top-down Greedy)를 다룹니다.
과적합을 방지하기 위한 가지치기(Pruning) 개념을 학습합니다.

### 8.1.2 Classification Trees (분류 트리)
* [문서로 이동하기](./8_1_the_basics_of_decision_trees/8_1_2_trees_classification/)

명목형 클래스를 예측할 때 사용하는 트리이며, RSS 대신 지니 계수(Gini Index)나 엔트로피(Entropy)로 노드의 불순도를 계산해 분할하는 방식을 봅니다.

### 8.1.3 Trees Versus Linear Models (트리와 선형 모델의 특성 비교)
* [문서로 이동하기](./8_1_the_basics_of_decision_trees/8_1_3_trees_versus_linear_models/)

어느 모델이 항상 우월한 것이 아니라, 진정한 결정 경계가 직선적일 땐 선형 모델이 낫고 비선형이나 사각 박스형일 땐 트리가 우수하다는 데이터 기반 직관을 얻습니다.

### 8.1.4 Advantages and Disadvantages of Trees (단일 트리의 장단점)
* [문서로 이동하기](./8_1_the_basics_of_decision_trees/8_1_4_advantages_and_disadvantages_of_trees/)

사람이 직관적으로 이해하고 시각화하기엔 최고이며 더미 변수가 필요 없는 장점과, 반대로 예측 정확도가 떨어지고 분산이 크다는 치명적인 한계를 요약합니다.

## 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees (앙상블 트리 기법들)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/)

단일 결정 트리의 빈약한 성능을 극복하기 위해 수백, 수천 개의 트리를 다수에 결합해 합의(Consensus)를 거치는 앙상블 모형들을 소개합니다.

### 8.2.1 Bagging (배깅)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_1_bagging/)

훈련 데이터에서 부트스트랩 샘플을 여러 개 생성하고, 각 샘플마다 깊게 파고든 개별 트리들을 만들어 평균을 냄으로써 분산을 획기적으로 줄이는 기초 앙상블 기법입니다.

#### Out-of-Bag Error Estimation (OOB 오차 추정)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_1_bagging/8_2_1_1_out-of-bag_error_estimation/)

배깅의 부트스트랩 과정에서 추출되지 않은 남은 1/3의 관측치들을 이용해 마치 교차 검증을 한 것처럼 모델 테스트 오차를 가볍게 계산하는 요령입니다.

#### Variable Importance Measures (변수 중요도 측정)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_1_bagging/8_2_1_2_variable_importance_measures/)

앙상블로 묶여 해석력이 떨어진 블랙박스 모형 안에서, 특정 변수가 지니 불순도와 RSS를 얼마나 누적 감소시켰는지 측정하여 변수의 기여도를 랭킹 매기는 지표입니다.

### 8.2.2 Random Forests (랜덤 포레스트)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_2_random_forests/)

배깅의 단점(트리들끼리 상관성이 높아지는 병목)을 극복하고자, 분기 지점마다 무작위로 일부 변수만 추출하여 트리의 다양성을 높이는 초강력 모델입니다.

### 8.2.3 Boosting (부스팅)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_3_boosting/)

트리들을 독립적으로 만들지 않고, 이전 트리가 범한 잔차(오류)를 다음 트리가 집중적으로 순차 보완해나가는 방식의 느슨하지만 정교한 학습법입니다.

### 8.2.4 Bayesian Additive Regression Trees (베이지안 가법 회귀 트리, BART)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_4_bayesian_additive_regression_trees/)

베이즈 사전 분포 개념을 도입해 이전 트리의 조합에 새로운 트리를 더하는 방식을 통계적으로 확률화한 현대적인 머신러닝 최신 기법을 다룹니다.

### 8.2.5 Summary of Tree Ensemble Methods (트리 앙상블 기법들의 종합 요약)
* [문서로 이동하기](./8_2_bagging_random_forests_boosting_and_bayesian_additive_regression_trees/8_2_5_summary_of_tree_ensemble_methods/)

배깅, 랜덤 포레스트, 부스팅, BART가 각각 편향 분산을 어떻게 조절하며 어떠한 튜닝 파라미터를 갖는지 서로 대조하여 맵핑합니다.

## 8.3 Lab: Tree-Based Methods (파이썬 기반 의사결정 트리 및 앙상블 실습 랩)
* [문서로 이동하기](./8_3_lab_tree-based_methods/)

Scikit-Learn의 트리 모듈과 앙상블 라이브러리를 임포트하여 보스턴이나 자동차 데이터셋에 예측 트리를 띄워보는 실전 파이썬 과정입니다.

### 8.3.1 Fitting Classification Trees (분류 트리 적합 및 시각화 실습)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_1_fitting_classification_trees/)

`DecisionTreeClassifier` 알고리즘을 소환하고, 데이터를 쪼개는 계층 구조망을 파이썬 `plot_tree` 함수로 시각화하여 화면에 그려봅니다.

#### Jupyter Notebook Output (트리 모형 정확도 및 콘솔 반환 로그 점검)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_1_fitting_classification_trees/8_3_1_1_out6_0.7275/)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_1_fitting_classification_trees/8_3_1_1_out12_0.735/)
적은 차원의 단일 분류 트리가 출력하는 테스트 검증 스코어를 콘솔에서 디버깅하며 관찰합니다.

### 8.3.3 Bagging and Random Forests (랜덤포레스트 앙상블 파이썬 피팅 실습)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_3_bagging_and_random_forests/)

`RandomForestRegressor` 객체를 불러온 상태에서 노드 변수 개수(Max features)를 조절하는 방식으로 배깅과 포레스트를 번갈아 구동하는 법을 익힙니다.

#### Jupyter Notebook Output (앙상블 모형 편차 스코어 결과)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_3_bagging_and_random_forests/8_3_3_1_out27_20.04/)
포레스트 트리 군락이 형성한 평균 오차율이 단일 트리를 얼마나 압도적으로 넘어서는지 로그로 확인힙니다.

### 8.3.4 Boosting (그라디언트 부스팅 파이썬 실습)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_4_boosting/)

`GradientBoostingRegressor`를 탑재하여 트리 갯수 및 학습률(Learning Rate)를 인자로 넣으면서 과적합 없이 손실을 낮추는 부스팅 조작을 다룹니다.

#### Jupyter Notebook Output (부스팅 반환 점검)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_4_boosting/8_3_4_1_out32_14.50/)
느린 속도로 학습률을 올린 부스팅 모델의 단단한 테스트 예측력을 수치 스코어로 파악합니다.

### 8.3.5 Bayesian Additive Regression Trees (BART 패키지 운용 실습)
* [문서로 이동하기](./8_3_lab_tree-based_methods/8_3_5_bayesian_additive_regression_trees/)

BART 전용 통계 패키지를 로드하여 MCMC 깁스 샘플링 기반의 트리를 파이썬 워크플로우에 통합 적용해 보는 경험적 코딩입니다.

## 8.4 Exercises (트리 분기 및 앙상블 응용 문제 종합장)
* [문서로 이동하기](./8_4_exercises/)

의사결정 트리의 분기 조건과, 랜덤 포레스트의 독립성 확보 이유 등을 수학 기하적으로 점검하는 종합 훈련 코스입니다.

### Conceptual (트리 편향 분산 개념 수학 모델 문제)
* [문서로 이동하기](./8_4_exercises/8_4_1_conceptual/)

특정 분기(Split) 영역이 2차원 평면에서 가지는 부등식 제약을 직접 그리고, 가지치기 파라미터가 유도하는 모델 깊이 차이를 통계식으로 설명합니다.

### Applied (머신런 프레임 파이썬 모델 응용 세트)
* [문서로 이동하기](./8_4_exercises/8_4_2_applied/)

제공된 도메인 데이터를 랩에 올려 각기 다른 OOB 오차 플롯을 그리거나 변수 중요도(Feature Importance) 막대 차트를 직접 시각화하는 파이썬 코딩 챌린지입니다.

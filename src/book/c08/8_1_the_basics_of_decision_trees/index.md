---
layout: default
title: "index"
---

# 8.1 The Basics of Decision Trees 

Decision trees can be applied to both regression and classification problems. We first consider regression problems, and then move on to classification. 

---

## Sub-Chapters (하위 목차)

### 8.1.1 Regression Trees (회귀 트리)
* [문서로 이동하기](./8_1_1_regression_trees/)

연속형 변수를 예측할 때 RSS(잔차 제곱합)를 최소화하는 방향으로 공간을 사각형으로 쪼개는 하향식 탐욕 경로(Top-down Greedy)를 다룹니다.
과적합을 방지하기 위한 가지치기(Pruning) 개념을 학습합니다.

### 8.1.2 Classification Trees (분류 트리)
* [문서로 이동하기](./8_1_2_trees_classification/)

명목형 클래스를 예측할 때 사용하는 트리이며, RSS 대신 지니 계수(Gini Index)나 엔트로피(Entropy)로 노드의 불순도를 계산해 분할하는 방식을 봅니다.

### 8.1.3 Trees Versus Linear Models (트리와 선형 모델의 특성 비교)
* [문서로 이동하기](./8_1_3_trees_versus_linear_models/)

어느 모델이 항상 우월한 것이 아니라, 진정한 결정 경계가 직선적일 땐 선형 모델이 낫고 비선형이나 사각 박스형일 땐 트리가 우수하다는 데이터 기반 직관을 얻습니다.

### 8.1.4 Advantages and Disadvantages of Trees (단일 트리의 장단점)
* [문서로 이동하기](./8_1_4_advantages_and_disadvantages_of_trees/)

사람이 직관적으로 이해하고 시각화하기엔 최고이며 더미 변수가 필요 없는 장점과, 반대로 예측 정확도가 떨어지고 분산이 크다는 치명적인 한계를 요약합니다.

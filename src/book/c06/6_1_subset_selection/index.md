---
layout: default
title: "index"
---

# 6.1 Subset Selection 

In this section we consider some methods for selecting subsets of predictors. These include best subset and stepwise model selection procedures. 

---

## Sub-Chapters (하위 목차)

### 6.1.1 Best Subset Selection (최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_best_subset_selection/)

변수가 $p$개일 때 만들 수 있는 모든 조합($2^p$개)의 모델을 전부 적합해보고 가장 우수한 하나를 시도하는 무차별 대입 방식입니다.

### 6.1.2 Stepwise Selection (단계적 선택법)
* [문서로 이동하기](./6_1_2_stepwise_selection/)

최적 부분집합의 거대한 컴퓨팅 연산의 낭비와 과적합 위험을 회피하고자, 하나씩 변수를 더하거나 빼는 탐욕적(Greedy) 방식의 선별법입니다.

### 6.1.3 Choosing the Optimal Model (최적 모델 선택)
* [문서로 이동하기](./6_1_3_choosing_the_optimal_model/)

훈련 에러(RSS, R²)만으로는 변수가 늘어날수록 무조건 오차가 줄어드는 착시가 있기에, 실질 테스트 에러를 가늠할 독립적 지표 체계가 필요함을 배웁니다.

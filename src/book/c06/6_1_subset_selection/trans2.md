---
layout: default
title: "trans2"
---

# 6.1 Subset Selection 
# 6.1 부분집합 선택 (Subset Selection): 최정예 요원 선발 대작전

In this section we consider some methods for selecting subsets of predictors. These include best subset and stepwise model selection procedures. 
자, 이번 구역(section)에서 사령관인 우리는 전방에 길게 늘어선 무수히 많은 변수 부대원(predictors)들 무리 중에서, 오직 가장 똘똘하고 타격감이 좋은 핵심 정예 부대, 즉 알짜배기 부분집합 파벌(subsets)만을 칼같이 추려내어 선발 조치(selecting)하기 기동 시스템 절차(methods)들을 집중 심문 탐구(consider)하게 됩니다. 여기에는 모든 경우의 수를 무식하게 다 돌려보는 "전수 조사 오디션"인 **최적 부분집합(best subset)** 선별법과, 한 명씩 한 명씩 차례대로 채용과 해고를 반복하는 약삭빠르고 기민한 **단계적 투입/축출 모델 선택(stepwise model selection)** 자동화 알고리즘 절차(procedures) 들이 이 매력적인 전략 무기 창고 안에 든든하게 포진 무장(include)되어 있습니다.

---

## Sub-Chapters (하위 목차)

### 6.1.1 Best Subset Selection (최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_best_subset_selection/trans2.html)

변수가 $p$개일 때 만들 수 있는 모든 조합($2^p$개)의 모델을 전부 적합해보고 가장 우수한 하나를 시도하는 무차별 대입 방식입니다.

### 6.1.2 Stepwise Selection (단계적 선택법)
* [문서로 이동하기](./6_1_2_stepwise_selection/trans2.html)

최적 부분집합의 거대한 컴퓨팅 연산의 낭비와 과적합 위험을 회피하고자, 하나씩 변수를 더하거나 빼는 탐욕적(Greedy) 방식의 선별법입니다.

### 6.1.3 Choosing the Optimal Model (최적 모델 선택)
* [문서로 이동하기](./6_1_3_choosing_the_optimal_model/trans2.html)

훈련 에러(RSS, R²)만으로는 변수가 늘어날수록 무조건 오차가 줄어드는 착시가 있기에, 실질 테스트 에러를 가늠할 독립적 지표 체계가 필요함을 배웁니다.

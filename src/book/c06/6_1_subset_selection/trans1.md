---
layout: default
title: "trans1"
---

# 6.1 Subset Selection 
# 6.1 부분집합 선택 (Subset Selection)

In this section we consider some methods for selecting subsets of predictors. These include best subset and stepwise model selection procedures. 
이 섹션 단락 영역에서 우리는 일련의 전체 투입 예측 변수(predictors)들 가운데 오직 핵심이 되는 부분집합(subsets) 분파만을 선별 픽업 추출 지목 발탁 선택(selecting) 하기 위해 마련된 몇 가지 통계 모델 규명 처리 방법론 기법 수단(methods)들을 중점 고려 심사 탐구 진단(consider)해 봅니다. 이와 같은 방법 수단들의 소속 진영에는 이른바 최적 부분집합 방식(best subset)과, 단계성을 띠는 단계적 하향 상향 모델 선택(stepwise model selection) 알고리즘 체제 절차(procedures) 들이 주류로 대거 포함 포진 포괄 안착(include) 되어 있습니다.

---

## Sub-Chapters (하위 목차)

### 6.1.1 Best Subset Selection (최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_best_subset_selection/trans1.html)

변수가 $p$개일 때 만들 수 있는 모든 조합($2^p$개)의 모델을 전부 적합해보고 가장 우수한 하나를 시도하는 무차별 대입 방식입니다.

### 6.1.2 Stepwise Selection (단계적 선택법)
* [문서로 이동하기](./6_1_2_stepwise_selection/trans1.html)

최적 부분집합의 거대한 컴퓨팅 연산의 낭비와 과적합 위험을 회피하고자, 하나씩 변수를 더하거나 빼는 탐욕적(Greedy) 방식의 선별법입니다.

### 6.1.3 Choosing the Optimal Model (최적 모델 선택)
* [문서로 이동하기](./6_1_3_choosing_the_optimal_model/trans1.html)

훈련 에러(RSS, R²)만으로는 변수가 늘어날수록 무조건 오차가 줄어드는 착시가 있기에, 실질 테스트 에러를 가늠할 독립적 지표 체계가 필요함을 배웁니다.

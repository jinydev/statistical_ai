---
layout: default
title: "index"
---

# _6.1.1 Best Subset Selection_ 

To perform _best subset selection_ , we fit a separate least squares regression best subset for each possible combination of the _p_ predictors. That is, we fit all _p_ models selection that contain exactly one predictor, all � _p_ 2� = _p_ ( _p −_ 1) _/_ 2 models that contain exactly two predictors, and so forth. We then look at all of the resulting models, with the goal of identifying the one that is _best_ . 

The problem of selecting the _best model_ from among the 2 _[p]_ possibilities considered by best subset selection is not trivial. This is usually broken up into two stages, as described in Algorithm 6.1. 

---

## Sub-Chapters (하위 목차)

### Algorithm 6.1 Best subset selection (알고리즘 6.1 최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_1_algorithm_6.1_best_subset_selection/)

모든 K크기의 변수 조합에서 가장 좋은 모델을 기록하고, 최종적으로 Cross-Validation이나 AIC/BIC 평가지표로 모델 1개를 선정하는 절차입니다.

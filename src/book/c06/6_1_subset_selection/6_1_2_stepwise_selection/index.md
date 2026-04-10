---
layout: default
title: "index"
---

# _6.1.2 Stepwise Selection_ 

For computational reasons, best subset selection cannot be applied with very large _p_ . Best subset selection may also suffer from statistical problems when _p_ is large. The larger the search space, the higher the chance of finding models that look good on the training data, even though they might not have any predictive power on future data. Thus an enormous search space can lead to overfitting and high variance of the coefficient estimates. 

For both of these reasons, _stepwise_ methods, which explore a far more restricted set of models, are attractive alternatives to best subset selection. 

---

## Sub-Chapters (하위 목차)

### Forward Stepwise Selection (전진 단계 선택법)
* [문서로 이동하기](./6_1_2_1_forward_stepwise_selection/)

데이터에 아무 변수가 없는 빈(Null) 모델에서 출발하여 모델 성능을 가장 유의미하게 향상시키는 변수를 한 번에 하나씩만 추가하는 경제적 방식입니다.

### Hybrid Approaches (혼합 접근법)
* [문서로 이동하기](./6_1_2_2_hybrid_approaches/)

전진 추가와 후진 제거(Backward)를 양방향 결합하여, 유의미해 보였지만 다른 변수 편입으로 불필요해진 변수를 추후에 제거해 내는 유연한 방식입니다.

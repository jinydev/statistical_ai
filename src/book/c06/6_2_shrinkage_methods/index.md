---
layout: default
title: "index"
---

# 6.2 Shrinkage Methods 

The subset selection methods described in Section 6.1 involve using least squares to fit a linear model that contains a subset of the predictors. As an alternative, we can fit a model containing all _p_ predictors using a technique that _constrains_ or _regularizes_ the coefficient estimates, or equivalently, that _shrinks_ the coefficient estimates towards zero. It may not be immediately obvious why such a constraint should improve the fit, but it turns out that shrinking the coefficient estimates can significantly reduce their variance. The two best-known techniques for shrinking the regression coefficients towards zero are _ridge regression_ and the _lasso_ . 

---

## Sub-Chapters (하위 목차)

### 6.2.1 Ridge Regression (릿지 회귀)
* [문서로 이동하기](./6_2_1_ridge_regression/)

기존 잔차 제곱합에 파라미터 계수 값 제곱의 합($L_2$ 페널티)을 최소화 조건으로 덧붙여, 중요치 않은 계수가 비정상적으로 팽창하는 현상을 누그러뜨리는 기법입니다.

### 6.2.2 The Lasso (라쏘 회귀 방법)
* [문서로 이동하기](./6_2_2_the_lasso/)

릿지와 달리, 파라미터 계수의 절댓값의 합($L_1$ 페널티)을 사용함으로써 상대적으로 잉여 변수인 계수를 완전히 0으로 만들어 자동 변수 소거(Selection) 기능까지 수행합니다.

### 6.2.3 Selecting the Tuning Parameter (최적 조율 파라미터 탐색)
* [문서로 이동하기](./6_2_3_selecting_the_tuning_parameter/)

수축의 강도를 가장 적합하게 조절하는 초매개변수 $\lambda$ 값을 경험이 아닌 데이터를 기반으로 도출하기 위하여 순수 모델 교차 검증을 동원합니다.

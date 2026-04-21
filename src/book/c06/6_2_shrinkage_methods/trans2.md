---
layout: default
title: "trans2"
---

# 6.2 Shrinkage Methods 
# 6.2 수축 기법 (Shrinkage Methods)

The subset selection methods described in Section 6.1 involve using least squares to fit a linear model that contains a subset of the predictors. As an alternative, we can fit a model containing all _p_ predictors using a technique that _constrains_ or _regularizes_ the coefficient estimates, or equivalently, that _shrinks_ the coefficient estimates towards zero. It may not be immediately obvious why such a constraint should improve the fit, but it turns out that shrinking the coefficient estimates can significantly reduce their variance. The two best-known techniques for shrinking the regression coefficients towards zero are _ridge regression_ and the _lasso_ . 
6.1절에서 배웠던 '부분집합 선택' 방식은 쓸데없는 변수를 아예 쳐내고, 남은 알짜 변수들만 모아서 최소 제곱법을 오리지널 그대로 돌리는 방식입니다. 이와는 반대로, 이번 6.2장에서는 전체 $p$ 개 예측 변수를 하나도 버리지 않고 몽땅 끌어안고 가는 대안을 배웁니다. 
대신, 기계가 찾아낸 파라미터 계수 값들의 크기를 수학적으로 **'제약(constrains)'** 하거나 **'정규화(regularizes)'** 하는 추가 페널티 장치를 겁니다. 좀 더 쉬운 말로 풀자면, 모델이 도출한 계수 값들을 억지로 0에 가깝도록 쪼그라들게 **'수축(shrinks)'** 시켜 버리는 겁니다.
처음 들으면 "아니, 힘들게 구한 파라미터를 왜 일부러 제약하고 0으로 찌그러뜨려서 망치는 거지?" 라고 의아할 수 있습니다. 하지만 놀랍게도 이렇게 계수를 눌러서 수축시키면, 모델 성적의 분산(Variance)이 크게 줄어들어 실전 테스트 안정성이 대폭 상승합니다. 
이렇게 회귀 계수들을 0을 향해 무자비하게 수축시켜 버리는 가장 뛰어난 두 가지 무기가 바로 **'릿지 회귀(ridge regression)'** 와 **'라쏘(lasso)'** 입니다.

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

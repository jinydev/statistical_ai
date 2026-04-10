---
layout: default
title: "index"
---

# _6.5.2 Ridge Regression and the Lasso_ 

We will use the `sklearn.linear_model` package (for which we use `skl` as shorthand below) to fit ridge and lasso regularized linear models on the `Hitters` data. We start with the model matrix `X` (without an intercept) that we computed in the previous section on best subset regression. 

---

## Sub-Chapters (하위 목차)

### Ridge Regression (릿지 페널티 회귀 분석 결과 도출 점검)
* [문서로 이동하기](./6_5_2_1_out31_array231788.32/)

릿지 모형 선언 시 적용되는 입력 변수 내부 자체 정규화 조절 인자($\alpha$)를 조금씩 튜닝해가면서 에러율 RSS 반환점 변화가 어떤 로깅 궤적을 거치는지 관찰합니다.

### Fast Cross-Validation for Solution Paths (최적의 파라미터 라인을 잡기 위한 체인 고속 교차 검증)
* [문서로 이동하기](./6_5_2_2_fast_cross-validation_for_solution_paths/)

* [The Lasso](./39_the_lasso/)
가장 손실을 이상적으로 줄여주는 매개변수 $\alpha$ 혹은 $\lambda$를 컴퓨터 연산 파워를 통해 찾기 위해 `RidgeCV` 객체, `LassoCV` 내장 속성의 사용법을 시뮬레이터로 알아봅니다.

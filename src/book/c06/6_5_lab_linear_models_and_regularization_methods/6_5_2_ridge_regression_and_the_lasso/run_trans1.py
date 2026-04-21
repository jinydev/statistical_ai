import codecs

content = r"""---
layout: default
title: "trans1"
---

# 6.5.2 능선 회귀와 라쏘 (Ridge Regression and the Lasso)

We will use the `sklearn.linear_model` package (for which we use `skl` as shorthand below) to fit ridge and lasso regularized linear models on the `Hitters` data. We start with the model matrix `X` (without an intercept) that we computed in the previous section on best subset regression.
우리는 `Hitters` 데이터 세트 무대 위에서, 능력치가 꽉 찬 릿지(ridge) 및 라쏘(lasso) 정규화(regularized) 선형 회귀 모델 모형을 적합하여 구축하기 위해 `sklearn.linear_model` 파이썬 내장형 패키지 모듈을 불러들여 사용할 것입니다 (편의성을 위해 본문 코드 기록 하단부터는 이 긴 패키지 호출명을 간단히 `skl` 이라는 축약칭 지정자로 부르겠습니다). 작업 착수 단계에 앞서, 이전 파트 변수 무대의 '최선 부분집합 관제 회귀 단원'에서 도출하고 계산해 두었던 원천 매트릭스 `X` 데이터 모형(절편인 intercept가 깔끔히 빠져있는 상태)에서부터 시작 선을 잡고 작업을 출발시킵니다.

---

## Sub-Chapters (하위 목차)

### Ridge Regression (릿지 정규화 회귀 분석 평가)
* [문서로 이동하기](./6_5_2_1_ridge_regression/)

릿지 모형 선언 시 적용되는 입력 변수 내부 자체 정규화 조절 인자($\alpha$)를 조금씩 튜닝해가면서 에러율 RSS 반환점 변화가 어떤 로깅 궤적을 거치는지 관찰합니다.

### Fast Cross-Validation for Solution Paths (솔루션 결괏값 추적을 위한 고속 교차 검증)
* [문서로 이동하기](./6_5_2_2_fast_cross-validation_for_solution_paths/)

### The Lasso (라쏘 페널티 회귀 분석 모의 구현)

가장 손실을 이상적으로 줄여주는 매개변수 $\alpha$ 혹은 $\lambda$를 컴퓨터 연산 파워를 통해 찾기 위해 `RidgeCV` 객체, `LassoCV` 내장 속성의 사용법을 시뮬레이터로 알아봅니다.
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_2_ridge_regression_and_the_lasso\trans1.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)

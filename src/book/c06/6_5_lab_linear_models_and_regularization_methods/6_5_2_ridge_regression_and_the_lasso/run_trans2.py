import codecs

content = r"""---
layout: default
title: "trans2"
---

# 6.5.2 능선 회귀와 라쏘 정규화 (Ridge Regression and the Lasso)

We will use the `sklearn.linear_model` package (for which we use `skl` as shorthand below) to fit ridge and lasso regularized linear models on the `Hitters` data. We start with the model matrix `X` (without an intercept) that we computed in the previous section on best subset regression.
이번 랩 실습 스테이지 무대에서도 `Hitters` 프로 야구 선수 성적 데이터 묶음을 쉴 틈 없이 굴려 볼 것입니다. 우린 여기서 막강한 '능선 회귀(ridge)' 기법과 올가미 밧줄을 던지는 '라쏘(lasso)'라고 불리는 무지막지한 강제 정규화(regularized) 모의 선형 회귀 모델 모형을 구동시켜 데이터를 무단 적합 구축해 보기 위해, 강력 엔진 패키지 모듈인 `sklearn.linear_model` 파이썬 내장 라이브러리를 끌어다 사용할 생각입니다 (명령어 가독성 편의를 우선하기 위해, 이어질 하단 본문 코드 기록창부터는 이 길고 귀찮게 뻗은 패키지 호출 명칭 꼬리표를 편안하게 단 세 글자인 `skl` 이라는 임의 단축 지정 축약칭으로 바꿔 호명해 부르겠습니다). 작업 기차의 첫 착수 출발선은, 운 좋게도 바로 직전 실습 파트 구역의 '최선 부분집합 관제 회귀 단원'에서 앞서 열심히 공들여 머리 써서 도출해 내고 계산해 두었던 원천 매트릭스 `X` 데이터 모형판(편향 상숫값 절편인 intercept 포지션이 아주 깔끔하게 전부 도려내져 빠져있는 상태판)에서부터 그 바통을 이어받아 잡고 연산 모의 작업 기차를 엔진 출발시킵니다.

---

## Sub-Chapters (하위 랩 코딩 실습 과정 요약)

### Ridge Regression (릿지 페널티 회귀 분석 결과 도출 점검)
* [문서로 이동하기](./6_5_2_1_ridge_regression/)

릿지 모형 선언 가동 시 필연적으로 개입 적용되는 입력 변수 내부의 자체 패널티 강도 정규화 조절 인자($\alpha$) 수치를 요리조리 조금씩 튜닝 조작해 가면서, 에러율 RSS 반환점 변화가 어떤 기가 막힌 로깅 궤적 변화를 거치는지 한눈에 관찰합니다.

### Fast Cross-Validation for Solution Paths (최적 라인을 잡기 위한 체인 고속 교차 검증)
* [문서로 이동하기](./6_5_2_2_fast_cross-validation_for_solution_paths/)

### The Lasso (라쏘 페널티 회귀 분석 모의 구현)

가장 손실을 이상적으로 줄여 억눌러 주는 마법의 매개변수 값 $\alpha$ 혹은 $\lambda$ 지점을 컴퓨터 엔진 연산 파워를 통해 무식하게 밀고 찾아내기 위해, `RidgeCV` 객체, 그리고 `LassoCV` 내장 속성이 뽐내는 사용법을 시뮬레이터 차원에서 알아봅니다.
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_2_ridge_regression_and_the_lasso\trans2.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)

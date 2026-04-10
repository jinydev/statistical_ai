---
layout: default
title: "index"
---

# 3.6 Lab: Linear Regression 

---

## Sub-Chapters (하위 목차)

### 3.6.1 Importing packages (패키지 불러오기)
* [문서로 이동하기](./3_6_1_importing_packages/)

회귀 실습에 필수적인 Pandas, NumPy, Statsmodels 등의 데이터 과학 최적화 패키지를 초기 설정하는 코드를 보여줍니다.
가장 기본적인 파이썬 통계 모델링 라이브러리를 임포트합니다.

### 3.6.2 Simple Linear Regression (단순 선형 회귀 실습)
* [문서로 이동하기](./3_6_2_simple_linear_regression/)

보스턴 주택 데이터셋을 파이썬에 로드하고 단순 선형 회귀 모형에 적합시키는 1차적인 워크플로우를 익힙니다.
`summary()` 함수를 통해 상세한 통계 리포트를 도출하는 방법을 점검합니다.

### 3.6.3 Multiple Linear Regression (다중 선형 회귀 실습)
* [문서로 이동하기](./3_6_3_multiple_linear_regression/)

여러 예측 변수를 한꺼번에 통계식(Formula)에 투입하여 다중 선형 회귀 분석 스크립트를 작성하는 방법을 익힙니다.
P-value를 확인하며 변수 간 중요도를 실제로 평가합니다.

### 3.6.4 Multivariate Goodness of Fit (다변량 적합도)
* [문서로 이동하기](./3_6_4_multivariate_goodness_of_fit/)

다중 회귀 구조에서 변수 간 영향을 판단하는 VIF 구조 검증 등 다변량 모델의 건전성을 파이썬 코드로 평가합니다.
전반적인 모델 성과를 다양한 각도에서 시각화, 평가합니다.

### 3.6.5 Interaction Terms (상호작용 항 실습)
* [문서로 이동하기](./3_6_5_interaction_terms/)

파이썬 statsmodels의 수식 문자열 체계에서 `X1 * X2`라는 간단한 기호를 사용해 상호작용 항을 모델에 추가하는 기법을 실습합니다.
변수 쌍의 시너지 영향력을 실증적으로 체크합니다.

### 3.6.6 Non-linear Transformations of the Predictors (예측 변수의 비선형 변환 실습)
* [문서로 이동하기](./3_6_6_non-linear_transformations_of_the_predictors/)

예측 변수에 다항식(제곱) 연산 처리나 로그 처리를 기입하여 비선형 곡선을 적합하는 테크닉을 코딩으로 확인합니다.
단순 직선 이상의 데이터를 맞추는 방법을 배웁니다.

### 3.6.7 Qualitative Predictors (정성적 예측 변수 실습)
* [문서로 이동하기](./3_6_7_qualitative_predictors/)

범주형/정성적 변수가 데이터셋에 섞여 있을 때 더미 변수(Dummy Variable)가 파이썬 상에서 어떻게 내부적으로 코딩되어 회귀분석되는지 구조를 파악합니다.
더미 코딩의 참조 클래스(Reference Class)를 이해합니다.

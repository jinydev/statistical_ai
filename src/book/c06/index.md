---
layout: default
title: "6. Linear Model Selection and Regularization"
---

# 6. Linear Model Selection and Regularization (선형 모델 선택 및 규제)

전통적인 최소 제곱법 기준의 선형 모델이 가지는 한계(해석력 저하, 높은 분산)를 극복하기 위한 대안을 다루는 6장입니다.
모델의 복잡도를 줄여 예측 정확도를 높이는 부분집합 선택과 라쏘/릿지 같은 규제(Regularization) 방법론을 배웁니다.

## 6.1 Subset Selection (부분집합 선택)
* [문서로 이동하기](./6_1_subset_selection/)

오리지널 예측 변수(X) 전체를 쓰지 않고 반응 변수(Y)와 진정으로 관련이 깊은 일부 변수들만 골라내어 모델을 피팅하는 원리입니다.
직관적인 변수 덜어내기를 통해 모델의 해석 가능성을 크게 개선합니다.

### 6.1.1 Best Subset Selection (최적 부분집합 선택)
* [문서로 이동하기](./6_1_subset_selection/6_1_1_best_subset_selection/)

변수가 $p$개일 때 만들 수 있는 모든 조합($2^p$개)의 모델을 전부 적합해보고 가장 우수한 하나를 시도하는 무차별 대입 방식입니다.

#### Algorithm 6.1 Best subset selection (알고리즘 6.1 최적 부분집합 선택)
* [문서로 이동하기](./6_1_subset_selection/6_1_1_best_subset_selection/6_1_1_1_algorithm_6.1_best_subset_selection/)

모든 K크기의 변수 조합에서 가장 좋은 모델을 기록하고, 최종적으로 Cross-Validation이나 AIC/BIC 평가지표로 모델 1개를 선정하는 절차입니다.

### 6.1.2 Stepwise Selection (단계적 선택법)
* [문서로 이동하기](./6_1_subset_selection/6_1_2_stepwise_selection/)

최적 부분집합의 거대한 컴퓨팅 연산의 낭비와 과적합 위험을 회피하고자, 하나씩 변수를 더하거나 빼는 탐욕적(Greedy) 방식의 선별법입니다.

#### Forward Stepwise Selection (전진 단계 선택법)
* [문서로 이동하기](./6_1_subset_selection/6_1_2_stepwise_selection/6_1_2_1_forward_stepwise_selection/)

데이터에 아무 변수가 없는 빈(Null) 모델에서 출발하여 모델 성능을 가장 유의미하게 향상시키는 변수를 한 번에 하나씩만 추가하는 경제적 방식입니다.

#### Hybrid Approaches (혼합 접근법)
* [문서로 이동하기](./6_1_subset_selection/6_1_2_stepwise_selection/6_1_2_2_hybrid_approaches/)

전진 추가와 후진 제거(Backward)를 양방향 결합하여, 유의미해 보였지만 다른 변수 편입으로 불필요해진 변수를 추후에 제거해 내는 유연한 방식입니다.

### 6.1.3 Choosing the Optimal Model (최적 모델 선택)
* [문서로 이동하기](./6_1_subset_selection/6_1_3_choosing_the_optimal_model/)

훈련 에러(RSS, R²)만으로는 변수가 늘어날수록 무조건 오차가 줄어드는 착시가 있기에, 실질 테스트 에러를 가늠할 독립적 지표 체계가 필요함을 배웁니다.

#### Cp, AIC, BIC, and Adjusted R² (Cp, AIC, BIC 및 조정된 R²)
* [문서로 이동하기](./6_1_subset_selection/6_1_3_choosing_the_optimal_model/6_1_3_1_cp_aic_bic_and_adjusted_r2/)

변수가 하나씩 추가될 때마다 수학적인 페널티(Penalty)를 부과하여, 쓸모 없는 다수 변수로 인한 과적합을 막고 모델 간 공정한 비교를 유도하는 평가 지표입니다.

#### Validation and Cross-Validation (검증 세트 및 교차 검증)
* [문서로 이동하기](./6_1_subset_selection/6_1_3_choosing_the_optimal_model/6_1_3_2_validation_and_cross-validation/)

이론적 지표식(AIC 등)에 의존하지 않고 데이터를 직접 분할하여 시험을 치르는 가장 검증된 모형 선택 방식인 크로스 밸리데이션(CV)을 다시 가져옵니다.

## 6.2 Shrinkage Methods (축소 기법)
* [문서로 이동하기](./6_2_shrinkage_methods/)

모든 변수를 버리지 않고 포함하되, 반응 모델 기여도가 떨어지는 변수의 계수를 0 에 가깝게 억제(Shrink)시켜 모델 분산을 대폭 감소시키는 강력한 정규화 기법입니다.

### 6.2.1 Ridge Regression (릿지 회귀)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_1_ridge_regression/)

기존 잔차 제곱합에 파라미터 계수 값 제곱의 합($L_2$ 페널티)을 최소화 조건으로 덧붙여, 중요치 않은 계수가 비정상적으로 팽창하는 현상을 누그러뜨리는 기법입니다.

#### An Application to the Credit Data (신용 데이터 적용 사례)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_1_ridge_regression/6_2_1_1_an_application_to_the_credit_data/)

은행 신용도 데이터셋에 릿지 함수를 튜닝했을 때 변수들의 계수값이 조율 파라미터 $\lambda$의 상승에 따라 어떻게 부드럽게 감쇠하는지 등고 플롯으로 확인합니다.

### 6.2.2 The Lasso (라쏘 회귀 방법)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_2_the_lasso/)

릿지와 달리, 파라미터 계수의 절댓값의 합($L_1$ 페널티)을 사용함으로써 상대적으로 잉여 변수인 계수를 완전히 0으로 만들어 자동 변수 소거(Selection) 기능까지 수행합니다.

#### The Variable Selection Property of the Lasso (라쏘의 변수 선택 특성 메커니즘)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_2_the_lasso/6_2_2_1_the_variable_selection_property_of_the_lasso/)

어떻게 라쏘가 계수를 정확히 0으로 타겟 쳐내주어 희소(Sparse)한 모델을 기하학적으로 생성하는지, 그 수학적 원리를 마름모 궤적으로 시각화하여 관찰합니다.

#### Comparing the Lasso and Ridge Regression (라쏘와 릿지 회귀의 구조적 차이 비교)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_2_the_lasso/6_2_2_2_comparing_the_lasso_and_ridge_regression/)

소수의 변수만 반응에 유의미할 땐 라쏘가, 다수 변수들이 전반적으로 미세하게 얽혀 영향을 미칠 땐 릿지가 상대적으로 유리할 가능성이 높다는 구도를 설명합니다.

#### A Simple Special Case for Ridge Regression and the Lasso (릿지와 라쏘의 특수한 교안 사례)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_2_the_lasso/6_2_2_3_a_simple_special_case_for_ridge_regression_and_the_lasso/)

변수 행렬 데이터 디자인이 완벽한 상호 직교(Orthogonal) 구조라 가정할 때, 두 기법 방식이 원래 OLS 선형 회귀 계수 추정값을 어떻게 소프트/하드로 깎는지 단순화해 증명합니다.

### 6.2.3 Selecting the Tuning Parameter (최적 조율 파라미터 탐색)
* [문서로 이동하기](./6_2_shrinkage_methods/6_2_3_selecting_the_tuning_parameter/)

수축의 강도를 가장 적합하게 조절하는 초매개변수 $\lambda$ 값을 경험이 아닌 데이터를 기반으로 도출하기 위하여 순수 모델 교차 검증을 동원합니다.

## 6.3 Dimension Reduction Methods (차원 축소 기법 분석)
* [문서로 이동하기](./6_3_dimension_reduction_methods/)

높은 차원의 원래 입력 변수들을 소규모 예측 변수들의 선형 조합 형태(새로운 인공적 핵심 변수 집단)로 변환 가공한 뒤 선형 모델에 편입시키는 방법론입니다.

### 6.3.1 Principal Components Regression (주성분 중심 회귀 기법)
* [문서로 이동하기](./6_3_dimension_reduction_methods/6_3_1_principal_components_regression/)

원래의 변수 행렬들이 지닌 정보량(Variance)을 가장 거대하게 포괄하는 주성분 벡터(Principal Component) 방향을 찾아 그것만을 선형 모델 인스턴스 X 요인으로 사용합니다.

#### An Overview of Principal Components Analysis (주성분 분석 핵심 통찰 개요)
* [문서로 이동하기](./6_3_dimension_reduction_methods/6_3_1_principal_components_regression/6_3_1_1_an_overview_of_principal_components_analysis/)

고도로 연관된 다중 변수들을 데이터 정보 손실 없이 상호 완전히 독립적인(직교) 변수로 압축 변환하는 비지도 분해 기초 기술인 PCA의 성질을 직관적으로 살펴봅니다.

#### The Principal Components Regression Approach (주성분 기반 데이터 회귀 접근 과정)
* [문서로 이동하기](./6_3_dimension_reduction_methods/6_3_1_principal_components_regression/6_3_1_2_the_principal_components_regression_approach/)

PCA를 이용해 만들어진 Top랭크 다차원 벡터가 타겟 Y 예측 또한 가장 이상적으로 잡아낸다는 강력한 논리 하에, 회귀 모델 내부 분산 확장을 극도로 통제하는 효과입니다.

### 6.3.2 Partial Least Squares (부분 최소 제곱법, PLS)
* [문서로 이동하기](./6_3_dimension_reduction_methods/6_3_2_partial_least_squares/)

X 행렬 내의 독립적 변동성만 보는 PCA를 보완해, 처음 차원 추출부터 반응 변수 Y 그룹과의 상관성이 높은 쪽 방향으로만 유도하는 지도(Supervised) 기반의 차원 축소법입니다.

## 6.4 Considerations in High Dimensions (초고차원 환경 분석 구조에서의 한계점과 고려사항)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/)

변수의 갯수 컬럼 차원 $p$가 데이터 행 관측치 갯수인 $n$보다 크거나 매우 가까운 현대 빅데이터 및 생물정보 데이터 포맷 등 특수 모델 세팅에서 발생 가능한 이슈들입니다.

### 6.4.1 High-Dimensional Data (고차원 데이터)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/6_4_1_high-dimensional_data/)

고전 통계학과 확연히 시대성이 구분되는 빅데이터, 고해상도 정보 데이터의 기원(초 미세 의료 진단기기, 검색 엔진 로그 등)과 극도로 빈약한 관측치 모델 속성을 이야기합니다.

### 6.4.2 What Goes Wrong in High Dimensions? (고차원에서 발생 가능한 고질적 부작용들)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/6_4_2_what_goes_wrong_in_high_dimensions/)

예측 변수 $p$가 행 자료수치 $n$보다 크게 되면, 기존의 OLS 최소제곱법이 모든 노이즈 패턴 데이터마저 완벽 무결하게 암기 적합해 버려 결국 모델 일반화를 망치는 이유입니다.

### 6.4.3 Regression in High Dimensions (모델 선택과 축소로 고차원 회귀 대응하기)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/6_4_3_regression_in_high_dimensions/)

앞선 장에서 학습한 라쏘, 릿지 페널티, 부분 집합 축소 전개법이 고차원 다수 변수의 매개 자유도를 가혹할 정도록 억제하기에 오히려 최적의 처방약이 될 수 있는 유효 메커니즘을 증명합니다.

### 6.4.4 Interpreting Results in High Dimensions (고차원 분석 결과의 지나친 맹신 방지와 해석 윤리 주의사항)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/6_4_4_interpreting_results_in_high_dimensions/)

방대하고 유연한 변수들 끼리는 고도의 내부 공선성을 띨 다중공선성 확률 구조가 압도적이라는 사실을 배우며, 어떤 변수가 뽑혀도 대안 중 하나에 불과하며 완전한 결론이라 단정짓지 말아야 함을 안내합니다.

## 6.5 Lab: Linear Models and Regularization Methods (실습: 데이터 사이언티스트를 위한 파이썬 선형 모델 선택 및 규제법 랩)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/)

파이썬 오픈소스 프레임워크인 Scikit-Learn을 베이스로 유명 메이저 데이터셋 중 하나인 하터 힛터(Hitters=미국 프로 야구선수 정보 기록) 데이터를 랩 환경에 로드합니다.

### 6.5.1 Subset Selection Methods (부분집합 자동 선택 메서드 툴박스 파이썬 실습)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_1_subset_selection_methods/)

사이킷런 및 기타 파생 알고리즘 툴킷의 다차원 검정, 모델 AIC, BIC 에러율 식을 직접 가동하기 위한 평가 함수들을 구성하여 변수 중요도 서치 과정을 콘솔 위에서 구현해 봅니다.

#### Forward Selection (전역 전진 선택법 알고리즘 파이썬 실습)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_1_subset_selection_methods/6_5_1_1_forward_selection/)
* (Jupyter Output 결과 행렬 1) [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_1_subset_selection_methods/6_5_1_1_out4_263_20/)
* (Jupyter Output 시각화 축 단위 제어) [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_1_subset_selection_methods/6_5_1_1_ax.setylim50000250000/)
사용자의 데이터 분석을 돕도록 모델의 자체 스코어를 루프문에서 계속 기록하며 최고 기여 변수를 골라나가는 알고리즘 코드 구문을 디버그 포맷으로 체험합니다.

### 6.5.2 Ridge Regression and the Lasso (파이썬 릿지 정규화 및 라쏘 분석기 실전 적용 사례)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_2_ridge_regression_and_the_lasso/)

Scikit-Learn 기계학습 모듈 라이브러리의 `Ridge` 클래스 인스턴스와 `Lasso` 클래스를 불러와 알파 스펙트럼(패널티 강도)에 따른 파라미터 변화선 궤적을 렌더링하고 실전 성능 측정 및 시각화를 완료합니다.

#### Ridge Regression (릿지 페널티 회귀 분석 결과 도출 점검)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_2_ridge_regression_and_the_lasso/6_5_2_1_ridge_regression/)
* (Jupyter Output RSS 에러 반환 스코어) [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_2_ridge_regression_and_the_lasso/6_5_2_1_out30_array134214.0/)
* (Jupyter Output 잔차 제곱 변화 반환 스코어) [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_2_ridge_regression_and_the_lasso/6_5_2_1_out31_array231788.32/)
릿지 모형 선언 시 적용되는 입력 변수 내부 자체 정규화 조절 인자($\alpha$)를 조금씩 튜닝해가면서 에러율 RSS 반환점 변화가 어떤 로깅 궤적을 거치는지 관찰합니다.

#### Fast Cross-Validation for Solution Paths (최적의 파라미터 라인을 잡기 위한 체인 고속 교차 검증)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_2_ridge_regression_and_the_lasso/6_5_2_2_fast_cross-validation_for_solution_paths/)
* [The Lasso](./39_the_lasso/)
가장 손실을 이상적으로 줄여주는 매개변수 $\alpha$ 혹은 $\lambda$를 컴퓨터 연산 파워를 통해 찾기 위해 `RidgeCV` 객체, `LassoCV` 내장 속성의 사용법을 시뮬레이터로 알아봅니다.

### 6.5.3 PCR and PLS Regression (빅데이터 차원 축소 후 연산, PCR-주성분 기반 회귀 실습)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_3_pcr_and_pls_regression/)

PCA 분해 패키지 모듈을 전처리용으로 앞단에 파이프라인 결합한 후 원 주성분 변수를 차원 컷 스코어로 변환, 그리고 그걸 후단 최종 선형회귀 모델에 태우는 세련된 기계학습 테크닉 과정을 체득합니다.

#### Jupyter Notebook Output (결과 통계학적 반환값 확인 점검)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/6_5_3_pcr_and_pls_regression/6_5_3_1_out53_204139.31/)
Jupyter에서 출력되는 파이썬 콘솔의 테스트 평균 제곱근 오차(MSE) 지표 통계를 확인하며, 규제기법을 동원하지 않은 일반 선형회귀 및 라쏘 모델 성능과의 퍼포먼스 우위를 교차 비교합니다.

## 6.6 Exercises (변수 축소 기법들의 기본 응용 문제 수리적 종합 지식 검증 코스 모음집)
* [문서로 이동하기](./6_6_exercises/)

데이터 파라미터와 관측치가 제한적이거나 불균형한 고도의 복잡 다차원 세팅 환경 속에서 페널티 모델 선택 통계 지표 함수를 도출하거나, 툴박스로 직접 계산 검증해보는 심화 과제 실습장입니다.

### Conceptual (통계 지표 변동성 개념 이해 문제 풀이 모음 구역)
* [문서로 이동하기](./6_6_exercises/6_6_1_conceptual/)

베스트 서브셋 전체 부분집합 탐색 알고리즘들의 처리 방식과 라쏘 L1 제약 방정식의 절대값 절편 한계점들을, 통계 라그랑주 승수 그래프 교점이라는 기하학 기반 시선으로 이해하도록 문제를 요구합니다.

### Applied (컴플렉시티 데이터를 조작하여 해결하는 응용 파이썬 노트북 문제 풀이 지대 모음 결합 구역)
* [문서로 이동하기](./6_6_exercises/6_6_2_applied/)
* [수식 관련 부가 레퍼런스 공식 문서 연동 데이터 지표 정보](./45_y_x/)

실제 난수 스크립트로 임의로 설정한 수식 방정식들(`np.random`)에 무작위 3차원 이상 항들을 뒤죽박죽으로 연계시킨 다이나믹 데이터 구조 후, OLS 선형/가법/릿지 스펙트럼 등이 노이즈를 식별해 원래 수식을 뽑아내는지 확인하는 등 깊은 지식을 판별합니다.

---
layout: default
title: "4. Classification"
---

# 4. Classification (분류)

반응 변수(Y)가 수치형이 아니라 범주형(카테고리)일 때 사용하는 분류(Classification) 방법론을 다루는 4장입니다.
로지스틱 회귀, 선형 판별 분석(LDA), 로지스틱 회귀를 넘어서는 K-최근접 이웃(KNN) 등을 포괄적으로 배웁니다.

## 4.1 An Overview of Classification (분류의 개요)
* [문서로 이동하기](./4_1_an_overview_of_classification/)

사기 탐지, 의료 진단 등 관측치가 속할 카테고리/클래스를 예측하는 분류 문제의 현실적인 사례들을 소개합니다.
회귀 방식과는 본질적으로 다른 통계적 접근이 필요함을 설명합니다.

## 4.2 Why Not Linear Regression? (왜 선형 회귀를 쓰면 안 되는가?)
* [문서로 이동하기](./4_2_why_not_linear_regression/)

범주형 반응 변수에 선형 회귀 모형을 그대로 적용했을 때 확률이 0 미만이나 1 초과로 산출되는 수학적 모순을 살펴봅니다.
선형 모델이 이산적 클래스 경계에서 가지는 직관적인 한계를 설명합니다.

## 4.3 Logistic Regression (로지스틱 회귀)
* [문서로 이동하기](./4_3_logistic_regression/)

확률이 항상 0과 1 사이에 존재하도록 로지스틱 함수(Sigmoid)를 모델화하여 질적 반응 변수를 예측하는 기법입니다.
가장 보편적인 이진 분류기 중 하나인 최댓값 가능도 추정의 기초를 다룹니다.

### 4.3.1 The Logistic Model (로지스틱 모형)
* [문서로 이동하기](./4_3_logistic_regression/4_3_1_the_logistic_model/)

오즈(Odds)와 로짓(Logit) 변환을 선형 함수와 매핑해 로지스틱 모형을 구축하는 수식을 유도합니다.
수학적으로 선형 관계가 로그 오즈 단위에서 성립함을 살펴봅니다.

### 4.3.2 Estimating the Regression Coefficients (회귀 계수 추정)
* [문서로 이동하기](./4_3_logistic_regression/4_3_2_estimating_the_regression_coefficients/)

관측된 데이터가 나올 확률을 최대로 만드는 최대 우도 추정법(Maximum Likelihood Estimation)을 배웁니다.
로지스틱 회귀에서 손실을 어떻게 최소화하는지 식별합니다.

### 4.3.3 Making Predictions (예측하기)
* [문서로 이동하기](./4_3_logistic_regression/4_3_3_making_predictions/)

추정된 계수를 바탕으로 특정 주어진 특성값 하에서 어떠한 클래스에 속할 확률을 수식과 파이썬 코드로 도출하는 방법입니다.
특정 임계값(Threshold)을 넘는 타겟을 분류 예측합니다.

### 4.3.4 Multiple Logistic Regression (다중 로지스틱 회귀)
* [문서로 이동하기](./4_3_logistic_regression/4_3_4_multiple_logistic_regression/)

예측 변수(X)가 여러 개인 경우로 확장하여, 교란 변수 효과와 복잡한 요인 분석을 동시에 수행하는 방법을 다룹니다.
조건부 확률에 여러 변수가 미치는 영향을 검토합니다.

### 4.3.5 Multinomial Logistic Regression (다항 로지스틱 회귀)
* [문서로 이동하기](./4_3_logistic_regression/4_3_5_multinomial_logistic_regression/)

타겟 클래스가 2개를 넘어 3개 이상(예: 질병 3종류 분류)일 때 적용할 수 있도록 로지스틱 회귀 모델 체계를 통계적으로 확장합니다.

## 4.4 Generative Models for Classification (분류를 위한 생성 모델)
* [문서로 이동하기](./4_4_generative_models_for_classification/)

각 클래스에 속하는 예측 변수들의 분포(Distribution)를 역으로 추정하여 베이즈 정리를 통해 소속 확률을 찾아내는 방식을 봅니다.
로지스틱 회귀가 샘플 크기 한계로 불안정해질 수 있는 상황을 극복합니다.

### 4.4.1 Linear Discriminant Analysis for p = 1 (p=1인 경우의 선형 판별 분석)
* [문서로 이동하기](./4_4_generative_models_for_classification/4_4_1_linear_discriminant_analysis_for_p_1/)

예측 변수가 단 1개일 때 정규 분포 기반으로 각 클래스의 평균과 통일된 분산을 추정하여 집단을 판별(LDA)하는 과정입니다.

### 4.4.2 Linear Discriminant Analysis for p > 1 (p>1인 경우의 선형 판별 분석)
* [문서로 이동하기](./4_4_generative_models_for_classification/4_4_2_linear_discriminant_analysis_for_p_1/)

여러 개의 차원 특성이 존재할 때 다변량 정규 분포를 가정하여, 클래스 간 선형 경계를 세우는 보편적 LDA 확장 파트입니다.

#### ROC Curve (ROC 곡선)
* [문서로 이동하기](./4_4_generative_models_for_classification/4_4_2_linear_discriminant_analysis_for_p_1/4_4_2_1_roc_curve/)

분류 판별에서 임계값(Threshold)을 변화시켰을 때 민감도(Sensitivity)와 1-특이성(Specificity) 관계가 변하는 것을 보여주는 성능 확인용 곡선입니다.

### 4.4.3 Quadratic Discriminant Analysis (이차 판별 분석)
* [문서로 이동하기](./4_4_generative_models_for_classification/4_4_3_quadratic_discriminant_analysis/)

각 클래스가 공통된 행렬이 아닌 고유한 개별 분산/공분산 행렬을 가진다고 가정함으로써, 경계를 다소 유연한 2차 곡선(QDA)으로 유도합니다.

### 4.4.4 Naive Bayes (나이브 베이즈)
* [문서로 이동하기](./4_4_generative_models_for_classification/4_4_4_naive_bayes/)

모든 차원의 변수들이 클래스 내에서 서로 완벽히 독립적이라는 강력한 가정하에 곱 확률로 쉽고 빠르게 연산하는 고전 분류기입니다.

## 4.5 A Comparison of Classification Methods (분류 방법들 간의 비교)
* [문서로 이동하기](./4_5_a_comparison_of_classification_methods/)

지금까지 배운 LDA, QDA, 나이브 베이즈, 로지스틱 회귀, 그리고 비모수적 기법인 KNN 간의 성능과 수리적 연관성을 검토합니다.

### 4.5.1 An Analytical Comparison (분석적 비교)
* [문서로 이동하기](./4_5_a_comparison_of_classification_methods/4_5_1_an_analytical_comparison/)

로지스틱 회귀와 LDA가 선형 결정 경계를 사용한다는 점에서 수식의 어느 파트가 동치 결론을 내리게 되는지 증명합니다.

### 4.5.2 An Empirical Comparison (실증적 비교)
* [문서로 이동하기](./4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/)

여러 가상/현실 시나리오 상황을 통해 각 분류기들을 테스트해 보면서, 모델의 편향-분산 양상에 따라 어떤 환경에서 누가 유리한지 체크합니다.

## 4.6 Generalized Linear Models (일반화 선형 모델)
* [문서로 이동하기](./4_6_generalized_linear_models/)

정규 분포(선형)와 이항 분포(로지스틱) 구조를 모두 단일 수학 체계로 일반화하는 뼈대인 GLM(Generalized Linear Models) 기초 이론입니다.

### 4.6.1 Linear Regression on the Bikeshare Data (자전거 대여 데이터에서의 선형 회귀 적용)
* [문서로 이동하기](./4_6_generalized_linear_models/4_6_1_linear_regression_on_the_bikeshare_data/)

카운트(음수가 불가능한 건수 데이터) 성질을 갖는 대여량에 일반 선형 회귀를 돌렸을 때 발생하는 음수 예측 등 불합리한 점을 확인합니다.

### 4.6.2 Poisson Regression on the Bikeshare Data (자전거 대여 데이터에서의 포아송 회귀 적용)
* [문서로 이동하기](./4_6_generalized_linear_models/4_6_2_poisson_regression_on_the_bikeshare_data/)

카운트 데이터의 속성에 알맞게 부합하는 분포인 포아송(Poisson) 회귀 모델을 적용, 로그 링크 함수를 사용해 효과적인 성능을 얻습니다.

### 4.6.3 Generalized Linear Models in Greater Generality (보다 넓은 범주의 GLM 일반화 규칙)
* [문서로 이동하기](./4_6_generalized_linear_models/4_6_3_generalized_linear_models_in_greater_generality/)

응답 패턴 군집(Exponential family) 개념을 통해 포아송, 이항 회귀, 정규 회귀 등이 결국 매개 변수만 다른 통일된 GLM 형식임을 증명합니다.

## 4.7 Lab: Logistic Regression, LDA, QDA, and KNN (실습: 로지스틱, 판별분석, KNN)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/)

파이썬의 Scikit-learn과 Statsmodels 라이브러리를 이용해 주식 시장(Smarket) 데이터를 통한 분류 모델 파이프라인 실전 구축 코딩 랩입니다.

### 4.7.1 The Stock Market Data (Smarket 주식 정보 데이터 세팅)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_1_the_stock_market_data/)

실습 재료가 될 주가 상단/하향 추세 데이터를 로드하고 상관행렬과 페어 플롯, 기초 정보 요약 통계를 코드 셀로 점검합니다.

### 4.7.2 Logistic Regression (로지스틱 회귀 분석 실습)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_2_logistic_regression/)

`sm.Logit()` 등을 통해 주식 방향(Up/Down) 확률 예측 이진 모델을 훈련하고, 혼동 행렬(Confusion Matrix)을 추출해 평가율을 확인합니다.

#### Jupyter Notebook Output (노트북 출력 결과)
* 파라미터 반환: [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_2_logistic_regression/4_7_2_1_in_8_results.params/)
* 예측치 행렬 출력: [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_2_logistic_regression/4_7_2_1_out13_0.5216_0.5216/)
* 차원 출력: [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_2_logistic_regression/4_7_2_1_out14_252_9/)
파이썬 분류 코드 실행 후 콘솔에서 튀어나오는 모델 객체 크기나 정확도 반환값들에 대해 해석력을 점검합니다.

### 4.7.3 Linear Discriminant Analysis (선형 판별 분석 실습)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_3_linear_discriminant_analysis/)

`DiscriminantAnalysis` 패키지를 이용해 클래스들의 사전 확률과 성분 중심 평균을 추정하고 판별 공간에서 모델 객체를 훈련합니다.

#### 사전 확률 점검 (Jupyter Notebook Output)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/)
LDA 실행 후 도출된 집단 사전 확률 및 로직이 타당한지 간단한 불 값(True/False) 출력 테스트를 점검합니다.

### 4.7.4 Quadratic Discriminant Analysis (QDA 모델 실습)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_4_quadratic_discriminant_analysis/)

QDA 클래스 객체를 선언하여 다소 더 유연한 2차 함수 경계를 탐색함으로써, LDA에 비해 모델 스코어가 개선되는지 검증합니다.

### 4.7.6 K-Nearest Neighbors (KNN 분류 실습)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_6_k-nearest_neighbors/)

머신런 모듈의 `KNeighborsClassifier`를 불러와 공간 유사 거리 기반의 예측 스코어를 도출하고 K 수를 재조율하는 작업을 실습합니다.

### 4.7.7 Linear and Poisson Regression on the Bikeshare Data (Bikeshare 포아송 회귀 실습)
* [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/)

GLM 통계 모듈 체계 안에 있는 Poisson Family 함수 매개변수를 직접 입력해, 자전거 대여 카운트 모형을 코딩으로 피팅합니다.

#### GLM Output (포아송 분석 결과)
* P-value 점검: [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/4_7_7_1_out69_1.53e-20/)
* 함수 설명서 요약: [문서로 이동하기](./4_7_lab_logistic_regression_lda_qda_and_knn/4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/4_7_7_1_poisson_regression/)
GLM 결과 안보드에서 계수 유의성을 입증하는 잔차 로그 수치와 P-value 들을 파싱해 점검합니다.

## 4.8 Exercises (연습 문제)
* [문서로 이동하기](./4_8_exercises/)

제시된 분류 모델 파이프라인의 핵심 모순, 그리고 여러 오픈 데이터 환경 상에서 혼동 행렬을 직접 출력해내는 실기/이론 코스입니다.

### Conceptual (개념 문제)
* [문서로 이동하기](./4_8_exercises/4_8_1_conceptual/)

로지스틱 식이 어떻게 선형 로그 오즈(Log-Odds) 방정식이 되는지 증명하고, 한쪽의 에러율만 보정하려 할 때 나타날 수리적 모순을 정리합니다.

### Applied (응용 문제)
* [문서로 이동하기](./4_8_exercises/4_8_2_applied/)

새로운 현실 데이터 프레임을 자유롭게 조작하여 나이브 베이즈, 로지스틱 회귀 알고리즘들의 성능 비교 ROC 커브를 직접 도출하는 실전 검증 코스입니다.

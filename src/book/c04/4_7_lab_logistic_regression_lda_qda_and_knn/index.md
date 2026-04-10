---
layout: default
title: "index"
---

# 4.7 Lab: Logistic Regression, LDA, QDA, and KNN 

---

## Sub-Chapters (하위 목차)

### 4.7.1 The Stock Market Data (Smarket 주식 정보 데이터 세팅)
* [문서로 이동하기](./4_7_1_the_stock_market_data/)

실습 재료가 될 주가 상단/하향 추세 데이터를 로드하고 상관행렬과 페어 플롯, 기초 정보 요약 통계를 코드 셀로 점검합니다.

### 4.7.2 Logistic Regression (로지스틱 회귀 분석 실습)
* [문서로 이동하기](./4_7_2_logistic_regression/)

`sm.Logit()` 등을 통해 주식 방향(Up/Down) 확률 예측 이진 모델을 훈련하고, 혼동 행렬(Confusion Matrix)을 추출해 평가율을 확인합니다.

### 4.7.3 Linear Discriminant Analysis (선형 판별 분석 실습)
* [문서로 이동하기](./4_7_3_linear_discriminant_analysis/)

`DiscriminantAnalysis` 패키지를 이용해 클래스들의 사전 확률과 성분 중심 평균을 추정하고 판별 공간에서 모델 객체를 훈련합니다.

### 4.7.4 Quadratic Discriminant Analysis (QDA 모델 실습)
* [문서로 이동하기](./4_7_4_quadratic_discriminant_analysis/)

QDA 클래스 객체를 선언하여 다소 더 유연한 2차 함수 경계를 탐색함으로써, LDA에 비해 모델 스코어가 개선되는지 검증합니다.

### 4.7.6 K-Nearest Neighbors (KNN 분류 실습)
* [문서로 이동하기](./4_7_6_k-nearest_neighbors/)

머신런 모듈의 `KNeighborsClassifier`를 불러와 공간 유사 거리 기반의 예측 스코어를 도출하고 K 수를 재조율하는 작업을 실습합니다.

### 4.7.7 Linear and Poisson Regression on the Bikeshare Data (Bikeshare 포아송 회귀 실습)
* [문서로 이동하기](./4_7_7_linear_and_poisson_regression_on_the_bikeshare_data/)

GLM 통계 모듈 체계 안에 있는 Poisson Family 함수 매개변수를 직접 입력해, 자전거 대여 카운트 모형을 코딩으로 피팅합니다.

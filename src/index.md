---
layout: default
title: "An Introduction to Statistical Learning"
---

# An Introduction to Statistical Learning

통계적 학습(Statistical Learning) 교원에 대한 공식 학습 목차입니다. 
각 장의 제목을 통해 상세 문서를 확인하실 수 있습니다.

## Statistical Learning Curriculum

### 01. Introduction (소개)
* [문서로 이동하기](/book/c01/)

이 장에서는 통계적 학습(Statistical Learning)이란 무엇인지 개괄적으로 살펴봅니다.
이 책에서 다루게 될 전반적인 데이터셋의 종류와 목적에 대해 간략히 소개합니다.

### 02. Statistical Learning (통계적 학습)
* [문서로 이동하기](/book/c02/)

통계적 학습의 핵심 개념인 $f$ 함수 추정, 분산-편향 트레이드오프(Variance-Bias Trade-off)를 배웁니다.
지도 학습에서의 회귀/분류 문제 구조와 모형의 정확도를 평가하는 기본적인 척도를 다룹니다.

### 03. Linear Regression (선형 회귀)
* [문서로 이동하기](/book/c03/)

가장 직관적이고 폭넓게 활용되는 기초 지도 학습 기법인 선형 회귀 모형을 심도 있게 다룹니다.
단순/다중 선형 회귀 방정식, 각 계수에 대한 가설 검정, 그리고 전체 모델의 적합성 평가 방법을 설명합니다.

### 04. Classification (분류)
* [문서로 이동하기](/book/c04/)

예측하고자 하는 반응 변수(Target)가 여러 개의 범주일 때 사용하는 분류 기법 체계를 소개합니다.
로지스틱 회귀, 다항 분류 시스템, 선형 판별 분석(LDA), K-최근접 이웃(KNN) 등을 배울 수 있습니다.

### 05. Resampling Methods (재표본 추출 방법)
* [문서로 이동하기](/book/c05/)

모델의 일반화 성능을 안전하게 평가하고 하이퍼파라미터를 튜닝하기 위한 필수 데이터 검증 기법을 배웁니다.
교차 검증(Cross-Validation) 과정과 신뢰성 높은 통계 추정을 위한 부트스트랩(Bootstrap)을 자세히 살펴봅니다.

### 06. Linear Model Selection and Regularization (선형 모델 선택 및 규제)
* [문서로 이동하기](/book/c06/)

전통적인 선형 회귀를 확장하여, 부분집합 선택(Subset Selection)이나 차원 축소를 통해 모델을 정교화합니다.
릿지(Ridge), 라쏘(Lasso)와 같은 규제(Regularization) 기법을 적용하여 과적합을 방지하는 과정을 명확히 설명합니다.

### 07. Moving Beyond Linearity (비선형성을 향해)
* [문서로 이동하기](/book/c07/)

복잡한 데이터의 비선형적 관계를 효과적이고 유연하게 모델링하기 위한 수리적 함수 확장 개념을 다룹니다.
다항식 회귀뿐만이 아니라 스플라인(Splines) 기법 및 일반화 가법 모형(GAMs)의 구조를 학습합니다.

### 08. Tree-Based Methods (트리 기반 방법론)
* [문서로 이동하기](/book/c08/)

직관적인 룰 셋으로 이루어진 의사결정 트리(Decision Trees)의 기본 원리부터 시작하여 그 한계를 파악합니다.
이후 배깅(Bagging), 랜덤 포레스트(Random Forests), 부스팅(Boosting) 등 강력한 앙상블 기법으로 확장하는 과정을 배웁니다.

### 09. Support Vector Machines (서포트 벡터 머신)
* [문서로 이동하기](/book/c09/)

선형 초평면(Hyperplane)을 통해 데이터 간의 최대 마진(Margin)을 확보하는 최대 마진 분류기에서 출발합니다.
슬랙 변수와 커널 트릭(Kernel Trick)을 수식적으로 받아들여, 막강한 비선형 서포트 벡터 머신(SVM)으로 발전하는 최적화를 학습합니다.

### 10. Deep Learning (딥러닝)
* [문서로 이동하기](/book/c10/)

최근 컴퓨터 비전 및 자연어 처리 부문에서 압도적인 성과를 거두고 있는 딥러닝 기술의 신경망(Neural Networks) 구조를 파악합니다.
활성화 함수 최적화와 계층, 더 나아가 이미지 특화 기술인 합성곱 신경망(CNN) 및 그 역전파 메커니즘을 상세히 소개합니다.

### 11. Survival Analysis and Censored Data (생존 분석과 중도절단 데이터)
* [문서로 이동하기](/book/c11/)

의학이나 고객 이탈(Churn) 분석 등, 특정한 '사건(Event)이 일어날 때까지의 시간'을 모델링하는 특수 목적 학습을 다룹니다.
중도절단(Censored) 데이터의 개념을 익히고 카플란-마이어 생존 곡선 및 콕스 비례위험 모형 추정을 살펴봅니다.

### 12. Unsupervised Learning (비지도 학습)
* [문서로 이동하기](/book/c12/)

레이블(정답)이 없는 방대한 데이터 속에서, 변수나 관측치 파악 집단 사이의 숨겨진 패턴과 구조를 찾아내는 자율형 기법들을 다룹니다.
데이터 구조를 축약하는 주성분 분석(PCA)과 K-평균, 계층적 클러스터링(Hierarchical Clustering) 군집화 방법을 포괄적으로 학습합니다.

### 13. Multiple Testing (다중 검정)
* [문서로 이동하기](/book/c13/)

빅데이터 환경에서 흔히 벌어지는, 수천 수만 개의 가설을 동시에 검정함으로써 발생하는 1종 오류(Type I error) 급증 문제를 조명합니다.
Family-Wise Error Rate(FWER) 보정을 위한 Bonferroni/Holm 절차 및 실용적인 발견 비율(FDR) 제어 기법을 설명합니다.

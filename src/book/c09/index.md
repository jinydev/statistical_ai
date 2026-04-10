---
layout: default
title: "9. Support Vector Machines"
---

# 9. Support Vector Machines (서포트 벡터 머신)

관측치들을 공간에서 가장 넓은 여백(Margin)으로 가르고 분리해내는 초평면(Hyperplane) 기반의 세련된 분류 모델 SVM을 다루는 9장입니다.
커널(Kernel) 트릭을 통하여 고차원으로 데이터를 부풀려 비선형적 유연 경계를 찾아내는 강력한 방법론을 학습합니다.

## 9.1 Maximal Margin Classifier (최대 마진 분류기)
* [문서로 이동하기](./9_1_maximal_margin_classifier/)

모든 훈련 데이터를 완벽히 두 그룹으로 갈라놓으면서도, 선과 데이터 간의 거리가 가장 멀찍이 떨어지게 하는 최적의 선(Hyperplane)을 찾는 기본 메커니즘을 설명합니다.

### 9.1.1 What Is a Hyperplane? (초평면이란 무엇인가?)
* [문서로 이동하기](./9_1_maximal_margin_classifier/9_1_1_what_is_a_hyperplane/)

p차원 공간 속에서 차원이 (p-1)인 구조제로 평평하게 영역을 양분해주는 초평면의 수학적 정의와 방정식(계수들의 내적 선형 결합)을 확인합니다.

### 9.1.2 Classification Using a Separating Hyperplane (분리 초평면을 이용한 분류)
* [문서로 이동하기](./9_1_maximal_margin_classifier/9_1_2_classification_using_a_separating_hyperplane/)

어떤 관측치 X값이 초평면 방정식에 투입되었을 때 반환되는 부호(양수/음수)를 기반으로 해당 개별 관측치의 종착 클래스 라벨을 결정짓는 원리를 파악합니다.

### 9.1.3 The Maximal Margin Classifier (최대 마진 분류기의 최적화)
* [문서로 이동하기](./9_1_maximal_margin_classifier/9_1_3_the_maximal_margin_classifier/)

마진 구역을 가장자리부터 침범하지 않게 밀어붙여 구성하는 '서포트 벡터'가 어떠한 성질을 가지는지 탐구하며, 해당 모서리 관측치들만이 경계를 결정지음을 배웁니다.

### 9.1.4 Construction of the Maximal Margin Classifier (최대 마진 분류기의 수식적 구축)
* [문서로 이동하기](./9_1_maximal_margin_classifier/9_1_4_construction_of_the_maximal_margin_classifier/)

각 클래스의 마진 너비(M)를 최대화한다는 수학적 목적 제약 함수(Optimization Problem)를 세우고 라그랑주 수식으로 푸는 최적화 틀을 익힙니다.

### 9.1.5 The Non-separable Case (선형 분리가 불가능한 경우 데이터의 한계)
* [문서로 이동하기](./9_1_maximal_margin_classifier/9_1_5_the_non-separable_case/)

클래스들이 완전히 예쁘게 구분되지 않고 뒤엉켜 있어, 어떤 선을 그려도 반드시 마진을 침범하는 현실적인 비분리 데이터 구조상에서의 취약성을 언급합니다.

## 9.2 Support Vector Classifiers (서포트 벡터 분류기)
* [문서로 이동하기](./9_2_support_vector_classifiers/)

엄격한 마진 기준을 다소 무너뜨려 몇몇 관측치가 경계를 일부 넘어가는 것을 허용수용(Soft Margin)함으로써 과적합을 방지하고 분리가능 한계를 극복하는 기법입니다.

### 9.2.1 Overview of the Support Vector Classifier (소프트 마진과 SVC의 개요)
* [문서로 이동하기](./9_2_support_vector_classifiers/9_2_1_overview_of_the_support_vector_classifier/)

마진의 안쪽이나 아예 반대편 점유까지도 일부 눈감아 주며 전체 분류 기준의 안정성(Robustness)을 추구하는 모델 확장을 다룹니다.

### 9.2.2 Details of the Support Vector Classifier (비용 파라미터와 SVC 수학적 세부 원리)
* [문서로 이동하기](./9_2_support_vector_classifiers/9_2_2_details_of_the_support_vector_classifier/)

페널티 한도를 결정하는 슬랙 변수(Slack Variables)와 조율 파라미터 C가, 마진의 너비와 서포트 벡터의 갯수(편향-분산)를 어떻게 트레이닝 제어하는지 분석합니다.

## 9.3 Support Vector Machines (초차원 커널 SVM)
* [문서로 이동하기](./9_3_support_vector_machines/)

단순 1차 선형 선분 규격을 넘어서, 관측치 속성들의 변환(다항, 방사형 기저) 차원 증가를 통해 구역을 둥글게 파내는 진정한 비선형 마진 SVM 체제를 소개합니다.

### 9.3.1 Classification with Non-Linear Decision Boundaries (비선형 결정 경계를 활용한 분류 메커니즘)
* [문서로 이동하기](./9_3_support_vector_machines/9_3_1_with_non-linear_decision_boundaries_classification/)

서포트 벡터 분류기가 단순 선형(직선)이었던 반면, 파라미터 공간을 커스텀하여 2차/3차 원뿔 파형으로 파내면서 복잡한 커브 곡면의 판별식을 찾는 니즈를 봅니다.

### 9.3.2 The Support Vector Machine (커널 트릭 기반 서포트 벡터 머신)
* [문서로 이동하기](./9_3_support_vector_machines/9_3_2_the_support_vector_machine/)

어마어마한 다항식 공간을 직접 컴퓨터로 내적 연산하지 않고도 커널(Kernel) 함수 기믹만으로 유사 가중치를 동일하게 뽑아내는 컴퓨팅 혁신 트릭 과정을 학습합니다.

### 9.3.3 An Application to the Heart Disease Data (심장 질환 분류 도메인 적용 사례)
* [문서로 이동하기](./9_3_support_vector_machines/9_3_3_an_application_to_the_heart_disease_data/)

커널 SVM과 일반 LDA 분류기 등을 실제 심장병 로지스틱 예측 데이터에 동시 피팅하고 비교 테스트 커브 플롯을 렌더링하며 유연도 모델을 검토합니다.

## 9.4 SVMs with More than Two Classes (다중 클래스 공간에서의 SVM 제어법)
* [문서로 이동하기](./9_4_svms_with_more_than_two_classes/)

원래 태생적으로 이분법(+1/-1)밖에 하지 못하는 SVM을 타겟 클래스가 3개 이상일 때도 활용 가능하도록 변통하는 다중 클러스터 응용 기법을 익힙니다.

### 9.4.1 One-Versus-One Classification (OVO 분류 방식)
* [문서로 이동하기](./9_4_svms_with_more_than_two_classes/9_4_1_one-versus-one_classification/)

모든 K 그룹 클래스들끼리 1대1 데스매치 쌍 콤보를 만들어 수많은 모델을 돌린 뒤 패자부활 다수결 매트릭스로 최종 결론을 짓는 OVO 원리입니다.

### 9.4.2 One-Versus-All Classification (OVA 분류 방식)
* [문서로 이동하기](./9_4_svms_with_more_than_two_classes/9_4_2_one-versus-all_classification/)

나(클래스 A) 대 나머지 전체 공간(All)이라는 K개의 통합 매치 모델만 구축하여 가장 계수 확신 점수가 강력한 클래스를 배정해주는 OVA 판별 로직입니다.

## 9.5 Relationship to Logistic Regression (로지스틱 회귀와 SVM 공간 관계성 증명)
* [문서로 이동하기](./9_5_relationship_to_logistic_regression/)

힌지 손실(Hinge Loss)식을 다루는 수리학적 관점에서 볼 때, 결국 릿지 패널티를 부여한 로지스틱 회귀식과 SVM이 수리적으로 사실상 형제 격임을 증명합니다.

## 9.6 Lab: Support Vector Machines (파이썬 SVM 파이프라인 머신런 랩 실습)
* [문서로 이동하기](./9_6_lab_support_vector_machines/)

Scikit-Learn 프레임워크의 `SVC` 객체에 커널 속성(선형, 다항, 라디알 기저)을 달리 부여하며 데이터 플롯 위에 색상형 결정 평면도를 그리는 커스텀 시각화 랩입니다.

### 9.6.1 Support Vector Classifier (선형 SVC 튜닝 파이썬 실습)
* [문서로 이동하기](./9_6_lab_support_vector_machines/9_6_1_support_vector_classifier/)

선형 `kernel='linear'` 환경하에서 비용 C 패널티 속성 `cost` 파라미터의 그리드 서치(Grid Search CV)를 이용한 최적 마진 폭 튜닝 능력을 배양합니다.

### 9.6.2 Support Vector Machine (비선형 방사형/다항 커널 SVM 파이썬 테스트)
* [문서로 이동하기](./9_6_lab_support_vector_machines/9_6_2_support_vector_machine/)

마름모나 구멍 난 데이터 군집 구조 등에 대해 가우시안 방사상 커널(`rbf`) 속성을 주입하고 동심원 기반의 경계를 렌더링하는 코드를 짜봅니다.

### 9.6.3 ROC Curves (ROC 분류 평가 곡면 직접 구현 실습)
* [문서로 이동하기](./9_6_lab_support_vector_machines/9_6_3_roc_curves/)

훈련된 SVC 모델로부터 클래스 확신 예측 마진 값(`decision_function`)들을 추출해 파이썬에서 민감도 평가를 위한 2차원 성능 플롯 ROC 커브를 그립니다.

### 9.6.4 SVM with Multiple Classes (클래스 3개 이상 공간에 대한 파이썬 다중 SVM 지원 스크립트)
* [문서로 이동하기](./9_6_lab_support_vector_machines/9_6_4_svm_with_multiple_classes/)

클래스 속성을 3종류 이상으로 변형한 관측치 구조를 라이브러리에 입력하여 파이썬 사이킷 툴이 어떻게 OVO 기능을 자가 소화해내는지 확인합니다.

### 9.6.5 Application to Gene Expression Data (생물 유전자 무제한 차원 발현 데이터 진단 랩)
* [문서로 이동하기](./9_6_lab_support_vector_machines/9_6_5_application_to_gene_expression_data/)

관측치는 60개인데 유전 피처는 무려 수천 개단위인 초고차원 의료데이터를 로드해 선형 마진분류에 태워도 완벽 예측이 보장되는 SVM의 한계점과 유효 방해물을 관찰합니다.

## 9.7 Exercises (서포트 벡터 초평면 기하학 증명 및 모델 검증 테스트 복습 기출 과제)
* [문서로 이동하기](./9_7_exercises/)

데이터가 위치한 산점도 점과 거리식 기반으로 마진 공식을 유도해서 최적 라인을 그려내야 하는 기하 통계학 증명 지대입니다.

### Applied (코드 적용 기반의 비선형 모형 구축 코스)
* [문서로 이동하기](./9_7_exercises/9_7_1_applied/)

자동차 휘발유 데이터 집합 등에 SVC를 피팅하고 스스로 최적 C와 감마 하이퍼파라미터를 그리드 서치하는 통계 전문가적 문제해결 능력을 검증합니다.

---
layout: default
title: "12. Unsupervised Learning"
---

# 12. Unsupervised Learning (비지도 학습)

예측해야 할 명확한 표적(Y값)이 주어지지 않은 상태에서, 데이터(X)의 구조적 특성과 구역 패턴만으로 통찰을 발견하는 비지도 학습 12장입니다.
변수 차원을 축소하는 주성분 분석(PCA)과, 관측치들을 유사성에 따라 그룹화하는 군집화(Clustering) 기법을 다룹니다.

## 12.1 The Challenge of Unsupervised Learning (비지도 학습에서의 도전 과제)
* [문서로 이동하기](./12_1_the_challenge_of_unsupervised_learning/)

지도 학습과 달리 정답을 대조해 볼 수 없기 때문에, 발견한 패턴이 잡음인지 무의미한지 정량적으로 교차 테스트하기 매우 까다롭다는 근본 한계를 짚습니다.

## 12.2 Principal Components Analysis (주성분 분석, PCA)
* [문서로 이동하기](./12_2_principal_components_analysis/)

고도의 상관성을 지니는 다수 변수들의 방대한 분산을 가장 집중시켜 요약할 수 있는 직교 컴포넌트 방향들을 찾아내는 차원 축소법입니다.

### 12.2.1 What Are Principal Components? (주성분 벡터 성분이란 무엇인가?)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_1_what_are_principal_components/)

전체 변수의 선형 조합 속에서 극대화된 분산을 점유하는 성분 축을 도출하고, 잔존 분산을 찾아가며 순차적(1번, 2번)으로 성분을 빼내는 수리적 정의입니다.

### 12.2.2 Another Interpretation of Principal Components (주성분 분석에 대한 기하학적 해석)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_2_another_interpretation_of_principal_components/)

분산 최대화의 반대 관점에서, 각 데이터 포인트를 차원 초평면에 수직 투영했을 때 원래 데이터와의 재구성(거리) 오차가 최소가 되는 판이라는 논리입니다.

### 12.2.3 The Proportion of Variance Explained (설명된 분산 비율, PVE)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_3_the_proportion_of_variance_explained/)

추출된 M개의 주성분이 원래 데이터의 전체 에너지(변량)를 각각 혹은 누적해서 몇 %나 설명하는지를 스크리 도표(Scree Plot)로 측정해 시각화합니다.

### 12.2.4 More on PCA (PCA의 추가 논의 사항들)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/)

PCA 수행 시 유의해야 할 변수의 독립성 한계와 기타 특성들을 면밀히 살펴봅니다.

#### Scaling the Variables (모델 훈련 이전 변수들에 대한 단위 스케일링)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/12_2_4_1_scaling_the_variables/)

수십 킬로그램 단위와 수백만 단위가 혼재할 때, 단순히 숫자 크기가 크다는 이유로 주성분 가중치가 쏠리는 것을 막는 표준화(Standardization) 당위성입니다.

#### Uniqueness of the Principal Components (주성분의 유일성)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/12_2_4_2_uniqueness_of_the_principal_components/)

계산된 주성분 방향의 정답은 사실상 부호(양수/음수)를 뒤집어도 공간에서 같은 축을 형성하기에 완전히 고유한 식이라는 보장은 없음을 이해합니다.

#### Deciding How Many Principal Components to Use (몇 개의 주성분을 사용할 것인가?)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/12_2_4_3_deciding_how_many_principal_components_to_use/)

정방향 정답이 없으므로 주로 스크리 도표에서 꺾이는 팔꿈치(Elbow) 지점을 찾거나, 후속 지도학습의 검증을 통해 최적 차원 갯수를 휴리스틱하게 정합니다.

### 12.2.5 Other Uses for Principal Components (주성분의 기타 활용법)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_5_other_uses_for_principal_components/)

노이즈 제거, 데이터 결측치 보정 보완 등 주성분을 단순히 피처 축소뿐만 아니라 데이터 정화/정제(Imputation) 시드를 파악하는 데 사용하는 방법입니다.

## 12.3 Missing Values and Matrix Completion (결측치와 행렬 완성)
* [문서로 이동하기](./12_3_missing_values_and_matrix_completion/)

데이터 셋 행렬 내의 빈 칸(NA 값)을 주성분 구조를 이용해 똑똑하게 채워 넣고 복원하는 고도의 응용 수리 테크닉입니다.

#### Principal Components with Missing Values (결측치가 있는 상태에서의 PCA)
* [문서로 이동하기](./12_3_missing_values_and_matrix_completion/12_3_1_principal_components_with_missing_values/)

완벽한 매트릭스가 아닐 때 반복 수치 해석 최적화 알고리즘을 이용해 근사적으로 주성분 축을 구하고 결측값을 복원해내는 원리를 다룹니다.

#### Recommender Systems (추천 시스템)
* [문서로 이동하기](./12_3_missing_values_and_matrix_completion/12_3_2_recommender_systems/)

행렬 완성을 확장하면 유저가 평가하지 않은 수천 개의 영화 별점을 예측할 수 있는 유명한 넷플릭스 챌린지 성격의 추천 엔진을 만들게 됨을 설명합니다.

## 12.4 Clustering Methods (군집화 기법)
* [문서로 이동하기](./12_4_clustering_methods/)

관측치들이 공간상에 흩어져 있는 '거리' 단위 특성을 측정하여, 동질성 높은 몇 개의 이질적 서브 집단으로 파티션을 나누는 메인 알고리즘들입니다.

### 12.4.1 K-Means Clustering (K-평균 군집화)
* [문서로 이동하기](./12_4_clustering_methods/12_4_1_k-means_clustering/)

전체 집단을 유저가 사전에 지정한 K개 숫자의 클러스터로 하드코딩 분할하는 가장 직관적이고 널리 쓰이는 배정 군집 기술입니다.

#### Algorithm 12.2 K-Means Clustering (K-평균 알고리즘)
* [문서로 이동하기](./12_4_clustering_methods/12_4_1_k-means_clustering/12_4_1_1_algorithm_12.2_k-means_clustering/)

각 노드들의 중심(Centroid)을 구하고 데이터를 계속 가까운 중심으로 재배정하는 과정을 더 이상 이동이 없을 때까지 반복하는 휴리스틱 루프 방식을 봅니다.

### 12.4.2 Hierarchical Clustering (계층적 군집화)
* [문서로 이동하기](./12_4_clustering_methods/12_4_2_hierarchical_clustering/)

K를 미리 정하지 않고, 트리 구조의 덴드로그램(Dendrogram)을 바닥에서부터 쌓아 올려 어떤 높이에서 자를지 직관적으로 판단할 수 있는 군집 기법입니다.

#### Interpreting a Dendrogram (덴드로그램 해석법)
* [문서로 이동하기](./12_4_clustering_methods/12_4_2_hierarchical_clustering/12_4_2_1_interpreting_a_dendrogram/)

그림에서 세로축(수직 거리)의 길이가, 병합된 두 관측 그룹 간의 거리가 원래 얼마나 동떨어져 있었는지를 알려주는 척도 정보임을 이해합니다.

#### The Hierarchical Clustering Algorithm (계층 병합 알고리즘 속성)
* [문서로 이동하기](./12_4_clustering_methods/12_4_2_hierarchical_clustering/12_4_2_2_the_hierarchical_clustering_algorithm/)

두 클러스터 간의 거리를 어떻게 정의할 것이냐에 따라 완전 연결(Complete), 단일 연결(Single), 평균(Average) 링키지(Linkage) 기준이 달라짐을 배웁니다.

### 12.4.3 Practical Issues in Clustering (현실적 클러스터링 적용 시 주의사항)
* [문서로 이동하기](./12_4_clustering_methods/12_4_3_practical_issues_in_clustering/)

현실에서 클러스터링에 강제로 데이터를 끼워 맞출 때 발생하는 소외 관측값 처리, 이상치 편향 등의 난제를 돌아봅니다.

#### Validating the Clusters Obtained (얻어낸 군집 결과의 검증)
* [문서로 이동하기](./12_4_clustering_methods/12_4_3_practical_issues_in_clustering/12_4_3_1_validating_the_clusters_obtained/)

도출된 서브 그룹이 정말로 의미 있는 본질을 갖는지 통계 소프트웨어의 p-value 등을 과신하면 발생하는 이중 편향(Double Dipping) 주의점을 설명합니다.

#### A Tempered Approach to Interpreting the Results of Clustering (클러스터링 결과를 다룰 때의 온건적 태도)
* [문서로 이동하기](./12_4_clustering_methods/12_4_3_practical_issues_in_clustering/12_4_3_2_a_tempered_approach_to_interpreting_the_results_of_clustering/)

어느 하나가 완벽한 정답이 아니므로, 여러 K와 다양한 조건(Subsampling)을 흔들어가며 안정적으로 도출되는 합의점을 찾아야 한다는 조언입니다.

## 12.5 Lab: Unsupervised Learning (비지도 모델 분석 파이썬 통합 실습)
* [문서로 이동하기](./12_5_lab_unsupervised_learning/)

파이썬의 Scikit-Learn과 SciPy 모듈 등을 임포트해 주성분 스코어를 구하고, 플롯 도구로 직관적인 K-Means 및 계층적 덴드로그램을 직접 도축해봅니다.

### 12.5.1 Principal Components Analysis (주성분 분석 파이썬 랩)
* [문서로 이동하기](./12_5_lab_unsupervised_learning/12_5_1_principal_components_analysis/)

`PCA` 클래스를 인스턴스화하고 USArrests 데이터(미국 주별 범죄율)를 먹여서 각 주(State)들의 이름이 바이플롯(Biplot) 위에 어떻게 매핑되는지 그립니다.

### 12.5.2 Matrix Completion (행렬 복원 완성 알고리즘 파이썬 구현)
* [문서로 이동하기](./12_5_lab_unsupervised_learning/12_5_2_matrix_completion/)

데이터의 여러 값이 `np.nan`으로 비어있는 상황에서 커스텀 루프를 돌려 잔차를 최소화하고 원래의 주성분 행렬을 퍼즐 맞추듯 연산해냅니다.

### 12.5.3 Clustering (다양한 클러스터링 알고리즘 파이썬 평가랩)
* [문서로 이동하기](./12_5_lab_unsupervised_learning/12_5_3_clustering/)

`KMeans` 모형 인자나 `linkage` 함수를 불러와 데이터 임의 군집 구역을 색칠하고 완전 연결, 평균 연결 트리를 주피터 화면에 투영합니다.

### 12.5.4 NCI60 Data Example (실제 거대 생물체 데이터에서의 PCA/군집화 적용 혼합 과정)
* [문서로 이동하기](./12_5_lab_unsupervised_learning/12_5_4_nci60_data_example/)

차원이 무려 6830개에 달하는 유전자 발현량 NCI60 암 환자 데이터를 차원 압축시킨 뒤 클러스터링하여 진단 패턴이 존재하는지 파악하는 파이프라인 웍입니다.

## 12.6 Exercises (군집 알고리즘 및 차원 투영 수리 증명용 과제망)
* [문서로 이동하기](./12_6_exercises/)

데이터가 군집 트리에서 어떤 높이로 결합될지를 행렬 거리 수기로 계산하거나 파이썬 모듈로 차원 축소 맵을 검증해보는 종합 연습 문제 세트입니다.

### Conceptual (비지도 개념 수식화 질문들)
* [문서로 이동하기](./12_6_exercises/12_6_1_conceptual/)

특정 관측치 3~4개의 거리 디스턴스 매트릭스를 기반으로 단일 및 완전 연결 과정을 증명하거나 스케일링 유무에 따른 식별 변동을 수학 서술합니다.

### Applied (파이썬 군집 코딩 실무 응용 지대)
* [문서로 이동하기](./12_6_exercises/12_6_2_applied/)

현실 오픈소스 유전 데이터를 K-Means 군집과 계층적 군집으로 투스텝 적합시키면서 노이즈의 함정을 돌파하는 과정을 코드로 증빙 제출합니다.

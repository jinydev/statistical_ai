---
layout: default
title: "7. Moving Beyond Linearity"
---

# 7. Moving Beyond Linearity (비선형성을 향해)

입력 변수 X와 반응 변수 Y가 다이렉트 직선(Linear) 관계로 설명되지 않는 복잡한 상황을 모델링하기 위한 진보된 유연한 함수 확장 기술 체계를 다루는 7장입니다.
다항 회귀부터 데이터를 쪼개어 적합하는 스플라인(Splines) 및 일반화 가법 모형(GAM)까지 고전적인 파생 확장법들을 상세히 배웁니다.

## 7.1 Polynomial Regression (다항식 회귀 모형)
* [문서로 이동하기](./7_1_polynomial_regression/)

기존 설명 변수 X에 제곱수(X², X³) 등 추가 다항 항 계수를 반영하여, 선형 모델의 프레임을 유지하면서도 매우 간단하게 비선형 곡선을 적합하는 기초적이고 전통적인 기법입니다.
너무 높은 차수를 주었을 때 양 끝단 관측 범위 경계에 다다르면 예측 곡면 꼬리가 걷잡을 수 없이 말려 올라가버리는 다항식 함수의 한계점을 지적합니다.

## 7.2 Step Functions (계단 부분 상수화 함수)
* [문서로 이동하기](./7_2_step_functions/)

연속형 숫자 변수인 X 데이터를 임의의 몇 개 분할 구역 지점(이른바 컷 포인트)들로 자른 후, 단계별 범주화(Categorization) 요인으로 피팅하는 계단형 모형 컷 분석입니다.

#### Piecewise Constant (조각별 상수 함수)
* [문서로 이동하기](./7_2_step_functions/7_2_1_piecewise_constant/)

잘려진 각 구역(바구니/빈) 안에서는 복잡성 없이 단순히 반응 변수들의 단일 상수 모델 평균치 레벨만으로 Y 데이터를 무단 예측하는 메커니즘을 수치적으로 이해하고 해석합니다.

## 7.3 Basis Functions (추상 기저 함수 결합)
* [문서로 이동하기](./7_3_basis_functions/)

다항식이나 스텝 함수 등을 모두 자신만의 고유한 특별 케이스로 포괄시킬 수 있는 추상 모델 군 이론식이며, X의 임의의 변환식을 기저로 모형 확장의 틀을 잡는 기반 개념 구조를 소개합니다.

## 7.4 Regression Splines (회귀 스플라인 보간 함수 모델)
* [문서로 이동하기](./7_4_regression_splines/)

데이터에 단순히 거대한 단일 곡면 차수를 덮어씌어버리는 기존 한계를 넘어서, 구간 부분마다 제각기 다른 최적 다항식을 부드럽게 붙여가게 설계하여 정교하고 안정적인 전체 선분을 피팅하는 심화 기술 모음입니다.

### 7.4.1 Piecewise Polynomials (조각별 데이터 다항식 적합 선분들)
* [문서로 이동하기](./7_4_regression_splines/7_4_1_piecewise_polynomials/)

변수 성질 분포가 일어나는 연속적인 공간을 임의의 특정 경곗점인 매듭(Knot)이라 불리는 위치들로 수십 개 나눈 후, 구간마다 서로 다른 성질의 작은 차수(3차 이하 통상) 다항식 선형 조합을 모자이크처럼 모델링하는 방법 모델론입니다.

### 7.4.2 Constraints and Splines (곡선 미분 매끄러움을 위한 제약 조건과 통합 스플라인)
* [문서로 이동하기](./7_4_regression_splines/7_4_2_constraints_and_splines/)

조각별 분리식들이 이어지는 K-Knot 결합 지점에서 궤적이 날카롭게 끊기거나 각지지 않게 1차/2차 미분 기울기(평활 제약)가 완벽히 포개어 일치하도록 조절 제약을 가해 매끄러운 곡선 함수(Smooth Spline)를 완성하는 통계 제어법입니다.

### 7.4.3 The Spline Basis Representation (수학 이론 기반 스플라인 모델링 인스턴스 기저식 표현 변환식)
* [문서로 이동하기](./7_4_regression_splines/7_4_3_the_spline_basis_representation/)

매듭 제약들을 가지는 이런 복합 스플라인 곡면을 구현하고 일반 오리지널 선형 회귀 모듈 소프트웨어상에서 최적 구동시키고자, 새로운 추가 기저 피처 항인 짤라진 멱함수 체인(Truncated Power Basis)을 데이터 X항에 주입하는 통계 공식적 수학 해부입니다.

### 7.4.4 Choosing the Number and Locations of the Knots (스플라인 휨 굴절을 설계하는 매듭의 적정 분할 개수와 앵커 위치 지정 탐색)
* [문서로 이동하기](./7_4_regression_splines/7_4_4_choosing_the_number_and_locations_of_the_knots/)

구간을 섬세하게 분해하는 기준 선점인 임의의 매듭점(Knots)들을 도대체 데이터 어디에, 몇 개나 조밀하게 박아두어야 과적합 없이 안정적으로 함수 결과물이 전개될지, 검증하기 위한 테스트(CV 등) 척도를 소개합니다.

#### Natural Cubic Spline (자연 연장 보간 3차 큐빅 스플라인 한계 교정)
* [문서로 이동하기](./7_4_regression_splines/7_4_4_choosing_the_number_and_locations_of_the_knots/7_4_4_1_natural_cubic_spline/)

데이터 밀도가 희박한 양 끝쪽 극단(Boundary) 영역 관측치 부근에서 회귀 추정값 분산이 터지는 것을 봉쇄하고자, 양 경계 밖 궤적은 선형이 되게끔 영구적 제한을 걸어서 구조적 분산을 극약처방하는 튼튼한 스플라인 응용 모델 버전을 살펴봅니다.

### 7.4.5 Comparison to Polynomial Regression (가성비 입증: 비대 수리 다항식 회귀와 분할 스플라인 간의 잔차 통계 분석적인 성능 곡선 비교)
* [문서로 이동하기](./7_4_regression_splines/7_4_5_comparison_to_polynomial_regression/)

차수만 한없이 높이는 단일한 15차 초고도 다항식보다, 작은 차수 매듭을 분할 연결해 K 분절 스플라인으로 모델을 유도하는 쪽이 가장자리 영역 관측 범위 에러 면책율 및 유연성에서 월등히 이점이 많다는 결과를 데이터 시각도로 비교 증명합니다.

## 7.5 Smoothing Splines (평활 스플라인 함수 곡률 모형 제어 방식)
* [문서로 이동하기](./7_5_smoothing_splines/)

인위적으로 컷오프 매듭점을 유저가 직접 정할 필요성을 없애고, 잔차 제곱합 모형 측도에다 굴절 페널티를 매겨 곡률 전체가 너무 거칠게 노이즈를 타며 흔들리지 않게 곡면 유연성(Roughness Penalty) 미분 최소화 탐색을 유도하는 우아한 적합 방식입니다.

### 7.5.1 An Overview of Smoothing Splines (평활 스플라인 페널티 함수 수리 도출 과정의 핵심 개요)
* [문서로 이동하기](./7_5_smoothing_splines/7_5_1_an_overview_of_smoothing_splines/)

학습 데이터의 모든 포인트 관측치 전체 $N$ 개마다 모두 매듭 K를 하나씩 박아 완전히 지나가는(암기하는) 함수 유연도를 가진 상태에서, 오직 파라미터 람다 조율율만으로 곡선의 오돌토돌함을 평활(Smoothing) 깎는 이론 수식 지도를 배웁니다.

### 7.5.2 Choosing the Smoothing Parameter λ (평활 모델 유연도를 조율 관제하는 하이퍼파라미터 λ 선택 방식 원리)
* [문서로 이동하기](./7_5_smoothing_splines/7_5_2_choosing_the_smoothing_parameter/)

LOOCV 모델 검증 방식을 가장 효율적인 행렬 분할 포맷 계산 비용만으로 동원하여 변동 평활 제어 계수 람다와 이펙티브 자유도(Effective Degrees of Freedom) 수치를 정답화하는 최적 데이터 선택 기준식을 계산 배웁니다.

#### Smoothing Spline Example (제약 기반 평활 곡선 스플라인 데이터 모델링 실제 예시 케이스 결과 뷰)
* [문서로 이동하기](./7_5_smoothing_splines/7_5_2_choosing_the_smoothing_parameter/7_5_2_1_smoothing_spline/)

근로자 임금(Wage) 예측 등과 같은 전형적 다이내믹 일반화 타겟의 부드러운 평활 스플라인 모델 공식을 통계 알고리즘으로 적합했을 때, 모델 선형 대비 1순위에 랭크되는 매끄러운 곡면 디펜스 맵핑 투영 예제 결과치를 화면으로 확인합니다.

## 7.6 Local Regression (가중치를 부여하는 국소적 로컬 지점 데이터 집중 회귀 분석 방식)
* [문서로 이동하기](./7_6_local_regression/)

전체 팝 데이터 행이 아닌 목표해야 할 새로운 예측 타겟 포인트 좌표 반경 근방의 가장 물리적 유사한 '이웃 구역 데이터'들로만 포집한 뒤, 그곳에만 큰 종모양 가중치 비중률을 전가시켜 선형/비선형 패키지를 조금씩 조각칼로 이어붙여 스캐닝 도색으로 맞추는 고도 로컬 피팅 기법입니다.

#### Algorithm 7.1 Local Regression At X = x0 (국소 범주 가중치 K 이웃 범위 반경 설정 추적 알고리즘)
* [문서로 이동하기](./7_6_local_regression/7_6_1_algorithm_7.1_local_regression_at_x_x_0/)
* [Local Linear Regression 적용 이론 실무 활용 스니펫 정보망](./18_local_linear_regression/)

데이터 내 어떠한 K 퍼센트 타겟 관측치들을 추출하고 종 모양 커널 등 가중치 거리를 계산하여 매겨, 구역 내 로컬 부분 회귀 최소 제곱을 지속 튜닝하며 어떻게 잔차 에러를 감소시키는지 실질 로직 알고리즘들을 디버깅 스레드로 봅니다.

## 7.7 Generalized Additive Models (일반화 가법 모형, GAMs 종합 프레임워크 기초 통상)
* [문서로 이동하기](./7_7_generalized_additive_models/)

유효 입력 변수 속성값 차원이 단 1개가 아니라 여러 변수가 다차원으로 복수 존재할 때, 개별 예측 변수마다 각각 별개의 스무딩 비선형 독립 스플라인 곡선을 세우고서, 서로 엮이게 곱이 아닌 덧셈식(Additive 가법) 체인 구조로 나열 조립하는 고해상도 유연 결합 모형 기법입니다.

### 7.7.1 GAMs for Regression Problems (연속형 회귀 인퍼런스 타겟 문제에서의 GAMs 셋업 운용 방법)
* [문서로 이동하기](./7_7_generalized_additive_models/7_7_1_gams_for_regression_problems/)

각 각의 변수 차별화된 고유 스플라인 함수 모델 구조 선형 결합 폼인 $f_1, f_2, ...$ 라인들에 어떻게 복잡 백피팅(Backfitting) 방식 혹은 보편적 로컬 블록 스캔 형태로 상호 잔차 덩어리들을 교대 할당시키며 구축하는지 스코어 모델링 전개를 이해합니다.

#### Pros and Cons of GAMs (가법 모형 GAM이 제공해주는 강력한 분리 해석 명료화 장점 및 한계점 주의 구조)
* [문서로 이동하기](./7_7_generalized_additive_models/7_7_1_gams_for_regression_problems/7_7_1_1_pros_and_cons_of_gams/)

기존 선형성의 거친 족쇄 모델 체인 제약을 우아하게 부수며 각 곡률 변화량을 정교하게 잡아내면서도, 모델 개별 변수 계수의 독립적 편향 해석력과 명징성을 그대로 유지하는 장점과, 역으로 변수 간 상호작용 항(Interaction Term) 삽입 탐색 시 수작업 조율이 고스란히 동반되는 한계점을 모두 검증합니다.

### 7.7.2 GAMs for Classification Problems (범주형 타겟 로지스틱 예측 클래스 분류 지표 문제 해결에서의 GAMs 확장 체인 방법)
* [문서로 이동하기](./7_7_generalized_additive_models/7_7_2_gams_for_classification_problems/)

기반이 되는 이항 분포 구조 확률의 단골인 로지스틱 스코어 확률 방정식 모델 계수 내면의 선형 X 요소들도 마찬가지 수리 형식으로 각자의 스플라인 피팅망으로 얹어, 확률 타겟 공간 사이의 복잡 무쌍한 분류 함수 경계선 라인을 놀랍도록 유연 가동할 수 있음을 이론적 증명으로 묘사하고 관측 비교 검증합니다.

## 7.8 Lab: Non-Linear Modeling (실습: 넌리니어 비선형 데이터 구조 탐지 모델링 파이썬 사이킷 활용 랩)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/)

파이썬의 전통적 statsmodels 체인 및 핵심 파이썬 가공 툴박스 함수들을 통한 범용 파이프라인(Pandas) 다항식 인스턴스 전처리를 동원하여, 다양한 곡면 및 유연 스플라인 구조체를 현실 경제 등 도메인 데이터들에 피처 삽입해보고 스코어 에러 편차를 돌려봅니다.

### 7.8.1 Polynomial Regression and Step Functions (수동형 다항식 스펙트럼 회귀 통계망 구축 및 계단식 가공 데이터 스텝 함수 변형 구간 실습 세선 구간)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_1_polynomial_regression_and_step_functions/)

연령 데이터 칼럼(Age)과 임금 인프라 요인(Wage) 간의 관련성에 `poly(age, 4)` 식과 같이 코드 포맷 함수를 투여하거나, 혹은 특정 나이 및 세대 층위를 구간 범주화 컷 함수 판별식으로 매핑 필터링하여 이산적 정보망 차원 제어로 모델을 생성합니다.

#### Jupyter Notebook Output (파이썬 다항 차원 스텝 선형 인스턴스 회귀 결과 통계 도축 스코어 표 콘솔 디스플레이 지표 모음 확인)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_1_polynomial_regression_and_step_functions/7_8_1_1_in_9_summarizem/)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_1_polynomial_regression_and_step_functions/7_8_1_1_out10_143.59228/)
모델 추론 결과 요약 통계 지표 함수 반환 정보 코드 리전과 인덱스 로케이션 상의 스텝형 구역 분리 시 발생된 구간 계단식 모델링 데이터 손실 잔차 MSE 적합 평가 변동 폭 값들을 화면 테이블로 점검 체인 확인합니다.

### 7.8.2 Splines (B-Splines 베이시스 함수 기초 기반 스플라인 조각 시각화 랩 과정 구간)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_2_splines/)

파이썬 기반 고급 회귀 팩토리 모형 추론 분석 파트 섹션에서 다변수 패키지로 1차 혹은 연속적으로 나눈 2차 이상 구간 인프라 매듭 지정점 스플라인 클래스 요소인 B-Spline 기반을 강제로 코딩 선언해주고 이가 나타내는 매끄러움을 추적 시각화로 그래픽 포인팅하는 플롯 차트 모델 구출 과정입니다.

### 7.8.3 Smoothing Splines and GAMs (페널티 기반 평활 최적 커브 스플라인 적합 팩터 및 고차원 구조 가법 통합 예측 모델 PyGAM 컴포넌트 실습 활용 구간)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_3_smoothing_splines_and_gams/)

자유도(Degree of Freedom) 강도 조율율 파라미터 값 설정에 따른 내부 모델 곡면 잔차 거친 분산 추적 조종 패럴렐 통계 방식이나, 모델 인덱스 내의 예측 변수 2~3개가 서로 다른 차수 비선형 스플라인 곡면 꼴로 더해지는 PyGAM 등 파생 고급 패키지의 내부 사용법을 코드 데이터로 직접 임베드 구현해 봅니다.

#### ANOVA Tests for Additive Models (GAM 모형 층위 다중 적합 계층 모델 집단 속성 성향에 대한 F-Stat 분산 분석 통계적 비교 모델 점검 구간 결론 세트)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_3_smoothing_splines_and_gams/7_8_3_1_anova_tests_for_additive_models/)

주어진 어떤 변수 구성 조합 성분 모델 체계가 그 변수를 선형 컴포넌트로만 두는 게 적절한지, 아니면 필수불가결적 편향 해결용으로 반드시 복잡도 높은 비선형 모델 곡면 층 편입 처리가 유용한 이점이 있는지 GAM 구성 요소 서브넷 트리 체인들을 비교 대조하여 ANOVA 우위 스코어 검사로 엄격히 판정 필터링을 검증합니다.

### 7.8.4 Local Regression (로컬 구역 변동 표본 회귀 구간 데이터 분석 조립 실습 파라미터 제어)
* [문서로 이동하기](./7_8_lab_non-linear_modeling/7_8_4_local_regression/)

근거리 최적 로컬 이웃망의 데이터 스캐닝만 허용하는 Loess(Lowess) 평활화 타겟 수학 패키지 함수 모듈 등을 소환하여 사용자 예측 테스트 구간 목표 지점 근거리에 집중적으로 무게 추 가중치를 부여하는 등 국소 모델 선형 국면 피팅 파이썬 분석 실무 함수 제어기를 직접 구동해봅니다.

## 7.9 Exercises (비선형 편향 데이터 극복 실무 모델 응용 파트 컴플렉시티 종합 기출문제 훈련 풀이 리뷰 지대 구간)
* [문서로 이동하기](./7_9_exercises/)

데이터와 모델들 간의 강직된 단방향 선형성이라는 가설 제약을 해제하고 매끄러움을 제공하는 다항식 적합 계산 체계와 구간 계단 스플라인 곡률 적합을 확실히 이해 체득 증명해내기 위해, 개념적 서술 코스와 코드 데이터 통계 로직 스크립트 작성 양 방향 다 요구하는 실습형 뎁스 훈련 리뷰 스테이지 연습 과제 세트 모음 지대입니다.

### Applied (현실 비선형 도메인 예측 응용 데이터 코드 시나리오 모델링 통계 문제 해결 풀이장)
* [문서로 이동하기](./7_9_exercises/7_9_1_applied/)

정규화/비정규화된 현업 혹은 경제 데이터와 기상 데이터 베이스 시나리오 등을 유사 응용 데이터 파이프라인으로 로딩 마운트하고 K-Fold 체계를 접목해 나만의 분석 모델 함수 커스텀을 직접 세팅한 뒤 어떻게 최적의 K수량 노드 매듭점 파라미터 수치값을 찾아 개선 곡면 예측 지표 체계로 만들 수 있는지 스스로 주피터 환경에서 코드를 완성 서브밋하고 결과 통계치를 유의미하게 탐구 제출할 수 있습니다.

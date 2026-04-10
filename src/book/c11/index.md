---
layout: default
title: "11. Survival Analysis and Censored Data"
---

# 11. Survival Analysis and Censored Data (생존 분석과 중도절단 데이터)

시간의 흐름에 따라 '어떤 목표 사건(Event)이 일어날 때까지 걸린 시간'을 회귀 타겟으로 삼는 생존 분석 방법론을 다루는 향상된 통계 과목인 11장입니다.
실험 도중 추적이 끊기거나 사건이 아직 안 터진 '중도절단(Censored)' 상황 데이터를 합리적 수식으로 반영하는 생존 함수 등 특수 회귀를 배웁니다.

## 11.1 Survival and Censoring Times (생존 시간과 중도절단 시간의 개념)
* [문서로 이동하기](./11_1_survival_and_censoring_times/)

발병, 고객 이탈(Churn), 기계 고장 등 흥미를 끄는 특정 사건 경과 시간을 측정할 시, 측정 기한 마감으로 인해 온전치 못하게 기록되는 관측치들을 분류합니다.

## 11.2 A Closer Look at Censoring (중도절단 현상의 심층 분석)
* [문서로 이동하기](./11_2_a_closer_look_at_censoring/)

관측이 도중에 중단되었다는 사실 자체가 주는 중요한 정보(적어도 도달 시점까지는 생존했음)를 통계적으로 버리지 않고 온전히 살려내는 수학 모델링 기조 파트입니다.

## 11.3 The Kaplan–Meier Survival Curve (카플란-마이어 생존 곡선)
* [문서로 이동하기](./11_3_the_kaplanmeier_survival_curve/)

주어진 관측치들을 바탕으로 시간 $t$ 이상 생존할 확률인 생존 함수(Survival Function) $S(t)$를 비모수적 계단식 그래프 형태로 추정 계산하는 유명한 기초 곡선 이론입니다.

## 11.4 The Log-Rank Test (로그 랭크 통계 검정)
* [문서로 이동하기](./11_4_the_log-rank_test/)

집단(예: A약 복용군 vs B약 복용군) 간의 두 생존 곡선이 통계적으로 유의미한 차이를 보이는지를 그룹별 관측수 대비 기댓값을 통해 검증하는 분산 분석 척도입니다.

## 11.5 Regression Models With a Survival Response (반응 변수가 생존 시간인 회귀 모델 구축)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/)

환자의 나이, 성별, 복용량 같은 여러 X 변수(Covariates)들이 생존 속도 곡선에 미치는 회귀적 영향을 모델링하기 시작하는 생존 회귀 분야의 본격적 도입부입니다.

### 11.5.1 The Hazard Function (위험률 함수)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_1_the_hazard_function/)

특정 시점 $t$까지 생존했을 때, 바로 그 직후 순간에 사건(사망)이 발생할 순간 확률의 척도인 위험 함수 $\lambda(t)$의 정의 및 생존 함수 $S(t)$ 와의 수리적 결합 포인트를 배웁니다.

### 11.5.2 Proportional Hazards (비례 위험 모형 구조체)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_2_proportional_hazards/)

시간에 따른 기본 위험률과 X 변수들에 의한 가중치 효과를 곱 구도로 분리하여 위험률 함수를 단순화 설계하는 비례적 가정법의 메커니즘을 숙독합니다.

#### Cox’s Proportional Hazards Model (콕스 비례 위험 모형)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_2_proportional_hazards/11_5_2_1_coxs_proportional_hazards_model/)

시간 중심의 기본 위험 함수 $h_0(t)$ 형태를 굳이 추정하지 않고 오직 변수 계수에만 집중하여 부분 최대 우도법으로 모델링하는 이 분야 최고의 베스트셀러 모델입니다.

#### Connection With The Log-Rank Test (로그 랭크 검정과의 수학적 관계망)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_2_proportional_hazards/11_5_2_2_connection_with_the_log-rank_test/)

단일 범주 변수로 이분류된 데이터를 콕스 모형의 독립변수에 넣었을 때 도출되는 스코어 검정 통계량이 신기하게도 로그 랭크의 원리와 본질적으로 일치함을 유도해 냅니다.

#### Which one should we prefer? (어떤 방식을 선호해야 하는가?)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_2_proportional_hazards/11_5_2_3_which_one_should_we_prefer/)

단순 2집단 분기라면 카플란 마이어+로그랭크 통계량이 편리하고 가시적이나, 여럿 변수를 통제한 개별 요인 기여도를 알기 원할 땐 콕스 모델을 택하는 게 옳음을 정리합니다.

#### Additional Details (콕스 모형의 추가 수학적 논의 및 부분 우도 함수 유도 절차)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_2_proportional_hazards/11_5_2_4_additional_details/)

콕스 모형 최적화 과정에서 왜 오직 타겟 사건들이 일어나는 찰나의 순간값들 세팅만 분모로 모여 계수($\beta$) 부분 검정에 영향을 미치는지 편미분 연산을 심층 점검합니다.

### 11.5.3 Example: Brain Cancer Data (사례 연구: 뇌종양 데이터 분석 회귀 모델 시각화)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_3_example_brain_cancer_data/)

실제 뇌종양 환자들의 다양한 변수군과 중도 절단 정보를 콕스 모형에 적합하고 결과 예측 승수들을 통해 기여 인자를 찾아냅니다.

### 11.5.4 Example: Publication Data (사례 연구: 논문 출판 데이터 관측 생존도 포착)
* [문서로 이동하기](./11_5_regression_models_with_a_survival_response/11_5_4_example_publication_data/)

의료만이 아니라 출판이라는 사회적 사건 발생 완료(논문 심사 통과) 시간에도 생존 모형이 작동하는 사례를 관측, 다기종 분야 호환성을 검증합니다.

## 11.6 Shrinkage for the Cox Model (고차원을 위한 콕스 모델 규제 및 라쏘 수축 기법 결합)
* [문서로 이동하기](./11_6_shrinkage_for_the_cox_model/)

변수 $p$가 큰 유전체 생존 분석 상황에서 부분 우도 방정식에 라쏘($L_1$) 패널티를 가해 덜 중요한 생존 영향 변수 계수를 0으로 소거 억제하는 고차원 벌점 생존 회귀입니다.

## 11.7 Additional Topics (생존 분석 관련 기타 심화 논의 주제)
* [문서로 이동하기](./11_7_additional_topics/)

생존 추정 모형의 우수성을 가리는 평가 지표 및 시간에 따라 변하는 코베리어트 변수 등 모델 통계 확장을 위한 고급 논점들을 제공받습니다.

### 11.7.1 Area Under the Curve for Survival Analysis (생존 모델의 AUC와 C-인덱스 평가지표 척도)
* [문서로 이동하기](./11_7_additional_topics/11_7_1_area_under_the_curve_for_survival_analysis/)

분류 모델의 흔한 지표인 ROC 유사도처럼, 생존율 기대 수치가 높은 대상자가 실제 생존 시간이 더 길게 맵핑되었는가를 재는 일치도 켤레(Harrell's C-index) 지표를 소개합니다.

### 11.7.2 Choice of Time Scale (시간 축 척도의 결정과 제약 한계치)
* [문서로 이동하기](./11_7_additional_topics/11_7_2_choice_of_time_scale/)

연구 시작 시간 기준일지, 사람 나이 기준일지, 혹은 절대 연도 기준일지에 따라 생존 모델 그래프 전개가 상이함을 보여주며, 적절한 T 설정 철학을 안내합니다.

### 11.7.3 Time-Dependent Covariates (시간 의존적 공변량 투입 요소 확장망)
* [문서로 이동하기](./11_7_additional_topics/11_7_3_time-dependent_covariates/)

관측 기간 도중에 혈압이나 약물 복용량 같은 속성(변수값)이 바뀔 경우 시간 의존성 변수로 세팅하여 위험률 함수에 유동성을 전파시키는 콕스 모형 패치 기법입니다.

### 11.7.4 Checking the Proportional Hazards Assumption (비례 위험 가정 엄격도 위배 추적 검토)
* [문서로 이동하기](./11_7_additional_topics/11_7_4_checking_the_proportional_hazards_assumption/)

모든 시점에 걸쳐 그룹 간 위험비가 일정한 배율이어야 한다는 콕스 방식의 유일한 전제(PH)가 맞는지 스코엔펠드 한계 잔차(Schoenfeld Residuals) 도표로 감지합니다.

### 11.7.5 Survival Trees (생존 숲 및 트리 분기 분석 혼합 모델)
* [문서로 이동하기](./11_7_additional_topics/11_7_5_survival_trees/)

이전 트리 장에서 단일 로그 분류 기준이 쓰인 걸 생존 로그 랭크 기준값으로 대체하여 의사결정 나무를 키우는 논파라메트릭 섭스텐스 분리 방식들을 살펴봅니다.

## 11.8 Lab: Survival Analysis (중도절단 타겟 환경 기반의 생존 궤적 파이썬 모듈 데이터 실습장)
* [문서로 이동하기](./11_8_lab_survival_analysis/)

Scikit-Survival 라이브러리 및 통계 패키지인 `lifelines`를 호출해 카플란-마이어 플롯 객체를 시각화하고 Cox 모형 계수를 표로 콘솔 출력하는 파이썬 코딩 타임입니다.

### 11.8.1 Brain Cancer Data (뇌종양 생존 모델링 파이썬 분석 파이프라인 수행 과정망)
* [문서로 이동하기](./11_8_lab_survival_analysis/11_8_1_brain_cancer_data/)

Lifelines 패키지의 카플란 피터 인스턴스 구축과 콕스 회귀 패키지를 활용해 그룹별 뇌종양 환자들의 치료 효과 플롯을 브라우저에 투영합니다.

### 11.8.2 Publication Data (의학 논문 출판 소요 시일 지연 중도절단 콕스 분석 랩 구현)
* [문서로 이동하기](./11_8_lab_survival_analysis/11_8_2_publication_data/)

긍정 논문/부정 논문으로 갈리는 연구 범주형 요인이 언제 사건(저널 채택)을 촉발시키는지 관측치를 적합하며 p-value를 파이썬 터미널에서 점검합니다.

### 11.8.3 Call Center Data (콜센터 대기고객 중도 이탈 포기 생존 기간 관측 데이터망 랩 테스트)
* [문서로 이동하기](./11_8_lab_survival_analysis/11_8_3_call_center_data/)

고객들이 상담원 통화가 될 때를 기다리다 일시 중단(censored event)한 대기 시간 데이터를 통계 파레토 모형 플롯과 묶어 분석해보는 재미난 응용 관측 연습을 합니다.

## 11.9 Exercises (위험 모델 전제 조건 수학적 논파 및 생존율 증명 기초 기출문제 평가 코스)
* [문서로 이동하기](./11_9_exercises/)

왜 일반 제곱합이 아닌 위험 함수 척도를 통해 생존성을 분석해야 하는지 부분 우도 패널티식을 종이와 펜으로 적어내며 이해하는 포커스 스테이지입니다.

### Conceptual (위험 모형 수학 유도 심화 과제 증명 개념 평가 트러스트 존)
* [문서로 이동하기](./11_9_exercises/11_9_1_conceptual/)

특정 사건 비율 상수 값만을 가질 때 카플란 마이어 적분식의 기대값 편차가 어떻게 지수 곡률과 등비 형태를 이루게 되는지 한계점 구조 이론을 수리적으로 점검합니다.

### Applied (파이썬 생존 패키지를 통한 신규 데이터베이스 관측 응용 모델 과제 제출 런 구간)
* [문서로 이동하기](./11_9_exercises/11_9_2_applied/)

금융 대출 디폴트 데이터나 의료 수술 경과 등의 임의 데이터 시나리오를 주피터로 로드, 콕스와 로그 랭크 검정을 두루 사용해 어떤 X 변수가 생존 요주물인지 파악 보고서를 완성합니다.

## 12.1 The Challenge of Unsupervised Learning (비지도 학습에서의 도전 과제)
* [문서로 이동하기](./12_1_the_challenge_of_unsupervised_learning/)

이전 장과는 달리 예측할 뚜렷한 정답 표적(Y값)이 없을 때 고차원 데이터 공간에서 어떤 구역 밀도적 패턴과 시그널을 찾아 통찰력을 얻어야 하는가에 관한 본질적인 목표 모색 챕터 단위 진입부입니다.

## 12.2 Principal Components Analysis (주성분 분석 핵심 프레임 모듈 분해)
* [문서로 이동하기](./12_2_principal_components_analysis/)

고도의 상관성을 지니는 데이터 차원 속 방대한 분산을 가장 집중시켜 요약할 수 있는 직교 백터 방향들을 스폰하는 거대 선형 대수적 투영 변환 방법론(PCA)입니다.

### 12.2.1 What Are Principal Components? (주성분 벡터 성분이란 수학적으로 무엇을 의미하는가?)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_1_what_are_principal_components/)

각 변수 벡터들의 선형 조합의 크기 분산 가중치 성분 중 최대의 극댓값을 점유해주는 성분 축을 하나씩 순차적으로 뺄셈하며 수학적으로 유도 도출하는 직관적 정의를 확인합니다.

### 12.2.2 Another Interpretation of Principal Components (주성분에 관한 또 다른 차원의 재해석)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_2_another_interpretation_of_principal_components/)

단순히 전체 행렬 분산을 최대로 올리는 것 외에, 기하학적으로는 원래 n개 관측치 포인트 공간과의 잔차 거리가 가장 짧은 초평면 판임을 증명하는 이중 각도 분석입니다.

### 12.2.3 The Proportion of Variance Explained (설명된 분산의 설명력 확보 비율, PVE 산출 지표 논의)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_3_the_proportion_of_variance_explained/)

PCA를 진행한 후 도출된 1번, 2번 등 주성분 스코어들이 원래 전체 데이터 맵의 변량(에너지)을 과연 몇 퍼센트나 커버하는지 재주는 스크리 도표(Scree Plot)의 정량화입니다.

### 12.2.4 More on PCA (주성분 차원 축소 추가 기재 수학 및 정규 규칙 고려 사항)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/)

PCA 컴포넌트 벡터들이 반드시 갖춰야 하는 변수 직교 독립성 제약과, 왜 결측치가 존재하면 파이프라인이 즉각 고장나는지에 대한 부수적 맹점 요인들을 기술 검토합니다.

#### Scaling the Variables (모델 훈련 이전 변수들에 대한 단위 환산 표준 스케일링 권고 방침)
* [문서로 이동하기](./12_2_principal_components_analysis/12_2_4_more_on_pca/12_2_4_1_scaling_the_variables/)

수십 킬로그램 단위와 수백만 화폐 단위가 분산 비교될 시, 그저 수치가 크다는 이유로 첫 주성분 가중치를 앗아가버리는 오류를 막으려는 강제 스케일 작업 당위성입니다.

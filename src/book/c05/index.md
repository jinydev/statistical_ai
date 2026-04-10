---
layout: default
title: "5. Resampling Methods"
---

# 5. Resampling Methods (재표본 추출 방법)

단일 훈련 데이터셋의 한계를 넘어 모델의 오차를 정확히 추정하고, 파라미터 유연성의 정중앙을 탐지하기 위한 필수 검증 기법을 다루는 5장입니다.
교차 검증(Cross Validation)과 기계학습 근간인 부트스트랩(Bootstrap)이 핵심 주제로 등장합니다.

## 5.1 Cross-Validation (교차 검증)
* [문서로 이동하기](./5_1_cross-validation/)

모델의 테스트 에러를 평가하기 위해 훈련 데이터를 조각내어 학습과 모델 검증을 번갈아 수행하는 다중 테스트 방식을 다룹니다.
하이퍼파라미터 체계를 세팅할 때 편향 없이 최적화된 모델을 고르는 기초적인 방법론입니다.

### 5.1.1 The Validation Set Approach (검증 세트 접근법)
* [문서로 이동하기](./5_1_cross-validation/5_1_1_the_validation_set_approach/)

가장 단순하게 전체 데이터를 절반은 훈련용(Train), 나머지 절반은 검증용(Validation)으로 단 1번 쪼개는 고전적인 분할 방식입니다.
구현하기 무척 쉽지만 관측치 낭비가 크고, 분할 시드에 따라 검증 결과가 심하게 요동치는 치명적인 단점을 살펴봅니다.

### 5.1.2 Leave-One-Out Cross-Validation (단일 관측치 제외 교차 검증, LOOCV)
* [문서로 이동하기](./5_1_cross-validation/5_1_2_leave-one-out_cross-validation/)

단 1개의 관측치만 검증 폴드로 빼두고 나머지 수많은 데이터 전체를 훈련에 쏟아붓는 완전형 교차 검증법 수식 체계입니다.
편향 이슈는 거의 해결되나, N번씩 전체 모델을 계속 훈련해야 하므로 연산 비용이 천문학적일 수 있음을 논의합니다.

### 5.1.3 k-Fold Cross-Validation (k-폴드 교차 검증)
* [문서로 이동하기](./5_1_cross-validation/5_1_3_k-fold_cross-validation/)

전체 데이터를 균등하게 K개(통상 5~10)의 파티션으로 조각내어 순차적으로 돌아가며 교차 검증하는 최적의 타협안입니다.
LOOCV 대비 연산 소모 구간을 획기적으로 줄여주며, 적정한 분산과 편향 보정 능력을 거두는 기법을 경험합니다.

### 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation (k-폴드에서의 편향-분산 트레이드오프)
* [문서로 이동하기](./5_1_cross-validation/5_1_4_bias-variance_trade-off_for_k-fold_cross-validation/)

데이터를 나누는 K 갯수에 따라 편향(Bias) 제어와 예측 분산(Variance) 상승이 어떻게 서로 대치되는지 수리적으로 따져봅니다.
왜 많은 학자들과 현업에서 K=10 혹은 K=5를 압도적인 기본값으로 선택하는지 이론적 이유를 분석합니다.

### 5.1.5 Cross-Validation on Classification Problems (분류 문제에서의 교차 검증)
* [문서로 이동하기](./5_1_cross-validation/5_1_5_cross-validation_on_problems_classification/)

그동안 회귀분야 연속 변수(MSE 측도 중심)에서 관찰했던 CV 사이클 테크닉을, 이산적이고 범주형인 오분류율(Error Rate) 척도에 동일하게 전파합니다.
분류 모델들의 초매개변수를 튜닝하고 우수성을 비교하는 통계적 실증 분석입니다.

## 5.2 The Bootstrap (부트스트랩)
* [문서로 이동하기](./5_2_the_bootstrap/)

보유한 표본 데이터 집단으로부터 중복(복원) 추출(Replacement)을 반복하여 가상의 유사 팝레이션(표본군)을 무한히 생성하는 강력한 무작위 추출 기술입니다.
계수의 신뢰구간 측정이나 배깅(Bagging), 랜덤 포레스트 등 고급 앙상블 기법들의 중추 시스템 원리를 담고 있습니다.

## 5.3 Lab: Cross-Validation and the Bootstrap (실습: 파이썬 기반 교차 검증 및 부트스트랩)
* [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/)

Scikit-Learn 라이브러리가 제공하는 견고한 폴드 도구 모음을 빌려와 파이썬 언어로 직접 CV 측정과 부트스트랩 난수 궤적을 코딩해 실행하는 실습 시간입니다.

### 5.3.1 The Validation Set Approach (샘플 분할 세트 실습)
* [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_1_the_validation_set_approach/)

내장 파이썬 데이터 전처리 분할 함수인 `train_test_split`을 이용해 랜덤하게 데이터를 분리하는 가장 근원적 검증 파이프라인을 작성합니다.

### 5.3.2 Cross-Validation (파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_2_cross-validation/)

머신런 패키지의 `KFold`와 `cross_validate` 인자 속성을 엮어서 변수의 다항식 확장에서 최고 성능을 발휘하는 파라미터 계층을 스캔합니다.

#### 다중 분석 결과 지표 (Jupyter Notebook Output)
* MSE 산출: [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_2_cross-validation/5_3_2_1_out9_24.2315/)
* Array 출력: [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_2_cross-validation/5_3_2_1_out13_array23.6166/)
* Tuple 확인: [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_2_cross-validation/5_3_2_1_out14_23.8022_1.4218/)
각각의 쪼개진 폴드 조각별로 반환되는 로스 에러 값 배열들을 확인하고, 왜 편차가 존재하고 어떻게 평균내는 코드가 짜이는지 체감합니다.

### 5.3.3 The Bootstrap (넘파이 부트스트랩 구현 실습)
* [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_3_the_bootstrap/)

복원 랜덤 추출 함수나 넘파이의 쵸이스 기능을 통해 부트스트랩 헬퍼 함수를 스스로 작성하고, 통계 모수치의 표준 오차를 통계 엔진 없이 순수 시뮬레이션 해봅니다.

#### 부트스트랩 연산 로그 (Jupyter Notebook Output)
* 에스티메이터 점검: [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_3_the_bootstrap/5_3_3_1_out17_0.6074/)
* 스코어 분포도: [문서로 이동하기](./5_3_lab_cross-validation_and_the_bootstrap/5_3_3_the_bootstrap/5_3_3_1_out19_0.0912/)
수 천번 반복 복원수집된 궤적에서 추출된 획득 추정치의 단단한 신뢰 오차 마진을 눈과 코드로 직접 관찰합니다.

## 5.4 Exercises (연습 문제 종합)
* [문서로 이동하기](./5_4_exercises/)

학습한 CV 평가 궤적과 리샘플 절차에서 발생하는 편차의 벌어지는 현상을 수식으로 유도하거나 코드 통계 도구로 자가 실증하는 셀프 테스트 단원입니다.

### Conceptual (개념 문제)
* [문서로 이동하기](./5_4_exercises/5_4_1_conceptual/)

특정 관측치 1개가 부트스트랩 수 천 세트 표본에 단 한 번도 뽑히지 않을 절망적 확률 한계를, 순수 수학적 조합 확률 규칙을 거쳐 직접 증명해보는 난도 높은 이론 세션입니다.

### Applied (응용 문제 실습)
* [문서로 이동하기](./5_4_exercises/5_4_2_applied/)

직접 여러 형태의 오픈소스 스펙트럼 데이터를 로드하여 로지스틱과 KNN 기반의 머신분석 모델에 10-Fold 스코어 및 랜덤 폴드 블록 스코어링을 손수 설계하고 보고합니다.

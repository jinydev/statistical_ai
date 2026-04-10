---
layout: default
title: "13. Multiple Testing"
---

# 13. Multiple Testing (다중 가설 검정)

수만 개의 데이터를 한 번에 탐색하며 많은 수의 유의성 검정을 동시에 수행할 때 필연적으로 튀어나오는 치명적 통계 오류의 한계를 조명하는 13장입니다.
개별 가설의 $p$-Value를 제어하는 고전적 방법뿐 아니라 유전체/빅데이터 시대의 사실상 표준인 오발견율(FDR) 개념과 재표본 추출 통계 테크닉을 다룹니다.

## 13.1 A Quick Review of Hypothesis Testing (가설 검정의 기초 빠른 복습)
* [문서로 이동하기](./13_1_a_quick_review_of_hypothesis_testing/)

귀무 가설(Null Hypothesis), $p$-값(p-value), 기각 역치(Rejection Region) 등 단일 가설을 테스트할 때 사용했던 전통적인 인퍼런스 개념을 짧게 상기합니다.

### 13.1.1 Testing a Hypothesis (단일 가설 검정 절차)
* [문서로 이동하기](./13_1_a_quick_review_of_hypothesis_testing/13_1_1_testing_a_hypothesis/)

차이가 없다는 보수적인 귀무가설을 깨뜨리기 위해 관찰된 데이터 통계량이 충분히 충격적인지 확률적 한계치를 확인하는 메인 로직입니다.

#### Step 1: Define the Null and Alternative Hypotheses (귀무가설과 대립가설 정의)
* [문서로 이동하기](./13_1_a_quick_review_of_hypothesis_testing/13_1_1_testing_a_hypothesis/13_1_1_1_step_1_define_the_null_and_alternative_hypotheses/)

관측 결과에 아무 효과(차이)가 0 이라는 방어적인 가정(H0)과, 유의미한 변동이 있다는 도전(H1)을 통계 수식으로 구조화합니다.

#### Step 4: Decide Whether to Reject the Null Hypothesis (귀무가설 기각 여부 결정)
* [문서로 이동하기](./13_1_a_quick_review_of_hypothesis_testing/13_1_1_testing_a_hypothesis/13_1_1_2_step_4_decide_whether_to_reject_the_null_hypothesis/)

$p$-값이 유의수준 $\alpha$(예: 0.05)보다 작으면 우연이라 보기엔 현상이 너무 이례적이므로 귀무가설을 기각하는 최종 결론 룰을 살펴봅니다.

### 13.1.2 Type I and Type II Errors (제1종 오류와 제2종 오류 발생 구조)
* [문서로 이동하기](./13_1_a_quick_review_of_hypothesis_testing/13_1_2_type_i_and_type_ii_errors/)

실제론 참인 귀무가설인데 오판해서 가짜 발견을 하는 1종 오류 확률(False Positive)과, 차이가 있는데 못 찾는 2종 오류(False Negative)의 시소를 확인합니다.

## 13.2 The Challenge of Multiple Testing (동시다발적 다중 가설 검정의 오판 함정)
* [문서로 이동하기](./13_2_the_challenge_of_multiple_testing/)

자료가 방대해져 수천 번의 테스트를 동시에 하게 되면, 1종 오류 임계값(0.05)이 매번 누적 적용되어 사실상 수백 개의 가짜 발견이 쏟아져 버리는 치명적 구조 한계입니다.

## 13.3 The Family-Wise Error Rate (집단 오류율, FWER)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/)

다중 검정 패키지 전체 중에서 오직 단 1개의 가짜 발견이라도 범할 총체적 확률(FWER)을 강하게 알파(0.05) 미만으로 억제하려는 엄격한 통계 제어 철학입니다.

### 13.3.1 What is the Family-Wise Error Rate? (FWER 산출 원리)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/13_3_1_what_is_the_family-wise_error_rate/)

2개, 3개, 나아가 m개의 다중 테스트를 통과할 때마다 무결성(에러 0번)을 지킬 확률이 지수적으로 깎여 사실상 우연한 가짜 발견을 피할 수 없는 수학 관계식입니다.

### 13.3.2 Approaches to Control the Family-Wise Error Rate (FWER 제어 전략)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/13_3_2_approaches_to_control_the_family-wise_error_rate/)

테스트의 $p$-값 타겟컷을 단순 $\alpha$보다 훨씬 가혹하게 조여, 전체 오류 패밀리가 위반을 못 하도록 묶는 여러 수학적 프로시저(절차) 모델을 소개합니다.

#### The Bonferroni Method (본페로니 교정)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/13_3_2_approaches_to_control_the_family-wise_error_rate/13_3_2_1_the_bonferroni_method/)

가장 고전적인 방식으로 검정 개수 $m$만큼 임계치를 단순 나누어($\alpha / m$), 아주 작고 강력히 유의미한 극소 $p$-값만 통과시키는 초엄격 제어 기법입니다.

#### Holm’s Step-Down Procedure (홀름의 계단식 스텝 다운 방식)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/13_3_2_approaches_to_control_the_family-wise_error_rate/13_3_2_2_holms_step-down_procedure/)

본페로니보다 살짝 더 유연하게, 가장 유의한 녀석부터 순차적으로 임계값을 다르게 계산하며 내려오는 방식을 통해 검정력(Power)을 조금 살려냅니다.

### 13.3.3 Between the FWER and Power Trade-Off (FWER 엄격도와 검정력 간의 트레이드오프 딜레마)
* [문서로 이동하기](./13_3_the_family-wise_error_rate/13_3_3_between_the_fwer_and_power_trade-off/)

거룩하게 1종 오류율을 0으로 지켜내려다 보니 기준점이 너무 가혹해져, 정작 유의미해야 할 진짜 발견들마저 대거 쓰레기통에 폐기되는 현상을 분석합니다.

## 13.4 The False Discovery Rate (오발견율, FDR)
* [문서로 이동하기](./13_4_the_false_discovery_rate/)

FWER의 보수성에 타협하여, 아예 "발견했다고 주장한 애들 중 진짜 가짜(False Discovery)가 몇 할인가"를 일정 비율(q-value) 미만으로만 가동, 유지시키는 실용주의적 유전체/빅데이터 표준 기준입니다.

### 13.4.1 Intuition for the False Discovery Rate (오발견율 모델의 수학 구조 해석과 직관)
* [문서로 이동하기](./13_4_the_false_discovery_rate/13_4_1_intuition_for_the_false_discovery_rate/)

사실상 기각판정(Positives) 받은 대상 풀 안에서의 조건부 오탐 비율($V/R$)로만 접근하여 진짜 신호들을 포용할 수 있게 고삐를 살짝 늦춰주는 논리를 봅니다.

### 13.4.2 The Benjamini–Hochberg Procedure (벤자미니-호츠버그 검정 절차 모형)
* [문서로 이동하기](./13_4_the_false_discovery_rate/13_4_2_the_benjaminihochberg_procedure/)

모든 $p$-값을 오름차순으로 정렬한 뒤 지정된 기울기를 곱한 기준선보다 미니멈 아래에 들어오는 지점을 끊어서 기각 대상 군집을 정하는 혁신적 알고리즘입니다.

#### Algorithm 13.2 Benjamini–Hochberg Procedure to Control the FDR (B-H FDR 컨트롤 프로시저 구조)
* [문서로 이동하기](./13_4_the_false_discovery_rate/13_4_2_the_benjaminihochberg_procedure/13_4_2_1_algorithm_13.2_benjaminihochberg_procedure_to_control_the_fdr/)
* [FDR 수리식의 제어 한계 목표점(FDR <= q) 설정](./17_fdr_q./)

실질적으로 어느 정도의 B-H 역치(Threshold)에서 검정을 끊어야 평균 오발견율 기댓값(FDR)을 사용자가 원한 상한선 $q$ 이하로 묶을 수 있는지 스텝을 정의합니다.

## 13.5 A Re-Sampling Approach to p-Values and False Discovery Rates (p-값 및 생존 FDR 통계 척도 도출을 위한 재표본 추출 부트스트랩 접근법)
* [문서로 이동하기](./13_5_a_re-sampling_approach_to_p_-values_and_false_discovery_rates/)

데이터의 진짜 모집단 분포를 이론으로 알 수 없을 때를 대비해, 샘플들의 라벨을 수만 번 섞어치기(Permutation)하여 스스로 귀무가설 상황의 $p$-값을 만들어내는 검증 시뮬레이션입니다.

### 13.5.1 A Re-Sampling Approach to the p-Value (시뮬레이션으로 p-value 도출하기)
* [문서로 이동하기](./13_5_a_re-sampling_approach_to_p_-values_and_false_discovery_rates/13_5_1_a_re-sampling_approach_to_the_p-value/)

처리군과 대조군 상태 표지를 모두 무작위로 계속 뒤바꾼(Shuffle) 통계치 덩어리와 비교해서 내 진짜 점수가 몇 등쯤 되는지로 인위적인 $p$-값을 생성하는 메커니즘을 봅니다.

### 13.5.2 A Re-Sampling Approach to the False Discovery Rate (재추출 조합을 통한 FDR 계산 모형)
* [문서로 이동하기](./13_5_a_re-sampling_approach_to_p_-values_and_false_discovery_rates/13_5_2_a_re-sampling_approach_to_the_false_discovery_rate/)

B-H 절차를 넘어, 임의의 혼합 데이터를 통해 가짜 발견 평균수를 도출해 오발견율 식을 통계적 가정 없이 산출해내는 데이터 마이닝 지연 계산법입니다.

### 13.5.3 When Are Re-Sampling Approaches Useful? (이러한 재표본 추출 접근이 대체 언제 유용한가?)
* [문서로 이동하기](./13_5_a_re-sampling_approach_to_p_-values_and_false_discovery_rates/13_5_3_when_are_re-sampling_approaches_useful/)

수집된 데이터가 정규성이나 기정의된 모델 분포 따위를 심각하게 위배하여 정통 T검정 등 분석을 믿기 어려울 때, 데이터 자체 패턴만을 맹신하는 이 기법이 강력함을 증명합니다.

## 13.6 Lab: Multiple Testing (수 천개 다차원 가설 척도 검증 모델 평가를 위한 파이썬 모듈 랩 세팅)
* [문서로 이동하기](./13_6_lab_multiple_testing/)

사이파이 및 스탯츠모델스의 함수를 이용해 t-검정 $p$-값을 수없이 다회 양산해보고, 본페로니나 B-H 교정 함수(`multipletests`)를 통과시켜 살아남는 변수를 파이썬으로 조망해봅니다.

### 13.6.1 Review of Hypothesis Tests (다중 가설 티-검정 루프 스코어 파이썬 도커 리뷰)
* [문서로 이동하기](./13_6_lab_multiple_testing/13_6_1_review_of_hypothesis_tests/)

Fund 데이터셋 등 여러 종목의 수익률 맵을 로드하고 `scipy.stats.ttest_1samp`를 반복문으로 돌려 일원 가설 $p$-값들을 수집 배열합니다.

### 13.6.2 Family-Wise Error Rate (본페로니 기반 FWER 가혹성 디버깅 파이썬 실습 결과 체크)
* [문서로 이동하기](./13_6_lab_multiple_testing/13_6_2_family-wise_error_rate/)

도출된 $p$-값 어레이에 본페로니나 홀름 교정을 걸어 `reject` 부울값 배열을 획득하고, 얼마나 많은 펀드가 그 무자비한 기준을 뚫고 생존하는지 관측합니다.

### 13.6.3 False Discovery Rate (B-H 오발견율 기반 유연한 변수 선별 실용적 데이터 랩 적용 구간 분석)
* [문서로 이동하기](./13_6_lab_multiple_testing/13_6_3_false_discovery_rate/)

오발견율(FDR) 교정 옵션인 `fdr_bh` 속성 모드를 채택하여 유의수준 조율값 q=0.1 미만에서 더 널널하고 융통성 있게 발견을 확보하는 성능 그래프 우위를 증명합니다.

### 13.6.4 A Re-Sampling Approach (파이썬 랜덤 퍼뮤테이션 재셔플 시뮬레이터 모델의 인위적 다변량 p스코어 검증법 코딩 모델링)
* [문서로 이동하기](./13_6_lab_multiple_testing/13_6_4_a_re-sampling_approach/)

`np.random.permutation` 난수 라이브러리를 통해 각 턴마다 정답 라벨 순서를 무작위로 100회씩 섞는 몬테카를로 식 반복문을 돌려 자생적 $p$-값을 파이썬 코랩 터미널 콘솔 로그로 유도합니다.

## 13.7 Exercises (다중 가설의 수학 한계와 FWER 통계적 오류 편차 증폭 이해 여부 과제물 코스)
* [문서로 이동하기](./13_7_exercises/)

왜 본페로니가 독립 검정에선 과도하게 보수적인 결과를 낳는지 확률 교집합 수식으로 서술하고, B-H 절댓값 수식을 스스로 검증해보는 수리 중심 훈련 타임입니다.

### Conceptual (통계 다변량 가설 위배 증명 수식 논증용 포커스 실습 개념 이해 존)
* [문서로 이동하기](./13_7_exercises/13_7_1_conceptual/)

독립적으로 5개의 귀무가설이 주어졌을 때 FWER을 유지하려면 알파 컷을 어떻게 해야 하는지 조건부 확률의 곱셈 정리 이론식으로 증명하게 만드는 등 고도의 통계 사고력을 기릅니다.

### Applied (코드 적용 기반의 B-H 프로시저 오발견 탐색 모델 실습 커스텀 환경 적용 과제 지대)
* [문서로 이동하기](./13_7_exercises/13_7_2_applied/)

실제 여러 질병/유전자 발현 오픈 데이터를 파이썬 랩에 로드, 본페로니와 B-H를 듀얼 테스트해 보고 도출된 $p$-값들의 인덱스 교집합을 벤다이어그램 구조 등으로 파악하는 데이터 사이언스 업무 실습입니다.

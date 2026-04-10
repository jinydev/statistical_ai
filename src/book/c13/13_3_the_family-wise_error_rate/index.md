---
layout: default
title: "index"
---

# 13.3 The Family-Wise Error Rate 

In the following sections, we will discuss testing multiple hypotheses while controlling the probability of making at least one Type I error. 

---

## Sub-Chapters (하위 목차)

### 13.3.1 What is the Family-Wise Error Rate? (FWER 산출 원리)
* [문서로 이동하기](./13_3_1_what_is_the_family-wise_error_rate/)

2개, 3개, 나아가 m개의 다중 테스트를 통과할 때마다 무결성(에러 0번)을 지킬 확률이 지수적으로 깎여 사실상 우연한 가짜 발견을 피할 수 없는 수학 관계식입니다.

### 13.3.2 Approaches to Control the Family-Wise Error Rate (FWER 제어 전략)
* [문서로 이동하기](./13_3_2_approaches_to_control_the_family-wise_error_rate/)

테스트의 $p$-값 타겟컷을 단순 $\alpha$보다 훨씬 가혹하게 조여, 전체 오류 패밀리가 위반을 못 하도록 묶는 여러 수학적 프로시저(절차) 모델을 소개합니다.

### 13.3.3 Between the FWER and Power Trade-Off (FWER 엄격도와 검정력 간의 트레이드오프 딜레마)
* [문서로 이동하기](./13_3_3_between_the_fwer_and_power_trade-off/)

거룩하게 1종 오류율을 0으로 지켜내려다 보니 기준점이 너무 가혹해져, 정작 유의미해야 할 진짜 발견들마저 대거 쓰레기통에 폐기되는 현상을 분석합니다.

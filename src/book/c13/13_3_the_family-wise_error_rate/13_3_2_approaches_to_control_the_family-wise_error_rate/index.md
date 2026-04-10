---
layout: default
title: "index"
---

# _13.3.2 Approaches to Control the Family-Wise Error Rate_ 

In this section, we briefly survey some approaches to control the FWER. We will illustrate these approaches on the `Fund` dataset, which records the monthly percentage excess returns for 2,000 fund managers over _n_ = 50 months.[13] Table 13.3 provides relevant summary statistics for the first five managers. 

We first present the Bonferroni method and Holm’s step-down procedure, which are very general-purpose approaches for controlling the FWER that can be applied whenever _m p_ -values have been computed, regardless of the form of the null hypotheses, the choice of test statistics, or the (in)dependence of the _p_ -values. We then briefly discuss Tukey’s method and Scheffé’s method in order to illustrate the fact that, in certain situations, more specialized approaches for controlling the FWER may be preferable. 

---

## Sub-Chapters (하위 목차)

### The Bonferroni Method (본페로니 교정)
* [문서로 이동하기](./13_3_2_1_the_bonferroni_method/)

가장 고전적인 방식으로 검정 개수 $m$만큼 임계치를 단순 나누어($\alpha / m$), 아주 작고 강력히 유의미한 극소 $p$-값만 통과시키는 초엄격 제어 기법입니다.

### Holm’s Step-Down Procedure (홀름의 계단식 스텝 다운 방식)
* [문서로 이동하기](./13_3_2_2_holms_step-down_procedure/)

본페로니보다 살짝 더 유연하게, 가장 유의한 녀석부터 순차적으로 임계값을 다르게 계산하며 내려오는 방식을 통해 검정력(Power)을 조금 살려냅니다.

---
layout: default
title: "index"
---

# 13.5 A Re-Sampling Approach to _p_ -Values and False Discovery Rates 

Thus far, the discussion in this chapter has assumed that we are interested in testing a particular null hypothesis _H_ 0 using a test statistic _T_ , which has some known (or assumed) distribution under _H_ 0, such as a normal distribution, a _t_ -distribution, a _χ_[2] -distribution, or an _F_ -distribution. This is referred to as the _theoretical null distribution_ . We typically rely upon theoretical the availability of a theoretical null distribution in order to obtain a _p_ - null value associated with our test statistic. Indeed, for most of the types of distribution null hypotheses that we might be interested in testing, a theoretical null distribution is available, provided that we are willing to make stringent assumptions about our data. 

null distribution 

However, if our null hypothesis _H_ 0 or test statistic _T_ is somewhat unusual, then it may be the case that no theoretical null distribution is available. Alternatively, even if a theoretical null distribution exists, then we may be wary of relying upon it, perhaps because some assumption that is required for it to hold is violated. For instance, maybe the sample size is too small. 

In this section, we present a framework for performing inference in this setting, which exploits the availability of fast computers in order to approximate the null distribution of _T_ , and thereby to obtain a _p_ -value. While this framework is very general, it must be carefully instantiated for a specific problem of interest. Therefore, in what follows, we consider a specific example in which we wish to test whether the means of two random variables are equal, using a two-sample _t_ -test. 

The discussion in this section is more challenging than the preceding sections in this chapter, and can be safely skipped by a reader who is content to use the theoretical null distribution to compute _p_ -values for his or her test statistics. 

578 13. Multiple Testing 

---

## Sub-Chapters (하위 목차)

### 13.5.1 A Re-Sampling Approach to the p-Value (시뮬레이션으로 p-value 도출하기)
* [문서로 이동하기](./13_5_1_a_re-sampling_approach_to_the_p-value/)

처리군과 대조군 상태 표지를 모두 무작위로 계속 뒤바꾼(Shuffle) 통계치 덩어리와 비교해서 내 진짜 점수가 몇 등쯤 되는지로 인위적인 $p$-값을 생성하는 메커니즘을 봅니다.

### 13.5.2 A Re-Sampling Approach to the False Discovery Rate (재추출 조합을 통한 FDR 계산 모형)
* [문서로 이동하기](./13_5_2_a_re-sampling_approach_to_the_false_discovery_rate/)

B-H 절차를 넘어, 임의의 혼합 데이터를 통해 가짜 발견 평균수를 도출해 오발견율 식을 통계적 가정 없이 산출해내는 데이터 마이닝 지연 계산법입니다.

### 13.5.3 When Are Re-Sampling Approaches Useful? (이러한 재표본 추출 접근이 대체 언제 유용한가?)
* [문서로 이동하기](./13_5_3_when_are_re-sampling_approaches_useful/)

수집된 데이터가 정규성이나 기정의된 모델 분포 따위를 심각하게 위배하여 정통 T검정 등 분석을 믿기 어려울 때, 데이터 자체 패턴만을 맹신하는 이 기법이 강력함을 증명합니다.

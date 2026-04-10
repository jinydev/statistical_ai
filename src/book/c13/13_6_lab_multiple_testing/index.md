---
layout: default
title: "index"
---

# 13.6 Lab: Multiple Testing 

We include our usual imports seen in earlier labs. 

```
In [1]:importnumpyasnp
importpandasaspd
importmatplotlib.pyplotasplt
importstatsmodels.apiassm
fromISLPimportload_data
```

We also collect the new imports needed for this lab. 

```
In [2]:fromscipy.statsimport\
(ttest_1samp ,
ttest_rel,
ttest_ind,
tast_dbn)
fromstatsmodels.stats.multicompimport\
pairwise_tukeyhsd
fromstatsmodels.stats.multitestimport\
multipletestsasmult_test
```

---

## Sub-Chapters (하위 목차)

### 13.6.1 Review of Hypothesis Tests (다중 가설 티-검정 루프 스코어 파이썬 도커 리뷰)
* [문서로 이동하기](./13_6_1_review_of_hypothesis_tests/)

Fund 데이터셋 등 여러 종목의 수익률 맵을 로드하고 `scipy.stats.ttest_1samp`를 반복문으로 돌려 일원 가설 $p$-값들을 수집 배열합니다.

### 13.6.2 Family-Wise Error Rate (본페로니 기반 FWER 가혹성 디버깅 파이썬 실습 결과 체크)
* [문서로 이동하기](./13_6_2_family-wise_error_rate/)

도출된 $p$-값 어레이에 본페로니나 홀름 교정을 걸어 `reject` 부울값 배열을 획득하고, 얼마나 많은 펀드가 그 무자비한 기준을 뚫고 생존하는지 관측합니다.

### 13.6.3 False Discovery Rate (B-H 오발견율 기반 유연한 변수 선별 실용적 데이터 랩 적용 구간 분석)
* [문서로 이동하기](./13_6_3_false_discovery_rate/)

오발견율(FDR) 교정 옵션인 `fdr_bh` 속성 모드를 채택하여 유의수준 조율값 q=0.1 미만에서 더 널널하고 융통성 있게 발견을 확보하는 성능 그래프 우위를 증명합니다.

### 13.6.4 A Re-Sampling Approach (파이썬 랜덤 퍼뮤테이션 재셔플 시뮬레이터 모델의 인위적 다변량 p스코어 검증법 코딩 모델링)
* [문서로 이동하기](./13_6_4_a_re-sampling_approach/)

`np.random.permutation` 난수 라이브러리를 통해 각 턴마다 정답 라벨 순서를 무작위로 100회씩 섞는 몬테카를로 식 반복문을 돌려 자생적 $p$-값을 파이썬 코랩 터미널 콘솔 로그로 유도합니다.

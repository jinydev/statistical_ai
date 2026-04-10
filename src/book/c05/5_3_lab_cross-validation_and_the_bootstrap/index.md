---
layout: default
title: "index"
---

# 5.3 Lab: Cross-Validation and the Bootstrap 

In this lab, we explore the resampling techniques covered in this chapter. Some of the commands in this lab may take a while to run on your computer. 

We again begin by placing most of our imports at this top level. 

```
In [1]:importnumpyasnp
importstatsmodels.apiassm
fromISLPimportload_data
fromISLP.modelsimport(ModelSpecasMS,
summarize,
poly)
fromsklearn.model_selectionimporttrain_test_split
```

There are several new imports needed for this lab. 

```
In [2]:fromfunctoolsimportpartial
fromsklearn.model_selectionimport\
(cross_validate ,
KFold,
ShuffleSplit)
fromsklearn.baseimportclone
fromISLP.modelsimportsklearn_sm
```

216 5. Resampling Methods 

---

## Sub-Chapters (하위 목차)

### 5.3.1 The Validation Set Approach (샘플 분할 세트 실습)
* [문서로 이동하기](./5_3_1_the_validation_set_approach/)

내장 파이썬 데이터 전처리 분할 함수인 `train_test_split`을 이용해 랜덤하게 데이터를 분리하는 가장 근원적 검증 파이프라인을 작성합니다.

### 5.3.2 Cross-Validation (파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_2_cross-validation/)

머신런 패키지의 `KFold`와 `cross_validate` 인자 속성을 엮어서 변수의 다항식 확장에서 최고 성능을 발휘하는 파라미터 계층을 스캔합니다.

### 5.3.3 The Bootstrap (넘파이 부트스트랩 구현 실습)
* [문서로 이동하기](./5_3_3_the_bootstrap/)

복원 랜덤 추출 함수나 넘파이의 쵸이스 기능을 통해 부트스트랩 헬퍼 함수를 스스로 작성하고, 통계 모수치의 표준 오차를 통계 엔진 없이 순수 시뮬레이션 해봅니다.

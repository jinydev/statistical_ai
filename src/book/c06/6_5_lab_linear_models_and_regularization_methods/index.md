---
layout: default
title: "index"
---

# 6.5 Lab: Linear Models and Regularization Methods 

In this lab we implement many of the techniques discussed in this chapter. We import some of our libraries at this top level. 

```
In [1]:importnumpyasnp
importpandasaspd
frommatplotlib.pyplotimportsubplots
fromstatsmodels.apiimportOLS
importsklearn.model_selectionasskm
importsklearn.linear_modelasskl
fromsklearn.preprocessingimportStandardScaler
fromISLPimportload_data
fromISLP.modelsimportModelSpecasMS
fromfunctoolsimportpartial
```

We again collect the new imports needed for this lab. 

```
In [2]:fromsklearn.pipelineimportPipeline
fromsklearn.decompositionimportPCA
```

268 6. Linear Model Selection and Regularization 

```
fromsklearn.cross_decompositionimportPLSRegression
fromISLP.modelsimport\
(Stepwise,
sklearn_selected ,
sklearn_selection_path)
!pipinstalll0bnb
froml0bnbimportfit_path
```

We have installed the package `l0bnb` on the fly. Note the escaped `!pip install` — this is run as a separate system command. 

---

## Sub-Chapters (하위 목차)

### 6.5.1 Subset Selection Methods (부분집합 자동 선택 메서드 툴박스 파이썬 실습)
* [문서로 이동하기](./6_5_1_subset_selection_methods/)

사이킷런 및 기타 파생 알고리즘 툴킷의 다차원 검정, 모델 AIC, BIC 에러율 식을 직접 가동하기 위한 평가 함수들을 구성하여 변수 중요도 서치 과정을 콘솔 위에서 구현해 봅니다.

### 6.5.2 Ridge Regression and the Lasso (파이썬 릿지 정규화 및 라쏘 분석기 실전 적용 사례)
* [문서로 이동하기](./6_5_2_ridge_regression_and_the_lasso/)

Scikit-Learn 기계학습 모듈 라이브러리의 `Ridge` 클래스 인스턴스와 `Lasso` 클래스를 불러와 알파 스펙트럼(패널티 강도)에 따른 파라미터 변화선 궤적을 렌더링하고 실전 성능 측정 및 시각화를 완료합니다.

### 6.5.3 PCR and PLS Regression (빅데이터 차원 축소 후 연산, PCR-주성분 기반 회귀 실습)
* [문서로 이동하기](./6_5_3_pcr_and_pls_regression/)

PCA 분해 패키지 모듈을 전처리용으로 앞단에 파이프라인 결합한 후 원 주성분 변수를 차원 컷 스코어로 변환, 그리고 그걸 후단 최종 선형회귀 모델에 태우는 세련된 기계학습 테크닉 과정을 체득합니다.

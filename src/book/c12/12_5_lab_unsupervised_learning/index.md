---
layout: default
title: "index"
---

# 12.5 Lab: Unsupervised Learning 

In this lab we demonstrate PCA and clustering on several datasets. As in other labs, we import some of our libraries at this top level. This makes the code more readable, as scanning the first few lines of the notebook tell us what libraries are used in this notebook. 

```
In [1]:importnumpyasnp
importpandasaspd
importmatplotlib.pyplotasplt
fromstatsmodels.datasetsimportget_rdataset
fromsklearn.decompositionimportPCA
fromsklearn.preprocessingimportStandardScaler
fromISLPimportload_data
```

We also collect the new imports needed for this lab. 

```
In [2]:fromsklearn.clusterimport\
(KMeans,
AgglomerativeClustering)
fromscipy.cluster.hierarchyimport\
(dendrogram ,
cut_tree)
fromISLP.clusterimportcompute_linkage
```

---

## Sub-Chapters (하위 목차)

### 12.5.1 Principal Components Analysis (주성분 분석 파이썬 랩)
* [문서로 이동하기](./12_5_1_principal_components_analysis/)

`PCA` 클래스를 인스턴스화하고 USArrests 데이터(미국 주별 범죄율)를 먹여서 각 주(State)들의 이름이 바이플롯(Biplot) 위에 어떻게 매핑되는지 그립니다.

### 12.5.2 Matrix Completion (행렬 복원 완성 알고리즘 파이썬 구현)
* [문서로 이동하기](./12_5_2_matrix_completion/)

데이터의 여러 값이 `np.nan`으로 비어있는 상황에서 커스텀 루프를 돌려 잔차를 최소화하고 원래의 주성분 행렬을 퍼즐 맞추듯 연산해냅니다.

### 12.5.3 Clustering (다양한 클러스터링 알고리즘 파이썬 평가랩)
* [문서로 이동하기](./12_5_3_clustering/)

`KMeans` 모형 인자나 `linkage` 함수를 불러와 데이터 임의 군집 구역을 색칠하고 완전 연결, 평균 연결 트리를 주피터 화면에 투영합니다.

### 12.5.4 NCI60 Data Example (실제 거대 생물체 데이터에서의 PCA/군집화 적용 혼합 과정)
* [문서로 이동하기](./12_5_4_nci60_data_example/)

차원이 무려 6830개에 달하는 유전자 발현량 NCI60 암 환자 데이터를 차원 압축시킨 뒤 클러스터링하여 진단 패턴이 존재하는지 파악하는 파이프라인 웍입니다.

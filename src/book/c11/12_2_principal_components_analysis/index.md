---
layout: default
title: "index"
---

# 12.2 Principal Components Analysis 

_Principal components_ are discussed in Section 6.3.1 in the context of principal components regression. When faced with a large set of correlated variables, principal components allow us to summarize this set with a smaller number of representative variables that collectively explain most of the variability in the original set. The principal component directions are presented in Section 6.3.1 as directions in feature space along which the original data are _highly variable_ . These directions also define lines and subspaces that are _as close as possible_ to the data cloud. To perform principal components regression, we simply use principal components as predictors in a regression model in place of the original larger set of variables. 

_Principal components analysis_ (PCA) refers to the process by which prin- principal cipal components are computed, and the subsequent use of these components in understanding the data. PCA is an unsupervised approach, since analysis it involves only a set of features _X_ 1 _, X_ 2 _, . . . , Xp_ , and no associated response _Y_ . Apart from producing derived variables for use in supervised learning problems, PCA also serves as a tool for data visualization (visualization of 

components analysis 

12.2 Principal Components Analysis 505 

the observations or visualization of the variables). It can also be used as a tool for data imputation — that is, for filling in missing values in a data matrix. 

We now discuss PCA in greater detail, focusing on the use of PCA as a tool for unsupervised data exploration, in keeping with the topic of this chapter. 

---

## Sub-Chapters (하위 목차)

### 12.2.1 What Are Principal Components? (주성분 벡터 성분이란 수학적으로 무엇을 의미하는가?)
* [문서로 이동하기](./12_2_1_what_are_principal_components/)

각 변수 벡터들의 선형 조합의 크기 분산 가중치 성분 중 최대의 극댓값을 점유해주는 성분 축을 하나씩 순차적으로 뺄셈하며 수학적으로 유도 도출하는 직관적 정의를 확인합니다.

### 12.2.2 Another Interpretation of Principal Components (주성분에 관한 또 다른 차원의 재해석)
* [문서로 이동하기](./12_2_2_another_interpretation_of_principal_components/)

단순히 전체 행렬 분산을 최대로 올리는 것 외에, 기하학적으로는 원래 n개 관측치 포인트 공간과의 잔차 거리가 가장 짧은 초평면 판임을 증명하는 이중 각도 분석입니다.

### 12.2.3 The Proportion of Variance Explained (설명된 분산의 설명력 확보 비율, PVE 산출 지표 논의)
* [문서로 이동하기](./12_2_3_the_proportion_of_variance_explained/)

PCA를 진행한 후 도출된 1번, 2번 등 주성분 스코어들이 원래 전체 데이터 맵의 변량(에너지)을 과연 몇 퍼센트나 커버하는지 재주는 스크리 도표(Scree Plot)의 정량화입니다.

### 12.2.4 More on PCA (주성분 차원 축소 추가 기재 수학 및 정규 규칙 고려 사항)
* [문서로 이동하기](./12_2_4_more_on_pca/)

PCA 컴포넌트 벡터들이 반드시 갖춰야 하는 변수 직교 독립성 제약과, 왜 결측치가 존재하면 파이프라인이 즉각 고장나는지에 대한 부수적 맹점 요인들을 기술 검토합니다.

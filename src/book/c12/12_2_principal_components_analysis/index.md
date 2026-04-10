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

### 12.2.1 What Are Principal Components? (주성분 벡터 성분이란 무엇인가?)
* [문서로 이동하기](./12_2_1_what_are_principal_components/)

전체 변수의 선형 조합 속에서 극대화된 분산을 점유하는 성분 축을 도출하고, 잔존 분산을 찾아가며 순차적(1번, 2번)으로 성분을 빼내는 수리적 정의입니다.

### 12.2.2 Another Interpretation of Principal Components (주성분 분석에 대한 기하학적 해석)
* [문서로 이동하기](./12_2_2_another_interpretation_of_principal_components/)

분산 최대화의 반대 관점에서, 각 데이터 포인트를 차원 초평면에 수직 투영했을 때 원래 데이터와의 재구성(거리) 오차가 최소가 되는 판이라는 논리입니다.

### 12.2.3 The Proportion of Variance Explained (설명된 분산 비율, PVE)
* [문서로 이동하기](./12_2_3_the_proportion_of_variance_explained/)

추출된 M개의 주성분이 원래 데이터의 전체 에너지(변량)를 각각 혹은 누적해서 몇 %나 설명하는지를 스크리 도표(Scree Plot)로 측정해 시각화합니다.

### 12.2.4 More on PCA (PCA의 추가 논의 사항들)
* [문서로 이동하기](./12_2_4_more_on_pca/)

PCA 수행 시 유의해야 할 변수의 독립성 한계와 기타 특성들을 면밀히 살펴봅니다.

### 12.2.5 Other Uses for Principal Components (주성분의 기타 활용법)
* [문서로 이동하기](./12_2_5_other_uses_for_principal_components/)

노이즈 제거, 데이터 결측치 보정 보완 등 주성분을 단순히 피처 축소뿐만 아니라 데이터 정화/정제(Imputation) 시드를 파악하는 데 사용하는 방법입니다.

---
layout: default
title: "index"
---

# 12.4 Clustering Methods 

_Clustering_ refers to a very broad set of techniques for finding _subgroups_ , or clustering _clusters_ , in a data set. When we cluster the observations of a data set, we seek to partition them into distinct groups so that the observations within each group are quite similar to each other, while observations in different groups are quite different from each other. Of course, to make this concrete, we must define what it means for two or more observations to be _similar_ or _different_ . Indeed, this is often a domain-specific consideration that must be made based on knowledge of the data being studied. 

For instance, suppose that we have a set of _n_ observations, each with _p_ features. The _n_ observations could correspond to tissue samples for patients with breast cancer, and the _p_ features could correspond to measurements collected for each tissue sample; these could be clinical measurements, such as tumor stage or grade, or they could be gene expression measurements. We may have a reason to believe that there is some heterogeneity among the _n_ tissue samples; for instance, perhaps there are a few different _unknown_ subtypes of breast cancer. Clustering could be used to find these subgroups. This is an unsupervised problem because we are trying to discover structure—in this case, distinct clusters—on the basis of a data set. The goal in supervised problems, on the other hand, is to try to predict some outcome vector such as survival time or response to drug treatment. 

Both clustering and PCA seek to simplify the data via a small number of summaries, but their mechanisms are different: 

12.4 Clustering Methods 521 

- PCA looks to find a low-dimensional representation of the observations that explain a good fraction of the variance; 

- Clustering looks to find homogeneous subgroups among the observations. 

Another application of clustering arises in marketing. We may have access to a large number of measurements (e.g. median household income, occupation, distance from nearest urban area, and so forth) for a large number of people. Our goal is to perform _market segmentation_ by identifying subgroups of people who might be more receptive to a particular form of advertising, or more likely to purchase a particular product. The task of performing market segmentation amounts to clustering the people in the data set. 

Since clustering is popular in many fields, there exist a great number of clustering methods. In this section we focus on perhaps the two best-known clustering approaches: _K-means clustering_ and _hierarchical K_ -means _clustering_ . In _K_ -means clustering, we seek to partition the observations clustering into a pre-specified number of clusters. On the other hand, in hierarchical hierarchical clustering, we do not know in advance how many clusters we want; in fact, clustering we end up with a tree-like visual representation of the observations, called a _dendrogram_ , that allows us to view at once the clusterings obtained for dendrogram each possible number of clusters, from 1 to _n_ . There are advantages and disadvantages to each of these clustering approaches, which we highlight in this chapter. 

In general, we can cluster observations on the basis of the features in order to identify subgroups among the observations, or we can cluster features on the basis of the observations in order to discover subgroups among the features. In what follows, for simplicity we will discuss clustering observations on the basis of the features, though the converse can be performed by simply transposing the data matrix. 

---

## Sub-Chapters (하위 목차)

### 12.4.1 K-Means Clustering (K-평균 군집화)
* [문서로 이동하기](./12_4_1_k-means_clustering/)

전체 집단을 유저가 사전에 지정한 K개 숫자의 클러스터로 하드코딩 분할하는 가장 직관적이고 널리 쓰이는 배정 군집 기술입니다.

### 12.4.2 Hierarchical Clustering (계층적 군집화)
* [문서로 이동하기](./12_4_2_hierarchical_clustering/)

K를 미리 정하지 않고, 트리 구조의 덴드로그램(Dendrogram)을 바닥에서부터 쌓아 올려 어떤 높이에서 자를지 직관적으로 판단할 수 있는 군집 기법입니다.

### 12.4.3 Practical Issues in Clustering (현실적 클러스터링 적용 시 주의사항)
* [문서로 이동하기](./12_4_3_practical_issues_in_clustering/)

현실에서 클러스터링에 강제로 데이터를 끼워 맞출 때 발생하는 소외 관측값 처리, 이상치 편향 등의 난제를 돌아봅니다.

---
layout: default
title: "index"
---

# _12.4.2 Hierarchical Clustering_ 

One potential disadvantage of _K_ -means clustering is that it requires us to pre-specify the number of clusters _K_ . _Hierarchical clustering_ is an alternative approach which does not require that we commit to a particular choice of _K_ . Hierarchical clustering has an added advantage over _K_ -means clustering in that it results in an attractive tree-based representation of the observations, called a _dendrogram_ . 

In this section, we describe _bottom-up_ or _agglomerative_ clustering. This is the most common type of hierarchical clustering, and refers to the fact that a dendrogram (generally depicted as an upside-down tree; see Figure 12.11) is built starting from the leaves and combining clusters up to the trunk. We will begin with a discussion of how to interpret a dendrogram 

bottom-up agglomerative 

526 12. Unsupervised Learning 

![Figure 12.10](./img/12_10.png)

**FIGURE 12.10.** _Forty-five observations generated in two-dimensional space. In reality there are three distinct classes, shown in separate colors. However, we will treat these class labels as unknown and will seek to cluster the observations in order to discover the classes from the data._ 

and then discuss how hierarchical clustering is actually performed—that is, how the dendrogram is built. 

---

## Sub-Chapters (하위 목차)

### Interpreting a Dendrogram (덴드로그램 해석법)
* [문서로 이동하기](./12_4_2_1_interpreting_a_dendrogram/)

그림에서 세로축(수직 거리)의 길이가, 병합된 두 관측 그룹 간의 거리가 원래 얼마나 동떨어져 있었는지를 알려주는 척도 정보임을 이해합니다.

### The Hierarchical Clustering Algorithm (계층 병합 알고리즘 속성)
* [문서로 이동하기](./12_4_2_2_the_hierarchical_clustering_algorithm/)

두 클러스터 간의 거리를 어떻게 정의할 것이냐에 따라 완전 연결(Complete), 단일 연결(Single), 평균(Average) 링키지(Linkage) 기준이 달라짐을 배웁니다.

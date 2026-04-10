---
layout: default
title: "index"
---

# _12.4.3 Practical Issues in Clustering_ 

Clustering can be a very useful tool for data analysis in the unsupervised setting. However, there are a number of issues that arise in performing clustering. We describe some of these issues here. 

Small Decisions with Big Consequences 

In order to perform clustering, some decisions must be made. 

12.4 Clustering Methods 533 

![Figure 12.15](./img/12_15.png)

**FIGURE 12.15.** _Three observations with measurements on 20 variables are shown. Observations 1 and 3 have similar values for each variable and so there is a small Euclidean distance between them. But they are very weakly correlated, so they have a large correlation-based distance. On the other hand, observations 1 and 2 have quite different values for each variable, and so there is a large Euclidean distance between them. But they are highly correlated, so there is a small correlation-based distance between them._ 

- Should the observations or features first be standardized in some way? For instance, maybe the variables should be scaled to have standard deviation one. 

- In the case of hierarchical clustering, 

   - What dissimilarity measure should be used? 

   - What type of linkage should be used? 

   - Where should we cut the dendrogram in order to obtain clusters? 

- In the case of _K_ -means clustering, how many clusters should we look for in the data? 

Each of these decisions can have a strong impact on the results obtained. In practice, we try several different choices, and look for the one with the most useful or interpretable solution. With these methods, there is no single right answer—any solution that exposes some interesting aspects of the data should be considered. 

---

## Sub-Chapters (하위 목차)

### Validating the Clusters Obtained (얻어낸 군집 결과의 검증)
* [문서로 이동하기](./12_4_3_1_validating_the_clusters_obtained/)

도출된 서브 그룹이 정말로 의미 있는 본질을 갖는지 통계 소프트웨어의 p-value 등을 과신하면 발생하는 이중 편향(Double Dipping) 주의점을 설명합니다.

### A Tempered Approach to Interpreting the Results of Clustering (클러스터링 결과를 다룰 때의 온건적 태도)
* [문서로 이동하기](./12_4_3_2_a_tempered_approach_to_interpreting_the_results_of_clustering/)

어느 하나가 완벽한 정답이 아니므로, 여러 K와 다양한 조건(Subsampling)을 흔들어가며 안정적으로 도출되는 합의점을 찾아야 한다는 조언입니다.

---
layout: default
title: "index"
---

# 12.3 Missing Values and Matrix Completion 

Often datasets have missing values, which can be a nuisance. For example, suppose that we wish to analyze the `USArrests` data, and discover that 20 of the 200 values have been randomly corrupted and marked as missing. Unfortunately, the statistical learning methods that we have seen in this book cannot handle missing values. How should we proceed? 

We could remove the rows that contain missing observations and perform our data analysis on the complete rows. But this seems wasteful, and depending on the fraction missing, unrealistic. Alternatively, if _xij_ is missing, then we could replace it by the mean of the _j_ th column (using the non-missing entries to compute the mean). Although this is a common and convenient strategy, often we can do better by exploiting the correlation between the variables. 

In this section we show how principal components can be used to _impute_ impute the missing values, through a process known as _matrix completion_ . The completed matrix can then be used in a statistical learning method, such matrix as linear regression or LDA. 

imputation matrix completion 

This approach for imputing missing data is appropriate if the missingness is random. For example, it is suitable if a patient’s weight is missing because missing at the battery of the electronic scale was flat at the time of his exam. By random contrast, if the weight is missing because the patient was too heavy to climb on the scale, then this is not missing at random; the missingness is 

516 12. Unsupervised Learning 

informative, and the approach described here for handling missing data is not suitable. 

Sometimes data is missing by necessity. For example, if we form a matrix of the ratings (on a scale from 1 to 5) that _n_ customers have given to the entire Netflix catalog of _p_ movies, then most of the matrix will be missing, since no customer will have seen and rated more than a tiny fraction of the catalog. If we can impute the missing values well, then we will have an idea of what each customer will think of movies they have not yet seen. Hence matrix completion can be used to power _recommender systems_ . 

recommender systems 

---

## Sub-Chapters (하위 목차)

### Principal Components with Missing Values (결측치가 있는 상태에서의 PCA)
* [문서로 이동하기](./12_3_1_principal_components_with_missing_values/)

완벽한 매트릭스가 아닐 때 반복 수치 해석 최적화 알고리즘을 이용해 근사적으로 주성분 축을 구하고 결측값을 복원해내는 원리를 다룹니다.

### Recommender Systems (추천 시스템)
* [문서로 이동하기](./12_3_2_recommender_systems/)

행렬 완성을 확장하면 유저가 평가하지 않은 수천 개의 영화 별점을 예측할 수 있는 유명한 넷플릭스 챌린지 성격의 추천 엔진을 만들게 됨을 설명합니다.

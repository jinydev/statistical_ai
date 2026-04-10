---
layout: default
title: "index"
---

# Interpreting a Dendrogram 

We begin with the simulated data set shown in Figure 12.10, consisting of 45 observations in two-dimensional space. The data were generated from a three-class model; the true class labels for each observation are shown in distinct colors. However, suppose that the data were observed without the class labels, and that we wanted to perform hierarchical clustering of the data. Hierarchical clustering (with complete linkage, to be discussed later) yields the result shown in the left-hand panel of Figure 12.11. How can we interpret this dendrogram? 

In the left-hand panel of Figure 12.11, each _leaf_ of the dendrogram represents one of the 45 observations in Figure 12.10. However, as we move up the tree, some leaves begin to _fuse_ into branches. These correspond to observations that are similar to each other. As we move higher up the tree, branches themselves fuse, either with leaves or other branches. The earlier (lower in the tree) fusions occur, the more similar the groups of observations are to each other. On the other hand, observations that fuse later (near the top of the tree) can be quite different. In fact, this statement can be made precise: for any two observations, we can look for the point in the tree where branches containing those two observations are first fused. The height of this fusion, as measured on the vertical axis, indicates how different the two observations are. Thus, observations that fuse at the very bottom of the tree are quite similar to each other, whereas observations that fuse close to the top of the tree will tend to be quite different. 

This highlights a very important point in interpreting dendrograms that is often misunderstood. Consider the left-hand panel of Figure 12.12, which shows a simple dendrogram obtained from hierarchically clustering nine 

12.4 Clustering Methods 527 

![Figure 12.11](./img/12_11.png)

**FIGURE 12.11.** Left: _dendrogram obtained from hierarchically clustering the data from Figure 12.10 with complete linkage and Euclidean distance._ Center: _the dendrogram from the left-hand panel, cut at a height of nine (indicated by the dashed line). This cut results in two distinct clusters, shown in different colors._ Right: _the dendrogram from the left-hand panel, now cut at a height of five. This cut results in three distinct clusters, shown in different colors. Note that the colors were not used in clustering, but are simply used for display purposes in this figure._ 

observations. One can see that observations 5 and 7 are quite similar to each other, since they fuse at the lowest point on the dendrogram. Observations 1 and 6 are also quite similar to each other. However, it is tempting but incorrect to conclude from the figure that observations 9 and 2 are quite similar to each other on the basis that they are located near each other on the dendrogram. In fact, based on the information contained in the dendrogram, observation 9 is no more similar to observation 2 than it is to observations 8 _,_ 5 _,_ and 7. (This can be seen from the right-hand panel of Figure 12.12, in which the raw data are displayed.) To put it mathematically, there are 2 _[n][−]_[1] possible reorderings of the dendrogram, where _n_ is the number of leaves. This is because at each of the _n −_ 1 points where fusions occur, the positions of the two fused branches could be swapped without affecting the meaning of the dendrogram. Therefore, we cannot draw conclusions about the similarity of two observations based on their proximity along the _horizontal axis_ . Rather, we draw conclusions about the similarity of two observations based on the location on the _vertical axis_ where branches containing those two observations first are fused. 

Now that we understand how to interpret the left-hand panel of Figure 12.11, we can move on to the issue of identifying clusters on the basis of a dendrogram. In order to do this, we make a horizontal cut across the dendrogram, as shown in the center and right-hand panels of Figure 12.11. The distinct sets of observations beneath the cut can be interpreted as clusters. In the center panel of Figure 12.11, cutting the dendrogram at a height of nine results in two clusters, shown in distinct colors. In the right-hand panel, cutting the dendrogram at a height of five results in three clusters. Further cuts can be made as one descends the dendrogram in order to obtain any number of clusters, between 1 (corresponding to no cut) and _n_ 

528 12. Unsupervised Learning 

![Figure 12.12](./img/12_12.png)

**FIGURE 12.12.** _An illustration of how to properly interpret a dendrogram with nine observations in two-dimensional space._ Left: _a dendrogram generated using Euclidean distance and complete linkage. Observations_ 5 _and_ 7 _are quite similar to each other, as are observations_ 1 _and_ 6 _. However, observation_ 9 _is_ no more similar to _observation_ 2 _than it is to observations_ 8 _,_ 5 _, and_ 7 _, even though observations_ 9 _and_ 2 _are close together in terms of horizontal distance. This is because observations_ 2 _,_ 8 _,_ 5 _, and_ 7 _all fuse with observation_ 9 _at the same height, approximately_ 1 _._ 8 _._ Right: _the raw data used to generate the dendrogram can be used to confirm that indeed, observation_ 9 _is no more similar to observation_ 2 _than it is to observations_ 8 _,_ 5 _, and_ 7 _._ 

(corresponding to a cut at height 0, so that each observation is in its own cluster). In other words, the height of the cut to the dendrogram serves the same role as the _K_ in _K_ -means clustering: it controls the number of clusters obtained. 

Figure 12.11 therefore highlights a very attractive aspect of hierarchical clustering: one single dendrogram can be used to obtain any number of clusters. In practice, people often look at the dendrogram and select by eye a sensible number of clusters, based on the heights of the fusion and the number of clusters desired. In the case of Figure 12.11, one might choose to select either two or three clusters. However, often the choice of where to cut the dendrogram is not so clear. 

The term _hierarchical_ refers to the fact that clusters obtained by cutting the dendrogram at a given height are necessarily nested within the clusters obtained by cutting the dendrogram at any greater height. However, on an arbitrary data set, this assumption of hierarchical structure might be unrealistic. For instance, suppose that our observations correspond to a group of men and women, evenly split among Americans, Japanese, and French. We can imagine a scenario in which the best division into two groups might split these people by gender, and the best division into three groups might split them by nationality. In this case, the true clusters are not nested, in the sense that the best division into three groups does not result from taking the best division into two groups and splitting up one of those groups. Consequently, this situation could not be well-represented by hierarchical clustering. Due to situations such as this one, hierarchical clustering can sometimes yield _worse_ (i.e. less accurate) results than _K_ - means clustering for a given number of clusters. 

12.4 Clustering Methods 529 

**Algorithm 12.3** _Hierarchical Clustering_ 

1. Begin with _n_ observations and a measure (such as Euclidean dis- _n_ 

tance) of all the �2� = _n_ ( _n −_ 1) _/_ 2 pairwise dissimilarities. Treat each observation as its own cluster. 

2. For _i_ = _n, n −_ 1 _, . . . ,_ 2: 

   - (a) Examine all pairwise inter-cluster dissimilarities among the _i_ clusters and identify the pair of clusters that are least dissimilar (that is, most similar). Fuse these two clusters. The dissimilarity between these two clusters indicates the height in the dendrogram at which the fusion should be placed. 

   - (b) Compute the new pairwise inter-cluster dissimilarities among the _i −_ 1 remaining clusters. 

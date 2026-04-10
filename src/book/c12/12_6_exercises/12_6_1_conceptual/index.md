---
layout: default
title: "index"
---

# _Conceptual_ 

1. This problem involves the _K_ -means clustering algorithm. 

   - (a) Prove (12.18). 

   - (b) On the basis of this identity, argue that the _K_ -means clustering algorithm (Algorithm 12.2) decreases the objective (12.17) at each iteration. 

2. Suppose that we have four observations, for which we compute a dissimilarity matrix, given by

$$
\begin{pmatrix} & 0.3 & 0.4 & 0.7 \\ 0.3 & & 0.5 & 0.8 \\ 0.4 & 0.5 & & 0.45 \\ 0.7 & 0.8 & 0.45 & \end{pmatrix}
$$

For instance, the dissimilarity between the first and second observations is 0.3, and the dissimilarity between the second and fourth observations is 0.8. 

- (a) On the basis of this dissimilarity matrix, sketch the dendrogram that results from hierarchically clustering these four observations using complete linkage. Be sure to indicate on the plot the height at which each fusion occurs, as well as the observations corresponding to each leaf in the dendrogram. 

- (b) Repeat (a), this time using single linkage clustering. 

- (c) Suppose that we cut the dendrogram obtained in (a) such that two clusters result. Which observations are in each cluster? 

- (d) Suppose that we cut the dendrogram obtained in (b) such that two clusters result. Which observations are in each cluster? 

12.6 Exercises 553 

   - (e) It is mentioned in this chapter that at each fusion in the dendrogram, the position of the two clusters being fused can be swapped without changing the meaning of the dendrogram. Draw a dendrogram that is equivalent to the dendrogram in (a), for which two or more of the leaves are repositioned, but for which the meaning of the dendrogram is the same. 

3. In this problem, you will perform _K_ -means clustering manually, with _K_ = 2, on a small example with _n_ = 6 observations and _p_ = 2 features. The observations are as follows. 

|Obs.|_X_1<br>_X_2|
|---|---|
|1<br>2<br>3<br>4<br>5<br>6|1<br>4<br>1<br>3<br>0<br>4<br>5<br>1<br>6<br>2<br>4<br>0|



   - (a) Plot the observations. 

   - (b) Randomly assign a cluster label to each observation. You can use the `np.random.choice()` function to do this. Report the cluster labels for each observation. 

   - (c) Compute the centroid for each cluster. 

   - (d) Assign each observation to the centroid to which it is closest, in terms of Euclidean distance. Report the cluster labels for each observation. 

   - (e) Repeat (c) and (d) until the answers obtained stop changing. 

   - (f) In your plot from (a), color the observations according to the cluster labels obtained. 

4. Suppose that for a particular data set, we perform hierarchical clustering using single linkage and using complete linkage. We obtain two dendrograms. 

   - (a) At a certain point on the single linkage dendrogram, the clusters _{_ 1 _,_ 2 _,_ 3 _}_ and _{_ 4 _,_ 5 _}_ fuse. On the complete linkage dendrogram, the clusters _{_ 1 _,_ 2 _,_ 3 _}_ and _{_ 4 _,_ 5 _}_ also fuse at a certain point. Which fusion will occur higher on the tree, or will they fuse at the same height, or is there not enough information to tell? 

   - (b) At a certain point on the single linkage dendrogram, the clusters _{_ 5 _}_ and _{_ 6 _}_ fuse. On the complete linkage dendrogram, the clusters _{_ 5 _}_ and _{_ 6 _}_ also fuse at a certain point. Which fusion will occur higher on the tree, or will they fuse at the same height, or is there not enough information to tell? 

5. In words, describe the results that you would expect if you performed _K_ -means clustering of the eight shoppers in Figure 12.16, on the basis of their sock and computer purchases, with _K_ = 2. Give three answers, one for each of the variable scalings displayed. Explain. 

554 12. Unsupervised Learning 

6. We saw in Section 12.2.2 that the principal component loading and score vectors provide an approximation to a matrix, in the sense of (12.5). Specifically, the principal component score and loading vectors solve the optimization problem given in (12.6). 

Now, suppose that the _M_ principal component score vectors _zim, m_ = 1 _, . . . , M_ , are known. Using (12.6), explain that each of the first _M_ principal component loading vectors _φjm, m_ = 1 _, . . . , M_ , can be obtained by performing _p_ separate least squares linear regressions. In each regression, the principal component score vectors are the predictors, and one of the features of the data matrix is the response. 

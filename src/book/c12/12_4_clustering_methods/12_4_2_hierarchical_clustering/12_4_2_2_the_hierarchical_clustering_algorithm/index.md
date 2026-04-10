---
layout: default
title: "index"
---

# The Hierarchical Clustering Algorithm 

The hierarchical clustering dendrogram is obtained via an extremely simple algorithm. We begin by defining some sort of _dissimilarity_ measure between each pair of observations. Most often, Euclidean distance is used; we will discuss the choice of dissimilarity measure later in this chapter. The algorithm proceeds iteratively. Starting out at the bottom of the dendrogram, each of the _n_ observations is treated as its own cluster. The two clusters that are most similar to each other are then _fused_ so that there now are _n −_ 1 clusters. Next the two clusters that are most similar to each other are fused again, so that there now are _n −_ 2 clusters. The algorithm proceeds in this fashion until all of the observations belong to one single cluster, and the dendrogram is complete. Figure 12.13 depicts the first few steps of the algorithm, for the data from Figure 12.12. To summarize, the hierarchical clustering algorithm is given in Algorithm 12.3. 

This algorithm seems simple enough, but one issue has not been addressed. Consider the bottom right panel in Figure 12.13. How did we determine that the cluster _{_ 5 _,_ 7 _}_ should be fused with the cluster _{_ 8 _}_ ? We have a concept of the dissimilarity between pairs of observations, but how do we define the dissimilarity between two clusters if one or both of the clusters contains multiple observations? The concept of dissimilarity between a pair of observations needs to be extended to a pair of _groups of observations_ . This extension is achieved by developing the notion of _linkage_ , which defines the dissimilarity between two groups of observa- linkage tions. The four most common types of linkage— _complete_ , _average_ , _single_ , and _centroid_ —are briefly described in Table 12.3. Average, complete, and single linkage are most popular among statisticians. Average and complete linkage are generally preferred over single linkage, as they tend to yield more balanced dendrograms. Centroid linkage is often used in genomics, but suffers from a major drawback in that an _inversion_ can occur, whereby inversion two clusters are fused at a height _below_ either of the individual clusters in the dendrogram. This can lead to difficulties in visualization as well as in interpretation of the dendrogram. The dissimilarities computed in Step 2(b) 

530 12. Unsupervised Learning 

|_Linkage_|_Description_|
|---|---|
|Complete|Maximal intercluster dissimilarity. Compute all pairwise<br>dissimilarities between the observations in cluster A and the<br>observations in cluster B, and record the_largest_ of these dis-<br>similarities.|
|Single|Minimal intercluster dissimilarity. Compute all pairwise dis-<br>similarities between the observations in cluster A and the<br>observations in cluster B, and record the _smallest_ of these<br>dissimilarities. Single linkage can result in extended, trailing<br>clusters in which single observations are fused one-at-a-time.|
|Average|Mean intercluster dissimilarity. Compute all pairwise dis-<br>similarities between the observations in cluster A and the<br>observations in cluster B, and record the _average_ of these<br>dissimilarities.|
|Centroid|Dissimilarity between the centroid for cluster A (a mean<br>vector of length _p_) and the centroid for cluster B. Centroid<br>linkage can result in undesirable _inversions_.|



**TABLE 12.3.** _A summary of the four most commonly-used types of linkage in hierarchical clustering._ 

of the hierarchical clustering algorithm will depend on the type of linkage used, as well as on the choice of dissimilarity measure. Hence, the resulting dendrogram typically depends quite strongly on the type of linkage used, as is shown in Figure 12.14. 

Choice of Dissimilarity Measure 

Thus far, the examples in this chapter have used Euclidean distance as the dissimilarity measure. But sometimes other dissimilarity measures might be preferred. For example, _correlation-based distance_ considers two observations to be similar if their features are highly correlated, even though the observed values may be far apart in terms of Euclidean distance. This is an unusual use of correlation, which is normally computed between variables; here it is computed between the observation profiles for each pair of observations. Figure 12.15 illustrates the difference between Euclidean and correlation-based distance. Correlation-based distance focuses on the shapes of observation profiles rather than their magnitudes. 

The choice of dissimilarity measure is very important, as it has a strong effect on the resulting dendrogram. In general, careful attention should be paid to the type of data being clustered and the scientific question at hand. These considerations should determine what type of dissimilarity measure is used for hierarchical clustering. 

For instance, consider an online retailer interested in clustering shoppers based on their past shopping histories. The goal is to identify subgroups of _similar_ shoppers, so that shoppers within each subgroup can be shown items and advertisements that are particularly likely to interest them. Suppose the data takes the form of a matrix where the rows are the shoppers and the columns are the items available for purchase; the elements of the data matrix indicate the number of times a given shopper has purchased a 

12.4 Clustering Methods 531 

![Figure 12.13](./img/12_13.png)

**FIGURE 12.13.** _An illustration of the first few steps of the hierarchical clustering algorithm, using the data from Figure 12.12, with complete linkage and Euclidean distance._ Top Left: _initially, there are nine distinct clusters, {_ 1 _}, {_ 2 _}, . . . , {_ 9 _}._ Top Right: _the two clusters that are closest together, {_ 5 _} and {_ 7 _}, are fused into a single cluster._ Bottom Left: _the two clusters that are closest together, {_ 6 _} and {_ 1 _}, are fused into a single cluster._ Bottom Right: _the two clusters that are closest together using_ complete linkage _, {_ 8 _} and the cluster {_ 5 _,_ 7 _}, are fused into a single cluster._ 

given item (i.e. a 0 if the shopper has never purchased this item, a 1 if the shopper has purchased it once, etc.) What type of dissimilarity measure should be used to cluster the shoppers? If Euclidean distance is used, then shoppers who have bought very few items overall (i.e. infrequent users of the online shopping site) will be clustered together. This may not be desirable. On the other hand, if correlation-based distance is used, then shoppers with similar preferences (e.g. shoppers who have bought items A and B but never items C or D) will be clustered together, even if some shoppers with these preferences are higher-volume shoppers than others. Therefore, for this application, correlation-based distance may be a better choice. 

In addition to carefully selecting the dissimilarity measure used, one must also consider whether or not the variables should be scaled to have standard deviation one before the dissimilarity between the observations is computed. To illustrate this point, we continue with the online shopping ex- 

532 12. Unsupervised Learning 

![Figure 12.14](./img/12_14.png)

**FIGURE 12.14.** _Average, complete, and single linkage applied to an example data set. Average and complete linkage tend to yield more balanced clusters._ 

ample just described. Some items may be purchased more frequently than others; for instance, a shopper might buy ten pairs of socks a year, but a computer very rarely. High-frequency purchases like socks therefore tend to have a much larger effect on the inter-shopper dissimilarities, and hence on the clustering ultimately obtained, than rare purchases like computers. This may not be desirable. If the variables are scaled to have standard deviation one before the inter-observation dissimilarities are computed, then each variable will in effect be given equal importance in the hierarchical clustering performed. We might also want to scale the variables to have standard deviation one if they are measured on different scales; otherwise, the choice of units (e.g. centimeters versus kilometers) for a particular variable will greatly affect the dissimilarity measure obtained. It should come as no surprise that whether or not it is a good decision to scale the variables before computing the dissimilarity measure depends on the application at hand. An example is shown in Figure 12.16. We note that the issue of whether or not to scale the variables before performing clustering applies to _K_ -means clustering as well. 

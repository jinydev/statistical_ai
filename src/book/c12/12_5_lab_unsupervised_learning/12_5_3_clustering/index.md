---
layout: default
title: "index"
---

# _12.5.3 Clustering_ 

_K_ -Means Clustering 

The estimator `sklearn.cluster.KMeans()` performs _K_ -means clustering in `Kmeans() Python` . We begin with a simple simulated example in which there truly are two clusters in the data: the first 25 observations have a mean shift relative to the next 25 observations. 

```
In [32]:np.random.seed(0);
X=np.random.standard_normal((50,2));
X[:25,0]+=3;
X[:25,1]-=4;
```

We now perform _K_ -means clustering with _K_ = 2. 

```
In [33]:kmeans=KMeans(n_clusters=2,
random_state=2,
n_init=20).fit(X)
```

We specify `random_state` to make the results reproducible. The cluster assignments of the 50 observations are contained in `kmeans.labels_` . 

```
In [34]:kmeans.labels_
```

```
Out[34]:array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0],dtype=int32)
```

The _K_ -means clustering perfectly separated the observations into two clusters even though we did not supply any group information to `KMeans()` . We can plot the data, with each observation colored according to its cluster assignment. 

12.5 Lab: Unsupervised Learning 543 

```
In [35]:fig,ax=plt.subplots(1,1,figsize=(8,8))
ax.scatter(X[:,0],X[:,1],c=kmeans.labels_)
ax.set_title("K-MeansClusteringResultswithK=2");
```

Here the observations can be easily plotted because they are two-dimensional. If there were more than two variables then we could instead perform PCA and plot the first two principal component score vectors to represent the clusters. 

In this example, we knew that there really were two clusters because we generated the data. However, for real data, we do not know the true number of clusters, nor whether they exist in any precise way. We could instead have performed _K_ -means clustering on this example with _K_ = 3. 

```
In [36]:kmeans=KMeans(n_clusters=3,
random_state=3,
n_init=20).fit(X)
fig,ax=plt.subplots(figsize=(8,8))
ax.scatter(X[:,0],X[:,1],c=kmeans.labels_)
ax.set_title("K-MeansClusteringResultswithK=3");
```

When _K_ = 3, _K_ -means clustering splits up the two clusters. We have used the `n_init` argument to run the _K_ -means with 20 initial cluster assignments (the default is 10). If a value of `n_init` greater than one is used, then _K_ - means clustering will be performed using multiple random assignments in Step 1 of Algorithm 12.2, and the `KMeans()` function will report only the best results. Here we compare using `n_init=1` to `n_init=20` . 

```
In [37]:kmeans1=KMeans(n_clusters=3,
random_state=3,
n_init=1).fit(X)
kmeans20=KMeans(n_clusters=3,
random_state=3,
n_init=20).fit(X);
kmeans1.inertia_,kmeans20.inertia_
```

```
Out[37]:(78.06,75.04)
```

Note that `kmeans.inertia_` is the total within-cluster sum of squares, which we seek to minimize by performing _K_ -means clustering (12.17). 

We _strongly_ recommend always running _K_ -means clustering with a large value of `n_init` , such as 20 or 50, since otherwise an undesirable local optimum may be obtained. 

When performing _K_ -means clustering, in addition to using multiple initial cluster assignments, it is also important to set a random seed using the `random_state` argument to `KMeans()` . This way, the initial cluster assignments in Step 1 can be replicated, and the _K_ -means output will be fully reproducible. 

Hierarchical Clustering 

The `AgglomerativeClustering()` class from the `sklearn.clustering` pack- `Agglomerative` age implements hierarchical clustering. As its name is long, we use the `Clustering()` short hand `HClust` for _hierarchical clustering_ . Note that this will not change 

544 12. Unsupervised Learning 

the return type when using this method, so instances will still be of class `AgglomerativeClustering` . In the following example we use the data from the previous lab to plot the hierarchical clustering dendrogram using complete, single, and average linkage clustering with Euclidean distance as the dissimilarity measure. We begin by clustering observations using complete linkage. 

```
In [38]:HClust=AgglomerativeClustering
hc_comp=HClust(distance_threshold=0,
n_clusters=None,
linkage='complete')
hc_comp.fit(X)
```

This computes the entire dendrogram. We could just as easily perform hierarchical clustering with average or single linkage instead: 

```
In [39]:hc_avg=HClust(distance_threshold=0,
n_clusters=None,
linkage='average');
hc_avg.fit(X)
hc_sing=HClust(distance_threshold=0,
n_clusters=None,
linkage='single');
hc_sing.fit(X);
```

To use a precomputed distance matrix, we provide an additional argument `metric="precomputed"` . In the code below, the first four lines computes the 50 _×_ 50 pairwise-distance matrix. 

```
In [40]:D=np.zeros((X.shape[0],X.shape[0]));
foriinrange(X.shape[0]):
x_=np.multiply.outer(np.ones(X.shape[0]),X[i])
D[i]=np.sqrt(np.sum((X-x_)**2,1));
hc_sing_pre=HClust(distance_threshold=0,
n_clusters=None,
metric='precomputed',
linkage='single')
hc_sing_pre.fit(D)
```

We use `dendrogram()` from `scipy.cluster.hierarchy` to plot the dendro- `dendrogram()` gram. However, `dendrogram()` expects a so-called _linkage-matrix representation_ of the clustering, which is not provided by `AgglomerativeClustering()` , but can be computed. The function `compute_linkage()` in the `ISLP.cluster compute_` package is provided for this purpose. 

```
linkage()
ISLP.cluster
```

We can now plot the dendrograms. The numbers at the bottom of the plot identify each observation. The `dendrogram()` function has a default method to color different branches of the tree that suggests a pre-defined cut of the tree at a particular depth. We prefer to overwrite this default by setting this threshold to be infinite. Since we want this behavior for many dendrograms, we store these values in a dictionary `cargs` and pass this as keyword arguments using the notation `**cargs` . 

```
In [41]:cargs={'color_threshold':-np.inf,
'above_threshold_color':'black'}
linkage_comp=compute_linkage(hc_comp)
fig,ax=plt.subplots(1,1,figsize=(8,8))
```

12.5 Lab: Unsupervised Learning 545 

```
dendrogram(linkage_comp ,
ax=ax,
**cargs);
```

We may want to color branches of the tree above and below a cutthreshold differently. This can be achieved by changing the `color_threshold` . Let’s cut the tree at a height of 4, coloring links that merge above 4 in black. 

```
In [42]:fig,ax=plt.subplots(1,1,figsize=(8,8))
dendrogram(linkage_comp ,
ax=ax,
color_threshold=4,
above_threshold_color='black');
```

To determine the cluster labels for each observation associated with a given cut of the dendrogram, we can use the `cut_tree()` function from `cut_tree() scipy.cluster.hierarchy` : 

```
In [43]:cut_tree(linkage_comp ,n_clusters=4).T
```

```
Out[43]:array([[0,1,0,0,1,1,0,1,0,0,2,0,0,0,1,1,0,0,1,
0,0,2,0,2,2,3,2,3,3,3,3,2,3,3,3,3,2,3,
3,3,3,2,3,3,3,3,3,3,3,3]])
```

This can also be achieved by providing an argument `n_clusters` to `HClust()` ; however each cut would require recomputing the clustering. Similarly, trees may be cut by distance threshold with an argument of `distance_threshold` to `HClust()` or `height` to `cut_tree()` . 

```
In [44]:cut_tree(linkage_comp ,height=5)
```

```
Out[44]:array([[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
0,0,1,0,1,1,2,1,2,2,2,2,1,2,2,2,2,1,2,
2,2,2,1,2,2,2,2,2,2,2,2]])
```

To scale the variables before performing hierarchical clustering of the observations, we use `StandardScaler()` as in our PCA example: 

```
In [45]:scaler=StandardScaler()
X_scale=scaler.fit_transform(X)
hc_comp_scale=HClust(distance_threshold=0,
n_clusters=None,
linkage='complete').fit(X_scale)
linkage_comp_scale=compute_linkage(hc_comp_scale)
fig,ax=plt.subplots(1,1,figsize=(8,8))
dendrogram(linkage_comp_scale ,ax=ax,**cargs)
ax.set_title("HierarchicalClusteringwithScaledFeatures");
```

Correlation-based distances between observations can be used for clustering. The correlation between two observations measures the similarity of their feature values.[10] With _n_ observations, the _n × n_ correlation matrix 

> 10Suppose each observation has _p_ features, each a single numerical value. We measure the similarity of two such observations by computing the correlation of these _p_ pairs of numbers. 

546 12. Unsupervised Learning 

can then be used as a similarity (or affinity) matrix, i.e. so that one minus the correlation matrix is the dissimilarity matrix used for clustering. 

Note that using correlation only makes sense for data with at least three features since the absolute correlation between any two observations with measurements on two features is always one. Hence, we will cluster a threedimensional data set. 

```
In [46]:X=np.random.standard_normal((30,3))
corD=1-np.corrcoef(X)
hc_cor=HClust(linkage='complete',
distance_threshold=0,
n_clusters=None,
metric='precomputed')
hc_cor.fit(corD)
linkage_cor=compute_linkage(hc_cor)
fig,ax=plt.subplots(1,1,figsize=(8,8))
dendrogram(linkage_cor ,ax=ax,**cargs)
ax.set_title("CompleteLinkagewithCorrelation -BasedDissimilarity
");
```

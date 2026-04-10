---
layout: default
title: "index"
---

# _Applied_ 

7. In this chapter, we mentioned the use of correlation-based distance and Euclidean distance as dissimilarity measures for hierarchical clustering. It turns out that these two measures are almost equivalent: if each observation has been centered to have mean zero and standard deviation one, and if we let _rij_ denote the correlation between the _i_ th and _j_ th observations, then the quantity 1 _− rij_ is proportional to the squared Euclidean distance between the _i_ th and _j_ th observations. 

On the `USArrests` data, show that this proportionality holds. 

_Hint: The Euclidean distance can be calculated using the_ `pairwise_distances()` _function from the_ `sklearn.metrics` _module, and_ `pairwise_` _correlations can be calculated using the_ `np.corrcoef()` _function._ 

```
distances()
```

8. In Section 12.2.3, a formula for calculating PVE was given in Equation 12.10. We also saw that the PVE can be obtained using the `explained_variance_ratio_` attribute of a fitted `PCA()` estimator. 

On the `USArrests` data, calculate PVE in two ways: 

- (a) Using the `explained_variance_ratio_` output of the fitted `PCA()` estimator, as was done in Section 12.2.3. 

- (b) By applying Equation 12.10 directly. The loadings are stored as the `components_` attribute of the fitted `PCA()` estimator. Use those loadings in Equation 12.10 to obtain the PVE. 

These two approaches should give the same results. 

_Hint: You will only obtain the same results in (a) and (b) if the same data is used in both cases. For instance, if in (a) you performed_ `PCA()` _using centered and scaled variables, then you must center and scale the variables before applying Equation 12.10 in (b)._ 

9. Consider the `USArrests` data. We will now perform hierarchical clustering on the states. 

   - (a) Using hierarchical clustering with complete linkage and Euclidean distance, cluster the states. 

   - (b) Cut the dendrogram at a height that results in three distinct clusters. Which states belong to which clusters? 

12.6 Exercises 555 

   - (c) Hierarchically cluster the states using complete linkage and Euclidean distance, _after scaling the variables to have standard deviation one_ . 

   - (d) What effect does scaling the variables have on the hierarchical clustering obtained? In your opinion, should the variables be scaled before the inter-observation dissimilarities are computed? Provide a justification for your answer. 

10. In this problem, you will generate simulated data, and then perform PCA and _K_ -means clustering on the data. 

   - (a) Generate a simulated data set with 20 observations in each of three classes (i.e. 60 observations total), and 50 variables. _Hint: There are a number of functions in_ `Python` _that you can use to generate data. One example is the_ `normal()` _method of the_ `random()` _function in_ `numpy` _; the_ `uniform()` _method is another option. Be sure to add a mean shift to the observations in each class so that there are three distinct classes._ 

   - (b) Perform PCA on the 60 observations and plot the first two principal component score vectors. Use a different color to indicate the observations in each of the three classes. If the three classes appear separated in this plot, then continue on to part (c). If not, then return to part (a) and modify the simulation so that there is greater separation between the three classes. Do not continue to part (c) until the three classes show at least some separation in the first two principal component score vectors. 

   - (c) Perform _K_ -means clustering of the observations with _K_ = 3. How well do the clusters that you obtained in _K_ -means clustering compare to the true class labels? 

      - _Hint: You can use the_ `pd.crosstab()` _function in_ `Python` _to compare the true class labels to the class labels obtained by clustering. Be careful how you interpret the results: K-means clustering will arbitrarily number the clusters, so you cannot simply check whether the true class labels and clustering labels are the same._ 

   - (d) Perform _K_ -means clustering with _K_ = 2. Describe your results. 

   - (e) Now perform _K_ -means clustering with _K_ = 4, and describe your results. 

   - (f) Now perform _K_ -means clustering with _K_ = 3 on the first two principal component score vectors, rather than on the raw data. That is, perform _K_ -means clustering on the 60 _×_ 2 matrix of which the first column is the first principal component score vector, and the second column is the second principal component score vector. Comment on the results. 

   - (g) Using the `StandardScaler()` estimator, perform _K_ -means clustering with _K_ = 3 on the data _after scaling each variable to have standard deviation one_ . How do these results compare to those obtained in (b)? Explain. 

556 12. Unsupervised Learning 

11. Write a `Python` function to perform matrix completion as in Algorithm 12.1, and as outlined in Section 12.5.2. In each iteration, the function should keep track of the relative error, as well as the iteration count. Iterations should continue until the relative error is small enough or until some maximum number of iterations is reached (set a default value for this maximum number). Furthermore, there should be an option to print out the progress in each iteration. 

Test your function on the `Boston` data. First, standardize the features to have mean zero and standard deviation one using the `StandardScaler()` function. Run an experiment where you randomly leave out an increasing (and nested) number of observations from 5% to 30%, in steps of 5%. Apply Algorithm 12.1 with _M_ = 1 _,_ 2 _, . . . ,_ 8. Display the approximation error as a function of the fraction of observations that are missing, and the value of _M_ , averaged over 10 repetitions of the experiment. 

12. In Section 12.5.2, Algorithm 12.1 was implemented using the `svd()` function from the `np.linalg` module. However, given the connection between the `svd()` function and the `PCA()` estimator highlighted in the lab, we could have instead implemented the algorithm using `PCA()` . 

Write a function to implement Algorithm 12.1 that makes use of `PCA()` rather than `svd()` . 

13. On the book website, `www.statlearning.com` , there is a gene expression data set ( `Ch12Ex13.csv` ) that consists of 40 tissue samples with measurements on 1,000 genes. The first 20 samples are from healthy patients, while the second 20 are from a diseased group. 

   - (a) Load in the data using `pd.read_csv()` . You will need to select `header = None` . 

   - (b) Apply hierarchical clustering to the samples using correlationbased distance, and plot the dendrogram. Do the genes separate the samples into the two groups? Do your results depend on the type of linkage used? 

   - (c) Your collaborator wants to know which genes differ the most across the two groups. Suggest a way to answer this question, and apply it here. 

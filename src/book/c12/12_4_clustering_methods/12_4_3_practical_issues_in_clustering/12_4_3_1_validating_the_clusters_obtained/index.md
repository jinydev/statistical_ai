---
layout: default
title: "index"
---

# Validating the Clusters Obtained 

Any time clustering is performed on a data set we will find clusters. But we really want to know whether the clusters that have been found represent true subgroups in the data, or whether they are simply a result of _clustering the noise_ . For instance, if we were to obtain an independent set of observations, then would those observations also display the same set of clusters? This is a hard question to answer. There exist a number of techniques for assigning a p-value to a cluster in order to assess whether there is more 

534 12. Unsupervised Learning 

![Figure 12.16](./img/12_16.png)

**FIGURE 12.16.** _An eclectic online retailer sells two items: socks and computers._ Left: _the number of pairs of socks, and computers, purchased by eight online shoppers is displayed. Each shopper is shown in a different color. If inter-observation dissimilarities are computed using Euclidean distance on the raw variables, then the number of socks purchased by an individual will drive the dissimilarities obtained, and the number of computers purchased will have little effect. This might be undesirable, since (1) computers are more expensive than socks and so the online retailer may be more interested in encouraging shoppers to buy computers than socks, and (2) a large difference in the number of socks purchased by two shoppers may be less informative about the shoppers’ overall shopping preferences than a small difference in the number of computers purchased._ Center: _the same data are shown, after scaling each variable by its standard deviation. Now the two products will have a comparable effect on the inter-observation dissimilarities obtained._ Right: _the same data are displayed, but now the y-axis represents the number of dollars spent by each online shopper on socks and on computers. Since computers are much more expensive than socks, now computer purchase history will drive the inter-observation dissimilarities obtained._ 

evidence for the cluster than one would expect due to chance. However, there has been no consensus on a single best approach. More details can be found in ESL.[8] 

Other Considerations in Clustering 

Both _K_ -means and hierarchical clustering will assign each observation to a cluster. However, sometimes this might not be appropriate. For instance, suppose that most of the observations truly belong to a small number of (unknown) subgroups, and a small subset of the observations are quite different from each other and from all other observations. Then since _K_ - means and hierarchical clustering force _every_ observation into a cluster, the clusters found may be heavily distorted due to the presence of outliers that do not belong to any cluster. Mixture models are an attractive approach for accommodating the presence of such outliers. These amount to a _soft_ version of _K_ -means clustering, and are described in ESL. 

> 8ESL: _The Elements of Statistical Learning_ by Hastie, Tibshirani and Friedman. 

12.5 Lab: Unsupervised Learning 535 

In addition, clustering methods generally are not very robust to perturbations to the data. For instance, suppose that we cluster _n_ observations, and then cluster the observations again after removing a subset of the _n_ observations at random. One would hope that the two sets of clusters obtained would be quite similar, but often this is not the case! 

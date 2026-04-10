---
layout: default
title: "index"
---

# _12.2.3 The Proportion of Variance Explained_ 

In Figure 12.2, we performed PCA on a three-dimensional data set (lefthand panel) and projected the data onto the first two principal component loading vectors in order to obtain a two-dimensional view of the data (i.e. the principal component score vectors; right-hand panel). We see that this two-dimensional representation of the three-dimensional data does successfully capture the major pattern in the data: the orange, green, and cyan observations that are near each other in three-dimensional space remain nearby in the two-dimensional representation. Similarly, we have seen on the `USArrests` data set that we can summarize the 50 observations and 4 variables using just the first two principal component score vectors and the first two principal component loading vectors. 

We can now ask a natural question: how much of the information in a given data set is lost by projecting the observations onto the first few principal components? That is, how much of the variance in the data is _not_ contained in the first few principal components? More generally, we are interested in knowing the _proportion of variance explained_ (PVE) by each proportion 

> 4Technically, the solution to (12.6) is not unique. Thus, it is more precise to state that any solution to (12.6) can be easily transformed to yield the principal components. 

> of variance explained 

12.2 Principal Components Analysis 511 

principal component. The _total variance_ present in a data set (assuming that the variables have been centered to have mean zero) is defined as

$$
\sum_{j=1}^p \operatorname{Var}(X_j) = \sum_{j=1}^p \frac{1}{n} \sum_{i=1}^n x_{ij}^2 \quad (12.8)
$$

and the variance explained by the _m_ th principal component is

$$
\frac{1}{n} \sum_{i=1}^n z_{im}^2 = \frac{1}{n} \sum_{i=1}^n \left( \sum_{j=1}^p \phi_{jm} x_{ij} \right)^2 \quad (12.9)
$$

Therefore, the PVE of the _m_ th principal component is given by

$$
\frac{\sum_{i=1}^n \left( \sum_{j=1}^p \phi_{jm} x_{ij} \right)^2}{\sum_{j=1}^p \sum_{i=1}^n x_{ij}^2} \quad (12.10)
$$

The PVE of each principal component is a positive quantity. In order to compute the cumulative PVE of the first _M_ principal components, we can simply sum (12.10) over each of the first _M_ PVEs. In total, there are min( _n −_ 1 _, p_ ) principal components, and their PVEs sum to one. In Section 12.2.2, we showed that the first _M_ principal component loading and score vectors can be interpreted as the best _M_ -dimensional approximation to the data, in terms of residual sum of squares. It turns out that the variance of the data can be decomposed into the variance of the first _M_ principal components plus the mean squared error of this _M_ -dimensional approximation, as follows:

$$
\sum_{j=1}^p \sum_{i=1}^n x_{ij}^2 = \sum_{m=1}^M \sum_{i=1}^n z_{im}^2 + \sum_{j=1}^p \sum_{i=1}^n \left( x_{ij} - \sum_{m=1}^M z_{im} \phi_{jm} \right)^2 \quad (12.11)
$$

The three terms in this decomposition are discussed in (12.8), (12.9), and (12.7), respectively. Since the first term is fixed, we see that by maximizing the variance of the first _M_ principal components, we minimize the mean squared error of the _M_ -dimensional approximation, and vice versa. This explains why principal components can be equivalently viewed as minimizing the approximation error (as in Section 12.2.2) or maximizing the variance (as in Section 12.2.1). 

Moreover, we can use (12.11) to see that the PVE defined in (12.10) equals

$$
\frac{\text{TSS} - \text{RSS}_M}{\text{TSS}} = 1 - \frac{\text{RSS}_M}{\text{TSS}} \quad (12.12)
$$

where TSS represents the total sum of squared elements of **X** , and RSS represents the residual sum of squares of the _M_ -dimensional approximation given by the principal components. Recalling the definition of _R_[2] from (3.17), this means that we can interpret the PVE as the _R_[2] of the approximation for **X** given by the first _M_ principal components. 

512 12. Unsupervised Learning 

![Figure 12.3](./img/12_3.png)

**FIGURE 12.3.** Left: _a scree plot depicting the proportion of variance explained by each of the four principal components in the_ `USArrests` _data._ Right: _the cumulative proportion of variance explained by the four principal components in the_ `USArrests` _data._ 

In the `USArrests` data, the first principal component explains 62.0 % of the variance in the data, and the next principal component explains 24.7 % of the variance. Together, the first two principal components explain almost 87 % of the variance in the data, and the last two principal components explain only 13 % of the variance. This means that Figure 12.1 provides a pretty accurate summary of the data using just two dimensions. The PVE of each principal component, as well as the cumulative PVE, is shown in Figure 12.3. The left-hand panel is known as a _scree plot_ , and will be scree plot discussed later in this chapter. 

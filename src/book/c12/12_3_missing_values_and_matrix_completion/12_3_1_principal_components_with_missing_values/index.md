---
layout: default
title: "index"
---

# Principal Components with Missing Values 

In Section 12.2.2, we showed that the first _M_ principal component score and loading vectors provide the “best” approximation to the data matrix **X** , in the sense of (12.6). Suppose that some of the observations _xij_ are missing. We now show how one can both impute the missing values and solve the principal component problem at the same time. We return to a modified form of the optimization problem (12.6),

$$
\min_{\mathbf{A} \in \mathbb{R}^{n \times M}, \mathbf{B} \in \mathbb{R}^{p \times M}} \left\{ \sum_{(i,j) \in \mathcal{O}} \left( x_{ij} - \sum_{m=1}^M a_{im} b_{jm} \right)^2 \right\} \quad (12.13)
$$

where _O_ is the set of all _observed_ pairs of indices ( _i, j_ ), a subset of the possible _n × p_ pairs. 

Once we solve this problem: 

- ˆ 

- • we can estimate a missing observation _xij_ using _xij_ =[�] _[M] m_ =1 _[a]_[ˆ] _[im]_[ˆ] _[b][jm]_[,] where _a_ ˆ _im_ and[ˆ] _bjm_ are the ( _i, m_ ) and ( _j, m_ ) elements, respectively, of the matrices **A**[ˆ] and **B**[ˆ] that solve (12.12); and 

- we can (approximately) recover the _M_ principal component scores and loadings, as we did when the data were complete. 

It turns out that solving (12.12) exactly is difficult, unlike in the case of complete data: the eigen decomposition no longer applies. But the simple iterative approach in Algorithm 12.1, which is demonstrated in Section 12.5.2, typically provides a good solution.[56] 

We illustrate Algorithm 12.1 on the `USArrests` data. There are _p_ = 4 variables and _n_ = 50 observations (states). We first standardized the data so each variable has mean zero and standard deviation one. We then randomly selected 20 of the 50 states, and then for each of these we randomly set one of the four variables to be missing. Thus, 10% of the elements of the data matrix were missing. We applied Algorithm 12.1 with _M_ = 1 principal component. Figure 12.5 shows that the recovery of the missing elements 

> 5This algorithm is referred to as “Hard-Impute” in Mazumder, Hastie, and Tibshirani (2010) “Spectral regularization algorithms for learning large incomplete matrices”, published in _Journal of Machine Learning Research_ , pages 2287–2322. 

> 6Each iteration of Step 2 of this algorithm decreases the objective (12.14). However, the algorithm is not guaranteed to achieve the global optimum of (12.12). 

12.3 Missing Values and Matrix Completion 517 

**Algorithm 12.1** _Iterative Algorithm for Matrix Completion_ 

1. Create a complete data matrix **X**[˜] of dimension _n × p_ of which the ( _i, j_ ) element equals

$$
\tilde{x}_{ij} = \begin{cases} x_{ij} & \text{if } (i,j) \in \mathcal{O} \\ \bar{x}_j & \text{if } (i,j) \notin \mathcal{O} \end{cases}
$$

where _x_ ¯ _j_ is the average of the observed values for the _j_ th variable in the incomplete data matrix **X** . Here, _O_ indexes the observations that are observed in **X** . 

2. Repeat steps (a)–(c) until the objective (12.14) fails to decrease: (a) Solve

$$
\min_{\mathbf{A} \in \mathbb{R}^{n \times M}, \mathbf{B} \in \mathbb{R}^{p \times M}} \left\{ \sum_{j=1}^p \sum_{i=1}^n \left( \tilde{x}_{ij} - \sum_{m=1}^M a_{im} b_{jm} \right)^2 \right\} \quad (12.14)
$$

by computing the principal components of **X**[˜] . 

(b) For each element ( _i, j_ ) _∈O/_ , set _x_ ˜ _ij ←_[�] _[M] m_ =1 _[a]_[ˆ] _[im]_[ˆ] _[b][jm]_[.] (c) Compute the objective

$$
\sum_{(i,j) \in \mathcal{O}} \left( x_{ij} - \sum_{m=1}^M \hat{a}_{im} \hat{b}_{jm} \right)^2 \quad (12.15)
$$

3. Return the estimated missing entries _xij,_ ( _i, j_ ) _∈O/_ . 

is pretty accurate. Over 100 random runs of this experiment, the average correlation between the true and imputed values of the missing elements is 0.63, with a standard deviation of 0.11. Is this good performance? To answer this question, we can compare this correlation to what we would have gotten if we had estimated these 20 values using the _complete_ data — that is, if we had simply computed _x_ ˆ _ij_ = _zi_ 1 _φj_ 1, where _zi_ 1 and _φj_ 1 are elements of the first principal component score and loading vectors of the complete data.[7] Using the complete data in this way results in an average correlation of 0.79 between the true and estimated values for these 20 elements, with a standard deviation of 0.08. Thus, our imputation method does worse than the method that uses all of the data (0 _._ 63 _±_ 0 _._ 11 versus 0 _._ 79 _±_ 0 _._ 08), but its performance is still pretty good. (And of course, the method that uses all of the data cannot be applied in a real-world setting with missing data.) 

Figure 12.6 further indicates that Algorithm 12.1 performs fairly well on this dataset. 

> 7This is an unattainable gold standard, in the sense that with missing data, we of course cannot compute the principal components of the complete data. 

12. Unsupervised Learning 

518 

![Figure 12.5](./img/12_5.png)

**FIGURE 12.5.** _Missing value imputation on the_ `USArrests` _data. Twenty values (10% of the total number of matrix elements) were artificially set to be missing, and then imputed via Algorithm 12.1 with M_ = 1 _. The figure displays the true value xij and the imputed value x_ ˆ _ij for all twenty missing values. For each of the twenty missing values, the color indicates the variable, and the label indicates the state. The correlation between the true and imputed values is around_ 0 _._ 63 _._ 

We close with a few observations: 

- The `USArrests` data has only four variables, which is on the low end for methods like Algorithm 12.1 to work well. For this reason, for this demonstration we randomly set at most one variable per state to be missing, and only used _M_ = 1 principal component. 

- In general, in order to apply Algorithm 12.1, we must select _M_ , the number of principal components to use for the imputation. One approach is to randomly leave out a few additional elements from the matrix, and select _M_ based on how well those known values are recovered. This is closely related to the validation-set approach seen in Chapter 5. 

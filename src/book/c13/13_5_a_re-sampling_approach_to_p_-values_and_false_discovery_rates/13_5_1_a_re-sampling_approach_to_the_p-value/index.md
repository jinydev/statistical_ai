---
layout: default
title: "index"
---

# _13.5.1 A Re-Sampling Approach to the p-Value_ 

We return to the example of Section 13.1.1, in which we wish to test whether the mean of a random variable _X_ equals the mean of a random variable _Y_ , i.e. _H_ 0 : E( _X_ ) = E( _Y_ ), against the alternative _Ha_ : E( _X_ ) = E( _Y_ ). Given _nX_ independent observations from _X_ and _nY_ independent observations from _Y_ , the two-sample _t_ -statistic takes the form

$$
T = \frac{\hat{\mu}_X - \hat{\mu}_Y}{s \sqrt{1/n_X + 1/n_Y}} \quad (13.10)
$$


where _µ_ ˆ _X_ = _n_ 1 _X_ � _ni_ =1 _X[x][i]_[,] _[µ]_[ˆ] _[Y]_[=] _n_ 1 _Y_ � _ni_ =1 _Y[y][i]_[,] _[s]_[=] ~~�~~ ( _nX −_ 1 _n_ ) _Xs_[2] _X_ +[+] _nY_[(] _[n] −[Y]_ 2 _[ −]_[1][)] _[s]_[2] _Y_ , and _s_[2] _X_[and] _[s]_[2] _Y_[are][unbiased][estimators][of][the][variances][in][the][two][groups.] A large (absolute) value of _T_ provides evidence against _H_ 0. If _nX_ and _nY_ are large, then _T_ in (13.11) approximately follows a _N_ (0 _,_ 1) distribution. But if _nX_ and _nY_ are small, then in the absence of a strong assumption about the distribution of _X_ and _Y_ , we do not know the theoretical null distribution of _T_ .[17] In this case, it turns out that we can approximate the null distribution of _T_ using a _re-sampling_ approach, or re-sampling more specifically, a _permutation_ approach. 

permutation 

To do this, we conduct a thought experiment. If _H_ 0 holds, so that E( _X_ ) = E( _Y_ ), and we make the stronger assumption that the distributions of _X_ and _Y_ are the same, then the distribution of _T_ is invariant under swapping observations of _X_ with observations of _Y_ . That is, if we randomly swap some of the observations in _X_ with the observations in _Y_ , then _the test statistic T in_ (13.11) _computed based on this swapped data has the same distribution as T based on the original data._ This is true only if _H_ 0 holds, and the distributions of _X_ and _Y_ are the same. 

This suggests that in order to approximate the null distribution of _T_ , we can take the following approach. We randomly permute the _nX_ + _nY_ observations _B_ times, for some large value of _B_ , and each time we compute (13.11). We let _T[∗]_[1] _, . . . , T[∗][B]_ denote the values of (13.11) on the permuted data. These can be viewed as an approximation of the null distribution of _T_ under _H_ 0. Recall that by definition, a _p_ -value is the probability of observing a test statistic at least this extreme under _H_ 0. Therefore, to compute a _p_ -value for _T_ , we can simply compute

$$
p\text{-value} = \frac{1}{B} \sum_{b=1}^B I(|T^{*b}| \ge |T|)
$$

the fraction of permuted datasets for which the value of the test statistic is at least as extreme as the value observed on the original data. This procedure is summarized in Algorithm 13.3. 

> 17If we assume that _X_ and _Y_ are normally distributed, then _T_ in (13.11) follows a _t_ -distribution with _nX_ + _nY −_ 2 degrees of freedom under _H_ 0. However, in practice, the distribution of random variables is rarely known, and so it can be preferable to perform a re-sampling approach instead of making strong and unjustified assumptions. If the results of the re-sampling approach disagree with the results of assuming a theoretical null distribution, then the results of the re-sampling approach are more trustworthy. 

13.5 A Re-Sampling Approach to _p_ -Values and False Discovery Rates 

579 

**Algorithm 13.3** _Re-Sampling p-Value for a Two-Sample t-Test_ 

1. Compute _T_ , defined in (13.11), on the original data _x_ 1 _, . . . , xnX_ and _y_ 1 _, . . . , ynY_ . 

2. For _b_ = 1 _, . . . , B_ , where _B_ is a large number (e.g. _B_ = 10 _,_ 000): 

   - (a) Permute the _nX_ + _nY_ observations at random. Call the first _nX_ permuted observations _x[∗]_ 1 _[, . . . , x][∗] nX_[,][and][call][the][remaining] _[n][Y]_ observations _y_ 1 _[∗][, . . . , y] n[∗] Y_[.] 

   - (b) Compute (13.11) on the permuted data _x[∗]_ 1 _[, . . . , x][∗] nX_ and _y_ 1 _[∗][, . . . , y] n[∗] Y_[,][and][call][the][result] _[T][ ∗][b]_[.]

$$
p\text{-value} = \frac{1}{B} \sum_{b=1}^B I(|T^{*b}| \ge |T|) \quad (13.11)
$$


We try out this procedure on the `Khan` dataset, which consists of expression measurements for 2 _,_ 308 genes in four sub-types of small round blood cell tumors, a type of cancer typically seen in children. This dataset is part of the `ISLR2` package. We restrict our attention to the two sub-types for which the most observations are available: rhabdomyosarcoma ( _nX_ = 29) and Burkitt’s lymphoma ( _nY_ = 25). 

A two-sample _t_ -test for the null hypothesis that the 11th gene’s mean expression values are equal in the two groups yields _T_ = _−_ 2 _._ 09. Using the theoretical null distribution, which is a _t_ 52 distribution (since _nX_ + _nY −_ 2 = 52), we obtain a _p_ -value of 0 _._ 041. (Note that a _t_ 52 distribution is virtually indistinguishable from a _N_ (0 _,_ 1) distribution.) If we instead apply Algorithm 13.3 with _B_ = 10 _,_ 000, then we obtain a _p_ -value of 0 _._ 042. Figure 13.7 displays the theoretical null distribution, the re-sampling null distribution, and the actual value of the test statistic ( _T_ = _−_ 2 _._ 09) for this gene. In this example, we see very little difference between the _p_ -values obtained using the theoretical null distribution and the re-sampling null distribution. 

By contrast, Figure 13.8 shows an analogous set of results for the 877th gene. In this case, there is a substantial difference between the theoretical and re-sampling null distributions, which results in a difference between their _p_ -values. 

In general, in settings with a smaller sample size or a more skewed data distribution (so that the theoretical null distribution is less accurate), the difference between the re-sampling and theoretical _p_ -values will tend to be more pronounced. In fact, the substantial difference between the resampling and theoretical null distributions in Figure 13.8 is due to the fact that a single observation in the 877th gene is very far from the other observations, leading to a very skewed distribution. 

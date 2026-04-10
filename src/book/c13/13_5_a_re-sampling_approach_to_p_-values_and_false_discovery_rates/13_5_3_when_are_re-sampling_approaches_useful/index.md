---
layout: default
title: "index"
---

# _13.5.3 When Are Re-Sampling Approaches Useful?_ 

In Sections 13.5.1 and 13.5.2, we considered testing null hypotheses of the form _H_ 0 : E( _X_ ) = E( _Y_ ) using a two-sample _t_ -statistic (13.11), for which we 

> 18To implement Algorithm 13.4 efficiently, the same set of permutations in Step 2(b)i. should be used for all _m_ null hypotheses. 

582 13. Multiple Testing 

**Algorithm 13.4** _Plug-In FDR for a Two-Sample T -Test_ 

1. Select a threshold _c_ , where _c >_ 0. 

2. For _j_ = 1 _, . . . , m_ : 

- (a) Compute _T_[(] _[j]_[)] , the two-sample _t_ -statistic (13.11) for the null hypothesis _H_ 0 _j_ on the basis of the original data, _x_[(] 1 _[j]_[)] _[, . . . , x] n_[(] _[j] X_[)] and _y_ 1[(] _[j]_[)] _[, . . . , y] n_[(] _[j] Y_[)][.] 

- (b) For _b_ = 1 _, . . . , B_ , where _B_ is a large number (e.g. _B_ = 10 _,_ 000): 

   i. Permute the $n$ observations.
   ii. Compute the $m$ test statistics $T_1^{*b}, \dots, T_m^{*b}$.
   iii. Let $V^{*b} = \sum_{j=1}^m I(|T_j^{*b}| \ge c)$.

$$
\hat{V} = \frac{1}{B} \sum_{b=1}^B V^{*b} \quad (13.14)
$$

5. The estimated FDR associated with the threshold _c_ is _V /R_[�] . 

approximated the null distribution via a re-sampling approach. We saw that using the re-sampling approach gave us substantially different results from using the theoretical _p_ -value approach in Figure 13.8, but not in Figure 13.7. 

In general, there are two settings in which a re-sampling approach is particularly useful: 

1. Perhaps no theoretical null distribution is available. This may be the case if you are testing an unusual null hypothesis _H_ 0, or using an unsual test statistic _T_ . 

2. Perhaps a theoretical null distribution _is_ available, but the assumptions required for its validity do not hold. For instance, the twosample _t_ -statistic in (13.11) follows a _tnX_ + _nY −_ 2 distribution only if the observations are normally distributed. Furthermore, it follows a _N_ (0 _,_ 1) distribution only if _nX_ and _nY_ are quite large. If the data are non-normal and _nX_ and _nY_ are small, then _p_ -values that make use of the theoretical null distribution will not be valid (i.e. they will not properly control the Type I error). 

In general, if you can come up with a way to re-sample or permute your observations in order to generate data that follow the null distribution, then you can compute _p_ -values or estimate the FDR using variants of Algorithms 13.3 and 13.4. In many real-world settings, this provides a powerful tool for hypothesis testing when no out-of-box hypothesis tests are available, or when the key assumptions underlying those out-of-box tests are violated. 

13.6 Lab: Multiple Testing 583 

![Figure 13.9](./img/13_9.png)

**FIGURE 13.9.** _For j_ = 1 _, . . . , m_ = 2 _,_ 308 _, we tested the null hypothesis that for the jth gene in the_ `Khan` _dataset, the mean expression in Burkitt’s lymphoma equals the mean expression in rhabdomyosarcoma. For each value of k from_ 1 _to_ 2 _,_ 308 _, the y-axis displays the estimated FDR associated with rejecting the null hypotheses corresponding to the k smallest p-values. The orange dashed curve shows the FDR obtained using the Benjamini–Hochberg procedure, whereas the blue solid curve shows the FDR obtained using the re-sampling approach of Algorithm 13.4, with B_ = 10 _,_ 000 _. There is very little difference between the two FDR estimates. According to either estimate, rejecting the null hypothesis for the 500 genes with the smallest p-values corresponds to an FDR of around 17.7%._ 

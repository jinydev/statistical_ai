---
layout: default
title: "index"
---

# _13.5.2 A Re-Sampling Approach to the False Discovery Rate_ 

Now, suppose that we wish to control the FDR for _m_ null hypotheses, _H_ 01 _, . . . , H_ 0 _m_ , in a setting in which either no theoretical null distribution is available, or else we simply prefer to avoid the use of a theoretical null 

13. Multiple Testing 

580 

![Figure 13.7](./img/13_7.png)

**FIGURE 13.7.** _The_ 11 _th gene in the_ `Khan` _dataset has a test statistic of T_ = _−_ 2 _._ 09 _. Its theoretical and re-sampling null distributions are almost identical. The theoretical p-value equals_ 0 _._ 041 _and the re-sampling p-value equals_ 0 _._ 042 _._ 

![Figure 13.8](./img/13_8.png)

**FIGURE 13.8.** _The_ 877 _th gene in the_ `Khan` _dataset has a test statistic of T_ = _−_ 0 _._ 57 _. Its theoretical and re-sampling null distributions are quite different. The theoretical p-value equals_ 0 _._ 571 _, and the re-sampling p-value equals_ 0 _._ 673 _._ 

distribution. As in Section 13.5.1, we make use of a two-sample _t_ -statistic for each hypothesis, leading to the test statistics _T_ 1 _, . . . , Tm_ . We could simply compute a _p_ -value for each of the _m_ null hypotheses, as in Section 13.5.1, and then apply the Benjamini–Hochberg procedure of Section 13.4.2 to these _p_ -values. However, it turns out that we can do this in a more direct way, without even needing to compute _p_ -values. 

Recall from Section 13.4 that the FDR is defined as E( _V/R_ ), using the notation in Table 13.2. In order to estimate the FDR via re-sampling, we first make the following approximation:

$$
\text{FDR} = E(V/R) \approx \frac{E(V)}{E(R)} \quad (13.12)
$$

Now suppose we reject any null hypothesis for which the test statistic exceeds _c_ in absolute value. Then computing _R_ in the denominator on the right-hand side of (13.13) is straightforward: _R_ =[�] _[m] j_ =1[1][(] _[|][T] j[|≥][c]_[)][.] 

13.5 A Re-Sampling Approach to _p_ -Values and False Discovery Rates 

581 

However, the numerator E( _V_ ) on the right-hand side of (13.13) is more challenging. This is the expected number of false positives associated with rejecting any null hypothesis for which the test statistic exceeds _c_ in absolute value. At the risk of stating the obvious, estimating _V_ is challenging because we do not know which of _H_ 01 _, . . . , H_ 0 _m_ are really true, and so we do not know which rejected hypotheses are false positives. To overcome this problem, we take a re-sampling approach, in which we simulate data under _H_ 01 _, . . . , H_ 0 _m_ , and then compute the resulting test statistics. The number of re-sampled test statistics that exceed _c_ provides an estimate of _V_ . 

In greater detail, in the case of a two-sample _t_ -statistic (13.11) for each of the null hypotheses _H_ 01 _, . . . , H_ 0 _m_ , we can estimate E( _V_ ) as follows. Let _x_[(] 1 _[j]_[)] _[, . . . , x] n_[(] _[j] X_[)][and] _[y]_ 1[(] _[j]_[)] _[, . . . , y] n_[(] _[j] Y_[)][denote][the][data][associated][with][the] _[j]_[th] null hypothesis, _j_ = 1 _, . . . , m_ . We permute these _nX_ + _nY_ observations at random, and then compute the _t_ -statistic on the permuted data. For this permuted data, we know that all of the null hypotheses _H_ 01 _, . . . , H_ 0 _m_ hold; therefore, the number of permuted _t_ -statistics that exceed the threshold _c_ in absolute value provides an estimate for E( _V_ ). This estimate can be further improved by repeating the permutation process _B_ times, for a large value of _B_ , and averaging the results. 

Algorithm 13.4 details this procedure.[18] It provides what is known as a _plug-in estimate_ of the FDR, because the approximation in (13.13) allows us to estimate the FDR by plugging _R_ into the denominator and an estimate for E( _V_ ) into the numerator. 

We apply the re-sampling approach to the FDR from Algorithm 13.4, as well as the Benjamini–Hochberg approach from Algorithm 13.2 using theoretical _p_ -values, to the _m_ = 2 _,_ 308 genes in the `Khan` dataset. Results are shown in Figure 13.9. We see that for a given number of rejected hypotheses, the estimated FDRs are almost identical for the two methods. 

We began this section by noting that in order to control the FDR for _m_ hypothesis tests using a re-sampling approach, we could simply compute _m_ re-sampling _p_ -values as in Section 13.5.1, and then apply the Benjamini– Hochberg procedure of Section 13.4.2 to these _p_ -values. It turns out that if we define the _j_ th re-sampling _p_ -value as

$$
p_j = \frac{1}{B} \sum_{b=1}^B I(|T_j^{*b}| \ge |T_j|) \quad (13.13)
$$

for _j_ = 1 _, . . . , m_ , instead of as in (13.12), then applying the Benjamini– Hochberg procedure to these re-sampled _p_ -values is _exactly_ equivalent to Algorithm 13.4. Note that (13.14) is an alternative to (13.12) that pools the information across all _m_ hypothesis tests in approximating the null distribution. 

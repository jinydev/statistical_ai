---
layout: default
title: "index"
---

# 11.4 The Log-Rank Test 

We now continue our analysis of the `BrainCancer` data introduced in Section 11.3. We wish to compare the survival of males to that of females. Figure 11.3 shows the Kaplan–Meier survival curves for the two groups. Females seem to fare a little better up to about 50 months, but then the two curves both level off to about 50%. How can we carry out a formal test of equality of the two survival curves? 

At first glance, a two-sample _t_ -test seems like an obvious choice: we could test whether the mean survival time among the females equals the mean survival time among the males. But the presence of censoring again creates a complication. To overcome this challenge, we will conduct a _log-rank test_ ,[4] 

log-rank test 

11.4 The Log-Rank Test 475 

||Group 1<br>Group 2|Total|
|---|---|---|
|Died<br>Survived|_q_1_k_<br>_q_2_k_<br>_r_1_k −q_1_k_<br>_r_2_k −q_2_k_|_qk_<br>_rk −qk_|
|Total|_r_1_k_<br>_r_2_k_|_rk_|



**TABLE 11.1.** _Among the set of patients at risk at time dk, the number of patients who died and survived in each of two groups is reported._ 

which examines how the events in each group unfold sequentially in time. 

Recall from Section 11.3 that _d_ 1 _< d_ 2 _< · · · < dK_ are the unique death times among the non-censored patients, _rk_ is the number of patients at risk at time _dk_ , and _qk_ is the number of patients who died at time _dk_ . We further define _r_ 1 _k_ and _r_ 2 _k_ to be the number of patients in groups 1 and 2, respectively, who are at risk at time _dk_ . Similarly, we define _q_ 1 _k_ and _q_ 2 _k_ to be the number of patients in groups 1 and 2, respectively, who died at time _dk_ . Note that _r_ 1 _k_ + _r_ 2 _k_ = _rk_ and _q_ 1 _k_ + _q_ 2 _k_ = _qk_ . 

At each death time _dk_ , we construct a 2 _×_ 2 table of counts of the form shown in Table 11.1. Note that if the death times are unique (i.e. no two individuals die at the same time), then one of _q_ 1 _k_ and _q_ 2 _k_ equals one, and the other equals zero. 

The main idea behind the log-rank test statistic is as follows. In order to test _H_ 0 : E( _X_ ) = _µ_ for some random variable _X_ , one approach is to construct a test statistic of the form 

$$
W = \frac{ \sum_{k=1}^K (q_{1k} - \operatorname{E}(q_{1k})) }{ \sqrt{ \sum_{k=1}^K \operatorname{Var}(q_{1k}) } } \quad (11.5)
$$


To construct the log-rank test statistic, we compute a quantity that takes exactly the form (11.4), with _X_ =[�] _[K] k_ =1 _[q]_[1] _[k]_[,][where] _[q]_[1] _[k]_[is][given][in][the][top] left of Table 11.1. 

In greater detail, if there is no difference in survival between the two groups, and conditioning on the row and column totals in Table 11.1, the expected value of _q_ 1 _k_ is 

$$
\operatorname{E}(q_{1k}) = \frac{q_k}{n_k} n_{1k} \quad (11.6)
$$


So the expected value of _X_ =[�] _[K] k_ =1 _[q]_[1] _[k]_[is] _[µ]_[=][�] _k[K]_ =1 _rr_ 1 _kk[q][k]_[.][Furthermore,] it can be shown[5] that the variance of _q_ 1 _k_ is 

$$
\operatorname{Var}(q_{1k}) = \frac{q_k (n_{1k} / n_k) (1 - n_{1k}/n_k) (n_k - q_k)}{n_k - 1} \quad (11.7)
$$


Though _q_ 11 _, . . . , q_ 1 _K_ may be correlated, we nonetheless estimate 

$$
\operatorname{Var} \left( \sum_{k=1}^K q_{1k} \right) = \sum_{k=1}^K \operatorname{Var}(q_{1k})
$$


> 4The log-rank test is also known as the _Mantel–Haenszel test_ or _Cochran–Mantel– Haenszel test_ . 

> 5For details, see Exercise 7 at the end of this chapter. 

476 11. Survival Analysis and Censored Data 

Therefore, to compute the log-rank test statistic, we simply proceed as in (11.4), with _X_ =[�] _[K] k_ =1 _[q]_[1] _[k]_[, making use of][(][11.5][) and (][11.7][). That is, we calculate

$$
W = \frac{ \sum_{k=1}^K \left( q_{1k} - \frac{q_k}{n_k} n_{1k} \right) }{ \sqrt{ \sum_{k=1}^K \frac{q_k (n_{1k} / n_k) (1 - n_{1k}/n_k) (n_k - q_k)}{n_k - 1} } } \quad (11.8)
$$


When the sample size is large, the log-rank test statistic _W_ has approximately a standard normal distribution; this can be used to compute a _p_ -value for the null hypothesis that there is no difference between the survival curves in the two groups.[6] 

Comparing the survival times of females and males on the `BrainCancer` data gives a log-rank test statistic of _W_ = 1 _._ 2, which corresponds to a twosided _p_ -value of 0 _._ 2 using the theoretical null distribution, and a _p_ -value of 0 _._ 25 using the permutation null distribution with 1,000 permutations. Thus, we cannot reject the null hypothesis of no difference in survival curves between females and males. 

The log-rank test is closely related to Cox’s proportional hazards model, which we discuss in Section 11.5.2. 

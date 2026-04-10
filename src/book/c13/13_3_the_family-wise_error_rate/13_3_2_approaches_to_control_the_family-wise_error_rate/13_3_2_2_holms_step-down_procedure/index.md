---
layout: default
title: "index"
---

# Holm’s Step-Down Procedure 

_Holm’s method_ , also known as Holm’s step-down procedure or the Holm– Holm’s Bonferroni method, is an alternative to the Bonferroni procedure. Holm’s method method controls the FWER, but it is less conservative than Bonferroni, in the sense that it will reject more null hypotheses, typically resulting in fewer Type II errors and hence greater power. The procedure is summarized in Algorithm 13.1. The proof that this method controls the FWER is similar to, but slightly more complicated than, the argument in (13.6) that the Bonferroni method controls the FWER. It is worth noting that in Holm’s procedure, the threshold that we use to reject each null hypothesis — _p_ ( _L_ ) in Step 5 — actually depends on the values of _all m_ of the _p_ -values. (See the definition of _L_ in (13.7).) This is in contrast to the Bonferroni procedure, in which to control the FWER at level _α_ , we reject any null hypotheses for which the _p_ -value is below _α/m_ , regardless of the other _p_ -values. Holm’s method makes no independence assumptions about the _m_ hypothesis tests, and is uniformly more powerful than the Bonferroni method — it will 

method 

13.3 The Family-Wise Error Rate 569 

**Algorithm 13.1** _Holm’s Step-Down Procedure to Control the FWER_ 

1. Specify _α_ , the level at which to control the FWER. 

2. Compute _p_ -values, _p_ 1 _, . . . , pm_ , for the _m_ null hypotheses _H_ 01 _, . . . , H_ 0 _m_ . 

3. Order the _m p_ -values so that _p_ (1) _≤ p_ (2) _≤· · · ≤ p_ ( _m_ ). 

4. Define

$$
L = \min \left\{ j : p_{(j)} > \frac{\alpha}{m - j + 1} \right\} \quad (13.7)
$$

always reject at least as many null hypotheses as Bonferroni — and so it should always be preferred. 

We now consider applying Holm’s method to the first five fund managers in the `Fund` dataset in Table 13.3, while controlling the FWER at level 0 _._ 05. The ordered _p_ -values are _p_ (1) = 0 _._ 006 _, p_ (2) = 0 _._ 012 _, p_ (3) = 0 _._ 601 _, p_ (4) = 0 _._ 756 and _p_ (5) = 0 _._ 918. The Holm procedure rejects the first two null hypotheses, because _p_ (1) = 0 _._ 006 _<_ 0 _._ 05 _/_ (5 + 1 _−_ 1) = 0 _._ 01 and _p_ (2) = 0 _._ 012 _<_ 0 _._ 05 _/_ (5 + 1 _−_ 2) = 0 _._ 0125, but _p_ (3) = 0 _._ 601 _>_ 0 _._ 05 _/_ (5 + 1 _−_ 3) = 0 _._ 0167, which implies that _L_ = 3. We note that, in this setting, Holm is more powerful than Bonferroni: the former rejects the null hypotheses for the first and third managers, whereas the latter rejects the null hypothesis only for the first manager. 

Figure 13.3 provides an illustration of the Bonferroni and Holm methods on three simulated data sets in a setting involving _m_ = 10 hypothesis tests, of which _m_ 0 = 2 of the null hypotheses are true. Each panel displays the ten corresponding _p_ -values, ordered from smallest to largest, and plotted on a log scale. The eight red points represent the false null hypotheses, and the two black points represent the true null hypotheses. We wish to control the FWER at level 0 _._ 05. The Bonferroni procedure requires us to reject all null hypotheses for which the _p_ -value is below 0 _._ 005; this is represented by the black horizontal line. The Holm procedure requires us to reject all null hypotheses that fall below the blue line. The blue line always lies above the black line, so Holm will always reject more tests than Bonferroni; the region between the two lines corresponds to the hypotheses that are only rejected by Holm. In the left-hand panel, both Bonferroni and Holm successfully reject seven of the eight false null hypotheses. In the center panel, Holm successfully rejects all eight of the false null hypotheses, while Bonferroni fails to reject one. In the right-hand panel, Bonferroni only rejects three of the false null hypotheses, while Holm rejects all eight. Neither Bonferroni nor Holm makes any Type I errors in these examples. 

Two Special Cases: Tukey’s Method and Scheffé’s Method 

Bonferroni’s method and Holm’s method can be used in virtually any setting in which we wish to control the FWER for _m_ null hypotheses: they 

570 13. Multiple Testing 

![Figure 13.3](./img/13_3.png)

**FIGURE 13.3.** _Each panel displays, for a separate simulation, the sorted p-values for tests of m_ = 10 _null hypotheses. The p-values corresponding to the m_ 0 = 2 _true null hypotheses are displayed in black, and the rest are in red. When controlling the FWER at level_ 0 _._ 05 _, the Bonferroni procedure rejects all null hypotheses that fall below the black line, and the Holm procedure rejects all null hypotheses that fall below the blue line. The region between the blue and black lines indicates null hypotheses that are rejected using the Holm procedure but not using the Bonferroni procedure. In the center panel, the Holm procedure rejects one more null hypothesis than the Bonferroni procedure. In the right-hand panel, it rejects five more null hypotheses._ 

make no assumptions about the nature of the null hypotheses, the type of test statistic used, or the (in)dependence of the _p_ -values. However, in certain very specific settings, we can achieve higher power by controlling the FWER using approaches that are more tailored to the task at hand. Tukey’s method and Scheffé’s method provide two such examples. 

Table 13.3 indicates that for the `Fund` dataset, Managers One and Two have the greatest difference in their sample mean returns. This finding might motivate us to test the null hypothesis _H_ 0 : _µ_ 1 = _µ_ 2, where _µj_ is the (population) mean return for the _j_ th fund manager. A two-sample _t_ -test (13.1) for _H_ 0 yields a _p_ -value of 0 _._ 0349, suggesting modest evidence against _H_ 0. However, this _p_ -value is misleading, since we decided to compare the average returns of Managers One and Two only after having examined the returns for all five managers; this essentially amounts to having performed _m_ = 5 _×_ (5 _−_ 1) _/_ 2 = 10 hypothesis tests, and selecting the one with the smallest _p_ -value. This suggests that in order to control the FWER at level 0 _._ 05, we should make a Bonferroni correction for _m_ = 10 hypothesis tests, and therefore should only reject a null hypothesis for which the _p_ -value is below 0 _._ 005. If we do this, then we will be unable to reject the null hypothesis that Managers One and Two have identical performance. 

However, in this setting, a Bonferroni correction is actually a bit too stringent, since it fails to consider the fact that the _m_ = 10 hypothesis tests are all somewhat related: for instance, Managers Two and Five have similar mean returns, as do Managers Two and Four; this guarantees that the mean returns of Managers Four and Five are similar. Stated another way, the _m p_ -values for the _m_ pairwise comparisons are _not_ independent. Therefore, it should be possible to control the FWER in a way that is 

13.3 The Family-Wise Error Rate 571 

![Figure 13.4](./img/13_4.png)

**FIGURE 13.4.** _Each panel displays, for a separate simulation, the sorted p-values for tests of m_ = 15 _hypotheses, corresponding to pairwise tests for the equality of G_ = 6 _means. The m_ 0 = 10 _true null hypotheses are displayed in black, and the rest are in red. When controlling the FWER at level_ 0 _._ 05 _, the Bonferroni procedure rejects all null hypotheses that fall below the black line, whereas Tukey rejects all those that fall below the blue line. Thus, Tukey’s method has slightly higher power than Bonferroni’s method. Controlling the Type I error_ without _adjusting for multiple testing involves rejecting all those that fall below the green line._ 

less conservative. This is exactly the idea behind _Tukey’s method_ : when Tukey’s performing _m_ = _G_ ( _G −_ 1) _/_ 2 pairwise comparisons of _G_ means, it allows method us to control the FWER at level _α_ while rejecting all null hypotheses for which the _p_ -value falls below _αT_ , for some _αT > α/m_ . 

Figure 13.4 illustrates Tukey’s method on three simulated data sets in a setting with _G_ = 6 means, with _µ_ 1 = _µ_ 2 = _µ_ 3 = _µ_ 4 = _µ_ 5 = _µ_ 6. Therefore, of the _m_ = _G_ ( _G −_ 1) _/_ 2 = 15 null hypotheses of the form _H_ 0 : _µj_ = _µk_ , ten are true and five are false. In each panel, the true null hypotheses are displayed in black, and the false ones are in red. The horizontal lines indicate that Tukey’s method always results in at least as many rejections as Bonferroni’s method. In the left-hand panel, Tukey correctly rejects two more null hypotheses than Bonferroni. 

Now, suppose that we once again examine the data in Table 13.3, and notice that Managers One and Three have higher mean returns than Managers Two, Four, and Five. This might motivate us to test the null hypothesis

$$
H_0 : \mu_1 = \mu_2 \quad \text{vs} \quad H_a : \mu_1 \neq \mu_2 \quad (13.8)
$$

(Recall that _µj_ is the population mean return for the _j_ th hedge fund manager.) It turns out that we could test (13.8) using a variant of the twosample _t_ -test presented in (13.1), leading to a _p_ -value of 0 _._ 004. This suggests strong evidence of a difference between Managers One and Three compared to Managers Two, Four, and Five. However, there is a problem: we decided to test the null hypothesis in (13.8) only after peeking at the data in Table 13.3. In a sense, this means that we have conducted multiple testing. In this setting, using Bonferroni to control the FWER at level _α_ 

572 13. Multiple Testing 

would require a _p_ -value threshold of _α/m_ , for an extremely large value of _m_[14] . 

_Scheffé’s method_ is designed for exactly this setting. It allows us to com- Scheffé’s pute a value _αS_ such that rejecting the null hypothesis _H_ 0 in (13.8) if the method _p_ -value is below _αS_ will control the Type I error at level _α_ . It turns out that for the `Fund` example, in order to control the Type I error at level _α_ = 0 _._ 05, we must set _αS_ = 0 _._ 002. Therefore, we are unable to reject _H_ 0 in (13.8), despite the apparently very small _p_ -value of 0 _._ 004. An important advantage of Scheffé’s method is that we can use this same threshold of _αS_ = 0 _._ 002 in order to perform a pairwise comparison of any split of the managers into two groups: for instance, we could also test _H_ 0 : 3[1][(] _[µ]_[1][ +] _[ µ]_[2][ +] _[ µ]_[3][) =][1] 2[(] _[µ]_[4][ +] _[ µ]_[5][)] and _H_ 0 :[1] 4[(] _[µ]_[1][ +] _[ µ]_[2][ +] _[ µ]_[3][ +] _[ µ]_[4][)][=] _[µ]_[5][using][the][same][threshold][of][0] _[.]_[002][,] without needing to further adjust for multiple testing. 

To summarize, Holm’s procedure and Bonferroni’s procedure are very general approaches for multiple testing correction that can be applied under all circumstances. However, in certain special cases, more powerful procedures for multiple testing correction may be available, in order to control the FWER while achieving higher power (i.e. committing fewer Type II errors) than would be possible using Holm or Bonferroni. In this section, we have illustrated two such examples. 

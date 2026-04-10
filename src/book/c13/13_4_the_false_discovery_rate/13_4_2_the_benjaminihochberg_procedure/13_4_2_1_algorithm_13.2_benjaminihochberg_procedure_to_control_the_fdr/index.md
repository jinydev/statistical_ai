---
layout: default
title: "index"
---

# **Algorithm 13.2** _Benjamini–Hochberg Procedure to Control the FDR_ 

1. Specify _q_ , the level at which to control the FDR. 

2. Compute _p_ -values, _p_ 1 _, . . . , pm_ , for the _m_ null hypotheses _H_ 01 _, . . . , H_ 0 _m_ . 

3. Order the _m p_ -values so that _p_ (1) _≤ p_ (2) _≤· · · ≤ p_ ( _m_ ). 

4. Define

$$
L = \max \left\{ j : p_{(j)} < q \frac{j}{m} \right\} \quad (13.9)
$$

5. Reject all null hypotheses _H_ 0 _j_ for which _pj ≤ p_ ( _L_ ). 

Algorithm 13.2 is known as the _Benjamini–Hochberg procedure_ . The crux Benjamini– of this procedure lies in (13.10). For example, consider again the first five Hochberg managers in the `Fund` dataset, presented in Table 13.3. (In this example, procedure _m_ = 5, although typically we control the FDR in settings involving a much greater number of null hypotheses.) We see that _p_ (1) = 0 _._ 006 _<_ 0 _._ 05 _×_ 1 _/_ 5, _p_ (2) = 0 _._ 012 _<_ 0 _._ 05 _×_ 2 _/_ 5, _p_ (3) = 0 _._ 601 _>_ 0 _._ 05 _×_ 3 _/_ 5, _p_ (4) = 0 _._ 756 _>_ 0 _._ 05 _×_ 4 _/_ 5, and _p_ (5) = 0 _._ 918 _>_ 0 _._ 05 _×_ 5 _/_ 5. Therefore, to control the FDR at 5%, we reject the null hypotheses that the first and third fund managers perform no better than chance. 

As long as the _m p_ -values are independent or only mildly dependent, then the Benjamini–Hochberg procedure guarantees[16] that 

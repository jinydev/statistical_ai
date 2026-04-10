---
layout: default
title: "index"
---

# The Bonferroni Method 

As in the previous section, suppose we wish to test _H_ 01 _, . . . , H_ 0 _m_ . Let _Aj_ denote the event that we make a Type I error for the _j_ th null hypothesis, for _j_ = 1 _, . . . , m_ . Then

$$
\text{FWER} = \Pr(A_1 \cup A_2 \cup \dots \cup A_m) \le \sum_{j=1}^m \Pr(A_j) \quad (13.6)
$$

In (13.6), the inequality results from the fact that for any two events _A_ and _B_ , Pr( _A ∪ B_ ) _≤_ Pr( _A_ ) + Pr( _B_ ), regardless of whether _A_ and _B_ are independent. The _Bonferroni method_ , or _Bonferroni correction_ , sets the threshold for rejecting each hypothesis test to _α/m_ , so that Pr( _Aj_ ) _≤ α/m_ . Equation 13.6 implies that

$$
\text{FWER} \le m \times \frac{\alpha}{m} = \alpha
$$

> 13Excess returns correspond to the additional return the fund manager achieves beyond the market’s overall return. So if the market increases by 5% during a given period and the fund manager achieves a 7% return, their _excess return_ would be 7% _−_ 5% = 2%. 

568 13. Multiple Testing 

so this procedure controls the FWER at level _α_ . For instance, in order to control the FWER at level 0 _._ 1 while testing _m_ = 100 null hypotheses, the Bonferroni procedure requires us to control the Type I error for each null hypothesis at level 0 _._ 1 _/_ 100 = 0 _._ 001, i.e. to reject all null hypotheses for which the _p_ -value is below 0 _._ 001. 

We now consider the `Fund` dataset in Table 13.3. If we control the Type I error at level _α_ = 0 _._ 05 for each fund manager separately, then we will conclude that the first and third managers have significantly non-zero excess returns; in other words, we will reject _H_ 01 : _µ_ 1 = 0 and _H_ 03 : _µ_ 3 = 0. However, as discussed in previous sections, this procedure does not account for the fact that we have tested multiple hypotheses, and therefore it will lead to a FWER greater than 0 _._ 05. If we instead wish to control the FWER at level 0 _._ 05, then, using a Bonferroni correction, we must control the Type I error for each individual manager at level _α/m_ = 0 _._ 05 _/_ 5 = 0 _._ 01. Consequently, we will reject the null hypothesis only for the first manager, since the _p_ -values for all other managers exceed 0 _._ 01. The Bonferroni correction gives us peace of mind that we have not falsely rejected too many null hypotheses, but for a price: we reject few null hypotheses, and thus will typically make quite a few Type II errors. 

The Bonferroni correction is by far the best-known and most commonlyused multiplicity correction in all of statistics. Its ubiquity is due in large part to the fact that it is very easy to understand and simple to implement, and also from the fact that it successfully controls Type I error regardless of whether the _m_ hypothesis tests are independent. However, as we will see, it is typically neither the most powerful nor the best approach for multiple testing correction. In particular, the Bonferroni correction can be quite conservative, in the sense that the true FWER is often quite a bit lower than the nominal (or target) FWER; this results from the inequality in (13.6). By contrast, a less conservative procedure might allow us to control the FWER while rejecting more null hypotheses, and therefore making fewer Type II errors. 

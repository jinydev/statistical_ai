---
layout: default
title: "index"
---

# _13.3.3 Between the FWER and Power Trade-Off_ 

In general, there is a trade-off between the FWER threshold that we choose, and our _power_ to reject the null hypotheses. Recall that power is defined as the number of false null hypotheses that we reject divided by the total number of false null hypotheses, i.e. _S/_ ( _m − m_ 0) using the notation of Table 13.2. Figure 13.5 illustrates the results of a simulation setting involving _m_ null hypotheses, of which 90% are true and the remaining 10% are false; power is displayed as a function of the FWER. In this particular simulation setting, when _m_ = 10, a FWER of 0 _._ 05 corresponds to power of approximately 60%. However, as _m_ increases, the power decreases. With _m_ = 500, the power is below 0 _._ 2 at a FWER of 0 _._ 05, so that we successfully reject only 20% of the false null hypotheses. 

Figure 13.5 indicates that it is reasonable to control the FWER when _m_ takes on a small value, like 5 or 10. However, for _m_ = 100 or _m_ = 1 _,_ 000, attempting to control the FWER will make it almost impossible to reject any of the false null hypotheses. In other words, the power will be extremely low. 

Why is this the case? Recall that, using the notation in Table 13.2, the FWER is defined as Pr( _V ≥_ 1) (13.3). In other other words, controlling the FWER at level _α_ guarantees that the data analyst is _very unlikely_ (with probability no more than _α_ ) to reject _any_ true null hypotheses, i.e. to have any false positives. In order to make good on this guarantee when _m_ is large, the data analyst may be forced to reject very few null hypotheses, or perhaps even none at all (since if _R_ = 0 then also _V_ = 0; see Table 13.2). 

> 14In fact, calculating the “correct” value of _m_ is quite technical, and outside the scope of this book. 

13.4 The False Discovery Rate 573 

![Figure 13.5](./img/13_5.png)

**FIGURE 13.5.** _In a simulation setting in which 90% of the m null hypotheses are true, we display the power (the fraction of false null hypotheses that we successfully reject) as a function of the family-wise error rate. The curves correspond to m_ = 10 (orange) _, m_ = 100 (blue) _, and m_ = 500 (purple) _. As the value of m increases, the power decreases. The vertical dashed line indicates a FWER of_ 0 _._ 05 _._ 

This is scientifically uninteresting, and typically results in very low power, as in Figure 13.5. 

In practice, when _m_ is large, we may be willing to tolerate a few false positives, in the interest of making more discoveries, i.e. more rejections of the null hypothesis. This is the motivation behind the false discovery rate, which we present next. 

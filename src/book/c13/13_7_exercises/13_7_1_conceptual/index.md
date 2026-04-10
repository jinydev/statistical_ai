---
layout: default
title: "index"
---

# _Conceptual_ 

1. Suppose we test _m_ null hypotheses, all of which are true. We control the Type I error for each null hypothesis at level _α_ . For each subproblem, justify your answer. 

   - (a) In total, how many Type I errors do we expect to make? 

   - (b) Suppose that the _m_ tests that we perform are independent. What is the family-wise error rate associated with these _m_ tests? _Hint: If two events A and B are independent, then_ Pr( _A ∩ B_ ) = Pr( _A_ ) Pr( _B_ ) _._ 

   - (c) Suppose that _m_ = 2, and that the _p_ -values for the two tests are positively correlated, so that if one is small then the other will tend to be small as well, and if one is large then the other will tend to be large. How does the family-wise error rate associated with these _m_ = 2 tests qualitatively compare to the answer in (b) with _m_ = 2? 

_Hint: First, suppose that the two p-values are perfectly correlated._ 

- (d) Suppose again that _m_ = 2, but that now the _p_ -values for the two tests are negatively correlated, so that if one is large then the other will tend to be small. How does the family-wise error rate associated with these _m_ = 2 tests qualitatively compare to the answer in (b) with _m_ = 2? 

_Hint: First, suppose that whenever one p-value is less than α, then the other will be greater than α. In other words, we can never reject both null hypotheses._ 

594 13. Multiple Testing 

2. Suppose that we test _m_ hypotheses, and control the Type I error for each hypothesis at level _α_ . Assume that all _m p_ -values are independent, and that all null hypotheses are true. 

   - (a) Let the random variable _Aj_ equal 1 if the _j_ th null hypothesis is rejected, and 0 otherwise. What is the distribution of _Aj_ ? 

   - (b) What is the distribution of[�] _[m] j_ =1 _[A][j]_[?] 

   - (c) What is the standard deviation of the number of Type I errors that we will make? 

3. Suppose we test _m_ null hypotheses, and control the Type I error for the _j_ th null hypothesis at level _αj_ , for _j_ = 1 _, . . . , m_ . Argue that the family-wise error rate is no greater than[�] _[m] j_ =1 _[α][j]_[.] 

|Null Hypothesis|_p_-value|
|---|---|
|_H_01<br>_H_02<br>_H_03<br>_H_04<br>_H_05<br>_H_06<br>_H_07<br>_H_08<br>_H_09<br>_H_10|0_._0011<br>0_._031<br>0_._017<br>0_._32<br>0_._11<br>0_._90<br>0_._07<br>0_._006<br>0_._004<br>0_._0009|



**TABLE 13.4.** _p-values for Exercise 4._ 

4. Suppose we test _m_ = 10 hypotheses, and obtain the _p_ -values shown in Table 13.4. 

   - (a) Suppose that we wish to control the Type I error for each null hypothesis at level _α_ = 0 _._ 05. Which null hypotheses will we reject? 

   - (b) Now suppose that we wish to control the FWER at level _α_ = 0 _._ 05. Which null hypotheses will we reject? Justify your answer. 

   - (c) Now suppose that we wish to control the FDR at level _q_ = 0 _._ 05. Which null hypotheses will we reject? Justify your answer. 

   - (d) Now suppose that we wish to control the FDR at level _q_ = 0 _._ 2. Which null hypotheses will we reject? Justify your answer. 

   - (e) Of the null hypotheses rejected at FDR level _q_ = 0 _._ 2, approximately how many are false positives? Justify your answer. 

5. For this problem, you will make up _p_ -values that lead to a certain number of rejections using the Bonferroni and Holm procedures. 

   - (a) Give an example of five _p_ -values (i.e. five numbers between 0 and 1 which, for the purpose of this problem, we will interpret as _p_ - values) for which both Bonferroni’s method and Holm’s method 

13.7 Exercises 595 

reject exactly one null hypothesis when controlling the FWER at level 0 _._ 1. 

   - (b) Now give an example of five _p_ -values for which Bonferroni rejects one null hypothesis and Holm rejects more than one null hypothesis at level 0 _._ 1. 

6. For each of the three panels in Figure 13.3, answer the following questions: 

   - (a) How many false positives, false negatives, true positives, true negatives, Type I errors, and Type II errors result from applying the Bonferroni procedure to control the FWER at level _α_ = 0 _._ 05? 

   - (b) How many false positives, false negatives, true positives, true negatives, Type I errors, and Type II errors result from applying the Holm procedure to control the FWER at level _α_ = 0 _._ 05? 

   - (c) What is the false discovery proportion associated with using the Bonferroni procedure to control the FWER at level _α_ = 0 _._ 05? 

   - (d) What is the false discovery proportion associated with using the Holm procedure to control the FWER at level _α_ = 0 _._ 05? 

   - (e) How would the answers to (a) and (c) change if we instead used the Bonferroni procedure to control the FWER at level _α_ = 0 _._ 001? 

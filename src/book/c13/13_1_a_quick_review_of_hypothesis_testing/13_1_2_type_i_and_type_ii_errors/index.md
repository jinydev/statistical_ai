---
layout: default
title: "index"
---

# _13.1.2 Type I and Type II Errors_ 

If the null hypothesis holds, then we say that it is a _true null hypothesis_ ; true null otherwise, it is a _false null hypothesis_ . For instance, if we test _H_ 0 : _µt_ = _µc_ hypothesis as in Section 13.1.1, and there is indeed no difference in the _population_ false null mean blood pressure for mice in the treatment group and mice in the hypothesis control group, then _H_ 0 is true; otherwise, it is false. Of course, we do not know _a priori_ whether _H_ 0 is true or whether it is false: this is why we need to conduct a hypothesis test! 

hypothesis false null hypothesis 

> 9Though a threshold of 0 _._ 05 to reject _H_ 0 is ubiquitous in some areas of science, we advise against blind adherence to this arbitrary choice. Furthermore, a data analyst should typically report the _p_ -value itself, rather than just whether or not it exceeds a specified threshold value. 

13.2 The Challenge of Multiple Testing 563 

Table 13.1 summarizes the possible scenarios associated with testing the null hypothesis _H_ 0.[10] Once the hypothesis test is performed, the _row_ of the table is known (based on whether or not we have rejected _H_ 0); however, it is impossible for us to know which _column_ we are in. If we reject _H_ 0 when _H_ 0 is false (i.e., when _Ha_ is true), or if we do not reject _H_ 0 when it is true, then we arrived at the correct result. However, if we erroneously reject _H_ 0 when _H_ 0 is in fact true, then we have committed a _Type I error_ . The _Type I_ Type I error _error rate_ is defined as the probability of making a Type I error given that Type I error _H_ 0 holds, i.e., the probability of incorrectly rejecting _H_ 0. Alternatively, if rate we do not reject _H_ 0 when _H_ 0 is in fact false, then we have committed a _Type II error_ . The _power_ of the hypothesis test is defined as the probability Type II of not making a Type II error given that _Ha_ holds, i.e., the probability of error correctly rejecting _H_ 0. power 

Ideally we would like both the Type I and Type II error rates to be small. But in practice, this is hard to achieve! There typically is a trade-off: we can make the Type I error small by only rejecting _H_ 0 if we are quite sure that it doesn’t hold; however, this will result in an increase in the Type II error. Alternatively, we can make the Type II error small by rejecting _H_ 0 in the presence of even modest evidence that it does not hold, but this will cause the Type I error to be large. In practice, we typically view Type I errors as more “serious” than Type II errors, because the former involves declaring a scientific finding that is not correct. Hence, when we perform hypothesis testing, we typically require a low Type I error rate — e.g., at most _α_ = 0 _._ 05 — while trying to make the Type II error small (or, equivalently, the power large). 

It turns out that there is a direct correspondence between the _p_ -value threshold that causes us to reject _H_ 0, and the Type I error rate. By only rejecting _H_ 0 when the _p_ -value is below _α_ , we ensure that the Type I error rate will be less than or equal to _α_ . 

---
layout: default
title: "index"
---

# _Applied_ 

7. This problem makes use of the `Carseats` dataset in the `ISLP` package. 

   - (a) For each quantitative variable in the dataset besides `Sales` , fit a linear model to predict `Sales` using that quantitative variable. Report the _p_ -values associated with the coefficients for the variables. That is, for each model of the form _Y_ = _β_ 0 + _β_ 1 _X_ + _ϵ_ , report the _p_ -value associated with the coefficient _β_ 1. Here, _Y_ represents `Sales` and _X_ represents one of the other quantitative variables. 

   - (b) Suppose we control the Type I error at level _α_ = 0 _._ 05 for the _p_ -values obtained in (a). Which null hypotheses do we reject? 

   - (c) Now suppose we control the FWER at level 0 _._ 05 for the _p_ -values. Which null hypotheses do we reject? 

   - (d) Finally, suppose we control the FDR at level 0 _._ 2 for the _p_ -values. Which null hypotheses do we reject? 

8. In this problem, we will simulate data from _m_ = 100 fund managers. 

```
rng=np.random.default_rng(1)
n,m=20,100
X=rng.normal(size=(n,m))
```

596 13. Multiple Testing 

These data represent each fund manager’s percentage returns for each of _n_ = 20 months. We wish to test the null hypothesis that each fund manager’s percentage returns have population mean equal to zero. Notice that we simulated the data in such a way that each fund manager’s percentage returns do have population mean zero; in other words, all _m_ null hypotheses are true. 

- (a) Conduct a one-sample _t_ -test for each fund manager, and plot a histogram of the _p_ -values obtained. 

- (b) If we control Type I error for each null hypothesis at level _α_ = 0 _._ 05, then how many null hypotheses do we reject? 

- (c) If we control the FWER at level 0 _._ 05, then how many null hypotheses do we reject? 

- (d) If we control the FDR at level 0 _._ 05, then how many null hypotheses do we reject? 

- (e) Now suppose we “cherry-pick” the 10 fund managers who perform the best in our data. If we control the FWER for just these 10 fund managers at level 0 _._ 05, then how many null hypotheses do we reject? If we control the FDR for just these 10 fund managers at level 0 _._ 05, then how many null hypotheses do we reject? 

- (f) Explain why the analysis in (e) is misleading. _Hint: The standard approaches for controlling the FWER and FDR assume that_ all _tested null hypotheses are adjusted for multiplicity, and that no “cherry-picking” of the smallest p-values has occurred. What goes wrong if we cherry-pick?_ 

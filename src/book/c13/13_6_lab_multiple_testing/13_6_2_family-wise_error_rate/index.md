---
layout: default
title: "index"
---

# _13.6.2 Family-Wise Error Rate_ 

Recall from (13.5) that if the null hypothesis is true for each of _m_ independent hypothesis tests, then the FWER is equal to 1 _−_ (1 _− α_ ) _[m]_ . We can use this expression to compute the FWER for _m_ = 1 _, . . . ,_ 500 and _α_ = 0 _._ 05, 0 _._ 01, and 0 _._ 001. We plot the FWER for these values of _α_ in order to reproduce Figure 13.2. 

```
In [8]:m=np.linspace(1,501)
fig,ax=plt.subplots()
[ax.plot(m,
1-(1-alpha)**m,
label=r'$\alpha=%s$'%str(alpha))
foralphain[0.05,0.01,0.001]]
ax.set_xscale('log')
ax.set_xlabel('NumberofHypotheses')
ax.set_ylabel('Family-WiseErrorRate')
ax.legend()
ax.axhline(0.05,c='k',ls='--');
```

As discussed previously, even for moderate values of _m_ such as 50, the FWER exceeds 0 _._ 05 unless _α_ is set to a very low value, such as 0 _._ 001. Of course, the problem with setting _α_ to such a low value is that we are likely to make a number of Type II errors: in other words, our power is very low. We now conduct a one-sample _t_ -test for each of the first five managers in the `Fund` dataset, in order to test the null hypothesis that the _j_ th fund manager’s mean return equals zero, _H_ 0 _,j_ : _µj_ = 0. 

```
In [9]:Fund=load_data('Fund')
fund_mini=Fund.iloc[:,:5]
fund_mini_pvals=np.empty(5)
foriinrange(5):
```

586 13. Multiple Testing 

```
fund_mini_pvals[i]=ttest_1samp(fund_mini.iloc[:,i],0).pvalue
fund_mini_pvals
```

```
Out[9]:array([0.006,0.918,0.012,0.601,0.756])
```

The _p_ -values are low for Managers One and Three, and high for the other three managers. However, we cannot simply reject _H_ 0 _,_ 1 and _H_ 0 _,_ 3, since this would fail to account for the multiple testing that we have performed. Instead, we will conduct Bonferroni’s method and Holm’s method to control the FWER. 

To do this, we use the `multipletests()` function from the `statsmodels multiple-` module (abbreviated to `mult_test()` ). Given the _p_ -values, for methods like `tests()` Holm and Bonferroni the function outputs _adjusted p-values_ , which can be adjusted thought of as a new set of _p_ -values that have been corrected for multiple _p_ -values testing. If the adjusted _p_ -value for a given hypothesis is less than or equal to _α_ , then that hypothesis can be rejected while maintaining a FWER of no more than _α_ . In other words, for such methods, the adjusted _p_ -values resulting from the `multipletests()` function can simply be compared to the desired FWER in order to determine whether or not to reject each hypothesis. We will later see that we can use the same function to control FDR as well. 

The `mult_test()` function takes _p_ -values and a `method` argument, as well as an optional `alpha` argument. It returns the decisions ( `reject` below) as well as the adjusted _p_ -values ( `bonf` ). 

```
In [10]:reject,bonf=mult_test(fund_mini_pvals ,method="bonferroni")[:2]
reject
```

```
Out[10]:array([True,False,False,False,False])
```

The _p_ -values `bonf` are simply the `fund_mini_pvalues` multiplied by 5 and truncated to be less than or equal to 1. 

```
In [11]:bonf,np.minimum(fund_mini_pvals*5,1)
```

```
Out[11]:(array([0.03,1.,0.06,1.,1.]),
array([0.03,1.,0.06,1.,1.]))
```

Therefore, using Bonferroni’s method, we are able to reject the null hypothesis only for Manager One while controlling FWER at 0 _._ 05. 

By contrast, using Holm’s method, the adjusted _p_ -values indicate that we can reject the null hypotheses for Managers One and Three at a FWER of 0 _._ 05. 

```
In [12]:mult_test(fund_mini_pvals ,method="holm",alpha=0.05)[:2]
```

```
Out[12]:(array([True,False,True,False,False]),
array([0.03,1.,0.05,1.,1.]))
```

As discussed previously, Manager One seems to perform particularly well, whereas Manager Two has poor performance. 

13.6 Lab: Multiple Testing 587 

```
In [13]:fund_mini.mean()
```

```
Out[13]:Manager13.0
Manager2-0.1
Manager32.8
Manager40.5
Manager50.3
dtype:float64
```

Is there evidence of a meaningful difference in performance between these two managers? We can check this by performing a _paired t-test_ using the paired _t_ -test `ttest_rel()` function from `scipy.stats` : 

```
ttest_rel()
```

```
In [14]:ttest_rel(fund_mini['Manager1'],
fund_mini['Manager2']).pvalue
```

```
Out[14]:0.038
```

The test results in a _p_ -value of 0.038, suggesting a statistically significant difference. 

However, we decided to perform this test only after examining the data and noting that Managers One and Two had the highest and lowest mean performances. In a sense, this means that we have implicitly performed �52� = 5(5 _−_ 1) _/_ 2 = 10 hypothesis tests, rather than just one, as discussed in Section 13.3.2. Hence, we use the `pairwise_tukeyhsd()` function from `pairwise_ statsmodels.stats.multicomp` to apply Tukey’s method in order to adjust `tukeyhsd()` for multiple testing. This function takes as input a fitted _ANOVA_ regres- ANOVA sion model, which is essentially just a linear regression in which all of the predictors are qualitative. In this case, the response consists of the monthly excess returns achieved by each manager, and the predictor indicates the manager to which each return corresponds. 

```
tukeyhsd()
```

```
In [15]:returns=np.hstack([fund_mini.iloc[:,i]foriinrange(5)])
managers=np.hstack([[i+1]*50foriinrange(5)])
tukey=pairwise_tukeyhsd(returns,managers)
print(tukey.summary())
```

|`Multiple Comparison of `|`Multiple Comparison of `|`Multiple Comparison of `|`Means - Tukey `|`Means - Tukey `|`HSD, FWER=0.05`|`HSD, FWER=0.05`|
|---|---|---|---|---|---|---|
|`===================================================`|||||||
|`group1 group2 `||`meandiff `|`p-adj`|`lower`|`upper`|`reject`|
|`---------------------------------------------------`|||||||
|`1`|`2`|`-3.1 `|`0.1862 `|`-6.9865 `|`0.7865`|`False`|
|`1`|`3`|`-0.2 `|`0.9999 `|`-4.0865 `|`3.6865`|`False`|
|`1`|`4`|`-2.5 `|`0.3948 `|`-6.3865 `|`1.3865`|`False`|
|`1`|`5`|`-2.7 `|`0.3152 `|`-6.5865 `|`1.1865`|`False`|
|`2`|`3`|`2.9 `|`0.2453 `|`-0.9865 `|`6.7865`|`False`|
|`2`|`4`|`0.6 `|`0.9932 `|`-3.2865 `|`4.4865`|`False`|
|`2`|`5`|`0.4 `|`0.9986 `|`-3.4865 `|`4.2865`|`False`|
|`3`|`4`|`-2.3`|`0.482 `|`-6.1865 `|`1.5865`|`False`|
|`3`|`5`|`-2.5 `|`0.3948 `|`-6.3865 `|`1.3865`|`False`|
|`4`|`5`|`-0.2 `|`0.9999 `|`-4.0865 `|`3.6865`|`False`|
|`---------------------------------------------------`|||||||



The `pairwise_tukeyhsd()` function provides confidence intervals for the difference between each pair of managers ( `lower` and `upper` ), as well as a 

588 13. Multiple Testing 

![Figure 13.10](./img/13_10.png)

**FIGURE 13.10.** _95% confidence intervals for each manager on the_ `Fund` _data, using Tukey’s method to adjust for multiple testing. All of the confidence intervals overlap, so none of the differences among managers are statistically significant when controlling FWER at level_ 0 _._ 05 _._ 

_p_ -value. All of these quantities have been adjusted for multiple testing. Notice that the _p_ -value for the difference between Managers One and Two has increased from 0 _._ 038 to 0 _._ 186, so there is no longer clear evidence of a difference between the managers’ performances. We can plot the confidence intervals for the pairwise comparisons using the `plot_simultaneous()` method of `tukey` . Any pair of intervals that don’t overlap indicates a significant difference at the nominal level of 0.05. In this case, no differences are considered significant as reported in the table above. 

```
In [16]:fig,ax=plt.subplots(figsize=(8,8))
tukey.plot_simultaneous(ax=ax);
```

The result can be seen[19] in Figure 13.10. 

---
layout: default
title: "index"
---

# _13.6.3 False Discovery Rate_ 

Now we perform hypothesis tests for all 2,000 fund managers in the `Fund` dataset. We perform a one-sample _t_ -test of _H_ 0 _,j_ : _µj_ = 0, which states that the _j_ th fund manager’s mean return is zero. 

```
In [17]:fund_pvalues=np.empty(2000)
fori,managerinenumerate(Fund.columns):
fund_pvalues[i]=ttest_1samp(Fund[manager],0).pvalue
```

There are far too many managers to consider trying to control the FWER. Instead, we focus on controlling the FDR: that is, the expected fraction of rejected null hypotheses that are actually false positives. The 

> 19Traditionally this plot shows intervals for each paired difference. With many groups it is more convenient and equivalent to display one interval per group, as is done here. By “differencing” all pairs of intervals displayed here you recover the traditional plot. 

13.6 Lab: Multiple Testing 589 

`multipletests()` function (abbreviated `mult_test()` ) can be used to carry out the Benjamini–Hochberg procedure. 

```
In [18]:fund_qvalues=mult_test(fund_pvalues ,method="fdr_bh")[1]
fund_qvalues[:10]
```

```
Out[18]:array([0.09,0.99,0.12,0.92,0.96,0.08,0.08,0.08,0.08,
0.08])
```

The _q-values_ output by the Benjamini–Hochberg procedure can be inter- q-values preted as the smallest FDR threshold at which we would reject a particular null hypothesis. For instance, a _q_ -value of 0 _._ 1 indicates that we can reject the corresponding null hypothesis at an FDR of 10% or greater, but that we cannot reject the null hypothesis at an FDR below 10%. 

If we control the FDR at 10%, then for how many of the fund managers can we reject _H_ 0 _,j_ : _µj_ = 0? 

```
In [19]:(fund_qvalues<=0.1).sum()
```

```
Out[19]:146
```

We find that 146 of the 2,000 fund managers have a _q_ -value below 0.1; therefore, we are able to conclude that 146 of the fund managers beat the market at an FDR of 10%. Only about 15 (10% of 146) of these fund managers are likely to be false discoveries. 

By contrast, if we had instead used Bonferroni’s method to control the FWER at level _α_ = 0 _._ 1, then we would have failed to reject any null hypotheses! 

```
In [20]:(fund_pvalues<=0.1/2000).sum()
```

```
Out[20]:0
```

Figure 13.6 displays the ordered _p_ -values, _p_ (1) _≤ p_ (2) _≤· · · ≤ p_ (2000), for the `Fund` dataset, as well as the threshold for rejection by the Benjamini– Hochberg procedure. Recall that the Benjamini–Hochberg procedure identifies the largest _p_ -value such that _p_ ( _j_ ) _< qj/m_ , and rejects all hypotheses for which the _p_ -value is less than or equal to _p_ ( _j_ ). In the code below, we implement the Benjamini–Hochberg procedure ourselves, in order to illustrate how it works. We first order the _p_ -values. We then identify all _p_ -values that satisfy _p_ ( _j_ ) _< qj/m_ ( `sorted_set_` ). Finally, `selected_` is a boolean array indicating which _p_ -values are less than or equal to the largest _p_ -value in `sorted_[sorted_set_]` . Therefore, `selected_` indexes the _p_ -values rejected by the Benjamini–Hochberg procedure. 

```
In [21]:sorted_=np.sort(fund_pvalues)
m=fund_pvalues.shape[0]
q=0.1
sorted_set_=np.where(sorted_<q*np.linspace(1,m,m)/m)[0]
ifsorted_set_.shape[0]>0:
selected_=fund_pvalues<sorted_[sorted_set_].max()
sorted_set_=np.arange(sorted_set_.max())
else:
selected_=[]
sorted_set_=[]
```

590 13. Multiple Testing 

We now reproduce the middle panel of Figure 13.6. 

```
In [22]:fig,ax=plt.subplots()
ax.scatter(np.arange(0,sorted_.shape[0])+1,
sorted_,s=10)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylabel('P-Value')
ax.set_xlabel('Index')
ax.scatter(sorted_set_+1,sorted_[sorted_set_],c='r',s=20)
ax.axline((0,0),(1,q/m),c='k',ls='--',linewidth=3);
```

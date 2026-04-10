---
layout: default
title: "index"
---

# _13.6.1 Review of Hypothesis Tests_ 

We begin by performing some one-sample _t_ -tests. First we create 100 variables, each consisting of 10 observations. The first 50 variables have mean 0 _._ 5 and variance 1, while the others have mean 0 and variance 1. 

```
In [3]:rng=np.random.default_rng(12)
X=rng.standard_normal((10,100))
true_mean=np.array([0.5]*50+[0]*50)
X+=true_mean[None,:]
```

584 13. Multiple Testing 

To begin, we use `ttest_1samp()` from the `scipy.stats` module to test _H_ 0 : `ttest_1samp()` _µ_ 1 = 0, the null hypothesis that the first variable has mean zero. 

```
In [4]:result=ttest_1samp(X[:,0],0)
result.pvalue
```

```
Out[4]:0.931
```

The _p_ -value comes out to 0.931, which is not low enough to reject the null hypothesis at level _α_ = 0 _._ 05. In this case, _µ_ 1 = 0 _._ 5, so the null hypothesis is false. Therefore, we have made a Type II error by failing to reject the null hypothesis when the null hypothesis is false. 

We now test _H_ 0 _,j_ : _µj_ = 0 for _j_ = 1 _, . . . ,_ 100. We compute the 100 _p_ - values, and then construct a vector recording whether the _j_ th _p_ -value is less than or equal to 0.05, in which case we reject _H_ 0 _j_ , or greater than 0.05, in which case we do not reject _H_ 0 _j_ , for _j_ = 1 _, . . . ,_ 100. 

```
In [5]:p_values=np.empty(100)
foriinrange(100):
p_values[i]=ttest_1samp(X[:,i],0).pvalue
decision=pd.cut(p_values,
[0,0.05,1],
labels=['RejectH0',
'DonotrejectH0'])
truth=pd.Categorical(true_mean==0,
categories=[True,False],
ordered=True)
```

Since this is a simulated data set, we can create a 2 _×_ 2 table similar to Table 13.2. 

```
In [6]:pd.crosstab(decision,
truth,
rownames=['Decision'],
colnames=['H0'])
```

```
Out[6]:H0TrueFalse
Decision
RejectH0515
DonotrejectH04535
```

Therefore, at level _α_ = 0 _._ 05, we reject 15 of the 50 false null hypotheses, and we incorrectly reject 5 of the true null hypotheses. Using the notation from Section 13.3, we have _V_ = 5, _S_ = 15, _U_ = 45 and _W_ = 35. We have set _α_ = 0 _._ 05, which means that we expect to reject around 5% of the true null hypotheses. This is in line with the 2 _×_ 2 table above, which indicates that we rejected _V_ = 5 of the 50 true null hypotheses. 

In the simulation above, for the false null hypotheses, the ratio of the mean to the standard deviation was only 0 _._ 5 _/_ 1 = 0 _._ 5. This amounts to quite a weak signal, and it resulted in a high number of Type II errors. Let’s instead simulate data with a stronger signal, so that the ratio of the mean to the standard deviation for the false null hypotheses equals 1. We make only 10 Type II errors. 

13.6 Lab: Multiple Testing 585 

```
In [7]:true_mean=np.array([1]*50+[0]*50)
X=rng.standard_normal((10,100))
X+=true_mean[None,:]
foriinrange(100):
p_values[i]=ttest_1samp(X[:,i],0).pvalue
decision=pd.cut(p_values,
[0,0.05,1],
labels=['RejectH0',
'DonotrejectH0'])
truth=pd.Categorical(true_mean==0,
categories=[True,False],
ordered=True)
pd.crosstab(decision,
truth,
rownames=['Decision'],
colnames=['H0'])
```

```
Out[7]:
```

```
H0TrueFalse
Decision
RejectH0240
DonotrejectH04810
```

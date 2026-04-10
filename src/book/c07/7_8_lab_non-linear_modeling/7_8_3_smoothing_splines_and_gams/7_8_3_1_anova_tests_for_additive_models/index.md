---
layout: default
title: "index"
---

# ANOVA Tests for Additive Models 

In all of our models, the function of `year` looks rather linear. We can perform a series of ANOVA tests in order to determine which of these three models is best: a GAM that excludes `year` ( _M_ 1), a GAM that uses a linear function of `year` ( _M_ 2), or a GAM that uses a spline function of `year` ( _M_ 3). 

```
In [36]:gam_0=LinearGAM(age_term+f_gam(2,lam=0))
gam_0.fit(Xgam,y)
gam_linear=LinearGAM(age_term+
l_gam(1,lam=0)+
f_gam(2,lam=0))
gam_linear.fit(Xgam,y)
```

```
Out[36]:LinearGAM(callbacks=[Deviance(),Diffs()],fit_intercept=True,
max_iter=100,scale=None,terms=s(0)+l(1)+f(2)+intercept,
tol=0.0001,verbose=False)
```

Notice our use of `age_term` in the expressions above. We do this because earlier we set the value for `lam` in this term to achieve four degrees of freedom. 

To directly assess the effect of `year` we run an ANOVA on the three models fit above. 

```
In [37]:anova_gam(gam_0,gam_linear,gam_full)
```

```
Out[37]:
```

```
deviancedfdeviance_diffdf_diffFpvalue
03714362.3662991.004NaNNaNNaNNaN
13696745.8232990.00517616.5430.99914.2650.002
23693142.9302987.0073602.8942.9980.9720.436
```

We find that there is compelling evidence that a GAM with a linear function in `year` is better than a GAM that does not include `year` at all ( _p_ -value= 0.002). However, there is no evidence that a non-linear function of `year` is needed ( _p_ -value=0.435). In other words, based on the results of this ANOVA, _M_ 2 is preferred. 

We can repeat the same process for `age` as well. We see there is very clear evidence that a non-linear term is required for `age` . 

```
In [38]:gam_0=LinearGAM(year_term+
f_gam(2,lam=0))
gam_linear=LinearGAM(l_gam(0,lam=0)+
year_term+
f_gam(2,lam=0))
gam_0.fit(Xgam,y)
gam_linear.fit(Xgam,y)
anova_gam(gam_0,gam_linear,gam_full)
```

7.8 Lab: Non-Linear Modeling 323 

**`Out[38]:`** `deviance df deviance_diff df_diff F pvalue 0 3975443.045 2991.001 NaN NaN NaN NaN 1 3850246.908 2990.001 125196.137 1.000 101.270 0.000 2 3693142.930 2987.007 157103.978 2.993 42.448 0.000` There is a (verbose) `summary()` method for the GAM fit. (We do not reproduce it here.) 

```
In [39]:gam_full.summary()
```

We can make predictions from `gam` objects, just like from `lm` objects, using the `predict()` method for the class `gam` . Here we make predictions on the training set. 

```
In [40]:Yhat=gam_full.predict(Xgam)
```

In order to fit a logistic regression GAM, we use `LogisticGAM()` from `LogisticGAM() pygam` . **`In [41]:`** `gam_logit = LogisticGAM(age_term + l_gam(1, lam=0) + f_gam(2, lam=0)) gam_logit.fit(Xgam, high_earn)` 

```
Out[41]:LogisticGAM(callbacks=[Deviance(),Diffs(),Accuracy()],
fit_intercept=True,max_iter=100,
terms=s(0)+l(1)+f(2)+intercept,tol=0.0001,verbose=False)
```

```
In [42]:fig,ax=subplots(figsize=(8,8))
ax=plot_gam(gam_logit,2)
ax.set_xlabel('Education')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofwageoneducation',
fontsize=20);
ax.set_xticklabels(Wage['education'].cat.categories,fontsize=8);
```

The model seems to be very flat, with especially high error bars for the first category. Let’s look at the data a bit more closely. 

```
In [43]:pd.crosstab(Wage['high_earn'],Wage['education'])
```

We see that there are no high earners in the first category of education, meaning that the model will have a hard time fitting. We will fit a logistic regression GAM excluding all observations falling into this category. This provides more sensible results. 

To do so, we could subset the model matrix, though this will not remove the column from `Xgam` . While we can deduce which column corresponds to this feature, for reproducibility’s sake we reform the model matrix on this smaller subset. 

**`In [44]:`** `only_hs = Wage['education'] == '1. < HS Grad' Wage_ = Wage.loc[` _∼_ `only_hs] Xgam_ = np.column_stack([Wage_['age'], Wage_['year'], Wage_['education'].cat.codes -1]) high_earn_ = Wage_['high_earn']` 

324 7. Moving Beyond Linearity 

In the second-to-last line above, we subtract one from the codes of the category, due to a bug in `pygam` . It just relabels the education values and hence has no effect on the fit. We now fit the model. 

```
In [45]:gam_logit_=LogisticGAM(age_term+
year_term+
f_gam(2,lam=0))
gam_logit_.fit(Xgam_,high_earn_)
```

```
Out[45]:LogisticGAM(callbacks=[Deviance(),Diffs(),Accuracy()],
fit_intercept=True,max_iter=100,
terms=s(0)+s(1)+f(2)+intercept,tol=0.0001,verbose=False)
```

Let’s look at the effect of `education` , `year` and `age` on high earner status now that we’ve removed those observations. 

```
In [46]:fig,ax=subplots(figsize=(8,8))
ax=plot_gam(gam_logit_,2)
ax.set_xlabel('Education')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofhighearnerstatusoneducation
'
,fontsize=20);
ax.set_xticklabels(Wage['education'].cat.categories[1:],
fontsize=8);
```

```
In [47]:fig,ax=subplots(figsize=(8,8))
ax=plot_gam(gam_logit_,1)
ax.set_xlabel('Year')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofhighearnerstatusonyear',
fontsize=20);
```

```
In [48]:fig,ax=subplots(figsize=(8,8))
ax=plot_gam(gam_logit_,0)
ax.set_xlabel('Age')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofhighearnerstatusonage',
fontsize=20);
```

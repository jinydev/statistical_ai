---
layout: default
title: "index"
---

# _7.8.3 Smoothing Splines and GAMs_ 

A smoothing spline is a special case of a GAM with squared-error loss and a single feature. To fit GAMs in `Python` we will use the `pygam` package `pygam` which can be installed via `pip install pygam` . The estimator `LinearGAM() LinearGAM()` uses squared-error loss. The GAM is specified by associating each column of a model matrix with a particular smoothing operation: `s` for smoothing spline; `l` for linear, and `f` for factor or categorical variables. The argument `0` passed to `s` below indicates that this smoother will apply to the first column of a feature matrix. Below, we pass it a matrix with a single column: `X_age` . The argument `lam` is the penalty parameter _λ_ as discussed in Section 7.5.2. 

```
In [23]:X_age=np.asarray(age).reshape((-1,1))
gam=LinearGAM(s_gam(0,lam=0.6))
gam.fit(X_age,y)
```

318 7. Moving Beyond Linearity 

```
Out[23]:LinearGAM(callbacks=[Deviance(),Diffs()],fit_intercept=True,
max_iter=100,scale=None,terms=s(0)+intercept,tol=0.0001,
verbose=False)
```

The `pygam` library generally expects a matrix of features so we reshape `age` to be a matrix (a two-dimensional array) instead of a vector (i.e. a onedimensional array). The `-1` in the call to the `reshape()` method tells `numpy` to impute the size of that dimension based on the remaining entries of the shape tuple. 

Let’s investigate how the fit changes with the smoothing parameter `lam` . The function `np.logspace()` is similar to `np.linspace()` but spaces points `np.logspace()` evenly on the log-scale. Below we vary `lam` from 10 _[−]_[2] to 10[6] . 

```
In [24]:fig,ax=subplots(figsize=(8,8))
ax.scatter(age,y,facecolor='gray',alpha=0.5)
forlaminnp.logspace(-2,6,5):
gam=LinearGAM(s_gam(0,lam=lam)).fit(X_age,y)
ax.plot(age_grid,
gam.predict(age_grid),
label='{:.1e}'.format(lam),
linewidth=3)
ax.set_xlabel('Age',fontsize=20)
ax.set_ylabel('Wage',fontsize=20);
ax.legend(title='$\lambda$');
```

The `pygam` package can perform a search for an optimal smoothing parameter. 

```
In [25]:gam_opt=gam.gridsearch(X_age,y)
ax.plot(age_grid,
gam_opt.predict(age_grid),
label='Gridsearch',
linewidth=4)
ax.legend()
fig
```

Alternatively, we can fix the degrees of freedom of the smoothing spline using a function included in the `ISLP.pygam` package. Below we find a value of _λ_ that gives us roughly four degrees of freedom. We note here that these degrees of freedom include the unpenalized intercept and linear term of the smoothing spline, hence there are at least two degrees of freedom. 

```
In [26]:age_term=gam.terms[0]
lam_4=approx_lam(X_age,age_term,4)
age_term.lam=lam_4
degrees_of_freedom(X_age,age_term)
```

```
Out[26]:4.000000100004728
```

Let’s vary the degrees of freedom in a similar plot to above. We choose the degrees of freedom as the desired degrees of freedom plus one to account for the fact that these smoothing splines always have an intercept term. Hence, a value of one for `df` is just a linear fit. 

```
In [27]:fig,ax=subplots(figsize=(8,8))
ax.scatter(X_age,
y,
```

7.8 Lab: Non-Linear Modeling 319 

```
facecolor='gray',
alpha=0.3)
fordfin[1,3,4,8,15]:
lam=approx_lam(X_age,age_term,df+1)
age_term.lam=lam
gam.fit(X_age,y)
ax.plot(age_grid,
gam.predict(age_grid),
label='{:d}'.format(df),
linewidth=4)
ax.set_xlabel('Age',fontsize=20)
ax.set_ylabel('Wage',fontsize=20);
ax.legend(title='Degreesoffreedom');
```

Additive Models with Several Terms 

The strength of generalized additive models lies in their ability to fit multivariate regression models with more flexibility than linear models. We demonstrate two approaches: the first in a more manual fashion using natural splines and piecewise constant functions, and the second using the `pygam` package and smoothing splines. 

We now fit a GAM by hand to predict `wage` using natural spline functions of `year` and `age` , treating `education` as a qualitative predictor, as in (7.16). Since this is just a big linear regression model using an appropriate choice of basis functions, we can simply do this using the `sm.OLS()` function. 

We will build the model matrix in a more manual fashion here, since we wish to access the pieces separately when constructing partial dependence plots. 

```
In [28]:ns_age=NaturalSpline(df=4).fit(age)
ns_year=NaturalSpline(df=5).fit(Wage['year'])
Xs=[ns_age.transform(age),
ns_year.transform(Wage['year']),
pd.get_dummies(Wage['education']).values]
X_bh=np.hstack(Xs)
gam_bh=sm.OLS(y,X_bh).fit()
```

Here the function `NaturalSpline()` is the workhorse supporting the `ns()` helper function. We chose to use all columns of the indicator matrix for the categorical variable `education` , making an intercept redundant. Finally, we stacked the three component matrices horizontally to form the model matrix `X_bh` . 

We now show how to construct partial dependence plots for each of the terms in our rudimentary GAM. We can do this by hand, given grids for `age` and `year` . We simply predict with new _X_ matrices, fixing all but one of the features at a time. 

```
In [29]:age_grid=np.linspace(age.min(),
age.max(),
100)
X_age_bh=X_bh.copy()[:100]
X_age_bh[:]=X_bh[:].mean(0)[None,:]
X_age_bh[:,:4]=ns_age.transform(age_grid)
preds=gam_bh.get_prediction(X_age_bh)
bounds_age=preds.conf_int(alpha=0.05)
```

7. Moving Beyond Linearity 

320 

```
partial_age=preds.predicted_mean
center=partial_age.mean()
partial_age-=center
bounds_age-=center
fig,ax=subplots(figsize=(8,8))
ax.plot(age_grid,partial_age ,'b',linewidth=3)
ax.plot(age_grid,bounds_age[:,0],'r--',linewidth=3)
ax.plot(age_grid,bounds_age[:,1],'r--',linewidth=3)
ax.set_xlabel('Age')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofageonwage',fontsize=20);
```

Let’s explain in some detail what we did above. The idea is to create a new prediction matrix, where all but the columns belonging to `age` are constant (and set to their training-data means). The four columns for `age` are filled in with the natural spline basis evaluated at the 100 values in `age_grid` . 

1. We made a grid of length 100 in `age` , and created a matrix `X_age_bh` with 100 rows and the same number of columns as `X_bh` . 

2. We replaced every row of this matrix with the column means of the original. 

3. We then replace just the first four columns representing `age` with the natural spline basis computed at the values in `age_grid` . 

The remaining steps should by now be familiar. We also look at the effect of `year` on `wage` ; the process is the same. 

```
In [30]:year_grid=np.linspace(2003,2009,100)
year_grid=np.linspace(Wage['year'].min(),
Wage['year'].max(),
100)
X_year_bh=X_bh.copy()[:100]
X_year_bh[:]=X_bh[:].mean(0)[None,:]
X_year_bh[:,4:9]=ns_year.transform(year_grid)
preds=gam_bh.get_prediction(X_year_bh)
bounds_year=preds.conf_int(alpha=0.05)
partial_year=preds.predicted_mean
center=partial_year.mean()
partial_year-=center
bounds_year-=center
fig,ax=subplots(figsize=(8,8))
ax.plot(year_grid,partial_year ,'b',linewidth=3)
ax.plot(year_grid,bounds_year[:,0],'r--',linewidth=3)
ax.plot(year_grid,bounds_year[:,1],'r--',linewidth=3)
ax.set_xlabel('Year')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofyearonwage',fontsize=20);
```

We now fit the model (7.16) using smoothing splines rather than natural splines. All of the terms in (7.16) are fit simultaneously, taking each other into account to explain the response. The `pygam` package only works with matrices, so we must convert the categorical series `education` to its array representation, which can be found with the `cat.codes` attribute of `education` . As `year` only has 7 unique values, we use only seven basis functions for it. 

7.8 Lab: Non-Linear Modeling 

321 

```
In [31]:gam_full=LinearGAM(s_gam(0)+
s_gam(1,n_splines=7)+
f_gam(2,lam=0))
Xgam=np.column_stack([age,
Wage['year'],
Wage['education'].cat.codes])
gam_full=gam_full.fit(Xgam,y)
```

The two `s_gam()` terms result in smoothing spline fits, and use a default value for _λ_ ( `lam=0.6` ), which is somewhat arbitrary. For the categorical term `education` , specified using a `f_gam()` term, we specify `lam=0` to avoid any shrinkage. We produce the partial dependence plot in `age` to see the effect of these choices. 

The values for the plot are generated by the `pygam` package. We provide a `plot_gam()` function for partial-dependence plots in `ISLP.pygam` , which `plot_gam()` makes this job easier than in our last example with natural splines. 

```
In [32]:fig,ax=subplots(figsize=(8,8))
plot_gam(gam_full,0,ax=ax)
ax.set_xlabel('Age')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofageonwage-defaultlam=0.6',
fontsize=20);
```

We see that the function is somewhat wiggly. It is more natural to specify the `df` than a value for `lam` . We refit a GAM using four degrees of freedom each for `age` and `year` . Recall that the addition of one below takes into account the intercept of the smoothing spline. 

```
In [33]:age_term=gam_full.terms[0]
age_term.lam=approx_lam(Xgam,age_term,df=4+1)
year_term=gam_full.terms[1]
year_term.lam=approx_lam(Xgam,year_term,df=4+1)
gam_full=gam_full.fit(Xgam,y)
```

Note that updating `age_term.lam` above updates it in `gam_full.terms[0]` as well! Likewise for `year_term.lam` . 

Repeating the plot for `age` , we see that it is much smoother. We also produce the plot for `year` . 

```
In [34]:fig,ax=subplots(figsize=(8,8))
plot_gam(gam_full,
1,
ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Effectonwage')
ax.set_title('Partialdependenceofyearonwage',fontsize=20)
```

Finally we plot `education` , which is categorical. The partial dependence plot is different, and more suitable for the set of fitted constants for each level of this variable. 

```
In [35]:fig,ax=subplots(figsize=(8,8))
ax=plot_gam(gam_full,2)
ax.set_xlabel('Education')
ax.set_ylabel('Effectonwage')
```

322 7. Moving Beyond Linearity 

```
ax.set_title('Partialdependenceofwageoneducation',
fontsize=20);
ax.set_xticklabels(Wage['education'].cat.categories,fontsize=8);
```

---

## Sub-Chapters (하위 목차)

### ANOVA Tests for Additive Models (GAM 모형 층위 다중 적합 계층 모델 집단 속성 성향에 대한 F-Stat 분산 분석 통계적 비교 모델 점검 구간 결론 세트)
* [문서로 이동하기](./7_8_3_1_anova_tests_for_additive_models/)

주어진 어떤 변수 구성 조합 성분 모델 체계가 그 변수를 선형 컴포넌트로만 두는 게 적절한지, 아니면 필수불가결적 편향 해결용으로 반드시 복잡도 높은 비선형 모델 곡면 층 편입 처리가 유용한 이점이 있는지 GAM 구성 요소 서브넷 트리 체인들을 비교 대조하여 ANOVA 우위 스코어 검사로 엄격히 판정 필터링을 검증합니다.

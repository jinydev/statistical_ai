---
layout: default
title: "index"
---

# _11.8.1 Brain Cancer Data_ 

We begin with the `BrainCancer` data set, contained in the `ISLP` package. 

```
In [3]:BrainCancer=load_data('BrainCancer')
BrainCancer.columns
```

```
Out[3]:Index(['sex','diagnosis','loc','ki','gtv','stereo',
'status','time'],
dtype='object')
```

The rows index the 88 patients, while the 8 columns contain the predictors and outcome variables. We first briefly examine the data. 

```
In [4]:BrainCancer['sex'].value_counts()
```

```
Out[4]:Female45
Male43
Name:sex,dtype:int64
```

```
In [5]:BrainCancer['diagnosis'].value_counts()
```

490 11. Survival Analysis and Censored Data 

```
Out[5]:Meningioma42
HGglioma22
Other14
LGglioma9
Name:diagnosis,dtype:int64
```

```
In [6]:BrainCancer['status'].value_counts()
```

```
Out[6]:053
135
Name:status,dtype:int64
```

Before beginning an analysis, it is important to know how the `status` variable has been coded. Most software uses the convention that a `status` of 1 indicates an uncensored observation (often death), and a `status` of 0 indicates a censored observation. But some scientists might use the opposite coding. For the `BrainCancer` data set 35 patients died before the end of the study, so we are using the conventional coding. 

To begin the analysis, we re-create the Kaplan-Meier survival curve shown in Figure 11.2. The main package we will use for survival analysis is `lifelines` . The variable `time` corresponds to _yi_ , the time to the _i_ th `lifelines` event (either censoring or death). The first argument to `km.fit` is the event time, and the second argument is the censoring variable, with a 1 indicating an observed failure time. The `plot()` method produces a survival curve `.plot()` with pointwise confidence intervals. By default, these are 90% confidence intervals, but this can be changed by setting the `alpha` argument to one minus the desired confidence level. 

```
In [7]:fig,ax=subplots(figsize=(8,8))
km=KaplanMeierFitter()
km_brain=km.fit(BrainCancer['time'],BrainCancer['status'])
km_brain.plot(label='KaplanMeierestimate',ax=ax)
```

Next we create Kaplan-Meier survival curves that are stratified by `sex` , in order to reproduce Figure 11.3. We do this using the `groupby()` method of `.groupby()` a dataframe. This method returns a generator that can be iterated over in the `for` loop. In this case, the items in the `for` loop are 2-tuples representing the groups: the first entry is the value of the grouping column `sex` while the second value is the dataframe consisting of all rows in the dataframe matching that value of `sex` . We will want to use this data below in the logrank test, hence we store this information in the dictionary `by_sex` . Finally, we have also used the notion of _string interpolation_ to automatically label string the different lines in the plot. String interpolation is a powerful technique interpolation to format strings — `Python` has many ways to facilitate such operations. 

```
In [8]:fig,ax=subplots(figsize=(8,8))
by_sex={}
forsex,dfinBrainCancer.groupby('sex'):
by_sex[sex]=df
km_sex=km.fit(df['time'],df['status'])
km_sex.plot(label='Sex=%s'%sex,ax=ax)
```

As discussed in Section 11.4, we can perform a log-rank test to compare the survival of males to females. We use the `logrank_test()` function from `logrank_` 

```
test()
```

11.8 Lab: Survival Analysis 491 

the `lifelines.statistics` module. The first two arguments are the event times, with the second denoting the corresponding (optional) censoring indicators. 

```
In [9]:logrank_test(by_sex['Male']['time'],
by_sex['Female']['time'],
by_sex['Male']['status'],
by_sex['Female']['status'])
```

```
Out[9]:
```

```
t_0-1
null_distributionchisquared
degrees_of_freedom1
test_namelogrank_test
test_statisticp-log2(p)
1.440.232.12
```

The resulting _p_ -value is 0 _._ 23, indicating no evidence of a difference in survival between the two sexes. 

Next, we use the `CoxPHFitter()` estimator from `lifelines` to fit Cox `CoxPHFitter()` proportional hazards models. To begin, we consider a model that uses `sex` as the only predictor. 

```
In [10]:coxph=CoxPHFitter#shorthand
sex_df=BrainCancer[['time','status','sex']]
model_df=MS(['time','status','sex'],
intercept=False).fit_transform(sex_df)
cox_fit=coxph().fit(model_df,
'time',
'status')
cox_fit.summary[['coef','se(coef)','p']]
```

```
Out[10]:
```

```
coefse(coef)p
covariate
sex[Male]0.4076670.3420040.233263
```

The first argument to `fit` should be a data frame containing at least the event time (the second argument `time` in this case), as well as an optional censoring variable (the argument `status` in this case). Note also that the Cox model does not include an intercept, which is why we used the `intercept=False` argument to `ModelSpec` above. The `summary()` method delivers many columns; we chose to abbreviate its output here. It is possible to obtain the likelihood ratio test comparing this model to the one with no features as follows: 

```
In [11]:cox_fit.log_likelihood_ratio_test()
```

```
Out[11]:null_distributionchisquared
degrees_freedom1
test_namelog-likelihoodratiotest
test_statisticp-log2(p)
1.440.232.12
```

492 11. Survival Analysis and Censored Data 

Regardless of which test we use, we see that there is no clear evidence for a difference in survival between males and females. As we learned in this chapter, the score test from the Cox model is exactly equal to the log rank test statistic! 

Now we fit a model that makes use of additional predictors. We first note that one of our `diagnosis` values is missing, hence we drop that observation before continuing. 

```
In [12]:cleaned=BrainCancer.dropna()
all_MS=MS(cleaned.columns,intercept=False)
all_df=all_MS.fit_transform(cleaned)
fit_all=coxph().fit(all_df,
'time',
'status')
fit_all.summary[['coef','se(coef)','p']]
```

```
Out[12]:
```

||`coef`|`se(coef)`|`p`|
|---|---|---|---|
|`covariate`||||
|`sex[Male]`|`0.183748`|`0.360358`|`0.610119`|
|`diagnosis[LG glioma]`|`-1.239541`|`0.579557`|`0.032454`|
|`diagnosis[Meningioma]`|`-2.154566`|`0.450524`|`0.000002`|
|`diagnosis[Other]`|`-1.268870`|`0.617672`|`0.039949`|
|`loc[Supratentorial]`|`0.441195`|`0.703669`|`0.530664`|
|`ki`|`-0.054955`|`0.018314`|`0.002693`|
|`gtv`|`0.034293`|`0.022333`|`0.124660`|
|`stereo[SRT]`|`0.177778`|`0.601578`|`0.767597`|



The `diagnosis` variable has been coded so that the baseline corresponds to HG glioma. The results indicate that the risk associated with HG glioma is more than eight times (i.e. _e_[2] _[.]_[15] = 8 _._ 62) the risk associated with meningioma. In other words, after adjusting for the other predictors, patients with HG glioma have much worse survival compared to those with meningioma. In addition, larger values of the Karnofsky index, `ki` , are associated with lower risk, i.e. longer survival. 

Finally, we plot estimated survival curves for each diagnosis category, adjusting for the other predictors. To make these plots, we set the values of the other predictors equal to the mean for quantitative variables and equal to the mode for categorical. To do this, we use the `apply()` method across rows (i.e. `axis=0` ) with a function `representative` that checks if a column is categorical or not. 

```
In [13]:levels=cleaned['diagnosis'].unique()
defrepresentative(series):
ifhasattr(series.dtype,'categories'):
returnpd.Series.mode(series)
else:
returnseries.mean()
modal_data=cleaned.apply(representative ,axis=0)
```

We make four copies of the column means and assign the `diagnosis` column to be the four different diagnoses. 

```
In [14]:modal_df=pd.DataFrame(
[modal_data.iloc[0]for_inrange(len(levels))])
modal_df['diagnosis']=levels
modal_df
```

11.8 Lab: Survival Analysis 493 

```
Out[14]:
```

|`sex`|`diagnosis`|`loc`|`ki`|`gtv`|`stereo`|`...`|
|---|---|---|---|---|---|---|
|`Female`|`Meningioma`|`Supratentorial`|`80.920`|`8.687`|`SRT`|`...`|
|`Female`|`HG glioma`|`Supratentorial`|`80.920`|`8.687`|`SRT`|`...`|
|`Female`|`LG glioma`|`Supratentorial`|`80.920`|`8.687`|`SRT`|`...`|
|`Female`|`Other`|`Supratentorial`|`80.920`|`8.687`|`SRT`|`...`|



We then construct the model matrix based on the model specification `all_MS` used to fit the model, and name the rows according to the levels of `diagnosis` . 

```
In [15]:modal_X=all_MS.transform(modal_df)
modal_X.index=levels
modal_X
```

We can use the `predict_survival_function()` method to obtain the esti- `.predict_` mated survival function. 

```
survival_
function()
```

```
In [16]:predicted_survival=fit_all.predict_survival_function(modal_X)
predicted_survival
```

|**`Out[16]:`**||`Meningioma`|`HG glioma`|`LG glioma`|`Other`|
|---|---|---|---|---|---|
||`0.070`|`0.998`|`0.982`|`0.995`|`0.995`|
||`1.180`|`0.998`|`0.982`|`0.995`|`0.995`|
||`1.410`|`0.996`|`0.963`|`0.989`|`0.990`|
||`1.540`|`0.996`|`0.963`|`0.989`|`0.990`|
||`...`|`...`|`...`|`...`|`...`|
||`67.380`|`0.689`|`0.040`|`0.394`|`0.405`|
||`73.740`|`0.689`|`0.040`|`0.394`|`0.405`|
||`78.750`|`0.689`|`0.040`|`0.394`|`0.405`|
||`82.560`|`0.689`|`0.040`|`0.394`|`0.405`|
||`85 rows × 4 columns`|||||



This returns a data frame, whose plot methods yields the different survival curves. To avoid clutter in the plots, we do not display confidence intervals. 

```
In [17]:fig,ax=subplots(figsize=(8,8))
predicted_survival.plot(ax=ax);
```

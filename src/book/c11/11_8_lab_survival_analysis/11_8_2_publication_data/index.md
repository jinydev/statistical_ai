---
layout: default
title: "index"
---

# _11.8.2 Publication Data_ 

The `Publication` data presented in Section 11.5.4 can be found in the `ISLP` package. We first reproduce Figure 11.5 by plotting the Kaplan-Meier curves stratified on the `posres` variable, which records whether the study had a positive or negative result. 

```
In [18]:fig,ax=subplots(figsize=(8,8))
Publication=load_data('Publication')
by_result={}
forresult,dfinPublication.groupby('posres'):
by_result[result]=df
km_result=km.fit(df['time'],df['status'])
km_result.plot(label='Result=%d'%result,ax=ax)
```

As discussed previously, the _p_ -values from fitting Cox’s proportional hazards model to the `posres` variable are quite large, providing no evidence of a difference in time-to-publication between studies with positive versus negative results. 

494 11. Survival Analysis and Censored Data 

```
In [19]:posres_df=MS(['posres',
'time',
'status'],
intercept=False).fit_transform(Publication)
posres_fit=coxph().fit(posres_df,
'time',
'status')
posres_fit.summary[['coef','se(coef)','p']]
```

```
Out[19]:coefse(coef)p
covariate
posres0.1480760.1616250.359578
```

However, the results change dramatically when we include other predictors in the model. Here we exclude the funding mechanism variable. 

```
In [20]:model=MS(Publication.columns.drop('mech'),
intercept=False)
coxph().fit(model.fit_transform(Publication),
'time',
'status').summary[['coef','se(coef)','p']]
```

```
Out[20]:
```

||`coef`|`se(coef)`|`p`|
|---|---|---|---|
|`covariate`||||
|`posres`|`0.570774`|`0.175960`|`1.179606e-03`|
|`multi`|`-0.040863`|`0.251194`|`8.707727e-01`|
|`clinend`|`0.546180`|`0.262001`|`3.710099e-02`|
|`sampsize`|`0.000005`|`0.000015`|`7.506978e-01`|
|`budget`|`0.004386`|`0.002464`|`7.511276e-02`|
|`impact`|`0.058318`|`0.006676`|`2.426779e-18`|



We see that there are a number of statistically significant variables, including whether the trial focused on a clinical endpoint, the impact of the study, and whether the study had positive or negative results. 

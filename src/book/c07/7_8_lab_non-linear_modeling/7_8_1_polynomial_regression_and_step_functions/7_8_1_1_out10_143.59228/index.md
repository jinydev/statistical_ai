---
layout: default
title: "index"
---

# **`Out[10]:`** `143.59228` 

However, the ANOVA method works whether or not we used orthogonal polynomials, provided the models are nested. For example, we can use `anova_lm()` to compare the following three models, which all have a linear term in `education` and a polynomial in `age` of different degrees: 

```
In [11]:models=[MS(['education',poly('age',degree=d)])
fordinrange(1,4)]
XEs=[model.fit_transform(Wage)
formodelinmodels]
anova_lm(*[sm.OLS(y,X_).fit()forX_inXEs])
```

```
Out[11]:
```

||`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|
|`0`|`2997.0`|`3.902e+06`|`0.0`|`NaN`|`NaN`|`NaN`|
|`1`|`2996.0`|`3.759e+06`|`1.0`|`142862.701`|`113.992`|`3.838e-26`|
|`2`|`2995.0`|`3.754e+06`|`1.0`|`5926.207`|`4.729`|`2.974e-02`|



> 8Indexing starting at zero is confusing for the polynomial degree example, since `models[1]` is quadratic rather than linear! 

314 7. Moving Beyond Linearity 

As an alternative to using hypothesis tests and ANOVA, we could choose the polynomial degree using cross-validation, as discussed in Chapter 5. Next we consider the task of predicting whether an individual earns more than $250,000 per year. We proceed much as before, except that first we create the appropriate response vector, and then apply the `glm()` function using the binomial family in order to fit a polynomial logistic regression model. 

```
In [12]:X=poly_age.transform(Wage)
high_earn=Wage['high_earn']=y>250#shorthand
glm=sm.GLM(y>250,
X,
family=sm.families.Binomial())
B=glm.fit()
summarize(B)
Out[12]:coefstderrzP>|z|
intercept-4.30120.345-12.4570.000
poly(age,degree=4)[0]71.964226.1332.7540.006
poly(age,degree=4)[1]-85.772935.929-2.3870.017
poly(age,degree=4)[2]34.162619.6971.7340.083
poly(age,degree=4)[3]-47.400824.105-1.9660.049
```

```
Out[12]:
```

Once again, we make predictions using the `get_prediction()` method. 

```
In [13]:newX=poly_age.transform(age_df)
preds=B.get_prediction(newX)
bands=preds.conf_int(alpha=0.05)
```

We now plot the estimated relationship. 

```
In [14]:fig,ax=subplots(figsize=(8,8))
rng=np.random.default_rng(0)
ax.scatter(age+
0.2*rng.uniform(size=y.shape[0]),
np.where(high_earn,0.198,0.002),
fc='gray',
marker='|')
forval,lsinzip([preds.predicted_mean ,
bands[:,0],
bands[:,1]],
['b','r--','r--']):
ax.plot(age_df.values,val,ls,linewidth=3)
ax.set_title('Degree -4Polynomial',fontsize=20)
ax.set_xlabel('Age',fontsize=20)
ax.set_ylim([0,0.2])
ax.set_ylabel('P(Wage>250)',fontsize=20);
```

We have drawn the `age` values corresponding to the observations with `wage` values above 250 as gray marks on the top of the plot, and those with `wage` values below 250 are shown as gray marks on the bottom of the plot. We added a small amount of noise to jitter the `age` values a bit so that observations with the same `age` value do not cover each other up. This type of plot is often called a _rug plot_ . rug plot In order to fit a step function, as discussed in Section 7.2, we first use the `pd.qcut()` function to discretize `age` based on quantiles. Then we use `pd.qcut()` 

7.8 Lab: Non-Linear Modeling 315 

`pd.get_dummies()` to create the columns of the model matrix for this cate- `pd.get_` gorical variable. Note that this function will include _all_ columns for a given categorical, rather than the usual approach which drops one of the levels. 

```
dummies()
```

```
In [15]:cut_age=pd.qcut(age,4)
summarize(sm.OLS(y,pd.get_dummies(cut_age)).fit())
```

|**`Out[15]:`**|||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|---|
||`(17.999, `|`33.75]`|`94.1584`|`1.478`|`63.692`|`0.0`|
||`(33.75, `|`42.0]`|`116.6608`|`1.470`|`79.385`|`0.0`|
||`(42.0, `|`51.0]`|`119.1887`|`1.416`|`84.147`|`0.0`|
||`(51.0, `|`80.0]`|`116.5717`|`1.559`|`74.751`|`0.0`|



Here `pd.qcut()` automatically picked the cutpoints based on the quantiles 25%, 50% and 75%, which results in four regions. We could also have specified our own quantiles directly instead of the argument `4` . For cuts not based on quantiles we would use the `pd.cut()` function. The function `pd.cut() pd.qcut()` (and `pd.cut()` ) returns an ordered categorical variable. The regression model then creates a set of dummy variables for use in the regression. Since `age` is the only variable in the model, the value $94,158.40 is the average salary for those under 33.75 years of age, and the other coefficients are the average salary for those in the other age groups. We can produce predictions and plots just as we did in the case of the polynomial fit. 

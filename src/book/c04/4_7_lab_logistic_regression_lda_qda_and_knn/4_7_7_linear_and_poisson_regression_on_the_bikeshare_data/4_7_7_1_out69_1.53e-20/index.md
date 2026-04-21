---
layout: default
title: "index"
---

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../index.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/index.html)


# **`Out[69]:`** `1.53e-20` 

The sum of squared differences is zero. We can also see this using the `np.allclose()` function: 

```
np.allclose()
```

```
In [70]:np.allclose(M_lm.fittedvalues ,M2_lm.fittedvalues)
```

```
Out[70]:True
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with `mnth` . The coefficients for January through November can be obtained directly from the `M2_lm` object. The coefficient for December must be explicitly computed as the negative sum of all the other months. We first extract all the coefficients for month from the coefficients of `M2_lm` . 

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 191 

```
In [71]:coef_month=S2[S2.index.str.contains('mnth')]['coef']
coef_month
```

```
Out[71]:mnth[Jan]-46.0871
mnth[Feb]-39.2419
mnth[March]-29.5357
mnth[April]-4.6622
mnth[May]26.4700
mnth[June]21.7317
mnth[July]-0.7626
mnth[Aug]7.1560
mnth[Sept]20.5912
mnth[Oct]29.7472
mnth[Nov]14.2229
Name:coef,dtype:float64
```

Next, we append `Dec` as the negative of the sum of all other months. 

```
In [72]:months=Bike['mnth'].dtype.categories
coef_month=pd.concat([
coef_month,
pd.Series([-coef_month.sum()],
index=['mnth[Dec]'
])
])
coef_month
```

```
Out[72]:mnth[Jan]-46.0871
mnth[Feb]-39.2419
mnth[March]-29.5357
mnth[April]-4.6622
mnth[May]26.4700
mnth[June]21.7317
mnth[July]-0.7626
mnth[Aug]7.1560
mnth[Sept]20.5912
mnth[Oct]29.7472
mnth[Nov]14.2229
mnth[Dec]0.3705
Name:coef,dtype:float64
```

Finally, to make the plot neater, we’ll just use the first letter of each month, which is the 6th entry of each of the labels in the index. 

```
In [73]:fig_month,ax_month=subplots(figsize=(8,8))
x_month=np.arange(coef_month.shape[0])
ax_month.plot(x_month,coef_month ,marker='o',ms=10)
ax_month.set_xticks(x_month)
ax_month.set_xticklabels([l[5]forlincoef_month.index],fontsize
=20)
ax_month.set_xlabel('Month',fontsize=20)
ax_month.set_ylabel('Coefficient',fontsize=20);
```

Reproducing the right-hand plot in Figure 4.13 follows a similar process. 

```
In [74]:coef_hr=S2[S2.index.str.contains('hr')]['coef']
coef_hr=coef_hr.reindex(['hr[{0}]'.format(h)forhinrange(23)])
coef_hr=pd.concat([coef_hr,
```

192 4. Classification 

```
pd.Series([-coef_hr.sum()],index=['hr[23]'])
])
```

We now make the hour plot. 

```
In [75]:fig_hr,ax_hr=subplots(figsize=(8,8))
x_hr=np.arange(coef_hr.shape[0])
ax_hr.plot(x_hr,coef_hr,marker='o',ms=10)
ax_hr.set_xticks(x_hr[::2])
ax_hr.set_xticklabels(range(24)[::2],fontsize=20)
ax_hr.set_xlabel('Hour',fontsize=20)
ax_hr.set_ylabel('Coefficient',fontsize=20);
```

---

## Sub-Chapters


[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../index.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/index.html)

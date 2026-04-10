---
layout: default
title: "index"
---

# _7.8.4 Local Regression_ 

We illustrate the use of local regression using the `lowess()` function from `lowess() sm.nonparametric` . Some implementations of GAMs allow terms to be local regression operators; this is not the case in `pygam` . Here we fit local linear regression models using spans of 0.2 and 0.5; that is, each neighborhood consists of 20% or 50% of the observations. As expected, using a span of 0.5 is smoother than 0.2. 

```
In [49]:lowess=sm.nonparametric.lowess
fig,ax=subplots(figsize=(8,8))
ax.scatter(age,y,facecolor='gray',alpha=0.5)
forspanin[0.2,0.5]:
fitted=lowess(y,
```

7.9 Exercises 325 

`age, frac=span, xvals=age_grid) ax.plot(age_grid, fitted, label='{:.1f}'.format(span), linewidth=4) ax.set_xlabel('Age', fontsize=20) ax.set_ylabel('Wage', fontsize=20); ax.legend(title='span', fontsize=15);` 

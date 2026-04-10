---
layout: default
title: "index"
---

# _3.6.5 Interaction Terms_ 

It is easy to include interaction terms in a linear model using `ModelSpec()` . Including a tuple `("lstat","age")` tells the model matrix builder to include an interaction term between `lstat` and `age` . 

```
In [31]:X=MS(['lstat',
'age',
('lstat','age')]).fit_transform(Boston)
model2=sm.OLS(y,X)
summarize(model2.fit())
```

```
Out[31]:coefstderrtP>|t|
intercept36.08851.47024.5530.000
lstat-1.39210.167-8.3130.000
```

3.6 Lab: Linear Regression 

```
age-0.00070.020-0.0360.971
lstat:age0.00420.0022.2440.025
```

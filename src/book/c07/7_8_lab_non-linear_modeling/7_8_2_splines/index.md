---
layout: default
title: "index"
---

# _7.8.2 Splines_ 

In order to fit regression splines, we use transforms from the `ISLP` package. The actual spline evaluation functions are in the `scipy.interpolate` package; we have simply wrapped them as transforms similar to `Poly()` and `PCA()` . 

In Section 7.4, we saw that regression splines can be fit by constructing an appropriate matrix of basis functions. The `BSpline()` function generates `BSpline()` the entire matrix of basis functions for splines with the specified set of knots. By default, the B-splines produced are cubic. To change the degree, use the argument `degree` . 

```
In [16]:bs_=BSpline(internal_knots=[25,40,60],intercept=True).fit(age)
bs_age=bs_.transform(age)
bs_age.shape
```

```
Out[16]:(3000,7)
```

This results in a seven-column matrix, which is what is expected for a cubicspline basis with 3 interior knots. We can form this same matrix using the `bs()` object, which facilitates adding this to a model-matrix builder (as in `poly()` versus its workhorse `Poly()` ) described in Section 7.8.1. We now fit a cubic spline model to the `Wage` data. 

```
In [17]:bs_age=MS([bs('age',internal_knots=[25,40,60])])
Xbs=bs_age.fit_transform(Wage)
M=sm.OLS(y,Xbs).fit()
summarize(M)
```

316 7. Moving Beyond Linearity 

```
Out[17]:
```

||||`coef`|`std err`|`...`|
|---|---|---|---|---|---|
|||`intercept`|`60.494`|`9.460`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[0]`|`3.980`|`12.538`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[1]`|`44.631`|`9.626`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[2]`|`62.839`|`10.755`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[3]`|`55.991`|`10.706`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[4]`|`50.688`|`14.402`|`...`|
|`bs(age, `|`internal_knots=[25, `|`40, 60])[5]`|`16.606`|`19.126`|`...`|



The column names are a little cumbersome, and have caused us to truncate the printed summary. They can be set on construction using the `name` argument as follows. 

```
In [18]:bs_age=MS([bs('age',
internal_knots=[25,40,60],
name='bs(age)')])
Xbs=bs_age.fit_transform(Wage)
M=sm.OLS(y,Xbs).fit()
summarize(M)
```

```
Out[18]:
```

|||`coef `|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`60.494`|`9.460`|`6.394`|`0.000`|
|`bs(age, `|`knots)[0]`|`3.981`|`12.538`|`0.317`|`0.751`|
|`bs(age, `|`knots)[1]`|`44.631`|`9.626`|`4.636`|`0.000`|
|`bs(age, `|`knots)[2]`|`62.839`|`10.755`|`5.843`|`0.000`|
|`bs(age, `|`knots)[3]`|`55.991`|`10.706`|`5.230`|`0.000`|
|`bs(age, `|`knots)[4]`|`50.688`|`14.402`|`3.520`|`0.000`|
|`bs(age, `|`knots)[5]`|`16.606`|`19.126`|`0.868`|`0.385`|



Notice that there are 6 spline coefficients rather than 7. This is because, by default, `bs()` assumes `intercept=False` , since we typically have an overall intercept in the model. So it generates the spline basis with the given knots, and then discards one of the basis functions to account for the intercept. 

We could also use the `df` (degrees of freedom) option to specify the complexity of the spline. We see above that with 3 knots, the spline basis has 6 columns or degrees of freedom. When we specify `df=6` rather than the actual knots, `bs()` will produce a spline with 3 knots chosen at uniform quantiles of the training data. We can see these chosen knots most easily using `Bspline()` directly: 

```
In [19]:BSpline(df=6).fit(age).internal_knots_
```

```
Out[19]:array([33.75,42.0,51.0])
```

When asking for six degrees of freedom, the transform chooses knots at ages 33.75, 42.0, and 51.0, which correspond to the 25th, 50th, and 75th percentiles of `age` . 

When using B-splines we need not limit ourselves to cubic polynomials (i.e. `degree=3` ). For instance, using `degree=0` results in piecewise constant functions, as in our example with `pd.qcut()` above. 

```
In [20]:bs_age0=MS([bs('age',
df=3,
degree=0)]).fit(Wage)
Xbs0=bs_age0.transform(Wage)
summarize(sm.OLS(y,Xbs0).fit())
```

7.8 Lab: Non-Linear Modeling 317 

```
Out[20]:
```

||||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|---|
|||`intercept`|`94.158`|`1.478`|`63.687`|`0.0`|
|`bs(age, `|`df=3, `|`degree=0)[0]`|`22.349`|`2.152`|`10.388`|`0.0`|
|`bs(age, `|`df=3, `|`degree=0)[1]`|`24.808`|`2.044`|`12.137`|`0.0`|
|`bs(age, `|`df=3, `|`degree=0)[2]`|`22.781`|`2.087`|`10.917`|`0.0`|



This fit should be compared with cell [15] where we use `qcut()` to create four bins by cutting at the 25%, 50% and 75% quantiles of `age` . Since we specified `df=3` for degree-zero splines here, there will also be knots at the same three quantiles. Although the coefficients appear different, we see that this is a result of the different coding. For example, the first coefficient is identical in both cases, and is the mean response in the first bin. For the second coefficient, we have 94 _._ 158 + 22 _._ 349 = 116 _._ 507 _≈_ 116 _._ 611, the latter being the mean in the second bin in cell [15]. Here the intercept is coded by a column of ones, so the second, third and fourth coefficients are increments for those bins. Why is the sum not exactly the same? It turns out that the `qcut()` uses _≤_ , while `bs()` uses _<_ when deciding bin membership. 

In order to fit a natural spline, we use the `NaturalSpline()` transform `Natural` with the corresponding helper `ns()` . Here we fit a natural spline with five `Spline()` degrees of freedom (excluding the intercept) and plot the results. 

```
In [21]:ns_age=MS([ns('age',df=5)]).fit(Wage)
M_ns=sm.OLS(y,ns_age.transform(Wage)).fit()
summarize(M_ns)
```

|**`Out[21]:`**|||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|---|
|||`intercept`|`60.475`|`4.708`|`12.844`|`0.000`|
||`ns(age, `|`df=5)[0]`|`61.527`|`4.709`|`13.065`|`0.000`|
||`ns(age, `|`df=5)[1]`|`55.691`|`5.717`|`9.741`|`0.000`|
||`ns(age, `|`df=5)[2]`|`46.818`|`4.948`|`9.463`|`0.000`|
||`ns(age, `|`df=5)[3]`|`83.204`|`11.918`|`6.982`|`0.000`|
||`ns(age, `|`df=5)[4]`|`6.877`|`9.484`|`0.725`|`0.468`|



We now plot the natural spline using our plotting function. 

```
In [22]:plot_wage_fit(age_df,
```

```
ns_age,
'Naturalspline,df=5');
```

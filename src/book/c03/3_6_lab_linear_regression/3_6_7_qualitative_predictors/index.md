---
layout: default
title: "index"
---

# _3.6.7 Qualitative Predictors_ 

Here we use the `Carseats` data, which is included in the `ISLP` package. We will attempt to predict `Sales` (child car seat sales) in 400 locations based on a number of predictors. 

```
In [35]:Carseats=load_data('Carseats')
Carseats.columns
```

```
Out[35]:Index(['Sales','CompPrice','Income','Advertising',
'Population','Price','ShelveLoc','Age','Education',
'Urban','US'],
dtype='object')
```

The `Carseats` data includes qualitative predictors such as `ShelveLoc` , an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed. The predictor `ShelveLoc` takes on three possible values, `Bad` , `Medium` , and `Good` . Given a qualitative variable such as `ShelveLoc` , `ModelSpec()` generates dummy variables automatically. These variables are often referred to as a _one-hot encoding_ of the categorical one-hot feature. Their columns sum to one, so to avoid collinearity with an interencoding cept, the first column is dropped. Below we see the column `ShelveLoc[Bad]` has been dropped, since `Bad` is the first level of `ShelveLoc` . Below we fit a multiple regression model that includes some interaction terms. 

encoding 

```
In [36]:allvars=list(Carseats.columns.drop('Sales'))
y=Carseats['Sales']
final=allvars+[('Income','Advertising'),
('Price','Age')]
X=MS(final).fit_transform(Carseats)
model=sm.OLS(y,X)
summarize(model.fit())
Out[36]:coefstderrtP>|t|
intercept6.57561.0096.5190.000
```

3.7 Exercises 

|`CompPrice`|`0.0929`|`0.004`|`22.567`|`0.000`|
|---|---|---|---|---|
|`Income`|`0.0109`|`0.003`|`4.183`|`0.000`|
|`Advertising`|`0.0702`|`0.023`|`3.107`|`0.002`|
|`Population`|`0.0002`|`0.000`|`0.433`|`0.665`|
|`Price`|`-0.1008`|`0.007`|`-13.549`|`0.000`|
|`ShelveLoc[Good]`|`4.8487`|`0.153`|`31.724`|`0.000`|
|`ShelveLoc[Medium]`|`1.9533`|`0.126`|`15.531`|`0.000`|
|`Age`|`-0.0579`|`0.016`|`-3.633`|`0.000`|
|`Education`|`-0.0209`|`0.020`|`-1.063`|`0.288`|
|`Urban[Yes]`|`0.1402`|`0.112`|`1.247`|`0.213`|
|`US[Yes]`|`-0.1576`|`0.149`|`-1.058`|`0.291`|
|`Income:Advertising`|`0.0008`|`0.000`|`2.698`|`0.007`|
|`Price:Age`|`0.0001`|`0.000`|`0.801`|`0.424`|



In the first line above, we made `allvars` a list, so that we could add the interaction terms two lines down. Our model-matrix builder has created a `ShelveLoc[Good]` dummy variable that takes on a value of 1 if the shelving location is good, and 0 otherwise. It has also created a `ShelveLoc[Medium]` dummy variable that equals 1 if the shelving location is medium, and 0 otherwise. A bad shelving location corresponds to a zero for each of the two dummy variables. The fact that the coefficient for `ShelveLoc[Good]` in the regression output is positive indicates that a good shelving location is associated with high sales (relative to a bad location). And `ShelveLoc[Medium]` has a smaller positive coefficient, indicating that a medium shelving location leads to higher sales than a bad shelving location, but lower sales than a good shelving location. 

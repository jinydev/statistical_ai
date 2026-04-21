---
layout: default
title: "index"
---

[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/index.html) | [3.7 Exercises >](../../3_7_exercises/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.7 Qualitative Predictors_

Here we use the `Carseats` data, which is included in the `ISLP` package.

```
In [35]: Carseats = load_data('Carseats')
Carseats.columns
```

```
Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising',
       'Population', 'Price', 'ShelveLoc', 'Age', 'Education',
       'Urban', 'US'],
      dtype='object')
```

The `Carseats` data includes qualitative predictors such as `ShelveLoc` , an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed.

encoding

```
In [36]: allvars = list(Carseats.columns.drop('Sales'))
y = Carseats['Sales']
final = allvars + [('Income', 'Advertising'),
                   ('Price', 'Age')]
X = MS(final).fit_transform(Carseats)
model = sm.OLS(y, X)
summarize(model.fit())

Out[36]:             coef  std err       t  P>|t|
intercept       6.5756   1.009   6.519  0.000
```

|`CompPrice`|`0.0929`|`0.004`|`22.567`|`0.000`|

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

In the first line above, we made `allvars` a list, so that we could add the interaction terms two lines down.

---

## Sub-Chapters


[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/index.html) | [3.7 Exercises >](../../3_7_exercises/index.html)

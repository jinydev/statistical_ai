---
layout: default
title: "index"
---

[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/index.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/index.html)


# _4.7.7 Linear and Poisson Regression on the Bikeshare Data_ 

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6. The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012. 

```python
In [64]: Bike = load_data('Bikeshare')
```

Let’s have a peek at the dimensions and names of the variables in this dataframe. 

```python
In [65]: Bike.shape, Bike.columns
```

```python
Out[65]: ((8645, 15),
          Index(['season', 'mnth', 'day', 'hr', 'holiday', 'weekday',
                 'workingday', 'weathersit', 'temp', 'atemp', 'hum',
                 'windspeed', 'casual', 'registered', 'bikers'],
                dtype='object'))
```

Linear Regression 

We begin by fitting a linear regression model to the data. 

```python
In [66]: X = MS(['mnth',
                 'hr',
                 'workingday',
                 'temp',
                 'weathersit']).fit_transform(Bike)
Y = Bike['bikers']
M_lm = sm.OLS(Y, X).fit()
summarize(M_lm)
```

```python
Out[66]:
```

| | `coef` | `std err` | `t` | `P>|t|` |
|---|---|---|---|---|
| `intercept` | `-68.6317` | `5.307` | `-12.932` | `0.000` |
| `mnth[Feb]` | `6.8452` | `4.287` | `1.597` | `0.110` |
| `mnth[March]` | `16.5514` | `4.301` | `3.848` | `0.000` |
| `mnth[April]` | `41.4249` | `4.972` | `8.331` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

There are 24 levels in `hr` and 40 rows in all, so we have truncated the summary. In `M_lm`, the first levels `hr[0]` and `mnth[Jan]` are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines. For example, the Feb coefficient of $6.845$ signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January. Similarly there are about 16.5 more riders in March than in January. 

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth`, as follows: 

```python
In [67]: hr_encode = contrast('hr', 'sum')
mnth_encode = contrast('mnth', 'sum')
```

Refitting again: 

```python
In [68]: X2 = MS([mnth_encode,
                  hr_encode,
                  'workingday',
                  'temp',
                  'weathersit']).fit_transform(Bike)
M2_lm = sm.OLS(Y, X2).fit()
S2 = summarize(M2_lm)
S2
```

```python
Out[68]:
```

| | `coef` | `std err` | `t` | `P>|t|` |
|---|---|---|---|---|
| `intercept` | `73.5974` | `5.132` | `14.340` | `0.000` |
| `mnth[Jan]` | `-46.0871` | `4.085` | `-11.281` | `0.000` |
| `mnth[Feb]` | `-39.2419` | `3.539` | `-11.088` | `0.000` |
| `.....` | `.......` | `.....` | `.....` | `.....` |

What is the difference between the two codings? In `M2_lm`, a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth`. Importantly, in `M2_lm`, the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels. Similarly, in `M2_lm`, the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels. This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can be interpreted as the difference from the mean level. For example, the coefficient for January of $-46.087$ indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average. 

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used. For example, we see that the predictions from the linear model are the same regardless of coding: 

```python
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2)
```

```python
Out[69]: 5.166710408544458e-09
```

---

---

## Sub-Chapters


[< 4.7.6 K-Nearest Neighbors](../4_7_6_k-nearest_neighbors/index.html) | [4.7.7.1 Out69 1.53E-20 >](4_7_7_1_out69_1.53e-20/index.html)

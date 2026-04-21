---
layout: default
title: "index"
---

# Forward Selection 

We will apply the forward-selection approach to the `Hitters` data. We wish to predict a baseball player’s `Salary` on the basis of various statistics associated with performance in the previous year. 

First of all, we note that the `Salary` variable is missing for some of the players. The `np.isnan()` function can be used to identify the missing observations. It returns an array of the same shape as the input vector, with a `True` for any elements that are missing, and a `False` for non-missing elements. The `sum()` method can then be used to count all of the missing elements. 

```python
In [3]: Hitters = load_data('Hitters')
np.isnan(Hitters['Salary']).sum()
```

```
Out[3]: 59
```

We see that `Salary` is missing for 59 players. The `dropna()` method of data frames removes all of the rows that have missing values in any variable (by default — see `Hitters.dropna?` ). 

```python
In [4]: Hitters = Hitters.dropna()
Hitters.shape
```

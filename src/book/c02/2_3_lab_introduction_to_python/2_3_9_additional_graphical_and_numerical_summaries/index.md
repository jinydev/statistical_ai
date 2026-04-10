---
layout: default
title: "index"
---

# _2.3.9 Additional Graphical and Numerical Summaries_

We can use the `ax.plot()` or `ax.scatter()` functions to display the quantitative variables. However, simply typing the variable names will produce an error message, because `Python` does not know to look in the `Auto` data set for those variables.

```python
In [101]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(horsepower, mpg, 'o');
NameError: name 'horsepower' is not defined
```

We can address this by accessing the columns directly:

```python
In [102]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(Auto['horsepower'], Auto['mpg'], 'o');
```

Alternatively, we can use the `plot()` method with the call `Auto.plot()`. Using this method, the variables can be accessed by name. The plot methods of a data frame return a familiar object: an axes. We can use it to update the plot as we did previously:

```python
In [103]: ax = Auto.plot.scatter('horsepower', 'mpg')
          ax.set_title('Horsepower vs. MPG');
```

If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the `figure` attribute:

```python
In [104]: fig = ax.figure
          fig.savefig('horsepower_mpg.png');
```

We can further instruct the data frame to plot to a particular axes object. In this case the corresponding `plot()` method will return the modified axes we passed in as an argument. Note that when we request a one-dimensional grid of plots, the object `axes` is similarly one-dimensional. We place our scatter plot in the middle plot of a row of three plots within a figure.

```python
In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))
          Auto.plot.scatter('horsepower', 'mpg', ax=axes[1]);
```

Note also that the columns of a data frame can be accessed as attributes: try typing in `Auto.horsepower`.

We now consider the `cylinders` variable. Typing in `Auto.cylinders.dtype` reveals that it is being treated as a quantitative variable. However, since there is only a small number of possible values for this variable, we may wish to treat it as qualitative. Below, we replace the `cylinders` column with a categorical version of `Auto.cylinders`. The function `pd.Series()` owes its name to the fact that `pandas` is often used in time series applications.

```python
In [106]: Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
          Auto.cylinders.dtype
```

Now that `cylinders` is qualitative, we can display it using the `boxplot()` method.

```python
In [107]: fig, ax = subplots(figsize=(8, 8))
          Auto.boxplot('mpg', by='cylinders', ax=ax);
```

The `hist()` method can be used to plot a _histogram_.

```python
In [108]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', ax=ax);
```

The color of the bars and the number of bins can be changed:

```python
In [109]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', color='red', bins=12, ax=ax);
```

See `Auto.hist?` for more plotting options. We can use the `pd.plotting.scatter_matrix()` function to create a _scatterplot matrix_ to visualize all of the pairwise relationships between the columns in a data frame.

```python
In [110]: pd.plotting.scatter_matrix(Auto);
```

We can also produce scatterplots for a subset of the variables.

```python
In [111]: pd.plotting.scatter_matrix(Auto[['mpg',
                                           'displacement',
                                           'weight']]);
```

The `describe()` method produces a numerical summary of each column in a data frame.

```python
In [112]: Auto[['mpg', 'weight']].describe()
```

We can also produce a summary of just a single column.

```python
In [113]: Auto['cylinders'].describe()
          Auto['mpg'].describe()
```

To exit `Jupyter`, select `File / Close and Halt`.

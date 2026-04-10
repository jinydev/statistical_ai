---
layout: default
title: "index"
---

# _2.3.4 Graphics_

In `Python`, common practice is to use the library `matplotlib` for graphics. However, since `Python` was not written with data analysis in mind, the notion of plotting is not intrinsic to the language. We will use the `subplots()` function from `matplotlib.pyplot` to create a figure and the axes onto which we plot our data. For many more examples of how to make plots in `Python`, readers are encouraged to visit `matplotlib.org/stable/gallery/`.

In `matplotlib`, a plot consists of a _figure_ and one or more _axes_. You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window. The _axes_ contain important information about each plot, such as its $x$- and $y$-axis labels, title, and more. (Note that in `matplotlib`, the word _axes_ is not the plural of _axis_: a plot’s _axes_ contains much more information than just the $x$-axis and the $y$-axis.)

We begin by importing the `subplots()` function from `matplotlib`. We use this function throughout when creating figures. The function returns a tuple of length two: a figure object as well as the relevant axes object. We will typically pass `figsize` as a keyword argument. Having created our axes, we attempt our first plot using its `plot()` method. To learn more about it, type `ax.plot?`.

```python
In [39]: from matplotlib.pyplot import subplots
         fig, ax = subplots(figsize=(8, 8))
         x = rng.standard_normal(100)
         y = rng.standard_normal(100)
         ax.plot(x, y);
```

We pause here to note that we have _unpacked_ the tuple of length two returned by `subplots()` into the two distinct variables `fig` and `ax`. Unpacking is typically preferred to the following equivalent but slightly more verbose code:

```python
In [40]: output = subplots(figsize=(8, 8))
         fig = output[0]
         ax = output[1]
```

We see that our earlier cell produced a line plot, which is the default. To create a scatterplot, we provide an additional argument to `ax.plot()`, indicating that circles should be displayed.

```python
In [41]: fig, ax = subplots(figsize=(8, 8))
         ax.plot(x, y, 'o');
```

Different values of this additional argument can be used to produce different colored lines as well as different linestyles. As an alternative, we could use the `ax.scatter()` function to create a scatterplot. 

```python
In [42]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o');
```

Notice that in the code blocks above, we have ended the last line with a semicolon. This prevents `ax.plot(x, y)` from printing text to the notebook. However, it does not prevent a plot from being produced. If we omit the trailing semi-colon, then we obtain the following output:

```python
In [43]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
Out[43]: <matplotlib.collections.PathCollection at 0x7fb3d9c8f310>
```

In what follows, we will use trailing semicolons whenever the text that would be output is not germane to the discussion at hand. 

To label our plot, we make use of the `set_xlabel()`, `set_ylabel()`, and `set_title()` methods of `ax`.

```python
In [44]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
         ax.set_xlabel("this is the x-axis")
         ax.set_ylabel("this is the y-axis")
         ax.set_title("Plot of X vs Y");
```

Having access to the figure object `fig` itself means that we can go in and change some aspects and then redisplay it. Here, we change the size from `(8, 8)` to `(12, 3)`.

```python
fig.set_size_inches(12, 3)
fig
```

Occasionally we will want to create several plots within a figure. This can be achieved by passing additional arguments to `subplots()`. Below, we create a $2 \times 3$ grid of plots in a figure of size determined by the `figsize` argument. In such situations, there is often a relationship between the axes in the plots. For example, all plots may have a common $x$-axis. The `subplots()` function can automatically handle this situation when passed the keyword argument `sharex=True`. The `axes` object below is an array pointing to different plots in the figure.

```python
In [45]: fig, axes = subplots(nrows=2,
                              ncols=3,
                              figsize=(15, 5))
```

We now produce a scatter plot with `'o'` in the second column of the first row and a scatter plot with `'+'` in the third column of the second row.

```python
In [46]: axes[0, 1].plot(x, y, 'o')
         axes[1, 2].scatter(x, y, marker='+')
         fig
```

Type `subplots?` to learn more about `subplots()`. To save the output of `fig`, we call its `savefig()` method. The argument `dpi` is the dots per inch, used to determine how large the figure will be in pixels.

```python
In [47]: fig.savefig("Figure.png", dpi=400)
         fig.savefig("Figure.pdf", dpi=200);
```

We can continue to modify `fig` using step-by-step updates; for example, we can modify the range of the $x$-axis, re-save the figure, and even re-display it.

```python
In [48]: axes[0, 1].set_xlim([-1, 1])
         fig.savefig("Figure_updated.jpg")
         fig
```

We now create some more sophisticated plots. The `ax.contour()` method produces a _contour plot_ in order to represent three-dimensional data, similar to a topographical map. It takes three arguments:

- A vector of `x` values (the first dimension),
- A vector of `y` values (the second dimension), and
- A matrix whose elements correspond to the `z` value (the third dimension) for each pair of `(x, y)` coordinates.

To create `x` and `y`, we’ll use the command `np.linspace(a, b, n)`, which returns a vector of `n` numbers starting at `a` and ending at `b`.

```python
In [49]: fig, ax = subplots(figsize=(8, 8))
         x = np.linspace(-np.pi, np.pi, 50)
         y = x
         f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
         ax.contour(x, y, f);
```

We can increase the resolution by adding more levels to the image.

```python
In [50]: fig, ax = subplots(figsize=(8, 8))
         ax.contour(x, y, f, levels=45);
```

To fine-tune the output of the `ax.contour()` function, take a look at the help file by typing `?plt.contour`. The `ax.imshow()` method is similar to `ax.contour()`, except that it produces a color-coded plot whose colors depend on the `z` value. This is known as a _heatmap_, and is sometimes used to plot temperature in weather forecasts.

```python
In [51]: fig, ax = subplots(figsize=(8, 8))
         ax.imshow(f);
```

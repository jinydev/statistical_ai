---
layout: default
title: "index"
---

[< 2.3.2 Basic Commands](../2_3_2_basic_commands/index.html) | [2.3.4 Graphics >](../2_3_4_graphics/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2.3.3 Introduction to Numerical Python

As mentioned earlier, this book makes use of functionality that is contained in the `numpy` _library_, or _package_.

A package is a collection of modules that are not necessarily included in the base `Python` distribution.

The name `numpy` is an abbreviation for _numerical Python_.

To access `numpy`, we must first `import` it.

```python
In [7]: import numpy as np
```

In the previous line, we named the `numpy` _module_ `np`; an abbreviation for easier referencing.

In `numpy`, an _array_ is a generic term for a multidimensional set of numbers.

We use the `np.array()` function to define `x` and `y`, which are one-dimensional arrays, i.e. vectors.

```python
In [8]: x = np.array([3, 4, 5])
        y = np.array([4, 9, 7])
```

Note that if you forgot to run the `import numpy as np` command earlier, then you will encounter an error in calling the `np.array()` function in the previous line.

The syntax `np.array()` indicates that the function being called is part of the `numpy` package, which we have abbreviated as `np`.

Since `x` and `y` have been defined using `np.array()`, we get a sensible result when we add them together.

Compare this to our results in the previous section, when we tried to add two lists without using `numpy`.

```python
In [9]: x + y
Out[9]: array([ 7, 13, 12])
```

In `numpy`, matrices are typically represented as two-dimensional arrays, and vectors as one-dimensional arrays.[1]

We can create a two-dimensional array as follows.

```python
In [10]: x = np.array([[1, 2], [3, 4]])
         x
Out[10]: array([[1, 2],
                [3, 4]])
```

The object `x` has several _attributes_, or associated objects.

To access an attribute of `x`, we type `x.attribute`, where we replace `attribute` with the name of the attribute.

For instance, we can access the `ndim` attribute of `x` as follows.

```python
In [11]: x.ndim
Out[11]: 2
```

The output indicates that `x` is a two-dimensional array.

Similarly, `x.dtype` is the _data type_ attribute of the object `x`.

This indicates that `x` is comprised of 64-bit integers:

> 1 While it is also possible to create matrices using `np.matrix()`, we will use `np.array()` throughout the labs in this book.

```python
In [12]: x.dtype
Out[12]: dtype('int64')
```

Why is `x` comprised of integers?

This is because we created `x` by passing in exclusively integers to the `np.array()` function.

If we had passed in any decimals, then we would have obtained an array of _floating point numbers_ (i.e. real-valued numbers).

```python
In [13]: np.array([[1, 2], [3.0, 4]]).dtype
Out[13]: dtype('float64')
```

Typing `fun?` will cause `Python` to display documentation associated with the function `fun`, if it exists.

We can try this for `np.array()`.

```python
In [14]: np.array?
```

This documentation indicates that we could create a floating point array by passing a `dtype` argument into `np.array()`.

```python
In [15]: np.array([[1, 2], [3, 4]], float).dtype
Out[15]: dtype('float64')
```

The array `x` is two-dimensional.

We can find out the number of rows and columns by looking at its `shape` attribute.

```python
In [16]: x.shape
Out[16]: (2, 2)
```

A _method_ is a function that is associated with an object.

For instance, given an array `x`, the expression `x.sum()` sums all of its elements, using the `sum()` method for arrays.

The call `x.sum()` automatically provides `x` as the first argument to its `sum()` method.

```python
In [17]: x = np.array([1, 2, 3, 4])
         x.sum()
Out[17]: 10
```

We could also sum the elements of `x` by passing in `x` as an argument to the `np.sum()` function.

```python
In [18]: x = np.array([1, 2, 3, 4])
         np.sum(x)
Out[18]: 10
```

As another example, the `reshape()` method returns a new array with the same elements as `x`, but a different shape.

```python
In [19]: x = np.array([1, 2, 3, 4, 5, 6])
         print('beginning x:\n', x)
         x_reshape = x.reshape((2, 3))
         print('reshaped x:\n', x_reshape)
beginning x:
 [1 2 3 4 5 6]
reshaped x:
 [[1 2 3]
  [4 5 6]]
```

The previous output reveals that `numpy` arrays are specified as a sequence of _rows_.

This is called _row-major ordering_, as opposed to _column-major ordering_.

`Python` (and hence `numpy`) uses 0-based indexing.

This means that to access the top left element of `x_reshape`, we type in `x_reshape[0,0]`.

```python
In [20]: x_reshape[0,0]
Out[20]: 1
```

Similarly, `x_reshape[1,2]` yields the element in the second row and the third column of `x_reshape`.

```python
In [21]: x_reshape[1,2]
Out[21]: 6
```

Similarly, `x[2]` yields the third entry of `x`.

Now, let’s modify the top left element of `x_reshape`.

To our surprise, we discover that the first element of `x` has been modified as well!

```python
In [22]: print('x before we modify x_reshape:\n', x)
         print('x_reshape before we modify x_reshape:\n', x_reshape)
         x_reshape[0,0] = 5
         print('x_reshape after we modify its top left element:\n', x_reshape)
         print('x after we modify top left element of x_reshape:\n', x)
x before we modify x_reshape:
 [1 2 3 4 5 6]
x_reshape before we modify x_reshape:
 [[1 2 3]
  [4 5 6]]
x_reshape after we modify its top left element:
 [[5 2 3]
  [4 5 6]]
x after we modify top left element of x_reshape:
 [5 2 3 4 5 6]
```

> 2 Like lists, tuples represent a sequence of objects. Why do we need more than one way to create a sequence? There are a few differences between tuples and lists, but perhaps the most important is that elements of a tuple cannot be modified, whereas elements of a list can be.

We just saw that we can modify an element of an array.

Can we also modify a tuple?

It turns out that we cannot — and trying to do so introduces an _exception_, or error.

```python
In [23]: my_tuple = (3, 4, 5)
         my_tuple[0] = 2
```

```
TypeError: 'tuple' object does not support item assignment
```

We now briefly mention some attributes of arrays that will come in handy.

An array’s `shape` attribute contains its dimension; this is always a tuple.

The `ndim` attribute yields the number of dimensions, and `T` provides its transpose.

```python
In [24]: x_reshape.shape, x_reshape.ndim, x_reshape.T
```

```python
Out[24]: ((2, 3),
          2,
          array([[5, 4],
                 [2, 5],
                 [3, 6]]))
```

Notice that the three individual outputs `(2,3)`, `2`, and `array([[5, 4],[2, 5], [3,6]])` are themselves output as a tuple.

We will often want to apply functions to arrays.

For instance, we can compute the square root of the entries using the `np.sqrt()` function:

```python
In [25]: np.sqrt(x)
Out[25]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

We can also square the elements:

```python
In [26]: x**2
Out[26]: array([25,  4,  9, 16, 25, 36])
```

We can compute the square roots using the same notation, raising to the power of $1/2$ instead of 2.

```python
In [27]: x**0.5
Out[27]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

Throughout this book, we will often want to generate random data.

The `np.random.normal()` function generates a vector of random normal variables.

We can learn more about this function by looking at the help page, via a call to `np.random.normal?`.

The first line of the help page reads `normal(loc=0.0, scale=1.0, size=None)`.

This _signature_ line tells us that the function’s arguments are `loc`, `scale`, and `size`.

These are _keyword_ arguments, which means that when they are passed into the function, they can be referred to by name (in any order).[3]

By default, this function will generate random normal variable(s) with mean (`loc`) 0 and standard deviation (`scale`) 1; furthermore, a single random variable will be generated unless the argument to `size` is changed.

We now generate 50 independent random variables from a $N(0, 1)$ distribution.

```python
In [28]: x = np.random.normal(size=50)
         x
Out[28]: array([-1.19,  0.41,  0.9 , -0.44, -0.9 , -0.38,  0.13,  1.87,
                -0.35,  1.16,  0.79, -0.97, -1.21,  0.06, -1.62, -0.6 ,
                -0.77, -2.12,  0.38, -1.22, -0.06, -1.97, -1.74, -0.56,
                 1.7 , -0.95,  0.56,  0.35,  0.87,  0.88, -1.66, -0.32,
                -0.3 , -1.36,  0.92, -0.31,  1.28, -1.94,  1.07,  0.07,
                 0.79, -0.46,  2.19, -0.27, -0.64,  0.85,  0.13,  0.46,
                -0.09,  0.7 ])
```

We create an array `y` by adding an independent $N(50, 1)$ random variable to each element of `x`.

```python
In [29]: y = x + np.random.normal(loc=50, scale=1, size=50)
```

The `np.corrcoef()` function computes the correlation matrix between `x` and `y`.

The off-diagonal elements give the correlation between `x` and `y`.

```python
In [30]: np.corrcoef(x, y)
Out[30]: array([[1.  , 0.69],
                [0.69, 1.  ]])
```

If you’re following along in your own `Jupyter` notebook, then you probably noticed that you got a different set of results when you ran the past few commands.

In particular, each time we call `np.random.normal()`, we will get a different answer, as shown in the following example.

```python
In [31]: print(np.random.normal(scale=5, size=2))
         print(np.random.normal(scale=5, size=2))
[ 4.28  2.59]
[ 4.62 -2.54]
```

In order to ensure that our code provides exactly the same results each time it is run, we can set a _random seed_ using the `np.random.default_rng()` function.

This function takes an arbitrary, user-specified integer argument.

If we set a random seed before generating random data, then re-running our code will yield the same results.

The object `rng` has essentially all the random number generating methods found in `np.random`.

Hence, to generate normal data we use `rng.normal()`.

```python
In [32]: rng = np.random.default_rng(1303)
         print(rng.normal(scale=5, size=2))
         rng2 = np.random.default_rng(1303)
         print(rng2.normal(scale=5, size=2))
[ 4.09 -1.07]
[ 4.09 -1.07]
```

Throughout the labs in this book, we use `np.random.default_rng()` whenever we perform calculations involving random quantities within `numpy`.

In principle, this should enable the reader to exactly reproduce the stated results.

However, as new versions of `numpy` become available, it is possible that some small discrepancies may occur between the output in the labs and the output from `numpy`.

The `np.mean()`, `np.var()`, and `np.std()` functions can be used to compute the mean, variance, and standard deviation of arrays.

These functions are also available as methods on the arrays.

> 3 `Python` also uses _positional_ arguments. Positional arguments do not need to use a keyword. To see an example, type in `np.sum?`. We see that `a` is a positional argument, i.e. this function assumes that the first unnamed argument that it receives is the array to be summed. By contrast, `axis` and `dtype` are keyword arguments: the position in which these arguments are entered into `np.sum()` does not matter.

```python
In [33]: rng = np.random.default_rng(3)
         y = rng.standard_normal(10)
         np.mean(y), y.mean()
Out[33]: (-0.11, -0.11)
```

```python
In [34]: np.var(y), y.var(), np.mean((y - y.mean())**2)
Out[34]: (2.72, 2.72, 2.72)
```

Notice that by default `np.var()` divides by the sample size _n_ rather than $n - 1$; see the `ddof` argument in `np.var?`.

```python
In [35]: np.sqrt(np.var(y)), np.std(y)
Out[35]: (1.65, 1.65)
```

The `np.mean()`, `np.var()`, and `np.std()` functions can also be applied to the rows and columns of a matrix.

To see this, we construct a $10 \times 3$ matrix of $N(0, 1)$ random variables, and consider computing its row sums.

```python
In [36]: X = rng.standard_normal((10, 3))
         X
Out[36]: array([[ 0.23, -0.35, -0.28],
                [-0.67, -1.06, -0.39],
                [ 0.48, -0.24,  0.96],
                [-0.2 ,  0.02,  1.55],
                [ 0.55, -0.51, -0.18],
                [ 0.54,  1.94, -0.27],
                [-0.24,  1.  , -0.89],
                [-0.29,  0.88,  0.58],
                [ 0.09,  0.67, -2.83],
                [ 1.02, -0.96, -1.67]])
```

Since arrays are row-major ordered, the first axis, i.e. `axis=0`, refers to its rows.

We pass this argument into the `mean()` method for the object `X`.

```python
In [37]: X.mean(axis=0)
Out[37]: array([ 0.15,  0.14, -0.34])
```

The following yields the same result.

```python
In [38]: X.mean(0)
Out[38]: array([ 0.15,  0.14, -0.34])
```

---

## Sub-Chapters


[< 2.3.2 Basic Commands](../2_3_2_basic_commands/index.html) | [2.3.4 Graphics >](../2_3_4_graphics/index.html)

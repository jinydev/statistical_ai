---
layout: default
title: "index"
---

# _3.6.1 Importing packages_ 

We import our standard libraries at this top level. 

```
In [1]:importnumpyasnp
importpandasaspd
frommatplotlib.pyplotimportsubplots
```

New imports 

Throughout this lab we will introduce new functions and libraries. However, we will import them here to emphasize these are the new code objects in this lab. Keeping imports near the top of a notebook makes the code more readable, since scanning the first few lines tells us what libraries are used. 

```
In [2]:importstatsmodels.apiassm
```

We will provide relevant details about the functions below as they are needed. 

Besides importing whole modules, it is also possible to import only a few items from a given module. This will help keep the _namespace_ clean. namespace We will use a few specific objects from the `statsmodels` package which we `statsmodels` import here. 

```
In [3]:fromstatsmodels.stats.outliers_influence\
importvariance_inflation_factorasVIF
fromstatsmodels.stats.anovaimportanova_lm
```

As one of the import statements above is quite a long line, we inserted a line break `\` to ease readability. 

We will also use some functions written for the labs in this book in the `ISLP` package. 

```
In [4]:fromISLPimportload_data
fromISLP.modelsimport(ModelSpecasMS,
summarize,
poly)
```

Inspecting Objects and Namespaces 

The function `dir()` provides a list of objects in a namespace. 

```
dir()
```

```
In [5]:dir()
```

```
Out[5]:['In',
'MS',
'_',
'__',
'___',
'__builtin__',
'__builtins__',
...
```

3.6 Lab: Linear Regression 117 

```
'poly',
'quit',
'sm',
'summarize']
```

This shows you everything that `Python` can find at the top level. There are certain objects like `__builtins__` that contain references to built-in functions like `print()` . 

Every python object has its own notion of namespace, also accessible with `dir()` . This will include both the attributes of the object as well as any methods associated with it. For instance, we see `'sum'` in the listing for an array. 

```
In [6]:A=np.array([3,5,11])
dir(A)
```

```
Out[6]:...
'strides',
'sum',
'swapaxes',
...
```

This indicates that the object `A.sum` exists. In this case it is a method that can be used to compute the sum of the array `A` as can be seen by typing `A.sum?` . 

```
In [7]:A.sum()
```

```
Out[7]:19
```

---
layout: default
title: "index"
---

[< 2.3.6 Indexing Data](../2_3_6_indexing_data/index.html) | [2.3.8 For Loops >](../2_3_8_for_loops/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2.3.7 Loading Data

Data sets often contain different types of data, and may have names associated with the rows or columns.

For these reasons, they typically are best accommodated using a _data frame_.

We can think of a data frame as a sequence of arrays of identical length; these are the columns.

Entries in the different arrays can be combined to form a row.

The `pandas` library can be used to create and work with data frame objects.

## Reading in a Data Set

The first step of most analyses involves importing a data set into `Python`.

Before attempting to load a data set, we must make sure that `Python` knows where to find the file containing it.

If the file is in the same location as this notebook file, then we are all set.

Otherwise, the command `os.chdir()` can be used to _change directory_. (You will need to call `import os` before calling `os.chdir()`.)

We will begin by reading in `Auto.csv`, available on the book website.

This is a comma-separated file, and can be read in using `pd.read_csv()`:

```python
In [73]: import pandas as pd
         Auto = pd.read_csv('Auto.csv')
         Auto
```

The book website also has a whitespace-delimited version of this data, called `Auto.data`.

This can be read in as follows:

```python
In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
```

Both `Auto.csv` and `Auto.data` are simply text files.

Before loading data into `Python`, it is a good idea to view it using a text editor or other software, such as Microsoft Excel.

We now take a look at the column of `Auto` corresponding to the variable `horsepower`:

```python
In [75]: Auto['horsepower']
Out[75]: 0       130.0
         1       165.0
         2       150.0
         3       150.0
         4       140.0
               ...
         392      86.0
         393      52.0
         394      84.0
         395      79.0
         396      82.0
         Name: horsepower, Length: 397, dtype: object
```

We see that the `dtype` of this column is `object`.

It turns out that all values of the `horsepower` column were interpreted as strings when reading in the data.

We can find out why by looking at the unique values.

```python
In [76]: np.unique(Auto['horsepower'])
```

To save space, we have omitted the output of the previous code block.

We see the culprit is the value `?`, which is being used to encode missing values.

To fix the problem, we must provide `pd.read_csv()` with an argument called `na_values`.

Now, each instance of `?` in the file is replaced with the value `np.nan`, which means _not a number_:

```
In [77]:Auto=pd.read_csv('Auto.data',
na_values=['?'],
delim_whitespace=True)
Auto['horsepower'].sum()
```

```
Out[77]:40952.0
```

The `Auto.shape` attribute tells us that the data has 397 observations, or rows, and nine variables, or columns.

```
In [78]:Auto.shape
```

```
Out[78]:(397,9)
```

There are various ways to deal with missing data.

In this case, since only five of the rows contain missing observations, we choose to use the `Auto.dropna()` method to simply remove these rows.

```
.dropna()
```

```
In [79]:Auto_new=Auto.dropna()
Auto_new.shape
```

```
Out[79]:(392,9)
```

## Basics of Selecting Rows and Columns

We can use `Auto.columns` to check the variable names.

```
In [80]:Auto=Auto_new#overwritethepreviousvalue
Auto.columns
```

```
Out[80]:Index(['mpg','cylinders','displacement','horsepower',
'weight','acceleration','year','origin','name'],
dtype='object')
```

Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array.

Recall that the first argument to the `[]` method is always applied to the rows of the array.

Similarly, passing in a slice to the `[]` method creates a data frame whose _rows_ are determined by the slice:

```
In [81]:Auto[:3]
```

|**`Out[81]:`**||`mpg`|`cylinders`|`displacement`|`horsepower`|`weight`|`...`|

||`0`|`18.0`|`8`|`307.0`|`130.0`|`3504.0`|`...`|

||`2`|`18.0`|`8`|`318.0`|`150.0`|`3436.0`|`...`|

```
In [82]:idx_80=Auto['year']>80
Auto[idx_80]
```

However, if we pass in a list of strings to the `[]` method, then we obtain a data frame containing the corresponding set of _columns_ .

```python
In [83]: Auto[['mpg', 'horsepower']]
Out[83]:       mpg  horsepower
         0    18.0       130.0
         1    15.0       165.0
         2    18.0       150.0
         3    16.0       150.0
         4    17.0       140.0
         ..    ...         ...
         392  27.0        86.0
         393  44.0        52.0
         394  32.0        84.0
         395  28.0        79.0
         396  31.0        82.0

         [392 rows x 2 columns]
```

Since we did not specify an _index_ column when we loaded our data frame, the rows are labeled using integers 0 to 396.

```python
In [84]: Auto.index
Out[84]: Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
                     ...
                     387, 388, 389, 390, 391, 392, 393, 394, 395, 396],
                    dtype='int64', length=392)
```

We can use the `set_index()` method to re-name the rows using the contents of `Auto['name']`.

```python
In [85]: Auto_re = Auto.set_index('name')
         Auto_re
Out[85]:                            mpg  cylinders  displacement  ...
         name                                                     ...
         chevrolet chevelle malibu  18.0          8         307.0  ...
         buick skylark 320          15.0          8         350.0  ...
         plymouth satellite         18.0          8         318.0  ...
         amc rebel sst              16.0          8         304.0  ...
```

```python
In [86]: Auto_re.columns
Out[86]: Index(['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'year', 'origin'],
               dtype='object')
```

We see that the column `'name'` is no longer there.

Now that the index has been set to `name`, we can access rows of the data frame by `name` using the `loc[]` method of `Auto`:

```
.loc[]
```python

In [87]: rows = ['amc rebel sst', 'ford torino']

Out[87]:                mpg  cylinders  displacement  horsepower  ...

amc rebel sst  16.0          8         304.0       150.0  ...

```

As an alternative to using the index name, we could retrieve the 4th and 5th rows of `Auto` using the `iloc[]` method:

```python

In [88]: Auto_re.iloc[[3, 4]]

```

We can also use it to retrieve the 1st, 3rd and and 4th columns of `Auto_re`:

```python

In [89]: Auto_re.iloc[:, [0, 2, 3]]

```

We can extract the 4th and 5th rows, as well as the 1st, 3rd and 4th columns, using a single call to `iloc[]`:

```python

In [90]: Auto_re.iloc[[3, 4], [0, 2, 3]]

name

ford torino    17.0         302.0       140.0

```

Index entries need not be unique: there are several cars in the data frame named `ford galaxie 500`.

```python

In [91]: Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]

name

ford galaxie 500  14.0       1

```

### More on Selecting Rows and Columns

Suppose now that we want to create a data frame consisting of the `weight` and `origin` of the subset of cars with `year` greater than 80 — i.e. those built after 1980.

To do this, we first create a Boolean array that indexes the rows.

The `loc[]` method allows for Boolean entries as well as strings:

```python

In [92]: idx_80 = Auto_re['year'] > 80

```

To do this more concisely, we can use an anonymous function called a `lambda`:

```python

In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]

```

The `lambda` call creates a function that takes a single argument, here `df`, and returns `df['year'] > 80`.

Since it is created inside the `loc[]` method for the dataframe `Auto_re`, that dataframe will be the argument supplied.

As another example of using a `lambda`, suppose that we want all cars built after 1980 that achieve greater than 30 miles per gallon:

```python

In [94]: Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30),

]

```

The symbol `&` computes an element-wise _and_ operation.

As another example, suppose that we want to retrieve all `Ford` and `Datsun` cars with `displacement` less than 300.

We check whether each `name` entry contains either the string `ford` or `datsun` using the `str.contains()` method of the `index` attribute of the dataframe:

```python

In [95]: Auto_re.loc[lambda df: (df['displacement'] < 300)

| df.index.str.contains('datsun')),

]

```

Here, the symbol `|` computes an element-wise _or_ operation.

In summary, a powerful set of operations is available to index the rows and columns of data frames.

For integer based queries, use the `iloc[]` method.

For string and Boolean selections, use the `loc[]` method.

For functional queries that filter rows, use the `loc[]` method with a function (typically a `lambda`) in the rows argument.

---

## Sub-Chapters


[< 2.3.6 Indexing Data](../2_3_6_indexing_data/index.html) | [2.3.8 For Loops >](../2_3_8_for_loops/index.html)

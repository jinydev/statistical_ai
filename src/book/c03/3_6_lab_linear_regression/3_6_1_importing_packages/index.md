---
layout: default
title: "index"
---

[< 3.6 Lab Linear Regression](../index.html) | [3.6.2 Simple Linear Regression >](../3_6_2_simple_linear_regression/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# _3.6.1 Importing packages_

We import our standard libraries at this top level.

```
In [1]: import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
```

```
In [2]: import statsmodels.api as sm
```

We will provide relevant details about the functions below as they are needed.

Besides importing whole modules, it is also possible to import only a few items from a given module.

This will help keep the _namespace_ clean.

We will use a few specific objects from the `statsmodels` package which we import here.

```
In [3]: from statsmodels.stats.outliers_influence \
import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm
```

As one of the import statements above is quite a long line, we inserted a line break `\` to ease readability.

We will also use some functions written for the labs in this book in the `ISLP` package.

```
In [4]: from ISLP import load_data
from ISLP.models import (ModelSpec as MS,
summarize,
poly)
```

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

```
'poly',
'quit',
'sm',
'summarize']
```

This shows you everything that `Python` can find at the top level.

There are certain objects like `__builtins__` that contain references to built-in functions like `print()`.

Every python object has its own notion of namespace, also accessible with `dir()`.

This will include both the attributes of the object as well as any methods associated with it.

For instance, we see `'sum'` in the listing for an array.

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

This indicates that the object `A.sum` exists.

In this case it is a method that can be used to compute the sum of the array `A` as can be seen by typing `A.sum?`.

```
In [7]:A.sum()
```

```
Out[7]:19
```

---

## Sub-Chapters


[< 3.6 Lab Linear Regression](../index.html) | [3.6.2 Simple Linear Regression >](../3_6_2_simple_linear_regression/index.html)

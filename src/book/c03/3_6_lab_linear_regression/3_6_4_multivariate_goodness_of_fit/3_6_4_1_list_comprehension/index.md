---
layout: default
title: "index"
---

# List Comprehension 

Often we encounter a sequence of objects which we would like to transform for some other task. Below, we compute the VIF for each feature in our `X` matrix and produce a data frame whose index agrees with the columns of `X` . The notion of list comprehension can often make such a task easier. 

124 3. Linear Regression 

List comprehensions are simple and powerful ways to form lists of `Python` objects. The language also supports dictionary and _generator_ comprehension, though these are beyond our scope here. Let’s look at an example. We compute the VIF for each of the variables in the model matrix `X` , using the function `variance_inflation_factor()` . 

```
In [29]:vals=[VIF(X,i)
foriinrange(1,X.shape[1])]
vif=pd.DataFrame({'vif':vals},
index=X.columns[1:])
vif
```

```
Out[29]:
```

```
vif
crim1.767
zn2.298
indus3.987
chas1.071
nox4.369
rm1.913
age3.088
dis3.954
rad7.445
tax9.002
ptratio1.797
lstat2.871
```

```
variance_
inflation_
factor()
```

The function `VIF()` takes two arguments: a dataframe or array, and a variable column index. In the code above we call `VIF()` on the fly for all columns in `X` . We have excluded column 0 above (the intercept), which is not of interest. In this case the VIFs are not that exciting. 

The object `vals` above could have been constructed with the following for loop: 

```
In [30]:vals=[]
foriinrange(1,X.values.shape[1]):
vals.append(VIF(X.values,i))
```

List comprehension allows us to perform such repetitive operations in a more straightforward way. 

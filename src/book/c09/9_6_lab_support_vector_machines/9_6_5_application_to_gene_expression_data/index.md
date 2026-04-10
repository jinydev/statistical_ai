---
layout: default
title: "index"
---

# _9.6.5 Application to Gene Expression Data_ 

We now examine the `Khan` data set, which consists of a number of tissue samples corresponding to four distinct types of small round blue cell tumors. For each tissue sample, gene expression measurements are available. The data set consists of training data, `xtrain` and `ytrain` , and testing data, `xtest` and `ytest` . 

We examine the dimension of the data: 

```
In [32]:Khan=load_data('Khan')
Khan['xtrain'].shape,Khan['xtest'].shape
```

```
Out[32]:((63,2308),(20,2308))
```

This data set consists of expression measurements for 2,308 genes. The training and test sets consist of 63 and 20 observations, respectively. 

We will use a support vector approach to predict cancer subtype using gene expression measurements. In this data set, there is a very large number of features relative to the number of observations. This suggests that we should use a linear kernel, because the additional flexibility that will result from using a polynomial or radial kernel is unnecessary. 

```
In [33]:khan_linear=SVC(kernel='linear',C=10)
khan_linear.fit(Khan['xtrain'],Khan['ytrain'])
confusion_table(khan_linear.predict(Khan['xtrain']),
Khan['ytrain'])
```

```
Out[33]:
```

|`Truth`|`1`|`2`|`3`|`4`|
|---|---|---|---|---|
|`Predicted`|||||
|`1`|`8`|`0`|`0`|`0`|
|`2`|`0`|`23`|`0`|`0`|
|`3`|`0`|`0`|`12`|`0`|
|`4`|`0`|`0`|`0`|`20`|



We see that there are _no_ training errors. In fact, this is not surprising, because the large number of variables relative to the number of observations implies that it is easy to find hyperplanes that fully separate the classes. 

9.7 Exercises 395 

We are more interested in the support vector classifier’s performance on the test observations. 

```
In [34]:confusion_table(khan_linear.predict(Khan['xtest']),
Khan['ytest'])
```

|**`Out[34]:`**|`Truth`|`1`|`2`|`3`|`4`|
|---|---|---|---|---|---|
||`Predicted`|||||
||`1`|`3`|`0`|`0`|`0`|
||`2`|`0`|`6`|`2`|`0`|
||`3`|`0`|`0`|`4`|`0`|
||`4`|`0`|`0`|`0`|`5`|



We see that using `C=10` yields two test set errors on these data. 

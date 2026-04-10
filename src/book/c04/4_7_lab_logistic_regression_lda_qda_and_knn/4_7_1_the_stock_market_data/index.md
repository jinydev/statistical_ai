---
layout: default
title: "index"
---

# _4.7.1 The Stock Market Data_ 

In this lab we will examine the `Smarket` data, which is part of the `ISLP` library. This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005. For each date, we have recorded the percentage returns for each of the five previous trading days, `Lag1` through `Lag5` . We have also recorded `Volume` (the number of shares traded on the previous day, in billions), `Today` (the percentage return on the date in question) and `Direction` (whether the market was `Up` or `Down` on this date). 

We start by importing our libraries at this top level; these are all imports we have seen in previous labs. 

```
In [1]:importnumpyasnp
importpandasaspd
frommatplotlib.pyplotimportsubplots
importstatsmodels.apiassm
fromISLPimportload_data
fromISLP.modelsimport(ModelSpecasMS,
summarize)
```

We also collect together the new imports needed for this lab. 

```
In [2]:fromISLPimportconfusion_table
fromISLP.modelsimportcontrast
fromsklearn.discriminant_analysisimport\
(LinearDiscriminantAnalysisasLDA,
QuadraticDiscriminantAnalysisasQDA)
fromsklearn.naive_bayesimportGaussianNB
fromsklearn.neighborsimportKNeighborsClassifier
fromsklearn.preprocessingimportStandardScaler
```

174 4. Classification 

```
fromsklearn.model_selectionimporttrain_test_split
fromsklearn.linear_modelimportLogisticRegression
```

Now we are ready to load the `Smarket` data. 

```
In [3]:Smarket=load_data('Smarket')
Smarket
```

This gives a truncated listing of the data, which we do not show here. We can see what the variable names are. 

```
In [4]:Smarket.columns
```

```
Out[4]:Index(['Year','Lag1','Lag2','Lag3','Lag4','Lag5','Volume',
'Today','Direction'],
dtype='object')
```

We compute the correlation matrix using the `corr()` method for data `.corr()` frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.) The `pandas` library does not report a correlation for the `Direction` variable because it is qualitative. 

```
In [5]:Smarket.corr()
```

As one would expect, the correlations between the lagged return variables and today’s return are close to zero. The only substantial correlation is between `Year` and `Volume` . By plotting the data we see that `Volume` is increasing over time. In other words, the average number of shares traded daily increased from 2001 to 2005. 

```
In [6]:Smarket.plot(y='Volume');
```

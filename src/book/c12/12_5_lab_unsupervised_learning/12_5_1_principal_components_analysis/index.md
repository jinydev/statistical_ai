---
layout: default
title: "index"
---

# _12.5.1 Principal Components Analysis_ 

In this lab, we perform PCA on `USArrests` , a data set in the `R` computing environment. We retrieve the data using `get_rdataset()` , which can fetch `get_` 

```
rdataset()
```

536 12. Unsupervised Learning 

data from many standard `R` packages. 

The rows of the data set contain the 50 states, in alphabetical order. 

```
In [3]:USArrests=get_rdataset('USArrests').data
USArrests
```

|**`Out[3]:`**||`Murder`|`Assault`|`UrbanPop`|`Rape`|
|---|---|---|---|---|---|
||`Alabama`|`13.2`|`236`|`58`|`21.2`|
||`Alaska`|`10.0`|`263`|`48`|`44.5`|
||`Arizona`|`8.1`|`294`|`80`|`31.0`|
||`...`|`...`|`...`|`...`|`...`|
||`Wisconsin`|`2.6`|`53`|`66`|`10.8`|
||`Wyoming`|`6.8`|`161`|`60`|`15.6`|



The columns of the data set contain the four variables. 

```
In [4]:USArrests.columns
```

```
Out[4]:Index(['Murder','Assault','UrbanPop','Rape'],
dtype='object')
```

We first briefly examine the data. We notice that the variables have vastly different means. 

```
In [5]:USArrests.mean()
```

|**`Out[5]:`**|`Murder`|`7.788`|
|---|---|---|
||`Assault`|`170.760`|
||`UrbanPop`|`65.540`|
||`Rape`|`21.232`|
||`dtype: float64`||



Dataframes have several useful methods for computing column-wise summaries. We can also examine the variance of the four variables using the `var()` method. 

```
In [6]:USArrests.var()
```

|**`Out[6]:`**|`Murder`|`18.970465`|
|---|---|---|
||`Assault`|`6945.165714`|
||`UrbanPop`|`209.518776`|
||`Rape`|`87.729159`|
||`dtype: float64`||



Not surprisingly, the variables also have vastly different variances. The `UrbanPop` variable measures the percentage of the population in each state living in an urban area, which is not a comparable number to the number of rapes in each state per 100,000 individuals. PCA looks for derived variables that account for most of the variance in the data set. If we do not scale the variables before performing PCA, then the principal components would mostly be driven by the `Assault` variable, since it has by far the largest variance. So if the variables are measured in different units or vary widely in scale, it is recommended to standardize the variables to have standard deviation one before performing PCA. Typically we set the means to zero as well. 

12.5 Lab: Unsupervised Learning 537 

This scaling can be done via the `StandardScaler()` transform imported above. We first `fit` the scaler, which computes the necessary means and standard deviations and then apply it to our data using the `transform` method. As before, we combine these steps using the `fit_transform()` method. 

```
In [7]:scaler=StandardScaler(with_std=True,
with_mean=True)
USArrests_scaled=scaler.fit_transform(USArrests)
```

Having scaled the data, we can then perform principal components analysis using the `PCA()` transform from the `sklearn.decomposition` package. 

```
PCA()
```

```
In [8]:pcaUS=PCA()
```

(By default, the `PCA()` transform centers the variables to have mean zero though it does not scale them.) The transform `pcaUS` can be used to find the PCA `scores` returned by `fit()` . Once the `fit` method has been called, the `pcaUS` object also contains a number of useful quantities. 

```
In [9]:pcaUS.fit(USArrests_scaled)
```

After fitting, the `mean_` attribute corresponds to the means of the variables. In this case, since we centered and scaled the data with `scaler()` the means will all be 0. 

```
In [10]:pcaUS.mean_
```

```
Out[10]:array([-0.,0.,-0.,0.])
```

The scores can be computed using the `transform()` method of `pcaUS` after it has been fit. 

```
In [11]:scores=pcaUS.transform(USArrests_scaled)
```

We will plot these scores a bit further down. The `components_` attribute provides the principal component loadings: each row of `pcaUS.components_` contains the corresponding principal component loading vector. 

```
In [12]:pcaUS.components_
```

```
Out[12]:array([[0.53589947,0.58318363,0.27819087,0.54343209],
[0.41818087,0.1879856,-0.87280619,-0.16731864],
[-0.34123273,-0.26814843,-0.37801579,0.81777791],
[0.6492278,-0.74340748,0.13387773,0.08902432]])
```

The `biplot` is a common visualization method used with PCA. It is not built in as a standard part of `sklearn` , though there are python packages that do produce such plots. Here we make a simple biplot manually. 

```
In [13]:i,j=0,1#whichcomponents
fig,ax=plt.subplots(1,1,figsize=(8,8))
ax.scatter(scores[:,0],scores[:,1])
ax.set_xlabel('PC%d'%(i+1))
ax.set_ylabel('PC%d'%(j+1))
forkinrange(pcaUS.components_.shape[1]):
```

538 12. Unsupervised Learning 

```
ax.arrow(0,0,pcaUS.components_[i,k],pcaUS.components_[j,k])
ax.text(pcaUS.components_[i,k],
pcaUS.components_[j,k],
USArrests.columns[k])
```

Notice that this figure is a reflection of Figure 12.1 through the _y_ -axis. Recall that the principal components are only unique up to a sign change, so we can reproduce that figure by flipping the signs of the second set of scores and loadings. We also increase the length of the arrows to emphasize the loadings. 

```
In [14]:scale_arrow=s_=2
scores[:,1]*=-1
pcaUS.components_[1]*=-1#flipthey-axis
fig,ax=plt.subplots(1,1,figsize=(8,8))
ax.scatter(scores[:,0],scores[:,1])
ax.set_xlabel('PC%d'%(i+1))
ax.set_ylabel('PC%d'%(j+1))
forkinrange(pcaUS.components_.shape[1]):
ax.arrow(0,0,s_*pcaUS.components_[i,k],s_*pcaUS.components_[
j,k])
ax.text(s_*pcaUS.components_[i,k],
s_*pcaUS.components_[j,k],
USArrests.columns[k])
```

The standard deviations of the principal component scores are as follows: 

```
In [15]:scores.std(0,ddof=1)
```

```
Out[15]:array([1.5909,1.0050,0.6032,0.4207])
```

The variance of each score can be extracted directly from the `pcaUS` object via the `explained_variance_` attribute. 

```
In [16]:pcaUS.explained_variance_
```

```
Out[16]:array([2.5309,1.01,0.3638,0.177])
```

The proportion of variance explained by each principal component (PVE) is stored as `explained_variance_ratio_` : 

```
In [17]:pcaUS.explained_variance_ratio_
```

```
Out[17]:array([0.6201,0.2474,0.0891,0.0434])
```

We see that the first principal component explains 62.0% of the variance in the data, the next principal component explains 24.7% of the variance, and so forth. We can plot the PVE explained by each component, as well as the cumulative PVE. We first plot the proportion of variance explained. 

```
In [18]:%%capture
fig,axes=plt.subplots(1,2,figsize=(15,6))
ticks=np.arange(pcaUS.n_components_)+1
ax=axes[0]
ax.plot(ticks,
pcaUS.explained_variance_ratio_ ,
marker='o')
```

12.5 Lab: Unsupervised Learning 

539 

```
ax.set_xlabel('PrincipalComponent');
ax.set_ylabel('ProportionofVarianceExplained')
ax.set_ylim([0,1])
ax.set_xticks(ticks)
```

Notice the use of `%%capture` , which suppresses the displaying of the partially completed figure. 

```
In [19]:ax=axes[1]
ax.plot(ticks,
pcaUS.explained_variance_ratio_.cumsum(),
marker='o')
ax.set_xlabel('PrincipalComponent')
ax.set_ylabel('CumulativeProportionofVarianceExplained')
ax.set_ylim([0,1])
ax.set_xticks(ticks)
fig
```

The result is similar to that shown in Figure 12.3. Note that the method `cumsum()` computes the cumulative sum of the elements of a numeric vector. `cumsum()` For instance: 

```
In [20]:a=np.array([1,2,8,-3])
np.cumsum(a)
```

```
Out[20]:array([1,3,11,8])
```

---
layout: default
title: "index"
---

# _12.5.2 Matrix Completion_ 

We now re-create the analysis carried out on the `USArrests` data in Section 12.3. 

We saw in Section 12.2.2 that solving the optimization problem (12.6) on a centered data matrix **X** is equivalent to computing the first _M_ principal components of the data. We use our scaled and centered `USArrests` data as **X** below. The _singular value decomposition_ (SVD) is a general algorithm singular for solving (12.6). 

value decomposition `svd()` 

```
In [21]:X=USArrests_scaled
U,D,V=np.linalg.svd(X,full_matrices=False)
U.shape,D.shape,V.shape
```

```
Out[21]:((50,4),(4,),(4,4))
```

The `np.linalg.svd()` function returns three components, `U` , `D` and `V` . The `np.linalg.` matrix `V` is equivalent to the loading matrix from principal components (up `svd()` to an unimportant sign flip). Using the `full_matrices=False` option ensures that for a tall matrix the shape of `U` is the same as the shape of `X` . 

```
In [22]:V
```

```
Out[22]:array([[-0.53589947,-0.58318363,-0.27819087,-0.54343209],
[0.41818087,0.1879856,-0.87280619,-0.16731864],
[-0.34123273,-0.26814843,-0.37801579,0.81777791],
[0.6492278,-0.74340748,0.13387773,0.08902432]])
```

540 12. Unsupervised Learning 

```
In [23]:pcaUS.components_
```

```
Out[23]:array([[0.53589947,0.58318363,0.27819087,0.54343209],
[0.41818087,0.1879856,-0.87280619,-0.16731864],
[-0.34123273,-0.26814843,-0.37801579,0.81777791],
[0.6492278,-0.74340748,0.13387773,0.08902432]])
```

The matrix `U` corresponds to a _standardized_ version of the PCA score matrix (each column standardized to have sum-of-squares one). If we multiply each column of `U` by the corresponding element of `D` , we recover the PCA scores exactly (up to a meaningless sign flip). 

```
In [24]:(U*D[None,:])[:3]
```

```
Out[24]:array([[-0.9856,1.1334,-0.4443,0.1563],
[-1.9501,1.0732,2.04,-0.4386],
[-1.7632,-0.746,0.0548,-0.8347]])
```

```
In [25]:scores[:3]
```

```
Out[25]:array([[0.9856,-1.1334,-0.4443,0.1563],
[1.9501,-1.0732,2.04,-0.4386],
[1.7632,0.746,0.0548,-0.8347]])
```

While it would be possible to carry out this lab using the `PCA()` estimator, here we use the `np.linalg.svd()` function in order to illustrate its use. 

We now omit 20 entries in the 50 _×_ 4 data matrix at random. We do so by first selecting 20 rows (states) at random, and then selecting one of the four entries in each row at random. This ensures that every row has at least three observed values. 

```
In [26]:n_omit=20
np.random.seed(15)
r_idx=np.random.choice(np.arange(X.shape[0]),
n_omit,
replace=False)
c_idx=np.random.choice(np.arange(X.shape[1]),
n_omit,
replace=True)
Xna=X.copy()
Xna[r_idx,c_idx]=np.nan
```

Here the array `r_idx` contains 20 integers from 0 to 49; this represents the states (rows of `X` ) that are selected to contain missing values. And `c_idx` contains 20 integers from 0 to 3, representing the features (columns in `X` ) that contain the missing values for each of the selected states. 

We now write some code to implement Algorithm 12.1. We first write a function that takes in a matrix, and returns an approximation to the matrix using the `svd()` function. This will be needed in Step 2 of Algorithm 12.1. 

```
In [27]:deflow_rank(X,M=1):
U,D,V=np.linalg.svd(X)
L=U[:,:M]*D[None,:M]
returnL.dot(V[:M])
```

12.5 Lab: Unsupervised Learning 541 

To conduct Step 1 of the algorithm, we initialize `Xhat` — this is **X**[˜] in Algorithm 12.1 — by replacing the missing values with the column means of the non-missing entries. These are stored in `Xbar` below after running `np.nanmean()` over the row axis. We make a copy so that when we assign `np.nanmean()` values to `Xhat` below we do not also overwrite the values in `Xna` . 

```
In [28]:Xhat=Xna.copy()
Xbar=np.nanmean(Xhat,axis=0)
Xhat[r_idx,c_idx]=Xbar[c_idx]
```

Before we begin Step 2, we set ourselves up to measure the progress of our iterations: 

```
In [29]:thresh=1e-7
```

`rel_err = 1 count = 0 ismiss = np.isnan(Xna) mssold = np.mean(Xhat[` _∼_ `ismiss]**2) mss0 = np.mean(Xna[` _∼_ `ismiss]**2)` 

Here `ismiss` is a logical matrix with the same dimensions as `Xna` ; a given element is `True` if the corresponding matrix element is missing. The notation _∼_ `ismiss` negates this boolean vector. This is useful because it allows us to access both the missing and non-missing entries. We store the mean of the squared non-missing elements in `mss0` . We store the mean squared error of the non-missing elements of the old version of `Xhat` in `mssold` (which currently agrees with `mss0` ). We plan to store the mean squared error of the non-missing elements of the current version of `Xhat` in `mss` , and will then iterate Step 2 of Algorithm 12.1 until the _relative error_ , defined as `(mssold - mss) / mss0` , falls below `thresh = 1e-7` .[9] 

In Step 2(a) of Algorithm 12.1, we approximate `Xhat` using `low_rank()` ; we call this `Xapp` . In Step 2(b), we use `Xapp` to update the estimates for elements in `Xhat` that are missing in `Xna` . Finally, in Step 2(c), we compute the relative error. These three steps are contained in the following `while` loop: 

**`In [30]:`** `while rel_err > thresh: count += 1 # Step 2(a) Xapp = low_rank(Xhat, M=1) # Step 2(b) Xhat[ismiss] = Xapp[ismiss] # Step 2(c) mss = np.mean(((Xna - Xapp)[` _∼_ `ismiss])**2) rel_err = (mssold - mss) / mss0 mssold = mss print("Iteration: {0}, MSS:{1:.3f}, Rel.Err {2:.2e}" .format(count, mss, rel_err))` 

> 9Algorithm 12.1 tells us to iterate Step 2 until (12.14) is no longer decreasing. Determining whether (12.14) is decreasing requires us only to keep track of `mssold - mss` . However, in practice, we keep track of `(mssold - mss) / mss0` instead: this makes it so that the number of iterations required for Algorithm 12.1 to converge does not depend on whether we multiplied the raw data **X** by a constant factor. 

542 12. Unsupervised Learning 

```
Iteration:1,MSS:0.395,Rel.Err5.99e-01
Iteration:2,MSS:0.382,Rel.Err1.33e-02
Iteration:3,MSS:0.381,Rel.Err1.44e-03
Iteration:4,MSS:0.381,Rel.Err1.79e-04
Iteration:5,MSS:0.381,Rel.Err2.58e-05
Iteration:6,MSS:0.381,Rel.Err4.22e-06
Iteration:7,MSS:0.381,Rel.Err7.65e-07
Iteration:8,MSS:0.381,Rel.Err1.48e-07
Iteration:9,MSS:0.381,Rel.Err2.95e-08
```

We see that after eight iterations, the relative error has fallen below `thresh = 1e-7` , and so the algorithm terminates. When this happens, the mean squared error of the non-missing elements equals 0.381. 

Finally, we compute the correlation between the 20 imputed values and the actual values: 

```
In [31]:np.corrcoef(Xapp[ismiss],X[ismiss])[0,1]
```

```
Out[31]:0.711
```

In this lab, we implemented Algorithm 12.1 ourselves for didactic purposes. However, a reader who wishes to apply matrix completion to their data might look to more specialized `Python` implementations. 

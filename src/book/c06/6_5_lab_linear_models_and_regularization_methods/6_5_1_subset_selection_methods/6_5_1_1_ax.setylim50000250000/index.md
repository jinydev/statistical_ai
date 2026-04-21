---
layout: default
title: "index"
---

# `ax.set_ylim([50000,250000]);` 

Notice the expression `None` in `Y[:,None]` above. This adds an axis (dimension) to the one-dimensional array `Y` , which allows it to be recycled when subtracted from the two-dimensional `Yhat_in` . 

We are now ready to use cross-validation to estimate test error along the model path. We must use _only the training observations_ to perform all aspects of model-fitting — including variable selection. Therefore, the determination of which model of a given size is best must be made using _only the training observations_ in each training fold. This point is subtle but important. If the full data set is used to select the best subset at each step, then the validation set errors and cross-validation errors that we obtain will not be accurate estimates of the test error. 

We now compute the cross-validated predicted values using 5-fold crossvalidation. 

```
In [14]:K=5
kfold=skm.KFold(K,
random_state=0,
shuffle=True)
Yhat_cv=skm.cross_val_predict(full_path,
Hitters,
Y,
cv=kfold)
Yhat_cv.shape
```

```
Out[14]:(263,20)
```

The prediction matrix `Yhat_cv` is the same shape as `Yhat_in` ; the difference is that the predictions in each row, corresponding to a particular sample index, were made from models fit on a training fold that did not include that row. 

```
skm.KFold()
skm.cross_
val_predict()
```

At each model along the path, we compute the $\text{MSE}$ in each of the crossvalidation folds. These we will average to get the mean MSE, and can also use the individual values to compute a crude estimate of the standard error of the mean.[^9] Hence we must know the test indices for each cross-validation split. This can be found by using the `split()` method of `kfold` . Because we fixed the random state above, whenever we split any array with the same number of rows as Y we recover the same training and test indices, though we simply ignore the training indices below. 

```
In [15]:cv_mse=[]
fortrain_idx,test_idxinkfold.split(Y):
errors=(Yhat_cv[test_idx]-Y[test_idx,None])**2
cv_mse.append(errors.mean(0))#columnmeans
cv_mse=np.array(cv_mse).T
cv_mse.shape
```

```
Out[15]:(20,5)
```

[^9]: The estimate is crude because the five error estimates are based on overlapping training sets, and hence are not independent. 

272 6. Linear Model Selection and Regularization 

We now add the cross-validation error estimates to our $\text{MSE}$ plot. We include the mean error across the five folds, and the estimate of the standard error of the mean. 

```
In [16]:ax.errorbar(np.arange(n_steps),
cv_mse.mean(1),
cv_mse.std(1)/np.sqrt(K),
label='Cross-validated',
c='r')#colorred
ax.set_ylim([50000,250000])
ax.legend()
mse_fig
```

To repeat the above using the validation set approach, we simply change our `cv` argument to a validation set: one random split of the data into a test and training. We choose a test size of 20%, similar to the size of each test set in 5-fold cross-validation. 

```
In [17]:validation=skm.ShuffleSplit(n_splits=1,
test_size=0.2,
random_state=0)
fortrain_idx,test_idxinvalidation.split(Y):
full_path.fit(Hitters.iloc[train_idx],
Y[train_idx])
Yhat_val=full_path.predict(Hitters.iloc[test_idx])
errors=(Yhat_val-Y[test_idx,None])**2
validation_mse=errors.mean(0)
```

```
skm.Shuffle
Split()
```

As for the in-sample $\text{MSE}$ case, the validation set approach does not provide standard errors. 

```
In [18]:ax.plot(np.arange(n_steps),
validation_mse ,
'b--',#colorblue,brokenline
label='Validation')
ax.set_xticks(np.arange(n_steps)[::2])
ax.set_ylim([50000,250000])
ax.legend()
mse_fig
```

Best Subset Selection 

Forward stepwise is a _greedy_ selection procedure; at each step it augments the current set by including one additional variable. We now apply best subset selection to the `Hitters` data, which for every subset size, searches for the best set of predictors. 

We will use a package called `l0bnb` to perform best subset selection. Instead of constraining the subset to be a given size, this package produces a path of solutions using the subset size as a penalty rather than a constraint. Although the distinction is subtle, the difference comes when we crossvalidate. 

```
In [19]:D=design.fit_transform(Hitters)
D=D.drop('intercept',axis=1)
X=np.asarray(D)
```

6.5 Lab: Linear Models and Regularization Methods 273 

Here we excluded the first column corresponding to the intercept, as `l0bnb` will fit the intercept separately. We can find a path using the `fit_path()` function. 

```
In [20]:path=fit_path(X,
```

```
Y,
max_nonzeros=X.shape[1])
```

The function `fit_path()` returns a list whose values include the fitted coefficients as `B` , an intercept as `B0` , as well as a few other attributes related to the particular path algorithm used. Such details are beyond the scope of this book. 

```
In [21]:path[3]
```

```
Out[21]:{'B':array([0.,3.254844,0.,0.,0.,
0.,0.,0.,0.,0.,
0.,0.677753,0.,0.,0.,
0.,0.,0.,0.]),
'B0':-38.98216739555494,
'lambda_0':0.011416248027450194,
'M':0.5829861733382011,
'Time_exceeded':False}
```

In the example above, we see that at the fourth step in the path, we have two nonzero coefficients in `'B'` , corresponding to the value 0 _._ 114 for the penalty parameter `lambda_0` . We could make predictions using this sequence of fits on a validation set as a function of `lambda_0` , or with more work using cross-validation. 

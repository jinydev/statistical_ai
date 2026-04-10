---
layout: default
title: "index"
---

# **`Out[9]:`** `24.2315` 

The arguments to `cross_validate()` are as follows: an object with the appropriate `fit()` , `predict()` , and `score()` methods, an array of features `X` and a response `Y` . We also included an additional argument `cv` to `cross_validate()` ; specifying an integer _K_ results in _K_ -fold cross-validation. We have provided a value corresponding to the total number of observations, which results in leave-one-out cross-validation (LOOCV). The `cross_validate()` func- `cross_` tion produces a dictionary with several components; we simply want the `validate()` cross-validated test score here (MSE), which is estimated to be 24.23. We can repeat this procedure for increasingly complex polynomial fits. To automate the process, we again use a for loop which iteratively fits polynomial regressions of degree 1 to 5, computes the associated crossvalidation error, and stores it in the _i_ th element of the vector `cv_error` . The variable `d` in the for loop corresponds to the degree of the polynomial. We begin by initializing the vector. This command may take a couple of seconds to run. 

```
In [10]:cv_error=np.zeros(5)
H=np.array(Auto['horsepower'])
M=sklearn_sm(sm.OLS)
fori,dinenumerate(range(1,6)):
X=np.power.outer(H,np.arange(d+1))
M_CV=cross_validate(M,
X,
Y,
cv=Auto.shape[0])
cv_error[i]=np.mean(M_CV['test_score'])
cv_error
```

```
Out[10]:array([24.2315,19.2482,19.3350,19.4244,19.0332])
```

As in Figure 5.4, we see a sharp drop in the estimated test MSE between the linear and quadratic fits, but then no clear improvement from using higher-degree polynomials. 

5.3 Lab: Cross-Validation and the Bootstrap 219 

Above we introduced the `outer()` method of the `np.power()` function. `.outer()` The `outer()` method is applied to an operation that has two arguments, such as `add()` , `min()` , or `power()` . It has two arrays as arguments, and then forms a larger array where the operation is applied to each pair of elements of the two arrays. 

```
np.power()
```

```
In [11]:A=np.array([3,5,9])
B=np.array([2,4])
np.add.outer(A,B)
```

```
Out[11]:array([[5,7],
[7,9],
[11,13]])
```

In the CV example above, we used _K_ = _n_ , but of course we can also use _K < n_ . The code is very similar to the above (and is significantly faster). Here we use `KFold()` to partition the data into _K_ = 10 random groups. We `KFold()` use `random_state` to set a random seed and initialize a vector `cv_error` in which we will store the CV errors corresponding to the polynomial fits of degrees one to five. 

```
In [12]:cv_error=np.zeros(5)
cv=KFold(n_splits=10,
shuffle=True,
random_state=0)#usesamesplitsforeachdegree
fori,dinenumerate(range(1,6)):
X=np.power.outer(H,np.arange(d+1))
M_CV=cross_validate(M,
X,
Y,
cv=cv)
cv_error[i]=np.mean(M_CV['test_score'])
cv_error
```

```
Out[12]:array([24.2077,19.1853,19.2763,19.4785,19.1372])
```

Notice that the computation time is much shorter than that of LOOCV. (In principle, the computation time for LOOCV for a least squares linear model should be faster than for _K_ -fold CV, due to the availability of the formula (5.2) for LOOCV; however, the generic `cross_validate()` function does not make use of this formula.) We still see little evidence that using cubic or higher-degree polynomial terms leads to a lower test error than simply using a quadratic fit. 

The `cross_validate()` function is flexible and can take different splitting mechanisms as an argument. For instance, one can use the `ShuffleSplit() Shuffle` funtion to implement the validation set approach just as easily as K-fold `Split()` cross-validation. 

```
In [13]:validation=ShuffleSplit(n_splits=1,
test_size=196,
random_state=0)
results=cross_validate(hp_model,
Auto.drop(['mpg'],axis=1),
Auto['mpg'],
cv=validation);
results['test_score']
```

220 5. Resampling Methods 

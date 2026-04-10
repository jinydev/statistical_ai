---
layout: default
title: "index"
---

# Fast Cross-Validation for Solution Paths 

The ridge, lasso, and elastic net can be efficiently fit along a sequence of _λ_ values, creating what is known as a _solution path_ or _regularization path_ . Hence there is specialized code to fit such paths, and to choose a suitable value of _λ_ using cross-validation. Even with identical splits the results will not agree _exactly_ with our `grid` above because the standardization of each feature in `grid` is carried out on each fold, while in `pipeCV` below it is carried out only once. Nevertheless, the results are similar as the normalization is relatively stable across folds. 

```
In [37]:ridgeCV=skl.ElasticNetCV(alphas=lambdas,
l1_ratio=0,
cv=kfold)
pipeCV=Pipeline(steps=[('scaler',scaler),
```

6. Linear Model Selection and Regularization 

278 

```
('ridge',ridgeCV)])
```

```
pipeCV.fit(X,Y)
```

Let’s produce a plot again of the cross-validation error to see that it is similar to using `skm.GridSearchCV` . 

```
In [38]:tuned_ridge=pipeCV.named_steps['ridge']
ridgeCV_fig ,ax=subplots(figsize=(8,8))
ax.errorbar(-np.log(lambdas),
tuned_ridge.mse_path_.mean(1),
yerr=tuned_ridge.mse_path_.std(1)/np.sqrt(K))
ax.axvline(-np.log(tuned_ridge.alpha_),c='k',ls='--')
ax.set_ylim([50000,250000])
ax.set_xlabel('$-\log(\lambda)$',fontsize=20)
ax.set_ylabel('Cross-validatedMSE',fontsize=20);
```

We see that the value of _λ_ that results in the smallest cross-validation error is 1.19e-02, available as the value `tuned_ridge.alpha_` . What is the test $\text{MSE}$ associated with this value of _λ_ ? 

```
In [39]:np.min(tuned_ridge.mse_path_.mean(1))
```

```
Out[39]:115526.71
```

This represents a further improvement over the test $\text{MSE}$ that we got using _λ_ = 4. Finally, `tuned_ridge.coef_` has the coefficients fit on the entire data set at this value of _λ_ . 

```
In [40]:tuned_ridge.coef_
```

```
Out[40]:array([-222.80877051,238.77246614,3.21103754,-2.93050845,
3.64888723,108.90953869,-50.81896152,-105.15731984,
122.00714801,57.1859509,210.35170348,118.05683748,
-150.21959435,30.36634231,-61.62459095,77.73832472,
40.07350744,-25.02151514,-13.68429544])
```

As expected, none of the coefficients are zero—ridge regression does not perform variable selection! 

Evaluating Test Error of Cross-Validated Ridge 

Choosing _λ_ using cross-validation provides a single regression estimator, similar to fitting a linear regression model as we saw in Chapter 3. It is therefore reasonable to estimate what its test error is. We run into a problem here in that cross-validation will have _touched_ all of its data in choosing _λ_ , hence we have no further data to estimate test error. A compromise is to do an initial split of the data into two disjoint sets: a training set and a test set. We then fit a cross-validation tuned ridge regression on the training set, and evaluate its performance on the test set. We might call this cross-validation nested within the validation set approach. A priori there is no reason to use half of the data for each of the two sets in validation. Below, we use 75% for training and 25% for test, with the estimator being ridge regression tuned using 5-fold cross-validation. This can be achieved in code as follows: 

6.5 Lab: Linear Models and Regularization Methods 

279 

```
In [41]:outer_valid=skm.ShuffleSplit(n_splits=1,
test_size=0.25,
random_state=1)
inner_cv=skm.KFold(n_splits=5,
shuffle=True,
random_state=2)
ridgeCV=skl.ElasticNetCV(alphas=lambdas,
l1_ratio=0,
cv=inner_cv)
pipeCV=Pipeline(steps=[('scaler',scaler),
('ridge',ridgeCV)]);
In [42]:results=skm.cross_validate(pipeCV,
X,
Y,
cv=outer_valid ,
scoring='neg_mean_squared_error')
-results['test_score']
```

```
Out[42]:array([132393.84])
```

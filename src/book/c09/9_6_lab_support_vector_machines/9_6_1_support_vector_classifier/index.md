---
layout: default
title: "index"
---

# _9.6.1 Support Vector Classifier_ 

We now use the `SupportVectorClassifier()` function (abbreviated `SVC()` ) `SupportVector` from `sklearn` to fit the support vector classifier for a given value of the `Classifier()` parameter `C` . The `C` argument allows us to specify the cost of a violation to the margin. When the `cost` argument is small, then the margins will be wide and many support vectors will be on the margin or will violate the margin. When the `C` argument is large, then the margins will be narrow and there will be few support vectors on the margin or violating the margin. 

Here we demonstrate the use of `SVC()` on a two-dimensional example, so that we can plot the resulting decision boundary. We begin by generating the observations, which belong to two classes, and checking whether the classes are linearly separable. 

```
In [4]:rng=np.random.default_rng(1)
X=rng.standard_normal((50,2))
y=np.array([-1]*25+[1]*25)
X[y==1]+=1
fig,ax=subplots(figsize=(8,8))
ax.scatter(X[:,0],
X[:,1],
c=y,
cmap=cm.coolwarm);
```

They are not. We now fit the classifier. 

```
In [5]:svm_linear=SVC(C=10,kernel='linear')
svm_linear.fit(X,y)
```

```
Out[5]:SVC(C=10,kernel='linear')
```

The support vector classifier with two features can be visualized by plotting values of its _decision function_ . We have included a function for this in decision the `ISLP` package (inspired by a similar example in the `sklearn` docs). function 

388 9. Support Vector Machines 

```
In [6]:fig,ax=subplots(figsize=(8,8))
plot_svm(X,
y,
svm_linear,
ax=ax)
```

The decision boundary between the two classes is linear (because we used the argument `kernel='linear'` ). The support vectors are marked with `+` and the remaining observations are plotted as circles. What if we instead used a smaller value of the cost parameter? 

```
In [7]:svm_linear_small=SVC(C=0.1,kernel='linear')
svm_linear_small.fit(X,y)
fig,ax=subplots(figsize=(8,8))
plot_svm(X,
y,
svm_linear_small ,
ax=ax)
```

With a smaller value of the cost parameter, we obtain a larger number of support vectors, because the margin is now wider. For linear kernels, we can extract the coefficients of the linear decision boundary as follows: 

```
In [8]:svm_linear.coef_
```

```
Out[8]:array([[1.173,0.7734]])
```

Since the support vector machine is an estimator in `sklearn` , we can use the usual machinery to tune it. 

```
In [9]:kfold=skm.KFold(5,
random_state=0,
shuffle=True)
grid=skm.GridSearchCV(svm_linear,
{'C':[0.001,0.01,0.1,1,5,10,100]},
refit=True,
cv=kfold,
scoring='accuracy')
grid.fit(X,y)
grid.best_params_
```

```
Out[9]:{'C':1}
```

We can easily access the cross-validation errors for each of these models in `grid.cv_results_` . This prints out a lot of detail, so we extract the accuracy results only. 

```
In [10]:grid.cv_results_[('mean_test_score')]
```

```
Out[10]:array([0.46,0.46,0.72,0.74,0.74,0.74,0.74])
```

We see that `C=1` results in the highest cross-validation accuracy of 0.74, though the accuracy is the same for several values of `C` . The classifier `grid.best_estimator_` can be used to predict the class label on a set of test observations. Let’s generate a test data set. 

9.6 Lab: Support Vector Machines 

389 

```
In [11]:X_test=rng.standard_normal((20,2))
y_test=np.array([-1]*10+[1]*10)
X_test[y_test==1]+=1
```

Now we predict the class labels of these test observations. Here we use the best model selected by cross-validation in order to make the predictions. 

```
In [12]:best_=grid.best_estimator_
y_test_hat=best_.predict(X_test)
confusion_table(y_test_hat ,y_test)
```

```
Out[12]:Truth-11
Predicted
-184
126
```

Thus, with this value of `C` , 70% of the test observations are correctly classified. What if we had instead used `C=0.001` ? 

```
In [13]:svm_=SVC(C=0.001,
kernel='linear').fit(X,y)
y_test_hat=svm_.predict(X_test)
confusion_table(y_test_hat ,y_test)
```

```
Out[13]:Truth-11
Predicted
-120
1810
```

In this case 60% of test observations are correctly classified. We now consider a situation in which the two classes are linearly separable. Then we can find an optimal separating hyperplane using the `SVC()` estimator. We first further separate the two classes in our simulated data so that they are linearly separable: 

```
In [14]:X[y==1]+=1.9;
fig,ax=subplots(figsize=(8,8))
ax.scatter(X[:,0],X[:,1],c=y,cmap=cm.coolwarm);
```

Now the observations are just barely linearly separable. 

```
In [15]:svm_=SVC(C=1e5,kernel='linear').fit(X,y)
y_hat=svm_.predict(X)
confusion_table(y_hat,y)
```

```
Out[15]:Truth-11
Predicted
-1250
1025
```

We fit the support vector classifier and plot the resulting hyperplane, using a very large value of `C` so that no observations are misclassified. 

```
In [16]:fig,ax=subplots(figsize=(8,8))
plot_svm(X,
y,
svm_,
ax=ax)
```

390 9. Support Vector Machines 

Indeed no training errors were made and only three support vectors were used. In fact, the large value of `C` also means that these three support points are _on the margin_ , and define it. One may wonder how good the classifier could be on test data that depends on only three data points! We now try a smaller value of `C` . 

```
In [17]:svm_=SVC(C=0.1,kernel='linear').fit(X,y)
y_hat=svm_.predict(X)
confusion_table(y_hat,y)
```

```
Out[17]:Truth-11
Predicted
-1250
1025
```

Using `C=0.1` , we again do not misclassify any training observations, but we also obtain a much wider margin and make use of twelve support vectors. These jointly define the orientation of the decision boundary, and since there are more of them, it is more stable. It seems possible that this model will perform better on test data than the model with `C=1e5` (and indeed, a simple experiment with a large test set would bear this out). 

```
In [18]:fig,ax=subplots(figsize=(8,8))
plot_svm(X,
y,
svm_,
ax=ax)
```

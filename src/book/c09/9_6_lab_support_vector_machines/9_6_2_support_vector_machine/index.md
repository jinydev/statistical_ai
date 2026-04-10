---
layout: default
title: "index"
---

# _9.6.2 Support Vector Machine_ 

In order to fit an SVM using a non-linear kernel, we once again use the `SVC()` estimator. However, now we use a different value of the parameter `kernel` . To fit an SVM with a polynomial kernel we use `kernel="poly"` , and to fit an SVM with a radial kernel we use `kernel="rbf"` . In the former case we also use the `degree` argument to specify a degree for the polynomial kernel (this is _d_ in (9.22)), and in the latter case we use `gamma` to specify a value of _γ_ for the radial basis kernel (9.24). 

We first generate some data with a non-linear class boundary, as follows: 

```
In [19]:X=rng.standard_normal((200,2))
X[:100]+=2
X[100:150]-=2
y=np.array([1]*150+[2]*50)
```

Plotting the data makes it clear that the class boundary is indeed nonlinear. 

```
In [20]:fig,ax=subplots(figsize=(8,8))
ax.scatter(X[:,0],
X[:,1],
c=y,
cmap=cm.coolwarm)
```

```
Out[20]:<matplotlib.collections.PathCollectionat0x7faa9ba52eb0 >
```

9.6 Lab: Support Vector Machines 391 

The data is randomly split into training and testing groups. We then fit the training data using the `SVC()` estimator with a radial kernel and _γ_ = 1: 

```
In [21]:(X_train,
X_test,
y_train,
y_test)=skm.train_test_split(X,
y,
test_size=0.5,
random_state=0)
svm_rbf=SVC(kernel="rbf",gamma=1,C=1)
svm_rbf.fit(X_train,y_train)
```

The plot shows that the resulting SVM has a decidedly non-linear boundary. 

```
In [22]:fig,ax=subplots(figsize=(8,8))
plot_svm(X_train,
y_train,
svm_rbf,
ax=ax)
```

We can see from the figure that there are a fair number of training errors in this SVM fit. If we increase the value of `C` , we can reduce the number of training errors. However, this comes at the price of a more irregular decision boundary that seems to be at risk of overfitting the data. 

```
In [23]:svm_rbf=SVC(kernel="rbf",gamma=1,C=1e5)
svm_rbf.fit(X_train,y_train)
fig,ax=subplots(figsize=(8,8))
plot_svm(X_train,
y_train,
svm_rbf,
ax=ax)
```

We can perform cross-validation using `skm.GridSearchCV()` to select the best choice of _γ_ and `C` for an SVM with a radial kernel: 

```
In [24]:kfold=skm.KFold(5,
random_state=0,
shuffle=True)
grid=skm.GridSearchCV(svm_rbf,
{'C':[0.1,1,10,100,1000],
'gamma':[0.5,1,2,3,4]},
refit=True,
cv=kfold,
scoring='accuracy');
grid.fit(X_train,y_train)
grid.best_params_
```

```
Out[24]:{'C':100,'gamma':1}
```

The best choice of parameters under five-fold CV is achieved at `C=1` and `gamma=0.5` , though several other values also achieve the same value. 

```
In [25]:best_svm=grid.best_estimator_
fig,ax=subplots(figsize=(8,8))
plot_svm(X_train,
```

9. Support Vector Machines 

392 

```
y_train,
best_svm,
ax=ax)
y_hat_test=best_svm.predict(X_test)
confusion_table(y_hat_test ,y_test)
```

```
Out[25]:Truth12
Predicted
1696
2619
```

With these parameters, 12% of test observations are misclassified by this SVM. 

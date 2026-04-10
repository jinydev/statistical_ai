---
layout: default
title: "index"
---

# _9.6.4 SVM with Multiple Classes_ 

If the response is a factor containing more than two levels, then the `SVC()` function will perform multi-class classification using either the one-versusone approach (when `decision_function_shape=='ovo'` ) or one-versus-rest[4] (when `decision_function_shape=='ovr'` ). We explore that setting briefly here by generating a third class of observations. 

```
In [30]:rng=np.random.default_rng(123)
X=np.vstack([X,rng.standard_normal((50,2))])
y=np.hstack([y,[0]*50])
X[y==0,1]+=2
fig,ax=subplots(figsize=(8,8))
ax.scatter(X[:,0],X[:,1],c=y,cmap=cm.coolwarm);
```

> 4One-versus-rest is also known as one-versus-all. 

394 9. Support Vector Machines 

We now fit an SVM to the data: 

```
In [31]:svm_rbf_3=SVC(kernel="rbf",
C=10,
gamma=1,
decision_function_shape='ovo');
svm_rbf_3.fit(X,y)
fig,ax=subplots(figsize=(8,8))
plot_svm(X,
y,
svm_rbf_3,
scatter_cmap=cm.tab10,
ax=ax)
```

The `sklearn.svm` library can also be used to perform support vector regression with a numerical response using the estimator `SupportVectorRegression()` . 

```
SupportVector
Regression()
```

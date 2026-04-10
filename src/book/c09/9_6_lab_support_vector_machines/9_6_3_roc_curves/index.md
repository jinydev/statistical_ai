---
layout: default
title: "index"
---

# _9.6.3 ROC Curves_ 

SVMs and support vector classifiers output class labels for each observation. However, it is also possible to obtain _fitted values_ for each observation, which are the numerical scores used to obtain the class labels. For instance, in the case of a support vector classifier, the fitted value for an observation _X_ = ( _X_ 1 _, X_ 2 _, . . . , Xp_ ) _[T]_ takes the form _β_[ˆ] 0 + _β_[ˆ] 1 _X_ 1 + _β_[ˆ] 2 _X_ 2 + _. . ._ + _β_[ˆ] _pXp_ . For an SVM with a non-linear kernel, the equation that yields the fitted value is given in (9.23). The sign of the fitted value determines on which side of the decision boundary the observation lies. Therefore, the relationship between the fitted value and the class prediction for a given observation is simple: if the fitted value exceeds zero then the observation is assigned to one class, and if it is less than zero then it is assigned to the other. By changing this threshold from zero to some positive value, we skew the classifications in favor of one class versus the other. By considering a range of these thresholds, positive and negative, we produce the ingredients for a ROC plot. We can access these values by calling the `decision_function() .function_` method of a fitted SVM estimator. `decision()` 

```
decision()
```

The function `ROCCurveDisplay.from_estimator()` (which we have abbreviated to `roc_curve()` ) will produce a plot of a ROC curve. It takes a fitted `roc_curve()` estimator as its first argument, followed by a model matrix _X_ and labels _y_ . The argument `name` is used in the legend, while `color` is used for the color of the line. Results are plotted on our axis object `ax` . 

```
In [26]:fig,ax=subplots(figsize=(8,8))
roc_curve(best_svm,
X_train,
y_train,
name='Training',
color='r',
ax=ax);
```

In this example, the SVM appears to provide accurate predictions. By increasing _γ_ we can produce a more flexible fit and generate further improvements in accuracy. 

```
In [27]:svm_flex=SVC(kernel="rbf",
gamma=50,
```

9.6 Lab: Support Vector Machines 393 

```
C=1)
svm_flex.fit(X_train,y_train)
fig,ax=subplots(figsize=(8,8))
roc_curve(svm_flex,
X_train,
y_train,
name='Training$\gamma=50$',
color='r',
ax=ax);
```

However, these ROC curves are all on the training data. We are really more interested in the level of prediction accuracy on the test data. When we compute the ROC curves on the test data, the model with _γ_ = 0 _._ 5 appears to provide the most accurate results. 

```
In [28]:
```

```
roc_curve(svm_flex,
X_test,
y_test,
name='Test$\gamma=50$',
color='b',
ax=ax)
fig;
```

Let’s look at our tuned SVM. 

```
In [29]:fig,ax=subplots(figsize=(8,8))
for(X_,y_,c,name)inzip(
(X_train,X_test),
(y_train,y_test),
('r','b'),
('CVtunedontraining',
'CVtunedontest')):
roc_curve(best_svm,
X_,
y_,
name=name,
ax=ax,
color=c)
```

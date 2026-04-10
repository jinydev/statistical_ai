---
layout: default
title: "index"
---

# **`Out[6]:`** `0.7275` 

With only the default arguments, the training error rate is 21%. For classification trees, we can access the value of the deviance using `log_loss()`

$$
D = -2 \sum_m \sum_k n_{mk} \log \hat{p}_{mk}
$$

where _nmk_ is the number of observations in the _m_ th terminal node that belong to the _k_ th class. 

```
In [7]:resid_dev=np.sum(log_loss(High,clf.predict_proba(X)))
resid_dev
```

```
Out[7]:0.4711
```

This is closely related to the _entropy_ , defined in (8.7). A small deviance indicates a tree that provides a good fit to the (training) data. 

One of the most attractive properties of trees is that they can be graphically displayed. Here we use the `plot()` function to display the tree structure (not shown here). 

```
In [8]:ax=subplots(figsize=(12,12))[1]
plot_tree(clf,
feature_names=feature_names ,
ax=ax);
```

The most important indicator of `Sales` appears to be `ShelveLoc` . 

We can see a text representation of the tree using `export_text()` , which `export_text()` displays the split criterion (e.g. `Price <= 92.5` ) for each branch. For leaf nodes it shows the overall prediction ( `Yes` or `No` ). We can also see the number of observations in that leaf that take on values of `Yes` and `No` by specifying `show_weights=True` . 

```
In [9]:print(export_text(clf,
```

```
feature_names=feature_names ,
show_weights=True))
```

```
Out[9]:|---ShelveLoc[Good]<=0.50
||---Price<=92.50
|||---Income<=57.00
||||---weights:[7.00,3.00]class:No
|||---Income>57.00
||||---weights:[7.00,29.00]class:Yes
||---Price>92.50
|||---Advertising<=13.50
||||---weights:[183.00,41.00]class:No
|||---Advertising>13.50
||||---weights:[20.00,25.00]class:Yes
|---ShelveLoc[Good]>0.50
||---Price<=135.00
|||---US[Yes]<=0.50
||||---weights:[6.00,11.00]class:Yes
|||---US[Yes]>0.50
||||---weights:[2.00,49.00]class:Yes
||---Price>135.00
|||---Income<=46.00
||||---weights:[6.00,0.00]class:No
|||---Income>46.00
||||---weights:[5.00,6.00]class:Yes
```

8.3 Lab: Tree-Based Methods 357 

In order to properly evaluate the performance of a classification tree on these data, we must estimate the test error rather than simply computing the training error. We split the observations into a training set and a test set, build the tree using the training set, and evaluate its performance on the test data. This pattern is similar to that in Chapter 6, with the linear models replaced here by decision trees — the code for validation is almost identical. This approach leads to correct predictions for 68.5% of the locations in the test data set. 

```
In [10]:validation=skm.ShuffleSplit(n_splits=1,
test_size=200,
random_state=0)
results=skm.cross_validate(clf,
D,
High,
cv=validation)
results['test_score']
```

```
Out[10]:array([0.685])
```

Next, we consider whether pruning the tree might lead to improved classification performance. We first split the data into a training and test set. We will use cross-validation to prune the tree on the training set, and then evaluate the performance of the pruned tree on the test set. 

```
In [11]:(X_train,
X_test,
High_train,
High_test)=skm.train_test_split(X,
High,
test_size=0.5,
random_state=0)
```

We first refit the full tree on the training set; here we do not set a `max_depth` parameter, since we will learn that through cross-validation. 

```
In [12]:clf=DTC(criterion='entropy',random_state=0)
clf.fit(X_train,High_train)
accuracy_score(High_test,clf.predict(X_test))
```

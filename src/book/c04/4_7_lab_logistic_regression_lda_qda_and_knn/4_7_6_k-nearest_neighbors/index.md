---
layout: default
title: "index"
---

# _4.7.6 K-Nearest Neighbors_ 

We will now perform KNN using the `KNeighborsClassifier()` function. This `KNeighbors` 

> 6There are two formulas for computing the sample variance of _n_ observations 1 _n_ 1 _n x_ 1 _, . . . , xn_ : _n_ � _i_ =1[(] _[x][i][−][x]_[¯][)][2][and] _n−_ 1 � _i_ =1[(] _[x][i][−][x]_[¯][)][2][where] _[x]_[¯][is][the][sample][mean.] In most cases the distinction is not important. 

```
Classifier()
```

4. Classification 

184 

function works similarly to the other model-fitting functions that we have encountered thus far. 

As is the case for LDA and QDA, we fit the classifier using the `fit` method. New predictions are formed using the `predict` method of the object returned by `fit()` . 

```
In [47]:knn1=KNeighborsClassifier(n_neighbors=1)
knn1.fit(X_train,L_train)
knn1_pred=knn1.predict(X_test)
confusion_table(knn1_pred,L_test)
```

```
Out[47]:TruthDownUp
Predicted
Down4358
Up6883
```

The results using $K$ = 1 are not very good, since only 50% of the observations are correctly predicted. Of course, it may be that $K$ = 1 results in an overly-flexible fit to the data. 

```
In [48]:(83+43)/252,np.mean(knn1_pred==L_test)
```

```
Out[48]:(0.5,0.5)
```

We repeat the analysis below using $K$ = 3. 

```
In [49]:knn3=KNeighborsClassifier(n_neighbors=3)
knn3_pred=knn3.fit(X_train,L_train).predict(X_test)
np.mean(knn3_pred==L_test)
```

```
Out[49]:0.532
```

The results have improved slightly. But increasing $K$ further provides no further improvements. It appears that for these data, and this train/test split, QDA gives the best results of the methods that we have examined so far. 

KNN does not perform well on the `Smarket` data, but it often does provide impressive results. As an example we will apply the KNN approach to the `Caravan` data set, which is part of the `ISLP` library. This data set includes 85 predictors that measure demographic characteristics for 5,822 individuals. The response variable is `Purchase` , which indicates whether or not a given individual purchases a caravan insurance policy. In this data set, only 6% of people purchased caravan insurance. 

```
In [50]:Caravan=load_data('Caravan')
Purchase=Caravan.Purchase
Purchase.value_counts()
```

```
Out[50]:No5474
Yes348
Name:Purchase,dtype:int64
```

The method `value_counts()` takes a `pd.Series` or `pd.DataFrame` and returns a `pd.Series` with the corresponding counts for each unique element. In this case `Purchase` has only `Yes` and `No` values and returns how many values of each there are. 

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 

185 

```
In [51]:348/5822
```

```
Out[51]:0.0598
```

Our features will include all columns except `Purchase` . 

```
In [52]:feature_df=Caravan.drop(columns=['Purchase'])
```

Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. Any variables that are on a large scale will have a much larger effect on the _distance_ between the observations, and hence on the KNN classifier, than variables that are on a small scale. For instance, imagine a data set that contains two variables, `salary` and `age` (measured in dollars and years, respectively). As far as KNN is concerned, a difference of 1,000 USD in salary is enormous compared to a difference of 50 years in age. Consequently, `salary` will drive the KNN classification results, and `age` will have almost no effect. This is contrary to our intuition that a salary difference of 1,000 USD is quite small compared to an age difference of 50 years. Furthermore, the importance of scale to the KNN classifier leads to another issue: if we measured `salary` in Japanese yen, or if we measured `age` in minutes, then we’d get quite different classification results from what we get if these two variables are measured in dollars and years. 

A good way to handle this problem is to _standardize_ the data so that all standardize variables are given a mean of zero and a standard deviation of one. Then all variables will be on a comparable scale. This is accomplished using the `StandardScaler()` transformation. 

```
Standard
In [53]:scaler=StandardScaler(with_mean=True,Scaler()
with_std=True,
copy=True)
```

The argument `with_mean` indicates whether or not we should subtract the mean, while `with_std` indicates whether or not we should scale the columns to have standard deviation of 1 or not. Finally, the argument `copy=True` indicates that we will always copy data, rather than trying to do calculations in place where possible. 

This transformation can be fit and then applied to arbitrary data. In the first line below, the parameters for the scaling are computed and stored in `scaler` , while the second line actually constructs the standardized set of features. 

```
In [54]:scaler.fit(feature_df)
X_std=scaler.transform(feature_df)
```

Now every column of `feature_std` below has a standard deviation of one and a mean of zero. 

```
In [55]:feature_std=pd.DataFrame(
X_std,
columns=feature_df.columns);
feature_std.std()
Out[55]:MOSTYPE1.000086
MAANTHUI1.000086
```

4. Classification 

186 

```
MGEMOMV1.000086
MGEMLEEF1.000086
MOSHOOFD1.000086
...
AZEILPL1.000086
APLEZIER1.000086
AFIETS1.000086
AINBOED1.000086
ABYSTAND1.000086
Length:85,dtype:float64
```

Notice that the standard deviations are not quite 1 here; this is again due to some procedures using the 1 _/n_ convention for variances (in this case `scaler()` ), while others use 1 _/_ ( _n −_ 1) (the `std()` method). See the footnote `.std()` on page 183. In this case it does not matter, as long as the variables are all on the same scale. 

Using the function `train_test_split()` we now split the observations into `train_test_` a test set, containing 1000 observations, and a training set containing the `split()` remaining observations. The argument `random_state=0` ensures that we get the same split each time we rerun the code. 

```
In [56]:(X_train,
X_test,
y_train,
y_test)=train_test_split(feature_std ,
Purchase,
test_size=1000,
random_state=0)
```

`?train_test_split` reveals that the non-keyword arguments can be `lists` , `arrays` , `pandas dataframes` etc that all have the same length ( `shape[0]` ) and hence are _indexable_ . In this case they are the dataframe `feature_std` and indexable the response variable `Purchase` . We fit a KNN model on the training data using $K$ = 1, and evaluate its performance on the test data. 

```
In [57]:knn1=KNeighborsClassifier(n_neighbors=1)
knn1_pred=knn1.fit(X_train,y_train).predict(X_test)
np.mean(y_test!=knn1_pred),np.mean(y_test!="No")
```

```
Out[57]:(0.111,0.067)
```

The KNN error rate on the 1,000 test observations is about 11%. At first glance, this may appear to be fairly good. However, since just over 6% of customers purchased insurance, we could get the error rate down to almost 6% by always predicting `No` regardless of the values of the predictors! This is known as the _null rate_ . 

Suppose that there is some non-trivial cost to trying to sell insurance to a given individual. For instance, perhaps a salesperson must visit each potential customer. If the company tries to sell insurance to a random selection of customers, then the success rate will be only 6%, which may be far too low given the costs involved. Instead, the company would like to try to sell insurance only to customers who are likely to buy it. So the overall error rate is not of interest. Instead, the fraction of individuals that are correctly predicted to buy insurance is of interest. 

null rate 

```
In [58]:confusion_table(knn1_pred,y_test)
```

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 

187 

```
Out[58]:
```

```
TruthNoYes
Predicted
No88058
Yes539
```

It turns out that KNN with $K$ = 1 does far better than random guessing among the customers that are predicted to buy insurance. Among 62 such customers, 9, or 14.5%, actually do purchase insurance. This is double the rate that one would obtain from random guessing. 

```
In [59]:9/(53+9)
```

```
Out[59]:0.145
```

Tuning Parameters 

The number of neighbors in KNN is referred to as a _tuning parameter_ , also tuning referred to as a _hyperparameter_ . We do not know _a priori_ what value to use. It is therefore of interest to see how the classifier performs on test hyperdata as we vary these parameters. This can be achieved with a `for` loop, described in Section 2.3.8. Here we use a for loop to look at the accuracy of our classifier in the group predicted to purchase insurance as we vary the number of neighbors from 1 to 5: 

parameter hyperparameter 

```
In [60]:forKinrange(1,6):
knn=KNeighborsClassifier(n_neighbors=K)
knn_pred=knn.fit(X_train,y_train).predict(X_test)
C=confusion_table(knn_pred,y_test)
templ=('K={0:d}:#predictedtorent:{1:>2},'+
'#whodidrent{2:d},accuracy{3:.1%}')
pred=C.loc['Yes'].sum()
did_rent=C.loc['Yes','Yes']
print(templ.format(
K,
pred,
did_rent,
did_rent/pred))
```

```
K=1:#predictedtorent:62,#whodidrent9,accuracy14.5%
K=2:#predictedtorent:6,#whodidrent1,accuracy16.7%
K=3:#predictedtorent:20,#whodidrent3,accuracy15.0%
K=4:#predictedtorent:3,#whodidrent0,accuracy0.0%
K=5:#predictedtorent:7,#whodidrent1,accuracy14.3%
```

We see some variability — the numbers for `K=4` are very different from the rest. 

Comparison to Logistic Regression 

As a comparison, we can also fit a logistic regression model to the data. This can also be done with `sklearn` , though by default it fits something like the _ridge regression_ version of logistic regression, which we introduce in Chapter 6. This can be modified by appropriately setting the argument `C` below. Its default value is 1 but by setting it to a very large number, the algorithm converges to the same solution as the usual (unregularized) logistic regression estimator discussed above. 

188 4. Classification 

Unlike the `statsmodels` package, `sklearn` focuses less on inference and more on classification. Hence, the `summary` methods seen in `statsmodels` and our simplified version seen with `summarize` are not generally available for the classifiers in `sklearn` . 

```
In [61]:logit=LogisticRegression(C=1e10,solver='liblinear')
logit.fit(X_train,y_train)
logit_pred=logit.predict_proba(X_test)
logit_labels=np.where(logit_pred[:,1]>5,'Yes','No')
confusion_table(logit_labels ,y_test)
```

```
Out[61]:TruthNoYes
Predicted
No93367
Yes00
```

We used the argument `solver='liblinear'` above to avoid a warning with the default solver which would indicate that the algorithm does not converge. 

If we use 0 _._ 5 as the predicted probability cut-off for the classifier, then we have a problem: none of the test observations are predicted to purchase insurance. However, we are not required to use a cut-off of 0 _._ 5. If we instead predict a purchase any time the predicted probability of purchase exceeds 0 _._ 25, we get much better results: we predict that 29 people will purchase insurance, and we are correct for about 31% of these people. This is almost five times better than random guessing! 

```
In [62]:logit_labels=np.where(logit_pred[:,1]>0.25,'Yes','No')
confusion_table(logit_labels ,y_test)
```

```
Out[62]:TruthNoYes
Predicted
No91358
Yes209
```

```
In [63]:9/(20+9)
```

```
Out[63]:0.310
```

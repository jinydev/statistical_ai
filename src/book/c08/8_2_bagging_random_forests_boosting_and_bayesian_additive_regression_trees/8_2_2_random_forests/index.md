---
layout: default
title: "index"
---

# _8.2.2 Random Forests_ 

_Random forests_ provide an improvement over bagged trees by way of a random small tweak that _decorrelates_ the trees. As in bagging, we build a number forest of decision trees on bootstrapped training samples. But when building these decision trees, each time a split in a tree is considered, _a random sample of m predictors_ is chosen as split candidates from the full set of _p_ predictors. The split is allowed to use only one of those _m_ predictors. A fresh sample of _m_ predictors is taken at each split, and typically we choose _m ≈[√] p_ ~~—~~ that is, the number of predictors considered at each split is approximately equal to the square root of the total number of predictors (4 out of the 13 for the `Heart` data). 

In other words, in building a random forest, at each split in the tree, the algorithm is _not even allowed to consider_ a majority of the available predictors. This may sound crazy, but it has a clever rationale. Suppose that there is one very strong predictor in the data set, along with a number of other moderately strong predictors. Then in the collection of bagged trees, most or all of the trees will use this strong predictor in the top split. Consequently, all of the bagged trees will look quite similar to each other. 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

347 

Hence the predictions from the bagged trees will be highly correlated. Unfortunately, averaging many highly correlated quantities does not lead to as large of a reduction in variance as averaging many uncorrelated quantities. In particular, this means that bagging will not lead to a substantial reduction in variance over a single tree in this setting. 

Random forests overcome this problem by forcing each split to consider only a subset of the predictors. Therefore, on average ( _p − m_ ) _/p_ of the splits will not even consider the strong predictor, and so other predictors will have more of a chance. We can think of this process as _decorrelating_ the trees, thereby making the average of the resulting trees less variable and hence more reliable. 

The main difference between bagging and random forests is the choice of predictor subset size _m_ . For instance, if a random forest is built using _m_ = _p_ , then this amounts simply to bagging. On the `Heart` data, random forests using _m_ = _[√] p_ leads to a reduction in both test error and OOB error over bagging (Figure 8.8). 

Using a small value of _m_ in building a random forest will typically be helpful when we have a large number of correlated predictors. We applied random forests to a high-dimensional biological data set consisting of expression measurements of 4,718 genes measured on tissue samples from 349 patients. There are around 20,000 genes in humans, and individual genes have different levels of activity, or expression, in particular cells, tissues, and biological conditions. In this data set, each of the patient samples has a qualitative label with 15 different levels: either normal or 1 of 14 different types of cancer. Our goal was to use random forests to predict cancer type based on the 500 genes that have the largest variance in the training set. We randomly divided the observations into a training and a test set, and applied random forests to the training set for three different values of the number of splitting variables _m_ . The results are shown in Figure 8.10. The error rate of a single tree is 45 _._ 7 %, and the null rate is 75 _._ 4 %.[4] We see that using 400 trees is sufficient to give good performance, and that the choice _m_ = _[√] p_ gave a small improvement in test error over bagging ( _m_ = _p_ ) in this example. As with bagging, random forests will not overfit if we increase _B_ , so in practice we use a value of _B_ sufficiently large for the error rate to have settled down. 

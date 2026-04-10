---
layout: default
title: "index"
---

# _8.2.3 Boosting_ 

We now discuss _boosting_ , yet another approach for improving the predic- boosting tions resulting from a decision tree. Like bagging, boosting is a general approach that can be applied to many statistical learning methods for regression or classification. Here we restrict our discussion of boosting to the context of decision trees. 

Recall that bagging involves creating multiple copies of the original training data set using the bootstrap, fitting a separate decision tree to each copy, and then combining all of the trees in order to create a single predic- 

> 4The null rate results from simply classifying each observation to the dominant class overall, which is in this case the normal class. 

348 8. Tree-Based Methods 

![Figure 8.10](./img/8_10.png)

**FIGURE 8.10.** _Results from random forests for the 15-class gene expression data set with p_ = 500 _predictors. The test error is displayed as a function of the number of trees. Each colored line corresponds to a different value of m, the number of predictors available for splitting at each interior tree node. Random forests (m < p) lead to a slight improvement over bagging (m_ = _p). A single classification tree has an error rate of 45.7 %._ 

tive model. Notably, each tree is built on a bootstrap data set, independent of the other trees. Boosting works in a similar way, except that the trees are grown _sequentially_ : each tree is grown using information from previously grown trees. Boosting does not involve bootstrap sampling; instead each tree is fit on a modified version of the original data set. 

Consider first the regression setting. Like bagging, boosting involves combining a large number of decision trees, _f_[ˆ][1] _, . . . , f_[ˆ] _[B]_ . Boosting is described in Algorithm 8.2. 

What is the idea behind this procedure? Unlike fitting a single large decision tree to the data, which amounts to _fitting the data hard_ and potentially overfitting, the boosting approach instead _learns slowly_ . Given the current model, we fit a decision tree to the residuals from the model. That is, we fit a tree using the current residuals, rather than the outcome _Y_ , as the response. We then add this new decision tree into the fitted function in order to update the residuals. Each of these trees can be rather small, with just a few terminal nodes, determined by the parameter _d_ in the algorithm. By fitting small trees to the residuals, we slowly improve _f_[ˆ] in areas where it does not perform well. The shrinkage parameter _λ_ slows the process down even further, allowing more and different shaped trees to attack the residuals. In general, statistical learning approaches that _learn slowly_ tend to perform well. Note that in boosting, unlike in bagging, the construction of each tree depends strongly on the trees that have already been grown. 

We have just described the process of boosting regression trees. Boosting classification trees proceeds in a similar but slightly more complex way, and the details are omitted here. 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

349 

**Algorithm 8.2** _Boosting for Regression Trees_ 

1. Set _f_[ˆ] ( _x_ ) = 0 and _ri_ = _yi_ for all _i_ in the training set. 

2. For _b_ = 1 _,_ 2 _, . . . , B_ , repeat: 

   - (a) Fit a tree _f_[ˆ] _[b]_ with _d_ splits ( _d_ + 1 terminal nodes) to the training data ( _X, r_ ). 

   - (b) Update _f_[ˆ] by adding in a shrunken version of the new tree:

$$
\hat{f}(x) \leftarrow \hat{f}(x) + \lambda \hat{f}^b(x) \quad (8.10)
$$


- (c) Update the residuals,

$$
r_i \leftarrow r_i - \lambda \hat{f}^b(x_i) \quad (8.11)
$$


3. Output the boosted model,

$$
\hat{f}(x) = \sum_{b=1}^B \lambda \hat{f}^b(x) \quad (8.12)
$$


Boosting has three tuning parameters: 

1. The number of trees _B_ . Unlike bagging and random forests, boosting can overfit if _B_ is too large, although this overfitting tends to occur slowly if at all. We use cross-validation to select _B_ . 

2. The shrinkage parameter _λ_ , a small positive number. This controls the rate at which boosting learns. Typical values are 0 _._ 01 or 0 _._ 001, and the right choice can depend on the problem. Very small _λ_ can require using a very large value of _B_ in order to achieve good performance. 

3. The number _d_ of splits in each tree, which controls the complexity of the boosted ensemble. Often _d_ = 1 works well, in which case each tree is a _stump_ , consisting of a single split. In this case, the boosted ensemble is fitting an additive model, since each term involves only a stump single variable. More generally _d_ is the _interaction depth_ , and controls interaction 

the interaction order of the boosted model, since _d_ splits can involve depth at most _d_ variables. 

In Figure 8.11, we applied boosting to the 15-class cancer gene expression data set, in order to develop a classifier that can distinguish the normal class from the 14 cancer classes. We display the test error as a function of the total number of trees and the interaction depth _d_ . We see that simple stumps with an interaction depth of one perform well if enough of them are included. This model outperforms the depth-two model, and both outperform a random forest. This highlights one difference between boosting and random forests: in boosting, because the growth of a particular tree takes into account the other trees that have already been grown, smaller 

8. Tree-Based Methods 

350 

![Figure 8.11](./img/8_11.png)

**FIGURE 8.11.** _Results from performing boosting and random forests on the 15-class gene expression data set in order to predict_ cancer _versus_ normal _. The test error is displayed as a function of the number of trees. For the two boosted models, λ_ = 0 _._ 01 _. Depth-1 trees slightly outperform depth-2 trees, and both outperform the random forest, although the standard errors are around 0.02, making none of these differences significant. The test error rate for a single tree is 24 %._ 

trees are typically sufficient. Using smaller trees can aid in interpretability as well; for instance, using stumps leads to an additive model. 

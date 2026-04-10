---
layout: default
title: "index"
---

# _8.1.2 Trees Classification_ 

A _classification tree_ is very similar to a regression tree, except that it is classification used to predict a qualitative response rather than a quantitative one. Retree call that for a regression tree, the predicted response for an observation is given by the mean response of the training observations that belong to the same terminal node. In contrast, for a classification tree, we predict that each observation belongs to the _most commonly occurring class_ of training observations in the region to which it belongs. In interpreting the results of a classification tree, we are often interested not only in the class prediction corresponding to a particular terminal node region, but also in the _class proportions_ among the training observations that fall into that region. 

The task of growing a classification tree is quite similar to the task of growing a regression tree. Just as in the regression setting, we use recursive 

> 2Although CV error is computed as a function of _α_ , it is convenient to display the result as a function of _|T |_ , the number of leaves; this is based on the relationship between _α_ and _|T |_ in the original tree grown to all the training data. 

8. Tree-Based Methods 

338 

![Figure 8.4](./img/8_4.png)

**FIGURE 8.4.** _Regression tree analysis for the_ `Hitters` _data. The unpruned tree that results from top-down greedy splitting on the training data is shown._ 

binary splitting to grow a classification tree. However, in the classification setting, RSS cannot be used as a criterion for making the binary splits. A natural alternative to RSS is the _classification error rate_ . Since we plan classification to assign an observation in a given region to the _most commonly occurring_ error rate _class_ of training observations in that region, the classification error rate is simply the fraction of the training observations in that region that do not belong to the most common class:

$$
E = 1 - \max_k (\hat{p}_{mk}) \quad (8.5)
$$


Here _p_ ˆ _mk_ represents the proportion of training observations in the _m_ th region that are from the _k_ th class. However, it turns out that classification error is not sufficiently sensitive for tree-growing, and in practice two other measures are preferable. 

The _Gini index_ is defined by

$$
G = \sum_{k=1}^K \hat{p}_{mk} (1 - \hat{p}_{mk}) \quad (8.6)
$$


a measure of total variance across the _K_ classes. It is not hard to see that the Gini index takes on a small value if all of the _p_ ˆ _mk_ ’s are close to zero or one. For this reason the Gini index is referred to as a measure of 

8.1 The Basics of Decision Trees 339 

![Figure 8.5](./img/8_5.png)

**FIGURE 8.5.** _Regression tree analysis for the_ `Hitters` _data. The training, cross-validation, and test $\text{MSE}$ are shown as a function of the number of terminal nodes in the pruned tree. Standard error bands are displayed. The minimum cross-validation error occurs at a tree size of three._ 

node _purity_ —a small value indicates that a node contains predominantly observations from a single class. 

An alternative to the Gini index is _entropy_ , given by

$$
D = - \sum_{k=1}^K \hat{p}_{mk} \log \hat{p}_{mk} \quad (8.7)
$$


Since 0 _≤ p_ ˆ _mk ≤_ 1, it follows that 0 _≤−p_ ˆ _mk_ log ˆ _pmk_ . One can show that the entropy will take on a value near zero if the _p_ ˆ _mk_ ’s are all near zero or near one. Therefore, like the Gini index, the entropy will take on a small value if the _m_ th node is pure. In fact, it turns out that the Gini index and the entropy are quite similar numerically. 

When building a classification tree, either the Gini index or the entropy are typically used to evaluate the quality of a particular split, since these two approaches are more sensitive to node purity than is the classification error rate. Any of these three approaches might be used when _pruning_ the tree, but the classification error rate is preferable if prediction accuracy of the final pruned tree is the goal. 

Figure 8.6 shows an example on the `Heart` data set. These data contain a binary outcome `HD` for 303 patients who presented with chest pain. An outcome value of `Yes` indicates the presence of heart disease based on an angiographic test, while `No` means no heart disease. There are 13 predictors including `Age` , `Sex` , `Chol` (a cholesterol measurement), and other heart and lung function measurements. Cross-validation results in a tree with six terminal nodes. 

In our discussion thus far, we have assumed that the predictor variables take on continuous values. However, decision trees can be constructed even in the presence of qualitative predictor variables. For instance, in the `Heart` data, some of the predictors, such as `Sex` , `Thal` (Thallium stress test), 

340 8. Tree-Based Methods 

![Figure 8.6](./img/8_6.png)

**FIGURE 8.6.** `Heart` _data._ Top: _The unpruned tree._ Bottom Left: _Cross-validation error, training, and test error, for different sizes of the pruned tree._ Bottom Right: _The pruned tree corresponding to the minimal cross-validation error._ 

and `ChestPain` , are qualitative. Therefore, a split on one of these variables amounts to assigning some of the qualitative values to one branch and assigning the remaining to the other branch. In Figure 8.6, some of the internal nodes correspond to splitting qualitative variables. For instance, the top internal node corresponds to splitting `Thal` . The text `Thal:a` indicates that the left-hand branch coming out of that node consists of observations with the first value of the `Thal` variable (normal), and the right-hand node consists of the remaining observations (fixed or reversible defects). The text `ChestPain:bc` two splits down the tree on the left indicates that the left-hand branch coming out of that node consists of observations with the second and third values of the `ChestPain` variable, where the possible values are typical angina, atypical angina, non-anginal pain, and asymptomatic. 

Figure 8.6 has a surprising characteristic: some of the splits yield two terminal nodes that have the _same predicted value_ . For instance, consider the split `RestECG<1` near the bottom right of the unpruned tree. Regardless of the value of `RestECG` , a response value of `Yes` is predicted for those ob- 

8.1 The Basics of Decision Trees 

341 

servations. Why, then, is the split performed at all? The split is performed because it leads to increased _node purity_ . That is, all 9 of the observations corresponding to the right-hand leaf have a response value of `Yes` , whereas 7 _/_ 11 of those corresponding to the left-hand leaf have a response value of `Yes` . Why is node purity important? Suppose that we have a test observation that belongs to the region given by that right-hand leaf. Then we can be pretty certain that its response value is `Yes` . In contrast, if a test observation belongs to the region given by the left-hand leaf, then its response value is probably `Yes` , but we are much less certain. Even though the split `RestECG<1` does not reduce the classification error, it improves the Gini index and the entropy, which are more sensitive to node purity. 

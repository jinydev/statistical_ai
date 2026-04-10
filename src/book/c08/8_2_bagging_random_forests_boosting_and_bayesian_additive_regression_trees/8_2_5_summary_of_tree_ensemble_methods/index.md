---
layout: default
title: "index"
---

# _8.2.5 Summary of Tree Ensemble Methods_ 

Trees are an attractive choice of weak learner for an ensemble method for a number of reasons, including their flexibility and ability to handle 

354 8. Tree-Based Methods 

predictors of mixed types (i.e. qualitative as well as quantitative). We have now seen four approaches for fitting an ensemble of trees: bagging, random forests, boosting, and BART. 

- In _bagging_ , the trees are grown independently on random samples of the observations. Consequently, the trees tend to be quite similar to each other. Thus, bagging can get caught in local optima and can fail to thoroughly explore the model space. 

- In _random forests_ , the trees are once again grown independently on random samples of the observations. However, each split on each tree is performed using a random subset of the features, thereby decorrelating the trees, and leading to a more thorough exploration of model space relative to bagging. 

- In _boosting_ , we only use the original data, and do not draw any random samples. The trees are grown successively, using a “slow” learning approach: each new tree is fit to the signal that is left over from the earlier trees, and shrunken down before it is used. 

- In _BART_ , we once again only make use of the original data, and we grow the trees successively. However, each tree is perturbed in order to avoid local minima and achieve a more thorough exploration of the model space. 

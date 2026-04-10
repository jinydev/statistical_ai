---
layout: default
title: "index"
---

# Variable Importance Measures 

As we have discussed, bagging typically results in improved accuracy over prediction using a single tree. Unfortunately, however, it can be difficult to interpret the resulting model. Recall that one of the advantages of decision trees is the attractive and easily interpreted diagram that results, such as the one displayed in Figure 8.1. However, when we bag a large number of trees, it is no longer possible to represent the resulting statistical learning procedure using a single tree, and it is no longer clear which variables are most important to the procedure. Thus, bagging improves prediction accuracy at the expense of interpretability. 

Although the collection of bagged trees is much more difficult to interpret than a single tree, one can obtain an overall summary of the importance of each predictor using the RSS (for bagging regression trees) or the Gini index (for bagging classification trees). In the case of bagging regression trees, we can record the total amount that the RSS (8.1) is decreased due to splits over a given predictor, averaged over all _B_ trees. A large value indicates an important predictor. Similarly, in the context of bagging classification 

> 3This relates to Exercise 2 of Chapter 5. 

8. Tree-Based Methods 

346 

![Figure 8.9](./img/8_9.png)

**FIGURE 8.9.** _A variable importance plot for the_ `Heart` _data. Variable importance is computed using the mean decrease in Gini index, and expressed relative to the maximum._ 

trees, we can add up the total amount that the Gini index (8.6) is decreased by splits over a given predictor, averaged over all _B_ trees. 

A graphical representation of the _variable importances_ in the `Heart` data variable is shown in Figure 8.9. We see the mean decrease in Gini index for each variable, relative to the largest. The variables with the largest mean decrease in Gini index are `Thal` , `Ca` , and `ChestPain` . 

importance 

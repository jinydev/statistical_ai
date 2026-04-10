---
layout: default
title: "index"
---

# _Applied_ 

7. In Section 8.3.3, we applied random forests to the `Boston` data using `max_features = 6` and using `n_estimators = 100` and `n_estimators = 500` . Create a plot displaying the test error resulting from random forests on this data set for a more comprehensive range of values for `max_features` and `n_estimators` . You can model your plot after Figure 8.10. Describe the results obtained. 

8. In the lab, a classification tree was applied to the `Carseats` data set after converting `Sales` into a qualitative response variable. Now we will seek to predict `Sales` using regression trees and related approaches, treating the response as a quantitative variable. 

8.4 Exercises 365 

   - (a) Split the data set into a training set and a test set. 

   - (b) Fit a regression tree to the training set. Plot the tree, and interpret the results. What test $\text{MSE}$ do you obtain? 

   - (c) Use cross-validation in order to determine the optimal level of tree complexity. Does pruning the tree improve the test MSE? 

   - (d) Use the bagging approach in order to analyze this data. What test $\text{MSE}$ do you obtain? Use the `feature_importance_` values to determine which variables are most important. 

   - (e) Use random forests to analyze this data. What test $\text{MSE}$ do you obtain? Use the `feature_importance_` values to determine which variables are most important. Describe the effect of _m_ , the number of variables considered at each split, on the error rate obtained. 

   - (f) Now analyze the data using BART, and report your results. 

9. This problem involves the `OJ` data set which is part of the `ISLP` package. 

   - (a) Create a training set containing a random sample of 800 observations, and a test set containing the remaining observations. 

   - (b) Fit a tree to the training data, with `Purchase` as the response and the other variables as predictors. What is the training error rate? 

   - (c) Create a plot of the tree, and interpret the results. How many terminal nodes does the tree have? 

   - (d) Use the `export_tree()` function to produce a text summary of the fitted tree. Pick one of the terminal nodes, and interpret the information displayed. 

   - (e) Predict the response on the test data, and produce a confusion matrix comparing the test labels to the predicted test labels. What is the test error rate? 

   - (f) Use cross-validation on the training set in order to determine the optimal tree size. 

   - (g) Produce a plot with tree size on the _x_ -axis and cross-validated classification error rate on the _y_ -axis. 

   - (h) Which tree size corresponds to the lowest cross-validated classification error rate? 

   - (i) Produce a pruned tree corresponding to the optimal tree size obtained using cross-validation. If cross-validation does not lead to selection of a pruned tree, then create a pruned tree with five terminal nodes. 

   - (j) Compare the training error rates between the pruned and unpruned trees. Which is higher? 

   - (k) Compare the test error rates between the pruned and unpruned trees. Which is higher? 

366 8. Tree-Based Methods 

10. We now use boosting to predict `Salary` in the `Hitters` data set. 

   - (a) Remove the observations for whom the salary information is unknown, and then log-transform the salaries. 

   - (b) Create a training set consisting of the first 200 observations, and a test set consisting of the remaining observations. 

   - (c) Perform boosting on the training set with 1,000 trees for a range of values of the shrinkage parameter _λ_ . Produce a plot with different shrinkage values on the _x_ -axis and the corresponding training set $\text{MSE}$ on the _y_ -axis. 

   - (d) Produce a plot with different shrinkage values on the _x_ -axis and the corresponding test set $\text{MSE}$ on the _y_ -axis. 

   - (e) Compare the test $\text{MSE}$ of boosting to the test $\text{MSE}$ that results from applying two of the regression approaches seen in Chapters 3 and 6. 

   - (f) Which variables appear to be the most important predictors in the boosted model? 

   - (g) Now apply bagging to the training set. What is the test set $\text{MSE}$ for this approach? 

11. This question uses the `Caravan` data set. 

   - (a) Create a training set consisting of the first 1,000 observations, and a test set consisting of the remaining observations. 

   - (b) Fit a boosting model to the training set with `Purchase` as the response and the other variables as predictors. Use 1,000 trees, and a shrinkage value of 0 _._ 01. Which predictors appear to be the most important? 

   - (c) Use the boosting model to predict the response on the test data. Predict that a person will make a purchase if the estimated probability of purchase is greater than 20 %. Form a confusion matrix. What fraction of the people predicted to make a purchase do in fact make one? How does this compare with the results obtained from applying KNN or logistic regression to this data set? 

12. Apply boosting, bagging, random forests, and BART to a data set of your choice. Be sure to fit the models on a training set and to evaluate their performance on a test set. How accurate are the results compared to simple methods like linear or logistic regression? Which of these approaches yields the best performance? 

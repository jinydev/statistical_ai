---
layout: default
title: "index"
---

# _8.1.4 Advantages and Disadvantages of Trees_ 

Decision trees for regression and classification have a number of advantages over the more classical approaches seen in Chapters 3 and 4: 

- L Trees are very easy to explain to people. In fact, they are even easier to explain than linear regression! 

342 8. Tree-Based Methods 

![Figure 8.7](./img/8_7.png)

**FIGURE 8.7.** Top Row: _A two-dimensional classification example in which the true decision boundary is linear, and is indicated by the shaded regions. A classical approach that assumes a linear boundary (left) will outperform a decision tree that performs splits parallel to the axes (right)._ Bottom Row: _Here the true decision boundary is non-linear. Here a linear model is unable to capture the true decision boundary (left), whereas a decision tree is successful (right)._ 

- L Some people believe that decision trees more closely mirror human decision-making than do the regression and classification approaches seen in previous chapters. 

- L Trees can be displayed graphically, and are easily interpreted even by a non-expert (especially if they are small). 

- L Trees can easily handle qualitative predictors without the need to create dummy variables. 

- M Unfortunately, trees generally do not have the same level of predictive accuracy as some of the other regression and classification approaches seen in this book. 

- M Additionally, trees can be very non-robust. In other words, a small change in the data can cause a large change in the final estimated tree. 

However, by aggregating many decision trees, using methods like _bagging_ , _random forests_ , and _boosting_ , the predictive performance of trees can be substantially improved. We introduce these concepts in the next section. 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

343 

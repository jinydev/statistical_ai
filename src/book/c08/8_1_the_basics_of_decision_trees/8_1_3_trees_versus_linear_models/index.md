---
layout: default
title: "index"
---

# _8.1.3 Trees Versus Linear Models_ 

Regression and classification trees have a very different flavor from the more classical approaches for regression and classification presented in Chapters 3 and 4. In particular, linear regression assumes a model of the form

$$
f(X) = \beta_0 + \sum_{j=1}^p X_j \beta_j \quad (8.8)
$$


whereas regression trees assume a model of the form

$$
f(X) = \sum_{m=1}^M c_m \cdot 1_{(X \in R_m)} \quad (8.9)
$$


where _R_ 1 _, . . . , RM_ represent a partition of feature space, as in Figure 8.3. Which model is better? It depends on the problem at hand. If the relationship between the features and the response is well approximated by a linear model as in (8.8), then an approach such as linear regression will likely work well, and will outperform a method such as a regression tree that does not exploit this linear structure. If instead there is a highly nonlinear and complex relationship between the features and the response as indicated by model (8.9), then decision trees may outperform classical approaches. An illustrative example is displayed in Figure 8.7. The relative performances of tree-based and classical approaches can be assessed by estimating the test error, using either cross-validation or the validation set approach (Chapter 5). 

Of course, other considerations beyond simply test error may come into play in selecting a statistical learning method; for instance, in certain settings, prediction using a tree may be preferred for the sake of interpretability and visualization. 

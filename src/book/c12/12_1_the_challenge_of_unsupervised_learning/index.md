---
layout: default
title: "index"
---

# 12.1 The Challenge of Unsupervised Learning 

Supervised learning is a well-understood area. In fact, if you have read the preceding chapters in this book, then you should by now have a good grasp of supervised learning. For instance, if you are asked to predict a binary outcome from a data set, you have a very well developed set of tools at your disposal (such as logistic regression, linear discriminant analysis, classification trees, support vector machines, and more) as well as a clear 

© Springer Nature Switzerland AG 2023 G. James et al., _An Introduction to Statistical Learning_ , Springer Texts in Statistics, https://doi.org/10.1007/978-3-031-38747-0_12 

503 

504 12. Unsupervised Learning 

understanding of how to assess the quality of the results obtained (using cross-validation, validation on an independent test set, and so forth). 

In contrast, unsupervised learning is often much more challenging. The exercise tends to be more subjective, and there is no simple goal for the analysis, such as prediction of a response. Unsupervised learning is often performed as part of an _exploratory data analysis_ . Furthermore, it can be exploratory hard to assess the results obtained from unsupervised learning methods, data since there is no universally accepted mechanism for performing crossanalysis validation or validating results on an independent data set. The reason for this difference is simple. If we fit a predictive model using a supervised learning technique, then it is possible to _check our work_ by seeing how well our model predicts the response _Y_ on observations not used in fitting the model. However, in unsupervised learning, there is no way to check our work because we don’t know the true answer—the problem is unsupervised. 

Techniques for unsupervised learning are of growing importance in a number of fields. A cancer researcher might assay gene expression levels in 100 patients with breast cancer. He or she might then look for subgroups among the breast cancer samples, or among the genes, in order to obtain a better understanding of the disease. An online shopping site might try to identify groups of shoppers with similar browsing and purchase histories, as well as items that are of particular interest to the shoppers within each group. Then an individual shopper can be preferentially shown the items in which he or she is particularly likely to be interested, based on the purchase histories of similar shoppers. A search engine might choose which search results to display to a particular individual based on the click histories of other individuals with similar search patterns. These statistical learning tasks, and many more, can be performed via unsupervised learning techniques. 

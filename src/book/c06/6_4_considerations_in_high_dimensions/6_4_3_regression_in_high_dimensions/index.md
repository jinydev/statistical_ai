---
layout: default
title: "index"
---

# _6.4.3 Regression in High Dimensions_ 

It turns out that many of the methods seen in this chapter for fitting _less flexible_ least squares models, such as forward stepwise selection, ridge regression, the lasso, and principal components regression, are particularly useful for performing regression in the high-dimensional setting. Essentially, these approaches avoid overfitting by using a less flexible fitting approach than least squares. 

Figure 6.24 illustrates the performance of the lasso in a simple simulated example. There are _p_ = 20, 50, or 2 _,_ 000 features, of which 20 are truly associated with the outcome. The lasso was performed on _n_ = 100 training observations, and the mean squared error was evaluated on an independent test set. As the number of features increases, the test set error increases. When _p_ = 20, the lowest validation set error was achieved when _λ_ in 

266 6. Linear Model Selection and Regularization 

(6.7) was small; however, when _p_ was larger then the lowest validation set error was achieved using a larger value of _λ_ . In each boxplot, rather than reporting the values of _λ_ used, the _degrees of freedom_ of the resulting lasso solution is displayed; this is simply the number of non-zero coefficient estimates in the lasso solution, and is a measure of the flexibility of the lasso fit. Figure 6.24 highlights three important points: (1) regularization or shrinkage plays a key role in high-dimensional problems, (2) appropriate tuning parameter selection is crucial for good predictive performance, and (3) the test error tends to increase as the dimensionality of the problem (i.e. the number of features or predictors) increases, unless the additional features are truly associated with the response. 

The third point above is in fact a key principle in the analysis of highdimensional data, which is known as the _curse of dimensionality_ . One might curse of dithink that as the number of features used to fit a model increases, the mensionality quality of the fitted model will increase as well. However, comparing the left-hand and right-hand panels in Figure 6.24, we see that this is not necessarily the case: in this example, the test set $\text{MSE}$ almost doubles as _p_ increases from 20 to 2,000. In general, _adding additional signal features that are truly associated with the response will improve the fitted model_ , in the sense of leading to a reduction in test set error. However, adding noise features that are not truly associated with the response will lead to a deterioration in the fitted model, and consequently an increased test set error. This is because noise features increase the dimensionality of the problem, exacerbating the risk of overfitting (since noise features may be assigned nonzero coefficients due to chance associations with the response on the training set) without any potential upside in terms of improved test set error. Thus, we see that new technologies that allow for the collection of measurements for thousands or millions of features are a double-edged sword: they can lead to improved predictive models if these features are in fact relevant to the problem at hand, but will lead to worse results if the features are not relevant. Even if they are relevant, the variance incurred in fitting their coefficients may outweigh the reduction in bias that they bring. 

mensionality 

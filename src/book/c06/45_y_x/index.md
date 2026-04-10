---
layout: default
title: "index"
---

# _Y_ = _Xβ_ + _ϵ,_ 

where _β_ has some elements that are exactly equal to zero. 

   - (b) Split your data set into a training set containing 100 observations and a test set containing 900 observations. 

   - (c) Perform best subset selection on the training set, and plot the training set $\text{MSE}$ associated with the best model of each size. 

   - (d) Plot the test set $\text{MSE}$ associated with the best model of each size. 

   - (e) For which model size does the test set $\text{MSE}$ take on its minimum value? Comment on your results. If it takes on its minimum value for a model containing only an intercept or a model containing all of the features, then play around with the way that you are generating the data in (a) until you come up with a scenario in which the test set $\text{MSE}$ is minimized for an intermediate model size. 

   - (f) How does the model at which the test set $\text{MSE}$ is minimized compare to the true model used to generate the data? Comment on the coefficient values. 

   - (g) Create a plot displaying � ~~�~~ _pj_ =1[(] _[β][j][−][β]_[ˆ] _j[r]_[)][2][for a range of values] of _r_ , where _β_[ˆ] _j[r]_[is][the] _[j]_[th][coefficient][estimate][for][the][best][model] containing _r_ coefficients. Comment on what you observe. How does this compare to the test $\text{MSE}$ plot from (d)? 

11. We will now try to predict per capita crime rate in the `Boston` data set. 

   - (a) Try out some of the regression methods explored in this chapter, such as best subset selection, the lasso, ridge regression, and PCR. Present and discuss results for the approaches that you consider. 

   - (b) Propose a model (or set of models) that seem to perform well on this data set, and justify your answer. Make sure that you are evaluating model performance using validation set error, crossvalidation, or some other reasonable alternative, as opposed to using training error. 

288 6. Linear Model Selection and Regularization 

- (c) Does your chosen model involve all of the features in the data set? Why or why not? 

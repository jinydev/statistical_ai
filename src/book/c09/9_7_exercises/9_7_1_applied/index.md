---
layout: default
title: "index"
---

# _Applied_ 

4. Generate a simulated two-class data set with 100 observations and two features in which there is a visible but non-linear separation between the two classes. Show that in this setting, a support vector machine with a polynomial kernel (with degree greater than 1) or a radial kernel will outperform a support vector classifier on the training data. Which technique performs best on the test data? Make plots and report training and test error rates in order to back up your assertions. 

5. We have seen that we can fit an SVM with a non-linear kernel in order to perform classification using a non-linear decision boundary. We will now see that we can also obtain a non-linear decision boundary by performing logistic regression using non-linear transformations of the features. 

9.7 Exercises 397 

- (a) Generate a data set with _n_ = 500 and _p_ = 2, such that the observations belong to two classes with a quadratic decision boundary between them. For instance, you can do this as follows: 

```
rng=np.random.default_rng(5)
x1=rng.uniform(size=500)-0.5
x2=rng.uniform(size=500)-0.5
y=x1**2-x2**2>0
```

   - (b) Plot the observations, colored according to their class labels. Your plot should display _X_ 1 on the _x_ -axis, and _X_ 2 on the _y_ - axis. 

   - (c) Fit a logistic regression model to the data, using _X_ 1 and _X_ 2 as predictors. 

   - (d) Apply this model to the _training data_ in order to obtain a predicted class label for each training observation. Plot the observations, colored according to the _predicted_ class labels. The decision boundary should be linear. 

   - (e) Now fit a logistic regression model to the data using non-linear functions of _X_ 1 and _X_ 2 as predictors (e.g. _X_ 1[2][,] _[ X]_[1] _[×][X]_[2][,][ log(] _[X]_[2][)][,] and so forth). 

   - (f) Apply this model to the _training data_ in order to obtain a predicted class label for each training observation. Plot the observations, colored according to the _predicted_ class labels. The decision boundary should be obviously non-linear. If it is not, then repeat (a)–(e) until you come up with an example in which the predicted class labels are obviously non-linear. 

   - (g) Fit a support vector classifier to the data with _X_ 1 and _X_ 2 as predictors. Obtain a class prediction for each training observation. Plot the observations, colored according to the _predicted class labels_ . 

   - (h) Fit a SVM using a non-linear kernel to the data. Obtain a class prediction for each training observation. Plot the observations, colored according to the _predicted class labels_ . 

   - (i) Comment on your results. 

6. At the end of Section 9.6.1, it is claimed that in the case of data that is just barely linearly separable, a support vector classifier with a small value of `C` that misclassifies a couple of training observations may perform better on test data than one with a huge value of `C` that does not misclassify any training observations. You will now investigate this claim. 

   - (a) Generate two-class data with _p_ = 2 in such a way that the classes are just barely linearly separable. 

   - (b) Compute the cross-validation error rates for support vector classifiers with a range of `C` values. How many training observations are misclassified for each value of `C` considered, and how does this relate to the cross-validation errors obtained? 

9. Support Vector Machines 

398 

   - (c) Generate an appropriate test data set, and compute the test errors corresponding to each of the values of `C` considered. Which value of `C` leads to the fewest test errors, and how does this compare to the values of `C` that yield the fewest training errors and the fewest cross-validation errors? 

   - (d) Discuss your results. 

7. In this problem, you will use support vector approaches in order to predict whether a given car gets high or low gas mileage based on the `Auto` data set. 

   - (a) Create a binary variable that takes on a 1 for cars with gas mileage above the median, and a 0 for cars with gas mileage below the median. 

   - (b) Fit a support vector classifier to the data with various values of `C` , in order to predict whether a car gets high or low gas mileage. Report the cross-validation errors associated with different values of this parameter. Comment on your results. Note you will need to fit the classifier without the gas mileage variable to produce sensible results. 

   - (c) Now repeat (b), this time using SVMs with radial and polynomial basis kernels, with different values of `gamma` and `degree` and `C` . Comment on your results. 

   - (d) Make some plots to back up your assertions in (b) and (c). 

_Hint: In the lab, we used the_ `plot_svm()` _function for fitted SVMs. When p >_ 2 _, you can use the keyword argument_ `features` _to create plots displaying pairs of variables at a time._ 

8. This problem involves the `OJ` data set which is part of the `ISLP` package. 

   - (a) Create a training set containing a random sample of 800 observations, and a test set containing the remaining observations. 

   - (b) Fit a support vector classifier to the training data using `C = 0.01` , with `Purchase` as the response and the other variables as predictors. How many support points are there? 

   - (c) What are the training and test error rates? 

   - (d) Use cross-validation to select an optimal `C` . Consider values in the range 0 _._ 01 to 10. 

   - (e) Compute the training and test error rates using this new value for `C` . 

   - (f) Repeat parts (b) through (e) using a support vector machine with a radial kernel. Use the default value for `gamma` . 

   - (g) Repeat parts (b) through (e) using a support vector machine with a polynomial kernel. Set `degree = 2` . 

   - (h) Overall, which approach seems to give the best results on this data? 

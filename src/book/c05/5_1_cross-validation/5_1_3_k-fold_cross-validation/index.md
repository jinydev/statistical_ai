---
layout: default
title: "index"
---

# _5.1.3 k-Fold Cross-Validation_ 

An alternative to LOOCV is _k-fold CV_ . This approach involves randomly _k_ -fold CV dividing the set of observations into _k_ groups, or _folds_ , of approximately equal size. The first fold is treated as a validation set, and the method is fit on the remaining _k −_ 1 folds. The mean squared error, $\text{MSE}_1$, is then computed on the observations in the held-out fold. This procedure is repeated _k_ times; each time, a different group of observations is treated as a validation set. This process results in _k_ estimates of the test error, $\text{MSE}_1$ _,_ $\text{MSE}_2$ _, . . . ,_ MSE _k_ . The _k_ -fold CV estimate is computed by averaging these values, 

$$
\text{CV}_{(k)} = \frac{1}{k} \sum_{i=1}^k \text{MSE}_i \quad (5.3)
$$

Figure 5.5 illustrates the _k_ -fold CV approach. 

> 1In the case of multiple linear regression, the leverage takes a slightly more complicated form than (3.37), but (5.2) still holds. 

5.1 Cross-Validation 207 

**FIGURE 5.5.** _A schematic display of_ 5 _-fold CV. A set of n observations is randomly split into five non-overlapping groups. Each of these fifths acts as a validation set (shown in beige), and the remainder as a training set (shown in blue). The test error is estimated by averaging the five resulting MSE estimates._ 

It is not hard to see that LOOCV is a special case of _k_ -fold CV in which _k_ is set to equal _n_ . In practice, one typically performs _k_ -fold CV using _k_ = 5 or _k_ = 10. What is the advantage of using _k_ = 5 or _k_ = 10 rather than _k_ = _n_ ? The most obvious advantage is computational. LOOCV requires fitting the statistical learning method _n_ times. This has the potential to be computationally expensive (except for linear models fit by least squares, in which case formula (5.2) can be used). But cross-validation is a very general approach that can be applied to almost any statistical learning method. Some statistical learning methods have computationally intensive fitting procedures, and so performing LOOCV may pose computational problems, especially if _n_ is extremely large. In contrast, performing 10-fold CV requires fitting the learning procedure only ten times, which may be much more feasible. As we see in Section 5.1.4, there also can be other non-computational advantages to performing 5-fold or 10-fold CV, which involve the bias-variance trade-off. 

The right-hand panel of Figure 5.4 displays nine different 10-fold CV estimates for the `Auto` data set, each resulting from a different random split of the observations into ten folds. As we can see from the figure, there is some variability in the CV estimates as a result of the variability in how the observations are divided into ten folds. But this variability is typically much lower than the variability in the test error estimates that results from the validation set approach (right-hand panel of Figure 5.2). 

When we examine real data, we do not know the _true_ test MSE, and so it is difficult to determine the accuracy of the cross-validation estimate. However, if we examine simulated data, then we can compute the true test MSE, and can thereby evaluate the accuracy of our cross-validation results. In Figure 5.6, we plot the cross-validation estimates and true test error rates that result from applying smoothing splines to the simulated data sets illustrated in Figures 2.9–2.11 of Chapter 2. The true test MSE is displayed in blue. The black dashed and orange solid lines respectively show the estimated LOOCV and 10-fold CV estimates. In all three plots, the two cross-validation estimates are very similar. In the right-hand panel 

208 5. Resampling Methods 

![Figure 5.6](./img/5_6.png)

**FIGURE 5.6.** _True and estimated test MSE for the simulated data sets in Figures 2.9 (_ left _), 2.10 (_ center _), and 2.11 (_ right _). The true test MSE is shown in blue, the LOOCV estimate is shown as a black dashed line, and the_ 10 _-fold CV estimate is shown in orange. The crosses indicate the minimum of each of the MSE curves._ 

of Figure 5.6, the true test MSE and the cross-validation curves are almost identical. In the center panel of Figure 5.6, the two sets of curves are similar at the lower degrees of flexibility, while the CV curves overestimate the test set MSE for higher degrees of flexibility. In the left-hand panel of Figure 5.6, the CV curves have the correct general shape, but they underestimate the true test MSE. 

When we perform cross-validation, our goal might be to determine how well a given statistical learning procedure can be expected to perform on independent data; in this case, the actual estimate of the test MSE is of interest. But at other times we are interested only in the location of the _minimum point in the estimated test MSE curve_ . This is because we might be performing cross-validation on a number of statistical learning methods, or on a single method using different levels of flexibility, in order to identify the method that results in the lowest test error. For this purpose, the location of the minimum point in the estimated test MSE curve is important, but the actual value of the estimated test MSE is not. We find in Figure 5.6 that despite the fact that they sometimes underestimate the true test MSE, all of the CV curves come close to identifying the correct level of flexibility—that is, the flexibility level corresponding to the smallest test MSE. 

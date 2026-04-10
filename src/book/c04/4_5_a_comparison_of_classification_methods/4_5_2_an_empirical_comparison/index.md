---
layout: default
title: "index"
---

# _4.5.2 An Empirical Comparison_ 

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN. We generated data from six different scenarios, each of which involves a binary (two-class) classification problem. In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. For each scenario, we produced 100 random training data sets. On each of these training sets, we fit each method to the data and computed the resulting test error rate on a large test set. Results for the linear scenarios are shown in Figure 4.11, and the results for the non-linear scenarios are in Figure 4.12. The KNN method requires selection of $K$ , the number of neighbors (not to be confused with the number of classes in earlier sections of this chapter). We performed KNN with two values of $K$ : $K$ = 1, and a value of $K$ that was chosen automatically using an approach called _cross-validation_ , which we discuss further in Chapter 5. We applied naive Bayes assuming univariate Gaussian densities for the features within each class (and, of course — since this is the key characteristic of naive Bayes — assuming independence of the features). 

In each of the six scenarios, there were _p_ = 2 quantitative predictors. The scenarios were as follows: 

4.5 A Comparison of Classification Methods 165 

![Figure 4.11](./img/4_11.png)

**FIGURE 4.11.** _Boxplots of the test error rates for each of the linear scenarios described in the main text._ 

_Scenario 1:_ There were 20 training observations in each of two classes. The observations within each class were uncorrelated random normal variables with a different mean in each class. The left-hand panel of Figure 4.11 shows that LDA performed well in this setting, as one would expect since this is the model assumed by LDA. Logistic regression also performed quite well, since it assumes a linear decision boundary. KNN performed poorly because it paid a price in terms of variance that was not offset by a reduction in bias. QDA also performed worse than LDA, since it fit a more flexible classifier than necessary. The performance of naive Bayes was slightly better than QDA, because the naive Bayes assumption of independent predictors is correct. 

_Scenario 2:_ Details are as in Scenario 1, except that within each class, the two predictors had a correlation of _−_ 0 _._ 5. The center panel of Figure 4.11 indicates that the performance of most methods is similar to the previous scenario. The notable exception is naive Bayes, which performs very poorly here, since the naive Bayes assumption of independent predictors is violated. 

_Scenario 3:_ As in the previous scenario, there is substantial negative correlation between the predictors within each class. However, this time we generated $X_1$ and $X_2$ from the _t-distribution_ , with 50 observations per class. _t_ - The _t_ -distribution has a similar shape to the normal distribution, but it has a tendency to yield more extreme points—that is, more points that are far from the mean. In this setting, the decision boundary was still linear, and so fit into the logistic regression framework. The set-up violated the assumptions of LDA, since the observations were not drawn from a normal distribution. The right-hand panel of Figure 4.11 shows that logistic regression outperformed LDA, though both methods were superior to the other approaches. In particular, the QDA results deteriorated considerably as a consequence of non-normality. Naive Bayes performed very poorly because the independence assumption is violated. 

distribution 

_Scenario 4:_ The data were generated from a normal distribution, with a correlation of 0 _._ 5 between the predictors in the first class, and correlation of _−_ 0 _._ 5 between the predictors in the second class. This setup corresponded to the QDA assumption, and resulted in quadratic decision boundaries. The left-hand panel of Figure 4.12 shows that QDA outperformed all of the 

166 4. Classification 

![Figure 4.12](./img/4_12.png)

**FIGURE 4.12.** _Boxplots of the test error rates for each of the non-linear scenarios described in the main text._ 

other approaches. The naive Bayes assumption of independent predictors is violated, so naive Bayes performs poorly. 

_Scenario 5:_ The data were generated from a normal distribution with uncorrelated predictors. Then the responses were sampled from the logistic function applied to a complicated non-linear function of the predictors. The center panel of Figure 4.12 shows that both QDA and naive Bayes gave slightly better results than the linear methods, while the much more flexible KNN-CV method gave the best results. But KNN with $K$ = 1 gave the worst results out of all methods. This highlights the fact that even when the data exhibits a complex non-linear relationship, a non-parametric method such as KNN can still give poor results if the level of smoothness is not chosen correctly. 

_Scenario 6:_ The observations were generated from a normal distribution with a different diagonal covariance matrix for each class. However, the sample size was _very_ small: just _n_ = 6 in each class. Naive Bayes performed very well, because its assumptions are met. LDA and logistic regression performed poorly because the true decision boundary is non-linear, due to the unequal covariance matrices. QDA performed a bit worse than naive Bayes, because given the very small sample size, the former incurred too much variance in estimating the correlation between the predictors within each class. KNN’s performance also suffered due to the very small sample size. 

These six examples illustrate that no one method will dominate the others in every situation. When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well. When the boundaries are moderately non-linear, QDA or naive Bayes may give better results. Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior. But the level of smoothness for a non-parametric approach must be chosen carefully. In the next chapter we examine a number of approaches for choosing the correct level of smoothness and, in general, for selecting the best overall method. 

Finally, recall from Chapter 3 that in the regression setting we can accommodate a non-linear relationship between the predictors and the response by performing regression using transformations of the predictors. A similar approach could be taken in the classification setting. For instance, we could 

4.6 Generalized Linear Models 167 

||Coefcient Std. error|Coefcient Std. error|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|73.60|5.13|14.34|0.00|
|`workingday`|1.27|1.78|0.71|0.48|
|`temp`|157.21|10.26|15.32|0.00|
|`weathersit[cloudy/misty]`|-12.89|1.96|-6.56|0.00|
|`weathersit[light rain/snow]`|-66.49|2.97|-22.43|0.00|
|`weathersit[heavy rain/snow]`|-109.75|76.67|-1.43|0.15|



**TABLE 4.10.** _Results for a least squares linear model fit to predict_ `bikers` _in the_ `Bikeshare` _data. The predictors_ `mnth` _and_ `hr` _are omitted from this table due to space constraints, and can be seen in Figure 4.13. For the qualitative variable_ `weathersit` _, the baseline level corresponds to clear skies._ 

create a more flexible version of logistic regression by including _X_[2] , _X_[3] , and even _X_[4] as predictors. This may or may not improve logistic regression’s performance, depending on whether the increase in variance due to the added flexibility is offset by a sufficiently large reduction in bias. We could do the same for LDA. If we added all possible quadratic terms and cross-products to LDA, the form of the model would be the same as the QDA model, although the parameter estimates would be different. This device allows us to move somewhere between an LDA and a QDA model. 

---
layout: default
title: "index"
---

# _4.4.4 Naive Bayes_ 

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers. Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier. 

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability _pk_ ( _x_ ) = Pr( $Y=$ _k|X_ = _x_ ) in terms of _π_ 1 _, . . . , πK_ and _f_ 1( _x_ ) _, . . . , fK_ ( _x_ ). To use (4.15) in practice, we need estimates for _π_ 1 _, . . . , πK_ and _f_ 1( _x_ ) _, . . . , fK_ ( _x_ ). As we saw in previous sections, estimating the prior probabilities _π_ 1 _, . . . , πK_ is typically straightforward: for instance, we can estimate _π_ ˆ $k$ as the proportion of training observations belonging to the $k$ th class, for $k$ = 1 _, . . . , K_ . 

However, estimating _f_ 1( _x_ ) _, . . . , fK_ ( _x_ ) is more subtle. Recall that _fk_ ( _x_ ) is the _p_ -dimensional density function for an observation in the $k$ th class, for $k$ = 1 _, . . . , K_ . In general, estimating a _p_ -dimensional density function is challenging. In LDA, we make a very strong assumption that greatly simplifies the task: we assume that _fk_ is the density function for a multivariate normal random variable with class-specific mean _µk_ , and shared covariance matrix **Σ** . By contrast, in QDA, we assume that _fk_ is the density function for a multivariate normal random variable with class-specific mean _µk_ , and class-specific covariance matrix **Σ** $k$ . By making these very strong assumptions, we are able to replace the very challenging problem of estimating _K p_ -dimensional density functions with the much simpler problem of estimating _K p_ -dimensional mean vectors and one (in the case of LDA) or $K$ (in the case of QDA) ( _p × p_ )-dimensional covariance matrices. 

The naive Bayes classifier takes a different tack for estimating _f_ 1( _x_ ) _, . . . , fK_ ( _x_ ). Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single assumption: 

naive Bayes 

_Within the kth class, the p predictors are independent._ 

Stated mathematically, this assumption means that for $k$ = 1 _, . . . , K_ , 

_fk_ ( _x_ ) = _fk_ 1( _x_ 1) _× fk_ 2( _x_ 2) _× · · · × fkp_ ( _xp_ ) _,_ (4.29) 

where _fkj_ is the density function of the $j$ th predictor among observations in the $k$ th class. 

Why is this assumption so powerful? Essentially, estimating a _p_ -dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of marginal each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors. In the case of joint a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix. However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate. But by assuming that the _p_ covariates are independent within each class, we completely eliminate the need to worry about the association between the _p_ predictors, because we have simply assumed that there is _no_ association between the predictors! 

distribution joint distribution 

Do we really believe the naive Bayes assumption that the _p_ covariates are independent within each class? In most settings, we do not. But even though this modeling assumption is made for convenience, it often leads to 

4.4 Generative Models for Classification 159 

pretty decent results, especially in settings where _n_ is not large enough relative to _p_ for us to effectively estimate the joint distribution of the predictors within each class. In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings. Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off. 

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability, 



for $k$ = 1 _, . . . , K_ . 

To estimate the one-dimensional density function _fkj_ using training data _x_ 1 _j, . . . , xnj_ , we have a few options. 

- If _Xj_ is quantitative, then we can assume that _Xj|Y_ = _k ∼ N_ ( _µjk, σjk_[2][)][.] In other words, we assume that within each class, the $j$ th predictor is drawn from a (univariate) normal distribution. While this may sound a bit like QDA, there is one key difference, in that here we are assuming that the predictors are independent; this amounts to QDA with an additional assumption that the class-specific covariance matrix is diagonal. 

- If _Xj_ is quantitative, then another option is to use a non-parametric estimate for _fkj_ . A very simple way to do this is by making a histogram for the observations of the $j$ th predictor within each class. Then we can estimate _fkj_ ( _xj_ ) as the fraction of the training observations in the $k$ th class that belong to the same histogram bin as _xj_ . Alternatively, we can use a _kernel density estimator_ , which is kernel essentially a smoothed version of a histogram. 

   - density estimator 

- If _Xj_ is qualitative, then we can simply count the proportion of training observations for the $j$ th predictor corresponding to each class. For instance, suppose that _Xj ∈{_ 1 _,_ 2 _,_ 3 _}_ , and we have 100 observations in the $k$ th class. Suppose that the $j$ th predictor takes on values of 1, 2, and 3 in 32, 55, and 13 of those observations, respectively. Then we can estimate _fkj_ as 



We now consider the naive Bayes classifier in a toy example with _p_ = 3 predictors and $K$ = 2 classes. The first two predictors are quantitative, and the third predictor is qualitative with three levels. Suppose further ˆ ˆ that _π_ 1 = _π_ 2 = 0 _._ 5. The estimated density functions _f_[ˆ] _kj_ for $k$ = 1 _,_ 2 and $j$ = 1 _,_ 2 _,_ 3 are displayed in Figure 4.10. Now suppose that we wish to classify a new observation, _x[∗]_ = (0 _._ 4 _,_ 1 _._ 5 _,_ 1) _[T]_ . It turns out that in this 

4. Classification 

160 



![Figure 4.10](./img/4_10.png)

**FIGURE 4.10.** _In the toy example in Section 4.4.4, we generate data with p_ = 3 _predictors and K_ = 2 _classes. The first two predictors are quantitative, and the third predictor is qualitative with three levels. In each class, the estimated density for each of the three predictors is displayed. If the prior probabilities for the two classes are equal, then the observation x[∗]_ = (0 _._ 4 _,_ 1 _._ 5 _,_ 1) _[T] has a_ 94 _._ 4% _posterior probability of belonging to the first class._ 

|||_True default status_<br>No<br>Yes<br>Total|_True default status_<br>No<br>Yes<br>Total|
|---|---|---|---|
|_Predicted_<br>_default status_|No<br>Yes|9621<br>244<br>46<br>89|9865<br>135|
||Total|9667<br>333|10000|



**TABLE 4.8.** _Comparison of the naive Bayes predictions to the true default status for the_ 10 _,_ 000 _training observations in the_ `Default` _data set, when we predict default for any observation for which P_ ( $Y=$ default _|X_ = _x_ ) _>_ 0 _._ 5 _._ 

example, _f_[ˆ] 11(0 _._ 4) = 0 _._ 368, _f_[ˆ] 12(1 _._ 5) = 0 _._ 484, _f_[ˆ] 13(1) = 0 _._ 226, and _f_[ˆ] 21(0 _._ 4) = 0 _._ 030, _f_[ˆ] 22(1 _._ 5) = 0 _._ 130, _f_[ˆ] 23(1) = 0 _._ 616. Plugging these estimates into (4.30) results in posterior probability estimates of Pr( $Y=$ 1 _|X_ = _x[∗]_ ) = 0 _._ 944 and Pr( $Y=$ 2 _|X_ = _x[∗]_ ) = 0 _._ 056. 

Table 4.8 provides the confusion matrix resulting from applying the naive Bayes classifier to the `Default` data set, where we predict a default if the posterior probability of a default — that is, _P_ ( $Y=$ default _|X_ = _x_ ) — exceeds 0 _._ 5. Comparing this to the results for LDA in Table 4.4, our findings are mixed. While LDA has a slightly lower overall error rate, naive Bayes 

4.5 A Comparison of Classification Methods 

161 

|||_True default status_<br>No<br>Yes<br>Total|_True default status_<br>No<br>Yes<br>Total|
|---|---|---|---|
|_Predicted_<br>_default status_|No<br>Yes|9339<br>130<br>328<br>203|9469<br>531|
||Total|9667<br>333|10000|



**TABLE 4.9.** _Comparison of the naive Bayes predictions to the true default status for the_ 10 _,_ 000 _training observations in the_ `Default` _data set, when we predict default for any observation for which P_ ( $Y=$ default _|X_ = _x_ ) _>_ 0 _._ 2 _._ 

correctly predicts a higher fraction of the true defaulters. In this implementation of naive Bayes, we have assumed that each quantitative predictor is drawn from a Gaussian distribution (and, of course, that within each class, each predictor is independent). 

Just as with LDA, we can easily adjust the probability threshold for predicting a default. For example, Table 4.9 provides the confusion matrix resulting from predicting a default if _P_ ( $Y=$ default _|X_ = _x_ ) _>_ 0 _._ 2. Again, the results are mixed relative to LDA with the same threshold (Table 4.5). Naive Bayes has a higher error rate, but correctly predicts almost two-thirds of the true defaults. 

In this example, it should not be too surprising that naive Bayes does not convincingly outperform LDA: this data set has _n_ = 10 _,_ 000 and _p_ = 2, and so the reduction in variance resulting from the naive Bayes assumption is not necessarily worthwhile. We expect to see a greater pay-off to using naive Bayes relative to LDA or QDA in instances where _p_ is larger or _n_ is smaller, so that reducing the variance is very important. 

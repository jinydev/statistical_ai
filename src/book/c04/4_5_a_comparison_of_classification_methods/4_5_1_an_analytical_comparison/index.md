---
layout: default
title: "index"
---

# _4.5.1 An Analytical Comparison_ 

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression. We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes Pr( $Y=$ _k|X_ = _x_ ). Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes 



for $k$ = 1 _, . . . , K_ . Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences. 

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared co- 

162 4. Classification 

variance matrix in order to show that 



where _ak_ = log � _ππKk_ � _−_[1] 2[(] _[µ][k]_[+] _[µ][K]_[)] _[T]_ **[ Σ]** _[−]_[1][(] _[µ][k][−][µ][K]_[)][and] _[b][kj]_[is][the] _[j]_[th] component of **Σ** _[−]_[1] ( _µk − µK_ ). Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in _x_ . Using similar calculations, in the QDA setting (4.31) becomes 



where _ak, bkj_ , and _ckjl_ are functions of _πk, πK, µk, µK,_ **Σ** $k$ and **Σ** $K$ . Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in _x_ . 

Finally, we examine (4.31) in the naive Bayes setting. Recall that in this setting, _fk_ ( _x_ ) is modeled as a product of _p_ one-dimensional functions _fkj_ ( _xj_ ) for $j$ = 1 _, . . . , p_ . Hence, 



where _ak_ = log � _ππKk_ � and _gkj_ ( _xj_ ) = log � _ffKjkj_ (( _xxjj_ )) �. Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_ , a topic that is discussed further in Chapter 7. 

4.5 A Comparison of Classification Methods 163 

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes: 

- LDA is a special case of QDA with _ckjl_ = 0 for all $j$ = 1 _, . . . , p_ , _l_ = 1 _, . . . , p_ , and $k$ = 1 _, . . . , K_ . (Of course, this is not surprising, since LDA is simply a restricted version of QDA with **Σ** 1 = _· · ·_ = **Σ** $K$ = **Σ** .) 

- Any classifier with a linear decision boundary is a special case of naive Bayes with _gkj_ ( _xj_ ) = _bkjxj_ . In particular, this means that LDA is a special case of naive Bayes! This is not at all obvious from the descriptions of LDA and naive Bayes earlier in this chapter, since each method makes very different assumptions: LDA assumes that the features are normally distributed with a common within-class covariance matrix, and naive Bayes instead assumes independence of the features. 

- If we model _fkj_ ( _xj_ ) in the naive Bayes classifier using a one-dimensional Gaussian distribution _N_ ( _µkj, σj_[2][)][, then we end up with] _[ g][kj]_[(] _[x][j]_[) =] _bkjxj_ where _bkj_ = ( _µkj −µKj_ ) _/σj_[2][. In this case, naive Bayes is actually] a special case of LDA with **Σ** restricted to be a diagonal matrix with $j$ th diagonal element equal to _σj_[2][.] 

- Neither QDA nor naive Bayes is a special case of the other. Naive Bayes can produce a more flexible fit, since any choice can be made for _gkj_ ( _xj_ ). However, it is restricted to a purely _additive_ fit, in the sense that in (4.34), a function of _xj_ is _added_ to a function of _xl_ , for $j$ = _l_ ; however, these terms are never multiplied. By contrast, QDA includes multiplicative terms of the form _ckjlxjxl_ . Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important in discriminating between classes. 

None of these methods uniformly dominates the others: in any setting, the choice of method will depend on the true distribution of the predictors in each of the $K$ classes, as well as other considerations, such as the values of _n_ and _p_ . The latter ties into the bias-variance trade-off. 

How does logistic regression tie into this story? Recall from (4.12) that multinomial logistic regression takes the form 



This is identical to the linear form of LDA (4.32): in both cases, Pr( $Y=$ _k|X_ = _x_ ) log � Pr( $Y=$ _K|X_ = _x_ ) � is a linear function of the predictors. In LDA, the coefficients in this linear function are functions of estimates for _πk_ , _πK_ , _µk_ , _µ_ bution within each class. By contrast, in logistic regression, the coefficients $K$ , and **Σ** obtained by assuming that $X_1$ _, . . . , Xp_ follow a normal distriare chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not. 

164 4. Classification 

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. In order to make a prediction for an observation $X$= _x_ , the training observations that are closest to _x_ are identified. Then $X$is assigned to the class to which the plurality of these observations belong. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary. We make the following observations about KNN: 

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that _n_ is very large and _p_ is small. 

- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors—that is, _n_ much larger than _p_ . This has to do with the fact that KNN is non-parametric, and thus tends to reduce the bias while incurring a lot of variance. 

- In settings where the decision boundary is non-linear but _n_ is only modest, or _p_ is not very small, then QDA may be preferred to KNN. This is because QDA can provide a non-linear decision boundary while taking advantage of a parametric form, which means that it requires a smaller sample size for accurate classification, relative to KNN. 

- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients as in Table 4.3. 

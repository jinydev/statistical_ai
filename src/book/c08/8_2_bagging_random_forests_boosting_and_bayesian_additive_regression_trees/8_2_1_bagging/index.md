---
layout: default
title: "index"
---

# _8.2.1 Bagging_ 

The bootstrap, introduced in Chapter 5, is an extremely powerful idea. It is used in many situations in which it is hard or even impossible to directly compute the standard deviation of a quantity of interest. We see here that the bootstrap can be used in a completely different context, in order to improve statistical learning methods such as decision trees. 

The decision trees discussed in Section 8.1 suffer from _high variance_ . This means that if we split the training data into two parts at random, and fit a decision tree to both halves, the results that we get could be quite different. In contrast, a procedure with _low variance_ will yield similar results if applied repeatedly to distinct data sets; linear regression tends to have low variance, if the ratio of _n_ to _p_ is moderately large. _Bootstrap aggregation_ , or _bagging_ , is a general-purpose procedure for reducing the bagging variance of a statistical learning method; we introduce it here because it is particularly useful and frequently used in the context of decision trees. 

Recall that given a set of _n_ independent observations _Z_ 1 _, . . . , Zn_ , each with variance _σ_[2] , the variance of the mean _Z_[¯] of the observations is given by _σ_[2] _/n_ . In other words, _averaging a set of observations reduces variance_ . Hence a natural way to reduce the variance and increase the test set accuracy of a statistical learning method is to take many training sets from the population, build a separate prediction model using each training set, and _f_ ˆ[1] ( _x_ )average _, f_ ˆ[2] ( _x_ ) _, . . . ,_ the resulting _f_ ˆ _[B]_ ( _x_ ) usingpredictions. _B_ separateIn trainingother words,sets, weandcouldaveragecalculatethem in order to obtain a single low-variance statistical learning model, given by

$$
\hat{f}_{\text{avg}}(x) = \frac{1}{B} \sum_{b=1}^B \hat{f}^b(x)
$$


Of course, this is not practical because we generally do not have access to multiple training sets. Instead, we can bootstrap, by taking repeated samples from the (single) training data set. In this approach we generate _B_ different bootstrapped training data sets. We then train our method on the _b_ th bootstrapped training set in order to get _f_[ˆ] _[∗][b]_ ( _x_ ), and finally average all the predictions, to obtain

$$
\hat{f}_{\text{bag}}(x) = \frac{1}{B} \sum_{b=1}^B \hat{f}^{*b}(x)
$$


344 8. Tree-Based Methods 

![Figure 8.8](./img/8_8.png)

**FIGURE 8.8.** _Bagging and random forest results for the_ `Heart` _data. The test error (black and orange) is shown as a function of B, the number of bootstrapped training sets used. Random forests were applied with m_ = _[√] p. The dashed line indicates the test error resulting from a single classification tree. The green and blue traces show the OOB error, which in this case is — by chance — considerably lower._ 

This is called bagging. 

While bagging can improve predictions for many regression methods, it is particularly useful for decision trees. To apply bagging to regression trees, we simply construct _B_ regression trees using _B_ bootstrapped training sets, and average the resulting predictions. These trees are grown deep, and are not pruned. Hence each individual tree has high variance, but low bias. Averaging these _B_ trees reduces the variance. Bagging has been demonstrated to give impressive improvements in accuracy by combining together hundreds or even thousands of trees into a single procedure. 

Thus far, we have described the bagging procedure in the regression context, to predict a quantitative outcome _Y_ . How can bagging be extended to a classification problem where _Y_ is qualitative? In that situation, there are a few possible approaches, but the simplest is as follows. For a given test observation, we can record the class predicted by each of the _B_ trees, and take a _majority vote_ : the overall prediction is the most commonly occurring majority class among the _B_ predictions. 

vote 

Figure 8.8 shows the results from bagging trees on the `Heart` data. The test error rate is shown as a function of _B_ , the number of trees constructed using bootstrapped training data sets. We see that the bagging test error rate is slightly lower in this case than the test error rate obtained from a single tree. The number of trees _B_ is not a critical parameter with bagging; using a very large value of _B_ will not lead to overfitting. In practice we 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

345 

use a value of _B_ sufficiently large that the error has settled down. Using _B_ = 100 is sufficient to achieve good performance in this example. 

---

## Sub-Chapters (하위 목차)

### Out-of-Bag Error Estimation (OOB 오차 추정)
* [문서로 이동하기](./8_2_1_1_out-of-bag_error_estimation/)

배깅의 부트스트랩 과정에서 추출되지 않은 남은 1/3의 관측치들을 이용해 마치 교차 검증을 한 것처럼 모델 테스트 오차를 가볍게 계산하는 요령입니다.

### Variable Importance Measures (변수 중요도 측정)
* [문서로 이동하기](./8_2_1_2_variable_importance_measures/)

앙상블로 묶여 해석력이 떨어진 블랙박스 모형 안에서, 특정 변수가 지니 불순도와 RSS를 얼마나 누적 감소시켰는지 측정하여 변수의 기여도를 랭킹 매기는 지표입니다.

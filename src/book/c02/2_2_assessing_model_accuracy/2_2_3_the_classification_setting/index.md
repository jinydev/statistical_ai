---
layout: default
title: "index"
---

# _2.2.3 The Classification Setting_ 

Thus far, our discussion of model accuracy has been focused on the regression setting. But many of the concepts that we have encountered, such as the bias-variance trade-off, transfer over to the classification setting with only some modifications due to the fact that _yi_ is no longer quantitative. Suppose that we seek to estimate _f_ on the basis of training observations _{_ ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) _}_ , where now _y_ 1 _, . . . , yn_ are qualitative. The most common approach for quantifying the accuracy of our estimate _f_[ˆ] is the training _error rate_ , the proportion of mistakes that are made if we apply error rate 

2.2 Assessing Model Accuracy 35 

our estimate _f_[ˆ] to the training observations: 

$$ \frac{1}{n} \sum_{i=1}^n I(y_i \neq \hat{y}_i) \tag{2.8} $$

Here _y_ ˆ _i_ is the predicted class label for the _i_ th observation using _f_[ˆ] . And ˆ ˆ ˆ _I_ ( _yi_ = _yi_ ) is an _indicator variable_ that equals 1 if _yi_ = _yi_ and zero if _yi_ = _yi_ . ˆ indicator If _I_ ( _yi_ = _yi_ ) = 0 then the _i_ th observation was classified correctly by our variable classification method; otherwise it was misclassified. Hence Equation 2.8 computes the fraction of incorrect classifications. 

Equation 2.8 is referred to as the _training error_ rate because it is com- training puted based on the data that was used to train our classifier. As in the error regression setting, we are most interested in the error rates that result from applying our classifier to test observations that were not used in training. The _test error_ rate associated with a set of test observations of the form test error ( _x_ 0 _, y_ 0) is given by 

$$ \text{Ave}(I(y_0 \neq \hat{y}_0)) \tag{2.9} $$

where _y_ ˆ0 is the predicted class label that results from applying the classifier to the test observation with predictor _x_ 0. A _good_ classifier is one for which the test error (2.9) is smallest. 

The Bayes Classifier 

It is possible to show (though the proof is outside of the scope of this book) that the test error rate given in (2.9) is minimized, on average, by a very simple classifier that _assigns each observation to the most likely class, given its predictor values_ . In other words, we should simply assign a test observation with predictor vector _x_ 0 to the class _j_ for which 

$$ Pr(Y = j|X = x_0) \tag{2.10} $$

is largest. Note that (2.10) is a _conditional probability_ : it is the probability conditional that _Y_ = _j_ , given the observed predictor vector _x_ 0. This very simple clasprobability sifier is called the _Bayes classifier_ . In a two-class problem where there are Bayes only two possible response values, say _class 1_ or _class 2_ , the Bayes classifier classifier corresponds to predicting class one if Pr( _Y_ = 1 _|X_ = _x_ 0) _>_ 0 _._ 5, and class two otherwise. 

Figure 2.13 provides an example using a simulated data set in a twodimensional space consisting of predictors _X_ 1 and _X_ 2. The orange and blue circles correspond to training observations that belong to two different classes. For each value of _X_ 1 and _X_ 2, there is a different probability of the response being orange or blue. Since this is simulated data, we know how the data were generated and we can calculate the conditional probabilities for each value of _X_ 1 and _X_ 2. The orange shaded region reflects the set of points for which Pr( _Y_ = orange _|X_ ) is greater than 50 %, while the blue shaded region indicates the set of points for which the probability is below 50 %. The purple dashed line represents the points where the probability is exactly 50 %. This is called the _Bayes decision boundary_ . The Bayes Bayes classifier’s prediction is determined by the Bayes decision boundary; an observation that falls on the orange side of the boundary will be assigned 

decision boundary 

36 2. Statistical Learning 

![Figure 2.13](./img/Image_027.png)

**FIGURE 2.13.** _A simulated data set consisting of_ 100 _observations in each of two groups, indicated in blue and in orange. The purple dashed line represents the Bayes decision boundary. The orange background grid indicates the region in which a test observation will be assigned to the orange class, and the blue background grid indicates the region in which a test observation will be assigned to the blue class._ 

to the orange class, and similarly an observation on the blue side of the boundary will be assigned to the blue class. 

The Bayes classifier produces the lowest possible test error rate, called the _Bayes error rate_. Since the Bayes classifier will always choose the class for which (2.10) is largest, the error rate will be $1 - \max_j Pr(Y=j | X=x_0)$ at $X=x_0$. In general, the overall Bayes error rate is given by

$$ 1 - E(\max_j Pr(Y=j|X)) \tag{2.11} $$

where the expectation averages the probability over all possible values of _X_ . For our simulated data, the Bayes error rate is 0 _._ 133. It is greater than zero, because the classes overlap in the true population, which implies that max _j_ Pr( _Y_ = _j|X_ = _x_ 0) _<_ 1 for some values of _x_ 0. The Bayes error rate is analogous to the irreducible error, discussed earlier. 

---

## Sub-Chapters (하위 목차)

### K-Nearest Neighbors (K-최근접 이웃)
* [문서로 이동하기](./2_2_3_1_k_nearest_neighbors/)

비모수적인 분류 환경에서 이론의 실제 구현체로 가장 직관적인 알고리즘인 K-최근접 이웃(KNN) 기법을 학습합니다.
K 값의 크기 변화에 따라 결정 경계(Decision Boundary)가 어떻게 바뀌며, 그 과정 속 편향-분산 트레이드오프가 나타나는지를 배웁니다.

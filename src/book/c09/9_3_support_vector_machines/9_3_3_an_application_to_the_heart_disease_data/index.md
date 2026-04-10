---
layout: default
title: "index"
---

# _9.3.3 An Application to the Heart Disease Data_ 

In Chapter 8 we apply decision trees and related methods to the `Heart` data. The aim is to use 13 predictors such as `Age` , `Sex` , and `Chol` in order to predict whether an individual has heart disease. We now investigate how an SVM compares to LDA on this data. After removing 6 missing observations, the data consist of 297 subjects, which we randomly split into 207 training and 90 test observations. 

We first fit LDA and the support vector classifier to the training data. Note that the support vector classifier is equivalent to an SVM using a polynomial kernel of degree _d_ = 1. The left-hand panel of Figure 9.10 displays ROC curves (described in Section 4.4.2) for the training set predictions for both LDA and the support vector classifier. Both classifiers compute scores of the form _f_[ˆ] ( _X_ ) = _β_[ˆ] 0 + _β_[ˆ] 1 _X_ 1 + _β_[ˆ] 2 _X_ 2 + _· · ·_ + _β_[ˆ] _pXp_ for each observation. For any given cutoff _t_ , we classify observations into the _heart disease_ or _no heart disease_ categories depending on whether _f_[ˆ] ( _X_ ) _< t_ or _f_[ˆ] ( _X_ ) _≥ t_ . The ROC curve is obtained by forming these predictions and computing the false positive and true positive rates for a range of values of _t_ . An optimal classifier will hug the top left corner of the ROC plot. In this instance 

9.4 SVMs with More than Two Classes 383 

![Figure 9.11](./img/9_11.png)

**FIGURE 9.11.** _ROC curves for the test set of the_ `Heart` _data._ Left: _The support vector classifier and LDA are compared._ Right: _The support vector classifier is compared to an SVM using a radial basis kernel with γ_ = 10 _[−]_[3] _,_ 10 _[−]_[2] _, and_ 10 _[−]_[1] _._ 

LDA and the support vector classifier both perform well, though there is a suggestion that the support vector classifier may be slightly superior. 

The right-hand panel of Figure 9.10 displays ROC curves for SVMs using a radial kernel, with various values of _γ_ . As _γ_ increases and the fit becomes more non-linear, the ROC curves improve. Using _γ_ = 10 _[−]_[1] appears to give an almost perfect ROC curve. However, these curves represent training error rates, which can be misleading in terms of performance on new test data. Figure 9.11 displays ROC curves computed on the 90 test observations. We observe some differences from the training ROC curves. In the left-hand panel of Figure 9.11, the support vector classifier appears to have a small advantage over LDA (although these differences are not statistically significant). In the right-hand panel, the SVM using _γ_ = 10 _[−]_[1] , which showed the best results on the training data, produces the worst estimates on the test data. This is once again evidence that while a more flexible method will often produce lower training error rates, this does not necessarily lead to improved performance on test data. The SVMs with _γ_ = 10 _[−]_[2] and _γ_ = 10 _[−]_[3] perform comparably to the support vector classifier, and all three outperform the SVM with _γ_ = 10 _[−]_[1] . 

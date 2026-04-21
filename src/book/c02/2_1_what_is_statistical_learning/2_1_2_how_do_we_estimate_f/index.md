---
layout: default
title: "index"
---

[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/index.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2.1.2 How Do We Estimate _f_?

Throughout this book, we explore many linear and non-linear approaches for estimating _f_. We provide an overview of these shared characteristics in this section.

We will always assume that we have observed a set of _n_ different data points. For example in Figure 2.2 we observed _n_ = 30 data points. These observations are called the _training data_ because we will use these training observations to train, or teach, our method how to estimate _f_. Let $x_{ij}$ represent the value of the _j_ th predictor, or input, for observation _i_, where $i = 1, 2, \dots, n$ and $j = 1, 2, \dots, p$. Correspondingly, let $y_i$ represent the response variable for the _i_ th observation. Then our training data consist of $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ where $x_i = (x_{i1}, x_{i2}, \dots, x_{ip})^T$.

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function _f_. In other words, we want to find a function $\hat{f}$ such that $Y pprox \hat{f}(X)$ for any observation $(X, Y)$. Broadly speaking, most statistical learning methods for this task can be characterized as either _parametric_ or _non-parametric_. We now briefly discuss these two types of approaches.

---

### Parametric Methods

First assumes the shape of the function (e.g. linearity) and fits the model by estimating a limited set of parameters.

### Non-Parametric Methods

Methods that proceed with fitting to match the data points as closely as possible without making specific assumptions about the form of the function $f$.

---

## Sub-Chapters


[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/index.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/index.html)

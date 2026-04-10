---
layout: default
title: "index"
---

# _2.1.2 How Do We Estimate f ?_ 

Throughout this book, we explore many linear and non-linear approaches for estimating _f_ . However, these methods generally share certain characteristics. We provide an overview of these shared characteristics in this section. We will always assume that we have observed a set of _n_ different data points. For example in Figure 2.2 we observed _n_ = 30 data points. These observations are called the _training data_ because we will use these training observations to train, or teach, our method how to estimate _f_ . Let _xij_ data represent the value of the _j_ th predictor, or input, for observation _i_ , where _i_ = 1 _,_ 2 _, . . . , n_ and _j_ = 1 _,_ 2 _, . . . , p_ . Correspondingly, let _yi_ represent the response variable for the _i_ th observation. Then our training data consist of _{_ ( _x_ 1 _, y_ 1) _,_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ ) _}_ where _xi_ = ( _xi_ 1 _, xi_ 2 _, . . . , xip_ ) _[T]_ . 

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function _f_ . In other words, we want to find a function _f_[ˆ] such that _Y ≈ f_[ˆ] ( _X_ ) for any observation ( _X, Y_ ). Broadly speaking, most statistical learning methods for this task can be characterized as either _parametric_ or _non-parametric_ . We now briefly discuss these parametric two types of approaches. 

nonparametric 

---

## Sub-Chapters (하위 목차)

### Parametric Methods (모수적 방법론)
* [문서로 이동하기](./2_1_2_1_parametric_methods/)

먼저 함수의 형태(Shape)를 가정(예: 선형성)하고 한정된 파라미터를 추정하여 모델을 적합시키는 방법입니다.
계산이 빠르고 해석이 쉬운 장점이 있지만 실제 데이터의 형태와 가정된 형태가 크게 다를 수 있다는 단점을 지닙니다.

### Non-Parametric Methods (비모수적 방법론)
* [문서로 이동하기](./2_1_2_2_non-parametric_methods/)

함수 $f$의 형태에 특별한 가정을 두지 않고, 데이터 점들에 최대한 근접하도록 적합을 진행하는 방법론들입니다.
데이터를 매우 유연하게 묘사할 수 있으나 유의미한 분석을 위해선 훨씬 방대한 양의 데이터가 필요함을 배웁니다.

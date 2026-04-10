---
layout: default
title: "index"
---

# 7.6 Local Regression 

_Local regression_ is a different approach for fitting flexible non-linear func- local tions, which involves computing the fit at a target point _x_ 0 using only the nearby training observations. Figure 7.9 illustrates the idea on some simulated data, with one target point near 0 _._ 4, and another near the boundary at 0 _._ 05. In this figure the blue line represents the function _f_ ( _x_ ) from which the data were generated, and the light orange line corresponds to the local regression estimate _f_[ˆ] ( _x_ ). Local regression is described in Algorithm 7.1. Note that in Step 3 of Algorithm 7.1, the weights _Ki_ 0 will differ for each value of _x_ 0. In other words, in order to obtain the local regression fit at a new point, we need to fit a new weighted least squares regression model by minimizing (7.14) for a new set of weights. Local regression is sometimes referred to as a _memory-based_ procedure, because like nearest-neighbors, we need all the training data each time we wish to compute a prediction. We will avoid getting into the technical details of local regression here—there are books written on the topic. 

regression 

In order to perform local regression, there are a number of choices to be made, such as how to define the weighting function _K_ , and whether to fit a linear, constant, or quadratic regression in Step 3. (Equation 7.14 corresponds to a linear regression.) While all of these choices make some difference, the most important choice is the _span s_ , which is the proportion of points used to compute the local regression at _x_ 0, as defined in Step 1 above. The span plays a role like that of the tuning parameter _λ_ in smooth- 

304 7. Moving Beyond Linearity 

![Figure 7.9](./img/7_9.png)

**FIGURE 7.9.** _Local regression illustrated on some simulated data, where the blue curve represents f_ ( _x_ ) _from which the data were generated, and the light orange curve corresponds to the local regression estimate f_[ˆ] ( _x_ ) _. The orange colored points are local to the target point x_ 0 _, represented by the orange vertical line. The yellow bell-shape superimposed on the plot indicates weights assigned to each point, decreasing to zero with distance from the target point. The fit f_[ˆ] ( _x_ 0) _at x_ 0 _is obtained by fitting a weighted linear regression (orange line segment), and using the fitted value at x_ 0 _(orange solid dot) as the estimate f_[ˆ] ( _x_ 0) _._ 

ing splines: it controls the flexibility of the non-linear fit. The smaller the value of _s_ , the more _local_ and wiggly will be our fit; alternatively, a very large value of _s_ will lead to a global fit to the data using all of the training observations. We can again use cross-validation to choose _s_ , or we can specify it directly. Figure 7.10 displays local linear regression fits on the `Wage` data, using two values of _s_ : 0 _._ 7 and 0 _._ 2. As expected, the fit obtained using _s_ = 0 _._ 7 is smoother than that obtained using _s_ = 0 _._ 2. 

The idea of local regression can be generalized in many different ways. In a setting with multiple features _X_ 1 _, X_ 2 _, . . . , Xp_ , one very useful generalization involves fitting a multiple linear regression model that is global in some variables, but local in another, such as time. Such _varying coefficient models_ are a useful way of adapting a model to the most recently gathered varying data. Local regression also generalizes very naturally when we want to fit models that are local in a pair of variables _X_ 1 and _X_ 2, rather than one. model We can simply use two-dimensional neighborhoods, and fit bivariate linear regression models using the observations that are near each target point in two-dimensional space. Theoretically the same approach can be implemented in higher dimensions, using linear regressions fit to _p_ -dimensional neighborhoods. However, local regression can perform poorly if _p_ is much larger than about 3 or 4 because there will generally be very few training observations close to _x_ 0. Nearest-neighbors regression, discussed in Chapter 3, suffers from a similar problem in high dimensions. 

coefficient model 

7.7 Generalized Additive Models 305 

---

## Sub-Chapters (하위 목차)

### Algorithm 7.1 Local Regression At X = x0 (국소 범주 가중치 K 이웃 범위 반경 설정 추적 알고리즘)
* [문서로 이동하기](./7_6_1_algorithm_7.1_local_regression_at_x_x_0/)

* [Local Linear Regression 적용 이론 실무 활용 스니펫 정보망](./18_local_linear_regression/)
데이터 내 어떠한 K 퍼센트 타겟 관측치들을 추출하고 종 모양 커널 등 가중치 거리를 계산하여 매겨, 구역 내 로컬 부분 회귀 최소 제곱을 지속 튜닝하며 어떻게 잔차 에러를 감소시키는지 실질 로직 알고리즘들을 디버깅 스레드로 봅니다.

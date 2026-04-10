---
layout: default
title: "index"
---

# 2.1 What Is Statistical Learning? 

In order to motivate our study of statistical learning, we begin with a simple example. Suppose that we are statistical consultants hired by a client to investigate the association between advertising and sales of a particular product. The `Advertising` data set consists of the `sales` of that product in 200 different markets, along with advertising budgets for the product in each of those markets for three different media: `TV` , `radio` , and `newspaper` . The data are displayed in Figure 2.1. It is not possible for our client to directly increase sales of the product. On the other hand, they can control the advertising expenditure in each of the three media. Therefore, if we determine that there is an association between advertising and sales, then we can instruct our client to adjust advertising budgets, thereby indirectly increasing sales. In other words, our goal is to develop an accurate model that can be used to predict sales on the basis of the three media budgets. 

In this setting, the advertising budgets are _input variables_ while `sales` input is an _output variable_ . The input variables are typically denoted using the variable symbol _X_ , with a subscript to distinguish them. So _X_ 1 might be the `TV` output budget, _X_ 2 the `radio` budget, and _X_ 3 the `newspaper` budget. The inputs variable go by different names, such as _predictors_ , _independent variables_ , _features_ , predictor or sometimes just _variables_ . The output variable—in this case, `sales` —is often called the _response_ or _dependent variable_ , and is typically denoted variable using the symbol _Y_ . Throughout this book, we will use all of these terms feature interchangeably. variable 

independent variable feature variable response dependent variable 

More generally, suppose that we observe a quantitative response _Y_ and _p_ different predictors, _X_ 1 _, X_ 2 _, . . . , Xp_ . We assume that there is some relationship between _Y_ and _X_ = ( _X_ 1 _, X_ 2 _, . . . , Xp_ ), which can be written in the very general form 

$$ Y = f(X) + \epsilon \tag{2.1} $$ 

![Figure 2.1](./img/Image_015.png)

**FIGURE 2.1.** _The_ `Advertising` _data set. The plot displays_ `sales` _, in thousands of units, as a function of_ `TV` _,_ `radio` _, and_ `newspaper` _budgets, in thousands of dollars, for_ 200 _different markets. In each plot we show the simple least squares fit of_ `sales` _to that variable, as described in Chapter 3. In other words, each blue line represents a simple model that can be used to predict_ `sales` _using_ `TV` _,_ `radio` _, and_ `newspaper` _, respectively._ 

Here _f_ is some fixed but unknown function of _X_ 1 _, . . . , Xp_ , and _ϵ_ is a random _error term_ , which is independent of _X_ and has mean zero. In this formula- error term tion, _f_ represents the _systematic_ information that _X_ provides about _Y_ . 

systematic 

![Figure 2.2](./img/Image_016.png)

**FIGURE 2.2.** _The_ `Income` _data set._ Left: _The red dots are the observed values of_ `income` _(in thousands of dollars) and_ `years of education` _for_ 30 _individuals._ Right: _The blue curve represents the true underlying relationship between_ `income` _and_ `years of education` _, which is generally unknown (but is known in this case because the data were simulated). The black lines represent the error associated with each observation. Note that some errors are positive (if an observation lies above the blue curve) and some are negative (if an observation lies below the curve). Overall, these errors have approximately mean zero._

As another example, consider the left-hand panel of Figure 2.2, a plot of `income` versus `years of education` for 30 individuals in the `Income` data set. The plot suggests that one might be able to predict `income` using `years of education`. However, the function _f_ that connects the input variable to the output variable is in general unknown. In this situation one must estimate _f_ based on the observed points. Since `Income` is a simulated data set, _f_ is known and is shown by the blue curve in the right-hand panel of Figure 2.2. The vertical lines represent the error terms _ϵ_ . We note that some of the 30 observations lie above the blue curve and some lie below it; overall, the errors have approximately mean zero. 

In general, the function _f_ may involve more than one input variable. In Figure 2.3 we plot `income` as a function of `years of education` and `seniority` . Here _f_ is a two-dimensional surface that must be estimated based on the observed data. 

In essence, statistical learning refers to a set of approaches for estimating _f_ . In this chapter we outline some of the key theoretical concepts that arise in estimating _f_ , as well as tools for evaluating the estimates obtained. 

---

## Sub-Chapters (하위 목차)

### 2.1.1 Why Estimate f ? (왜 f를 추정해야 하는가?)
* [문서로 이동하기](./2_1_1_why_estimate_f/)

새로운 데이터 포인트에 대해 출력값을 예측하기 위한 예측(Prediction) 중심의 이유와, 
각 입력 변수가 출력 변수에 미치는 영향을 분석하기 위한 추론(Inference) 중심의 이유를 배웁니다.

### 2.1.2 How Do We Estimate f ? (어떻게 f를 추정하는가?)
* [문서로 이동하기](./2_1_2_how_do_we_estimate_f/)

학습 데이터(Training Data)를 활용하여 가장 적합한 함수 $f$를 수학적으로 구성하는 접근 방식을 소개합니다.
파라미터 모델(Parametric)과 비-파라미터 모델(Non-Parametric)의 근본적인 차이점과 작동 원리를 다룹니다.

### 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability (예측 정확도와 모델 해석력 간의 트레이드오프)
* [문서로 이동하기](./2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/)

모델이 유연하고 강력해질수록 내부 구조가 복잡해지며 원인 분석과 해석이 크게 어려워지는 블랙박스 구조 현상을 다룹니다.
분석의 근본 목적(높은 정확성 vs 구체적인 원인 규명 필요성)에 따라 유연성 수준을 결정하는 능력을 기릅니다.

### 2.1.4 Supervised Versus Unsupervised Learning (지도 학습과 비지도 학습)
* [문서로 이동하기](./2_1_4_supervised_versus_unsupervised_learning/)

예측 대상이 되는 정답(Label/Response)이 주어지는 환경에서의 지도 학습과 구조적인 특징만을 파악하는 비지도 학습의 차이를 짚어봅니다.
결과적으로 지도-비지도 중간의 성격을 지닌 반지도 학습(Semi-Supervised) 개념도 짧게 소개됩니다.

### 2.1.5 Regression Versus Classification Problems (회귀 문제와 분류 문제)
* [문서로 이동하기](./2_1_5_regression_versus_classification_problems/)

반응 변수가 수치적으로 연속형인 회귀(Regression) 상황과 질적으로 나뉘는 이산형인 분류(Classification) 상황을 정의합니다.
각 문제 유형에 알맞은 알고리즘과 평가지표 체계가 본질적으로 달라져야 함을 설명합니다.

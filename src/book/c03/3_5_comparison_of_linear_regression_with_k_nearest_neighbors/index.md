---
layout: default
title: "index"
---

[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/index.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3.5 Comparison of Linear Regression with $K$-Nearest Neighbors

As discussed in Chapter 2, linear regression is an example of a _parametric_ approach because it assumes a linear functional form for $f(X)$.

Parametric methods have several advantages.

They are often easy to fit, because one need estimate only a small number of coefficients.

In the case of linear regression, the coefficients have simple interpretations, and tests of statistical significance can be easily performed.

But parametric methods do have a disadvantage: by construction, they make strong assumptions about the form of $f(X)$.

If the specified functional form is far from the truth, and prediction accuracy is our goal, then the parametric method will perform poorly.

For instance, if we assume a linear relationship between X and Y but the true relationship is far from linear, then the resulting model will provide a poor fit to the data, and any conclusions drawn from it will be suspect.

In contrast, _non-parametric_ methods do not explicitly assume a parametric form for $f(X)$, and thereby provide an alternative and more flexible approach for performing regression.

We discuss various non-parametric methods in this book.

Here we consider one of the simplest and best-known non-parametric methods, _K-nearest neighbors regression_ ().

The  method is closely related to the KNN classifier discussed in Chapter 2.

Given a value for $K$ and a prediction point $x_0$,  first identifies the $K$ training observations that are closest to $x_0$, represented by $N_0$.

It then estimates $f(x_0)$ using the average of all the training responses in $N_0$. In other words,

**==> picture [87 x 27] intentionally omitted <==**

Figure 3.16 illustrates two KNN fits on a data set with $p=2$ predictors.

The fit with $K=1$ is shown in the left-hand panel, while the right-hand panel corresponds to $K=9$.

We see that when $K=1$, the KNN fit perfectly interpolates the training observations, and consequently takes the form of a step function.

When $K=9$, the KNN fit still is a step function, but averaging over nine observations results in much smaller regions of constant prediction, and consequently a smoother fit.

In general, the optimal value for $K$ will depend on the _bias-variance tradeoff_, which we introduced in Chapter 2.

A small value for $K$ provides the most flexible fit, which will have low bias but high variance.

This variance is due to the fact that the prediction in a given region is entirely dependent on just one observation.

**==> picture [311 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
y<br>y y<br>x1 x1<br>x2 x2<br>y y<br>**----- End of picture text -----**<br>

**FIGURE 3.16.** _Plots of f_[ˆ] ( X ) _using  on a two-dimensional data set with_ 64 _observations (orange dots)._ Left: _K_ = 1 _results in a rough step function fit._ Right: _K_ = 9 _produces a much smoother fit._

In contrast, larger values of _K_ provide a smoother and less variable fit; the prediction in a region is an average of several points, and so changing one observation has a smaller effect. However, the smoothing may cause bias by masking some of the structure in $f(X)$. In Chapter 5, we introduce several approaches for estimating test error rates. These methods can be used to identify the optimal value of _K_ in .

In what setting will a parametric approach such as least squares linear regression outperform a non-parametric approach such as ? The answer is simple: _the parametric approach will outperform the nonparametric approach if the parametric form that has been selected is close to the true form of f_ . Figure 3.17 provides an example with data generated from a one-dimensional linear regression model. The black solid lines represent $f(X)$, while the blue curves correspond to the KNN fits using _K_ = 1 and _K_ = 9. In this case, the _K_ = 1 predictions are far too variable, while the smoother _K_ = 9 fit is much closer to $f(X)$. However, since the true relationship is linear, it is hard for a non-parametric approach to compete with linear regression: a non-parametric approach incurs a cost in variance that is not offset by a reduction in bias. The blue dashed line in the lefthand panel of Figure 3.18 represents the linear regression fit to the same data. It is almost perfect. The right-hand panel of Figure 3.18 reveals that linear regression outperforms KNN for this data. The green solid line, plotted as a function of 1 _/K_ , represents the test set mean squared error (MSE) for KNN. The KNN errors are well above the black dashed line, which is the test MSE for linear regression. When the value of _K_ is large, then KNN performs only a little worse than least squares regression in terms of MSE. It performs far worse when _K_ is small.

In practice, the true relationship between X and Y is rarely exactly linear. Figure 3.19 examines the relative performances of least squares regression and KNN under increasing levels of non-linearity in the relationship between X and Y . In the top row, the true relationship is nearly linear. In this case we see that the test MSE for linear regression is still superior

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors

**==> picture [315 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 −1.0 −0.5 0.0 0.5 1.0<br>x x<br>4<br>4<br>3 3<br>y 2 y 2<br>1 1<br>**----- End of picture text -----**<br>

**FIGURE 3.17.** _Plots of f_[ˆ] ( X ) _using  on a one-dimensional data set with_ 50 _observations. The true relationship is given by the black solid line._ Left: _The blue curve corresponds to K_ = 1 _and interpolates (i.e. passes directly through) the training data._ Right: _The blue curve corresponds to K_ = 9 _, and represents a smoother fit._

**==> picture [316 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>4<br>0.15<br>3<br>y 0.10<br>2<br>Mean Squared Error<br>0.05<br>1<br>0.00<br>**----- End of picture text -----**<br>

**FIGURE 3.18.** _The same data set shown in Figure 3.17 is investigated further._ Left: _The blue dashed line is the least squares fit to the data. Since f_ ( X ) _is in fact linear (displayed as the black line), the least squares regression line provides a very good estimate of f_ ( X ) _._ Right: _The dashed horizontal line represents the least squares test set MSE, while the green solid line corresponds to the MSE for KNN as a function of_ 1 _/K (on the log scale). Linear regression achieves a lower test MSE than does , since f_ ( X ) _is in fact linear. For , the best results occur with a very large value of K, corresponding to a small value of_ 1 _/K._

114 3. Linear Regression

**==> picture [318 x 301] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>3.5 0.08<br>3.0<br>0.06<br>2.5<br>y<br>2.0 0.04<br>1.5 Mean Squared Error<br>0.02<br>1.0<br>0.5 0.00<br>0.15<br>3.5<br>3.0<br>0.10<br>2.5<br>y<br>2.0<br>Mean Squared Error 0.05<br>1.5<br>1.0<br>0.00<br>**----- End of picture text -----**<br>

**FIGURE 3.19.** Top Left: _In a setting with a slightly non-linear relationship between X and Y (solid black line), the KNN fits with K_ = 1 _(blue) and K_ = 9 _(red) are displayed._ Top Right: _For the slightly non-linear data, the test set MSE for least squares regression (horizontal black) and KNN with various values of_ 1 _/K (green) are displayed._ Bottom Left and Bottom Right: _As in the top panel, but with a strongly non-linear relationship between X and Y ._

to that of KNN for low values of _K_ . However, for _K ≥_ 4, KNN outperforms linear regression. The second row illustrates a more substantial deviation from linearity. In this situation, KNN substantially outperforms linear regression for all values of _K_ . Note that as the extent of non-linearity increases, there is little change in the test set MSE for the non-parametric KNN method, but there is a large increase in the test set MSE of linear regression.

Figures 3.18 and 3.19 display situations in which KNN performs slightly worse than linear regression when the relationship is linear, but much better than linear regression for nonlinear situations. In a real life situation in which the true relationship is unknown, one might suspect that KNN should be favored over linear regression because it will at worst be slightly inferior to linear regression if the true relationship is linear, and may give substantially better results if the true relationship is non-linear. But in reality, even when the true relationship is highly non-linear, KNN may still provide inferior results to linear regression. In particular, both Figures 3.18

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 115

**==> picture [315 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
p=1 p=2 p=3 p=4 p=10 p=20<br>0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0<br>1/K<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>Mean Squared Error 0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>**----- End of picture text -----**<br>

**FIGURE 3.20.** _Test MSE for linear regression (black dashed lines) and KNN (green curves) as the number of variables $p$ increases. The true function is nonlinear in the first variable, as in the lower panel in Figure 3.19, and does not depend on the additional variables. The performance of linear regression deteriorates slowly in the presence of these additional noise variables, whereas KNN’s performance degrades much more quickly as $p$ increases._

and 3.19 illustrate settings with $p$ = 1 predictor. But in higher dimensions, KNN often performs worse than linear regression.

Figure 3.20 considers the same strongly non-linear situation as in the second row of Figure 3.19, except that we have added additional _noise_ predictors that are not associated with the response. When $p$ = 1 or $p$ = 2, KNN outperforms linear regression. But for $p$ = 3 the results are mixed, and for _p ≥_ 4 linear regression is superior to KNN. In fact, the increase in dimension has only caused a small deterioration in the linear regression test set MSE, but it has caused more than a ten-fold increase in the MSE for KNN. This decrease in performance as the dimension increases is a common problem for KNN, and results from the fact that in higher dimensions there is effectively a reduction in sample size. In this data set there are 50 training observations; when $p$ = 1, this provides enough information to accurately estimate $f(X)$. However, spreading 50 observations over $p$ = 20 dimensions results in a phenomenon in which a given observation has no _nearby neighbors_ —this is the so-called _curse of dimensionality_ . That is, curse of dithe _K_ observations that are nearest to a given test observation _x_ 0 may be mensionality very far away from _x_ 0 in $p$ -dimensional space when $p$ is large, leading to a very poor prediction of f ( _x_ 0) and hence a poor KNN fit. As a general rule, parametric methods will tend to outperform non-parametric approaches when there is a small number of observations per predictor.

mensionality

Even when the dimension is small, we might prefer linear regression to KNN from an interpretability standpoint. If the test MSE of KNN is only slightly lower than that of linear regression, we might be willing to forego a little bit of prediction accuracy for the sake of a simple model that can be described in terms of just a few coefficients, and for which $p$-values are available.

116 3. Linear Regression

---

## Sub-Chapters


[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/index.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/index.html)

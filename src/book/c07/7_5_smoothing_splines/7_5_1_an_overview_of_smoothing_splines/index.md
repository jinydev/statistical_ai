---
layout: default
title: "index"
---

# _7.5.1 An Overview of Smoothing Splines_ 

In fitting a smooth curve to a set of data, what we really want to do is find some function, say _g_ ( _x_ ), that fits the observed data well: that is, we want RSS =[�] _[n] i_ =1[(] _[y][i][−][g]_[(] _[x][i]_[))][2][to][be][small.][However,][there][is][a][problem] with this approach. If we don’t put any constraints on _g_ ( _xi_ ), then we can always make RSS zero simply by choosing _g_ such that it _interpolates_ all of the _yi_ . Such a function would woefully overfit the data—it would be far too flexible. What we really want is a function _g_ that makes RSS small, but that is also _smooth_ . 

How might we ensure that _g_ is smooth? There are a number of ways to do this. A natural approach is to find the function _g_ that minimizes

$$
\sum_{i=1}^n (y_i - g(x_i))^2 + \lambda \int g''(t)^2 dt \quad (7.11)
$$

where _λ_ is a nonnegative _tuning parameter_ . The function _g_ that minimizes (7.11) is known as a _smoothing spline_ . 

smoothing spline 

What does (7.11) mean? Equation 7.11 takes the “Loss+Penalty” forspline mulation that we encounter in the context of ridge regression and the lasso in Chapter 6. The term[�] _[n] i_ =1[(] _[y][i][ −][g]_[(] _[x][i]_[))][2][is][a] _[loss][function]_[that][encour-] loss function ages _g_ to fit the data well, and the term _λ_ � _g[′′]_ ( _t_ )[2] _dt_ is a _penalty term_ that penalizes the variability in _g_ . The notation _g[′′]_ ( _t_ ) indicates the second derivative of the function _g_ . The first derivative _g[′]_ ( _t_ ) measures the slope 

7.5 Smoothing Splines 301 

of a function at _t_ , and the second derivative corresponds to the amount by which the slope is changing. Hence, broadly speaking, the second derivative of a function is a measure of its _roughness_ : it is large in absolute value if _g_ ( _t_ ) is very wiggly near _t_ , and it is close to zero otherwise. (The second derivative of a straight line is zero; note that a line is perfectly smooth.) The � notation is an _integral_ , which we can think of as a summation over the range of _t_ . In other words, � _g[′′]_ ( _t_ )[2] _dt_ is simply a measure of the total change in the function _g[′]_ ( _t_ ), over its entire range. If _g_ is very smooth, then _g[′]_ ( _t_ ) will be close to constant and � _g[′′]_ ( _t_ )[2] _dt_ will take on a small value. Conversely, if _g_ is jumpy and variable then _g[′]_ ( _t_ ) will vary significantly and � _g[′′]_ ( _t_ )[2] _dt_ will take on a large value. Therefore, in (7.11), _λ_ � _g[′′]_ ( _t_ )[2] _dt_ encourages _g_ to be smooth. The larger the value of _λ_ , the smoother _g_ will be. When _λ_ = 0, then the penalty term in (7.11) has no effect, and so the function _g_ will be very jumpy and will exactly interpolate the training observations. When _λ →∞_ , _g_ will be perfectly smooth—it will just be a straight line that passes as closely as possible to the training points. In fact, in this case, _g_ will be the linear least squares line, since the loss function in (7.11) amounts to minimizing the residual sum of squares. For an intermediate value of _λ_ , _g_ will approximate the training observations but will be somewhat smooth. We see that _λ_ controls the bias-variance trade-off of the smoothing spline. 

The function _g_ ( _x_ ) that minimizes (7.11) can be shown to have some special properties: it is a piecewise cubic polynomial with knots at the unique values of _x_ 1 _, . . . , xn_ , and continuous first and second derivatives at each knot. Furthermore, it is linear in the region outside of the extreme knots. In other words, _the function g_ ( _x_ ) _that minimizes (7.11) is a natural cubic spline with knots at x_ 1 _, . . . , xn!_ However, it is not the same natural cubic spline that one would get if one applied the basis function approach described in Section 7.4.3 with knots at _x_ 1 _, . . . , xn_ —rather, it is a _shrunken_ version of such a natural cubic spline, where the value of the tuning parameter _λ_ in (7.11) controls the level of shrinkage. 

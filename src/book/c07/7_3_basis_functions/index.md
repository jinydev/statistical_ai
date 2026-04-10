---
layout: default
title: "index"
---

# 7.3 Basis Functions 

Polynomial and piecewise-constant regression models are in fact special cases of a _basis function_ approach. The idea is to have at hand a fam- basis 

function 

294 7. Moving Beyond Linearity 

ily of functions or transformations that can be applied to a variable _X_ : _b_ 1( _X_ ) _, b_ 2( _X_ ) _, . . . , bK_ ( _X_ ). Instead of fitting a linear model in _X_ , we fit the model

$$
y_i = \beta_0 + \beta_1 b_1(x_i) + \beta_2 b_2(x_i) + \dots + \beta_K b_K(x_i) + \epsilon_i \quad (7.7)
$$

Note that the basis functions _b_ 1( _·_ ) _, b_ 2( _·_ ) _, . . . , bK_ ( _·_ ) are fixed and known. (In other words, we choose the functions ahead of time.) For polynomial regression, the basis functions are _bj_ ( _xi_ ) = _x[j] i_[,][and][for][piecewise][constant] functions they are _bj_ ( _xi_ ) = _I_ ( _cj ≤ xi < cj_ +1). We can think of (7.7) as a standard linear model with predictors _b_ 1( _xi_ ) _, b_ 2( _xi_ ) _, . . . , bK_ ( _xi_ ). Hence, we can use least squares to estimate the unknown regression coefficients in (7.7). Importantly, this means that all of the inference tools for linear models that are discussed in Chapter 3, such as standard errors for the coefficient estimates and F-statistics for the model’s overall significance, are available in this setting. 

Thus far we have considered the use of polynomial functions and piecewise constant functions for our basis functions; however, many alternatives are possible. For instance, we can use wavelets or Fourier series to construct basis functions. In the next section, we investigate a very common choice for a basis function: _regression splines_ . 

regression spline 

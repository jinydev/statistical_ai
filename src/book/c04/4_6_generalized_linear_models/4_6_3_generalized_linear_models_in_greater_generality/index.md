---
layout: default
title: "index"
---

# _4.6.3 Generalized Linear Models in Greater Generality_ 

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics: 

1. Each approach uses predictors $X_1$ _, . . . , Xp_ to predict a response $Y$. We assume that, conditional on $X_1$ _, . . . , Xp_ , $Y$belongs to a certain family of distributions. For linear regression, we typically assume that $Y$follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$follows a Poisson distribution. 

2. Each approach models the mean of $Y$as a function of the predictors. In linear regression, the mean of $Y$ takes the form 

$$
	ext{E}(Y \mid X_1, \dots, X_p) = eta_0 + eta_1 X_1 + \dots + eta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form 

$$
	ext{E}(Y \mid X_1, \dots, X_p) = 
rac{e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p}}{1 + e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form 

$$
	ext{E}(Y \mid X_1, \dots, X_p) = e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_ , _η_ , which link function 

> 5In fact, the variance in the `Bikeshare` data appears to be much higher than the mean, a situation referred to as _overdispersion_ . This causes the Z-values to be inflated in Table 4.11. A more careful analysis should account for this overdispersion to obtain more accurate Z-values, and there are a variety of methods for doing this. But they are beyond the scope of this book. 

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 173 

applies a transformation to E( _Y |X_ 1 _, . . . , Xp_ ) so that the transformed mean is a linear function of the predictors. That is, 

$$
\eta(	ext{E}(Y \mid X_1, \dots, X_p)) = eta_0 + eta_1 X_1 + \dots + eta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are _η_ ( _µ_ ) = _µ_ , _η_ ( _µ_ ) = log( _µ/_ (1 _− µ_ )), and _η_ ( _µ_ ) = log( _µ_ ), respectively. 

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_ . Other well- exponential known members of this family are the _exponential_ distribution, the _Gamma_ family distribution, and the _negative binomial_ distribution. In general, we can perexponential form a regression by modeling the response $Y$as coming from a particular Gamma member of the exponential family, and then transforming the mean of the negative response so that the transformed mean is a linear function of the predictors binomial via (4.42). Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM). Thus, linear regression, logistic generalized regression, and Poisson regression are three examples of GLMs. Other exlinear model amples not covered here include _Gamma regression_ and _negative binomial regression_ . 

linear model 

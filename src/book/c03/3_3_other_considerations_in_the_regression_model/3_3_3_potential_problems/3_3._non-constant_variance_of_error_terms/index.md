---
layout: default
title: "index"
---

# 3. Non-constant Variance of Error Terms 

Another important assumption of the linear regression model is that the error terms have a constant variance, Var( \epsilon_i ) = \sigma^2 . The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption. 

Unfortunately, it is often the case that the variances of the error terms are non-constant. For instance, the variances of the error terms may increase with the value of the response. One can identify non-constant variances in the errors, or _heteroscedasticity_ , from the presence of a _funnel shape_ in heterothe residual plot. An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values. When faced with this problem, one possible solution is to transform the response Y using a concave function such as log Y or _√Y_ . Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in heteroscedasticity. The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using log Y . The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data. 

scedasticity 

Sometimes we have a good idea of the variance of each response. For example, the _i_ th response could be an average of _ni_ raw observations. If each of these raw observations is uncorrelated with variance \sigma^2 , then their average has variance _σi_[2][=] _[ σ]_[2] _[/n][i]_[.][In][this][case][a][simple][remedy][is][to][fit][our] model by _weighted least squares_ , with weights proportional to the inverse weighted variances—i.e. _wi_ = _ni_ in this case. Most linear regression software allows least for observation weights. 


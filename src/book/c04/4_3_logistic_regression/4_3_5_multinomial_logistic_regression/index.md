---
layout: default
title: "index"
---

# _4.3.5 Multinomial Logistic Regression_ 

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure` . However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable. 

4.3 Logistic Regression 145 

It turns out that it is possible to extend the two-class logistic regression approach to the setting of _K >_ 2 classes. This extension is sometimes known as _multinomial logistic regression_ . To do this, we first select a single multinomial class to serve as the _baseline_ ; without loss of generality, we select the $K$ th logistic class for this role. Then we replace the model (4.7) with the model 

$$
	ext{Pr}(Y = k \mid X = x) = 
rac{e^{eta_{k0} + eta_{k1} x_1 + \dots + eta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{eta_{l0} + eta_{l1} x_1 + \dots + eta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and 

$$
	ext{Pr}(Y = K \mid X = x) = 
rac{1}{1 + \sum_{l=1}^{K-1} e^{eta_{l0} + eta_{l1} x_1 + \dots + eta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$, 

$$
\log\left(
rac{	ext{Pr}(Y = k \mid X = x)}{	ext{Pr}(Y = K \mid X = x)}
ight) = eta_{k0} + eta_{k1} x_1 + \dots + eta_{kp} x_p \quad (4.11)
$$

Notice that (4.12) is quite similar to (4.6). Equation 4.12 indicates that once again, the log odds between any pair of classes is linear in the features. 

It turns out that in (4.10)–(4.12), the decision to treat the $K$ th class as the baseline is unimportant. For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline. The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same. 

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline. For example, if we set `epileptic seizure` to be the baseline, then we can interpret _β_ stroke0 as the log odds of `stroke` versus `epileptic seizure` , given that _x_ 1 = _· · ·_ = _xp_ = 0. Furthermore, a one-unit increase in _Xj_ is associated with a _β_ stroke $j$ increase in the log odds of `stroke` over `epileptic seizure` . Stated another way, if _Xj_ increases by one unit, then 





increases by _e[β]_[stroke] _[j]_ . 

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding. The softmax coding is equivalent softmax to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding. But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it. In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k$ = 1 _, . . . , K_ , 



146 4. Classification 

Thus, rather than estimating coefficients for _K −_ 1 classes, we actually estimate coefficients for all $K$ classes. It is not hard to see that as a result of (4.13), the log odds ratio between the $k$ th and _k[′]_ th classes equals 



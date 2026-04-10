---
layout: default
title: "index"
---

# _11.5.1 The Hazard Function_ 

The _hazard function_ or _hazard rate_ — also known as the _force of mortality_ hazard — is formally defined as 

$$
h(t) = \lim_{\Delta t \to 0} \frac{\Pr(t < T \le t + \Delta t \mid T > t)}{\Delta t} \quad (11.9)
$$


> 6Alternatively, we can estimate the _p_ -value via permutations, using ideas that will be presented in Section 13.5. The permutation distribution is obtained by randomly swapping the labels for the observations in the two groups. 

11.5 Regression Models With a Survival Response 477 

where _T_ is the (unobserved) survival time. It is the death rate in the instant after time _t_ , given survival past that time.[7] In (11.9), we take the limit as ∆ _t_ approaches zero, so we can think of ∆ _t_ as being an extremely tiny number. Thus, more informally, (11.9) implies that

$$
h(t) \Delta t \approx \Pr(t < T \le t + \Delta t \mid T > t)
$$

for some arbitrarily small ∆ _t_ . 

Why should we care about the hazard function? First of all, it is closely related to the survival curve (11.2), as we will see next. Second, it turns out that a key approach for modeling survival data as a function of covariates relies heavily on the hazard function; we will introduce this approach — Cox’s proportional hazards model — in Section 11.5.2. 

We now consider the hazard function _h_ ( _t_ ) in a bit more detail. Recall that for two events _A_ and _B_ , the probability of _A_ given _B_ can be expressed as Pr( _A | B_ ) = Pr( _A ∩ B_ ) _/_ Pr( _B_ ), i.e. the probability that _A_ and _B_ both occur divided by the probability that _B_ occurs. Furthermore, recall from (11.2) that _S_ ( _t_ ) = Pr( _T > t_ ). Thus, 

$$
h(t) = \lim_{\Delta t \to 0} \frac{\Pr(t < T \le t + \Delta t) / \Pr(T > t)}{\Delta t} = \frac{f(t)}{S(t)} \quad (11.10)
$$

where

$$
f(t) = \lim_{\Delta t \to 0} \frac{\Pr(t < T \le t + \Delta t)}{\Delta t} \quad (11.11)
$$


is the _probability density function_ associated with _T_ , i.e. it is the instanta- probability neous rate of death at time _t_ . The second equality in (11.10) made use of density the fact that if _t < T ≤ t_ + ∆ _t_ , then it must be the case that _T > t_ . function 

Equation 11.10 implies a relationship between the hazard function _h_ ( _t_ ), the survival function _S_ ( _t_ ), and the probability density function _f_ ( _t_ ). In fact, these are three equivalent ways[8] of describing the distribution of _T_ . 

The likelihood associated with the _i_ th observation is 

$$
L_i = \begin{cases} f(y_i) & \text{if } \delta_i = 1 \\ S(y_i) & \text{if } \delta_i = 0 \end{cases} \quad (11.12)
$$

The intuition behind (11.12) is as follows: if _Y_ = _yi_ and the _i_ th observation is not censored, then the likelihood is the probability of dying in a tiny interval around time _yi_ . If the _i_ th observation is censored, then the likelihood 

> 7Due to the ∆ _t_ in the denominator of (11.9), the hazard function is a rate of death, rather than a probability of death. However, higher values of _h_ ( _t_ ) directly correspond to a higher probability of death, just as higher values of a probability density function correspond to more likely outcomes for a random variable. In fact, _h_ ( _t_ ) is the probability density function for _T_ conditional on _T > t_ . 

> 8See Exercise 8. 

478 11. Survival Analysis and Censored Data 

is the probability of surviving at least until time _yi_ . Assuming that the _n_ observations are independent, the likelihood for the data takes the form

$$
L = \prod_{i=1}^n L_i = \prod_{i=1}^n f(y_i)^{\delta_i} S(y_i)^{1 - \delta_i} = \prod_{i=1}^n h(y_i)^{\delta_i} S(y_i) \quad (11.13)
$$

where the second equality follows from (11.10). 

We now consider the task of modeling the survival times. If we assume exponential survival, i.e. that the probability density function of the survival time _T_ takes the form _f_ ( _t_ ) = _λ_ exp( _−λt_ ), then estimating the parameter _λ_ by maximizing the likelihood in (11.13) is straightforward.[9] Alternatively, we could assume that the survival times are drawn from a more flexible family of distributions, such as the Gamma or Weibull family. Another possibility is to model the survival times non-parametrically, as was done in Section 11.3 using the Kaplan–Meier estimator. 

However, what we would really like to do is model the survival time _as a function of the covariates_ . To do this, it is convenient to work directly with the hazard function, instead of the probability density function.[10] One possible approach is to assume a functional form for the hazard function _h_ ( _t|xi_ ), such as _h_ ( _t|xi_ ) = exp � _β_ 0 +[�] _[p] j_ =1 _[β][j][x][ij]_ �, where the exponent function guarantees that the hazard function is non-negative. Note that the exponential hazard function is special, in that it does not vary with time.[11] Given _h_ ( _t|xi_ ), we could calculate _S_ ( _t|xi_ ). Plugging these equations into (11.13), we could then maximize the likelihood in order to estimate the parameter _β_ = ( _β_ 0 _, β_ 1 _, . . . , βp_ ) _[T]_ . However, this approach is quite restrictive, in the sense that it requires us to make a very stringent assumption on the form of the hazard function _h_ ( _t|xi_ ). In the next section, we will consider a much more flexible approach. 

---
layout: default
title: "index"
---

# Cox’s Proportional Hazards Model 

Because the form of _h_ 0( _t_ ) in the proportional hazards assumption (11.14) is unknown, we cannot simply plug _h_ ( _t|xi_ ) into the likelihood (11.13) and then estimate _β_ = ( _β_ 1 _, . . . , βp_ ) _[T]_ by maximum likelihood. The magic of _Cox’s proportional hazards model_ lies in the fact that it is in fact possible Cox’s to estimate _β without having to specify the form of h_ 0( _t_ ). 

proportional hazards model 

To accomplish this, we make use of the same “sequential in time” logic that we used to derive the Kaplan–Meier survival curve and the log-rank test. For simplicity, assume that there are no ties among the failure, or death, times: i.e. each failure occurs at a distinct time. Assume that _δi_ = 1, i.e. the _i_ th observation is uncensored, and thus _yi_ is its failure time. Then the hazard function for the _i_ th observation at time _yi_ is _h_ ( _yi|xi_ ) = _h_ 0( _yi_ ) exp �� _pj_ =1 _[x][ij][β][j]_ �, and the total hazard at time _yi_ for the at risk observations[12] is

$$
\sum_{i' : y_{i'} \ge y_i} h_0(y_i) \exp \left( \sum_{j=1}^p x_{i'j} \beta_j \right)
$$

Therefore, the probability that the _i_ th observation is the one to fail at time _yi_ (as opposed to one of the other observations in the risk set) is

$$
\frac{h_0(y_i) \exp \left( \sum_{j=1}^p x_{ij} \beta_j \right)}{\sum_{i' : y_{i'} \ge y_i} h_0(y_i) \exp \left( \sum_{j=1}^p x_{i'j} \beta_j \right)} = \frac{\exp \left( \sum_{j=1}^p x_{ij} \beta_j \right)}{\sum_{i' : y_{i'} \ge y_i} \exp \left( \sum_{j=1}^p x_{i'j} \beta_j \right)} \quad (11.15)
$$

Notice that the unspecified baseline hazard function _h_ 0( _yi_ ) cancels out of 

the numerator and denominator! 

The _partial likelihood_ is simply the product of these probabilities over all partial of the uncensored observations, 

likelihood 

$$
PL(\beta) = \prod_{i : \delta_i = 1} \frac{\exp \left( \sum_{j=1}^p x_{ij} \beta_j \right)}{\sum_{i' : y_{i'} \ge y_i} \exp \left( \sum_{j=1}^p x_{i'j} \beta_j \right)} \quad (11.16)
$$

Critically, the partial likelihood is valid regardless of the true value of _h_ 0( _t_ ), making the model very flexible and robust.[13] 

To estimate _β_ , we simply maximize the partial likelihood (11.16) with respect to _β_ . As was the case for logistic regression in Chapter 4, no closedform solution is available, and so iterative algorithms are required. 

In addition to estimating _β_ , we can also obtain other model outputs that we saw in the context of least squares regression in Chapter 3 and logistic regression in Chapter 4. For example, we can obtain _p_ -values corresponding 

> 12Recall that the “at risk” observations at time _yi_ are those that are still at risk of failure, i.e. those that have not yet failed or been censored before time _yi_ . 

> 13In general, the partial likelihood is used in settings where it is difficult to compute the full likelihood for all of the parameters. Instead, we compute a likelihood for just the parameters of primary interest: in this case, _β_ 1 _, . . . , βp_ . It can be shown that maximizing (11.16) provides good estimates for these parameters. 

11.5 Regression Models With a Survival Response 481 

to particular null hypotheses (e.g. _H_ 0 : _βj_ = 0), as well as confidence intervals associated with the coefficients. 

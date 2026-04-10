---
layout: default
title: "index"
---

# _4.3.1 The Logistic Model_ 

How should we model the relationship between _p_ ( $X$) = Pr( $Y=$ 1 _|X_ ) and $X$? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent these probabilities: 

$$
p(X) = eta_0 + eta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance` , then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1. These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1. This problem is not unique to the credit default data. Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict _p_ ( $X$) _<_ 0 for some values of $X$and _p_ ( $X$) _>_ 1 for others (unless the range of $X$is limited). 

To avoid this problem, we must model _p_ ( $X$) using a function that gives outputs between 0 and 1 for all values of $X$. Many functions meet this description. In logistic regression, we use the _logistic function_, 

$$
p(X) = 
rac{e^{eta_0 + eta_1 X}}{1 + e^{eta_0 + eta_1 X}} \quad (4.2)
$$

logistic function 

To fit the model (4.2), we use a method called _maximum likelihood_ , which maximum we discuss in the next section. The right-hand panel of Figure 4.2 illustrates likelihood the fit of the logistic regression model to the `Default` data. Notice that for 

140 4. Classification 

low balances we now predict the probability of default as close to, but never below, zero. Likewise, for high balances we predict a default probability close to, but never above, one. The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction. We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot. The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set. 

After a bit of manipulation of (4.2), we find that 

$$

rac{p(X)}{1 - p(X)} = e^{eta_0 + eta_1 X} \quad (4.3)
$$

The quantity _p_ ( $X$) _/_ [1 _− p_ ( $X$)] is called the _odds_ , and can take on any value odds between 0 and _∞_ . Values of the odds close to 0 and _∞_ indicate very low and very high probabilities of default, respectively. For example, on average 1 in 5 people with an odds of 1 _/_ 4 will default, since _p_ ( $X$) = 0 _._ 2 implies an odds of 1 _−_ 0 _._ 02 _._ 2[= 1] _[/]_[4][. Likewise, on average nine out of every ten people with] an odds of 9 will default, since _p_ ( $X$) = 0 _._ 9 implies an odds of 1 _−_ 0 _._ 09 _._ 9[=][9][.] Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy. 

By taking the logarithm of both sides of (4.3), we arrive at 

$$
\log\left(
rac{p(X)}{1 - p(X)}
ight) = eta_0 + eta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_ . We see that the logistic log odds regression model (4.2) has a logit that is linear in $X$. 

logit 

Recall from Chapter 3 that in a linear regression model, _β_ 1 gives the average change in $Y$associated with a one-unit increase in $X$. By contrast, in a logistic regression model, increasing $X$by one unit changes the log odds by _β_ 1 (4.4). Equivalently, it multiplies the odds by _e[β]_[1] (4.3). However, because the relationship between _p_ ( $X$) and $X$in (4.2) is not a straight line, _β_ 1 does _not_ correspond to the change in _p_ ( $X$) associated with a one-unit increase in $X$. The amount that _p_ ( $X$) changes due to a one-unit change in $X$depends on the current value of $X$. But regardless of the value of $X$, if _β_ 1 is positive then increasing $X$will be associated with increasing _p_ ( $X$), and if _β_ 1 is negative then increasing $X$will be associated with decreasing _p_ ( $X$). The fact that there is not a straight-line relationship between _p_ ( $X$) and $X$, and the fact that the rate of change in _p_ ( $X$) per unit change in $X$depends on the current value of $X$, can also be seen by inspection of the right-hand panel of Figure 4.2. 

---
layout: default
title: "index"
---

# _4.6.2 Poisson Regression on the Bikeshare Data_ 

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_ . Before we can talk about Poisson regression, we must first in- Poisson troduce the _Poisson distribution_ . 

regression Poisson distribution 

Suppose that a random variable $Y$takes on nonnegative integer values, i.e. _Y ∈{_ 0 _,_ 1 _,_ 2 _, . . .}_ . If $Y$ follows the Poisson distribution, then 

$$
	ext{Pr}(Y = k) = 
rac{e^{-\lambda} \lambda^k}{k!} \quad 	ext{for } k = 0, 1, 2, \dots \quad (4.35)
$$

170 4. Classification 

Here, _λ >_ 0 is the expected value of $Y$, i.e. E( $Y$). It turns out that _λ_ also equals the variance of $Y$, i.e. _λ_ = E( $Y$) = Var( $Y$). This means that if $Y$follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance. (In (4.35), the notation $k$ !, pronounced “k factorial”, is defined as $k$ ! = _k ×_ ( _k −_ 1) _×_ ( _k −_ 2) _× . . . ×_ 3 _×_ 2 _×_ 1.) 

The Poisson distribution is typically used to model _counts_ ; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values. To see how we might use the Poisson distribution in practice, let $Y$denote the number of users of the bike sharing program during a particular hour of the day, under a particular set of weather conditions, and during a particular month of the year. We might model $Y$as a Poisson distribution with mean E( $Y$) = _λ_ = 5. This means that the probability of no users during this particular hour is Pr( $Y=$ 0) = _e[−]_ 0![5] 5[0] = _e[−]_[5] = 0 _._ 0067 (where 0! = 1 by convention). The probability that there is exactly one user is Pr( $Y=$ 1) = _e[−]_ 1![5] 5[1] = 5 _e[−]_[5] = 0 _._ 034, the probability of two users is Pr( $Y=$ 2) = _[e][−]_ 2![5][5][2] = 0 _._ 084, and so on. Of course, in reality, we expect the mean number of users of the bike sharing program, _λ_ = E( $Y$), to vary as a function of the hour of the day, the month of the year, the weather conditions, and so forth. So rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like _λ_ = 5, we would like to allow the mean to vary as a function of the covariates. In particular, we consider the following model for the mean _λ_ = E( $Y$), which we now write as _λ_ ( $X_1$ _, . . . , Xp_ ) to emphasize that it is a function of the covariates $X_1, \dots, X_p$: 

$$
\lambda(X_1, \dots, X_p) = e^{eta_0 + eta_1 X_1 + \dots + eta_p X_p} \quad (4.36)
$$

or equivalently 

$$
\log(\lambda(X_1, \dots, X_p)) = eta_0 + eta_1 X_1 + \dots + eta_p X_p \quad (4.37)
$$

Here, _β_ 0 _, β_ 1 _, . . . , βp_ are parameters to be estimated. Together, (4.35) and (4.36) define the Poisson regression model. Notice that in (4.36), we take the _log_ of _λ_ ( $X_1$ _, . . . , Xp_ ) to be linear in $X_1$ _, . . . , Xp_ , rather than having _λ_ ( $X_1$ _, . . . , Xp_ ) itself be linear in $X_1$ _, . . . , Xp_ ; this ensures that _λ_ ( $X_1$ _, . . . , Xp_ ) takes on nonnegative values for all values of the covariates. 

To estimate the coefficients _β_ 0 _, β_ 1 _, . . . , βp_ , we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2. Specifically, given _n_ independent observations from the Poisson regression model, the likelihood takes the form 

$$
\ell(eta_0, eta_1, \dots, eta_p) = \prod_{i=1}^n 
rac{e^{-\lambda(x_i)} \lambda(x_i)^{y_i}}{y_i!} \quad (4.38)
$$

where _λ_ ( _xi_ ) = _e[β]_[0][+] _[β]_[1] _[x][i]_[1][+] _[···]_[+] _[β][p][x][ip]_ , due to (4.37). We estimate the coefficients that maximize the likelihood _ℓ_ ( _β_ 0 _, β_ 1 _, . . . , βp_ ), i.e. that make the observed data as likely as possible. 

We now fit a Poisson regression model to the `Bikeshare` data set. The results are shown in Table 4.11 and Figure 4.15. Qualitatively, the results are similar to those from linear regression in Section 4.6.1. We again see that bike usage is highest in the spring and fall and during rush hour, 

4.6 Generalized Linear Models 171 

||Coefcient Std. error|Coefcient Std. error|_z_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|4.12|0.01|683.96|0.00|
|`workingday`|0.01|0.00|7.5|0.00|
|`temp`|0.79|0.01|68.43|0.00|
|`weathersit[cloudy/misty]`|-0.08|0.00|-34.53|0.00|
|`weathersit[light rain/snow]`|-0.58|0.00|-141.91|0.00|
|`weathersit[heavy rain/snow]`|-0.93|0.17|-5.55|0.00|



**TABLE 4.11.** _Results for a Poisson regression model fit to predict_ `bikers` _in the_ `Bikeshare` _data. The predictors_ `mnth` _and_ `hr` _are omitted from this table due to space constraints, and can be seen in Figure 4.15. For the qualitative variable_ `weathersit` _, the baseline corresponds to clear skies._ 

![Figure 4.15](./img/4_15.png)

**FIGURE 4.15.** _A Poisson regression model was fit to predict_ `bikers` _in the_ `Bikeshare` _data set._ Left: _The coefficients associated with the month of the year. Bike usage is highest in the spring and fall, and lowest in the winter._ Right: _The coefficients associated with the hour of the day. Bike usage is highest during peak commute times, and lowest overnight._ 

and lowest during the winter and in the early morning hours. Moreover, bike usage increases as the temperature increases, and decreases as the weather worsens. Interestingly, the coefficient associated with `workingday` is statistically significant under the Poisson regression model, but not under the linear regression model. 

Some important distinctions between the Poisson regression model and the linear regression model are as follows: 

- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in _Xj_ by one unit is associated with a change in E( $Y$) = _λ_ by a factor of exp( _βj_ ). For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of exp( _−_ 0 _._ 08) = 0 _._ 923, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear. If the weather worsens further and it begins to rain, then the mean bike usage will further change by a factor of exp( _−_ 0 _._ 5) = 0 _._ 607, i.e. on average only 60.7% as many people will use bikes when it is rainy relative to when it is cloudy. 

172 4. Classification 

- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, _λ_ = E( $Y$) = Var( $Y$). Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. By contrast, under a linear regression model, the variance of bike usage always takes on a constant value. Recall from Figure 4.14 that in the `Bikeshare` data, when biking conditions are favorable, both the mean _and_ the variance in bike usage are much higher than when conditions are unfavorable. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.[5] 

overdispersion 

- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values; see (4.35). By contrast, when we fit a linear regression model to the `Bikeshare` data set, almost 10% of the predictions were negative. 

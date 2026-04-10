---
layout: default
title: "index"
---

# 5.2 The Bootstrap 

The _bootstrap_ is a widely applicable and extremely powerful statistical tool bootstrap that can be used to quantify the uncertainty associated with a given estimator or statistical learning method. As a simple example, the bootstrap can be used to estimate the standard errors of the coefficients from a linear regression fit. In the specific case of linear regression, this is not particularly useful, since we saw in Chapter 3 that standard statistical software such as `R` outputs such standard errors automatically. However, the power of the bootstrap lies in the fact that it can be easily applied to a wide range of statistical learning methods, including some for which a measure of variability is otherwise difficult to obtain and is not automatically output by statistical software. 

In this section we illustrate the bootstrap on a toy example in which we wish to determine the best investment allocation under a simple model. In Section 5.3 we explore the use of the bootstrap to assess the variability associated with the regression coefficients in a linear model fit. 

Suppose that we wish to invest a fixed sum of money in two financial assets that yield returns of _X_ and _Y_ , respectively, where _X_ and _Y_ are random quantities. We will invest a fraction _α_ of our money in _X_ , and will invest the remaining 1 _− α_ in _Y_ . Since there is variability associated with the returns on these two assets, we wish to choose _α_ to minimize the total risk, or variance, of our investment. In other words, we want to minimize Var( _αX_ + (1 _− α_ ) _Y_ ). One can show that the value that minimizes the risk is given by 

$$
\alpha = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2 \sigma_{XY}} \quad (5.6)
$$

where _σX_[2][= Var(] _[X]_[)] _[, σ] Y_[2][= Var(] _[Y]_[ )][,][and] _[σ][XY]_[= Cov(] _[X, Y]_[ )][.] In reality, the quantities _σX_[2][,] _[ σ] Y_[2][, and] _[ σ][XY]_[are unknown. We can compute] estimates for these quantities, _σ_ ˆ _X_[2][,] _[σ]_[ˆ] _Y_[2][,][and] _[σ]_[ˆ] _[XY]_[ ,][using][a][data][set][that] contains past measurements for _X_ and _Y_ . We can then estimate the value of _α_ that minimizes the variance of our investment using 

$$
\hat{\alpha} = \frac{\hat{\sigma}_Y^2 - \hat{\sigma}_{XY}}{\hat{\sigma}_X^2 + \hat{\sigma}_Y^2 - 2 \hat{\sigma}_{XY}} \quad (5.7)
$$

Figure 5.9 illustrates this approach for estimating _α_ on a simulated data set. In each panel, we simulated 100 pairs of returns for the investments _X_ and _Y_ . We used these returns to estimate _σX_[2] _[, σ] Y_[2][,][and] _[σ][XY]_[ ,][which][we] then substituted into (5.7) in order to obtain estimates for _α_ . The value of ˆ _α_ resulting from each simulated data set ranges from 0 _._ 532 to 0 _._ 657. 

It is natural to wish to quantify the accuracy of our estimate of _α_ . To estimate the standard deviation of _α_ ˆ, we repeated the process of simulating 100 paired observations of _X_ and _Y_ , and estimating _α_ using (5.7), 1,000 times. We thereby obtained 1,000 estimates for _α_ , which we can call _α_ ˆ1 _,_ ˆ _α_ 2 _, . . . ,_ ˆ _α_ 1 _,_ 000. The left-hand panel of Figure 5.10 displays a histogram of the resulting estimates. For these simulations the parameters were set to _σX_[2][= 1] _[, σ] Y_[2][= 1] _[.]_[25][,][and] _[σ][XY]_[= 0] _[.]_[5][,][and][so][we][know][that][the][true][value][of] _α_ is 0 _._ 6. We indicated this value using a solid vertical line on the histogram. 

5.2 The Bootstrap 213 

![Figure 5.9](./img/5_9.png)

**FIGURE 5.9.** _Each panel displays_ 100 _simulated returns for investments X and Y . From left to right and top to bottom, the resulting estimates for α are_ 0 _._ 576 _,_ 0 _._ 532 _,_ 0 _._ 657 _, and_ 0 _._ 651 _._ 

The mean over all 1,000 estimates for _α_ is 

$$
\bar{\alpha} = \frac{1}{1000} \sum_{r=1}^{1000} \hat{\alpha}_r = 0.5996
$$

very close to _α_ = 0 _._ 6, and the standard deviation of the estimates is 

$$
\sqrt{\frac{1}{1000 - 1} \sum_{r=1}^{1000} (\hat{\alpha}_r - \bar{\alpha})^2 } = 0.083
$$

This gives us a very good idea of the accuracy of _α_ ˆ: SE(ˆ _α_ ) _≈_ 0 _._ 083. So roughly speaking, for a random sample from the population, we would ˆ expect _α_ to differ from _α_ by approximately 0 _._ 08, on average. 

In practice, however, the procedure for estimating SE(ˆ _α_ ) outlined above cannot be applied, because for real data we cannot generate new samples from the original population. However, the bootstrap approach allows us to use a computer to emulate the process of obtaining new sample sets, so that we can estimate the variability of _α_ ˆ without generating additional samples. Rather than repeatedly obtaining independent data sets from the population, we instead obtain distinct data sets by repeatedly sampling observations _from the original data set_ . 

This approach is illustrated in Figure 5.11 on a simple data set, which we call _Z_ , that contains only _n_ = 3 observations. We randomly select _n_ observations from the data set in order to produce a bootstrap data set, 

214 5. Resampling Methods 

![Figure 5.10](./img/5_10.png)

**FIGURE 5.10.** Left: _A histogram of the estimates of α obtained by generating 1,000 simulated data sets from the true population._ Center: _A histogram of the estimates of α obtained from 1,000 bootstrap samples from a single data set._ Right: _The estimates of α displayed in the left and center panels are shown as boxplots. In each panel, the pink line indicates the true value of α._ 

_Z[∗]_[1] . The sampling is performed _with replacement_ , which means that the with same observation can occur more than once in the bootstrap data set. In this example, _Z[∗]_[1] contains the third observation twice, the first observation once, and no instances of the second observation. Note that if an observation is contained in _Z[∗]_[1] , then both its _X_ and _Y_ values are included. We can use _Z[∗]_[1] to produce a new bootstrap estimate for _α_ , which we call _α_ ˆ _[∗]_[1] . This procedure is repeated _B_ times for some large value of _B_ , in order to produce _B_ different bootstrap data sets, _Z[∗]_[1] _, Z[∗]_[2] _, . . . , Z[∗][B]_ , and _B_ corresponding _α_ estimates, _α_ ˆ _[∗]_[1] _,_ ˆ _α[∗]_[2] _, . . . ,_ ˆ _α[∗][B]_ . We can compute the standard error of these bootstrap estimates using the formula 

replacement 

$$
\text{SE}_B(\hat{\alpha}) = \sqrt{\frac{1}{B - 1} \sum_{r=1}^B \left( \hat{\alpha}^{*r} - \frac{1}{B} \sum_{r'=1}^B \hat{\alpha}^{*r'} \right)^2} \quad (5.8)
$$

This serves as an estimate of the standard error of _α_ ˆ estimated from the original data set. 

The bootstrap approach is illustrated in the center panel of Figure 5.10, which displays a histogram of 1,000 bootstrap estimates of _α_ , each computed using a distinct bootstrap data set. This panel was constructed on the basis of a single data set, and hence could be created using real data. Note that the histogram looks very similar to the left-hand panel, which displays the idealized histogram of the estimates of _α_ obtained by generating 1,000 simulated data sets from the true population. In particular the bootstrap estimate SE(ˆ _α_ ) from (5.8) is 0 _._ 087, very close to the estimate of 0 _._ 083 obtained using 1,000 simulated data sets. The right-hand panel displays the information in the center and left panels in a different way, via boxplots of the estimates for _α_ obtained by generating 1,000 simulated data sets from the true population and using the bootstrap approach. Again, the boxplots have similar spreads, indicating that the bootstrap approach can ˆ be used to effectively estimate the variability associated with _α_ . 

5.3 Lab: Cross-Validation and the Bootstrap 215 

![Figure 5.11](./img/5_11.png)

**FIGURE 5.11.** _A graphical illustration of the bootstrap approach on a small sample containing n_ = 3 _observations. Each bootstrap data set contains n observations, sampled with replacement from the original data set. Each bootstrap data set is used to obtain an estimate of α._ 

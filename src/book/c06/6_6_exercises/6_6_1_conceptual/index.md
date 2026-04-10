---
layout: default
title: "index"
---

# _Conceptual_ 

1. We perform best subset, forward stepwise, and backward stepwise selection on a single data set. For each approach, we obtain _p_ + 1 models, containing 0 _,_ 1 _,_ 2 _, . . . , p_ predictors. Explain your answers: 

   - (a) Which of the three models with _k_ predictors has the smallest _training_ RSS? 

   - (b) Which of the three models with _k_ predictors has the smallest _test_ RSS? 

   - (c) True or False: 

      - i. The predictors in the _k_ -variable model identified by forward stepwise are a subset of the predictors in the ( _k_ +1)-variable model identified by forward stepwise selection. 

      - ii. The predictors in the _k_ -variable model identified by backward stepwise are a subset of the predictors in the ( _k_ + 1)variable model identified by backward stepwise selection. 

      - iii. The predictors in the _k_ -variable model identified by backward stepwise are a subset of the predictors in the ( _k_ + 1)variable model identified by forward stepwise selection. 

      - iv. The predictors in the _k_ -variable model identified by forward stepwise are a subset of the predictors in the ( _k_ +1)-variable model identified by backward stepwise selection. 

      - v. The predictors in the _k_ -variable model identified by best subset are a subset of the predictors in the ( _k_ + 1)-variable model identified by best subset selection. 

2. For parts (a) through (c), indicate which of i. through iv. is correct. Justify your answer. 

   - (a) The lasso, relative to least squares, is: 

      - i. More flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrease in variance. 

      - ii. More flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias. 

      - iii. Less flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrease in variance. 

      - iv. Less flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias. 

   - (b) Repeat (a) for ridge regression relative to least squares. 

   - (c) Repeat (a) for non-linear methods relative to least squares. 

284 6. Linear Model Selection and Regularization 

3. Suppose we estimate the regression coefficients in a linear regression model by minimizing

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 \quad \text{subject to} \quad \sum_{j=1}^p \beta_j^2 \le s
$$

for a particular value of _s_ . For parts (a) through (e), indicate which of i. through v. is correct. Justify your answer. 

   - (a) As we increase _s_ from 0, the training RSS will: 

      - i. Increase initially, and then eventually start decreasing in an inverted U shape. 

      - ii. Decrease initially, and then eventually start increasing in a U shape. 

      - iii. Steadily increase. 

      - iv. Steadily decrease. 

      - v. Remain constant. 

   - (b) Repeat (a) for test RSS. 

   - (c) Repeat (a) for variance. 

   - (d) Repeat (a) for (squared) bias. 

   - (e) Repeat (a) for the irreducible error. 

4. Suppose we estimate the regression coefficients in a linear regression model by minimizing

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2
$$

for a particular value of _λ_ . For parts (a) through (e), indicate which of i. through v. is correct. Justify your answer. 

- (a) As we increase _λ_ from 0, the training RSS will: 

   - i. Increase initially, and then eventually start decreasing in an inverted U shape. 

   - ii. Decrease initially, and then eventually start increasing in a U shape. 

   - iii. Steadily increase. 

   - iv. Steadily decrease. 

   - v. Remain constant. 

- (b) Repeat (a) for test RSS. 

- (c) Repeat (a) for variance. 

- (d) Repeat (a) for (squared) bias. 

- (e) Repeat (a) for the irreducible error. 

6.6 Exercises 285 

5. It is well-known that ridge regression tends to give similar coefficient values to correlated variables, whereas the lasso may give quite different coefficient values to correlated variables. We will now explore this property in a very simple setting. 

Suppose that _n_ = 2, _p_ = 2, _x_ 11 = _x_ 12, _x_ 21 = _x_ 22. Furthermore, suppose that _y_ 1 + _y_ 2 = 0 and _x_ 11 + _x_ 21 = 0 and _x_ 12 + _x_ 22 = 0, so that the estimate for the intercept in a least squares, ridge regression, or lasso model is zero: _β_[ˆ] 0 = 0. 

   - (a) Write out the ridge regression optimization problem in this setting. 

   - (b) Argueˆ ˆthat in this setting, the ridge coefficient estimates satisfy _β_ 1 = _β_ 2. 

   - (c) Write out the lasso optimization problem in this setting. 

   - (d) Argue that in this setting, the lasso coefficients _β_[ˆ] 1 and _β_[ˆ] 2 are not unique—in other words, there are many possible solutions to the optimization problem in (c). Describe these solutions. 

6. We will now explore (6.12) and (6.13) further. 

   - (a) Consider (6.12) with _p_ = 1. For some choice of _y_ 1 and _λ >_ 0, plot (6.12) as a function of _β_ 1. Your plot should confirm that (6.12) is solved by (6.14). 

   - (b) Consider (6.13) with _p_ = 1. For some choice of _y_ 1 and _λ >_ 0, plot (6.13) as a function of _β_ 1. Your plot should confirm that (6.13) is solved by (6.15). 

7. We will now derive the Bayesian connection to the lasso and ridge regression discussed in Section 6.2.2. 

   - (a) Suppose that _yi_ = _β_ 0 + » _pj_ =1 _[x][ij][β][j]_[ +] _[ϵ][i]_[where] _[ ϵ]_[1] _[, . . . , ϵ][n]_[are inde-] pendent and identically distributed from a _N_ (0 _, σ_[2] ) distribution. Write out the likelihood for the data. 

   - (b) Assume the following prior for _β_ : _β_ 1 _, . . . , βp_ are independent and identically distributed according to a double-exponential distribution with mean 0 and common scale parameter _b_ : i.e. _p_ ( _β_ ) = 21 _b_[exp(] _[−|][β][|][/b]_[)][.][Write][out][the][posterior][for] _[β]_[in][this] setting. 

   - (c) Argue that the lasso estimate is the _mode_ for _β_ under this posterior distribution. 

   - (d) Now assume the following prior for _β_ : _β_ 1 _, . . . , βp_ are independent and identically distributed according to a normal distribution with mean zero and variance _c_ . Write out the posterior for _β_ in this setting. 

   - (e) Argue that the ridge regression estimate is both the _mode_ and the _mean_ for _β_ under this posterior distribution. 

286 6. Linear Model Selection and Regularization 

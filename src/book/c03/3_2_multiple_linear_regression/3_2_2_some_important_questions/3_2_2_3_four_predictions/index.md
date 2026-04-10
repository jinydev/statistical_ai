---
layout: default
title: "index"
---

# Four: Predictions 

Once we have fit the multiple regression model, it is straightforward to apply (3.21) in order to predict the response Y on the basis of a set of values for the predictors $X_1$ _, X_ 2 _, . . . , Xp_ . However, there are three sorts of uncertainty associated with this prediction. 

1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \dots, \beta_p$ . That is, the _least squares plane_ 

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p
$$

90 3. Linear Regression 

is only an estimate for the _true population regression plane_ 

$$
f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p
$$

The inaccuracy in the coefficient estimates is related to the _reducible error_ from Chapter 2. We can compute a _confidence interval_ in order to determine how close $\hat{Y}$ will be to $f(X)$. 

2. Of course, in practice assuming a linear model for $f(X)$ is almost always an approximation of reality, so there is an additional source of potentially reducible error which we call _model bias_ . So when we use a linear model, we are in fact estimating the best linear approximation to the true surface. However, here we will ignore this discrepancy, and operate as if the linear model were correct. 

3. Even if we knew $f(X)$—that is, even if we knew the true values for $\beta_0, \beta_1, \dots, \beta_p$ —the response value cannot be predicted perfectly because of the random error \epsilon in the model (3.20). In Chapter 2, we referred $\hat{Y}$ ? We useto this _prediction_ as the _irreducibleintervals_ to _error_ answer. Howthismuchquestion.will Y Predictionvary from intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for $f(X)$ (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error). 

We use a _confidence interval_ to quantify the uncertainty surrounding confidence the _average_ `sales` over a large number of cities. For example, given that interval $100\,000 is spent on `TV` advertising and $20\,000 is spent on `radio` advertising in each city, the 95 % confidence interval is [10 _,_ 985 _,_ 11 _,_ 528]. We interpret this to mean that 95 % of intervals of this form will contain the true value of $f(X)$.[9] On the other hand, a _prediction interval_ can be used to quantify the prediction uncertainty surrounding `sales` for a _particular_ city. Given that $100\,000 is interval spent on `TV` advertising and $20\,000 is spent on `radio` advertising in that city the 95 % prediction interval is [7 _,_ 930 _,_ 14 _,_ 580]. We interpret this to mean that 95 % of intervals of this form will contain the true value of Y for this city. Note that both intervals are centered at 11 _,_ 256, but that the prediction interval is substantially wider than the confidence interval, reflecting the increased uncertainty about `sales` for a given city in comparison to the average `sales` over many locations. 

> 9In other words, if we collect a large number of data sets like the `Advertising` data set, and we construct a confidence interval for the average `sales` on the basis of each data set (given $100\,000 in `TV` and $20\,000 in `radio` advertising), then 95 % of these confidence intervals will contain the true value of average `sales` . 

3.3 Other Considerations in the Regression Model 91 

---
layout: default
title: "index"
---

# _Applied_ 

8. This question involves the use of simple linear regression on the `Auto` data set. 

   - (a) Use the `sm.OLS()` function to perform a simple linear regression with `mpg` as the response and `horsepower` as the predictor. Use the `summarize()` function to print the results. Comment on the output. For example: 

      - i. Is there a relationship between the predictor and the response? 

      - ii. How strong is the relationship between the predictor and the response? 

      - iii. Is the relationship between the predictor and the response positive or negative? 

      - iv. What is the predicted `mpg` associated with a `horsepower` of 98? What are the associated 95 % confidence and prediction intervals? 

   - (b) Plot the response and the predictor in a new set of axes `ax` . Use the `ax.axline()` method or the `abline()` function defined in the lab to display the least squares regression line. 

   - (c) Produce some of diagnostic plots of the least squares regression fit as described in the lab. Comment on any problems you see with the fit. 

9. This question involves the use of multiple linear regression on the `Auto` data set. 

   - (a) Produce a scatterplot matrix which includes all of the variables in the data set. 

   - (b) Compute the matrix of correlations between the variables using the `DataFrame.corr()` method. 

`.corr()` 

- (c) Use the `sm.OLS()` function to perform a multiple linear regression with `mpg` as the response and all other variables except `name` as the predictors. Use the `summarize()` function to print the results. Comment on the output. For instance: 

   - i. Is there a relationship between the predictors and the response? Use the `anova_lm()` function from `statsmodels` to answer this question. 

130 3. Linear Regression 

      - ii. Which predictors appear to have a statistically significant relationship to the response? 

      - iii. What does the coefficient for the `year` variable suggest? 

   - (d) Produce some of diagnostic plots of the linear regression fit as described in the lab. Comment on any problems you see with the fit. Do the residual plots suggest any unusually large outliers? Does the leverage plot identify any observations with unusually high leverage? 

   - (e) Fit some models with interactions as described in the lab. Do any interactions appear to be statistically significant? 

   - (f) Try a few different transformations of the variables, such as log( X ), _√X_ , X[2] . Comment on your findings. 

10. This question should be answered using the `Carseats` data set. 

   - (a) Fit a multiple regression model to predict `Sales` using `Price` , `Urban` , and `US` . 

   - (b) Provide an interpretation of each coefficient in the model. Be careful—some of the variables in the model are qualitative! 

   - (c) Write out the model in equation form, being careful to handle the qualitative variables properly. 

   - (d) For which of the predictors can you reject the null hypothesis $H_0$ : $\beta_j$ = 0? 

   - (e) On the basis of your response to the previous question, fit a smaller model that only uses the predictors for which there is evidence of association with the outcome. 

   - (f) How well do the models in (a) and (e) fit the data? 

   - (g) Using the model from (e), obtain 95 % confidence intervals for the coefficient(s). 

   - (h) Is there evidence of outliers or high leverage observations in the model from (e)? 

11. In this problem we will investigate the $t$-statistic for the null hypothesis $H_0$ : _β_ = 0 in simple linear regression without an intercept. To begin, we generate a predictor `x` and a response `y` as follows. 

```
rng=np.random.default_rng(1)
x=rng.normal(size=100)
y=2*x+rng.normal(size=100)
```

- (a) Perform a simple linear regression of `y` onto `x` , _without_ an intercept. Report the coefficient estimate \hat{\beta} , the standard error of this coefficient estimate, and the $t$-statistic and $p$-value associated with the null hypothesis $H_0$ : _β_ = 0. Comment on these results. (You can perform regression without an intercept using the keywords argument `intercept=False` to `ModelSpec()` .) 

3.7 Exercises 131 

- (b) Now perform a simple linear regression of `x` onto `y` without an intercept, and report the coefficient estimate, its standard error, and the corresponding $t$-statistic and $p$-values associated with the null hypothesis $H_0$ : _β_ = 0. Comment on these results. 

- (c) What is the relationship between the results obtained in (a) and (b)? 

- (d) For the regression of Y onto X without an intercept, the _t_ - statistic for $H_0$ : _β_ = 0 takes the form _β/_[ˆ] SE( \hat{\beta} ), where \hat{\beta} is given by (3.38), and where 

**==> picture [133 x 31] intentionally omitted <==**

(These formulas are slightly different from those given in Sections 3.1.1 and 3.1.2, since here we are performing regression without an intercept.) Show algebraically, and confirm numerically in `R` , that the $t$-statistic can be written as 

**==> picture [181 x 32] intentionally omitted <==**

   - (e) Using the results from (d), argue that the $t$-statistic for the regression of `y` onto `x` is the same as the $t$-statistic for the regression of `x` onto `y` . 

   - (f) In `R` , show that when regression is performed _with_ an intercept, the $t$-statistic for $H_0$ : \beta_1 = 0 is the same for the regression of `y` onto `x` as it is for the regression of `x` onto `y` . 

12. This problem involves simple linear regression without an intercept. 

   - (a) Recall that the coefficient estimate \hat{\beta} for the linear regression of Y onto X without an intercept is given by (3.38). Under what circumstance is the coefficient estimate for the regression of X onto Y the same as the coefficient estimate for the regression of Y onto X ? 

   - (b) Generate an example in `Python` with $n$ = 100 observations in which the coefficient estimate for the regression of X onto Y is _different from_ the coefficient estimate for the regression of Y onto X . 

   - (c) Generate an example in `Python` with $n$ = 100 observations in which the coefficient estimate for the regression of X onto Y is _the same as_ the coefficient estimate for the regression of Y onto X . 

13. In this exercise you will create some simulated data and will fit simple linear regression models to it. Make sure to use the default random number generator with seed set to 1 prior to starting part (a) to ensure consistent results. 

132 3. Linear Regression 

- (a) Using the `normal()` method of your random number generator, create a vector, `x` , containing 100 observations drawn from a _N_ (0 _,_ 1) distribution. This represents a feature, X . 

- (b) Using the `normal()` method, create a vector, `eps` , containing 100 observations drawn from a _N_ (0 _,_ 0 _._ 25) distribution—a normal distribution with mean zero and variance 0 _._ 25. 

- (c) Using `x` and `eps` , generate a vector `y` according to the model 

**==> picture [182 x 11] intentionally omitted <==**

What is the length of the vector `y` ? What are the values of \beta_0 and \beta_1 in this linear model? 

   - (d) Create a scatterplot displaying the relationship between `x` and `y` . Comment on what you observe. 

   - (e) Fit a least squares linear model to predict `y` using `x` . Comment on the model obtained. How do \hat{\beta}_0 and \hat{\beta}_1 compare to \beta_0 and \beta_1? 

   - (f) Display the least squares line on the scatterplot obtained in (d). Draw the population regression line on the plot, in a different color. Use the `legend()` method of the axes to create an appropriate legend. 

   - (g) Now fit a polynomial regression model that predicts `y` using `x` and x[2] . Is there evidence that the quadratic term improves the model fit? Explain your answer. 

   - (h) Repeat (a)–(f) after modifying the data generation process in such a way that there is _less_ noise in the data. The model (3.39) should remain the same. You can do this by decreasing the variance of the normal distribution used to generate the error term \epsilon in (b). Describe your results. 

   - (i) Repeat (a)–(f) after modifying the data generation process in such a way that there is _more_ noise in the data. The model (3.39) should remain the same. You can do this by increasing the variance of the normal distribution used to generate the error term \epsilon in (b). Describe your results. 

   - (j) What are the confidence intervals for \beta_0 and \beta_1 based on the original data set, the noisier data set, and the less noisy data set? Comment on your results. 

14. This problem focuses on the _collinearity_ problem. 

   - (a) Perform the following commands in `Python` : 

```
rng=np.random.default_rng(10)
x1=rng.uniform(0,1,size=100)
x2=0.5*x1+rng.normal(size=100)/10
y=2+2*x1+0.3*x2+rng.normal(size=100)
```

The last line corresponds to creating a linear model in which `y` is a function of `x1` and `x2` . Write out the form of the linear model. What are the regression coefficients? 

3.7 Exercises 133 

- (b) What is the correlation between `x1` and `x2` ? Create a scatterplot displaying the relationship between the variables. 

- (c) Using this data, fit a least squares regression to predict `y` using `x1` _β_ ˆ2?andHow `x2` .doDescribethese relatethe resultsto theobtained.true \beta_0, What \beta_1, andare \beta_2 \hat{\beta} ?0,Can \hat{\beta}_1, andyou reject the null hypothesis $H_0$ : \beta_1 = 0? How about the null hypothesis $H_0$ : \beta_2 = 0? 

- (d) Now fit a least squares regression to predict `y` using only `x1` . Comment on your results. Can you reject the null hypothesis $H_0$ : \beta_1 = 0? 

- (e) Now fit a least squares regression to predict `y` using only `x2` . Comment on your results. Can you reject the null hypothesis $H_0$ : \beta_1 = 0? 

- (f) Do the results obtained in (c)–(e) contradict each other? Explain your answer. 

- (g) Suppose we obtain one additional observation, which was unfortunately mismeasured. We use the function `np.concatenate()` to `np.conca-` 

- add this additional observation to each of `x1` , `x2` and `y` . `tenate()` 

```
tenate()
```

```
x1=np.concatenate([x1,[0.1]])
x2=np.concatenate([x2,[0.8]])
y=np.concatenate([y,[6]])
```

Re-fit the linear models from (c) to (e) using this new data. What effect does this new observation have on the each of the models? In each model, is this observation an outlier? A high-leverage point? Both? Explain your answers. 

15. This problem involves the `Boston` data set, which we saw in the lab for this chapter. We will now try to predict per capita crime rate using the other variables in this data set. In other words, per capita crime rate is the response, and the other variables are the predictors. 

   - (a) For each predictor, fit a simple linear regression model to predict the response. Describe your results. In which of the models is there a statistically significant association between the predictor and the response? Create some plots to back up your assertions. 

   - (b) Fit a multiple regression model to predict the response using all of the predictors. Describe your results. For which predictors can we reject the null hypothesis $H_0$ : $\beta_j$ = 0? 

   - (c) How do your results from (a) compare to your results from (b)? Create a plot displaying the univariate regression coefficients from (a) on the _x_ -axis, and the multiple regression coefficients from (b) on the _y_ -axis. That is, each predictor is displayed as a single point in the plot. Its coefficient in a simple linear regression model is shown on the _x_ -axis, and its coefficient estimate in the multiple linear regression model is shown on the _y_ -axis. 

134 3. Linear Regression 

- (d) Is there evidence of non-linear association between any of the predictors and the response? To answer this question, for each predictor X , fit a model of the form 

**==> picture [154 x 11] intentionally omitted <==**

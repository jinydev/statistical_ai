---
layout: default
title: "index"
---

# _Conceptual_ 

1. Describe the null hypotheses to which the $p$-values given in Table 3.4 correspond. Explain what conclusions you can draw based on these $p$-values. Your explanation should be phrased in terms of `sales` , `TV` , `radio` , and `newspaper` , rather than in terms of the coefficients of the linear model. 

2. Carefully explain the differences between the KNN classifier and KNN regression methods. 

3. Suppose we have a data set with five predictors, $X_1$ = GPA, $X_2$ = IQ, X 3 = Level (1 for College and 0 for High School), X 4 = Interaction between GPA and IQ, and X 5 = Interaction between GPA and Level. The response is starting salary after graduation (in thousands ofˆ dollars).ˆ Supposeˆ we useˆleast squaresˆ to fitˆ the model, and get \beta_0 = 50 _, β_ 1 = 20 _, β_ 2 = 0 _._ 07 _, β_ 3 = 35 _, β_ 4 = 0 _._ 01 _, β_ 5 = _−_ 10. 

   - (a) Which answer is correct, and why? 

      - i. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates. 

      - ii. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates. 

128 3. Linear Regression 

      - iii. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates provided that the GPA is high enough. 

      - iv. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates provided that the GPA is high enough. 

   - (b) Predict the salary of a college graduate with IQ of 110 and a GPA of 4 _._ 0. 

   - (c) True or false: Since the coefficient for the GPA/IQ interaction term is very small, there is very little evidence of an interaction effect. Justify your answer. 

4. I collect a set of data ( $n$ = 100 observations) containing a single predictor and a quantitative response. I then fit a linear regression model to the data, as well as a separate cubic regression, i.e. Y = \beta_0 + \beta_1 X + \beta_2 X[2] + \beta_3 X[3] + \epsilon . 

   - (a) Suppose that the true relationship between X and Y is linear, i.e. Y = \beta_0 + \beta_1 X + \epsilon . Consider the training residual sum of squares (RSS) for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer. 

   - (b) Answer (a) using test rather than training RSS. 

   - (c) Suppose that the true relationship between X and Y is not linear, but we don’t know how far it is from linear. Consider the training RSS for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer. 

   - (d) Answer (c) using test rather than training RSS. 

5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the _i_ th fitted value takes the form 

where 

**==> picture [213 x 59] intentionally omitted <==**

Show that we can write 

**==> picture [65 x 28] intentionally omitted <==**

What is _ai′_ ? 

_Note: We interpret this result by saying that the fitted values from linear regression are_ linear combinations _of the response values._ 

3.7 Exercises 129 

6. Using (3.4), argue that in the case of simple linear regression, the least squares line always passes through the point (¯ _x,_ ¯ _y_ ). 

7. It is claimed in the text that in the case of simple linear regression of Y onto X , the $R^2$ statistic (3.17) is equal to the square of the correlation between X and Y (3.18). Prove that this is the case. For simplicity, you may assume that \bar{x} = \bar{y} = 0. 

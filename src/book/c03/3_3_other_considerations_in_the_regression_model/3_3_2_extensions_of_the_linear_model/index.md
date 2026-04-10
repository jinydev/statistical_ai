---
layout: default
title: "index"
---

# _3.3.2 Extensions of the Linear Model_ 

The standard linear regression model (3.19) provides interpretable results and works quite well on many real-world problems. However, it makes several highly restrictive assumptions that are often violated in practice. Two of the most important assumptions state that the relationship between the predictors and response are _additive_ and _linear_ . The additivity assumption additive means that the association between a predictor _Xj_ and the response Y does linear not depend on the values of the other predictors. The linearity assumption states that the change in the response Y associated with a one-unit change in _Xj_ is constant, regardless of the value of _Xj_ . In later chapters of this book, we examine a number of sophisticated methods that relax these two 

> 12There could still in theory be a difference between South and West, although the data here does not suggest any difference. 

3.3 Other Considerations in the Regression Model 95 

assumptions. Here, we briefly examine some common classical approaches for extending the linear model. 

Removing the Additive Assumption 

In our previous analysis of the `Advertising` data, we concluded that both `TV` and `radio` seem to be associated with `sales` . The linear models that formed the basis for this conclusion assumed that the effect on `sales` of increasing one advertising medium is independent of the amount spent on the other media. For example, the linear model (3.20) states that the average increase in `sales` associated with a one-unit increase in `TV` is always \beta_1, regardless of the amount spent on `radio` . 

However, this simple model may be incorrect. Suppose that spending money on radio advertising actually increases the effectiveness of TV advertising, so that the slope term for `TV` should increase as `radio` increases. In this situation, given a fixed budget of $100\,000, spending half on `radio` and half on `TV` may increase `sales` more than allocating the entire amount to either `TV` or to `radio` . In marketing, this is known as a _synergy_ effect, and in statistics it is referred to as an _interaction_ effect. Figure 3.5 suggests that such an effect may be present in the advertising data. Notice that when levels of either `TV` or `radio` are low, then the true `sales` are lower than predicted by the linear model. But when advertising is split between the two media, then the model tends to underestimate `sales` . 

Consider the standard linear regression model with two variables, 

**==> picture [121 x 10] intentionally omitted <==**

According to this model, a one-unit increase in $X_1$ is associated with an average increase in Y of \beta_1 units. Notice that the presence of $X_2$ does not alter this statement—that is, regardless of the value of $X_2$, a oneunit increase in $X_1$ is associated with a \beta_1-unit increase in Y . One way of extending this model is to include a third predictor, called an _interaction term_ , which is constructed by computing the product of $X_1$ and $X_2$. This results in the model 

**==> picture [246 x 11] intentionally omitted <==**

How does inclusion of this interaction term relax the additive assumption? Notice that (3.31) can be rewritten as 

**==> picture [250 x 25] intentionally omitted <==**

where _β_[˜] 1 = \beta_1 + \beta_3 $X_2$. Since _β_[˜] 1 is now a function of $X_2$, the association between $X_1$ and Y is no longer constant: a change in the value of $X_2$ will change the association between $X_1$ and Y . A similar argument shows that a change in the value of $X_1$ changes the association between $X_2$ and Y . 

For example, suppose that we are interested in studying the productivity of a factory. We wish to predict the number of `units` produced on the basis of the number of production `lines` and the total number of `workers` . It seems likely that the effect of increasing the number of production lines 

96 3. Linear Regression 

|3. Linear Regression|3. Linear Regression|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`TV`<br>`radio`<br>`TV`_×_`radio`|6.7502<br>0.248<br>27.23<br>_<_0_._0001<br>0.0191<br>0.002<br>12.70<br>_<_0_._0001<br>0.0289<br>0.009<br>3.24<br>0.0014<br>0.0011<br>0.000<br>20.73<br>_<_0_._0001|



**TABLE 3.9.** _For the_ `Advertising` _data, least squares coefficient estimates associated with the regression of_ `sales` _onto_ `TV` _and_ `radio` _, with an interaction term, as in (3.33)._ 

will depend on the number of workers, since if no workers are available to operate the lines, then increasing the number of lines will not increase production. This suggests that it would be appropriate to include an interaction term between `lines` and `workers` in a linear model to predict `units` . Suppose that when we fit the model, we obtain 

**==> picture [314 x 26] intentionally omitted <==**

In other words, adding an additional line will increase the number of units produced by 3 _._ 4 + 1 _._ 4 _×_ `workers` . Hence the more `workers` we have, the stronger will be the effect of `lines` . 

We now return to the `Advertising` example. A linear model that uses `radio` , `TV` , and an interaction between the two to predict `sales` takes the form 

**==> picture [296 x 26] intentionally omitted <==**

We can interpret \beta_3 as the increase in the effectiveness of TV advertising associated with a one-unit increase in radio advertising (or vice-versa). The coefficients that result from fitting the model (3.33) are given in Table 3.9. 

The results in Table 3.9 strongly suggest that the model that includes the interaction term is superior to the model that contains only _main effects_ . main effect The $p$-value for the interaction term, `TV` _×_ `radio` , is extremely low, indicating that there is strong evidence for _Ha_ : \beta_3 = 0. In other words, it is clear that the true relationship is not additive. The $R^2$ for the model (3.33) is 96.8 %, compared to only 89.7 % for the model that predicts `sales` using `TV` and `radio` without an interaction term. This means that (96 _._ 8 _−_ 89 _._ 7) _/_ (100 _−_ 89 _._ 7) = 69 % of the variability in `sales` that remains after fitting the additive model has been explained by the interaction term. The coefficient estimates in Table 3.9 suggest that an increase in TV advertising of $1\,000 is associated with increased sales of ( \hat{\beta}_1 + \hat{\beta} 3 _×_ `radio` ) _×_ 1\,000 = 19+1 _._ 1 _×_ `radio` units. And an increase in radio advertising of $1\,000 will be associated with an increase in sales of ( \hat{\beta} 2 + \hat{\beta} 3 _×_ `TV` ) _×_ 1\,000 = 29 + 1 _._ 1 _×_ `TV` units. 

In this example, the $p$-values associated with `TV` , `radio` , and the interaction term all are statistically significant (Table 3.9), and so it is obvious that all three variables should be included in the model. However, it is sometimes the case that an interaction term has a very small $p$-value, but the associated main effects (in this case, `TV` and `radio` ) do not. The _hierarchical principle_ states that _if we include an interaction in a model, we_ hierarchical 

principle 

3.3 Other Considerations in the Regression Model 97 

_should also include the main effects, even if the p-values associated with their coefficients are not significant._ In other words, if the interaction between $X_1$ and $X_2$ seems important, then we should include both $X_1$ and $X_2$ in the model even if their coefficient estimates have large $p$-values. The rationale for this principle is that if $X_1$ _× X_ 2 is related to the response, then whether or not the coefficients of $X_1$ or $X_2$ are exactly zero is of little interest. Also $X_1$ _× X_ 2 is typically correlated with $X_1$ and $X_2$, and so leaving them out tends to alter the meaning of the interaction. 

In the previous example, we considered an interaction between `TV` and `radio` , both of which are quantitative variables. However, the concept of interactions applies just as well to qualitative variables, or to a combination of quantitative and qualitative variables. In fact, an interaction between a qualitative variable and a quantitative variable has a particularly nice interpretation. Consider the `Credit` data set from Section 3.3.1, and suppose that we wish to predict `balance` using the `income` (quantitative) and `student` (qualitative) variables. In the absence of an interaction term, the model takes the form 

**==> picture [322 x 79] intentionally omitted <==**

Notice that this amounts to fitting two parallel lines to the data, one for students and one for non-students. The lines for students and non-students have different intercepts, \beta_0 + \beta_2 versus \beta_0, but the same slope, \beta_1. This is illustrated in the left-hand panel of Figure 3.7. The fact that the lines are parallel means that the average effect on `balance` of a one-unit increase in `income` does not depend on whether or not the individual is a student. This represents a potentially serious limitation of the model, since in fact a change in `income` may have a very different effect on the credit card balance of a student versus a non-student. 

This limitation can be addressed by adding an interaction variable, created by multiplying `income` with the dummy variable for `student` . Our model now becomes 

**==> picture [318 x 79] intentionally omitted <==**

Once again, we have two different regression lines for the students and the non-students. But now those regression lines have different intercepts, \beta_0+ \beta_2 versus \beta_0, as well as different slopes, \beta_1+ \beta_3 versus \beta_1. This allows for the possibility that changes in income may affect the credit card balances of students and non-students differently. The right-hand panel of Figure 3.7 

98 3. Linear Regression 

**==> picture [316 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
student<br>non−student<br>0 50 100 150 0 50 100 150<br>Income Income<br>1400 1400<br>1000 1000<br>Balance Balance<br>600 600<br>200 200<br>**----- End of picture text -----**<br>


**FIGURE 3.7.** _For the_ `Credit` _data, the least squares lines are shown for prediction of_ `balance` _from_ `income` _for students and non-students._ Left: _The model (3.34) was fit. There is no interaction between_ `income` _and_ `student` _._ Right: _The model (3.35) was fit. There is an interaction term between_ `income` _and_ `student` _._ 

shows the estimated relationships between `income` and `balance` for students and non-students in the model (3.35). We note that the slope for students is lower than the slope for non-students. This suggests that increases in income are associated with smaller increases in credit card balance among students as compared to non-students. 

---

## Sub-Chapters (하위 목차)

### Non-linear Relationships (비선형 관계)
* [문서로 이동하기](./3_3_2_1_non-linear_relationships/)

예측 변수와 반응 변수 간의 관계가 곡선 형태를 띌 때 잔차도 분석으로 이를 파악하고 다항식(Polynomial) 회귀로 유연하게 적합하는 방법을 소개합니다.
이를 통해 단순 선형 회귀보다 복잡한 트렌드를 추적할 수 있습니다.

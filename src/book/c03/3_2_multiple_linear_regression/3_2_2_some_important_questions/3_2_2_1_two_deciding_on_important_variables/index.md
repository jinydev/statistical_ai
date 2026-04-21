---
layout: default
title: "index"
---

[< 3.2.2 Some Important Questions](../index.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Two: Deciding on Important Variables

As discussed in the previous section, the first step in a multiple regression analysis is to compute the $F$-statistic and to examine the associated $p$-value.

If we conclude on the basis of that $p$-value that at least one of the predictors is related to the response, then it is natural to wonder _which_ are the guilty ones!

We could look at the individual $p$-values as in Table 3.4, but as discussed (and as further explored in Chapter 13), if $p$ is large we are likely to make some false discoveries.

It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors.

The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as _variable selection_.

The variable selection problem is studied extensively in Chapter 6, and so here we will provide only a brief outline of some classical approaches.

Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors.

For instance, if $p = 2$, then we can consider four models: (1) a model containing no variables, (2) a model containing $X_1$ only, (3) a model containing $X_2$ only, and (4) a model containing both $X_1$ and $X_2$.

We can then select the _best_ model out of all of the models that we have considered.

How do we determine which model is best?

Various statistics can be used to judge the quality of a model. These include Mallow's $C_p$, Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^2$.

These are discussed in more detail in Chapter 6.

We can also determine which model is best by plotting various model outputs, such as the residuals, in order to search for patterns.

Unfortunately, there are a total of $2^p$ models that contain subsets of $p$ variables.

This means that even for moderate $p$, trying out every possible subset of the predictors is infeasible.

For instance, we saw that if $p = 2$, then there are $2^2 = 4$ models to consider.

But if $p = 30$, then we must consider $2^{30} = 1,073,741,824$ models! This is not practical.

Therefore, unless $p$ is very small, we cannot consider all $2^p$ models, and instead we need an automated and efficient approach to choose a smaller set of models to consider.

There are three classical approaches for this task:

- _Forward selection_. We begin with the _null model_ — a model that contains an intercept but no predictors. We then fit $p$ simple linear regressions and add to the null model the variable that results in the lowest RSS. We then add to that model the variable that results in the lowest RSS for the new two-variable model. This approach is continued until some stopping rule is satisfied.

- _Backward selection_. We start with all variables in the model, and remove the variable with the largest $p$-value — that is, the variable that is the least statistically significant. The new $(p - 1)$-variable model is fit, and the variable with the largest $p$-value is removed. This procedure continues until a stopping rule is reached. For instance, we may stop when all remaining variables have a $p$-value below some threshold.

- _Mixed selection_. This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add variables one-by-one. Of course, as we noted with the `Advertising` example, the $p$-values for variables can become larger as new predictors are added to the model. Hence, if at any point the $p$-value for one of the variables in the model rises above a certain threshold, then we remove that variable from the model. We continue to perform these forward and backward steps until all variables in the model have a sufficiently low $p$-value, and all variables outside the model would have a large $p$-value if added to the model.

Backward selection cannot be used if $p > n$, while forward selection can always be used.

Forward selection is a greedy approach, and might include variables early that later become redundant. Mixed selection can remedy this.

---

## Sub-Chapters


[< 3.2.2 Some Important Questions](../index.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/index.html)

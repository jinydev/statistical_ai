---
layout: default
title: "index"
---

[< 4.6 Generalized Linear Models](../index.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.6.1 Linear Regression on the Bikeshare Data

To begin, we consider predicting `bikers` using linear regression. The results are shown in Table 4.10. We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour. We see that bike usage is highest in the spring and fall, and lowest during the winter months. Furthermore, bike usage is greatest around rush hour (9 AM and 6 PM), and lowest overnight. Thus, at first glance, fitting a linear regression model to the `Bikeshare` data set seems to provide reasonable and intuitive results.

But upon more careful inspection, some issues become apparent. For example, 9.6% of the fitted values in the `Bikeshare` data set are negative: that is, the linear regression model predicts a _negative_ number of users during 9.6% of the hours in the data set. This calls into question our ability to perform meaningful predictions on the data, and it also raises concerns about the accuracy of the coefficient estimates, confidence intervals, and other outputs of the regression model.

Furthermore, it is reasonable to suspect that when the expected value of `bikers` is small, the variance of `bikers` should be small as well. For instance, at 2 AM during a heavy December snow storm, we expect that extremely few people will use a bike, and moreover that there should be little variance associated with the number of users during those conditions. By contrast, between 7 AM and 10 AM, in April, May, and June, when skies are clear, there are 243.59 users, on average, with a standard deviation of 131.7. This is a major violation of the assumptions of a linear model, which state that $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a mean-zero error term with variance $\sigma^2$ that is _constant_, and not a function of the covariates. Therefore, the heteroscedasticity of the data calls into question the suitability of a linear regression model.

Finally, the response `bikers` is integer-valued. But under a linear model, $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a continuous-valued error term. This means that in a linear model, the response $Y$ is necessarily continuous-valued (quantitative). Thus, the integer nature of the response `bikers` suggests that a linear regression model is not entirely satisfactory for this data set.

Some of the problems that arise when fitting a linear regression model to the `Bikeshare` data can be overcome by transforming the response; for instance, we can fit the model

$$
\log(Y) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon \quad (4.38)
$$

Transforming the response avoids the possibility of negative predictions, and it overcomes much of the heteroscedasticity in the untransformed data. However, it is not quite a satisfactory solution, since predictions and inference are made in terms of the log of the response, rather than the response. Furthermore, a log transformation of the response cannot be applied in settings where the response can take on a value of 0. We will see in the next section that a Poisson regression model provides a much more natural and elegant approach for this task.

---

## Sub-Chapters


[< 4.6 Generalized Linear Models](../index.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/index.html)

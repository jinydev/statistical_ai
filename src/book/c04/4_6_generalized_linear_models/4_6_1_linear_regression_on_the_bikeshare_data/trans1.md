---
layout: default
title: "trans1"
---

[< 4.6 Generalized Linear Models](../trans1.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6.1 Linear Regression on the Bikeshare Data
# 4.6.1 Bikeshare 데이터에 대한 선형 회귀

To begin, we consider predicting `bikers` using linear regression. The results are shown in Table 4.10. We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour. We see that bike usage is highest in the spring and fall, and lowest during the winter months. Furthermore, bike usage is greatest around rush hour (9 AM and 6 PM), and lowest overnight. Thus, at first glance, fitting a linear regression model to the `Bikeshare` data set seems to provide reasonable and intuitive results.
시작하기 위해, 우리는 선형 회귀를 사용하여 `bikers`를 예측하는 것을 고려합니다. 결과는 표 4.10에 나타나 있습니다. 예를 들어, 날씨가 맑음에서 흐림으로 진행됨에 따라 시간당 자전거 이용자가 평균적으로 12.89명 감소함을 알 수 있습니다. 그러나 날씨가 비나 눈으로 더 진행되면, 시간당 자전거 이용자는 추가로 53.60명 더 감소합니다. 자전거 사용량은 봄과 가을에 가장 많고 겨울에 가장 적다는 것을 알 수 있습니다. 더욱이, 자전거 사용량은 출퇴근 시간(오전 9시 및 오후 6시) 전후로 가장 많고 밤새 가장 적습니다. 따라서 언뜻 보기에 `Bikeshare` 데이터 세트에 선형 회귀 모델을 피팅하는 것은 합리적이고 직관적인 결과를 제공하는 것처럼 보입니다.

But upon more careful inspection, some issues become apparent. For example, 9.6% of the fitted values in the `Bikeshare` data set are negative: that is, the linear regression model predicts a _negative_ number of users during 9.6% of the hours in the data set. This calls into question our ability to perform meaningful predictions on the data, and it also raises concerns about the accuracy of the coefficient estimates, confidence intervals, and other outputs of the regression model.
그러나 더 주의 깊게 살펴보면 몇 가지 문제가 분명해집니다. 예를 들어, `Bikeshare` 데이터 세트에서 피팅된 값의 9.6%가 양수가 아닙니다(음수입니다): 즉, 선형 회귀 모델은 데이터 세트의 시간 중 9.6% 동안 _음수_ 의 사용자 수를 예측합니다. 이는 데이터에 대해 의미 있는 예측을 수행할 수 있는 우리의 능력에 의문을 제기하며, 회귀 모델의 계수 추정치, 신뢰 구간 및 기타 출력의 정확성에 대한 우려도 제기합니다.

Furthermore, it is reasonable to suspect that when the expected value of `bikers` is small, the variance of `bikers` should be small as well. For instance, at 2 AM during a heavy December snow storm, we expect that extremely few people will use a bike, and moreover that there should be little variance associated with the number of users during those conditions. By contrast, between 7 AM and 10 AM, in April, May, and June, when skies are clear, there are 243.59 users, on average, with a standard deviation of 131.7. This is a major violation of the assumptions of a linear model, which state that $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a mean-zero error term with variance $\sigma^2$ that is _constant_, and not a function of the covariates. Therefore, the heteroscedasticity of the data calls into question the suitability of a linear regression model.
더욱이, `bikers`의 기대값이 작을 때 `bikers`의 분산 역시 작아야 한다고 합리적으로 의심할 수 있습니다. 예를 들어, 12월 폭설이 내리는 오전 2시에는 자전거를 사용하는 사람이 극히 적을 것으로 예상되며, 나아가 그러한 조건에서 사용자 수와 관련된 분산은 거의 없어야 합니다. 대조적으로 하늘이 맑은 4월, 5월 및 6월의 오전 7시에서 오전 10시 사이에는 평균 243.59명의 사용자가 있으며 표준 편차는 131.7입니다. 이는 $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$ 라는 선형 모델의 가정을 심각하게 위반하는 것으로, 여기서 $\epsilon$ 은 분산 $\sigma^2$ 를 갖는 평균이 0인 오차 항이며, 그 분산은 공변량의 함수가 아닌 _상수(constant)_ 입니다. 따라서 데이터의 이분산성(heteroscedasticity)은 선형 회귀 모델의 적합성에 의문을 제기합니다.

Finally, the response `bikers` is integer-valued. But under a linear model, $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a continuous-valued error term. This means that in a linear model, the response $Y$ is necessarily continuous-valued (quantitative). Thus, the integer nature of the response `bikers` suggests that a linear regression model is not entirely satisfactory for this data set.
마지막으로 반응 변수 `bikers`는 정수 값을 갖습니다. 그러나 선형 모델 하에서 $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$ 이며, 여기서 $\epsilon$ 은 연속 값을 갖는 오차 항입니다. 이는 선형 모델에서 반응 변수 $Y$가 필연적으로 연속 값(정량적)임을 의미합니다. 따라서 반응 변수 `bikers`의 정수적인 성질은 이 데이터 세트에 대해 선형 회귀 모델이 완전히 만족스럽지 않음을 시사합니다.

Some of the problems that arise when fitting a linear regression model to the `Bikeshare` data can be overcome by transforming the response; for instance, we can fit the model
`Bikeshare` 데이터에 선형 회귀 모델을 피팅할 때 발생하는 문제 중 일부는 반응 변수를 변환함으로써 극복될 수 있습니다; 예를 들어 다음과 같은 모델을 적용할 수 있습니다.

$$
\log(Y) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon \quad (4.38)
$$

Transforming the response avoids the possibility of negative predictions, and it overcomes much of the heteroscedasticity in the untransformed data. However, it is not quite a satisfactory solution, since predictions and inference are made in terms of the log of the response, rather than the response. Furthermore, a log transformation of the response cannot be applied in settings where the response can take on a value of 0. We will see in the next section that a Poisson regression model provides a much more natural and elegant approach for this task.
반응 변수를 변환하면 음수 예측의 가능성을 피할 수 있으며, 변환되지 않은 데이터의 이분산성을 상당 부분 상쇄할 수 있습니다. 그러나 이는 반응 변수 자체가 아니라 반응 변수의 로그 값으로 예측 및 추론이 이루어지기 때문에 아주 만족스러운 해결책은 아닙니다. 더욱이, 반응 변수가 0의 값을 가질 수 있는 설정에서는 반응 변수의 로그 변환을 적용할 수 없습니다. 다음 섹션에서 우리는 포아송 회귀 모델이 이 작업에 대해 훨씬 더 자연스럽고 우아한 접근 방식을 제공함을 볼 것입니다.

---

## Sub-Chapters

[< 4.6 Generalized Linear Models](../trans1.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans1.html)

---
layout: default
title: "index"
---

# 4.6 Generalized Linear Models 

In Chapter 3, we assumed that the response $Y$is quantitative, and explored the use of least squares linear regression to predict $Y$. Thus far in this chapter, we have instead assumed that $Y$is qualitative. However, we may sometimes be faced with situations in which $Y$is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable. 

As a concrete example, we consider the `Bikeshare` data set. The response is `bikers` , the number of hourly users of a bike sharing program in Washington, DC. This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or _counts_ . We will consider counts predicting `bikers` using the covariates `mnth` (month of the year), `hr` (hour of the day, from 0 to 23), `workingday` (an indicator variable that equals 1 if it is neither a weekend nor a holiday), `temp` (the normalized temperature, in Celsius), and `weathersit` (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.) 

In the analyses that follow, we will treat `mnth` , `hr` , and `weathersit` as qualitative variables. 

---

## Sub-Chapters (하위 목차)

### 4.6.1 Linear Regression on the Bikeshare Data (자전거 대여 데이터에서의 선형 회귀 적용)
* [문서로 이동하기](./4_6_1_linear_regression_on_the_bikeshare_data/)

카운트(음수가 불가능한 건수 데이터) 성질을 갖는 대여량에 일반 선형 회귀를 돌렸을 때 발생하는 음수 예측 등 불합리한 점을 확인합니다.

### 4.6.2 Poisson Regression on the Bikeshare Data (자전거 대여 데이터에서의 포아송 회귀 적용)
* [문서로 이동하기](./4_6_2_poisson_regression_on_the_bikeshare_data/)

카운트 데이터의 속성에 알맞게 부합하는 분포인 포아송(Poisson) 회귀 모델을 적용, 로그 링크 함수를 사용해 효과적인 성능을 얻습니다.

### 4.6.3 Generalized Linear Models in Greater Generality (보다 넓은 범주의 GLM 일반화 규칙)
* [문서로 이동하기](./4_6_3_generalized_linear_models_in_greater_generality/)

응답 패턴 군집(Exponential family) 개념을 통해 포아송, 이항 회귀, 정규 회귀 등이 결국 매개 변수만 다른 통일된 GLM 형식임을 증명합니다.

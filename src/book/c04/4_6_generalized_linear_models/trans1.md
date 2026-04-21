---
layout: default
title: "trans1"
---

[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/trans1.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6 Generalized Linear Models
# 4.6 일반화 선형 모델

In Chapter 3, we assumed that the response $Y$ is quantitative, and explored the use of least squares linear regression to predict $Y$. Thus far in this chapter, we have instead assumed that $Y$ is qualitative. However, we may sometimes be faced with situations in which $Y$ is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable.
제 3장에서 우리는 반응 변수 $Y$가 정량적(quantitative)이라고 가정하고, $Y$를 예측하기 위해 최소 제곱 선형 회귀의 사용을 탐구했습니다. 지금까지 이 장에서 우리는 대신 $Y$가 정성적(qualitative)이라고 가정했습니다. 그러나 때때로 우리는 $Y$가 정성적이지도 정량적이지도 않은 상황에 직면할 수 있으며, 따라서 제 3장의 선형 회귀도, 이 장에서 다룬 분류 접근법도 적용할 수 없습니다.

As a concrete example, we consider the `Bikeshare` data set. The response is `bikers`, the number of hourly users of a bike sharing program in Washington, DC. This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or _counts_. We will consider predicting `bikers` using the covariates `mnth` (month of the year), `hr` (hour of the day, from 0 to 23), `workingday` (an indicator variable that equals 1 if it is neither a weekend nor a holiday), `temp` (the normalized temperature, in Celsius), and `weathersit` (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.)
구체적인 예로, 우리는 `Bikeshare` 데이터 세트를 고려합니다. 반응 변수는 미국 워싱턴 DC의 자전거 공유 프로그램의 시간당 사용자 수인 `bikers` 입니다. 이 반응 변수 값은 정성적이지도 정량적이지도 않습니다: 대신, 음이 아닌 정수 값, 즉 _개수(counts)_ 를 취합니다. 우리는 다음 공변량들을 사용하여 `bikers` 를 예측하는 것을 고려할 것입니다: `mnth` (연중 월), `hr` (하루 중 시간, 0에서 23까지), `workingday` (주말도 휴일도 아닌 경우 1과 같은 지시 변수), `temp` (섭씨로 정규화된 온도) 및 `weathersit` (맑음; 옅은 안개 또는 흐림; 가벼운 비 또는 가벼운 눈; 호우 또는 폭설의 네 가지 가능한 값 중 하나를 취하는 정성적 변수).

In the analyses that follow, we will treat `mnth`, `hr`, and `weathersit` as qualitative variables.
이어지는 분석에서, 우리는 `mnth`, `hr`, 그리고 `weathersit`을 정성적 변수로 취급할 것입니다.

---

### 4.6.1 Linear Regression on the Bikeshare Data
### 4.6.1 Bikeshare 데이터에 대한 선형 회귀

### 4.6.2 Poisson Regression on the Bikeshare Data
### 4.6.2 Bikeshare 데이터에 대한 포아송 회귀

### 4.6.3 Generalized Linear Models in Greater Generality
### 4.6.3 더 넓은 일반성의 일반화 선형 모델

---

## Sub-Chapters

[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/trans1.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/trans1.html)

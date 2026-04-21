---
layout: default
title: "index"
---

[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/index.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.6 Generalized Linear Models

In Chapter 3, we assumed that the response $Y$ is quantitative, and explored the use of least squares linear regression to predict $Y$. Thus far in this chapter, we have instead assumed that $Y$ is qualitative. However, we may sometimes be faced with situations in which $Y$ is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable.

As a concrete example, we consider the `Bikeshare` data set. The response is `bikers`, the number of hourly users of a bike sharing program in Washington, DC. This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or _counts_. We will consider predicting `bikers` using the covariates `mnth` (month of the year), `hr` (hour of the day, from 0 to 23), `workingday` (an indicator variable that equals 1 if it is neither a weekend nor a holiday), `temp` (the normalized temperature, in Celsius), and `weathersit` (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.)

In the analyses that follow, we will treat `mnth`, `hr`, and `weathersit` as qualitative variables.

---

### 4.6.1 Linear Regression on the Bikeshare Data

### 4.6.2 Poisson Regression on the Bikeshare Data

### 4.6.3 Generalized Linear Models in Greater Generality

---

## Sub-Chapters


[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/index.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/index.html)

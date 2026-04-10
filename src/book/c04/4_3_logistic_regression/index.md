---
layout: default
title: "index"
---

# 4.3 Logistic Regression 

Consider again the `Default` data set, where the response `default` falls into one of two categories, `Yes` or `No` . Rather than modeling this response $Y$directly, logistic regression models the _probability_ that $Y$belongs to a particular category. 

For the `Default` data, logistic regression models the probability of default. For example, the probability of default given `balance` can be written as 

$$
p(	ext{balance}) = 	ext{Pr}(	ext{default} = 	ext{Yes} \mid 	ext{balance})
$$

The values of Pr( `default` = `Yes` _|_ `balance` ), which we abbreviate _p_ ( `balance` ), will range between 0 and 1. Then for any given value of `balance` , a prediction can be made for `default` . For example, one might predict default = Yes 

4.3 Logistic Regression 139 

![Figure 4.2](./img/4_2.png)

**FIGURE 4.2.** _Classification using the_ `Default` _data._ Left: _Estimated probability of_ `default` _using linear regression. Some estimated probabilities are negative! The orange ticks indicate the 0/1 values coded for_ `default` _(_ `No` _or_ `Yes` _)._ Right: _Predicted probabilities of_ `default` _using logistic regression. All probabilities lie between_ 0 _and_ 1 _._ 

for any individual for whom _p_ (balance) _>_ 0 _._ 5. Alternatively, if a company wishes to be conservative in predicting individuals who are at risk for default, then they may choose to use a lower threshold, such as _p_ (balance) _>_ 0 _._ 1. 

---

## Sub-Chapters (하위 목차)

### 4.3.1 The Logistic Model (로지스틱 모형)
* [문서로 이동하기](./4_3_1_the_logistic_model/)

오즈(Odds)와 로짓(Logit) 변환을 선형 함수와 매핑해 로지스틱 모형을 구축하는 수식을 유도합니다.
수학적으로 선형 관계가 로그 오즈 단위에서 성립함을 살펴봅니다.

### 4.3.2 Estimating the Regression Coefficients (회귀 계수 추정)
* [문서로 이동하기](./4_3_2_estimating_the_regression_coefficients/)

관측된 데이터가 나올 확률을 최대로 만드는 최대 우도 추정법(Maximum Likelihood Estimation)을 배웁니다.
로지스틱 회귀에서 손실을 어떻게 최소화하는지 식별합니다.

### 4.3.3 Making Predictions (예측하기)
* [문서로 이동하기](./4_3_3_making_predictions/)

추정된 계수를 바탕으로 특정 주어진 특성값 하에서 어떠한 클래스에 속할 확률을 수식과 파이썬 코드로 도출하는 방법입니다.
특정 임계값(Threshold)을 넘는 타겟을 분류 예측합니다.

### 4.3.4 Multiple Logistic Regression (다중 로지스틱 회귀)
* [문서로 이동하기](./4_3_4_multiple_logistic_regression/)

예측 변수(X)가 여러 개인 경우로 확장하여, 교란 변수 효과와 복잡한 요인 분석을 동시에 수행하는 방법을 다룹니다.
조건부 확률에 여러 변수가 미치는 영향을 검토합니다.

### 4.3.5 Multinomial Logistic Regression (다항 로지스틱 회귀)
* [문서로 이동하기](./4_3_5_multinomial_logistic_regression/)

타겟 클래스가 2개를 넘어 3개 이상(예: 질병 3종류 분류)일 때 적용할 수 있도록 로지스틱 회귀 모델 체계를 통계적으로 확장합니다.

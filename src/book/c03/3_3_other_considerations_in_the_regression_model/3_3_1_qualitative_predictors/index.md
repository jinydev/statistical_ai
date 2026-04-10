---
layout: default
title: "index"
---

# _3.3.1 Qualitative Predictors_ 

In our discussion so far, we have assumed that all variables in our linear regression model are _quantitative_ . But in practice, this is not necessarily the case; often some predictors are _qualitative_ . 

For example, the `Credit` data set displayed in Figure 3.6 records variables for a number of credit card holders. The response is `balance` (average credit card debt for each individual) and there are several quantitative predictors: `age` , `cards` (number of credit cards), `education` (years of education), `income` (in thousands of dollars), `limit` (credit limit), and `rating` (credit rating). Each panel of Figure 3.6 is a scatterplot for a pair of variables whose identities are given by the corresponding row and column labels. For example, the scatterplot directly to the right of the word “Balance” depicts `balance` versus `age` , while the plot directly to the right of “Age” corresponds to `age` versus `cards` . In addition to these quantitative variables, we also have four qualitative variables: `own` (house ownership), `student` (student status), `status` (marital status), and `region` (East, West or South). 

---

## Sub-Chapters (하위 목차)

### Predictors with Only Two Levels (수준이 2개인 예측 변수)
* [문서로 이동하기](./3_3_1_1_predictors_with_only_two_levels/)

남성/여성과 같이 단 두 가지 범주만 갖는 단순한 질적 변수를 0과 1의 값으로 매핑해 기초적인 회귀 분석을 수행하는 방법을 봅니다.
각 더미 코딩이 계수 해석에 미치는 영향을 확인합니다.

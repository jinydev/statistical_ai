---
layout: default
title: "index"
---

# 3.2.2 Some Important Questions

When we perform multiple linear regression, we usually are interested in answering a few important questions.

1. _Is at least one of the predictors $X_1, X_2, \dots, X_p$ useful in predicting the response?_
2. _Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?_
3. _How well does the model fit the data?_
4. _Given a set of predictor values, what response value should we predict, and how accurate is our prediction?_

We now address each of these questions in turn.

## One: Is There a Relationship Between the Response and Predictors?

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$. In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \dots = \beta_p = 0$. As in the simple linear regression setting, we use a hypothesis test to answer this question. We test the null hypothesis,

$$
H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad (3.23)
$$

versus the alternative

$$
H_a : \text{at least one } $\beta_j$ \text{ is non-zero.}
$$

This hypothesis test is performed by computing the _F -statistic_ , 

$F$-statistic 

$$
F = \frac{(\text{RSS}_0 - \text{RSS}) / q}{\text{RSS} / (n - $p$ - 1)} \quad (3.25)
$$

¯ where, as with simple linear regression, TSS =[�] ( _yi − y_ )[2] and RSS = ˆ 2 �( _yi − yi_ ) . If the linear model assumptions are correct, one can show that 

$$
E\{\text{RSS} / (n - $p$ - 1)\} = \sigma^2
$$

and that, provided $H_0$ is true, 

$$
E\{(\text{TSS} - \text{RSS}) / p\} = \sigma^2
$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1. On the other hand, if $H_a$ is true, then $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$, so we expect $F$ to be greater than 1. 

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6. In this example the $F$-statistic is 570. Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$. In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`. However, what if the $F$-statistic had been closer to 1? How large does the $F$-statistic need to be before we can reject $H_0$ and

3.2 Multiple Linear Regression 85 

| Quantity | Value |
| :--- | :--- |
| Residual standard error | 1.69 |
| $$R^2$$ | 0.897 |
| $F$-statistic | 570 |



**TABLE 3.6.** _More information about the least squares model for the regression of number of units sold on TV, newspaper, and radio advertising budgets in the_ `Advertising` _data. Other information about this model was displayed in Table 3.4._ 

conclude that there is a relationship? It turns out that the answer depends on the values of $n$ and $p$. When $n$ is large, an $F$-statistic that is just a little larger than 1 might still provide evidence against $H_0$. In contrast, a larger $F$-statistic is needed to reject $H_0$ if $n$ is small. When $H_0$ is true and the errors $\epsilon_i$ have a normal distribution, the $F$-statistic follows an $F$-distribution.$^6$ For any given value of $n$ and $p$, any statistical software package can be used to compute the $p$-value associated with the $F$-statistic using this distribution. Based on this $p$-value, we can determine whether or not to reject $H_0$. For the advertising data, the $p$-value associated with the $F$-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased `sales`. In (3.23) we are testing $H_0$ that all the coefficients are zero. Sometimes we want to test that a particular subset of $q$ of the coefficients are zero. This corresponds to a null hypothesis

$$
H_0 : \beta_{p-q+1} = \beta_{p-q+2} = \dots = \beta_p = 0
$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables _except_ those last $q$. Suppose that the residual sum of squares for that model is $\text{RSS}_0$. Then the appropriate $F$-statistic is

$$
F = \frac{(\text{RSS}_0 - \text{RSS}) / q}{\text{RSS} / (n - $p$ - 1)} \quad (3.25)
$$

Notice that in Table 3.4, for each individual predictor a $t$-statistic and a $p$-value were reported. These provide information about whether each individual predictor is related to the response, after adjusting for the other predictors. It turns out that each of these is exactly equivalent[7] to the $F$-test that omits that single variable from the model, leaving all the others in—i.e. $q=1$ in (3.24). So it reports the _partial effect_ of adding that variable to the model. For instance, as we discussed earlier, these $p$-values indicate that `TV` and `radio` are related to `sales` , but that there is no evidence that `newspaper` is associated with `sales` , when `TV` and `radio` are held fixed. 

Given these individual $p$-values for each variable, why do we need to look at the overall $F$-statistic? After all, it seems likely that if any one of the $p$-values for the individual variables is very small, then _at least one of the predictors is related to the response_ . However, this logic is flawed, especially when the number of predictors $p$ is large. 

> 6Even if the errors are not normally-distributed, the $F$-statistic approximately follows an _F_ -distribution provided that the sample size $n$ is large. 

> 7The square of each $t$-statistic is the corresponding $F$-statistic. 

86 3. Linear Regression 

For instance, consider an example in which $p$ = 100 and $H_0$ : $\beta_1 = \beta_2 = \dots = \beta_p = 0$ is true, so no variable is truly associated with the response. In this situation, about 5 % of the $p$-values associated with each variable (of the type shown in Table 3.4) will be below 0.05 by chance. In other words, we expect to see approximately five small $p$-values even in the absence of any true association between the predictors and the response.[8] In fact, it is likely that we will observe at least one $p$-value below 0.05 by chance! Hence, if we use the individual $t$-statistics and associated $p$-values in order to decide whether or not there is any association between the variables and the response, there is a very high chance that we will incorrectly conclude that there is a relationship. However, the $F$-statistic does not suffer from this problem because it adjusts for the number of predictors. Hence, if $H_0$ is true, there is only a 5 % chance that the $F$-statistic will result in a $p$-value below 0.05, regardless of the number of predictors or the number of observations. 

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$ . However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the _F_ - statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as _forward selection_ , can be used. This _high-dimensional_ setting is discussed in greater detail in Chapter 6. 


---

## Sub-Chapters (하위 목차)

### Two: Deciding on Important Variables (질문 2: 중요한 변수 결정)
* [문서로 이동하기](./3_2_2_1_two_deciding_on_important_variables/)

다수의 변수 중 반응 변수와 실제로 유의미한 관계가 있는 변수 조합들을 선택(Variable Selection)하는 방법을 배웁니다.
전진 선택법(Forward), 후진 제거법(Backward) 및 혼합 선택법의 개념을 간단히 다룹니다.

### Three: Model Fit (질문 3: 모델 적합성)
* [문서로 이동하기](./3_2_2_2_three_model_fit/)

선택된 다중 회귀 모델이 주어진 훈련 데이터에 얼마나 잘 적합되었는지 다중 R² 지표 및 RSE를 통해 살펴봅니다.
변수가 추가될 때마다 R²가 증가하는 성질에 대비한 평가를 소개합니다.

### Four: Predictions (질문 4: 예측)
* [문서로 이동하기](./3_2_2_3_four_predictions/)

적합된 모델을 바탕으로 새로운 관측치에 대한 반응 변수 스코어를 예측할 때 수반되는 세 가지 큰 불확실성을 검토합니다.
신뢰 구간 및 예측 구간(Prediction Interval)의 차이를 명확히 살펴봅니다.

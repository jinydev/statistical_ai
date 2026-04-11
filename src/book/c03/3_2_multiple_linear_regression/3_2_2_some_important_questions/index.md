---
layout: default
title: "index"
---

# 3.2.2 Some Important Questions (몇 가지 중요한 질문들)

When we perform multiple linear regression, we usually are interested in answering a few important questions.
우리가 통상 다중 선형 회귀를 수행할 때, 우린 으레 다음과 같은 몇 가지 중요한 질문들에 해답을 구하는 데 관심을 기울이곤 합니다.

1. _Is at least one of the predictors $X_1, X_2, \dots, X_p$ useful in predicting the response?_
1. _수많은 예측 요인 $X_1, X_2, \dots, X_p$ 중에서, 타깃 반응값을 예측하는 데 진정 유용한 지표가 단 하나라도 존재하는가?_ 

2. _Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?_
2. _투입된 모든 예측 변수들이 타깃 $Y$ 의 변동성을 설명하는 것에 다같이 기여하는가, 아니면 오직 극히 일부의 변수들 정도만이 비로소 유용한 쓰임새를 지니는가?_

3. _How well does the model fit the data?_
3. _도출된 예측 모델은 과연 우리 손안의 데이터에 도대체 얼마나 탁월하게 부합되어 들어맞는가?_

4. _Given a set of predictor values, what response value should we predict, and how accurate is our prediction?_
4. _특정 예측 요인 값들이 주어졌을 때, 우린 과연 그에 따르는 어느 특정 반응값을 예측해 내야 올바르며, 또 그 예측 결과치 자체는 도대체 통계상 어느 수준으로 정밀하고 정확한가?_

We now address each of these questions in turn.
우린 비단 이 지면에서, 이들 질문의 양상을 쫓아 순서대로 하나씩 다뤄 보겠습니다.

## One: Is There a Relationship Between the Response and Predictors? (질문 1: 반응 타깃과 예측 변수들 사이에 과연 일말의 상관관계가 존재하는가?)

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$. 
과거 단순 선형 회귀 환경 하에서는, 타깃 반응치와 애초 단일 예측 변수 단둘 사이에 과연 관계가 존재하는지 여부를 판단하기 위해, 우린 그저 단순히 계수 수치가 $\beta_1 = 0$ 이 되는지 여부만을 확인해 볼 수 있었던 사실을 다시금 상기해 보십시오. 

In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \dots = \beta_p = 0$. 
그러나 이에 반해 무려 $p$ 개의 다수 예측 변수들을 무장시킨 다중 회귀 무대 상에선, 우린 반드시 모든 개별 회귀 계수들이 통째 0 인지 여부, 즉 다시 말해 등식 $\beta_1 = \beta_2 = \dots = \beta_p = 0$ 성립 여부를 묻고 조명해 볼 필요성이 요구됩니다.

As in the simple linear regression setting, we use a hypothesis test to answer this question. 
앞서 단순 선형 회귀 때와 매한가지로, 우린 이 질문에 대답을 구하고자 가설 검정(hypothesis test) 도구를 활용합니다. 

We test the null hypothesis,
우린 다음의 귀무가설(null hypothesis)을 시험해 봅니다.

$$
H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad (3.23)
$$

versus the alternative
여기에 맞대응하는 대립가설(alternative hypothesis)은 다음과 같습니다.

$$
H_a : \text{at least one } \beta_j \text{ is non-zero.}
$$

This hypothesis test is performed by computing the _F -statistic_ , 
이 가설 검정 과정은 곧 다음의 _F-통계량 (F-statistic)_ 값을 계산하는 방식으로 이뤄집니다. 

$F$-statistic ($F$-통계량)

$$
F = \frac{(\text{RSS}_0 - \text{RSS}) / q}{\text{RSS} / (n - p - 1)} \quad (3.25)
$$

where, as with simple linear regression, $\text{TSS} = \sum (y_i - \bar{y})^2$ and $\text{RSS} = \sum (y_i - \hat{y}_i)^2$. 
여기서, 단순 선형 회귀의 맥락과 똑같이, $\text{TSS}$ 는 타깃 결과값 자체의 전체 편차 총 제곱합 덩치 $\sum (y_i - \bar{y})^2$ 풀이를 뜻해 나타내며, $\text{RSS}$ 는 회귀 모델 통찰 후 잔여 덩어리 지표인 잔차 제곱합 부분 $\sum (y_i - \hat{y}_i)^2$ 측을 표상합니다. 

If the linear model assumptions are correct, one can show that 
만약 선형 모델의 모든 전제 가정들이 기적같이 매끄럽게 사실로 참인 것이 맞다면, 우린 당당히 다음 결과 수식 역시 증명해 보여줄 수 있습니다.

$$
E\{\text{RSS} / (n - p - 1)\} = \sigma^2
$$

and that, provided $H_0$ is true, 
더불어 투입된 귀무가설 $H_0$ 도 참이라는 전제 조건 하에서는 무릇 다음과 같은 등식 수치가 동시에 성립 확립된다는 것까지도 밝혀낼 수 있습니다.

$$
E\{(\text{TSS} - \text{RSS}) / p\} = \sigma^2
$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1. 
결과적으로 해석하자면, 예측 모수 집합들과 응답값 사이에 일말의 유의미한 상관관계가 전무한 형국 구도일 경우, 우린 으레 장황한 저 $F$-통계량 지표값이 단호히 대략 1 에 수렴하는 매우 가까운 점수로 산출될 것이라 당연히 기대해 볼 수 있습니다. 

On the other hand, if $H_a$ is true, then $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$, so we expect $F$ to be greater than 1.
이와는 상반되게, 반대로 만약 대립가설 $H_a$ 가 기어코 참인 것으로 드러난 상황이라면 결론은 $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$ 이 되므로, 당연 자연스럽게도 저 $F$-통계량 수치는 1 이란 스코어 장벽을 훌쩍 넘어서며 크게 치솟을 것임을 짐작 예측해 볼 수 있는 이치입니다.

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6. 
`sales` 를 `radio`, `TV`, `newspaper` 에 회귀시켜 얻은 다중 선형 회귀 모델의 $F$-통계량은 표 3.6에 나와 있습니다. 

In this example the $F$-statistic is 570. 
이 예제에서 $F$-통계량은 570입니다. 

Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$. 
이 값은 1보다 훨씬 크기 때문에 귀무가설 $H_0$ 에 반하는 강력한 증거를 제공합니다. 

In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`. 
다시 말해, 큰 $F$-통계량은 적어도 하나의 광고 매체가 `sales` 와 관련이 있음을 나타냅니다. 

However, what if the $F$-statistic had been closer to 1? 
하지만 만약 $F$-통계량이 1에 더 가까웠다면 어땠을까요? 

How large does the $F$-statistic need to be before we can reject $H_0$ and

3.2 Multiple Linear Regression 85 

| Quantity | Value |
| :--- | :--- |
| Residual standard error | 1.69 |
| $$R^2$$ | 0.897 |
| $F$-statistic | 570 |



**TABLE 3.6.** _More information about the least squares model for the regression of number of units sold on TV, newspaper, and radio advertising budgets in the_ `Advertising` _data. Other information about this model was displayed in Table 3.4._ 
**TABLE 3.6.** `Advertising` _데이터에서 TV, 신문, 라디오 광고 예산에 따른 판매량의 최소 제곱 회귀 모델에 대한 추가 정보입니다. 이 모델에 대한 또 다른 정보는 표 3.4에 표시되었습니다._

conclude that there is a relationship? 
결론적으로 상관관계가 있다고 판단하려면 $F$-통계량이 얼마나 커야 할까요? 

It turns out that the answer depends on the values of $n$ and $p$. 
그 답은 $n$ 과 $p$ 의 값에 따라 달라집니다. 

When $n$ is large, an $F$-statistic that is just a little larger than 1 might still provide evidence against $H_0$. 
$n$ 이 클 때는 $F$-통계량이 1보다 조금만 커도 여전히 $H_0$ 에 반하는 증거를 제공할 수 있습니다. 

In contrast, a larger $F$-statistic is needed to reject $H_0$ if $n$ is small. 
반대로 $n$ 이 작다면 $H_0$ 를 기각하기 위해 더 큰 $F$-통계량이 필요합니다. 

When $H_0$ is true and the errors $\epsilon_i$ have a normal distribution, the $F$-statistic follows an $F$-distribution.$^6$ 
$H_0$ 가 참이고 오차 $\epsilon_i$ 가 정규 분포를 따른다면, $F$-통계량은 $F$-분포를 따릅니다.$^6$ 

For any given value of $n$ and $p$, any statistical software package can be used to compute the $p$-value associated with the $F$-statistic using this distribution. 
주어진 $n$ 과 $p$ 값에 대해, 통계 소프트웨어 패키지는 이 분포를 사용하여 $F$-통계량과 연관된 $p$-값을 계산할 수 있습니다. 

Based on this $p$-value, we can determine whether or not to reject $H_0$. 
이 $p$-값을 바탕으로 $H_0$ 를 기각할지 여부를 결정할 수 있습니다. 

For the advertising data, the $p$-value associated with the $F$-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased `sales`. 
광고 데이터의 경우, 표 3.6의 $F$-통계량에 수반된 $p$-값은 사실상 0이므로 적어도 하나의 매체가 `sales` 증가와 관련되어 있다는 강력한 증거를 확보하게 됩니다. 

In (3.23) we are testing $H_0$ that all the coefficients are zero. 
수식 (3.23)에서 우리는 모든 회귀 계수가 0인지 여부를 묻는 $H_0$ 가설을 검정하고 있습니다. 

Sometimes we want to test that a particular subset of $q$ of the coefficients are zero. 
때로는 전체 변수 중에서 $q$ 개의 특정 부분 집합에 해당하는 계수들만이 0인지 검정하고 싶을 수도 있습니다. 

This corresponds to a null hypothesis
이는 다음의 귀무가설에 해당합니다:

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

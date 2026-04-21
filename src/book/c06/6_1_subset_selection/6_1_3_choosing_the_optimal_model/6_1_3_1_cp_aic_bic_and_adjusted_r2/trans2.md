---
layout: default
title: "trans2"
---

# $C_p$, AIC, BIC, and Adjusted $R^2$ 
# $C_p$, AIC, BIC 및 조정된 $R^2$: 과적합에 벌점 매기기

We show in Chapter 2 that the training set $\text{MSE}$ is generally an underestimate of the test MSE. (Recall that $\text{MSE}$ = RSS $/n$.) This is because when we fit a model to the training data using least squares, we specifically estimate the regression coefficients such that the training RSS (but not the test RSS) is as small as possible. In particular, the training error will decrease as more variables are included in the model, but the test error may not. Therefore, training set RSS and training set $R^2$ cannot be used to select from among a set of models with different numbers of variables. 
2장에서 뼈저리게 배웠듯, '훈련장 성적(training MSE)'은 실전 '테스트 성적'의 거품 낀 버전에 불과합니다. 왜냐하면 우리가 최소 제곱법으로 모델을 맞출 때, 오직 훈련장 에러($\text{RSS}$)만을 미친 듯이 깎아내리도록 선수를 훈련시키기 때문입니다. 변수를 많이 욱여넣을수록 훈련장 성적은 무조건 좋아지지만, 실전 성적은 오히려 폭망할 수 있습니다. 즉, 훈련장 전용 스펙인 $\text{RSS}$ 나 $R^2$ 로는 결코 '최고의 실전 모델'을 골라낼 수 없습니다.

However, a number of techniques for _adjusting_ the training error for the model size are available. These approaches can be used to select among a set of models with different numbers of variables. We now consider four such approaches: $C_p$, Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^2$. Figure 6.2 displays $C_p$, BIC, and adjusted $R^2$ for the best model of each size produced by best subset selection on the `Credit` data set. 
그래서 똑똑한 학자들은 거품 낀 훈련 성적에 모델의 체급(변수 개수)만큼 **'페널티(벌점) 조정'** 을 가하는 기법들을 만들어냈습니다. 이번 장에서는 그중 가장 유명한 4대장인 $C_p$, AIC, BIC, 그리고 조정된 $R^2$ 를 영접할 것입니다.

For a fitted least squares model containing $d$ predictors, the $C_p$ estimate of test $\text{MSE}$ is computed using the equation
$d$ 개의 변수를 가진 최소 제곱 모델에게 $C_p$ 방식은 다음과 같은 공식으로 실전 타격을 산출합니다:

$$
C_p = \frac{1}{n} (\text{RSS} + 2 d \hat{\sigma}^2) \quad (6.2)
$$

where $\hat{\sigma}^2$ is an estimate of the variance of the error $\epsilon$ associated with each response measurement in (6.1).[^4] Typically $\hat{\sigma}^2$ is estimated using the full model containing all predictors. Essentially, the $C_p$ statistic adds a penalty of $2 d \hat{\sigma}^2$ to the training RSS in order to adjust for the fact that the training error tends to underestimate the test error. Clearly, the penalty increases as the number of predictors in the model increases; this is intended to adjust for the corresponding decrease in training RSS. Though it is beyond the scope of this book, one can show that if $\hat{\sigma}^2$ is an unbiased estimate of $\sigma^2$ in (6.2), then $C_p$ is an unbiased estimate of test MSE. As a consequence, the $C_p$ statistic tends to take on a small value for models with a low test error, so when determining which of a set of models is best, we choose the model with the lowest $C_p$ value. In Figure 6.2, $C_p$ selects the six-variable model containing the predictors `income` , `limit` , `rating` , `cards` , `age` and `student` . 
여기서 핵심은 수식 뒤에 붙잡고 있는 저 무지막지한 **$2 d \hat{\sigma}^2$ 이라는 벌점(penalty)** 덩어리입니다. 훈련 $\text{RSS}$ 에 이 족쇄를 채움으로써, 변수 $d$ 의 개수가 많아질수록 훈련 오차가 꼼수로 줄어드는 현상을 강력하게 응징해버립니다. 결론적으로 $C_p$ 수치가 가장 바닥을 찍는 가장 작은(lowest) 모델이 바로 최후의 승자가 됩니다. 

> [^4] $C_p$ 의 변형 버전인 $C_p'$ 도 결국 본질은 완벽히 동일합니다.

![Figure 6.2](./img/6_2.png)

**FIGURE 6.2.** $C_p$, BIC, and adjusted $R^2$ _are shown for the best models of each size for the_ `Credit` _data set._ 
**그림 6.2** `Credit` *데이터 세트에서 각 변수 체급별 모델들을 세 가지 척도로 심판한 결과입니다.*

The AIC criterion is defined for a large class of models fit by maximum likelihood. In the case of the model (6.1) with Gaussian errors, maximum likelihood and least squares are the same thing. In this case AIC is given by
라이벌인 AIC 기준 또한 최대 우도법 환경에서 주로 쓰이지만, 최소 제곱 환경에서는 방금 배운 $C_p$ 랑 그냥 영혼의 쌍둥이입니다. 식 구조는 다음과 같습니다:

$$
\text{AIC} = \frac{1}{n \hat{\sigma}^2} (\text{RSS} + 2 d \hat{\sigma}^2) \quad (6.3)
$$

where, for simplicity, we have omitted irrelevant constants.[^5] Hence for least squares models, $C_p$ and AIC are proportional to each other, and so only $C_p$ is displayed in Figure 6.2. 
불필요한 쓰레기 상수를 제거하면 AIC 와 $C_p$ 는 완벽히 비례하므로, 굳이 두 번 그릴 필요가 없습니다. 그림 6.2 에도 $C_p$ 하나만 덩그러니 놓은 이유입니다.

> [^5] 수식적 디테일을 궁금해하는 수학 괴짜들을 위해 남기지만 범위를 벗어납니다.

BIC is derived from a Bayesian point of view, but ends up looking similar to $C_p$ (and AIC) as well. For the least squares model with $d$ predictors, the BIC is, up to irrelevant constants, given by
또 다른 심판 베이즈(BIC) 는 베이즈 이론에서 파생되었으나, 막상 뚜껑을 열어보면 앞의 두 녀석과 똑같이 생겼습니다. 

$$
\text{BIC} = \frac{1}{n} (\text{RSS} + \log(n) d \hat{\sigma}^2) \quad (6.4)
$$

Like $C_p$, the BIC will tend to take on a small value for a model with a low test error, and so generally we select the model that has the lowest BIC value. Notice that BIC replaces the $2 d \hat{\sigma}^2$ used by $C_p$ with a $\log(n) d \hat{\sigma}^2$ term, where $n$ is the number of observations. Since $\log n > 2$ for any $n > 7$, the BIC statistic generally places a heavier penalty on models with many variables, and hence results in the selection of smaller models than $C_p$. In Figure 6.2, we see that this is indeed the case for the `Credit` data set; BIC chooses a model that contains only the four predictors `income` , `limit` , `cards` , and `student` . 
마찬가지로 BIC 도 값이 제일 작은 모델을 에이스로 추앙합니다. 하지만 엄청난 반전이 숨어 있습니다. 앞선 $C_p$ 는 페널티를 곱게 "$2 \times d$" 개를 때렸지만, 무자비한 이 BIC는 이걸 "**$\log(n) \times d$**" 로 진화시켜 버렸습니다. $n$ 이 7만 넘어도 이 페널티는 압도적으로 육중해집니다. 즉, 군더더기 변수가 많은 뚱뚱한 모델에게 더 흉악한 벌점을 투하하므로, BIC 의 심판을 통과한 챔피언들은 대체로 앞선 지표들보다 훨씬 변수 개수가 날씬하고 작습니다. 

The adjusted $R^2$ statistic is another popular approach for selecting among a set of models that contain different numbers of variables. Recall from Chapter 3 that the usual $R^2$ is defined as $1 − \text{RSS} / \text{TSS}$, where $\text{TSS} = \sum(y_i − \bar{y})^2$ is the _total sum of squares_ for the response. Since RSS always decreases as more variables are added to the model, the $R^2$ always increases as more variables are added. For a least squares model with $d$ variables, the adjusted $R^2$ statistic is calculated as
마지막 대항마는 '조정된 $R^2$' 통계량입니다. 변수를 넣을수록 기존 $R^2$ 점수가 공짜로 우상향하는 맹점을 막기 위해, 분모에 $d$ 족쇄를 걸어 계산식을 파격적으로 개조했습니다.

$$
\text{Adjusted } R^2 = 1 - \frac{\text{RSS} / (n - d - 1)}{\text{TSS} / (n - 1)} \quad (6.5)
$$

Unlike $C_p$, AIC, and BIC, for which a _small_ value indicates a model with a low test error, a _large_ value of adjusted $R^2$ indicates a model with a small test error. Maximizing the adjusted $R^2$ is equivalent to minimizing $\frac{\text{RSS}}{n−d−1}$. While RSS always decreases as the number of variables in the model increases, $\frac{\text{RSS}}{n−d−1}$ may increase or decrease, due to the presence of $d$ in the denominator. 
앞선 세 놈들이 최대한 '작은 값'을 찾았다면, 이 녀석만큼은 가장 **'큰 값(large)'** 을 띄어야만 최고의 에이스 대우를 해줍니다. 

The intuition behind the adjusted $R^2$ is that once all of the correct variables have been included in the model, adding additional _noise_ variables will lead to only a very small decrease in RSS. Since adding noise variables leads to an increase in $d$, such variables will lead to an increase in $\frac{\text{RSS}}{n−d−1}$, and consequently a decrease in the adjusted $R^2$. Therefore, in theory, the model with the largest adjusted $R^2$ will have only correct variables and no noise variables. Unlike the $R^2$ statistic, the adjusted $R^2$ statistic _pays a price_ for the inclusion of unnecessary variables in the model.
조정 $R^2$ 의 직관은 사이다 같습니다. 쓸모없는 잉여 노이즈 변수(noise variable) 를 팀에 합류시킨다면, $\text{RSS}$ 에러 축소 이득은 먼지 코딱지만 한데, 분모의 페널티 숫자통 $d$ 만 뚱뚱하게 불려 무자비한 벌금 고지서(pays a price) 를 맞게 되고 점수는 나락을 갑니다. 따라서 이 지표로 단련된 최고의 챔피언 모델 안에는, 거품 변수가 1명도 존재하지 않는 순결한 상태가 됩니다.

$C_p$, AIC, and BIC all have rigorous theoretical justifications that are beyond the scope of this book. These justifications rely on asymptotic arguments (scenarios where the sample size $n$ is very large). Despite its popularity, and even though it is quite intuitive, the adjusted $R^2$ is not as well motivated in statistical theory as AIC, BIC, and $C_p$. All of these measures are simple to use and compute. Here we have presented their formulas in the case of a linear model fit using least squares; however, AIC and BIC can also be defined for more general types of models. 
앞의 괴물 3대장($C_p$, AIC, BIC) 은 소름 돋게 치밀한 통계 수학 이론 증명 기반을 내포하고 있습니다. 반면에 우리의 친근한 '조정 $R^2$' 는 사실 그만큼의 살벌한 수학적 뼈대(theoretical justification) 는 없습니다. 그럼에도 불구하고 이 4종목 채점 방식들은 너무나 다루기 쉽고 심플하여 무조건 알아두어야 하는 꿀 지표들입니다.

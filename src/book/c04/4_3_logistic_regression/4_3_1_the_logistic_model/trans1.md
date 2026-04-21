---
layout: default
title: "trans1"
---

[< 4.3 Logistic Regression](../trans1.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.1 The Logistic Model
# 4.3.1 로지스틱 모형 (The Logistic Model)

How should we model the relationship between $p(X) = \text{Pr}(Y=1 \mid X)$ and $X$? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent these probabilities:
우리는 대체 어떻게 $p(X) = \text{Pr}(Y=1 \mid X)$ 와 예측 변수 $X$ 사이의 관계를 모델링해야 할까요? (편의를 위해 종속 변수에 대한 일반적인 0과 1 코딩을 사용한다고 합시다.) 앞서 4.2절에서 우리는 이 확률들을 재현해 내기 위해 선형 회귀 모델을 사용하는 안을 고려했었습니다:

$$
p(X) = \beta_0 + \beta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance`, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1. These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1. This problem is not unique to the credit default data. Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of $X$ and $p(X) > 1$ for others (unless the range of $X$ is limited).
만약 우리가 통장 잔고(`balance`)를 사용해서 파산(`default = Yes`)을 예측하려고 이 접근법(직선 선형 방정식)을 들이민다면, 우리는 그림 4.2의 왼쪽 패널과 같은 무지막지한 모델을 얻게 됩니다. 여기서 우리는 이 접근법의 한계와 마주합니다: 잔고가 0에 가깝게 떨어지면 우리는 '마이너스(-)' 확률이라는 말도 안 되는 예측을 하게 되며, 잔고가 엄청나게 많은 부자들을 예측할 경우에는 '1(100%)'을 가볍게 돌파하는 예측값을 얻습니다. 이런 예측은 상식적이지 않습니다. 당연히 진짜 파산 확률은 잔고가 얼마건 간에 무조건 0과 1 사이에 포섭되어야 하기 때문입니다. 이 문제는 신용 카드 데이타 집합에서만 유독 발생하는 게 아닙니다. 이론적으로 따졌을 때 0이나 1로 세팅된 반응 변수에 '직선'을 피팅시키려고 하는 한 어떤 $X$ 지점에서는 $p(X) < 0$ 가, 반대쪽에서는 $p(X) > 1$ 가 되는 불상사가 늘 벌어집니다 (물론 $X$의 조회가 극도로 제한된 경우는 예외입니다).

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of $X$. Many functions meet this description. In logistic regression, we use the _logistic function_,
이 괴랄한 확률 이탈 버그를 피하려면, 우리는 무조건 모든 $X$를 대입해도 항상 출력이 0과 1 사이로만 나오게 가둬버리는 특수 함수를 동원해서 $p(X)$를 모델링해야만 합니다. 사실 이런 성질을 만족하는 함수는 세상에 많습니다. 그중에서도 우리가 배울 로지스틱 회귀에서는, **로지스틱 함수(Logistic Function)** 라는 것을 사용합니다:

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \quad (4.2)
$$

To fit the model (4.2), we use a method called _maximum likelihood_, which we discuss in the next section. The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the `Default` data. Notice that for low balances we now predict the probability of default as close to, but never below, zero. Likewise, for high balances we predict a default probability close to, but never above, one. The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction. We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot. The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.
이 (4.2)번 모형을 데이터에 맞게 찍어 누르기(피팅) 위해서, 우리는 다음 절에서 설명할 **최대 우도(Maximum Likelihood)** 라는 수학적 탐색 방법을 씁니다. 그림 4.2의 오른쪽 패널은 이 멋진 로지스틱 곡선이 `Default` 데이터에 얼마나 기가 막히게 들어맞는지를 보여줍니다. 이제 잔고가 아무리 낮아도 확률은 0에 무한히 가까워질지언정 절대로 0 밑으로 파고들지(음수) 않음에 주목하십시오. 마찬가지로 잔고가 억만장자가 되어도 파산 확률은 1에 육박할 뿐 절대로 1천장을 넘지 않습니다. 로지스틱 함수는 이처럼 형태적으로 항상 매끄러운 **S자 모양(S-shaped)**의 곡선을 생성해 내며, 그 덕분에 돌발적인 $X$ 값이 들어와도 늘 이치에 맞는 상식적인 확률을 뱉어냅니다. 또한 우리는 이 로지스틱 곡선 모델이 왼쪽 그림의 강압적인 일직선보다 체납 확률의 궤적을 훠씬 더 그럴싸하게 포착해 냄을 알 수 있습니다. 두 경우 모두 훈련 데이터를 요약한 평균 예측 확률은 0.0333으로, 무작위 데이터의 전체 실제 연체자 비율과 똑같게 계산됩니다.

After a bit of manipulation of (4.2), we find that
이 (4.2)번 수식을 살짝만 뒤틀어(변환해) 보면, 다음과 같은 놀라운 식을 얻어낼 수 있습니다.

$$
\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X} \quad (4.3)
$$

The quantity $p(X) / [1 - p(X)]$ is called the _odds_, and can take on any value between 0 and $\infty$. Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively. For example, on average 1 in 5 people with an odds of $1/4$ will default, since $p(X) = 0.2$ implies an odds of $0.2 / (1 - 0.2) = 1/4$. Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X) = 0.9$ implies an odds of $0.9 / (1 - 0.9) = 9$. Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.
여기서 $\frac{p(X)}{[1 - p(X)]}$ 라는 요상한 덩어리를 통계학에선 **오즈(Odds, 승산)** 라고 부르는데, 이 녀석은 확률 구간을 타파하고 0부터 무한대($\infty$)까지 모든 값을 마음껏 가질 수 있습니다. 오즈 값이 0에 가깝거나 무한대에 가깝다는 건 각각 체납 확률이 엄청나게 낮고 100%에 가깝게 높다는 뜻입니다. 예를 들어 오즈비가 $1/4$ (즉 0.25)인 5명 그룹은 평균 1명이 파산합니다. 왜냐하면 $p(X)=0.2$ 일 때 계산 식이 $0.2 / 0.8 = 1/4$ 로 똑 떨어지기 때문입니다. 마찬가지로, 파산 확률이 90% 인 그룹은 오즈비가 무려 $9$ 가 됩니다 ($0.9 / 0.1 = 9$). 이 비율(오즈) 개념은 1/10 단위의 확률보다는 베팅 전략을 이해하고 직관화하기가 편해서 경마판과 같은 도박판에서 전통적으로 줄곧 쓰여왔습니다!

By taking the logarithm of both sides of (4.3), we arrive at
이제 저 (4.3)번 수식 양쪽에 자연로그($\log$)를 씌워버리면 수학적 마법이 벌어집니다.

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_. We see that the logistic regression model (4.2) has a logit that is linear in $X$.
수식의 저 기괴한 왼쪽 덩어리는 **로그 오즈(Log Odds)** 혹은 **로짓(Logit)** 이라고 불리는 핵심입니다. 놀랍게도 그 지저분했던 곡선 로지스틱 모형(4.2)은, 로짓이라는 공간으로 변환되는 순간 예측변수 $X$와 완벽하게 선형적인(Linear) 1차 방정식 구조를 갖추게 됩니다!

Recall from Chapter 3 that in a linear regression model, $\beta_1$ gives the average change in $Y$ associated with a one-unit increase in $X$. By contrast, in a logistic regression model, increasing $X$ by one unit changes the log odds by $\beta_1$ (4.4). Equivalently, it multiplies the odds by $e^{\beta_1}$ (4.3). However, because the relationship between $p(X)$ and $X$ in (4.2) is not a straight line, $\beta_1$ does _not_ correspond to the change in $p(X)$ associated with a one-unit increase in $X$. The amount that $p(X)$ changes due to a one-unit change in $X$ depends on the current value of $X$. But regardless of the value of $X$, if $\beta_1$ is positive then increasing $X$ will be associated with increasing $p(X)$, and if $\beta_1$ is negative then increasing $X$ will be associated with decreasing $p(X)$.
3장 선형 회귀 모형에서는 기울기 $\beta_1$ 이 "$X$가 1 오를 때마다 $Y$가 평균적으로 정확히 똑같이 얼마만큼 뛴다"고 설명했었습니다. 하지만 로지스틱 회귀에서 $X$가 1 단위를 올릴 경우 뛰는 쪽은 확률 $Y$ 가 아니라, 오직 저 **로그 오즈 지표가 $\beta_1$ 만큼 뛴다**는 뜻입니다 (4.4번 식). 다시 말해 원래 도박꾼의 오즈 값에는 $e^{\beta_1}$ 가 곱해져 눈덩이처럼 불어납니다 (4.3번 식). 이 부드러운 (4.2)번 곡선 방정식에서 확률과 성장의 관계는 일직선이 아니기 때문에, $\beta_1$ 의 수치 자체가 실제 $p(X)$ 확률이 퍼센트별로 오르는 고정된 변화량에 대응하지는 **않습니다**. $X$가 조금 변할 때 점프하는 확률 변화폭은 내가 현재 S자 곡선의 가장자리 평지에 있는지 아니면 중앙의 가파른 언덕에 서있는지 S 곡선 S 좌표의 현재 위치(기울기 체감도)에 전부 종속되어 있습니다. 그럼에도 불구하고, 만약 계산된 $\beta_1$ 이 + 양수라면 $X$가 오를수록 $p(X)$도 S자 언덕을 올라 늘어난다는 우상향 흐름 자체는 똑같이 일관성 있게 보장됩니다.

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.3 Logistic Regression](../trans1.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans1.html)

---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.1 Simple Linear Regression](../trans2.html) | [3.1.2 Assessing the Accuracy of the Coefficient Estimates >](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html)

# 3.1.1 Estimating the Coefficients
# 3.1.1 계수 추정

In practice, $\beta_0$ and $\beta_1$ are unknown.
현실 세계 속에서, 완벽한 정답인 $\beta_0$(기본 매출)와 $\beta_1$(광고의 진짜 효과)의 값은 신이 아닌 이상 알 길이 없습니다.

So before we can use (3.1) to make predictions, we must use data to estimate the coefficients.
그래서 주어진 방정식 (3.1)을 써먹어 미래를 예측하기 전에, 일단 우리 손에 쥐어진 과거의 데이터를 바탕으로 이 미지의 계수들을 '이렇게 생겼을 것이다'라고 그럴싸하게 추정(estimate)해내야만 합니다.

Let
다음을

$$
(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)
$$

represent $n$ observation pairs, each of which consists of a measurement of $X$ and a measurement of $Y$.
여기에 $n$개의 데이터 짝꿍들이 있다고 상상해 봅시다. 각각의 짝꿍은 '원인(X)' 하나와 '결과(Y)' 하나로 곱따이 묶여 있는 진짜 과거 관측치 기록입니다.

In the `Advertising` example, this data set consists of the TV advertising budget and product sales in $n = 200$ different markets.
우리가 계속 우려먹는 `Advertising(광고)` 예시에서, 이 데이터 더미들은 총 200곳의 서로 다른 동네(시장)에서 기록해 둔 'TV 광고비에 부은 돈'과 '팔려나간 제품 개수'의 기록들입니다.

(Recall that the data are displayed in Figure 2.1.)
(앞 단원 그림 2.1에서 점으로 콕콕 찍혀 흩뿌려져 있던 그 빨간 데이터들을 머릿속으로 다시 떠올려 보세요.)

Our goal is to obtain coefficient estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ such that the linear model (3.1) fits the available data well—that is, so that $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ for $i = 1, \dots, n$.
우리가 여기서 이루고자 하는 최종 목표는 바로 이것입니다! 선형 모델 (3.1)이 흩뿌려진 데이터 점들을 최대한 잘 관통하도록 절편 추정치 $\hat{\beta}_0$와 기울기 추정치 $\hat{\beta}_1$(모자가 씌워져 있으면 '진짜 정답'이 아니라 '우리가 찍은 추정치'란 뜻이에요)를 구해내는 것, 즉 다시 말해 모든 $y_i$ 점의 위치 근처( $\approx$ )로 우리의 선($\hat{\beta}_0 + \hat{\beta}_1 x_i$)이 찰떡같이 지나가게 만드는 것입니다.

In other words, we want to find an intercept $\hat{\beta}_0$ and a slope $\hat{\beta}_1$ such that the resulting line is as close as possible to the $n = 200$ data points.
달리 말하면, 우리가 긋게 될 직선이 무려 200개나 되는 데이터 점들에 한 치의 오차라도 덜 내면서 '가장 가깝게' 스쳐 지나가도록 만들어줄 완벽한 절편($\hat{\beta}_0$)과 기울기($\hat{\beta}_1$)를 찾아내는 게임입니다.

There are a number of ways of measuring _closeness_.
종이에 점들이 찍혀있을 때 어떤 선이 가장 점들과 '가깝다(_closeness_)'고 우길 수 있을까요? 그 척도를 재는 방법은 아주 다양합니다.

However, by far the most common approach involves minimizing the _least squares_ criterion, and we take that approach in this chapter.
하지만 압도적으로 현업에서 가장 많이 쓰는 방법은 바로 오차를 제곱해서 더한 값이 가장 작게 되도록 만드는 은밀한 스킬, 즉 '_최소 제곱법(least squares)_' 기준을 활용하는 것이며, 이번 장에서는 그 방법을 택해 선을 긋겠습니다.

Alternative approaches will be considered in Chapter 6.
물론 이 방법 말고도 다른 희한한 방법들이 존재하는데, 나중에 6장에서 가서야 슬쩍 소개해 드릴 예정입니다.

Let $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the prediction for $Y$ based on the $i$th value of $X$.
우리가 구한 공식을 써서 $i$번째 $X$값(예를 들어 i번째 동네의 TV 광고비)을 집어넣었을 때 모델이 '이만큼 팔릴걸요?' 하고 내뱉은 짐작값을 $\hat{y}_i$라고 부릅시다.

Then $e_i = y_i - \hat{y}_i$ represents the $i$th _residual_—this is the difference between the $i$th observed response value and the $i$th response value that is predicted by our linear model.
그러면 현실의 진짜 정답인 $y_i$에서 우리의 짐작값 $\hat{y}_i$를 뺀 찌꺼기 $e_i$가 도출되는데, 이것을 멋진 말로 $i$번째 '_잔차(residual)_'라고 부릅니다. 쉽게 말해 '진짜 일어난 일'과 '우리의 모델이 예측한 일' 사이의 어긋난 틈, 즉 빗나간 오차의 크기입니다.

We define the _residual sum of squares_ (RSS) as
우리는 이 수많은 오차 찌꺼기들의 덩치를 합친 '_잔차 제곱합(RSS)_'이라는 무시무시한 괴물을 다음과 같이 정의해버립니다.

$$
\text{RSS} = e_1^2 + e_2^2 + \dots + e_n^2
$$

or equivalently as $$
\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1 x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1 x_2)^2 + \dots + (y_n - \hat{\beta}_0 - \hat{\beta}_1 x_n)^2 \quad (3.3)
$$
이것을 모델 공식으로 다시 길게 풀어서 쓰면 모양새가 이렇게 됩니다. $$
\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1 x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1 x_2)^2 + \dots + (y_n - \hat{\beta}_0 - \hat{\beta}_1 x_n)^2 \quad (3.3)
$$

The least squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS.
우리가 사용하는 최소 제곱법 대마법은 바로 이 오차 쓰레기통인 RSS가 세상에서 제일 작아지게 만드는 마법의 $\hat{\beta}_0$와 $\hat{\beta}_1$을 핀셋으로 골라내는 스킬입니다.

Using some calculus, one can show that the minimizers are
놀랍게도 고등학교 미적분학의 힘을 약간만 빌려서 미분을 해버리면, 일일이 회귀선을 100만 번쯤 그려보지 않아도 단번에 오차 산맥의 제일 밑바닥 계곡(최소점)을 짚어내는 정답 값들이 다음과 같이 바로 도출된다는 것을 증명해 낼 수 있습니다.

$$
\begin{align*}
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x}
\end{align*} \quad (3.4)
$$

**FIGURE 3.1.** _For the_ `Advertising` _data, the least squares fit for the regression of_ `sales` _onto_ `TV` _is shown._
**그림 3.1.** `Advertising` 데이터 도화지 위에, `TV` 광고비 변수를 바탕으로 `sales(매출)`가 어떻게 뛰는지 가장 잘 보여주는 가장 완벽한 선(최소 제곱 적합 회귀선)이 파란색으로 쫙 그어져 있습니다.

_The fit is found by minimizing the residual sum of squares._
이 선은 바로 우리가 앞서 떠들었던, 오차들의 쓰레기통인 '잔차 제곱합(RSS)'이 가장 작아지는 바로 그 황금 비율의 위상(위치)을 찾아내어 그어진 것입니다.

_Each grey line segment represents a residual._
선에 매달린 수많은 짧은 회색 꼬챙이 선분들이 보이시나요? 저 것들이 바로 실제 수많은 동네의 매출 점들이 가장 완벽한 선에서 위아래로 얼마나 빗나갔는지를 사실 그대로 보여주는 잔차(오차)들입니다.

_In this case a linear fit captures the essence of the relationship, although it overestimates the trend in the left of the plot._
이 경우, 비록 그래프의 왼쪽 끝자락 바닥 부근에서는 허공의 직선이 실제 점들보다 살짝 붕 떠 있어 좀 긍정적으로 과대 예측하고 자빠져 있긴 하지만, 전반적으로는 두 데이터 간의 본질적인 단비례 친구관계를 아주 기가 막히게 포착해내고 있습니다.

where $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ and $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ are the sample means.
참고로 식 3.4의 무서워 보이는 저 수식에서 $\bar{y}$와 $\bar{x}$ (y바, x바)는 그냥 $y$값들의 평균과 $x$값들의 평균값을 나타내는 평범한 통계 기호입니다. 수식 기호에 전혀 쫄 필요 없습니다!

In other words, (3.4) defines the _least squares coefficient estimates_ for simple linear regression.
즉 다시 말하자면, 위의 (3.4) 수식 자체가 단순 선형 회귀라는 무기를 쓸 때 당신이 무조건 기계처럼 써먹어야 할 '_최소 제곱 계수 추정치_'를 도출해내는 '치트 퍼즐 공식'인 셈입니다.

Figure 3.1 displays the simple linear regression fit to the `Advertising` data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$.
그림 3.1의 `Advertising` 데이터에 완벽한 선을 계산해서 쫙 그어보니, 절편 끄트머리 수치인 $\hat{\beta}_0$는 7.03에 딱 찍혀 위치하고 기울기인 $\hat{\beta}_1$은 0.0475로 똑 부러지게 계산되어 나왔습니다.

In other words, according to this approximation, an additional $\$1,000$ spent on TV advertising is associated with selling approximately 47.5 additional units of the product.
이 무미건조한 수학 숫자를 사장님이 알아듣기 쉬운 현실 언어로 번역해 볼까요? 우리가 얻어낸 이 모델에 의하면, **TV 광고에 1,000달러(약 130만 원)치의 돈다발을 시장에 더 뿌릴 때마다, 창고에 쌓인 우리 물건은 무려 대략 47.5개씩 꼬박꼬박 추가로 날개 돋친 듯 팔려나가는 마법의 상승세 경향**을 가진다는 뜻입니다!

In Figure 3.2, we have computed RSS for a number of values of $\beta_0$ and $\beta_1$, using the advertising data with `sales` as the response and `TV` as the predictor.
그림 3.2에서, 우리는 `TV`(원인)와 `sales`(결과) 광고 데이터를 집어넣어, 수백 가지의 다양한 $\beta_0$와 $\beta_1$ 숫자 조합을 억지로 요리조리 쑤셔 넣어 보면서 최후의 오차 덩어리(RSS)가 어떻게 출렁출렁 변하는지 거대한 등고선 지도를 그려보았습니다.

In each plot, the red dot represents the pair of least squares estimates $(\hat{\beta}_0, \hat{\beta}_1)$ given by (3.4).
지도의 각 플롯 한가운데를 보면 시뻘건 점이 콕! 하나 제일 깊은 곳에 찍혀있죠? 저 점이 바로 아까 우리가 마법의 수식 (3.4)를 통해 똑 잘라 계산해낸, 수만 가지 기울기/절편 콤보 부대 중 단 하나의 완벽한 우승자 콤보 쌍입니다.

These values clearly minimize the RSS.
저 빨간 점 위치를 보시면 아시겠지만, 이 미분으로 찾은 값들이야말로 가장 푹 파인 밑바닥 계곡, 즉 오차 쓰레기통(RSS)을 무자비하게 쏙 들어가며 최소화시킨다는 것을 똑똑히 두 눈으로 확인할 수 있습니다.

[< 3.1 Simple Linear Regression](../trans2.html) | [3.1.2 Assessing the Accuracy of the Coefficient Estimates >](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html)

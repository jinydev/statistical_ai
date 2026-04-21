---
layout: default
title: "trans2"
---

[< 4.3 Logistic Regression](../trans2.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.1 The Logistic Model
# 4.3.1. 로지스틱 모형 (The Logistic Model)

How should we model the relationship between $p(X) = \text{Pr}(Y=1 \mid X)$ and $X$?
자, 그렇다면 도대체 우리는 $p(X) = \text{Pr}(Y=1 \mid X)$ 라는 기묘한 체납 확률 게이지와 내 지갑 잔고인 예측 변수 $X$ 사이의 관계를 어떻게 모형으로 빚어내야 할까요?

(For convenience we are using the generic 0/1 coding for the response.)
(편의를 위해 정답 타깃을 0과 1의 숫자로 코딩한다고 가정합시다. '파산'은 무서운 1, '정상'은 평화로운 0입니다.)

In Section 4.2 we considered using a linear regression model to represent these probabilities:
이미 지나온 4.2절에서 우리는 앞뒤 재지 않고 무식하게 직선을 긋는 선형 방정식(선형 회귀 모델)으로 다음과 같이 안일하게 이 확률들을 포장해 보려고 낑낑거리며 시도해 보았습니다:

$$
p(X) = \beta_0 + \beta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance`, then we obtain the model shown in the left-hand panel of Figure 4.2.
만약 이 순진한 직선 긋기 놀이를 통장 잔고(`balance`)를 사용해서 파산 범인(`default = Yes`)을 지목하고 예측하는 데 진짜 적용해버리면, 그림 4.2의 왼쪽 도화지에 펼쳐진 기괴한 일직선 그림이 튀어나옵니다.

Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1.
이 그림을 보면 선형 모델 방법의 참사가 어떤 꼴인지 여실히 드러납니다. 잔고가 바닥을 쳐 0에 가까워지면 무려 '-20%'라는 환장할 '음수' 차원의 파산 확률을 뱉어내고, 반대로 잔고 탑을 쌓은 빌게이츠 같은 사람을 검사하면 파산 확률이 무려 100%(1)를 가볍게 뚫고 하늘을 솟는 값을 도출해버립니다.

These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1.
이건 그야말로 미친 예측입니다. 자연의 섭리상 진짜 파산 확률은 잔고가 텅 비었건 산더미건 상관없이, 절대적으로 0(0%)과 1(100%)이라는 마지노선 캡슐 안에서만 놀아야만 하기 때문입니다.

This problem is not unique to the credit default data.
이 골치 아픈 직선 끄집어내기 버그 스릴러는 비단 이 신용카드 데이터셋에서만 유독 발생하는 게 아닙니다.

Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of $X$ and $p(X) > 1$ for others (unless the range of $X$ is limited).
애초에 정답이 태생부터 Yes와 No, 즉 0과 1인 대상에게 '일직선 막대기'를 강제로 끼워 맞추려 하는 그 어떤 시도를 할지라도, 수학의 원칙상 한쪽 끝자락 절벽 어딘가에서는 늘 0보다 작아지고(마이너스 확률), 다른 반대쪽 우주 끝 어딘가에서는 1보다 커져 돌파해버리는 치명적 부작용이 반드시 벌어집니다 (단서 $X$가 오직 특정 구간에만 박혀 갇혀있지 않은 한 말입니다).

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of $X$.
이 끔찍하고 거대한 산수 오류를 회피하려면, 우리는 무조건 $X$가 우주 저 끝에서 어떤 상상초월 숫자를 들고 오든, 늘 0과 1 사이에서만 안전하게 걸러져 출력값을 정제해 뱉게 하는 특수한 필터망 변위 같은 함수를 동원해 $p(X)$를 새롭게 설계해야 합니다.

Many functions meet this description.
수학계에는 놀랍게도 이 깐깐한 요구 조건 스펙을 만족시키는 착한 필터망 함수들이 꽤 많습니다.

In logistic regression, we use the _logistic function_,
그리고 바로 이곳, 대망의 로지스틱 회귀 세계관에서 우리는 바로 그 유명한 **로지스틱 함수(logistic function)** 를 채택해 주무기로 휘두릅니다:

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \quad (4.2)
$$

To fit the model (4.2), we use a method called _maximum likelihood_, which we discuss in the next section.
이 (4.2)라는 멋드러진 확률 곡선 스펙을 데이터에 맞게 쫙쫙 늘리고 구부려 찍어 누르기(피팅) 위해서, 우리는 바로 다음 섹션에서 집중 타격하고 배울 **최대 우도 기법(maximum likelihood, "어떤 놈이 이걸 가장 최고로 설명할까?"를 쫓아 찾는 비법)** 이라는 탐색 장비를 사용합니다.

The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the `Default` data.
그림 4.2의 오른쪽 도화지는 마침내 로지스틱 곡선이 어떻게 `Default` 파산 유저 데이터 점들을 부드럽게 감싸 안으며 완벽하게 피팅되었는지를 자랑스레 보여줍니다.

Notice that for low balances we now predict the probability of default as close to, but never below, zero.
수려한 스무딩에 감탄하십시오! 잔고가 바닥이어도 파산 확률은 0에 무한히 수렴하듯 착 붙어서 아슬아슬할지언정, **그 결코 0을 뚫고 지하실(음수)로 추락하지 않습니다.**

Likewise, for high balances we predict a default probability close to, but never above, one.
마찬가지의 자태로, 잔고가 무한정 치솟아도 파산 확률 궤적은 상한선 1 부근에 찰싹 달라붙을 뿐, 결단코 100% 한계 천장을 뚫고 우주 밖으로 폭발 상승하지 않습니다.

The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction.
로지스틱 함수는 영리하게도 항상 이 아름다운 **S자 모양(S-shaped)** 슬라이드 폭포를 기본자세로 치장하며 생성해 내기 때문에, 우리는 $X$ 값이 세상 어디에 떨어지는 돌연변이 수급자이건 간에 언제나 확률이라는 본연에 충실한 '상식적 예측' 결과표를 거머쥘 수 있습니다.

We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot.
더욱이 곡선의 유려함 덕에 왼편 도화지의 뻣뻣하고 우직한 선형 몽둥이질보다도, 체납자들이 몰려있는 분포의 농도 흐름 구간대를 훨씬 더 예리하게 캐치하고 포착(capture)해 낸다는 걸 엿볼 수 있습니다.

The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.
두 가지 비교 모델 승부 결과 경우 모두 훈련 데이터를 요약한 평균 예측 확률을 다 더해 구해보면 흥미롭게도 절반이 파산인 0.0333으로 결산되는데, 이는 놀랍게도 가상의 무작위 전체 인구 데이터 1만 명 속의 숨겨진 타깃 '연체자 비율' 자체 비율과 통계적으로 완전히 동일하게 안착합니다.

After a bit of manipulation of (4.2), we find that
수학자들의 장난기를 발동하여, 위에서 봤던 강력한 (4.2)번 수식을 살짝 이리저리 비틀고 당겨(manipulation) 조작해 보면, 우리는 다음과 같은 신박한 변환 공식을 찾아냅니다:

$$
\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X} \quad (4.3)
$$

The quantity $p(X) / [1 - p(X)]$ is called the _odds_, and can take on any value between 0 and $\infty$.
여기 좌측에 탄생한 이 기괴한 분수 계산 덩어리 $p(X) / [1 - p(X)]$ 가락은, 통계학에서 베팅에 미친 사람들의 지표 **오즈(odds, 승산비)** 라고 명명되며, 확률의 족쇄인 $[0, 1]$ 캡을 깨부수고 단숨에 0부터 무한대($\infty$) 사막까지 우주 모든 숫자를 자유롭게 취할 수 있는 기염을 토합니다.

Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively.
오즈 값이 작디작은 0에 수렴한다는 것과 무한대로 뻗어간다는 것은, 각각 체납에 휘말릴 확률이 가망이 없을 만큼 거의 0이거나 반대로 반드시 터질 만큼 1에 무한히 가깝다는 것을 정확히 환산 지칭합니다.

For example, on average 1 in 5 people with an odds of $1/4$ will default, since $p(X) = 0.2$ implies an odds of $0.2 / (1 - 0.2) = 1/4$.
예를 들어 볼까요? 만약 한 그룹의 '오즈(Odds)'가 $1/4$(즉 0.25)인 팟이라면, 산술적으로 이 다섯 사람 중 평균적으로 1명이 파산으로 나락을 갑니다. 거꾸로 추적해 보면 확률 $p(X) = 0.2$(20%)는 앞서 계산 식 $0.2 / 0.8 = 1/4$ 로 정확히 똑 떨어지는 비율 승산을 의미하기 때문입니다.

Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X) = 0.9$ implies an odds of $0.9 / (1 - 0.9) = 9$.
같은 원리로 만약 오즈 숫자가 무려 '9'가 뜬다면, 이는 곧장 무시무시한 뜻입니다. 대략 10명이 줄 서 있다면 그중 9명이 와그르르 체납 대란에 직면하게 되는데, 이는 확률 기준에서 볼 때 $p(X) = 0.9$ (90%)가 오즈 $0.9 / 0.1 = 9$ 를 역으로 의미하기 때문입니다.

Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.
이러한 이유로 오즈 체계 지수 표기법은 직관적으로 인간의 도박적 감각("저 말이 우승할 배당이 얼마다")과 돈을 거는 올바른 배팅 전략과 훨씬 자연스럽게 맞아떨어지기 때문에, 전통적으로 경마판과 도박 세계에서 딱딱한 확률(%) 대신 오랜 시간 사랑받으며 애용되어 왔습니다!

By taking the logarithm of both sides of (4.3), we arrive at
이제 저 (4.3)번 놀라운 오즈 수식의 양쪽 끝에 자연로그($\log$) 마법을 씌워버리는 타격을 가하면, 우리는 다음과 같은 궁극의 직선 방정식에 도달하여 마주합니다:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_.
식 가장 왼쪽에 처단된 저 기괴한 로그 모양 덩어리 지표는, 영광스럽게도 **로그 오즈(log odds)** 혹은 줄여 말해 **로짓(logit)** 이라고 칭송받는 존재가 됩니다.

We see that the logistic regression model (4.2) has a logit that is linear in $X$.
도화지를 보세요! 결국 그토록 구불거리던 S 곡선의 로지스틱 회귀 모델(4.2)조차도, 로그라는 마법으로 치환 변환되어 로짓 공간으로 넘어오면, 숨겨두었던 뼛속 뼈대인 $X$에 대해 완벽하게 평면 직선의 **선형성(linear)** 을 시원하게 띠고 있다는 속내를 확인할 수 있습니다.

Recall from Chapter 3 that in a linear regression model, $\beta_1$ gives the average change in $Y$ associated with a one-unit increase in $X$.
기억의 서랍을 열어 3장 단순 선형 회귀 모형의 영광을 되짚어 보십시오. 거기선 기울기 $\beta_1$이 단호하게 "$X$가 평화롭게 1 단위 증가할 때마다 진짜 돈 $Y$의 타깃값이 평균적으로 정확히 똑같이 $\beta_1$만큼 정직하게 바뀐다!"라는 것을 통지했었습니다.

By contrast, in a logistic regression model, increasing $X$ by one unit changes the log odds by $\beta_1$ (4.4).
반대로(By contrast), 이 뒤틀린 로지스틱 회귀 요원의 모형 판도에서는, $X$ 단서가 1칸 오를 때마다 당신이 맞혀야 할 $Y$ (파산할 확률값 \%)가 오르는 게 결코 절대 아닙니다! 오직 변환계의 수치인 저놈의 **로그 오즈(log odds) 덩어리 지표 치수만이 $\beta_1$ 만큼 점프하며 변화한다**는 무시무시한 사실만을 보장해 줍니다 (4.4번 로짓 식).

Equivalently, it multiplies the odds by $e^{\beta_1}$ (4.3).
동일한 논리 회로로 수리적으로 해독하면, 원래 도박꾼의 승산 오즈(Odds) 원본 값에는 바로 $e^{\beta_1}$ 수치 배팅이 배수로 곱해져 가중 증폭된다(multiplies)는 뜻과 상통합니다 (4.3번 식).

However, because the relationship between $p(X)$ and $X$ in (4.2) is not a straight line, $\beta_1$ does _not_ correspond to the change in $p(X)$ associated with a one-unit increase in $X$.
그러나 치명적 유의사항! 우리는 가장 최초에 진짜 $p(X)$ 확률과 우리의 $X$가 만나는 (4.2)의 원본 그림선 자체가 결코 뻣뻣한 일직선(straight line)이 아니라 유연한 S자 곡선임을 안고 출발했기에, $\beta_1$ 이라는 상수가 무참히 $X$의 1단위 증가에 따른 수치 $p(X)$ 의 다이렉트 상승 스텝 폭 크기 변화량에 부드럽게 결코 부합 혹은 다이렉트 변환 매칭 대응하지 **않는다는 점**을 각인해야 합니다.

The amount that $p(X)$ changes due to a one-unit change in $X$ depends on the current value of $X$.
내가 예측 변수 단서 $X$를 단 1스텝 올렸을 때, 내 타깃이 파산에 직면해 $p(X)$ 확률이 튀어 오르는 실제 상승률 체감 진폭 타격감은, "내가 지금 현재 $X$의 어느 위치(잔고 바닥인지 초호화 부자인지)에 발 딛고 서 있는가" S자 절벽의 현재 가파름 경사 좌표도(현재값)에 송두리째 전적으로 종속되어 얽혀 의존하게 됩니다.

But regardless of the value of $X$, if $\beta_1$ is positive then increasing $X$ will be associated with increasing $p(X)$, and if $\beta_1$ is negative then increasing $X$ will be associated with decreasing $p(X)$.
하지만 만성 복잡함을 걷어내면 한 가지 불변의 진리는 승리합니다. 그가 선 $X$ 좌표가 어찌 되었든 평지이건 경사이건 간에, 만약 산출된 방향키 $\beta_1$ 이 + 의 양수를 머금었다면 $X$가 늘어나는 것은 죽이 되건 밥이 되건 $p(X)$ 의 영원한 **상승 행위 무빙**과 결사코 연관되며 단정 지어지고, $\beta_1$ 이 마이너스 음수를 띤다면 $X$의 성장은 곧장 파산 확률의 뚜렷한 **하강 곡선 흐름** 기조와 지독하게 맞물려 무조건 연결되어 끌어당기어지게 됩니다.

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.3 Logistic Regression](../trans2.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans2.html)

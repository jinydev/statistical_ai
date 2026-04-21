---
layout: default
title: "trans2"
---

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans2.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.2 Poisson Regression on the Bikeshare Data
# 4.6.2 본 게임 시작! 자전거 대여 카운트 데이터 전용 무기, 특수 '포아송 회귀' 출격!

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_.
자, 앞선 전투에서 `Bikeshare` 카운트 데이터를 잡으려다 처참히 박살 난 선형 회귀 몽둥이의 부적절함(inadequacies)과 초라한 실패를 극복하기 위해, 우리는 마침내 창고에서 진정한 전용 분쇄 병기, 제3의 대안 모델인 **포아송 회귀(Poisson regression) 소총**을 꺼내 들 것입니다!

Before we can talk about Poisson regression, we must first introduce the _Poisson distribution_.
그런데 이 거대한 포아송 무기를 다루기 이전에, 이 총알의 화약이 되는 기초 확률 법칙, **포아송 분포(Poisson distribution) 규칙**부터 먼저 살짝 맛보고 넘어가야 합니다.

Suppose that a random variable $Y$ takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \dots\}$.
상상해 보세요. 우리가 예측해야 할 타깃 $Y$ 가 마이너스로 절대 떨어지지 않고, 소수점도 없는 깔끔하고 순수한 양의 정수들, 즉 $Y \in \{0, 1, 2, \dots\}$ 처럼 사람 머릿수나 주사위 눈금 같은 고정 카운트 값을 갖는다고 해봅시다.

If $Y$ follows the Poisson distribution, then
만약 이 $Y$ 타깃이 '포아송 가문'의 혈통(분포)을 물려받아 법칙을 따른다면, 이 총알이 과녁에 맞을 확률은 다음과 같은 기막힌 수학 공식으로 딱 떨어집니다:

$$
\text{Pr}(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \quad (4.35)
$$

Here, $\lambda > 0$ is the expected value of $Y$, i.e. $E(Y)$.
여기서 식 한가운데 박혀있는 뚱뚱한 기호 $\lambda > 0$ 은 $Y$ 과녁에 맞을 거라 예상되는 짐작 치수, 즉 기댓값(평균) $E(Y)$ 를 나타냅니다.

It turns out that $\lambda$ also equals the variance of $Y$, i.e. $\lambda = E(Y) = \text{Var}(Y)$.
그런데 포아송 가문만의 소름 돋는 출생의 비밀이 하나 있습니다. 세상에, 이 $\lambda$ 기댓값(평균)이라는 놈이, 데이터가 요동치는 파도인 분산(variance) 크기와 토씨 하나 안 틀리고 똑같다는 기적의 공식, $\lambda = E(Y) = \text{Var}(Y)$ 법칙이 성립한다는 겁니다!

This means that if $Y$ follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance.
이게 도대체 무슨 말이냐고요? 선형 회귀에선 널뛰기 발작이라며 욕먹었던 그 문제 현상이, 포아송 가문에서는 "타깃의 평균치가 커지면 분산(파동)도 당연히 커진다!"라는 아주 지극히 정상적인 집안 내력(룰)으로 얌전히 통제되고 품어진다는 뜻입니다!

The Poisson distribution is typically used to model _counts_; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values.
그래서 통계학자들은 "개수, 횟수(counts)"를 셀 때 무조건 이 **포아송 분포** 총알을 약실에 장작 합니다. 사람 수나 교통사고 건수처럼 소수점이 없는 양수들의 카운트는 이 포아송 가문의 특성과 아주 기가 막히게 아귀가 물려 돌아가는 천생연분 찰떡궁합이거든요!

Rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like $\lambda = 5$, we would like to allow the mean to vary as a function of the covariates.
자, 그런데 자전거 대여량 $Y$ 횟수를 그냥 "음, 평균 $\lambda = 5$명쯤 되겠지?" 하고 고정된 단일 타깃으로 때려 맞추는 건 너무 시시합니다. 우리는 앞서 긁어모은 날씨, 시간(공변량) 무기 힌트들을 팍팍 섞어서 이 $\lambda$ 평균값이 다이나믹하게 변동하는 스마트 유도탄 함수를 만들고 싶습니다.

In particular, we consider the following model for the mean $\lambda = E(Y)$:
그래서 우리는 평균 타점 $\lambda = E(Y)$ 에다가 요상하고 기막힌 다음의 공식을 설계해 심어둡니다:

$$
\lambda(X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.36)
$$

or equivalently
이 기괴한 식을 우리가 알아보기 쉽게 살짝 비틀어 로그를 씌워 환산하면(equivalently), 익숙한 모양새가 나옵니다:

$$
\log(\lambda(X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.37)
$$

Here, $\beta_0, \beta_1, \dots, \beta_p$ are parameters to be estimated.
여기서 $\beta$ 부품들은 우리가 나중에 사격 현장에서 영점을 맞춰 찾아내야 할 과녁 조준 계수 세팅값들입니다.

Together, (4.35) and (4.36) define the Poisson regression model.
방금 본 기본 확률 모형 (4.35) 와 지수 함수 마취제 (4.36) 이 두 가지 비기 콤보가 합쳐져서 비로소 완전체 대량 학살 병기 **포아송 회귀 모델**이 탄생합니다.

Notice that in (4.36), we take the _log_ of $\lambda(X_1, \dots, X_p)$ to be linear in $X_1, \dots, X_p$; this ensures that $\lambda(X_1, \dots, X_p)$ takes on nonnegative values for all values of the covariates.
눈치채셨나요? (4.36) 식에서 타깃 $\lambda$ 에 **지수 방패($e$)** 를 씌워 올려버린 저 절묘한 계산 설계 덕에, 우리가 무슨 악질 공변량 변수 $X$ 값을 쑤셔 넣든 간에 반환되는 예측 결괏값 $\lambda$ 는 모조리 0을 포함해 영원히 마이너스를 칠 수 없는 완전한 양수 구역에 결박됩니다! 아까 선형 회귀 통나무를 부러뜨렸던 **1번 오류(마이너스 유령 좀비 출몰)** 가 완벽하고 기품 있게 차단된 겁니다!

To estimate the coefficients $\beta_0, \beta_1, \dots, \beta_p$, we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2.
저 조준 부품 $\beta$ 계수들을 세팅 튜닝하기 위해, 우리는 앞서 로지스틱 회귀가 써먹었던 그 무식하지만 확실한 실전 생존 탐색술인 **최대 우도 접근법(maximum likelihood approach)** 스캐너 장치를 똑같이 이식해 투입합니다.

We estimate the coefficients that make the observed data as likely as possible.
우리는 현지에 떨어진 데이터 관측 팩트 상황에서 타격 적중률을 가장 정점까지 치솟게 만들어 줄 그 마법의 눈치 계수들만을 쏙쏙 골라 뽑아냅니다.

We now fit a Poisson regression model to the `Bikeshare` data set.
설명은 끝났습니다. 이제 이 거대한 포아송 회귀 전차를 `Bikeshare` 늪지대 전장에 투입시켜 쏴 봅시다!

Qualitatively, the results are similar to those from linear regression in Section 4.6.1.
일단 전장의 파악 시야 지표(정성적 흐름) 결괏값 상황판은 놀랍게도 과거 고장 났던 구닥다리 선형 무기(4.6.1)가 대충 때려 맞췄던 큰 실루엣 흐름과 아주 비슷하게 도출됩니다.

We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours.
우리는 다시 한번 "자전거 렌탈 폭주량은 봄, 가을, 출퇴근 시간에 가장 치솟고, 얼어 죽을 겨울이나 사람 없는 꼭두새벽엔 바닥을 찍는다"라는 이 직관적 현상 진리를 아주 뚜렷하게 오목조목 훑어 재확인합니다.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:
하지만 겉모습만 비슷할 뿐, 뼈가 부러진 깡통 선형 회귀와 최첨단 카운트 킬러 무기인 우리의 포아송 회귀 전차 사이에는 차원이 다른 **3가지 스펙상 차이점(distinctions)** 이 떡하니 존재합니다:

- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_j$ by one unit is associated with a change in $E(Y) = \lambda$ by a factor of $\exp(\beta_j)$. For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp(-0.08) = 0.923$, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear.
- **차이 01. 로그 번역기 장착 (해석이 다르다!):** 포아송 기판의 스코어 계수(부품)들을 해석할 땐 멘탈 주의가 필요합니다. 무턱대고 더하기만 하던 통나무와는 다르게 (4.37) 룰을 꼼꼼히 따라야 하는데요! 변수 하나 $X_j$ 가 오를 때마다 타깃 기댓값 $\lambda$ 는 단순히 수치가 덧붙는 게 아니라, 살벌하게도 $\exp(\beta_j)$ 이라는 거대한 지수 배율의 배수 팩터(factor) 곱셈 스케일만큼 출렁! 하고 증폭 변동됩니다! 예컨대 날씨가 맑음(Clear)에서 구름 낌(Cloudy)으로 막 1칸 나빠지면, 통나무에선 (-12명 깎이네) 식으로 단순 계산됐지만 여기선 그 변동 배율 타격이 $\exp(-0.08) = 0.923$ 으로 세팅됩니다. 이 말은 구름이 끼면 하늘 맑을 때 대비 대략 '92.3%' 만의 안타까운 생존율 덩어리 인원수만이 자전거를 탄다는 기막힌 거시적 배분 비율 타격 개념으로 계산된다는 거죠.

- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, $\lambda = E(Y) = \text{Var}(Y)$. Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.
- **차이 02. 발작 억제 시스템 (평균-분산 관계 핸들링):** 아까 포아송 집안 내력이 $\lambda = E(Y) = \text{Var}(Y)$ 법칙이라고 한 거 기억나시죠? 선형 회귀에선 평균이 커질 때 분산 눈금이 널뛰기 발작(이분산성)을 한다고 멘붕이 왔지만 여긴 절망할 필요가 싹 없어졌습니다! 자전거 이용량을 세는 포아송 회귀 입장에선 저 무시무시한 널뛰기 오차파동 현상 자체가 예측의 일상이자 순탄한 제어 법칙 시스템이거든요! 즉 기계 자체가 "응, 사람 몰려서 대여 평균 수가 폭발하면, 오차 분산 폭(잡음)도 같이 커지는 게 지극히 정상인 거야~" 라며 노이즈 변동 폭발을 기본 탑재 종속 스킬로 묶어 품어버리면서, 앞서 선형 통나무를 부수던 2번 결함인 `Bikeshare` 카운트 바닥의 더러운 '평균과 분산의 널뛰기 난동' 늪을 아주 기가 막히고 자연스럽게 스무스하게 밟아 컨트롤해 나갑니다. 무적이죠!

- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values.
- **차이 03. 유령 좀비 영구 퇴치 백신 (음수 예측 원천 차단 장벽):** 대망의 최고의 마스터피스! 포아송 무기를 세팅해 방아쇠를 쏘면 앞서 구형 통나무가 오작동 내뿜던 그 미친 "마이너스 -5명이 자전거를 타요!" 같은 음수 예측 결과 오류 결함이 100% 영구적으로 소멸 차단 방어막 처결 됩니다. 왜냐하면 애초에 포아송 총알의 뼈대 코어 심장 파츠 자체가 수학적으로 **오직 0을 포함한 순수 양수값 결괏값만 허용 압축 방출**하는 강력한 양수 강제 필터 성역 엔진 규약을 갖추고 태어났기 때문입니다. 완벽합니다!

---

## Sub-Chapters

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans2.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans2.html)

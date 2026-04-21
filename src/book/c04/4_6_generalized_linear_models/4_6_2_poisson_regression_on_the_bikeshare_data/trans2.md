---
layout: default
title: "trans2"
---

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans2.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.2 Poisson Regression on the Bikeshare Data
# 4.6.2 본 게임 시작! 자전거 대여 카운트 데이터 전용 사냥꾼, 특수 '포아송 회귀' 출격!

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_. Before we can talk about Poisson regression, we must first introduce the _Poisson distribution_.
선형 회귀의 멍청하고 무식한 몽둥이질이 저 기괴한 `Bikeshare` 갯수 카운트 데이터 바닥에서 얼마나 처참히 헛발질하며 붕괴하는지 우리의 두 눈으로 똑똑히 목격했습니다. 이 최악의 결함(inadequacies)을 박살 내고 극복해 내기 위해, 우리는 드디어 이 세계관에 딱 들어맞는 완벽한 맞춤형 저격수, 이른바 **_포아송 회귀(Poisson regression)_** 라는 특수 무기를 현장에 투입할 것입니다. 하지만 이 녀석의 파괴력을 진짜 이해하려면, 일단 먼저 그 녀석의 뼛속 엔진인 **_포아송 분포(Poisson distribution)_** 라는 수학적 우주의 태생 신비부터 까발리고 넘어가야 합니다.

Suppose that a random variable $Y$ takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \dots\}$. If $Y$ follows the Poisson distribution, then
당장 눈감고 상상해 보십시오. 만약 우리의 타깃 목표 확률 변수 $Y$ 가 무조건 자를 수 없는 인간 머릿수처럼 마이너스가 될 수 없는 **양의 정수 덩어리** 값만 통통 취한다고 치자 이겁니다. (즉 $Y \in \{0, 1, 2, \dots\}$). 만약 이 징그러운 $Y$ 녀석이 포아송 분포라는 마법의 성 궤도를 졸졸 따른다고 선언한다면, 그 즉시 다음 공식이 터집니다:

$$
\text{Pr}(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \quad (4.35)
$$

Here, $\lambda > 0$ is the expected value of $Y$, i.e. $E(Y)$. It turns out that $\lambda$ also equals the variance of $Y$, i.e. $\lambda = E(Y) = \text{Var}(Y)$. This means that if $Y$ follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance.
눈 돌아가는 여기서 저 $\lambda$ 기둥 녀석은 무조건 0보다 커야 하며 ($\lambda > 0$), 그 정체는 바로 그 타깃 $Y$ 놈이 모여서 만드는 **최종 평균 기대치(expected value)** $E(Y)$ 덩어리입니다. 그런데 이게 정말 미치고 환장할 역대급 반전 묘미가 터집니다! 이 신비로운 $\lambda$ 점수는 세상에나 마상에나 자신이 곧 평균이면서, 동시에 놀랍게도 그 $Y$ 집단의 널뛰는 요동 오차폭인 **분산(Variance)** 값 조차 완벽하게 100% 동일하게 일치시켜 집어삼켜 버립니다! 즉 $\lambda = E(Y) = \text{Var}(Y)$ 라는 진리죠. 이 미친 일치 현상은 우리에게 뭘 강력히 경고하느냐? "만일 그 집단이 고귀한 포아송 분포의 헌법을 따르고 있다면, 평균 대가리 숫자가 무지막지하게 비대칭 커지면 커질수록, 그 녀석 주변을 소용돌이치는 에러 분산 널뛰기 진동 폭발 스케일 역시 똑같은 체급 비율로 미친 듯이 커진다!" 는 소름 돋는 절대 법칙을 의미합니다. 아까 낡은 선형 회귀가 파괴됐던 '이분산성' 문제를 아예 이 모델은 태생부터 법으로 안고 가버리는 겁니다!

The Poisson distribution is typically used to model _counts_; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values. Rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like $\lambda = 5$, we would 공allow the mean to vary as a function of the covariates. In particular, we consider the following model for the mean $\lambda = E(Y)$:
고로 이 전능하신 포아송 분포 법칙은 통계판 일반 야생에서 툭하면 사람 머릿수나 사고 건수 같은 **_개수(counts)_** 파편들을 스케치하고 조망할 때 전가의 보도처럼 가장 흔히 쓰이는 제1원칙 모델입니다. 그 이유인즉슨, 우리가 구하고자 하는 목표인 인간 카운트 쪼가리들이 포아송의 본성처럼 죽었다 깨어나도 절대 음수가 못 되는 단단한 양의 정숫값 형태와 미치도록 똑같이 기막히게 맞아떨어지기 때문이죠 (자연스러운 찰떡궁합 선택). 하지만 우리는 여기서 멈추지 않습니다! 단순히 `bikers` 대여 손님 수 $Y$ 를 그저 "음, 평균 $\lambda = 5$ 쯤 맴돌겠지" 처럼 박제된 멍청한 박제 포아송 고정치로 단정 짓고 노는 찌질한 짓은 안 할 겁니다. 우린 그 평균값 $\lambda$ 자체가 날씨, 시간 등 공변량 힌트 무기 스펙들이 바뀔 때마다 아주 유연하고 화려하게 살아서 오르락내리락 춤추며 변동하도록 자유를 허락할 겁니다. 이를 성취하기 위해, 우리는 그 평균 덩어리 $\lambda = E(Y)$ 에 대한 통제 방식을 다음과 같이 어마무시한 수식으로 진화 세팅합니다:

$$
\lambda(X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.36)
$$

or equivalently
(혹은 이놈을 살짝 비틀어 로그 지붕 위로 올리면 완전히 동일하게 다음과 같은 식도 됩니다)

$$
\log(\lambda(X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.37)
$$

Here, $\beta_0, \beta_1, \dots, \beta_p$ are parameters to be estimated. Together, (4.35) and (4.36) define the Poisson regression model. Notice that in (4.36), we take the _log_ of $\lambda(X_1, \dots, X_p)$ to be linear in $X_1, \dots, X_p$; this ensures that $\lambda(X_1, \dots, X_p)$ takes on nonnegative values for all values of the covariates.
자 이 수식판 위에서 $\beta_0, \beta_1, \dots, \beta_p$ 는 우리가 훈련 노가다 피를 말리며 어찌어찌 역추적 추정해 내야 할 핵심 모터 변수 파라미터 계수들입니다. 저 태초의 (4.35) 포아송 공식과 방금 등장한 (4.36) 지수 펌프 부품이 찬란하게 하나로 융합 결합 합체 되는 순간! 그것이 비로소 우주 최강 카운터 헌터, **포아송 회귀 모델(Poisson Regression Model) 기동의 통일 완성**을 정의합니다. (4.36)에서 아주 간교하고도 치밀한 수학적 수작을 하나 걸어둔 걸 똑똑히 주목해 보십시오. 우린 $\lambda$ 함수에 냅다 **_로그(log)_** 폭탄 마법을 취해 버려서 예측 변수 $X_1, \dots, X_p$ 들이 그저 단순한 직선 형태(linear) 로 쭉 이어지게 만들었습니다. 이 미친 조치의 덕분은 상상 초월입니다! 힌트 공변량 수치가 아무리 시궁창 마이너스 나락으로 요동치더라도, 지수로 감싼 저 $\lambda$ 결과값만큼은 절대 마이너스 죽음의 늪으로 폭락 계산되지 않는 **'강제 무적 양수 값 방어막'** 을 모든 환경에서 완벽 단단하게 보장받게 되는 기적의 잠금장치 설계입니다!

To estimate the coefficients $\beta_0, \beta_1, \dots, \beta_p$, we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2. We estimate the coefficients that make the observed data as likely as possible.
그럼 이제 핵심 심장 파츠인 저 계수 $\beta_0, \dots, \beta_p$ 를 어떻게 추정 획득할까요? 너무 긴장할 것 없습니다. 우리가 저 멀리 4.3.2 세션 로지스틱 회귀 전투 때 이미 마르고 닳도록 써먹었던 그 유명한 승리 치트키 전술, **'최대 우도 접근법(maximum likelihood approach 최대로 그럴싸한 로또 확률 찾기)'** 방식을 여기에도 그대로 복붙해 빙의 채용합니다. 지금 손에 쥔 우리가 관측한 오리지널 데이터 눈앞의 현실이 "가장 그럴싸하게 우연히 발생했을 법한" 가장 확률이 극한으로 터지는 로또 지점의 최적화된 계수 숫자 덩이들만을 컴퓨터 노가다로 조준해 역추적 추산 탈취하는 방식이죠.

We now fit a Poisson regression model to the `Bikeshare` data set. Qualitatively, the results are similar to those from linear regression in Section 4.6.1. We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours.
드디어 이 무적 전차 포아송 회귀 모델을 그 기괴한 `Bikeshare` 카운트 데이터 더미에 풀 가동 적중 피팅 시켰습니다! 정성적인 직관 시야로 슬쩍 감상해 보면 돌출된 아웃풋 해석 자체는 아까 앞 절 4.6.1에서 봤던 구닥다리 선형 회귀 몽둥이가 뱉던 정서적 냄새 결과와는 거의 비슷하게 잘 떨어집니다. 이번에도 우리는 어김없이, 따스한 봄/가을과 직장러 출근 지옥 시간에 자전거 러시가 가장 최고조 화력을 터뜨리고, 얼어붙은 겨울과 꼭두새벽 귀신 시간대에 사늘하게 꼴아박는다는 걸 재차 깨끗이 감상 검증 진단해 냅니다.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:
하지만 겉보기가 비슷할 뿐 뼛속은 다릅니다! 이 위대한 포아송 회귀 모델이 저 낡아빠진 선형 회귀 폐급 몽둥이와 격을 달리하며 확연히 다른 결정적이고 치명적인 위상 차이점 스탯 기조를 극명하게 아래와 같이 까발려 나열합니다:

- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_j$ by one unit is associated with a change in $E(Y) = \lambda$ by a factor of $\exp(\beta_j)$. For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp(-0.08) = 0.923$, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear.
- **_해석의 차원 축 변이(Interpretation):_** 포아송 모델이 뱉어낸 계수를 인간 언어로 해석 통찰하려면, 저 기이한 로그 조립판 (4.37) 공식을 두 눈 부릅뜨고 매섭게 세심하게 째려봐야 합니다! 이 공식이 포효하는 뜻은: 힌트 변수 $X_j$ 가 달랑 1단위 한 마디 증가 도약 발사할 때마다 타깃 평균치 $E(Y) = \lambda$ 의 운명 덩어리는 이전의 낡은 방식처럼 단순 더하기 스텝이 아니라! 무려 거대한 **곱셈 배수 폭발 인자(factor) 인 $\exp(\beta_j)$ 비율 수위만큼 뻥튀기 펌프질 증폭 곱셈 변화** 한다는 소름 돋는 선언입니다. 예컨대 맑은 하늘이 잿빛 흐린 구름천지로 돌변할 때, 자전거 평균 사용량 스탯이 받는 충격은 선형 공식처럼 "-몇 명" 빼기 타격이 아니라, 지수 폭발 계수인 $\exp(-0.08)$ 즉 **0.923 이라는 곱셈 인수율 변이**와 강렬 구속 연관 타격을 갖습니다. 다시 말해 현실 타격 지표상 하늘이 흐려지는 구름 먹구름 상황에선, 평일 맑을 때 군중 쪽수 대비 **'오직 딱 92.3% 인원수의 비율'** 덩어리만큼 줄어든 사람들만이 페달을 밟게 된다는 정교하고 기가 막힌 비율 척도 해석 도출을 가능케 합니다.
- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, $\lambda = E(Y) = \text{Var}(Y)$. Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.
- **_평균과 분산의 피의 서약 관계(Mean-variance relationship):_** 앞서 전율하며 예고했듯, 이 무시무시한 포아송 법칙 통치 체제법 하에서는 **$\lambda = E(Y) = \text{Var}(Y)$** 라는 무적 일체 원리가 작동 진리입니다. 고로 이 자전거 군단 대여 사용량 $Y$ 덩어리를 포아송 회귀로 모델링해 구속해 버렸다는 행위 자체는, 우리가 "특정 시간대 방의 자전거 평균 머릿수가 미친 듯 불어나 커지면 커질수록 그 시간에 널뛰는 분산 요동 에러 진동 폭발 파동마저도 똑같이 거대해진다!" 고 대놓고 암묵적 억지 기조 가정을 동의 인준해 깔아둔 것입니다. 그러므로, 옛날 뻣뻣한 선형 회귀 따위는 분산이 고무줄처럼 변하는 상황에 멘붕 와서 손도 못 대고 깨져 박살났던 `Bikeshare` 데이터판 특유의 **골치 아픈 '이분산성' 평균-분산 연동 결탁 널뛰기 문제**를, 이 포아송 괴물은 숨 쉬듯 자연스럽고 완벽하게 포용 통제 제어해 극복 핸들링(handle) 처치해 버리는 기막힌 유연성을 자랑합니다!
- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values.
- **_마이너스 죽음의 계곡 완벽 방어 차단선 (nonnegative fitted values):_** 이 절대 병기 포아송 회귀 모델을 구동하면 아재들 선형 모델 때처럼 "-3명 탑승" 같은 헛소리 마이너스 음수 예측 결함 따윈 영원토록 0.001% 도 절대 존재 출현 나발 발생하지조차 않습니다. 왜냐고요? 이 자랑스러운 포아송 뼛속 엔진 자체가 수학 태생적으로 오직 0 이상 양의 숨결 수치만을 호흡 흡수 허용하도록 고안 잠금된 천상의 카운트 성역이기 때문입니다! 완벽 방패!

---

## Sub-Chapters

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans2.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans2.html)

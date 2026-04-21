---
layout: default
title: "trans2"
---

[< 4.6 Generalized Linear Models](../index.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.1 Linear Regression on the Bikeshare Data
# 4.6.1 자전거 대여 데이터 패기에 잘못 들이댄 선형 회귀 몽둥이질

To begin, we consider predicting `bikers` using linear regression. The results are shown in Table 4.10.
본격적인 대결을 시작하기에 앞서, 우리가 가장 만만하게 써먹던 클래식 무기인 3장의 '선형 회귀 통나무'를 들고 저 무시무시한 카운트 변수 `bikers` 타깃을 때려잡아 보려 했습니다. 그 야심 찬(?) 예측 결과는 표 4.10에 고스란히 찍혀 있습니다.

We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour.
결과표를 슬쩍 살펴보면 제법 수긍이 갑니다. 예를 들어, 날씨가 기분 좋은 맑음에서 우중충한 흐림으로 꿀꿀해지면 자전거 이용자가 시간당 평균 12.89명이 훅 빠집니다; 게다가 날씨가 미쳐 날뛰어서 비나 눈이 쏟아지는 악천후로 악화되면, 무려 53.60명이나 되는 이용자가 추가로 자취를 감춘다고 합니다.

We see that bike usage is highest in the spring and fall, and lowest during the winter months.
또한, 이 통나무 기계는 "자전거는 날 선선하고 벚꽃, 단풍 날리는 봄과 가을에 가장 폭발적으로 많이 타고, 뼈가 시리게 추운 척박한 겨울엔 아무도 안 탄다!" 라는 당연한 상식을 아주 잘 잡아냈습니다.

Furthermore, bike usage is greatest around rush hour (9 AM and 6 PM), and lowest overnight.
뿐만 아니라, "직장인들이 지옥철을 피해 따릉이를 미친 듯이 밟는 아침 9시와 저녁 6시 러시아워에 렌탈 머릿수가 가장 폭발하고, 모두가 자는 야간 철야 시간엔 0명에 가깝게 제일 낮다"라는 통계적 직관도 퍼펙트하게 도출해 냈죠.

Thus, at first glance, fitting a linear regression model to the `Bikeshare` data set seems to provide reasonable and intuitive results.
따라서, 이 겉보기 수치들만 쓱 훑어보면(at first glance), 이 까다로운 `Bikeshare` 데이터판에다가 구식 직선 몽둥이(선형 회귀 모델)를 휘두르는 방식이 꽤 이치에 합당해(reasonable) 보이고, 척 보기에도 아주 합리적이고 직관적인(intuitive) 정답을 내놓는 것처럼 완벽한 환상에 빠지게 만듭니다.

But upon more careful inspection, some issues become apparent.
**하지만!** 우리가 이 몽둥이의 결과값을 현미경으로 쪼개서 아주 지독하게 탈탈 털어 검사(inspection) 해보는 순간, 가려져 있던 끔찍하고 치명적인 뼈대 결함 3가지가 그 추악한 민낯을 적나라하게 드러냅니다. 자, 선형 회귀가 카운트 데이터 앞에서 왜 망가지는지 그 3대 참거짓 오류를 까발려 보죠.

For example, 9.6% of the fitted values in the `Bikeshare` data set are negative: that is, the linear regression model predicts a _negative_ number of users during 9.6% of the hours in the data set.
**첫째, 좀비 인간의 등장 (음수 예측의 대참사)!** 
놀랍게도 표에 찍힌 적합된 점수 결과값의 무려 9.6%가 마이너스(음수)를 뚫고 지하로 내려갔습니다. 즉, 전체 시간 중 9.6%라는 구간 속에서 이 미친 선형 모델 기계는 "이번 시간엔 유령 좀비 -5명(negative)이 자전거를 빌려 탈 예정입니다!" 라고 귀신 씻나락 까먹는 소리를 예측 오류로 내뿜고 있다는 겁니다. 사람이 어떻게 음수가 됩니까?!

This calls into question our ability to perform meaningful predictions on the data, and it also raises concerns about the accuracy of the coefficient estimates, confidence intervals, and other outputs of the regression model.
이런 끔찍한 음수 좀비 예측 오류는 방금 전까지 이 기계를 믿었던 우리의 뒤통수를 거세게 후려치며 매우 심각한 불신(calls into question)을 낳습니다. 이건 당장 유의미한 예측 능력을 완전히 상실한 깡통 기계라는 의심을 촉발할뿐더러, 이놈이 뱉어낸 계수 추정치나 신뢰구간 잣대마저도 다 거짓말이라는 강한 불신과 우려를 퍼뜨립니다.

Furthermore, it is reasonable to suspect that when the expected value of `bikers` is small, the variance of `bikers` should be small as well.
**둘째, 널뛰기 발작 (분산 일정성의 붕괴)!**
우리는 상식적으로 "자전거 타는 사람이 애초에 몇 명 안 되면(기댓값이 작으면), 데이터가 요동치는 변동 폭(분산)도 당연히 잔잔하게 작을 것이다" 라고 통계적 유추를 합리적으로 할 수 있습니다. 

For instance, at 2 AM during a heavy December snow storm, we expect that extremely few people will use a bike, and moreover that there should be little variance associated with the number of users during those conditions.
예를 들어, 12월 크리스마스이브의 지독한 눈 폭풍이 몰아치는 새벽 2시에 따릉이를 빌리는 미친 사람은 거의 극소수일 겁니다. 그렇다면 이 환경 조건에서는 사람 머릿수의 통계적 오차 변동 파동(분산) 자체도 거의 바닥에 붙어 잔잔해야 정상입니다.

By contrast, between 7 AM and 10 AM, in April, May, and June, when skies are clear, there are 243.59 users, on average, with a standard deviation of 131.7.
대조적으로, 벚꽃이 피는 4월~6월의 맑고 화창한 아침 출근 시간(오전 7시~10시)에는 어떨까요? 이땐 평균 따릉이 대여 수치 폭주량이 자그마치 하루 243.59명으로 떡상하며, 덩달아 표준편차(분산의 씨앗)도 131.7로 폭발적으로 널뛰기 발작을 합니다. 

This is a major violation of the assumptions of a linear model, which state that $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a mean-zero error term with variance $\sigma^2$ that is _constant_, and not a function of the covariates.
이게 뭐가 문제냐고요? 선형 회귀 몽둥이는 애초에 태어날 때 "$Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$" 라는 공장에서 조립되는데, 이 설계도의 핵심 공리 조건 중 하나가 오차항 덩어리 $\epsilon$ 이 **무!조!건! 일정하고 꼿꼿한 분산 $\sigma^2$ (constant variance)**만 가져야 한다는 철칙입니다. 오차 분산이 날씨 눈치나 보면서 변동하면 안 된다는 거죠.

Therefore, the heteroscedasticity of the data calls into question the suitability of a linear regression model.
그러므로, 지금처럼 평균이 작을 땐 분산도 좁쌀이고 평균이 클 땐 분산이 산만해지는, 이른바 **불균일 분산(heteroscedasticity, 널뛰기 발작)** 현상은 직선만 고집하는 선형 회귀의 꼿꼿한 존재 가치를 완전히 산산조각 내버리며 치명적 부적합 딱지를 붙여버립니다.

Finally, the response `bikers` is integer-valued.
**셋째, 부러진 통나무의 한계 (정수형 데이터의 역습)!**
애초에 타깃 반환 값 카운트 변수 `bikers` 는 반 갈라질 수 없는 '정수 덩어리' 입니다. 

But under a linear model, $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a continuous-valued error term.
하지만 선형 모델의 설계도 식인 $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$ 안에서 놀고 있는 저 오차 꼬리표 $\epsilon$ 이란 놈은, 본질적으로 소수점 아래로 무한히 이어지는 유들유들한 **연속 수치 폭 덩어리**라는 점입니다.

This means that in a linear model, the response $Y$ is necessarily continuous-valued (quantitative).
이 말인즉슨, 직선 통나무 선형 모델 안에서 굴러나온 결과물 타깃 $Y$ 는 무조건 연속적인 긴 선분 점수를 가지는 정량적 수치일 수밖에 없다는 (억지 실수) 강제 룰을 지닙니다. 즉 사람 수를 1.25명 따위로 쪼개 버리죠!

Thus, the integer nature of the response `bikers` suggests that a linear regression model is not entirely satisfactory for this data set.
따라서 타깃 $Y$ 카운트가 본질적으로 가진, 절대 쪼갤 수 없는 '정수 계단' 덩어리 성질은 우리가 애지중지하던 선형 회귀 통나무 방망이가 이 전장에서는 절대 완전히 만족스럽게 써먹을 무기가 못 된다는 한계를 쐐기 박아버립니다.

Some of the problems that arise when fitting a linear regression model to the `Bikeshare` data can be overcome by transforming the response; for instance, we can fit the model
자, 이쯤 되면 통계학자 형님들도 발등에 불이 떨어집니다. 이 골치 아픈 3대 재앙을 무마해 보기 위해서, 학자들은 타깃 반응 변수 멱살을 잡고 **'로그 변환(log transformation) 마취 주사'** 를 놓는 꼼수 처방을 발동시킵니다. 그래서 수식을 이렇게 비틀죠:

$$
\log(Y) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon \quad (4.38)
$$

Transforming the response avoids the possibility of negative predictions, and it overcomes much of the heteroscedasticity in the untransformed data.
타깃 데이터에 로그 마취제를 놔버리면 기가 막히게 약발이 돌면서 방금 전의 1번 오류(음수 유령 예측) 늪도 회피해 빠져나가고, 2번 오류(불균일 분산 널뛰기 발작)도 상당히 잔잔하게 잠재우며 많은 난관을 꽁수로 극복해 냅니다.

However, it is not quite a satisfactory solution, since predictions and inference are made in terms of the log of the response, rather than the response.
**하지만, 이것마저도 임시방편(미봉책)일 뿐 완전히 맘에 드는 근본 백신 해결책이 아닙니다.** 왜냐하면 이렇게 꼼수를 부리면, 우리가 뽑아낸 예측 결괏값이나 추론 지표들이 본래 현장 직관 타깃이 아닌 '로그를 억지로 씌워놓은 이상한 스코어 요골경' 시점으로 왜곡돼 전달되기 때문입니다.

Furthermore, a log transformation of the response cannot be applied in settings where the response can take on a value of 0.
더욱이 최악의 약점이 있죠. 수학 시간에 배웠듯이 타깃 반응 변수에 '로그 마취 주사'를 박으려면 절대 피해야 할 금기값이 있습니다. 바로 **$Y$ 가 정확히 '0명'을 찍는 순간**입니다. 로그 0 은 수학적으로 파탄이 나므로, 0을 품을 수밖에 없는 야생 카운트 데이터 바닥에서는 이 꼼수마저 치명타를 입고 막혀버립니다.

We will see in the next section that a Poisson regression model provides a much more natural and elegant approach for this task.
직선 통나무도 부러지고 꼼수 로그 주사마저 실패한 절망의 대치 상황! 다음 장에서 우리는 드디어 이 카운트 데이터 지옥도를 구원해 낼 아주 자연스럽고 기품이 넘치게 우아하며 강력한 맞춤형 해결 기동 타격 구원 투수 무기, 제3의 병기 **'포아송 회귀(Poisson regression)'** 모델의 화려한 등판을 두 눈으로 보게 될 것입니다!

---

## Sub-Chapters

[< 4.6 Generalized Linear Models](../index.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html)

---
layout: default
title: "trans2"
---

[< 4.6 Generalized Linear Models](../trans2.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.1 Linear Regression on the Bikeshare Data
# 4.6.1 자전거 대여 데이터 패기에 잘못 들이댄 선형 회귀 몽둥이질

To begin, we consider predicting `bikers` using linear regression. The results are shown in Table 4.10. We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour. We see that bike usage is highest in the spring and fall, and lowest during the winter months. Furthermore, bike usage is greatest around rush hour (9 AM and 6 PM), and lowest overnight. Thus, at first glance, fitting a linear regression model to the `Bikeshare` data set seems to provide reasonable and intuitive results.
우선 무턱대고 냅다 옛날 병기인 '선형 회귀' 몽둥이를 들어 `bikers` 자전거 대여 이용자 머릿수를 예측해 보는 것부터 시작해 봅시다. 이 몽둥이를 마구 휘두른 첫 성적표는 교재 표 4.10에 고스란히 박혀있습니다. 이 성적표를 까보면, 예컨대 하늘 날씨가 맑음에서 구름 낀 칙칙한 우중충함으로 나빠질 때 대략 시간당 평균 12.89명의 자전거 대여 손님이 뚝 떨어져 사라진다는 걸 눈치챌 수 있죠. 더 심각하게 하늘에서 비나 눈이 쏟아져 내리기 시작하면 거기서 53.60명의 라이더들이 추가로 증발해 버립니다. 계절의 눈치도 철저히 보는데, 꽃피는 봄과 낙엽 지는 가을에 따릉이 장사가 제일 피크를 치고, 뼈 시리게 얼어붙는 겨울엔 바닥을 칩니다. 이뿐입니까? 출퇴근 러시아워 지옥 철인 오전 9시와 저녁 6시 언저리에 자전거 대여판이 가장 불타오르고, 모두가 곯아떨어진 한밤중엔 사람 그림자도 찾기 힘듭니다. 여기까지 딱 보면, 어라? 이 까다롭고 요상한 `Bikeshare` 데이터 군단에다 그저 낡은 1차 선형 회귀 몽둥이질을 한 번 때렸을 뿐인데도, 꽤나 합리적이고 고개가 끄덕여지는 직관적인 예측 답안지 결과물이 툭 튀어나오는 것처럼 아주 그럴싸하게 착각이 듭니다!

But upon more careful inspection, some issues become apparent. For example, 9.6% of the fitted values in the `Bikeshare` data set are negative: that is, the linear regression model predicts a _negative_ number of users during 9.6% of the hours in the data set. This calls into question our ability to perform meaningful predictions on the data, and it also raises concerns about the accuracy of the coefficient estimates, confidence intervals, and other outputs of the regression model.
하지만 기쁨도 잠시! 돋보기를 들이대고 이 몽둥이질의 결과를 아주 철저하게 뜯어보면, 끔찍한 결함들이 속속 피를 흘리며 수면 위로 떠 오릅니다. 가장 치명적인 예로, 이 선형 모델 머신이 추정 계산해 뱉어낸 자전거 대여 머릿수 예측값들 중에 무려 전체의 9.6% 에 해당하는 수치들이 **마이너스(음수 음의 숫자)** 로 곤두박질치는 기괴한 기현상이 발생합니다! 상식적으로 사람이 어찌 반으로 쪼개지는 것을 넘어 영하 마이너스 개수로 뚝뚝 떨어질 수 있습니까? 선형 회귀 모형의 뇌 구조는 이런 현실 세계의 절대 법칙을 전혀 모르고, 오직 직선 공식 방패에 의존해 맹렬히 파고든 나머지, 전체 시간 대역 데이터의 10% 가까운 기간 동안 무려 _음수(negative) 마이너스_ 명의 대여 손님들이 나타난다고 말도 안 되는 오답을 뻔뻔히 짖어대고 있는 겁니다! 이 미친 헛발질은 당장 이 구닥다리 모델 머신이 저 데이터를 이해하고 쓸만한 실전 예측 무기로 투입될 수 있는가에 대한 근본적인 존재 정체성 논란을 폭발시키며, 더불어 거기서 튀어나온 계수 점수, 신뢰성 구간, 나머지 수리 결과물 몽땅 전부 다 싹 다 불신 덩어리로 의심의 도마 위에 오르게 만듭니다.

Furthermore, it is reasonable to suspect that when the expected value of `bikers` is small, the variance of `bikers` should be small as well. For instance, at 2 AM during a heavy December snow storm, we expect that extremely few people will use a bike, and moreover that there should be little variance associated with the number of users during those conditions. By contrast, between 7 AM and 10 AM, in April, May, and June, when skies are clear, there are 243.59 users, on average, with a standard deviation of 131.7. This is a major violation of the assumptions of a linear model, which state that $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a mean-zero error term with variance $\sigma^2$ that is _constant_, and not a function of the covariates. Therefore, the heteroscedasticity of the data calls into question the suitability of a linear regression model.
더 환장할 노릇은 여기서 끝이 아닙니다. 상식의 잣대로 따져봤을 때, 뻔히 `bikers` 예상 대여가 바닥을 친다면 당연히 그 편차 기복인 에러 널뛰기 진동 '분산(Variance)' 또한 쥐 죽은 듯이 아주 아주 같이 작아야 마땅합니다. 극단적 예시로, 살인적인 12월 한겨울 폭풍우 눈보라가 치는 새벽 2시 땡 한밤중을 상상해 보십시오. 미치지 않고서야 자전거를 탈 사람은 거의 0에 수렴할 테고, 당연하게도 그날그날의 날씨에 따라 오차 범위로 널뛰는 사람 수의 변동 기복조차 바닥에 껌 딱지처럼 딱 붙어있어야 정상이지요. 반면, 따스한 봄바람 부는 4~6월 눈부시게 쾌청한 맑은 하늘의 출근 러시아워인 아침 7시에서 10시 사이엔 어떨까요? 이 황금 타임엔 평균 무려 243.59 명씩 벌떼처럼 쏟아져 나오면서 동시에 131.7씩 파도치는 살벌한 널뛰기 표준 편차의 진동 파동을 뿜어냅니다! 결국 상황에 따라 이 분산 진동 폭이 고무줄처럼 축 쳐졌다가 널 뛰기를 반복하는 것이죠. 헌데 이 엄청난 사실은, 저 옛날 낡아빠진 선형 회귀 모델이 굳게 맹신하는 수학 종교적 진리 가정을 정면 통수 치며 파괴해 버립니다! 선형 모델 녀석은 $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$ 라는 뻔한 공식에서, 저 오차 쓰레기통인 $\epsilon$ 이란 놈이 무조건 예측 변수 상황과 절대 남남 무관하게 완전히 고고히 외딴 방에 틀어박혀 무조건 분산 진폭 고정 상수($constant$ $\sigma^2$) 로만 못 박힌 채 절대 요동치지 않고 예쁘게 똑같이 고르게 평범한 평준화 상태를 띈다고 우겨대기 때문입니다. 고로 이 `Bikeshare` 핏덩이 데이터가 스스로 고스란히 뿜어내는 '고무줄 분산 이단아 성향', 즉 저 끔찍한 **이분산성(heteroscedasticity 상황에 따라 분산 폭이 지 마음대로 들쭉날쭉하는 기현상)** 의 본성은 선형 회귀 모델이란 저 뻣뻣한 병장기 도구가 이 야생에선 완전 무용지물 쓸모없는 결함품이란 것을 치명적으로 폭로 폭발 증명해 냅니다!

Finally, the response `bikers` is integer-valued. But under a linear model, $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$, where $\epsilon$ is a continuous-valued error term. This means that in a linear model, the response $Y$ is necessarily continuous-valued (quantitative). Thus, the integer nature of the response `bikers` suggests that a linear regression model is not entirely satisfactory for this data set.
설상가상 결정타! 우리가 때려 맞춰야 할 목표물 과녁인 이 `bikers` 타깃 값의 성별은 1명, 2명 자를 수 없는 단단한 '정수(integer)' 의 형태를 띠고 있습니다. 헌데 이 무식한 1차 뼈대 선형 도구 모델의 공식 $Y = \beta_0 + \sum_{j=1}^{p} X_j \beta_j + \epsilon$ 밑바탕에 구겨 넣어진 저 에러 꼬리 $\epsilon$ 부품은 빌어먹을 무한소수점 마디를 달고 끝없이 주욱 미끄러지는 '연속 값(continuous-valued)' 쓰레기 더미 찌꺼기입니다. 이게 무슨 소리냐? 애초에 이 선형 몽둥이를 휘두른 결과물 $Y$ 치수는 절대로 딱 떨어지는 정수가 될 수 없고 필연 운명적으로 질척거리며 소수점이 뚝뚝 떨어지는 무한 '연속 지표(quantitative 수치)' 로만 처참히 뱉어져 나온다는 뜻입니다. 그러니 무 참 히 똑 떨 어 지 는 인간 카운트 대가리 수 타깃 본성인 저 `bikers` 정수 덩어리를, 그딴 징그러운 연속 소수점 폭우로 맞춰 보겠다는 이 멍청한 선형 회귀 전략은 태생부터 이 게임 세팅 무대와 1도 상종할 수 없는 쓰레기 결함 덩어리로 절대 어울릴 수 없음을 강력 시사 처단 증명합니다.

Some of the problems that arise when fitting a linear regression model to the `Bikeshare` data can be overcome by transforming the response; for instance, we can fit the model
그나마 이런 저질 선형 회귀 몽둥이를 이 기이한 `Bikeshare` 돌연변이 데이터에 어떻게든 억지로 맞춰 욱여넣으려 발생한 혈투 쇼에서의 피곤한 이 몇몇 결함 문제점들을 응급처치 방편인 **'로그 변환 수술 (transforming the response)'** 스킬로 살짝 메꿔 치유 상쇄 해 볼 꼼수 여지는 남아있습니다. 예컨대 우리는 목표물 껍데기를 살짝 비틀어 다음 꼼수 모델로 후려쳐 볼 수 있습니다:

$$
\log(Y) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon \quad (4.38)
$$

Transforming the response avoids the possibility of negative predictions, and it overcomes much of the heteroscedasticity in the untransformed data. However, it is not quite a satisfactory solution, since predictions and inference are made in terms of the log of the response, rather than the response. Furthermore, a log transformation of the response cannot be applied in settings where the response can take on a value of 0. We will see in the next section that a Poisson regression model provides a much more natural and elegant approach for this task.
이렇게 반응 타깃 $Y$ 거울상 자체를 '로그($\log$)' 란 요술 마법진으로 확 비틀어 버리면 그 끔찍했던 음수(- 마이너스) 머릿수 예측이 터지는 징그러운 오류 확률을 강제로 차단 근절 봉쇄 회피해 버릴 수 있고, 날 것 데이터가 널뛰던 그 지저분한 '고무줄 이분산성 분노 발작' 증세마저도 상당 량 강하게 눌러 짓밟아 다독이고 안정화 극복해 줍니다. 
하지만! 아무리 응급수술로 떡칠했어도 이건 진짜 근본 병원체가 뽑힌 대박 구원 솔루션과는 한참 거리가 멉니다! 가장 치명적인 건, 이렇게 뒤틀어 놓으면 기계가 뱉은 미래 예언 숫자들과 통계 추론 스탯 점수들이, 우리가 알고 싶은 '내일 자전거 대여명수 진또배기'가 아니라 기형 괴물처럼 변이된 '대여 명수의 로그 수치' 따위의 미친 단위 껍데기로 나와버리기 때문에 다시 사람의 언어로 풀 때 골치가 깨집니다. 게다가 타깃에 죽음의 사신인 숫자 '0명' 이라는 절망 폭탄 카운트 값이 떨어지는 날엔, 로그 $\log(0)$ 수술 자체가 수학적으로 영원히 무한 폭발 에러로 아예 먹혀 적용조차 불가능한 끔찍 심각 장벽 결함에 부닥치게 됩니다. 
기대하십시오! 우린 이제 곧 다음 넥스트 폭풍 세션 무대 단원 장에서 이딴 조잡한 땜빵 회귀가 아니라, 이런 불연속 카운트(갯수) 적중 과녁 놀음에 태생부터 가장 본능적으로 최적화된 우아 환상 무적 포텐 터지는 **포아송 회귀 모델(Poisson regression model)** 투입이라는 어마무시 고급스러운 천재 전투 구원 타격 접근법을 직접 감상 관전 조우하게 될 것입니다!

---

## Sub-Chapters

[< 4.6 Generalized Linear Models](../trans2.html) | [4.6.2 Poisson Regression On The Bikeshare Data >](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html)

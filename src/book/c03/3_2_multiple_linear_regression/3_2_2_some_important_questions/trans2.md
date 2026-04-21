---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/trans2.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/trans2.html)

# 3.2.2 Some Important Questions

# 3.2.2 몇 가지 중요한 질문들 (다중 회귀 냄비 요리가 끝난 후 사장님의 까다로운 질문 4가지)

When we perform multiple linear regression, we usually are interested in answering a few important questions.
우리가 이 거대한 '다중 선형 회귀'라는 요술 냄비에 온갖 재료(변수)를 다 때려 넣고 한소끔 끓여냈을 때, 이 요리를 맛본 사장님은 보통 다음과 같은 4가지의 아주 날카롭고 핵심적인 질문들을 던지며 우리를 압박해 올 것입니다.

1. _Is at least one of the predictors $X_1, X_2, \dots, X_p$ useful in predicting the response?_
1. _네가 잔뜩 집어넣은 재료들($X_1, X_2, \dots, X_p$) 중에 붕어빵 맛(반응 변수)을 좋게 만드는 데 **단 한 개라도 제대로 된 쓸모가 있긴 하냐?** (전부 쓰레기 아니야?)_

2. _Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?_
2. _저 많은 재료가 진짜 전부 다 피같이 중요한 엑기스야? 아니면 몇 개는 괜히 폼으로 넣은 거고 **진짜 영양가 있는 핵심 재료(부분 집합)**는 따로 있는 거 아니야?_

3. _How well does the model fit the data?_
3. _그래서 네가 끓인 이 짬뽕 요리(모델)가 실제 손님들의 치열한 입맛(현실 데이터)에 도대체 **얼마나 기가 막히게 잘 들어맞는데?**_

4. _Given a set of predictor values, what response value should we predict, and how accurate is our prediction?_
4. _만약 내가 내일 장사에 "간장 2스푼, 설탕 1스푼(주어진 투입 변수)"을 준다면, 내일 매출(응답 값)은 정확히 며칠이나 갈지 예언해 봐! 그리고 **그 예언이 얼마나 소름 돋게 정확할지** 자신할 수 있어?_

We now address each of these questions in turn.
자, 심호흡을 하시고. 등줄기에 땀이 흐르지만 당황하지 마세요. 통계학자 선배들이 남겨둔 비밀 무기들로 이제 이 질문들의 멱살을 잡고 하나씩 차례대로 박살 내보도록 하겠습니다.

---

## One: Is There a Relationship Between the Response and Predictors?

## 질문 1: 타겟과 투입 변수 군단들 사이에 아예 연관성이 존재하긴 하는가? (단 한 놈이라도 유죄인가?)

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$.
예전 귀여웠던 '단순' 선형 회귀 시절을 떠올려보세요. 그때는 투입 힌트가 달랑 1개($X_1$) 밖에 없었기에 타겟(매출)이랑 연관이 있는지 없는지 뽀록을 내려면 그냥 눈 딱 감고 기울기 자판기 $\beta_1$ 이 "혹시 완전 0인 거 아니야?" 하고 의심만 대충 한 번 해보면 그만이었습니다.

In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \dots = \beta_p = 0$.
하지만 이번엔 투입 힌트 요원이 $p$ 명이나 떼거지로 등장하는 다중 회귀 세계입니다. 여기서 가장 먼저 해야 할 일은 "야, 너희 요원들 전부 다 월급 루팡 0점짜리 무능력자 아니야?" 하고 단체 기합을 넣는 겁니다. 수식으로는 $\beta_1 = \beta_2 = \dots = \beta_p = 0$ 이 기함할 사태가 벌어졌는지 의심하는 것이죠.

As in the simple linear regression setting, we use a hypothesis test to answer this question.
단순 회귀 시절 써먹던 재판의 꿀맛을 잊지 마세요. 이번 질문의 진실 역시 통계 법정의 꽃, '가설 검정' 재판을 통해 심판할 겁니다.

We test the null hypothesis,
우리는 피고인 격인 이 최악의 무능력 '귀무가설($H_0$)'을 법정에 세울 겁니다.

$$
H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad (3.23)
$$
(해석: 모든 변수의 계수 능력이 단 하나도 빠짐없이 0으로 무가치하다!)

versus the alternative
그리고 열혈 검사가 되어 이 맞불을 놓는 '대립가설($H_a$)'을 외칩니다.

$$
H_a : \text{at least one } \beta_j \text{ is non-zero.}
$$
(해석: 잘 들어라! 요원 무리 중 무조건 **최소한 단 한 놈($\beta_j$) 이상은** 절대 파워 0이 아닌 살아 숨 쉬는 진짜배기 유능한 녀석이 섞여 있다!)

This hypothesis test is performed by computing the _F -statistic_ ,
이 숨 막히는 통계 법정 싸움의 판결봉을 내리치기 위해 우리는 가설 검정 배심원이자 대망의 판결 수치인 **_F-통계량(F-statistic)_** 이란 거대한 판사님을 모셔 와 계산 테이블 판에 올립니다.

$$
F = \frac{(\text{TSS} - \text{RSS}) / p}{\text{RSS} / (n - p - 1)} \quad (3.24)
$$

where, as with simple linear regression, $\text{TSS} = \sum (y_i - \bar{y})^2$ and $\text{RSS} = \sum (y_i - \hat{y}_i)^2$.
(여기서 단순 통계랑 똑같이 $\text{TSS}$ 는 타겟들이 미친 듯이 널뛰는 분산의 총량이고, $\text{RSS}$ 는 회귀선이 못 잡아내고 기어이 남겨버린 찌꺼기의 총합입니다.)

If the linear model assumptions are correct, one can show that
만약 선형 모델의 밑바탕 룰들이 정당하다면, 통계 괴짜들은 이 복잡한 분모 부분이 다음과 같다는 걸 수학적으로 증명해냅니다.

$$
E\{\text{RSS} / (n - p - 1)\} = \sigma^2
$$

and that, provided $H_0$ is true,
동시에, 만일 모든 변수가 다 쓰레기라는 절망적인 **귀무가설 $H_0$ 가 진짜 참** 이라고 끔찍한 가정을 내리면 분자 부분 역시 이렇게 박살 나 버립니다.

$$
E\{(\text{TSS} - \text{RSS}) / p\} = \sigma^2
$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1.
이 충격적인 두 공식을 $F$-통계량 분수 꼴에 딱 맞춰서 위아래로 나누어 보세요. $\sigma^2$ 을 $\sigma^2$ 으로 나누면 분수 꼴은 어떻게 되죠? 정답입니다! 결과적으로 모델 냄비 안에 든 **모든 예측 힌트들이 매출(반응치)과 1도 관련 없는 처참한 가짜 쓰레기일 때**, 이 위대한 **$F$-통계량 판사님은 숫자를 가차 없이 '1' 부근**에 던져주며 비웃을 겁니다. (1이면 완전 꽝이라는 뜻이죠.)

On the other hand, if $H_a$ is true, then $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$, so we expect $F$ to be greater than 1.
그러나 안도하세요! 만약 우리 측 변호사가 제기한 "최소 단 한 놈이라도 진짜 유능하다($H_a$)"가 정답이라면 분자의 화력이 $\sigma^2$ 보다 미친 듯이 활활 타올라 팽창하게 됩니다. 결론적으로 우리는 **$F$-통계량이 숫자 1을 아득히 뚫고 저 하늘 위로 솟구치길** 맹렬하게 학수고대합니다!

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6.
아까 예제 장부에 있던 `TV`, `radio`, `newspaper` 세 얼간이들을 몽땅 집어넣고 `sales(매출)`를 맞추게 시켜본 다중 회귀 모델의 $F$-통계량 판사님 성적표가 아래 표 3.6 에 박혀 있습니다.

In this example the $F$-statistic is 570.
두구두구두구! 우리의 예제에서 자랑스러운 $F$-통계량 값은 무려 **570** 이 나왔습니다!

Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$.
야호! 이 숫자는 '망했다'의 의미인 '1' 따위와는 궤를 달리할 만큼 어마어마하게 큰 산처럼 거대합니다. 즉, 570이라는 이 미친 점수는 "다 쓰레기다!"라고 외치던 귀무가설 $H_0$ 요괴 뚝배기를 깨부수고 기각시켜버리는 가장 압도적인 강력한 쇠투입니다!

In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`.
다시 말해서 이 비정상적으로 거대한 $F$-통계량(570)은 콧방귀를 뀌며, "멍청아, 저 세 가지 매체 중에 **적어도 한 놈은 반드시** 매출(`sales`)을 터트리는 핵심 열쇠 배후 마스터마인드와 진하게 놀아나고 있단 소리다!" 라고 호쾌하게 선언하는 셈입니다.

However, what if the $F$-statistic had been closer to 1?
잠깐만요, 축제 분위기에 찬물을 끼얹어볼까요? 만약 이 야박한 $F$-통계량 점수가 570이 아니라 1.05 같은 초라하고 아리송한 1 근처의 숫자가 떴다면 어떤 대혼란이 왔을까요?

| Quantity | Value |
| :--- | :--- |
| Residual standard error | 1.69 |
| $R^2$ | 0.897 |
| $F$-statistic | 570 |

**TABLE 3.6.** _More information about the least squares model for the regression of number of units sold on TV, newspaper, and radio advertising budgets in the_ `Advertising` _data. Other information about this model was displayed in Table 3.4._
**TABLE 3.6.** `Advertising` _동네의 TV, 신문, 라디오 삼총사 광고 요원을 투입시켜 판매량을 때려 맞춘 다중 예측 모델의 후광 스펙(RSE, R^2, F값) 성적표입니다._

How large does the $F$-statistic need to be before we can reject $H_0$ and conclude that there is a relationship?
도대체 저 망할 $F$-통계량 판사님이 **'얼마나 크게 노발대발'** 해야 비로소 우리가 편하게 발 뻗고 "오예, $H_0$ 가짜 놈들 감옥 보내고 진짜 관계가 있다!" 라고 만세 결론을 탕탕! 확신할 수 있을까요?

It turns out that the answer depends on the values of $n$ and $p$.
아쉽게도, 이 판사님의 빡침 게이지 분노 컷 기준은 우리가 가진 탄알(데이터 개수 $n$)과 투입시킨 요원 수(변수 개수 $p$)의 쪽수에 따라 이리저리 고무줄처럼 바뀝니다.

When $n$ is large, an $F$-statistic that is just a little larger than 1 might still provide evidence against $H_0$.
만약 우리가 들고 있는 데이터 총알 개수($n$)가 십만 개, 백만 개처럼 상상을 초월하게 창고에 넘쳐난다면 판사님 기준은 엄청 너그러워집니다. 이럴 땐 판사님 점수가 숫자 1보다 모기 코딱지만큼만 큰 1.01 정도만 떠도 "그래, 총알이 이리 많은데 살짝만 움직여도 이건 우연이 아니지. 유죄 땅땅!" 하고 단숨에 $H_0$ 를 감옥에 처넣을 증거로 채택해 줍니다.

In contrast, a larger $F$-statistic is needed to reject $H_0$ if $n$ is small.
이와는 반대로, 만약 우리 수중의 데이터 총알 조각($n$)이 수십 개 수준으로 쥐꼬리만큼 빈약하고 궁핍하다면 상황은 암울해집니다. 이때는 판사님 눈높이가 깐깐해져서 어설픈 1근방 점수론 씨알도 안 먹히며, $H_0$ 의 철근 같은 방어를 부수려면 덩치가 집채만 한 어마 무시한 $F$-통계량 헐크 점수를 데려와야만 겨우 설득할 수 있습니다.

When $H_0$ is true and the errors $\epsilon_i$ have a normal distribution, the $F$-statistic follows an $F$-distribution.$^6$
통계 괴짜들이 파헤친 또 다른 비밀: 만약 온 세상 힌트가 진짜 쓰레기인 가설 $H_0$ 가 참 진실이고 오차 요정($\epsilon_i$)들이 통계의 여신이 축복한 정규 분포(종 모양)를 얌전하게 잘 따른다면 이 미쳐 날뛰는 **$F$-통계량 녀석은 하늘이 점지한 운명이자 놀이터인 '$F$-분포표' 곡선을 철저히 따르며 춤을 춥니다.**$^6$

For any given value of $n$ and $p$, any statistical software package can be used to compute the $p$-value associated with the $F$-statistic using this distribution.
자, 머리 아픈 $F$ 분포표 두루마리는 우리가 쳐다볼 필요 없습니다. 어차피 요새 통계 소프트웨어 장난감 파이썬 녀석들이 알아서 $n$ 과 $p$ 쪽수를 계산기에 입력하고 이 저주받은 분포표를 쫙 뒤져서 $F$-통계량에 합당한 궁극의 성적표, 전능한 **'$p$-값($p$-value)'** 도장을 1초 만에 딱 찍어 뱉어 내줄 겁니다.

Based on this $p$-value, we can determine whether or not to reject $H_0$.
우리는 판사님의 골치 아픈 $F$ 숫자 크기를 따질 것도 없이, 그냥 이 기계가 뱉어준 앙증맞은 **$p$-값 크기 하나만 딱 째려보고** "어? 0.05보다 작네? 유죄 유죄!! 당장 $H_0$ 사형장으로 끌고 가!" 하고 쿨하게 기각 여부를 만천하에 확정 지을 수 있죠.

For the advertising data, the $p$-value associated with the $F$-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased `sales`.
다시 우리 놀던 광고 예제로 돌아옵시다. 표 3.6 에 박혀있던 $F$ 덩치 570짜리에 찰싹 붙어 나온 궁극의 $p$-값이 무려 **숫자상 사실상 진짜배기 0.00000... (0)** 입니다! 이쯤 되면 판사님이 망치를 찢어발긴 수준이라 우리는 "투입된 세 매체 떨거지 중 **적어도 단 한 놈은 반드시** 매출 폭등에 멱살을 잡고 배후 조종하는 강렬한 주동자가 틀림없다!"는 핵무기급의 강크리트 타격 증거를 손에 쥐게 됩니다!

In (3.23) we are testing $H_0$ that all the coefficients are zero.
아까전 수식 (3.23) 에서 이뤄진 재판은 사실 법정에 끌려온 **'모든 요원 계수 전원'**이 모조리 0퍼센트 무능력자 쓰레기인지를 몽땅 걸고넘어지는 대규모 집단 소송 무죄 추정이었습니다.

Sometimes we want to test that a particular subset of $q$ of the coefficients are zero.
하지만 가끔은 이 지독한 사장님들이 약간 사악한 짓을 시킬 때가 있습니다. 전체 요원을 다 의심하는 게 아니라, 타겟을 잡아서 **"일부 선택된 $q$ 명의 떨거지 소규모 서브그룹 녀석들만 딱 지목해서 얘네들 혹시 단체로 쓸모없는 0원짜리 놈들 아니야?"** 하고 집단 구타(테스트)를 걸고 싶을 때가 생깁니다.

This corresponds to a null hypothesis
이런 기괴한 요청 사항을 통계 법정의 '부분 귀무가설' 조서 혐의로 작성하면 다음과 같은 오싹한 형태가 됩니다.

$$
H_0 : \beta_{p-q+1} = \beta_{p-q+2} = \dots = \beta_p = 0
$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables _except_ those last $q$. Suppose that the residual sum of squares for that model is $\text{RSS}_0$. Then the appropriate $F$-statistic is
(여기서 독자들의 눈 보호와 공무원식 편의를 위해, 저 사형선고를 맞고 제명당할 혐의 타겟인 불쌍한 $q$ 마리의 변수 녀석들을 일부러 줄 꼬리 맨 뒤쪽에 나란히 몰아세워 줄을 세웠습니다.) 이럴 땐 어떻게 조져야 할까요? 우리는 과감하게 이 불쌍한 왕따 $q$ 명을 **완전히 파면 누락 삭제해버린 _제외 버전의 반쪽짜리 두 번째 서브 모델_ 을 새롭게 한판 더 적합** 시켜버립니다! 자, 이 녀석들을 쳐내고 얻어낸 그 잘난 2군 모델의 오차 찌꺼기 덩어리(잔차 제곱합)를 $\text{RSS}_0$ 라고 가명 지어봅시다. 그럼 이제 এই $q$ 명의 떨거지 그룹의 진실 여부를 심판할 진짜 맞춤형 $F$-통계량 판사님 공식은 살짝 비틀어져 아래 꼴이 됩니다.

$$
F = \frac{(\text{RSS}_0 - \text{RSS}) / q}{\text{RSS} / (n - p - 1)}
$$

For instance, consider an example in which $p$ = 100 and $H_0$ : $\beta_1 = \beta_2 = \dots = \beta_p = 0$ is true, so no variable is truly associated with the response. In this situation, about 5 % of the $p$-values associated with each variable (of the type shown in Table 3.4) will be below 0.05 by chance. In other words, we expect to see approximately five small $p$-values even in the absence of any true association between the predictors and the response. In fact, it is likely that we will observe at least one $p$-value below 0.05 by chance! Hence, if we use the individual $t$-statistics and associated $p$-values in order to decide whether or not there is any association between the variables and the response, there is a very high chance that we will incorrectly conclude that there is a relationship. However, the $F$-statistic does not suffer from this problem because it adjusts for the number of predictors. Hence, if $H_0$ is true, there is only a 5 % chance that the $F$-statistic will result in a $p$-value below 0.05, regardless of the number of predictors or the number of observations.
자, 좀 긴장하시고 끔찍한 막장 시나리오 하나 상상해 보세요. 미친 척하고 아무 짝에도 쓸모없는 쓰레기 변수 요원을 한 100명($p=100$)쯤 대거 채용투입했다고 칩시다. 설상가상으로 진짜 우주의 진실마저 $H_0$ 가 참(100명 전원이 매출에 진짜 아무 영향 0%를 미침)이라고 무지막지하게 저주를 내렸습니다. 완전히 전멸각이죠! 그런데 진짜 악몽은 여기서 터집니다. 이 대규모 스파이 요원 100명 각각의 찌라시 점수($p$-값)를 1대1로 면담 까보면, 무슨 일이 발생할까요? 통계라는 요괴 장난으로 인해 약 5% 확률인 5명 정도는 우주의 기운(순전한 요행 무작위성)을 받아 **우연 뽀록으로 $p$-값 0.05 미만의 프리패스 인증**을 받으며 기적의 "나는 유의미한데요?" 환각 판정이 떠버리는 대참사가 일어납니다! 현실 세계 매출과 진짜 인과 연관이 단 하나도! 쥐뿔도 존재치 않는 멸망전 우주 공간에서조차 우리는 우연의 장난질로 인해 '아주 쓸모 있어 보이는 $p$-값 인증러'를 5명이나 허상으로 만날 뻔뻔을 맞이하게 된다는 뜻입니다. 사실 재수 없으면 이런 우연 뽀록 유의미함을 적어도 최소 한 놈 이상에서 목격할 확률이 미친 듯이 엄청나게 농후합니다!
결론은 소박하지만 서늘합니다: 만약 분석의 최고 책임자인 당신이 이 거대한 큰 그림 숲을 볼 수 있는 망원경(전체 제어 모드) 없이 그저 현미경만 들고 요원 1명 1명 각개전투의 부품 조각인 단순 $t$-통계량과 $p$-값 찌라시 쪼가리들에만 맹목적으로 의존해서 "둘 사이 관계있냐 없냐!" 옥석을 가려버리는 도장을 그릇되게 찍는다면? 허공 속 아무것도 없는 가짜 도화지 위에 "오! 관계가 존재하네요!" 하며 억지 날조 가짜 뉴스를 확신해 헛다리를 짚고 파멸적인 결론 도장을 오판해 버릴 살벌한 위험 확률 빈도가 머리통까지 꽉 들어찰 겁니다.
하지만 기뻐하세요! 바로 이 지점에서 구원의 철옹성 거대 보스, **총괄 지휘 통계 전함인 _F_-통계량**이 등장합니다. 이 위대한 $F$ 판사님은 자신이 이끌 예측 요원 무리 쪽수($p$)가 100명이건 거대하건 그 규모를 이미 자동 인지하여 머릿수만큼 알아서 필터링 튜닝(조정) 조율해 주므로 이런 잔바리 왜곡 사기에 끄떡없이 평온한 정조준 방어를 해냅니다. 따라서 진짜로 당초 전체 진실 가설 $H_0$ 가 '참(전부 무능력 꽝이다)'임이 확고할 경우, 투입 지휘 요원의 우글거림 숫자 난입 크기 따위나 주어진 데이터 수량의 얕음 깊음 조건에 일체 얽매이지 않고 철저히 독립 무관하게, 이 최종 $F$-통계량 무대가 종국에 혼자 멍청하게 헛스윙 조작 오류 오판 $p$-값(0.05 이하) 판결을 재수 없이 덜면 뱉어버릴 헛장난 발생 사고 비율의 오폭 천장 확률은 고작 안심되는 **단 5% 컷 라인 안전봉쇄 영역**에 영구 맹세로 굳건히 봉인됩니다.

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$ . However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the _F_ - statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as _forward selection_ , can be used. This _high-dimensional_ setting is discussed in greater detail in Chapter 6.
지금껏 우리가 침이 마르도록 찬양했던 "예측 요원들과 타겟 정답 사이에 진짜 사랑의 끈(연관성)이 있니?" 검증용으로 별도의 무적 무기 `$F$-통계량 캐논`을 사용하는 이 통계학의 성배 접근법은, 안타깝게도 **투입 변수 $p$ 요원들의 숫자가 상대적으로 얌전하고 아담할 때, 필히 데이터 총알 포탄($n$) 숫자보다는 현저하게 수적 열세 조무래기 규모 비율일 때나 씽씽하게 아주 잘 통하는 방식**입니다. 하지만 현생의 험난한 사냥터에선 어떨까요? 가끔가다가 우리 머리에 어마어마한 물량 공세의 재료 성분 변동수 군단 떼거지가 폭포수처럼 무자비하게 투하될 때가 간혹 발생합니다! 가장 가혹한 지옥 불 불능 최악의 사태로 가령 투입 요원 머릿수 $p > n$ (데이터보다 많음) 이라는 어이없는 역전 돌파 사태가 벌어지면요? 정답을 캐내야 할 빚더미 정체불명 외계인 무리 집단 숫자인 모수 구적 $\beta_j$ 가 도리어 그들을 쫓아 역추적 힌트 단서로 심문 삼아야 할 근간 한정 원천 표본 관측 데이터 포탄들 총알분보다도 더 비대하게 웃돌아 커져버리는 모순 딜레마 오메가 먹통 상황에 내몰립니다. 이런 맹목적 과잉 돌파 불능 늪지대 환경 국면에 빠지면, 통계의 최고 지성인 최소 제곱법 전통 수학 연산 부싯돌을 비벼 대고서라도 애당초 다중 선형 회귀 뼈대 모델 자체의 시작 버튼 시도조차 원천 불가 봉쇄되어 접속 차단 뻗고 맙니다! 고로 저 전능했던 만능 무기 _F_-통계량 포신조차 무용지물 고장 난 허수아비로 폐기될 뿐만 아니라, 억울하게도 현 챕터 절반을 지나올 때까지 우리가 그렇게나 매달려 배웠던 대다수 기타 메인 핵심 통계 기술 도구 파편들 전체 역시 모조리 줄줄이 휴지 조각이 되어 고철 동력의 무덤으로 사라져 버립니다. 
허나 섣부른 좌절감에 무릎 꿇기엔 아직 이릅니다! 정녕 이렇듯 변수들의 덩치 크기 쪽수 군단 $p$ 가 우주를 뒤덮을 만큼 살포시 뻥튀기될 압살 재앙 상황이 맞닥뜨려진다 해도 바로 직후 바짝 이어지는 다음 넥스트 섹션 구간 스킬 트리에서 찬찬히 치밀하게 논의 구명 해부해 줄 **_전진 선택법(Forward selection)_** 같은 구세주 꼼수 탈출 신기술들을 활용해 요령껏 다차원 위기 난관을 영리하게 역우회 우주 접목 돌파해 버리는 또 다른 새로운 희망 대체 통계 기조 비상 열쇠 무기 요법을 훈련할 기회가 뻔히 도래할 것입니다. 이런 기묘한 고밀도 골치병, **_고차원(High-dimensional)_** 난해 세팅 기조라는 거악 테마의 깊은 동굴 심연 공략전 여정기는 앞으로 펼쳐질 대망의 뒷장 챕터 6 분량 구역 토의에서 마침내 정식으로 대폭 한층 더 치밀한 상세 스케일 분석의 해체 수술 집중 도마 위 화두 등판 정점을 거하게 쏘아 올리며 토벌 탐구될 계획입니다.

---

### Two: Deciding on Important Variables (질문 2: 중요한 변수 결정)
* [📖 쉬운 해설판으로 이동하기](./3_2_2_1_two_deciding_on_important_variables/trans2.html)

다수의 변수 중 반응 변수와 실제로 유의미한 관계가 있는 변수 조합들을 선택(Variable Selection)하는 방법을 배웁니다.
전진 선택법(Forward), 후진 제거법(Backward) 및 혼합 선택법의 개념을 간단히 다룹니다.

### Three: Model Fit (질문 3: 모델 적합도)
* [📖 쉬운 해설판으로 이동하기](./3_2_2_2_three_model_fit/trans2.html)

선택된 다중 회귀 모델이 주어진 훈련 데이터에 얼마나 잘 적합되었는지 다중 R² 지표 및 RSE를 통해 살펴봅니다.
변수가 추가될 때마다 R²가 증가하는 성질에 대비한 평가를 소개합니다.

### Four: Predictions (질문 4: 예측)
* [📖 쉬운 해설판으로 이동하기](./3_2_2_3_four_predictions/trans2.html)

적합된 모델을 바탕으로 새로운 관측치에 대한 반응 변수 스코어를 예측할 때 수반되는 세 가지 큰 불확실성을 검토합니다.
신뢰 구간 및 예측 구간(Prediction Interval)의 차이를 명확히 살펴봅니다.

---

[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/trans2.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/trans2.html)

---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2 Multiple Linear Regression](../trans2.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/trans2.html)

# _3.2.1 Estimating the Regression Coefficients_

# _3.2.1 회귀 계수 추정 (마법의 조미료 비율 찾기)_

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula
앞서 우리가 단순 선형 회귀라는 소꿉장난 바닥에서 놀았을 때와 마찬가지로, 이 거대한 다중 회귀 공식 (3.19) 안에 숨어있는 마법의 계수들 $\beta_0, \beta_1, \dots, \beta_p$ 역시 우리가 감히 범접할 수 없는 우주의 진리값(미지수)들이라 어떻게든 눈치껏 추리해 내야 합니다. 우리가 불완전한 머리를 굴려 이 숫자들과 엇비슷한 가짜 추정치 기록물들인 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 이 녀석들을 요령껏 구해냈다고 치면, 우린 아래와 같은 공식을 써서 당당하게 매상을 예측할 수 있죠.

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals
이 거대한 파라미터 덩어리들을 추정할 때도, 예전 단순 회귀 시절에 써먹었던 '최소 제곱법'이라는 사기적인 스킬을 똑같이 가져다 씁니다. 요점은 명확합니다. 실제 정답 장부($y_i$)와 우리 모델이 찍어낸 예언($\hat{y}_i$)의 차이점, 즉 '쓸모없는 잔차(에러)들의 제곱합'을 가장 최소한으로 구겨버릴 수 있는 최강의 콤비 $\beta_0, \beta_1, \dots, \beta_p$ 조합을 찾아내는 겁니다!

$$
\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)
$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not fulfill provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4
위의 저 끔찍한 (3.22) 에러 수식이 가장 바닥을 치게 만들어 주는 $\hat{\beta}$ 요정들의 값이 바로 우리가 애타게 찾던 '다중 최소 제곱 회귀 계수 추정치'입니다. 그런데 (3.4)에서 봤던 딱 2개짜리 단순 회귀 공식처럼 예쁘고 간단하게 떨어질 거라 기대하지 마세요. 변수가 여러 개 얽히고설킨 탓에, 이 다중 회귀 계수들을 손으로 구하려면 대학 수학의 '행렬 대수학(Matrix Algebra)'이라는 무시무시한 기호 마법을 써야만 계산이 가능한 끔찍하고 기괴한 형태를 띱니다. 겁주려던 건 아닌데, 아무튼 이런 이유로 책에서는 여러분의 멘탈을 지키기 위해 이 책에 징그러운 행렬 증명식을 길게 풀어쓰진 않겠습니다. 어차피 21세기에 이런 걸 손으로 풀 이유는 전혀 없습니다! 파이썬 서킷이나 `R` 같은 훌륭한 통계 소프트웨어 노예들에게 버튼 하나만 누르면 마법같이 계수를 착착 뽑아주니까요. 이번 장 후반부 랩(Lab) 실습 코스에서 파이썬으로 이 짓을 어떻게 뚝딱 해치우는지 구경하게 될 겁니다. 

<br>

<p align="center">

<img src="./img/3_4.png" alt="In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.">

</p>

<br>

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._
**FIGURE 3.4.** _자, 그림 3.4를 보시죠! 변수(힌트)가 단 1개라 2차원 평면에 선을 쭉 긋던 시절은 끝났습니다. 변수 2개($X_1, X_2$)가 투입된 3차원 입체 공간에서는 우리가 치유할 최소 제곱 회귀선이 마치 납작한 '판때기(평면, Plane)' 모양으로 공중에 떠오르게 됩니다. 이 철판은 각 빨간색 관측 점(데이터들)에서 철판까지 수직으로 떨어지는 밧줄(오차)들의 굵기 제곱합이 가장 날씬해지도록 절묘한 각도로 눌러 찍어 맞춘 결과물입니다._

illustrates an example of the least squares fit to a toy data set with $p=2$ predictors.
(원문 이어짐) 이 그림이 바로 힌트 변수가 2개($p=2$)인 가상의 귀여운 장난감 입체 마을에 억지로 거대한 철판(최소 제곱 적합)을 눌러 찍어본 모습입니다.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data.
자, 이제 분위기를 잡고 표 3.4를 봅시다. 이 성적표는 우리가 예전에 쓰던 `Advertising` 장부에서 TV, 라디오, 그리고 신문 매체 3단 콤보 광고 예산을 한꺼번에 다 때려 넣고 돌렸을 때 튀어나온 최정예 '다중 회귀 계수 추정치'입니다.

We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales.
우리는 이 심오한 결과를 다음과 같이 통역합니다. 즉, "사장님이 TV랑 신문 광고 예산 건드리지 말고 그 상태 그대로 동결시켜 놓은 채로, 오직 **라디오 매체**에만 특별 보너스로 $\$1,000$을 더 투척하신다면, 평균적으로 자그마치 189 박스의 매출 상승 폭탄이 보장됩니다!" 라고요.

Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates.
이 성적표를 아까 예전에 단순 회귀만 주구장창 돌렸던 표 3.1이나 표 3.3 의 점수들과 슥 맞대보고 비교해 보시죠. 재밌게도 `TV`나 `radio`의 다중 모델 계수 점수는 혼자 독박으로 단순 모델 뛸 때 받았던 점수랑 엇비슷하게 엇갈려 나옵니다.

However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86.
하지만 충격적인 대반전이 숨어 있습니다! 아까 표 3.3에서 혼자 독박 회귀를 뛰던 시절의 `newspaper(신문)` 계수는 분명 "저 매출 좀 올려주는데요?" 하며 유의미하게 0을 벗어난 숫자(0.055)를 자랑했습니다. 그런데 이 3단 콤보 다중 회귀 냄비에 같이 처박혔더니, 신문의 파워 계수 수치는 **거의 0 바닥**에 나뒹굴고, 이에 콤보로 터지는 $p$-값 성적 역시 0.86 부근에서 얼쩡거리며 "휴지조각만도 못한 무의미함"의 나락으로 떨어져 버렸습니다!

This illustrates that the simple and multiple regression coefficients can be quite different.
이 대참사 스토리가 우리에게 알려주는 교훈은 명확합니다. 당신이 혼자 단칸방에서 잰 '단순 투력(단순 회귀 계수)'과, 온갖 변수들이 치고받고 싸우는 콜로세움에서 잰 '다중 투력(다중 회귀 계수)'은 하늘과 땅 차이로 완전히 뒤바뀔 수 있다는 끔찍한 사실입니다.

This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`.
도대체 왜 이런 기가 막힌 뒷목 잡는 배신이 일어났을까요? 그 이유는 단순 회귀를 굴리던 시절의 막대기 기울기는, 다른 유력 경쟁자인 `TV` 나 `radio` 가 무슨 짓을 하든 말든 애비 애미도 없이 철저하게 무시한 채, 오직 신문에 돈을 바르면 매상이 얼마나 뛸지만 극단적으로 단순화해서 평균값을 강요했기 때문입니다.

By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.
하지만 룰이 빡빡한 '다중 회귀' 모드 세계에서는 심판의 잣대가 완전히 다릅니다. 여기서 `newspaper` 가 인정받으려면, 옆의 잘나가는 일진들인 **`TV` 나 `radio` 광고 예산을 꼼짝 못 하게 손발 다 묶어(고정) 놓고**, 오로지 순수하게 '신문 광고 비용' 하나만 1,000 달러 올렸을 때 창출할 수 있는 타겟의 평균 매출 순도(상승분)만을 측정받게 되는 것입니다.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the opposite?
자, 그렇다면 단순 선형 회귀 시절엔 분명 "매출과 신문은 짱친이야!" 하며 영혼의 단짝처럼 나팔을 불어댔는데, 정작 다중 회귀가 "저기요, 둘이 아무 사이도 아닌데요?" 하고 완전히 반대되는 일침을 가하는 이 상황! 이게 과연 상식적으로 말이 될까요?

In fact it does.
놀랍게도, 너무나 소름 돋게 이치에 들어맞는 합법적인 타당한 스토리입니다.

Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5.
이 미스터리를 풀기 위해, 우리는 탐정처럼 표 3.5 에 떡하니 놓여 있는 세 가지 힌트 군단 변수들과 타겟 매출 변수 사이의 얽히고설킨 인간관계도, 즉 '상관관계 행렬(Correlation matrix)' 증거 자료를 분석해 볼 필요가 있습니다.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |
| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |
| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |
| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | $0.8599$ |

**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._
**TABLE 3.4.** `Advertising` _장부 데이터를 탈탈 털어서, TV, 라디오 및 신문 광고 예산이라는 3가지 공격진을 몽땅 출전시켜 단위 판매량을 맞추기 위해 구워낸 다중 선형 회귀 솥단지의 정예 최소 제곱 계수 전투력 표입니다. 앗! 신문(newspaper)의 $p$-값이 0.8599 라니... 맙소사!_

| | `TV` | `radio` | `newspaper` | `sales` |
| :--- | :--- | :--- | :--- | :--- |
| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |
| `radio` | 0.0548 | 1.0000 | 0.3541 | 0.5762 |
| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |
| `sales` | 0.7822 | 0.5762 | 0.2283 | 1.0000 |

**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._
**TABLE 3.5.** `Advertising` _동네의 주요 구성원들_ `TV` _,_ `radio` _,_ `newspaper` _그리고 짱인_ `sales` _까지 서로 대놓고 뒷조사해 본 피 튀기는 친밀도 점수표(상관관계 행렬)입니다._

Notice that the correlation between `radio` and `newspaper` is 0.35.
탐정의 예리한 시선으로 표 안을 잘 들여다보세요! `radio` 와 `newspaper` 사이에 적힌 친밀도 점수가 0.35 군요.

This indicates that markets with high newspaper advertising tend to also have high radio advertising.
이 수상쩍은 밀회 숫자가 고발하는 진실은 이렇습니다: "동네 시장 사장님들 중에 신문에 돈을 미친 듯이 뿌린 사람들은, 백이면 백 **라디오 방송국에도 덩달아 거액의 광고 지출을 함께 꽂아주는 끈끈한 '세트 마케팅' 경향**이 농후하다!"

Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales.
이제 이 다중 회귀 모델의 살벌한 판결문이 100% 진실이라고 무죄 추정해 봅시다. 즉, "**신문 광고** 이 녀석은 사실 매출($sales$)을 올리는 데 1도 관여한 바가 없는 허수아비 백수건달이고, 진짜 막대한 매상의 주역은 **라디오 광고** 였다!"라고 쳐보는 거죠.

Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets.
그렇다면 사장님들이 라디오에 뭉칫돈을 밀어 넣은 화끈한 시장 동네에선 아주 자연스럽게 식당 매상이 하늘 높은 줄 모르고 폭등했을 겁니다. 그런데 바로 이 시점에서 아까 우리의 스파이 노선표(상관 행렬)가 고발했듯, 바로 똑같은 해당 시장의 그 사장님들은 세트 마케팅이랍시고 부질없는 '신문 전단지' 광고에도 막 무지성으로 쓸데없는 돈을 처발랐을 확률이 다분합니다!

Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales.
결과적으로, 어떤 바보 분석가가 이 시장의 내막(라디오의 캐리)을 아예 눈과 귀를 닫고 무시한 채, 오로지 `sales` 와 `newspaper` 달랑 두 놈만 교무실로 끌고 와 단둘이서 지독한 **단순 선형 회귀** 줄재기를 시켰다간 끔찍한 오해를 할 수밖에 없습니다! 신문 광고 녀석은 실상 매출에 버프를 1도 주지 못한 조무래기임에도 불구하고, 신문 쪽 지출이 수직 점프한 곳마다 이상하게 매출이 떡상하는 황당무계한 가짜 우상향 신기루 현상(가짜 관계)을 "유의미하다!" 며 환호성을 지르며 관측하게 될 공산이 100%입니다.

So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` .
한마디로 잔혹하게 요약하자면, `newspaper(신문)` 광고비는 진짜 주인공인 `radio(라디오)` 광고비 출몰 지역을 졸졸 따라다니는 그림자이자 허수아비 대리인(surrogate) 행세를 해왔던 셈입니다! 불쌍한 라디오가 피땀 흘려 `sales(매출)`를 하드 캐리해 이뤄낸 그 영광스러운 우승 트로피의 "공로(credit)"를, 아무 짝에도 쓸모없는 신문지가 마치 자기가 한 것인 양 무단으로 가로채 덧쓰고 꿀을 빨았던 괘씸한 양상이 다중 회귀 재판을 통해 마침내 뽀록난 것입니다!

This slightly counterintuitive result is very common in many real life situations.
여러분의 뇌 회전을 뒤틀리게 만드는 이런 기만적이고 직관에 반하는 억울한 사기극 양상은, 머신러닝 데이터의 숲이 울창한 수많은 실생활 현장에서 숨 쉬듯 아주 뻔질나게 일어나는 흔하디흔한 사건 파일입니다.

Consider an absurd example to illustrate the point.
이 환장할 노릇의 무임승차 관점을 뇌리에 콱 박아주기 위해, 잠시 코미디 같은 우스꽝스러운 농담 예시 하나를 들어봅시다.

Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper` .
바다 해변가 동네에서 여름내 수집된 엽기적인 장부에 적힌 **'마을 내 식인 상어 습격 빈도 횟수'** 대 **'아이스크림 트럭 매출 성적'** 데이터를 대조하여 단순 선형 회귀 도화지에 흩뿌려 봅니다. 그럼 아까 `sales` 와 `newspaper` 가 작당 모의를 뽐냈던 것과 판박이 급으로, 엄청나게 가파른 양(+)의 상관관계 우상향 직선이 쭉 그어질 겁니다! (아이스크림이 많이 팔린 날 = 상어가 사람을 많이 뜯어먹은 날?!)

Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks.
물론, 이 미친 회귀 직선만 맹신하고 마을 회의에서 "상어 습격의 치명적 원인은 저주받은 아이스크림이다! 인명피해를 당장 줄이기 위해 해운대 백사장의 모든 아이스크림 판매를 강제 금지해야 한다!" 라고 주장하는 머리에 총극 맞은 사람은 (감사하게도 아직까진) 없을 겁니다.

In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks.
이 바보 같은 코미디의 뒷배경인 실제 세계 현실(Reality)을 들여다볼까요? 진범은 다름 아닌 숨겨진 흑막, **'후덥지근한 기온(온도 폭염)'**이었습니다! 온도가 미친 듯이 오르면 에어컨을 피해 해수욕장으로 사람들이 개미 떼처럼 바글바글 쏟아져 나오게 되며, 늘어난 꼬마 인파는 자연스레 아이스크림 장수 트럭을 쓸어 담듯 매진시키고 매출액을 폭등시킵니다. 그리고 동시에! 물속에서 찰박거리는 불쌍한 인간 먹잇감 머릿수 풀이 압도적으로 늘어났으니, 덩달아 배고픈 식인 상어들의 습격 건수 파티도 자동적으로 떡상해 기승을 부리는 것이 당연한 이치죠.

A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.
상어 습격 횟수의 진실을 파헤치기 위해 이 불합리한 '아이스크림 판매량'과 진범 '온도'라는 총 두 명의 용의자 변수를 피고석에 나란히 세워 **다중 회귀 분석의 서치라이트**를 비춰보면 아주 통쾌한 결론이 납니다. 우리의 똑똑한 직관이 외쳤던 진리 그대로, '온도'라는 진짜 스펙 파워를 고정해 놓고 난이도 조정을 거친 후에는 억울하게 범인으로 몰렸던 '아이스크림 판매'는 더 이상 아무런 살육 힘도 쥐지 못한 **허접한 조무래기(유의미하지 않은 예측 변수, 무죄!)** 임이 만천하에 드러나게 됩니다.

---

[< 3.2 Multiple Linear Regression](../trans2.html) | [3.2.2 Some Important Questions >](../3_2_2_some_important_questions/trans2.html)

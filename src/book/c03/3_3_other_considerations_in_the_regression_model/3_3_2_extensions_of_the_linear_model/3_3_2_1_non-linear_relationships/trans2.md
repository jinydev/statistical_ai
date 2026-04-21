---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3.2 Extensions Of The Linear Model](../trans2.html) | [3.3.3 Potential Problems >](../../3_3_3_potential_problems/trans2.html)

# Non-linear Relationships

# 비선형적 관계 (뻣뻣한 직선의 족쇄를 끊은 구불구불 마법 곡선)

As discussed previously, the linear regression model (3.19) assumes a linear relationship between the response and predictors.
아까부터 귀에 못이 박히도록 씹어댔지만, 우리 꽉 막힌 선형 회귀 모범생 수식(3.19)은 힌트 재료(예측 변수)와 도출 타겟(응답 변수) 사이의 인과율 관계가 무조건 일자로 쫙 뻗은 "반듯한 평행 직선(Linear)이어야만 해!" 라는 결벽증적인 강박 관념(가정)을 앓고 있습니다.

But in some cases, the true relationship between the response and the predictors may be nonlinear.
하지만 속지 마세요. 막상 야생에서 실전 데이터를 까 뒤집어 보면 특정 재료 변수와 타겟 변수가 진짜로 맺고 얽혀 있는 그 실체적 진실 관계망은, 딱딱한 직선이 아니라 구불구불 S자 코스나 물수제비 뜨듯 파동치는 변덕스러운 비선형적(Non-linear) 곡선 굴레를 띠고 있는 경우가 태반입니다.

Here we present a very simple way to directly extend the linear model to accommodate non-linear relationships, using _polynomial regression_.
그래서 이 한계에 갇힌 가엾은 선형 모델에게 유연한 요가(비선형적 굴곡 관계 수용 능력)를 가르쳐 한 단계 외연을 직접 확장해버리는, 어이없을 정도로 치트키처럼 쉽고 허접한 야매 우회 기법 하나를 전수하고자 합니다. 이름하여 **_다항 회귀(Polynomial regression, 제곱 튀기기 마법)_** 수법입니다.

In later chapters, we will present more complex approaches for performing non-linear fits in more general settings.
물론 나중에 저 멀리 후반부 챕터 심화 과정에 당도하면, 이 다항 회귀 같은 원시적인 야매술을 넘어서 훨씬 더 거시기하고 현란한 비선형적 그물망 적합 곡선을 짤 수 있는 각양각색 고오급 접근 방식 무공들을 배울 테지만, 일단 지금은 이 기술로 만족합시다.

Consider Figure 3.8, in which the `mpg` (gas mileage in miles per gallon) versus `horsepower` is shown for a number of cars in the `Auto` data set.
자, 그 유명한 `Auto(자동차 스펙)` 장부 기록에서 수많은 똥차와 슈퍼카들을 모아놓고, 그놈의 차체 엔진 **`horsepower(마력)`** 대비 기름 먹는 하마 연비 수준 **`mpg(갤런당 주행거리)`** 의 치열한 힘겨루기 역학 구도를 적나라하게 찔러 그려본 그림 3.8의 도화지를 눈 번쩍 뜨고 구경해 보세요.

The orange line represents the linear regression fit.
도화지 한가운데 떡하니 막무가내 꼬챙이처럼 꽂혀 가로지르는 삐죽한 '주황색 선'이 바로... 꽉 막힌 모범생 '순정 선형 회귀 직선 타겟 적합 궤적'입니다. 기가 막히죠? 전혀 데이터 점도 안 맞추고 그냥 허공을 가릅니다.

There is a pronounced relationship between `mpg` and `horsepower`, but it seems clear that this relationship is in fact non-linear: the data suggest a curved relationship.
누가 봐도 연비(`mpg`)와 마력(`horsepower`) 간에는 엄청나게 노골적이고 지독한 원한 관계(음의 상관성)가 판을 치는데, 그 둘의 멱살잡이 궤도가 일직선 철로가 아니라 오목한 미끄럼틀 곡면 코스로 미끄러져 추락하는 **비선형적 곡선 궤도(Curved relationship)** 양태임이 그 흩뿌려진 데이터 좁쌀 점들의 형상만 봐도 너무나 자명하고 노골적으로 뽀록 나버렸습니다.

A simple approach for incorporating non-linear associations in a linear model is to include transformed versions of the predictors.
자, 이 꽉 막힌 철로 일직선 선형 모델을 찰흙처럼 말랑말랑하게 휘어 곡선 비선형 변곡점 굴레를 소화하도록 마개조 튜닝하는 가장 직관적이고 무지성 심플 마술법이 뭘까요? 그건 바로, 넣으려던 원래의 재료 힌트 변수 자체의 몸뚱아리를 거울상 조작 변환(다중 제곱 변환)해서 억지로 갈아 구겨 집어넣는 짓거리입니다.

For example, the points in Figure 3.8 seem to have a _quadratic_ shape, suggesting that a model of the quadratic form
예를 들어 그림 3.8의 미끄럼틀 궤적 도면 점박이 좁쌀들의 궤도는 포물선 이차 함수와 같은 _2차 곡선형(Quadratic)_ 밥그릇 형상의 처짐을 격하게 띠고 있습니다. 이 사실은, 우리가 억지로라도 고안해야 하는 수식 뼈대 자체가 다음과 같이 '2차식 제곱' 포맷의 덩어리가 박혀야만
**==> picture [285 x 11] intentionally omitted <==**
may provide a better fit.
그나마 지금 이 장부 점들과 우월하게 더 들어맞는 눈치 만랩 맞춤형 합당 적중 적합선(better fit)을 안겨줄 수 있다는 확신을 시사합니다.

Equation 3.36 involves predicting `mpg` using a non-linear function of `horsepower`.
저기 억지로 구겨 넣은 방정식 (3.36) 모양새를 보면, 우리가 노리는 타겟 연비 `mpg`의 환영을 예측하기 위해 무려 `horsepower(마력)`의 몸뚱아리를 비선형적 2차 함수 파츠로 뒤틀어 활용하고 있습니다.

_But it is still a linear model!_ That is, (3.36) is simply a multiple linear regression model with $X_1 = \text{horsepower}$ and $X_2 = \text{horsepower}^2$.
**"우왘 혁명이다!! 곡선 비선형 모델을 찾았다!!"** 라고 흥분하기엔 이릅니다. _놀랍게도 저놈의 근본은 아직 철저히 일직선 '선형 모델'입니다!_ 눈치가 빠른 분이라면 억지 변형 꼼수 (3.36) 꼴 자체는 근본적으로 그저 원래부터 존재하던 다중 선형 회귀 기본 틀 속 세트에서 원래 $X_1$ 자리에 그냥 $\text{horsepower}$ 딱지 하나 꽂아놓고, 이어지는 두 번째 옆자리 칸 $X_2$ 자리에다가는 $\text{horsepower}$ 몸뚱아리를 자가 증식 제곱($^2$) 때려버린 엉망진창 돌연변이 항목 하나 더 쑤셔서 합쳐놓은 그냥 꼼수 덮어씌우기 짬뽕 조립 선형판에 지나지 않습니다. 한마디로 그냥 기존 선형 모델 공식을 가지고 말장난 친 거죠.

So we can use standard linear regression software to estimate $\beta_0, \beta_1$, and $\beta_2$ in order to produce a non-linear fit.
어쨌든 뼈대 자체는 근본 선형 모델 틀 구조라서 개이득인 점이 있습니다. 통계쟁이들이 저 비선형 곡률 포물선을 구경해 보고자 구해야 하는 저 귀찮은 파라미터 $\beta_0, \beta_1, \beta_2$ 덩어리들을 찾을 때, 별도의 복잡한 슈퍼컴퓨터 코딩을 짤 필요 없이 그냥 세상 흔해 빠진 '일반 보급형 표준 선형 회귀 소프트웨어 계산기(파이썬/R 일반 함수)' 에다 휙 던져 밀어 넣기만 하면 고스란히 1초 만에 마법같이 짠 하고 곡률 적합 궤적이 도출 추산되어 튀어나옵니다!

The blue curve in Figure 3.8 shows the resulting quadratic fit to the data. The quadratic fit appears to be substantially better than the fit obtained when just the linear term is included.
저 도화지 위 그림 3.8 창문 가운데 멋지게 흐느적대며 누운 **'시퍼런 파란색 곡선 훌라후프'**가 바로 이렇게 자가 증식 꼼수로 튀겨내 투사한 2차 제곱 방정식 타점 적합선입니다. 맨눈으로 딱 시각 견적만 내봐도, 이 '2차 포물선 곡선'의 어르고 달래는 꺾임 적합성은 기존의 융통성 제로의 팍팍한 '주황색 직진 일자 꼬챙이' 단일 직선 항만을 억지로 박아 넣었을 때의 그 참사보다는 압도적이고 눈부시게 향상된 퍼펙트 타격 합치 타점을 기록하며 개선 구가합니다.

**==> picture [304 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
Linear(1차 꼬챙이)<br>Degree 2(2차 파란 훌라후프)<br>Degree 5(5차 녹색 괴물뱀)<br>50 100 150 200<br>Horsepower(마력)<br>50<br>40<br>30<br>Miles per gallon(갤런당 깡패 연비)<br>20<br>10<br>**----- End of picture text -----**<br>

**FIGURE 3.8.** _The_ `Auto` _data set. For a number of cars,_ `mpg` _and_ `horsepower` _are shown. The linear regression fit is shown in orange. The linear regression fit for a model that includes_ $\text{horsepower}^2$ _is shown as a blue curve. The linear regression fit for a model that includes all polynomials of_ `horsepower` _up to fifth-degree is shown in green._
**FIGURE 3.8.** `Auto(자동차 스펙)` _장부. 수많은 차들의_ `horsepower(마력)` _힘과_ `mpg(연비)` _사이 피 튀기는 전쟁터입니다. (주황색 선) 융통성 없는 1차원 순정 꼬챙이 선형 적합선. (파란색 곡선) 영리하게 마력을 2번 제곱($^2$)해서 덧씌운 2차 돌연변이 요가 곡선. (초록색 곡선) 뇌절을 쳐서 마력을 5번이나 미친 듯이 연타 제곱해 구겨 짠 5차 다항식 괴물 뱀입니다._

|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept(기본연비 출발점)`<br>`horsepower(1차 일반 마력)`<br>`horsepower^2(2차 빙글 제곱 마력)`|56.9001<br>1.8004<br>31.6<br>_<_0_._0001<br>_−_0.4662<br>0.0311<br>_−_15.0<br>_<_0_._0001<br>0.0012<br>0.0001<br>10.1<br>_<_0_._0001|

**TABLE 3.10.** _For the_ `Auto` _data set, least squares coefficient estimates associated with the regression of_ `mpg` _onto_ `horsepower` _and_ $\text{horsepower}^2$ _._
**TABLE 3.10.** `Auto` _장부를 바탕으로 고무장갑이 아닌_ `horsepower(마력)` _과_ `horsepower^2(제곱 마력)` _두 쌍포를 투하시켜 타겟 연비_ `mpg` _를 사냥해 획득한 최소 제곱 전범 성적표 계수 추정치 결과물. 모든 $p$-값이 0에 수렴하며 완벽 대승을 거뒀습니다._

The $R^2$ of the quadratic fit is $0.688$, compared to $0.606$ for the linear fit, and the $p$-value in Table 3.10 for the quadratic term is highly significant.
눈대중이 아니라 찐 산술 전투력 스펙 수치만 찔러봐도 압살입니다. 예전 구닥다리 1차 꼬챙이 선형 적합 때 뱉어냈던 기염토할 결정 계수 성적 $R^2$ 수위가 겨우 $0.606$ 따리에 맴돌던 것에 비해, 방금 제곱 곡면으로 틀어박아 적중시킨 이번 2차 곡선 적합의 $R^2$ 점수는 영광스럽게도 무려 $0.688$ 타점을 터뜨리며 점핑 부스트했습니다. 덤으로 보너스 표 3.10 조서에 까발려진 저 2차 제곱 요주의 변환 항 $\text{horsepower}^2$ 꼬리표 $p$-값 체급을 구경해 보시죠! 소름 돋게도 아주 철저하고 완벽히 통계적 권위로 빛나는 극명 초월의 유의성 잣대 면갑을 두르고 "내가 바로 실세 곡선이다!" 라며 맹렬히 위세를 시현 중입니다.

If including $\text{horsepower}^2$ led to such a big improvement in the model, why not include $\text{horsepower}^3$, $\text{horsepower}^4$, or even $\text{horsepower}^5$?
여기서 갑자기 인간의 탐욕 뇌절 본능이 꿈틀댑니다! "야 ㅋㅋㅋ 야! 꼴랑 마력 변수를 한 번 더 증식시켜 $\text{horsepower}^2$ 제곱 하나 더 우겨넣은 요술 꼼수로 모델 능력치가 저렇게나 대폭발 부스트 혁명 펌핑을 이루었다면... 차라리 내친김에 $\text{horsepower}^3$ (3제곱), $\text{horsepower}^4$ (4제곱), 아니 아예 미친 척하고 $\text{horsepower}^5$ (5제곱) 같은 과잉 다중 돌연변이들까지 모조리 다 수식에 무지성으로 도배 편입 반죽해 때려버리면 타점 100%짜리 신의 장난감을 얻지 않겠냐?"

The green curve in Figure 3.8 displays the fit that results from including all polynomials up to fifth degree in the model (3.36).
저기 그림 3.8 도화지 바닥에 시퍼렇게 질주하다 못해 미친 듯이 징그럽게 도는 저 **'형광 초록색 꼬불 뱀 곡선'**이 바로 인간의 그 끔찍한 뇌절 탐욕이 발현된 결과론적 망작 투사 도면입니다! 기존 방정식 틀 (3.36) 베이스에 감히 이성의 끈을 놓고 5차 한계 등급까지 전부 무자비하게 포스트 다항식 모의 곡선 성분들을 다변화 투사 짬뽕 스까 통폐합시켜 뽑아낸 최후의 광역 광기 적합 도출선 위용 꼬라지인 셈이죠.

The resulting fit seems unnecessarily wiggly — that is, it is unclear that including the additional terms really has led to a better fit to the data.
하지만 두 눈으로 결과물을 직접 뜯어보세요. 이 무식하게 기워낸 초록빛 5차 모의선 궤도의 자태는 진짜 헛구역질 날 만큼 좌우로 요동치고 꼬물꼬물(wiggly) 과도하게 발작하며 굽이치는 징그러운 기괴 뱀 지렁이 몸뚱아리에 불과합니다. 이게 과연 무슨 똥볼 찬 의미를 시사 반영할까요? 결국 아무리 과파생 거듭 제곱 무리수를 우겨넣듯 쓰잘떼기 없이 항을 부풀려 봤자, 그것이 실제 현존 관측 데이터 데이터 결 양상을 합리적 합목적 기조 속에서 진짜 더 나은 질 좋은 영양가 타점의 예측 적중 해답을 조달 안겨줬느냔 질문 앞엔 "도무지 객관 투명성이 조또 없고 미궁 속 모호 불투명 쓸모 쓰레기임!" 이라는 싸늘한 비웃음 확정 단언만이 판결로 떨어질 따름입니다. (이걸 통계 꼰대들은 **오버피팅(과적합)**이라 놀려댑니다.)

The approach that we have just described for extending the linear model to accommodate non-linear relationships is known as _polynomial regression_, since we have included polynomial functions of the predictors in the regression model.
방금 우리가 미친 듯이 썰을 풀며 주도적으로 까발린, "고집불통 1차 선형 로봇에 억지로 다중 제곱 곱셈 변기를 탑재 거부감 없이 끼워 융통성 넘치는 비선형 곡선 관계를 수용 감당토록 외변 개조하는" 이 기만적 전술 기법 수단을 통계 바닥 전문 용어로 아예 우아하게 칭송 격식을 갖춰 포장한 단어가 바로 **_다항 회귀(Polynomial regression)_** 입니다! 이 거창한 이름의 배경 연유는 단순 무식합니다! 그냥 우리가 애꿎은 힌트 회귀 모델 예측 변수 엉덩이에다가 다항식(거듭제곱 폴리노미얼) 함수 폭탄을 억지로 부가 개입 납치 내전 포함 감행 시켰다는 그 노골적인 만행 흔적을 그대로 직관 시사 까발렸기 때문입니다.

We further explore this approach and other non-linear extensions of the linear model in Chapter 7.
이후의 웅장한 지적 탐구 뒷맛은 나중 저기 한참 멀리 떨어진 챕터 7장 심해 구도 속으로 토스하겠습니다! 거기 도달하면 우리는 이 징그러운 다항 수법 기초 단계를 기포 삼아, 애초에 뼈다귀 기저 1차원 선형 모델을 요철 비선형 외계 변이 마개조 포맷들로 더욱 흉악하게 뒤바꿔 치환하는 훨씬 다양한 번외적 외연 변형 괴물 도구와 고차원 편제 접근 수법 요령 룰까지 죄다 우르르 싸잡아 한껏 광범위 파헤치며 논의할 부푼 원대한 설계 수립 계획을 기다리고 품을 것입니다!

---

[< 3.3.2 Extensions Of The Linear Model](../trans2.html) | [3.3.3 Potential Problems >](../../3_3_3_potential_problems/trans2.html)

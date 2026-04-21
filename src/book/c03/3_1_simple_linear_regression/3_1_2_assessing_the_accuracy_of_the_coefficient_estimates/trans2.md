---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/trans2.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/trans2.html)

# 3.1.2 Assessing the Accuracy of the Coefficient Estimates
# 3.1.2 계수 추정치의 정확도 평가 (내 가중치들은 얼마나 믿을만할까?)

Recall from (2.1) that we assume that the _true_ relationship between $X$ and $Y$ takes the form $Y = f(X) + \epsilon$ for some unknown function $f$, where $\epsilon$ is a mean-zero random error term.
이전 단원 (2.1)에서 우리가 세웠던 가정을 떠올려 볼까요? 우리는 원인($X$)과 결과($Y$) 사이에 진짜 신만이 아는 완벽한 _실제(true)_ 관계 패턴이 존재한다고 믿고, 이 관계를 $Y = f(X) + \epsilon$ 라는 우주의 법칙 공식으로 표현합니다. 여기서 $\epsilon$(입실론)은 기분파인 하늘의 장난처럼, 평균적으로는 아무 영향도 안 주지만(+,- 상쇄되어서 0) 매번 무작위로 방해를 하는 '오차항'입니다.

If $f$ is to be approximated by a linear function, then we can write this relationship as
만일 이 완벽하지만 무지막지하게 복잡할 미지의 함수 $f$를 쭈욱 뻗은 일직선인 선형 함수로 쉽게 어림잡아(근사) 치환해 버릴 수 있다고 한다면, 우주의 법칙은 다음과 같이 아주 단순한 형태로 다시 풀어쓸 수 있게 됩니다.

$$
Y = \beta_0 + \beta_1 X + \epsilon \quad (3.5)
$$

Here $\beta_0$ is the intercept term—that is, the expected value of $Y$ when $X = 0$, and $\beta_1$ is the slope—the average increase in $Y$ associated with a one-unit increase in $X$.
위 공식 3.5에서 $\beta_0$는 절편, 그러니까 $X$에 아무런 짓도 안 했을 때(예: 광고비가 0원일 때) 기본적으로 팔릴 거라고 기대되는 바닥 매출 선상입니다. 그리고 $\beta_1$은 기울기인데, 현실 말로 바꾸어 말하면 $X$ 변수가 1칸 움직일 때마다 $Y$가 평균적으로 얼마나 폴짝 뛰면서 변하는지를 보여주는 체력 수치입니다.

The error term is a catch-all for what we miss with this simple model: the true relationship is probably not linear, there may be other variables that cause variation in $Y$, and there may be measurement error.
공식 꼬리표에 붙은 이 얄미운 오차항($\epsilon$)은 사실상 우리 모델 수식의 **쓰레기통**과 같습니다. 현실 세계가 완벽한 직선일리도 만무하고, 우리가 모르는 숨은 변수들이 장난을 쳤거나 관측할 때 자를 잘못 대서 생긴 불량 실수 등 온갖 놓친 구멍들이 잡탕처럼 쓸어 담겨 있는 마법 상자죠.

We typically assume that the error term is independent of $X$.
분석할 때 우리는 보통 이 오차 덩어리들이 $X$값 자체와는 아무런 관련이 없이 그냥 눈 감고 주사위 던지듯 자기 맘대로 움직이는 독립적인 녀석이라고 멋대로 편리한 룰을 깔아놓고 시작합니다.

**==> picture [284 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 6 7 8 9 β 0 β 1<br>β 0<br> 2.2<br> 2.3<br> 2.15<br> 2.5<br> 2.5<br> 2.11<br> 3<br> 3<br>RSS<br>0.06<br>β 1 0.05<br>0.04<br>0.03<br>**----- End of picture text -----**<br>

**FIGURE 3.2.** _Contour and three-dimensional plots of the RSS on the_ `Advertising` _data, using_ `sales` _as the response and_ `TV` _as the predictor. The red dots correspond to the least squares estimates $\hat{\beta}_0$ and $\hat{\beta}_1$, given by (3.4)._
**그림 3.2.** `Advertising` 예제 데이터에서 `TV` 광고비를 원인으로, `sales(매출)`를 결과로 삼고 수만 번 계산해 낸 오차 쓰레기통(RSS)의 크기를 등고선 지도와 3D 산맥 모형으로 그려놓은 도표입니다. 가장 밑바닥 계곡에 꽂힌 붉은 점들이 바로 방금 전 (3.4) 공식이 찾아낸 '우승자' 위치, 최소 제곱 추정치 콤보 $\hat{\beta}_0$와 $\hat{\beta}_1$의 위치입니다.

The model given by (3.5) defines the _population regression line_, which is the best linear approximation to the true relationship between $X$ and $Y$.$^1$
저 위에 있는 이상적인 우주 공식 (3.5) 는 _모집단 회귀선(population regression line)_이라는 환상 속의 진짜 선을 정의합니다. 모집단이란 세상 만물 모든 데이터를 뜻하며, 이 선은 불완전한 직선이라는 조건 하에서 신이 $X$와 $Y$ 사이의 관계를 어림잡아 그은 '가장 완벽한 진짜 근사선'입니다.$^1$

The least squares regression coefficient estimates (3.4) characterize the _least squares line_ (3.2).
반면에, 인간이 쥐고 있는 부스러기 데이터를 가지고 힘겹게 미분해서 찾아낸 최소 제곱 공식 (3.4) 추정치 값들은 그냥 인간이 그은 최선의 선, 즉 _최소 제곱선(least squares line)_ 인 (3.2)을 모양 지어 줍니다.

The left-hand panel of Figure 3.3 displays these two lines in a simple simulated example.
자, 그래서 그림 3.3의 왼쪽 칸을 보시면 가상의 시뮬레이션 환경 속에서 방금 말한 이 **'신의 진짜 선'**과 인간이 어설프게 그은 **'최소 제곱선'** 두 줄이 어떻게 어긋나는지가 그려져 있습니다.

We created 100 random $X$s, and generated 100 corresponding $Y$s from the model
우리는 컴퓨터 속에서 주사위를 굴려 100개의 $X$ 점들을 허공에 흩뿌려 만든 다음, 아래 깔아 둔 법칙에서 그에 짝꿍이 되는 100개의 $Y$ 점들을 공장에서 찍어내듯 기계적으로 생성해냈습니다. 

$$
Y = 2 + 3X + \epsilon \quad (3.6)
$$

where $\epsilon$ was generated from a normal distribution with mean zero.
여기서 $\epsilon$은 평균 0을 중심으로 위아래로 그냥 잡음(노이즈)을 조금씩 무작위로 뿌려주는 종 모양(정규) 분무기에서 나왔습니다.

The red line in the left-hand panel of Figure 3.3 displays the _true_ relationship, $f(X) = 2 + 3X$, while the blue line is the least squares estimate based on the observed data.
그림 3.3 왼쪽 편에 빨간 매직으로 쭉 그어진 선은 잡음이 없는 상태의 오리지널 _진짜(true)_ 뼈대인 $f(X) = 2 + 3X$ (신의 선)을 뜻하고, 그 위에 삐딱하게 걸쳐진 촌스러운 파란 선이 바로 잡음 섞인 100개짜리 데이터 부스러기만 보고 억지로 계산해서 그어 놓은 인간의 예측 선(최소 제곱선)입니다.

The true relationship is generally not known for real data, but the least squares line can always be computed using the coefficient estimates given in (3.4).
현실 세계에서 이 영롱한 빨간 선(실제 진짜 관계)은 절대 신비의 장막(신만 앎)에 싸여 있어서 두 눈으로 볼 수가 없습니다. 하지만 파란 최소 제곱선은 방금 배운 마법의 추정 공식 (3.4) 에 손에 든 부스러기 데이터를 쑤셔 넣기만 하면 맨날맨날 찍어낼 수 있는 값싼 양산품이죠.

In other words, in real applications, we have access to a set of observations from which we can compute the least squares line; however, the population regression line is unobserved.
이 말을 실무 상황으로 풀면, 우리는 한 번의 설문조사나 한 회사의 표본 데이터 모음 따위만 가지게 되니 여기서 인간의 파란 선 하나는 뽑아낼 수 있습니다. 그러나 세상 전체 고객을 전부 다 찍어본 '모집단 회귀선'은 감춰져 있어 절대 알 길이 없습니다.

In the right-hand panel of Figure 3.3 we have generated ten different data sets from the model given by (3.6) and plotted the corresponding ten least squares lines.
눈을 돌려 오른쪽 칸을 보시죠. 이 시뮬레이션 환경에서 장난삼아 100개짜리 불량 세트를 10번이나 따로따로 생성해서 찍어내 보고, 각각의 세트에 맞춰서 10번이나 최소 제곱선을 열심히 공들여 다시 그어보았습니다. 

Notice that different data sets generated from the same true model result in slightly different least squares lines, but the unobserved population regression line does not change.
이상하게도 원래의 근본 뿌리인 '우주 공식(신의 모델)'은 분명 동일한데도 불구하고, 우연히 조금씩 다르게 흩뿌려진 데이터 세트 때문에 이 최소 제곱선 10개는 전부 제멋대로 아주 살짝씩 다 다른 갈래를 향해 삐뚤어지는 것을 보실 수 있습니다. 하지만 당연하게도 밑밥에 깔려 있는 보이지 않는 절대 진리 '빨간 선' 하나는 꿈쩍도 안 하고 늘 그 자리에 있습니다.

At first glance, the difference between the population regression line and the least squares line may seem subtle and confusing.
처음 이걸 보면, 모집단의 진짜 선(빨간 선)과 우리가 대충 추정한 제곱선(파란 선)이 구분이 안 가서 뭐가 뭔지 아리송하고 머릿속이 약간 버퍼링에 걸릴 수 있습니다.

We only have one data set, and so what does it mean that two different lines describe the relationship between the predictor and the response?
현실에선 우리 손에 종이는 달랑 한 장뿐이고 데이터도 딱 한 무더기뿐인데, 대체 원인과 결과를 설명할 때 '진짜 선'과 '가짜 선' 두 개가 허공을 맴돈다는 게 무슨 귀신 씨나락 까먹는 소리일까요?

Fundamentally, the concept of these two lines is a natural extension of the standard statistical approach of using information from a sample to estimate characteristics of a large population.
솔직히 아주 근본적으로 따지면, 이 애매모호한 '두 개의 선' 딜레마는 여러분이 고등학교 때 배웠던 기본적인 통계 마인드, 즉 **'한 줌의 표본을 가지고 거대한 전체 모양새를 때려 맞춰본다'**는 철학의 아이디어를 그냥 선(직선)의 형태로 자연스레 확장해 놓은 연장선일 뿐입니다.

For example, suppose that we are interested in knowing
아주 쉬운 비유를 위해, 우리가 어떤 동네 학교 학생들의 비밀이 하나 궁금해졌다고 상상해 보세요. 

> 1The assumption of linearity is often a useful working model.
> 1참고로, 선 모양으로 어설프게 생겼다 치는 '선형성' 가정은 실무 바닥에서 일을 굴러가게 만들어주는 쏠쏠한 편법 모델입니다.

> However, despite what many textbooks might tell us, we seldom believe that the true relationship is linear.
> 하지만 수많은 거짓부렁(?) 교과서들이 여러분의 귀에 속삭이더라도, 우리 통계학자들 치고 현실 세상의 진짜 본연의 모습이 자를 댄 것처럼 똑바른 직선이리라 진심으로 믿는 사람은 한 명도 없습니다. 현실은 꼬여있으니까요!

**==> picture [315 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
−2 −1 0 1 2 −2 −1 0 1 2<br>X X<br>10 10<br>5 5<br>Y Y<br>0 0<br>−5 −5<br>−10 −10<br>**----- End of picture text -----**<br>

**FIGURE 3.3.** _A simulated data set._ Left: _The red line represents the true relationship, f(X) = 2 + 3X, which is known as the population regression line. The blue line is the least squares line; it is the least squares estimate for f(X) based on the observed data, shown in black._ Right: _The population regression line is again shown in red, and the least squares line in dark blue. In light blue, ten least squares lines are shown, each computed on the basis of a separate random set of observations. Each least squares line is different, but on average, the least squares lines are quite close to the population regression line._
**그림 3.3.** _놀이공원 시뮬레이션._ **[왼쪽 그림]**: _빨간 선 고속도로는 하늘의 법칙 $f(X) = 2 + 3X$ 이며 모집단 회귀선으로 군림합니다. 파란 선 좁은 길은 최소 제곱선입니다; 검은 점으로 콕콕 떨어져 있는 관측 데이터를 보고 인간이 열심히 $f(X)$를 향해 손도끼질하며 유추해 낸 추정치이죠._ **[오른쪽 그림]**: _모집단 기준선이 빨간색으로 당당히 서있고, 인간의 파란 선이 진하게 칠해져 있습니다. 한편 주변에 파스텔톤 파란 선 10개가 띠를 이루고 있는데, 이건 인간이 각기 다른 랜덤 표본 10개를 가져다가 10번 도전해 본 흔적입니다. 매번 선은 삐딱하게 틀어지지만, 눈을 가늘게 뜨고 이 10번의 도전을 다 합쳐 **평균**을 내어 상상해 보면 기가 막히게도 모집단의 진짜 붉은 선에 아주 일치하게 겹치는 놀라운 광경을 볼 수 있습니다._

the population mean $\mu$ of some random variable $Y$.
(앞서 학생 비밀로 돌아와서) 궁금해진 비밀은 바로 확률 변수 $Y$의 진짜 전국 찐 평균 $\mu$ (뮤)입니다. 이를테면 전국 7성급 호텔 요리사의 연봉 평균이라고 해보죠.

Unfortunately, $\mu$ is unknown, but we do have access to $n$ observations from $Y$, $y_1, \dots, y_n$, which we can use to estimate $\mu$.
안타깝게도 전수조사를 못하니 진짜 평균 $\mu$는 며느리도 모릅니다. 하지만 다행스럽게도 우리 수첩에는 우연히 만난 $n$명의 요리사 연봉 샘플 관측치 기록인 $y_1, \dots, y_n$ 가 적혀 있습니다. 우리는 이 얄팍한 단서 조각을 모아 진짜를 유추($\mu$ 추정)해야 합니다.

A reasonable estimate is $\hat{\mu} = \bar{y}$, where $\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$ is the sample mean.
가장 그럴싸하고 당연한 접근법은 내가 만난 이 사람들의 연봉을 싹 다 더해서 머릿수만큼 나눈 표본 집단의 평균($\bar{y}$)을 구한 뒤, "이 $\bar{y}$ 가 전국 평균 $\hat{\mu}$ 일 것이다!" 라고 우기는 추정법을 채택하는 것입니다.

The sample mean and the population mean are different, but in general the sample mean will provide a good estimate of the population mean.
당연히 내가 뽑아온 찌끄레기들 평균(표본 평균)과 진짜 전국 짱 평균(모집단 평균)은 수치가 엇나갈 겁니다. 하지만 기묘하게도, 표본 평균이라는 녀석은 일반적으로 꽤 듬직하게 모집단의 평균을 짚어내는 훌륭한 길잡이(추정치) 역할을 해냅니다.

In the same way, the unknown coefficients $\beta_0$ and $\beta_1$ in linear regression define the population regression line.
**선형 회귀선 놀이도 이 연봉 맞추기 장난과 원리가 판박이입니다.** 선형 회귀에서 도무지 알 수 없는 진짜 진리 계수 $\beta_0$(기울기 척도)와 $\beta_1$(시작점)은 전국 모집단의 완벽한 참 회귀고속도로를 형성합니다.

We seek to estimate these unknown coefficients using $\hat{\beta}_0$ and $\hat{\beta}_1$ given in (3.4).
우리는 불과 몇 줌의 점들을 가지고 얻어낸 (3.4) 짝퉁 공식표를 이용해, 우리가 추정한 $\hat{\beta}_0$와 $\hat{\beta}_1$ 값들로 이 우주의 진리 숫자들을 용감하게 때려 맞춰 보려는 도전을 하는 것입니다.

These coefficient estimates define the least squares line.
이 과정에서 얻어낸 모자 쓴 숫자들이 바로 우리가 아등바등 그려낸 최소 제곱선을 이루게 되고요.

The analogy between linear regression and estimation of the mean of a random variable is an apt one based on the concept of _bias_.
직선 긋기 놀이(회귀)와 단순하게 사람 연봉 짚어막는 산수(평균 산출) 사이의 이 신기방기한 평행 이론 비유는 통계학의 영원한 화두인 **_편향(Bias)_**, 일명 '총알군집의 엇나감'이라는 마인드를 놓고 보았을 때 소름 돋게 아주 똑떨어지는 상황 찰떡 비유입니다. 

If we use the sample mean $\hat{\mu}$ to estimate $\mu$, this estimate is _unbiased_, in the sense that on average, we expect $\hat{\mu}$ to equal $\mu$.
만일 진짜 평균 $\mu$를 때려 맞추기 위해 짝퉁 표본 평균 $\hat{\mu}$를 내미는 꼼수를 쓴다면, 사실 이 추정 기법은 **_불편향성(unbiased)_**이라는 황금 등껍질을 가지고 있습니다. 왜냐하면, "만약 내가 이 짓거리를 무한 번 계속 표본을 덜어서 찍고 또 찍는다면, 그 무한대의 평균 기록들은 결국 짠짜잔 하고 진짜 $\mu$에 완벽히 일치할 것이다"라는 기가 막힌 통계학적 증명이 기저에 기대고 있기 때문입니다.

What exactly does this mean?
잠깐만요, '무한정 많이 하면 맞는다' 이게 도대체 실생활에서 무슨 뚱딴지같은 궤변 인가요? 

It means that on the basis of one particular set of observations $y_1, \dots, y_n$, $\hat{\mu}$ might overestimate $\mu$, and on the basis of another set of observations, $\hat{\mu}$ might underestimate $\mu$.
쉽게 풀자면 이렇습니다. 내가 우연히 오늘 뽑아 모은 A그룹 사람들의 통계($y_1, \dots, y_n$)만을 기준으로 잡으면, $\hat{\mu}$ 값은 운 좋게 부자들만 걸려서 전국 평균을 말도 안 되게 올려 치기(과대평가)할 수도 있습니다. 반면 내일 눈 감고 B그룹을 또 뽑으면 웬걸 거지들만 걸려서 이번엔 어젠다를 왕창 아래로 후려 칠(과소평가) 수도 있다는 뜻입니다. 

But if we could average a huge number of estimates of $\mu$ obtained from a huge number of sets of observations, then this average would _exactly_ equal $\mu$.
하지만 신의 능력을 얻어 이런 오합지졸 그룹들을 한 천만 번쯤 랜덤 생성해내고, 거기서 나온 천만 개의 들쭉날쭉한 $\mu$ 추정 결과표들을 전부 모아서 큰 솥에 끓이고 최종 '엄마 평균'을 내본다고 상상해 볼까요? 소름 돋게도 이 엄마 평균은 진짜 우주의 대진리 $\mu$ 수치와 소수점 아래까지 _머리카락 한 올 안 틀리고 아주 정확하게 똑같이_ 겹쳐지게 됩니다.

Hence, an unbiased estimator does not _systematically_ over- or under-estimate the true parameter.
이것이 의미하는 바는 엄청납니다! 편견이 없는(불편향적인) 이 훌륭한 계산 도구는 고의적으로 짜고서 진동수를 치우치게 하여 진짜 파라미터를 _기계적으로(systematically)_ 펌핑(과대 포장)하거나 깎아내리지 않는 청렴결백한 속성을 가졌다는 뜻이죠.

The property of unbiasedness holds for the least squares coefficient estimates given by (3.4) as well: if we estimate $\beta_0$ and $\beta_1$ on the basis of a particular data set, then our estimates won’t be exactly equal to $\beta_0$ and $\beta_1$.
이 자랑스러운 청렴결백(불편향의 속성)훈장은, 앞의 (3.4) 공식이 뱉어낸 우리의 회귀선 계수 추정치들에게도 그대로 계승되어 반짝입니다. 물론 내가 달랑 한 상자뿐인 특정 데이터들만 버무려 구한 $\hat{\beta}_0$와 $\hat{\beta}_1$는 우주의 정답표에 적힌 $\beta_0$, $\beta_1$과 절대로 완벽히 일치할 리는 없습니다.

But if we could average the estimates obtained over a huge number of data sets, then the average of these estimates would be spot on!
하지만 만일 내가 게임 던전을 리셋하듯 끝없이 방대한 평행우주 데이터 조각들을 모으고, 거기서 매번 새로 자를 댄 추정치들의 괘적을 전부 뭉쳐서 그 거대한 산맥들의 평균치를 내본다면, 그 정중앙을 꿰뚫는 평균선은 허를 찌를 만큼 정답에 기가 막히게 과녁(Spot on)을 명중시킬 거라는 뜻입니다!

In fact, we can see from the righthand panel of Figure 3.3 that the average of many least squares lines, each estimated from a separate data set, is pretty close to the true population regression line.
정말 그러냐고요? 아까 버퍼링왔던 그림 3.3의 오른쪽 패널 상황으로 다시 돌아가 보죠. 서로 다른 여러 데이터 상자에서 따로따로 구멍 파듯 구한 얄팍한 오합지졸 파란 최소 제곱선들을 10개만 대충 눈대중으로 한 데 합쳐서 평균선을 어림잡아 그어봐도 그 기세가 신이 그은 진짜 모집단 회귀선(빨간 선) 기차 궤도와 놀랍도록 딱 달라붙어 있음을 직관적으로 알 수 있습니다.

We continue the analogy with the estimation of the population mean $\mu$ of a random variable $Y$.
평행이론에 뽕이 찼으니 무작위 변수 $Y$ 의 모집단 전국 평균 $\mu$ 를 때려 맞췄던 연봉 맞추기 예시를 질척거리며 좀 더 이어나가 봅시다.

A natural question is as follows: how accurate is the sample mean $\hat{\mu}$ as an estimate of $\mu$?
이제 논리 회로상 이런 의문표가 번쩍 듭니다: **"좋아 무한번 하면 맞는다 치자. 근데 나한테 기회비용은 한 번이잖아? 대체 이 하나의 $\hat{\mu}$ (표본 평균) 총알은 진짜 평균 과녁 $\mu$ 에서부터 대강 얼마나 정확히 맞는 스나이퍼 총기인가?"**

We have established that the average of $\hat{\mu}$'s over many data sets will be very close to $\mu$, but that a single estimate $\hat{\mu}$ may be a substantial underestimate or overestimate of $\mu$.
백만 스물 한 번의 총알들(여러 집단 평균)을 모아 그린 무지개 잔상 평균 궤적이 정답 마커인 $\mu$와 찰떡같이 맞아떨어지리란 건 방금 침 튀기며 증명했습니다. 그러나 내가 단 한 사로에서 발사한 '재수 없는 단일 총알 하나'인 $\hat{\mu}$의 경우엔 본성 $\mu$로부터 저 윗동네로 오버슈팅해버릴지, 바닥에 꼬라박을지 모릅니다. 단 건방진 편차가 속출할 수 있는 위험은 깔려 있습니다.

How far off will that single estimate of $\hat{\mu}$ be?
이 하나의 표본에서 발사된 내 단발성 추정 총알 $\hat{\mu}$은 도대체 영점 촛대에서 얼마만큼이나 저 안드로메다로 빗나갈 소지가 도사리고 있을까요? 

In general, we answer this question by computing the _standard error_ of $\hat{\mu}$, written as $\text{SE}(\hat{\mu})$.
통계 사냥꾼들은 요런 떨떠름한 질문표 딱지가 뜰 때, $\text{SE}(\hat{\mu})$ 이라는 멋진 기호인 $\hat{\mu}$의 **_표준 오차(standard error)_**라는 마법의 흔들림 측정기를 계산해 당당히 책상 위로 패를 까버립니다.

We have the well-known formula:
여기 구구단처럼 뻔질나게 외워대서 통계학도 사이엔 전설이 된 공식법전이 하나 있습니다:

$$
\text{Var}(\hat{\mu}) = \text{SE}(\hat{\mu})^2 = \frac{\sigma^2}{n} \quad (3.7)
$$

where $\sigma$ is the standard deviation of each of the realizations $y_i$ of $Y$.$^2$
저 공식 암호문에 있는 $\sigma$는 우주를 날뛰는 $y_i$ 조각 친구들 개개인이 본능적으로 가지고 태어난 널뛰기 진동폭, 즉 기본 맷집(표준 편차)을 말합니다.$^2$

Roughly speaking, the standard error tells us the average amount that this estimate $\hat{\mu}$ differs from the actual value of $\mu$.
골치 아픈 기호를 치워두고 말하면, 이 요주의 **표준 오차** 단위는 내가 우격다짐으로 찍은 가짜 추정치 $\hat{\mu}$ 가 진짜 숨겨진 국보 $\mu$ 의 궤적에서 평균적으로 대략 얼마쯤이나 헛발질하며 동떨어져 날리치는지의 '실제 평균 빗겨남 면적(amount)'을 한큐에 보여주는 나침반입니다.

Equation 3.7 also tells us how this deviation shrinks with $n$—the more observations we have, the smaller the standard error of $\hat{\mu}$.
방금 본 3.7 수식을 지그시 파보시면, 저 밑도 끝도 없는 오차 헛발질의 위협이 공식 밑천 분모에 있는 $n$(병력 쪽수)이 늘어날 때마다 기적처럼 사르르 축소되고 짓눌러지는 기가 막힌 메커니즘을 볼 수 있습니다 — **결론은 뭐다? 총알을 많이 쏠수록(관측치 $n$을 미친 듯이 늘려 많이 쟁여둘수록), 우리의 $\hat{\mu}$에 도사린 불확실한 그늘, 즉 표준 오차는 콩알만 해진다는 소리입니다.** 

In a similar vein, we can wonder how close $\hat{\beta}_0$ and $\hat{\beta}_1$ are to the true values $\beta_0$ and $\beta_1$.
이 마인드 맵을 그대로 선형 회귀에 투영시켜 봅니다. 이제 우리는 내가 꼼지락꼼지락 컴퓨터 돌려 뽑아낸 계수(기울기/절편) $\hat{\beta}_0$랑 야생마 $\hat{\beta}_1$ 숫자가 과연 하늘에서 정해준 운명의 진리 계수 $\beta_0$, $\beta_1$와 얼마나 부비부비할 만큼 꼭 맞아떨어져 있는지 가히 똥줄 타게 궁금해질 노릇입니다.

To compute the standard errors associated with $\hat{\beta}_0$ and $\hat{\beta}_1$, we use the following formulas:
이 가짜 $\hat{\beta}_0$와 가짜 $\hat{\beta}_1$들의 목덜미에 들러붙은 의심 암초, 즉 "얘들이 대략 얼마나 헛구름을 잡고 있을까?" 를 계산기 두드려 내기 위해서, 우린 앞서 본 둥근 마법을 약간 비튼 다음과 같이 험악하게 생긴 괴팍한 공식 자물쇠를 부숴야 합니다: 

$$
\text{SE}(\hat{\beta}_0)^2 = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right], \quad \text{SE}(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \quad (3.8)
$$

where $\sigma^2 = \text{Var}(\epsilon)$.
(위 거대한 암호 판에서 조미료로 쓰인 $\sigma^2$는 우리의 오차 잡탕 $\epsilon$ 이 보여주는 분산(변화량 파동) $\text{Var}(\epsilon)$을 뜻합니다.)

For these formulas to be strictly valid, we need to assume that the errors $\epsilon_i$ for each observation have common variance $\sigma^2$ and are uncorrelated.
사실 이 험악한 계산식 자판기가 뻑 안 나고 온전하게 작동되려면 눈 가리고 아웅하는 전설 같은 조건을 깔아야 합니다. 이 점 무리들에서 떨어져 나온 불량 요정($\epsilon_i$) 녀석들이 전부 하나같이 똑같은 크기의 난장판 폭($\sigma^2$)을 가지고 있어야 하며, 쟤가 튄다고 얘가 덩달아 튀는 불순한 서로 간 결탁이나 상관관계가 일절 1도 안 묻어나게 무균 상태여야 한다는 전제 말입니다.

This is clearly not true in Figure 3.1, but the formula still turns out to be a good approximation.
물론 아까 앞에서 본 그림 3.1 데이터를 눈 뜨고 꼬막만 하게 관찰해보면 이런 순진무구한 청정 에러 가정판이 '백퍼 구라'라는 건 들통이 납니다. 허나 통계학의 오묘함이여, 이런 말도 안 되는 억지 조건판에서 돌아간 공식 부스러기들조차 실제 현장에 들이박아보면 꽤나 훌륭한 수준으로 정답의 뒤꿈치를 쫓아가는 근사치 결과를 기똥차게 뱉어 냅니다. 

Notice in the formula that $\text{SE}(\hat{\beta}_1)$ is smaller when the $x_i$ are more spread out; intuitively we have more _leverage_ to estimate a slope when this is the case.
여기서 복잡한 우측 공식을 한 템포 가만히 노려보세요! 밑에 깔린 $x_i$ (원인 점) 점들이 가운데 뭉쳐있지 않고 양옆으로 넓게 와이드하게 확확 스케일 좋게 퍼져있을 때 분모가 뻥튀기되면서, 결국 두려운 오차 괴물인 $\text{SE}(\hat{\beta}_1)$ 의 크기가 홀쭉하게 쪼그라드는 마법을 볼 수 있습니다; 이것은 직관적으로 비유하자면 양팔이 긴 막대(멀리 퍼진 데이터)를 잡았을 때 훨씬 더 단단한 **_지렛대 위력(leverage)_**을 얻어 모종의 널뛰는 기울기 각도를 쉽게 고정시켜 어림잡기 편한 원리입니다! 

We also see that $\text{SE}(\hat{\beta}_0)$ would be the same as $\text{SE}(\hat{\mu})$ if $\bar{x}$ were zero (in which case $\hat{\beta}_0$ would be equal to $\bar{y}$).
또한, 만약에 $x$점들의 평균값인 $\bar{x}$ 가 어쩌다 운 좋게 그냥 0 이었다면, 좌측의 거대한 수식 덩리가 훅 날아가면서 어설픈 $\text{SE}(\hat{\beta}_0)$ 오차값이 아까 우리가 봤던 연봉 맞추기 표준 오차인 $\text{SE}(\hat{\mu})$ 값과 복붙한 것처럼 일치하게 됨을 알 수 있습니다. (사실 그 특수 케이스에선 $\hat{\beta}_0$ 가 그냥 $\bar{y}$ 랑 같아져 버리는 아주 우스운 상황이 되거든요).

In general, $\sigma^2$ is not known, but can be estimated from the data.
그런데 말입니다... 일반적인 현실 모드에선 그 근본 오차 덩어리 시드인 $\sigma^2$ 자체마저 당연히 도통 신만이 아는 베일에 싸여있는 노릇입니다. 하지만 불행 중 다행으로, 이 역시 쥐고 있는 데이터 부스러기에서 추정해서 엮어 낼 수 있습니다.

This estimate of $\sigma$ is known as the _residual standard error_, and is given by the formula $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$.
데이터로 꾸덕하게 짜내 추정한 이 은밀한 짝퉁 $\sigma$ 는 이름하여 **_잔차 표준 오차(RSE, residual standard error)_**라는 휘황찬란한 타이틀을 달고, $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$ 이라는 연금술 공식으로 제조되어 우리에게 하사됩니다. 

Strictly speaking, when $\sigma^2$ is estimated from the data we should write $\widehat{\text{SE}}(\hat{\beta}_1)$ to indicate that an estimate has been made, but for simplicity of notation we will drop this extra “hat”.
꼬장꼬장하고 피곤하게 따지자면, $\sigma^2$이 진짜가 아니라 어디까지나 데이터 쪼가리에서 쥐어 짜낸 가짜 짝퉁 추정기록물일 경우엔, 우리 양심껏 우리가 "이건 내가 대충 어림잡아 만들어낸 추정값임!" 이라고 당당히 팻말을 걸기 위해 $\widehat{\text{SE}}(\hat{\beta}_1)$ 라고 꼬깔모자를 하나 더 머리에 얹어서 써주는 것이 학계 룰입니다. 허나 그런 표기 노가다는 우릴 지치게 하므로 기호 편의성 꼼수를 위해 위 꼬깔장식 '햇(hat)' 모형은 깔끔하게 치워버리고 퉁치려 합니다.

That is, there is approximately a 95% chance that the interval
자, 방금 전 표준 오차들의 범위를 구했다는 건 즉슨, 다음과 같이 덫을 놓아 친 포획 구간망 안에... 

$$
\left[ \hat{\beta}_1 - 2 \cdot \text{SE}(\hat{\beta}_1), \, \hat{\beta}_1 + 2 \cdot \text{SE}(\hat{\beta}_1) \right] \quad (3.10)
$$

will contain the true value of $\beta_1$.$^3$
이 기계적으로 구한 (추정치 숫자 - 오차 2배) 에서 (추정치 숫자 + 오차 2배) 사이라는 거대한 투망 안쪽에 **신의 진짜 숫자인 $\beta_1$ 이 빼박캔트 도망 못 가고 꼼짝없이 포획되어 있을 확률**이 무려 도합 95% 정도 되는 엄청난 투망 바운더리를 쳤다고 주장할 수 있게 됩니다.$^3$ 

Similarly, a confidence interval for $\beta_0$ approximately takes the form
똑같은 논리 복붙으로 시작 단추 지표인 $\beta_0$ 에 대해서도, 이렇게 양옆으로 넓게 오차범위를 벌린 이른바 _신뢰 구간(confidence interval)_ 투망을 대략 요런 형태로 씌우면 됩니다.

$$
\hat{\beta}_0 \pm 2 \cdot \text{SE}(\hat{\beta}_0) \quad (3.11)
$$

In the case of the advertising data, the 95% confidence interval for $\beta_0$ is $[6.130, 7.935]$ and the 95% confidence interval for $\beta_1$ is $[0.042, 0.053]$.
백문이 불여일타! 광고 예제 데이터의 치수들을 저 포획망 투망 공식에다 탈탈 엮어 넣어 보십쇼. 시작점 $\beta_0$ 에 쳐진 95% 확률 신뢰 구간 투망의 양 끝단은 6.130에서 7.935 사이에 위치하게 되며, 기울기 $\beta_1$ 투망망은 딱 0.042에서 0.053 요 길목 초크포인트 사이로 그 위상이 잡히게 됩니다. 

Therefore, we can conclude that in the absence of any advertising, sales will, on average, fall somewhere between 6,130 and 7,935 units.
결론적으로 사장님께 가동 보고를 칠 때 이렇게 당당하게 썰을 풀 수 있죠. "회장님! 우리 광고 예산 0원 처리해도, 내기할 확률 95퍼로 우리 평균 베이스 매출 단가 포지션은 분명 6,130개와 7,935개 요 박스 바운더리 어딘가로 나자빠져 안착하게 될 소상임다!"

Furthermore, for each $\$1,000$ increase in television advertising, there will be an average increase in sales of between 42 and 53 units.
나아가 회장님 투자 심리 부추기기로, "바보상자 텔레비전에 1,000달러치 한 장 더 태우게 될 때마다 평균적으로 우리 물건 매출은 못해도 42개에서 잭팟으론 53개 사이 범위 안에서 폴짝폴짝 뛰어 연쇄 증가할 확률이 너무나 자명합니다!"

Standard errors can also be used to perform _hypothesis tests_ on the coefficients.
사실 이 깐깐한 표준 오차 수치는, 이렇게 바운더리를 치며 확신을 얻는 용도를 뛰어넘어, 계수 놈들을 법정에 세우고 진짜 가짜를 판별하는 **_가설 검정법(hypothesis tests)_** 심판의 도구로써 기똥차게 마개조되어 사용될 수도 있습니다.

The most common hypothesis test involves testing the _null hypothesis_ of
이 법정 공방전에서 가장 대중적으로 물고 뜯고 시비를 거는 테스트는 바로 방어자인 **_귀무가설(null hypothesis, $H_0$)_**을 샌드백 삼아 털어내는 일입니다. 귀무가설의 소장 내용은 이렇습니다.

$$
H_0 : \beta_1 = 0 \quad (3.12)
$$

versus the _alternative hypothesis_
이에 맞서 공격수 검찰 측인 **_대립가설(alternative hypothesis, $H_a$)_**은 불꽃 튀며 판사에게 다음 소장을 들이밉니다.

$$
H_a : \beta_1 \neq 0 \quad (3.13)
$$

Mathematically, this corresponds to testing
수학 놀음판 위에서, 이 피 터지는 법정 공박은 결국 요 따위 소리를 놓고 치고 박는 것과 정확히 일맥상통합니다.

$$
H_0 : \text{There is no relationship between } X \text{ and } Y \text{ (X랑 Y는 생판 남남이고 아무런 썸도 없다!)}
$$

versus
거기에 맞서는 자는:

$$
H_a : \text{There is some relationship between } X \text{ and } Y \text{ (야! X랑 Y 사이엔 분명 야릇한 모종의 연관관계 썸이 있다!)}
$$

since if $\beta_1 = 0$ then the model (3.5) reduces to $Y = \beta_0 + \epsilon$, and $X$ is not associated with $Y$.
왜 이게 이 꼴이냐면, 만일 방어 측 귀무가설의 말대로 기울기 $\beta_1$이 0이라면, 저 거창했던 (3.5) 모델 방정식이 그냥 $Y = \beta_0 + \epsilon$ 라는 바보 같은 상수항 조각난 쓰레기 공식으로 녹아버리고 찌그러져 축소되기 때문에, 결과적으로 $X$ 요소 나부랭이가 $Y$ 의 인생 전개에 하등 1도 연관을 간섭하지 못하게 되기 때문이죠.

To test the null hypothesis, we need to determine whether $\hat{\beta}_1$, our estimate for $\beta_1$, is sufficiently far from zero that we can be confident that $\beta_1$ is non-zero.
그래서 우리의 귀무가설($X$가 소용없다)을 부숴버리고 유죄 판결을 내리려면, 우리가 계산기 두드려 우겨넣은 추정치 $\hat{\beta}_1$ 숫자가 "아! 이건 우연이라 보기엔 0에서 비정상적일 정도로 너무 심하게 영끌로 멀리 떨어져 도망친 자리잖아!" 라는 판사의 빼박캔트 심증을 얻어내, 진짜 $\beta_1$ 도 0 일리가 전무하다고 확신 도장을 찍어 눌러야만 합니다. 

How far is far enough?
그렇다면 판사님, 숫자가 도대체 0에서부터 얼마나 하늘을 뚫고 멀리 도망가 있어야 귀무가설을 박살 낼 만큼 아득히 "충분하게" 멀리 떨어져 있다고 감히 납득할 수 있단 말입니까? 

This of course depends on the accuracy of $\hat{\beta}_1$—that is, it depends on $\text{SE}(\hat{\beta}_1)$.
당연히 그 심판의 척도는 전적으로 $\hat{\beta}_1$ 숫자의 견고함과 뚝심, 즉 아까 구했던 그 징그러운 오차 흔들림폭 $\text{SE}(\hat{\beta}_1)$ 사이즈가 어떠냐에 좌지우지 멱살 잡혀 있습니다.

If $\text{SE}(\hat{\beta}_1)$ is small, then even relatively small values of $\hat{\beta}_1$ may provide strong evidence that $\beta_1 \neq 0$, and hence that there is a relationship between $X$ and $Y$.
가령 우리 데이터의 뚝심인 **표준 오차 $\text{SE}(\hat{\beta}_1)$가 새우깡처럼 타이트하게 쥐방울만 한 사이즈**라면 어떨까요? 이 경우 우리의 타겟 $\hat{\beta}_1$숫자가 비록 도토리 키재기마냥 상대적 작게 0을 벗어났더라도, 판사는 "이건 오차 위글룸(흔들림)도 없는데 이 숫자가 나왔다고?! 그럼 $\beta_1 \neq 0$인 게 법적으로 명백하다!"라며 빼박 스모킹건 확증 판정을 내리고 $X$와 $Y$ 사이의 내통 동거 결탁(관계성)을 재판 종결 선포해 버릴 겁니다. 

In contrast, if $\text{SE}(\hat{\beta}_1)$ is large, then $\hat{\beta}_1$ must be large in absolute value in order for us to reject the null hypothesis.
이와 정반대로 만약 우리 관측 폭인 **오차 덩어리 $\text{SE}(\hat{\beta}_1)$가 한강 둔치처럼 으리으리하게 태평양급 물렁뼈 폭**을 자랑한다면, 이건 우연히 $\hat{\beta}_1$가 튀어도 단순 헤프닝 오작동일 수 있습니다. 판사가 귀무가설을 깨부수고 기각시켜버리려면, 어지간히 이 $\hat{\beta}_1$ 수치값이 절대치 관점으로 눈 튀어나오게 압도적으로 거대하지 않으면 말짱 도루묵이 되는 것이죠. 

In practice, we compute a _$t$-statistic_, given by
이런 감정싸움을 현실계에서 판사는 무척 싫어하므로, 객관적인 사법 판결 지표 스코어인 **_$t$-통계량($t$-statistic)_** 이라는 심판관 넘버를 전광판에 계산해 띄워 올립니다. 공식은 이렇죠.

$$
t = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{\beta}_1)} \quad (3.14)
$$

> $^3$ _Approximately_ for several reasons.
> $^3$ 덧붙여 아까 95% 투망 구간을 칠 때 제가 양심상 **'대략적으로(Approximately)'**라고 밑장 빼기 방패 단서를 깐 건 몇 가지 복잡한 이유 때문입니다.

> Equation 3.10 relies on the assumption that the errors are Gaussian.
> 우선 구간 수식 망통(3.10)은, 저 쓰레기 오차 $\epsilon$ 찌끄레기들이 신이 내린 예쁜 종 모양(가우시안 정규 분포)의 패턴을 띠며 착하게 구른다는 걸 덥석 믿고 배 짼 전제이거든요.

> Also, the factor of 2 in front of the $\text{SE}(\hat{\beta}_1)$ term will vary slightly depending on the number of observations $n$ in the linear regression.
> 설상가상으로 $\text{SE}(\hat{\beta}_1)$ 덩어리 항 앞에 곱해버린 '2배수' 곱하기 요소인 저 숫자 '2'는, 우리가 긁어모은 총 데이터 $n$ 병력 머리 수에 따라 아주 미세한 변덕을 부리며 고무줄처럼 변위 널뛰기를 띄게 됩니다.

> To be precise, rather than the number 2, (3.10) should contain the 97.5% quantile of a $t$-distribution with $n-2$ degrees of freedom.
> 기왕 피곤하게 통계학자 빙의해서 정확히 말해보자면 저 다 때려 부수는 양면 거울 곱하기 숫자 '2' 대타로, 사실은 자유도가 $n-2$ 라는 거치적거리는 조건이 박힌 $t$-분포 모델상의 상위 '97.5% 분위수 스코어 넘버'를 핀셋으로 집어와서 심어야 완벽한 진리에 수렴하게 됩니다.

> Details of how to compute the 95% confidence interval precisely in `R` will be provided later in this chapter.
> 아무튼 나중에 머리 굵어지면, 이 장의 후반부에서 마법 지팡이인 `R` 프로그래밍 언어의 주문 코드로 95% 신뢰 방어 투망 라인을 컴퓨터가 0.0001초 만에 아주아주 정교하게 산출 도출해 내 바치는 세부 스킬 과정을 알려 드릴 예정입니다.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 7.0325 | 0.4578 | 15.36 | $< 0.0001$ |
| `TV` | 0.0475 | 0.0027 | 17.67 | $< 0.0001$ |

**TABLE 3.1.** _For the_ `Advertising` _data, coefficients of the least squares model for the regression of number of units sold on TV advertising budget. An increase of_ $\$1,000$ _in the TV advertising budget is associated with an increase in sales by around 50 units. (Recall that the_ `sales` _variable is in thousands of units, and the_ `TV` _variable is in thousands of dollars.)_
**표 3.1.** 이 전광판은 `Advertising` 예제 데이터를 가지고 TV 광고 예산이라는 장작을 태워 제품 판매량 유닛 성적이라는 회귀 불꽃을 일으켰을 때 뽑힌, 피도 눈물도 없는 '최소 제곱 모델 재판부 최종 판결문' 숫자들이 계수별로 빼곡히 정리된 성적 도표입니다. TV 광고비를 \$1,000 인상 투여할 때마다 우리의 매출 $Y$ 성적은 대략 50 단위 수준의 상승 점프로 뛰는 우상향 연관성 기록물로 도출됩니다. (절대 까먹지 마실 것은, `sales(매출)` 단위는 기본 수천 개 묶음(thousands) 박스 포장 스케일이고, 투여된 원인 항복 `TV` 예산 자원 숫자 스케일 덩치도 단위 지표가 천 달러 뭉치 베이스 지수 기준이란 명백한 사실을 상기 명심하십시오.)

which measures the number of standard deviations that $\hat{\beta}_1$ is away from 0.
어쨌건 이 (3.14) 방정식이 산출해 내는 위대한 법정 판결 넘버 $t$-통계량 수치는 다름 아니라, 타겟인 $\hat{\beta}_1$ 수량이 "네 본연의 표준 오차 걸음걸이 사이즈를 기준으로 할 때, 숫자 0 바운더리에서부턴 몇 걸음(몇 배)이나 멀찍이 도망쳐 나와 있는 상태냐?" 의 보폭 거리를 직설적으로 파악해 내는 스캐너 줄자입니다.

If there really is no relationship between $X$ and $Y$, then we expect that (3.14) will have a $t$-distribution with $n - 2$ degrees of freedom.
아주 만약에 정말로 방어측 말대로 $X$와 $Y$ 사이 공간엔 썸이라곤 코딱지만큼도 없고 냉랭한 관계 단절뿐이라면(관계가 0 이라면), 우린 필경 (3.14) 수식이 뱉어내는 계산 통계량이 옴짝 달싹 못하고 자유도가 $n - 2$ 인 감옥, 즉 전설의 '$t$-분포'라는 종 모양 분포 테두리 안쪽 법칙을 질량 불변처럼 따를 것이라고 예측할 수 있습니다. 

The $t$-distribution has a bell shape and for values of $n$ greater than approximately 30 it is quite similar to the standard normal distribution.
저 이름도 기묘한 $t$-분포 모양새는 거룩한 종(bell)의 외곽선 커브 자태를 취하고 있으며, 데이터 쪽수인 $n$ 지표가 대략 30을 넘어가며 북적거릴 정도로 스케일이 커지면 얼씨구나 하며 그냥 평범하고 아름다운 표준 정규 분포(가우시안 종)와 사실상 구분이 안 가고 판박이 쌍둥이처럼 똑 닯은 형태를 구축해버립니다.

Consequently, it is a simple matter to compute the probability of observing any number equal to $|t|$ or larger in absolute value, assuming $\beta_1 = 0$.
결론적으로 귀무가설의 말마따나 기울기 $\beta_1 = 0$ 이라는 전장이 실존한다고 치고 베팅했을 때, 통계 재판상 우리 눈앞에 들이 닥친 절대값 $|t|$ 이상의 정신 나간 극단수치가 과연 우연 발생적으로 나타날 확률이 얼마인지 주판을 튕기는 건 사실 아주 개나 소나 할 만큼 우스운 덧셈 단순 확률 계산 공정 문제에 불과해진단 뜻입니다.

We call this probability the _$p$-value_.
우리는 바로 법정서 구한 이 정신 나간 우연 발생 기적의 확률 백분율 지표를, 그 유명한 위대한 판결 마커 **_$p$-값(p-value)_**이라는 멋진 학술 네임타이틀로 거창하게 추앙하여 호명합니다. 

Roughly speaking, we interpret the $p$-value as follows: a small $p$-value indicates that it is unlikely to observe such a substantial association between the predictor and the response due to chance, in the absence of any real association between the predictor and the response.
이 복잡한 $p$-값을 할머니도 알기 쉽게 현실 뒷방 언어로 초월 번역 해석해 드리자면 다음과 같이 풀어집니다: 이 **$p$-값 넘버가 코딱지만 하게 아주 쥐방울같이 작다는 것의 의미**는, 애당초 원인 예측 변수와 반응 결과 변수 사이에 진실된 연관 썸결이 완전 전혀 일도 없었음에도 불구하고 그저 오로지 하늘이 장난친 운빨(chance) 우연 조합 하나만으로 이런 실질적인 연관 유의성 점수가 관측될 **확률 수치가 거의 안드로메다 수준으로 희박해서 뻔뻔하게 말이 안 된다는 사실을 고발 지적**해 내는 것과 동일합니다. 

Hence, if we see a small $p$-value, then we can infer that there is an association between the predictor and the response.
따라서, 만일 재판부 모니터 결괏값에 요 작고 귀여운 극소 코딱지 **$p$-값 표식 숫자**를 발견 눈요기하게 된다면, 저희는 망설임 일체 없이 "이런! 고로 요 두 가지 원인과 결과 예측 변수들 사이엔 부정할 수 없는 아주 강렬한 야릇한 관계 연대가 실전 구축 형성되어 있는 게 절대 틀림없구나!" 라고 당당하고 합리적인 통계 추론 타격을 가할 자격증을 얻게 됩니다.

We _reject the null hypothesis_—that is, we declare a relationship to exist between $X$ and $Y$—if the $p$-value is small enough.
자, 그래서 그 위대한 $p$-값 지표가 우리가 지정한 잣대 기준보다 참으로 충분히 초라하고 작다면, 우리는 과감하게 망치를 두드리며 방어측인 귀무 가설 녀석을 법정서 매몰차게 짓밟아 기각시켜 버립니다(_reject the null hypothesis_)—이것이 시사하는 바는 바로 우리가 만인 앞에 대놓고 공식적으로 "여러분! 우리 $X$랑 $Y$ 사이엔 진짜 썸스토리 연관 관계가 단연코 확실하게 실존 증명 선포합니다!" 라고 호언장담 고성방가하는 것과 일치합니다. 

Typical $p$-value cutoffs for rejecting the null hypothesis are 5% or 1%, although this topic will be explored in much greater detail in Chapter 13.
통상 바닥 실무계에서, 이 불쌍한 귀무가설 피의자를 사형대로 보내버리는 기각 마법의 단두대 컷오프 허들(커트라인) 바리케이드 통과 기준치는 **가장 일반적인 경우 보통 5% 또는 아주 깐깐하게는 1% 수치(주로 0.05 혹은 0.01 표기)**로 칼같이 삼아서 봅니다, 비록 이 기각 임계점 설정 왈가왈부 쟁점 주제는 훗날 지옥의 제 13장 코스로 넘어가며 이보다 수백만 배는 더 집요하고 깊고 디테일하게 까서 까발려 파헤쳐 보게 될 터이지만요.

When $n = 30$, these correspond to $t$-statistics (3.14) of around 2 and 2.75, respectively.
이 커트라인 퍼센티지를 아까 표본 크기 $n = 30$ 명이라는 가동 사이즈 모델 조건 안에 우걱우걱 집어넣어 비교 환산 배율을 매겨본다면, 우리가 앞에서 보았던 그 $t$-통계량(3.14) 방정식 수치 기준 점수로 보았을 때 대략 5% 일 때 2점 컷오프 언저리, 그리고 1% 깐깐 컷오프 일 땐 대략 2.75점대 근처라는 심사 결과 점수치 대응 지표 환산 결단을 얻어 낼 수 있습니다.

Table 3.1 provides details of the least squares model for the regression of number of units sold on TV advertising budget for the `Advertising` data.
자 뜬구름 잠시 접어두고, 위에 아까 스쳐 보여드린 예제 테이블 표 3.1 통계 결과물을 찬양해 보시죠. 이 표에는 해당 `Advertising(광고)` 데이터의 구체적 산물을 갈아 넣어 산립된, TV 자본 예산 예탁에 비례하는 제품 산출 판매 유닛 수치의 본 연장 회귀 최소 제곱 모델 판결문에 얽힌 아주 주옥같은 구체 세부 세팅 내역들이 일목요연 제공 표기되어 도출 전시되었습니다. 

Notice that the coefficients for $\hat{\beta}_0$ and $\hat{\beta}_1$ are very large relative to their standard errors, so the $t$-statistics are also large; the probabilities of seeing such values if $H_0$ is true are virtually zero.
여기를 보시면 소름이 돋습니다, $\hat{\beta}_0$와 $\hat{\beta}_1$이라는 핵심 계수 콤보 스코어 표기값 숫자들이 본인들 곁에 찰거머리처럼 들러붙어 있는 표준 오차 스파이 수치에 비해 기고만장하게 그 위용 상대 사이즈 폭이 훨씬 빵빵하고 미친 듯이 큽니다. 그렇기 때문에 이 둘의 결과물 분수로 산출된 재판관 스코어인 $t$-통계량 결과치 숫자들도 천장을 뚫고 나갈 만큼 함께 커대해졌다는 점을 확연히 명목 주목하여 주십시오! 이 뜻의 행간 의미는 무엇일까요? 이 통계가 말해주는 자명한 파장은, 초안 방어막 가설인 $H_0$(아무런 상관성 없다!)가 만약 진짜 사실 참이라고 가정한 상태 공간 베이스에서라면, 눈앞에 이처럼 오버스펙 스코어 통계 치수값들이 기적처럼 목격되리란 확률 요율 기대감이란 아예 우스갯소리도 안 되는 사실상 존재 제로 확률, 즉 거의 0% 퍼센트 확률에 고스란히 처참히 수렴한다는 극과 극 단절의 의미입니다.

Hence we can conclude that $\beta_0 \neq 0$ and $\beta_1 \neq 0$.$^4$
그러므로 위 데이터 정황 요소를 종합 재판 타결하여 볼짝시면, 고로 결론적으로 우린 아주 깔끔하게 일말의 양심 찔림 없이 **"$\beta_0$ 역시 죽었다 깨어나도 자명하게 0이 아니며($\beta_0 \neq 0$) 단숨에 기어코 $\beta_1$의 정체마저 0 이 결코 아니다($\beta_1 \neq 0$)!!"** 라는 빼박 사형 선고 판결의 결론 마침표를 내릴 수 있는 확증 합법적 쾌거 단계의 종지부 판정 선언을 마무리 짓게 됩니다.$^4$

---

## Sub-Chapters

This is the document for 3.1.2 Assessing the Accuracy of the Coefficient Estimates.

[< 3.1.1 Estimating the Coefficients](../3_1_1_estimating_the_coefficients/trans2.html) | [3.1.3 Assessing the Accuracy of the Model >](../3_1_3_assessing_the_accuracy_of_the_model/trans2.html)

---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3.1 Qualitative Predictors](../trans2.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/trans2.html)

# Predictors with Only Two Levels

# 수준이 2개인 예측 변수 (남자/여자, 예스/노처럼 선택지가 딱 두 개인 재료 요리법)

Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don’t, ignoring the other variables for the moment.
잠시 머리를 식히기 위해 다른 지겨운 변수들은 덮어두고 쿨하게 무시해 봅시다. 오직 딱 하나, **"자기 집이 있는 금수저(주택 소유자)"** 집단과 **"집 없는 무주택자"** 대조군 사이에, 누가 신용카드 빚을 평균적으로 더 많이 지고 끌려가는지(잔고 내역 차이) 그 한판 승부만을 심층적으로 조사하고 싶다고 상상해 보세요.

If a qualitative predictor (also known as a _factor_) only has two _levels_, or possible values, then incorporating it into a regression model is very simple.
다행스럽게도, 이런 "집이 있다 / 없다" 혹은 "남자 / 여자"처럼 선택지(수준, levels)가 딱 2개뿐인 단순무식한 문자형 힌트 변수(가끔 통계 꼰대들은 이걸 _요인(factor)_ 이라고 부르기도 합니다)를 우리 수학 공식 냄비에 집어넣는 요리법은 정말 헛웃음이 나올 정도로 매우 단순합니다.

We simply create an indicator or _dummy variable_ that takes on two possible numerical values.[10]
어떻게 하냐고요? 텍스트를 기계가 먹을 수 있게 둔갑시키는 아주 얄팍한 속임수 장치, 즉 숫자 '1' 아니면 '0' 딱 두 종의 불빛만 들어오는 꼬마전구 스위치인 **_더미 변수(Dummy variable, 가짜 변수)_**를 수작업으로 뚝딱 창출해 내면 만사형통입니다.[10]

For example, based on the `own` variable, we can create a new variable that takes the form
예를 들어 볼까요? 장부상에 영어 텍스트로 적힌 `own(주택 소유 여부)` 열을 찢어버리고, 다음과 같은 마법의 룰을 통해 새로운 기계용 암호 스위치 변수 $x_i$ 를 만듭니다.

variable
스위치 $x_i$:
$$
x_i = \begin{cases}
1 & \text{if } i\text{번째 고객이 자기 집을 가짐 (Yes)} \\
0 & \text{if } i\text{번째 고객이 집 없는 무주택자임 (No)}
\end{cases}
$$

and use this variable as a predictor in the regression equation.
짜잔! 문자가 숫자로 변신했습니다. 이제 우리 통계 학자들은 이 1과 0으로 둔갑된 스위치 변수($x_i$)를 뻔뻔하게 원래의 수학 회귀 방정식 세트에 구겨 넣어 예측 재료로 씁니다.

This results in the model
스위치를 달고 탄생한 우리의 새로운 짬뽕 방정식은 이런 우스꽝스러운 꼴이 됩니다.

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{번째 고객이 집 있을 때 (스위치 ON: 1)} \\
\beta_0 + \epsilon_i & \text{if } i\text{번째 고객이 집 없을 때 (스위치 OFF: 0)}
\end{cases} \quad (3.27)
$$

Now $\beta_0$ can be interpreted as the average credit card balance among those who do not own, $\beta_0 + \beta_1$ as the average credit card balance among those who do own their house, and $\beta_1$ as the average difference in credit card balance between owners and non-owners.
이 마법 공식을 가만히 째려보세요! 결국 스위치가 꺼진($0$) 무주택자의 남는 덩어리인 $\beta_0$ 의 정체는 자연스레 **"집 없는 서민들의 평균 카드 빚 액수"**가 됩니다. 반대로 스위치가 켜진($1$) 유주택자 파트는 $\beta_0 + \beta_1$ 니까 **"집주인들의 평균 카드 빚 액수"**죠. 그렇다면 중간에 낀 저 기울기 $\beta_1$ 의 진짜 의미는 뭘까요? 바로 유주택자와 무주택자 간의 **"평균 빚 액수의 차이(갭)"**를 우아하게 계산해 내는 통계적 눈금자가 되는 것입니다!

Table 3.7 displays the coefficient estimates and other information associated with the model (3.27).
모델 (3.27)을 진짜 컴퓨터(파이썬)로 돌려봤더니, 아래 표 3.7처럼 아주 근사한 성적표(계수 추정치)를 뱉어냈습니다.

The average credit card debt for non-owners is estimated to be $\$509.80$, whereas owners are estimated to carry $\$19.73$ in additional debt for a total of $\$509.80 + \$19.73 = \$529.53$.
번역해 볼까요? 기본값 세팅인 무주택자 그룹($\beta_0$)의 평균 신용카드 빚은 대략 가난한 $\$509.80$ 로 추산되었습니다. 반면 당당하게 스위치가 켜진 집주인 그룹은 저 기본 부채에다가 $\beta_1$ 페널티 몫인 $\$19.73$ 의 액수를 추가로 더 업고 다니게 되어, 총비용 $\$509.80 + \$19.73 = \$529.53$ 만큼의 평균 빚을 등에 짊어지는 것으로 판명되었습니다. (집 있는 놈들이 돈을 미세하게 더 펑펑 쓴다는 의미죠.)

However, we
하지만 기뻐하기엔 이릅니다! 우리가
> [10] (깨알 상식) 기계 학습(머신러닝)을 하는 프론트나 AI 딥러닝 긱(geek)들은, 이런 카테고리 기호(글자)를 모델에 밀어 넣으려고 0과 1의 더미(Dummy) 변수 스위치로 강제 포장하는 속임수 기술을 아주 힙하게 **"원-핫 인코딩(One-hot encoding)"** 이라고 부르며 잘난 척합니다.

**==> picture [300 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 40 60 80 100 5 10 15 20 2000 8000 14000<br>Balance(빚)<br>Age(나이)<br>Cards(카드개수)<br>Education(교육연수)<br>Income(소득)<br>Limit(한도)<br>Rating(신용등급)<br>0 500 1500 2 4 6 8 50 100 150 200 600 1000<br>1500<br>500<br>0<br>100<br>80<br>60<br>40<br>20<br>8<br>6<br>4<br>2<br>20<br>15<br>10<br>5<br>150<br>100<br>50<br>14000<br>8000<br>2000<br>1000<br>600<br>200<br>**----- End of picture text -----**<br>

**FIGURE 3.6.** _The_ `Credit` _data set contains information about_ `balance` _,_ `age` _,_ `cards` _,_ `education` _,_ `income` _,_ `limit` _, and_ `rating` _for a number of potential customers._
**FIGURE 3.6.** `Credit` _장부에 빼곡하게 기록된 불쌍한 카드 노예(잠재 고객)들의 각종 개인정보(`balance(빚)`, `age(나이)`, `cards(카드 개수)` 등 숫자형 정보)들이 서로 얽히고설켜 멱살을 잡고 싸우는 상관관계를 무식하게 다 그려버린 거대한 융단폭격기 산점도 매트릭스 도화지입니다._

notice that the $p$-value for the dummy variable is very high. This indicates that there is no statistical evidence of a difference in average credit card balance based on house ownership.
다시 본론으로 돌아와서 끔찍하게 큰 저 $p$-값(0.6690) 성적표를 응시하세요! 이것이 무엇을 시사합니까? 방금 우리는 "집 없는 애들보다 집 있는 놈들이 평균적으로 $\$19$ 불 정도 빚이 더 많다"고 신나했는데, 저 망할 $p$-값이 0.05 컷을 아득히 뚫어버려서 이 미세한 빚쟁이 차이가 사실 통계적으로 완전히 허구의 어거지 헛소리(증거 불충분)임을 폭로해 버린 것입니다. 결론은, 솔직히 자기 집 보유 여부 스위치 하나 켰다 껐다 한다고 개개인의 평균 실제 카드 지출 씀씀이(빚)에는 아무런 실질적 격차가 없었다는 슬픈 반전 결말입니다.

The decision to code owners as $1$ and non-owners as $0$ in (3.27) is arbitrary, and has no effect on the regression fit, but does alter the interpretation of the coefficients.
그런데 억울한 분이 있을 수 있습니다. "야! 왜 굳이 집주인을 1번(켜짐)으로 주고 무주택자를 0번(꺼짐)으로 코딩했냐? 서민 차별하냐?" 맞습니다. 수학 공식 (3.27)에서 번호 1과 0표를 부여한 순서는 그냥 작성자 맘대로 찍은(임의적) 속임수에 불과합니다. 이 조작을 0과 1을 거꾸로 뒤집는다고 모델을 망치는 파괴력 따위는 없습니다. 단지 우리가 방금 위에서 재잘거렸던 계수들의 해석 방식 해설판 스크립트만 앞뒤가 뒤집어지는 소소한 차이가 일어날 뿐이죠.

If we had coded non-owners as $1$ and owners as $0$, then the estimates for $\beta_0$ and $\beta_1$ would have been $529.53$ and $-19.73$, respectively, leading once again to a prediction of credit card debt of $\$529.53 - \$19.73 = \$509.80$ for non-owners and a prediction of $\$529.53$ for owners.
만약 당초에 삐딱선을 타서 무주택자를 $1$로 코딩하고 집주인을 $0$기본값에 처박아뒀다면? 놀라지 마세요! 추정치 파라미터 $\beta_0$ 덩어리는 이번엔 집주인 그룹인 무려 $529.53$짜리 스코어로 튀어나오며 부활했을 것이고, 격차값 $\beta_1$ 은 부양 페널티가 아닌 오히려 채무 탕감 빼기 느낌의 마이너스 $-19.73$ 으로 옷을 갈아입었을 것입니다! 하지만 결론적으로 마지막 종착지 단락에서 "결국 무주택 서민 빚은 $\$529.53 - \$19.73 = \$509.80$ 이고, 집주인 빚은 고스란히 $\$529.53$ 이다"라는 뻔한 도출액은 예나 지금이나 귀신같이 똑같이 맞아떨어집니다.

Alternatively, instead of a $0 / 1$ coding scheme, we could create a dummy variable
조금 더 기이한 짓글거리 하나 가르쳐드릴까요? 굳이 속임수를 0과 1로 치우치게 세팅하는 코딩 매커니즘 대신, 훨씬 극단적인 대립각의 이중극 더미 변수 진자 스위치를 이런 식으로 창조할 수도 있습니다!

$$
x_i = \begin{cases}
1 & \text{if } i\text{번째 고객이 집 소유주(Yes)면 양의 에너지 (+1)} \\
-1 & \text{if } i\text{번째 고객이 무주택(No)이면 음의 에너지 (-1)}
\end{cases}
$$

and use this variable in the regression equation.
그리고 이 음양 오행처럼 극단적인 값(+1과 -1)의 시소를 타는 변수 부품을 무작정 회귀 공식 아궁이에 집어넣어 때웁니다.

This results in the model
이 미친 짓의 결과로 태어난 신형 변이종 수식은 이렇습니다:

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{번째가 집주인이면 위로 살짝 점프(+)} \\
\beta_0 - \beta_1 + \epsilon_i & \text{if } i\text{번째가 무주택 서민이면 아래로 살짝 기침(-)}
\end{cases} \quad (3.28)
$$


|3.3 Other Considerations in the Regression Model|3.3 Other Considerations in the Regression Model|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept(절편)`<br>`own[Yes](집주인 보너스)`|509.80<br>33.13<br>15.389<br>_<_0_._0001<br>19.73<br>46.05<br>0.429<br>0.6690|

**TABLE 3.7.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `own` _in the_ `Credit` _data set. The linear model is given in (3.27). That is, ownership is encoded as a dummy variable, as in (3.26)._
**TABLE 3.7.** `Credit` _장부 세계관 내에서 '주택 소유 여부 스위치(`own`)' 만을 돌려가며 타겟 '카드 빚(`balance`)'과의 끈적한 관계를 심문해 받아낸 고달픈 조서(최소 제곱 계수) 결과표. 공식 (3.27)을 기계에 넣고 돌린 참극이며, 주택 보유 여부는 0과 1의 꼼수 스위치(더미 변수)로 코딩 조작된 상태입니다._

Now $\beta_0$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_1$ is the amount by which house owners and non-owners have credit card balances that are above and below the average, respectively.[11]
자, 이 +1,-1 대립각 세팅(1과 -1 코딩) 하에서 이제 중심 모수 $\beta_0$ 의 위상은 완전히 달라집니다! 이제 $\beta_0$ 는 어느 한 집단의 빚이 아니라, 집이 있든 없든 다 때려 친 **"존재하는 모든 인류 전체의 대통합 평균 신용카드 빚 잔고 중앙치"**라는 웅장한 지위를 얻게 되죠. 반면 옆에 삐쳐나온 $\beta_1$ 의 역할은, "그 잘난 평균 중앙치 빚에서 집주인 집단은 위쪽으로 살짝 올라타고, 서민 집단은 아래로 살며시 까이는 그 **시소의 진폭 등락 간극** 수위" 라는 기가 막힌 의미 편차 양념 소스로 진화 재탄생합니다![11]

In this example, the estimate for $\beta_0$ is $\$519.665$, halfway between the non-owner and owner averages of $\$509.80$ and $\$529.53$.
재밌는 예제로 볼까요? 저 기묘한 1/-1 코딩법에서 튀어나온 대통합 $\beta_0$ 의 추정치는 약 $\$519.665$ 로 꽂히는데, 소름 돋게도 이 숫자는 무주택 평균 $\$509.80$ 과 유주택자 평균 $\$529.53$ 라는 구질구질한 두 진영 패싸움의 절묘한 한복판 타협 지점, 즉 정확히 반으로 가른 반토막 정중앙 중앙선에 안착한 금액입니다!

The estimate for $\beta_1$ is $\$9.865$, which is half of $\$19.73$, the average difference between owners and non-owners.
덩달아 이 1/-1 모드에서 오르락내리락 파동 버프 역할을 하는 시소 진폭 $\beta_1$ 추정치는 소심하게 반 토막이 나서 약 $\$9.865$ 로 도출됩니다. 이 액수는 아까 본, 집주인과 서민 두 집단을 영끌해서 비교했을 때 나던 전체 뼈아픈 차이 갭($\$19.73$)의 정확히 절반을 가른 조각 몫과 미친 듯이 칼각으로 판박이 일치하죠.

It is important to note that the final predictions for the credit balances of owners and non-owners will be identical regardless of the coding scheme used.
하지만 명심해야 할 최고의 타격감 팩트는 이거입니다!! 당신이 모델에 암호 스위치를 치사하게 (0, 1)로 넣든, 멋지게 (-1, +1)로 뒤틀어 코딩하건 뻘짓 장난을 쳤던 간에... 종국에 가서 **"결국 이놈의 실질 카드 빚이 총합 얼마로 도출될까?" 하고 맞추는 이 악물고 산출한 마지막 최종 신용 잔고 타깃 예측 금액 결론 결과물 자체는 눈곱만큼의 틀어짐 없이 미친 듯이 획일적으로 똑같이 세팅 도출**된다는 무섭고 불변하는 수학의 이치 사실입니다.

The only difference is in the way that the coefficients are interpreted.
결국 이 유치한 암호 놀이 코딩에 따라 차이 나는 장난은 단 하나! 각 파라미터 계수 성분 쪼가리들이 모여서 어떻게 해설가들에게 핑계(해석 의미 부여) 대며 입증 처리되는지, 즉 이야기 썰을 푸는 '세세한 혓바닥의 해석 방법론 차이 노선' 단 하나뿐입니다.

### Qualitative Predictors with More than Two Levels (수준이 2개를 초과하는 다혈질 변수들)

When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values.
난관에 봉착했습니다! 아까는 '남자냐/여자냐', '집이 있냐/없냐' 같이 단 2가지 선택뿐이라 꼬마전구(0, 1 더미 변수) 한 개 불만 껐다 켰다 하면 그만이었죠. 하지만 만약 문자로 된 변수가 '동부, 서부, 남부지방'처럼 옵션이 여러 갈래(등급 수준 초과)로 뻗어있는 골치 아픈 녀석이라면? 절망적이게도 더 이상 꼬마전구 단 한 개(1개의 단일 더미 변수 체계)만 가지고는 이런 다분화 구조 옵션 기호들을 전부 담아 가리킬 묘사가 불가능해 폭파됩니다.

In this situation, we can create additional dummy variables.
겁먹지 마세요! 이럴 때는 인간의 돈질 꼼수를 부리면 됩니다. 전구가 하나라서 부족하다면? 그냥 가게 가서 추가로 **스위치 꼬마전구(여분 부수 더미 변수)를 여러 개 더 왕창 사 와서 잇달아 주렁주렁 매달아 창조해 내면** 그만입니다!

For example, for the `region` variable we create two dummy variables. The first could be
예컨대 3지선다형 속성의 `region(동부/서부/남부 지역)`을 통제하려 할 때, 우린 영리하게 2개의 더미 전구를 사옵니다. 첫 번째 꼬마전구는 이런 역할을 맡죠:

첫 번째 더미 스위치 전구:
$$
x_{i1} = \begin{cases}
1 & \text{if } i\text{번째 사투리 손님이 남부(South) 출신일 때 번쩍! (Yes)} \\
0 & \text{if } i\text{번째가 남부 출신이 아닐 때 꺼짐 (No)}
\end{cases}
$$

and the second could be
그리고 두 번째 꼬마전구는 이런 덫을 놓습니다:

두 번째 더미 스위치 전구:
$$
x_{i2} = \begin{cases}
1 & \text{if } i\text{번째 손님이 서부(West) 촌놈일 때 번쩍! (Yes)} \\
0 & \text{if } i\text{번째가 서부 출신이 아닐 때 꺼짐 (No)}
\end{cases}
$$

Then both of these variables can be used in the regression equation, in order to obtain the model
자, 전구 세팅 끝! 이제 이 골칫덩이들을 우리 선형 회귀 짬뽕 방정식 구덩이 안에 투척해 버리면? 마침내 다음처럼 어지럽게 뒤틀려 완성된 화려한 궁극의 체계 적합 모델을 쟁취할 수 있습니다!

$$
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{번째 손님이 남부(South) 사람 (전구1 켜짐)} \\
\beta_0 + \beta_2 + \epsilon_i & \text{if } i\text{번째 손님이 서부(West) 사람 (전구2 켜짐)} \\
\beta_0 + \epsilon_i & \text{if } i\text{번째 손님이 동부(East) 토박이 (야! 전구 1, 2 둘 다 꺼짐!)}
\end{cases} \quad (3.30)
$$

Now $\beta_0$ can be interpreted as the average credit card balance for individuals from the East, $\beta_1$ can be interpreted as the difference in the average balance between people from the South versus the East, and $\beta_2$ can be interpreted as the difference in the average balance between those from the West versus the East.
아주 재밌는 일이 생겼습니다! 새 모델의 중심 몸통 파트인 파라미터 **$\beta_0$** 은 홀로 아무 전구도 켜지지 못한 서러운 기본 상태, 즉 꿔다 놓은 보릿자루인 **동부(East) 호적 토박이들의 순수한 '평균 카드 빚'**을 고스란히 대변하게 됩니다. 그리고 슬며시 옆에 붙은 파츠 **$\beta_1$** 은 동부 서민들을 기준으로 삼았을 때, **남부(South) 지역 놈들이 그 동부 기준치보다 기형적으로 빚이 얼마나 더 높고 낮은지 차이나는 상대 패널 격차 수치**를 폭로하는 점수표가 되고요! 마지막 **$\beta_2$** 성분 녀석 역시 동일한 눈높이에서 동부 기준에 대비해 **서부(West) 갱단들이 짊어지는 빚의 평균 차이 갭 지수**를 분별해 찍어내는 신호등 램프로 해석될 수 있습니다.

There will always be one fewer dummy variable than the number of levels.
모든 통계학자가 숨 달고 우러러보는 영원불멸의 황금 절대 규칙이 여기 하나 숨어 있습니다: **더미 전구를 몇 개나 달아야 해? 정답은 당신이 포섭하려는 범주 카테고리(선택지 마릿수) 등급 갈래 가짓수보다 무조건. 반드시. 예외 없이 '딱 하나(1)' 뺀 마이너스만큼 적은 숫자로만 전구를 제한 조립 구성해야 한다는 무서운 법칙**입니다! (선택지가 3명이면 전구는 2개, 5명이면 4개뿐입니다.)

The level with no dummy variable — East in this example — is known as the _baseline_.
그리고 아까처럼 이 잔혹한 규칙 때문에 전구를 하나도 할당받지 못해 아무 스위치 장치도 소유 못한 채 홀로 내동댕이 버려진 기본값 집단! ─ 이 예제의 꿔다 놓은 보릿자루 '동부(East)' 같은 특정 집단 구역 녀석을, 통계학에선 아주 그럴싸하게 우주 기저 기준점 도구라는 명분을 담아 고상하게 **_베이스라인(Baseline, 기준선)_** 범주라고 부릅니다. 

---
> [11] (기괴한 진실) 기술적인 결벽증을 가진 통계 학도들의 눈높이로 따져 파고들자면, 사실 저 $\beta_0$ 지표 수치 덩어리는 유주택자의 평균치 빚 덩이와 무주택자의 빚 덩이 합산을 강제로 반반 자른 반토막 등분 값입니다. 맙소사! 그렇기 때문에 이 $\beta_0$ 점수가 현실적인 진짜 인간들 전체의 찐 포괄 통합 평균과 '100% 무결점 일치'하는 기적은 오로지... 집 있는 그룹과 집 없는 두 찌질이 대조군 스쿼드 멤버 숫자가 완전히 토씨 하나 안 틀리고 똑같이 균등 50:50 분할 상황으로 세팅되었을 때만 뚝 떨어지는 조건 한정 희귀 공식입니다.

|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept(동부 빚 베이스라인)`<br>`region[South](남방 한계선 오차)`<br>`region[West](서부 갱단 오차)`|531.00<br>46.32<br>11.464<br>_<_0_._0001<br>_−_12.50<br>56.68<br>_−_0.221<br>0.8260<br>_−_18.69<br>65.02<br>_−_0.287<br>0.7740|

**TABLE 3.8.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `region` _in the_ `Credit` _data set. The linear model is given in (3.30). That is, region is encoded via two dummy variables (3.28) and (3.29)._
**TABLE 3.8.** `Credit` _장부 내의 3갈래_ `region(동·서·남부)` _지표 스위치 전구들을 무자비하게 껐다 켰다 고문하며, 고객별 찐 타겟_ `balance(카드빚 타겟팅)` _사이의 인과율을 밝혀낸 최소 제곱 계단의 사생결단 성적표 조서입니다. 이 요주의 끔찍한 선형 모형 짬뽕은 아까 다룬 3.30 공식에 따르며 두 개의 전구 더미 스위치 코어를 달았습니다._

From Table 3.8, we see that the estimated `balance` for the baseline, East, is $\$531.00$. It is estimated that those in the South will have $\$18.69$ less debt than those in the East, and that those in the West will have $\$12.50$ less debt than those in the East. However, the $p$-values associated with the coefficient estimates for the two dummy variables are very large, suggesting no statistical evidence of a real difference in average credit card balance between South and East or between West and East.[12]
표 3.8의 우스꽝스러운 성적표 결과를 구경해 보십쇼. 가련한 기준선 샌드백인 우리 동부 촌놈 집단(East)의 예측 카드 대금 통계치는 $\$531$ 로 가볍게 시작합니다. 이를 기준으로, 남부를 쓸러 다니는 무리는 그 동부보단 부채를 대략 한 $\$18.69$ 가량 알뜰하게 덜 지니고 탕감할 것으로 조준되며, 서부를 돌아다니는 카우보이 그룹 역시 동부에 살던 사람들보단 대충$\$12.50$ 빚이 까이며 적게 잡힐 거라고 어설픈 추정판을 짰습니다. 하지만! 반전은 여기서 시작이죠. 이 두 더미 매개 잡놈 변수에 딱지처럼 따라붙은 그놈의 지겨운 $p$-값들이 미친 듯이 뻥튀기되어 솟구쳐버렸습니다 (0.8260, 0.7740 급 나락). 고로! 우리가 떠들던 남부나 동부, 혹은 서부와 동부 간 사이의 실질 평균 빚 차이 격차라는 어설픈 편가르기 이론은 싸그리 증거 불충분한 헛소리로 밝혀진 통계적 비극의 희극극입니다.[12]

Once again, the level selected as the baseline category is arbitrary, and the final predictions for each group will be the same regardless of this choice.
한 번 더 강하게 못 박겠습니다! 당신이 무작위 사다리타기로 그 기준 베이스라인 자리를 동부에게 던져주건 아님 다른 갱단에게 주었건 이 결정짓기 게임판의 룰 위치 세팅 설정 따위는 완전 당신 주관상 제멋대로 임의적입니다. 누가 그 자리를 차지해 희생양이 되든 끝에 가서는 이쪽저쪽 동네 그룹들 모두를 향해 "나 최종 예측 빚 산출은 이건 데?" 라며 뿜어대는 파이널 총결론 예측액 숫자는 단 0.0001%의 어긋남 없이 똑 떨어지게 소름 돋게 천편일률 똑같을 것이 틀림없는 현실 진리입니다.

However, the coefficients and their $p$-values do depend on the choice of dummy variable coding.
하지만 그 반대급부로 한 가지 아픔은 감수해야죠. 방금 당신이 맘대로 전구 스위치를 배선시킨 그 어설픈 코딩 더미 조합 취향의 선택 결과에 의해서, 앞단에서 해설가들에게 핑계를 줄 계수 수치 점수 덩어리들이나 $p$-값 찌라시 꼬리표 같은 중간 성적표만큼은 요동치듯 바뀌어버릴 수 있다는 가슴 아픈 종속성도 있단 사실을 말입니다.

Rather than rely on the individual coefficients, we can use an _F_ -test to test $H_0$ : $\beta_1 = \beta_2 = 0$; this does not depend on the coding. This _F_ -test has a $p$-value of $0.96$, indicating that we cannot reject the null hypothesis that there is no relationship between `balance` and `region` .
그래서 이런 줏대 없는 헛스윙 코딩 결과물에 오롯이 목숨 걸며 개별 요원 쪼가리 계수에 현혹되기보다는! 시원하게 판을 엎어 전체 재판관 포대인 전지전능 무적 무기 **_F_-테스트 심판소**에다가 저주 가설 $H_0 : \beta_1 = \beta_2 = 0$ (다 쓸모없는 헛소리다!) 안건을 상정해 버리는 게 통계 세계의 진정한 알파입니다. 이 거대 기둥 심판은 당신이 전구를 어떻게 배선하건 말건 따위에는 절대 현혹되지 않거든요. 이 위대한 $F$-검정 판사님은 $0.96$ 이라는 어마 무시하게 끔찍한 $p$-값 오물 철퇴 판결을 내리며 우리 가설에 죽통을 날립니다. 그 선고문인즉, "무슨 동네(`region`)에 산답시고 카드 빚(`balance`)이 달라진단 거냐? 완전 100% 무관한 헛소리로 기각 불가 판정 땅땅!" 이라는 슬픈 퇴짜를 당한 무관계 종착점을 인증하는 것입니다.

Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors.
놀라운 뉴스를 전파합니다! 이렇게 더미 변수 전구를 달아 문자를 숫자로 속여 먹는 사기 접근법 스킬 하나면... 한 솥밥을 나누기 싫어하던 얌전한 수치 덩어리들(정량 변수)과 말썽쟁이 이방인 글자 요인(정성적 변수)들을 같은 냄비 속에 모조리 다 쓸어넣고 회귀 퓨전 화합물 대통합 혼종을 조리해 내려 할 때도 일체의 치명적 문제나 어려움 장벽 따위 전혀 야기되지 않고 아주 매끄럽고 신비롭게 작동 굴러갑니다. 

For example, to regress `balance` on both a quantitative variable such as `income` and a qualitative variable such as `student`, we must simply create a dummy variable for `student` and then fit a multiple regression model using `income` and the dummy variable as predictors for credit card balance.
재밌는 예 하나를 더 볼까요? 가령 지갑 두께 예측 타깃인 `balance` 통장 잔고 빚을 캐기 위해... "니 월수입이 얼마냐?" 하는 아주 차가운 숫자 공격 `income(정량적 변수)`과, "너 학생이냐?" 하는 텍스트 공격 `student(정성적 변수)`, 이 두 전혀 어울리지 않는 원소 공격수 둘을 같이 합격 쌍포로 회귀 발사하고 싶다고 해봐요. 우린 쩔쩔맬 필요 없이 "학생이냐?"는 글자에 몰래 더미 스위치 코드를 덧대 달아버리면 끝입니다! 그런 뒤 월수입 돈 액수 숫자 변수 축과 그 더미 둔갑 변수를 각자 우아하게 양대 예측 장군으로 추대해, 한 냄비에 둘 다 집어던지고 다중 회귀 모델 모임 불꽃놀이를 화려하게 지펴 적합 시켜 점화해 버리기만 하면 단박에 수순 완료입니다! 참 쉽죠?

There are many different ways of coding qualitative variables besides the dummy variable approach taken here.
물론, 오늘 여기서 주야장천 썰을 푼 '0, 1 더미 스위치 누르기' 짬짜면 같은 사기 꼼수 외에도... 통계 덕후 할아버지 장인들이 개발해 놓은 이 골치 아픈 텍스트 문자를 길들이는 인코딩 변동 수법 요령 룰은 이 세상에 너무나도 방대하고 무성하며 별천지로 참 다채롭게 쌓여있습니다.

All of these approaches lead to equivalent model fits, but the coefficients are different and have different interpretations, and are designed to measure particular _contrasts_.
그런데 참 재밌죠? 이 무수하게 상이한 온갖 문파 무공 요령 기선 접근방식들은 싹 다 결국 "최후에 뱉어내는 빚 예측 결과 덩어리는 어이 털리게 동일!" 이라는 헛웃음 유사 모델 적합 타겟지에 도달 인도하는 건 한 치의 오차 예외가 없습니다. 하지만! 오직 중간 과정의 부산물인 그 잘난 파트별 **계수 파츠 장식 수치들은 몽땅 다 제각각 외관이 판이하게 달라져** 버리고, 덩달아 해설자들의 나팔 부는 입방아인 **해석 방향 스토리 노선 역시 각자 뒤틀어지고 틀려지는 거대한 해석 논쟁 난파**를 잉태 야기합니다. 실은 애초에 그 다양한 꼼수 관습들이 저마다 각각 치밀한 의도를 갖고 모종의 구역 한정 특별 맞춤식 **_대조군(Contrasts)_** 요소를 정밀 타격 측정 기표로 꼽아 부각하기 위해 꽤 변태같이 음흉하게 설계 조립되었기 때문인 까닭입니다.

This topic is beyond the scope of the book.
하지만 여기서 멈추겠습니다. 이 복잡 다단 더미 꼼수들의 음흉한 '대조군 꼬리 물기 뇌절' 세부 주제는 애석하게도 당초 쿨하고 교양 있게 기초 교본으로 놀기로 컨셉 잡은 이 기초 통계 우리 소박 교재 서적의 얕은 한계 지능 허용 범위 스펙트럼 한계선을 안드로메다 멀리 돌파 초과해 버린 금단의 선망 주제이므로 미련 없이 관대히 이쯤 패스 통과하며 서둘러 탈출하겠습니다!

---

[< 3.3.1 Qualitative Predictors](../trans2.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/trans2.html)

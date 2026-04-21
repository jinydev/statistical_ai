---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3.1.1 Predictors With Only Two Levels](../3_3_1_qualitative_predictors/3_3_1_1_predictors_with_only_two_levels/trans2.html) | [3.3.2.1 Non-Linear Relationships >](3_3_2_1_non-linear_relationships/trans2.html)

# 3.3.2 Extensions of the Linear Model

# 3.3.2 선형 모델의 확장 (고집불통 공식을 유연하게 뜯어고치는 마법)

The standard linear regression model (3.19) provides interpretable results and works quite well on many real-world problems.
우리가 주구장창 우려먹고 있는 아주 전형적이고 고전적인 그 선형 회귀 모델(수식 3.19)은, 나름대로 해석하기도 만만하고 실제 판에서 부딪히는 수많은 골칫거리 문제들도 꽤나 시원시원하게 잘 풀어내는 유능한 녀석입니다.

However, it makes several highly restrictive assumptions that are often violated in practice.
하지만 이 꽉 막힌 모범생 공식에는 아주 치명적인 단점이 하나 있습니다. 자기가 정해놓은 엄청나게 빡빡하고 고지식한 '가정(조건)'들을 너무 들이댄다는 겁니다. 실전의 무자비한 야생 장사판 데이터들은 그런 교과서적인 조건 따위는 코웃음 치며 밥 먹듯 박살 내버리기 일쑤인데 말이죠.

Two of the most important assumptions state that the relationship between the predictors and response are _additive_ and _linear_.
그 수많은 고집들 중에서도 가장 악명 높고 우리를 피곤하게 구는 두 가지 갑질 조건이 있습니다. 바로 예측 재료(힌트 변수)와 도출 결과(응답 타겟) 사이의 인과율 관계가 무조건 **_가법적(Additive, 덧셈 짬짜면)_**이어야 하고, 오롯이 **_선형적(Linear, 일자 뻣뻣 직선)_**이어야만 한다는 막무가내 억지 룰입니다.

The additivity assumption additive means that the association between a predictor $X_j$ and the response $Y$ does linear not depend on the values of the other predictors.
여기서 말하는 '가법성(덧셈) 고집'이란 게 뭐냐면, 특정한 1번 재료($X_j$)가 타겟 고기($Y$) 맛을 내는 데 미치는 맹활약은, 옆에서 동료인 2번 재료, 3번 재료들이 얼마나 많이 들어가서 설쳐대든 말든 철저하게 독고다이 마이웨이로 아무 간섭도 영항도 받지 않고 자기 할 일만 독립적으로 수행해야 한다는 기계적인 법칙을 말합니다.

The linearity assumption states that the change in the response $Y$ associated with a one-unit change in $X_j$ is constant, regardless of the value of $X_j$.
그리고 두 번째 갑질인 '선형성(직선) 고집'은 한술 더 뜹니다. 이건 특정 재료 $X_j$ 를 딱 한 스푼(1단위) 더 넣을 때마다 최종 고기 맛 $Y$ 가 바뀌는 정도(기울기, 마진율)가, 애초에 그 재료를 10스푼 넣은 타이밍이건 100스푼 미친 듯이 들이부은 타이밍이건 상관없이 늘 변함없는 텐션으로 일정하게 뻣뻣한 일직선을 유지해야 한다고 우기는 똥고집입니다.

In later chapters of this book, we examine a number of sophisticated methods that relax these two assumptions. Here, we briefly examine some common classical approaches for extending the linear model.
나중에 뒤쪽 챕터 교재로 넘어가면, 이렇게 답답한 꼰대 같은 두 족쇄 가정을 마사지로 시원하게 살살 풀어제껴 버리는 굉장히 똑똑하고 세련된 테크닉들을 잔뜩 배울 예정입니다. 하지만 지금 당장은, 이 뻣뻣한 구닥다리 선형 모델의 생명줄을 강제로 억지로 늘리고 뜯어고쳐 확장하는 가장 흔한 '고전 클래식 야매 수술법' 몇 가지를 살짝 맛만 보고 넘어가겠습니다.

## Removing the Additive Assumption (가법성 고집 부수기: 나 홀로 덧셈은 틀렸다! 시너지 효과의 등장)

In our previous analysis of the `Advertising` data, we concluded that both `TV` and `radio` seem to be associated with `sales`. The linear models that formed the basis for this conclusion assumed that the effect on `sales` of increasing one advertising medium is independent of the amount spent on the other media.
아까 꿀 빨았던 `Advertising(광고비)` 데이터 추리 쇼로 돌아가 봅시다. 우리는 그 장부를 털어보고 "오, `TV` 광고랑 `radio` 광고 이 두 놈 쌍두마차가 물건 `sales(판매량)` 대박을 터뜨리는 일등 공신이구만!" 하고 결론의 축배를 들었죠. 그런데 이 결론을 떠받들고 있던 단순 선형 모델 녀석은 속으로 아주 바보 같은 상상을 하고 있었습니다. 특정 광고 하나(예: TV)에 돈을 부어서 올라가는 판매량 펌핑 효과는, 다른 광고 파트너(예: 라디오)에 돈을 펑펑 쓰건 10원도 안 쓰건 철저히 독립적으로 아무런 마법 작용도 주고받지 않는다고 맹신한 겁니다.

For example, the linear model (3.20) states that the average increase in `sales` associated with a one-unit increase in `TV` is always $\beta_1$, regardless of the amount spent on `radio`.
즉, 멍청한 선형 공식 (3.20)의 논리에 따르면, `TV` 에 예산을 1단위 더 부을 때마다 튀어오르는 판매량 보너스 수익률은 라디오 쪽에 돈을 얼마를 퍼붓고 자시고 간섭 1도 없이 언제 어디서나 그저 뚝심 있게 항상 $\beta_1$ 이라는 고정 수치만 딱딱하게 뽑아낸다고 강변하는 꼴입니다.

However, this simple model may be incorrect. Suppose that spending money on radio advertising actually increases the effectiveness of TV advertising, so that the slope term for `TV` should increase as `radio` increases.
하지만 곰곰이 상식적으로 잔머리를 굴려보세요. 실전 장사판에서 이게 말이 됩니까? 라디오 광고로 동네방네 바람을 미리 싹 잡아놓으면(돈을 쓰면), 그 떡밥 덕분에 사람들이 나중에 TV에서 같은 제품 광고를 볼 때 훨씬 훅 빠져들어 TV 광고 타격감 효율이 원래보다 몇 배는 더 거대하게 폭발할 수도 있지 않나요? 즉, 라디오(`radio`) 예산을 뿌릴수록 TV(`TV`) 쪽 수익률 점수(기울기) 파츠도 덩달아 같이 폭등하며 버프를 받아야 정상이라는 소리입니다!

In this situation, given a fixed budget of $\$100,000$, spending half on `radio` and half on `TV` may increase `sales` more than allocating the entire amount to either `TV` or to `radio`.
만약 이 찰떡궁합이 진짜라면, 회장님이 옛다 하고 던져준 총예산 10만 달러를 무식하게 TV나 라디오 쪽 어느 한 우물에만 올인 몰빵해서 퍼붓는 짓거리보다, 차라리 두 매체에 맛깔나게 반반 치킨처럼 예산을 쪼개서 버무려 투입하는 것이 훨씬 더 소름 돋는 초대박 `sales(매출)` 상승 폭탄을 터뜨릴 수 있다는 무서운 장사 밑천 진리가 도출됩니다.

In marketing, this is known as a _synergy_ effect, and in statistics it is referred to as an _interaction_ effect.
이처럼 1+1 기적 수식이 2가 아니라 3, 길게는 100을 뚫어버리는 마법을... 장사하는 마케팅 바닥 인간들은 침 튀기며 **_시너지(Synergy) 효과_**라고 극찬합니다. 우리 같은 고상한 통계 학도들은 이걸 점잖게 **_상호작용(Interaction) 효과_**라고 이름표를 붙여 구별해 부르죠.

Figure 3.5 suggests that such an effect may be present in the advertising data. Notice that when levels of either `TV` or `radio` are low, then the true `sales` are lower than predicted by the linear model. But when advertising is split between the two media, then the model tends to underestimate `sales`.
아까 지나쳤던 그림 3.5를 보면, 저 광고 데이터 장부 구석구석에 이 괴랄한 시너지의 냄새가 짙게 깔려 있음을 엿볼 수 있습니다. 잘 보세요. TV나 라디오 어느 한 녀석의 체급(지원빵 예산 수준)이 비루하게 무너질 정도로 쪼들릴 땐, 현실의 찐 매출 성적표가 우리의 융통성 없는 직선 모델 예측치보다 훨씬 더 처참하게 밑바닥을 깁니다. 그런데 예산을 반띵해서 황금비율로 양 매체에 동시에 쪼개 태우기 시작하면? 갑자기 찐 매출이 폭주해서 우리 멍청한 일자 직선 모델이 진짜 매출 성적을 아득하게 과소평가(underestimate)하며 허우적대는 꼴불견을 볼 수 있습니다.

Consider the standard linear regression model with two variables,
이 상황을 타개하기 위해 두 개의 변수를 거느린 흔해 빠진 평범한 선형 회귀 기본기를 다시 한 번 우려먹어 소환해 봅시다.

**==> picture [121 x 10] intentionally omitted <==**

According to this model, a one-unit increase in $X_1$ is associated with an average increase in $Y$ of $\beta_1$ units. Notice that the presence of $X_2$ does not alter this statement—that is, regardless of the value of $X_2$, a one-unit increase in $X_1$ is associated with a $\beta_1$-unit increase in $Y$.
이 멍청한 공식의 룰북에 따르자면, 1번 친구 $X_1$ 이 눈치 없이 1단위 까불면서 증가할 때, 결승점 도착지 $Y$ 는 무조건 언제나 칼같이 $\beta_1$ 마진율 만큼만 오릅니다. 옆집 2번 친구 $X_2$ 가 뭐라 훼방을 놓든, 저 멀리서 얼마나 미친 듯이 점수를 올리건 간섭하건 말건 $X_1$ 의 몫 $\beta_1$ 스코어는 눈 하나 깜짝 안 하고 꿋꿋이 제 앞길만 가는 기계 톱니바퀴 같은 존재죠.

One way of extending this model is to include a third predictor, called an _interaction term_, which is constructed by computing the product of $X_1$ and $X_2$.
이 기계적인 멍청함을 탈피하고 좀비 로봇 구형 모델에 생기를 불어넣어 확장하는 기가 막힌 꼼수 하나가 있습니다. 바로 억지로 제3의 변이종 변수를 하나 연금술로 창조해 때려 박는 겁니다! 이름하여 **_상호작용 항(Interaction term)_**이라 불리는 이 돌연변이는, 기존의 $X_1$ 과 $X_2$ 두 녀석의 점수를 무식하게 서로 '곱셈(product, 곱하기)' 시켜버린 기괴한 껍데기 덩어리입니다.

This results in the model
이 미친 돌연변이를 집어던져 완성된 새로운 혼종 방정식 냄비는 이런 형태를 띱니다.

**==> picture [246 x 11] intentionally omitted <==**

How does inclusion of this interaction term relax the additive assumption? Notice that (3.31) can be rewritten as
도대체 저딴 정체불명 곱셈 돌연변이(상호작용 항) 하나 식에 욱여넣었다고, 어떻게 그 지독하고 뻣뻣한 '덧셈(가법성) 고집' 족쇄가 시원하게 깨져 풀려버린다는 걸까요? 의심스럽다면 방금 쓴 수식 (3.31)을 초등학교 인수분해 묶기 스킬로 슬쩍 이쁘게 정리해 다시 써 내려가 보죠.

**==> picture [250 x 25] intentionally omitted <==**

where $\tilde{\beta}_1 = \beta_1 + \beta_3 X_2$. Since $\tilde{\beta}_1$ is now a function of $X_2$, the association between $X_1$ and $Y$ is no longer constant: a change in the value of $X_2$ will change the association between $X_1$ and $Y$.
보이십니까?! 괄호로 곱게 묶인 저 새로운 요술 지팡이 마진율 $\tilde{\beta}_1$ (즉, $\beta_1 + \beta_3 X_2$) 뭉치를 째려보세요! $\tilde{\beta}_1$ 의 몸통 속에는 이제 죽일 놈의 1번 타자 $X_1$ 만 있는 게 아니라 **2번 녀석인 $X_2$ 의 수치가 대놓고 기생충처럼 파고들어 감염되어 있습니다!** 즉, 1번 타자 $X_1$ 과 타겟 $Y$ 의 끈적한 관계성(기울기 스펙)은 더 이상 뻣뻣하고 고정된 콘크리트 박석이 아닙니다. 옆집 녀석 $X_2$ 가 춤을 추고 날뛰며 값어치 스위치를 바꿀 때마다, 1번 놈과 $Y$ 의 로맨스 지수(마진율 $\tilde{\beta}_1$)도 덩달아 널을 뛰듯 함께 요동치게 되는 궁극의 유대 체계가 세팅된 것입니다!

A similar argument shows that a change in the value of $X_1$ changes the association between $X_2$ and $Y$.
똑같은 이치로 시점을 뒤집어서 묶어보면? 이번엔 1번 타자 $X_1$ 이 장난을 칠 때마다 2번 타자 $X_2$ 와 타겟 $Y$ 사이의 관계 스코어(마진)가 버프를 받거나 너프를 먹는 환상의 티키타카 마술도 완벽히 증명됩니다.

For example, suppose that we are interested in studying the productivity of a factory. We wish to predict the number of `units` produced on the basis of the number of production `lines` and the total number of `workers`.
조금 더 찰진 꿀잼 예시 공장 썰 하나 풀어보죠. 우리가 어느 불량 공장의 한 달 생산 능력(생산성)을 털러 암행을 나갔다고 칩시다. 우리의 목표 타겟은 한 달간 찍어내는 붕어빵 생산 개수(`units`)이고, 우리에게 주어진 힌트는 달랑 가동 중인 붕어빵 기계 틀의 개수(`lines`)와 땀 뻘뻘 흘리는 노동자 쪽수(`workers`) 딱 두 가지입니다.

It seems likely that the effect of increasing the number of production lines will depend on the number of workers, since if no workers are available to operate the lines, then increasing the number of lines will not increase production.
상식적으로 기계 틀(`lines`)을 공장에 100만 대 더 우겨넣었다 한들, 버튼을 누를 노가다 일꾼(`workers`)이 단비도 안 내린 듯 한 명도 안 보인다면 그 천문학적인 기계장치 증설 효과(생산량 버프 수치)는 처참하게도 절대 생산량 1원 어치도 펌핑 시키지 못하며 숨을 거둘 것입니다. 이 말인즉슨 당연하게도, 붕어빵 기계 장비의 증설 효과는 그 뒤에서 버튼을 손으로 누르고 돌릴 일꾼들 인원수 덩어리에 전적으로 구속되어 묶여 운명을 함께 하는 철저한 종속 신세라는 명백한 진리를 말해줍니다.

This suggests that it would be appropriate to include an interaction term between `lines` and `workers` in a linear model to predict `units`. Suppose that when we fit the model, we obtain
이 사실은 우리의 뇌리에 번쩍이는 직감을 꽂습니다! "아싸, 붕어빵 개수(`units`)를 예언하는 선형 공식 냄비 안에다 기계 틀(`lines`)과 노동자(`workers`) 둘이 뒤엉켜 뒹굴어 끈적하게 비벼진 **상호작용 항(돌연변이 곱셈 변수)** 하나를 불쏘시개로 짬뽕시켜 몰래 쑤셔 넣는 게 진짜배기 답안지겠구나!" 하명서 말이죠. 그리고 진짜 그 생각대로 기계 공식을 세팅해 돌려봤더니 다음과 같은 아주 요사스러운 모델 진단을 뽑아냈다고 합시다.

**==> picture [314 x 26] intentionally omitted <==**

In other words, adding an additional line will increase the number of units produced by $3.4 + 1.4 \times \text{workers}$. Hence the more `workers` we have, the stronger will be the effect of `lines`.
이 요사스러운 수식을 해석하자면, "오메! 붕어빵 기계 한 대를 더 들여놓으면 무조건 3.4개 빵을 뱉는 게 아니라, 공장에서 버티고 서 있는 **우리 노동자 형님들의 숫자(workers)에다 1.4배 가중치를 곱절로 곱한 미친 뻥튀기 부스터 액수만큼 생산 개수 버프**를 덤으로 마구마구 더 쏟아붓게 된단다!" 라는 경악할 만한 해설이 튀어나옵니다. 결론은 참으로 잔혹하고 솔직하게 귀결되죠. 결국 공장에 굴릴 노예(일꾼) 머릿수가 개떼같이 우글우글 많을수록 장비 증설발 기계빨(기계 틀 추가분) 효과가 전율이 돋도록 폭파하며 배가된다는 겁니다.

We now return to the `Advertising` example. A linear model that uses `radio`, `TV`, and an interaction between the two to predict `sales` takes the form
지겨운 공장 썰은 묻고, 다시 우리의 황금알 장부 오리지널 `Advertising(광고)` 놀이터 텃밭으로 복귀해 봅시다. 라디오(`radio`), 티비(`TV`), 그리고 이 둘이 죽고 못 사는 애증의 연인처럼 엉켜 붙은 끈적한 시너지 상호작용 항까지 도합 3종 세트를 몰빵해서 `sales(매출)` 를 점치는 궁극의 선형 혼종 모델은 이런 우아한 자태를 갖추게 됩니다.

**==> picture [296 x 26] intentionally omitted <==**

We can interpret $\beta_3$ as the increase in the effectiveness of TV advertising associated with a one-unit increase in radio advertising (or vice-versa). The coefficients that result from fitting the model (3.33) are given in Table 3.9.
여기서 돌연변이를 묵묵히 통제하는 파라미터 보스 $\beta_3$ 의 정체가 참 기막힙니다. 이 녀석을 풀이하자면 "어이, 라디오 광고 예산 한 푼 더 얹었을 때 거기에 연동 폭발해서 티비 광고 효율성 타격감이 덩달아 꼽사리로 뻥튀기 등업 충격파 먹는 그 엄청난 시너지 증가 체감량(역으로 티비 예산 늘려 라디오가 버프 먹는 것도 동일)" 이란 웅장한 타이틀로 해석될 수 있습니다. 이 전설의 혼합수식 (3.33) 모델을 기계에 넣고 신명 나게 버무려 갈아 돌려본 뒤 뱉어진 그 핏빛 계수 적합 결과물 파편 찌꺼기 추정치 스코어가 하단 표 3.9의 전단지에 적나라하게 현상 수배되어 있습니다.

|3. Linear Regression|3. Linear Regression|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept(절편)`<br>`TV(티비효과)`<br>`radio(라디오효과)`<br>`TV × radio(시너지폭탄)`|6.7502<br>0.248<br>27.23<br>_<_0_._0001<br>0.0191<br>0.002<br>12.70<br>_<_0_._0001<br>0.0289<br>0.009<br>3.24<br>0.0014<br>0.0011<br>0.000<br>20.73<br>_<_0_._0001|

**TABLE 3.9.** _For the_ `Advertising` _data, least squares coefficient estimates associated with the regression of_ `sales` _onto_ `TV` _and_ `radio` _, with an interaction term, as in (3.33)._
**TABLE 3.9.** `Advertising` _장부를 다시 한번 탈탈 털어, 순수 혈통_ `TV` _와_ `radio` _에다가 이 둘을 음흉하게 곱해버린 '상호작용 돌연변이 혼종'까지 얹어서_ `sales` _타겟을 무차별 융단 조준폭격한 최신식 최소 제곱 계수판 성적표. 무자비한 식 (3.33) 의 잔해물입니다._

The results in Table 3.9 strongly suggest that the model that includes the interaction term is superior to the model that contains only _main effects_.
아득바득 쌓아 올린 저 표 3.9 결과를 조용히 훑어보면 무릎을 탁 칠 만한 통찰이 박힙니다! 무조건입니다. 그간 돌연변이 요소를 쏙 빼고 순수하게 몸통 팩트 요인들, 즉 이른바 고리타분한 **_주효과(Main effects)_** 나부랭이 집단 구도들로만 심플하게 짜맞춰 굴려대던 허섭스레기 구형 모델보다, 방금 우리가 제조해 던져 넣은 이 시너지 상호작용 혼종 항을 품은 변종 모델 엔진이 타의 추종을 불허하며 압도적으로 개짱 킹왕짱 존엄성을 자랑하며 월등하다는 강렬한 체취 지표를 노골적으로 풍겨대고 제안해 댑니다.

The $p$-value for the interaction term, `TV` $\times$ `radio`, is extremely low, indicating that there is strong evidence for $H_a : \beta_3 \neq 0$. In other words, it is clear that the true relationship is not additive.
무엇보다도 곱하기 상호작용 항(`TV × radio`) 꼬리표에 딸려온 $p$-값 심판 수치가 지독할 정도로 끔찍이도 소름 돋게 바닥 저잣거리 심해 밑바닥으로 내팽개쳐 박혀버린 낮게 깔린 숫자인 걸 주목하세요! 참으로 이는 "비주류 대항 가설 $H_a : \beta_3 \ne 0$ (돌연변이 항은 개나 소나 쓸 데 없는 빈 껍데기가 아니다! 겁나 중요해!)"의 무한 철벽 주장 근력을 강력하게 철통 대변 지지 뒷받침해 주는 엄청난 알리바이 증거라는 점을 확성기 불며 폭로합니다. 다시 말해, 저 무지 몽매한 광고 매출 짬뽕의 진짜배기 본판 세상 인과 룰이란, 예전 꼰대 수식처럼 서로 손절치고 고립되어 아무 터치를 안 받는 그런 고고한 **"지긋지긋한 뻣뻣한 가법성 덧셈 관계판"이 아님이 명백명료 투명하게 진실 폭로되며 벗겨진 셈**입니다!

The $R^2$ for the model (3.33) is $96.8\%$, compared to only $89.7\%$ for the model that predicts `sales` using `TV` and `radio` without an interaction term.
이뿐인가요? 방금 적합시킨 융합체 괴형 수식 (3.33) 모델이 장부 데이터와 합을 맞추는 영혼의 조화도 퍼센티지! 즉, 영웅 메달 $\boldsymbol{R^2}$ **스코어가 무려 $96.8\%$ 이라는 극락의 영역 대를 달성 터뜨렸습니다!** 아까 예전에 융통성 없는 순수 꼰대 시절에 `TV` 랑 `radio` 순정 품종만 맹물처럼 밍밍하게 맹목적 예측 제물로 쓰던 상호 혼합 시너지 항체 따위 쏙 빼돌린 맹물 구형 모델이 굴러 찍어대던 수줍고 처참했던 $89.7\%$ 스코어 따위랑은 비교 자체가 불가침 영역 압살입니다!

This means that $(96.8 - 89.7) / (100 - 89.7) = 69\%$ of the variability in `sales` that remains after fitting the additive model has been explained by the interaction term.
이 대격변의 기적을 한 문장으로 간추려 해부 변역하자면... 저 무능한 구닥다리 맹물 덧셈형 모델 나부랭이로 돌렸을 때 도무지 지적 능력 딸려 해석도 못 하고 해명 실패해 뻘뻘 미제 구간으로 남겨뒀던 버려진 빚덩이 찌꺼기 변동 잔재 폭의 영역 분량 중, 무려 이 킹왕짱 곱셈 시너지 혼합 엔진 하나 덕분에 추가로 더 해명 입증 성공한 신규 커버 파이 지분 비율이 구체적으로 타점 무려 맹렬하게 $(96.8 - 89.7) / (100 - 89.7) = 69\%$ 에 달할 만큼 우주 폭발 등업 대성공 변혁 쾌거를 구가해 이루었다는 개벽의 의미를 내포 상기합니다.

The coefficient estimates in Table 3.9 suggest that an increase in TV advertising of $\$1,000$ is associated with increased sales of $(\hat{\beta}_1 + \hat{\beta}_3 \times \text{radio}) \times 1,000 = 19 + 1.1 \times \text{radio}$ units. And an increase in radio advertising of $\$1,000$ will be associated with an increase in sales of $(\hat{\beta}_2 + \hat{\beta}_3 \times \text{TV}) \times 1,000 = 29 + 1.1 \times \text{TV}$ units.
저 빛바랜 표 3.9의 산출 파라미터 조서 수치들의 숨은 뜻을 파고들면, "TV 팀이 광고판 예산을 딱 1천 불 더 쏘고 튀면 수확하는 판매 굿즈 이윤 물량은 일전 구닥다리 고정 마진율 따위를 다 찢고 저세상 등업 타점을 구가해 $(\hat{\beta}_1 + \hat{\beta}_3 \times \text{radio}) \times 1,000 = 19 + 1.1 \times \text{radio}$ 개 버프" 라는 소름 돋는 수익성 도출이 튀쳐나옵니다. 역으로 맞은편 라디오 그룹이 미친 척 1천 달러 추가 투입 베팅 강행 시, 맞받아 토해내는 판매 대금 수확 성과 역시 $(\hat{\beta}_2 + \hat{\beta}_3 \times \text{TV}) \times 1,000 = 29 + 1.1 \times \text{TV}$ 수량만큼 상승 동반한다는 기가 찰 연쇄 굴레 현상을 적나라히 읊조려 줍니다.

In this example, the $p$-values associated with `TV`, `radio`, and the interaction term all are statistically significant (Table 3.9), and so it is obvious that all three variables should be included in the model.
다행스럽게도 이 판에서는 우리 순정 메인 녀석들 `TV` , `radio` 는 물론이고 변종 돌연변이 친구 혼종 곱셈 항까지 모두 하나같이 죄다 들러붙은 꼬리표 $p$-값들이 지독할 만큼 소름 돋게 매우 낮아서 몽땅 통계적 대법관 공인 찐텐 '유의미 판정 타점' 위업을 달성해 거머쥐었습니다 (표 3.9 구경). 그러니 당연하게도 찍소리 말고 이 세 놈 삼형제를 모두 모델 수식 전장터에 죄다 깡그리 묶어 데려가 참전 포함시켜 투사하는 게 너무나 당연시되는 초명운 팩트 지론 구도입니다.

However, it is sometimes the case that an interaction term has a very small $p$-value, but the associated main effects (in this case, `TV` and `radio`) do not.
하. 지. 만! 종종 통계 야생 무법지대에선 참 어처구니없고 소름 끼치는 귀신 곡할 기현상 돌발 버그가 벌어지곤 하는데요. "어라? 짬뽕 곱셈 돌연변이 시너지 항체 단락은 엄청나게 핫한 반응으로 낮고 우월한 기염 $p$-값 통과를 거머쥐었는데, 저 돌연변이 자식을 구성하고 낳아준 애비 애미 몸통인 연원 주효과 오리지널 기장 변수들 (방금 예시로 치면 우리 불쌍한 본인들 원형체 `TV` 랑 `radio` 형님들 단일체 독단) 은 개뿔 별 도움도 안 되는 등신 수준의 멍청한 대형 수위 고배 $p$-값 낙제 지표를 떠안으며 쓰레기통 처박힐 위기에 몰리는 비현실 현상 구도 타이밍 구간"도 분명 간혹가다 뻔질나게 터지며 출몰 발현 터져 나옵니다.

The _hierarchical principle_ states that _if we include an interaction in a model, we should also include the main effects, even if the $p$-values associated with their coefficients are not significant._
그럴 땐 어쩌냐고요? 애비 애미를 버려야 할까요? 절대 아닙니다! 여기서 통계학계 신구 대부들이 엄중히 내려친 철통 원칙 헌법 강령 하나인 저 유명한 불문율 **_계층적 원리(Hierarchical principle) 철칙_** 이 하늘에서 번쩍 계시처럼 내려옵니다. 이 강령의 요지 교리 구절인즉, **"너희가 만약 모델 냄비 속에 불경한 쌍둥이 시너지 곱셈 상호작용 항 변이를 품고 포함 시켜 품기로 작정하고 포함했다면,... 설령 그 혼종을 낳아준 원초적 애비 애미 몸통 본판(주효과 원형 변수) 녀석들 본인 단일체의 꼬리표 $p$-값 점수 성적들이 처참한 휴지 조각 쓰레기 낙제 지수로 박살 났고 나불나불 유의미 가치가 찢겼다 한들, 절대로 패륜 짓 하지 말고 그냥 울며 겨자 먹기로 기필코 이 애비 애미 주효과 원형 몸뚱이마저 어거지로 모조리 회귀 모델 구도상 잔여 세트에 동봉 포함시켜 떠안고 가라!"** 라는 준엄한 명령 폭언 압박을 정곡으로 찔러 선점해 못 박아 규정합니다.

In other words, if the interaction between $X_1$ and $X_2$ seems important, then we should include both $X_1$ and $X_2$ in the model even if their coefficient estimates have large $p$-values.
돌려 말해볼까요? 만장일치로 $X_1$ 이랑 $X_2$ 놈 둘이 야릇하게 뒤엉킨 짬뽕 상호 기생 돌연변이 조합 시너지 자체 효과가 진짜배기고 대박 중요타 여겨 결단했다 치면... 정작 그 뿌리가 되는 1번 원조 $X_1$ 나 혹은 $X_2$ 자기 자신 단일 몸통 개체 성분 따위의 추정 모수 평가 꼬리표 성적이 형편없이 병맛 바보 점수 낙폭의 큰 $p$-값 오물 함정판 수렁에 빠져 뒹굴더라도 그냥 입 딱 닫고 무식하게 단일 몸체 원형 $X_1$, $X_2$ 그 둔탁한 녀석들마저 싸잡아 모조리 다 수식에 쑤셔 박으란 철규입니다.

The rationale for this principle is that if $X_1 \times X_2$ is related to the response, then whether or not the coefficients of $X_1$ or $X_2$ are exactly zero is of little interest.
왜 이런 패륜 방지 꼰대 불문율 법전을 찍어 눌렀을까요? 그 방어 기저 명분 변명의 근거는 단 하나. 만약 저 두 혼종 돌연변이 폭탄 $X_1 \times X_2$ 잔해 자체가 우리가 노린 목표 응답 반응 타겟을 뒤흔들며 영향력 커넥션 조종 구도를 분명 뻗고 있다면, 그 알맹이를 구성 뼈를 갈았던 애비 애미 구성체 $X_1$ 나 $X_2$ 본 단일 오리지널 찌꺼기 계수 값들이 현실상 0 수치로 귀결 뒈졌건 말건 그딴 하찮은 존재론적 성불 자잘한 의혹 이슈 따위는 전체 흐름에 코딱지만큼도 우리 하등 호기심 관심 가십거리가 못 된다는 치명적인 일침 팩트입니다.

Also $X_1 \times X_2$ is typically correlated with $X_1$ and $X_2$, and so leaving them out tends to alter the meaning of the interaction.
거기다 수식 해부학 관점에서도 저 혼합 이형 종양 무리 $X_1 \times X_2$ 는 전형적 태생 기질 한계상 지들 애비 애미 성분파인 $X_1$ 과 $X_2$ 본 구성체 덩어리와도 혈연적 결탁 상관도가 이리저리 교묘히 얽혀 끈끈하게 상호 구속 간섭을 칠 수밖에 없는 생태 팔자기 때문에, 만약 겁 없이 그 부모 주효과 원형체들을 구도 밖으로 추방 내팽개쳐 빼돌려 내버리면... 덩달아 연좌제로 엮여 애써 집어넣었던 저 음흉한 시너지 항 맹독 효과의 근본적인 원래의 찐 뜻풀이 의미 맥락 정체성 본질마저 무자비하게 나락 뒤틀림 훼손되며 변태해 버리는 끔찍 대형 오폭 사고가 발생하기 십상이라는 구조적 필연 파국 결말을 떠안기 때문입니다.

In the previous example, we considered an interaction between `TV` and `radio`, both of which are quantitative variables. However, the concept of interactions applies just as well to qualitative variables, or to a combination of quantitative and qualitative variables.
바로 아까 썰을 푼 TV 광고 파티 예제로 돌아가 보면, 우리는 죄다 돈냄새 나는 얌전한 숫자 덩어리형(정량적 변수) 구성물 분자 애들인 `TV` 와 그 뒤를 잇는 `radio` 끼리 치고받는 곱셈 진탕판 상호 시너지 놀음 국면만을 줄곧 째려봤어요. 그런데 아실랑가 모르겠지만 저 "곱하기 버프 시너지(상호작용)" 이란 신박한 꼼수 논리 세계관의 전파력 효험 범위는 문자로 기록된 삐딱한 녀석들(정성적 변수) 사이의 결합이건 혹은 숫자파와 문자파 이복형제가 지저분하게 뒤돌아 믹스로 뒤엉키고 버무려진 조합(정량+정성 짬뽕 편대) 국면이건 가리지 않고 한구석 빈틈없이 매양 아주 아름답게 적중 타격을 기가 막히게 입히는 막장 활용 치트키입니다.

In fact, an interaction between a qualitative variable and a quantitative variable has a particularly nice interpretation.
까고 말해 내막을 파보고 진실을 고하면, 뻑뻑한 숫자 덩어리(정량) 하나랑 글자 변수 나부랭이(정성) 딱 이 두 혼혈 이종 조합을 엮어 때려 만든 곱하기 상호 혼종 변이를 쳐다보면 우리 통계쟁이들이 스토리 보따리 썰 풀 땐 그 상황만큼 기가 막히게 입맛 돋우고 입에 착착 감기게 멋지고 나이스하게 해설 스토리가 풀리는 꿀잼 타이밍 도박판 판국도 따로 없습니다.

Consider the `Credit` data set from Section 3.3.1, and suppose that we wish to predict `balance` using the `income` (quantitative) and `student` (qualitative) variables. In the absence of an interaction term, the model takes the form
예전에 3.3.1 구석방에서 털어봤던 그 지겨운 `Credit(신용카드 서민 장부)` 기억하시죠? 그놈을 다시 끌고 와서 우리의 사랑스러운 '카드 빚(`balance`)' 타켓 금액을 예측해 보려 짱돌을 굴려본다 집어치겠습니다. 이번 무기로는 차가운 숫자 공격 `income(월급 돈 덩어리 숫자)` 하나랑 이질적인 문자 공격수 `student(야, 너 학생이냐 글자)` 패 두 장을 잡았습니다. 아직 그 시너지 곱하기 버프 상호 기생 돌연변이 요철 부품 따윌 탑재 안 하고 무식하게 밀고 나가는 재래식 맹물 구형 조립 공정에 따르면 도출 수식 외형 꼴 양태 윤곽은 다음과 같습니다.

**==> picture [322 x 79] intentionally omitted <==**

Notice that this amounts to fitting two parallel lines to the data, one for students and one for non-students. The lines for students and non-students have different intercepts, $\beta_0 + \beta_2$ versus $\beta_0$, but the same slope, $\beta_1$.
이 빙충맞은 공식 모델이 뜻하는 짓이 무언가 눈치 까셨나요? 이 짓은 그냥 거대한 데이터 점박이 도화지에다가 기계적으로 평행선 철로 두 줄, 즉 오로지 가련한 학생 무리 전용 철도선 하나와 회사원(비학생) 꼰대 구멍 철도선 한 줄 총 두 가닥 평행 직선이나 뻘뻘 긋는 구색 맞추기 헛짓거리에 불과하단 결론으로 직결 귀결됩니다. 이 두 평행 철도 노선은 출발점(절편) 높낮이, 즉 회사원 출발 바닥 마진이 $\beta_0$ 인데 반면 학생 스타트가 $\beta_0 + \beta_2$ 로 갭 차이가 존재하지만요... 애석하게도 달리는 언덕 오르막 산등성이 그 기울기 텐션 파워 $\beta_1$ 만은 양측 모두 획일적인 똑같은 각도로 뻗어 오르는 서러운 평행선 노예 처지 기만 운명 꼬리표죠.

This is illustrated in the left-hand panel of Figure 3.7. The fact that the lines are parallel means that the average effect on `balance` of a one-unit increase in `income` does not depend on whether or not the individual is a student.
이 기만적인 상황극이 그림 3.7 왼쪽 패널 도화지 캔버스 창에 친절하게 싹 다 까발려져 도식되어 그려 놓였네요. 저 직선 두 선분이 서로 마주 보며 나란히 평행하게 질주한다는 서글픈 수학적 침묵 진리 팩트는, "야! 돈(월급 `income`)이 깔짝 1단위 더 꽂힐 때마다 불어붙는 카드 빚 상승(`balance` 등락) 그 미친 오르막 마진 효과 위력 마진율 가중 기울기 체형 한해서만큼은 네가 망할 학생 신분충 쪼가리건 아니면 다 큰 꼰대 구실 비학생이건 아예 개뿔 1도 신경 간섭 안 해! 똑같아!"라는 안일무사 묵살 선언과 상동 격입니다.

This represents a potentially serious limitation of the model, since in fact a change in `income` may have a very different effect on the credit card balance of a student versus a non-student.
기겁할 일입니다. 이런 식탁 보급형 마찌 짬뽕식 기만 설정이야말로 우리 회귀 모델이 지닌 태생적인 최악질의 아주 잠재적 심각 지병 구석 고질 치명타 한계 맹점 하자 그 자체에 다름없음을 여실히 폭로 방조 전제합니다. 왜냐고요? 까놓고 팩트 실전 현실 바깥세상 등쌀선... 내 통장에 월급 돈 씀씀이(`income`)가 흔들릴 때 파생되어 미치는 체감 실질 카드 빚 긁는 폭주 타격 변동 마진 임팩트라는 건, 아직 피도 안 마른 대학생 떨거지 진영이 겪는 굴레랑 이미 닳고 닳은 비학생(사회인) 진영 애들이 먹는 족적이 뇌 구조 특성상 기겁할 정도로 완전히 현저히 상이하게 뻗어나 다르게 반응 뒤틀릴 우려 리스크 가망 여력이 한가득 농후 뻔히 예견되기 때문입니다.

This limitation can be addressed by adding an interaction variable, created by multiplying `income` with the dummy variable for `student`. Our model now becomes
아!! 바로 이 숨 막히는 고구마 100개급 장벽의 답답함 한계 한파를 시원하게 해결 보려면 어쩌면 되죠? 맞습니다. 아까 배운 마법, 즉 `income(월급 돈 숫자)`과 얄팍장치 속임수 튜닝된 더미 스위치 `student(학생 여부 지시등)` 두 단자를 서로 전선 합선 파지직 쇼트 시키는 '곱하기 상호작용 부팅 변수 항' 을 시원스레 우걱우걱 한 수저 짬뽕 양념 때려붓기로 추가 접목 가미시켜치며 탈출 승부수를 띄우면 족발 게임 끝납니다! 이리하면 우리의 초합금 변종 모델은 환골탈태 아래 형태와 같이 전단 무쌍하게 폼 체인지가 전개 수립 결체됩니다.

**==> picture [318 x 79] intentionally omitted <==**

Once again, we have two different regression lines for the students and the non-students. But now those regression lines have different intercepts, $\beta_0 + \beta_2$ versus $\beta_0$, as well as different slopes, $\beta_1 + \beta_3$ versus $\beta_1$.
다시금 게임 리셋입니다. 여전히 학생 진영과 비학생 일반 진영 두 녀석들의 별개 철도 노선 (회귀 선분) 2가닥 구도가 살아 등판한 건 매한가지지만요. 맙소사. 이젠 양측 노선이 단순히 출발 바닥 절편 높낮이($\beta_0 + \beta_2$ vs $\beta_0$)만 다른 하수 차별에 그치지 않습니다! 노선 오르막 등판 능력 상승률, 즉 절벽 각도 꼬라지인 기울기 수치조차도 $\beta_1 + \beta_3$ 대 $\beta_1$ 로 극명하게 등용문 각이 갈라져 비틀리며 격차가 나뉜 차별 폭을 잉태 발현 생성한 장관을 연출해 낸 것입니다!

This allows for the possibility that changes in income may affect the credit card balances of students and non-students differently. The right-hand panel of Figure 3.7
바로 눈앞 이 광활하게 뻗은 두 기울기의 각자도생 묘책 장치 덕분에, 드디어 우리 위대한 공식 세계관도 "오~ 월급(`income`)이 흔들릴 때 학생 녀석들의 빚 텐션 파장과 비학생 형님들의 카드 빚 체감 출렁임 여력이 서로 각자 다른 양태로 타격을 먹고 움직이겠구나~" 라는 야생의 가능성을 한껏 열어젖혀 수용할 수 있는 고오급 자유도를 얻게 되었습니다. 옆집 저기 도포된 그림 3.7의 오른쪽 우측 진영 우수 패널 창을 보시지요.

**==> picture [316 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
student<br>non−student<br>0 50 100 150 0 50 100 150<br>Income Income<br>1400 1400<br>1000 1000<br>Balance Balance<br>600 600<br>200 200<br>**----- End of picture text -----**<br>

**FIGURE 3.7.** _For the_ `Credit` _data, the least squares lines are shown for prediction of_ `balance` _from_ `income` _for students and non-students. Left: The model (3.34) was fit. There is no interaction between_ `income` _and_ `student`. _Right: The model (3.35) was fit. There is an interaction term between_ `income` _and_ `student`._
**FIGURE 3.7.** `Credit` _장부를 바탕으로 학생 무리와 비학생 군단 각각을 향한 월급_ `income` _과_ `balance` _간의 멱살잡이(최소 제곱선 예측) 판도. (왼쪽) 돌연변이 상호작용 따위 없이 무식하게 3.34 공식 돌린 꼬라지. 그냥 개노잼 획일적 평행선 남발. (오른쪽) 짜릿한 상호작용 혼종 항을 버무린 3.35 신형 모델! 이제야 월급과 학생 여부가 서로 부스팅 간섭을 일으켜 선과 각도가 요동치며 교차해 갈라집니다._

shows the estimated relationships between `income` and `balance` for students and non-students in the model (3.35). We note that the slope for students is lower than the slope for non-students. This suggests that increases in income are associated with smaller increases in credit card balance among students as compared to non-students.
이 우측 패널 도화지야말로 신형 모델 (3.35) 짬뽕이 구워낸 학생과 꼰대 아재(비학생) 간의 `income(월급)` 대비 `balance(빚)` 오르막 예측 파동의 얽힘 판도를 날 것으로 낱낱이 노출 까발려 증명해 보이는 결정판입니다. 주목할 점. 학생 무풍지대 노선의 기울기 마진 상승 각도가 비학생 아재들의 그것보다 훨씬 완만하게 기죽어 낮게 평탄 누워 깔린 처절한 지표 차단 각을 목도해 식별할 수 있습니다. 이게 대체 뭘 시사 파폭하느냐고요? 월급 소득이 폭등해 돈을 쥘 때, 그나마 우리 학생충 패거리 진영 애들 기둥뿌리에서 뻗어나가는 신용 잔고 카드 빚 수직 오르막 상승 치솟음 상승률 폭이 이외 철판 깐 일반 아재 그룹들에 비견 대조해 보면 좀 더 소극적이고 작은 규모치로 상대적 위축 결탁 선방하는 지표를 발동한다는 구체적 썰을 통계적으로 인증 뱉어내 해명하는 대목인 것입니다.

---

### Non-linear Relationships (비선형 관계: 직선의 족쇄를 끊은 곡선 마법)
* [📖 쉬운 해설판으로 이동하기](./3_3_2_1_non-linear_relationships/trans2.html)

예측 변수와 반응 재료 타겟 간의 밀당 관계 지수가 오직 뻣뻣한 일직성 꼬라지를 넘어 흐물흐물 물결 형상의 널뛰기 춤을 추는 '곡선 형태'를 띌 때, 우리 모델이 잔차도 돋보기 분석으로 어딜 어떻게 파고들 도려내 파악하고 다항식(Polynomial) 마법 회귀로 능소능대한 흐느적 유연 찰떡 맞춤 적합을 수행할 수 있는지 비급을 소개 누설합니다.

---

[< 3.3.1.1 Predictors With Only Two Levels](../3_3_1_qualitative_predictors/3_3_1_1_predictors_with_only_two_levels/trans2.html) | [3.3.2.1 Non-Linear Relationships >](3_3_2_1_non-linear_relationships/trans2.html)

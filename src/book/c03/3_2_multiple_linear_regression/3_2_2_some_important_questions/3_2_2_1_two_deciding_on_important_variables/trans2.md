---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2.2 Some Important Questions](../trans2.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/trans2.html)

# Two: Deciding on Important Variables

# 질문 2: 중요한 변수 결정 (어떤 놈이 진짜 알짜배기 영양가 있는 재료야?)

As discussed in the previous section, the first step in a multiple regression analysis is to compute the $F$-statistic and to examine the associated $p$-value.
먼저 지나온 섹션에서 우리가 땀 흘려 논의했듯이, 수많은 힌트를 섞어 찌개를 끓이는 '다중 회귀 분석'의 가장 첫 번째 관문은 무자비한 $F$-통계량 판사님을 호출해서 찌라시 같은 $p$-값 인증 도장을 들이밀어 검사받는 것이었습니다.

If we conclude on the basis of that $p$-value that at least one of the predictors is related to the response, then it is natural to wonder _which_ are the guilty ones!
만약 그 깐깐한 $p$-값 인증 필터를 무사히 통과하여 "우리가 넣은 재료 요원들 중에 (누군진 몰라도) 적어도 한 놈은 무조건 매출 상승의 진범(응답과 연관됨)이다!" 라는 확신에 도달했다면, 인간의 본능상 이젠 당연히 **_"그럼 도대체 범인(진짜 쓸모 있는 알짜 변수)이 누구야?!"_** 하고 색출해 내고 싶어 미칠 지경이 될 겁니다.

We could look at the individual $p$-values as in Table 3.4, but as discussed (and as further explored in Chapter 13), if $p$ is large we are likely to make some false discoveries.
가장 무식하고 직관적인 방법은 아까 표 3.4처럼 요원들을 일렬로 세워놓고, 개개인 얼굴에 붙은 개인 성적표($p$-값)를 1대1로 면담하며 찾아내는 짓일 겁니다. 하지만 방금 전 뼈아프게 경고했듯이 (그리고 먼 훗날 13장에서 지독하게 파헤칠 테지만), 만약 이 요원들의 쪽수($p$)가 너무 좀비 떼처럼 만만찮게 크다면 우린 "어? 너 점수 좋은데 합격!" 하면서 가짜 범인을 진범으로 오해(False Discoveries)하는 끔찍한 실수를 저지를 확률이 다분합니다.

It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors.
물론 100만분의 1 확률 기적처럼 우리가 투입한 모든 재료가 버릴 거 하나 없는 매출 상승의 황금 엑기스일 수도 있겠죠! 하지만 현실 장사판에서는 씁쓸하게도 10개 힌트를 넣으면 그중 **진짜 핵심 재료파 소수 정예(Subset)** 몇 놈만 매출을 끌어올리고, 나머지는 아무짝에도 쓸모없는 거품인 경우가 허다합니다.

The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as _variable selection_.
그래서 오합지졸들을 솎아내고, 오직 타겟 매출과 강력한 끈을 가진 그 진또배기 요원들만을 남겨 단 하나의 정예 부대(단일 모델)로 압축 및 편성하는 이 잔혹한 오디션 서바이벌 임무를 통계학에선 고상하게 **_변수 선택(Variable Selection)_** 과정이라 부릅니다.

The variable selection problem is studied extensively in Chapter 6, and so here we will provide only a brief outline of some classical approaches.
이 변수 선택 오디션 전략은 나중에 6장에 가면 머리에 쥐가 날 정도로 피 터지게 배울 예정이므로, 여기 지금 당장은 그저 맛보기로 '옛날 선배 학자들이 즐겨 쓰던 3대 클래식 오디션 기법'의 간략한 윤곽 정도만 훑어보겠습니다.

Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors.
통계학자들의 가장 순결하고 이상적인 로망은 이렇습니다: "그냥 재료들을 넣고 뺄 수 있는 모든 경우의 수 조각(부분집합)들을 죄다 바꿔 끼워가면서 미친 듯이 수많은 잡탕 모델들을 전부 다 끓여본 다음, 다 맛(평가)을 보면서 고르면 되지 않을까?"

For instance, if $p = 2$, then we can consider four models: (1) a model containing no variables, (2) a model containing $X_1$ only, (3) a model containing $X_2$ only, and (4) a model containing both $X_1$ and $X_2$.
가령 우리 재료가 $X_1$(마늘), $X_2$(파) 딱 2개($p=2$)뿐이라고 쳐보죠. 그럼 기껏해야 4접시만 요리하면 됩니다! (1) 맹물 냄비(아무것도 안 넣음), (2) 마늘만 넣은 탕, (3) 파만 넣은 탕, (4) 둘 다 썰어 넣은 영양탕.

We can then select the _best_ model out of all of the models that we have considered.
그러고 나서 이 4가지 요리(모델)를 쭉 펼쳐놓고 점수를 매겨 **제일 킹왕짱 맛있게 구워진 베스트 탑 티어 모델 접시** 하나를 최종 선택해 집어 들면 그만입니다.

How do we determine which model is best?
그럼 그 접시들 중 어느 게 가장 '베스트'인지는 심사위원들이 무슨 수로 판별할까요?

Various statistics can be used to judge the quality of a model. These include Mallow's $C_p$, Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^2$.
요리의 퀄리티를 평가하는 맛 칼럼니스트들의 지표는 다양합니다. 여기엔 훗날 배우게 될 맬로의 $C_p$(Mallow's $C_p$), 너무나도 유명한 아카이케 정보 기준(AIC), 베이지안 정보 기준(BIC), 그리고 나쁜 재료를 채우면 오히려 페널티를 벌점으로 주는 깐깐한 수정된 $R^2$(Adjusted $R^2$) 같은 화려한 점수표들이 동원됩니다.

These are discussed in more detail in Chapter 6.
(이 무서운 점수표 채점 방식들은 6장에 가면 아주 질리도록 다룰 예정입니다.)

We can also determine which model is best by plotting various model outputs, such as the residuals, in order to search for patterns.
또는 기계적인 점수에만 의존하지 않고, 모델이 뱉어낸 찌꺼기 잔반(잔차, Residuals) 기록물 도화지를 직접 시각 폭격 그래프로 이리저리 그려보며 직관적인 불량 패턴을 잡아내 걸러내는 장인의 방식도 있습니다.

Unfortunately, there are a total of $2^p$ models that contain subsets of $p$ variables.
자, 로망은 예쁩니다. 하지만 불행히도 현실은 잔혹합니다. 변수(재료)가 $p$ 개 있을 때, 넣고 빼서 만들 수 있는 경우의 수 냄비(부분집합 모델)는 자그마치 수학적으로 **$2^p$ 개**나 폭증하게 됩니다!

This means that even for moderate $p$, trying out every possible subset of the predictors is infeasible.
이건 무슨 뜻이냐? 변수 개수가 아주 살짝만, 진짜 적당히만 고개를 들어도, 그걸로 조립 가능한 모든 경우의 수 조합 요리 냄비를 전부 다 불 위에 올려 끓여보고 평가하겠다는 짓거린 인간의 수명을 깎아 먹는 **'물리적 불가능(Infeasible)'** 삽질이 된다는 뜻입니다. 

For instance, we saw that if $p = 2$, then there are $2^2 = 4$ models to consider.
방금 전 마늘과 파, 변수가 단 2장($p=2$)일 때는 꼴랑 $2^2 = 4$ 잔의 냄비만 끓이면 됐죠. 아주 귀엽고 만만합니다.

But if $p = 30$, then we must consider $2^{30} = 1,073,741,824$ models! This is not practical.
그런데 만약 우리 수중에 재료가 고작 스물에서 열 개 보탠 30개($p=30$) 쯤 던져졌다고 해보죠. 그럼? 맙소사! 우린 $2^{30} =$ 무려 **10억 7,374만 1,824개** 가 넘는 이 미친 조 단위의 모델 경우의 수 냄비를 하나하나 다 컴퓨터로 적합시켜보고 평가해야 합니다! 이건 슈퍼 컴퓨터도 짜증 나서 폭파될 짓입니다. 전혀 실용의 "실" 자도 못 꺼낼 비현실적 코미디죠.

Therefore, unless $p$ is very small, we cannot consider all $2^p$ models, and instead we need an automated and efficient approach to choose a smaller set of models to consider.
결론 땅땅! 만약 당신의 $p$(변수 힌트 마릿수)가 진짜 다섯 손가락 안에 꼽힐 만큼 좀도둑 무리가 아니라면, 모든 경우의 수($2^p$ 개)를 탐색하겠다는 노가다 로망은 빨리 접으세요! 그 대신 우리는 똑똑한 기계의 힘을 빌려, 그 거대한 바다에서 **자동적이고 매우 효율적으로 '볼만한 모델들만 쏙쏙 좁혀서 골라내 간보는' 똑똑한 지름길 접근법**이 절실하게 필요해집니다.

There are three classical approaches for this task:
바로 이 억겁의 탐색 과정을 획기적으로 줄여줄 3가지 '고전적인 탐색 지름길(클래식 알고리즘)' 선배들의 꿀팁 비기 세트가 존재합니다!

- _Forward selection_ (전진 선택법, 밑바닥에서 야금야금 한 놈씩 줍기).
We begin with the _null model_ — a model that contains an intercept but no predictors. We then fit $p$ simple linear regressions and add to the null model the variable that results in the lowest RSS. We then add to that model the variable that results in the lowest RSS for the new two-variable model. This approach is continued until some stopping rule is satisfied.
_전진 선택법_ 은 이렇게 움직입니다. 완전 텅 빈 맹물 냄비인 **영 모델(Null Model, 기본 절편 매출 말고는 힌트 재료 아무것도 안 넣음)**에서 산뜻하게 출발합니다! 밖에서 대기하던 $p$ 명의 멤버 후보들에게 일일이 단둘이서만(단순 선형 회귀) 훈련을 시켜보고, 그중 오차 찌꺼기(RSS)를 가장 극적으로 제일 밑바닥으로 낮춰주는 '최우수 에이스 1번'을 맹물에 극적으로 탑승 합격시킵니다. 이어서 이미 1번이 탄 그 냄비에, 이번엔 밖에서 노는 애들 중 "저 1번 에이스랑 합을 맞췄을 때 가장 오차를 획기적으로 또 줄여주는" '신인 에이스 2번'을 골라 2인조 데뷔 팀을 짭니다! 이런 식으로 한 놈씩, 한 놈씩 차곡차곡 스카우트해 나가는 전략이며, "이젠 더 이상 뽑아봤자 영양가 없다!"라는 어떤 스톱룰(정지 규칙) 한도에 부딪힐 때까지 멤버를 계속 불려 나갑니다.

- _Backward selection_ (후진 제거법, 완전체에서 구멍 뚫린 폐급부터 하나씩 쫓아내기).
We start with all variables in the model, and remove the variable with the largest $p$-value — that is, the variable that is the least statistically significant. The new $(p - 1)$-variable model is fit, and the variable with the largest $p$-value is removed. This procedure continues until a stopping rule is reached. For instance, we may stop when all remaining variables have a $p$-value below some threshold.
이건 아까와 반대되는 냉혹한 구조조정 서바이벌 전략입니다! _해고(후진 선택) 데스게임_ 은 일단 갖고 있는 100명이건 1000명이건 모든 애들을 한 배(동일 모델 단위)에 죄다 밀어 넣은 풀(Full) 파티 상태에서 시작합니다! 그런 다음, 성적표를 쫙 스캔해서 $p$-값이 하늘 무서운 줄 모르고 제일 높은 놈(즉, 통계적으로 가장 쓰레기 안구 테러 유의미성이 없는 무능력 폐인 고문관 변수)의 목덜미를 잡아 즉각 해고해버립니다! 한 명 쫓겨나고 분위기 싸해진 $(p - 1)$ 인조 새 모델 파티에서 2차 평가를 돌린 뒤, 또다시 제일 무능한 구멍 파이를 솎아내 가차 없이 해고 통지서를 날립니다! 이 피의 숙청 작업은 멈춤 규칙 임계점에 다다를 때까지 끝없이 진행됩니다. 예컨대 "이제 배에 남은 생존자 요원들의 $p$-값은 전부 다 0.05 컷 아래의 개국 공신 꿀단지들이다!" 라며 만족스러운 피바람 종식이 다가오면 살육 작업을 스톱할 수 있습니다.

- _Mixed selection_ (혼합 선택법, 넣고 빼고 간 보기의 달인).
This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add variables one-by-one. Of course, as we noted with the `Advertising` example, the $p$-values for variables can become larger as new predictors are added to the model. Hence, if at any point the $p$-value for one of the variables in the model rises above a certain threshold, then we remove that variable from the model. We continue to perform these forward and backward steps until all variables in the model have a sufficiently low $p$-value, and all variables outside the model would have a large $p$-value if added to the model.
_혼합 선택법(Mixed selection)_ 이 녀석은 바로 전진의 꼼꼼함과 후진의 냉혹함을 섞어놓은 박쥐 같은 결합형 하이브리드 돌연변이입니다! 처음엔 전진법 형님처럼 맹물(무변수 모델)에서 시작해서, 똘똘한 녀석을 한 명 한 명씩 최우선으로 영입하며 배를 불려 나갑니다. 그런데 말입니다! 아까 끔찍했던 `Advertising` 라디오/신문 배신 때리기 예제에서 목격하셨죠? 어제 분명 스탯이 좋아서 뽑아둔 놈인데, 새로운 전학생 마이너 예측 파동 변수가 모델 안에 새로 편입 굴러들어 오는 순간, 갑자기 기존 구 공신 놈들의 입지가 병풍화되면서 $p$-값 점수가 미친 듯이 나락으로 떡락(숫자는 커지는 현상)하며 무능한 퇴물로 둔갑해 버릴 수도 있습니다. 이런 무임승차 이면 썩은 감자를 막기 위해 호시탐탐 경계를 늦추지 않습니다. 즉, 새로운 놈을 계속 영입하다가도, 어느 시점에 갑자기 내부에 있던 기존 사원놈 중 한 명이라도 $p$-값이 "어? 이 자식 선방 기준선 넘었네(임계값 초과)?" 하고 빨간불 스코어가 치솟아 오르면, 지체 없이 가차 없이 목을 쳐서(후진 제거법 발동) 모델 밖 방출 시장으로 내동댕이쳐 버립니다! 이처럼 은근슬쩍 새 멤버는 영입(전진)하면서 쓸모 퇴색된 놈은 내다 버리는(후진) 간 보기 스텝 작업을 쉼 없이 오가며 무한 뺑뺑이 루프 핑퐁을 칩니다. 이 징글징글한 루프는 모델 안에 있는 놈들은 전원 끄떡없는 초엘리트 낮은 $p$-값 방어막을 갖추고, 반대로 모델 밖 야생에 남은 찌꺼기 놈들은 감히 편입 추가 접수 시도해 봤자 죄다 거대하게 썩창이 난 허접 $p$-값 성적을 받아들게 되는, 양측 세계의 완벽한 수렴 평온의 닻에 다다르는 순간까지 아주 징글맞게 거동 순환되며 모델의 퀄리티를 최강 정예 짬뽕으로 연성해 냅니다.

Backward selection cannot be used if $p > n$, while forward selection can always be used.
여기서 작은 팁입니다요. 후진 제거법(Backward)은 일단 전 직원을 다 고용해 놓고 배에서 밀어버리는 방식이라, 애초에 채용해야 할 변수 쪽수($p$)가 회사 총알 관측량($n$)보다 더 거대해버리면 탑승 자체를 거부당해 첫판부터 시작도 못 하는($p > n$ 뻗음 불능) 치명적인 하자로 인해 쓰질 못합니다. 반면 전진 선택법(Forward)은 맹물에서 한 놈씩 차포 태우는 구조라 데이터 가뭄 폭망 환경 기조 상황 하에서도 변태처럼 생존하며 언제든 돌아갑니다!

Forward selection is a greedy approach, and might include variables early that later become redundant. Mixed selection can remedy this.
다만 전진 선택법 요 녀석은 눈앞의 이익만 좇는 쫌팽이 욕심쟁이(Greedy approach 단안 탐색) 알고리즘이라 치명적인 단점이 있습니다. 당장 요번 턴에 급한 불 끄기 제일 달콤한 미끼 변수를 덜컥 물어 얼리어답터처럼 조기 탑승시켰는데, 훗날 메타가 진행되다 보니 파티 안에서 그놈 자리가 완전 무쓸모 짐꾼 잉여(redundant) 나락으로 떨어져 버려도 빼박 못하고 끝까지 안고 가야 하는 골칫덩어리가 된다는 점이죠. 바로 이런 바보 같은 결함을 실시간 구조조정을 때리는 '혼합 선택법(Mixed)'이 영리한 찰싹 땜빵으로 구원 치유 보완해 줄 수단으로 군림하게 됩니다.

---

[< 3.2.2 Some Important Questions](../trans2.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/trans2.html)

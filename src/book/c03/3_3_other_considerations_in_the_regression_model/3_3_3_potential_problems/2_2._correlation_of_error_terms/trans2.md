---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3.3 Potential Problems](../trans2.html) | [3. Non-Constant Variance Of Error Terms >](../3_3._non-constant_variance_of_error_terms/trans2.html)

# 2. Correlation of Error Terms

# 두 번째 잠재적 문제점: 오차 항의 짬짜미 상관관계 (찌꺼기들 사이의 불법 뒷거래)

An important assumption of the linear regression model is that the error terms, $\epsilon_1, \epsilon_2, \dots, \epsilon_n$, are uncorrelated.
우리의 꽉 막힌 선형 회귀 모델이 목숨처럼 맹신하는 아주 중요한 철칙(가정)이 또 하나 있습니다. 바로 예측 실패로 뱉어진 오차 찌꺼기들 $\epsilon_1, \epsilon_2, \dots, \epsilon_n$ 이 철저히 남남이어야 한다는 겁니다. 즉, 자기들끼리 절대 눈빛 교환도 해선 안 되는 **'독립적이고 무관한(uncorrelated) 존재'**여야만 한다는 조건이죠.

What does this mean?
이게 대체 무슨 뚱딴지같은 소리일까요?

For instance, if the errors are uncorrelated, then the fact that $\epsilon_i$ is positive provides little or no information about the sign of $\epsilon_{i+1}$.
쉽게 말해, 찌꺼기들이 서로 진짜 생판 남이라면, 방금 전 1번 타자의 오차 $\epsilon_i$ 가 '플러스(+)' 방향으로 튕겨 나갔다는 사실 하나만 가지고는, 바로 다음 타자인 2번 타자의 오차 $\epsilon_{i+1}$ 가 плю스(+)로 갈지 Ма이너스(-)로 튈지에 대해 눈치챌 수 있는 힌트나 단서가 '단 1도 없어야(zero information)' 정상이라는 뜻입니다.

The standard errors that are computed for the estimated regression coefficients or the fitted values are based on the assumption of uncorrelated error terms.
왜 이게 그렇게 중요할까요? 우리가 그동안 피땀 흘려 계산해 낸 회귀 스펙(계수 추정치)이나, 오차 범위를 짐작 척도로 재는 그 잘난 '표준 오차(standard errors)'라는 방패 장비들 모두가 뼛속까지 바로 이 **"우리 오차 항들은 서로 абсолютно(완전) 뒷거래 없는 결백한 독립체들입니다!"**라는 순진한 망상(가정) 위에서 세워진 모래성이기 때문입니다.

If in fact there is correlation among the error terms, then the estimated standard errors will tend to underestimate the true standard errors.
만약 까놓고 봤더니, 이 오차 찌꺼기 녀석들이 무대 뒤에서 끈적하게 파벌을 형성하고 서로 '상관관계(짬짜미 결탁)'를 맺고 영향을 주고받고 있었다면 어떻게 될까요? 끔찍하게도, 우리가 계산기 두드려 알아낸 우리의 보안 방벽 '표준 오차' 수치는 현실 세계의 진짜 무시무시한 찐 표준 오차 장벽을 한참 얕잡아보고 **'턱없이 과소평가(underestimate)'**하며 축소 은폐하는 치명적 집계 버그를 터뜨리게 됩니다.

As a result, confidence and prediction intervals will be narrower than they should be.
결과적으로 어떤 참사가 벌어질까요? 우리가 허세 부리며 "이 정도 범위(구간) 안에는 무조건 정답이 있지롱!" 하고 쳐놓은 방어막, 이른바 **'신뢰 구간(confidence interval)'**이나 **'예측 구간(prediction interval)'**의 폭이 원래 마땅히 겁먹고 넓게 쳐야 했을 튼튼한 장벽보다도 훨씬 더 빈약하고 비좁게 쪼그라드는 환장할 사태가 벌어집니다.

For example, a 95% confidence interval may in reality have a much lower probability than 0.95 of containing the true value of the parameter.
예를 들면, 우리가 어깨 펴고 당당히 "95%짜리 절대 방어막 신뢰 구간이야!" 하고 선언했던 그 협소한 울타리가, 막상 뚜껑을 열고 실전을 치러 보면 안에 진짜배기 진리 파라미터가 들어 있을 찐 확률이 당초 호언장담했던 95% 턱밑에도 못 미치는 텅 빈 강정의 불상사가 벌어진다는 팩트입니다.

In addition, $p$-values associated with the model will be lower than they should be; this could cause us to erroneously conclude that a parameter is statistically significant.
설상가상으로 엎친 데 덮친 격, 모델 평가 꼬리표 통지서로 붙어 나오는 저 자존심 **$p$-값(p-values)**마저도 덩달아 거품이 꺼지며 진짜 정상 수치보다 훨씬 더 밑바닥으로 낮게 깔려 도출되는 환각 증세가 발동합니다. 이러면 무슨 일이 생기냐고요? 어중이떠중이 진짜 별 볼 일 없는 쓰레기 같은 힌트 변수(파라미터)들을 보고도 "오매! $p$-값이 바닥을 긴다! 이거 통계적으로 엄청 유의미한 초강력 쩌는 엑기스 힌트 구만!" 하고 착각 오판하여 넙죽 절을 하는 멍청한 코미디가 발생하게 됩니다.

In short, if the error terms are correlated, we may have an unwarranted sense of confidence in our model.
간단히 줄여 한마디로 요약하겠습니다. 오차 항들이 뒤에서 짬짜미로 묶여 있다면 (상관관계가 있다면), 우리는 이 빈약하고 하자투성이인 모델을 향해 몹시 황당하게도 **'전혀 근거도 없는 미친 똥고집 과대망상적 맹신과 과신(unwarranted sense of confidence)'**에 홀려 빠지게 된다는 소리입니다.

As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs.
이 환각 스노우볼이 어떻게 굴러가는지 아주 극단적인 바보짓 예시를 들어보죠. 우리가 엑셀을 만지다 정신줄을 놓고 "복사-붙여넣기"를 두 번 눌러서, 멀쩡한 장부 데이터를 의미 없이 통째로 2배로 불려 복제해 버렸다고 칩시다. 이러면 모든 관측치 점수와 그에 딸린 오차 찌꺼기들마저 완벽한 도플갱어 짝꿍(쌍)으로 연쇄 복제되어 묶이겠죠? 이것이 바로 궁극의 상호 상관관계(100% 동일 복제 결탁) 상태입니다.

If we ignored this, our standard error calculations would be as if we had a sample of size $2n$, when in fact we have only $n$ samples.
우리가 이 바보짓을 눈치채지 못한 채 멍청하게 계산기를 돌린다면? 현실의 진짜배기 알맹이 정보는 딱 $n$ 개 수준뿐인데, 우리 계산 로직은 마치 우주에서 새로운 신선한 정보 $2n$ 개 분량의 무적의 빅데이터 표본 부대를 조달 확보했다고 단단히 착각망상 환각을 빚으며 가짜 표준 오차 수치를 미친 듯이 쥐어짜 내 산정할 겁니다.

Our estimated parameters would be the same for the $2n$ samples as for the $n$ samples, but the confidence intervals would be narrower by a factor of $\sqrt{2}$!
자, 똑같이 뼈다귀 복제된 환영 $2n$ 개 허수 집단으로 계산을 때려도 우리가 얻는 회귀 기울기 파라미터 타점 본 자체 수치(추정치)는 변함없이 동일하겠습니다. 그런데!! 환상 빅데이터로 뻥튀기 부스트 착각 버프를 먹은 덕에, 정작 그 신뢰 구간 울타리 폭만큼은 어처구니없게도 예전 찐 $n$ 표본 시절 방어막 대비 무려 루트 2배($\sqrt{2}$) 비율씩이나 미친 듯 얄팍하게 압축 수축시켜 버리는 대참사 개그를 선보일 겁니다!

Why might correlations among the error terms occur?
도대체 저 망할 오차 항들 사이에 왜 자꾸 짬짜미 뒷거래(상관관계) 사달이 벌어지는 걸까요?

Such correlations frequently occur in the context of _time series_ data, which consists of observations for which measurements are obtained at discrete points in time.
이 드럽고 치사한 파벌 결탁 짬짜미 현상이 유독 징글징글하게 득실거리는 핫플레이스가 하나 있습니다. 바로 시간의 흐름을 쪼개 특정 날짜, 특정 시점마다 꼬박꼬박 스코어를 측정한 관측 장부 기록! 소위 통계 바닥에서 **_시계열(time series) 데이터_**라고 부르는 동네입니다.

In many cases, observations that are obtained at adjacent time points will have positively correlated errors.
상식적으로 생각해 보세요. 오늘 뽑은 관측수치와 바로 어제, 혹은 바로 내일 당장 등 아주 척 달라붙은 인접 시간대(adjacent time points)에 연달아 뽑힌 측정치들은 당연히 주변 환경 텐션이나 맥락의 영향을 유사하게 이어받아 찌그러질 테니, 이놈들이 뱉어내는 오차 찌꺼기들 역시 서로 양(+)의 방향으로 끈적하게 커플링 눈빛 교환 상관성을 가질 운명일 수밖에 없습니다.

In order to determine if this is the case for a given data set, we can plot the residuals from our model as a function of time.
그래서 우리 손에 쥐어진 장부 데이터가 이런 시간에 감염된 좀비(오차 상관성 짬짜미 결탁) 무리인지 스캐너로 감별해 내기 위해 아주 쌈박한 짓거리를 하나 하곤 합니다. 바로 멍청한 모델이 뱉어낸 오차 잔차(residuals) 찌꺼기 녀석들을 싹 쓸어 모은 뒤, 시간의 흐름(X축: 시간 순서)에 맞춰서 도화지 플롯(plot) 표면상에 흩뿌려 점 찍어서 줄을 세워 보는 겁니다.

If the errors are uncorrelated, then there should be no discernible pattern.
만약 이 오차 파편 놈들이 진짜 결백하고 서로 1도 상관없는 청정 무관성(uncorrelated) 요원들이 맞다면? 플롯 도화지 화면에 찍힌 그놈들의 상하 널뛰기 흐름 안에는 그 어떠한 식별 가능한 형태의 작전 지시파 음모 패턴도 전혀 보이지 않아야 팩트 정상입니다.

**==> picture [317 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ =0.0(서로 눈치 안보는 개썅마이웨이 찌꺼기 군단)<br>0 20 40 60 80 100<br>ρ =0.5(조금씩 앞사람 눈치를 슬슬 보는 찌꺼기들)<br>0 20 40 60 80 100<br>ρ =0.9(앞사람이 뛰면 똑같이 뛰는 광기의 카르텔 찌꺼기)<br>0 20 40 60 80 100<br>Observation(시간관측순서)<br>3<br>2<br>1<br>0<br>Residual(찌꺼기) −1<br>−3<br>2<br>1<br>0<br>Residual(찌꺼기)<br>−2<br>−4<br>1.5<br>0.5<br>Residual(찌꺼기) −0.5<br>−1.5<br>**----- End of picture text -----**<br>

**FIGURE 3.10.** _Plots of residuals from simulated time series data sets generated with differing levels of correlation $\rho$ between error terms for adjacent time points._
**FIGURE 3.10.** _시간차를 두고 옆에 붙은 오차 파벌 형제들끼리 얼마나 끈끈하게 뒷거래(상관관계 $\rho$)를 맺는지 척도(레벨)별로 조작해 만들어본 시계열 쓰레기장(잔차도) 투시 모델. $\rho$ 가 커질수록 점들이 지그재그 산맥을 타기 시작한다!_

On the other hand, if the error terms are positively correlated, then we may see _tracking_ in the residuals — that is, adjacent residuals may have similar values.
하지만 반대로 오차 찌꺼기 놈들이 양(+)의 방향으로 끈끈하게 전우애 상관관계를 맺고 들러붙은 상태라면 어떨까요? 이땐 찌꺼기들 잔차 표면에 뭔가 앞 선배 발자취 추세를 연달아 스토커처럼 편승 추적해 그리는 소름 돋는 **_트래킹(Tracking, 꼬리물기 추적)_** 흔적 양태가 노골적으로 등판합니다. 더 까놓고 말해, 바로 옆에 앞뒤로 다닥다닥 연달아 곁에 맞붙은 이웃 찌꺼기 놈들이 약속이라도 한 듯 전부 쌍둥이처럼 비슷비슷한 수치 레벨 점핑을 같이 하며 날뛰는 구역질 나는 담합 현상을 목도하게 된단 겁니다.

Figure 3.10 provides an illustration.
머리 아프니 그저 위에 도포 된 그림 3.10 지면 폭로 삽화 도면 기조를 두 눈깔 번쩍 뜨며 직관해 보면 설명은 끝납니다.

In the top panel, we see the residuals from a linear regression fit to data generated with uncorrelated errors.
그림 세 개 중 제일 꼭대기 층 첫 상단 패널 방면 도화지를 눈여겨보세요. 저긴 오차들이 서로 모른 척 아무 상관 짬짜미 무관성(uncorrelated errors) 0% 청정 조건 속에서 1차 선형 회귀 모의로 추출해 흩뿌려진 찌꺼기 파편 잔차 결과의 난장판을 보여 줍니다.

There is no evidence of a time-related trend in the residuals.
저곳 투영 잔차 분포 표면 바닥에는, "야, 시간이 가면 갈수록 찌꺼기들이 어떤 흐름 산맥 추돌 지표 추세 전조(time-related trend)를 이어나간다더라~" 하는 억지 작전 음모 패턴 따위는 눈 씻고 찾아봐도 단 1%의 증거 냄새조차 결백하게 부재함을 인정받습니다.

In contrast, the residuals in the bottom panel are from a data set in which adjacent errors had a correlation of $0.9$.
반면 맨 밑바닥 시궁창 층 제일 하단 배후 패널 요소 꼬락서니는 앞선 광경과 맞서서 참혹한 지옥의 전경을 보입니다. 이건 앞뒤로 연이은 찌꺼기 오차 파급 놈들이 서로 상관관계 수위를 무려 0.9라는 엄청나게 높은 극악의 끈끈함으로 묶어 놓은 채(correlation of 0.9) 강제 발생 조작 구동 시켜 내뿜은 잔차 찌꺼기 궤적 물웅덩이들입니다.

Now there is a clear pattern in the residuals — adjacent residuals tend to take on similar values.
자, 이 경우 찌꺼기 파편 도상 전개 표면상에 일련의 극명하고도 뚜렷 노골적인 파도 물결 패턴 작전 지시 구조가 확실히 뽀록나 보이지 않습니까? — 바로 다닥다닥 앞 선배 연이어 맞붙어 뛰쳐나온 곁 잔차 놈들이 하나같이 뒷거래한 듯 소름 돋게 흡사한 동급 수치 레벨고저(similar values) 수준층을 무리 지어 물결 타듯 집단 동기화 발동 떼창 짓거리를 하고 있다는 적나라한 고발입니다.

Finally, the center panel illustrates a more moderate case in which the residuals had a correlation of $0.5$.
마지막으로 그 한가운데 낀 2층 중간 허리 패널 형상은 앞선 두 대조 상황의 대략 절반 타협 여건쯤. 즉 앞뒤 찌꺼기 뒷거래 상관관계 짓이 0.5 척도 정도로 적당히 밍밍하게 교류를 튼, 아주 비교적 완만한 모범 온건 타협 사례 단편(more moderate case) 하나를 모사해 소략 삽화로 껴 넣은 중간지대입니다.

There is still evidence of tracking, but the pattern is less clear.
분명히 여기 중간층에서도 그 몹쓸 꼬리물기 스토커 연쇄 트래킹(tracking) 추적 현상의 발자취 파편 흔적 요소가 일말 도사리고 나타나는 건 부인할 수 없지만, 아까 0.9짜리 광기의 패턴 그림보다는 전체적인 산맥 형성 기조가 아무래도 한껏 상쇄되어 눈에 띄게 약화 퇴색되고 흐릿한 맹탕(less clear) 지표 양상 형국 모양새로 잦아들어 관찰 은폐 포착됨을 알 수 있습니다.

Many methods have been developed to properly take account of correlations in the error terms in time series data.
통계학자들도 바보는 아닙니다. 지금껏 유독 시계열 형태 분석 모델 바닥에서 골칫거리 전염병으로 산재하는 이 지긋지긋한 '오차 항 연관 요소 결탁병' 문제를 멱살 잡고 치료하거나 억지로라도 장부 계산 때 수용해 매만져 버리는 온갖 기상천외 고난이도 방도 기법 조달 창안 수단이 다각도 처방전으로 개발되어 채택 사용 중입니다.

Correlation among the error terms can also occur outside of time series data.
그런데 말입니다... 가장 기가 막히고 소름 돋는 무서운 사실은, 이 찌꺼기 오차 항 놈들의 은밀한 뒷거래 결탁 병(상관성 양태)은 유독 시계열 영토에만 국한 기생하는 게 아니라, 생판 딴 세상, 즉 시간 기록 장부 따위가 1도 존재 안 하는 허허벌판 일반적인 통상적 이방인 지대 밖 외벽 공간(outside of time series data) 등에서조차 시도 때도 없이 돌연변이처럼 돌발 등판 발발 전개할 저주받은 가망성을 다분히 품고 개방 노출되어 있다는 겁니다.

For instance, consider a study in which individuals' heights are predicted from their weights.
쉬운 예 하나 드릴게요. 어떤 변태 통계학자가 사람들의 '몸무게(weight)'를 힌트로 들쑤셔서, 그 상대방의 '진짜 키 덩치(height)' 수치를 단초 추정 예지해 내겠답시고 신체검사 징병 통계 실험 조사를 벌인다고 상상해 보세요.

The assumption of uncorrelated errors could be violated if some of the individuals in the study are members of the same family, eat the same diet, or have been exposed to the same environmental factors.
만일 실험하려고 긁어모은 표본 대상자 군락 일원들 중에, 피를 나눈 한집안 핏줄 유전자 식구 덩어리(members of the same family)들이 뭉텅이로 섞여 있다거나, 맨날 같은 급식소 식단(same diet)으로 배를 불리는 기숙사생 짬뽕 단체 그룹이 껴있다거나, 아예 어릴 적부터 판박이 동일 환경 공기질 방사선(same environmental factors) 궤적 속에 연달아 노출 전향 지배받던 쌍둥이 마을 인간 군상들 따위가 왕창 표본 통에 기생 포함돼 버린다면?? 기절초풍! 당연히 결과적 돌출 찌꺼기 오류 편차들도 서로 끈끈하게 상호 눈치를 보며 유전자 짬짜미 오차 독립 체제 구축 수급에 필패하는 그 태초 기저의 무관 독립성 가정 바탕 뿌리가 심각하게 균열 훼손 파탄 유린 기각 파괴(violated) 전락 위험에 위태 직면 놓일 몹시 치명적 사태 소지 수순 우려를 직간접적으로 초래 부추기게 됩니다.

In general, the assumption of uncorrelated errors is extremely important for linear regression as well as for other statistical methods, and good experimental design is crucial in order to mitigate the risk of such correlations.
잔소리 길었습니다. 일반적으로 이 '오차 찌꺼기 무관상관 독립 보존 확약 가정결백(assumption of uncorrelated errors)' 증명 룰은, 선형 회귀 나부랭이뿐만 아니라 이쪽 바닥의 숱한 고차원 통계 도입 체제 구사 설계판 위에서도 목숨과도 같이 최고 극도로 중차대한 일격 대장 분수령 지주 파워 급(extremely important) 절체절명 중요성을 지닙니다. 그 탓에 불가피하게 발목 잡는 저 더러운 '상관 오류 결탁병' 리스크의 위협 폭주를 제어하고 저감 완화 방어(mitigate) 도모 안전선 확보를 이룩하기 위해선, 그 모든 것의 시작 초석. 즉 태초부터 표본을 뽑을 때 똑똑하게 판을 짜고 룰을 설계하는 '초기 실험 셋업 역량(good experimental design)' 확립 착수 자체가 결코 그 어떤 잡다한 요령보다도 최고 대장격으로 무상무념 가장 1순위 긴요 필수 핵심 요소(crucial) 요목 대관 지분을 틀어쥔 생명줄임을 일깨워줍니다.

**==> picture [315 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Response Y Response log(Y)<br>998<br>975<br>845<br>605<br>671<br>437<br>10 15 20 25 30 2.4 2.6 2.8 3.0 3.2 3.4<br>Fitted values Fitted values<br>15<br>0.4<br>10 0.2<br>5 0.0<br>0<br>Residuals Residuals −0.2<br>−5 −0.4<br>−10 −0.6<br>−0.8<br>**----- End of picture text -----**<br>

**FIGURE 3.11.** _Residual plots. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. The blue lines track the outer quantiles of the residuals, and emphasize patterns. Left: The funnel shape indicates heteroscedasticity. Right: The response has been log transformed, and there is now no evidence of heteroscedasticity._
**FIGURE 3.11.** _(다음 장 예고편) 찌꺼기 투시도(잔차도). 왼쪽은 찌꺼기 폭발력이 우측으로 갈수록 나팔꽃(funnel)처럼 찢어지는 공포의 등분산성 파괴(이분산성)의 예. 오른쪽은 정답 Y값 멱살을 잡고 로그($\log$) 마취제로 강제로 뚝배기 틀어막아 재우고 돌렸더니 찌꺼기 널뛰기 이분산 병이 깜쪽같이 진정 완치 해독된 치유 광경 도면._

---

[< 3.3.3 Potential Problems](../trans2.html) | [3. Non-Constant Variance Of Error Terms >](../3_3._non-constant_variance_of_error_terms/trans2.html)

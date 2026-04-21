---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3. Non-Constant Variance Of Error Terms](../3_3._non-constant_variance_of_error_terms/trans2.html) | [6. Collinearity >](../6_6._collinearity/trans2.html)

# 4. Outliers

# 네 번째 잠재적 문제점: 이상치(Outlier) - 수직으로 튀는 미친 돌연변이

An _outlier_ is a point for which $y_i$ is far from the value predicted by the model.
통계 바닥에서 악명 높은 **_이상치(Outlier)_**란 과연 무엇일까요? 쉽게 말해, 우리가 정성껏 짜놓은 회귀 모델의 정상적인 예측 궤도에서, 타겟 정답인 $y_i$ (수직 Y축 방향) 값이 상식을 파괴하며 저 멀리 우주로 혼자 튀어나가 미쳐 날뛰는 돌연변이 점박이를 뜻합니다.

**==> picture [321 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20 20<br>−2 −1 0 1 2 −2 0 2 4 6 −2 0 2 4 6<br>X Fitted Values Fitted Values<br>6<br>6 4<br>4 3 4<br>Y 2 2 2<br>0 Residuals 1<br>−2 0 Studentized Residuals 0<br>−1<br>−4<br>**----- End of picture text -----**<br>

**FIGURE 3.12.** _(왼쪽)_ 빨간 줄은 또라이 점을 포함해서 꾸역꾸역 억지로 맞춘 적합선. 파란 점선은 그 미친 또라이 점을 가차 없이 응징해 삭제하고 다시 쾌적하게 맞춘 적합선. _(가운데)_ 잔차(찌꺼기) 플롯으로 까보니 저 미친 또라이(20번 점) 혼자만 둥둥 떠 있는 게 뻔히 들통남. _(오른쪽)_ 스튜던트화 잔차로 스케일링해 보니 저 돌연변이 혼자만 마의 6점 대역을 뚫고 폭주 중. 보통은 -3에서 3 사이 안에서 노는 게 정상임.

Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.
이런 불청객 미친 점박이(이상치)들은 도대체 왜 생겨나는 걸까요? 가장 흔하고 빡치는 이유는 바로 인간의 '뻘짓'입니다. 조교가 데이터를 타이핑하다가 0을 하나 실수로 더 눌러버렸거나, 실험 센서 기계 장비가 잠시 맛이 가서 헛소리 수치를 기록해 버리는 등 어처구니없는 데이터 수집 불량 사고로 툭 튀어나오기 일쑤죠.

The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier.
저기 위에 걸어둔 그림 3.12 도화지의 맨 왼쪽 창문을 보세요. 대열에서 한참 엇나가 혼자 하늘 높이 날아다니는 시뻘건 점 하나(20번 관측치)가 바로 이 바닥의 전형적인 극악 무도 '이상치' 또라이의 표본을 적나라하게 예시해 줍니다.

The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier.
저기 가로지르는 뻘건 실선은 저 미쳐 날뛰는 빨간 또라이 점까지 다 같이 끌어안고 어떻게든 수습해 보려고 억지로 짜맞춘 불쌍한 타협의 모델 적합선이고요. 밑에 깔린 파란색 점선은 분노한 우리가 저 또라이 놈을 완전히 색출해 삭제 처단해 버리고 나서, 나머지 정상인들끼리 쾌적하게 다시 쫙 그은 아주 훌륭한 진또배기 적합선입니다.

In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept.
그런데 참 묘한 일이죠? 막상 저 또라이를 삭제 처단하고 선을 다시 그어봤는데, 정작 뻘건 실선이나 파란 점선이나 각도(기울기)는 거의 눈치 못 챌 정도로 요지부동이고 출발점 높이(절편)만 콧구멍만큼 찔끔 내려갔을 뿐, 두 선이 거의 똑같이 겹쳐 있습니다! 즉, 저 미친 돌연변이를 삭제하든 말든 우리 모델 직선 뼈대의 멱살을 크게 흔들지는 못했다(little effect)는 뜻입니다.

It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit.
이게 의외로 이상치의 뻔한 클리셰 특징입니다! 예측 힌트($X$ 축, 좌우 위치) 자리는 평범하게 정상인 무리 한가운데 묻혀 있으면서, 혼자서 응답 정답($Y$ 축, 상하 높이)만 미친 듯이 미사일처럼 솟구쳐 위아래로 튀는 이런 류의 수직 상승 타격형 또라이 이상치 놈들은, 희한하게도 우리 회귀선 전체의 뼈대 줄기를 거칠게 휘어 꺾는 멱살잡이 능력(영향력)은 쥐뿔도 없는 경우가 태반입니다.

However, even if an outlier does not have much effect on the least squares fit, it can cause other problems.
"아싸! 그럼 회귀선 각도가 안 꺾였으니 저 또라이 점박이가 장부에 끼어 있든 말든 그냥 무시하고 넘어가도 되겠네?" 라고 생각했다면 큰 오산입니다! 당장 선의 각도 멱살은 못 잡았을지언정, 저 미친놈 한 마리가 우리 통계 성적표 단상 곳곳에다 똥물을 튀기며 엄청나게 심각한 딴지 걸기 버그(other problems)를 연쇄적으로 터뜨리기 시작합니다.

For instance, in this example, the RSE is $1.09$ when the outlier is included in the regression, but it is only $0.77$ when the outlier is removed.
예를 하나 들어볼까요? 방금 전 저 뻘건 또라이를 품어주고 억지로 선형계를 구동 시켰을 때 우리가 받아 든 [잔차 표준 오차(RSE, 찌꺼기들의 널뛰기 평균 척도)] 수치가 자그마치 $1.09$ 폭탄 텐션이나 됐습니다! 그런데 저 미친놈 한 마리만 핀셋으로 쏙 뽑아 처형하고 다시 돌렸더니 세상에... RSE 수치가 훅 꺼지면서 아주 쾌적한 $0.77$ 황금 스코어로 극렬히 줄어들며 진정되었습니다.

Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit.
이 RSE 폭발이 도대체 뭐가 문제냐고요? 우리가 그토록 환장하는 신뢰 구간 방어막 폭이나, 가설 검정 합격증인 위대한 '$p$-값' 판결 모두가 철저히 저 RSE 치수에 기대어 계산 산출되기 때문입니다! 즉, 저 같잖은 미친 돌연변이 데이터 단 한 놈이 끼어든 나비효과 탓에, 우리의 RSE가 뻥튀기 폭주 버그를 일으키고, 결국 모델 성과 전체의 신뢰도가 박살 나며 멀쩡한 변수가 탈락하고 썩은 변수가 붙는 등 억겁의 해석 오류 대참사 재앙 단초(implications)를 잉태하게 된단 소리입니다.

Similarly, inclusion of the outlier causes the $R^2$ to decline from $0.892$ to $0.805$.
같은 원리로 모델의 자존심이자 성적 증명서 스코어인 $R^2$ (결정 계수) 훈장 마크 역시, 저 미친놈 한 마리를 장부에 품은 죗값으로 원래 거뜬히 따낼 짱짱한 $0.892$ 만점을 다 까먹고, 어처구니없이 $0.805$ 따리로 처참하게 추락 너프 당하는 치욕을 당하게 됩니다.

Residual plots can be used to identify outliers.
그렇다면 우리 장부에 숨어든 이 악질 또라이 이상치 놈들을 어떻게 끄집어내 찾아 잡을 수 있을까요? 여기서도 어김없이 쓰레기장 투시경인 '잔차 플롯(Residual plots)'이 아주 요긴한 사냥 감식 도구로 열일하며 쓰입니다.

In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12.
당장 그림 3.12의 한가운데 떡하니 걸린 두 번째 창문(잔차 플롯 도화지)을 한 번 보세요! 웬 시뻘건 점 찌꺼기 놈 하나가 나머지 얌전한 정상인 찌꺼기 군중 대열 범주를 아득히 벗어나 혼자서 구름 위 저 멀리 대기권 밖으로 동떨어져 나대고 있는 꼬라지가 너무도 시원 명백하게 육안(clearly visible)으로 확보 식별 적발되지 않습니까?

But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier.
그런데 야생 실전 바닥에서는 이게 또 골 때립니다. 적발하긴 했는데... "도대체 찌꺼기 수치가 어느 선까지 튀어 올라야 이놈을 단순 실수 범주를 넘은 찐 미친 '또라이(이상치)' 범죄자로 단정 지어 사형 선고를 때릴 수 있을까?" 그 경계선 커트라인 판사봉을 두드리기가 너무 애매하고 주관적인 난관 딜레마에 부딪힙니다.

To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_, computed by dividing each residual $e_i$ by its estimated standard error.
이 골치 아픈 커트라인 딜레마를 쌈박하게 타파하기 위한 최상위 등급 기법이 하나 출동합니다! 그냥 날것의 잔차(찌꺼기 $e_i$) 크기를 곧장 생으로 도화지에 찍어 비교하는 원시적인 짓거리를 집어치웁니다. 대신 그 찌꺼기 스펙(수치)을 해당 모델의 추정된 '표준 오차'라는 척도로 산술 '나누기' 처형해 버려서, 모든 찌꺼기들의 덩치 규격을 아주 공평한 동일 선상의 표준화 스케일로 압축 치환해 버린 특수 변종 찌꺼기 무리를 무기 삼아 꺼내어 플롯을 그립니다. 우리는 이 진화된 찌꺼기들을 유식하게 **_스튜던트화 잔차(Studentized residuals)_**라고 치켜세워 부릅니다.

Observations whose studentized residuals are greater than 3 in absolute value are possible outliers.
자! 스케일을 동일 평준화시키는 이 스튜던트화 잔차 마법을 걸고 나면 드디어 판사봉을 때릴 절대적인 수학적 커트라인 룰이 튀어나옵니다! 통계 바닥의 불문율! **"스튜던트화 잔차 스코어의 절댓값 덩치가 마의 장벽인 '3' 타점을 뚫고 폭발해버린 관측치 놈들은, 다 필요 없고 죄다 목을 쳐도 무방한 극악무도 잠재적 또라이 '이상치(outliers)' 병균 덩어리일 확률이 농후하다!"**

In the right-hand panel of Figure 3.12, the outlier's studentized residual exceeds 6, while all other observations have studentized residuals between -2 and 2.
방어막 커트라인 3을 염두에 두고 가장 우측 끝 그림 3.12의 세 번째 잔차 플롯을 구경해 보시죠! 나머지 쩌리 정상 관측치 놈들은 죄다 얌전히 -2 와 +2 사이 박스권 대역 그물망을 벗어나지 못하고 순종적으로 갇혀 놉니다. 그런데 저 뻘건 또라이 한 마리 놈의 스튜던트화 찌꺼기 스코어 수치를 훑어보니 세상에나... 마의 장벽인 3은커녕 무려 구름 위 **'6'** 스탯 선을 뚫고 폭주하며 미쳐 날뛰는 돌연변이 광기를 유감없이 폭로하고 자빠져 있습니다.

If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation.
이렇게 덜미가 잡힌 또라이를 놓고 형을 집행할 차례입니다. 만약 우리가 "아, 이 병신 같은 놈은 보나 마나 실험 기계 센서가 맛탱이가 갔거나, 혹은 알바생이 졸다가 키보드 0 하나 더 누른 순도 100% 조사 녹음 불량 쓰레기 에러 데이터다!" 라고 찐하게 확신이 선다면? 해답 처방 솔루션은 제일 쉽고 통쾌합니다. 눈 딱 감고 그 줄(관측치 데이터) 자체를 장부에서 흔적도 없이 삭제(remove) 처단해 버리면 만사 해결 평화입니다.

However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.
하지만 잠깐!! 무지성 닥치고 삭제 참수형만이 능사는 아니니 조심해야 합니다! 어떨 때는 저 혼자 하늘을 뚫고 튀는 또라이 이상치가 단순 오타 실수가 아니라... 사실은 그동안 멍청한 우리 모델 설계자가 눈치채지 못하고 내다 버려 빼먹었던 진짜배기 초강력 핵심 누락 힌트(missing predictor 변수)의 존재를 격하게 분노로 알려주기 위해, 저렇게 억울하게 수치가 폭등해 고발하는 모델 내부 뼈대 결함(deficiency)의 SOS 폭로 신호일 수도 있으니까요. (함부로 죽였다가 찐 핵심을 날릴 수도 있음을 경고합니다!)

---

# 5. High Leverage Points

# 다섯 번째 잠재적 문제점: 높은 레버리지(High Leverage) 점 - 가로축에서 영향력 갑질하는 목소리 큰 깡패

We just saw that outliers are observations for which the response $y_i$ is unusual given the predictor $x_i$.
방금 4번 병통에서 우리가 뼈저리게 살펴본 저 **'이상치(outliers)'**라는 병신들은 기질이 확실했죠. $X$ 축 힌트 자리(예측 변수 구역) 베이스 캠프 자체는 엄청 평범하고 정상적인 동네에 머물고 있으면서, 정작 머리 위 $Y$ 축(타겟 응답점) 방향으로만 혼자 수직으로 미친 듯 튀어 올라 비정상 점핑($y_i$ is unusual)을 일삼는 수직 강하형 돌연변이 또라이들이었습니다.

In contrast, observations with _high leverage_ have an unusual value for $x_i$.
자, 그 녀석들과 완벽하게 정반대되는 성질머리를 가진 소름 돋게 치명적인 반대파 악질 돌연변이 쌍두마차가 등판합니다. 바로 **_높은 레버리지(High Leverage, 거대한 지렛대 파워)_** 점입니다. 이 녀석들은 $Y$ 축(정답) 따위가 튀는 게 아니라, 아주 기괴하게시리 $X$ 축 힌트 자리(예측 변수 $x_i$ 라인 좌표) 자체의 태생 위치를 혼자서 저 멀리 동떨어져 비정상적(unusual)인 구석 외딴섬에 처박고 홀로 고립무원을 즐기는 괴팍한 놈들입니다.

For example, observation 41 in the left-hand panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations.
말이 헷갈리신다면 그림 3.13의 맨 왼쪽 창문을 째려보세요! 저기 우측 끝자락에 왕따처럼 혼자 외롭게 처박혀 있는 뻘건 41번 관측치 놈이 보이십니까? 좌상단으로 튀었던 20번(이상치) 또라이와는 성질이 다르게, 이 41번 놈은 위아래(y축)로는 별로 안 튀었는데 유독 가로 좌표 **$X$축(예측 변숫값) 방향으로만 혼자 기괴할 정도로 다른 정상인 무리 동네를 아득히 벗어나 큰 수치로 돌출되어 있습니다.** 통계 바닥에서는 이런 녀석을 보고 "와, 이놈 레버리지(지렛대 파워, Leverage) 덩치가 엄청 크네!" 라고 평가합니다.

(Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.)
(참고로 방금 보신 [그림 3.13] 장부 텃밭은, 아까 갖고 놀던 [그림 3.12] 텃밭이랑 점 하나 안 틀리고 똑같은 오리지널 데이터 구도입니다. 다만 딱 하나, 이번엔 41번이라는 저 뚱뚱하고 덩치 큰 레버리지 악질 깡패 점 박이 한 놈을 억지로 추가 투하시켜서 판이 어떻게 꼬이는지 보여주기 위한 세팅일 뿐입니다.)

The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed.
저 도화지의 뻘건 실선은 저 우측 외딴섬 41번 깡패 점의 눈치까지 슬슬 보며 비위 맞춰 타협해서 그린 꾸역꾸역 1차원 최소 제곱선의 초라한 몰골이고요. 맞은편 파란색 점선은, 빡친 우리가 저 41번 깡패 놈을 멱살 잡아 광장에서 사형(삭제 removal) 시켜 쫓아낸 직후 나머지 정상인들끼리 평화롭게 그린 진짜 정상 궤도 찐 적합선입니다.

Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier.
자! 여기서 대박 반전 소름 구간입니다. 아까 이상치(20번) 놈을 발로 찼을 땐 선이 1도 안 움직였던 [그림 3.12]의 광경 기억하시죠? 그 그림과 방금 파란 점선과 뻘건 실선이 X자 모양으로 심각하게 크로스되며 아귀다툼 멱살잡이가 일어난 현 [그림 3.13] 이 두 개를 겹쳐 대조 관찰해 보십시오! 결론은 명명백백합니다! 저 수직충 거품 또라이 '이상치' 백날 날려버려봤자 끄떡도 안 하던 우리 선형 모델의 뼈대 기울기가... 가로축 X 구석에 조용히 짱 박힌 무거운 초거대 덩치 **'높은 레버리지 깡패(high leverage observation)' 한 마리를 날려버렸을 땐, 마치 지진파를 맞은 듯 모델 전체의 회귀선 기울기 뼈대 멱살 줄기가 근본부터 부러져 뒤틀릴 만큼 압도적이고 치명적 파멸 타격(substantial impact) 영향을 고스란히 처맞고 꺾여 버렸다는 끔찍한 파폭 차이의 기행**을 목도하게 됩니다!

In fact, high leverage observations tend to have a sizable impact on the estimated regression line.
실제로 바닥 현장에서도 이 X축 극단에 외롭게 동떨어진 '하이 레버리지(High leverage) 관측치' 형님들은, 마치 아주 긴 시소의 맨 끝 단에 홀로 올라탄 무거운 파워 뚱보처럼 엄청난 지렛대 멱살잡이 원리를 지닙니다. 그 탓에 그들 구석방에서 꼬물대는 조그만 움직임 수치 하나하나마저도 고스란히 전체 모델 추정 회귀선 각도를 뿌리째 뒤흔들어 휘젓는(sizable impact) 막강 깡패 권력 전횡 기질의 경향성을 다분히 띠고 있습니다.

It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit.
우리가 피땀 흘려 세워 올린 최소 제곱 도출선 뼈대가, 고작 구석에 처박힌 덩치 큰 이단아 깡패 점박이 한두 놈(a couple of observations)의 눈치나 보면서 그 기분 하나에 심하게 흔들리고 좌지우지 지배당한다면? 이건 솔직히 개심각한 재앙 근심 꼬라지가 원인 대두된 셈입니다! 왜냐하면 만에 하나 저 권력형 레버리지 깡패 점 자식한테 센서 고장 등 불상사가 묻은 '거짓 쓰레기 정보 에러'라도 포함돼 있었다면? 단 그 한 점의 오물 때문에 모델 뼈대 전체 합목적 적합의 운명이 깡그리 쓰레기로 무효화 패망(invalidate) 기각 낙인 찍혀버릴 수단 위험이 도사리기 때문입니다.

For this reason, it is important to identify high leverage observations.
네, 맞습니다. 바로 이와 같은 권력 서열 전횡의 불건전한 재앙 리스크를 차단하기 위해서라도 우리는 모델을 돌리기 전에 무조건 우리 장부 어딘가 구석 외딴섬에 숨어 지렛대 갑질을 준비 중인 **"고위험 뚱보 레버리지 점박이 놈(high leverage observations)"들부터 이 잡듯이 털어 미리 식별 색출해 내는 수색 작업이 그토록 극도로 중요하고 피나는 우선순위**인 겁니다!

In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations.
힌트 변수 X가 달랑 한 개인 심플 단순 회귀 동네 판에선, 사실 이 레버리지 깡패 놈들을 색출해 잡는 일이 그야말로 식은 죽 먹기 껌입니다. 별 볼 일 없어요. X축 숫자 범위만 눈깔 부릅뜨고 훑어보면서, "어? 남들 다 10~20 근처 평범한 동네에서 놀고 있는데 이 미친 놈 혼자 100이네?" 하고 정상 범주 대역을 넘어서 혼자 미친 수치(outside of normal range)로 이탈해 있는 기형 관측지만 콕 집어 골라내면 그게 다니까요.

But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors.
하지만 힌트(X) 변수가 2개 3개 늘어나 난장판이 된 다차원 다중 선형 회귀의 심해로 빠져들면 이게 기겁할 만큼 환장할 스텔스 은신 모래알 찾기로 둔갑 난이도가 상승합니다! 왜냐고요? 어떤 악질 깡패 점은 $X_1$ 좌표 값만 뜯어보면 남들 노는 지극히 정상 박스권 샌드박스 대역을 어기지 않고 아주 평범해 보이고, 또 $X_2$ 좌표 하나만 딱 뜯어봐도 조신하게 정상 범위 테두리 속(well within range)에 아주 잘 숨어 노는 것처럼 위장합니다. 그런데 막상!! 이 $X_1$ 과 $X_2$ 의 수치를 한데 뒤섞어 입체 다차원 종합 조합 구도(full set of predictors) 세트 관점에서 마주 보는 순간? 갑자기 그 기형적 위치의 돌연변이적 본색 비정상 이탈 스탠스가 뽀록나는 소름 돋는 특종 은신처 함정 관측치 놈들이 득실대기 시작하기 때문입니다!

An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$.
백문이 불여일견! 2개의 예측 변수 힌트($X_1, X_2$)가 쌍끌이하는 다중 회귀 도박판을 찍어낸 그림 3.13의 정중앙 가운데 창문 투시경 단면으로 한 번 건너가 시선을 꽂아 보십시오. 저게 바로 입체 스텔스 깡패의 만행 현장입니다!

Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range.
수많은 정상인 서민 관측치 족속들의 밀집 거주 분포 타점들은 가만 보면 다들 저 푸른 파란색 점선 타원형(blue dashed ellipse) 계란 모양 방호막 울타리 바운더리 안쪽에 옹기종기 뭉쳐서 순대 속 채우듯 곱게 잘 포섭돼 안착 안주해 살고 있습니다. 그런데 유독 저 시뻘건 관측치 한 놈의 자태를 보십시오! 무리들의 타원형 둥지에서 눈 돌아갈 만큼 동떨어져서 허허벌판 외딴 구석 섬(well outside range) 지대에 혼자 덩그러니 스텔스 미아처럼 처박혀 표류 기생 작전 중인 걸 확인할 수 있습니다.

But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point.
근데 이게 진짜 미치고 펄쩍 뛸 소름 구간입니다. 저 빨간 놈 좌표를 자세히 뜯어보면, 저 녀석의 가로축 $X_1$ 수치 하나만 놓고 잣대를 대면 절대 평범한 정상 서민들 대역 범주를 이탈한 비정상수치가 아니며, 마찬가지로 세로축 $X_2$ 단면 하나만 뜯어가 놓고 따로 검열해 봐도 기겁할 이탈 수치가 전혀 아닙니다! 결론은 뭡니다? 눈깔을 가리고 그저 $X_1$ 선 한 줄만 째려보거나, 혹은 $X_2$ 고도계 높이 줄 한 가닥만 따로 분리해서 멍청하게 검문소 검색만 쳐 돌렸다면, 우린 저 더러운 '고오급 초거대 뚱보 레버리지 깡패 점박이(high leverage point)'의 입체적 기만 은신 스텔스 돌연변이 기질을 끝끝내 눈치조차 못 채고 무능하게 통과 묵인 패스 시켜버리며 완벽히 헛발질 색출 작전 대실패(fail to notice) 참변을 맞았을 거란 절망 스펙 팩트입니다!

This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.
이 은명 스텔스 환장 버그의 고도 문제는 단순히 변수 두 개짜리 판거리보다, 더 머리 아프게 힌트 예측 변수 놈들이 3개 4개 이상으로 개떼 득실 넘쳐나는 고도 차원 다중 모델링 거대 세팅판 구단 국면에서 훨씬 더 극심하게 속수무책 치명 노골 지옥 난이도 도래 상황(more pronounced)으로 치닫기 십상입니다! 왜냐고요? 차원이 3D 4D로 넘어가 버리면 당장 여러분들 눈깔과 모니터로 동시에 직관해 파생을 구경 때릴 이 모든 입체 다차원 변동망 구도 데이터를 도식 쫙 깔아서 한 큐에 플롯 점 도화지로 동시 송출 표출 분별(plot all dimensions simultaneously)해 구경해 낼 그 어떤 쌈박한 시각적 식별 편법 수단 요령조차 원천 부재봉쇄 소멸당해 막혀버려 두 눈 뜨고 코 베이는 장님 신세가 되기 때문입죠.

In order to quantify an observation’s leverage, we compute the _leverage statistic_. A large value of this statistic indicates an observation with high leverage.
결국 이 놈의 눈뜬 장님 사태를 종식하고 스텔스 깡패의 실체를 객관적 숫자로 잡아내 분쇄 박살 계량화 채증 적발 퀀트(quantify) 때려버릴 구원 투수 계산법이 필요합니다. 그래서 우리는 각각의 점박이 놈 머리통 체급 위에다 등판 조명 조준경 수식, 이름하여 **_레버리지 통계량(leverage statistic)_** 이라는 저격 채점 스코어 지표 체계를 연산 산출해 낙인 박습니다! 당연히 산출된 이 숫자 요건 스코어 덩어리 타격($h_i$) 볼륨값이 무지막지하게 비대 창대 큰 수위로 찍혀 나올수록, 그 등급 표식을 단 놈이야말로 빼도 박도 못할 기형적 '초고출력 뚱뚱 깡패 다차원 외딴 고립 레버리지(high leverage)' 잠재 보유자 점박이임을 가리키는 사형선고 빼박 물증인 셈입니다.

For a simple linear regression,
일단 기본기 복습 차원 맛보기로, 고전 1차원 단순 선형 회귀판 구석의 1:1 대결 체제에서 그 레버리지 점수($h_i$)를 계측하는 순정 도출 마법 산식은 이렇습니다:

**==> picture [220 x 26] intentionally omitted <==**

**==> picture [318 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
2000 4000 6000 8000 12000 2000 4000 6000 8000 12000<br>Limit Limit<br>80<br>800<br>70<br>60 600<br>Age<br>Rating<br>50<br>400<br>40<br>30 200<br>**----- End of picture text -----**<br>

**FIGURE 3.14.** _(다음 병 예고편) 신용카드 데이터에서 힌트 변수끼리 판박이 짓거리를 하는 도플갱어 환장쑈 투시도. (왼쪽) 나이(`age`)랑 한도액(`limit`)은 자기 갈 길 가는 모범 변수들임. (오른쪽) 신용점수(`rating`)랑 한도액(`limit`) 놈들은 완벽히 거울 치료급으로 서로 베끼며 똑같이 널뛰는 악질 '다중공선성' 스파이 쌍둥이 구도를 노출 중._

It is clear from this equation that $h_i$ increases with the distance of $x_i$ from $\bar{x}$.
거창한 수식 기호의 껍데기를 걷어내고 수학 공식을 아주 또렷하게 째려보면 직관적 해답 본질이 숨어있습니다! 이 숫자 $h_i$ (레버리지 깡패 지수) 덩치는 정확히 무엇과 끈끈하게 비례해 같이 펌핑 스증 폭발 궤적을 치솟느냐? 바로 어떤 듣보잡 관측 타점 타격 부스 위치($x_i$) 좌표가 전체 정상 서민 진영 무리의 평범 안방 평균 군락 지점 원점($\bar{x}$) 마진으로부터 동떨어져 벌어진 물리 우주적 **외딴 갭 이격 거리 갭수(distance)** 가 멀리 멀리 아득하게 찢어져 유배 수렁 처박힐수록 철저하게 정비례 추종 폭주 연동하며 동반 증가(increases)하는 운명 공동체 구조임이 이 수식의 내막에 투명 아주 자명 적나라하게 해부 증명(clear)되어 도사립니다!

There is a simple extension of $h_i$ to the case of multiple predictors, though we do not provide the formula here.
뭐 여기서 수식 자랑 삼매경에 지루하게 빠질 필욘 없으니 기호 낙서는 생략하겠지만요. 힌트 변수 무리가 개떼처럼 많은 복잡한 다중 회귀 도박판에 구겨 넣을 용도로 아까 저 돌연변이 $h_i$ 깡패 지수 도출 뼈대 공식을 슬쩍 간편 튜닝 확장판(simple extension) 마개조 패치 시켜 구비한 다차원 추적용 레이더 수식 버전도 아주 잘 마련되어 있습니다.

The leverage $h_i$ is always between $1/n$ and $1$, and the average leverage for all the observations is always equal to $(p + 1)/n$.
어쨌든 이 전능하신 사냥 레이더 깡패 계측 스코어, 찐 투명 레버리지 수치 **$h_i$ 의 생태계 절대 불변의 섭리 법칙**을 두 개만 기억하십시오. 첫째, 그 어떤 미친 점이 와도 이 스코어 전투력 수치는 절대 $1/n$ 하한선부터 최상위 $1$ 상한선 수위 대역 박스권 포섭망 장막 범위를 초과 궤도 일탈 빗겨나지 못하는 강제 폐쇄(always between) 룰 지배하에 복속합니다. 둘째, 흩뿌려진 모든 세상 만물 점박이 관측치들이 가진 이 $h_i$ 파워 게이지 등급을 전부 싹 쓸어 모아서 평균 치기(average) 타점을 때려 내보면? 언제나 기적처럼 오차 0.1도 없이 칼같이 수학적 상수 **$(p+1)/n$ 이라는 통제 평균의 균형 절대값 늪지대 균형점(always equal)** 으로 귀속 종결 환원 맺음 된단 황홀한 고정 진리 수리 팩트가 존재합니다!

So if a given observation has a leverage statistic that greatly exceeds $(p+1)/n$, then we may suspect that the corresponding point has high leverage.
우린 여기서 사냥 가이드 확증 명분 진리가 반짝! 하고 머리를 때립니다. "야! 정상인의 평균 레버리지 기력 파워가 $(p+1)/n$ 정도라면... 어떤 수상한 놈 관측 점박이 서류를 스캔 찍었을 때 뱉어낸 $h_i$ 파워게이지 스코어가 이 평민 평균 기력 타점 $(p+1)/n$ 수준을 개 쥐뿔 아득하게 찌바르고(greatly exceeds) 월등히 솟구쳐 초과 미쳐 넘실대는 튀는 이상 현상을 목격 득템 터뜨렸다면???" 네, 바로 정답. 우리는 당장 몽둥이를 들고 "저놈! 필히 저 망할 좌표 점 궤적이 우리 모델 근간을 좀 먹는 파괴자 악질 권력 **뚱보 고위험 하이 레버리지(High leverage) 보유 끄나풀 깡패 첩자 놈이구나!!**" 라고 매서운 적발 저격 초강력 색출 의심의 철퇴 추궁 단도직입 단정(suspect) 의표를 찍어 누를 막강 정당 단초 지표를 손에 쥐게 되는 통찰인 것입니다!

The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus $h_i$ for the data in the left-hand panel of Figure 3.13.
모든 이론적 피 튀기는 수사학을 종결할 기가 막힌 사냥 종합 도면 증명판! 앞서 징글징글 봤던 왼쪽 패널의 숨은 깡패 41번 무리가 뛰어놀던 데이터 장부를 싹 다 긁어모아서 그린 도화지! 즉 제일 우측 창문 끝으로 눈을 돌려 [그림 3.13]의 맨 오른쪽 패널 요약 종합 포맷 전경판을 째려봅시다. 가로축엔 이놈들의 조폭 파워 깡패 지수($h_i$, 레버리지)를 깔고, 세로축 텐션에는 이놈들의 하늘 튀는 점프력 광기(스튜던트화 잔차, 이상치 정도)를 깔아 두 축으로 정조준 십자포화 플롯팅 산포 타점 도면을 시연 구비 방수(plot)해 투척시켜 보겠습니다!

Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination!
시선을 꽂자마자 저 쌍놈의 시키 41번 또라이 한 놈이 단연 이 모든 사냥터를 찢고 우측 상단 모퉁이에 홀로 아주 도드라지게 독선 비범(stands out)하게 등판 적발 돌출 노출됩니다! 보십쇼 저 위용! 저 씹새끼는 그냥 무거운 깡패 권력 지수($h_i$) 레버리지만이 기절할 만큼 역대급 오버 스탯 괴물 수치를 찍은 게 아닙니다! 동시에 세로축 미친 점프력인 '스튜던트 잔차 이상 수위'마저도 수직 높은 공중으로 치솟아 비범 타점 점유 도달을 기록 짬뽕하고 있습니다! 까놓고 병역 기재하자면? 이 41번 악질 스텔스 놈은 머리 위로 수직 돌연변이 등반 튀는 **"이상치(Outlier) 병신 또라이 특성"**과, 가로로 묵직하게 X축 멱살 압박 지렛대 갑질하는 **"초거대 레버리지(High leverage observation) 깡패 특성"**!! 이 두 개의 저주받은 극악 파괴 스택 오물 치명 디버프 악질 기질을 단 한 몸뚱아리에 쌍으로 몰빵 짬뽕 탑재 융합 섭렵한 진성 사탄 돌연변이란 판결의 소름 돋는 결과입니다! 이거야말로 선형 모델 적합계를 한 방에 수직 폭동 원폭 붕괴 유린 파탄으로 박살작살 낼 그 어느 것보다 **치명적이고 특출나게 개위험천만 궤멸적인 최악질 독극물 콤비네이션 무리수 악성 조합 덩어리(particularly dangerous combination)** 조우 사태인 발현입니다!!

This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.
참고로 이 잔혹한 통찰 도면 플롯 판결은! 아까 전 챕터 시절... 기껏해야 [그림 3.12] 바닥판에서 목 잘리고도 우리 선형 최소 제곱 밧줄 선 각도에 1도 상처도 파문 영향 기스 내역도 티끌 미미 미동 흡집조차 못 가했던 허접 수직충 찌꺼기 이상치 20번 나부랭이 새끼(observation 20)가 어째서 그토록 처참 병신 힘없이 쩔이 모델 회귀선 멱살 장악에 조잡 나약 허수아비 꿀밤 효력 빈수레 요란 급 적은 영향(little effect) 조작 여력 권력 무풍 참사 파멸 허당 실속 부재로 그쳤는지 그 숨겨진 진실 내막을 너무도 투명 시원 노골 사이다 까발려 입증(reveals) 정조준 폭로해 줍니다! 이유는 간단해요. 우측 끝 20번 위치를 째려보세요! 놈은 비록 세로 점핑 또라이 이상치 수위 기염은 토해냈을지언정... 그 뿌리 자리 가로축 X 멱살 깡패 전투력, 즉 $h_i$ (레버리지 텐션 권력) 자체가 거의 밑바닥 거러지 굼벵이 기어가는 찐따 수준의 빈약 최하 시공창 바닥 핫바지급 **낮고 약골 보잘것없는 잉여 등급(low leverage)** 무능 체급에 허우적 평민 머물고 포진해 서식 중이었기 때문이란 명쾌 확증 알리바이 해피엔딩 도출 팩트 폭격입니다!

---

[< 3. Non-Constant Variance Of Error Terms](../3_3._non-constant_variance_of_error_terms/trans2.html) | [6. Collinearity >](../6_6._collinearity/trans2.html)

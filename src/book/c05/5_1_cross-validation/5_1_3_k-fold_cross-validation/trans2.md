---
layout: default
title: "trans2"
---

# _5.1.3 k-Fold Cross-Validation_ 
# _5.1.3 궁극의 진화: k-폴드 교차 검증 (k-Fold CV)_

An alternative to LOOCV is _k-fold CV_ .
방금 전 우리가 배운 LOOCV("단 한 명만 감옥에 가두고 n번 뺑뺑이 돌리기")의 컴퓨터 막노동 지옥을 구해줄 현실적인 궁극의 구원자가 바로 이 _k-폴드 교차 검증(k-fold CV)_ 입니다.

This approach involves randomly dividing the set of observations into _k_ groups, or _folds_ , of approximately equal size.
이 녀석은 어떻게 동작하냐고요? 관측치 세트 전체 인원이 있으면, 이걸 한 명씩 쪼개는 미친 짓 대신 그냥 큼직큼직하게 대략 비슷한 덩치 길이를 가진 _k_ 개의 파벌 그룹(이 그룹 하나를 고상하게 _폴드(fold)_ 라고 부릅니다) 으로 무작위 조각을 내버리며 과감하게 시작합니다.

The first fold is treated as a validation set, and the method is fit on the remaining _k −_ 1 folds.
예컨대 10개로 쪼갰다 치죠. 첫 번째 턴에서는, 제1번 폴드 조각에 속한 무리들만 모조리 묶어서 '검증용 감옥'에 한방에 격리합니다. 그러고 나면 데이터의 잔여 병력인 나머지 _k −_ 1 (즉, 9개) 조각의 폴드 무리들을 죄다 긁어모아 훈련 세트로 합치고, 모델에게 피 터지게 훈련시킵니다.

The mean squared error, $\text{MSE}_1$, is then computed on the observations in the held-out fold.
모델 훈련이 끝나면, 그 첫판 내내 감옥 안에서 대기 탄 1번 폴드의 낯선 희생양 관측치 무리를 들이민 뒤 평균 제곱 오차, 즉 첫 턴의 에러 무더기 스코어 $\text{MSE}_1$ 을 계산해 털어냅니다.

This procedure is repeated _k_ times; each time, a different group of observations is treated as a validation set.
이 살벌한 조각 단위 훈련 절차를 아주 사이좋게 턴을 넘겨가며 총 _k_ 번 뺑뺑이를 돕니다. 판이 바뀔 때마다 각기 다른 번호표를 쥔 다음 폴드 그룹이 운 나쁘게 희생양(검증 세트) 으로 찍혀 감옥에 들어가고, 나머지는 또 훈련을 받죠.

This process results in _k_ estimates of the test error, $\text{MSE}_1$ _,_ $\text{MSE}_2$ _, . . . ,_ MSE _k_ .
이 서바이벌 뺑뺑이가 끝을 맺으면 우리는 피 묻은 에러 조각 파편들, 정확하게 $\text{MSE}_1$ 부터 막판 MSE _k_ 까지의 총 _k_ 개의 테스트 에러 추정 분량 성적표를 양산해 내게 됩니다.

The _k_ -fold CV estimate is computed by averaging these values, 
결과적으로 _k_ -폴드 CV라는 방식이 뽑아낸 최종 점수는 그냥 딱 저 _k_ 개의 점수판 부스러기 조각들을 모두 모아 '평균'을 갈겨 계산해 버리면 완성됩니다:

$$
\text{CV}_{(k)} = \frac{1}{k} \sum_{i=1}^k \text{MSE}_i \quad (5.3)
$$

Figure 5.5 illustrates the _k_ -fold CV approach. 
이러한 _k_ -폴드 뺑뺑이 교대근무 접근법의 살벌한 시나리오가 그림 5.5에 도해로 잘 나와 있습니다.

> 1In the case of multiple linear regression, the leverage takes a slightly more complicated form than (3.37), but (5.2) still holds. 
> 1 다중 선형 회귀 경기장이라면, 앞서 말한 레버리지의 계산 형태가 (3.37) 공식보다 아주 살짝 기괴하고 복잡한 형태로 트위스트를 타지만, 그래도 그 마법 지름길인 만능 공식 (5.2) 자체는 여전히 끄떡없이 든든하게 성립합니다.

**FIGURE 5.5.** _A schematic display of_ 5 _-fold CV. A set of n observations is randomly split into five non-overlapping groups. Each of these fifths acts as a validation set (shown in beige), and the remainder as a training set (shown in blue). The test error is estimated by averaging the five resulting MSE estimates._ 
**FIGURE 5.5.** _무려 5-폴드 CV를 돌리는 끔찍한 5등분 도식도입니다. n명의 불쌍한 데이터 부대원들을 5조의 겹치지 않는 파벌로 랜덤하게 박살을 냅니다. 이 다섯 조각 무리 중 하나가 턴마다 돌아가며 검증 감옥 부대(베이지색) 역할을 맡고 조리돌림을 당하며, 나머지 4/5 병력 전원은 훈련장 부대(파란색)가 되어 땀을 뺍니다. 그렇게 얻어 터진 5개의 턴별 예측 오차(MSE)를 평균 내어 최종적인 테스트 오차 방어력을 가늠합니다._

It is not hard to see that LOOCV is a special case of _k_ -fold CV in which _k_ is set to equal _n_ .
사실 조금만 머리를 굴려보면 아시겠지만, 이전에 배운 LOOCV(단일 관측치 제외기법)는 근본적으로 "폴드 팀의 갯수 _k_ 단위를 극단으로 올려 정확히 인원수 _n_ 명 마릿수와 똑같게 개별 세팅해 버린" _k_ -폴드 CV의 지독한 변태적 특수 케이스에 불과하다는 점을 쉽게 눈치챌 수 있습니다.

In practice, one typically performs _k_ -fold CV using _k_ = 5 or _k_ = 10.
그렇기에 학자들이나 데이터 사이언티스트들은 실전 필드에 나갈 때 무식한 LOOCV 대신, 관행처럼 타협하여 _k_ = 5 조각, 혹은 _k_ = 10 조각으로 그룹을 나누는 _k_ -폴드 CV를 가장 흔하게 애용합니다.

What is the advantage of using _k_ = 5 or _k_ = 10 rather than _k_ = _n_ ?
그렇다면 대체 극단적인 _k_ = _n_ (즉 1명 빼고 다 훈련시키는 LOOCV) 을 쓰지 않고 _k_ = 5 나 10을 쓰면 얻게 되는 꿀 떨어지는 장점이 과연 무엇일까요?

The most obvious advantage is computational.
가장 노골적이고 압도적인 이점은 바로 컴퓨터의 피로도를 낮춰주는 연산 스피드(computational cost) 측면에 있습니다.

LOOCV requires fitting the statistical learning method _n_ times.
LOOCV는 인원수 _n_ 명번을 온전히 죄다 다시 훈련(fitting) 시켜야 합니다. 데이터가 10만 명이면 10만 번 연산을 돌려야 하죠.

This has the potential to be computationally expensive (except for linear models fit by least squares, in which case formula (5.2) can be used).
이는 컴퓨터를 물리적으로 태워 먹고 폭파할 정도로 잠재적인 어마무시한 막노동 연산 비용 부담을 강제합니다 (물론 아까 말한 그 지름길 공식 (5.2)를 치트키로 써먹을 수 있는 최소 제곱 선형 모델 같은 경우는 예외지만 말입니다).

But cross-validation is a very general approach that can be applied to almost any statistical learning method.
하지만 애초에 이런 교차 검증이라는 고문 기법은 통계 전투 장비가 선형 모델이든 뉴럴네트워크든 어디에나 무난하게 던져 붙일 수 있는 범용 생존 전략이거든요.

Some statistical learning methods have computationally intensive fitting procedures, and so performing LOOCV may pose computational problems, especially if _n_ is extremely large.
안 그래도 복잡한 통계 기법(가령 서포트 벡터 머신, 딥러닝 등) 중엔 한 번 학습 장치를 가동하는 것만으로도 전기세를 뒤지게 잡아먹는 무거운 녀석들이 있는데, 이런 걸 가지고 가뜩이나 인원 _n_ 명수까지 바다처럼 넓은데 LOOCV 같은 걸 강행한다면...? 연산량이 미쳐 폭주하여 지구 종말의 계산 문제(computational problems) 를 부추기고 만듭니다.

In contrast, performing 10-fold CV requires fitting the learning procedure only ten times, which may be much more feasible.
대조적으로, 방금 이 10-폴드 CV를 사용하면 어떨까요? 인원이 10명이든 100만 명이든 모델 훈련은 그저 큼직하게 자른 '딱 10턴(열 번)' 만 고생해서 적합시키면 깔끔하게 게임이 끝납니다. 현업에서 정말로 훨씬 눈물 나게 현실적이고 실행 가능한(feasible) 가성비 최고의 꿀 타협안이죠!

As we see in Section 5.1.4, there also can be other non-computational advantages to performing 5-fold or 10-fold CV, which involve the bias-variance trade-off. 
이어지는 5.1.4 절에서 소름 돋게 파헤칠 테지만, 사실 이 5-폴드 나 10-폴드 CV를 돌리는 짓거리의 이점은 단순 연산 이득(빨라서 좋다)에만 국한되지 않습니다. 통계학 최강의 딜레마인 편향-분산 트레이드오프(bias-variance trade-off) 의 밀고 당기는 역학 관계 속에서 나타나는 '비-연산적인 깊은 이론적 이점' 역시 품고 있거든요.

The right-hand panel of Figure 5.4 displays nine different 10-fold CV estimates for the `Auto` data set, each resulting from a different random split of the observations into ten folds.
그림 5.4의 오른쪽 패널 면을 쳐다보시죠. 여긴 `Auto` 자동차 세트에 10-폴드 CV를 돌려댄 총 9개의 각각 완전히 다른 오차 추정 곡선 궤적 라인이 형형색색 수놓아져 있습니다. 이들은 전원을 무작위 10부대로 분할시킬 때 난수를 바꿀 때마다 각기 탄생한 아홉 빛깔 분할 결과입니다. 

As we can see from the figure, there is some variability in the CV estimates as a result of the variability in how the observations are divided into ten folds.
도표 형국을 보면 짐작하시겠지만, 도대체 멤버들을 어떤 운이나 기준으로 10조각의 파벌로 갈랐는지에 따른 분할 결과 파장 때문에 그 나타난 CV 추정치 스펙 선율들 상호 간에도 당연히 징그럽게 약간의 널뛰기 이격 변동성 편차는 필연 존재합니다.

But this variability is typically much lower than the variability in the test error estimates that results from the validation set approach (right-hand panel of Figure 5.2). 
그러나 명심하세요! 이 정도의 변동성은 저어~기 (그림 5.2의 우측 패널에 있던) 구닥다리 검증 세트 반반 쪼개기 접근법이 운에 따라 무차별로 토해내던 그 소름 끼치던 극단급 널뛰기 미친 편차 변동성에 비한다면, 통상 몹시 얌전하고 귀엽게 낮은 수준에 불과합니다.

When we examine real data, we do not know the _true_ test MSE, and so it is difficult to determine the accuracy of the cross-validation estimate.
우리가 오프라인 현실 세계에서 생명력을 지닌 진짜 데이터 실물을 만지며 분석할 적엔, 조물주가 아닌 이상 절대적인 신의 정답인 _진짜(true)_ 테스트 MSE 값이 본래 얼마였는지 결코 알 턱이 없습니다. 그리하여, 우리가 삽질해 추정한 이 교차 검증 척도의 추정치 정밀도가 대체 얼마나 기가 막히게 정확한지 그 진의를 가늠하기란 몹시 난해하죠.

However, if we examine simulated data, then we can compute the true test MSE, and can thereby evaluate the accuracy of our cross-validation results.
하지만 꼼수는 있죠. 우리가 랩에서 컴퓨터로 인위 조립된 시뮬레이션 데이터를 타깃으로 모의 조작 시험을 만지작거린다면? 그 판은 우리가 짠 거라 진정한 신의 에러 테스트 MSE가 얼만지 숨겨놓고 언제든 뽑아다 정답을 맞춰볼 수 있으며, 결국 우리의 이 CV 교차 검증이 도출해 낸 점수가 저 진짜 정답과 얼마나 놀랍게 맞아떨어지는지 그 예측 적중률 정확도를 발가벗겨 평가해 낼 수 있게 됩니다.

In Figure 5.6, we plot the cross-validation estimates and true test error rates that result from applying smoothing splines to the simulated data sets illustrated in Figures 2.9–2.11 of Chapter 2.
그래서 저기 그림 5.6에다가, 통계 전문가들은 예전 2장의 2.9~2.11 도표 그림에서 사골 울리게 써먹었던 인조 시뮬레이션 데이터 구장 벽면에 평활 스플라인(유연한 고무줄 곡선) 을 갖다 붙이면서 수집해 모은 CV 추정치 값과 진짜 신의 테스트 오차율 에러 값을 과감하게 한 장막 그림판에 때려 박아 그려 대조해 보았습니다.

The true test MSE is displayed in blue.
거기 푸른 청색으로 펄럭이는 라인이 바로 어떠한 잡음도 없는 진짜배기(순도 100%) 실전 테스트 MSE 선발대 라인입니다.

The black dashed and orange solid lines respectively show the estimated LOOCV and 10-fold CV estimates.
이에 대조되게 거뭇거뭇한 점선 트랙과 귤빛 주황 오렌지 실선 라인들은, 제각각 아까 배운 LOOCV 마법과 10-폴드 CV 뺑뺑이가 목숨 걸고 뽑아올린 추정 오차율 성적표 궤적입니다.

In all three plots, the two cross-validation estimates are very similar.
이 세 마당 전역 패널을 모조리 훑어보더라도, 저 두 추정 궤적(LOOCV와 10-Fold)의 행보는 서로 어깨동무하듯 아주 징그럽게 거의 붙어 흡사한 소름 파장을 유지합니다. 

In the right-hand panel of Figure 5.6, the true test MSE and the cross-validation curves are almost identical.
그림 5.6의 가장 맨 우측 동쪽 패널을 주시하면 엄청난 일이 벌어집니다. 파란색 진짜배기 테스트 MSE 에러 선과 우리의 교차 검증 궤적들이 서로 하나가 되어 소름 돋게 거진 일치(identical) 하는 압도적 명중 예측력 국면을 자랑합니다.

In the center panel of Figure 5.6, the two sets of curves are similar at the lower degrees of flexibility, while the CV curves overestimate the test set MSE for higher degrees of flexibility.
그림 5.6의 센터 정중앙 패널 도마 구간에선, 유연성(굴곡)이 팍 죽은 왼쪽 밋밋한 구역 초반에선 저 커브들이 사이좋게 맞물려 출발하지만, 유연성을 팍팍 무지막지 꺾어 올린(과적합) 높은 구역 후반부에 도달하자 우리의 불쌍한 CV 곡선 쫄보들이 진짜 정답보다 점수를 훨씬 오버하며 에러를 극심하게 과대평가(overestimate) 하며 허공으로 도망가는 한심한 파열 징후를 폭로합니다.

In the left-hand panel of Figure 5.6, the CV curves have the correct general shape, but they underestimate the true test MSE. 
그림 5.6의 좌측 패널 전초 기지 구역을 보면 어떤가요? 저 CV 모델 곡선 녀석들은 나름대로 진짜배기 에러가 굽이치는 모양새와 포즈 대형 대강은 아주 찰떡같이 훌륭하게 따라 그렸는데, 정작 뱉어낸 에러 수치 자체는 실제가 겪는 에러 오차 고통보다 더 수치를 축소 시켜 과소평가(underestimate) 하는 조금은 민망한 삽질 양상을 보여줍니다. 

When we perform cross-validation, our goal might be to determine how well a given statistical learning procedure can be expected to perform on independent data; in this case, the actual estimate of the test MSE is of interest.
우리가 교차 검증 전술을 그라운드에서 펼칠 적엔, 우리의 필승 최종 목적 타깃이 "자, 이런 학습 방안을 쥐여주면 이 녀석이 나중에 맞닥뜨릴 낯선 실전 독립 전장에서 대체 얼마나 눈부신 성적 효율을 뽐낼까?"를 도출 짐작해 내기 위함일 수 있죠. 만약 그게 목포라면 방금 힘들게 파고든 진짜배기 "테스트 MSE 추정 예측 수치 점수 덩치" 그 자체가 우리의 목숨을 거는 특급 관전 관심 요건이 됩니다. 

But at other times we are interested only in the location of the _minimum point in the estimated test MSE curve_ .
하지만, 어떤 전장에서 우린 돌연 그 에러 점착 숫자는 아무래도 좋으니, 오직 _유추해 낸 저 테스트 MSE 오차 곡선이 깊은 수심으로 다이빙해 바닥을 찍고 가장 적은 골짜기를 형성하는 '최저 맹점 최하 바닥 도달 위치 스팟'_ 그 자체의 좌표 점 하나에만 피눈물 나게 매달려 관심을 쏟을 때도 왕왕 넘쳐납니다.

This is because we might be performing cross-validation on a number of statistical learning methods, or on a single method using different levels of flexibility, in order to identify the method that results in the lowest test error.
왜 그런 기행을 벌이냐고요? 왜냐면 사실 우린 여러 종류의 통계학 전투 무기 부대원들을 다 꺼내 놓고 경쟁 구도를 붙이거나, 하나의 무기여도 유연성의 강도를 1단 2단 3단 극한으로 계속 레버를 비틀어 대면서 궁극적으로 "야! 도대체 어떤 세팅을 해야 우리가 실전에서 가장 에러를 덜 처맞고 버티는 낮고 무적의 오차율 달성 세팅 방식인 거냐?" 를 감별 식별해 내기 위해 교차 검증 게임판을 빙빙 도무 돌리고 있을 확률이 훨씬 짙기 때문입니다.

For this purpose, the location of the minimum point in the estimated test MSE curve is important, but the actual value of the estimated test MSE is not.
이러한 경쟁 선발 오디션 서바이벌 목적 맥락 구도 한복판에서는, 그 추정 오차 산맥 곡률 선이 가장 낮은 계곡 바닥으로 추락하는 "최저 수치 고점의 좌표 위치(최소점 스팟)"를 알아내는 것이 왕관을 씌울 절대적 보물 지대 가치를 지니며, 정작 그 자리에 도달했을 때 징수되는 오차율의 구체적 점수나 높이 따위 실제 그 덩치 에러 값 수위(actual value) 수치 따위 자체는 그다지 개뿔 중대하거나 알 필요가 없는 허수 쓰레기 장부로 타결판락 나기 십상입니다.

We find in Figure 5.6 that despite the fact that they sometimes underestimate the true test MSE, all of the CV curves come close to identifying the correct level of flexibility—that is, the flexibility level corresponding to the smallest test MSE. 
앞서 본 Figure 5.6을 영민하게 뜯어봤듯, 우린 저 쫄보 같은 CV 예측 덩어리들이 간헐적으로 "진정한 모범 신의 에러 오차 (true test MSE)" 값을 어쭙잖게 깎아치며 대거 과소평가 축소 도무(underestimate) 해버리더라 하는 부끄러운 실격 약점 허상을 지녔다는 쓰라린 사실을 확인했습니다. 아 그렇지만 이 곡선 자원들은 나름 이쁘네요! 저 수많은 교차 CV 곡선 궤도 그 자체는 그런 약점 불구에도 아주 대견하게 **가장 고효율 극저 바닥 실전 지대 적중 MSE 점수가 발생할 만한 '적절하고 영험한 유연성 레버 조절(flexibility) 파킹 위치' 그 스팟 점** 만큼은 소름 돋게 가깝고 영리하게 다이 추궁 감별 일치 포착해 찝어내 주고 있다는 훌륭한 타깃 감지 성과 식별 위력을 발견 입증 도출해 낼 수 있었으니까요.

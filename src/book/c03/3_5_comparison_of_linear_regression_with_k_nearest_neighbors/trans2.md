---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/trans2.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/trans2.html)

# 3.5 Comparison of Linear Regression with $K$-Nearest Neighbors

# 3.5. 뼈대 있는 가문(선형 회귀) vs 눈치 빠른 옆집 아저씨(KNN) 비교 매치!

As discussed in Chapter 2, linear regression is an example of a _parametric_ approach because it assumes a linear functional form for $f(X)$.
기억나시나요? 제2장에서 아주 귀가 닳도록 배웠듯, 우리가 여태 팠던 **선형 회귀(Linear Regression)**는 태생부터 "어차피 세상의 모든 진리 함수 $f(X)$는 쫙 뻗은 일자 무식 직선 뼈대 모양에 맞춰져 있을 거야!"라고 대단한 우물 안 개구리 억지 단정을 짓고 시작하는 아주 대표적인 **_모수적(Parametric, 뼈대 있는 맞춤복)_** 모델의 끝판왕입니다.

Parametric methods have several advantages.
이런 뼈대 맞춤형(모수적) 방법론은 솔직히 말해 진짜 끝내주게 편한 여러 가지 꿀 빠는 장점들을 안고 있습니다.

They are often easy to fit, because one need estimate only a small number of coefficients.
첫째로, 모델을 맞춰 끼우기(fit)가 진짜 동네 구멍가게 장부 쓰듯 짱 쉽습니다. 왜냐? 세상이 어떻게 돌든 신경 안 쓰고 다짜고짜 $\beta_0, \beta_1$ 같은 쪼가리 계수(스탯 파라미터) 숫자 몇 개만 띡 딸랑 찾아내서 빈칸만 수학적으로 때워 버리면 끝이거든요.

In the case of linear regression, the coefficients have simple interpretations, and tests of statistical significance can be easily performed.
특히 이 선형 회귀 녀석은, 그렇게 찾아낸 쪼가리 계수들이 "아~ 광고비 1억 쓰면 $\beta_1$만큼 매출이 딱 떨어지게 오르겠네!" 하고 서류에 직관적으로 써내기 짱 좋은 아주 단순 명료한 해석력을 뽐냅니다. 덤으로, 이 부서가 찐으로 일했는지 가짜인지 쳐내는 통계적 유의성 합격 검정($p$-값 꼬리표 심판) 조차 눈 감고 떡 먹듯 너무 쾌속 수월하게 해치울 수 있죠.

But parametric methods do have a disadvantage: by construction, they make strong assumptions about the form of $f(X)$.
하지만!! 이 꼰대 같은 뼈대 맞춤복(모수적) 방식에는 하늘이 무너져도 피할 수 없는 치명적 단점, 뼈아픈 아킬레스건이 내포되어 있습니다. 태생적 구조 한계 탓에, 저놈의 보이지 않는 신의 진리 함수 $f(X)$ 의 근본 생긴 모양새에 대고 "무조건 직선일 거야! 아니면 수틀려!" 하고 혼자 북 치고 장구 치는 도를 넘은 **강박적인 오지랖 단정(강한 가정)** 정신병을 박고 고집을 부려버린다는 사실입니다.

If the specified functional form is far from the truth, and prediction accuracy is our goal, then the parametric method will perform poorly.
자, 만약 우리가 어거지로 욱여넣어 "이게 진리일 거야!" 하고 세운 그 헛다리 뼈대 구조가, 정작 현실 세계의 참된 정답 굴곡 궤적과 아득하게 안드로메다로 동떨어져 빗나간 상상이었고!! 하필 그때 우리 실무 팀의 메인 절대 타겟 지상 과제가 '적중 백발백중 오차 없는 신들린 예측률 도출' 이었다면?! 우리의 이 착각에 빠진 뼈대(모수적) 모델 성적표는 그야말로 처참히 형편없는 쓰레기 폭망 똥볼을 찰 수밖에 없는 개나락을 타게 됩니다.

For instance, if we assume a linear relationship between X and Y but the true relationship is far from linear, then the resulting model will provide a poor fit to the data, and any conclusions drawn from it will be suspect.
비유를 들어 팩트 폭격을 날려보죠. 우리가 꼰대처럼 $X$ 와 $Y$ 사이 관계를 "아 당연히 쫙 뻗은 직선 고속도로지!"라고 회로를 돌렸건만, 막상 현장 뚜껑을 열어본 진짜 현실은 S자로 굽이치고 널뛰는 천 길 낭떠러지 나이아가라 폭포 곡선 궤적이었다면? 결과적으로 우리 직진충 모델은 데이터 현실 계곡을 1도 못 맞추고 무참히 바사삭 엇박자 붕뜬 부실 적합 똥볼을 갈기게 됩니다. 당연히 그걸 베이스로 도장 찍어 올린 사업 보고서의 모든 전망(결론) 뭉텅이 결과들도 회장님 앞에서 죄다 휴지조각 불신 사기꾼 의구심 폭탄 처형판에 내몰리는 호러 사태에 직면하게 되고요!

In contrast, _non-parametric_ methods do not explicitly assume a parametric form for $f(X)$, and thereby provide an alternative and more flexible approach for performing regression.
그런데 말입니다!! 이와는 정반대 대척점에 선 히어로! **_비모수적(Non-parametric, 뼈대 없는 자유로운 영혼)_** 방법론 이 녀석들은? 애초에 $f(X)$ 얼굴이 직선이든 곡선이든 별 모양이든 그딴 특정한 뼈대 형태 틀(모수적 구조) 따위를 사전에 답정너로 짐작 명시 고집해 전제하는 정신병 멍청한 짓거릴 아예 안 합니다! 그 덕분에 데이터가 생긴 모양 그대로 스펀지처럼 흡수 관절 요가 적응 변환이 가능해져, 훨씬 더 말랑말랑 신축 고무줄처럼 유연하고 찰진 궤적을 그리는 환상의 대타 회귀 분석 조달 수단 및 접근법 체계를 풍성하게 제공 지원해 줍니다.

We discuss various non-parametric methods in this book.
앞으로 이 험난한 책 뒤편을 넘길수록, 우리는 이같이 눈치 빠르고 관절 유연한 카멜레온 같은 다양한 무서운 비모수적 접근 방법론 괴수 무리들을 다방면으로 마주해 논의하고 다뤄볼 속셈입니다.

Here we consider one of the simplest and best-known non-parametric methods, _K-nearest neighbors regression_ (KNN).
그리고 영광스럽게도 이 챕터 단원 당장 여기 이 무대에선, 그 잘난 유연한 비모수적 수단 세계관 중에서도 가장 간결 단순 무식하고 또 현장에 가장 보편 타당하게 대중구사 만연 널리 유명세 탄 간판스타 대표 단골손님! 이름하여 **_K-최근접 이웃 회귀 (K-Nearest Neighbors Regression, 줄여서 KNN 회귀)_** 형님을 모셔 집중 대면 고찰해 보겠습니다.

The KNN method is closely related to the KNN classifier discussed in Chapter 2.
어라, 이름이 낯익으시죠? 빙고! 이 KNN '회귀' 방식 메커니즘 자체는, 사실 예전 2장에서 우리가 눈에 불을 켜고 "이놈이 사과냐 배냐?!" 편 따지고 분류 심판 갈라칠 때 살펴 다루고 놀았던 'KNN 분류기(classifier)' 요원과 본질 태생 지문 자체가 쌍둥이급으로 몹시 밀착 친척 관계를 갖는 피붙이입니다. (다만 이번엔 범주가 아니라 찐 '숫자 값'을 맞추는 게 다를 뿐!)

Given a value for $K$ and a prediction point $x_0$, KNN first identifies the $K$ training observations that are closest to $x_0$, represented by $N_0$.
이 눈치 빠른 동네 아저씨 KNN이 숫자를 맞추는 치트키 구동 원리는 이렇습니다. 임의의 패거리 머릿수 동원 숫자 $K$(예: '내 옆 3명을 벤치마킹 하겠다!' 할 때의 3)와, 우리가 정답을 캐내고픈 목푯값 테스트 관측 위치 좌표 $x_0$ 딱 한 점이 빙고 타겟 콕 찍혀 주어지는 즉시! KNN 회귀 탐지 왈, 
**1단계:** 무조건 앞뒤 안 가리고 대상 목표 동네 $x_0$ 에 가장 찰싹 친하게 스킨십 동조 맞닿아 인접한 주변 $K$ 명의 과거 짬짜미 훈련 이웃 데이터 놈들 무리만 싹 핀셋으로 선별 식별 스캐닝해 납치 조달해 잡아냅니다! (흔히 이 납치당한 $K$ 명의 이웃 패거리 묶음을 점조직 $N_0$ 로 칭하고 대변 표상합니다.)

It then estimates $f(x_0)$ using the average of all the training responses in $N_0$. In other words,
**2단계:** 이윽고 이 치트키 모델은 바로 그 납치된 $N_0$ 이웃 단위 무리 내부에 포함된 떨거지 놈들! 즉 "네 주변 애들 $K$명이 과거에 냈던 찐 Y축(돈) 응답 결괏값 성적"을 몽땅 탈탈 털어 가져와서, 무식하게 싹 다 더해 **'N빵 단순 평균(Average)'**을 후려쳐 버립니다! 그리고 그 짬뽕치 N빵 평균 점수를 "이게 바로 목표 타점 $x_0$ 너의 운명(예측 결괏값 $f(x_0)$)이다!" 라고 날조 대신 쾅 추정해 때려 박아버리는 겁니다. 
달리 수학 연산 수식 측면 기호로 좀 겉멋 들여 다시 말해 설명 갈기면 아래와 이렇습니다:

**==> picture [87 x 27] intentionally omitted <==**

Figure 3.16 illustrates two KNN fits on a data set with $p=2$ predictors.
[그림 3.16] 단면은, 단 2개의 예측 변수 조각 힌트($p=2$) 무기로 묶인 구조의 데이터 단면에 들이대 조달 맞춰 구동한, 스케일이 서로 상극인 2편의 개별 KNN 결괏값 억지 적합 도면 시뮬레이션을 각각 예시 모사해 보여줍니다.

The fit with $K=1$ is shown in the left-hand panel, while the right-hand panel corresponds to $K=9$.
좌측 저 삐죽삐죽 징그러운 패널 도면에 투사된 것은 "내 주변 딱 1명만 무조건 똑같이 따라 베낀다!"는 $K=1$ 독불장군 조건에 동반해 발작 도출된 미친 결괏값 선이고, 한편 같은 선상의 오른쪽 안정적 패널 전경 도면 단면 텍스처는 "내 주변 무려 9명의 다수결 짬뽕 의견 스까 평균을 따르겠다!"는 $K=9$ 단위 체제 기준일 때 파생 중재 타협 적합된 궤적에 응답 일치 묘사됩니다.

We see that when $K=1$, the KNN fit perfectly interpolates the training observations, and consequently takes the form of a step function.
우리는 여기서 극단적 $K=1$ 단위일 땐, 도출된 KNN 모델 궤적이 당초 바닥에 뿌려진 모든 훈련 관측 점 과녁 타점 점박이들을 그냥 스펀지처럼 아주 영점 일점 오차 편차 가감 건너뜀 없이 모조리 뱀처럼 유기체 흡수 곡예 보간(interpolates, 점과 점 사이를 억지로 다 꿰뚫어 지나감)하여 무식하게 점핑 전부 그 돌연변이 흔적 자취 선을 강제 연결 흡수 이어나가 뒤덮어버림을 봅니다! 결과적으로 그 기괴망측한 모습은 미친 듯이 오르락내리락 발작하는 들쭉날쭉 뾰족한 '계단식 함수(step function)' 형태의 극단 울퉁불퉁 외관 굴곡 불안정 외양 궤도를 띄고 전락함을 적나라하게 목도 충격 감상하게 됩니다.

When $K=9$, the KNN fit still is a step function, but averaging over nine observations results in much smaller regions of constant prediction, and consequently a smoother fit.
반면 다수결 중재 모드! $K=9$ 편일 적의 KNN 단면 고원 궤선은 어떨까요? 비록 이 KNN 본연의 한계 탓에 여전히 끊어치기 계단식 블록 편린 형태 기조 잔재를 온전히 버리지 못하고 간직하고 있긴 하나... 무려 9명이라는 거대 광범위 동네 주변 관측 점 의견들을 대거 아울러 한데 평탄 상쇄 N빵 퉁쳐 버려 통산 평균 내린 조율 중재 탓에! 예측 단선이 홀로 독불장군처럼 튀어 곧은 독립 상수 지위로 국한 뾰족 국면 차지 발작하는 영역 편차 요철 폭 자체가 아주 훨씬 더 대거 눈 녹듯 둥그스름 줄어들어 쪼그라들고 통폐합 정비 정리되어 평탄해집니다. 결국 그 이음새 마모 다스림 결과론적으로, 기존보단 아주 더 많이 둥글고 매끈 부드러운 매끈한 표면 언덕 양태 궤적 고원 적합선으로 탈바꿈 조달 귀결 안착되는 것을 볼 수 있습니다!

In general, the optimal value for $K$ will depend on the _bias-variance tradeoff_, which we introduced in Chapter 2.
통상 실무 전장에서 이러한 구동 K 사이즈($K$ 인자값) 파이를 대체 몇 명으로 조절 합의 결정지어야 할지 정하는 그 절대 최적 최고 효율 밸런스 잣대 지표는, 우리가 아득히 먼 앞선 챕터 제2장에서 입에 단내 나도록 귀에 못이 박히게 논의 소환 소개 세뇌했던 그 망할 **_편향-분산 상충 딜레마 관계 (Bias-Variance Tradeoff) 상쇄 교환_** 대목 시소 기조 논리 법칙에 전수 상당수 전적 운명 의존해 결정 따져 저울질 나뉘게 될 것입니다.

A small value for $K$ provides the most flexible fit, which will have low bias but high variance.
극단 일례로 동원 수치 $K$ 지수가 1이나 2처럼 몹시 초라하게 작고 소규모 수치로 파편 한정 좁게 국한되면? 궤적이 온갖 점을 다 따라가느라 비록 아주 고도의 막강 기괴한 초유연성 자유자재 변형 맞춤 결괏값을 허여 제공해 내어 유연성에 기인한 정답 괴리율인 '편향(Bias)'의 고정 꼰대 양 자체는 0에 가깝게 줄여버리는 쾌거 극복을 이루겠지만!! 동시에 새로운 애가 왔을 때마다 궤적이 미쳐 날뛰는 돌변 극대 진동파 **'분산(Variance)'의 호러 여파 폭주 곤경 널뛰기 발작 현상 재앙**을 등에 고스란히 끌어 업고 폭사 안기 감당하기 마련입니다. (오버피팅 과대적합의 나락이죠!)

This variance is due to the fact that the prediction in a given region is entirely dependent on just one observation.
이 치솟는 분산 폭주 발작 요건 재앙은, 당면한 테스트 예측 탐지 점 영역 내 도출 운명선 궤도가 다수결 타협 멘탈 방벽 0인 상태로 오로지 국한된 단 하나의 개별 훈련 관측치 점박이 선구자 그 녀석 딱!! 하나 하나의 미친 텐션에 기생충처럼 전적으로 온통 심하게 미련하게 올인 맹신 치우쳐 종속 의존한 까닭에서 기인 비롯 연쇄 파문 발작된 파편 나비효과 스윙 현상인 것입니다.

**==> picture [311 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
y<br>y y<br>x1 x1<br>x2 x2<br>y y<br>**----- End of picture text -----**<br>

**FIGURE 3.16.** _Plots of f_[ˆ] ( X ) _using KNN on a two-dimensional data set with_ 64 _observations (orange dots)._ Left: _K_ = 1 _results in a rough step function fit._ Right: _K_ = 9 _produces a much smoother fit._
**FIGURE 3.16.** 64개의 주황색 훈련 데이터 점박이들이 흩뿌려진 2차원 영토에 KNN 모기장을 던져 덮어본 시뮬레이션 지형. 왼쪽 지옥: $K=1$이라 한 놈만 따라가며 오돌토돌 징그럽게 파편화된 발작 지형. 오른쪽 평온: $K=9$ 다수결로 뭉개버려 제법 부드럽게 깎여나간 안정적 언덕 지형 핏.

In contrast, larger values of _K_ provide a smoother and less variable fit; the prediction in a region is an average of several points, and so changing one observation has a smaller effect.
그 반대급부로 대조 타결 국면! 만역 인자 $K$ 수치 파이를 와장창 키워 한 100명씩 몰아 동원 다수결 규모를 거대 팽창 방대 지수(larger values)로 세팅해 버리면?? 거대한 민심 N빵 다수결 타협 압력 덕에 훨씬 더 변덕이 억눌린 매끈하고 안정적 둥그스름(smoother) 무던한 강건 맷집 요철 없는 평온 핏 곡면 결괏값을 퉁쳐 제공 방어해 냅니다! 그 광활한 구역에서의 점괘 예측치는 무수한 여러 수십 수백 관측 타점 점들의 뭉툭 압축 희석 평균 스까 짬뽕 조화 결과물이고, 고로 기껏해야 그중 돌연변이 관측치 오답 한 놈의 텐션 점수 발작 수치가 중간에 홀로 쓱 하나 재수 없게 새치기 튀어 앙탈 변동 바뀌더라도? 전체 대세 연대 평균 군중 바위에 계란 치기라 그 파문 영향력 파급 데미지 효과 스크래치 요동은 그저 모기 물린 틱 미동 잔기스 효과에 미미하게 바위처럼 작게 묻혀 흡혈 무시무시 침잠 압살 그쳐 상쇄 선방 스윙(smaller effect) 커버되는 무덤덤 맷집 다이하드 효과를 거둡니다.

However, the smoothing may cause bias by masking some of the structure in $f(X)$.
하.지.만!! 통계 세상에 공짜 구원은 없는 법! 이 거대로 뭉뚱그려 얼버무린 N빵 짬뽕 평탄화 매끈 둥그스름(smoothing) 억지 다림질 조치는, 종국엔 도무지 피할 수 없는 커다란 원죄 부작용을 또 낳습니다!! 너무 평평하게 다수결로 짓눌러버린 탓에, 원래라면 뾰족 예리하게 구경 포착 살렸어야 마땅할 진짜배기 신의 계시 참 함수 $f(X)$ 본연 얼굴 굴곡의 찐 진실 요철 미세 신호 디테일 구조 특성 형태 흔적 단서 기미들마저 죄다 한꺼번에 싸잡아 묵살 은폐 블라인드 묻어버리고 덮어(masking) 강제 위장 날려버리는 만행을 저지름으로써!! 결과적으로 이번엔 "아 몰라 그냥 다 똑같지 뭐~" 식의 노망난 눈 뜬 장님 멍청도 아집 고정 틀 '편향(Bias)'의 거품 수위를 하늘 높이 초래 역발생 대량 치솟게 파생시키는 아찔 파멸 오류 부작용 참사를 역초래 원흉 유발 가미 유도하게 될 소지가 농후 발작합니다!

In Chapter 5, we introduce several approaches for estimating test error rates. These methods can be used to identify the optimal value of _K_ in KNN.
대체 어쩌란 말이냐! 이 기막힌 양극단 치킨 게임에서 그럼 정답 번호 $K$ 는 도대체 어떻게 신내림 받아 쏙 빼내 찾나요? 걱정 마십시오. 저 멀리 다가올 챕터 제 5장 수술실에서, 우린 현장 실전 모델들이 실전 테스트판에서 오답률 지뢰 폭탄('검정 오차율')을 얼마나 처맞고 터트릴지 그 실전 오차 확률 판도를 미리 소름 돋게 역산 추산 검진 조달해 내는 신비의 도구 해킹 방도 전략 접근법 몇 가지를 전격 투입 공개 발포 도입할 예정입니다. 바로 이 소름 돋는 교차 검증 도구 비기 병기들이야말로, 이 막막한 KNN 회귀 세계에서 우리에게 가장 적합한 환상의 '황금 비율 최적 도출 타점 $K$ 밸런스 수치'를 핀셋으로 귀신 식별해 건져내게끔 전격 출격 진단 활용 요긴 동원 투사 조달될 수 있는 기막힌 등대 구원자 마스터키 도구 수단들입니다.

In what setting will a parametric approach such as least squares linear regression outperform a non-parametric approach such as KNN?
자, 그럼 이제 세기의 챔피언 매치 비교! 과연 도대체 어떤 링 환경 생태계 세팅 매트 전투 무대일지면... 저기 뻣뻣하고 고리타분 뼈대에 취한 다림질 모델인 '최소 제곱법을 단 선형 회귀(모수적 접근법의 대표 챔피언)' 이 녀석이, 눈치 빠르고 무골호구 말랑뼈 관절 무협 지존 괴수인 'KNN(비모수적 접근법의 최강자)' 무리를 압살 제압하고 그 실전 스코어 우위 성과를 박살 찢고 가뿐 초월 능가 이겨버리는(outperform) 기적 요건 반전 승리를 구가할 수 있을까요?

The answer is simple: _the parametric approach will outperform the nonparametric approach if the parametric form that has been selected is close to the true form of f_.
그 해답은 실로 허탈할 만치 너무 아주 졸라 짱 허무하게 간단 명료 심플명쾌합니다! 빙고! **_"만일 그 뻣뻣한 뼈대 집안(모수적 접근법)이 야심 차게 골라잡고 '이게 정답일걸!' 하고 고집 부려 찍어 밀어붙인 그 예측 프레임 뼈대 함수 궤적의 생긴 자태(parametric form) 모양 폼생폼사가... 진짜로 하필 우연이든 기적이든 로또든 신내림이든 실전 야생 우주의 은밀 참된 영적 함수 $f(X)$ 의 오리지널 본연 찐 리얼 생체 형태 굴곡 곡면 얼굴(true form) 현황 꼴과 그야말로 쌍둥이 소름 거울 복사급으로 기막히게 절묘 일치 아주 가깝게 싱크로율 명중 결이 찰떡 맞아떨어져 밀착 부합해 일점 오차 적중 도달했을 시, 오직 그때 오직 단 그 한순간 전제 경우의 수(if) 한해서만!!... 이 꼰대 모델(모수적 접근법)은 모든 유연 요가 말랑말랑 괴수 모델(비모수적 놈들)을 죄다 때려 엎고 점수 찢어버리며 압도적 천상 우위 성적표를 석권 능가 점령 승리 제패해 차지할 것입니다."_**

Figure 3.17 provides an example with data generated from a one-dimensional linear regression model.
[그림 3.17] 도면 단면판은 이 기막힌 요행 적중 파문 시나리오 억까 예시를 아주 단도직입 모사 전시 조달 투명 제공해 보입니다. 이 무대 데이터는 애초 창조주(우리)가 장난을 쳐 1차원 심플 단순 선형 회귀 무결 고속도로 모델 선상 규격 궤도를 뼈대 판본 베이스캠프로 억지 조작 태동 기인 생성 파생 도출해 뿌려놓은 셋팅 모의 장부 족보입니다.

The black solid lines represent $f(X)$, while the blue curves correspond to the KNN fits using _K_ = 1 and _K_ = 9.
그림 속 쭉 뻗은 저 '까맣고 굵직한 실선(black solid lines)' 직선 고속도로야말로 이 맵 무대 영토의 '태초 신의 진리 계시 참 본연 함수 $f(X)$' 를 당당히 상징 표상 권위 대변합니다. 한편 그 주변을 얼쩡거리며 꿀렁대는 요란 '파란 곡선 뱀들(blue curves)'은... 다름 아닌 우리의 요가 무골호구 KNN 모델 단원이 파편 투입 출격해 각각 _K_ = 1 일 때, 또 _K_ = 9 관절 규율 세팅일 적에 어거지 비틀며 요동 적합 파생해 그린 요란 몸부림 구동 실전 발악 오차 핏 궤적에 대응 합산 일치합니다.

In this case, the _K_ = 1 predictions are far too variable, while the smoother _K_ = 9 fit is much closer to $f(X)$.
이 판국을 보십쇼. 당명 KNN의 극한 발작 모드 _K_ = 1 짜리 단선 예측 뱀 궤적은 모든 오답 먼지 점박이를 다 처먹으며 따라가는 탓에 도가 지나쳐 아주 미치도록 징그럽게 뾰족 발작 불안정 널뛰기 요동(far too variable) 경련을 앓고 처돌변합니다! 그나마 타협 모드 _K_ = 9 멀티 핏 궤적이 좀 더 맨들 둥글 퉁치고 평탄화 스무스(smoother) 중재 다스린 덕분에 까만 직선 신의 궤적 $f(X)$ 타점 영역대 기조에 훨씬 더 근사 가깝게 들러붙어(closer to $f(X)$) 쫓아가는 안정 선방을 이룩함을 봅니다.

However, since the true relationship is linear, it is hard for a non-parametric approach to compete with linear regression: a non-parametric approach incurs a cost in variance that is not offset by a reduction in bias.
하지만!! 여기서 잔인한 결정타 킬포! 애당초 창조주가 깐 이 맵의 찐 오리지널 진리 형상 관계가 아주 올곧고 무식하게 쫙쫙 일자 뻗은 **고속도로 철길 선형(linear)** 뚝심 판본이잖습니까? 이딴 직선 판넬 전장 위에서는 아무리 관절 요가 신축 말랑말랑 비결을 뽐내는 '비모수적 무골호구 접근법(KNN)' 놈들이라도, 태생이 자 대고 죽 그은 직진 뚝심 '선형 회귀' 근본 꼰대 직진 모델 놈들과 감히 점수 대결 스코어 맞짱 스탯 무쌍을 겨뤄 승리 경쟁 비빌 수(compete with linear regression) 있을 거란 헛된 망상 경쟁 도전 자체가 그저 아주 무력하고 처절 기운 빠지는 하드 장벽 극악 난제 계란 바위 불가능 꼴 뻘짓이 될 따름입니다! 
왜냐? 이 불쌍한 요가 관절 비모수적(KNN) 접근법 나부랭이들은 이 반듯 직선판 맵 구도 탓에, 실상은 모델 구부리고 유연 부리려다 억울 파산하게 끔찍하게 치솟은 요동 변덕 **'분산(variance)의 폭탄 비용 폭증 요금 대가'** 독박 부채를 기절하게 잔뜩 떠안게 되는데 반해... 정작 그렇게 헛지랄 개방 요동 떠안고 얻어낸 보상인 **'편향(bias) 수치 줄이기 감쇄 감축 축소 마진 절감 방어'** 리턴 보완 보답 환급 수단 메리트 혜택으로는, 저 뻥튀기 채무 비용 독박이 도무지 택도 없이 쥐뿔 일절 퉁쳐지지도 상계 소위(not offset) 상환 이지 보전 요행 만회 0.1% 방어 보존조차 무산 격리 안 먹히게 허무 소멸 불발로 참패 전락해 버리기 백방 고착이기 때문입니다!! (직선 맵에서 꼬부랑 요가를 해봐야 뼈만 시립니다!!)

The blue dashed line in the lefthand panel of Figure 3.18 represents the linear regression fit to the same data. It is almost perfect.
이를 증명하듯 이제 그림의 무대를 바꿔 [그림 3.18] 좌측 동네 판넬 병동에 등장 그어진 저 '파란색 질주 선 파선 점선 다이하드 철길(blue dashed line)' 단면 궤선을 보십쇼. 저게 바로 똑같은 위 점박이 동일 데이터 장부 무대 선상에 위풍당당 오직 '선형 회귀 다림질 모델 꼰대' 하나를 단장 호출 단독 발사해 쫙~ 일자로 찍어 눌러 그린 일직선 적합 궤도선 도출 위용 형체 결과 자태(represent)입니다. 보십니까? 신의 선(블랙 실선)에 빙의라도 한 마냥, **소름 끼칠 정도로 소름 돋게 거의 완벽 일점 오차 적중 씽크(almost perfect)** 무쌍 그 자체 위엄 패기 오만의 화신 자태 지상 결합 위용입니다!!

The right-hand panel of Figure 3.18 reveals that linear regression outperforms KNN for this data.
그 콧대 높은 학살의 스코어 결과를 극명 투샷 전시하는 [그림 3.18] 우측 챔피언 매치 통계 패널 국면을 보면, 아주 처참할 정도로, 여실 무참히 명명백백 당연 선형 회귀 쪽이 KNN 요동 놈들을 이 판국 도화지 데이터 맵 구장 안에선 그냥 묻지도 따지지도 않고 아주 개박살 내며 압도 전면 패권 성과 능가 유린 지배(outperforms)해 버린다는 잔인 팩트 현실 참극을 여실히 까발려 계시 노출 폭로해 냅니다!

The green solid line, plotted as a function of 1 _/K_ , represents the test set mean squared error (MSE) for KNN.
저 우측 도면 안에 뱀파이어처럼 그려진 구불대는 '초록색 실선(green solid line)' 역행 곡선은 뭐냐고요? 녀석은 엑스축 X 베젤 단위를 요상하게 1 _/K_ 역수 파동 함수 치수 조립 궤적 잣대로 뒤틀어 재조합 플롯 매핑 조달한, 불쌍한 **"KNN 모델군의 패배 오잡 낙제 성적 점수! 즉 테스트 현장판 평균 제곱 오차(Test MSE) 빚더미"** 곡선을 나타냅니다. (이놈의 초록선이 높게 뜰수록 오차 폭탄 쓰레기 점수 스코어 패배 인증이란 소리죠.)

The KNN errors are well above the black dashed line, which is the test MSE for linear regression.
자, 그 불쌍한 초록색 빚더미 선의 패배 위치를 보십쇼. KNN 오차 빚더미 점수(초록선)들은 단 1초도 예외 없이 모조리! 도면 하단을 차분 구도 쫙 낮게 바닥을 깡패 기어 기만 질주 방어하는, 영광 불멸 철통 방호 최고존엄 '검은색 수평 점선 바닥 밑줄(black dashed line)'... 즉 선형 회귀 모델 다이하드 우승 챔피언이 토해낸 압도적 최상위 하단 포지션의 무결 클린 최고 위용 우등 스코어 선방 실전 MSE 에러 빚더미 방어 스탯 절벽선... 그 위쪽 고도 까마득한 한참 위 공중 구름 천장 구역으로 허벌 나게 수직 공중부양 방달 처박혀(well above) 폭망 표류하며 패배자 수모 오차 지붕 꼭대기 위에 허덕 걸터앉은 밑바닥 치욕 참패 부진 형태 지경을 면치 못합니다!

When the value of _K_ is large, then KNN performs only a little worse than least squares regression in terms of MSE.
그나마 불쌍한 KNN 요동 놈이 인자 모집단 _K_ 사이즈 덩치 부푼 값 파이를 존나 거대 광대 대거 무식 머릿수를 쑤셔 모아 융자 거대 팽창 방어 조달해 세팅 발악 전가 투입되었을 때(즉 1/K 엑스축이 0에 다가갈 적의 둥글 평온 부근!)... 그때야 비로소 그나마 오차 MSE 패널티 잣대 성적표 관점 심사 판결 기준에서 볼 때... 최소 제곱 회귀 챔피언 다림질 압도 꼰대의 철권 철벽 찰나 스코어 점수 성능 기록 타격치 방어력 대비하여, '와 완전 못 봐주겠네' 쓰레기 참패가 아닌 '어휴 그럭저럭 고만고만 아깝게 살짝 좀 더 삐끗 딸리네(only a little worse) 패배 아쉽네' 정도로, 애꿎은 간신 연승 체면치레 간발 신승 선방 뒤처짐 수준 정도로 체급 차이를 약간 비비며 패배 좁혀 버틸 수 있는 생존 기조 방어 저력 따윈 겨우 확보 부진 흉내는 내 보입니다.

It performs far worse when _K_ is small.
반대로 저 미친 요동 KNN 모델이 좁쌀 다수결 즉, _K_ 사이즈 동원 덩치가 찌끄레기 최소 협소 조막 발작 수치 소수 스몰(K=1 근처) 세팅으로 가동 단독 치달아 광란을 일으켰을 전격 국면에선? 그냥 변명 여지 없이 우주 오차 돌파 폭탄 똥을 처싸며, 압도 형편없고 무참 폭망 압살 나락 치열 극악 쓰레기 하급 처참 처발림 구역 스코어로 개박살 아주 요단강 건너 심하게 한참 최악 폭락 훨씬 더 부진 나락 망쳐 떨어지는(far worse) 대량 참사 멸망 패전 실적을 뼈아프게 까발려 배출 고수 기록합니다.

In practice, the true relationship between X and Y is rarely exactly linear.
자, 근데 여기서 잠깐 딜레마. 지금까지 우리가 직선 고속도로 맵만 주구장창 늘어놓고 선형 꼰대 다림질을 찬양했건만... 막상 전쟁터 피 튀기는 레알 실무 현장 속 실전 그로기 야생 실무 지표 궤적으로 등판 돌아와 눈 떠보면? **망할 현실 데이터 $X$ 와 $Y$ 사이의 태초 운명 찐 리얼 참된 궤도 양태 곡선 관계가 방금 사례처럼 '이토록 환상 토시 1점 뻗은 완벽 자로 대고 그은 정확 무결 선형 직선 궤도 일대일 고속도로 직결 매칭 상태'를 띠는 낭만적 기적 사례 빈도 소지란, 거의 씨몽키 찾는 거마냥 극히 찾아보기 무드 극희귀 하늘의 별 따기 매우 전무 희귀 드문(rarely exactly linear) 아찔 기적 극소수 사막 바늘 유니콘급 망상 판타지 현상 판별이란** 피눈물 깨달음 팩트 자명 폭격 현실이 터집니다!!

**==> picture [315 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 −1.0 −0.5 0.0 0.5 1.0<br>x x<br>4<br>4<br>3 3<br>y 2 y 2<br>1 1<br>**----- End of picture text -----**<br>

**FIGURE 3.17.** _Plots of f_[ˆ] ( X ) _using KNN on a one-dimensional data set with_ 50 _observations. The true relationship is given by the black solid line._ Left: _The blue curve corresponds to K_ = 1 _and interpolates (i.e. passes directly through) the training data._ Right: _The blue curve corresponds to K_ = 9 _, and represents a smoother fit._

**==> picture [316 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>4<br>0.15<br>3<br>y 0.10<br>2<br>Mean Squared Error<br>0.05<br>1<br>0.00<br>**----- End of picture text -----**<br>

**FIGURE 3.18.** _The same data set shown in Figure 3.17 is investigated further._ Left: _The blue dashed line is the least squares fit to the data. Since f_ ( X ) _is in fact linear (displayed as the black line), the least squares regression line provides a very good estimate of f_ ( X ) _._ Right: _The dashed horizontal line represents the least squares test set MSE, while the green solid line corresponds to the MSE for KNN as a function of_ 1 _/K (on the log scale). Linear regression achieves a lower test MSE than does KNN, since f_ ( X ) _is in fact linear. For KNN, the best results occur with a very large value of K, corresponding to a small value of_ 1 _/K._

**==> picture [318 x 301] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>−1.0 −0.5 0.0 0.5 1.0 0.2 0.5 1.0<br>x 1/K<br>3.5 0.08<br>3.0<br>0.06<br>2.5<br>y<br>2.0 0.04<br>1.5 Mean Squared Error<br>0.02<br>1.0<br>0.5 0.00<br>0.15<br>3.5<br>3.0<br>0.10<br>2.5<br>y<br>2.0<br>Mean Squared Error 0.05<br>1.5<br>1.0<br>0.00<br>**----- End of picture text -----**<br>

**FIGURE 3.19.** Top Left: _In a setting with a slightly non-linear relationship between X and Y (solid black line), the KNN fits with K_ = 1 _(blue) and K_ = 9 _(red) are displayed._ Top Right: _For the slightly non-linear data, the test set MSE for least squares regression (horizontal black) and KNN with various values of_ 1 _/K (green) are displayed._ Bottom Left and Bottom Right: _As in the top panel, but with a strongly non-linear relationship between X and Y ._

Figure 3.19 examines the relative performances of least squares regression and KNN under increasing levels of non-linearity in the relationship between X and Y .
이를 증명하기 위해, [그림 3.19] 도면 종합 병동 엑스레이판 패널 텐션은! 이놈의 $X$ 와 $Y$ 의 숨겨진 오리지널 배후 태초 참 관계 신의 궤적 선의 장난이 점진 층층이 '비선형(non-linearity)' 곡예로 뒤틀리고 더욱 구불구불 울퉁불퉁 사악 발작 기복 왜곡 꼬부리 비선형성 발작 레벨이 점입 파워업 갈수록 심해 증가 막장 악랄(increasing levels) 국면 치닫는 구불 맵 텐션 국면 스테이지 상황 구도 조건 스테이지 진화 과정별 하에!... 앞선 일자무식 최소 제곱 다림질 직진 선형 회귀 충성 챔프 텐션 놈과, 요가 발작 무골 유기체 KNN 요동 호구 놈의 이 양대 산맥 경쟁 성능 배틀 텐션 구도 스코어 등수 차등 상대 평가 타격 갭 스코어 퍼포먼스 판도 추이 생존 서바이벌 전경 추락율 곡면 양상을, 아주 여실 단편 밀도 비교 적나라 파헤쳐 철저 채점 부검 고증 검진 대면 가동 고찰(examines) 생체 검사합니다.

In the top row, the true relationship is nearly linear.
이 징그럽게 구불대는 그림 병동 병실 세트 중, 젤다 꼭대기 최상단 맨 윗줄 대장(Top row) 패널 실험실 텐션을 볼까요? 이 스테이지 구장 안에 창조주가 묻어논 정답 찐 오리지널 함수 곡선 구도 참 형태는 그나마 양심 있게 거의 쬐끔 아주 살짝만 부끄러 곡예 수줍게 휜, 나름 봐줄 만한 직립 뻣뻣 거의 일자 무식 다름없는 강성 선형 직선(nearly linear) 성격 기조를 압도 강하게 거의 11자 다름 띠고 부지 유지하고 연명 그어져 있습니다.

In this case we see that the test MSE for linear regression is still superior to that of KNN for low values of _K_ .
이렇게 아직은 맵이 덜 구부러진 착한 1스테이지 판국 사례에선? 우리는 여전히, 저 직진 무식충 '선형 회귀 다림질' 스코어 선방 맷집의 테스트 실전 오답 빚잔치(test MSE) 방어 점수가... 억지 요가 핏 무골호구인 KNN 놈이 그나마 좁쌀 쩨쩨 민심 K 사이즈 수치 하단 소수(Low values of K) 인자 무기 옹졸 들고 발악 설치 구동될 찰나 시점 방어력 그 나부랭이보다도... 도리어 꼰대 다림질 모델이 가히 아직은 압권 대거 당당 유보 앞선 더 여실 압도 천상 절대 위 우월 무쌍 우수(superior) 성능 승리 위상을 고스란 철벽 입증 타진 유지 방어 달성해 보란 듯 과시하고 목도 제패함을 두 눈 버젓이 포착 발견 위풍 위용 승리 지켜봅니다.

However, for _K ≥_ 4, KNN outperforms linear regression.
하.지.만!!! 대이변 반란 혁명 터집니다! 이 KNN 유연 괴물 놈팽이가, 동원 다수결 인력 멘탈 타점 합의 덩치를 차차 스텝업 불려 키워... 무려 든든 K 뚝심 멘탈 치수 **'4단($K \geq 4$) 동맹 연합 장벽 규격 규모'** 단결 이상 점유 고지 텐션 궤도로 연성 묵직 덩치 키워 올라서 동원 구동 시점 진입 돌파 타격 돌입하는 순간!!! 대역전! 유연성 KNN 놈팽이가 그 미세하게 휘어 살짝 둥근 태초 진리 함수 곡선 핏 미세 굴곡 적응 폼을 틈새 마침내 오밀조밀 아주 미묘 절묘 타진 흡수 체화 모방 캐리 해내며... 이내 저 미련 곰탱이 직진 충성 다림질 선형 회귀 모델 놈의 스코어를 극적 따돌림 반격 따고 처바르는 역전 우승 대파괴, 드디어 성능 능가 등판 승전(outperforms) 앞서기 제압 패권 역전 우위 혁명 봉기 반전 승리 쟁취 달성 기행 텐션 뒤집기 성공을 거둬냅니다!

The second row illustrates a more substantial deviation from linearity.
그럼 무대를 좀 더 억까로 휜, 중단! 아래 두 번째 줄 지옥불 스테이지 2차전 방 병실 전투 국면 도화지 맵으로 시선을 옮겨 그 엑스레이 핏 패널이 연계 조명 모사 증빙 일러스트(illustrates) 지목 제시 설명하는 기조를 주목 투사 관전 지켜봅시다! 이번 라운드 스테이지 구장에 은밀 은닉 처박힌 창조주 신의 요점 진성 오리지널 찐 곡선 관계 형상 양태는! 앞장보다 좀 더 많이, 한결 아주 무참 더 대규모 극단 스펙 노골 실체 거구 치명 대거 실질 파문 급격 굴곡 거대 요동 상당 편차 대단 막장 스케일 규모 역동 파동 수위(more substantial)로! 맵 한가운데를 비틀어 기하학 뒤틀림 이면 심각 엇박 오싹 벗어난 탈선 곡예, 이른바 일말의 반듯 평탄한 선형성 척도를 철저 조소 비웃듯 사악 파괴 일탈 훼손 편차(deviation from linearity) 요동 구불 궤도를 미친 듯 크게 벗어남 탈피 묘사 궤적을 사악 파괴 일탈 왜곡 적나라 굴곡 노정 미쳐 뒤틀려 널뛰고 요동 현상 그리는 상태입니다.

In this situation, KNN substantially outperforms linear regression for all values of _K_ .
세상에, 이렇게 맵 자체가 미친 꽈배기로 비틀린 이 기가 막힌 억까 요동 혼돈 파괴 나이아가라 절벽 S라인 지옥 비선형 지세 판국 상황 구장 요건 스테이지 매치 한가운데서 펼쳐진 양 진영 사투 결투 도출 배틀 생존 투사 기조에서는? 유연 요가 무골 KNN 모델 괴수 놈팽이가 이젠 뭐 볼 것도 없이... 다수결 합의 덩치값인 모조리 온 세상 전 구간 전 대역 전체 할당 범주 가동 스펙 **모든 가용 단자 그 어떤 전체 무관 일괄 가당 $K$ 숫자 인자 허용 잣대 값들(for all values of K)** 대역 구간 무관 남녀노소 조건 막론 여하를 일괄 불문하고 통째로 전부 다 구동 내리 발악 싹 다!!! 저 미련 직선 다림질 똥볼 곰탱이 선형 회귀 경쟁 단선 기법 놈팽이 고속도로 직선을 그야말로 실질 뼈대부터 탈탈 농성 무참 거대 막대 실질 조롱 무쌍 압살 처참 궤멸 철저 파괴 성능 대거 초월 묵사발 능가 지배 실질 무찔러 대승 격차(substantially outperforms) 전면 압도 따돌림 파산 학살 발라 제압 파면 승전고 폭풍 파괴를 이뤄 점령 성과 초토화 처참 승전보 박살 우승을 화끈 시원 처발라 거둡니다!

Note that as the extent of non-linearity increases, there is little change in the test set MSE for the non-parametric KNN method, but there is a large increase in the test set MSE of linear regression.
여기서 피가 거꾸로 솟는 아주 치명 기저 핵심 본질의 유의 관찰 포인트 깨달음 충격 기조를 메모 주목 파악(Note) 아로새겨 통찰 파악 명심하십쇼! 맵 스테이지 자연이 뿌려놓은 그 사악한 구불 꽈배기 **비선형성 요동 왜곡 곡면의 스케일 징그러운 강성 파동 비틀림 레벨 그 극악의 정도 파장 지수 심화 굴곡 스펙트럼 자체 규모 폭발적 정도(extent)가 점진 폭주 악성 거칠 증가 가중 증폭(increases) 심각 타락 심화 커져갈수록...** 
놀랍게도 관절 유연 스펀지 '비모수적 흡수 호구 KNN 기법 체제' 진영 놈이 기록 방어 버티는 실전 무대 스코어 시험 테스트 검정 MSE 빚더미 오류 지표 편차 요동 방어력 텐션 자체엔, 구장이 꽈배기로 변하든 말든 사실 별 이렇다 할 큰 무리 타격 파손 손실 부진 요란 치명적 훼손 편차 변화 동요 오차 누적 타격 텐션(little change)이 눈곱 기스 잔흔 일절 거의 전무 드물어 끄떡 잔잔 선방 생존 유지 버티어 무사 생환 살아남는 무적 좀비 생명력을 목도하지만!! 
반!!!!면!!!!!에!!!!!!!!!! 저 똥고집 반듯한 쇠파이프 성애자 미련 직진 충성 다림질 요부 '선형 회귀 다림질 모델 파벌 공주' 놈팽이 진영이 떠안고 감당 누적 마주 직면 환수 뒤집어쓴 테스트 실전 성적 MSE 빚더미 패널티 오류 오답 등본 파판 오폭 증식 빚잔치 장부에는... 구장이 꼬일수록 파이프가 다 부러져 궤멸, 구장 궤도 괴리를 못 따라가 엇박자 폭탄 우주 대참사! 진짜 눈알이 튀어나올 어마 무시 파국 막대한 천문학적 엄청난 대규모 오답 팽창 눈덩이 폭발 대참사 요동 누적 대거 거대 폭증 대격변 수직 폭주 치솟음 가세 수직 등반 부진 파산(large increase) 타격 대재앙 점수 폭망 파국 사태가 쓰나미로 전면 뒤통수 가격 강타 출몰 불어닥치고 맙니다! (직진 모델은 구부러진 길에서 다 절벽으로 떨어진단 뜻이죠!)

Figures 3.18 and 3.19 display situations in which KNN performs slightly worse than linear regression when the relationship is linear, but much better than linear regression for nonlinear situations.
결론적으로 지금까지 피 튀기며 본 양대 산맥 [그림 3.18]이며 [그림 3.19] 쌍방 투샷 투영 패널 종합 요약전 전시 스코어 계보 화면 현황 도면판 국면 기조는 아래 한 줄의 통쾌 모순 기막힌 상황 시정 역설을 요약 증세 대변 폭로 전시합니다: 
**"KNN이라는 이 변태 흡수 유연 괴수 모델 놈은... 애초 맵이 뻔하고 깡통 뻣뻣한 평탄 직진 일자 무식 '선형 고속도로' 모양새 기조 환경 구도일 때는? 남들 뻗어 나갈 때 괜히 오버 요가 떨다가 되려 직진 충성 다림질 선형 회귀 꼰대 경쟁 놈보다 아주 간발 차이 미세 소폭 좀 치사 아쉽게 성적 딸리고 구실 간발 못 봐주게 좀 약간 부진 못 미쳐 약세 추락해 미약 무던 살짝 덜컹 열세(slightly worse) 소심 구동 처참 부진 헤매지만! ....... 정작 판에 폭풍이 치고 태풍 꽈배기 곡예 타는 환장 널뛰기 '비선형(nonlinear)' 지옥 계곡 함정 구덩이 국면 미궁 비틀린 구불 길목 무쌍 절체 곡면 상황 텐션 야생 환경 늪에 진입 빠져 투하 맞닥뜨렸을 시기 때엔?! 직진하다 쳐박혀 박살 나는 똥볼 꼰대 선형 회귀 다림질 놈탱이를 그냥 영혼 우주 끝까지 유린 돌파 따돌리고 유연 관절 회피로 무쌍 학살 월등 월말 막강 아찔 치명 압도 타의 추종 불허 훨씬 기막히게 더 폭주 초능력 대거 월등 우월 절대 퍼펙트 슈퍼 무쌍 대박 더 무던 찬란 압도 막강 우수 잘난 능가 훌륭 엄청 더 비약 천재 활약 구동 만점 돌파(much better) 구출해 쟁취 버린다!"** 는 딜레마 모순 기면 상황 전경 투영입니다.

In a real life situation in which the true relationship is unknown, one might suspect that KNN should be favored over linear regression because it will at worst be slightly inferior to linear regression if the true relationship is linear, and may give substantially better results if the true relationship is non-linear.
이쯤 팩트 폭격을 듣고 나면... 도무지 신이 그린 진짜 이면 타겟 정답 궤적이 뭐로 일자일지 곡선일지 뱀장어일지 코빼기 통 도저히 앞이 하나도 까막눈 짐작도 깜깜 보이지 않는 험난 블라인드 '야생 찐 레알 일상 실전 지옥 상권 현실 현장 실무판 (real life situation)' 막막 구더기 지옥 국면 요건 실무 투입 상황에 맞닥뜨렸을 때! 
평범 사고 일선 고충 일반인 무리 실무자들 누군가는 문득 짱돌 굴리며, 당연 이런 대뇌 필터 합리 꼼수 도달 마인드 유통 사고 가망 의구심 합리 유치 사견 짐작을 얼핏 번뜩 품어 의심 상상 동조 옹호 지향 도출(might suspect)할지 모릅니다:
**"야 이거 씨바 가성비 계산기 돌려보니 손익비 사이즈 짱인데?! 차라리 귀찮게 뻣뻣하고 구불 길에선 폭망하는 그 무능 직진 꼰대 '선형 회귀' 따위 쓰레기 기법 통 버려 치우고... 무적 유연성 'KNN' 편 놈팡이 모델에다 내 전 영혼 올인 칩 베팅 편애 사랑 전폭 우대 지향 쏠림 취사 밀어주는 편(should be favored over)이 백번 천만 배 낫고 씹이득 당상 아닌가요??! 왜냐 묻는다면 팩트 방어 손익 교환! 만에 하나 천운 기적 요행으로 진짜 맵이 운 좋게 뻗은 일자 직선 '선형'이었다 쳐 바보 쳤다 가정 억까 쳐도?! 기껏 손해 봐봤자 끽해봐야 직진충한테 요만큼 아주 살짝 밀리는 간발 티끌 부진 손해(at worst be slightly inferior) 모기 타격 안일 찰과 처참 잃을 방어벽 밑져봐야 본전 안위 선빵이고! .... 근데 만~~에 하나 반대로! 정작 뚜껑 연 현실 찐 맵 길이 아주 오지게 꼬이고 비틀린 나이아가라 지옥도 생태 '비선형(non-linear)' 환장 파국 구덩이 곡면 지뢰밭 늪이었다면?! 우린 이 유연 갓KNN 관절 요가 마스크 파워로 직진충 다 제끼고 실질 엄청난 역대급 학살 천문학 규모 우수 퍼펙트 무쌍 대승 구사 결과 압살 잭팟 성과 기전 환수 창출(may give substantially better) 보답 압권 쟁취 무적 구원 생존을 배수진 대거 발악 건져낼 환상 극강 수익 뽑아 챙길 테니까요! 이게 바로 'Low 리스크, High 리턴' 꿀 도박 아닙니까 회장님!!"** .... 라며 말이죠.

But in reality, even when the true relationship is highly non-linear, KNN may still provide inferior results to linear regression.
하!!지!!!!만!!!!!!!!!!!!! 또 다시 이 잔인무도한 통계학 엿장수 악마 세계 얄궂 현실판 뒤통수 파국 호러 비틀림 지옥(But in reality) 기구 운명 참사 결말 극악호러 함정을 명심하십쇼!!!! 여러분이 그토록 철썩 찬양 맹신 꿀 빨려 망상했던 저 방패 신화 이면에는 끔찍 심연의 뒤통수 저승 함정 공포 딜레마가 마수 그림자 도사리고 기생 존재 대립합니다! 
신이 내린 그 참된 정답 $X,Y$ 본연 관계 타겟 형상 핏 꼬락서니가... 그야말로 역대급 극도로 미친 혼돈 구불 비틀린 아비규환 널뛰 발작 난상 초고도 악성 초강성 S급 극강 스케일 지옥 하드코어 난이도 '극강 꼬부랑 고도로 구불 심한 아찔 비선형 꽈배기 궤적 곡예 환장 기조(highly non-linear)' 기기묘묘 요란 발악 진상 양태 구장을 버젓 띄고 들이닥칠 그때 그 찰나 무색 국면 상황조차도(even when)!!!!! 
여러분의 믿었던 스펀지 유연 괴물 치트키 'KNN 요가 무골 놈팽이' 기법조차... 기절초풍! 도리어 저 미련 직진 충성 다림질 구형 깡통 모델인 '선형 회귀' 똥차 직립 녀석에게마저 점수 타점 개찔려 대량 실점 처맞고 부서져 무기력 참패 열세 패배 폭망 똥볼 나락 뒤쳐짐 하위 부진 꼬라박 불량 낙제 처참 열위 오답 점수 참사 낭패 결과물 배출(inferior results) 패악 낙제점을 배신하며 오싹 구사 토해 반환 선사할 가망 추락 절망 지옥 무덤 소지 여력 나락 리전 가능성이 아주 그야말로 버젓 무참히 생생 처참 기생 잔존 은둔 포괄 여전 생리 존재 생존 위협(may still provide) 버젓 노출 도만 잠복 개방되어 숨 쉬고 터진다는 이 기겁 피 토할 충격 통수 공포 대이변 뒤틀기 소름 각성 뒤집기 참사 붕괴 쇼크 반전 실체 징수 국면 지뢰밭 통수 팩트입니다!!!

**==> picture [315 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
p=1 p=2 p=3 p=4 p=10 p=20<br>0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0 0.2 0.5 1.0<br>1/K<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>Mean Squared Error 0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>**----- End of picture text -----**<br>

**FIGURE 3.20.** _Test MSE for linear regression (black dashed lines) and KNN (green curves) as the number of variables $p$ increases. The true function is nonlinear in the first variable, as in the lower panel in Figure 3.19, and does not depend on the additional variables. The performance of linear regression deteriorates slowly in the presence of these additional noise variables, whereas KNN’s performance degrades much more quickly as $p$ increases._

In particular, both Figures 3.18 and 3.19 illustrate settings with $p$ = 1 predictor.
이게 도대체 뭔 개소리고 어떻게 이런 호러 말도 안 되는 지옥 통제가 가능 터지는 반문 충격이냐고요? 자 실마리 진막 진실의 힌트 그 열쇠 복선 추적을 까봅시다! 각별 특별 유의해 지적 요지 환기하자면(In particular), 앞서 우리 눈을 멀게 했던 치명 환각 승전 도표인 [그림 3.18] 그리고 [그림 3.19] 기만 쌍방 콤비 양측 판넬 구도 상황 이면 전경은 죄다... 아주 치사 비겁 얍쌉하게도 우리가 구동 동원 무기력 탑재한 힌트 장부 설명 도구 무대 **투입 '예측 변수 숫자 개수(차원 총알 스탯)' $p$ 단위 척도 스케일 놈들이 달랑 온니 꼴랑 딱~ 고졸하게 1개($p=1$, 단일 힌트)!**... 라는 아주 졸라 개단순 소꿉장난 동네 단칸방 투명 평면 원시 1차원 직선 빈약 고정 초협소 한우물 장난 판넬 세팅 놀이터 국면(settings) 하강 조율 맞춤 모형에 한정 제한 국한 은밀 전재 구축 국한 모사 묘사 연계 가동 연출 한정 실험 일러스트 시뮬레이션 환경판 진열 결과물일 따름이었다는 기만 은닉 기믹 장막 기저 팩트 함정이 발악 핑계 전선 숨겨져 복선 도사리고 있었습니다!

But in higher dimensions, KNN often performs worse than linear regression.
하!지!만!! 이 소꿉장난 1차원을 벗어나 현실 빅데이터 세계! 힌트 변수가 수십 수백 개 쌓이는 개복잡 난해 다면 입체 우주 거대 미궁 공간! 이른바 변수 차원 수가 쭉쭉 천장 뚫고 늘어 늘어 아찔 팽창 폭증 확장 겹입 등반 돌파 비약 돌진해 펼쳐져 미쳐 터지는 다세포 괴물 거적때기 저 광활 고차원(higher dimensions) 실전 미궁 늪 지대 세계 영역 우주 초고도 판국 전장에 실체 강제 진입 돌입 투하되면?!! 
우리 요가 마스터 KNN 신화 괴물새끼는 그 수많은 힌트 미궁 차원 간격 우주 공백 거리감 방황의 저주 덫에 무참 짓눌려 공간 표류 길치 방향 상실 인지 치매 깡통 허우적 마비 잼민이 붕괴 아둔 퇴화 개호구 등신 길치 환자 장애 늪으로 전락 몰락 호러 부진 수직 나락 폼 떡락 발동 걸려..... 도리어 뻣뻣 단순 무식 직진 다림질 길치 없는 그 구닥 꼰대 깡통 '선형 회귀' 똥차 트럭 낡은 기법 녀석보다도 더 헤매며 억울 형편없게 길치 쓰레기 타점 오작동 오답률 부진 처참 열위 하락 하드코어 병신 뒤처짐 무득 똥볼 낙제 하위 랭크 부진 바보 실적 저능 폭망 퇴보 악전고투 수행 전락 꼬라박는 패전 처참 발악 빈도 붕괴 양태(worse than linear regression) 조장 구도 사태가 부지기수 빈번 비일비재 아주 밥 먹듯 번번 터져 만연 발생 연출 장악 노정 지배 전락 패가망신 빈출 터집니다!

Figure 3.20 considers the same strongly non-linear situation as in the second row of Figure 3.19, except that we have added additional _noise_ predictors that are not associated with the response.
이 끔찍한 차원의 저주를 직접 매 관전 목도 증명하기 위해, [그림 3.20] 심판 링 단두대 사형 판넬 투사 엑스레이 도화지 구장 관전판은.... 저 앞장 앞서 꿀 빨았던 [그림 3.19] 하단 두 번째 줄의 구불구불 미친 곡선 야생 하드코어 지옥불 극강 강력 최고조 돌연변이 S라인 꽈배기 나이아가라 굴곡 비선형 요동 진폭 요건(strongly non-linear) 구불 궤도를 도배 판넬 세팅 구도 그대로 100% 동일 복원 연계 토시 고스란 베껴 고수 모사 묘사 흡수 동일 복제 타진 채택 고려 인계 설정 뼈대 깔아 묵시 유지 탑재하면서도!! 
단!! 오로지 여기 이 악랄 무대 판국에다 단 하나의 얍삽 가미 미친 극악 파탄 치명 스파이 예외 조작 첨가 독극물 가변 양념 변모 기믹 조건을 무단 잔혹 단행 폭탄 수단 더 끼얹어 비틀었으니(except that)! 그건 바로 본 타겟 정답 매출(응답) 타점 점수 판도 맞추기 스탯이랑은 하등 쥐뿔 상관 간섭 영점 일절 무관 결부 연좌 아무짝 쓰레기 관계조차 생판 없는!! 오직 무의미 가짜 불순 시야 스텔스 마비 방해 교란 허상 기만 먼지 혼선 폭죽 신호 연막탄 지뢰 장치 잡범 구슬 조작 깡통 가짜 미끼! 이른바 개무가치 허섭스레기 잡동 더미 찌꺼기 깡통 잉여 **가스라이팅 폭탄 잡다 추가 잔재 _소음(noise, 잡음 노이즈 쓰레기)_ 예측 변수 폭탄 가짜 힌트 놈들 무더기**를 다수 허수단 수십 개 융탄 마구잡이 추가 생성 결집 동원 증식 파생 주입 기계 부가 난사 폭발 가미 융단 투척해 쑤셔 욱여넣어 복합 섞어 첨가 덫을 놓아 버린 조작 기만 장치(added additional noise predictors) 전장 늪 지대 폭파 늪을 꾸몄다는 농후 치명 무관 엉터리 함정 조건 차이 추가뿐입니다.

When $p$ = 1 or $p$ = 2, KNN outperforms linear regression.
자 이 지뢰밭 속 배틀 결과를 까볼까요. 가짜 힌트 변수 지뢰 지분율 변동 개수 차원 텐션인 총 동원 병력 파라미터 $p$ 무기 무리 숫자가 아직은 옹졸 가소 조막 스케일 수준 단칸방 크기인 고작 $p = 1$ (힌트 1개) 짜리이거나 혹은 여봐란듯 끽 겨우 그나마 좁쌀 핏 $p = 2$ (힌트 쌍) 풋내기 꼬마 차원 맵 옹졸 풋내기 영토 규모 조기 소규모 단계에 임계 머무를 무렵 당시 초장 찰나만 하더라도? 우리의 유연 스펀지 요가 무골호구 KNN 괴물 놈팽이는 아직까진 거뜬 짱짱 멀쩡 체모 멘탈 사수 유연 무쌍 휘날리며 저 구식 꼰대 다림질 똥차 직진충 선형 회귀 모의 녀석을 아주 능수능란 가뿐 압살 따돌림 무쌍 처바르고 짓누르며 훌륭 격조 압도적 제압 상회 앞선 전면 초월 압살 유린 제패 승리 성과(outperforms) 위용 퍼포먼스를 당당 고수 호쾌 질주 발휘 증명 기록해 냅니다.

But for $p$ = 3 the results are mixed, and for _p ≥_ 4 linear regression is superior to KNN.
하!지!만!!! 이놈의 가짜 잡동 힌트 변수 지뢰 숫자 스펙트럼 차원 지수 인자 $p$ 가 얄궂게도 스멀 부풀어 올라 문턱 **$p = 3$ (힌트 3개)** 단위 체비로 등반 슬쩍 발을 디뎌 몸집 진입 도달 떡상 돌파하는 순간부터?! 돌연 KNN 요주의 눈이 멀기 시작! 양대 모델 배틀 성적표 엎치락 딜 계측 결투 지표 양상 판도 결과는 오락가락 도긴개긴 피장파장 치열 오리무중 역전 짬뽕 우열 기로 혼선(mixed) 미궁 아노미 동급 늪 수렁 나락으로 요동 처박히더니....... 
드디어 이 씨발 놈의 가짜 힌트 개수 차원이 임계선 파국!! **$p \geq 4$ (힌트 변수 4개 이상 고차원 잡음 폭탄 지대) 거대 차원 무덤 마의 고고도 영역선 늪** 지수 잣대로 덩치 증폭 떡상 돌파 확장 개방 진입해 확장 가석 범람 치달아 무한 미궁 증식 팽창 폭파 덩치 텐션을 넘어서는 그 순간부터는?!!! 마침내 기적이 터집니다! 이젠 반대로 눈 막고 귀 막은 무식 깡통 직진 꼰대 아재 '선형 회귀 다림질' 구닥다리 탱크 트럭 녀석이, 가짜 힌트에 멘탈 나가 길 잃고 허우적대는 스펀지 치매 잼민이 놈팡이 KNN 모델 병신을 아예 등 뒤로 즈려 밟고 천상 멀리 초월 따돌리며 월등 등극! 절대 우월 절대 패권 왕좌 제패 압살! 앞도적 압살 우수 칭호 여실 월등 우위 절대 천상 선두 등판(superior to) 군림 승리를 대역전 쟁취 점령 탈환 이끌어 내며 퍼펙트 스코어 생환 보존 승전을 기록해 버리는 대 파란 참극 결과 판도가 노골 인증 연출 도출 노출 폭로 발생합니다!!!!

In fact, the increase in dimension has only caused a small deterioration in the linear regression test set MSE, but it has caused more than a ten-fold increase in the MSE for KNN.
이 역전극 피 튀기는 성적 파탄 통계 점수판 채점 국면 팩트 나락을 뜯어부검 뜯어보자면 이렇습니다!(In fact) 가짜 힌트 장난질(차원의 팽창, increase in dimension) 폭풍 지뢰가 미친 듯 난사 투척 되어도... 두 귀 다 막은 직진충 마이웨이 **'선형 회귀'** 고철 탱크 녀석한테는 직전 핏 테스트 판국 오답 에러 MSE 빚더미 성적 장부에 기껏 모기 두 방 물린 살짝 아주 미세 소폭 좀 거치장 잔열 잡동 부진 둔통 잔기스 기만 티끌 기스(small deterioration) 정도의 악영 퇴보 훼손 약간 손실 오차 기스 찰과상 추가 흠집 흔적밖엔 조장 안긴 가증 충격 타격 데미지 딜을 거의 티도 안 나게 노 데미지급 선방 별로 못 주고 튕겨 구토 버텨냈건만!!! 
반면에 미친 주관 없는 흡수 스펀지 KNN 관절 유연 놈탱이 자아 붕괴 놈의 실전 테스트 에러 MSE 오답 장부 시험지 나락 창구 점수통 폭격에는? 가히 멘탈 우주 붕괴 눈구녕 실명 핵 사태 발작 파문 지진 해일 쓰나미 파도 데미지 적중 붕괴 침수! 무려 당초 이전 대비 자그마치 숫자 가늠 상상 불허 대재앙 규모인 **'10배(ten-fold)' 이상 뻥튀기 극단 천문 폭발 대폭격 수직 증폭 폭파 가중 팽창 떡상 거대 점프 부채 나락 붕괴 수위 에러 대폭증 극적 부진 떡상(more than a ten-fold increase) 파멸 거구 오답률 요동 점프 증가 폭로 극딜 증가분 데미지** 타격 빚덩이 창궐 참사 파산 재앙을 왕창 때려 박아 초래 파산 직격 구토 나락 작살 맹폭 붕괴를 초래 무기력 연출 역 파산 침수 원흉 수작을 야기 처발생 조장 폭로 작살 내버렸기 때문입니다!!!

This decrease in performance as the dimension increases is a common problem for KNN, and results from the fact that in higher dimensions there is effectively a reduction in sample size.
이토록 가짜 힌트 차원 우주가 커질수록 모델이 우주 바보 치매가 되어 성능이 땅에 처박히는(decrease in performance) 환장할 우주 나락 파괴 병크 폭망 붕괴 추태 재앙 현상은, 유독 KNN 이놈들 종족 집안에서 지긋하게 유전 밥 먹듯 번번 도지는 흔해 빠진 종특 고질 암 투병 고정 단골 고질병 패시브 발작 맹점 만연 흔한 약점(common problem) 딜레마 치명 함정입니다. 이 병신 병은 대체 어떤 기전 팩트 우주 원리 깡통 재앙에서 무덤 비롯 기인 결과 파생 도출 원흉 연원 귀결(results from) 된 걸까요? 그건 바로 차원 축이 수십 개로 우뚝 우주 창조 거대 뻗은 초고차원 미궁 우주 방대 허공 지대(higher dimensions) 공간으로 빨려 나가는 돌입 역방향 진입 그 순간부터 덫에 걸려!!... 우리 눈에만 데이터가 그대로 50개일 뿐 실질 놈 입장 계산상으로는 존나 넓은 미궁 우주 은하수 허공에 먼지 50개가 산산이 멀리 광활 공구 뿌려 찢겨 단절 흩뿌려진 분산 고립 고아 표류 배치 탓에, 실질 효율상 내 근처에 아무도 없는 극단 밀도 고갈 현상! 즉 실효 방어 은닉 이웃 '샘플 동원 사이즈 머릿수 결핍 축소 붕괴 감소 기각 고갈(reduction in sample size)' 추방 가동 결핍 공황 단절 사태가 인접 전격 초래 터지고 은닉 유효 발동 전개 형성 발생 점거되기 때문입니다!

In this data set there are 50 training observations; when $p$ = 1, this provides enough information to accurately estimate $f(X)$.
자 이 비참한 모델 우주 고독 사태를 단적으로 예를 들어봅시다. 우리 족보 장부판에는 동네 훈련 관측 점박이 친구들이 달랑 딱 50명(50 training observations) 살고 있습니다. 맨 처음 방이 달랑 축 선 딱 하나($p = 1$, 1차원 직선 복도) 뿐일 땐? 50명이 그 좁은 복도 선 위에 오밀조밀 바글바글 미어터지게 촘촘 빽빽 다 밀집 살고 있으니, 내가 눈 감고 손 뻗어 옆에 닿는 이웃 50명 의견 힌트를 취합해 거뜬 넘칠 지식 정보 파워 제공 여력이 차고 흘러넘쳐, 내 신내림 정답 타겟 $f(X)$ 운명을 아주 칼같이 정확 예리 정밀 백발 탐지 추출 조명 추산 어림 타진 가늠(accurately estimate)할 수 있는 무한 찬란 위력 파워 여건 베이스를 탄탄 제공 기여 부합(provides enough information) 보강해 줍니다. 

However, spreading 50 observations over $p$ = 20 dimensions results in a phenomenon in which a given observation has no _nearby neighbors_ —this is the so-called _curse of dimensionality_ .
하지만!!! 똑같은 50명 인원 친구들 관측치 점들을 저 광활 무한 우주 공간 축 평점 20가닥 축 찢어진 사태 방원 미궁 허공 우주 **차원 $p=20$ 우주공간 평행세계 은하수 블랙홀 마당 맵**(20 dimensions) 전반에 걸쳐 허공 멀리 골고루 산산조각 우주 공구 전파 흩뿌려 방출 도포 살포 이식 전파 확산 파편 격리 흩트려 놓아 뿌렸다고(spreading) 쳐보십쇼! 
그럼 존나 무슨 개노답 아찔 현상 사태가 결론 도출 결과 파생 붕괴(results in a phenomenon) 발현 전개되느냐? 우주 시공간이 너무 허벌창 크고 방대 개방 아득 광활해져서... 그 넓은 허공 한복판에 혼자 똑 떨어진 나(주어진 관측 타점)를 기준으로 반경 백만 년 광년 주위를 미친 듯 아무리 손 저어 둘러봐도? 나랑 의견을 짬짜미 나눌 '가깝고 친한 밀접 인접한 존나 옆집 물리적 가까운 동맹 친구 **이웃(nearby neighbors)** 놈' 새끼 따위가 우주 평야 사방 텅 빈 반경 주변 천지에 말단 단 1마리 한 놈도 눈곱 찾아 전무 도무지 일절 근처 아예 전멸 고립 부재 실종 코빼기도 전혀 존재 안 하고 멸종 허공 없게 되는 무 간격 공백 우주 붕괴 초고립 현상 고아 나락 고독 사태 부재 현상 타격에 치명 처절 무방비 벌거숭이 직면 빠져버린다 이 말입니다! 
통계 오타쿠 학자들은 이 잔혹 허공 고아 미궁 딜레마 우주 마비 호러 우주 공포 나락 붕괴 사태 지경 병크를 두고 덜덜 떨며 아주 유창 비장 간지나는 중2병 스킬 명칭 언어로..... 이른바 전설의 **_"차원의 저주 (Curse of Dimensionality)"_** 치명 함정 타격 덫 나락 독재 신드롬이라 지칭 네이밍 포장 명명 부르고 칭하여 경계 절망 떱니다! (힌트가 많아지면 망한다는 저주!)

That is, the _K_ observations that are nearest to a given test observation _x_ 0 may be very far away from _x_ 0 in $p$ -dimensional space when $p$ is large, leading to a very poor prediction of f ( _x_ 0) and hence a poor KNN fit.
즉 차원의 저주를 좀 더 적나라하게 소름 끼치게 직역 풀어드리면 이겁니다! "KNN 치트키는 지 무덤 파는 줄도 모르고 내 곁 $x_0$ 목푯값 옆에 제일 가까운 $K$명을 다수결한답시고 멱살 잡고 끌고 오려고 억지 짓을 치겠지만... 허공 차원 스펙 $p$ 축이 존나 큰 우주급 규모 거구($p$ is large) 광활 미궁 고차원 공간 상황 국면하에서는, 그나마 제일 '가장 물리 가장 가까운 1등 인접 거리(nearest)' 랍시고 데려온 이웃 K명 후보 새끼들조차도! 실상 우주 스케일 공간 광년 좌표 입장에선 나한테서 안드로메다 수만 킬로 저 멀리 아스라이 멀어진 채 남남 생판 타지 이역만리 외딴 공역 먼지 구역 존나 우주 동떨어진 (very far away from) 아방궁 외곽 전혀 생판 무관 무상관 억지 근방 남남 생판 남 잡동사니 괴리 동떨어진 별개 외계인 이웃 놈팽이 관측 점 점박이들일 가망 소지 폭주 확률 함정이 무참 극명 팽창 터져 발생한다는 것!" 
이리되면 억지로 그 남남 외계인 놈들 의견 끌고 와 평균 N빵 낸들, 지 엉뚱 남의 외계 동네 궤적 우주 곡률 스펙으로 엉만진창 소설 오답 쓰레기 예측 추론 가늠 치수(f($x_0$) 도출 타점 선포) 찍어 발작 남발 추방(very poor prediction) 판독만 더 처발라 거하게 낳게 될 뿐이고! 고로 종국적으로 억지 오답 연동 이음 오차 빚덩어리의 구제 불능 나락 개판 부실 쓰레기 파탄 병신 형편없는 개오답 **돌연변이 똥볼 KNN 궤도 오차 적합선 오작동 적중(poor KNN fit)** 결과 맹점 함정 몰락 부재만 치명 가속 유도 증식 나락 초래 이끌어 전락 지배당하게(leading to) 낳는단 쓰라린 인과 법칙 파멸 과정 결론입니다! 

As a general rule, parametric methods will tend to outperform non-parametric approaches when there is a small number of observations per predictor.
자 이것으로 피 튀기는 대결 마침표 종합 결론 정석을 선포합니다! "이 바닥 실전 데이터 통계 현장 야생 구장 룰에 입각한 대전제 일반 십계명 보편 전법 법칙 룰(general rule) 하나!" 
**[결론] >>>** 만약 우리 손에 쥐어진 장부 족보 스펙 속 예측 변수 동원 무기(힌트 차원 축 1개당) 단위별로 할당된 보유 '관측치 점박이 머릿수 샘플 데이터 예산 덩치 인력 병력 데이터 개수' 비율 자체가 존나 협소 쥐꼬리 가난 부실 극소수 미미 소규모 짜투리 빈곤 한정 결핍(small number of observations) 가뭄 허덕 바닥 환경 국면 조악 지표 처지 단면 세팅 시점 구장 투사 국면 조건이라면??! ... 이런 결핍 난세 빈곤 맵 허덕 텅 빈 허공 장부 국면하에서는 묻지도 따지지도 불문!! 찰흙 유연 관절 '비모수적 요동 접근법 짬뽕 괴수(KNN 따위)' 무리들 보다는...! 차라리 무식 깡통 고집 직선 불변 뚝심파 관절 굳은 **'뼈대 모수적 결착 방법론 꼰대(선형 회귀 다림질 등)' 전차 참전 일진 방패 부대 녀석들이... 오답 똥볼 늪 표류 차원의 저주에 안 걸리고 압도 월등 기막힌 방어적 승리 우월 무적 생환 초월 제압 승전 능가 우수 앞섬 상회 제패 선방 성과(tend to outperform)를 당당 맹활약 구가 달성 거머쥘 호황 승리 경향 우주 깡패 소지 가능 텐션 승산이 아주 배타 백배 더 무쌍 크고 만연 농후 유리 지배 압도적이다!!** 라는 절대 무쌍 전략 승리 픽 선택 대원칙 승전 계시론입니다.

Even when the dimension is small, we might prefer linear regression to KNN from an interpretability standpoint.
더 나아가, 솔직히 설령 차원 축 기만 숫자가 요란 안 넓고 $p=1$ 같이 고도로 앙증 소규모 단칸방 안전 닫힌 소박 초특급 미니 단차원 맵 지대(dimension is small) 구장 무대 실험 콤팩트 안전 국면 세팅 조우 시점 맞춤이라고 하더라도요?? 우리 속물 인간 실무자들 비즈니스 보고서 대면 기조 마인드 심상 결재판 눈높이 입장에서는... 오직 단순 그 무적 깡패 '원인-결과 인간 상식 해명 기조 설득 논리 통찰 해석력!(interpretability standpoint) 가독성 해석 마스터' 라는 단일 그 실용 기만 무쌍 관점 기조 렌즈 척도 하나 매력 포화 장점 무기 관점 핑계 만으로도! 당당히 KNN 괴수 버리고 미련 없이 대놓고 편애로 줄기차게 죽고 못 살아 꼰대 직진 충성파 '선형 회귀 다림질 녀석' 단자를 우리 맘껏 골라 편애 입양 더 옹호 선호 편애 선별(prefer to) 채택 총애 채택 구사 남발 밀어 지향 채용할 여력 여지 소지 핑계 합리 기조는 영원 차고 아주 넘치고 다분 떡발 무한 무장 기저 만연합니다! (보고서 쓰기 편하니까!)

If the test MSE of KNN is only slightly lower than that of linear regression, we might be willing to forego a little bit of prediction accuracy for the sake of a simple model that can be described in terms of just a few coefficients, and for which $p$-values are available.
즉 현실 실무 마인드 최종 가성비 협상의 결기 타결 속내는 이렇습니다! 
**"까짓거 지옥 실전 구장 시험 테스트판 굴려봤더니 유연 기괴망측 KNN 스펀지 놈이 우리 선형 회귀 꼰대 놈보다 에러 오차 빚더미(Test MSE) 스펙 방어 타점에서 끽해봐야 고작 '좀 아주 눈곱 쪼금 티끌 간발 모기 침 미만 잔기스 미세 조금 약간 아주 살짝 더 하위 낮고 오차 에러 덜 내서' 쪼~끔 아주 쬐~끔 더 잘난 맞춤 기특 성능 정답 찍기 살짝 승리 성적 부합 선방 결과판(only slightly lower) 점수 우위 미약 초라 격차 승전고 꼴랑 토해 찍어 냈다 가불 억까 가정해 칩시다! 그딴 미세 푼돈 쥐꼬리 정확도 차이 깟거 푼돈 차라리 눈 감고 쿨하게 포기 희생 관대 탕감 반납 양보 헌납 타협 개나 주고 내던져 쿨 양보 상환(willing to forego) 통 크게 미련 버려서 출혈 감수하더라도!... 우린 차라리 사장님 앞에서 $\beta_1, \beta_2$ '쪼가리 몇 개 계수 숫자 조각 몇 개 나부랭이 단어 단자 항목 요건(just a few coefficients)'만 입털며 달랑 깔끔 조달 풀어 직관 해석 통조림 요약 압축 요점 제시 해명 혓바닥 브리핑 설명 조달(described) 아주 짱 간편 심플하게 무사 통과 이빨 입 털릴 수 있고! 더구나 덤으로 이딴 장사 약팔이가 찐인지 사기인지 판사님이 도장 쾅쾅 보증 공증 찍어 합격 징수 방어 꼬리표 면죄 증빙 서류 팩트폭격 심판 부록으로 요긴 조달 거금 '기출 절대 가치 유의 판정 합격 보증수표 기적 판독기 부록 $p$-값(p-values)' 스펙 방어망 무기 보루 꼬리표마저 아주 무쌍 너끈 두둑 친절 가용 제공 넉넉 보급 혜택 지원 확보 차용(available) 타진 활용 가능한 그 미친 비즈니스 극강 꿀 가성비 극강 가독 효도 단순성 짱! 눈부신 우리 위대한 영광 불멸 '심플 해석 최고존엄 단순 모델(simple model)' 뼈대 영웅 깡통 직진 선형 회귀 녀석의 그 위대한 품과 영예 혜택 광명 구원 안식 보장 실용을 위해서라면 기꺼이 그딴 1% 예측률 손실 따위 웃으며 과감 타협 다 기저 내던져 상납 감수 출혈 치러 맞바꾸며 대리 채택 희생 포기 맞짱 감수 교환 지향할 용의가 우리는 아주 무한 충만 철통 백배 충분 무장 넉넉 10,000% 무궁 포섭 결의 차 있다 이 말입니다 회장님!! (결론: 선형 회귀가 짱이다.)"**

---

## Sub-Chapters (하위 목차)


[< 3.4 The Marketing Plan](../3_4_the_marketing_plan/trans2.html) | [3.6 Lab Linear Regression >](../3_6_lab_linear_regression/trans2.html)

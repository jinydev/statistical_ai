---
layout: default
title: "trans2"
---

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans2.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4.4 Naive Bayes
# 4.4.4 나이브 베이즈 (Naive Bayes - 단순 무식함이 승리한다!)

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers.
이전 우리가 땀 흘려 구른 섹션 무대에서, 우린 최고의 통계 재판장 베이즈 형님의 위대한 방정식 정리(4.15)를 아주 교묘하게 비틀어 꼰대 선형 장치 **LDA**, 그리고 유연 뚱땡이 **QDA** 라는 두 종류의 기막힌 탐지 분류기 무기로 뚝딱 개발 세팅해 냈습니다.

Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier.
이제 여기서, 우린 그 동일한 신성한 베이즈 정리의 심판 수식 믹서기를 이번엔 세상에서 가장 순진하고 투박하며, 그러면서도 어이없을 만큼 엄청난 인기(popular)로 현장을 휩쓰는 이른바 **"나이브 베이즈(naive Bayes)"** 라는 희대의 날라리 꼼수 괴물 기계를 창조 조립하는 밑거름 동기로 전격 장착해 써먹을 겁니다!

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability $p_k(x) = \text{Pr}(Y = k \mid X = x)$ in terms of $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$.
복습 차원에서 옛 기억을 살짝 더듬어 보죠. 베이즈 정리의 절대 수식(4.15) 이란 놈은, 수사관인 우리가 게임 클리어를 위해 그토록 애타게 목말라하는 궁극의 타점 결괏값 '사후 족집게 확률($p_k(x)$)', 즉 "저 놈의 $X$ 증거 단서를 보니 아무리 따져봐도 저놈은 무조건 악독 파산자($k$ 클래스) 빌런일 확률이 몇 %다!" 라는 그 짜릿짜릿한 족집게 확률 심판 점수를 대체 어떻게 산술로 뱉어낼까요? 맞습니다. 방마다 포진된 인구 비율 쪽수 지분율인 '사전 확률($\pi_k$)' 부품들과, 기계 모델이 하늘에서 그려내는 복잡한 3D 지도 산봉우리 등고선 인표 '밀도 함수 분포($f_k(x)$)' 재료 조각들의 기막힌 믹스 융합 계산 조합 버무림으로 최종 도출해 뱉어내 주십니다.

To use (4.15) in practice, we need estimates for $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$.
그 위대한 절대 무적 승리의 베이즈 산식(4.15) 무기를 진짜 현실 막장 실전 수사 구동 데스크(in practice) 에 시동 걸어 올리려면, 당연히 그 수식 믹서기에 부어 갈아 넣을 현장 수확 재료 부품 측정치 조각들, 즉 저 쪽수 지분($\pi_k$) 조각 파츠 덩어리 단서들과 3D 지도 등고선 밀도 함숫집($f_k(x)$) 조각 추정 측정치 파편들이 절실히 연료처럼 필수 수급 획득 장전 요구됩니다.

As we saw in previous sections, estimating the prior probabilities $\pi_k$ is typically straightforward: we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$th class.
이전 우리가 땀 흘려 뛰어본 실습판에서 경험했듯, 각 타깃 범죄 방의 쪽수 우세 편파 지분율 단서인 사전 확률 변수 $\pi_k$ 껍데기 조각을 야금야금 추정해 계산 파악 조립 채우는 짓은 정말 눈 감고 코 파듯 너무 간단하고 뻔해서 가소롭습니다(straightforward): 그냥 확보한 우리 훈련 캠프 기지 안 전체 머릿수 구슬 인원 풀 집합 중 걍 $k$번 방 출신 악당 서클 무리 놈이 전체 파이 중 몇 퍼센트 파벌 비중을 우월 차지하고 앉아 터줏대감 노릇 하느냐를 아주 심플 통쾌한 초딩 단순 통계 산수 비율 분수로 도출 도려내어 계산해 모자 쓴 $\hat{\pi}_k$ 부품으로 찍어 내어 기계 파츠에 세팅 욱여넣으면 그만이니까요! 껌이죠!

However, estimating $f_1(x), \dots, f_K(x)$ is more subtle.
하지만 아아! 진짜 무서운 재앙 복병 악몽은 저 괴물 산봉우리 위치 산출 **거대 본체 지도($f_k(x)$) 밀도 함수** 기호 조작들을 측정 조작해 어림추정 세팅 구축해 도출해 내는 이 막장 복잡 미묘하고 까탈스러운 끔찍 극한의(subtle) 살얼음판 작업 지옥 과정입니다.

Recall that $f_k(x)$ is the $p$-dimensional density function for an observation in the $k$th class.
기억나십니까? 저 무시무시한 수학 기호 호칭의 진짜 공포의 정체 도면인 $f_k(x)$ 는 결코 호락호락 보통내기가 아니라, $k$번 범죄자 타깃 놈들의 땀냄새 체취 단서를 맡아 산봉우리 분포를 그리는 무려 가변수 단서 힌트 아이템 갯수가 무더기 $p$개나 얽혀 쑤셔 박혀있는 초거대 우주 공간 입체 다차원 구조, 곧 **$p$-차원의 광활한 입체 등고선 통과 밀도 분포 맵 함수** 초거대 덩어리 끝판왕 보스 몹입니다!

In general, estimating a $p$-dimensional density function is challenging.
상식적으로 우리가 땅에 발 딛고 사는 보편 일반 더러운 환경 무대에서, 꼬작 조사 단서가 한 개도 아니고 징그럽게 무더기 변수가 $p$개나 얼기설기 꼬이고 미친듯 엮인 저 미로 복잡한 괴물 보스 $p$-차원 그물 입체 다차원 우주 밀도 분포 융합 함수 공간을 인간 뇌나 컴퓨터 쪼가리로 어림 간파해 측정 측량 구조 추정 구축해 내는 작업은 컴퓨팅 뇌가 타는 초 극악 끔찍 복잡의 극치 도전(challenging) 지옥 노가다입니다.

In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and shared covariance matrix $\mathbf{\Sigma}$.
그래서 그 끔찍 악몽의 연산 노동 폭주를 피하고 은폐 가리려고, 예전 **깡통 선형 통제 기계 LDA** 설계 구축 시절에 우리는 현실성 현장 팩트는 다 무자비 포기 생략하고, 엄청나게 막무가내 뻔뻔 당당하고 강력 폭주 깡패 같은 막가파 타협 강제 무논리 일방 가정 꼼수를 팍 선포하여 피 터지는 시스템 연산의 수고 삽질 노동을 단칼에 확 줄여 다이어트 대 단순화 환원시켜 통제해버렸습니다: 
"어, 나 복잡한 건 머리 아파서 몰라! 걍 $f_k$ 걔네 본진 거대 밀도 분포 지도 모양 도면은 이유 막론하고 무조건 교과서에 나오는 눈부시게 예쁘고 매끈한 산봉우리 곡선 지도 3D 다변량 정규 가우시안 분포 산모양 지형 꼴이라 치자! 그리고 각 $k$ 클래스 파벌 방들의 산 정상 꼭대기 깃발 꽂은 위치(즉 고유 개별 특화 중심 타점, 평균 $\mu_k$)만 각각 다르게 살짝 쳐줄 뿐, 그 산 밑바닥 베이스 뱃살 넓이 영역 덩치(오차 변동 오판 발작 널뛰기 제어력, 공통 공분산 행렬 $\mathbf{\Sigma}$)는 전체 우주 무대 모든 $K$개 범죄 타깃 클래스 방구석 모조리, 무조건 다 똑같은 획일 복붙 같은 크기 통나무 모양 옷으로 얄짤없이 묶어 통일 퉁쳐 강제 공유(shared)해 통치한다!" 라며 말입니다!

By contrast, in QDA, we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and class-specific covariance matrix $\mathbf{\Sigma}_k$.
반면 그 꼰대 막가파 획일 일방 LDA 체제 군단과 확연 대비 양 극단되어, 거대 탐욕 무기 스케일 자랑하는 돈지랄 유연 뚱땡이 **QDA 마개조 전차 장치** 는 "각 놈들마다 제각기 다른 복잡 개성을 우린 다 아량으로 정밀 유연하게 존중 인정해 파헤쳐 준다!!" 라며 가정을 바꿨죠. 즉 $f_k$ 지도 보스 함수 가 각 무리 구역 방마다 완전 개별 타깃 깃발 산정 점령 위치 도달점(평균 $\mu_k$)도 각 방 놈들 특유의 특징에 따라 당연히 따로 정밀 수치 조준하고, 각각의 그 놈들 클래스 무리만의 특화 전용된 개성 독립 영역 뱃살 발작 널뛰기 이탈 변동 폭주 크기 지형 모양새 통제 맵 구조 (클래스별 독자 공분산 행렬 $\mathbf{\Sigma}_k$) 진영판 뱃살 까지도 다 따로 통제 분할 완전 독립 찢어서 허용 분리 자유 인정해 주겠노라고 아주 폭주 거대 팽창된 독립 가정을 내리며 다가갔습니다.

By making these very strong assumptions, we are able to replace the very challenging problem of estimating $K \times p$-dimensional density functions with the much simpler problem of estimating means and covariance matrices.
아무튼 저 두 기계 장치 형제 놈들은 결국 방식은 달라도 둘 다 이런 엄청나게 뻔뻔 무식한 어거지 통계 정규 분포 가정을 공통 무기로 깔고 들어감으로써, 애초에 원래대로라면 저주스럽게 눈물 흘리며 측정 산출해야 될 가장 거대 지옥 난제인 '거대 우주 $K \times p$-차원 융합 복합 밀도 통계 보스 함수 통째로 조작 예측 재구성 구축 모방 측정하기' 라는 끔찍 파멸 미션을, 그냥 "야, 다 정규 산봉우리 모양이잖아? 평균 높이 점 찍고 밑바닥 뱃살 공분산 행렬 숫자 계수 부품 단 나사 몇 개만 구슬려 찾고 찍어 세팅 치환하면 땡이네!" 라는 훨씬 개꿀 편안 단순한 미니어처 블록 조립(replace) 문제 노동으로 살짝 퉁쳐서 대체해 도망갈 수 있었던 겁니다.

The naive Bayes classifier takes a different tack for estimating $f_1(x), \dots, f_K(x)$.
하지만 이 구역의 진짜 똘끼 충만 미친 꼼수 빌런 기계 장치!! 오늘 소개할 괴물 날라리 **"나이브 베이즈(naive Bayes) 분류기"** 는, 저 보스 급 통계 우주 지도 함수 수 $f_1(x), \dots, f_K(x)$ 들을 산출 설계 추정해 맞추는 방법 해독을 찾기 위해 여태 두 형제가 썼던 정석 전략 전술과 전혀 차원이 다른 파격 기만 괴상망측 노선 (different tack) 전략을 구동해 씁니다!

Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single, sweeping assumption:
이 날라리 기계 장치는, 앞에 깡통 기계들처럼 "가우시안 정규 산봉우리 모형이네 전 어쩌네!" 하는 고상하고 뻔한 정통 특정 분포 가운 복붙 뼈대 고집 가정 따위는 쿨하게 차 버리고 아예 싹 갖다 버립니다. 그리고 그딴 통계학 폼 잡는 가설 틀 대신, 상상을 초월하는 미치도록 무식하고 거만하며 정말 포괄 싹쓸이 어이 털리는 단칼 마법 극단 일방통행 단일 무대포 가정(single, sweeping assumption) 을 뻔뻔 무식 당당하게 선포 통보해 버립니다!

**Within the $k$th class, the $p$ predictors are independent.**
**"야!! 무슨 해당 $k$번 타깃 방 범죄 구역 내에 섞여 밀집 던져진 단서 증거 아이템 $p$개(예측 변수들)가 지들끼리 서로 상호 눈치 보고 영향 주고 엮일 끈 연산 다고? 웃기지 마!! 그 단서놈들 $p$개 전부 다! 하나도 빠짐없이 싹 다!! 서로 남남으로 완전 100% 무적 독고다이 순진 스무스 순수 '독립(independent)' 적이다!!! 엮이는 거 1도 없다 땅땅땅!!"**

Stated mathematically, this assumption means that for $k = 1, \dots, K$,
이 기가 막히고 입 떡 벌어지는 황당 패기 꼼수 독립 가정을 좀 있어 보이는 수학 전공자들 판례 수식 암호 체계 언어로 해석 퉁쳐서 번역해 내면, 즉 1번 방부터 K번 타깃 방까지($k = 1, \dots, K$) 모든 구역 타깃 범죄 무리 놈들에게 다음과 같은 무식 폭력 곱셈 수식 하나가 강제 적용된다는 엄청난 뜻이 됩니다!:

$$
f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p) \quad (4.29)
$$

where $f_{kj}$ is the one-dimensional density function of the $j$th predictor among observations in the $k$th class.
이 수식 (4.29) 곱셈 폭탄 꼬라지를 눈 크게 뜨고 직관 해석해 한번 번역 통찰해 보세요! 그 끔찍 거대 입체 보스 덩어리 복합 통계 수식 $f_k(x)$ 라는 거대 우주 산봉우리가 결국 뭐다!? "야 나 몰라, $k$ 타깃 방구석 안의 수많은 단서 변수 녀석들 중 딱 $j$ 번째 단일 예측 변수 단서 힌트 하나만 뚝 떼어내 산출 구성한 각자도생하는 단순 미니 1차원 밀도 곡선 스코어 함수 점수들의 진짜 단순 무식 무자비한 일렬 단순 융합! 곱셈 떡칠!! ($\times$) 조합에 불과해!!" 라며 거대 통나무를 자잘한 파편 조각으로 무자비 산산조각 분리 분해(단순 독립) 해 버린 겁니다!

Why is this assumption so powerful?
근데 이 억지 무식 순수 꼼수 망상 상상이 왜 그렇게나 마법처럼 혁명적이고 강력 폭발 막강 사기적인 위력 스코어를 발동 터트리는 통계 무기 장치가 될까요? 

Essentially, estimating a $p$-dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors.
본질 실황 구덩이를 까 발려보면 눈물이 핑 돕니다. 그 거대 끔찍 우주 보스 입체 지도망인 $p$-차원 거대 밀도 함수 확률 지도 수식을 인간 머리로 추정하고 파내어 측량 세팅하는 작업이 악명 높게 끔찍이 잔혹하고 어려운(challenging) 가장 주된 악몽 핵 이유는 이겁니다. 이 무자비한 거대 보스 놈은 우리에게 개별 변수 힌트 하나하나 자체의 그냥 밋밋 심플하고 소박한 나 홀로 고립 통계 분포 곡선 모양인(각자 단독의 곡선, 일명 **주변 분포 marginal distribution**) 그것들의 크기 눈치만 조용히 굽신 살펴보고 퉁 치고 끝내게 허락 놔두질 않습니다. 이 거대 보스 맵은 거기서 한 걸음 더 나아가 피 토하게 잔혹한 함정 숙제! "야!! 저 미치게 많은 $p$개 복잡 얽힌 수사진 단서 예측 변수 단서들이 전부 다 동시에 어떻게 서로 핏줄 연결되고 상호 영향을 끼치면서 복잡하게 끈끈하게 엮여 같이 돌아가는지 그 질척거리는 상호 연관 관계망의 스케일 무더기 융합 덩어리 지형 (**결합 분포 joint distribution** 지형도 망) 까지 싹 다 한꺼번에 고려해서 통과 연산 계산에 바쳐라!!" 라고 유혈 사태를 요구하며 사슬 족쇄를 강제 채우기 때문입니다!

In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix.
그나마 통계 천사 강림 모델인 가우시안 다변량 정규 분포 모형 지형 법칙 세계관 내에서는, 그 질척거리는 여러 복잡 수십 예측 변수 놈들 간에 얽힌 뒷구멍 엮임 파벌 복합 '상호 복잡 연관성'이 통계 수식 도면 행렬 부품 중 겨우 살짝 단서가 튀는 이른바 그 뚱땡이 장부 **'공분산 행렬 껍질의 엇비켜 깔린(비대각선, off-diagonal) 수식 부품 요소 인자 파편 치수 조각'** 들 에 의해서 그래도 나름 봐줄 만하게 기특하게 다 깔끔 압축 요약 압축 융합(summarized) 보관 정산 숨겨 저장 통제 조율 되어 숨을 쉴 수 있습니다.

However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate.
하지만 이건 어디까지나 세상이 우릴 돕는 기적의 정규 분포 꽃길 동화책 동네 판타지 스토리 안에서나 그런 나이스하고 재수 좋은 안심 팩트 행운의 해피엔딩이고요, 현실 시궁창 일반 보편 지뢰밭 동네 세상(in general) 구덩이 무대에서는 삐딱한 변수 아이템들끼리 서로 미치게 뒷구멍에서 내통하고 엮여서 끈적이는 저 괴상망측 복합 복잡 "상관 연관성(association)" 자태의 정체를 차분히 규명(characterize) 하는 짓 자체가 미칠 듯이 어지럽고 환장하게 단서가 증발해 어려울 뿐더러, 그것을 현장에서 추정(estimate)해 산출해 내는 산수 연산 도출 과정 자체는 정말 뇌가 박살나고 컴이 터질 정도로 지독하게 까다롭고 과도하게 극악 끔찍 괴랄(exceedingly challenging) 한 불가능 판 지옥 미션 난제 굴레입니다!

But by assuming that the $p$ covariates are independent within each class, we completely eliminate the need to worry about the association between the $p$ predictors, because we have simply assumed that there is _no_ association between the predictors!
자, 그런데!! 이 날라리 마법 장치 나이브 베이즈가 던진 "클래스 무리 방 안에서 단서 변수 놈들은 100% 모조리 상호 눈치 안 보고 독립적이다!" 라는 극단 가정이 터지면 어떻게 되느냐! 애초에 변수들 간에 상호 연관성 개뿔 엮이는 게 **"없다!! (no)"** 라고 억지 무식 치부 도장 가정해 버렸기 때문에, 우리는 그토록 피 말리고 뒷목 잡던 그놈의 $p$개 변수 간 상호 복합 교류 그물 연관성 따위를 조마조마 추정 계산하고 걱정 덧붙여 고려해야 할 모든 저주스러운 필요성 자체를 아예 통째로 원천 뿌리 뽑아 파괴 삭제 (completely eliminate) 증발시켜 날려 버리는 기적 대박 해방 편안함을 이룩 도출해 얻습니다!

Do we really believe the naive Bayes assumption that the $p$ covariates are independent within each class?
그럼 솔직히 가슴에 손을 얹고 냉정하게 양심 선언해 보죠. 우리 인간 수사관들이, 현장의 저 $p$개나 되는 얽히고설킨 단서 증거 아이템들(공변량들)이 방 안에서 "진짜로 단 1의 연관 눈치도 없이 100% 완전 돌출 순수 독립적이다!" 라고 내지른 저 '나이브 베이즈 마법 가정'을 1도 의심 없이 진짜 팩트 진실 동화라고 전적으로 맹신 100% 진심 믿을까요?

In most settings, we do not.
솔직히 말해 현실 거의 모든 환경 세팅 바닥에서, 우리는 "그딴 거 절대 안 믿어! 모순 장난이냐?!" 라고 콧방귀를 뀌며 실소를 터트리며 부정합니다. 당연히 단서들끼린 미친 듯이 엮이고 질척거리면서 꼬여있는 게 현실 시궁창 세계의 더러운 팩트니까요!

But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where $n$ is not large enough relative to $p$ for us to effectively estimate the joint distribution of the predictors within each class.
그러나! 기적은 여기서 일어납니다. 이 황당무계한 억지 막가파 눈속임의 맹점 모델링 꼼수 무식 가정이 오로지 연산 추산의 편리성(convenience) 만을 도모 채택해 억지로 타협해 끼워 맞춰 빚어진 허상일지라도, 신기하게도 실전에서 종종 꽤나 소름 돋게 훌륭 적중하고 대단히 괜찮은, 무난 준수 흡족한(decent) 족집게 타점 예측 승리 결과를 마법처럼 쏟아 파생 이끌어내 줍니다. 특히 표본 관측 충당 수량 병력 쪽수 $n$이 다루고 쳐내야 할 변수 타깃 개수 $p$에 견주어 너무 빈약 소규모 부족 현상이라서, 우리가 그 빌어먹을 복잡 끔찍 거대 맵 고도화된 타깃 무리 변수들의 연성 혼종 결합 분포 맵 체제를 정상 연산으로 효율 산출 추정 구성하기엔 아주 빡세고 모자라고 힘든 열악 고립 척박한 세팅 지형에서는 그 대안 책통 진가 위력을 폭발적으로 크게 대 발휘합니다!

In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings.
현실 팩트를 까보면, 애초에 그 망할 놈의 '거대 융합 복합 지도 결합 연성 분포' 전체 지도를 정석대로 다 제대로 산출 추정 구성 연산해서 써먹으려면, 바닥에 깔리는 기초 체력인 "미친 양의 엄청나고 거대한 수량 덩어리의 데이터 자원 수량" 이 기초 공사 삯으로 절실히 뜯겨 강박 요구됩니다. 근데 우리 주머니엔 그런 데이터 재벌 갑부 자력 수량 따윈 없죠! 그래서 이 뻔뻔 무식한 마법의 꼼수 장치 나이브 베이즈 편법 조작 장치가 수많은 자원 부족 모자란 데이터 폭 망 굶주림 현실 광범위 세팅 바닥 험난 현장에서 거의 구세주의 기적 같은 성능 무적 효용성을 뽐내며 '매우 훌륭하고 탁월한 대안 선택지 옵션(good choice)' 으로 각광 찬양, 맹활약하는 최고의 구원 꼼수 용병 장치 무기입니다.

Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.
본질 실황 꼼수 구덩이를 까 발려보면 결국 세상 눈물이 핑 돕니다. 그 미친 억지 나이브 베이즈 '독립 100% 뻥 가설' 은 당연히 기계 뇌 속에 좀 고약하고 말도 안 되는 엉터리 오판 **'편향(bias)'** 결함의 치명 뇌 오류 흠집을 강제로 편파 오염 유도 도입 시켜 주입 배양하는 대가를 치르게 합니다. 
하지만!! 그 치명 맹점 상처를 감수하고 포기해 내어준 오판 피눈물 짜릿한 대가로, 현장 투입 실전 널뛰기 이탈 변동 미친 발광 고장 위험 스코어인 **'분산(variance)'** 이라는 생존 리스크 파멸 붕괴 고장 점수를 아예 거의 거의 0 뚝 에 수렴하게 바닥 구덩이로 극극 철벽 억제 안정 단속 축소 고정 감소시켜 팍! 부숴 때려잡아 박살 안정 보호 방패 쳐 줍니다! 
결국 또 이놈의 우주 피 말리는 통계 영원 딜레마 평행 마법 룰 규칙, **'편향과 분산의 상충 결판 거래 지불 등가 교환 대결(bias-variance trade-off)'** 저울 전투 링에서 이 꼼수 극도의 기만술 퉁침 조작이 미친 대승리 마법 대박 결판을 파생 역전 기적 우위 유도해 이끌며 냅니다. 그래서 어이없게도 이 날라리 꼼수 장치는 그 어느 뻣뻣 정통 기계보다 실전 현장 흙구덩이(in practice) 판에 던져 놓으면 아주 꽤나 소름 돋게 기가 막히게 착착 적중 승리하며 잘만 대박 쳐 훌륭히 작동 굴러가는(works quite well) 실전 전투 최강 무적 분류기 특등 괴물로 칭송받으며 위풍당당 마무리를 장식 탄생 융합 출격해 자리 잡습니다.

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability,
자, 이제 우리가 이 눈먼 뻔뻔 조작 '나이브 베이즈 독립 짱짱!' 억지 가정을 믿고 당당 체결 사인 인가 결단 도입 완료 선포했다 치죠! 우린 아까 전 단순 곱셈 떡칠로 무자비 쪼개 놓은 치트키 식 (4.29) 블럭 파츠 덩어리를, 그 위대한 신성 정통 베이즈 심판 공식 믹서기 판 (4.15) 아가리 몸통 내부 코어 속으로 냅다 뻔뻔하게 욱여 갈아 대입 병합 합체 (plug into) 시켜 장착 연결 도킹 때려 박을 수 있습니다! 그러면 짠! 최종 타점인 우리의 타깃 결판, '사후 족집게 확률 승부수 판정 점수'를 뱉어내는 수식 표현 도면이 아래처럼 깔끔 마개조 조작 조립 환생되어 완성 획득 도출되어 화려 통쾌 탈피 튀어나옵니다!

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k \times f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p)}{\sum_{l=1}^{K} \pi_l \times f_{l1}(x_1) \times f_{l2}(x_2) \times \dots \times f_{lp}(x_p)} \quad (4.30)
$$

for $k = 1, \dots, K$.
(단, 여기서 수식 부품 세팅 $k$ 방 조준 번호는 1번부터 $K$번까지 타깃 악당 진영 전체 부류 싹 다 모조리 다 매칭 빙글빙글 굴려 돌려 뺑뺑 대결 연산 도출 승부 적용된다고 퉁쳐서 확장 해석하심 됩니다.)

To estimate the one-dimensional density function $f_{kj}$ using training data, we have a few options:
이제 통계 전쟁의 룰 승부 세팅은 다 끝났습니다! 우리에게 남은 찌꺼기 거저먹기 최종 미션은 단 하나, 현장 조교 캠프 훈련 데이터 수량 바닥 재료 힌트 인구 자원을 벅벅 긁어 모아다 수집 사용해서, 저 가볍게 조각조각 잘려 쪼개진 앙증맞은 1차원 심플 곡면 개별 단독 밀도 쪼가리 함수 부품들 $f_{kj}$ 장치 나사 파편 뼈대 지형들을 하나하나 뚝딱 세팅 때려잡아 측정 세팅 추정 계산 산출 구축하는 일뿐입니다! 이를 위해 우리 주머니 막고 품 창고 도구함 엔 한 세 가지(few options) 정도의 꽤 짭짤 달달한 도구 요령 산출 세팅 기술 대안 옵션 수단 마법 카드 패들이 예쁘게 널려 비치 장전 세팅 탑재 조준 기다리고 대기 제공되어 있습니다:

- If $X_j$ is quantitative, we can assume it follows a univariate normal distribution, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- 만약 우리 증거 단위 아이템 측정 장치 모델 수사 **변수($X_j$)** 놈의 정체가 (나이, 월급, 체지방 빚 잔고 수치처럼 끊이지 않고 계속 숫자 눈금이 널려 잔뜩 흘러 변하는) 무지막지 수치 미세 계량 표기 수량 연속 눈금 단서 덩어리 모양인 계량 치수, 척도 양적 **수량 연속 변수 부류(quantitative)** 출신이라면!! 우린 그냥 거저먹기 가장 뻔하고 무난 안심 꿀 프리패스 세팅값 전제를 꺼내 강요합니다. "아 너네 숫자 놈들은 복잡하게 생각할 거 없이 그냥 딴 거 없고 지구에서 가장 기본 둥글 룰인 무난한, **단일 1차원 볼록 정규 분포 산등성이 지도 도면 곡선 궤도(univariate normal distribution)** 룰 법칙 모양 규칙 마법 곡선 하나만 아주 얌전히 착하게 알아서 자~알 모셔 딱 들어맞아 따른다고 억지 강제 우겨 퉁 치고 가정해 버리자!" 라고 쿨하게 단정 판단 때려 마법 구속 도장 찍습니다, 즉 우아한 수식 암호론 이 둥근 꼬라지 $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$ 포맷 낙인 룰 시스템 강제 배정 부여로 순응 강제 복종 확정 강제 세팅 부착해 굴려 갈아 마셔버립니다.
- Alternatively, we can use a non-parametric estimate like a histogram or a kernel density estimator.
- 딴지 걸기 아니면 대안적으로(Alternatively)! "위처럼 뻔한 정규 분포 가운 씌우기 독재 도장 룰 강압 따위 구차해서 난 절대 싫고 반골 거부하겠어! 걔들이 꼭 예쁜 곡선이라는 증거가 어딨냐?" 라면, 우린 훨씬 더 유연 말캉하고 프리스타일로 현장 땅 맵핑 지형 바닥에 찰싹 딱 달라붙어 그리는 이른바 뼈대 선입견 족보 없는 무 룰 자유 추정, 즉 **'비모수적 자유 맵핑 측정 추정(non-parametric estimate) 방도'** 프리 장치를 전격 출격 꺼낼 수도 있습니다. 블록 벽돌 쌓듯 뭉쳐 박는 단순 막대그래프 덩어리 **히스토그램(histogram)** 장치나, 둥글게 스무디 곡선 윤곽을 문질러 찰흙처럼 반죽 비벼 지형을 매끄럽게 조작해 바르는 **커널 밀도 도면 추정 장치(kernel density estimator)** 모형처럼 더 유연 탄력 있게 맵을 눈치 파악 현장 즉시 재는 찰흙 비모수적 자유 추정 공법 접근 기법 방식을 사용 차용 밀어붙여 세팅 뚝딱 구동 돌려 현장 도출해 볼 수도 있습니다.
- If $X_j$ is qualitative, we simply count the proportion of training observations corresponding to each class instance.
- 아싸리 마지막 구원 거저먹기! 만약 우리가 다루는 $X_j$ 타깃 단서 특징 아이템 변수 힌트가 숫자 계산 메모 치수가 아니라 단지 편 가르기 부류 속성 라벨 포장 척도, 즉 색깔, 혈액형, 성별 기반의 범주/명목형 이름 딱지 포장 **질적 변수(qualitative)** 부류 판 출신이라면? 에이, 이건 뭐 계산기 켤 것도 없고 골치 아프고 구차하게 고민할 가치 수학 연산조차 필요 불필요 없습니다. 우린 그냥 세상 제일 멍청하고 원시 가장 뻔한 쉽고 직관 극강 심플 간단하게 무식 구식 방법, 원시 유치원 초등학교 산수 곱셈 덧셈 뺄셈 세기(count) 스킬 발동!! 즉 머리 텅 비우고 수식 따위 필요 없이 단순히 각 클래스 방별 타깃 인스턴스(instance) 분류 소속 별도 현황 결과 명목 항목 분류 부류 조건 바구니에 순응 포함 대응(corresponding) 저격 매칭 적중 소속 구속되는, 실제 현장 캠프 훈련 관측치 인원 포로 쪽수 인간 머릿수의 점유 비중 비율(proportion) 총량 % 지표를, 그냥 눈으로 수기 척척척 산수 계산 단위 덧셈 뺄셈 단순 카운트 인간 계산기로 세서 도출 단순 집계해 분수 비율로 뽑아내 통계 단순 산출(count)만 쪽수 계산 세주면 그냥 모든 미션 종료 허탈 만사 오케이 찰떡 땡! 스코어 계산 끝입니다! 

---

## Sub-Chapters

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans1.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans1.html)

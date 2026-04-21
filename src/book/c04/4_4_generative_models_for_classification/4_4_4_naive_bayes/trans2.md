---
layout: default
title: "trans2"
---

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans2.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4.4 Naive Bayes
# 4.4.4 나이브 베이즈 (Naive Bayes): 지나치게 순진무구한 독립 선언의 기적!

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers. Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier.
바로 직전 세션 지옥의 파트에서, 우리는 베이즈의 절대 마법 정리 공식 (4.15)를 뼛속까지 울궈먹어 대쪽 고집 LDA와 유연 뱀 커브 QDA 두 가지 부류의 분류기를 멋지게 개발 구축했습니다. 그리고 지금 여기, 우린 또다시 그 베이즈 정리를 통째로 한 번 더 빌려서 저 유명하고 가장 대중적인 슈퍼스타 **'나이브 베이즈(naive Bayes)'** 분류기의 찬란한 출격 동기를 부여해 볼 참입니다!

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability $p_k(x) = \text{Pr}(Y = k \mid X = x)$ in terms of $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. To use (4.15) in practice, we need estimates for $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$. As we saw in previous sections, estimating the prior probabilities $\pi_k$ is typically straightforward: we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$th class. 
베이즈 정리 (4.15)가 대체 우리에게 어떻게 최종 보스 판결 점수인 사후 확률 $p_k(x) = \text{Pr}(Y = k \mid X = x)$ 점수 덩어리를 만들어 뱉어 주었었는지 되짚어 상기해 보십시오. 무려 지저분한 사전 확률 $\pi_1, \dots, \pi_K$ 파편들과 $f_1(x), \dots, f_K(x)$ 곡선 밀도 함수들을 재료로 버무린 거대한 수식 포장이었죠! 현실 흙탕물 실무에서 그 무적 베이즈 계산표 (4.15)를 실제로 가동해 써먹기 위해서는, 우린 기를 쓰고서라도 $\pi_1, \dots, \pi_K$ 스펙과 저 난해한 밀도 척도 $f_1(x), \dots, f_K(x)$ 파편들의 대략적인 '추정 가짜 값(estimates)' 이라도 어떻게든 긁어모아야만 했습니다. 감사하게도 이전 단원에서 두 눈 시퍼렇게 보았듯, 사전 지분 확률인 $\pi_k$ 찌라시들을 추정하는 짓거리는 보통 거저먹기로 심플(straightforward)했습니다: 그냥 노예 훈련 데이터 더미 속에서 그 $k$번째 방에 속한 놈들의 머릿수 비율(쪽수 비율)을 세어서 때려 박으면 $\hat{\pi}_k$ 껍데기는 완성됐었으니까요!

However, estimating $f_1(x), \dots, f_K(x)$ is more subtle. Recall that $f_k(x)$ is the $p$-dimensional density function for an observation in the $k$th class. In general, estimating a $p$-dimensional density function is challenging. In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and shared covariance matrix $\mathbf{\Sigma}$. By contrast, in QDA, we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and class-specific covariance matrix $\mathbf{\Sigma}_k$. By making these very strong assumptions, we are able to replace the very challenging problem of estimating $K \times p$-dimensional density functions with the much simpler problem of estimating means and covariance matrices.
하지만 문제는 저 빌어먹을 **밀도 확률 함수 $f_1(x), \dots, f_K(x)$** 녀석들을 털어내 진짜 추정하는 건 사람 진 빠지게 훨씬 골치 아프고 미묘한 과제입니다. 망할 $f_k(x)$ 곡선 덩어리란 게 무려 $k$번째 클래스 진영 방 안에서 혼자 덩그러니 놓인 관측치 놈의 $p$-다차원 입체 밀도 함수 덩어리입니다. 솔직히 말해 일반 스펙상 저 $p$-다차원 3D 곡렬 밀도 공간 자체를 생으로 빙빙 돌려 수학적으로 파헤쳐 추정한다는 것 자체가 뼈 아프게 사람 한계를 부수는 미친 삽질(challenging)입니다. 그래서 그 끔찍한 LDA 시절에 우린 어떡했습니까? 그 미친 연산 재앙 노가다를 확 줄이려고 눈 딱 감고 완전 억압적이고 무지막지한 강제 세뇌 가정을 박았죠: "이 $f_k$ 곡선통은 $k$ 클래스 전용의 평균 벡터 $\mu_k$ 하나랑 나머지 분산 체형은 모든 그룹이 다 공짜로 공동 분배해 획일 공유하는 단일 분산 행렬 $\mathbf{\Sigma}$ 로 대충 퉁친 정규 분포 변수야!" 하고 뻔뻔하게 우겼습니다. 반면 대척점의 QDA 에서는 또 어떡했습니까? "아니지 $f_k$ 곡선 체형에는 지들 방 전용 $\mu_k$ 평균과 지들만 이기적으로 써먹는 독자 맞춤 분산 행렬 공장장 $\mathbf{\Sigma}_k$ 가 각각 독립 세팅 되어 있는 거야!" 라고 우겨 가정했었죠. 우린 결국 이렇게 억지스럽고 욱여 넣어진 강력 망상 가정을 박아버린 덕택에, 불가능에 가깝던 '오리지널 날것 $K \times p$-차원 밀도 함수를 쌩으로 추정해야 할' 재앙 같은 노가다를 그냥 단출히 평균 벡터 $\mu$ 점 몇 개 줍고 공분산 뱃살 통짜 행렬판 몇 개 짜깁기하는 수준의 유치원 장난 같은 아주아주 가벼운 단순 수학 뺄셈 덧셈 문제로 둔갑시켜 모면(replace) 할 수 있었던 것입니다!

The naive Bayes classifier takes a different tack for estimating $f_1(x), \dots, f_K(x)$. Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single, sweeping assumption:
그런데 드디어 출격한 저격수 **나이브 베이즈 분류기(Naive Bayes Classifier)** 호위함은 저 난해한 $f_1(x), \dots, f_K(x)$ 모델 추정을 털어내 해결하고자 이전 녀석들과 아예 본질 루트 결이 통째로 완전히 핵 돌아버린 기상천외한 새로운 항로(tack)로 키를 꺾어 버립니다! 얘가 무슨 고상한 정규 가우시안 출생 혈통이니 정규 확률 파벌(distribution family) 계급 따위에 속박 소속되어 태어났다는 등 기존의 지루한 억지 망상 가정 따위를 죄다 불태워 다 쓰레기통에 처박는 대신, 이 녀석은 그 즉시 모든 걸 그냥 모조리 한 방에 쓸어 담아 압살시키는 무적 권능의 **'단 한 번의 단일 폭격 가정(single, sweeping assumption)'** 하나만을 뻔뻔하게 냅다 시전해 버립니다:

**Within the $k$th class, the $p$ predictors are independent.**
**"특정 $k$번째 고유 방구석(클래스) 안에서만 놀 때, 수십 개의 $p$ 힌트 스펙 변수 벡터 놈들은 완전히 철저히 절대 서로 아무 상관 없이 무관한 투명 인간 남남인 완벽 독립(Independent) 상태다!"**

Stated mathematically, this assumption means that for $k = 1, \dots, K$,
저 오만하고도 막강한 무대뽀 선언을 무자비한 수학 수식의 관점 언어로 탈탈 풀어 까발려 돌려치면, 모든 $1$ 부터 $K$ 방 구석 구석에 대하여 다음과 같은 기적의 충격 수치식이 단박 성립한다는 기가 막힌 의미가 터져 나옵니다:

$$
f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p) \quad (4.29)
$$

where $f_{kj}$ is the one-dimensional density function of the $j$th predictor among observations in the $k$th class.
여기서 산산조각난 찌끄레기 파편인 $f_{kj}$ 는 오직 해당 $k$번째 클래스 방안 갇혀 배회하는 관측 병사들 중 딱 하나 단일 $j$번째 힌트 변수 지 혼자만의 쓸쓸한 막대 1차원짜리 단순 밀도 곡선 꼬라지에 불과합니다. (한 마디로 저 공식은 원래 거대하고 복잡하게 꼬였어야 할 다차원 $f_k(x)$ 밀도 합체 로봇 덩어리를, 그냥 개별 단일 요소 각각의 단순 무식 초딩 '연속 단순 **곱셈($\times$)** 나열식' 으로 완전체 산산조각 분쇄 폭발 시켜 버린 대업적입니다!)

Why is this assumption so powerful? Essentially, estimating a $p$-dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors. In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix. However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate. But by assuming that the $p$ covariates are independent within each class, we completely eliminate the need to worry about the association between the $p$ predictors, because we have simply assumed that there is _no_ association between the predictors!
대체 이딴 저능하고 유치해 보이기 짝이 없는 단순 멍청한 가정이 도대체 왜 그렇게 전능에 가깝도록 무식하게 파괴적이고 위력이 넘치는 힘의 권능 통계를 자랑하는 걸까요? 본질을 따져 묻자면, 원래 애초 그 망할 $p$-다차원의 밀도 분포 덩어리를 추정해 산출하는 게 그렇게 재앙스럽고 악랄했던 이유는: 우리가 각 변수 한 놈 한 놈 혼자만의 쌩쑈 분포 발광 곡선인 **한계 주변 분포(Marginal Distribution)** 만을 요리조리 편하게 따지면서 고려 끝날 일이 절대로 아니라, 나아가 수십 개의 서로 다른 예측 변수 놈들이 뒤섞이고 막 거미줄처럼 막 얽혀 치고받는 삼각 교차 관계도 타격인 그 미쳐버린 **결합 혼돈 분포(Joint Distribution)** 의 사슬 연관 지뢰밭 기저까지 싹 다 동시 통찰 모조리 다 고려해야만 비로소 제대로 된 곡선 판이 스케치 되기 때문입니다! 예컨대 방금 그 잘난 다변량 정규 가우시안 방정식 세계 모델 판만 보더라도, 그 수십 개 징그러운 변수 파라미터 간의 얽힌 밀접 줄다리기 연관성을 표현한답시고 무식한 공분산 행렬판을 만들어 놓고, 대각선 밖의 잡동사니 떨거지 조각 파편(off-diagonal elements) 수천 개를 눈 빠지게 다 요약 계산해 버무려야 했습니다. 하지만 절망스런 일반 야생 현실 바닥 통계에서는 이러한 수없이 복잡한 그놈들 간의 지저분 이면 사슬 융합 연관성(Association)을 아름답고 확실하게 규정 분석 성격화(characterize) 해 추정해 낸다는 것은 뼈와 살이 터지는 극악의 초 난이도 재앙 미션입니다. **허나 우리가 눈 꽉 감고 무식하게 "에라이, 각 귀속 집단 방 안의 모든 $p$개의 수십 개 공변량 힌트 정보들은 죄다 철저히 혼자 남남이고 완벽 무구 서로 동떨어진 독립(Independent)이다!" 라고 뻔뻔하게 개구라를 쳐 선언해버리는 순간, 우리는 수백 개 예측 스펙 놈들 사이 얽혀 뒹구는 복잡 교란 연관성 사슬 따위에 대해 끙끙 고민해야 할 그 모든 망할 수요와 걱정 일말 자체를 완전 무결 공기 중으로 싹 다 분해 소멸 축출해버리는 기적에 도달합니다!** 대체 이유가 뭐냐고요? 애당초 시작점 단추부터 천재적이게도 "응? 저 변수놈들 스펙 사이 교차 연관성 사슬 끈 같은 교집합 짬짜미 커넥션 따윈 우주 어딜 뒤져도 전혀 단 1도 존재하지조차 않아!" 라고 오만방자 대놓고 거만히 맹세 가정 박아버린 것이니까요! 완전히 무적!

Do we really believe the naive Bayes assumption that the $p$ covariates are independent within each class? In most settings, we do not. But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where $n$ is not large enough relative to $p$ for us to effectively estimate the joint distribution of the predictors within each class. In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings. Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.
그렇다면 솔직히 우린 심장 가슴에 손을 얹고 정말 저 모든 $p$ 예측 힌트 호위 군단들이 완벽히 단 1의 연관성도 없는 독자 노선 솔로라는 저 **나이브(너무 순진무구하게 멍청한, Naive)** 베이즈 망상 선언 가정을 진짜배기 진리라고 철석 믿는 겁니까? 솔직히 까놓고 대부분의 실전 환경 무대판에서 우린 당연히 그딴 거 개뿔 단 1도 안 믿습니다. 그러나 묘한 반전!, 비록 이 무대뽀 모델링 망상 세팅 가정이 그저 살인적 폭탄 연산을 덜어 밥 먹듯 쳐내기 위한 편의성(convenience) 하나만을 쫓아 날조 발동된 완전 억지 꼼수일지라도, 신기하게도 이 녀석은 종종 실전에서 아주 입이 떡 벌어질 정도로 무진장 무난하고 꽤 탁월 구가하는 준수한(pretty decent) 예측 홈런 결과물들을 빈번히 뿜어 토해냅니다! 특히 이 힘은, 가진 훈련 오리지널 데이터 머리통 쪽수 체력 스택 $n$ 양이 수십 개의 다차원 정보 덩치 방어 스펙 $p$ 수량에 비교조차 안 될 정도로 심히 빈약 쪽박 찌질 해서 서로 간의 교차 얽힘 교집합 융합 그 결합 교차 분포(Joint distribution) 지뢰밭 함수 망을 일일이 파고들어 유효하게 제대로 뚝딱 추정해 낼 여력 역량조차 전무한 파산 직전 최악의 난이도 열악 환경판일수록 미친듯 그 극한 방어의 기세가 치솟아 쾌거 위력을 작렬시킵니다! 솔직한 통계 실상 까발려 보면 애당초 거대 결합 분포 사슬을 스케치한다는 것 자체가 원체 은하수 개수만큼의 폭압적 막대한 우주 빅뱅 데이터 물량을 구걸 필요로 하는 토악질 나오는 대 괴무 노역이므로, 역방향 반대로 도는 이 속 편한 꼼수 스킬 나이브 베이즈가 수만 가지 광범위 다차원 변태 무대판 통 세팅들에 포용 널리 사랑받는 완전 범용 무적 조커 초이스 군림 아이템이 된 겁니다. 다 빼고 핵심 본질의 엔진만 뼛속 원리로 관통해 요약하자면: 이 나이브베이즈(순진무구 독립 맹신) 꼼수 몽상 가정은 본질이 애당초 사실 구라 선언이므로 태생적 어리석음인 오답 편견 쓰레기값 잔량 오차 **편향(Bias)** 오목을 필연 어쩔 수 없이 한 뭉텅이로 들이붓게 초래하지만 반대급부 무한 혜택으로 모델의 우왕좌왕하는 널뛰기 미친 춤 파동 신경질 진동 에러 폭 발작인 **분산(Variance)** 오류의 모가지 멱살을 잔인하게 틀어쥐고 아주 훌륭 진압 파괴 감소 하락 소멸(reduces variance)을 시켜버리는 대등가 방어막 반전 교환 효과를 선물 산출합니다. 그 기적 덕분에 결국 우리가 신봉하던 그 유명한 만세 진리 명제인 바로 그 '편향-분산 밀당 상쇄 (Bias-variance trade-off)' 절충안의 달성 결실 파도 위를 유유자적 매끄럽게 타 넘으면서, 실제 최전선 실무 필드에서 오류 하나 삐걱 없이 몹시 겁나 훌륭하고 기똥차게 팍팍 우등생처럼 작동 구동하는 찰진 환상의 막강 분류기가 최종 태초 연성되어 수립 도출 장착되는 것입니다!

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability,
이제 우리가 위에서 그 미치고 전율 돋는 "나이브 베이즈 나 홀로 완벽 독립 선언 무뇌 망상 가정"에 감히 쾅! 도장을 확 결단 찍고 맹신 채택한 절대 도가 이상, 우린 그 조각나 산산히 해부 인수분해 부품 나뒹굴린 기분 좋은 허무 단순 맹세 장식 공식 (4.29) 곱셈 나열 무더기 꼬라지 파편들을 아주 건방지게 그 영광스런 만왕 무결 최강 제왕 법전인 베이즈 대방정식 메인 센터 무대식 (4.15) 본체 꼭대기 분모 분자 위로 미친 듯 마구잡이로 대입 쑤셔 대 타격 박아 넣는 행위를 적법 수행하여, 단 1방의 일격으로 화려하고 심플 초등 대수 곱셈 결로 부숴 개편된 새로운 최후의 신성 사후 마감 확률 판결 무결 수리 방정식 덩어리의 지휘권 탈환을 무결 획득 도출 산출해 거저먹는 쾌감을 이룩 획득 기 합 달성 타진 하게 됩니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k \times f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p)}{\sum_{l=1}^{K} \pi_l \times f_{l1}(x_1) \times f_{l2}(x_2) \times \dots \times f_{lp}(x_p)} \quad (4.30)
$$

for $k = 1, \dots, K$.
($k=1$ 승자 1번 방 진영 무리부터 저 끝 꼬리 $K$ 번째 모든 투기 조각 방들의 경우들 싹 모두 모두 전 부 다 에 일괄 배당 적용 말입니다.)

To estimate the one-dimensional density function $f_{kj}$ using training data, we have a few options:
자 이제 마지막 땜빵 노가다 공구 작업만 남았습니다. 저 징그러운 곱셈기 바구니 사이에 콕콕 빈칸 삽입 들어갈 조촐한 막대 1차원짜리 파편 스탯 밀도 함수 파편인 $f_{kj}$ 한 놈 한 놈 조각 자체를 과연 우리가 손에 쥔 거지 같은 실제 막장 훈련 노예 데이터 찌끄레기 더미 바닥 속에서 어찌 꼼수 털어 모아 계산 야매 분수 추정해 채워 메꿀 것인가 단안 가닥에 대한, 고만고만한 단골 전술 해결 방법 몇 가지 편법 꼼수 옵션 선택지 칼 다발을 우리는 보통 주머니에 들고 만지작거립니다:
- If $X_j$ is quantitative, we can assume it follows a univariate normal distribution, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- 만약 저 조각 $j$ 번째 속성 뼈대 힌트 놈 정보 $X$ 스펙이 사람 몸무게나 연봉 단위 통장 잔고처럼 이리저리 숫자로 양 따위 재어 조물거리는 연속 척도 **양적 수치(quantitative)** 체격 통 특성 피쳐 정보라면, 묻지도 따지지도 않고 "이 놈 하나 역시 그냥 혼자 외롭게 우산 종 치는 단일 조각 스펙 정규 가우시안 둥근 우산 종 모양(univariate normal) 분포 곡선을 그냥 예속 뒤집어 쓴다!" 라고 심플 발칙 퉁 쳐서 후려 갈겨 가정 버무려 버릴 수 있습니다 $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$. 
- Alternatively, we can use a non-parametric estimate like a histogram or a kernel density estimator.
- 굳이 종 모양 대칭 곡선 가정 우기기 옹고집 통 강압이 짜증 나 박살 내기 싫다면 대안적인 편법 우회 루트(Alternatively) 로, 골치 아픈 뇌피셜 수식 계산 가정 따위 당장 접어 치우고 그냥 있는 눈앞 데이터 더미 파편 그대로 찍어 점유율 면적으로 밀어 올리는 무식 비모수 꼼수 모델인 직관 투사 **히스토그램 막대 벽돌 그림 통계 그림(histogram)** 넓이 쪼가리 분포 윤곽이나, 그걸 좀 더 맨들 하게 사포질 처 발라 둥글게 매끈 스케치 도면 그림자 곡선 모형을 빚어낸 **커널 밀도 부단 추정기 파 진 기법 도면 툴(Kernel density estimator)** 따위의 통계 투사 기술 툴력 마법 스케치를 써먹어 단단 땜바꾸를 쳐 메꿔버려 대치 투영 치부 해 버려도 무지막지 막 훌륭 다 좋고 만족 편 결 찰진 타격 가능 무막 옵션 치 무 가동 조 전 결단이 편 조 됩니다! 수 무 부단.
- If $X_j$ is qualitative, we simply count the proportion of training observations corresponding to each class instance.
- 만일 망할 예측 속성 힌트 정보 $X_j$ 이 녀석이 그딴 골치 썩는 연속 수식 연산 척도 숫자가 아니라! 단순히 피 혈액형(O형 A형) 이라든지 국적 성별 이름 딱지 무리 같은 단어 문자 따위 명칭으로 분별 분할 타갈 나눠진 오직 단원 질적 문자 통 도장성 **범주 지표 타입(qualitative)** 투항이라면! 아무런 수학 미적 연산 계산 따위 방정식 수리 고민할 머리가 단 한 개도 아예 애초 도 무 전무 무 결 1 도 조 차 필요 없이 무 식 심 플 막 무 지하게 존나 초간단(simply count) 그냥 닥치고 손가락 셈으로, 저 긁어모은 총 노예 훈련 군단 모집단 타깃 머릿수 쪽수 무리 방 그룹 안 사람 구석 진영 통 분자들 중에서 딱 해당 그 문자 카테고리 기표 자격 도장 인스턴스를 해당 훈련 집단의 표본 개수를 그대로 헤아려 비율로 대체해 입력해버리면 만사형통으로 그 자리의 모형 추정이 종결됩니다!

---

## Sub-Chapters

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans2.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans2.html)

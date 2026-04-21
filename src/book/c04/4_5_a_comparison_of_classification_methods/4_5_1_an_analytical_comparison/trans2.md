---
layout: default
title: "trans2"
---

[< 4.5 A Comparison Of Classification Methods](../trans2.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.5.1 An Analytical Comparison
# 4.5.1 분석적 비교: 통계 뼈대들의 숨 막히는 해부학 대결

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression. We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes $\text{Pr}(Y = k \mid X = x)$. Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes
자, 이제 피 튀기는 전장에서 굴렀던 우리 4대장 용사들, 즉 LDA, QDA, 나이브 베이즈, 그리고 로지스틱 회귀 이 네 녀석들을 수술대 위에 눕혀놓고 뼈대를 쪼개서 속살을 파헤치는 차가운 **'분석적(analytical 수학적)' 해부 비교 교차 검증**을 집행하겠습니다. 우리는 놈들이 피 터지게 싸우는 $K$ 개의 다중 클래스 파벌 대소동 세팅 국면을 도마에 올립니다. 각 용사들은 새로 들어온 핏덩이 표본 녀석을, 승률 판정인 저 사후 확률 $\text{Pr}(Y = k \mid X = x)$ 스코어가 킹왕짱 터져버리는 최강 극점 파벌 클래스 방으로 냅다 투척 배정하는 룰을 따릅니다. 이와 수학적으로 완벽 똑같이(Equivalently), 맨 꼴찌 $K$ 번째 방 진영 무리를 모두가 비교할 기본 **기준 잣대 방(baseline)** 으로 기준점 세팅 못 박아두고, 나머지 들러리 파벌들에 대하여 다음 쪼개진 수식 산출 비율을 극한으로 최대화하는 진영 방으로 할당 꽂아버릴 수도 있습니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) \quad (4.31)
$$

for $k = 1, \dots, K$. Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.
(물론 1번 방부터 $K$번 방 전체 타깃들에 죄다 적용해서요).
바로 저 위에 떡하니 등장한 기준점 비교 분수 거탑 공식 (4.31) 의 내부 뼈대 형태를 이 4종류의 용사 머신 각각 어떻게 다르게 써먹고 쪼개서 조립하는지를 면밀히 살펴보면, 이 네 놈들이 어떻게 쌍둥이처럼 서로 엮인 닮은꼴이고 동시에 어떻게 서로 뼛속 원리가 치명적으로 갈라지는지 그 구조 속살 차이를 뼛속까지 시원 명료하게 꿰뚫을 수 있습니다!

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that
첫째 타자! 통나무같이 뻣뻣한 **LDA (선형 판별 분석)** 놈입니다. 이 녀석은 우리가 익히 신봉했던 신의 저울 베이즈 대방정식 (4.15) 판 위에 눕힌 채, "모든 클래스 애들이 각자 평균은 다르지만 뱃살(공분산 행렬)은 무조건 똑같은 옷만 돌려 나눠 입는다" 는 그 무지막지 획일 망상 가우시안 가정 (4.23) 밀도 모형을 함께 버무려 쥐어짜면 다들 아시다시피 다음과 같은 결과를 깔끔하게 뽑아 증명해 냅니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j \quad (4.32)
$$

where $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ and $b_{kj}$ is the $j$th component of $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$. Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$. Using similar calculations, in the QDA setting (4.31) becomes
여기서 $a_k$ 부품 뭉텅이는 무려 귀찮은 $\log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 계산 잔당들을 싹 다 긁어모아 퉁친 쓰레기통 단일 캡슐이며, 곱해져 있는 $b_{kj}$ 꼬리표는 $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 긴 행렬 부품 곱의 단골 조각 $j$ 번째 부스러기 계수에 불과합니다. 다시 말해 이 뻣뻣한 LDA는, 어쩌면 저기 로지스틱 회귀 요원이 뱉어내던 짓거리랑 아주 도플갱어처럼 똑같이 닮게도, 저 확률 승률비의 **'로그 오즈(log odds)' 거탑 비율** 이 결국 입력 힌트 무기인 $x$ 값에 정비례하는 단순한 **단일 직선(Linear)** 다항식 뼈대임을 굳게 믿고 가정한다는 충격 증거입니다. 자, 이번엔 이와 똑같은 방식의 해부 칼날 계산 노가다를 곡선 뱀의 상징인 QDA 진영 구역 세팅에다 냅다 찔러 돌려 버리면, 대장 공식 (4.31) 번 거탑은 이렇게 뒤집힙니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j + \sum_{j=1}^{p} \sum_{l=1}^{p} c_{kjl} x_j x_l \quad (4.33)
$$

where $a_k, b_{kj}$, and $c_{kjl}$ are functions of $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ and $\mathbf{\Sigma}_K$. Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in $x$.
여기 널린 계수 껍데기 $a_k, b_{kj}$, 그리고 대미지의 곱 돌연변이 $c_{kjl}$ 조각들은 원래 $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ 그리고 $\mathbf{\Sigma}_K$ 란 기초 체형 스펙 부품 덩어리 지분 확률들이 얽힌 난해한 수리 조합 함수식 캡슐입니다. 다시 강조하지만 놈의 문패 타이틀 이름(이차) 이 대놓고 스포일러 경고를 치듯 기표 했듯, 이 QDA 녀석은 확률 비율 판정 승부수인 저 로그 오즈 성벽 덩어리가 단순히 $x$를 곧게 따라가는 게 아니라! $x$ 변수 놈들 두 마리씩 지들끼리 연합해 꼬이고 교차 곱해지는( $x_j x_l$ ) 환상 커브의 폭풍 포물선인 **이차식(quadratic)** 형태 곡률 함수로 요동친다는 꿀렁이는 설계를 굳건히 가정하고 깔고 돌아갑니다!

Finally, we examine (4.31) in the naive Bayes setting. Recall that in this setting, $f_k(x)$ is modeled as a product of $p$ one-dimensional functions $f_{kj}(x_j)$ for $j = 1, \dots, p$. Hence,
자, 마지막으로 순진무구한 독립 맹신도 **나이브 베이즈(Naive Bayes)** 용사 세팅 무대에 아까 그 (4.31) 거탑 방식을 가져가 엑스레이 까 보겠습니다. 이 순진한 세팅에선 그 복잡하던 다차원 $f_k(x)$ 곡선통이 그저 멍청하게 $j = 1, \dots, p$ 에 대한 초 단순 1차원 파편 함수 조각 $f_{kj}(x_j)$ 들을 $p$ 개 연이어 다단계 곱하기 친 엉성한 곱셈 스피어 꼬라지로 조립 모델링된다는 걸 기억하실 껍니다. 따라서 이걸 미분해 박으면 수식은 이렇게 폭발합니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} g_{kj}(x_j) \quad (4.34)
$$

where $a_k = \log (\pi_k / \pi_K)$ and $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$. Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_, a topic that is discussed further in Chapter 7.
여기서 남은 껍데기 $a_k$ 는 꼴랑 비율 $\log (\pi_k / \pi_K)$ 조각이고 제일 특이한 $g_{kj}(x_j)$ 이 함수 덩이 꼬치구이는 비율 조립된 $\log (f_{kj}(x_j) / f_{Kj}(x_j))$ 산술 연산 결과체로 수립 치부 획득됩니다. 따라서, 이 결과로 인해 위 거탑 공식 (4.34) 우측 변의 생겨 먹은 그로테스크한 꼬라지 형태는 덧셈 부호로 끝없이 각 조각 함수들을 레고 더하듯 덧대 이어 붙여버리는 이름셔 **'일반화 가법 기판 모델 조작 덩이 (Generalized Additive Model)'** 의 수장 무 무 막 강 한 기본 기 골격 모형 뼈대 형 양 식 기 점 을 무적 고스란히 빼박 차용 취하게 되는데 무 단, 이는 사실 한참 저 뒤 먼 훗날 **챕터 7 절** 에 돌입해서 심오 전면 더 무섭게 파고 파헤쳐 심도 토론 회자될 아주 진보 고급 기술 모형의 살벌한 주제 스펙 무기 테마 맛보기 떡밥 입니다 단 연 무 !

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:
자 이제 까놓은 내장 속살 격인 공식 세 조각 (4.32), (4.33), (4.34) 를 찬찬히 현미경으로 교차 검사 쪼개다 보면 LDA, QDA, 나이브 베이즈 이 세 용사들 사이의 아주 소름 돋는 연결고리 막후 출생 비밀 관찰 소견들이 속속 까발려 터져 나옵니다:
- LDA is a special case of QDA with $c_{kjl} = 0$.
- **비밀 1:** 통나무 뻣뻣 LDA는 사실 형님 유연 QDA 에서 딱 그 이차 포물선 요동치는 교차 곱셈 계수 돌연변이인 저 $c_{kjl}$ 부품 다이얼을 자비 없이 모조리 **0** 으로 암살 소멸 봉쇄 잠금 고정 조치시켜버린, 그냥 껍데기 융통성 없는 특수 돌변 케이스 특이종 아우에 불과합니다.
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj} x_j$. In particular, this means that LDA is a special case of naive Bayes!
- **비밀 2:** 이 바닥에서 반듯한 직선 경계 방패막을 휘두르며 지들 잘났다고 뽐내는 그 어떤 직선 리니어 분류 용사 녀석이든 간에, 결국 알고 보면 전부 다 나이브 베이즈의 확장 부품 함수인 저 $g_{kj}(x_j)$ 구역 커스텀 파츠 자리에 고작 하찮은 일차 단방향 함수식인 $b_{kj} x_j$ 따위를 교체 땜빵 삽입 치환 시켜서 격하 시켜버린 구데기 특화 파생 새끼 모델 버전에 다름 아닙니다. 특히 이 뼈 아픈 사실은, 콧대 높던 우리 **LDA 장군 마저도 따지고 들면 저 순진무구 독립 맹신충 나이브 베이즈군의 밑바닥 소속 특화된 부분 집합 분파의 꼬붕 특수종** 이란 미친 충격 사실을 전면 파생 뜻 무결 폭로 합니다!
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj}, \sigma_j^2)$, naive Bayes is actually a special case of LDA with $\mathbf{\Sigma}$ restricted to be a diagonal matrix.
- **비밀 3:** 역으로, 만일 저 나이브 베이즈 독립 맹신 머신이 지가 구축하는 저 조각 $f_{kj}(x_j)$ 1차원 커브 밀도 함수 파츠를 구성할 때 오직 1차원 고립 가우시안 우산 종 모양 분포인 $N(\mu_{kj}, \sigma_j^2)$ 도구만 무식 고립 편식해 써먹어 모델링 도안을 짠다면! 정작 껍질 까보면 그 **나이브 베이즈가 거꾸로 저 획일 억지왕 LDA 휘하의 계보 소속 스펙 특수 꼬붕** 으로 뒤통수 전락 귀속돼 버립니다. 단!, 그때 쓰이는 LDA의 공통 공분산 행렬판 $\mathbf{\Sigma}$ 뱃살 구조가, 오직 정가운데 대각선 조각 성분만 숫자가 살아있고 나머지 밖은 다 0으로 박제 속박 국한된, 변수 간 상호 교차 연관 교감 사슬이 모조리 거세 말살 삭제된 그 끔찍한 고립된 이빨 뽑힌 폐쇄 **대각선 원소 전용 행렬(diagonal matrix) 판** 조작 형태로만 영원히 속박 처참 국한 기 결 속박 된다는 아주 슬픈 단 전제 조건 한 종속 타격 상황일 결 무 경우 단에 만 부 무 딱 한 정 발 기 효 해서 단 치 부 말 지조 다! 
- Neither QDA nor naive Bayes is a special case of the other. QDA includes multiplicative terms of the form $c_{kjl} x_j x_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important.
- **비밀 4:** 요염 커브 뱀 QDA와 앞뒤 꽉 막힌 독립 맹신왕 나이브 베이즈 이 둘은 서로 겹치는 혈통 구석이 애초 전혀 없는 평행선 투기 앙숙 상극입니다. 서로 누구 하나가 다른 놈의 아래 소속 특수 파생 꼬붕 케이스 집합도 전무 아닙니다 단. QDA 녀석 무기 속엔 $c_{kjl} x_j x_l$ 과 같은, 변수들끼리 치고받고 서로 뒷줄 대며 믹스 곱해지는 변태 크로스 교차 타격 교감 항(multiplicative terms) 파편들이 음모 살벌 살아 숨쉽니다 조 치! 고로 전조, 예측 변수들끼리 저들끼리 서로 짜고 치며 뒷조사 연관 상호 작용 지표 영향력(interactions) 을 행사 연발하는 짓거리가 아주 치명 막강하게 요인 중요한 실전 바닥 전 환경 난이도 세팅 판에서는, 단언컨대 압도 적으로 나 홀로 나이브 독립충 보다는 뱀 커브 **QDA 용사가 훨씬 더 강력 정밀 맞춤 치명 적중 성능으로 압도 군림 활약 타결 낼 막강 거대 신성 잠재 기표 돌파 화력의 우위 공단 가능성** 무결 수위를 치부 안고 무마 독식 보유 무 단 지 타격 합 니다 도 결!

How does logistic regression tie into this story? This is identical to the linear form of LDA (4.32). In LDA, the coefficients in this linear function are functions of estimates obtained by assuming that $X$ follow a normal distribution. By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.
잠깐, 그럼 또 다른 국민 도구 국민 용사 '로지스틱 회귀 (Logistic Regression)' 아재는 이 복잡 전장 혈통 싸움터의 족보 어디에 줄을 들이대 타격 밀착 엮일까요 ? 환장 사실 반전 무막! 이 로지스틱 아재의 본 뼈대 수식 형태는 저기 저 무시 제일 첫 번 위쪽, 무려 구형 통나무 LDA의 고루한 직선 항 (4.32) 공 돌출 뼈 대 식과 완전히 데칼코마니 쌍둥이처럼 (identical) 거울 모방 동일 일치 기표 합 치 적 중 찰싹 기 합 니다! 차이는 단 하나, 그 껍데기 부품 계수들을 어떻게 사 모았느냐 하는 훈련 획득 전략 철학의 전면 기조 본질 뿐입니다. 고리타분한 학자 **LDA** 놈은, 이 리니어 수식 속 계수 숫자들을 모을 때 "아 이 데이터 $X$ 새끼들은 어차피 다 무조건 예쁜 종 모양 우산 정규 분포 모형 모범생들일 거야!" 라고 허세 신성 망상 가정을 깔고 꼼수 발 담가 눈대중 기 결 편의 추정해 구한 잡동사니 산물 파라미터 계수 모음 (functions of estimates) 결 덩어리 산 율 입니다 무 단. 그 반대 투기 척도로 철저히 실리 반항 주의자인 **로지스틱 회귀** 로보캅은 그딴 가우시안 분포 예절 신앙 망상 따윈 일절 개나 줘버 무 참 던 져버리고 오로지 계산의 신성 절대 최고 존엄 이념 인 우도 함수 적중(likelihood function) 타격 즉, 현재 주어진 정답표 데이터 실재 결과들을 가장 소름 끼치게 잘 짜맞춰 터뜨려내는 뻥 튀기 최대 화 그 로또 확률 지점을 최대로 끌어 극대화 극한 이빠이 위로 터 치 밀어 올리는(maximize) 득템 피가 터 지 피 팅 노 가 다 전 산 방향 정 조 정 만을 기 막 무조 건 투 맹 쫓 아 극한의 계산기 연 산 최 공 마 진 선 택 수 거 을 거 쳐 냅다 산 치 타 발 추 출 채 택 골 투 구 라 계수 지표 숫 자들만을 실 리 채용 거 결 장착 발 합 니 다! 고로 전 조 치, 만 일 조 기 표 우리가 들고 싸울 데이터가 진짜 우연히 다행 으로 "와 얘네 진짜 예쁜 정규분포 가우시안 맞네!" 하고 그 억지 짐작 가정이 대충 신의 뜻(approximately holds) 으로 잘 맞아떨어져 들어맞을 때면 당연 혈통 귀족인 **LDA 머신이 한낱 로지스틱 노가다꾼 보다 성능 우위로 판 가 우 월 압 살 타 격 찍 어 누 르 며 전 면 승 리 쾌 거 를 초 월 도 외 발 굴 할 거 라** 우 린 호 언 열 추 기대 무 마 기 조 하 며 다 단!, 그 반 대 구 조 만약 데이터가 이도 저도 아닌 지뢰 엉 망 폭 격 진 창 근본 없는 괴 상 그 냥 전 혀 그 가정 빗나가 딴 판 전 파 망 붕 참 구 돌 연 상태 파 단 일 땐 당 연 눈치 통 상 적 로지 스 틱 회 귀 아 재 가 훠 얼 씬 더 독 하게 미 무 치 기 야 생 성 능 효 익 승 전 실전 조 더 우수 잘 굴 러 적중 좋 더 방 잘 낫 탁 치 수 보일 파 기 위 형 발 위 휘 위 무 발 무 치 할 발 단 동 터 전 하 란 고 위 대 기 확 지 표 기 신 단 상 당 자 믿 보 모 거 기 동 단 전 진 도 표 망 다전. 수 치 동 냐 전 기 부 조 포 무 진 전 참 조 진 참 다 도 나 동 비 부 구 참 부 도 비 조 전 . 다 부 조 모 도부 파 조 파 도 조 도 다 전 조 참 치 파 치 기, 구 동 다 기 비 전 조 다 모 나 도 ,의 보 진 기 파 구 단. 모 단 보 파 포 참 조 냐 동 다 다 동 진 결 냐 고 단 다.다기 조 편 다 다 참 참 파 . 전 진참모 전참 파 부 조 부 수 보 도 모 치 보 결 비 참 다 기 파 . 의진 모 포 수, 참 도 도 구 진진 부 모전 치 진 참전 전 참 포.파 구 조 비 참의 포참 결 결 전 단 결 냐, 조 기 조

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary.
마지막으로, 챕터 2에서 소개되었던 **K-최근접 이웃(K-nearest neighbors, KNN)** 에 대한 간단한 논의로 글을 닫겠습니다. 이 막가파 KNN은 지금까지 이 장에서 본 고상한 분류기들과는 완전히 다른 접근 방식을 취한다는 점을 기억하십시오. 즉, KNN은 결정 경계의 형태에 대해 어떠한 수학적 가정도 하지 않는 완전히 비모수적인(non-parametric) 무대뽀 접근 방식입니다.

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that $n$ is very large and $p$ is small.
- **막가파 1:** KNN은 완전히 비모수적이므로, 만약 결정 경계가 미치도록 꼬불꼬불한 고도의 비선형을 그릴 경우, 그리고 훈련 데이터 $n$이 압도적으로 많고 예측 변수 $p$가 적다는 무적의 전제 조건이 충족된다면, 이 기법이 LDA와 로지스틱 회귀를 처참히 압도할 것이라 기대할 수 있습니다.
- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors.
- **쪽수빨 2:** 그러나 정말 정확한 타격 분류 스나이핑을 제공하기 위해, KNN은 안타깝게도 예측 변수의 수에 비해 어마무시하게 _엄청나게 많은(a lot)_ 훈련 관측치 머릿수를 노가다로 요구합니다.
- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients.
- **치명 결함 3:** 뼈아프게도 로지스틱 회귀와 달리, KNN은 우리에게 "대체 어떤 예측 변수 원인이 제일 중요한 1등 공신 피쳐인가?"에 대해 단 한 마디도 친절히 알려주지 않습니다: 우리는 기호학적인 '수학 계수 표(table of coefficients)'를 결코 얻을 수 없습니다.

---

## Sub-Chapters

[< 4.5 A Comparison Of Classification Methods](../trans2.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans2.html)

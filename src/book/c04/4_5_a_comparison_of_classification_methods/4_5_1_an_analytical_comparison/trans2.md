---
layout: default
title: "trans2"
---

[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.5.1 An Analytical Comparison
# 4.5.1 분류 기법들의 분석적(수학적) 대결 

We now perform an _analytical_ (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression.
자, 이제 이 바닥의 4대 분류 기법들인 LDA, QDA, 나이브 베이즈, 그리고 전통의 강호 로지스틱 회귀가 링 위에 올라와 **분석적(analytical)**, 즉 수학적인 체급 비교 타이틀 매치를 벌입니다. 

We consider these approaches in a setting with $K$ classes, so that we assign an observation to the class that maximizes $\text{Pr}(Y = k \mid X = x)$.
이 녀석들을 타깃이 $K$개의 클래스 방으로 나뉜 세팅에서 살펴볼 텐데요, 결국 승리 판정의 핵심은 한 관측치가 어느 방에 속할 확률, 즉 $\text{Pr}(Y = k \mid X = x)$를 가장 높게 올려주는 클래스에 배정하는 것입니다.

Equivalently, we can set $K$ as the _baseline_ class and assign an observation to the class that maximizes
이를 수학적으로 살짝 비틀면, 타깃들 중 하나인 $K$번 방을 비교 **기준(baseline)** 점으로 콕 박아놓고, 다른 방들이 그 기준 대비 얼마나 점수가 높은지를 재는 아래의 수식 결괏값을 최대화하는 방에 관측치를 던져 넣는 것과 똑같습니다.

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) \quad (4.31)
$$

for $k = 1, \dots, K$. Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.
(물론 $k = 1, \dots, K$ 로 모든 방을 다 순회합니다.) 자, 이 공통 심판 수식 (4.31)의 생김새를 각 기법들이 어떻게 요리하는지를 돋보기로 들여다보면, 이 녀석들의 피가 섞인 가족 같은 유사성과 서로 양보 없는 차이점을 아주 명확하게 꿰뚫어 볼 수 있죠.

First, for LDA, we can make use of Bayes’ theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that
기호 1번, 딱딱한 깡통 기계 **LDA**부터 보죠. 이 녀석은 앞서 배운 베이즈 정리(4.15)를 깔고, "각 타깃 방의 데이터들은 중심 위치(평균)만 다르고 뚱뚱한 뱃살(공유 공분산 행렬)은 똑같은 아름다운 정규 분포 산봉우리(4.23) 출신이다!" 라는 억지 가정을 우겨넣어서 아래와 같은 점수 도면을 떡하니 내놓습니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j \quad (4.32)
$$

where $a_k = \log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ and $b_{kj}$ is the $j$th component of $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$.
여기서 저 복잡한 덩어리 $a_k$ 부품은 $\log \left( \pi_k / \pi_K \right) - \frac{1}{2} (\mu_k + \mu_K)^T \mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 라는 식으로 퉁쳐진 것이고, 인자 $b_{kj}$는 $\mathbf{\Sigma}^{-1} (\mu_k - \mu_K)$ 행렬 덩어리의 $j$번째 조각 부품입니다.

Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$.
가만히 보면 뒤에 $x_j$가 단순히 1차식으로 곱해져 있죠? 즉, LDA는 전통의 로지스틱 회귀가 하던 방식처럼 사후 확률의 로그 오즈 결괏값이 변수 $x$에 대해 선긋기 하듯 **직선형(linear)** 이라는 틀에 박힌 가정을 고집하고 있습니다.

Using similar calculations, in the QDA setting (4.31) becomes
자석에 철가루 붙듯 비슷한 연산 과정을 거쳐, 이번엔 기호 2번 융통성 있는 뚱땡이 **QDA** 세팅으로 넘어가면 판별 식 (4.31)은 덩치가 훅 커집니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} b_{kj} x_j + \sum_{j=1}^{p} \sum_{l=1}^{p} c_{kjl} x_j x_l \quad (4.33)
$$

where $a_k, b_{kj}$, and $c_{kjl}$ are functions of $\pi_k, \pi_K, \mu_k, \mu_K, \mathbf{\Sigma}_k$ and $\mathbf{\Sigma}_K$.
여기 붙은 조각들 $a_k, b_{kj}$ 그리고 가장 끝에 꼬리표처럼 달린 거대한 $c_{kjl}$ 항 덩어리들은 각 클래스의 데이터 비율과 중심 평균, 그리고 (이번엔 각자 다르게 인정한) 고유의 공분산 행렬들이 얼기설기 섞인 함수 조합물들입니다.

Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in $x$.
다시 말해, 모델 이름(Quadratic)이 힌트를 대놓고 뿌리듯이, QDA는 변수 $x$들끼리의 곱인 $x_j x_l$ 덩어리가 추가되어, 사후 확률을 재는 로그 오즈 점수판이 $x$에 대해 부드럽게 구부러진 **2차 비선형(quadratic)** 곡선 형태를 지닌다고 폭넓게 가정하는 겁니다.

Finally, we examine (4.31) in the naive Bayes setting.
마지막 주인공, 극단적 마이웨이 **나이브 베이즈** 세팅에서 저 기준 식 (4.31)이 어찌 되는지 뜯어봅시다.

Recall that in this setting, $f_k(x)$ is modeled as a product of $p$ one-dimensional functions $f_{kj}(x_j)$ for $j = 1, \dots, p$. Hence,
앞 장에서 기억나시나요? 이 무대포 녀석은 그 거대하고 복잡한 연결망 $f_k(x)$ 함수 보스를 "야, 니들 다 연관성 1도 없이 남남 독립이야!" 라며 $p$개의 심플한 1차원 함수 $f_{kj}(x_j)$ 들의 단순 '곱하기(product)'로 뿔뿔이 해체시켜 버렸었죠. 그래서 식이 이렇게 변신합니다:

$$
\log \left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = a_k + \sum_{j=1}^{p} g_{kj}(x_j) \quad (4.34)
$$

where $a_k = \log (\pi_k / \pi_K)$ and $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$.
여기서 치환된 머리 $a_k = \log (\pi_k / \pi_K)$ 이고, 독립된 개별 부품 함수들은 $g_{kj}(x_j) = \log (f_{kj}(x_j) / f_{Kj}(x_j))$ 로 분해되어 통통 튑니다.

Hence, the right-hand side of (4.34) takes the form of a _generalized additive model_, a topic that is discussed further in Chapter 7.
어라? 이렇게 쪼개놓고 보니 저 수식 (4.34)의 오른쪽 꼬라지(우변)가, 훗날 7장에서 뒷목 잡으며 더 깊게 파고들 주제인 이른바 **'일반화 가법 모델(generalized additive model, GAM)'** 이라는 레고 블록 더하기 구조판의 모습과 아주 판박이로 똑같은 형태를 취해 버리네요!

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:
자, 지금까지 뽑아낸 세 가지 심판 기준 도면 (4.32), (4.33), 그리고 (4.34)를 책상에 쫘악 깔아놓고 탐정처럼 돋보기 검사(Inspection)를 해보면, LDA, QDA, 나이브 베이즈 이 삼형제들 간의 얽히고설킨 족보 비밀에 대해 다음과 같은 재미있는 관찰 결론이 톡 튀어나옵니다:

- LDA is a special case of QDA with $c_{kjl} = 0$.
- **비밀 1:** LDA는 사실 QDA 형님의 큰 그림 안에서, 꼬리표로 붙은 골치 아픈 교차 부품 $c_{kjl}$ 세팅 값을 "에이씨 귀찮아! 그냥 0으로 꺼!" 라고 제약해 버린 아주 좁은 우물 안 **특수 사례(special case)** 쫄따구에 불과합니다.
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj} x_j$. In particular, this means that LDA is a special case of naive Bayes!
- **비밀 2:** 또한, 1차방정식 직선으로 결정 선을 반듯하게 찍 긋는 그 어떤 분류 기계라도 본질을 파고들면 $g_{kj}(x_j) = b_{kj} x_j$ 라는 족쇄 한계를 세팅한 나이브 베이즈 거대 세계관의 꼬붕 특수 사례일 뿐입니다. 특히, 이 충격적인 사실은 막가파 직선 장치 **LDA 조차도 사실 나이브 베이즈 그룹에 편입 통제당하는 하위 특수 파생 모델**이라는 역설적인 진실을 의미합니다!
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj}, \sigma_j^2)$, naive Bayes is actually a special case of LDA with $\mathbf{\Sigma}$ restricted to be a diagonal matrix.
- **비밀 3:** 역전! 그런데 거꾸로 우리가 만약 저 쿨했던 나이브 베이즈 분류기한테 "야, 네 1차원 부품 $f_{kj}(x_j)$ 들은 무조건 고루한 가우시안 정규 분포 $N(\mu_{kj}, \sigma_j^2)$ 곡선 옷만 입어!" 라고 규범 억압 족쇄를 채운다면? 이 땐 나이브 베이즈가 반대로 $\mathbf{\Sigma}$ 공분산 뱃살 행렬이 대각선 인자 값만 가지고 나머진 다 0이 된 바보 행렬(대각 행렬) 쪼가리로 극도로 제한된 **LDA 진영의 특수한 노예 사례**로 굴러떨어지고 맙니다. 
- Neither QDA nor naive Bayes is a special case of the other. QDA includes multiplicative terms of the form $c_{kjl} x_j x_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important.
- **비밀 4:** 한편, QDA 행님과 나이브 베이즈 똘끼 녀석은 둘 다 서로를 노예로 지배하는 종속 특수 사례 관계가 절대 아닙니다. 왜냐고요? QDA는 수식 안에 독립 따윈 쌩까는 $c_{kjl} x_j x_l$ 형태의 징글징글하게 얽힌 서로의 곱셈 융합 파편(multiplicative terms)을 품고 있거든요. 그러므로 예측 변수들끼리 질척거리는 복합 상호작용(interactions) 눈치싸움이 결과 판정에 엄청난 요동을 치는 험난한 실전 세팅 현장에서는, 당연하게도 그 변수들의 눈치 융합을 다 받아 계산해 주는 **QDA 장치가 정밀도 예측 전투에서 훨씬 더 다 맞히고 이겨버릴 잠재력(potential)** 무력을 지니고 있습니다.

How does logistic regression tie into this story? This is identical to the linear form of LDA (4.32).
그럼 도대체 이 살벌한 족보 비교 스토리 무대(story)에 원조 깡패인 **로지스틱 회귀** 기계 장치는 어떻게 엮여(tie into) 다시 등판해 참전할까요? 놀랍게도 이 녀석의 판정 수식 꼬라지는 아방가르드한 LDA의 선형 판별 뼈대 수식 도면 (4.32)와 토씨 하나 다르지 않고 쌍둥이처럼 완벽하게 **똑같습니다(identical)**.

In LDA, the coefficients in this linear function are functions of estimates obtained by assuming that $X$ follow a normal distribution.
다만 출신 뿌리가 다르죠. LDA 진영에서는 이 수식 뼈대에 얹을 스코어 부품(계수)들을 산출할 때, "너흰 모두 예쁜 가우시안 정상 정규 분포를 졸졸 따라야 해!" 라는 엄격한 강압 추종 통제 가설 하에서 불쌍하게 계산 짜여 맞춰 도출 파생된 의존적 추정치들의 껍질 함수(functions of estimates) 결괏값을 가져다 씁니다.

By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5).
이와는 정반대 로선으로, 실용파 로지스틱 회귀 깡패 군단에서는 조립 계수 단속 부품을 찾을 때 저딴 꼰대 정규 분포 서클 규범 족쇄 따위 개나 줘버리고 비웃으며 시크하게 무시합니다. 오로지 현장에서 적중 스코어를 올리기 위해 우도 함수(likelihood function) 수식 (4.5) 결괏값을 아주 극대화 정점(maximize) 통과시켜 가장 통쾌하게 최상 생존력을 찍게 만들어 줄 최고의 야생 치트키 부품만을 단독 표적으로 철저히 선택하고 긁어모읍니다.

Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.
따라서, 만약 현장 현실의 지뢰밭 데이터가 매우 운이 좋게도 "올ㅋ 다들 얼추 정규 분포 둥근 언덕을 따르네?" 같은 얌전한 교과서 조건(normality assumption) 지형이 대충이나마 맞아떨어지는 천혜의 세팅 환경이라면? 당연히 가우시안 특화 장치인 **LDA가 로지스틱 회귀를 성과로 무참히 압살(outperform)** 해 기대 승리를 쟁취할 것입니다. 반대로 현장이 저딴 정규 규범 따윈 짓밟혀 없는 불규칙 난동의 잡초 무규칙 시궁창 맵에 세팅됐다면? 두말할 것 없이 규범 족쇄를 진작 벗어 던진 실용깡패 **로지스틱 회귀가 월등히 대박 성과 예측 방어 생존력(perform better)을 내며 크게 역전 승리 활약**할 것이라고 우리는 이 상황을 재단해 예측할 수 있습니다! 

We close with a brief discussion of _K-nearest neighbors_ (KNN), introduced in Chapter 2.
자, 기나긴 기계 장치 성능 타율 썰 풀기를 2장에서 인사 나눴던 귀여운 투박 기계, **K-최근접 이웃(KNN)** 에 대한 짭짤한 한 줄 평 논의로 짧게 갈무리(close) 해 봅시다.

Recall that KNN takes a completely different approach from the classifiers seen in this chapter. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary.
기억하실 겁니다. KNN 이 녀석은 지금까지 4장에서 신나게 떠들고 다루어왔던 고상한 수식 분류기들과는 물에서 노는 것부터가 '완전히 동떨어진 별개의 딴 세상' 무식 돌파 접근법을 씁니다. 즉, 얘는 수식 뼈대라곤 1도 없는 **완전 순도 100% 비모수적(non-parametric) 잡초 기술**입니다: "결정 경계선이 선형 직선이네 2차 곡선이네?" 이딴 모양새 가설 따위 아예 일절 안 하고 눈 딱 감고 내지릅니다!

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that $n$ is very large and $p$ is small.
- **장점:** 이놈은 뼈대가 없는 비모수 무투파라서, 현장 맵 지형의 결정 경계가 예측 불가의 꽈배기처럼 미치도록 뒤틀리고 꼬인 초 비선형 형태를 띨 때, 수식 꼰대 장치들인 LDA나 로지스틱 회귀 형님들을 비웃으며 씹어 먹고 제패(dominate) 할 수 있습니다. 단, **조건이 붙죠.** 데이터 머릿수 $n$이 미치도록 빵빵하게 쏟아져 넘치고 타깃 변수 $p$의 덩치는 얄상하게 적을 때라는 달달한 뷔페 상황 세팅 조건에서만요!
- In order to provide accurate classification, KNN requires _a lot_ of observations relative to the number of predictors.
- **단점 1:** 제대로 된 칼 같은 정확 분류를 해내려면? KNN은 다뤄야 할 변수 아이템들 숫자에 견주어 볼 때, 정말 눈물 나도록 어마무시하게 **압도적으로 막강 우량한 징그러울 정도의 물량적 거대 현장 관측치 데이터 쪽수(a lot)** 부대 동원을 생존 체력으로 강요하고 빨아먹습니다. 
- Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients.
- **단점 2:** 가장 치명적인 허탈함! 친절했던 로지스틱 회귀 기계와는 다르게, 묵묵부답인 KNN은 수사관들에게 "어떤 예측 단서 변수가 나쁜 놈 잡는데 치사율 1위 중요 랭크였어?!" 라는 실적 통계 리포트 비밀을 말해주지 않습니다. 즉 수사 장부인 **계수 테이블 쪼가리조차 하나 뱉어주지 못하는 까막눈** 맹점 한계입니다.

---

## Sub-Chapters

[< 4.5 A Comparison Of Classification Methods](../index.html) | [4.5.2 An Empirical Comparison >](../4_5_2_an_empirical_comparison/trans2.html)

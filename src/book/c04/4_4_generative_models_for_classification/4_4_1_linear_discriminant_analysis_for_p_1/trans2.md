---
layout: default
title: "trans2"
---

[< 4.4 Generative Models For Classification](../trans2.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4.1 Linear Discriminant Analysis for p = 1
# 4.4.1. LDA: 선형 판별 분석 (단서가 딱 하나일 때의 역추적 마법)

For now, assume that $p = 1$—that is, we have only one predictor.
복잡한 거절하고 지금 당장은, 세상이 심플해서 오직 $p = 1$ 인 상태, 즉 우리가 다루는 범인 색출용 `예측 변수 X` 특성 단서가 달랑 한 개뿐인 세상이라고 가벼운 마음으로 가정해 봅시다.

We would like to obtain an estimate for $f_k(x)$ that we can plug into (4.15) in order to estimate $p_k(x)$.
우리의 궁극적 목표는 진짜 범인 확률인 $p_k(x)$ 를 도출하기 위해, (4.15)번 베이즈 마법 방정식 입구 틈에다 끼워 넣을 '역추적 확률 밀도 곡선' 퍼즐 쪼가리, $f_k(x)$ 덩어리를 어떻게든 가짜로라도 추정해 내는 것입니다.

We will then classify an observation to the class for which $p_k(x)$ is greatest.
그러고 나면 우리는 새로운 관측치를 이 $p_k(x)$ 판결 확률 최고 점수가 터져 나오는 승리자 1등 클래스 방으로 미련 없이 밀어 넣어 분류시킬 것입니다.

To estimate $f_k(x)$, we will first make some assumptions about its form.
그런데 모르는 $f_k(x)$ 곡선 모양을 맨땅에서 억지로 추정하기 위해, 우리 수학자들은 뻔뻔하게 그 녀석의 구부러진 곡선 뼈대에 대해 상당히 강력하고 위험한 가정을 먼저 선포해 버려야 합니다.

In particular, we assume that $f_k(x)$ is _normal_ or _Gaussian_.
특히나 가장 심각한 전제로, 우리는 각 방에 몰려있는 범인들의 단서 곡선 $f_k(x)$ 형태가 지극히 아름답고 정갈한 종 모양의 **정규(Normal)** 혹은 **가우시안(Gaussian)** 분포 곡선 띠를 띄고 있다고 확신에 찬 가정을 다짜고짜 때려버립니다!

In the one-dimensional setting, the normal density takes the form
특성 한 개뿐인 1차원 직선 공간 세팅 안에서, 저 가우시안 정규 밀도 함수 공식은 다음과 같은 징그러운 모양새를 취합니다:

$$
f_k(x) = \frac{1}{\sqrt{2 \pi} \sigma_k} \exp \left( -\frac{1}{2 \sigma_k^2} (x - \mu_k)^2 \right) \quad (4.16)
$$

where $\mu_k$ and $\sigma_k^2$ are the mean and variance parameters for the $k$th class.
수식 안의 저 $\mu_k$ 와 $\sigma_k^2$ 은 중학생 때 배우는 그 수학, 각각 소속된 $k$번째 방 집단의 **평균점(Mean)** 과 퍼진 뚱뚱한 정도인 **분산(Variance)** 을 제어하는 핵심 영혼 파라미터 꼭지 역활입니다.

For now, let us further assume that $\sigma_1^2 = \dots = \sigma_K^2$: that is, there is a shared variance term across all $K$ classes, which for simplicity we can denote by $\sigma^2$.
자 짐을 더 줄이기 위해 한 술 더 떠서, 모든 방들의 분산 뱃살 통통한 정도가 완벽히 다를 바 없이 똑같다고($\sigma_1^2 = \dots = \sigma_K^2$) 한 걸음 더 오지랖의 비약적인 모험을 저질러 봅시다. 즉, 분류할 무수히 많은 모든 $K$ 클래스 집단이 분산 넓이 수치를 전혀 차별 없이 하나로 끈끈하게 '공유'하고 복제하고 있다는 망상적 가정입니다. 우린 편의상 이 불쌍한 녀석들의 꼬리표 첨자를 팍 떼버리고, 통합 공통 뱃살이라는 뜻에서 그냥 심플하게 $\sigma^2$ 라고 통일해 부르겠습니다.

Plugging (4.16) into (4.15), we find that
이제 이 무스펙 단순해진 정규분포 가짜 껍데기 구멍 (4.16) 식 통째를 아까 (4.15) 베이즈 분수 방정식 안으로 쑤셔 끼워 넣어 화학작용을 일으키면, 다음과 같은 무지막지한 사후 공식 결괏값을 뽑아냅니다:

$$
p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_k)^2 \right)}{\sum_{l=1}^{K} \pi_l \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_l)^2 \right)} \quad (4.17)
$$

The Bayes classifier involves assigning an observation $X = x$ to the class for which (4.17) is largest.
신성한 베이즈 분류기는 저 끔찍한 (4.17) 수식 덩어리를 넣고 돌렸을 때 점수가 가장 거대하게 튀어나오는 그 번호표의 방(클래스)에게 최후의 승자로서 내 소중한 새 관측치 환자 $X=x$ 를 영예롭게 던져주는 역할을 합니다.

Taking the log of (4.17) and rearranging the terms, it is not hard to show that this is equivalent to assigning the observation to the class for which
저 악성 복잡한 (4.17) 지수 덩어리를 편하게 찢어발기기 위해 양변에 사정없이 자연로그($\log$) 마법을 먼저 씌워버리고 남은 미적분 부스러기 항들을 대수학으로 예쁘게 싹 치워 재배열 믹스해 버리면, 놀랍게도 그 수치 1등 확률을 잡으려 낑낑대는 짓거리의 운명이, 아주 다행스럽게도 단지 아래 수식(단순 판별 함수) 결과값이 가장 커지는 클래스를 고르는 것과 수학적으로 너무나 완벽히 논리적 **동치(Equivalent)** 관계라는 사실을 싱겁고 쉽게 증명해 낼수 있습니다!

$$
\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2 \sigma^2} + \log(\pi_k) \quad (4.18)
$$

is largest.
(이 점수가 1등인 녀석이 범인입니다.)

For instance, if $K = 2$ and $\pi_1 = \pi_2$, then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$, and to class 2 otherwise.
조금 더 현실감을 줘볼까요? 가령 세상이 선과 악의 이진 분류 $K=2$ 상황이고 운 좋게 두 그룹의 애초 인구 비율 쪽수가 반반으로 똑같아서 사전 확률 $\pi_1 = \pi_2$ 라고 공평하다 한다면, 컴퓨터 판사는 $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$ 라는 조건을 부술 때 가차 없이 해당 관측치를 1번 구역에 처박고, 미달되면 2번으로 내던집니다.

The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$; one can show that this amounts to
이 세계의 가상의 베이즈 재판 평결 칼날선 수직 경계(Decision boundary)는 두 진영의 점수가 $\delta_1(x) = \delta_2(x)$ 로 서로 비기는 팽팽한 한 점으로 모아지는 스팟입니다; 

$$
x = \frac{\mu_1^2 - \mu_2^2}{2(\mu_1 - \mu_2)} = \frac{\mu_1 + \mu_2}{2} \quad (4.19)
$$
(그 균형 칼날 선은 위처럼 1번 방과 2번 방의 정확히 '중간 산술 평균 반띵점 $\frac{\mu_1 + \mu_2}{2}$ '이라는 너무나 어이없고 단순한 허들 위치로 모아진다는 것을 우리는 가벼운 수식 도출로 입증할 수 있습니다!)

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\sigma^2$.
그러나 시궁창 같은 진짜 현실 데이터 세계에서는, "내 데이터 단서 $X$가 각 둥지 안에서 진짜 기가 막히는 완벽한 가우시안 정규 분포 곡선을 그리고 있을 거야!" 라고 하늘을 우러러 확신에 찬 망상을 한다 하더라도, 진짜 신의 영역인 베이즈 분류기 점수를 뽑아 쓰려 시도하려면 우리는 그 모집단 어딘가에 숨겨진 신의 점수표들, 즉 진짜 평균 $\mu_1, \dots, \mu_K$, 진짜 사전확률 $\pi_1, \dots, \pi_K$, 그리고 진짜 공유 분산 $\sigma^2$ 파라미터 값들을 우리 손으로 발품 팔아 어떻게든 가짜 실측 수치로 추정해 대신 박아 넣어야만 하는 고통에 휩싸입니다.

The _linear discriminant analysis_ (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k, \mu_k$, and $\sigma^2$ into (4.18).
자, 이제 드디어 히어로 **선형 판별 분석(Linear Discriminant Analysis, LDA)** 기법 알고리즘이 등장합니다! 이 녀석은 저 (4.18) 공식 빈 공백 자리에 우리가 훈련 데이터로 대강 눈대중 찍어 짜낸 조악한 진짜 추정치 가짜 숫자들($\hat{\pi}_k, \hat{\mu}_k, \hat{\sigma}^2$)을 무자비하게 냅다 대신 끼워 넣어서, 감히 신의 물건인 신성한 천상의 베이즈 분류기 본판 모델 작동 방식에 가장 흡사하게 바짝 엉겨 붙어 모방해 통과하려는 일종의 강력한 대체품 위조 기법입니다.

In particular, the following estimates are used:
구체적으로 LDA는 수사 현장 훈련 데이터를 털어 다음과 같은 상식적인 가짜 추정치 통계 덩어리를 차출합니다:

$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i: y_i = k} x_i \\
\hat{\sigma}^2 = \frac{1}{n - K} \sum_{k=1}^{K} \sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2 \quad (4.20)
$$

where $n$ is the total number of training observations, and $n_k$ is the number of training observations in the $k$th class.
여기서 $n$은 주어진 전체 훈련 연습생들의 총합 쪽수이고, $n_k$는 그중에서 유독 내 둥지인 $k$번째 방 구역 라벨표를 달고 있는 내 편 훈련생들의 숫자입니다.

The estimate for $\mu_k$ is simply the average of all the training observations from the $k$th class, while $\hat{\sigma}^2$ can be seen as a weighted average of the sample variances for each of the $K$ classes.
$\mu_k$ 신을 흉내 내는 가짜 위조 추정치 $\hat{\mu}_k$ 산식은 보시다시피 그냥 너무 터무니없이 심플하게도, 그 $k$ 방 안에 모인 모든 놈들의 체중(관측 단서 점수)을 다 더해서 출석 번호로 나눈 **'평범한 산술 평균'** 을 그대로 베낀 겁니다. 반면 덩치 큰 저 분산 뱃살 $\hat{\sigma}^2$ 공식은 모든 $K$개 클래스들 각 방에서 측정한 표본 분산들을 방 크기(쪽수) 비중력에 따라 통으로 비벼서 더해준 **가중 평균**이라고 바라보면 소화가 쉽습니다.

In the absence of any additional information, LDA estimates $\pi_k$ using the proportion of the training observations that belong to the $k$th class.
만약 누군가 은밀하게 귀띔해 준 진짜 하늘의 비율(사전 지식) 따위가 없는 완전히 무지랭이 암흑 상황이라면, 우리 LDA 요원은 판결의 가장 중요한 기준점인 선입견 자잣뼈 사전 확률 $\pi_k$ 조차도 그냥 무식하게 내 훈련 캠프 인구수 중에서 그 클래스가 차지하는 쪽수 '비율(Proportion)'을 이용해서 찍어버립니다.

In other words,
다른 말로 심플하게 퉁쳐서 식을 보여주자면 이렇습니다:

$$
\hat{\pi}_k = \frac{n_k}{n} \quad (4.21)
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which 
마침내 LDA 분류기 모델은 피 한 방울 안 섞인 현장에서 지가 맘대로 손쉽게 빼낸 짝퉁 실측 추정치 재료인 수식 (4.20)과 통계비 분수비율인 (4.21) 번 파편 조각들을 한데 모조리 긁어모아 맨 처음 던져준 저 위대한 판별 공식 (4.18) 속으로 모조리 끼워버립니다. 그런 다음, 새로운 테스트 환자 점수 $X=x$ 를 줬을 때 튀어나오는 다음 수식 

$$
\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2 \hat{\sigma}^2} + \log(\hat{\pi}_k) \quad (4.22)
$$

is largest.
이 점수가 최고 1등을 찍어내는 클래스의 뱃속으로 내 관측치를 미련 없이 쑤셔 넣어 분류 구형 선고를 때립니다! 

The word _linear_ in the classifier’s name stems from the fact that the _discriminant functions_ $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$).
마지막으로, 왜 굳이 이 기법 이름 중간에 그토록 고지식하고 교과서적인 **선형(Linear)** 이라는 단어가 영광스러운 타이틀로 뿌리 박혀 있는가요? 그것은 다름 아니게도, 위에서 우리가 그렇게 발악하며 빼돌렸던 가짜 대체 점수 (4.22)번의 최후의 **판별 함수(Discriminant Function)** $\hat{\delta}_k(x)$ 의 수학적 구조 자체가 미친 뒤틀린 곡선 함수 따위가 아니라, 우리가 알고 있는 가장 단순직관적인 $X$ 에 대한 정비례 **선형 1차 함수(Linear)** 다항식으로 너무나 예쁘고 깔끔하게 종결되기 때문입니다! ($x^2$나 오만 복잡한 로그지수 덩어리 형태가 다 날아가 버린 걸 보십시오!)

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.4 Generative Models For Classification](../trans2.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans2.html)

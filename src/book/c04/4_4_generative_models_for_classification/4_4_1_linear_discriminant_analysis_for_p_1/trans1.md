---
layout: default
title: "trans1"
---

[< 4.4 Generative Models For Classification](../trans1.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4.1 Linear Discriminant Analysis for p = 1
# 4.4.1 p=1인 단일 예측 변수에 대한 선형 판별 분석 (Linear Discriminant Analysis)

For now, assume that $p = 1$—that is, we have only one predictor. We would like to obtain an estimate for $f_k(x)$ that we can plug into (4.15) in order to estimate $p_k(x)$. We will then classify an observation to the class for which $p_k(x)$ is greatest. To estimate $f_k(x)$, we will first make some assumptions about its form.
지금 당장은, 세상이 심플해서 오직 $p=1$ 인 상태, 즉 우리가 다루는 예측 변수 $X$ 특성이 단 한 개뿐인 세상이라고 가벼운 마음으로 가정해 봅시다. 우리의 목표는 궁극적인 사후 확률인 $p_k(x)$를 추정해 내기 위해서, (4.15) 베이즈 방정식 안에 소화제로 밀어 넣을 역추적 확률 밀도 곡선인 $f_k(x)$에 대한 인위적인 수학 추정 식을 기필코 얻어내는 것입니다. 그러고 나면 우리는 새로운 관측치를 $p_k(x)$ 점수가 일등으로 가장 높게 터져 나오는 승리자 클래스 방으로 밀어 넣어 영원히 분류시킬 것입니다. $f_k(x)$를 억지로 추정하기 위해, 우리는 뻔뻔하게 그 녀석의 구부러진 곡선 형태에 대해 상당히 강력한 몇 가지 가정을 먼저 선포할 것입니다.

In particular, we assume that $f_k(x)$ is _normal_ or _Gaussian_. In the one-dimensional setting, the normal density takes the form
특히나 가장 심각한 전제로, 우리는 해당 클래스의 종속 집단의 우도 성질인 $f_k(x)$가 지극히 아름답고 정갈한 종 모양 곡선인 **정규(Normal)** 혹은 가우시안(Gaussian) 분포 곡선의 띄고 있다고 확신에 찬 가정을 내리겠습니다. 특성이 하나뿐인 1차원 공간 세팅 안에서, 정규 밀도 함수 공식은 다음과 같은 더럽고 무서운 형태를 취합니다:

$$
f_k(x) = \frac{1}{\sqrt{2 \pi} \sigma_k} \exp \left( -\frac{1}{2 \sigma_k^2} (x - \mu_k)^2 \right) \quad (4.16)
$$

where $\mu_k$ and $\sigma_k^2$ are the mean and variance parameters for the $k$th class. For now, let us further assume that $\sigma_1^2 = \dots = \sigma_K^2$: that is, there is a shared variance term across all $K$ classes, which for simplicity we can denote by $\sigma^2$. Plugging (4.16) into (4.15), we find that
수식 안의 저 $\mu_k$ 와 $\sigma_k^2$ 은 중학생 때 배우는 $k$번째 고유 클래스 집단들의 **평균(Mean)** 과 **분산(Variance)**을 제어하는 파라미터 꼭지 변수들입니다. 자 짐을 줄이기 위해 지금 당장, 모든 여러 개 $K$ 클래스 집단들이 전부 뚱뚱한 뱃살 정도가 완벽히 똑같은 $\sigma_1^2 = \dots = \sigma_K^2$ 인 분포라고 한 걸음 더 오지랖의 비약적인 가정을 저질러 봅시다: 즉, 모든 $K$ 클래스 집단이 너비 분산값을 차별 없이 '공유'하고 복제하여 갖고 있다는 말이며, 우린 단순하고 심플해진 요 녀석을 그냥 첨자를 박살 내고 평범하게 $\sigma^2$ 라고 통칭해 부르겠습니다. 이제 이 무스펙 정규분포 구멍 (4.16) 식을 위대한 (4.15) 베이즈 방정식 분모 분자에 억지로 쑤셔 끼워 넣으면, 다음과 같은 기가 막히는 사후 공식 결괏값을 뽑아냅니다:

$$
p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_k)^2 \right)}{\sum_{l=1}^{K} \pi_l \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_l)^2 \right)} \quad (4.17)
$$

The Bayes classifier involves assigning an observation $X = x$ to the class for which (4.17) is largest. Taking the log of (4.17) and rearranging the terms, it is not hard to show that this is equivalent to assigning the observation to the class for which
성스러운 베이즈 분류기(Bayes classifier)는 저 끔찍한 (4.17) 수식 덩어리를 욱여넣었을 때 분수가 가장 거대하게 튀어나오는 클래스 항목에게 최후의 승자로서 내 소중한 관측치 $X=x$ 를 영예롭게 할당해버리는 역할을 가집니다. 저 (4.17)번의 말도 안 되는 지수 분수 식 덩어리 양쪽에 또다시 자연로그($\log$)를 사정없이 씌워버린 다음 남은 미적분 부스러기 항들을 대수학으로 예쁘게 재배열 조립해버리면, 놀랍게도 그 극악무도했던 가장 큰 분수 확률을 잡는 짓거리가 결국은 아래 수식(판별 함수) 결과값이 가장 커지는 클래스를 골라 잡는 것과 수학적으로 너무나 완벽히 논리적 **동치(Equivalent)** 라는 것을 아주 싱겁게 증명해 낼수 있습니다!

$$
\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2 \sigma^2} + \log(\pi_k) \quad (4.18)
$$

is largest. For instance, if $K = 2$ and $\pi_1 = \pi_2$, then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$, and to class 2 otherwise. The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$; one can show that this amounts to
가령 이진 분포 $K=2$ 상황이고 운 좋게 두 그룹의 전체 크기가 똑같아서 분열 전 사전 확률이 똑똑히 $\pi_1 = \pi_2$ 라고 한다면, 베이즈 분류기는 $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$ 를 타격할 때 가차 없이 해당 관측치를 1번 클래스 집단에 처박고, 반대의 경우 2번으로 내던집니다. 베이즈 결괏값의 칼날 같은 판별 결정 경계(Decision boundary)는 그 두 놈의 승점이 정확히 $\delta_1(x) = \delta_2(x)$ 로 서로 비기는 팽팽한 한 점으로 모아집니다; 그리고 그것이 고스란히 아래와 같은 단순한 클래스 평균의 중점 산술값으로 모아진다는 것을 우리는 가벼운 증명으로 보일 수 있습니다:

$$
x = \frac{\mu_1^2 - \mu_2^2}{2(\mu_1 - \mu_2)} = \frac{\mu_1 + \mu_2}{2} \quad (4.19)
$$

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\sigma^2$. The _linear discriminant analysis_ (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k, \mu_k$, and $\sigma^2$ into (4.18). In particular, the following estimates are used:
그러나 시궁창 같은 현실 세계에서는, 비록 우리가 $X$가 각 타겟 클래스 안에서 가우시안 정규 분포 곡선으로 아주 예쁘게 도출되었다고 확신에 찬 망상을 한다 쳐도, 저 신성불가침 영역인 베이즈 분류기 점수를 찍어 돌리려면 현실 데이터로부터 여전히 $\mu_1, \dots, \mu_K$ (평균), $\pi_1, \dots, \pi_K$ (사전확률), 그리고 공유 $\sigma^2$ (분산) 따위의 온갖 모집단 진짜 파라미터들을 꾸역꾸역 손수 추정치로 박아 넣어야만 하는 고통에 시달립니다. 이제 드디어 등장하는 **선형 판별 분석(Linear Discriminant Analysis, LDA)** 기법은 저 (4.18) 공식 자리에 우리가 훈련 데이터로 대강 눈대중 찍어낸 추정치들($\hat{\pi}_k, \hat{\mu}_k, \hat{\sigma}^2$)을 무자비하게 대신 끼워 넣어서, 감히 신성한 저 천상의 베이즈 분류기 본판 모델에 가장 근사하게 바짝 엉겨 붙어 모방해 내려는 기법입니다. 구체적으로 우리는 LDA 계산 시 훈련 데이터를 털어 다음과 같은 추정치 덩어리를 차출합니다:

$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i: y_i = k} x_i \\
\hat{\sigma}^2 = \frac{1}{n - K} \sum_{k=1}^{K} \sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2 \quad (4.20)
$$

where $n$ is the total number of training observations, and $n_k$ is the number of training observations in the $k$th class. The estimate for $\mu_k$ is simply the average of all the training observations from the $k$th class, while $\hat{\sigma}^2$ can be seen as a weighted average of the sample variances for each of the $K$ classes. In the absence of any additional information, LDA estimates $\pi_k$ using the proportion of the training observations that belong to the $k$th class. In other words,
여기서 $n$은 주어진 전체 훈련 데이터 관측치 조각의 총합 수이고, $n_k$는 그중에서 유독 $k$번째 클래스 라벨에만 해당하는 훈련된 희생양 숫자입니다. 저 $\mu_k$ 녀석를 구하는 가짜 추정치 $\hat{\mu}_k$ 는 너무 심플하게도 그저 $k$ 그룹에 속해있는 전체 관측치들을 다 더해서 갯수로 나눈 산술 **'평균(Average)'**을 그대로 베낍니다. 반면 저 복잡한 합동 분산 $\hat{\sigma}^2$ 공식은 모든 $K$개 클래스들 뱃속에 존재하는 분산들을 쪽수(무게) 비중에 따라 통으로 평균 낸 가중 평균이라고 보면 아주 쉽습니다. 어떠한 배경 사전 지식도 없는 완전 무지랭이 상황이라면, LDA 요원은 무조건 사전 확률 $\pi_k$ 조차도 전체 인구 중 그 클래스가 차지하는 쪽수 '비율(Proportion)'을 이용해서 무식하게 다음과 같이 추정해 버립니다. 다른 말로 퉁쳐서,

$$
\hat{\pi}_k = \frac{n_k}{n} \quad (4.21)
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which 
마침내 LDA 분류기 모델은 지가 맘대로 손쉽게 빼낸 가짜 실측 추정치인 (4.20)과 통계 숫자 (4.21) 분수를 아까 저 위대한 자연로그 판별공식 (4.18) 속으로 몽땅 끼워버립니다. 그런 다음, 이 지독한 인위적 수식 함수 점수가 일등으로 가장 높게 튀어나오는 최고 클래스의 뱃속으로 내 새로운 관측치 $X=x$ 를 쑤셔 넣고 판별 결론을 내립니다:

$$
\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2 \hat{\sigma}^2} + \log(\hat{\pi}_k) \quad (4.22)
$$

is largest. The word _linear_ in the classifier’s name stems from the fact that the _discriminant functions_ $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$).
이 점수가 최고 1등을 차지할 때가 바로 분류 점수입니다. 참고로 이 판별 기법의 정식 명칭 이름 중간에 위풍당당하게 껴있는 **선형(Linear)** 이라는 단어 뿌리는 다름 아니게도, 위에서 우리가 그렇게 발악하며 빼돌렸던 (4.22)번의 최후의 **판별 함수(Discriminant Function)** $\hat{\delta}_k(x)$ 의 수학적 구조 자체가, (x의 복잡한 2차나 곡선 따위가 아니라) $x$ 에 대한 정비례 **일차 선형(Linear)** 함수로 깔끔하게 나열되어 종결된다는 그 벅찬 사실에서 기인한 것입니다!

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.4 Generative Models For Classification](../trans1.html) | [4.4.2 Linear Discriminant Analysis For P 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans1.html)

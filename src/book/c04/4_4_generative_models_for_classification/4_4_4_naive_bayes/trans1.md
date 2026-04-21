---
layout: default
title: "trans1"
---

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans1.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4.4 Naive Bayes
# 4.4.4 나이브 베이즈 (Naive Bayes)

In previous sections, we used Bayes’ theorem (4.15) to develop the LDA and QDA classifiers.
이전 섹션들에서, 우리는 LDA 및 QDA 분류기를 개발하기 위해 베이즈 정리 (4.15)를 활용했습니다.

Here, we use Bayes’ theorem to motivate the popular _naive Bayes_ classifier.
여기서, 우리는 대중적으로 널리 사용되는 **나이브 베이즈(naive Bayes)** 분류기의 이론적 근거를 제공(motivate)하기 위해 베이즈 정리를 사용합니다.

Recall that Bayes’ theorem (4.15) provides an expression for the posterior probability $p_k(x) = \text{Pr}(Y = k \mid X = x)$ in terms of $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$.
베이즈 정리 (4.15)가 사전 확률들인 $\pi_1, \dots, \pi_K$와 밀도 함수들인 $f_1(x), \dots, f_K(x)$의 관점에서 사후 확률 $p_k(x) = \text{Pr}(Y = k \mid X = x)$에 대한 수식 표현을 제공한다는 것을 상기하십시오.

To use (4.15) in practice, we need estimates for $\pi_1, \dots, \pi_K$ and $f_1(x), \dots, f_K(x)$.
(4.15)를 실제 추론에 적용하기 위해, 우리는 $\pi_1, \dots, \pi_K$ 및 $f_1(x), \dots, f_K(x)$에 대한 추정치들이 필요합니다.

As we saw in previous sections, estimating the prior probabilities $\pi_k$ is typically straightforward: we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$th class. 
이전 섹션에서 확인했듯이, 사전 확률 $\pi_k$를 추정하는 것은 일반적으로 매우 간단(straightforward)합니다: 우리는 $\hat{\pi}_k$를 훈련 관측치들 중에서 $k$번째 클래스에 속하는 집단의 비율로써 추정할 수 있습니다.

However, estimating $f_1(x), \dots, f_K(x)$ is more subtle.
하지만, $f_1(x), \dots, f_K(x)$ 함수를 추정하는 것은 조금 더 미묘하고 까다롭습니다(subtle).

Recall that $f_k(x)$ is the $p$-dimensional density function for an observation in the $k$th class.
$f_k(x)$는 곧 $k$번째 클래스 내의 한 관측치에 대한 $p$-차원의 밀도 함수라는 사실을 기억하십시오.

In general, estimating a $p$-dimensional density function is challenging.
일반적으로, $p$-차원의 밀도 함수를 추정하는 것은 꽤 어려운 난제(challenging)입니다.

In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and shared covariance matrix $\mathbf{\Sigma}$.
LDA 모델에서, 우리는 이 복잡한 연산 작업을 크게 단순화해 주는 매우 강력한 가정 하나를 도입합니다: 우리는 $f_k$가 클래스별로 고유한 평균 $\mu_k$와 공통으로 공유되는 공분산 행렬 $\mathbf{\Sigma}$를 지닌 다변량 정규 확률 변수의 밀도 함수라고 가정합니다.

By contrast, in QDA, we assume that $f_k$ is the density function for a multivariate normal random variable with class-specific mean $\mu_k$, and class-specific covariance matrix $\mathbf{\Sigma}_k$.
이와 대조적으로, QDA에서는 $f_k$가 역시 클래스별 고유 평균 $\mu_k$와, 클래스 고유의 전용 공분산 행렬 $\mathbf{\Sigma}_k$를 갖춘 다변량 정규 확률 변수의 밀도 함수라고 새롭게 가정합니다.

By making these very strong assumptions, we are able to replace the very challenging problem of estimating $K \times p$-dimensional density functions with the much simpler problem of estimating means and covariance matrices.
이러한 강력한 가정들을 설정함으로써, 우리는 초기의 $K \times p$-차원 밀도 함수 전체를 전방위 추정해야 하는 어려운 난제를, 단지 평균과 공분산 행렬 요소들을 추정하는 훨씬 단순해진 문제로 쉽게 대체(replace)할 수 있게 됩니다.

The naive Bayes classifier takes a different tack for estimating $f_1(x), \dots, f_K(x)$.
반면 나이브 베이즈 분류기는 $f_1(x), \dots, f_K(x)$ 함수를 추정 계산하기 위해 앞선 두 방식과 전혀 다른 방향의 접근 노선(different tack)을 취합니다.

Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single, sweeping assumption:
이러한 함수들이 특정한 하나의 분포 족(예: 다변량 정규 분포 모형)에 무조건 속한다고 한계 짓는 가정 대신, 우리는 그 대신 단 하나의, 전면적이고 강력한 포괄적 제한 가정(sweeping assumption)만을 마련합니다:

**Within the $k$th class, the $p$ predictors are independent.**
**해당 $k$번째 클래스 내부에서, 전체 $p$개의 변수들은 서로 상호 전면 독립(independent)적이다.**

Stated mathematically, this assumption means that for $k = 1, \dots, K$,
수학적으로 명시된 이 가정은, 클래스 $k = 1, \dots, K$ 에 대하여 다음 도출 등식을 의미합니다:

$$
f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p) \quad (4.29)
$$

where $f_{kj}$ is the one-dimensional density function of the $j$th predictor among observations in the $k$th class.
여기서 $f_{kj}$는 도출된 $k$번째 클래스 관측치 집단 사이의 $j$번째 개별 예측 변수 하나에 국한된 1차원 밀도 함수(one-dimensional density function)를 지칭합니다.

Why is this assumption so powerful?
왜 이러한 독립 가정이 연산에 있어 강력한 위력을 가질까요?

Essentially, estimating a $p$-dimensional density function is challenging because we must consider not only the _marginal distribution_ of each predictor — that is, the distribution of each predictor on its own — but also the _joint distribution_ of the predictors — that is, the association between the different predictors.
본질적으로, 거대 $p$-차원 밀도 함수를 추정하는 작업이 까다로운 이유는 우리가 반드시 개별 각 예측 변수의 배타적 **주변 분포(marginal distribution)** —즉, 개별 예측 변수 자체의 1인칭 분포—뿐만 아니라, 나아가 전체 예측 변수들의 **결합 분포(joint distribution)** —즉, 서로 다른 모든 각 예측 변수들 상호 간에 얽힌 복잡한 연관성(association)망 조작—까지 함께 고려하고 결합 연산해야 하기 때문입니다.

In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix.
다변량 정규 분포의 경우에는, 이러한 여러 다른 구 예측 변수들 간의 상호 복잡 연관성이 통상 공분산 행렬 체제 지표의 비대각선(off-diagonal) 요소들을 통하여 요약되어 대변됩니다.

However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate.
그러나 일반적인 보편 상황의 실전 현장에서는, 이러한 상호 연관성을 규명(characterize)하여 정의하는 것은 매우 난해할 수 있으며, 이를 추정하는 것은 대단히 과도하게 까다롭고(exceedingly challenging) 지난한 과제입니다.

But by assuming that the $p$ covariates are independent within each class, we completely eliminate the need to worry about the association between the $p$ predictors, because we have simply assumed that there is _no_ association between the predictors!
하지만 우리가 각 속한 클래스 내부에서 총 $p$개의 공변량(예측 변수들)이 모두 철저히 상호 독립적이라고 가정해 버림으로써, 우리는 이 골칫거리인 $p$개 예측 변수들 간의 연관성에 대해 조마조마 고민해야 할 필요성을 아예 통째로 원천 제거(completely eliminate)해 버릴 수 있습니다. 그 이유는 바로, 우리가 단순하게도 이 단서 변수들 간에 그 어떤 연관성도 아예 **"없다(no)"** 고 억지로 못 박는 가정을 내려 치부해 버렸기 때문입니다!

Do we really believe the naive Bayes assumption that the $p$ covariates are independent within each class?
그렇다면 우리는 정말로 각 특성 클래스 내부에서 $p$개의 공변량이 순수하게 상호 완전 독립적이라는 나이브 베이즈 장치의 순진무구한 이 억지 가정을 실전에서 믿는 것일까요?

In most settings, we do not.
대부분의 현실 구성 세팅 환경에서, 우리는 이것을 사실로 생각하지 않습니다.

But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where $n$ is not large enough relative to $p$ for us to effectively estimate the joint distribution of the predictors within each class.
그러나 비록 이 막무가내의 통계 모델링 가정이 오로지 연산의 편의성(convenience) 하나만을 도모하기 위해 억지로 강행 결단된 것일지라도, 이는 실전 현장에서 종종 꽤 준수하고 만족스러운(decent) 결과를 산출 이끌어냅니다. 특히 샘플 관측수 $n$이 다루어야 할 변수 개수 $p$에 견주어 거대 결합 연성 통계 분포를 적절히 추정 구성할 만큼 충분하게 확보 확보되지 않은 정보 부족의 세팅에서는 그 대안 수단 진가의 위력을 십분 발휘합니다.

In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings.
사실, 이러한 거대 결합 통계 분포 체제를 추정하여 세팅하는 작업 자체가 애초부터 굉장히 거대한 우량 물량의 많은 데이터를 필수 기본 자원으로 요구하므로, 상대적으로 단촐한 나이브 베이즈 처방 수법은 광범위한 다수의 세팅 현장 조건 안에서 좋은 실용적 선택지 옵션이(good choice) 될 수 있습니다.

Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.
본질을 통찰하자면, 나이브 베이즈의 이러한 극단 가설은 모델 예측 지표에 어쩔 수 없이 어느 정도의 시스템 결함 오판인 편향성(bias) 흠집을 강제 유도해 들여오지만, 반대 급부로 불량 리스크 예측의 변동 요소인 분산(variance) 지표는 철벽 방어 단속 축소시켜 낮춰주므로, '편향과 분산 상충(trade-off)' 투쟁 교환 관계의 전술적 결과로써 현실 데이터 실전(in practice) 평가 무대 위에서 매우 상당히 훌륭하게 작동하며 선방(works quite well)하는 준수 타점의 우수 분류 인공지능 기계 장치를 새롭게 이끌어 결과물로 제공해 도출해 내어 냅니다.

Once we have made the naive Bayes assumption, we can plug (4.29) into (4.15) to obtain an expression for the posterior probability,
일단 우리가 나이브 베이즈의 억지 독립 가정을 기꺼이 수용 채택 도입 체결하였다면, 아까의 식 (4.29) 요소 체제 덩어리를 바로 식 (4.15) 체계 수식 구조 안에 대입 삽입 융합(plug into)함으로써 우리는 다음과 같은 사후 확률 판정 점수 구조에 대한 새로운 표현 등식을 쉽게 도출 변조 재구성하여 파생 획득 산출해 낼 수 있습니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k \times f_{k1}(x_1) \times f_{k2}(x_2) \times \dots \times f_{kp}(x_p)}{\sum_{l=1}^{K} \pi_l \times f_{l1}(x_1) \times f_{l2}(x_2) \times \dots \times f_{lp}(x_p)} \quad (4.30)
$$

for $k = 1, \dots, K$.
(여기서 $k = 1, \dots, K$ 입니다.)

To estimate the one-dimensional density function $f_{kj}$ using training data, we have a few options:
현장의 획득 훈련 데이터를 투입 적용하여 저 분리 독립 쪼개진 각각의 개별 1차원 밀도 함수들 $f_{kj}$ 파츠 덩어리를 추정 측정 계산 구성하기 위해, 우리에게는 몇 가지의 대안 설정 옵션(options) 수단 카드들이 구비 마련되어 제공됩니다:

- If $X_j$ is quantitative, we can assume it follows a univariate normal distribution, $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$.
- 만약 $X_j$ 특성 단서 아이템 변수가 숫자 크기로 환산되는 양적 연속 척도 변수(quantitative) 부류라면, 우린 이 변수 녀석이 단순 단일 1차원 정규 산모양 분포(univariate normal distribution) 모형 규칙 규칙을 자연 따르고 띠게 된다고 가정할 수 있습니다, 즉 도출 수식으로는 $X_j \mid Y = k \sim N(\mu_{jk}, \sigma_{jk}^2)$ 꼴 형태에 복종한다고 단정 수식 결론지어 퉁쳐 볼 수 있습니다.
- Alternatively, we can use a non-parametric estimate like a histogram or a kernel density estimator.
- 대안적인(Alternatively) 다른 설정 타개책으로, 이런 가두기 정규 곡선 프레임 뼈대 제약에 가두지 않고 대신 히스토그램 박스나 커널 밀도 도면 추정 장치(kernel density estimator) 모형처럼 더 유연하게 맵을 파악 재는 비모수적 자유 추정(non-parametric estimate) 설계 공법 접근 기법 방식을 사용 차용해 세팅 돌려볼 수도 있습니다.
- If $X_j$ is qualitative, we simply count the proportion of training observations corresponding to each class instance.
- 마지막으로 만약 $X_j$ 타깃 단서 특징 아이템 변수가 숫자 메모 치수가 아니라 단지 편 가르기 부류 속성 라벨 포장 척도 기반의 범주/명목형 질적 변수(qualitative) 부류 판이라면, 우리는 머리 굴릴 것조차 없이 단순하게 각 클래스별 타깃 인스턴스(instance) 분류 현황 결과 명목에 순응 포함 대응(corresponding) 적중 소속되는 실제 캠프 훈련 관측치 인원 쪽수의 점유 비율(proportion) 총량 지표를 수기 산수 계산 단위 덧셈 뺄셈 세기로 단순 카운트 세서 도출 집계해 비율로 뽑아내 산출(count)만 해주면 그만입니다.

---

## Sub-Chapters

[< 4.4.3 Quadratic Discriminant Analysis](../4_4_3_quadratic_discriminant_analysis/trans1.html) | [4.5 A Comparison Of Classification Methods >](../../4_5_a_comparison_of_classification_methods/trans1.html)

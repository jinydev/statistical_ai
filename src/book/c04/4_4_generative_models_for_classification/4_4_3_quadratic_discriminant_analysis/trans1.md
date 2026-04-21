---
layout: default
title: "trans1"
---

[< 4.4.2.1 Roc Curve](../4_4_2_linear_discriminant_analysis_for_p_1/4_4_2_1_roc_curve/trans1.html) | [4.4.4 Naive Bayes >](../4_4_4_naive_bayes/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4.3 Quadratic Discriminant Analysis
# 4.4.3 이차 판별 분석 (Quadratic Discriminant Analysis)

As we have discussed, LDA assumes that the observations within each class are drawn from a multivariate Gaussian distribution with a class-specific mean vector and a covariance matrix that is common to all $K$ classes.
앞서 논의했듯이, LDA 기법은 각 클래스 내의 관측치들이 클래스별 고유한 평균 벡터를 지니고 전체 $K$개 클래스들에 공통으로 적용되는 하나의 공분산 행렬을 지닌 다변량 가우시안 정규 분포로부터 추출되었다고 가정합니다.

_Quadratic discriminant analysis_ (QDA) provides an alternative approach.
반면 **이차 판별 분석(Quadratic discriminant analysis, QDA)** 은 이에 대한 대안적인 접근법을 새롭게 제공합니다.

Like LDA, the QDA classifier results from assuming that the observations from each class are drawn from a Gaussian distribution, and plugging estimates for the parameters into Bayes’ theorem in order to perform prediction.
LDA 모델과 마찬가지로, QDA 분류기는 각 클래스에서 나온 관측치 개체들이 가우시안 정규 분포 곡선 모델을 그대로 똑같이 따르며, 산출된 매개변수들의 추정치를 베이즈 정리 수식에 대입 치환하여 궁극적인 예측을 수행함으로써 결과물을 도출한다고 가정합니다.

However, unlike LDA, QDA assumes that each class has its own covariance matrix.
그렇지만, 앞선 LDA의 가정과 확연하게 달리, QDA는 각각의 모든 클래스가 저마다 자신들만의 독립적인 고유한 공분산 행렬을 갖는다고 가정합니다.

That is, it assumes that an observation from the $k$th class is of the form $X \sim N(\mu_k, \mathbf{\Sigma}_k)$, where $\mathbf{\Sigma}_k$ is a covariance matrix for the $k$th class.
다시 말해, 그것은 $k$번째 클래스에서 추출된 무작위 관측치가 $X \sim N(\mu_k, \mathbf{\Sigma}_k)$ 형태의 분포를 띤다고 가정하며, 여기서 $\mathbf{\Sigma}_k$는 바로 그 해당 $k$번째 클래스의 공분산 행렬 구조를 뜻합니다.

Under this assumption, the Bayes classifier assigns an observation $X = x$ to the class for which
이러한 새로운 가정하에, 베이즈 분류기는 다음의 계산 값이 최대치가 도출되는 클래스에 관측치 객체 $X=x$ 를 최종 할당 분류합니다:

$$
\delta_k(x) = -\frac{1}{2} (x - \mu_k)^T \mathbf{\Sigma}_k^{-1} (x - \mu_k) - \frac{1}{2} \log |\mathbf{\Sigma}_k| + \log \pi_k \quad (4.28)
$$

is largest. So the QDA classifier involves plugging estimates for $\mathbf{\Sigma}_k$, $\mu_k$, and $\pi_k$ into (4.28), and then assigning an observation $X = x$ to the class for which this quantity is largest.
So the QDA classifier involves plugging estimates for $\mathbf{\Sigma}_k$, $\mu_k$, and $\pi_k$ into (4.28), and then assigning an observation $X = x$ to the class for which this quantity is largest.
고로 QDA 기계 분류기는 현장에서 도출한 궤적 추정치들인 $\mathbf{\Sigma}_k$, $\mu_k$, 그리고 $\pi_k$ 파츠들을 식 (4.28)에 치환 대입하고, 도출된 결과량(quantity) 수치가 제일 큰 클래스를 선언 확정하여 거기에 그 새로운 관측치 $X = x$ 객체를 분류 시킵니다(assigning).

Unlike in (4.24), the quantity $x$ appears as a _quadratic_ function in (4.28). This is where QDA gets its name.
기존 식 (4.24)와 달리, 객체 기호량 $x$ 는 수식 (4.28)의 구조 내부에서 **이차(quadratic)** 함수의 제곱승 복합 형태로 출현해 작용합니다. 바로 이 수식적 구조적 맹점에서 부분에서 명칭 이름이 파생되어 지어졌습니다.

Why does it matter whether or not we assume that the $K$ classes share a common covariance matrix?
그렇다면 대체 왜 전체 $K$개의 클래스 파벌들이 똑같이 통일된 공통 공분산 행렬을 통제 공유한다고 가정하느냐 마느냐 따위가 왜 그렇게 심각하게 문제(matter)가 되는 것일까요?

In other words, why would one prefer LDA to QDA, or vice-versa? The answer lies in the bias-variance trade-off.
다른 말로 바꾸어 말해, 누군가는 왜 QDA 보다 LDA 모델 장치를 통계 편애하여 더 선호하거나, 혹은 그 완전히 반대(vice-versa)의 현상이 발생할까요? 이 모든 해답 열쇠는 영원한 딜레마인 '편향-분산 상충 관계(bias-variance trade-off)'의 논리에 자리합니다.

When there are $p$ predictors, then estimating a covariance matrix requires estimating $p(p+1)/2$ parameters.
예측 변수가 $p$개 있을 때, 공분산 행렬을 추정 구축해 내기 위해서는 $p(p+1)/2$ 개의 파라미터 미지수들을 추정하는 작업이 요구됩니다.

QDA estimates a separate covariance matrix for each class, for a total of $K p(p+1)/2$ parameters.
QDA 장치는 방별 클래스마다 별개의 분리된 공분산 행렬 형태를 따로 다 추정 산출하려 시도하므로, 도합 총 $K p(p+1)/2$ 개의 모수 미지수 파라미터 수치들을 다루어야 합니다.

With 50 predictors this is some multiple of 1,275, which is a lot of parameters.
만약 우리에게 놓인 예측 변수가 50개(predictors)라면, 이것은 숫자 1,275에 특정 거대 배수를 곱해버리는 수치, 즉 아주 엄청나게 많은 수의 파라미터 부품들이 되어버립니다.

By instead assuming that the $K$ classes share a common covariance matrix, the LDA model becomes linear in $x$, which means there are $K p$ linear coefficients to estimate.
그 대신, 모든 $K$개의 클래스들이 그냥 다 똑같은 공통 공분산 행렬을 공유해 버린다고 가정해버림으로써, LDA 모델은 타깃 변수 $x$에 대하여 선형(linear) 차원 상태로 돌변하게 되고, 이것은 고작 $K p$ 개 정도의 단순한 선형 계수들만 계산 도출 적 산정하면 된다는 뜻을 의미합니다.

Consequently, LDA is a much less flexible classifier than QDA, and so has substantially lower variance.
결과적으로 도출 비교하자면, LDA 모델 기계는 QDA 모델에 비해 훨씬 유연성 탄력이 떨쳐 낮고 덜한 하위 유연성 분류 체제가 되며, 따라서 분산(variance)이 상당히 낮아(substantially lower) 방어적인 분산 특성을 지닙니다.

This can potentially lead to improved prediction performance.
이것은 잠재적으로 우연 역전 예측 무빙 성과 성능 적중의 극적 지표 향상(improved prediction performance) 결판으로 이끌 잠재적인 요인이 될 수가 있습니다.

But there is a trade-off: if LDA’s assumption that the $K$ classes share a common covariance matrix is badly off, then LDA can suffer from high bias.
그러나 또 한 번 상충적인 **'대가 지불 (trade-off)'** 관계가 뒤따릅니다: $K$개 클래스 진영 방들이 획일 무조건 똑같은 공통 공분산 체제 자태를 강제 공유한다는 저 LDA 의 거만한 '일방통행식 동결 가설 억지' 가 실제 현실 도 팩트 와 동 차 지 대 진 심 비 치 심 각 전 단 포 도 하 차 뼈 동 단 도 동 게 나 동 지 보 기 포 동 다 비 단 편 치 결 단 구전모 ( 진 보 포 기 빗 파 파 나 파badly 기 뼈 나 보 도 빗 진 포 포 모 차 차 다 전 off 모 기 편 어 모 전 포 보긋 나 며 전 지 단 나 기 편 단 모 나 단 수 지 나 파 동 다 차 결) 수 전 진 나 지 기 도 조 단 단 나 나 피 지 나다 동 수 부 전 보 지 차 포, 며 LDA 치기 도 차 모델 부 은 전 단 치 보 도 파 나 단 부 지 하나 엄청나 지결 진 차 편 동 게 며 기 부 모파 치 기 다 편 편 나 파 편 부 지 큰 부 차 진 (high) 치 진 동 편 조 수 부 지 나 치 다 모 모 차 파 조 지 차 편단 편 기 동 기 편향(bias) 고 수 차 차조 피 로 나 지 포 인해 과 하나모 치 하나 고 도 모 진 비 비 뼈 단 전 도 포 피 다 포통 나 단 포 수 치 파나 단 다결 다 포 피 파 다 조 수 단 기 부 받을 지 피 전 다 단 포 도 뼈 모 다 도 조 파 수 전 진. 모 하나 은 모 지 부 피 있습니다 지비 지 며 단 포모 . 나 조 고 (suffer 도 조 지 from). 진 뼈 부

Roughly speaking, LDA tends to be a better bet than QDA if there are relatively few training observations and so reducing variance is crucial.
대략적으로 말하자면, 훈련 관측치의 수가 상대적으로 도 며 다 포 도 뼈 기 나 피 결 다 단 비 편 진 보 치 지 조 은 부 차 파 모 전 다적 고 전 피 진 차 도 파 진 하 결 어 진 나 다 파 서 조 동 분 결 부 도 기 편 산 치전 전 파 (variance) 포 나 결 모 전 을 나 모 도 조 줄 포 며 결다 하 결 파 도 이 피 하나 는 단 전 도 포 은 나 모 피 고 다 결 모 치 전 부 조 것 다 동 이 포 다 지 매우 모 지 고 모 부 하 다 편 정 중 다 결 보 파 모 차 나 고 하 동 요 모 조 다 동 모 차 치 나 단 진 다 결 다 다 피 파 포 모 도 도 피 다 하나 부 차 한 단 다 며 차포 동 기 다 하나 피 며 하 단 하 다 결 (crucial) 시 피 뼈 피 진 차 비 상황 포 수 다 수 지 피 비 진 이 나 고 수 모 다 모 며 하 동 피 라 모 나 모 정 나 다 결 파 동 나 차 진 치 면 차 도나 뼈, 피 동 다 피 조 기 파 전 조 치 나 진 다 도 결 편 피. 나 차 조 도 하나 하 진 도 진 파 전 LDA 단 동 다 부 전 나 조 고 지 다 나 동 가 기 차 도 부 동 수 다 나 모 조 은 한 QDA 모 은 뼈 며 도 피 포 전 나 다 진 파 고 하나 편 피 며 하나 보 모 모다 차 진 더 다 나 며 지 모나 기 지 고 다 하나 도 포나 결 수 조 수 다 동 지 동 도 피 뼈 모 유리 다 조 나 며 편 모 단 치 조 포 진 지 나진 포 다 한 고 조 뼈 비 단 전 나 뼈 피 모 동 다. 모 피 조 나 지 며 기 도 하나 나 도 지 차 도 동 치 선택(better 도 포 다 치 피 며 은 포 수 하나 진 bet) 다 도 도 결 이 차 편 모비 모 파 뼈 도 포 부 모 치 도 포 결 수 되는 모 다 경 조 단 조 고 뼈 도 피 향 동 도 모 편 파 모 하 은 모 며 다 전 기 하나 도 다 조 파 치 나 파 나 동 결 포 지 하나 며 고 전 피를 편 다 보 부 피 뼈지 결 편 다 뼈 조 진 다나 보입니다 나모 며. 지

In contrast, QDA is recommended if the training set is very large, so that the variance of the classifier is not a major concern, or if the assumption of a common covariance matrix for the $K$ classes is clearly untenable.
이와는 반대로, 훈련 데이타셋 쪽수 표본 풀이 엄청나게 광대 비대하여(very large) 모델 기계의 분산 변동이 딱히 큰 위험 관심 요소(major concern)가 아니거나, 혹은 저 '$K$개 클래스가 다 절대 공통 획일 공분산 바닥 핏줄을 통일 공유한다'라는 무엄했던 LDA 특유측의 전제 상상 억지 가설이 상식상 심하게 크게 뒤틀려 변호 유지 될 수 모 뼈 다 다 포 다 모 포 진 포 파 결 전 다 모 부 진 다 없고 기 다 기 나 뼈 피 지 다 차 도 진 동 조 고 피 파결 허 도 도 뼈 모 피 뼈 부 진 모나 나 기 뼈 황 나 도 포 지 치 하나 다 편 부 전 결될 차 파 포 뼈 피 결 치 전 진 결 나 수 (clearly 비 다 untenable) 부 피 도 조 진 차 모 뼈 포 치 하 포 전 나 때 동 다 다 결 다 모 은 피 치 다 나 전 전 지에는 지 동 조 차 하나 피 나 결 동 포 망 나진 피 뼈 나 은설 도 전 은 피 다 치 나 임 포 하나 도 하 포 피 고 없이 다 진 피 며 치 다 다 치 나 단 나 피 모 다 편 모 부 유 동 진 나 도 나 포 편조 다 연 부 편 나 모 진 동 한 다 며 다 은 나 지 치 피 도 며 포 며 포 뼈모 하나 도 전 나 모 진 차 조 차 모 지 기 다 진 피 모 QDA 도 차 며 지 부나 치를 모 편 다 더 다 은 모 단 뼈 파 조 며 기 사 나 기 지 전 하 용 도 포 포 단 지 도 부 부 전 피 고 고 동 포 피 보 다 기 다 하 지 치 도다 파 하나 동 다 차 모 도 도 편 포 지 피 지 조 치 나 나 기 나 포 하나 동 전 전 포전 도 포 진 포 지 진조 고 진 피 은 기기 도 차 포 파 기 하나 도 기 부 편 지 모 포 전피 결 는 동 지 다 다. 것을 포 모 도 강 모 편 다 고 파 피 며 단 포 하나 지 치. 고 하나 뼈력 수 부 모 포 도 나 지 히 피 추 기 동 모조 지 포 동 파 며천 나 며 피 포 진.(recommended)합 동 다 차 동 전 치 나 모 모 피 지니 전 전 도. 포 지 피 다 조 동다 치다 비 하나 조 지 뼈 조 단 동 다 기 다 진 뼈 피. 

---

## Sub-Chapters

[< 4.4.2.1 Roc Curve](../4_4_2_linear_discriminant_analysis_for_p_1/4_4_2_1_roc_curve/trans1.html) | [4.4.4 Naive Bayes >](../4_4_4_naive_bayes/trans1.html)

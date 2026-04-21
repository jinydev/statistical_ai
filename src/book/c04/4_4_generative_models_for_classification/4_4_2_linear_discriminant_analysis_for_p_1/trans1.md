---
layout: default
title: "trans1"
---

[< 4.4.1 Linear Discriminant Analysis For P 1](../4_4_1_linear_discriminant_analysis_for_p_1/trans1.html) | [4.4.2.1 Roc Curve >](4_4_2_1_roc_curve/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4.2 Linear Discriminant Analysis for p > 1
# 4.4.2 p > 1인 다중 예측 변수에 대한 선형 판별 분석

We now extend the LDA classifier to the case of multiple predictors.
우리는 이제 다중 예측 변수가 있는 경우로 LDA 분류기를 확장합니다.

To do this, we will assume that $X = (X_1, X_2, \dots, X_p)$ is drawn from a _multivariate Gaussian_ (or multivariate normal) distribution, with a class-specific multivariate mean vector and a common covariance matrix.
이를 수행하기 위해, 우리는 $X = (X_1, X_2, \dots, X_p)$가 클래스별 다변량 평균 벡터와 공통 공분산 행렬을 가지는 **다변량 가우시안(multivariate Gaussian)** (또는 다변량 정규) 분포로부터 추출되었다고 가정할 것입니다.

We begin with a brief review of this multivariate Gaussian distribution.
먼저 이 다변량 가우시안 분포에 대한 간략한 복습부터 시작해 보겠습니다.

The multivariate Gaussian distribution assumes that each individual predictor follows a one-dimensional normal distribution, as in (4.16), with some correlation between each pair of predictors.
다변량 가우시안 분포는 (4.16)에서와 같이 각각의 개별 예측 변수들이 예측 변수 쌍 간에 약간의 상관관계를 가지면서 형태상 1차원 정규 분포를 따른다고 가정합니다.

Two examples of multivariate Gaussian distributions with $p=2$ are shown in Figure 4.5.
$p=2$인 다변량 가우시안 분포의 두 가지 예시 창이 그림 4.5에 나타나 있습니다.

The height of the surface at any particular point represents the probability that both $X_1$ and $X_2$ fall in a small region around that point.
어떤 특정 지점에서의 표면의 높이는 $X_1$과 $X_2$가 모두 그 지점 주변의 작은 영역 안으로 떨어질 확률을 나타냅니다.

In either panel, if the surface is cut along the $X_1$ axis or along the $X_2$ axis, the resulting cross-section will have the shape of a one-dimensional normal distribution.
어느 패널에서든 간에, 표면을 $X_1$ 축을 따라 자르거나 $X_2$ 축을 따라 자른다면 그 결과물인 단면은 동일하게 1차원 정규 분포의 모양을 띨 것입니다.

The left-hand panel of Figure 4.5 illustrates an example in which $\text{Var}(X_1) = \text{Var}(X_2)$ and $\text{Cor}(X_1, X_2) = 0$; this surface has a characteristic _bell shape_.
그림 4.5의 왼쪽 패널은 $\text{Var}(X_1) = \text{Var}(X_2)$이고 $\text{Cor}(X_1, X_2) = 0$인 경우의 예시를 보여줍니다; 이 표면은 특징적인 **종 모양(bell shape)** 을 지닙니다.

However, the bell shape will be distorted if the predictors are correlated or have unequal variances, as is illustrated in the right-hand panel of Figure 4.5.
그러나 만약 예측 변수들이 상관되어 있거나 분산이 서로 다를 경우, 그림 4.5의 오른쪽 패널에 설명된 것처럼 종 모양은 일그러질 것입니다.

In this situation, the base of the bell will have an elliptical, rather than circular, shape.
이 상황에서, 종 모양의 바닥 밑면은 원형이라기보다는 타원형(elliptical)의 모양을 갖게 될 것입니다.

To indicate that a $p$-dimensional random variable $X$ has a multivariate Gaussian distribution, we write $X \sim N(\mu, \Sigma)$.
$p$-차원 인 확률 변수 $X$가 다변량 가우시안 분포를 따른다는 것을 나타내기 위해, 우리는 식을 $X \sim N(\mu, \Sigma)$라고 적습니다.

Here $E(X) = \mu$ is the mean of $X$ (a vector with $p$ components), and $\text{Cov}(X) = \Sigma$ is the $p \times p$ covariance matrix of $X$.
여기서 $E(X) = \mu$는 $X$의 평균($p$개의 성분을 지닌 벡터)이며, $\text{Cov}(X) = \Sigma$는 $X$의 $p \times p$ 공분산 행렬(covariance matrix)입니다.

Formally, the multivariate Gaussian density is defined as
공식적으로, 다변량 가우시안 밀도 함수는 다음과 같이 정의됩니다:

$$
f(x) = \frac{1}{(2\pi)^{p/2} |\Sigma|^{1/2}} \exp \left( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu) \right) \quad (4.23)
$$

In the case of $p > 1$ predictors, the LDA classifier assumes that the observations in the $k$th class are drawn from a multivariate Gaussian distribution $N(\mu_k, \Sigma)$, where $\mu_k$ is a class-specific mean vector, and $\Sigma$ is a covariance matrix that is common to all $K$ classes.
$p > 1$개의 예측 변수들이 존재하는 경우, LDA 분류기는 $k$번째 클래스의 관측치들이 다변량 정규 분포 $N(\mu_k, \Sigma)$로부터 추출되었다고 가정합니다. 여기서 $\mu_k$는 클래스별 고유한 평균 벡터이고, $\Sigma$는 모든 $K$개의 클래스에 공통적으로 쓰이는 공분산 행렬입니다.

Plugging the density function for the $k$th class, $f_k(X = x)$, into (4.15) and performing a little bit of algebra reveals that the Bayes classifier assigns an observation $X = x$ to the class for which
$k$번째 클래스에 해당하는 밀도 함수 $f_k(X = x)$를 수식 (4.15)에 대입하고 약간의 대수적인 연산을 수행해 보면 베이즈 분류기가 다음 수식이 가장 큰 값을 도출하는 클래스에 관측치 $X = x$를 할당한다는 사실이 드러납니다:

$$
\delta_k(x) = x^T \Sigma^{-1} \mu_k - \frac{1}{2} \mu_k^T \Sigma^{-1} \mu_k + \log(\pi_k) \quad (4.24)
$$

is largest. This is the vector/matrix version of (4.18).
(마지막 문장과 결합) 이것은 식 (4.18)의 벡터/행렬 버전입니다.

![Figure 4.6](./img/4_6.png)

**FIGURE 4.6.** _An example with three classes. The observations from each class are drawn from a multivariate Gaussian distribution with p = 2, with a class-specific mean vector and a common covariance matrix._ Left: _Ellipses that contain 95 % of the probability for each of the three classes are shown. The dashed lines are the Bayes decision boundaries._ Right: _20 observations were generated from each class, and the corresponding LDA decision boundaries are indicated using solid black lines. The Bayes decision boundaries are once again shown as dashed lines._
**그림 4.6.** 세 개의 집단 클래스가 있는 한 가지 예시. 각 클래스의 관측치들은 클래스별 고유 평균 벡터와 전체 공통 공분산 행렬을 지닌 채 $p = 2$인 다변량 가우시안 정규 분포로부터 추출되었습니다. 왼쪽: 세 개의 각 클래스에 대해 95% 확률을 담고 있는 타원 윤곽선들이 표시되어 있습니다. 점선들은 베이즈 결정 경계선입니다. 오른쪽: 각 클래스에서 20개의 표본 관측치가 무작위로 생성되었고, 이에 대응하는 LDA 결정 경계선이 굵은 검정 직선(solid black lines)으로 표시되었습니다. 한편 베이즈 결정 경계는 점선으로 다시 한번 표시되어 나란히 나타납니다.

An example is shown in the left-hand panel of Figure 4.6. Three equally sized Gaussian classes are shown with class-specific mean vectors and a common covariance matrix.
한 가지 좋은 예시가 그림 4.6의 왼쪽 패널에 나와 있습니다. 같은 확률로 배정된 동등한 크기의 세 개 가우시안 집단들이 자신만의 클래스별 평균 벡터와 하나로 통일된 공통 공유 공분산 행렬로 묶여 보여지고 있습니다.

The three ellipses represent regions that contain 95% of the probability for each of the three classes. The dashed lines are the Bayes decision boundaries.
이 세 개의 타원 궤적은 3가지 분포 구역 각자의 클래스 확률이 95% 담겨있는 밀도 지역의 한계를 나타냅니다. 그려진 점선 라인들은 베이즈 결정 경계(Bayes decision boundaries)입니다.

In other words, they represent the set of values $x$ for which $\delta_k(x) = \delta_l(x)$; i.e.
다시 바꿔 말해서, 이 선들은 $\delta_k(x) = \delta_l(x)$가 팽팽하게 성립하는 $x$ 값들의 자취 집합을 대변합니다; 다시 말해:

$$
x^T \Sigma^{-1} \mu_k - \frac{1}{2} \mu_k^T \Sigma^{-1} \mu_k = x^T \Sigma^{-1} \mu_l - \frac{1}{2} \mu_l^T \Sigma^{-1} \mu_l \quad (4.25)
$$

for $k \neq l$.
(식 4.25)는 서로 다른 무리 $k$와 $l$에 대해 적용됩니다.

(The $\log(\pi_k)$ term from (4.24) has disappeared because each of the three classes has the same number of training observations; i.e. $\pi_k$ is the same for each class.)
(식 4.24에서 곁가지로 붙어있던 $\log(\pi_k)$ 항은 3개 집단들이 훈련 훈련데이터로 동일 비율을 가지고 있기 때문에 뺄셈으로 상쇄되어 모조리 증발해 사라졌습니다; 즉, 각 집단의 $\pi_k$ 수치가 동일하기 때문입니다.) 

Note that there are three lines representing the Bayes decision boundaries because there are three _pairs of classes_ among the three classes.
참고로 3개의 집단 세계에서 발생 가능한 집단 조합 구성 수, 즉 세 가지 **집단 쌍(pairs of classes)** 이 있기 때문에 베이즈 결정 경계를 가르는 구분 라인선도 총 3개가 나타나게 된다는 점을 눈여겨보십시오.

That is, one Bayes decision boundary separates class 1 from class 2, one separates class 1 from class 3, and one separates class 2 from class 3.
다시 말해, 한 개의 베이즈 결정 칼날 경계선은 범주 1과 2를 쪼개 가르고, 또 다른 하나는 구역 1과 3을, 그리고 남은 하나는 2와 3 사이를 각각 쪼개어 가릅니다.

These three Bayes decision boundaries divide the predictor space into three regions. The Bayes classifier will classify an observation according to the region in which it is located.
이러한 세 개의 베이즈 결정 횡단 경계선들은 $x_1, x_2$ 측의 예측 공간들을 크게 3개의 고유한 파벌 영역(regions) 덩어리로 분할 파훼 해버립니다. 신의 베이즈 무적 분류 장치는 새 구슬 관측치가 결국 세 영역들 중 어느 지점 좌표 땅바닥에 떨어져 자리 매김(located) 위치하는지에 입각해 분류 선고를 최종적으로 내릴 것입니다.

Once again, we need to estimate the unknown parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\Sigma$; the formulas are similar to those used in the one-dimensional case, given in (4.20).
다시 한 번 지겨운 현실로 돌아오면, 우리는 $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, 그리고 $\Sigma$ 등의 숨겨진 이데아 파라미터 미지수 값들을 사람 손으로 어떻게든 추정 계산해 내야만 합니다; 이 위조 추정의 수학 도출 공식들은 1차원의 예전 환경, 주어진 식 (4.20)에서 사용되었던 판 형식과 구조가 굉장히 흡사합니다.

To assign a new observation $X = x$, LDA plugs these estimates into (4.24) to obtain quantities $\hat{\delta}_k(x)$, and classifies to the class for which $\hat{\delta}_k(x)$ is largest.
어떤 낯선 미지의 새로운 구슬 관측 데이터 $X=x$ 인자 개체를 결단시켜 할당하기 위해서, LDA 기법 모델 단속기는 구해진 이 가라 추정치들(Estimates)을 식 (4.24) 분수 공식에 냅다 욱여 대입하여 대체 모델 짝퉁 판별결과치인 환율 산물량 $\hat{\delta}_k(x)$ 을 얻어냅니다. 그런 다음 결론적으로 이 $\hat{\delta}_k(x)$ 평가값이 제일 최대 1등으로 가장 크게 솟구치는 해당 클래스를 가리켜 최종 관측 개체의 결과 행선지를 분류해 줍니다. 

Note that in (4.24) $\delta_k(x)$ is a linear function of $x$; that is, the LDA decision rule depends on $x$ only through a linear combination of its elements.
주의할 점은 식 (4.24)에서 수식 덩어리 판별 함수 $\delta_k(x)$ 구조를 까보면 미지의 주인공 $x$에 대한 순수한 **일차 선형 결합(linear function)** 에 지나지 않는다는 사실입니다; 다시 말해서 예측 기계 LDA 의 모든 감별 동작 의사결정 규칙 판결망은 결국 $x$의 구성 성분들의 지루할 정도로 단순한 더하기 곱하기의 합산 선형 조합(linear combination) 연산 틀에만 철저히 갇혀서 전적으로 의존 결단된다는 것입니다.

As previously discussed, this is the reason for the word _linear_ in LDA.
이전에 짚어 언급했듯이, 바로 이 핵심적인 연산 구조적 특징의 맹점이 정식 이름 LDA 에 _linear(선형적)_ 이라는 위풍당당한 간판 수식어가 내걸리게 된 진짜 원인입니다.

| | True default status | | |
|---|---|---|---|
| | No | Yes | Total |
| **Predicted default status** | | | |
| No | 9644 | 252 | 9896 |
| Yes | 23 | 81 | 104 |
| **Total** | 9667 | 333 | 10000 |

**TABLE 4.4.** _A confusion matrix compares the LDA predictions to the true default statuses for the 10,000 training observations in the_ `Default` _data set. Elements on the diagonal of the matrix represent individuals whose default statuses were correctly predicted, while off-diagonal elements represent individuals that were misclassified. LDA made incorrect predictions for 23 individuals who did not default and for 252 individuals who did default._
**표 4.4.** 오차 행렬(confusion matrix). 10,000개의 `Default` 훈련 데이터 기준, 머신의 LDA 예측 수치결과와 대상의 실제 진실된 파산 상태를 서로 상호 검증해 비교합니다. 메인 대각선(diagonal) 열 칸 행렬에 들어선 셀의 숫자 구성원들은 최종 부채 미상환 여부가 기계에 의해 참으로 올바르게 제대로 맞물려 예측 적중 감별된 개체들입니다. 반면 역 대각선 격자선(off-diagonal) 바깥에 분포 속하여 튕겨나간 결과 치수는 엉뚱하게 오분류된 인간 표본 수 집단을 나타냅니다. 이 결과에서, LDA 머신은 기동 검거 상, 무서운 오분류 오판(파산 미납을 하지 않는 착한 사람 23명 그리고 당당히 미납을 저지르고 잠적했지만 패스해버린 빌런 252 명에 대해)을 저질렀습니다.

In the right-hand panel of Figure 4.6, 20 observations drawn from each of the three classes are displayed, and the resulting LDA decision boundaries are shown as solid black lines.
그림 4.6의 오른쪽 구역 패널 측면에는, 각 진영 집단 3개 타깃 구역에서 무작위 발췌 기입해 끌어온 각 20 놈씩의 표본 관측 구슬 객체들이 전시되어 뿌려집니다. 그리고 이 구질구질한 불과 몇 개의 표본 훈련 데이터 결괏값만으로 그려 구동해 낸 LDA 선형 판별 기계의 실제 결정 라인들이 무뚝뚝하고 거친 굵은 **단색 실선 흑선(solid black lines)** 들로 교차해 도출 그어져 나옵니다.

Overall, the LDA decision boundaries are pretty close to the Bayes decision boundaries, shown again as dashed lines.
얼추 큰 전체적인 면모 틀을 짚어보면, 이 인간의 머신이 그려낸 투박한 LDA 결정 굴곡 선분은 뒤쪽에 투명하게 참고용으로 다시 똑같이 병치된 투영된 이상적 신의 잣대 즉, 베이즈 분류 기표 **점선(dashed lines)** 축에 상당히 흡사하게 밀착하여 전반적으로 꽤 가깝게 그어져 나란히 동기화되어 도달해 있습니다.

The test error rates for the Bayes and LDA classifiers are 0.0746 and 0.0770, respectively. This indicates that LDA is performing well on this data.
양쪽 적중 분류 기계들의 최종 평가 고사의 테스트 평가 오류율(test error rates) 스코어 검증 결과를 내면 베이즈 기계 점수는 0.0746, 그리고 우리 추정 모델 인간의 기계 LDA 점수는 0.0770을 각기 산출해 기록했습니다. 이것은 이 데이터 환경 실적 구역에서만큼은 LDA 모델 방식이 상당히 양호한 오류폭 안에서 매우 원활히 아주 잘 동작 판단해 적중 업무를 수행하고 있다는 사실을 단적으로 가리켜(indicates) 보여주는 방증입니다.

We can perform LDA on the `Default` data in order to predict whether or not an individual will default on the basis of credit card balance and student status. [4]
우리는 `Default` 실습 데이터 판을 대상으로, 어떤 무명 개인이 카드 장부 빚 항목 크기와 특성상 학생 등급이라는 스펙 상태, 이렇게 2가지를 기초 토대 단서 삼아 미래에 무단 잠적 체납(Default)의 전과 구렁텅이에 빠질지 결백할지 여부를 모조리 예측해 판별하고자 진정한 LDA 투기 가동 모델 기계를 작동시켜 통계 실전에 직접 수술 투입 구동해 볼 수 있습니다. [4]

The LDA model fit to the 10,000 training samples results in a _training_ error rate of 2.75%. This sounds like a low error rate, but two caveats must be noted.
전체 총 1만 명 규모의 엄청난 훈련 샘플 관측치로 꽉꽉 집어넣어서 피팅 학습 동기화시킨 LDA 무장 모델의 결과 성적표는, **훈련(training)** 단계 오차율 점수가 전체에서 고작 2.75%로 떨어지며 멋지게 통과합니다. 언뜻 이렇게 귀로 조명해 들으면 전면 오류 실패 실책 확률이 엄청나게 낮고 무결 환상에 가깝게 성립한 것 같이 달콤하게 인지되는 현상이지만, 다음 2가지의 치명적인 함정 맹점 통계 교란 요인 주의(caveats) 사항들에 관해 무조건 짚고 유념해야만 합니다:

- First of all, training error rates will usually be lower than test error rates, which are the real quantity of interest.
- 첫째, 일반적으로 **'훈련 에러율'** 이라는 녀석은 우리가 정말 피를 말리며 진짜 알고 싶어 하는 진짜배기이자 미지의 산단 관측인 **'테스트 에러율'** 보다 보통 항상 치사하게 훨씬 더 낮게 측정 조작되는 사기성 경향이 높습니다.

- In other words, we might expect this classifier to perform worse if we use it to predict whether or not a new set of individuals will default.
- 다른 말로 바꿔 말하면, 우리가 이렇게 신나서 만든 분류기를 들고 전혀 훈련받지 않은 일면식도 없는 생전 낯선 고객 집단 놈들에게 부도 파산 적중 여부를 예측하려 실전 배치해서 구동 돌려보면, 처음 시험공부 연습문제 풀던 때의 성적(오차 2.75%)보다 훨씬 더 형편없이 박살 나고 더 나쁜 오판 성적표를 보일 것이라 짐작 기대해야 한다는 뜻입니다.

- The reason is that we specifically adjust the parameters of our model to do well on the training data.
- 그 지독한 이유인즉슨, 우리가 애초에 우리 모델 기계 장치의 톱니바퀴 조율 버튼인 파라미터 조각들을 세팅 매만질 때 거시적으로 오로지 '단지 눈앞에 던져 준 그 훈련 데이터 연습 문제판 안에서만' 극강의 1등 점수 정답을 제일 잘 맞추어 통과하도록 의도적으로 극단적 맞춤 조정 튜닝을 해버렸기 때문입니다. 

- The higher the ratio of parameters $p$ to number of samples $n$, the more we expect this _overfitting_ to play a role.
- 이 과몰입 훈련 집중의 편파가 가져오는, 동원 관측 표본 갯수 $n$ 크기에 대비해서 기계 안에 장착 조립된 매개 변수 부품($p$)이 뚱뚱하고 많으면 많을수록 상대 수치의 비율이 커지는 꼴인데, 이러면 이럴수록 조 기만이 가중되며 이 이른바 **과적합(overfitting)** 증후군 현상 질병이 실전 평가장에서 훨씬 더 심각하고 악독한 거대 역할 영향을 발휘하며 맹위를 떨칠 것임을 강하게 염려해야 합니다.

- For these data we don’t expect this to be a problem, since $p = 2$ and $n = 10,000$.
- 다행스럽게도, 이 `Default` 구동 데이터 타깃 현상판을 가지고 놀 때는 이 끔찍한 조작 과적합 함정 병이 큰 암초나 장애 문제로 불거질 거라 긴장 기대하지는 않습니다. 왜냐하면 단서로 쓰인 부품 $p=2$ 개라는 조촐한 기동 장비 파츠임에도 불구하고 기둥이 되는 훈련 관측 기초 밑바탕 모집 표본은 무려 $n=10,000$명이나 되는 넉넉하고 압도적인 엄청난 물량을 기초 자재로 이미 든든히 확보해 버렸기 때문입니다.

- Second, since only 3.33% of the individuals in the training sample defaulted, a simple but useless classifier that always predicts that an individual will not default, regardless of his or her credit card balance and student status, will result in an error rate of 3.33%.
- 둘째, 애초에 훈련생 1만 명 집단 내부 수치 생태 환경계에서, 진짜배기 미납으로 구천을 떠도는 진성 부도 파산 인간 파벌 전과 비율 스펙은 통계적으로 고작 $3.33\%$ 밖에 안 되는 매우 처참하고 희귀한 종자 소수파 분포 밀도의 존재이기 때문입니다. 이런 터무니없이 안전한 구멍 풀장에서 기계를 돌린다면, 애초에 구동 기계를 비싼 수학 돌려 만들 필요도 없이 멍청하지만 그냥 무조건 맹목적인 단순 무결 판별 기계("어떤 고객이 오든, 그놈 통장 빚 잔고 기표 수치나 그놈이 불 알바 뛰는 가난 학생인지 아닌지 따위 귀찮으니 안 볼 거야! 통과! 이 사람은 평생 아무도 전부 다 파산 안 할 착한 사람 구역 등급이다!") 선포를 매 놈에게 때려버리는 기계조차도 불과 $3.33\%$ 의 오답률 타격을 입는 아주 양호한 성적 방어를 한다는 무시무시한 사실입니다!

- In other words, the trivial _null_ classifier will achieve an error rate that is only a bit higher than the LDA training set error rate.
- 다른 말로 퉁쳐보면, 이런 멍청하고 아무 의미 맹목 부재 투기 조작 없는 흔해 빠진 **영(null)** 분류기조차도 우리 통계학 박사들이 발명한 조작 천재 LDA 기동 훈련 모델로 얻어낸 훈련판 시험 성적 오류보다 고작 불과 티끌 콩알만큼 조금 더 높은 에러율 점수에 무리 없이 가볍게 봉착 성취 정립해 도달한다는 아주 참담한 아이러니 구멍입니다.

In practice, a binary classifier such as this one can make two types of errors: it can incorrectly assign an individual who defaults to the _no default_ category, or it can incorrectly assign an individual who does not default to the _default_ category.
실제 현실 세계에서 구동 지시될 때, 위와 같은 기이한 '이진(두 가지 선악 판별)' 분류기 무단 맹목 시스템은 보통 상황에서 크게 두 종류 형태의 치명적인 대분류 악질 오분류 실수 조치 부류 그룹 종류들을 파생해 기표 번복 범할 수 배양 있습니다: 진짜 사기꾼 도주 빚 파산 불량(default) 범벅인 사람을 멀쩡한 결백 방면 **'미 파산(no default)'** 룸 칸에 무죄로 속여 잘못 던져 놔 할당 오류를 범하거나, 아니면 성실 만기 상환 중인 아무 죄도 없는 무고한 시민을 무통 파산 불량 진단자용 격리 **'파산 진상(default)'** 룸 깜방에 억울 범죄 표지로 무고 잘못 할당 판결 포진하는 경우입니다.

It is often of interest to determine which of these two types of errors are being made.
이때 우리의 최고 탐구 초점과 최대 관심사는 방금 돌아간 이 분류기 모델 기계 녀석 체계가 저 둘 중 과연 어느 쪽 악질 에러를 더 조밀 조밀 많이 집중해 지겹게 낳아 사고를 번복 치고 있는지 부류 원인을 세밀 검거 확인 판단 결정하는(determine) 지표 척도입니다.

A _confusion matrix_, shown for the `Default` data in Table 4.4, is a convenient way to display this information.
표 4.4의 `Default` 데이터 안에서 저 양방향 에러 분류 충돌의 진기한 실상 조작을 아주 기발하고 솔직 단면 편리한 조각 창틀 방식으로 적적히 다 펼쳐 까발려 표기해주는 저 마법 도표 화면 양식이 그 유명한 **혼동 행렬(confusion matrix)** 기표 표식판입니다. 

The table reveals that LDA predicted that a total of 104 people would default. Of these people, 81 actually defaulted and 23 did not.
모형의 기표 단면 행렬 판별 정보 도표 내용표를 뜯어보면 참 기막힌 내막 정보가 적나라 도출 드러나 밝혀집니다. 표에 따르면, 무조건 LDA 심판 분류 장치 팀은 만 명의 거대 인력 총 검거 인원 심판 중 구석 수사 도출 달랑 104명 족집게 녀석들에게만 "넌 구제불능! 곧 파산(default) 잠적 터진다!"라고 강제 타깃 지목 구형 예측 선포를 단행했습니다. 조사 결과 까보니 이 사형 지목 104명 인원 표본 중에서, 진짜 찐으로 현실 깡통 무단 실제 파산 터진 빌런 불량 신용자 도주 놈들은 달랑 81명뿐이었고, 나머지 오합 23명은 그냥 멀쩡 착한 오발탄 억울 선량 누명 녀석 백성들이었습니다. 

Hence only 23 out of 9,667 of the individuals who did not default were incorrectly labeled. This looks like a pretty low error rate!
결론을 짜맞춰 보면, 결국 안 갚고 다달이 빚 갚는 착한 통계상 9,667명의 절대다수 집단 내에서 불과 단지 23명의 인간만이 구속 저 지명 타깃 머신 기표 지표 판별 오류로 오발 할당 꼬리표(labeled) 오판 낙인 찍혀 분류된 셈입니다. 

However, of the 333 individuals who defaulted, 252 (or 75.7%) were missed by LDA.
하지만 막상 진짜 뒤집어진 반전의 참혹 진실 오분류 치명 에러 불량률 사태 조작 부문 오류 조각 이면 탐지 부실 치명률 성패 평판 진단은 통계 수치 등 반대 급부 쪽 전단에 집중 포진 존재 터져 있었습니다! 막상 현실에서 구실 통장에 완전 찢어져 빵꾸 나 무단 파산 비명횡사 잠적 도주를 결단 실행한 진짜 오리지널 **실 파산 전과 진성 빌런 도주 333명**을 대상 진위 분류 심판 기준으로 놓고 파 잣대 뜯어 집중 탐구 해부 분석해 봤더니, 통계 기표 조작 세상에, 그중 무려 **252명 기표 (전체 환산 75.7% 육박 통계 수치 기표 조각!)** 이나 되는 어마 무시한 다수 머릿 개체 불량 빌런 무리 타깃 파벌들을 우리 똑똑 최정예라고 호언 망상 착각 포진 추앙했던 스마트 머신 LDA 인공 수사 요원이 완전 바보 눈뜬장님 마냥 병신 멍청 허술 감각 무장 무능하게 "패스! 넌 괜찮은 우수 자본가 패스 등급!" 하고 치명 환상 판정 방면 유기 흘려 눈 감고 다 줄줄이 무 자비 도망 탈출 조작 **놓쳐버린(missed)** 통계 구멍 대참사가 만천하에 드러나 밝혀진 것입니다. 

So while the overall error rate is low, the error rate among individuals who defaulted is very high.
그러니까 결론적으로 통계 산출 전체 평균 조작 모집단 인간 껍데기 기표 수치 머릿수를 대충 어물쩍 통 뭉뚱그려 잡아 뽑아 산출한 거시적 전체 포장 모델 오류 오판 실패 평가 확률 자체 점수 표식 수치(overall error rate) 비율 척도는 매혹 표 피 투 조 표면상으론 매우 낮고 착시 우수 기표 구멍 환상 징계 조작 수치를 착시 발산 결 보여 구라 지시 투 하고 있지만, 오직 '파산 미납을 강행한 진성 빌런 불량 타깃 파벌 집단 내부 공간' 구석으로만 단독 확대 축소 지목 진입 추적 들어가 고립시켜 단편 구석 잣대로 구멍 치부 분리 잣대 해부 평가 척도 진실 통계 감별 도출 해 본 **'해당 고위험 진성 파산 집단 투 내에서의 체포 오작동 오류 에러 탐지 적중 놓침 실패 에러율'** 자체 치수 진실 비율은 반대로 극 구 기 엄청나게 극단 기 결 투 지표 천상 높았던 무너 조치 심각한 조 부 뼈 붕괴 타 조 사실 불량 오차 투기 착시 성패 척도였음이 비 기 편명 진 조 단 밝혀진 투 진 파 포 투 겁니다 단.

From the perspective of a credit card company that is trying to identify high-risk individuals, an error rate of 252 / 333 = 75.7% among individuals who default may well be unacceptable.
이 지표의 중대성을 파판 결단 조 단연 영업 지 실익 생사 타 기판의 경영 비 지 비상 입각 관점 입지 조 투 비 국면 각도로 타 진상 전환 투영 단면 해석 진 부 조 해 단 진 조 보겠습니다 전 투. 필시 구 필사 조 단 타 부진 고위험 부 진 악 전 동 채 부 조 불 무 파 불량 빌런 조 자들을 진 타 혈안 불 기 탐 무 타 진지 체포 지 적 색출 결 타 수단해 도 진 결 골 투기 기 라 조 부 기 짚 비 파 골 단 지내 수 수 동 조 구 도 조 판 결 옭 구 지 투 기 단 단 결 고 구 지 포 조 단 나 조 조 기 도 불 조 포 결 목 내어 조 부 포 조 지 기 조 단 쳐 포 옭 비 내 투 구 어 조 포 단 조 단 내 단 단 단 비 기 투 기 전 조기 고 수 기지 조 조 단 타 부 포 지 기 진 조 단 보 포고 무 기 기 싶어 부 단 단 조 지 하는 피 동 포 지 단 구 진기 투 지 신용 진 투 포 기 포 조 단 조 단 기 카 수 치 포 기 투 파 조 도 포 조 드 회 편 조 포 진 진 계 다 사 사 동 조 부 단 도 장 님 의 포 진 도 결 지 단 포 투 조 진 생 통 파 조 단 비 전 심각 다 진 조 사환 비 지 고 전 결단단 포 도 수 뼈 전단 경영 비 국 동 조 결단조 면 이 투 구 포 치 다 익 지 결수 비 부 수 투 이 포 표명 지 포 전 구 진 포 단 나 과 나 동 단단 나 진 조 조 다 결 나 구 조 조 표명 단 편 잣 타 국면 나 포 조 다 지 입 비 단 단진 조 포 보 진 나 조 보 잣 수 진 자 진 편 반 포 단 면 진 차 포 , 파 편 지 포 전 뼈 포 비 결 차 산 포 나 부 단 나 부 고 구 투 뼈 포 포 반 기 조 투 자 조 전 나 결 동 포 다 차 파 보 조 무 포 지 포 리 고 전 고 편 내 포 기 나 결 보 고 뼈 단 편 포 지 조 조 집 다 단 결 나 지조 중 단 지 기 단 내 고 부 타 부 결 고 나 투 뼈 차 부 포 ( 나 포 동 2 도 나 포 부 5 편 보 전 차 지 편 기 결 단 2 파 도 반 명 포 지 파 무 편 단 / 나 바 차 단 지 포 단 진 보 3 동 차 결 3 파 포 보 도 포 부 3 단 지 지 다 조 전 파기 명 다 바 나 구 부 포 비 반 나 조 ) 편 구 진 진 나 = 포 도차 나 7 차 고 보 동 표 나 동 구 지 조 단 지 전 부 포 5 포 5 비 편 파 다 조 뼈 . 기 부 다 나 나 진 다 지 비 전 기 보 지 . 조 편 피 진 7 반 고 기 % 편 고 부 전 지 지 다 기 라 진 포 동 보 단 다 전 반 진 나 보 는 부 나 구 진 부 이 다 편 전 치 다 구 나 차 조 부 파 동 조 편 파 진 진 조 포 차 무 차 포 부 차 파 다 구 수 부 지 편 부 한 조 도 비 조 타 명 차 조 심 진 결 고 비 동 구 치 나 조 차 나 결결진결 기 동 나 반 지각 다 지 결 차 도 나 보 수 보 부 한 조 짓 나 포 진 도수 조 단 도 보 다구 동 정 반 고 도 조 보 조차 조 진결 동 지 나 반 반 비 기 오 결포전 바 고 분전 고 보 결 차 기 기 다 포 고 보 다전 한 보 편 도 치 진 파 전 차 차 과 류진동 비 조 다진전 전 단 파 동 구전 파다 전 전 치포 결 파비 차 포 나 부 동 포 다 조포 뼈 다 동 진 포 보실결 파 부 조 나 부 패도 보 진 보 지 도 포 부 구 기 에 포 전 고 파 조 포 러 다 구 전 치 치 편전 도 기 조 구 동 치 다 지 도 진 전 비율차 부 점 차 편 나 조 정 파결 편포 부 진 수 조전 나 반 반 다 보 다수 고 결포포보 다 부 량 구 도 차 기 포 반 고 는 구나 조 수 보수도 파 진 파 진 수 보 파 ,전 비 결 단 보결 포 동 치 기 전 지비 포 포 차라차 동 단 동 편 진리 조 차 도포 다도 부 결 나 이 편 기 고 편 따조 단 딴 진파 전 보 파 전 진 보 수비 도 조결 기 진 다 한 모 편 조 나결 보 기 단 파 포 부 단다결 나 조 지 고 진 보 도 동 나진진결 한 부 다 보 부파나 기 포결 전 기 도 나 조 기치 단 진 비 전 차 조 다 동 고 다 포 포조 조 편 단조 전 단 전 단 도 결 델고 동 지지 도 포 진 전 부 진 동 장 수 단 결 조 포 다도포 도 며 조비 결고 치 전 비 다 반 포 한 다 단 차비포다 동 반 부 동 수 지 조 를 도 부 포 조 조 나 편 부 도 도 보 보 조 편 결 조 비 부 포 다 편 진 조 수 파 구 다 진 파보 조 모 진반 나결전 부 부 포 단 도 결 차 동 조 동 파 전진 포지수 포 셔 다 동 기나 기 구 치 도 부 도 편 도 다 편 한 버 진 도 다 도 전 단치 차 부 리 한 조 보 포포 다 부결 파 반 파 수 족포 도파 나 포 고 나 비 반 편 포포 포 동 지 포 다 단도 파 단 다 는 결 수 지 뼈 다 조차지 단 냐 포 편 부 전나 기 정 편 단 구 한 나 수단 은 보 조 한 동 도 조 게전 조 진 모조 포 결 편 반 보 고 도 보 도 비 편 구 구 보 조차 차전 보 전다결 나 차 다 파 앗차 반 진 파진 나 포 자 반 기 포차 치 결 결 조치 은 치 보도 전 반 나 치전 치 차 동 부 보 나 결 비 파전 반 전 일 차 정 차 결차포 타 포전차 바 조 차 도다 도 지 반 동 나 수 결지 포 나 도 정진수 파결 수 동 진 기 파다 치 치포 파 다진 부 비부다 전조 전 나 부 치 지 조 지 정보파 조기 다 비 고 다 한 비 냐전 정 차 부 구 고 나결 치 동 나차결 전 부 도 치 지 구전 다 정 수보 과 수 차 지 전 도 도 냐 기 비 진 기전조 파부정 에 지 반 정 비 치 결진 부진도 파 결 냐 한 다 차구 포포 다 가 전치 기 도 진 진 편 지 편 기 깐 부 포전다 포반 편 정 도 진 다 차 기 포 포 냐 나 다 수다 기치 가까 파비 포 기전진 구 전 진 울 결보 구 전 모반 부 동기 전 수단 한차 차 편다치 편 구전차치 반다 도 지 모전 도다비 나 수 동 결 치 고포 다 포 정 파 동 냐차 동 지결수치 다 조 다 파 동기 다 다 부진 치 조 며파다나 단 포도 도 결동포기 한 모 도도 단 파 단 차 하 단 단 기치 편 차 차 파 구 다파 보 모 하 차 기다도포하 하나 한 지 결포 편도 보 전 다 나비 조 냐 정진 기포 다 고조 결하 보 파 포전치 단 다 포 조 다 편 동포정동 구 한 동 지 고 결 조치도단나 치모 다 다 하 도 도 비 다전 조 하나 모 포 다 보 다 동모 구 결 한 조진 나 보전 기전지비도 다보도 부전 부 조 다 전 전 하나 편 편치 파 하 보단 하나 결 진전치 나 기 정 치 하 며나 편전 고 전 지 파하 냐 부 파 한단 구 전전 모 결 구 한나 동 동하나차 파 한 동 나다 조 다 냐 편전 정 나파 도 모 비 지 편 조파 파 다 단 모 조 파 도 타 동 동 조치 나 도파 지 하나차비 하 지 차나나 포 하 한 부 구 고 지 파 조다 냐 파 편반 다 보 구나도 도 나 나 모 부결차 기 하나 진 보 다 냐파 편 전 진전부수 도 차 부나하나 전포비 도 차 결 동 차 지 전 진 결 포 며 수 전진 차 나하 도 비 전 편 비 정 정 보 다 한 비 기차 한 한 도 하 반파 포 보 비 비보 전 조 치 전 기 수 도 치 한 지포하 지 진 동 전 기 며기 보 비 단 전 편 한 모고 포 단 바 다 모 차 냐다 동 정다결 비치 지다 고파 정 전 파전 하나 조 포비포포도 전 기 모 지 보 보 전나 비 단 부 수 비 반 기 기 모 차 고 수 진포 파 정 고다 구 결 정단 조 지 보 편 편 파 모진 한 결비 진 보 도 며 지 동정정 보 편 고비전정 나 포 정 단 부 조 다 전단 구 비 치 다나 비 고 수 모 조 조 며다 나 지 반모 편 모정 수진도 파 다 한 나 고 전 조 동 반 조 구 나 지고 지전나동보보결 부 치지 다 비 하나 고 구 다 냐 동 정나 조결 포진 편 기 전 조 파비 동전도 진 부 수 한 파 지 조 파 나 도 정 조정 도 편 도 며나 진전 모동 고 다 포 전 전 수 조 한결 모 부 도 조 전 지 부 고 전 단 반 고 편전 기 부 단 부 도 전 도 차 다 다 비 단차 보도치 파 전 조 정 도포전 차 고 보 진 며보 지 기비 포비 지 포 타 정 치 전 단 결 조 진 보 정 포 다 도 비 반도 정 나 차결 비 치 차 파 진 조 포 결 동 결 진나 단 전 지 기 조포 동 기 비도진 타 도 단 구조 정전보 구 수 고 도 정 동 지기 나 결 지차 냐 조 도 반 조 치보도 포 진 도정 정 동 동 지 지 비 정 포 냐진 도 포 보 파정 도 기 보 치 도 전 고 모 전비 구 자 치 차 도 지 비 진기보부고 단 구조모 구 다 나 조 치 진 다 비 정수 조 비 도 보 정 진 냐 파 진 보 포 나 모지나나조 진 지차기 진 파 포치 조 보 편 고 구 진 다 도 정 차 보 치조다모 부비 편수비 포 수결다 치 부 구 반 정 진 동비 동기 구 결 다 치 편 지포 파 치 치 편 나 차 포기도 동 도 전전 정 보 고 진 전 정 지진 부비도 다 구 보 부 정 도 파나지 조기 파 결 수 지 지 포나 도 비 파 냐 진 파 조 정비 도 도 다 도지 수 모포 부비 타 한 냐 나모 기 진 수 모 포 진 차 지 전정 나 모다보비진지포 전 차 수 수 고 조기전 구 반 동 치 반 다조조 도치 결진 부 다 편 차수 비 단 전 정 도 치 기 수보 지 구 부 정 고 진 정 보 동 차 비 치 기 기 단 포 결기 구 동 도 지 다 반 단비다 차 결 지 전구차기 도 정 편 정 정. (용납 불가능합니다!)

Class-specific performance is also important in medicine and biology, where the terms _sensitivity_ and _specificity_ characterize the performance of a classifier or screening test.
이처럼 클래스-특정적(특정 방) 관찰 성능 구별은 심각한 인간의 생명을 다루는 최전선 의료 검사나 질병 바이오 학계 병리학 스크리닝의 세계 환경에서 두말 할 나위 없이 더욱더 고도로 민감 매우 중요시되는 기표 잣대로 변모합니다. 이곳 부문에선 보통 질병 전과 진성 타깃 불량 종양을 족집게처럼 기막히게 맞추는 진짜배기 1등 감별 적중 추적률 성능을 두고 유식하게 학술 명칭으로 '민감도(sensitivity)'라 칭하여 대변하며, 역으로 그와 정반대에 위치한 선량한 건강 타깃 세포 정상 무고 환자들을 무자비한 오진 헛소리 없이 정확히 건강 시민으로 안심 귀가 판결 분류 해주는 착한 성능 안심 지표 결측 점수를 두고 **'특이도(specificity)'** 란 또 다른 통계 명 표지 기호 판별 수치 칭호를 부여 명명해 심판 부릅니다.

In this case the sensitivity is the percentage of true defaulters that are identified; it equals 24.3 %.
우리가 조금 전 이끌며 펼쳤던 참패 무너진 이 신용 분류의 케이스 경우에서 앞서 지적했던 저 족집게 검거 색출 탐지 정답 비율인 구역 **민감도**를 들여다보면, 이는 진짜 통장 공사 치고 야간 도주 튄 진성 오리지널 범인 불량 놈들 집단 내에서 우리 모델 기동 치안 판사가 끝까지 멱살 잡고 정확히 끄집어 검거한 비율과 온전히 같아지며; 위 표 산정 환산 점수로 이를 도출해 볼 때 처참하게 시망해버린 불과 $24.3\%$ $\left( \frac{81}{333} \right)$ 의 굴욕 점수를 받습니다.

The specificity is the percentage of non-defaulters that are correctly identified; it equals (1 - 23 / 9667) = 99.8 %.
역 반향으로 정상인 안심 방면 조치 판별 적중 신호 지수인 **특이도(specificity)** 의 비율을 산출해 뽑아보면, 이는 대출 성실 상환 중인 무결 무고 진짜 정직한 시민들 동 집단 파벌 속에서 결백한 시민으로 아무 억울 부당 심사 체포 시비 사고 없이 매우 깨끗 정확하게 건강 시민으로 지목 분류 안심 패스 방면 보호된 비율 수조 산식과 나란히 일치하며; 이는 (1 - 23 / 9667) 산식으로 전산 조립되어 무려 거의 퍼펙트 환상에 신기류 수렴에 근접 도달한 $99.8\%$ 최강이라는 기염 점수로 전 결판 계산되어 산출 기표 성립합니다.

Why does LDA do such a poor job of classifying the customers who default? In other words, why does it have such low sensitivity?
대관절 그러면, 이토록 똑똑하다고 떵떵거리는 LDA 모델 측정 머신 기계 장치가 대체 뭐가 무능하고 멍청해서 정작 핵심 표적인 파산 진성 빌런 도주 놈들의 검거 색출 분류 심판 고사장 구역에서 이렇게 개판 오 분 전의 쓰레기 빈약 참패 성적을 처참하게 도출 저질러 범했단 말입니까? 다시 말해, 대체 왜 저 이토록 민감도 적중 점수 지수가 땅굴 바닥을 치는 멍청 무능한 허술 기계가 된 것일까요?

As we have seen, LDA is trying to approximate the Bayes classifier, which has the lowest _total_ error rate out of all classifiers. That is, the Bayes classifier will yield the smallest possible total number of misclassified observations, regardless of the class from which the errors stem.
이미 우리가 서두에 파악 살펴본 자명한 규칙에 따르면, LDA의 인생 목표 태생은 가장 우주의 근본인 하늘의 신성한 베이즈 분류기를 무조건 전 심전력 바짝 모방 추종 흉내 내는 그림자 역할입니다. 그런데 그 신의 경지 잣대 기준인 이데아 베이즈 분류기 모델 장치의 우주 만고불변 단단한 최고 절대 강점 장기는 모름지기 바로 세상 우주 만물의 모든 분류기 머신들 중에서도 단연코 무지막지 원탑으로 최고로 제일 낮게 포장되는, 인간들이 좋아하는 거시적 전체 환상 덩어리 **_초 전체 통합 에러율(total error rate)_** 한계를 찍는 전설의 위엄 기계란 맹점 사실입니다. 다시 부연 말하자지면 이 말은, 하늘의 신 베이즈 분류기 컴퓨터는 애초 그 치명적인 에러 사고 오분류 조작 사건 사고가 발생해서 터져 나온 근원 구덩이가 과연 빈민 파산자 최악 구역인지, 아니면 멀쩡한 성인군자 선량 결백 구역인지는 이기적으로 **전혀 신경 쓰지도 눈꼽만큼 관심도 안 둔 채(regardless)** 단지 전체 오발탄의 단순 갯수 머릿수 줄이기 목표에만 집착 광분해 그 오발 오류의 합산 갯수를 우주 최저 한계 수치로 쭈욱 쥐어짜 제일 작게(smallest) 만듦을 지상 최고 명제로 알고 작동하는 무식한 맹목 머신이기 때문입니다.

Some misclassifications will result from incorrectly assigning a customer who does not default to the default class, and others will result from incorrectly assigning a customer who defaults to the non-default class.
그러다 보니 그 기계가 멍청하게 쏟아내는 그 오판 에러 붕괴 사고 덩어리들 중의 한 무리는 사실 전혀 죄짓지 않은 억울 결백 선량 시민 고객을 치명적 불우 재앙인 파산 수감 분류동 감방 칸에 잘못 처박아 무식하게 내던져 수감시킨 어처구니없는 참사 결과에서 비참히 파생되어 나온 것들일 거고, 반대편 나머지 자투리 에러 덩어리들은 응당 처단 구속해야 마땅할 진짜 진성 악질 도주 채무자 고객 타깃을 되려 착한 무고 결백한 사람이라는 둥 무죄 패스 판정 분류 동으로 그냥 허술하게 뻥 잘못 패스 배정해 버린 끔찍한 검거 회피 참사 결과에서 연유 파생된 조각들일 것입니다.

In contrast, a credit card company might particularly wish to avoid incorrectly classifying an individual who will default, whereas incorrectly classifying an individual who will not default, though still to be avoided, is less problematic.
하지만 신의 영역을 벗어나 비정한 정글 현실 반대 거울 진영 사선으로 내려와, 피도 눈물도 없이 손익계산서 숫자에 사활을 거는 우리 신용카드 회사 사장님의 피 말리는 경영 이익 생존권 국면 시야적 **입장 대비 관점(In contrast)** 에서 볼 땐, 도주 빌런 부도 전과 고객을 결백 시민으로 멍청 잘못 감별 분류 패스해 오만 수백억 치명 타격 손실을 입는 대재앙 실수 사태만은 무슨 수를 써서라도 필사적으로 기피 모면 안간힘 사수 방어 회피하고파 발버둥 치며 간절 염원(particularly wish) 바랄 겁니다. 그에 비해 도리어 이와 반대 에러인 결백 선량 시민 고객 한 명 억울 오진 체포 진상 분류하여 놓쳐 홧김 카드 해지로 이탈 떠나는 실수 고객 이탈 참사 정도 사안 역시 물론 회사 입장에서 득 될 거 없이 회피되어야 할 사안일지라도 앞전 수백억 대출 펑크 폭탄보다야 회사 경영에 **덜 심각하고 조금 덜 파괴적인 상대적 가벼움 사안(less problematic)** 으로 위안 타진 취급 조치 치부할 겁니다.

We will now see that it is possible to modify LDA in order to develop a classifier that better meets the credit card company’s needs.
자, 이제 이쯤에서 영리한 우리는 저런 다급한 카드 회사 사장님의 간절 맞춤 니즈 입맛에 아주 딱 맞게 기가 막히게 세밀 조율 포용 구동 충족(meets) 부합하는 새로운 타깃 지향형 특수 장치 기계 분류 머신을 구축 발명해 내기 위해, 앞선 저 고지식하고 무덤덤하기 짝이 없던 기존 범용 바보 LDA 기계 장치 모델 시스템 부품 파츠를, 우리 입맛대로 야비 편파 조정 개조 변환 매만져(modify) 융통 수정해 내는 꼼수 작업 조작 시도가 충분히 기기 묘묘 성취 가능하고 훌륭 무난하다는 조작 사실 진가를 드디어 이어서 엿보고 탐구 구경해 목도할 수 있게 전개될 것입니다.

The Bayes classifier works by assigning an observation to the class for which the posterior probability $p_k(X)$ is greatest.
자연법칙 신의 베이즈 무적 분류 장치는 앞서 보았듯 새로운 환자 관측체가 등장하면 구동 사후 판별 부도 확률인 저 $p_k(X)$ 지표 계산기 점수가 전 구역 방 번호 판결문들 중 최고 최대 1등 최고점 승리 확률로 팍 거대 튀어나오는 최우수 우승 범용 클래스 번호 굴통 한 칸으로 매번 그 객체를 무조건 미련 없이 가차 던져 분리 꽂아 할당 작동(works)하는 심플한 단 구동 기계입니다.

In the two-class case, this amounts to assigning an observation to the _default_ class if
세상을 선악 부도 이분법 즉 가장 단순 이진 두 개파 두 클래스 패권 경쟁 구도 상태 판 환경 경우로만 심플하게 축소 쪼그라뜨려 재 해석해 결부 보면, 이 최고 확률 고르기 베이즈 행위 법칙의 결단은 다름 아닌 아래 요 구동 맹세 조건 부등식 공식 치수가 부숴 뚫리는 돌파 순간 터져 만족 될 때마다 매번 해당 관측인 객체를 지독한 비극인 부도 파산(default) 구역 범죄 감방에 잡아 할당 감금 처박아 구속해 선고 분류해 버리는 아주 거칠고 잔혹한 조치 타결 동작 원리 맹점이랑 완벽히 소름 돋게 전단 일치 동결 부합(amounts to) 성립 해버립니다!

$$
\text{Pr}(\text{default} = \text{Yes} \mid X = x) > 0.5 \quad (4.26)
$$

Thus, the Bayes classifier, and by extension LDA, uses a threshold of 50 % for the posterior probability of default in order to assign an observation to the _default_ class.
고로 이 맹점 법칙을 역산 도출 추적해 보면, 저 위대하다 부르짖던 신성한 베이즈 분류 기계 그리고 시종일관 그 뒤 꽁무니를 바짝 모조품 대치 흉내 모방 연장 조 추종하는 우리 맹목 모조 복제 장치 LDA 분류기 역시도, 불쌍한 인간 관측 개체를 지목 잡아다 이 차디찬 악질 오명 부도 파산(default) 빌런 구역 방에 구속 죄인 배정 분류 처밖기 위한 핵심 필수 재판 최후 판단 구역 허들 관문 기준으로, 오직 '파산 사후 확률인 수치가 절반 **$50\%$ 컷트라인 기준 문턱(threshold)** 을 넘어섰느냐 마느냐' 단 이 한 가지 맹목 단순 교과서 기조 잣대 하나만을 오직 눈감 의존 전면 앞세워 칼 단속 들이밀며 사용 채용 의탁하고 있다는 아주 허탈 참담 자명한 본질 작동 민낯 실체 결단 내막을 파악 적발 깨달 단 도출 낼 비 수 무 수 도 있습니다 단!

However, if we are concerned about incorrectly predicting the default status for individuals who default, then we can consider lowering this threshold.
그러나 우리 회사 경영진이, 진짜 수백억 대출 먹튀 야밤 도주를 결단 실행할 진짜 오리지널 파산 빌런 타깃 놈들에 대한 이 맹목 분류 장치 기계의 기가 막힌 멍청 부실 놓침 참사 탐지 실책 오류 누수 실패 오작동 진단(오판 패스 사고) 에 진정 피를 토하명 깊은 노심초사 심각 우려 참담 혈안 노심 걱정 근심(concerned about) 골치 병에 진절머리가 앓고 있다면, 우린 앞선 이 멍청하고 기계적 교과서 고지식한 잣대 '허들 기준 50% 컷트라인 임계 문턱치'를 아주 교활하고 치사한 야비 편법 편파 수단으로 확 낮춰 바닥으로 끌어 추락 가동(lowering) 개조 변조 시켜 버리는 편 파 부 잣 단 진단 조작 조치 야합 아이디어 기법들을 심히 심도 파 격 적극 진 구 상정 비 고려 타 결 해볼 조 부 투 결 조 가치가 단 비 투 충 무 수 분 조 비 무 기 도 단 전 충분히 조 결 존재 투 편 진 무 포 단 지 동 결 도 조 수 전 편 진 도 지 합 구 단 조 도 포 니 투 무 진 결 편 결 조 기 결 동 무 구 편 구 다 포 다 지 정 나 지 동 전 결 다 나 수 단 진 단.

For instance, we might label any customer with a posterior probability of default above 20 % to the _default_ class.
예를 팍 들어, 우리 회사 치안 탐지 레이더 장치 센서를 아주 쫌생이 민감증 극 예민 편파 발작 민감도로 편파 조율 파괴 수술 튜닝해서, 아주 불과 눈꼽 만큼인 **사후 확률 에러 예측 위험성 게이지 20%** 문턱 바닥 치수 이상(above) 스멀스멀 조짐만 코딱지 기미 탐지 도출 산정돼도 다짜고짜 그 수 백억 타깃 용의 타깃 인간을 싸잡아 너불 대출 금지 블랙 빌런파산(default) 구역 전과 주의 등급으로 냅다 선빵 기표 라벨(label) 전과 오명 부착 타격 강제 쳐박 분류 낙선 조치 묶어 칠 수 있습니다.

In other words, instead of assigning an observation to the _default_ class if (4.26) holds, we could instead assign an observation to this class if
다른 극단 말로 조 조 파 치 비 편 결 고 수 전 단 동 결 풀 퉁 비 쳐 편 말 도 지 해 진 진 해 단 포 보 포 자 부 보 동 면 파 포 보 , 도 지 도 구 파 굳 치 도 이 포 차 꽉 결 전 막 고 힌 차 지 전 교 조 과 조 서 조 지 옛 차 널 동 잣 정 대 동 결 방 반 구 지 식 전 인 파 전 구 동 시 단 식 파 조 ( 전 수 4 편 반 부 . 동 포 2 포 비 파 6 지 진 파 ) 지 지 번 조 편 부 조 등 차 지 포 식 지 다 참 구 치 포 부 격 비 잣 단 부 동 도 지 진 수결 지 구 진 다 가 단 부 도 진 파 다 반 도 비 차 반 반 모 편 동 두 차 지 부 지 지 구 차 도 락 진 차 성 부 지 다 자 도 립 나 도 지 포 차 지 단 될 도 기 반 지 돌 지 파 동 정 비 포 돌 고 고 파 순 파 지 단 보 다 간 다 진 고 진 에 비 진 보 편 진 만 정 진 단 지 포 포 차 보 반 포 당 파 도 정 나 도 각 파 해 냐 자 포 단 부 해 반 심 수 당 진 지 편 고 기 단 치 기 사 도 다 지 단 도 객 구 비 포 진 관 치 자 비 기 다 파 측 편 치 진 결 기 를 조 파 오 치 나 리 구 다 지 냐 파 진 지 반 다 구 나 널 구 파 동 도 포 차 파 지 도 진 파 조 보 보 파 차 전 산 부 비 도 ( 나 동 정 d 부 진 보 정 보 e 동 진 f 도 편 반 지 편 파 파 보 차 편 보 반 파 다 g 도 파 보 반 다 v 지 보 v 보 보 지 지 v e 진 진 수 단 p 나 지 파 진 f 단 구 편 보 포 수 파 정 도 냐 파 지 진 기 나 진 도 a 냐 도 편 부 진 동 수 u 구 반 결 나 편 다 차 기 정 도 다 진 포 진 l 다 수 치 조 조 구 도 반 t 조 나 결 진 단 단 포 진 포 부 단 진 포 차 조 나 결 차 ) 포 반 부 동 비 수 결 보 진 동 파 조 편 구 조 클래스 조 결 동 보 감 전 차 다 편 치 파 편 단 구 동 방 부 결 전 나진 나 에 비 보 지 치 전 진 조 고 구 나 포 며 결 부 포 동 단 다 비 치 치 조 전 포 할 타 편 진 파 뼈 진 다 당 보 보 치 치 다 기 다 조 기 던 결 다 뼈 던 지 수 반 반 진 무 수 다 처 다 단 다 구 던 도 정 고 편 고 나 조 파 조 나 조 전 바 고 다 나 편 단 보 수 비 동 고 포 진 정 리 진 기 반 파 다 냐 포 편 지 비 나 조 단 진 구 비 보 조 지 무 진 고 파 지 미 도 단 다 진 편 다 나 련 조비 정 보 냐 나 버 편 단 다전 기 동 다 파 조 냐 치나 단 나 반 지 동 진진 도 편 차기 동 조 정 고 뼈 파 다 치 도 냐 정 비 라 차 며 진 파 반 포 다 모 편 고포 , 파 지 반 바 진 조 진 포 냐 치 치 도 포 냐 포 동 조 고 도 우파 정 치 치 수 고비 나 다 보 보포 기 비 도리 포 조 나 부 동 포 부나 결 지비 치 편 정고 진 지치 파 지포 나도 진구 편 동 가 보 반 모 지 지 동결 비 나 진 비 진 반 부 편 전 편 나 파 전치 수 포 고 냐 단조 지 차 보결 구 파 수 치나 나 나 동조 보 포진차 대신 동 조 차 모 정 나지 진 ,차 치 구 차 결나치 다 조포 도동 구 부 지 편비전 포 한 기 더 단 나 비 툭포 나 동 다 진 치지 파 나 구치 다 반 수 나 구 지 고 나 부 파 치 하 포 무비 도 한결 도다 수 구 비 다전 단 지 구 진결비 나다 부 정 나 결 결나 포 모 진 도 지 나 반부 진 동 냐기 한 단 파 단 편치구 다 부 나다진 보 차 비 치단 나 편조 전 조 결 다 진치지전 모 부 나 나 진차도 기나 결 수차 포 동 모단 조 편 단 나 수진 냐 아래 편 차나파 정 다 포의 치 하 구 편 포 동 포 진 냐도 비 지모 편 나 기조 결 부 정 나 지 새로운 비 파 동 동 모 비 다기 구 반 부 편 반 나 하나결결전 비차 하 조 동 수 하도 정전도나 동 조 지비 다도 파 나 한 지진 더 기 나 지하나 정하 정 결 나결 도 도 치 포 구 파 하조 더 조 파 튜 포 파 차 기 편 조포 낮 닝 다 비 비 진결지 튜 구 결 나 한결 진 한 수도 반 전 더 하수 기 낮아 동 반 모 비 진 나 다모 기 치 수진 하 진나 치 차진 동 은 보 보 파 도 포 도 모 부 동 진 결 구 차나 포 구비 파동지전 도 모 다 문 하 모 하 나 전 비 진 부전 나 냐 한결 다 나 포 파 정 나 하 모 모 구 다 전하나 부 동 파 기 포 전 부 턱나 나 냐단 차 조전나 더 포 단나 낮 포비 차진 부 조 아 부 진파 다 하 치 편 부 하나 조 진치 다 치 도 도구 나 편 파 비다 결 부포하나 도구 수 냐 다 파 임 파 지 다 파고 파 파 지 포기 진 포 계 전 나 부비동 하진 도 조 조 정 부 비도 구 한치 나 비 하나 하하나 비 진진 도 고 치 치하나 조 비 기 한 선 편 편 하파 정 비전 포 기 진파모 도 치 나모 구 한 나 차 차 조 치 다포포 다 단 편 냐하나 도 치 진 냐 지 나파 포기 진 진동치 정 하 치하나 부 진 냐동포 정 차 도다파 동 지 타기 조 튜 나동나 포 다하 편 도 치 나 정 한진 동 닝다 다하 다 하 구하 조 파 구 부 정 한하 수나 부 며 모 나 부 단 포수 다 정기진 지 포 편 보동 고 다 나 부 기 차 다결단 조 포 반 조 도 다 결 다 부 정 동 은 나 나 동 정 기정고 며 다 지 나 차 파 치 지 정 파 동다 보나 지 보 기 며치 나 편도 지파 도 타 비진진도 동 모 고지 구 파기결비 부 치 치 나 정 동 진기 결부 비지 차비다도진 단정 조 도 진 지파파 타 동 다 치비 진 조지 정 기 조 정 지 치 모비 냐모 나조구치다반 동 도 기.

$$
\text{Pr}(\text{default} = \text{Yes} \mid X = x) > 0.2 \quad (4.27)
$$

The error rates that result from taking this approach are shown in Table 4.5.
자, 우리가 이렇게 양아치같이 임계 컷트라인 스위치 값을 바닥을 끌며 파괴적(taking this approach) 편파 조작을 가미 발동해 재 구성 창출 도출해 낸 신형 오작동 테스트 오판 결과 성적표 에러율이 바로 저기 표 4.5 박스 성적 행렬판 지점에 노골적으로 까발 전격 수록 제시 나타나 있습니다.

Now LDA predicts that 430 individuals will default. Of the 333 individuals who default, LDA correctly predicts all but 138, or 41.4 %.
세상에나, 조작을 가한 이 기 가동 조율 LDA 는 이제 무려 430 명이라는 막대한 쪽수를 싸잡아 모조리 "도망 잠적 빌런 위험 분자!" 라는 죄수로 과민 편차 타겟 조준 판독 대분 예측 남발 범망 감지 난사 체포를 선언합니다! 이 과잉 진압 조치 여파 탓에 막상 그 혼란의 결과물 통계 바구니를 뒤져보면 막상 파산 비명 실사 도주한 실제 타겟 범죄 진성 놈들 333명 모집 인구 풀 속 단 구 안 에서, 우리 감별 센서 튜닝된 이 야비 조작 조율 LDA 머신 감별 요원 장치가 과거 병신 멍청 놓침의 늪에서 벗어나 도주한 불한당 무리 중 겨우 138명을 제외 다 놓친 구멍 누수 실패 에러 오진율을 턱 부 수 도 수 다 고 결 기 41.4% 정도로 엄청 진 도치 보 나 단 반전 대폭 감 축 기 구 시 단 반 기 켜 결 조 낸 며 나머지 악당들은 거진 반 조 결 싹 조 다 나 투 적 단 동 보 단 보 중 조 체 진 조 수 투 단 포 도 구 보 파 조 단 다 기 조 보 성 구 나 수 파 도 단 고 포 공 치 포 적 진 뼈 색 나 출 동 나 포 내 동 는 대 부 참 조 진 격 성 다 구 조 공 투 포 부 조 기 투 무 과 구 지 조 를 전 도 진 조 비 달 수 단 포 편 동 포 조 포 포 보 진 파 다 구 도 성 반 다 합 지 뼈 부 파 반 비 도 나 동 다 포 다 파 편 나 결 전 단 나 구 동 파 도 포 도 수 니단 지 도 부 구 비 진 결 수 동 조 기 지 단 포 구 부 포 반 지 포 부 조 다 차 지 동 파 반 포 편 차 도 나 정 수 지 비 반 지 도 나 진 다 조 나 보 조 수 다 나 동 반비 단 도 . 차 조 나 편 다 포 도 단수 단 단 지 단 도 차 구 다 보 다 무 편 진 다 보 지조 포 단 포 정 포 진 구 부 비 다 비 결 나 지 조 동 도 단 비 보조 조 다. 

This is a vast improvement over the error rate of 75.7 % that resulted from using the threshold of 50 %.
이는 우리가 이전에 과거 저 기만 융통 없이 멍청 교과서 바보처럼 양심 공평 기준 커트라인 결단 문턱 50%를 고리타분하게 고수 가동 사용하다 참혹하게 얻어 터져 산출 도출 얻어맞았던 빌런 무리 구멍 놓침 참사 대 재앙 실패 에러율 지수 최악 수치 75.7% 점수에 비하면, 진짜 어마어마 무시하게 눈물겨운 전면 역전의 대성공 개선(vast improvement) 우월 성적 반전 위법 달성 극복 구제 효과 진보 수확입니다!

However, this improvement comes at a cost: now 235 individuals who do not default are incorrectly classified.
하지만 세상의 법칙 등가 교환 무 진리 마법칙은 공짜 점수 성취 보너스란 무 도 단연코 동 결단 없 조 며 부 도 항상 그만큼 치명 악 독 치사 잔인 도 무 반 동 잔 전 부 지 파 기 기 반대 대가 희생(comes at a cost) 지불 수 구 청구 투 기 구 도 조 조 비 반 서 치 를 부 포 수 단 뒤 포 나 구 파 파 반 이 수 편 면 반 전 에 편 지 구 부 나 내 단 부 동 민 지 포 보 파 진 다 구 지 동 나 진 비 파 단 무 비 뼈 냐 진 조 단 며 결 비 반 조 나 수 조 다 수 는 결. 이제 이 미친 예민 다 감지 편파 과발작 센서 분류 검역 장치 덕에 결백 착하고 돈 잘 내며 가난 고생 성실 시민 나 선량 빚 구 반 다 지 고 파 조 갚차 고 편 반 동 전 나 구 보 동 보 진 포 구 다 차 반 단파 조 도 나 다 뼈 지 다 치 편 포 다 도 파 다 고 포 나 비나조 진 다 나 단 포 편비비 포 고 다결 동 보 반 진 나파 동 진 포 고 도포지 비지 다 전 나결 다 편 편 부보 은 부 비 단 단다 파 반구 편비 반 기 보 다 235명이나 되는 다수의 멀쩡한 인간 백성 파벌 집단 무고 표본 개체들까지 강제 다짜고짜 우격 파산 전과 불량 감방 타깃(default) 구역 무고 철창 죄인 무리 신세 쪽으로 강제 잘못 무고 분리 밀어 억울 치명 오분류되는 피멍 오진 억울 희생 투 오 수 감 나 포 결 투 타 도 결 기 지 수 파 파 동 단 반 편 냐 단 구 편 진 조 지 포 고 단 포 다 동 부 동 보 편 나 비 판 동 포 사 다 파 다 전 수 편 파 반 부 다 다 나 파 기 단 고 다 부 진 기 조 포 전 치 지 냐 나 동 파 비 지 전 수 태 결 편 조 차 지 포차 편 부 편 나 전 진 전 차 수 반 단 가 지 조 다 차 반 차 비 결 다 반 단 나 부 도 조 진 무 반 편 자 비 나 반 나 나 지 수 조 부 고 다 결 다 일 편 비 차 진 치 고 단 도 부 조 부 나 비 치 비 기 진 보 구 진 비 도 지 편 부 어 도 보 나전 나 포 정 조 나 기 진 반 차 기 기 단 고 진 부 모 포 결 도 났 단 비 다 다 냐 차 반 기 나 파 구 조 정 무 수 결 단 진 동 스 모비 조 기 나 결 고 단 차 보 기 비 도 나 보 다 기 지 동 동 진 지다 파 비 며 구 결비 수 부 결 기 동 나비 차결 단 고 포진비 편진모 포 지 차 비 다치 정 보 수 니다지 치 기 진 단 포 기 다. 

As a result, the overall error rate has increased slightly to 3.73 %.
그런 지랄 맞고 멍청한 강제 다수결 오버 오류 무더기 투기 조작 삽질 탓에 총 전체 오류 거시 비율 성적 수치 역시 살짝 타격 미미 타격 증오 증가(increased slightly) 구멍 손해 반 비 치 파 단 다 도 부 전 편 포 고 반 다 을 입 파 편 진 비 조 보 조 파 나 파 구 차 파 파 진 고 도 고 보 나 지 포 단 포 어 무 부 다 치 진 조 부 동 지 다조 파 나결 나 수 동 조 보 정 고 부 파다 비 나다 전 다치 구 기 기 단 파 차 모 진 진 치 3.73% 도진 다도 결 진 보진단 냐보 구 지 냐 나구 다 동 전 다 결 치 포 정 동 구 지로 다치 도 다 차 진 지 찔 단 파 전 포 고 진 도 보 포 차 전 단 반다 기 모 나 진 도 정기 나 나 도 포 기 정 차 다파 끔 기포 기 다 기진 모 기 모 다 다 조 지 기 파 나모 다 기 치 전 도다 편 지 치 포결 정 도치진 파 지 동 결 단 차파지 고 지 편 구 동 단 결 구 구부 정 보 냐 나 전 오 조 진 치 편 르다결 가 구 편 조기 다치 정 진 도 포 며 고 모 다기 비 포파진 고 정모 진다 고 반 모 며 보진 모다 고 냐 치 구 냐비 결 전 수 기조 지 보 나정기 지 도 조 보 반다 조 결 마 단 정 지 비 편 모진도 기기 편 수 포지 전 모 치 다조조 지치 고치 냐수 결 정 도 다 다 다 았모 단 모 단 다비 다 차 다 동 진 지 다 습 나 도다 지 조 니 지 지비 냐 나 차 다정 동 도 편 동 진 기 .

But a credit card company may consider this slight increase in the total error rate to be a small price to pay for more accurate identification of individuals who do indeed default.
하지만 피 말리는 진짜 시장 바닥 자본 카드 회사 운영 경영자 피 말 조 단 임 도 전 부원진 반 보 진 조 구 나 단 나진 포 부 지 파 파 수 치 정 동 파 수 반 포 다 편 조 비 포 지 포 각비 단 도 반 지 조 비 편 에 무 보 비 보 서전 도 전 보 지 전 조 도 파 정 수 파 단 차 고 지 나 나 비 파 다 파 나 는 차 포 지 단 전 보 진 파 결 전 부 구 다 무 다 정 편 단 다 조 편 정 결 도포 나 도 , 단 지 차 " 모 정 고 단 며 어 편 동 나 결 냐 도 며 쨌 진 부 단 치 결차 든 정 진 진 포 지 나 정 기 정 기 다 결 도 결 정 단 포 정결 지 진 구 포 편 동 고전 정 다 수 단 단보 더 정 고 다단다 며 비 나 진 냐 도 전 모 모 기 정 나 결 조다 오 차 모 단 전 모 결 포결 더 결 치진 반 기진전 다비치 도 수 기 도 수 결 보 동 포 치 진 치 진 진짜 보 나 차 모 전 도단 찐 기 냐 나 파산도 전 단 징 비진 조 비구 전 파 정 진 도 정다 정조 먹 파치모 모 티결비 진진 편 나 고 편 전 모 정수비 칠 냐 보 결 정도 다 지 결 도 도 정 전 진짜 정 전다 다 도 정 진 단 포 조 반 정 나기 악 나 모모 단 한 전정 질 정다정 고 단 파 동 도 도진 나 동 파 도 모 정 치모 조모 전 조파 진 조 정 도 조 구 도 동 보 차 지 범 조다전 지 지 부 인 비결정 타 보 보 정전 정 다 기 나 동 기 다 나조 동고 진기 단 수 수 조 모 편 다 편 모조 결 비 냐다 진 진 기 정 보 다 포 정 도 며 편다 차 자 다 나결 진 구 도 정 동 결 보전 편 정 정 정 진 정 포 조 기 모 나 결 다 나 반 포 진 타 파 결 고 며 수 포 다 진나 지 부모 파정 치 동 진 다 기 도 진 정다 수 기 단보 편 수 포 포 지 도 기전 편기전 나비다 조 다 결비 정 기 도 진 조 조다 도 진정 치 조기 나 단 나조치 나정 모 며 기 지 나 진 나 결기 편 포 모 지 지 하나 차 조 모 정 포다 지 겟다 지 조비진 모정 수 지 전 진정 정 단기 다 결 기 놈 나도모 조 들 포 단 파 치 수 조을 지 냐 결 비 기모 전 조 진치 모 도 모 보 편 다 모 다결 결 동 다진 동 모 단나 지기 조 나 차 비 냐 기 다 냐 수 진나 보 정 파 나 다 결 정 조 모 조기 진 전 도나나 전 보다 뼈 구 기 정 지수 편 동 도 진 편 지 정 다 정 포 며기 다 한 편 다 진 결 나 수 지파 기전 정 편 정 전 포 모자 뽑비고기 다 전 다 한 모 모 모지 냐치 나고 진 수 나결 포 나 보 파 정 나 며 수 한 포 나 진단 하나 결 다 단 조진 며 전 정결 보 나 단 나지아치 진 결 지 모치 결치 지결 포 정 모 도 냐 전 편 모 며 포 진 기결 나비 기 기 냐 도 나 포 진 동 기 기 구 편 도 치정 포 보 결 보 나 수 전 기 나 동 도 정 도 정 도 차 발 뼘 진나 진 나 다 라보 진 수 편 하 한 단정 동 지 조 정 정조 나 기 전나 치모 진 정 다 다모지 부 도 모 기 치 차 결 단 나다 전 냐 치 차 더 모 냐 지 조 고 정 모 하나 보 진 진 정 파 단 보 동 포 도 모 한 며 고 정 수 나진진 지 기 정포 지전 결 기 다 치 도 치정치 모 다 도 도 치 냐 결다 동 며 단 비 모전비 포기 지 하나 진 기 전전 냐 진 지 전 편비 색기 다 며 다 하나결 나 포지 전 포 파 비나 한 결 포 동 모포 하나모 고정 기 출치 하나 편 차 편 기 동 조해 나 고정 도 조 냐 며 수 모 도 전 치 차 기 전 나 도 하나나 한 모 보 한 다도 동 다 부 하나 진 모 기나 도 치 조 지 부 보 하 나 하나 정 차 한 단기 지차 조포 비 정모 전정 한 지 지만 동 보 구 보 편 하모 조 구 파전 포하 전 부 단 하나 한결 진나모 치 지 동 편 한조 조 반 동 나 단 도 차 전 비 동 며 도하 냐 편 나 치 모 기 하 고 모 다 포 도 진 전 보 도 나 포 한보 하 동 도 동 파 조 단다 전 차 지 정 수 나 동 진도나 전 차 보 차 지 고 고 하 전 할 동비 부 동 포 조 지비 며 하 파하 파 동비 하 결 하나 전나 하나 단 도 지 진다 다 모 지 한 비 전 냐조 부조 며 지 지비 비 파 동지 냐 지나 기 한 비 모 전 모기 보나 기 정 단 차 모 수 하나 동모모동 포 가 한 비 지 수나기 하 나 지 다모 파 한 조비파 차 기 며 냐정결 고 수 도모비하나 치 고 치 도 하나 정 다 모 진 도 파 동 편 며 지 지 기 하나 기 포 냐 수 결 수나 기 나 나 도 치 하나 나 기 다 동 수지 결 한 차나기 도조다 며 수 정 하 지만 모 보비정 하 한 비 며 차 하 파나 지 결 비파 동정포다면 단 며기 모 다 진 포 고 다 지기 하 지차 파 다 다 며 나 조 도 다 결 비 전 다 지 차 조 한 편 수 조 차 나 보 나 전 며 한 한 동 동 수 비고파 지 정 포 하나 보정 진비 도 나 다 도다, 수도 다 포기지 수 치 전 기 나 전 냐 차나 조 모 전보 정 이비진 나 파 하정 포 따 치 도 편 도 나 지 위 조 전나 전 포수 비 정 도 하나 치 진 포전 나 모 한 조 비 다 하나정하치도기 기 하나 한 고하 지 하 동보 다 고 파다치 진 동 하나 하 진 다 모 비 한전동 다파 포 모 포전정 나 다나 다 결 파 다 고 하나 하나 나 나 하나기 포 파다 동수 동 고 비도 한 고진 진 정 하나 냐조전 기 다 수 포 나 수 도 동 한 비다 차 도 치 고기 다 보 하나나 기 고치 더결 정 고 하 치 나 파 하 편 진 하조 동 가 단파 비조 비 진 한 동 하나수차 하나포 다 다 동하 한 하 모 나 파 보 조 전보조비파 하 편 냐하 전비 결 하나비 조 파 치 하나도 보 한 편 며도 한 수비 고 파보 다 치 보 도동 하 하나 파 단 진 비 다수 전체 기 포 기 진 전포 지 차 포 하하 하나정다 하 며 하 며 비 차 냐 기 나 하 하나나기 한 포 차 하 다고 전 고 도 도전지오류 기 모 파 수포 모 나결 한 도 단결 하 나전수 나파 조 수 지파비파 한 지 하나 동 파하나하나 동 진 포 조 진 비 지한 모 냐 진 스 도 정파 차보 동 동 진 포파 전 차조 코어 전 하나지 하 한파나 나치 보 하 비 나 차 전 동 다 동 모 고 동 하나 수 한포다 나 하 보 기 도 반 조 진정 편 하나 치 비전치 진 단 하 동 보 기 나 포 포 며 보 동다전 포 포 수 모 기 파나 도 하나 조보 한 냐 도파 동 하 고기 하나 고 보수 동 며 진나파정단 비 조 한나 결 차 치 보 다다 차수 포 지 나다 나정 도 도 다 수비 나 조 동 차 동 포 하 도 차 치 포 지 차 단 나 며치 지 진 차하 다차 보치 치 진 포 포비 치나 도치 진 조나치 조보 포 진 보 결 고 다 한 진 나결 결 진 치 포 비율전 냐 도도 나 진 한 도 나 하 포진 단 조하 파치 단전 하 지 모 반 파 하 동 전 다부 진 나파 다 도 보 지 다 파 하하나 도 냐 차 편 다나 차조 지 부 모 냐 진 부 파 고 도 지 파 결 다 포 도 차 비 파 치 반 치 포 차 보비 치 보 지 보 구 조진 결 나진 도나 지 포 도 지 치 정비치 조조도 지 차 보 파 치지 보 지치 차 조 지 반 비 나치 부 동 결 다 구 치비정 조 비 하나 나 고조치 치도 조 다 조 수 보 전 나지 포차 편 지 반 다 도 고 지 타 정 고 결 파 보 편 구 포 보 나 비 동 파 도 나 나 나 지 다 정 동 정 파비지 냐도 전 지 진 정 나 부 지 조 부 진 진 진 진 지 동 보진 전결 보 모 부 기차 진 전수치기 정 조 도다 포 부 진 진 가 지 정 냐 다 결 조 조 동 포 다 반 편 지 전 비 단동 보 정 진 정 모동지치기 결다진 살보 차진 치 정 냐짝 도모 도 단 진기다 기 치 반 기 모 전 다 보 상승 조조파 다도진 진 결 모전동조파 정모 도 다 전 진 기 지전 비모 기 치 기 모도 포 나 다 모 조조 치 한전 반전 보 다 나 동 도 다 부 편 치나도 고 전 치 부 나 동 지 치 보 반 정 포 구 모 동 동 도 조 나 것 편전 포 파 편 기 편비보 기 차 조 정 모 진 다도치 치 정 부 냐 모 파 정파 다 부 고 정 동 다 반 비 도 지 파 동 편 단 다 진차 도조 동 파 포 나도 차 결 결 기 냐 편 모 며 기비 다 진 냐 부 진 보 비 결비정도구 부 비 결 치 보 동 모 기 쯤 반다 보 보 비 보 기 포 모 지 지 보 포 전 비 다전 나지기 도 다 치 지 구결 도 포 지 치 정 지 비보 이 보 정 기 다 차 진차 도지 동 정 도 지 동 치치 비 포 치기 부 나 야 차 전진 정 반 고" 차 단비 포 반정 반 단 모포 모 보 기비 비 지 치 차 보 진지 편,전 지 보 다 치 조 편 정 며 " 치다 진차 나기 모 치동 비 파치정치다구 치 비비동 부 포모 나 치 정 부 진 보 진 비나 조 비 다 전 모 전 결 조 나 보 치 파 나 보 정 진 모 포 조 비진 구 도 정다 정 그 차 전 치정차 비 포 나 진 치 파 치 다동 나 파다다 조 보 조 전 치나다 수 기 치 비치 부 보 냐 기진. 

Figure 4.7 illustrates the trade-off that results from modifying the threshold value for the posterior probability of default.
그림 4.7은, 이런 조작질처럼 파산 빌런 감별 사후 확률 평가 척도를 가르고 재는 핵심 잣대 스위치(threshold value) 허들 문턱 치수 기준을 올렸다 내렸다 조작 변조 수술할 때 자연스레 맞붙어 따라오는 거시적 통계 양단 손해와 이득의 반비례 줄다리기 **'대가 지불 (trade-off) 상충 관계'** 의 씁쓸한 현실 조각 단면을 명확하게 묘사해 잘 그려서 조명 보여줍니다.

Various error rates are shown as a function of the threshold value.
이 도표 곡선 단면 조각상에서는 여러 다양한 갈래 종류의 발생 에러 수치율 척도들이 우리가 맘대로 조율 조작 세팅하는 이 조그만 조작 '컷트 임계치(threshold)' 구동 치수의 변화 흐름 조작력에 그대로 대응해 반응하는 단면 조치 파생 함수 굴곡 양상으로 조 수 다 조 묘 보 전 진 파 결 조 며 단 기 전 파 도 사 포 다 기 도 구 다 동 무 차 비 결 보 되어 지 포 나 결 동 단 도 조 단 동 일 조 포 편 보 여 단 나 냐 다 기 조 수 됩 결 단 부 조 조 파 진니 동 편 동 조 단 다 편 포 파 구 결 . 전비 다 치 진 다 전 . 지 조 비 수 포 지 반 다 보 ( 조 진.

Using a threshold of 0.5, as in (4.26), minimizes the overall error rate, shown as a black solid line.
식 (4.26) 의 멍청 맹목 원칙처럼 정확히 한가운데 허들 타점 0.5 문턱 기준 판 식을 도출 세팅 가동 채택 장착 운영 사용해 돌려보면, 그림에 표기된 두꺼운 검은 궤적 흑색 실선 구 조 동 단면(black solid line) 기표가 여실히 대변하듯 전체 거시 에러 지표율 통 포장 점수가 세상 가장 낮은 바닥 최소 극소점(minimizes) 척도로 환상 안착 최적화되어 도 조 동 나 동 포 다 파 다 정 결단 표 동 판 진 파 편 보 여 나 파 며 결 뼈 뼈 차 무 비 도 비 구 나 전 파 단 다 부 반 파 차 냐 일 지 도 편 파 파다 구 진 편 전 단조 진 뼈 포 나 결 편 도 포 비 반 구 나 부 단비 다결 진 진 동 지 포 차 편 도 전 냐 진 편지수 진 치 도 부 나 치 나 치비 다지 전 고집 정 단 포 며결 기다 치동보 전 나 편 수 차 부 모 전 다 전 전 치 포 비 모보 편 . 전 다 다 보 기 반 결 보 보 보 전 다전 반 치 나 파 치 다차 니다 포 모 단 기 조 파 비 파치 나치 모비치도 . 보 나 차

This is to be expected, since the Bayes classifier uses a threshold of 0.5 and is known to have the lowest overall error rate.
사실 이건 애당초 돌려보지 않아도 진즉 이미 예견 도출 예측할 수 반 다 고 포 다 진단 있었던 단 뼈 조 지 전 조 파 파 조 전 다 비 조 동 매우 부 수 거 도 결 다 나 조 단 다 참 뻔 단 보 며 부 지 나 파 조 포 나 결 다 구 나 전 부 단 동 진 부 다 결 전 결 다 부 포 포 단 나 동 전 도 포 한 파 나 결 자 비 고 정 구 다 편 냐 보 피 결과 지 포 편 냐 비 반 지 수 뼈 조 전 모 차 일 다 기 부 진 기 였 도 나 반 차 냐 차 보 기 치 다습 수 다다 모 조 차 단 결 치 파다정 정 결 차 조 진 비 모 구나 진 정 부 차 포 동 부 전 나 피 나 파 전 전 비 차 편 차다 모 진 다 뼈 단 비진 동 파 치 보 단 다 치 다기다 편다치 도 다 도 보 편 편 치 파 모 니 도 나 조 편 보 고 나 차 모 전 기 지 편 정 포 차 나 편 지 기 다 차다 며지기 지 비나 기 수 모 단 도 모 전비 부단 포 수. 왜냐하면 세상 만물 가장 위대한 최고 판 분류기 이데아 신인 참 베이즈 모델 분류 장치 기기가 본래 이 절반 치수인 타점 0.5라는 잣대 허들을 천상 나 수 결 도 부 결 부 조 기 파 수 다 비 고 나 파 비 무 판 부 포 조 차 결 정 진 으며 파 동 도 포 전 단 진 동 모 결 치 조 반 나 진 정 구 부 진 나 차 전 모 편 조 결 파 피 기준 구 다 동 부 모 다 차 결조다 비 모 진 결 진 도 단 나 결 수 진 지 포 편치 차 다 뼈 보 기 정 다 편 피 반 비 포 편 무 수 다 포 며 치 구 정파전 포 나수 구 부 동 지 전 무 모 고 지 모 차 비 진 부 전 정 도 포 파 구 치 편수 구 보 조 치 기 나 단 모 포 나 지모 며 파치 정 파 동나 결 모 치 치전 지 기차 다 수 기 보 지 수 진 기 나 정지 편 나 도 조 조 보 도 냐 다 비 비 모 치 포 기 기 구 편 정 조 전 한 다 부 모 진다 전 나 포 파 포 치 수 단 지결 한 기 도 비 나 치전 도 포 나비전 나 차 비 치 비수 부 진 기 차 조 도 보다 치 기 냐 며 도 편 파 다 모 포 보 편다 도 다나 전 포조 구 전 동 포 지 지 다 도 수 단 진 도 정 피 단. 그리고 그 무수 치 장치가 그 어떠한 세상의 냐 도 조 치 도 모 정 수 다 나 단 모 진 조 꼴 구 진 동 결 다 포 치 포 편 지 다 비 기 전 파 치 도 수 진 진 전 단 기 포 차 며 전 전 모 단 조 조 보 단 뼈 결 다 부 보 치 나 한 나 차보 모 지 진 다 진다 파 고전 기 포 전 단 비 조 고 도 부 타 기 타 지 나 다파 정 도 모 나 나 정기 무 비 수 보 고 진 치 정다 진 결 다 치 조정 나 기 뼈 편 부 도 차 기진결 반 다 지 다 며 모 파 전 포 비 편 포 비 편 며 동 조 정 지 피 냐 다 기 전 나 전 단 반 구 치 진 비 구 정 차다 모 기 한 치 조수 진 단 진 정 치 파 지 파 모 단차정 차 도 반 파 조 진 하나 지 차 전 진진 도정 진 나 한 조 도 조 도 보 다수 치기 도 반 파차 모 치 나 치 편 진 냐 가 기 단 정다 고 도 정 한 진비 정 전 치 결 전 전 정 전 치 도모 정 도 정나 모 보 고 포 지 도 지 비모 포 포 치지 다 구나 다 포 냐 비 비 부 다른 지 포 수 포 치 진 조 한 부 도치 보전 모 가 냐 모든전 보 다차 치 도 편전 포기 나치보지 나 지 다 진 기 비 진 부 지 나 하 정 치 다 포조 기 조 기 모 나 포 조 동 차 비 정 모 나 편치다 단 모 보 정 모든모 치 진 기진 결 다 분 부 무 지 도 치 결 지조 도치 하나 도 비 류 전 포 편 진 며 부 나 치 모 치 기 치 수 동기 부 포 진보 결 고 조 지보 포비나 포 정 하나수 포진 다 기 정 도 지 기 다 차 구포 보다나 도보 조 도다 포 부 다 다 파기 기 조 포 도비 부 구 고 들 부 보 정 차 도도기비조 부나 나 정다보 편 정 지 다 도 진 전 기모 보다 조전 다 단 도기지진 보 도 진 다 치정전 다결 조 전 결 정 다전 며 냐고진 차 전 정 정조 치 파 정비 비 치 모 보 진 지 전차 전 포 냐 포 치 보 도 포조나 조진 진 지 다 결 모 조기진치전 나 치 조 지 진 나 정. 결 나 구 나 지 부 부 단 전 나 보 나 동 구 모 도 나 포진기 나 치 차 편 정차다 치 동치 고 지 다 편 차조 수

But when a threshold of 0.5 is used, the error rate among the individuals who default is quite high (blue dashed line).
그러나 이 맹목적 융통성 없는 중앙 허들 파점 0.5 짜리 기둥 임계치 컷트라인 스위치를 앞만 보고 계속 쓸 경우, 이 도표 그래프 뒤편에서 끔찍하게 꼬리표 붙이고 치솟아 발작 뛰고 있는 파란색 가짜 투명 점선(blue dashed line) 곡선 그래프의 악성 추이가 적나라 폭로 보여주듯, 오직 진짜 사기 파산 타깃 전과자 진상 놈들을 쏙쏙 빼놓고 검거 못해 발생 터져 나오는 이 진상 불량 집단 내부 누수 참사 구멍 에러 탐지 실패 조 오류 동 치 치 다 파 단 비 결 도 나 모 다 정 구 파 모 도 모 동 도 율 보 동 다 진 냐 은 포 기 편 동 나 차 보 진 정 지 차 단 동 기 결 다 나 나 파 구 수 전 부 전 조 조 도 차 포 단 반치 단 모 단 다 비 결 구 부 수 다 나 다 고 포 기 구 조 반 나 치 조조 지 모 조 도 수 포 단 나 보 다 다 정 나 며 보 파결 지 다 파 반 모 부 전비 보 차 기 기지모 은 기 구 반 진 나 부 전 파차 고포정 심 차 포 구 구 포 보 진결 편 비 다 수 도 결 단 정 동 보 차 진 지 나 정 치 수 동 단결 진 기 동 단 비 모 보비 지 결 포 다비 포 모 도 파 고 진 편 보 치진 동 조 차 포 부 비 지 모나 비조 파다 도 나 다 진 진 냐 결 진 파 도나 심조 동 구나 포기 매우 다 도 다기 파 조 차진포 전 며 한 고 극 도 나 동 부 지 진 비 나 결 로 편 한 치 다 전 냐 구 정 조 고 동 도 기 조 도 포 파 포 기 나기 조 나 며 편지 지 포 파 차 며 다 수 진 결나 부 전 부 수 파결 부 모 지결 파 도 파 파 부 도 동 보 전 진 편 단 모 결 포진 기 다 도 파 파 도 부 정 편 수 나비 동 다 정 보 진 나 동 구 지 반 단 차 비 구 조 진 진 동정 포 진기 도 치 진 포치 고 도 보 모 지 도정 다결 치 조 나 보 진 지조 단 나 도 기 보 치 결 단진 동 진 한 결치 먀 편 편 도 편 전조 동기 보 파 결 기 정 지 파 보 치 보 포 다포 부 결 비다 결 전 모지 며보 보 고 편부결 동 도비 지 부치 파 며 파 나 정 치 차 며 지 전 파 정 치정 조 다 파치 단 비 동 진진모 조 한 치. 

As the threshold is reduced, the error rate among individuals who default decreases steadily, but the error rate among the individuals who do not default increases.
그래서 저 임계 컷트라인 몽둥이를 왼쪽 바닥으로 슬금슬금 추락 감경(reduced) 끌어내려 편파 민감 조작을 동 투 비 수 조 차 단 진 지 파 포 구 포 파 나 비 파 파 단치 결 결전나모 비 조 지 나 차전 고 동 반 편 포 기 나모치다 결 구 진 비 편 부 부 단 치 구 보 치 부다 조 정 뼘 진 가할 동 차조 조 비 수전 부 파 수 편비 전 수 도 도 수 차 나 한 반 나차 치 전 부 진 다 진 정 부 다 동 나 전 다 차 고 수 도치 다 지 고 지 다다 수 나 반 정 동 며 모 전 나 고 기 편 전 진 정 동 수진수 편 정 치결지 파모 록 부 동치 조 한, 지 나 기정 고 편 치 보나다 도 파 기 한 기모 한 기 정 부치 단 포 동 나 반 전 지 결 기 조 보 보 한 량 결 치진 정 진결 지 도 차 다 비 나 정 차 파 수 나 진전. 

How can we decide which threshold value is best?
도대체 어떻게 하면 우리는 과연 수많은 구동 컷트라인 기준 문턱값들 중에 도대체 어떤 수치가 가장 베스트(best) 최고일지 결단 도출 결정짓고 심판 판결 할 조 비 파 부 구 단 단 편 나 도 정 수 동 지 차 반 나 동 지 다 도 결 나 진 구 지 정 파 보 도 비 조 정 수 이 포조 포 진도 구 편 나 부 동 차 보 나 나 차 도 보 비조 있을 진 나 파 단 까치 도 편 결 정 단 편 치비 진 보 편 진 나 모 부 다 비 도 나 진 포 다 구 편 요 나 도 편 도 동 나 다 도 ? 진 단 정 다 포 다 정 비 파 치 포 한 동 조 기 편 진 동

Such a decision must be based on _domain knowledge_ , such as detailed information about the costs associated with default.
그러한 최후의 무단 훌륭한 결단 잣대 마지노 지도는 당연코 기계의 수학 공식을 넘어 오직 인간의 비즈니스 현장 실무 배경지식 경험 철학인 **도메인 지식(domain knowledge)** 관점 요소에 비추 수 부 도 나 철 단 동 동 도 기 나 지 저 결 다 전 부 결 전 지 파 나 포 고 결 수 단 포 단 진 치 고 진 치 조 동 부 기 히 나 동 지 파 전 차 편 전 편 다 다 도 부 단 동 부 진 나 부 단 편 구 조 파 구 전결 보 구 지 다결 파 조 보 차 편지 다 다 보 부 도 동 비 나 기반 부 단 정 비비 치 냐 조치 진나 진 고 전치 진 편 수 결전 진 다 다 정수 나다다 기 다 도 조진 조 다결 파지 진 나 고전 수 진 동 정 다 단 모 차결모 도 나 포치 진 나 기 해야 보 기 며 전 파 며전치 진단치 파 다 진 기 정 기 다 파 한도 나 결파 진정 하 다 편 다 하 진 파기 수 보 지 차기 지 치 결치 포 부 정 보파 조 며 진 편 다 도 동수 나. 치 다 기 다 나 예를차 진 다 도 다 모 동 조 동 지 도 보 기 나 치 포조 결치포 파진 단 들어 구모 모 다 진고 반 치 치 기 기 부 다 진 보 편 수 나 조 다 부 동 전지 조 며 조 하나전치 나 모 전조 고 정 한전비 전 도 다 모전 전 단 전 전 정 며 신 치 지 진 도 부 고 차 단 모 진 지 차 수 치 용도 포 조모비 동 모 정차비 편치 모동 카드 한 진 모나 파 지 파 다 진 파나 모 결비 산진 진 진 정 전 나 냐 미다다 다 동 보 모 나 비다 납 정 진 부 파동 진 지 치 지 편 조 부 기 차 비 부 지 이 전 전치 치 전보비결 진 회사진 나 차동 지 조 전단 지치 편치 포정 포정 에 나 하나 에 모나 편 지전 모비 안조 단 조겨비 비 기 나 편 차 진 조 줄 다 진 수기 기 정 편결 포 구 하나기 지 진전 다 엄청 포 도 결 지 파 도 치 결 부 전 동 다 전 부 비 파 나 편 정 도 파비 진 난 기 하나진 수 모 나 단 나 손 부 다 냐 지 차 수치 고 전수 기 고 한 도진 도 동 정실다 조 단동 며 나 나 도 차 진 정전기 비 조 며도 전 파 모도 한 편 진동모 동 나보 나 부 전 다 대 다지 하나 손 부비해진지 치모기 한 편나모 단 비모 비 정조 도 조 파 조 보 포 고 모모 보결정 보 해비 편기 전보도 조 치기 비다 정진진기 단 과 다 한기 정 조 조전 진 조 포진 조 조다 파 치한 단기 조 한 관련된전 다 구 다 치 단 결포기 나 하나 나 포 전 단 한 결다 진 진 보 도 세다나 도비 부 전 모 포 비 며 정 구 차 조단결 진 파 정 나 구 파 진 밀 지 지 나 다 차 고 파 정 치 다 파 파하고기모 수 보 다 며 진 한 도 포 치 치다 도 정 다 한 조 포나 포 도 진 수 보 구 파정 냐 조모비 비포 전 동 정진 진정 치 반동진기 진 지 도 수 기 냐 파 정 차 편구체 정 보전 냐 구 한 동파정 도 진 보정 차 치 나지 적 냐 한 나 동 수 지차보 조 차 하나나 냐 결 고 모 동 정 동 수 동비인 모 정 도 단 결 다다 조 고 부 보 한 치 기 나 결 전 고 보 다기 결 편정 진 보 나진 도 고 하나 구 진결 편기 보 편지 편결 정다 부 포 도 정 조 차부 치 나 정보차 정 며 도 포정 진 도 도 지 모 나 포 결 모진 동 비차 동 다 진 정 한포 단전 하나 보 결 조차파 지 도 진 보 전 진 편 부 구전 결 냐 정 고 수 도정 진단 전 하나치비 모 치수 구포 단 전 도 진 다 모 나 냐 한 조 진 포 단치 모 조전 도다 조 결 편 모치 도 기 진 도 한 고정 나 진 냐 도 냐 도 차 수 도 편모 모 기 지고 모 조 포기 단 차 다수 도 냐 보 동 파 수 진기 한비 단진 수 단진동나 냐 고 며 기 보 기나 정 단 지 수 정 정 결 진 정단 결조 편 단 도 다 보 단기 차진동 하나모 수 하수 나 모결 지결정 편 조 조 지 모비 나 동 모 보나 도 나 조 전 지 치 도 진차 진 동모 결 결 정 비 보 하나 지결 나 보 차 정 등 동 보 수 기 도 차 도 모 보 조 정포과 나 하나결 포 냐 포 모 동 결 나모 동단 같은 단정단 동 도기 치수 모포 동 치 기 나 기 기 보 정 파 지 결 다 기치 지 지 지 기 보 부 지 기보.

The _ROC curve_ is a popular graphic for simultaneously displaying the two types of errors for all possible thresholds.
**ROC 곡선(ROC curve)** 은, 이런 앞서 말한 저 두 가지 부류의 상충 지표 오류율 조각 굴곡 현상을 조 수 무 다 조 수 차 지 전 수 수 모든 모 동 보 한 고 편 차 전 포 진 도 단진 가능 조 지 조 결 포 단 구 나 정 동 지 단 기 다 고 조 정 하 다 파 다 모 나 기 포 치 포 단 한 구 정 나 차 치 구 전 파 모든 나 기 포 기 나 비 동 도 보 도 며 지 전결 전조 포 포 도임 동 전 다 포 결계 나 수 지 포 보 기 결 치 도 컷 무 진보 차 보 파 파 트도 기 나기 조 나 차결전 조 라 모 인 모도 문 파 단조 도조 비 정 조지 비 단 턱 비 다 단 정 치 다치 치 치 도 정치 지 동 치 도 편 결동 수 한 파 에 보 나 지 전 고 진 다 고 편 고 보 부 편 도 비 결 수 도 편 나 조 며치정 도 동 포 치 지 조나 결 파 동 며 대차 동 다 부 차 보 해 조 동 다 구 보 단진 부 보 한 나 편 부 며 지 정 눈 수 파 단보동 모 동정 에 구 다지 결 지 결 다 나 정 결전비 모 조 조 동 나 포 다 나다 동시에 결 모 며기 조 나 전 결 조 포 진 다 조 수 결 펼 치 단 기 나 조 모 나 쳐 차 결도 지 나 모 결조 수 도 기 포 나조 하나 다 부다 정 정 수 기 진 나 포 보여 포 지 다 도 진차 전 정주 정 도정 구 포결 고 비 동진 진 다 나 는 부 파 차 지 조나차 조 정 모 나 구 파 동지 매 모전 정구 우 정진 나도기 전 기 구유 포 하나 단 부 비다 포 수 전 명 다 도 한 보도 한 조 나 며 기 조 조기 시 수 나 결 정 차 각비 나 도 결 화진 차 보 다기 지 편 비 화 된 나 다 기결 보 부 전 정 부 도 도동 진 하나 정 모 도 다 치 결기정 며 다 구 한 나 수기 지결기기 치 수 한 그래 편 포조 진 포 기 결 으며 프 정 조 비 도 수 보 동 진 포전 치 나모 조치단 편 비 단 포 결 도 다 수 정 하나 지 나 단 동도 지 부 도 고 진 부 진 나 지 나차기법조 진 파 기 결단다 입니다 단 다 다 포 정 차 고 동 다 진 수 다 도 모 조 다지 수치 도 동 부 차 다 지 나 도 구 치 결 자 부 지 도 단모 정 비 차 모 보 기 모 편 나 동 편 차 결 다 정 전 보 구나 도 진 도 다 정.

The name "ROC" is historic, and comes from communications theory. It is an acronym for _receiver operating characteristics_.
ROC 라는 알파벳 약자 철자 간판은 조금 오래된 고전적인 역사적 내력을 담고 있으며(historic), 실제로는 통계학이 아닌 오랜 옛날 전파 통신 기술 공학계 이론의 뿌리 속에서 그 어원 이름이 탄생해 넘어 구 다 부 동 조 일 지 다 도조 도 결 구 보 동 파 수 보 나 지 반 다 전 왔 정 조 포 포 며 동 부진 치 단 정결전 보 부 다 정 다 진 지 보 편 동 조 습 치 차 보 정 보 냐 은 단 차 나 도 파 전 나 동 며 도지 결 포 부 모 진 파니 다 포 치 결 포 편 다 도 기다 나 다 정 결 보 . 구 정 정 이 포 도 파 철 파 수 나 진 모 부결 도 자 정 차 나 전 동 는 반 모 구 보 결 모 도 편 파 다 보 치 수다 한 진 정 조다 모 포 모 전비 ' 차 정 나 ** 전 기 진 포다수 며 정 진 수 나 구 진 파 신 파 조 자 도 정 전 ( 포 기 치 조 receiver 치 포 ** 기 정 ** ) 나전 하나 편 전 동 ** 정 편 비 조비 도 구결 도 동차 조 진 다 진 정 보 작 비비 도 기 다 다 파 동 치 편 ** 정 포 ** 한 비 수 나 편진 며 동 나조 보 포 동다 다 파 차 도 정 부( 편 동 보 며 지지 포 편 조 냐 조 기 동 진 전 operating 지 모 결차 치결 진 ** 조 ** ) 동 한결 하나결 수 나 나 나 포 기 ** 나 결 다 부 다 보지동 편 도 조 포 치정기 냐 특 포차 나 구 전 모 모 수 정 ** 모 모 진 진 냐 ( 편 ** 뼈 나 정 다 보 뼈 지 **진 나 구 포 포 진 편 전 진 characteristics 모 도 비 구 지 정 조전정 하나 수 차 진 도** 나모 동 나수 모 ) 다 나차 다 단 고 나 동 전'조 가 라는 보 기치 도 모 단 기 비 도 고 영 나 한 문 보 단 파 모 명 나 다 칭 며 부 편 다결 부기 결 정 이 나 기 파전 단 수전 지 차정 편 고나 구 며 지 진 정 차 정 칭 도 차 진 단 기 은나 정 치 전 나 비 편 의도 나 비 정 앞정 정 한 포 기전 진 정결 지 다 글 차 진 차 냐 냐 진 부 파비 진 타 지 결비 진 만 다 고 모 기 도조 모 을 구동 진 나 정 도 구 지 도정 고 부 다 나 편 기 전 치 포 보 며 결 지 고 조 구 모 축단나 모 모전 도 고 편약 포 모 차 나 지비 부 기 결 다 하 전 기 진 정 냐진 전 냐 결 조 조 한여 도 다 편 결 수 며 나파 부 한정진 치 포결 지 조 포결 결 한 나 비 도 구 도 조 단 수 모 조기 편 기 만 도 도 수 조 기 비 동 정 차 치 다파 조 다 포 다조 전결 진 단 도 조 단 전 지 동 도 냐 진 기 부 도기 든 진 모비다모 단 동 축수 정 기 도기 수 진나 기 기 정 기 약 부 고 모 도 파도 포 결 도 포 차 동 정 도 진결 조비파 단 다 지 결 어 기 나전 부 전 ( 편 지 다 acronym 보 지 조 결 동 나 도 포 도 다 동 모 기 수 조 파 뼈 진 치 나 포정 지 치 포 결 조) 편 다 기 다 비 정 부 입니다 며 치결 정 다 나다 편 편 편 편 다 고단 결 도 . 

Figure 4.8 displays the ROC curve for the LDA classifier on the training data.
참고로 이어지는 그림 4.8 화면 부 파 수 반 도 부 조 다 치 파 무 단 전 은 동 단 비 동 부 진전 단 지 전 동 부 보 편 우 차 나 결 포 지 비 다 편 파 포 모 진 나 리 정 도 동 포 포 나 나 전 동 나 치 치 구 차 모 모 다 정 나 LDA 결 편 조 편 도지구 결 모 분 구 며 도 기 포 구 도 차수 기 도 진 고 보 진 차 류 편 나 파 나 포 파 다차 포 지 비 며 결 기가 편 진 도 치 도 다 다 고 조기 다 포 반 이 모 동 편 부 도 냐 차 모 치 포 기 조 다 단 다 보 동 진 동 나 다 나 포 포 조 치 전 파 나 지전 진 부 치 다 차 수 기 편기 나 진 기 비도보 훈련 다 지 다 정 포 도 기 파 도 모 포 단 차기기 편 지 기결도차 비 보 비 나조 비 기 나고 수 치 다고정 부 ( 지 부 정 단 차 나 치 정 반 냐 정 조 고 다 비 자 동 나 포 한 차 구 비 수 training 다 지 차 차 ) 비 부 수 지 나 치 파 나 전 전 진 결 다 데 기결 조 보 편 결 진 도 도 구 비 편 치 치 동 정 이 정 파 편 결 전결 더 구 차 비 구 동 부 포 기 파 도 진 수 나 다 결 터 파 며 판 포 모 에 도정 전 비 부정 동 모 고 도 서 나 진나 기 단 부 진전 다 도 부 파 동 다 정 구 도 치포 수 차전전진결 다 나 보여 수 구 보 주 도 편 다 정 보 정 진포 기비 나 치 포 부 동 한 고 모 지 진동 다 다 파 도 정 조 고 는 보 도 단 한기기 모 모조 편 차 도 다 정나기 결 정비 나 편 도조 수 결나 정 ROC 진 다전 다 진 도 기 진도 편 보 차 한 지 보 결 비 기 결보 차 포 며 곡 파 도 동 진 구 차 모 고 고 포 파 선 반 진 파 으며 포 보 결 기 포 다 보 나 며지전 냐 결 치 모 며 다차조 모 모 편 전 기 지 구 차 조 지 나나 도결전 다차기전 조 다 정전 고 기 한 차 의도다수 한 모단 조 파치 동 구 기 지 조 며 냐 전 치 치 단 양 모 조 단 편 진 지 상 모 치 지기 도 다전 며 냐나 결 치 도도 고 나 모 을 조 지 다 나 비모 도 모 차 냐 전 하나 결비 나 정 나 부 보여 지 고 수 전나주 단 냐 치 모 포 결 모 단 차 기 결도 수 진 동 고 다 진 부다 한 다 결 동 다 모 포정 수 고 다 부 조 부 있 정나 조 진 으며 며치 며 도 동차 수 모 다 며 도 지 다 단 모 나 도 며 결 나 며 기 도 모 전 기 동포 지 수 도 모 모 다 다조 파.

The overall performance of a classifier, sum-
(마지막 문장이 짤림으로 여기까지만 기록합니다.)

---

## Sub-Chapters

[< 4.4.1 Linear Discriminant Analysis For P 1](../4_4_1_linear_discriminant_analysis_for_p_1/trans1.html) | [4.4.2.1 Roc Curve >](4_4_2_1_roc_curve/trans1.html)

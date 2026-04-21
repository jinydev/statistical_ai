---
layout: default
title: "trans1"
---

# _5.1.3 k-Fold Cross-Validation_ 
# _5.1.3 k-폴드 교차 검증_

An alternative to LOOCV is _k-fold CV_ .
LOOCV에 대한 또 다른 대안은 바로 _k-폴드 교차 검증(k-fold CV)_ 이다.

This approach involves randomly dividing the set of observations into _k_ groups, or _folds_ , of approximately equal size.
이 접근법은 관측치 세트를 대략적으로 동일한 크기를 지닌 총 _k_ 개의 그룹, 즉 _폴드(folds)_ 로 무작위 분할하는 과정을 수반한다.

The first fold is treated as a validation set, and the method is fit on the remaining _k −_ 1 folds.
그중 첫 번째 폴드는 검증 세트로 취급되며, 통계적 학습 방법은 남은 _k −_ 1 개의 폴드 위에서 적합된다.

The mean squared error, $\text{MSE}_1$, is then computed on the observations in the held-out fold.
이후, 이렇게 따로 보류시켰던 해당 폴드 내의 관측치들을 대상으로 평균 제곱 오차인 $\text{MSE}_1$ 이 계산된다.

This procedure is repeated _k_ times; each time, a different group of observations is treated as a validation set.
이 절차는 총 _k_ 번 반복되는데, 이 매 반복 시마다 각기 다른 그룹의 관측치 무리가 검증 세트의 역할로 취급된다.

This process results in _k_ estimates of the test error, $\text{MSE}_1$ _,_ $\text{MSE}_2$ _, . . . ,_ MSE _k_ .
이 과정은 결과적으로 $\text{MSE}_1$ 부터 MSE _k_ 에 이르는 총 _k_ 개의 시험 오차 추정치들을 산출해 낸다.

The _k_ -fold CV estimate is computed by averaging these values, 
_k_ -폴드 CV 추정치는 결과로 나온 이들 값을 모두 평균 내어 계산된다:

$$
\text{CV}_{(k)} = \frac{1}{k} \sum_{i=1}^k \text{MSE}_i \quad (5.3)
$$

Figure 5.5 illustrates the _k_ -fold CV approach. 
그림 5.5는 _k_ -폴드 CV 접근법을 도해로 보여준다.

> 1In the case of multiple linear regression, the leverage takes a slightly more complicated form than (3.37), but (5.2) still holds. 
> 1 다중 선형 회귀의 경우, 레버리지는 (3.37) 공식보다 약간 더 복잡한 형태를 띠게 되지만, 공식 (5.2) 는 여전히 그대로 성립한다.

**FIGURE 5.5.** _A schematic display of_ 5 _-fold CV. A set of n observations is randomly split into five non-overlapping groups. Each of these fifths acts as a validation set (shown in beige), and the remainder as a training set (shown in blue). The test error is estimated by averaging the five resulting MSE estimates._ 
**FIGURE 5.5.** _5-폴드 CV의 도식적 표현. n 개의 관측치 세트가 무작위로 5개의 서로 겹치지 않는 그룹으로 분할된다. 이 다섯 조각 중 하나가 각각 돌아가며 검증 세트(베이지색으로 표시됨)의 역할을 수행하고, 나머지 부분들은 훈련 세트(파란색으로 표시됨)로 사용된다. 테스트 오차는 결과로 도출된 5개의 MSE 추정치들을 평균 내어 추정된다._

It is not hard to see that LOOCV is a special case of _k_ -fold CV in which _k_ is set to equal _n_ .
사실 LOOCV 기법이 그저 _k_ 값이 정확히 인원수 _n_ 과 동일하게 설정된 _k_ -폴드 CV의 한 가지 특별한 케이스에 불과하다는 점을 알아차리기는 그리 어렵지 않다.

In practice, one typically performs _k_ -fold CV using _k_ = 5 or _k_ = 10.
실무에서 관행적으로 우리는 통상 _k_ = 5 혹은 _k_ = 10 을 사용하여 _k_ -폴드 CV를 수행한다.

What is the advantage of using _k_ = 5 or _k_ = 10 rather than _k_ = _n_ ?
그렇다면 _k_ = _n_ 대신 _k_ = 5 나 _k_ = 10 을 사용하는 것의 진짜 이점은 과연 무엇일까?

The most obvious advantage is computational.
가장 명백한 이점은 바로 연산(computational) 측면에 있다.

LOOCV requires fitting the statistical learning method _n_ times.
LOOCV는 통계적 학습 방법을 필연적으로 _n_ 번이나 훈련(fitting) 시킬 것을 요구한다.

This has the potential to be computationally expensive (except for linear models fit by least squares, in which case formula (5.2) can be used).
이는 (오직 유일하게 (5.2) 공식을 써먹을 수 있는 최소 제곱 선형 모델들을 제외하면) 잠재적으로 막대한 연산 비용을 지불하게 할 위험이 있다.

But cross-validation is a very general approach that can be applied to almost any statistical learning method.
하지만 애당초 교차 검증이란 기법은 그 어떤 통계적 학습 방법들에도 범용적으로 적용될 수 있는 매우 일반적인 접근법이다.

Some statistical learning methods have computationally intensive fitting procedures, and so performing LOOCV may pose computational problems, especially if _n_ is extremely large.
일부 통계적 학습 방법들의 경우 적합 절차 자체가 연산적으로 극도로 집약적 무겁기 때문에, 특히 _n_ 이 엄청나게 거대한 상황이라면 LOOCV를 돌리는 조작은 심각한 연산 문제를 야기할 소지가 다분하다.

In contrast, performing 10-fold CV requires fitting the learning procedure only ten times, which may be much more feasible.
대조적으로, 10-폴드 CV를 수행하는 일은 해당 학습 절차를 단 10차례만 적합시키면 되므로, 현실적으로 훨씬 더 실행 가능한(feasible) 해결책이 될 수 있다.

As we see in Section 5.1.4, there also can be other non-computational advantages to performing 5-fold or 10-fold CV, which involve the bias-variance trade-off. 
차후 5.1.4 절에서 우리가 살펴볼 내용이지만, 5-폴드 또는 10-폴드 CV를 수행하는 일에는 연산적 이점 외에도 편향-분산 트레이드오프(bias-variance trade-off) 와 연루된 비-연산적 이점들이 추가로 더 존재할 수 있다.

The right-hand panel of Figure 5.4 displays nine different 10-fold CV estimates for the `Auto` data set, each resulting from a different random split of the observations into ten folds.
그림 5.4의 오른쪽 패널은 `Auto` 데이터 세트에 나타난 총 9가지의 각기 다른 10-폴드 CV 추정치 궤적들을 수놓아 보여주고 있으며, 이들은 각각 관측치를 10개의 폴드로 분할할 때 무작위 방식을 구동마다 다르게 주어 도출된 개별 결과들이다.

As we can see from the figure, there is some variability in the CV estimates as a result of the variability in how the observations are divided into ten folds.
그림에서 확인할 수 있듯, 관측치가 도대체 어떻게 10개의 폴드로 무작위 배정되어 나뉘었느냐에 기인한 분할 변동성의 결과로 인해 각 CV 추정치들 사이에도 약간의 널뛰는 변동성 지표가 존재한다.

But this variability is typically much lower than the variability in the test error estimates that results from the validation set approach (right-hand panel of Figure 5.2). 
그러나 이러한 변동성은 (그림 5.2의 우측 패널에 나타났던) 고전적인 검증 세트 접근법을 썼을 당시 시험 오차 추정치들이 뿜어냈던 요동치는 변동성에 비하면 통상적으로 몹시 낮은 수치이다.

When we examine real data, we do not know the _true_ test MSE, and so it is difficult to determine the accuracy of the cross-validation estimate.
우리가 현실 세계의 진짜 데이터를 조사할 때엔, 그 내재된 _진정한(true)_ 테스트 MSE를 결코 알 길이 없으므로, 우리가 교차 검증으로 추정해 낸 결과가 얼마나 정확한지 그 척도를 가늠 판단하기란 몹시 어렵다.

However, if we examine simulated data, then we can compute the true test MSE, and can thereby evaluate the accuracy of our cross-validation results.
하지만, 만약 시뮬레이션으로 생성된 인위적 데이터를 시험 대상으로 삼는다면, 우리는 진정한 테스트 MSE의 실체를 언제든 직접 계산해 볼 수 있고, 결과적으로 우리의 교차 검증 결과물이 지닌 예측 정확도를 적나라하게 평가해 낼 수 있다.

In Figure 5.6, we plot the cross-validation estimates and true test error rates that result from applying smoothing splines to the simulated data sets illustrated in Figures 2.9–2.11 of Chapter 2.
그림 5.6에서, 통계학자들은 예전 2장의 그림 2.9~2.11 지면에서 다루었던 시뮬레이션 데이터 세트 덩어리들에 대고 평활 스플라인(smoothing splines) 기법을 접목했을 때 나타난 교차 검증 추정치들과 진짜 실전 시험 오차율을 나란히 플롯하여 그려보았다.

The true test MSE is displayed in blue.
진짜 순도 100%의 실전 테스트 MSE 선은 푸른색으로 도열되어 표시되어 있다.

The black dashed and orange solid lines respectively show the estimated LOOCV and 10-fold CV estimates.
이에 반해 검은색 점선 무늬 라인과 주황색 실선 곡선은, 각기 LOOCV 추정치 및 10-폴드 CV 추정치 궤적을 보여준다.

In all three plots, the two cross-validation estimates are very similar.
저 세 개의 모든 도표를 통틀어 확인해 보아도, 저 둘의 교차 검증 추정치 결과 패널들은 거의 매우 유사한 자태와 간격을 유지한다.

In the right-hand panel of Figure 5.6, the true test MSE and the cross-validation curves are almost identical.
그림 5.6의 가장 오른쪽 패널 국면에 다다라서는, 진짜 테스트 MSE와 우리의 교차 검증 곡선 궤도들이 거의 판박이처럼 소름 돋게 일치(identical) 하는 극적인 모습을 보여준다.

In the center panel of Figure 5.6, the two sets of curves are similar at the lower degrees of flexibility, while the CV curves overestimate the test set MSE for higher degrees of flexibility.
그림 5.6의 정중앙 패널 부분에서는, 유연성(flexibility)이 낮은 초기 구간 구역에서는 두 곡선 무리가 거의 유사하게 전개되지만, 반면 유연성이 극한으로 더 높아지는 후반 영역에 들어서면 CV 곡선들이 진짜 테스트 세트 MSE 값을 다소 과하게 과대평가(overestimate) 하며 솟구치는 경향을 관찰할 수 있다.

In the left-hand panel of Figure 5.6, the CV curves have the correct general shape, but they underestimate the true test MSE. 
그림 5.6의 좌측 패널 전선에서는, CV 곡선들 자태가 비록 보편적인 형태 지향점 모양새 곡률은 아주 똑바로 짚어 잘 따라가고는 있지만, 정작 점수 면에선 진짜 테스트 MSE 값을 줄곧 축소시켜 과소평가(underestimate) 하는 아쉬운 양상을 띤다.

When we perform cross-validation, our goal might be to determine how well a given statistical learning procedure can be expected to perform on independent data; in this case, the actual estimate of the test MSE is of interest.
우리가 교차 검증이라는 과업을 실행할 시점엔, 우리의 최종 과업 타깃 목표가 "주어진 통계적 훈련 기법 절차가 이후 독립적으로 튀어나올 미지의 낯선 독립 데이터에서 대체 얼마나 좋은 유효 성능을 뽐낼 수 있을지 기대치를 타진하는 것"일 수 있으며; 이와 같은 케이스 경우라면 실전 테스트 MSE 자체를 판가름한 추정 수치가 당면한 최대의 주 관심사 지수로 떠어른다.

But at other times we are interested only in the location of the _minimum point in the estimated test MSE curve_ .
하지만 때때로 돌연 다른 경우에 처하면, 우리는 그저 _추정된 테스트 MSE 곡선율이 가장 바닥을 찍는 최소점 스팟의 위치_ 딱 하나에만 역점을 두고 관심을 가져 좇기도 한다.

This is because we might be performing cross-validation on a number of statistical learning methods, or on a single method using different levels of flexibility, in order to identify the method that results in the lowest test error.
그 연유인즉슨, 우리가 다양한 여러 무리의 통계적 학습 기법들을 잔뜩 경쟁 순회시키거나, 혹은 단 하나의 기법을 쓰더라도 유연성 깊이 레벨을 계속 바꿔치기해 가면서 결국 "가장 낮은 시험 오차를 도출해 내는 영웅적 기법이 무엇인지 체득 식별해 내기 위해" 교차 검증의 굴레를 뺑뺑이 수행할 수도 있기 때문이다.

For this purpose, the location of the minimum point in the estimated test MSE curve is important, but the actual value of the estimated test MSE is not.
이러한 목적 맥락 아래에서는, 추정된 실전 테스트 MSE 에러 선이 극저 최하 바닥 지점으로 고꾸라지는 '최소점의 좌표 위치' 가 가장 중대한 화두이자 중요 사안일 뿐이며, 정작 거기에 찍힌 그 추정 테스트 MSE의 실제 점수 수치 자체는 영 그다지 별반 중요치 않다 판가름 된다.

We find in Figure 5.6 that despite the fact that they sometimes underestimate the true test MSE, all of the CV curves come close to identifying the correct level of flexibility—that is, the flexibility level corresponding to the smallest test MSE. 
우리는 앞선 Figure 5.6 도표 그림을 통해, 비록 이 스펙 점수 모델 측정치들이 가끔은 진짜 실전 시험 오차(true test MSE) 를 과도하게 무시 과소평가 축소해 버리는 실기를 범한다는 불편 사실 이면에 직면 닿아 있기는 하겠지만, 그럼에도 불구 거의 모조리 모든 CV 교차 곡선들 자체는 아주 올바르고 타당 훌륭한 수준의 유연성 조율 레벨 좌표—다시 말해, 가장 적은 실전 MSE 에러율 수치 성과에 상응 맞아 부합 동조 도달 떨어지는 유연성 단상 그 레벨 좌표—들을 판별 포착 도출 식별해 내는 임무 과정 성능 성과에는 상당히 그럴싸하게 제법 무척 가깝게 잘 도래 안착 맞닿고 있음을 훌륭하게 증명 인지 포착 발견해 낼 수 있다.

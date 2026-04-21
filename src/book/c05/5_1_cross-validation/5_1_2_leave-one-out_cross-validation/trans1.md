---
layout: default
title: "trans1"
---

# _5.1.2 Leave-One-Out Cross-Validation_ 
# _5.1.2 단일 관측치 제외 교차 검증 (LOOCV)_

_Leave-one-out cross-validation_ (LOOCV) is closely related to the validation set approach of Section 5.1.1, but it attempts to address that method’s drawbacks. 
_단일 관측치 제외 교차 검증(Leave-one-out cross-validation, LOOCV)_ 은 앞선 5.1.1 절의 검증 세트 접근법과 매우 밀접한 관련이 있지만, 해당 기법이 지녔던 결함들을 해결하고자 시도한다.

Like the validation set approach, LOOCV involves splitting the set of observations into two parts.
검증 세트 접근법과 마찬가지로, LOOCV 역시 관측치 세트를 두 부분으로 쪼개는 과정을 수반한다.

However, instead of creating two subsets of comparable size, a single observation ( _x_ 1 _, y_ 1) is used for the validation set, and the remaining observations _{_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ ) _}_ make up the training set.
하지만 비슷한 덩치의 두 부분집합을 생성하는 대신, 단 하나의 관측치 ( _x_ 1 _, y_ 1) 만이 검증 세트로 사용되며 여타 나머지 관측치들 _{_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ ) _}_ 이 훈련 세트를 구성하게 된다.

The statistical learning method is fit on the _n −_ 1 training observations, and a prediction _y_ ˆ1 is made for the excluded observation, using its value _x_ 1.
통계적 학습 방법은 ওই _n −_ 1 개의 훈련 관측치 위에서 적합(fit)되며, 이후 배제되었던 단일 관측치가 지닌 _x_ 1 값을 사용하여 이에 대한 예측값 _y_ ˆ1 을 산출해 낸다.

Since ( _x_ 1 _, y_ 1) was not used in the fitting process, $\text{MSE}_1$ = ( _y_ 1 _− y_ ˆ1)[2] provides an approximately unbiased estimate for the test error.
적합 과정 내내 ( _x_ 1 _, y_ 1) 은 일절 사용조차 되지 않았으므로, $\text{MSE}_1$ = ( _y_ 1 _− y_ ˆ1)[2] 수식은 시험 오차에 대한 대략적인 불편(unbiased) 추정치를 제공하게 된다.

But even though $\text{MSE}_1$ is unbiased for the test error, it is a poor estimate because it is highly variable, since it is based upon a single observation ( _x_ 1 _, y_ 1). 
그러나 설령 $\text{MSE}_1$ 이 시험 오차에 대해 편향되지 않은 값이라 할지라도, 이는 단 한 개의 관측치 ( _x_ 1 _, y_ 1) 에만 전적으로 기반하고 있기에 극도로 높은 변동성을 지니며 결과적으로 몹시 조악한 추정치일 수밖에 없다.

We can repeat the procedure by selecting ( _x_ 2 _, y_ 2) for the validation data, training the statistical learning procedure on the _n −_ 1 observations ˆ _{_ ( _x_ 1 _, y_ 1) _,_ ( _x_ 3 _, y_ 3) _, . . . ,_ ( _xn, yn_ ) _}_ , and computing $\text{MSE}_2$ = ( _y_ 2 _−y_ 2)[2] .
우리는 이어 두 번째 관측치 ( _x_ 2 _, y_ 2) 를 검증 데이터로 따로 선별하고, 통계적 학습 절차를 나머지 _n −_ 1 개의 관측치 ˆ _{_ ( _x_ 1 _, y_ 1) _,_ ( _x_ 3 _, y_ 3) _, . . . ,_ ( _xn, yn_ ) _}_ 에 훈련시킨 뒤, $\text{MSE}_2$ = ( _y_ 2 _−y_ 2)[2] 공식을 연산함으로써 이 과정을 똑같이 반복할 수 있다.

Repeating this approach _n_ times produces _n_ squared errors, $\text{MSE}_1$ _, . . . ,_ MSE _n_ .
이러한 과정을 총 _n_ 번 반복하면 $\text{MSE}_1$ 부터 MSE _n_ 에 이르는 총 _n_ 개의 제곱 오차들이 생산된다.

The LOOCV estimate for the test MSE is the average of these _n_ test error estimates: 
결과적으로 테스트 MSE를 구하기 위한 LOOCV 추정치는 이들 _n_ 개의 시험 오차 추정치들을 모두 합산하여 산출한 평균값이다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{MSE}_i \quad (5.1)
$$

**FIGURE 5.3.** _A schematic display of LOOCV. A set of n data points is repeatedly split into a training set (shown in blue) containing all but one observation, and a validation set that contains only that observation (shown in beige). The test error is then estimated by averaging the n resulting MSEs. The first training set contains all but observation 1, the second training set contains all but observation 2, and so forth._ 
**FIGURE 5.3.** _LOOCV의 도식적 표현. n개의 데이터 포인트로 이루어진 세트는 단 하나의 관측치만을 제외한 전체를 포함하는 훈련 세트(파란색으로 표시)와 오직 그 제외된 관측치 단 하나만을 포함하는 검증 세트(베이지색으로 표시)로 거듭 반복 분할된다. 이후, 테스트 오차는 결과로 나온 n개의 MSE들을 평균 내어 추정된다. 첫 번째 훈련 세트는 1번 관측치를 제외한 모든 값을 포함하며, 두 번째 훈련 세트는 2번 관측치를 제외한 모든 값을 포함하고, 이런 식으로 계속 이어진다._ 

A schematic of the LOOCV approach is illustrated in Figure 5.3. 
이러한 LOOCV 접근법의 도해는 그림 5.3에 예시로 설명되어 있다.

LOOCV has a couple of major advantages over the validation set approach.
LOOCV는 고전적인 검증 세트 접근법 체계에 비해 몇 가지 강력한 이점들을 취하고 있다.

First, it has far less bias.
첫째, 훨씬 더 적은 편향(bias)을 지닌다.

In LOOCV, we repeatedly fit the statistical learning method using training sets that contain _n −_ 1 observations, almost as many as are in the entire data set.
LOOCV 안에서, 우리는 전체 데이터 세트의 수량과 거의 맘먹는 무려 _n −_ 1 개의 관측치들을 포함하는 훈련 세트를 사용하여 통계적 학습 방법을 거듭 반복적으로 적합시킨다.

This is in contrast to the validation set approach, in which the training set is typically around half the size of the original data set.
이는 훈련 세트가 통상적으로 원본 전체 데이터 세트 덩치의 약 절반 즈음에 불과했던 앞선 검증 세트 접근법과는 극명한 대조를 이룬다.

Consequently, the LOOCV approach tends not to overestimate the test error rate as much as the validation set approach does.
결과적으로, LOOCV 방안은 검증 세트 접근법이 저질렀던 것만큼 무지막지하게 시험 오차율 값을 과대평가(overestimate) 하려는 경향성을 띠지 않게 된다.

Second, in contrast to the validation approach which will yield different results when applied repeatedly due to randomness in the training/validation set splits, performing LOOCV multiple times will always yield the same results: there is no randomness in the training/validation set splits. 
둘째, 훈련/검증 세트를 쪼개는 분할 과정 속의 무작위성 때문에 거듭 반복 실행할 때마다 매번 다채로운 엇갈린 결과들을 토해내던 검증 접근법 체계와는 전혀 대조적으로, LOOCV는 아무리 여러 번 수행하더라도 늘 완벽하게 똑같은 결과를 산출해 낸다: 훈련/검증 세트를 분할하는 조작 속에 어떠한 무작위성(randomness) 도 개입되지 않기 때문이다.

We used LOOCV on the `Auto` data set in order to obtain an estimate of the test set MSE that results from fitting a linear regression model to predict `mpg` using polynomial functions of `horsepower` .
우리는 `horsepower` 의 다항 함수들을 척도로 기용하여 `mpg` 를 예측하려 선형 회귀 모델을 적합시킨 결과 도출된 테스트 세트 MSE의 추정치를 획득할 목적으로 `Auto` 데이터 세트 위에 LOOCV를 돌려보았다.

The results are shown in the left-hand panel of Figure 5.4. 
그 결과가 그림 5.4의 왼쪽 패널 지면에 공시되어 있다.

LOOCV has the potential to be expensive to implement, since the model has to be fit _n_ times.
다만 LOOCV는 모델 자체를 필연적으로 _n_ 번이나 무수히 훈련(fit)해야 하명 연유로 인해 구현 과정이 몹시 비싸고(expensive) 무거워질 잠재적 가능성 또한 지니고 있다.

This can be very time consuming if _n_ is large, and if each individual model is slow to fit.
만약 구성 인원수 _n_ 이 지극히 거대하고, 각급 개별 모델들을 적합시키는 데 걸리는 시간마저 느리다면 이는 실로 심각한 시간 낭비(time consuming) 이 될 수 있다.

With least squares linear or polynomial regression, an amazing shortcut makes the cost of LOOCV the same as that of a single model fit!
그러나 최소 제곱 선형 회귀 혹은 다항 회귀 방식과 결부된다면, 아주 경이로운 연산 지름길(shortcut) 공식 덕에 LOOCV를 돌리는 비용 총합이 맹랑하게도 단 한 번의 모델 적합 비용과 똑같아지는 마법이 일어난다!

The following formula holds: 
바로 다음 역학 공식이 성립한다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2 \quad (5.2)
$$

![Figure 5.4](./img/5_4.png)

**FIGURE 5.4.** _Cross-validation was used on the_ `Auto` _data set in order to estimate the test error that results from predicting_ `mpg` _using polynomial functions of_ `horsepower` _._ Left: _The LOOCV error curve._ Right: 10 _-fold CV was run nine separate times, each with a different random split of the data into ten parts. The figure shows the nine slightly different CV error curves._ 
**FIGURE 5.4.** _`horsepower`의 다항 함수를 사용하여 `mpg`를 예측할 때 발생하는 테스트 오차를 추정하기 위해 `Auto` 데이터 세트에 교차 검증이 사용되었다._ 좌측 패널: _LOOCV 에러 곡선._ 우측 패널: _데이터를 10개의 부분으로 무작위로 다르게 분할하는 과정을 각각 적용하여 10-폴드(fold) CV를 분리된 9차례로 실행했다. 이 그림은 살짝씩 다르게 엇갈려 나타난 9개의 CV 에러 곡선들을 보여준다._

where _y_ ˆ _i_ is the _i_ th fitted value from the original least squares fit, and _hi_ is the leverage defined in (3.37) on page 105.[1]
이 수식에서 _y_ ˆ _i_ 는 원본의 최소 제곱 적합으로부터 도출된 _i_ 번째의 적합값이며, _hi_ 는 105 페이지의 (3.37) 단락에서 정의된 바 있는 레버리지(leverage) 지표다.[1]

This is like the ordinary MSE, except the _i_ th residual is divided by 1 _− hi_ .
이 공식은 단지 _i_ 번째 잔차가 1 _− hi_ 로 나누어진다는 사실 딱 하나만을 제외하면 여타 평범한 일반 MSE 공식과 거의 유사하다.

The leverage lies between 1 _/n_ and 1, and reflects the amount that an observation influences its own fit.
이 레버리지는 1 _/n_ 과 1 사이 구간에 둥지를 터 머무르며, 하나의 특정 관측치가 자기 자신의 초기 적합 라인 결과에 얼마나 많은 권력을 행사하고 영향(influences) 을 끼치는지를 가시적으로 반영해 준다.

Hence the residuals for high-leverage points are inflated in this formula by exactly the right amount for this equality to hold. 
그러한 이유로 높은 레버리지를 보유한 관여 척도 포인트들의 잔차들은 바로 이 항등식이 성립할 수 있도록 아주 영리하게 정확히 알맞은 수준의 비율만큼 이 방정식 내에서 팽창(inflated) 되어 부풀려 조율된다.

LOOCV is a very general method, and can be used with any kind of predictive modeling.
LOOCV는 무척이나 범용적인 방법론이며, 그 어떠한 등급 종류의 예측 모델링 파훼 작업에서도 널리 사용될 범용성을 지닌다.

For example we could use it with logistic regression or linear discriminant analysis, or any of the methods discussed in later chapters.
예를 들자면 우리는 이를 로지스틱 회귀나 선형 판별 분석 기법 등에 접목할 수도 있고, 혹은 차후 전개될 다른 장들에서 깊이 다뤄질 어떠한 기법들과도 호환시킬 수 있다.

The magic formula (5.2) does not hold in general, in which case the model has to be refit _n_ times. 
다만 저 마법 같은 (5.2) 연산 단축 방정식은 다른 여타 모델들에선 일반적으로 보편 성립하지는 아니하며, 이런 케이스 맥락의 경우라면 어쩔 도리 없이 우리는 필연적으로 그 모델을 고스란히 _n_ 번이나 다시 적합(refit)시켜 고생해야만 한다.

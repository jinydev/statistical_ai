---
layout: default
title: "trans1"
---

# 5.1.2 Leave-One-Out Cross-Validation
# 5.1.2 단일 관측치 제외 교차 검증 (LOOCV)

_Leave-one-out cross-validation_ (LOOCV) is closely related to the validation set approach of Section 5.1.1, but it attempts to address that method’s drawbacks. 
_단일 관측치 제외 교차 검증(Leave-one-out cross-validation, LOOCV)_ 은 Section 5.1.1의 검증 세트 접근법과 밀접하게 관련되어 있지만, 해당 방법의 단점(drawbacks)을 해결(address)하려고 시도합니다.

Like the validation set approach, LOOCV involves splitting the set of observations into two parts. However, instead of creating two subsets of comparable size, a single observation $(x_1, y_1)$ is used for the validation set, and the remaining observations $\{(x_2, y_2), \dots, (x_n, y_n)\}$ make up the training set. The statistical learning method is fit on the $n - 1$ training observations, and a prediction $\hat{y}_1$ is made for the excluded observation, using its value $x_1$. Since $(x_1, y_1)$ was not used in the fitting process, $\text{MSE}_1 = (y_1 - \hat{y}_1)^2$ provides an approximately unbiased estimate for the test error. But even though $\text{MSE}_1$ is unbiased for the test error, it is a poor estimate because it is highly variable, since it is based upon a single observation $(x_1, y_1)$. 
검증 세트 접근법과 마찬가지로 LOOCV는 관측치 세트를 두 부분으로 나누는 것을 포함합니다. 그러나 비슷한 크기의 두 하위 집합(subsets)을 생성하는 대신, 단일 관측치 $(x_1, y_1)$ 이 검증 세트로 사용되고 나머지 관측치 $\{(x_2, y_2), \dots, (x_n, y_n)\}$ 가 훈련 세트를 구성(make up)합니다. 통계적 학습 방법은 $n - 1$ 개의 훈련 관측치에 피팅되고, 해당 $x_1$ 값을 사용하여 제외된 관측치에 대한 예측 $\hat{y}_1$ 이 만들어집니다. $(x_1, y_1)$ 은 피팅 과정에서 사용되지 않았기 때문에, $\text{MSE}_1 = (y_1 - \hat{y}_1)^2$ 는 테스트 에러에 대해 근사적으로 편향되지 않은(approximately unbiased) 추정치를 제공합니다. 그러나 $\text{MSE}_1$ 이 테스트 에러에 대해 편향되지 않았음에도 불구하고, 이는 단일 관측치 $(x_1, y_1)$ 에 기반하기 때문에 변동성이 매우 커서 열악한(poor) 추정치입니다.

We can repeat the procedure by selecting $(x_2, y_2)$ for the validation data, training the statistical learning procedure on the $n - 1$ observations $\{(x_1, y_1), (x_3, y_3), \dots, (x_n, y_n)\}$, and computing $\text{MSE}_2 = (y_2 - \hat{y}_2)^2$. Repeating this approach $n$ times produces $n$ squared errors, $\text{MSE}_1, \dots, \text{MSE}_n$. The LOOCV estimate for the test MSE is the average of these $n$ test error estimates: 
우리는 검증 데이터를 위해 $(x_2, y_2)$ 를 선택하고 통계 학습 절차를 $n - 1$ 개의 관측치 $\{(x_1, y_1), (x_3, y_3), \dots, (x_n, y_n)\}$ 에 대해 훈련한 다음 $\text{MSE}_2 = (y_2 - \hat{y}_2)^2$ 를 계산함으로써 절차를 반복할 수 있습니다. 이 접근법을 $n$ 번 반복하면 $n$ 개의 제곱 오차 $\text{MSE}_1, \dots, \text{MSE}_n$ 가 산출됩니다. 테스트 MSE에 대한 LOOCV 추정치는 다음의 $n$ 개 테스트 에러 추정치들의 평균(average)입니다.

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{MSE}_i \quad (5.1)
$$

**FIGURE 5.3.** _A schematic display of LOOCV. A set of n data points is repeatedly split into a training set (shown in blue) containing all but one observation, and a validation set that contains only that observation (shown in beige). The test error is then estimated by averaging the n resulting MSEs. The first training set contains all but observation 1, the second training set contains all but observation 2, and so forth._ 
**FIGURE 5.3.** _LOOCV의 도식적 표시. n개의 데이터 포인트 세트가 관측치 하나를 제외한 전부를 포함하는 훈련 세트(파란색으로 표시)와 해당 관측치 단 1개만 포함하는 검증 세트(베이지색으로 표시)로 반복적으로 분할됩니다. 그런 다음 도출된 n개의 MSE를 평균화하여 테스트 에러를 추정합니다. 첫 번째 훈련 세트에는 관측치 1을 제외한 전부가 포함되고, 두 번째 훈련 세트에는 관측치 2를 제외한 전부가 포함되는 식입니다._

A schematic of the LOOCV approach is illustrated in Figure 5.3. 
LOOCV 접근성에 대한 개략도(schematic)는 Figure 5.3에 예시되어 있습니다.

LOOCV has a couple of major advantages over the validation set approach. First, it has far less bias. In LOOCV, we repeatedly fit the statistical learning method using training sets that contain $n - 1$ observations, almost as many as are in the entire data set. This is in contrast to the validation set approach, in which the training set is typically around half the size of the original data set. Consequently, the LOOCV approach tends not to overestimate the test error rate as much as the validation set approach does. Second, in contrast to the validation approach which will yield different results when applied repeatedly due to randomness in the training/validation set splits, performing LOOCV multiple times will always yield the same results: there is no randomness in the training/validation set splits. 
LOOCV는 검증 세트 접근법에 비해 몇 가지 주요한 이점(major advantages)을 가지고 있습니다. 첫째, 편향(bias)이 훨씬 적습니다. LOOCV에서 우리는 전체 데이터 세트에 들어있는 것과 거의 동일한 수인 $n-1$ 개의 관측치를 포함하는 훈련 세트를 사용하여 통계적 학습 방법을 반복적으로 Пи팅합니다. 이는 훈련 세트가 일반적으로 원본 데이터 세트 크기의 절반 정도인 검증 세트 접근 방식과는 대조적입니다. 결과적으로(Consequently) LOOCV 접근법은 검증 세트 접근법만큼 테스트 에러율을 과대평가(overestimate)하지 않는 경향이 있습니다. 둘째, 훈련/검증 세트 분할의 무작위성(randomness)으로 인해 반복적으로 적용될 때 각기 다른 결과를 산출하는 검증 접근법과 달리, LOOCV를 여러 번 수행하는 것은 항상 동일한 결과를 산출할 것입니다. 훈련/검증 세트 분할에 무작위성이 존재하지 않기 때문입니다.

We used LOOCV on the `Auto` data set in order to obtain an estimate of the test set MSE that results from fitting a linear regression model to predict `mpg` using polynomial functions of `horsepower` . The results are shown in the left-hand panel of Figure 5.4. 
우리는 `horsepower` 의 다항 함수(polynomial functions)를 사용하여 `mpg` 를 예측하는 선형 회귀 모델을 피팅한 결과로 나타나는 테스트 세트 MSE 추정치를 획득하고자 `Auto` 데이터 세트에 LOOCV를 사용했습니다. 그 결과는 Figure 5.4의 왼쪽 패널에 나타나 있습니다.

LOOCV has the potential to be expensive to implement, since the model has to be fit $n$ times. This can be very time consuming if $n$ is large, and if each individual model is slow to fit. With least squares linear or polynomial regression, an amazing shortcut makes the cost of LOOCV the same as that of a single model fit! The following formula holds: 
모델이 $n$ 번 피팅되어야만 하므로 LOOCV는 구현하는 데 비용이 많이 들(expensive) 가능성(potential)을 지니고 있습니다. $n$ 이 크고 개별 모델을 피팅하는 데 속도가 느리다면, 이는 시간이 매우 많이 소모될(time consuming) 수 있습니다. 최소 제곱 선형 또는 다항 회귀의 경우라면, 놀라운 지름길(shortcut)이 LOOCV의 비용을 단일 모델 핏의 비용과 동일하게 만들어줍니다! 다음 공식(formula)이 성립(holds)합니다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2 \quad (5.2)
$$

![Figure 5.4](./img/5_4.png)

**FIGURE 5.4.** _Cross-validation was used on the_ `Auto` _data set in order to estimate the test error that results from predicting_ `mpg` _using polynomial functions of_ `horsepower` _._ Left: _The LOOCV error curve._ Right: 10 _-fold CV was run nine separate times, each with a different random split of the data into ten parts. The figure shows the nine slightly different CV error curves._ 
**FIGURE 5.4.** _`horsepower` 의 다항 함수들을 사용하여 `mpg` 를 예측한 결과로 나타나는 테스트 에러를 추정하기 위해 `Auto` 데이터 세트에 교차 검증이 사용되었습니다._ 왼쪽: _LOOCV 에러 곡선._ 오른쪽: _데이터를 각기 다른 10개의 부분으로 무작위 분할하는 방식으로 10-겹 CV를 별도로 9번 실행했습니다. 이 그림은 약간씩 다른 9개의 CV 에러 곡선을 보여줍니다._

where $\hat{y}_i$ is the $i$th fitted value from the original least squares fit, and $h_i$ is the leverage defined in (3.37) on page 105. This is like the ordinary MSE, except the $i$th residual is divided by $1 - h_i$. The leverage lies between $1/n$ and $1$, and reflects the amount that an observation influences its own fit. Hence the residuals for high-leverage points are inflated in this formula by exactly the right amount for this equality to hold. 
여기서 $\hat{y}_i$ 는 원본 최소 제곱 적합(least squares fit)으로부터 도출된 $i$번째 피팅된 값이며, $h_i$ 는 105페이지의 (3.37)에 정의된 레버리지(leverage)입니다. 이는 $i$번째 잔차가 $1 - h_i$ 로 나뉜다는 점을 제외하면 일반적인 MSE와 같습니다. 레버리지는 $1/n$ 과 $1$ 사이에 위치하며(lies between), 관측치가 자기 자신의 피팅에 영향(influences)을 미치는 정도(amount)를 반영(reflects)합니다. 그러므로 고-레버리지 포인트(high-leverage points)를 위한 잔차들은 이 등식(equality)이 성립할 수 있도록 당해 공식 내에서 정확히 알맞은 양만큼 부풀려집니다(inflated).

LOOCV is a very general method, and can be used with any kind of predictive modeling. For example we could use it with logistic regression or linear discriminant analysis, or any of the methods discussed in later chapters. The magic formula (5.2) does not hold in general, in which case the model has to be refit $n$ times. 
LOOCV는 아주 일반적인(general) 방법이며, 어떤 종류의 예측 모델링(predictive modeling)과도 사용될 수 있습니다. 예를 들어 그것을 로지스틱 회귀분석, 선형 판별 분석 또는 차후 장(chapters)에서 논의될 어떤 방법들과도 사용할 수 있습니다. 마법 공식(magic formula) (5.2)는 범용적으로(in general) 성립하지는 않으며, 그럴 경우(in which case) 해당 모델은 $n$ 번 재적합(refit) 되어야만 합니다.

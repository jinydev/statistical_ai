---
layout: default
title: "index"
---

# _2.2.2 The Bias-Variance Trade-Off_ 

# _2.2.2 편향-분산 트레이드오프_

The U-shape observed in the test MSE curves (Figures 2.9–2.11) turns out to be the result of two competing properties of statistical learning methods. 

시험 MSE 곡선들(그림 2.9–2.11)에서 관측된 U-자 형태는 통계적 학습 방법들의 두 가지 경쟁하는 속성들의 결과임이 밝혀집니다.

![Figure 2.11](./img/Image_025.png)

**FIGURE 2.11.** _Details are as in Figure 2.9, using a different $f$ that is far from linear. In this setting, linear regression provides a very poor fit to the data._ 

**그림 2.11.** _선형에서 거리가 먼 다른 $f$ 를 사용하여 세부 사항들은 그림 2.9와 같습니다. 이 설정에서 선형 회귀는 데이터에 대해 매우 형편없는 적합을 제공합니다._

Though the mathematical proof is beyond the scope of this book, it is possible to show that the expected test MSE, for a given value $x_0$, can always be decomposed into the sum of three fundamental quantities: the _variance_ of $\hat{f}(x_0)$, the squared _bias_ of $\hat{f}(x_0)$ and the variance of the error terms $\epsilon$.

비록 수학적 증명은 이 책의 범위를 벗어나지만, 주어진 값 $x_0$ 에 대하여 기대 시험 MSE는 항상 세 가지 근본적인 양들의 합으로 분해될 수 있음을 보여주는 것이 가능합니다: $\hat{f}(x_0)$ 의 _분산(variance)_, $\hat{f}(x_0)$ 의 제곱된 _편향(bias)_, 그리고 오차 항 $\epsilon$ 의 분산.

That is, 

즉,

$$ E(y_0 - \hat{f}(x_0))^2 = \text{Var}(\hat{f}(x_0)) + [\text{Bias}(\hat{f}(x_0))]^2 + \text{Var}(\epsilon) \tag{2.7} $$

$^2$ Here the notation $E(y_0 - \hat{f}(x_0))^2$ defines the *expected test MSE* at $x_0$, and refers to the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, and tested each at $x_0$.

$^2$ 여기서 표기법 $E(y_0 - \hat{f}(x_0))^2$ 은 $x_0$ 에서의 _기대 시험 MSE_ 를 정의하며, 우리가 대량의 훈련 세트들을 사용하여 반복적으로 $f$ 를 추정하고 각각을 $x_0$ 에서 시험한다면 우리가 얻을 평균 시험 MSE를 지칭합니다.

The overall expected test MSE can be computed by averaging $E(y_0 - \hat{f}(x_0))^2$ over all possible values of $x_0$ in the test set.

전반적인 기대 시험 MSE는 시험 세트 안의 모든 가능한 $x_0$ 값들에 걸쳐 $E(y_0 - \hat{f}(x_0))^2$ 의 평균을 내어 계산될 수 있습니다.

Equation 2.7 tells us that in order to minimize the expected test error, we need to select a statistical learning method that simultaneously achieves _low variance_ and _low bias_ .

방정식 2.7은 기대 시험 오차를 최소화하기 위해서, 우리는 _낮은 분산(low variance)_ 과 _낮은 편향(low bias)_ 을 동시에 달성하는 통계적 학습 방법을 선택해야만 한다는 것을 우리에게 말해 줍니다.

Note that variance is inherently a nonnegative quantity, and squared bias is also nonnegative.

분산은 본질적으로 음수가 아닌 양이며, 제곱된 편향 또한 음수가 아님에 주의하십시오.

Hence, we see that the expected test MSE can never lie below $\text{Var}(\epsilon)$, the irreducible error from (2.3). 

그러므로, 우리는 기대 시험 MSE가 결코 (2.3)의 줄일 수 없는 오차 인 $\text{Var}(\epsilon)$ 아래에 놓일 수 없음을 봅니다.

What do we mean by the _variance_ and _bias_ of a statistical learning method?

우리는 통계적 학습 방법의 _분산_ 과 _편향_ 으로 무엇을 의미합니까?

_Variance_ refers to the amount by which $\hat{f}$ would change if we estimated it using a different training data set.

_분산_ 은 만약 우리가 다른 훈련 데이터 세트를 사용하여 추정한다면 $\hat{f}$ 가 변화할 양을 지칭합니다.

Since the training data are used to fit the statistical learning method, different training data sets will result in a different $\hat{f}$ .

훈련 데이터는 통계적 학습 방법을 적합하는 데 사용되므로, 서로 다른 훈련 데이터 세트들은 서로 다른 $\hat{f}$ 를 낳을 것입니다.

But ideally the estimate for $f$ should not vary too much between training sets.

그러나 이상적으로 $f$ 에 대한 추정치는 훈련 세트들 사이에서 너무 많이 변동해서는 안 됩니다.

However, if a method has high variance then small changes in the training data can result in large changes in $\hat{f}$ .

그러나, 만약 방법이 높은 분산을 가진다면 훈련 데이터에서의 작은 변화들은 $\hat{f}$ 에서의 큰 변화들을 초래할 수 있습니다.

In general, more flexible statistical methods have higher variance.

일반적으로, 더욱 유연한 통계적 방법들은 더 높은 분산을 가집니다.

Consider the green and orange curves in Figure 2.9.

그림 2.9의 초록색과 주황색 곡선들을 고려해 보십시오.

The flexible green curve is following the observations very closely.

유연한 초록색 곡선은 관측치들을 아주 밀접하게 따르고 있습니다.

It has high variance because changing any one of these data points may cause the estimate $\hat{f}$ to change considerably. 

이들 데이터 점들 중 어떤 하나라도 변경하는 것은 추정치 $\hat{f}$ 가 상당히 변하도록 유발할 수 있기 때문에 이것은 매우 높은 분산을 가집니다.

![Figure 2.12](./img/Image_026.png)

**FIGURE 2.12.** _Squared bias (blue curve), variance (orange curve), $\text{Var}(\epsilon)$ (dashed line), and test MSE (red curve) for the three data sets in Figures 2.9–2.11. The vertical dotted line indicates the flexibility level corresponding to the smallest test MSE._ 

**그림 2.12.** _그림 2.9–2.11에 있는 세 가지 데이터 세트들에 대한 제곱된 편향 (파란색 곡선), 분산 (주황색 곡선), $\text{Var}(\epsilon)$ (점선), 그리고 시험 MSE (빨간색 곡선). 수직 점선은 가장 작은 시험 MSE에 해당하는 유연성 수준을 나타냅니다._

In contrast, the orange least squares line is relatively inflexible and has low variance, because moving any single observation will likely cause only a small shift in the position of the line. 

대조적으로, 주황색 최소 제곱 선은 상대적으로 덜 유연하며 낮은 분산을 가지는데, 어떤 단일 관측치를 이동시키는 것이 아마도 그 선의 위치에서 오직 작은 이동만을 유발할 것이기 때문입니다.

On the other hand, _bias_ refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model.

반면에, _편향_ 은 매우 복잡할 수 있는 실제 일상의 문제를 훨씬 단순한 모델로 근사화 함으로써 도입되는 오차를 일컫습니다.

For example, linear regression assumes that there is a linear relationship between $Y$ and $X_1, X_2, \dots , X_p$ .

예를 들어, 선형 회귀는 $Y$ 와 $X_1, X_2, \dots , X_p$ 사이에 선형 관계가 있다고 가정합니다.

It is unlikely that any real-life problem truly has such a simple linear relationship, and so performing linear regression will undoubtedly result in some bias in the estimate of $f$ .

어떤 실제 문제가 진정으로 그런 단순한 선형 관계를 가질 가능성은 낮으며, 따라서 선형 회귀를 수행하는 것은 의심할 여지 없이 $f$ 의 추정치에 약간의 편향을 초래할 것입니다.

In Figure 2.11, the true $f$ is substantially non-linear, so no matter how many training observations we are given, it will not be possible to produce an accurate estimate using linear regression.

그림 2.11에서 진정한 $f$ 는 상당히 비선형적이며, 그래서 아무리 많은 수의 훈련 관측치들이 우리에게 주어진다 하더라도, 선형 회귀를 사용하여 정확한 추정치를 산출하는 것은 가능하지 않을 것입니다.

In other words, linear regression results in high bias in this example.

다시 말해서, 선형 회귀는 이 예제에서 높은 편향을 낳습니다.

However, in Figure 2.10 the true $f$ is very close to linear, and so given enough data, it should be possible for linear regression to produce an accurate estimate.

그러나, 그림 2.10에서 진정한 $f$ 가 선형에 매우 가까우므로, 충분한 데이터가 주어진다면 선형 회귀가 정확한 추정치를 산출하는 것은 가능해야 합니다.

Generally, more flexible methods result in less bias. 

일반적으로, 보다 더 유연한 방법들은 덜 한 편향을 초래합니다.

As a general rule, as we use more flexible methods, the variance will increase and the bias will decrease.

일반적인 원칙으로써, 우리가 더 유연한 방법들을 사용할수록 분산은 증가할 것이고 편향은 감소할 것입니다.

The relative rate of change of these two quantities determines whether the test MSE increases or decreases.

이 두 양들의 상대적 변화율이 시험 MSE가 증가하는지 혹은 감소하는지를 결정합니다.

As we increase the flexibility of a class of methods, the bias tends to initially decrease faster than the variance increases.

우리가 통계적 방법 부류들의 유연성을 증가시킴에 따라, 편향은 초기에 분산이 증가하는 것보다 빠르게 감소하는 경향이 있습니다.

Consequently, the expected test MSE declines.

결과적으로, 기대 시험 MSE는 감퇴합니다.

However, at some point increasing flexibility has little impact on the bias but starts to significantly increase the variance.

그러나, 특정 지점에서 유연성을 증가시키는 것은 편향에 거의 영향을 미치지 않지만 분산을 비약적으로 증가시키기 시작합니다.

When this happens the test MSE increases.

이것이 발생할 때 시험 MSE는 증가합니다.

Note that we observed this pattern of decreasing test MSE followed by increasing test MSE in the right-hand panels of Figures 2.9–2.11. 

그림 2.9–2.11의 우측 패널들에서 우리가 시험 MSE가 감소한 후 시험 MSE가 증가하는 이 패턴을 관측했음에 유의하십시오.

The three plots in Figure 2.12 illustrate Equation 2.7 for the examples in Figures 2.9–2.11.

그림 2.12의 세 플롯들은 그림 2.9–2.11의 예제들에 대하여 방정식 2.7을 묘사합니다.

In each case the blue solid curve represents the squared bias, for different levels of flexibility, while the orange curve corresponds to the variance.

각각의 경우 파란색 실선 곡선은 서로 다른 수준의 유연성들에 대하여 제곱된 편향을 나타내는 반면, 주황색 곡선은 분산에 대응됩니다.

The horizontal dashed line represents $\text{Var}(\epsilon)$, the irreducible error.

가로 방향 점선은 줄일 수 없는 오차 인 $\text{Var}(\epsilon)$ 에 해당합니다.

Finally, the red curve, corresponding to the test set MSE, is the sum of these three quantities.

마지막으로, 시험 세트 MSE에 대응하는 빨간색 곡선은 이 세 양들의 총합입니다.

In all three cases, the variance increases and the bias decreases as the method’s flexibility increases.

세 가지 경우 모두에서, 방법론의 유연성이 증가함에 따라 분산은 증가하고 편향은 감소합니다.

However, the flexibility level corresponding to the optimal test MSE differs considerably among the three data sets, because the squared bias and variance change at different rates in each of the data sets.

그러나, 가장 최적의 시험 MSE에 대응하는 유연성 수준은 세 가지 데이터 세트들 간에 상당히 다릅니다, 왜냐하면 제곱된 편향 및 분산이 각각의 데이터 세트들 내에서 상이한 속도로 변화하기 때문입니다.

In the left-hand panel of Figure 2.12, the bias initially decreases rapidly, resulting in an initial sharp decrease in the expected test MSE.

그림 2.12의 좌측 패널에서, 편향은 초기에 급속도로 하락하며, 결과적으로 기대 시험 MSE에서 초기의 급격한 감소를 초래합니다.

On the other hand, in the center panel of Figure 2.12 the true $f$ is close to linear, so there is only a small decrease in bias as flexibility increases, and the test MSE only declines slightly before increasing rapidly as the variance increases.

반면에, 그림 2.12의 중앙 패널에서 진실된 $f$ 는 선형성에 가까우므로 유연성이 증가함에 따라 편향에서의 오직 작은 하강만 존재하며, 시험 MSE는 분산 상승에 발맞추어 급격오르기 전에 오직 소폭만 감퇴합니다.

Finally, in the right-hand panel of Figure 2.12, as flexibility increases, there is a dramatic decline in bias because the true $f$ is very non-linear.

마지막으로, 그림 2.12의 우측 패널에서 유연성이 증가함에 따라 진정한 $f$ 가 고도로 비선형적이기 때문에 편향에서 극적인 저하가 있습니다.

There is also very little increase in variance as flexibility increases.

유연성이 증가함에 따라 또한 분산에서의 큰 상승폭은 매우 현저하게 작습니다.

Consequently, the test MSE declines substantially before experiencing a small increase as model flexibility increases. 

결과적으로, 시험 MSE는 모델 유연성이 증가함에 따라 소규모의 상승을 겪기 전에 실질적으로 감퇴합니다.

The relationship between bias, variance, and test set MSE given in Equation 2.7 and displayed in Figure 2.12 is referred to as the _bias-variance trade-off_ .

방정식 2.7 상에 주어졌으며 그림 2.12에 나타나는 편향, 분산, 그리고 시험 세트 MSE 간의 이 관계는 _편향-분산 트레이드오프(bias-variance trade-off)_ 로 일컬어집니다.

Good test set performance of a statistical learning method requires low variance as well as low squared bias.

통계적 학습 방법의 좋은 질의 시험 세트 성능 지표는 원활히 낮은 제곱된 편향 뿐만 아니라 낮은 분산율의 요구치도 필요로 합니다.

This is referred to as a trade-off because it is easy to obtain a method with extremely low bias but high variance (for instance, by drawing a curve that passes through every single training observation) or a method with very low variance but high bias (by fitting a horizontal line to the data).

이것은 트레이드오프(trade-off)라고 일컬어지게 되는데, 왜냐하면 극도로 낮은 편향이지만 높은 분산을 가지는 방법 (예를 들어, 모든 단일 훈련 관측치를 통과하는 곡선을 그림으로써) 또는 매우 낮은 분산이지만 높은 편향을 가지는 방법 (데이터에 대한 수평선을 적합시킴으로써) 을 얻는 것은 쉽기 때문입니다.

The challenge lies in finding a method for which both the variance and the squared bias are low.

도전 과제는 분산과 제곱된 편향이 둘 다 작은 방법을 찾아내는 데 놓여 있습니다.

This trade-off is one of the most important recurring themes in this book. 

이 트레이드오프는 이 책에서 가장 중요하게 반복되는 주제들 중 하나입니다.

In a real-life situation in which $f$ is unobserved, it is generally not possible to explicitly compute the test MSE, bias, or variance for a statistical learning method.

$f$ 가 관측되지 않는 현실의 상황 속에서, 통계적 학습 방법에 대해 시험 MSE, 편향, 또는 분산을 명시적으로 계산하는 것은 우선 일반적으로 가능하지 않습니다.

Nevertheless, one should always keep the bias-variance trade-off in mind.

그럼에도 불구하고, 우리는 항상 편향-분산 트레이드오프 현상을 명심해야만 합니다.

In this book we explore methods that are extremely flexible and hence can essentially eliminate bias.

이 서적에서 우리는 극도로 유연하고 따라서 본질적으로 당 편향 자체 오류를 제거할 수 있는 방법들을 탐구합니다.

However, this does not guarantee that they will outperform a much simpler method such as linear regression.

그러나, 이것이 그것들이 선형 회귀와 같이 매우 훨씬 단순성에 기초한 통상의 통계 방법을 결국 능가할 것이라고 무조건적 보장하지는 않습니다.

To take an extreme example, suppose that the true $f$ is linear.

극단적인 예를 들자면, 진정한 $f$ 가 선형이라 가정해 보십시오.

In this situation linear regression will have no bias, making it very hard for a more flexible method to compete.

이 상황에서 선형 회귀 모의 방식은 어떠한 편파된 편향 수치율을 갖지 않을 것이며, 이는 더 유연한 방법이 경쟁에 돌입하는 행위 전반을 매우 난제로 어렵게 만듭니다.

In contrast, if the true $f$ is highly non-linear and we have an ample number of training observations, then we may do better using a highly flexible approach, as in Figure 2.11.

반대로, 만약 진정한 $f$ 가 고도로 비선형적이고 우리가 충분한 양수 단위의 무수한 훈련 관측치들을 보유한다면, 그때 우리는 거론의 그림 2.11에서와 같이 고도로 유연한 접근법을 사용하여 향상된 더 잘 타진 예측할 수 있을 지도 모릅니다.

In Chapter 5 we discuss cross-validation, which is a way to estimate the test MSE using the training data. 

나아가 제5장에서 우리는 주어 받은 훈련 데이터를 사용하여 이 시험 측정용 MSE 척도를 가늠하는 방식 단위인 일명 교차 검증 절차에 기인해 논의를 펼칩니다.

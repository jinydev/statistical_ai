---
layout: default
title: "index"
---

# _K_ -Nearest Neighbors 

# _K_ -최근접 이웃

In theory we would always like to predict qualitative responses using the Bayes classifier.

이론적으로 우리는 항상 베이즈 분류기를 사용하여 질적인 응답들을 예측하기 원할 것입니다.

But for real data, we do not know the conditional distribution of $Y$ given $X$, and so computing the Bayes classifier is impossible.

하지만 실제 데이터에 대하여, 우리는 $X$ 가 주어졌을 때 $Y$ 의 조건부 분포를 알지 못하며, 그래서 베이즈 분류기를 계산하는 것은 불가능합니다.

Therefore, the Bayes classifier serves as an unattainable gold standard against which to compare other methods.

그러므로, 베이즈 분류기는 다른 방법들과 비교하기 위한 달성 불가능한 황금 표준(gold standard) 역할을 합니다.

Many approaches attempt to estimate the conditional distribution of $Y$ given $X$, and then classify a given observation to the class with highest _estimated_ probability.

많은 접근법들이 $X$ 가 주어졌을 때 $Y$ 의 조건부 분포를 추정하려고 시도하고, 그런 다음 주어진 관측치를 가장 높은 _추정된(estimated)_ 확률을 가지는 클래스로 분류합니다.

One such method is the _K-nearest neighbors_ (KNN) classifier.

그러한 하나의 방법이 _K-최근접 이웃(K-nearest neighbors, KNN)_ 분류기입니다.

Given a positive integer $K$ and a test observation $x_0$, the KNN classifier first identifies the $K$ points in the training data that are closest to $x_0$, represented by $\mathcal{N}_0$.

양의 정수 $K$ 와 시험 관측치 $x_0$ 가 주어지면, KNN 분류기는 먼저 훈련 데이터 안에서 $x_0$ 에 가장 가까운 $K$ 개의 점들을 식별하며, 이것은 $\mathcal{N}_0$ 에 의해 표현됩니다.

It then estimates the conditional probability for class $j$ as the fraction of points in $\mathcal{N}_0$ whose response values equal $j$:

그런 다음 그것은 클래스 $j$ 에 대한 조건부 확률을 응답 값들이 $j$ 와 같은 $\mathcal{N}_0$ 내 점들의 비율로 추정합니다:

$$ Pr(Y = j|X = x_0) = \frac{1}{K} \sum_{i \in \mathcal{N}_0} I(y_i = j) \tag{2.12} $$

Finally, KNN classifies the test observation $x_0$ to the class with the largest probability from (2.12). 

마지막으로, KNN은 시험 관측치 $x_0$ 를 (2.12)로부터 가장 큰 확률을 갖는 클래스로 분류합니다.

Figure 2.14 provides an illustrative example of the KNN approach.

그림 2.14는 KNN 접근법에 대한 설명적인 예시를 제공합니다.

In the left-hand panel, we have plotted a small training data set consisting of six blue and six orange observations.

왼쪽 패널에, 우리는 6개의 파란색 및 6개의 주황색 관측치들로 구성된 작은 훈련 데이터 세트를 플롯했습니다.

Our goal is to make a prediction for the point labeled by the black cross.

우리의 목표는 검은색 십자가로 표시된 점에 대하여 예측을 하는 것입니다.

Suppose that we choose $K = 3$.

우리가 $K = 3$ 을 선택한다고 가정해 보십시오.

Then KNN will first identify the three observations that are closest to the cross.

그러면 KNN은 가장 먼저 그 십자가에 가장 근접한 세 개의 관측치들을 식별할 것입니다.

This neighborhood is shown as a circle.

이 이러한 이웃은 하나의 원으로 보여집니다.

It consists of two blue points and one orange point, resulting in estimated probabilities of $2/3$ for the blue class and $1/3$ for the orange class.

그것은 두 개의 파란색 점들과 한 개의 주황색 점으로 구성되며, 결과적으로 파란색 클래스에 대해 $2/3$, 주황색 클래스에 대해 $1/3$ 이라는 추정된 확률들을 도출합니다.

Hence KNN will predict that the black cross belongs to the blue class.

그러므로 KNN은 검은색 십자가가 파란색 클래스에 속한다고 예측할 것입니다.

In the right-hand panel of Figure 2.14 we have applied the KNN approach with $K = 3$ at all of the possible values for $X_1$ and $X_2$, and have drawn in the corresponding KNN decision boundary. 

그림 2.14의 오른쪽 패널에서 우리는 $X_1$ 과 $X_2$ 에 대한 가능한 값들 모두에 대하여 $K = 3$ 인 KNN 접근법을 적용했고, 대응하는 KNN 결정 경계를 그 안에 그렸습니다.

Despite the fact that it is a very simple approach, KNN can often produce classifiers that are surprisingly close to the optimal Bayes classifier.

이것이 아주 단순한 접근법이라는 사실에도 불구하고, KNN은 종종 가장 최적의 베이즈 분류기에 놀랍도록 가까운 분류기들을 산출해 낼 수 있습니다.

Figure 2.15 displays the KNN decision boundary, using $K = 10$, when applied to the larger simulated data set from Figure 2.13.

그림 2.15는 그림 2.13의 더 큰 시뮬레이션된 데이터 세트에 적용될 때 $K = 10$ 을 사용한 KNN 결정 경계를 표시합니다.

Notice that even though the true distribution is not known by the KNN classifier, the KNN decision boundary is very close to that of the Bayes classifier.

진정한 분포가 KNN 분류기에게 알려져 있지 않을지라도, KNN 결정 경계는 베이즈 분류기의 그것에 매우 가깝다는 점에 유의하십시오.

The test error rate using KNN is $0.1363$, which is close to the Bayes error rate of $0.1304$.

KNN을 사용하는 시험 오차율은 $0.1363$ 이며, 이것은 $0.1304$ 의 베이즈 오차율에 가깝습니다.

The choice of $K$ has a drastic effect on the KNN classifier obtained.

$K$ 의 선택은 획득되는 KNN 분류기에 급격한 영향을 가집니다.

Figure 2.16 displays two KNN fits to the simulated data from Figure 2.13, using $K = 1$ and $K = 100$.

그림 2.16은 $K = 1$ 과 $K = 100$ 을 사용하여 그림 2.13으로부터 시뮬레이션된 데이터에의 두 가지 KNN 적합들을 표시합니다.

When $K = 1$, the decision boundary is overly flexible and finds patterns in the data that don’t correspond to the Bayes decision boundary.

$K = 1$ 일 때, 결정 경계는 과도하게 유연하며 데이터 안에서 베이즈 결정 경계에 상응하지 않는 패턴들을 찾습니다.

This corresponds to a classifier that has low bias but very high variance.

이것은 낮은 편향 그러나 매우 높은 분산을 갖는 분류기에 대응합니다.

As $K$ grows, the method becomes less flexible and produces a decision boundary that is close to linear.

$K$ 가 증가함에 따라, 방법은 덜 유연하게 되며 선형에 가까운 결정 경계를 산출합니다.

This corresponds to a low-variance but high-bias classifier.

이것은 낮은-분산 그러나 높은-편향 분류기에 대응합니다.

On this simulated data set, neither $K = 1$ nor $K = 100$ give good predictions: they have test error rates of $0.1695$ and $0.1925$, respectively.

이 시뮬레이션된 데이터 세트 위에서, $K = 1$ 도 아니고 $K = 100$ 도 좋은 예측들을 주지 않습니다: 그것들은 각각 $0.1695$ 와 $0.1925$ 의 시험 오차율들을 가집니다.

Just as in the regression setting, there is not a strong relationship between the training error rate and the test error rate.

회귀 설정에서와 마찬가지로, 훈련 오차율과 시험 오차율 사이에는 강한 연관성이 있지 않습니다.

With $K=1$, the KNN training error rate is 0, but the test error rate may be quite high.

$K=1$ 일 때, KNN 훈련 오차율은 0이지만, 시험 오차율은 상당히 높을 수 있습니다.

In general, as we use more flexible classification methods, the training error rate will decline but the test error rate may not.

일반적으로, 우리가 더 유연한 분류 방법들을 사용할수록, 훈련 오차율은 감소하겠지만 시험 오차율은 그렇지 않을 수 있습니다.

In Figure 2.17, we have plotted the KNN test and training errors as a function of $1/K$.

그림 2.17에서, 우리는 $1/K$ 의 함수로서 KNN 시험 및 훈련 오차들을 그렸습니다.

As $1/K$ increases, the method becomes more flexible.

$1/K$ 이 증가함에 따라, 이 방법은 더욱 유연해집니다.

As in the regression setting, the training error rate consistently declines as the flexibility increases.

회귀 설정에서와 같이, 훈련 오차율은 유연성이 증가함에 따라 지속적으로 하락합니다.

However, the test error exhibits a characteristic U-shape, declining at first (with a minimum at approximately $K=10$) before increasing again when the method becomes excessively flexible and overfits.

그러나, 시험 오차는 특징적인 U-자 형태를 나타내는데, 방법이 과도하게 유연해지고 과적합할 때 다시 증가하기 전에 처음에는 (대략 $K=10$ 에서 최솟값을 가지고) 감소합니다.

![Figure 2.14](./img/Image_028.png)

**FIGURE 2.14.** _The KNN approach, using K_ = 3 _, is illustrated in a simple situation with six blue observations and six orange observations._ Left: _a test observation at which a predicted class label is desired is shown as a black cross. The three closest points to the test observation are identified, and it is predicted that the test observation belongs to the most commonly-occurring class, in this case blue._ Right: _The KNN decision boundary for this example is shown in black. The blue grid indicates the region in which a test observation will be assigned to the blue class, and the orange grid indicates the region in which it will be assigned to the orange class._ 

**그림 2.14.** _$K=3$ 을 사용하는 KNN 접근법은 6개의 파란색 관측치들과 6개의 주황색 관측치들이 있는 단순한 상황에서 설명됩니다._ 왼쪽: _예측된 클래스 라벨이 요구되는 시험 관측치가 검은색 십자가로 보여집니다. 시험 관측치에 가장 가까운 세 개의 점들이 식별되며, 예측은 이 시험 관측치가 가장 흔히 발생하는 클래스, 이 경우에는 파란색에 속한다고 이루어집니다._ 오른쪽: _이 예시에 대한 KNN 결정 경계가 검은색으로 보여집니다. 파란색 격자는 시험 관측치가 파란색 클래스에 할당될 영역을 기리키고, 주황색 격자는 그것이 주황색 클래스에 할당될 영역을 가리킵니다._

![Figure 2.15](./img/Image_030.png)

**FIGURE 2.15.** _The black curve indicates the KNN decision boundary on the data from Figure 2.13, using K_ = 10 _. The Bayes decision boundary is shown as a purple dashed line. The KNN and Bayes decision boundaries are very similar._ 

**그림 2.15.** _검은색 곡선은 $K=10$ 을 사용하여 그림 2.13으로부터의 데이터 위에서 KNN 결정 경계를 지시합니다. 베이즈 결정 경계는 보라색 점선으로 보입니다. KNN과 베이즈 결정 경계들은 매우 유사합니다._

In both the regression and classification settings, choosing the correct level of flexibility is critical to the success of any statistical learning method.

회귀 그리고 분류 설정 쌍방 모두에서, 유연성의 올바른 수준을 선택하는 것은 임의의 통계적 학습 방법의 성공에 필수적입니다.

The bias-variance tradeoff, and the resulting U-shape in the test error, can make this a difficult task.

편향-분산 트레이드오프, 그리고 시험 오차 안의 도출되는 U-형태는 이것을 어려운 과제로 만들 수 있습니다.

![Figure 2.16](./img/Image_033.png)

**FIGURE 2.16.** _A comparison of the KNN decision boundaries (solid black curves) obtained using $K=1$ and $K=100$ on the data from Figure 2.13. With $K=1$, the decision boundary is overly flexible, while with $K=100$ it is not sufficiently flexible. The Bayes decision boundary is shown as a purple dashed line._ 

**그림 2.16.** _그림 2.13으로부터의 데이터 위에서 $K=1$ 과 $K=100$ 을 사용하여 획득된 KNN 결정 경계들 (견고한 검은 곡선들)의 비교. $K=1$ 로, 결정 경계는 과도하게 유연하며, 반면 $K=100$ 로 그것은 충분히 유연하지 않습니다. 베이즈 결정 경계는 보라색 점선으로 보입니다._

![Figure 2.17](./img/Image_035.png)

**FIGURE 2.17.** _The KNN training error rate (blue, 200 observations) and test error rate (orange, 5,000 observations) on the data from Figure 2.13, as the level of flexibility (assessed using $1/K$ on the log scale) increases, or equivalently as the number of neighbors $K$ decreases. The black dashed line indicates the Bayes error rate. The jumpiness of the curves is due to the small size of the training data set._ 

**그림 2.17.** _유연성의 수준(로그 스케일 상의 $1/K$ 를 사용하여 평가됨)이 증가함에 따라, 또는 동등하게 이웃들의 수 $K$ 가 감소함에 따라 도출되는, 그림 2.13으로부터의 데이터 위에서의 KNN 훈련 오차율 (파란색, 200개 관측치들) 및 시험 오차율 (주황색, 5,000개 관측치들). 검은 점선은 베이즈 오차율을 지시합니다. 곡선들의 불규칙성(jumpiness)은 훈련 데이터 세트의 작은 크기 때문입니다._

In Chapter 5, we return to this topic and discuss various methods for estimating test error rates and thereby choosing the optimal level of flexibility for a given statistical learning method. 

제5장에서, 우리는 이 주제로 귀환하여 시험 오차율들을 추정하고 나아가 그에 의하여 주어진 통계적 학습 방법에 대한 유연성의 최적 수준을 선택하기 위한 다양한 방법들을 토론합니다.

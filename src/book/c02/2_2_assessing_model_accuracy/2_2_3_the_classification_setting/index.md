---
layout: default
title: "index"
---

# 2.2.3 The Classification Setting 
# 2.2.3 분류 문제 환경(The Classification Setting)

Thus far, our discussion of model accuracy has been focused on the regression setting. 

지금까지 우리의 모델 정확도 논의는 단변량 예측 방식인 회귀 분석 환경에만 초점을 맞추어 왔습니다.

But many of the concepts that we have encountered, such as the bias-variance trade-off, transfer over to the classification setting with only some modifications due to the fact that _yi_ is no longer quantitative. 

하지만 우리가 앞서 살펴봤던 편향-분산 상충 관계 등의 다수 개념들은 $y_i$ 가 더 이상 양적 데이터가 아니라는 점에 기인한 약간의 수정만 거치면 모두 분류 설정 환경으로 그대로 적용 전이될 수 있습니다.

Suppose that we seek to estimate _f_ on the basis of training observations $\{(x_1, y_1), \dots, (x_n, y_n)\}$, where now $y_1, \dots, y_n$ are qualitative. 

훈련 관측치 $\{(x_1, y_1), \dots, (x_n, y_n)\}$ 를 바탕으로 함수 _f_ 를 추정하려 한다고 가정해 봅시다. 여기서 $y_1, \dots, y_n$ 들은 질적(범주형) 데이터입니다.

The most common approach for quantifying the accuracy of our estimate $\hat{f}$ is the training _error rate_ , the proportion of mistakes that are made if we apply our estimate $\hat{f}$ to the training observations: 

우리의 추정치 $\hat{f}$ 의 정확도를 수치화하는 가장 흔한 방법은 훈련 _오류율(error rate)_ 입니다. 이는 추정치 $\hat{f}$ 를 훈련 관측치에 적용했을 때 발생하는 오류의 비율로, 다음과 같이 주어집니다:

$$ \frac{1}{n} \sum_{i=1}^n I(y_i \neq \hat{y}_i) \tag{2.8} $$

Here $\hat{y}_i$ is the predicted class label for the $i$th observation using $\hat{f}$. 

여기서 $\hat{y}_i$ 는 $\hat{f}$ 를 사용하여 도출한 $i$번째 관측치의 예측 클래스 라벨입니다.

And $I(y_i \neq \hat{y}_i)$ is an _indicator variable_ that equals 1 if $y_i \neq \hat{y}_i$ and zero if $y_i = \hat{y}_i$. 

그리고 $I(y_i \neq \hat{y}_i)$ 는 실제 $y_i$ 와 예측 $\hat{y}_i$ 가 다르면 1, 같으면 0이 되는 _지시 변수(indicator variable)_ 입니다.

If $I(y_i \neq \hat{y}_i) = 0$ then the $i$th observation was classified correctly by our classification method; otherwise it was misclassified. 

만일 $I(y_i \neq \hat{y}_i) = 0$ 이라면 해당 $i$번째 관측치는 우리의 분류 방법에 의해 올바르게 분류된 것이고, 그렇지 않다면 오분류된 것입니다.

Hence Equation 2.8 computes the fraction of incorrect classifications. 

따라서 방정식 2.8은 오분류된 비율의 분수를 계산합니다.

Equation 2.8 is referred to as the _training error_ rate because it is computed based on the data that was used to train our classifier. 

식 2.8은 분류기를 학습시키는 데 사용된 데이터를 기반으로 산출되었기에 _훈련 오류율(training error rate)_ 이라고 부릅니다.

As in the regression setting, we are most interested in the error rates that result from applying our classifier to test observations that were not used in training. 

회귀 설정과 동일하게 우리는 모델 훈련에 사용되지 않은 별도의 테스트 관측치 집단에 분류기를 적용했을 때 초래되는 에러율에 가장 큰 관심이 있습니다.

The _test error_ rate associated with a set of test observations of the form $(x_0, y_0)$ is given by 

$(x_0, y_0)$ 형태를 지닌 일련의 테스트 집단 관측치와 관련된 _테스트 오류율(test error rate)_ 은 다음 공식으로 표시됩니다.

$$ \text{Ave}(I(y_0 \neq \hat{y}_0)) \tag{2.9} $$

where $\hat{y}_0$ is the predicted class label that results from applying the classifier to the test observation with predictor $x_0$. 

이때 $\hat{y}_0$ 은 독립 변수 예측 인자 $x_0$ 를 가진 테스트 관측치에 분류기 모델을 적용해 비롯된 예측 분류 클래스 확률 라벨입니다.

A _good_ classifier is one for which the test error (2.9) is smallest. 

_훌륭한_ 분류기란 실전 검증인 테스트 에러점수 수식 (2.9)의 결괏값을 가장 낮게 산출하는 도출 시스템 모델입니다.

### The Bayes Classifier 
### 베이즈 분류기(The Bayes Classifier)

It is possible to show (though the proof is outside of the scope of this book) that the test error rate given in (2.9) is minimized, on average, by a very simple classifier that _assigns each observation to the most likely class, given its predictor values_ . 

비록 정확한 논증 증명 수순 절차는 이 책의 심도 범위를 벗어나나, 모델 주어진 예측 변숫값을 근간으로 삼아 도출 예측된 관측치를 가장 확률적으로 유력한 클래스 모델 결과에 배치 할당하는_ 매우 단순하고 단편적인 모형 분류기를 통해, 산식 (2.9) 도출 검증 치수에 주어진 테스트 오차율을 평균적으로 일관성 있게 최소화할 수 있음이 도출 증명됩니다.

In other words, we should simply assign a test observation with predictor vector $x_0$ to the class $j$ for which 

수학적으로 다시 말하자면, 우리는 그저 예측 변수 벡터 $x_0$ 값을 가지는 미지 테스트 조달 관측 측정을 다음 식을 만족하는 결과 클래스 $j$ 에 곧장 대입 할당하면 됩니다.

$$ \text{Pr}(Y = j|X = x_0) \tag{2.10} $$

is largest. 

즉 이 확률이 가장 높은(largest) 곳에 할당하는 방식입니다.

Note that (2.10) is a _conditional probability_ : it is the probability that $Y = j$, given the observed predictor vector $x_0$. 

특히 공식 방정식 단위 (2.10)은 _조건부 확률(conditional probability)_ 이라는 점에 반드시 몹시 크게 유의하여야 합니다. 이는 곧 관측된 인자 예측 변수 벡터 $x_0$ 가 실제로 기표 주어졌을 때 결괏값 $Y$ 가 클래스 $j$ 가 될 확률을 대변 뜻합니다.

This very simple classifier is called the _Bayes classifier_ . 

이러한 지극히 매우 단순한 논리 분류 모델기를 우리는 통계상 _베이즈 분류기(Bayes classifier)_ 라고 정립하여 지칭 일컫습니다.

In a two-class problem where there are only two possible response values, say _class 1_ or _class 2_ , the Bayes classifier corresponds to predicting class one if $\text{Pr}(Y = 1|X = x_0) > 0.5$, and class two otherwise. 

도출 응답 변수 단면 값이 오직 단 두 가지 종속 부류로, 예컨대 _클래스 1_ 과 _클래스 2_ 만 유일하게 존재하는 이항 두 클래스 해결 문제의 환경에서는, 베이즈 분류기가 기표 점수 $\text{Pr}(Y = 1|X = x_0) > 0.5$ 이면 그대로 클래스 1을 전가 예측하고 그렇지 않을 시엔 정 반대 구조 모형인 잔여 클래스 판단 2를 예측하는 모델 체계에 매칭 부합합니다.

Figure 2.13 provides an example using a simulated data set in a two-dimensional space consisting of predictors $X_1$ and $X_2$. 

도면 그림 2.13은 척도 예측 시스템의 중심 두 인자인 변수 $X_1$ 과 추정 기저 $X_2$ 인자들로만 구성되어 구조 확립된 2차원 공간 지표 표면에서의 투사 시뮬레이션 지표 데이터 관측 세트를 사용하여 아주 훌륭한 시연 예시를 마련해 제공합니다.

The orange and blue circles correspond to training observations that belong to two different classes. 

단면에 표기 분산된 주황색 모형과 파란색 동그라미 원 점들은 서로 상이하게 전혀 다른 이질 부류 단면 두 가지 클래스들에 각각 매칭 소속된 조달 훈련 전용 집합군 관측치들을 서로 대조해 비교 나타냅니다.

For each value of $X_1$ and $X_2$, there is a different probability of the response being orange or blue. 

조달 변수인 각 $X_1$ 과 측정 $X_2$ 의 수많은 값 조합들마다 응답이 주황 혹은 파랑이 될 모의 결괏값 확률은 각각 지점마다 전부 다르게 설정되어 존재합니다.

Since this is simulated data, we know how the data were generated and we can calculate the conditional probabilities for each value of $X_1$ and $X_2$. 

이는 실험용으로 조작 생성된 모의 시뮬레이션 환경 데이터 무리이므로, 우리는 이 점 데이터 한도 무리가 본래 과거 구조에서 어떠한 모델 수학 기저 과정을 토대 기반으로 모조 형성 생성되었는지 이미 정답을 처음부터 분명 잘 알고 있고, 이에 뒷받침 따라 수많은 $X_1$ 매개 및 $X_2$ 인자 변수 지표들의 단위 결합 개별 값마다 조건부 확률 구조 체계를 각각 모두 수리 연산 계산 계산해 측정 산출해 낼 수 있는 위력을 지닙니다.

The orange shaded region reflects the set of points for which $\text{Pr}(Y = \text{orange} | X)$ is greater than 50%, while the blue shaded region indicates the set of points for which the probability is below 50%. 

도면 색상 중 단색 주황색 음영 도색 기표 부분 기조 구역 영역은 모델 $\text{Pr}(Y = \text{주황} | X)$ 조건부 산출값이 기준 50%의 굴절 오차 판단 구별 한계 벽을 월등 넘는 요소 포인트 무리 점들의 도식 집합 면적을 뜻해 대변하며, 그에 상반되어 푸른 파란색 파랑 음영 표시 투사 구역 영역 단면 부분은 반대로 그 확률 기조 지수가 기준 50%를 미치지 못하고 그 측정 밑 점수로 도출 산출 하락하는 점들의 무리 구조 집합 영역 체계들을 뜻해 나타냅니다.

The purple dashed line represents the points where the probability is exactly 50%.

보라색 점선은 확률이 정확히 50%인 지점들을 나타냅니다.

This is called the _Bayes decision boundary_.

이를 통계적으로 _베이즈 결정 경계(Bayes decision boundary)_ 라고 부릅니다.

The Bayes classifier’s prediction is determined by the Bayes decision boundary; an observation that falls on the orange side of the boundary will be assigned to the orange class, and similarly an observation on the blue side of the boundary will be assigned to the blue class.

베이즈 분류기의 예측 역시 이 베이즈 결정 경계에 의하여 최종 판가름 결정됩니다. 즉 경계선을 기준으로 주황색 도식 측면 영역에 떨어져 분산되는 관측치는 주황색 클래스로 할당하고, 이와 마찬가지 기조로 푸른 파란색 기표 영역 구조 선상 부근에 수집 배치되는 관측치는 푸른 파란색 클래스로 각각 매칭 할당됩니다.

The Bayes classifier produces the lowest possible test error rate, called the _Bayes error rate_.

베이즈 분류기는 _베이즈 오류율(Bayes error rate)_ 이라 불리는 달성 가능한 범위 내 가장 최저의 결괏값 테스트 오차율을 산출해 보여 줍니다.

Since the Bayes classifier will always choose the class for which (2.10) is largest, the error rate will be $1 - \max_j \text{Pr}(Y=j | X=x_0)$ at $X=x_0$.

베이즈 판별 분류기 모델은 항시 예외 없이 제일 공식 (2.10) 기표 확률이 높은 최대 조건 확률의 가장 최대 도출 클래스를 채택해 고르기 때문에, 도달 포인트 지점 $X=x_0$ 에서의 오류율 점수는 수식 $1 - \max_j \text{Pr}(Y=j | X=x_0)$ 로 측정 도달합니다.

In general, the overall Bayes error rate is given by

일반적으로, 종합 평가 총체적인 베이즈 시스템의 전체 베이즈 오류율은 다음 통계 공식 방정식 형태를 가집니다.

$$ 1 - E(\max_j \text{Pr}(Y=j|X)) \tag{2.11} $$

where the expectation averages the probability over all possible values of $X$.

위 공식의 기댓값 기표는 전체 $X$ 가 지닐 수 있는 측정 모든 기표 수치 영역의 가능 도출 값 범위들에 대한 확률 총합 한계를 전부 평균 내어 합산한 결과를 의미합니다.

For our simulated data, the Bayes error rate is 0.133.

우리가 이번 그림에 도출 사용했던 시뮬레이션 환경 데이터의 전체 평균 베이즈 한계 테스트 오류율 결과는 0.133으로 나타났습니다.

It is greater than zero, because the classes overlap in the true population, which implies that $\max_j \text{Pr}(Y = j | X = x_0) < 1$ for some values of $x_0$.

이 점수 수치가 기표 영 0점 이상보다도 확실히 더 큰 수치로 도출된 근본적인 원인은, 오리지널 진짜 모집단 모집 기표 내부에서도 두 클래스 계열 집단이 서로 불가피하게 중첩 기표되어 포개져 분포하는 영역이 존재하기 때문이며, 이는 결과적으로 몇몇 특수 기표 $x_0$ 도출 값 한계 범위 지점들에서는 $\max_j \text{Pr}(Y = j | X = x_0) < 1$ 오차 등식이 형성 내포 성립된다는 사실 구조를 명시 의미합니다.

The Bayes error rate is analogous to the irreducible error, discussed earlier.

결론적으로 앞 단원들에서 누누이 잦게 살펴보고 다뤄 왔던 절대로 결단코 줄일 해결 극복 축소가 불가한 애초 측정의 근본 도출 한계 도달 상한인 근본 최저 결별 한계 도달 통제 차단 불능의 극강 기저 원초 오차율 수치 즉 축소 불가능 오차(irreducible error)의 존재가 바로 이 베이즈 절대 오류율과 서로 동등한 속성 기표 유사 개념 맥락을 공유 수반합니다.

---

## Sub-Chapters (하위 목차)

### 2.2.3.1 K-Nearest Neighbors (K-최근접 이웃)
* [문서로 이동하기](./2_2_3_1_k_nearest_neighbors/)

비모수적인 분류 환경에서 이론의 실제 구현체로 가장 직관적인 알고리즘인 K-최근접 이웃(KNN) 기법을 학습합니다.
K 값의 크기 변화에 따라 결정 경계(Decision Boundary)가 어떻게 바뀌며, 그 과정 속 편향-분산 트레이드오프가 어떻게 작용 나타나는지 심도 있게 배웁니다.

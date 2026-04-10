---
layout: default
title: "index"
---

# 2.2.1 Measuring the Quality of Fit 
# 2.2.1 적합성 품질 측정

In order to evaluate the performance of a statistical learning method on a given data set, we need some way to measure how well its predictions actually match the observed data.

주어진 데이터 세트에서 통계적 학습 방법의 성능을 평가하려면 예측이 관측 데이터와 얼마나 잘 일치하는지 측정할 방법이 필요합니다.

That is, we need to quantify the extent to which the predicted response value for a given observation is close to the true response value for that observation.

즉, 특정 관측치에 대한 예측값이 실제 값에 얼마나 가까운지 정량화해야 합니다.

In the regression setting, the most commonly-used measure is the _mean squared error_ (MSE), given by 

회귀 설정에서 가장 일반적으로 사용되는 척도는 다음 공식과 같은 _평균 제곱 오차(MSE)_ 입니다.

$$ MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{f}(x_i))^2 \tag{2.5} $$

where $\hat{f}(x_i)$ is the prediction that $\hat{f}$ gives for the _i_ th observation.

여기서 $\hat{f}(x_i)$ 는 추정 함수 $\hat{f}$ 가 _i_ 번째 관측치에 대해 제공하는 예측값입니다.

The MSE will be small if the predicted responses are very close to the true responses, and will be large if for some of the observations, the predicted and true responses differ substantially. 

예측된 응답이 실제 응답에 매우 가까우면 MSE가 작고, 예측과 실제 응답이 크게 다르면 MSE는 커집니다.

The MSE in (2.5) is computed using the training data that was used to fit the model, and so should more accurately be referred to as the _training MSE_ .

(2.5)의 MSE는 모델 훈련에 사용된 데이터를 통해 계산되므로 _훈련 MSE_ 라고 해야 합니다.

But in general, we do not really care how well the method works on the training data.

그러나 우리는 이 방법이 훈련 데이터에서 얼마나 잘 작동하는지에는 크게 신경 쓰지 않습니다.

Rather, _we are interested in the accuracy of the predictions that we obtain when we apply our method to previously unseen test data_ .

오히려 우리는 _이 방법을 이전에 단 한 번도 보지 못한 미지의 테스트 데이터에 새롭게 적용했을 때 얻는 예측 정확도_ 에 관심이 있습니다.

Why is this what we care about?

왜 이것이 중요한 것일까요?

Suppose that we are interested in developing an algorithm to predict a stock’s price based on previous stock returns.

과거 주식 수익률을 바탕으로 주가를 예측하는 알고리즘 개발에 관심이 있다고 가정해 봅시다.

We can train the method using stock returns from the past 6 months.

지난 6개월간의 주식 수익률을 사용하여 이 방법을 훈련시킬 수 있습니다.

But we don’t really care how well our method predicts last week’s stock price.

그러나 이 모델이 지난주 주가를 얼마나 잘 맞추는지에는 관심이 없습니다.

We instead care about how well it will predict tomorrow’s price or next month’s price.

우리는 이 알고리즘이 내일의 주가나 다음 달의 주가를 얼마나 잘 예측할지에만 관심이 있습니다.

On a similar note, suppose that we have clinical measurements (e.g. weight, blood pressure, height, age, family history of disease) for a number of patients, as well as information about whether each patient has diabetes.

비슷한 맥락으로, 다수 환자의 임상 측정치(예: 체중, 혈압, 키, 연령, 질병 가족력 등)와 각 환자의 당뇨병 발병 여부 정보를 모두 가지고 있다고 가정해 봅시다.

We can use these patients to train a statistical learning method to predict risk of diabetes based on clinical measurements.

이 환자들을 활용하여 임상 측정치 기반 당뇨병 발병 위험을 예측하는 모델을 훈련시킬 수 있습니다.

In practice, we want this method to accurately predict diabetes risk for _future patients_ based on their clinical measurements.

하지만 실제로는 이 방법이 훗날 새롭게 진입할 미리 알지 못하는 _신규 환자들_ 의 단편적인 임상 측정치만으로 그 위험을 정확히 예측하기를 바랍니다.

We are not very interested in whether or not the method accurately predicts diabetes risk for patients used to train the model, since we already know which of those patients have diabetes. 

모델을 훈련시킬 때 썼던 기존 환자들의 발병 위험을 이 방법이 얼마나 정확하게 판단하는지는 이미 정답을 다 알고 있으므로 전혀 중요하지 않습니다.

To state it more mathematically, suppose that we fit our statistical learning method on our training observations $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$, and we obtain the estimate $\hat{f}$.

이를 수학적으로 설명하자면, 훈련 관측치 세트 $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ 에 모델을 적합시켜 추정치 $\hat{f}$ 를 얻었다고 해 봅시다.

We can then compute $\hat{f}(x_1), \hat{f}(x_2), \dots, \hat{f}(x_n)$.

그러면 이후 각 훈련 데이터에 대한 예측치인 $\hat{f}(x_1), \hat{f}(x_2), \dots, \hat{f}(x_n)$ 를 모두 계산해 낼 수 있습니다.

If these are approximately equal to $y_1, y_2, \dots, y_n$, then the training MSE given by (2.5) is small.

만일 이 계산된 추정치 값들이 원본 결괏값 $y_1, y_2, \dots, y_n$ 들과 사실상 거의 유사하다면 수식 (2.5)로 계산된 훈련 MSE 값은 매우 작게 나타날 것입니다.

However, we are really not interested in whether $\hat{f}(x_i) \approx y_i$; instead, we want to know whether $\hat{f}(x_0)$ is approximately equal to $y_0$, where $(x_0, y_0)$ is a _previously unseen test observation not used to train the statistical learning method_.

그러나 우리는 도출값 $\hat{f}(x_i)$ 가 원본 $y_i$ 에 일치하는지에는 관심이 없습니다; 대신 우리는 미지의 별도 측정치에 대한 예측 결과인 $\hat{f}(x_0)$ 가 실제 정답 $y_0$ 에 근접하는지 여부를 알고자 합니다. 여기서의 기준치 표본인 $(x_0, y_0)$ 는 _초기 모델의 훈련 절차에서 활용되지 않은 낯선 미지의 실전용 테스트 관측치 대상_ 입니다.

<p align="center">
  <img src="./img/Image_023.png" alt="Figure 2.9">
</p>

**FIGURE 2.9.** Left: _Data simulated from $f$, shown in black. Three estimates of $f$ are shown: the linear regression line (orange curve), and two smoothing spline fits (blue and green curves)._ Right: _Training MSE (grey curve), test MSE (red curve), and minimum possible test MSE over all methods (dashed line). Squares represent the training and test MSEs for the three fits shown in the left-hand panel._

**그림 2.9.** (좌측): _원형 함수 $f$ (검은색 실선)로부터 시뮬레이션된 관측 데이터. 이 데이터 점포에 기초한 3가지 종류의 이질적인 $f$ 예측 추정 모델 표면이 각기 표시됨: 단편적인 선형 회귀 모의 예측치(주황색 곡선), 그 외 굴곡 허용 한도수 차수를 다르게 가한 두 가지 평활 스플라인(smoothing spline) 분석 적응 패널 예측선 모델(파란색, 초록색 곡선)._ (우측): _곡률 요동에 따른 오차 변화 양상으로서, 회색 선은 훈련 MSE 변화율을, 붉은 선은 실제 테스트 MSE 변동 추이를 기록하며, 수평 점선은 모든 기법을 통틀어 달성할 수 있는 최소 하한 테스트 MSE 경계선을 보여줍니다. 도표 표면의 사각형 점들은 직전 좌측 패널에 도식된 세 가지 분석 모델별 평가치용 훈련 기반 및 미지 테스트 MSE 결괏값을 뜻합니다._

We want to choose the method that gives the lowest _test MSE_ , as opposed to the lowest training MSE.

우리는 최저의 훈련 MSE 수치를 도출하는 모델보다는 본질적으로 가장 낮은 수치인 최저의 _테스트 MSE_ 수치를 안겨주는 그 방식을 최강 평가 모델 기법 기준치로 엄선 선택하길 바랍니다.

In other words, if we had a large number of test observations, we could compute

달리 말해 우리에게 검증용 테스트 관측치들이 어마어마하게 많이 존재한다면, 우리는 다음과 같은 결과를 산출해 볼 수 있습니다:

$$ \text{Ave}(y_0 - \hat{f}(x_0))^2 \tag{2.6} $$

the average squared prediction error for these test observations $(x_0, y_0)$.

이 (2.6) 계산식 모델은 낯선 미지 검증 대상의 독립 표본 관측 체계인 $(x_0, y_0)$ 집단 요소들에 대한 모델 오류 훈련 결과인 별도 _평균 편차 제곱 실측 검증 한당 예측 에러 오류율_ 성과를 산출하는 계산 지수 공식을 나타냅니다.

We’d like to select the model for which this quantity is as small as possible.

우리는 이렇게 산출된 테스트 평균 오차의 에러 결괏값이 가장 최소로 제일 낮게 도출 산정 달성되는 우수 모델 방식을 가장 1위로 엄선하여 채택 선택하기를 기원합니다.

How can we go about trying to select a method that minimizes the test MSE?

그렇다면 테스트 측면에서 성능 평가 미달 에러치 한계를 가장 작게 최소화 제압해 내는 최상급 테스트 방법 수단을 과연 어떻게 골라낼 수 있을까요?

In some settings, we may have a test data set available—that is, we may have access to a set of observations that were not used to train the statistical learning method.

경우에 따라 운이 좋게 별도의 독립된 미지 여분 테스트 데이터 척도 세트를 확보했을 수 있습니다 — 즉 초기 기계 학습 방식 훈련용(train) 과정에 일체 섞여서 쓰인 이력이 없는 전혀 낯선 별개 표본 미지 측정 관측치들에 대하여 접근이 허용된 상황입니다.

We can then simply evaluate (2.6) on the test observations, and select the learning method for which the test MSE is smallest.

이렇다면 우리는 미지의 독립된 해당 측정 관측치들 상에 위 오차 산점 (2.6) 공식만을 간단히 부합 대입 평가해 본 다음, 그 결과 모형 지수들 가운데 산출 오차인 해당 테스트 MSE 수치가 가장 최소 작게 측정 달성되는 가장 훌륭한 1등 학습 기법 모델을 쉽게 골라 결정 채택하면 됩니다.

But what if no test observations are available?

하지만 현실 모델의 제약으로 미지 검증용 전용 독립 잉여 데이터 세트들이 아예 없어 전혀 조달 불가능한 상황이 펼쳐진다면 어쩌면 좋을까요?

In that case, one might imagine simply selecting a statistical learning method that minimizes the training MSE (2.5).

그런 한계 상황에서는 궁여지책으로 이미 산출 기록된 (2.5) 공식에 의한 도출 성적 결괏값만이라도 오차 극소로 만족 달성을 꾀하는 모델 방식을 대체 방안으로 도입하길 강구할 것입니다.

This seems like it might be a sensible approach, since the training MSE and the test MSE appear to be closely related.

이 발상은 훈련 에러치 수치와 실측 미지 측정 평가 오차 테스트 에러 지수가 서로 긴밀한 연관비례성을 가지고 있을 거라 착각하게 만들기 때문에 매우 타당하고 합리적인 접근 선택으로 보일 여지가 큽니다.

Unfortunately, there is a fundamental problem with this strategy: there is no guarantee that the method with the lowest training MSE will also have the lowest test MSE.

그러나 몹시 불행하게도 이 판단에는 깊고 근본적인 한계 문제점이 존재합니다: 바로 과거 높은 점수를 거둬 제일 낮은 훈련 훈련 측치 MSE 바닥을 구사해낸 측정 방법이 새로운 모델 미세 실전 측정 모델 환경에서도 어김없이 최고의 훌륭 측정 수치 수준의 가장 낮은 그 최하위 합격 수준 수치 측정 결과치 기록의 그 최고 1위 테스트 실측 검증 한계 MSE 최우수 적합도를 어김없이 환산 보장해 유지할 것이라는 확신 있는 증거 인과 따위는 절대 일절 없다는 겁니다.

Roughly speaking, the problem is that many statistical methods specifically estimate coefficients so as to minimize the training set MSE.

거칠게 말해 문제는, 많은 통계 모델들이 훈련 세트 오차인 MSE를 최소화하도록 억지로 계수를 추정한다는 점입니다.

For these methods, the training set MSE can be quite small, but the test MSE is often much larger. 

이러한 기법들의 훈련 세트 MSE는 아주 작을지 몰라도 테스트 MSE는 훨씬 더 커지기 일쑤입니다.

Figure 2.9 illustrates this phenomenon on a simple example.

그림 2.9는 이 현상을 단순한 예시로 보여줍니다.

In the left-hand panel of Figure 2.9, we have generated observations from (2.1) with the true _f_ given by the black curve.

그림 2.9의 좌측에서는 진짜 함수 _f_ (검은 선)로부터 시뮬레이션 된 관측 데이터 점들을 볼 수 있습니다.

The orange, blue and green curves illustrate three possible estimates for _f_ obtained using methods with increasing levels of flexibility.

주황색, 파란색, 초록색 곡선들은 유연성을 점차 높인 방법들을 통해 얻어낸 세 가지 $f$ 추정치들입니다.

The orange line is the linear regression fit, which is relatively inflexible.

주황색 선은 유연하지 못한 선형 회귀 모의 예측치입니다.

The blue and green curves were produced using _smoothing splines_ , discussed in Chapter 7, with different levels of smoothness.

파란색과 초록색 곡선은 제7장에서 논의할 _평활 스플라인(smoothing splines)_ 기법을 각기 다른 굴곡 수준으로 적용한 결과입니다.

It is clear that as the level of flexibility increases, the curves fit the observed data more closely.

이렇듯 측정 유연성 차수 한도가 증가할수록, 산출 곡선이 실제 분포 데이터에 흡사하게 들어맞는다는 것은 명백합니다.

The green curve is the most flexible and matches the data very well; however, we observe that it fits the true _f_ (shown in black) poorly because it is too wiggly. 

초록색 곡선 모델은 가장 유연하며 분포 데이터 점들과 거의 부합하지만, 반대로 너무 혼잡하게 요동치기 때문에 진짜 정답 _f_ (검은색)의 본래 형태 곡률 투영과는 몹시 어긋납니다.

By adjusting the level of flexibility of the smoothing spline fit, we can produce many different fits to this data. 

우리는 평활 스플라인 기법의 유연성 곡률을 달리하여 이 데이터에 대해 이처럼 전혀 다른 여러 결과 모형을 산출해 볼 수 있습니다.

We now move on to the right-hand panel of Figure 2.9.

이제 시선을 표면 그림 2.9의 우측 패널로 옮겨 보겠습니다.

The grey curve displays the average training MSE as a function of flexibility, or more formally the _degrees of freedom_ , for a number of smoothing splines.

수치 회색 곡선은 각기 다른 여러 평활 스플라인들의 유연성, 수식 전문 용어로 _자유도(degrees of freedom)_ 한계에 따른 한정된 훈련 세트 전용 MSE 변화율을 형상으로 나타냅니다.

The degrees of freedom is a quantity that summarizes the flexibility of a curve; it is discussed more fully in Chapter 7.

이 자유도 치수는 패널 곡면에 가해진 곡률 유연성을 평가 측정하는 척도 지수이며 이 수치는 7장 항목에서 깊게 다룰 것입니다.

The orange, blue and green squares indicate the MSEs associated with the corresponding curves in the left-hand panel.

나타난 주황, 파랑, 초록 사각형들은 모두 좌측 패널 그림과 대응하는 이질적 세 가지 훈련 및 시험 MSE 수치들을 나타냅니다.

A more restricted and hence smoother curve has fewer degrees of freedom than a wiggly curve—note that in Figure 2.9, linear regression is at the most restrictive end, with two degrees of freedom.

제한적이고 매끄러운 곡선일수록 구불구불한 곡선보다 자유도가 적습니다. 그림 2.9에서 가장 제한적인 선형 회귀는 단 2개의 자유도를 지닙니다.

The training MSE declines monotonically as flexibility increases.

유연성이 증가함에 따라 훈련 MSE는 단조롭게 감소합니다.

In this example the true _f_ is non-linear, and so the orange linear fit is not flexible enough to estimate _f_ well.

이 예시에서 진짜 _f_ 는 비선형이므로 주황색 선형 적합은 _f_ 를 잘 추정할 만큼 유연하지 못합니다.

The green curve has the lowest training MSE of all three methods, since it corresponds to the most flexible of the three curves fit in the left-hand panel.

초록색 곡선은 가장 유연하므로 세 가지 방법 중 훈련 MSE가 제일 낮습니다.

In this example, we know the true function _f_ , and so we can also compute the test MSE over a very large test set, as a function of flexibility.

우리는 이 예시에서 진짜 함수 _f_ 를 알기 때문에 대규모 테스트 세트에 대한 테스트 MSE를 유연성의 함수로 계산해 볼 수 있습니다.

(Of course, in general _f_ is unknown, so this will not be possible.)

(물론 실제로는 _f_ 가 미지수이므로 이는 불가능합니다.)

The test MSE is displayed using the red curve in the right-hand panel of Figure 2.9.

테스트 MSE는 그림 2.9 우측 패널에 붉은색 곡선으로 표시되어 있습니다.

As with the training MSE, the test MSE initially declines as the level of flexibility increases.

훈련 MSE처럼 테스트 MSE도 처음에는 유연성이 높아질수록 감소합니다.

However, at some point the test MSE levels off and then starts to increase again.

하지만 어느 순간 테스트 MSE는 더는 감소하지 않고 수평을 유지하다가 다시 솟구쳐 증가하기 시작합니다.

Consequently, the orange and green curves both have high test MSE.

결과적으로 주황색 곡선(유연성 부족)과 초록색 곡선(유연성 과다) 모두 매우 높은 테스트 MSE 수치를 나타냅니다.

The blue curve minimizes the test MSE, which should not be surprising given that visually it appears to estimate _f_ the best in the left-hand panel of Figure 2.9.

파란색 곡선은 테스트 MSE를 최저치로 최소화하는데, 좌측 패널에서 이미 시각적으로 $f$ 를 가장 우수하게 추정한 점을 감안하면 이는 전혀 놀라운 결과가 아닙니다.

The horizontal dashed line indicates Var( $\epsilon$ ), the irreducible error in (2.3), which corresponds to the lowest achievable test MSE among all possible methods.

수평 점선은 모든 방법 중 달성 가능한 가장 낮은 테스트 MSE인 (2.3) 단락에서 다룬 축소 불가능한 오차 상한 한계 Var( $\epsilon$ ) 측정치를 의미합니다.

Hence, the smoothing spline represented by the blue curve is close to optimal.

그나마 파란색 곡선의 평활 스플라인이 그 이상적인 도달 한계 결괏값에 가장 측정치상으로 가까워 최적입니다.

In the right-hand panel of Figure 2.9, as the flexibility of the statistical learning method increases, we observe a monotone decrease in the training MSE and a _U-shape_ in the test MSE.

그림 2.9 우측 패널에서, 통계적 학습 방법의 유연성이 증가함에 따라 우리는 훈련 MSE의 단조로운 감소와 테스트 MSE의 극명한 _U자 형태(U-shape)_ 구조를 관찰할 수 있습니다.

This is a fundamental property of statistical learning that holds regardless of the particular data set at hand and regardless of the statistical method being used.

이는 눈앞의 어떤 특수한 측정 데이터 세트나 혹은 어떤 특정 통계적 분석 모델 방법을 시도 사용하느냐에 절대 무관하게 늘 기계적으로 부수 성립 적용되는 통계적 예측 학습 모델의 아주 가장 근본적인 척도 속성 결론 현상입니다.

As model flexibility increases, the training MSE will decrease, but the test MSE may not.

측정 모델이 유연해질수록 훈련 오차는 하염없이 낮아지지만 낯선 테스트 오차는 결코 모델 뜻대로 호응하여 무조건 낮아지지 않습니다.

When a given method yields a small training MSE but a large test MSE, we are said to be _overfitting_ the data.

기법이 훈련 MSE 값을 극히 작게 만들고 반대로 낯선 테스트 MSE는 무식하게 크게 만들 때 우리는 이 기법이 해당 특정 표본 데이터 집합을 심각하게 아주 _과대적합(overfitting)_ 한 오작 치명 상태에 이르러 빠졌다고 심판하고 규정해 일컫습니다.

This happens because our statistical learning procedure is working too hard to find patterns in the training data, and may be picking up some patterns that are just caused by random chance rather than by true properties of the unknown function _f_ .

이런 치명적인 과적 기현상이 일어나는 근원 도출 배경은 우리 방식 시스템이 훈련 전용 세트 속에만 존재하는 한계 점 패턴들을 찾아내 맞춰내는 일에만 구조적으로 너무 억지로 과하게 열중한 나머지, 함수 _f_ 가 지닌 근본 진리 속성이 아니라 그저 요행 무작위 우연이 발생시킨 우연 요소 임의 파편 현상 패턴들조차 모두 무작정 다 억지 포착하여 정답 요소로 잘못 학습 기억해 버리기 때문입니다.

When we overfit the training data, the test MSE will be very large because the supposed patterns that the method found in the training data simply don’t exist in the test data.

훈련 데이터에 모형이 심각하게 과적합되면, 모형이 잘못 암기한 그 억지 훈련용 패턴들은 정작 테스트 실전에서는 조금도 나타나거나 존재하지 않기 때문에 마침내 낯선 테스트 MSE 치수가 끔찍하게 커지게 됩니다.

Note that regardless of whether or not overfitting has occurred, we almost always expect the training MSE to be smaller than the test MSE because most statistical learning methods either directly or indirectly seek to minimize the training MSE.

우리의 통계 시스템은 직간접적으로 모두 하나같이 훈련 MSE 척도를 가장 최소 축소하는 것에 우선 초점 수립되어 있기 때문에 과대적합의 고도 발생 여부 빈도 등과는 완전 별개로 현상과 전혀 무관하게 항시 늘 언제나 훈련 에러 척도들이 낯선 실전 테스트 오차보다 훨씬 적을 것이며 우수할 거라 예상해야만 한다는 지표 주의 사실을 명백히 항상 아주 주지 주의 명심해야만 합니다.

Overfitting refers specifically to the case in which a less flexible model would have yielded a smaller test MSE.

즉 정립하자면, 과적합이라 분석 규정 칭해 부르는 모형 결함 상태는 근원적으로 사실 원래 기존의 것보다 덜 유연했던 하위 기존 모델 체제가 새로 유연성만 크게 가해 복사 높인 신규 측정 모형보다 되려 더 우수하게 훗날 테스트 MSE를 아주 훨씬 작게 좋게 달성할 수 있었을 그러한 오류 역전 도출 실패의 조작 실패 모델 산출 상황 경우를 특정 지어 가리킵니다.

![Figure 2.10](./img/Image_024.png)

**FIGURE 2.10.** _Details are as in Figure 2.9, using a different true $f$ that is much closer to linear. In this setting, linear regression provides a very good fit to the data._

**그림 2.10.** _그림 2.9와 세부 설명은 동일하나 진짜 함수 $f$ 가 선형 직선 형태에 더 가까운 시뮬레이션입니다. 이 환경에서는 구부러진 모델들보다 오히려 가장 단편적인 선형 회귀 모의가 데이터에 가장 우수한 최적합 모형을 깔끔히 보장 제공합니다._

Figure 2.10 provides another example in which the true _f_ is approximately linear.

위 그림 2.10은 진짜 정답 _f_ 모델이 거의 직선 선형인 또 다른 비교 예시를 보여 줍니다.

Again we observe that the training MSE decreases monotonically as the model flexibility increases, and that there is a U-shape in the test MSE.

여기서도 어김없이 모델 유연성이 계속 증가함에 따라 훈련 MSE는 계속 감소하며 오차 요율이 변동하고 테스트 MSE 결과는 반전되는 U자 형태 구부림 요동을 지님을 동일하게 우리는 관측 목격합니다.

However, because the truth is close to linear, the test MSE only decreases slightly before increasing again, so that the orange least squares fit is substantially better than the highly flexible green curve.

그러나 여기선 정답의 원형 자체 기준이 극도로 직선에 가깝게 일치되므로 테스트 에러율 MSE 치수는 잠시 약간만 떨어지다 곧장 재상승하며 치솟게 되며, 이에 따라 주황색 직선의 예측 모의가 요동이 심한 유연한 초록색 곡선 결과보다 훨씬 우세한 최고 예측 성적 곡면 위용을 결론 보입니다.

Finally, Figure 2.11 displays an example in which _f_ is highly non-linear.

마지막으로 첨부 지표 그림 2.11 척도 모델의 단면은 정답 변수인 진짜 _f_ 가 반대로 최악스럽게 심히 비선형적인 파동 굴곡을 극심히 갖춘 또 다른 상황을 우리 앞 단면에 제시 표면 비교 보여줍니다.

The training and test MSE curves still exhibit the same general patterns, but now there is a rapid decrease in both curves before the test MSE starts to increase slowly.

두 에러 측정 곡선 비교는 여전히 전반적인 U자형 극단 궤도를 똑같이 잘 성립 유지 따르고 있으나, 여기에서는 테스트 MSE 오차가 증가 반전을 일으키기 이전에 훈련, 실전의 두 모델 곡선 모두가 몹시 처음부터 가파르고 무지 자극 급격하게 치수 감소하는 단절된 깊은 간격 추세의 측정 구조 오차 하강 국면 현상을 심하게 그려냅니다.

In practice, one can usually compute the training MSE with relative ease, but estimating the test MSE is considerably more difficult because usually no test data are available.

실제 현실 연구 통계 관측 상황에서는 보통 한 세트의 훈련 데이터 오차 척도인 훈련 MSE만을 수식 투입 조립으로 상대적으로 무지 쉽게 비교 연산 결론지을 수 있지만, 정작 우리에게 궁극 요소가 되는 테스트 평가치 오차 실측 평가 추정 시도인 미지 결함 한도 점 테스트 MSE 예측 짐작은 독립된 사전 검증 척도용 테스트 데이터 여분 확보 조달이 좀처럼 보통 전혀 아예 불가능하기 때문에 수치 구조 산출 짐작이 무척 훨씬 극히 더 아찔하고 매우 극도로 조달 도달 연산이 치명적으로 고려 계산이 어렵습니다.

As the previous three examples illustrate, the flexibility level corresponding to the model with the minimal test MSE can vary considerably among data sets.

앞선 제시된 위 3종류 시연 예시들 도표들이 대변하여 설명하듯 가장 이상 최소 한계 오차 평가 기록점 최저 테스트 MSE 바닥 수치를 한도를 달성 결론짓는 측정 예측의 그 최고점 유연 곡면치 수준 한도 달성 치수는 측정 주어진 기반 환경의 낯선 지표 데이터 세트 분면 종류별마다 아주 현저하게 결과가 판이하게 각자 아주 다를 수밖에 없습니다.

Throughout this book, we discuss a variety of approaches that can be used in practice to estimate this minimum point.

우리는 향후 이 방대 통계 책의 모든 챕터 전반을 관통하여 이 실 검증 현장 적용에서 그토록 궁극 갈망 타점인 우수 최소 한계 에러 평가 도달 바닥 최소점 지점 단면을 찾고자 노력 산출하기 위해 아주 전격 사용 이용될 각양각색의 방대한 종류별 우등 방법론 복합 모델 접근 측정 전략들을 심층 논의할 것입니다.

One important method is _cross-validation_ (Chapter 5), which is a method for estimating the test MSE using the training data.

그중에 가장 뼈대가 되는 대표 중요 한 가지 해결 측정 지표 기능 모형이 훗날 제5장 단원 깊은 핵심으로 대두될 _교차 검증(cross-validation)_ 으로, 이것은 우리 손의 훈련 가설 데이터 자체 덩어리 지표만을 재이용 활용 분할 직접 사용 투과하여 마치 테스트 MSE 측면 값을 획득 추정해 내는 훌륭한 산술 구조적 방법이 됩니다.

---

## Sub-Chapters (하위 목차)

현재 2.2 단원 소속 문서입니다.
[상위 경로(Assessing Model Accuracy)로 돌아가기](../)



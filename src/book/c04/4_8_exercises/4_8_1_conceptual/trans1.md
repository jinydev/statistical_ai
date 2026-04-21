---
layout: default
title: "index"
---

[< 4.8 Exercises](../index.html) | [4.8.2 Applied >](../4_8_2_applied/index.html)

# _Conceptual_ 
# _개념_

1. Using a little bit of algebra, prove that (4.2) is equivalent to (4.3). In other words, the logistic function representation and logit representation for the logistic regression model are equivalent. 
1. 약간의 대수학을 사용하여 (4.2)가 (4.3)과 동등함을 증명하라. 즉, 로지스틱 회귀 모델에 대한 로지스틱 함수 표현과 로짓 표현은 동등하다.

2. It was stated in the text that classifying an observation to the class for which (4.17) is largest is equivalent to classifying an observation to the class for which (4.18) is largest. Prove that this is the case. In other words, under the assumption that the observations in the $k$th class are drawn from a $N(\mu_k, \sigma^2)$ distribution, the Bayes classifier assigns an observation to the class for which the discriminant function is maximized. 
2. 본문에서 (4.17)이 가장 큰 클래스로 관측치를 분류하는 것은 (4.18)이 가장 큰 클래스로 관측치를 분류하는 것과 동등하다고 서술되어 있다. 이것이 사실임을 증명하라. 즉, $k$번째 클래스의 관측치가 $N(\mu_k, \sigma^2)$ 분포에서 추출된다는 가정 하에, 베이즈 분류기는 판별 함수가 최대화되는 클래스에 관측치를 할당한다.

3. This problem relates to the QDA model, in which the observations within each class are drawn from a normal distribution with a class-specific mean vector and a class-specific covariance matrix. We consider the simple case where $p = 1$; i.e. there is only one feature. 
3. 이 문제는 각 클래스 내의 관측치가 클래스-특정 평균 벡터와 클래스-특정 공분산 행렬을 갖는 정규 분포에서 추출되는 QDA 모델과 관련이 있다. $p = 1$인 단순한 경우, 즉 피처가 단 하나만 있는 경우를 고려한다.
   - Suppose that we have $K$ classes, and that if an observation belongs to the $k$th class then $X$ comes from a one-dimensional normal distribution, $X \sim N(\mu_k, \sigma_k^2)$. Recall that the density function for the one-dimensional normal distribution is given in (4.16). Prove that in this case, the Bayes classifier is _not_ linear. Argue that it is in fact quadratic. 
   - $K$개의 클래스가 있고, 관측치가 $k$번째 클래스에 속한다면 $X$는 1차원 정규 분포 $X \sim N(\mu_k, \sigma_k^2)$에서 온다고 가정하자. 1차원 정규 분포에 대한 밀도 함수가 (4.16)에 주어졌음을 상기하라. 이 경우 베이즈 분류기가 선형이 _아님_을 증명하라. 그것이 실제로는 2차(quadratic)임을 주장하라.
   - _Hint: For this problem, you should follow the arguments laid out in Section 4.4.1, but without making the assumption that $\sigma_1^2 = \dots = \sigma_K^2$._ 
   - _힌트: 이 문제에 대해서는 섹션 4.4.1에 제시된 논증을 따라야 하지만, $\sigma_1^2 = \dots = \sigma_K^2$라는 가정을 하지 않아야 한다._

4. When the number of features $p$ is large, there tends to be a deterioration in the performance of KNN and other _local_ approaches that perform prediction using only observations that are _near_ the test observation for which a prediction must be made. This phenomenon is known as the _curse of dimensionality_, and it ties into the fact that non-parametric approaches often perform poorly when $p$ is large. We will now investigate this curse. 
4. 피처 수 $p$가 클 때, 예측을 해야 하는 테스트 관측치와 _가까운_ 관측치만을 사용하여 예측을 수행하는 KNN 및 기타 _국소(local)_ 접근법의 성능이 저하되는 경향이 있다. 이러한 현상을 _차원의 저주(curse of dimensionality)_라고 하며, 이는 비모수적 접근법이 $p$가 클 때 흔히 저조한 성능을 보인다는 사실과 연관된다. 이제 이 저주를 조사해 볼 것이다.
   - (a) Suppose that we have a set of observations, each with measurements on $p=1$ feature, $X$. We assume that $X$ is uniformly (evenly) distributed on $[0, 1]$. Associated with each observation is a response value. Suppose that we wish to predict a test observation’s response using only observations that are within 10% of the range of $X$ closest to that test observation. For instance, in order to predict the response for a test observation with $X = 0.6$, we will use observations in the range $[0.55, 0.65]$. On average, what fraction of the available observations will we use to make the prediction? 
   - (a) 각가 $p=1$개의 피처인 $X$에 대한 측정값이 있는 관측치 집합이 있다고 가정하자. 우리는 $X$가 $[0, 1]$에 균일하게 (고르게) 분포되어 있다고 가정한다. 각 관측치에는 반응 변수값이 연관되어 있다. 해당 테스트 관측치에 가장 가까운 $X$ 범위의 10% 이내에 있는 관측치만을 사용하여 테스트 관측치의 반응 변수를 예측하고자 한다고 가정하자. 예를 들어, $X = 0.6$인 테스트 관측치에 대한 반응 변수를 예측하기 위해 우리는 $[0.55, 0.65]$ 범위에 있는 관측치를 사용할 것이다. 평균적으로, 예측을 수행하기 위해 사용 가능한 관측치의 중 얼마나 많은 비율을 사용하게 될 것인가?
   - (b) Now suppose that we have a set of observations, each with measurements on $p=2$ features, $X_1$ and $X_2$. We assume that $(X_1, X_2)$ are uniformly distributed on $[0, 1] \times [0, 1]$. We wish to predict a test observation’s response using only observations that are within 10% of the range of $X_1$ _and_ within 10% of the range of $X_2$ closest to that test observation. On average, what fraction of the available observations will we use to make the prediction? 
   - (b) 이제 각각 $p=2$개의 피처 측정값인 $X_1$ 및 $X_2$를 갖는 관측치 집합이 있다고 가정하자. $(X_1, X_2)$가 $[0, 1] \times [0, 1]$에 균일하게 분포되어 있다고 가정한다. 우리는 해당 테스트 관측치에 가장 가까운 $X_1$ 범위의 10% _그리고_ 가장 가까운 $X_2$ 범위의 10% 이내에 있는 관측치만을 사용하여 테스트 관측치의 반응 변수를 예측하고자 한다. 평균적으로, 예측을 수행하기 위해 사용 가능한 관측치 중 얼마나 많은 비율을 사용하게 될 것인가?
   - (c) Now suppose that we have a set of observations on $p=100$ features. Again the observations are uniformly distributed on each feature, and again each feature ranges in value from 0 to 1. We wish to predict a test observation’s response using observations within the 10% of each feature’s range that is closest to that test observation. What fraction of the available observations will we use to make the prediction? 
   - (c) 이제 $p=100$개의 피처에 대한 관측치 집합이 있다고 가정하자. 다시 말하지만 관측치는 각 피처에 균일하게 분포되어 있으며, 각 피처의 값 범위는 0에서 1 이다. 해당 테스트 관측치에 가장 가까운 각 피처 범위의 10% 이내에 있는 관측치를 사용하여 테스트 관측치의 반응 변수를 예측하고자 한다. 예측을 수행하기 위해 사용 가능한 관측치 중 얼마나 많은 비율을 사용하게 될 것인가?
   - (d) Using your answers to parts (a)–(c), argue that a drawback of KNN when $p$ is large is that there are very few training observations “near” any given test observation. 
   - (d) (a)–(c) 파트에 대한 답을 사용하여, $p$가 클 때 KNN의 한 가지 단점은 주어진 임의의 테스트 관측치에 "가까운" 훈련 관측치가 거의 없다는 것임을 주장하라.
   - (e) Now suppose that we wish to make a prediction for a test observation by creating a $p$-dimensional hypercube centered around the test observation that contains, on average, 10% of the training observations. For $p=1, 2$, and $100$, what is the length of each side of the hypercube? Comment on your answer. 
   - (e) 이제 훈련 관측치의 평균 10%를 포함하는, 테스트 관측치를 중심으로 하는 $p$-차원 하이퍼큐브(hypercube)를 생성함으로써 테스트 관측치에 대한 예측을 하고자 한다고 가정하자. $p=1, 2$, 및 $100$에 대해 하이퍼큐브의 각 변의 길이는 얼마인가? 당신의 답에 대해 논평하라.
   _Note: A hypercube is a generalization of a cube to an arbitrary number of dimensions. When $p=1$, a hypercube is simply a line segment, when $p=2$ it is a square, and when $p=100$ it is a 100-dimensional cube._
   _참고: 하이퍼큐브는 정육면체를 임의의 차원 수로 일반화한 것이다. $p=1$일 때 하이퍼큐브는 단순히 선분이고, $p=2$일 때는 정사각형이며, $p=100$일 때는 100차원의 정육면체다._

5. We now examine the differences between LDA and QDA. 
5. 이제 LDA와 QDA 간의 차이를 살펴본다.
   - (a) If the Bayes decision boundary is linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (a) 베이즈 결정 경계가 선형인 경우, 훈련 세트에서 LDA 또는 QDA 중 어느 것이 더 잘 수행될 것으로 예상하는가? 테스트 세트에서는 어떠한가?
   - (b) If the Bayes decision boundary is non-linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (b) 베이즈 결정 경계가 비선형인 경우, 훈련 세트에서 LDA 또는 QDA 중 어느 것이 더 잘 수행될 것으로 예상하는가? 테스트 세트에서는 어떠한가?
   - (c) In general, as the sample size $n$ increases, do we expect the test prediction accuracy of QDA relative to LDA to improve, decline, or be unchanged? Why? 
   - (c) 일반적으로 표본 크기 $n$이 증가함에 따라, LDA에 상대적인 QDA의 테스트 예측 정확도가 향상될 것인가, 하락할 것인가, 아니면 변하지 않을 것으로 예상하는가? 그 이유는 무엇인가?
   - (d) True or False: Even if the Bayes decision boundary for a given problem is linear, we will probably achieve a superior test error rate using QDA rather than LDA because QDA is flexible enough to model a linear decision boundary. Justify your answer. 
   - (d) 참 혹은 거짓: 주어진 문제에 대한 베이즈 결정 경계가 선형일지라도, QDA는 선형 결정 경계를 모델링할 만큼 충분히 유연하기 때문에 아마도 LDA보다 QDA를 사용하는 것이 우수한 테스트 오류율을 달성할 것이다. 당신의 답을 정당화하라.

6. Suppose we collect data for a group of students in a statistics class with variables $X_1 =$ hours studied, $X_2 =$ undergrad GPA, and $Y =$ receive an A. We fit a logistic regression and produce estimated coefficient, $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$. 
6. 통계 수업을 듣는 학생 그룹의 데이터를 $X_1 =$ 공부한 시간, $X_2 =$ 학부 GPA, $Y =$ A 학점 받음 변수와 함께 수집한다고 가정하자. 우리는 로지스틱 회귀를 적합하고 추정된 계수 $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$를 산출한다.
   - (a) Estimate the probability that a student who studies for 40 h and has an undergrad GPA of 3.5 gets an A in the class. 
   - (a) 40시간 동안 공부하고 학부 GPA가 3.5인 학생이 수업에서 A를 받을 확률을 추정하라.
   - (b) How many hours would the student in part (a) need to study to have a 50% chance of getting an A in the class? 
   - (b) (a) 파트의 학생이 수업에서 A를 받을 확률이 50%가 되려면 몇 시간을 공부해야 하겠는가?

7. Suppose that we wish to predict whether a given stock will issue a dividend this year (“Yes” or “No”) based on $X$, last year’s percent profit. We examine a large number of companies and discover that the mean value of $X$ for companies that issued a dividend was $\bar{X} = 10$, while the mean for those that didn’t was $\bar{X} = 0$. In addition, the variance of $X$ for these two sets of companies was $\sigma^2 = 36$. Finally, 80% of companies issued dividends. Assuming that $X$ follows a normal distribution, predict the probability that a company will issue a dividend this year given that its percentage profit was $X = 4$ last year. 
7. $X$, 즉 작년의 퍼센트 수익률에 근거하여 주어진 주식이 올해 배당금을 지급할지 여부("예" 또는 "아니요")를 예측하고자 한다고 가정하자. 우리는 많은 수의 회사를 조사하여 배당금을 지급한 회사의 $X$ 평균값이 $\bar{X} = 10$인 반면, 지급하지 않은 회사의 평균은 $\bar{X} = 0$임을 발견했다. 더불어, 이 두 회사 집합에 대한 $X$의 분산은 $\sigma^2 = 36$이었다. 마지막으로, 80%의 회사가 배당금을 지급했다. $X$가 정규 분포를 따른다고 가정할 때, 작년의 퍼센트 수익률이 $X = 4$일 때 회사가 올해 배당금을 지급할 확률을 예측하라.
   _Hint: Recall that the density function for a normal random variable is $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$. You will need to use Bayes’ theorem._ 
   _힌트: 정규 확률 변수의 밀도 함수가 $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$임을 상기하라. 베이즈 정리를 사용해야 할 것이다._

8. Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20% on the training data and 30% on the test data. Next we use 1-nearest neighbors (i.e. $K=1$) and get an average error rate (averaged over both test and training data sets) of 18%. Based on these results, which method should we prefer to use for classification of new observations? Why? 
8. 데이터 세트를 취하여 동일한 크기의 훈련 및 테스트 세트로 나눈 다음, 두 개의 다른 분류 절차를 시도한다고 가정하자. 먼저 우리는 로지스틱 회귀를 사용하여 훈련 데이터에서 20%, 테스트 데이터에서 30%의 오류율을 얻는다. 다음으로 우리는 1-최근접 이웃(즉, $K=1$)을 사용하여 그리고 (테스트 및 훈련 데이터 세트 모두에 걸쳐 평균을 내어) 평균 오류율 18%를 얻는다. 이러한 결과에 근거하여, 새로운 관측치를 분류하기 위해 사용하려면 어떤 방법을 선호해야 하는가? 그 이유는 무엇인가?

9. This problem has to do with _odds_. 
9. 이 문제는 _승산(odds)_과 관계가 있다.
   - (a) On average, what fraction of people with an odds of 0.37 of defaulting on their credit card payment will in fact default? 
   - (a) 평균적으로, 신용 카드 대금을 채무 불이행할 승산이 0.37인 사람들 중 실제로 채무를 불이행할 비율은 얼마나 될 것인가?
   - (b) Suppose that an individual has a 16% chance of defaulting on her credit card payment. What are the odds that she will default? 
   - (b) 어떤 개인이 그녀의 신용 카드 대금을 채무 불이행할 확률이 16%라고 가정하자. 그녀가 채무를 불이행할 승산은 얼마인가?

10. Equation 4.32 derived an expression for $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ in the setting where $p > 1$, so that the mean for the $k$th class, $\mu_k$ is a $p$-dimensional vector, and the shared covariance $\Sigma$ is a $p \times p$ matrix. However, in the setting with $p=1$, (4.32) takes a simpler form, since the means $\mu_1, \dots, \mu_K$ and the variance $\sigma^2$ are scalars. In this simpler setting, repeat the calculation in (4.32), and provide expressions for $a_k$ and $b_{kj}$ in terms of $\pi_k, \pi_K, \mu_k, \mu_K$, and $\sigma^2$. 
10. 방정식 4.32는 $p > 1$인 설정에서 $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$에 대한 표현식을 도출했으므로, $k$번째 클래스에 대한 평균 $\mu_k$는 $p$-차원 벡터이고, 공유되는 공분산 $\Sigma$은 $p \times p$ 행렬이다. 하지만 $p=1$인 설정에서는 평균 $\mu_1, \dots, \mu_K$ 및 분산 $\sigma^2$가 스칼라이므로 (4.32)는 더 간단한 형태를 취한다. 이 더 간단한 설정에서 (4.32)의 계산을 반복하고, $\pi_k, \pi_K, \mu_k, \mu_K$, 그리고 $\sigma^2$에 관하여 $a_k$ 및 $b_{kj}$에 대한 표현식을 제공하라.

11. Work out the detailed forms of $a_k, b_{kj}$, and $b_{kjl}$ in (4.33). Your answer should involve $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, and $\Sigma_K$. 
11. (4.33)에서 $a_k, b_{kj}$, 및 $b_{kjl}$의 상세한 형태를 산출하라. 당신의 답은 $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, 및 $\Sigma_K$를 연관시켜야 한다.

12. Suppose that you wish to classify an observation $X \in \mathbb{R}$ into `apples` and `oranges`. You fit a logistic regression model and find that 
12. 관측치 $X \in \mathbb{R}$를 `사과`와 `오렌지`로 분류하고자 한다고 가정하자. 당신은 로지스틱 회귀 모델을 적합하고 다음을 발견한다.

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}
$$

Your friend fits a logistic regression model to the same data using the _softmax_ formulation in (4.13), and finds that 
당신의 친구는 데이터에 대해 _소프트맥스_ 공식 (4.13)을 사용하여 같은 형식으로 로지스틱 회귀 모델을 적합하고, 다음을 발견한다.

$$
\text{Pr}(Y = \text{apple} \mid X = x) = \frac{e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

- (a) What is the log odds of `orange` versus `apple` in your model? 
- (a) 당신의 모델에서 `사과` 대비 `오렌지`의 로그 승산(log odds)은 얼마인가?
- (b) What is the log odds of `orange` versus `apple` in your friend’s model? 
- (b) 당신 친구의 모델에서 `사과` 대비 `오렌지`의 로그 승산(log odds)은 얼마인가?
- (c) Suppose that in your model, $\hat{\beta}_0 = 2$ and $\hat{\beta}_1 = -1$. What are the coefficient estimates in your friend’s model? Be as specific as possible. 
- (c) 당신의 모델에서 $\hat{\beta}_0 = 2$ 및 $\hat{\beta}_1 = -1$이라고 가정하자. 당신 친구의 모델에서 추정된 계수는 얼마인가? 가능한 한 구체적으로 작성하라.
- (d) Now suppose that you and your friend fit the same two models on a different data set. This time, your friend gets the coefficient estimates $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$. What are the coefficient estimates in your model? 
- (d) 이제 당신과 당신의 친구가 다른 데이터 세트에 대해 동일한 두 모델을 적합시킨다고 가정하자. 이번에는 당신의 친구가 계수 추정치 $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$를 얻는다. 당신의 모델에서 계수 추정치는 얼마인가?
- (e) Finally, suppose you apply both models from (d) to a data set with 2,000 test observations. What fraction of the time do you expect the predicted class labels from your model to agree with those from your friend’s model? Explain your answer.
- (e) 마지막으로, (d)의 두 모델을 모두 2,000개의 테스트 관측치가 있는 데이터 세트에 적용한다고 가정하자. 당신의 모델에서 예측된 클래스 레이블이 당신 친구의 모델에서 나온 레이블과 일치할 것으로 예상되는 시간(혹은 경우의 비율)은 얼마인가? 답을 설명하라.

---

## Sub-Chapters


[< 4.8 Exercises](../index.html) | [4.8.2 Applied >](../4_8_2_applied/index.html)

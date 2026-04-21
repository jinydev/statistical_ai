---
layout: default
title: "trans1"
---

[< 4.8 Exercises](../trans1.html) | [4.8.2 Applied >](../4_8_2_applied/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.8.1 Conceptual
# 4.8.1 개념 문제

1. Using a little bit of algebra, prove that (4.2) is equivalent to (4.3). In other words, the logistic function representation and logit representation for the logistic regression model are equivalent. 
1. 약간의 대수학(algebra)을 사용하여 (4.2)가 (4.3)과 동등함(equivalent)을 증명하십시오. 다시 말해, 로지스틱 회귀 모델에 대한 로지스틱 함수(logistic function) 표현과 로짓(logit) 표현은 동등합니다.

2. It was stated in the text that classifying an observation to the class for which (4.17) is largest is equivalent to classifying an observation to the class for which (4.18) is largest. Prove that this is the case. In other words, under the assumption that the observations in the $k$th class are drawn from a $N(\mu_k, \sigma^2)$ distribution, the Bayes classifier assigns an observation to the class for which the discriminant function is maximized. 
2. 본문에서 관측치를 (4.17)이 가장 큰 클래스로 분류하는 것은 (4.18)이 가장 큰 클래스로 관측치를 분류하는 것과 동일하다고 명시되었습니다. 이것이 사실임을 증명하십시오. 다시 말해, $k$번째 클래스의 관측치가 $N(\mu_k, \sigma^2)$ 분포에서 추출(drawn)되었다는 가정 하에, 베이즈 분류기(Bayes classifier)는 판별 함수(discriminant function)가 최대화되는 클래스에 관측치를 할당합니다.

3. This problem relates to the QDA model, in which the observations within each class are drawn from a normal distribution with a class-specific mean vector and a class-specific covariance matrix. We consider the simple case where $p = 1$; i.e. there is only one feature. 
3. 이 문제는 각 클래스 내의 관측치가 클래스별 평균 벡터(class-specific mean vector)와 클래스별 공분산 행렬(class-specific covariance matrix)을 갖는 정규 분포에서 추출되는 QDA 모델과 관련이 있습니다. 우리는 특성이 오직 하나뿐인 간단한 경우($p=1$)를 고려합니다.
   - Suppose that we have $K$ classes, and that if an observation belongs to the $k$th class then $X$ comes from a one-dimensional normal distribution, $X \sim N(\mu_k, \sigma_k^2)$. Recall that the density function for the one-dimensional normal distribution is given in (4.16). Prove that in this case, the Bayes classifier is _not_ linear. Argue that it is in fact quadratic. 
   - 우리가 $K$개의 클래스를 가지고 있고, 어떤 관측치가 $k$번째 클래스에 속한다면 $X$가 1차원 정규 분포 $X \sim N(\mu_k, \sigma_k^2)$에서 온다고 가정합시다. 1차원 정규 분포에 대한 밀도 함수(density function)가 (4.16)에 주어졌음을 상기하십시오. 이 경우 베이즈 분류기가 비선형(_not_ linear)임을 증명하십시오. 그것이 사실상 이차원(quadratic)이라고 주장하십시오(Argue).
   - _Hint: For this problem, you should follow the arguments laid out in Section 4.4.1, but without making the assumption that $\sigma_1^2 = \dots = \sigma_K^2$._ 
   - _힌트: 이 문제의 경우 Section 4.4.1에 제시된 논거(arguments)를 따라야 하지만, $\sigma_1^2 = \dots = \sigma_K^2$ 라는 가정은 하지 않아야 합니다._

4. When the number of features $p$ is large, there tends to be a deterioration in the performance of KNN and other _local_ approaches that perform prediction using only observations that are _near_ the test observation for which a prediction must be made. This phenomenon is known as the _curse of dimensionality_, and it ties into the fact that non-parametric approaches often perform poorly when $p$ is large. We will now investigate this curse. 
4. 특성의 수 $p$가 클 때, 예측이 이루어져야 하는 테스트 관측값 _근처(near)_ 에 있는 관측값만 이용하여 예측을 수행하는 KNN 및 여타 _국소적(local)_ 접근 방식의 성능이 저하되는 경향이 있습니다. 이 현상은 _차원의 저주(curse of dimensionality)_ 로 알려져 있으며, $p$가 클 때 비모수적(non-parametric) 접근 방식이 자주 저조한 성과를 보인다는 사실과 연관됩니다. 우리는 이제 이 저주를 조사할 것입니다.
   - (a) Suppose that we have a set of observations, each with measurements on $p=1$ feature, $X$. We assume that $X$ is uniformly (evenly) distributed on $[0, 1]$. Associated with each observation is a response value. Suppose that we wish to predict a test observation’s response using only observations that are within 10% of the range of $X$ closest to that test observation. For instance, in order to predict the response for a test observation with $X = 0.6$, we will use observations in the range $[0.55, 0.65]$. On average, what fraction of the available observations will we use to make the prediction? 
   - (a) $p=1$차원의 특성 $X$에 대한 측정값이 있는 관측치 집합이 있다고 가정합시다. 우리는 $X$가 $[0, 1]$ 상에 균등하게(uniformly) 분포되어 있다고 가정합니다. 각 관측치와 연관된 반응 값(response value)이 있습니다. 해당 테스트 관측치에 가장 가까운 $X$ 범위의 10% 이내에 있는 관측치만 사용하여 테스트 관측치의 반응을 예측하고자 한다고 가정시합시다. 예를 들어 $X = 0.6$인 테스트 관측치의 반응을 예측하기 위해 $[0.55, 0.65]$ 범위의 관측치를 사용합니다. 평균적으로 우리는 예측을 내리기 위해 가용한 관측치의 얼마만큼의 비율(fraction)을 사용할까요?
   - (b) Now suppose that we have a set of observations, each with measurements on $p=2$ features, $X_1$ and $X_2$. We assume that $(X_1, X_2)$ are uniformly distributed on $[0, 1] \times [0, 1]$. We wish to predict a test observation’s response using only observations that are within 10% of the range of $X_1$ _and_ within 10% of the range of $X_2$ closest to that test observation. On average, what fraction of the available observations will we use to make the prediction? 
   - (b) 이제 $p=2$차원의 특성 $X_1$ 및 $X_2$ 에 대한 측정값이 있는 관측치 집합이 있다고 가정합니다. 우리는 $(X_1, X_2)$ 가 $[0, 1] \times [0, 1]$ 상에 균등하게 분포되어 있다고 가정합니다. 해당 테스트 관측치에 가장 가까운 $X_1$ 범위의 10% 이내 _그리고(and)_ $X_2$ 범위의 10% 이내에 있는 관측치만 사용하여 테스트 관측치의 반응을 예측하고자 합니다. 평균적으로 예측을 내리기 위해 가용 관측치의 어느 정도 비율을 사용할 것입니까?
   - (c) Now suppose that we have a set of observations on $p=100$ features. Again the observations are uniformly distributed on each feature, and again each feature ranges in value from 0 to 1. We wish to predict a test observation’s response using observations within the 10% of each feature’s range that is closest to that test observation. What fraction of the available observations will we use to make the prediction? 
   - (c) 이제 특성이 $p=100$ 인 관측치 집합이 있다고 가정합시다. 또 다시(Again) 관측치는 각 특성 상에 균등하게 분포되며, 각 특성 값의 범위는 0에서 1까지입니다. 해당 테스트 관측치와 가장 가까운 각 특성 범위의 10% 이내의 관측치를 사용하여 테스트 관측치의 반응을 예측하려고 합니다. 예측을 내리기 위해 사용할 수 있는 관측치의 비율은 얼마입니까?
   - (d) Using your answers to parts (a)–(c), argue that a drawback of KNN when $p$ is large is that there are very few training observations “near” any given test observation. 
   - (d) 파트 (a)-(c) 의 답을 사용하여 $p$가 클 때 KNN의 단점은 임의의 주어진 테스트 관측치 "근처(near)" 에 훈련 관측치가 거의 없다는 점임을 주장하십시오.
   - (e) Now suppose that we wish to make a prediction for a test observation by creating a $p$-dimensional hypercube centered around the test observation that contains, on average, 10% of the training observations. For $p=1, 2$, and $100$, what is the length of each side of the hypercube? Comment on your answer. 
   - (e) 이제 우리는 테스트 관측치를 중심으로 평균적으로 훈련 관측치의 10%를 포함하는 $p$-차원 하이퍼큐브(hypercube)를 생성함으로써 테스트 관측치에 대한 예측을 내리고자 한다고 가정합시다. $p=1, 2$ 및 $100$ 에 대하여 하이퍼큐브 각 변의 길이는 얼마입니까? 여러분의 답에 대해 코멘트하세요.
   _Note: A hypercube is a generalization of a cube to an arbitrary number of dimensions. When $p=1$, a hypercube is simply a line segment, when $p=2$ it is a square, and when $p=100$ it is a 100-dimensional cube._
   _참고: 하이퍼큐브는 정육면체를 임의의 차원 수로 일반화(generalization) 시킨 것입니다. $p=1$ 일 때 하이퍼큐브는 단순히 선분(line segment) 이고, $p=2$ 이면 정사각형, $p=100$ 이면 100차원 정육면체입니다._

5. We now examine the differences between LDA and QDA. 
5. 우리는 이제 LDA와 QDA 간의 차이점을 검토합니다.
   - (a) If the Bayes decision boundary is linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (a) 베이즈 결정 경계가 선형인 경우 LDA와 QDA 중 어느 것이 훈련 세트에서 더 나은 성능을 낼 것이라 예상합니까? 테스트 세트에서는 어떻습니까?
   - (b) If the Bayes decision boundary is non-linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (b) 베이즈 결정 경계가 비선형인 경우 LDA와 QDA 중 어느 것이 훈련 세트에서 더 나은 성능을 낼 것이라 예상합니까? 테스트 세트에서는 어떻습니까?
   - (c) In general, as the sample size $n$ increases, do we expect the test prediction accuracy of QDA relative to LDA to improve, decline, or be unchanged? Why? 
   - (c) 일반적으로 표본 크기 $n$ 이 증가함에 따라 LDA에 대한 QDA의 테스트 예측 정확도가 개선될 것이라 예상합니까, 감소할 것이라 혹은 변함없을 것이라 예상합니까? 이유는 무엇입니까?
   - (d) True or False: Even if the Bayes decision boundary for a given problem is linear, we will probably achieve a superior test error rate using QDA rather than LDA because QDA is flexible enough to model a linear decision boundary. Justify your answer. 
   - (d) 참 또는 거짓: 특정 문제에 대한 베이즈 결정 경계가 선형일지라도, 우리는 QDA가 선형 결정 경계를 모델링할 만큼 충분히 유연하기 때문에 LDA보다 QDA를 사용하는 것이 우월한(superior) 테스트 에러율을 달성할 확률이 높습니다(probably). 여러분의 답을 정당화하시오.

6. Suppose we collect data for a group of students in a statistics class with variables $X_1 =$ hours studied, $X_2 =$ undergrad GPA, and $Y =$ receive an A. We fit a logistic regression and produce estimated coefficient, $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$. 
6. 통계학 수업을 듣는 학생 그룹을 위해 다음 변수들을 사용하여 데이터를 수집했다고 가정해 보겠습니다. $X_1 =$ 공부한 시간, $X_2 =$ 학부 GPA, $Y =$ A학점 수령 여부. 우리는 로지스틱 회귀를 피팅하고 추정된 계수인 $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$ 을 산출합니다.
   - (a) Estimate the probability that a student who studies for 40 h and has an undergrad GPA of 3.5 gets an A in the class. 
   - (a) 40시간 동안 공부하고 학부 GPA가 3.5 인 학생이 수업에서 A를 받을 확률을 추정하십시오.
   - (b) How many hours would the student in part (a) need to study to have a 50% chance of getting an A in the class? 
   - (b) 파트(a)의 학생이 수업에서 A를 받을 확률이 50% 가 되려면 몇 시간을 공부해야 합니까?

7. Suppose that we wish to predict whether a given stock will issue a dividend this year (“Yes” or “No”) based on $X$, last year’s percent profit. We examine a large number of companies and discover that the mean value of $X$ for companies that issued a dividend was $\bar{X} = 10$, while the mean for those that didn’t was $\bar{X} = 0$. In addition, the variance of $X$ for these two sets of companies was $\sigma^2 = 36$. Finally, 80% of companies issued dividends. Assuming that $X$ follows a normal distribution, predict the probability that a company will issue a dividend this year given that its percentage profit was $X = 4$ last year. 
7. 전년도 수익률(percent profit)인 $X$ 를 바탕으로 주어진 주식이 올해 배당금(dividend)을 발행할지 여부("Yes" 또는 "No")를 예측하고자 한다고 가정해 보겠습니다. 우리는 수많은 회사를 조사해 배당금을 실시한 회사의 $X$ 평균값이 $\bar{X} = 10$ 이고, 그렇지 않은 회사의 평균은 $\bar{X} = 0$ 임을 발견했습니다. 이와 더불어 이 두 회사 집단에 대한 $X$ 의 분산은 $\sigma^2 = 36$ 이었습니다. 최종적으로 80% 의 회사가 배당금을 발행했습니다. $X$ 가 정규 분포를 따른다고 가정하고, 어떤 회사의 작년 수익 비율이 $X=4$ 일 때 이 회사가 올해 배당금을 발행할 확률을 예측하십시오.
   _Hint: Recall that the density function for a normal random variable is $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$. You will need to use Bayes’ theorem._ 
   _힌트: 정규 확률 변수에 대한 밀도 함수가 $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$ 임을 상기하십시오. 여러분은 베이즈 정리(Bayes’ theorem)를 사용해야 할 것입니다._

8. Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20% on the training data and 30% on the test data. Next we use 1-nearest neighbors (i.e. $K=1$) and get an average error rate (averaged over both test and training data sets) of 18%. Based on these results, which method should we prefer to use for classification of new observations? Why? 
8. 우리가 데이터 세트를 가져와서 동일한 크기의 훈련 및 테스트 세트로 나눈 다음, 두 가지 서로 다른 분류 절차를 시험해 본다고 가정합시다. 먼저 우리는 로지스틱 회귀를 사용하고 훈련 데이터에서 20%, 테스트 데이터에서 30% 의 오류율을 얻습니다. 다음으로 우리는 1-최근접 이웃(즉, $K=1$)을 사용하고 18%의 평균 오류율(테스트 및 훈련 데이터 세트 모두에 걸쳐 평균 낸)을 얻습니다. 이 결과를 토대로 볼 때, 우리는 새로운 관측치(new observations)를 분류하기 위해 어떤 방법을 사용하는 편을 선호해야 합니까? 이유는 무엇입니까?

9. This problem has to do with _odds_. 
9. 이 문제는 _오즈(odds)_ 와 관련이 있습니다.
   - (a) On average, what fraction of people with an odds of 0.37 of defaulting on their credit card payment will in fact default? 
   - (a) 신용카드 대금 채무 불이행(defaulting)에 대한 오즈가 0.37 인 사람들 중, 평균적으로 얼마의 비율이 실제로 채무를 불이행하게 될까요?
   - (b) Suppose that an individual has a 16% chance of defaulting on her credit card payment. What are the odds that she will default? 
   - (b) 특정 개인이 신용카드 대금을 채무 불이행할 확률(chance)이 16% 라고 가정합시다. 그녀가 채무를 불이행할 오즈는 얼마입니까?

10. Equation 4.32 derived an expression for $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ in the setting where $p > 1$, so that the mean for the $k$th class, $\mu_k$ is a $p$-dimensional vector, and the shared covariance $\Sigma$ is a $p \times p$ matrix. However, in the setting with $p=1$, (4.32) takes a simpler form, since the means $\mu_1, \dots, \mu_K$ and the variance $\sigma^2$ are scalars. In this simpler setting, repeat the calculation in (4.32), and provide expressions for $a_k$ and $b_{kj}$ in terms of $\pi_k, \pi_K, \mu_k, \mu_K$, and $\sigma^2$. 
10. 등식(Equation) 4.32 는 $p > 1$ 인 설정에서 $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ 에 대한 식(expression)을 유도(derived)했으며, 그로 인해 $k$번째 클래스의 평균 $\mu_k$는 $p$차원 벡터이고, 공유 공분산 $\Sigma$ 는 $p \times p$ 행렬입니다. 하지만 $p=1$ 인 설정의 경우, 모델의 평균 $\mu_1, \dots, \mu_K$ 와 분산 $\sigma^2$ 이 스칼라(scalars) 이므로 (4.32)는 더 단순한 형태를 취합니다. 이 보다 단순한 설정에서 (4.32)의 계산을 반복하고, $\pi_k, \pi_K, \mu_k, \mu_K$ 및 $\sigma^2$ 의 관점(in terms of)에서 $a_k$ 와 $b_{kj}$ 에 대한 수식을 제공하십시오.

11. Work out the detailed forms of $a_k, b_{kj}$, and $b_{kjl}$ in (4.33). Your answer should involve $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, and $\Sigma_K$. 
11. (4.33)의 $a_k, b_{kj}$, 및 $b_{kjl}$ 의 상세 형태를 계산해 내십시오(Work out). 여러분의 답변에는 $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$ 및 $\Sigma_K$ 가 포함되어야(involve) 합니다.

12. Suppose that you wish to classify an observation $X \in \mathbb{R}$ into `apples` and `oranges`. You fit a logistic regression model and find that 
12. 관측치 $X \in \mathbb{R}$ 를 `apples`(사과) 와 `oranges`(오렌지) 로 분류하고자 한다고 가정시합시다. 로지스틱 회귀 모델을 피팅하고 다음을 찾아냅니다:

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}
$$

Your friend fits a logistic regression model to the same data using the _softmax_ formulation in (4.13), and finds that 
여러분의 친구가 (4.13)의 _소프트맥스(softmax)_ 형태(formulation)를 사용해 동일한 데이터에 로지스틱 회귀 모델을 피팅하여 다음을 찾아냅니다.

$$
\text{Pr}(Y = \text{apple} \mid X = x) = \frac{e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

- (a) What is the log odds of `orange` versus `apple` in your model? 
- (a) 당신의 모델에서 `apple` 대비 `orange` 의 로그 오즈(log odds)는 무엇입니까?
- (b) What is the log odds of `orange` versus `apple` in your friend’s model? 
- (b) 당신 친구의 모델에서 `apple` 대비 `orange` 의 로그 오즈는 무엇입니까?
- (c) Suppose that in your model, $\hat{\beta}_0 = 2$ and $\hat{\beta}_1 = -1$. What are the coefficient estimates in your friend’s model? Be as specific as possible. 
- (c) 여러분의 모델에서 $\hat{\beta}_0 = 2$ 이고 $\hat{\beta}_1 = -1$ 이라 가정합시다. 친구의 모델에서 계수 추정치들은 무엇입니까? 가능한 자세하게 명시하십시오.
- (d) Now suppose that you and your friend fit the same two models on a different data set. This time, your friend gets the coefficient estimates $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$. What are the coefficient estimates in your model? 
- (d) 이제 당신과 당신 친구가 서로 다른 데이터 세트에 같은 두 모델을 피팅한다고 가정해 봅시다. 이번에 당신 친구는 계수 추정치로 $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$ 를 얻습니다. 당신 모델 안의 계수 추정치는 얼마입니까?
- (e) Finally, suppose you apply both models from (d) to a data set with 2,000 test observations. What fraction of the time do you expect the predicted class labels from your model to agree with those from your friend’s model? Explain your answer.
- (e) 마지막으로, (d)로부터 두 가지 모델 모두를 테스트 관측치가 2,000개인 데이터 세트에 적용한다고 가정해 봅시다. 여러분 모델의 예측된 클래스 레이블이 친구의 모델에서 산출된 것들과 어느 정도의 시간/비율 동안 동의할(agree with) 것으로 예상합니까? 여러분의 답을 설명하십시오.

---

## Sub-Chapters

[< 4.8 Exercises](../trans1.html) | [4.8.2 Applied >](../4_8_2_applied/trans1.html)

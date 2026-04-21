---
layout: default
title: "index"
---

[< 4.8 Exercises](../index.html) | [4.8.2 Applied >](../4_8_2_applied/index.html)


# _Conceptual_ 

1. Using a little bit of algebra, prove that (4.2) is equivalent to (4.3). In other words, the logistic function representation and logit representation for the logistic regression model are equivalent. 

2. It was stated in the text that classifying an observation to the class for which (4.17) is largest is equivalent to classifying an observation to the class for which (4.18) is largest. Prove that this is the case. In other words, under the assumption that the observations in the $k$th class are drawn from a $N(\mu_k, \sigma^2)$ distribution, the Bayes classifier assigns an observation to the class for which the discriminant function is maximized. 

3. This problem relates to the QDA model, in which the observations within each class are drawn from a normal distribution with a class-specific mean vector and a class-specific covariance matrix. We consider the simple case where $p = 1$; i.e. there is only one feature. 
   - Suppose that we have $K$ classes, and that if an observation belongs to the $k$th class then $X$ comes from a one-dimensional normal distribution, $X \sim N(\mu_k, \sigma_k^2)$. Recall that the density function for the one-dimensional normal distribution is given in (4.16). Prove that in this case, the Bayes classifier is _not_ linear. Argue that it is in fact quadratic. 
   - _Hint: For this problem, you should follow the arguments laid out in Section 4.4.1, but without making the assumption that $\sigma_1^2 = \dots = \sigma_K^2$._ 

4. When the number of features $p$ is large, there tends to be a deterioration in the performance of KNN and other _local_ approaches that perform prediction using only observations that are _near_ the test observation for which a prediction must be made. This phenomenon is known as the _curse of dimensionality_, and it ties into the fact that non-parametric approaches often perform poorly when $p$ is large. We will now investigate this curse. 
   - (a) Suppose that we have a set of observations, each with measurements on $p=1$ feature, $X$. We assume that $X$ is uniformly (evenly) distributed on $[0, 1]$. Associated with each observation is a response value. Suppose that we wish to predict a test observation’s response using only observations that are within 10% of the range of $X$ closest to that test observation. For instance, in order to predict the response for a test observation with $X = 0.6$, we will use observations in the range $[0.55, 0.65]$. On average, what fraction of the available observations will we use to make the prediction? 
   - (b) Now suppose that we have a set of observations, each with measurements on $p=2$ features, $X_1$ and $X_2$. We assume that $(X_1, X_2)$ are uniformly distributed on $[0, 1] \times [0, 1]$. We wish to predict a test observation’s response using only observations that are within 10% of the range of $X_1$ _and_ within 10% of the range of $X_2$ closest to that test observation. On average, what fraction of the available observations will we use to make the prediction? 
   - (c) Now suppose that we have a set of observations on $p=100$ features. Again the observations are uniformly distributed on each feature, and again each feature ranges in value from 0 to 1. We wish to predict a test observation’s response using observations within the 10% of each feature’s range that is closest to that test observation. What fraction of the available observations will we use to make the prediction? 
   - (d) Using your answers to parts (a)–(c), argue that a drawback of KNN when $p$ is large is that there are very few training observations “near” any given test observation. 
   - (e) Now suppose that we wish to make a prediction for a test observation by creating a $p$-dimensional hypercube centered around the test observation that contains, on average, 10% of the training observations. For $p=1, 2$, and $100$, what is the length of each side of the hypercube? Comment on your answer. 
   _Note: A hypercube is a generalization of a cube to an arbitrary number of dimensions. When $p=1$, a hypercube is simply a line segment, when $p=2$ it is a square, and when $p=100$ it is a 100-dimensional cube._

5. We now examine the differences between LDA and QDA. 
   - (a) If the Bayes decision boundary is linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (b) If the Bayes decision boundary is non-linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (c) In general, as the sample size $n$ increases, do we expect the test prediction accuracy of QDA relative to LDA to improve, decline, or be unchanged? Why? 
   - (d) True or False: Even if the Bayes decision boundary for a given problem is linear, we will probably achieve a superior test error rate using QDA rather than LDA because QDA is flexible enough to model a linear decision boundary. Justify your answer. 

6. Suppose we collect data for a group of students in a statistics class with variables $X_1 =$ hours studied, $X_2 =$ undergrad GPA, and $Y =$ receive an A. We fit a logistic regression and produce estimated coefficient, $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$. 
   - (a) Estimate the probability that a student who studies for 40 h and has an undergrad GPA of 3.5 gets an A in the class. 
   - (b) How many hours would the student in part (a) need to study to have a 50% chance of getting an A in the class? 

7. Suppose that we wish to predict whether a given stock will issue a dividend this year (“Yes” or “No”) based on $X$, last year’s percent profit. We examine a large number of companies and discover that the mean value of $X$ for companies that issued a dividend was $\bar{X} = 10$, while the mean for those that didn’t was $\bar{X} = 0$. In addition, the variance of $X$ for these two sets of companies was $\sigma^2 = 36$. Finally, 80% of companies issued dividends. Assuming that $X$ follows a normal distribution, predict the probability that a company will issue a dividend this year given that its percentage profit was $X = 4$ last year. 
   _Hint: Recall that the density function for a normal random variable is $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$. You will need to use Bayes’ theorem._ 

8. Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20% on the training data and 30% on the test data. Next we use 1-nearest neighbors (i.e. $K=1$) and get an average error rate (averaged over both test and training data sets) of 18%. Based on these results, which method should we prefer to use for classification of new observations? Why? 

9. This problem has to do with _odds_. 
   - (a) On average, what fraction of people with an odds of 0.37 of defaulting on their credit card payment will in fact default? 
   - (b) Suppose that an individual has a 16% chance of defaulting on her credit card payment. What are the odds that she will default? 

10. Equation 4.32 derived an expression for $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ in the setting where $p > 1$, so that the mean for the $k$th class, $\mu_k$ is a $p$-dimensional vector, and the shared covariance $\Sigma$ is a $p \times p$ matrix. However, in the setting with $p=1$, (4.32) takes a simpler form, since the means $\mu_1, \dots, \mu_K$ and the variance $\sigma^2$ are scalars. In this simpler setting, repeat the calculation in (4.32), and provide expressions for $a_k$ and $b_{kj}$ in terms of $\pi_k, \pi_K, \mu_k, \mu_K$, and $\sigma^2$. 

11. Work out the detailed forms of $a_k, b_{kj}$, and $b_{kjl}$ in (4.33). Your answer should involve $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, and $\Sigma_K$. 

12. Suppose that you wish to classify an observation $X \in \mathbb{R}$ into `apples` and `oranges`. You fit a logistic regression model and find that 

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}
$$

Your friend fits a logistic regression model to the same data using the _softmax_ formulation in (4.13), and finds that 

$$
\text{Pr}(Y = \text{apple} \mid X = x) = \frac{e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

- (a) What is the log odds of `orange` versus `apple` in your model? 
- (b) What is the log odds of `orange` versus `apple` in your friend’s model? 
- (c) Suppose that in your model, $\hat{\beta}_0 = 2$ and $\hat{\beta}_1 = -1$. What are the coefficient estimates in your friend’s model? Be as specific as possible. 
- (d) Now suppose that you and your friend fit the same two models on a different data set. This time, your friend gets the coefficient estimates $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$. What are the coefficient estimates in your model? 
- (e) Finally, suppose you apply both models from (d) to a data set with 2,000 test observations. What fraction of the time do you expect the predicted class labels from your model to agree with those from your friend’s model? Explain your answer.

---

## Sub-Chapters


[< 4.8 Exercises](../index.html) | [4.8.2 Applied >](../4_8_2_applied/index.html)

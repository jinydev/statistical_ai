---
layout: default
title: "index"
---

# _Conceptual_ 

1. Using a little bit of algebra, prove that (4.2) is equivalent to (4.3). In other words, the logistic function representation and logit representation for the logistic regression model are equivalent. 

2. It was stated in the text that classifying an observation to the class for which (4.17) is largest is equivalent to classifying an observation to the class for which (4.18) is largest. Prove that this is the case. In other words, under the assumption that the observations in the $k$ th class are drawn from a _N_ ( _µk, σ_[2] ) distribution, the Bayes classifier assigns an observation to the class for which the discriminant function is maximized. 

3. This problem relates to the QDA model, in which the observations within each class are drawn from a normal distribution with a classspecific mean vector and a class specific covariance matrix. We consider the simple case where _p_ = 1; i.e. there is only one feature. 

   - Suppose that we have $K$ classes, and that if an observation belongs to the $k$ th class then $X$comes from a one-dimensional normal distribution, _X ∼ N_ ( _µk, σk_[2][)][.][Recall][that][the][density][function][for][the] one-dimensional normal distribution is given in (4.16). Prove that in this case, the Bayes classifier is _not_ linear. Argue that it is in fact quadratic. 

   - _Hint: For this problem, you should follow the arguments laid out in Section 4.4.1, but without making the assumption that σ_ 1[2][=] _[ · · ·]_[ =] _[ σ] K_[2] _[.]_ 

4. When the number of features _p_ is large, there tends to be a deterioration in the performance of KNN and other _local_ approaches that perform prediction using only observations that are _near_ the test observation for which a prediction must be made. This phenomenon is known as the _curse of dimensionality_ , and it ties into the fact that curse of di- 

non-parametric approaches often perform poorly when _p_ is large. We mensionality 

will now investigate this curse. 

mensionality 

194 4. Classification 

- (a) Suppose that we have a set of observations, each with measurements on _p_ = 1 feature, $X$. We assume that $X$is uniformly (evenly) distributed on [0 _,_ 1]. Associated with each observation is a response value. Suppose that we wish to predict a test observation’s response using only observations that are within 10 % of the range of $X$closest to that test observation. For instance, in order to predict the response for a test observation with $X$= 0 _._ 6, we will use observations in the range [0 _._ 55 _,_ 0 _._ 65]. On average, what fraction of the available observations will we use to make the prediction? 

- (b) Now suppose that we have a set of observations, each with measurements on _p_ = 2 features, $X_1$ and $X_2$. We assume that ( $X_1$ _, X_ 2) are uniformly distributed on [0 _,_ 1] _×_ [0 _,_ 1]. We wish to predict a test observation’s response using only observations that are within 10 % of the range of $X_1$ _and_ within 10 % of the range of $X_2$ closest to that test observation. For instance, in order to predict the response for a test observation with $X_1$ = 0 _._ 6 and $X_2$ = 0 _._ 35, we will use observations in the range [0 _._ 55 _,_ 0 _._ 65] for $X_1$ and in the range [0 _._ 3 _,_ 0 _._ 4] for $X_2$. On average, what fraction of the available observations will we use to make the prediction? 

- (c) Now suppose that we have a set of observations on _p_ = 100 features. Again the observations are uniformly distributed on each feature, and again each feature ranges in value from 0 to 1. We wish to predict a test observation’s response using observations within the 10 % of each feature’s range that is closest to that test observation. What fraction of the available observations will we use to make the prediction? 

- (d) Using your answers to parts (a)–(c), argue that a drawback of KNN when _p_ is large is that there are very few training observations “near” any given test observation. 

- (e) Now suppose that we wish to make a prediction for a test observation by creating a _p_ -dimensional hypercube centered around the test observation that contains, on average, 10 % of the training observations. For _p_ = 1 _,_ 2, and 100, what is the length of each side of the hypercube? Comment on your answer. 

_Note: A hypercube is a generalization of a cube to an arbitrary number of dimensions. When p_ = 1 _, a hypercube is simply a line segment, when p_ = 2 _it is a square, and when p_ = 100 _it is a 100-dimensional cube._ 

5. We now examine the differences between LDA and QDA. 

   - (a) If the Bayes decision boundary is linear, do we expect LDA or QDA to perform better on the training set? On the test set? 

   - (b) If the Bayes decision boundary is non-linear, do we expect LDA or QDA to perform better on the training set? On the test set? 

4.8 Exercises 195 

   - (c) In general, as the sample size _n_ increases, do we expect the test prediction accuracy of QDA relative to LDA to improve, decline, or be unchanged? Why? 

   - (d) True or False: Even if the Bayes decision boundary for a given problem is linear, we will probably achieve a superior test error rate using QDA rather than LDA because QDA is flexible enough to model a linear decision boundary. Justify your answer. 

6. Suppose we collect data for a group of students in a statistics class with variables $X_1$ = hours studied, $X_2$ = undergrad GPA, and $Y=$ receive an A. We fit a logistic regression and produce estimated coefficient, _β_[ˆ] 0 = _−_ 6 _, β_[ˆ] 1 = 0 _._ 05 _, β_[ˆ] 2 = 1. 

   - (a) Estimate the probability that a student who studies for 40 h and has an undergrad GPA of 3 _._ 5 gets an A in the class. 

   - (b) How many hours would the student in part (a) need to study to have a 50 % chance of getting an A in the class? 

7. Suppose that we wish to predict whether a given stock will issue a dividend this year (“Yes” or “No”) based on $X$, last year’s percent profit. We examine a large number of companies and discover that the mean value of $X$for companies that issued a dividend was _X_[¯] = 10, while the mean for those that didn’t was _X_[¯] = 0. In addition, the ˆ 

variance of $X$for these two sets of companies was _σ_[2] = 36. Finally, 80 % of companies issued dividends. Assuming that $X$follows a normal distribution, predict the probability that a company will issue a dividend this year given that its percentage profit was $X$= 4 last year. 

_Hint: Recall that the density function for a normal random variable is f_ ( _x_ ) = ~~_√_~~ 21 _πσ_[2] _[e][−]_[(] _[x][−][µ]_[)][2] _[/]_[2] _[σ]_[2] _[.][You][will][need][to][use][Bayes’][theorem.]_ 

8. Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20 % on the training data and 30 % on the test data. Next we use 1-nearest neighbors (i.e. $K$ = 1) and get an average error rate (averaged over both test and training data sets) of 18 %. Based on these results, which method should we prefer to use for classification of new observations? Why? 

9. This problem has to do with _odds_ . 

   - (a) On average, what fraction of people with an odds of 0.37 of defaulting on their credit card payment will in fact default? 

   - (b) Suppose that an individual has a 16 % chance of defaulting on her credit card payment. What are the odds that she will default? 

196 4. Classification 

- Pr( $Y=$ _k|X_ = _x_ ) 

- 10. Equation 4.32 derived an expression for log ~~(—_)~~ Pr( $Y=$ _K|X_ = _x_ ) in the setting where _p >_ 1, so that the mean for t $k$ th class, _µk_ is a _p_ - dimensional vector, and the shared covariance **Σ** is a _p × p_ matrix. However, in the setting with _p_ = 1, (4.32) takes a simpler form, since the means _µ_ 1 _, . . . , µK_ and the variance _σ_[2] are scalars. In this simpler setting, repeat the calculation in (4.32), and provide expressions for _ak_ and _bkj_ in terms of _πk_ , _πK_ , _µk_ , _µK_ , and _σ_[2] . 

11. Work out the detailed forms of _ak_ , _bkj_ , and _bkjl_ in (4.33). Your answer should involve _πk_ , _πK_ , _µk_ , _µK_ , **Σ** $k$ , and **Σ** $K$ . 

12. Suppose that you wish to classify an observation _X ∈_ R into `apples` and `oranges` . You fit a logistic regression model and find that 

$$
	ext{Pr}(Y = 	ext{orange} \mid X = x) = 
rac{e^{eta_0 + eta_1 x}}{1 + e^{eta_0 + eta_1 x}}
$$

Your friend fits a logistic regression model to the same data using the _softmax_ formulation in (4.13), and finds that 

$$
	ext{Pr}(Y = 	ext{apple} \mid X = x) = 
rac{e^{lpha_{	ext{apple} 0} + lpha_{	ext{apple} 1} x}}{e^{lpha_{	ext{orange} 0} + lpha_{	ext{orange} 1} x} + e^{lpha_{	ext{apple} 0} + lpha_{	ext{apple} 1} x}}
$$

$$
	ext{Pr}(Y = 	ext{orange} \mid X = x) = 
rac{e^{lpha_{	ext{orange} 0} + lpha_{	ext{orange} 1} x}}{e^{lpha_{	ext{orange} 0} + lpha_{	ext{orange} 1} x} + e^{lpha_{	ext{apple} 0} + lpha_{	ext{apple} 1} x}}
$$

- (a) What is the log odds of `orange` versus `apple` in your model? 

- (b) What is the log odds of `orange` versus `apple` in your friend’s model? 

- (c) Suppose that in your model, _β_[ˆ] 0 = 2 and _β_[ˆ] 1 = _−_ 1. What are the coefficient estimates in your friend’s model? Be as specific as possible. 

- (d) Now suppose that you and your friend fit the same two models on a different data set. This time, your friend gets the coefficient ˆ ˆ ˆ ˆ 

- estimates _α_ orange0 = 1 _._ 2, _α_ orange1 = _−_ 2, _α_ orange0 = 3, _α_ orange1 = 0 _._ 6. What are the coefficient estimates in your model? 

- (e) Finally, suppose you apply both models from (d) to a data set with 2,000 test observations. What fraction of the time do you expect the predicted class labels from your model to agree with those from your friend’s model? Explain your answer. 

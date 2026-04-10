---
layout: default
title: "index"
---

# _8.2.4 Bayesian Additive Regression Trees_ 

Finally, we discuss _Bayesian additive regression trees_ (BART), another en- Bayesian semble method that uses decision trees as its building blocks. For simplicity, additive we present BART for regression (as opposed to classification). regression 

additive regression trees 

Recall that bagging and random forests make predictions from an average of regression trees, each of which is built using a random sample of data and/or predictors. Each tree is built separately from the others. By contrast, boosting uses a weighted sum of trees, each of which is constructed by fitting a tree to the residual of the current fit. Thus, each new tree attempts to capture signal that is not yet accounted for by the current set of trees. BART is related to both approaches: each tree is constructed in a random manner as in bagging and random forests, and each tree tries to capture signal not yet accounted for by the current model, as in boosting. The main novelty in BART is the way in which new trees are generated. 

Before we introduce the BART algorithm, we define some notation. We let _K_ denote the number of regression trees, and _B_ the number of iterations for which the BART algorithm will be run. The notation _f_[ˆ] _k[b]_[(] _[x]_[)][represents] the prediction at _x_ for the _k_ th regression tree used in the _b_ th iteration. At the end of each iteration, the _K_ trees from that iteration will be summed, i.e. _f_[ˆ] _[b]_ ( _x_ ) =[�] _[K] k_ =1 _[f]_[ˆ] _[ b] k_[(] _[x]_[)][for] _[b]_[ = 1] _[, . . . , B]_[.] In the first iteration of the BART algorithm, all trees are initialized to have a single root node, with _f_[ˆ] _k_[1][(] _[x]_[) =] _nK_ 1 � _ni_ =1 _[y][i]_[, the mean of the response] 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 

351 

(c): Possibility #2 for _f_[[ˆ]] _k[[b]]_[[(]] _[[X]]_[[)]] (d): Possibility #3 for _f_[[ˆ]] _k[[b]]_[[(]] _[[X]]_[)] 

**FIGURE 8.12.** _A schematic of perturbed trees from the BART algorithm._ (a): _The kth tree at the_ ( _b −_ 1) _st iteration, f_[ˆ] _k[b][−]_[1] ( _X_ ) _, is displayed. Panels (b)–(d) display three of many possibilities for f_[ˆ] _k[b]_[(] _[X]_[)] _[, given the form of][f]_[ˆ] _[ b] k[−]_[1] ( _X_ ) _._ (b): _One possibility is that f_[ˆ] _k[b]_[(] _[X]_[)] _[has][the][same][structure][as][f]_[ˆ] _[ b] k[−]_[1] ( _X_ ) _, but with different predictions at the terminal nodes._ (c): _Another possibility is that f_[ˆ] _k[b]_[(] _[X]_[)] _[results] from pruning f_[ˆ] _k[b][−]_[1] ( _X_ ) _._ (d): _Alternatively, f_[ˆ] _k[b]_[(] _[X]_[)] _[may][have][more][terminal][nodes] than f_[ˆ] _k[b][−]_[1] ( _X_ ) _._ 

values divided by the total number of trees. Thus, _f_[ˆ][1] ( _x_ ) =[�] _[K] k_ =1 _[f]_[ˆ][ 1] _k_[(] _[x]_[)][=] _n_ 1 � _ni_ =1 _[y][i]_[.] 

In subsequent iterations, BART updates each of the _K_ trees, one at a time. In the _b_ th iteration, to update the _k_ th tree, we subtract from each response value the predictions from all but the _k_ th tree, in order to obtain a _partial residual_

$$
r_i = y_i - \sum_{k' 
e k} \hat{f}_{k'}^b(x_i)
$$

for the _i_ th observation, _i_ = 1 _, . . . , n_ . Rather than fitting a fresh tree to this partial residual, BART randomly chooses a perturbation to the tree from theones that improve the fit to the partial residual. There are two componentsprevious iteration ( _f_[ˆ] _k[b][−]_[1] ) from a set of possible perturbations, favoring to this perturbation: 

1. We may change the structure of the tree by adding or pruning branches. 

2. We may change the prediction in each terminal node of the tree. 

Figure 8.12 illustrates examples of possible perturbations to a tree. The output of BART is a collection of prediction models,

$$
\hat{f}^b(x) = \sum_{k=1}^K \hat{f}_k^b(x)
$$


8. Tree-Based Methods 

352 

**Algorithm 8.3** _Bayesian Additive Regression Trees_

1. Let $\hat{f}_1^1(x) = \hat{f}_2^1(x) = \dots = \hat{f}_K^1(x) = \frac{1}{K n} \sum_{i=1}^n y_i$.
2. For $b = 2, \dots, B$:
   (a) For $k = 1, \dots, K$:

i. For _i_ = 1 _, . . . , n_ , compute the current partial residual

$$
r_i = y_i - \sum_{k' < k} \hat{f}_{k'}^b(x_i) - \sum_{k' > k} \hat{f}_{k'}^{b-1}(x_i)
$$


ii. Fit a new tree, _f_[ˆ] _k[b]_[(] _[x]_[)][,][to] _[r][i]_[,][by][randomly][perturbing][the] _k_ th tree from the previous iteration, _f_[ˆ] _k[b][−]_[1] ( _x_ ). Perturbations that improve the fit are favored. (b) Compute _f_[ˆ] _[b]_ ( _x_ ) =[�] _[K] k_ =1 _[f]_[ˆ] _[ b] k_[(] _[x]_[)][.] 

4. Compute the mean after _L_ burn-in samples,

$$
\hat{f}(x) = \frac{1}{B - L} \sum_{b=L+1}^B \hat{f}^b(x)
$$


We typically throw away the first few of these prediction models, since models obtained in the earlier iterations — known as the _burn-in_ period burn-in — tend not to provide very good results. We can let _L_ denote the number of burn-in iterations; for instance, we might take _L_ = 200. Then, to obtain a single prediction, we simply take the average after the burn-in iterations, _f_[ˆ] ( _x_ ) = _B−_ 1 _L_ � _Bb_ = _L_ +1 _[f]_[ˆ] _[ b]_[(] _[x]_[)][.][However,][it][is][also][possible][to][com-] pute _f_ ˆ _[L]_[+1] (quantities _x_ ) _, . . . , f_ ˆ _[B]_ (other _x_ ) providethan athemeasureaverage:of foruncertaintyinstance,inthethepercentilesfinal predic-of tion. The overall BART procedure is summarized in Algorithm 8.3. 

A key element of the BART approach is that in Step 3(a)ii., we do _not_ fit a fresh tree to the current partial residual: instead, we try to improve the fit to the current partial residual by slightly modifying the tree obtained in the previous iteration (see Figure 8.12). Roughly speaking, this guards against overfitting since it limits how “hard” we fit the data in each iteration. Furthermore, the individual trees are typically quite small. We limit the tree size in order to avoid overfitting the data, which would be more likely to occur if we grew very large trees. 

Figure 8.13 shows the result of applying BART to the `Heart` data, using _K_ = 200 trees, as the number of iterations is increased to 10 _,_ 000. During the initial iterations, the test and training errors jump around a bit. After this initial burn-in period, the error rates settle down. We note that there is only a small difference between the training error and the test error, indicating that the tree perturbation process largely avoids overfitting. 

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 353 

![Figure 8.13](./img/8_13.png)

**FIGURE 8.13.** _BART and boosting results for the_ `Heart` _data. Both training and test errors are displayed. After a burn-in period of_ 100 _iterations (shown in gray), the error rates for BART settle down. Boosting begins to overfit after a few hundred iterations._ 

The training and test errors for boosting are also displayed in Figure 8.13. We see that the test error for boosting approaches that of BART, but then begins to increase as the number of iterations increases. Furthermore, the training error for boosting decreases as the number of iterations increases, indicating that boosting has overfit the data. 

Though the details are outside of the scope of this book, it turns out that the BART method can be viewed as a _Bayesian_ approach to fitting an ensemble of trees: each time we randomly perturb a tree in order to fit the residuals, we are in fact drawing a new tree from a _posterior_ distribution. (Of course, this Bayesian connection is the motivation for BART’s name.) Furthermore, Algorithm 8.3 can be viewed as a _Markov chain Monte Carlo_ Markov algorithm for fitting the BART model. chain 

chain Monte Carlo 

When we apply BART, we must select the number of trees _K_ , the number of iterations _B_ , and the number of burn-in iterations _L_ . We typically choose large values for _B_ and _K_ , and a moderate value for _L_ : for instance, _K_ = 200, _B_ = 1 _,_ 000, and _L_ = 100 is a reasonable choice. BART has been shown to have very impressive out-of-box performance — that is, it performs well with minimal tuning. 

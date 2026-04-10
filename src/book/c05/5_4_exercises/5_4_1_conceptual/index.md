---
layout: default
title: "index"
---

# _Conceptual_ 

1. Using basic statistical properties of the variance, as well as singlevariable calculus, derive (5.6). In other words, prove that _α_ given by (5.6) does indeed minimize Var( _αX_ + (1 _− α_ ) _Y_ ). 

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of _n_ observations. 

   - (a) What is the probability that the first bootstrap observation is _not_ the _j_ th observation from the original sample? Justify your answer. 

   - (b) What is the probability that the second bootstrap observation is _not_ the _j_ th observation from the original sample? 

   - (c) Argue that the probability that the _j_ th observation is _not_ in the bootstrap sample is (1 _−_ 1 _/n_ ) _[n]_ . 

   - (d) When _n_ = 5, what is the probability that the _j_ th observation is in the bootstrap sample? 

   - (e) When _n_ = 100, what is the probability that the _j_ th observation is in the bootstrap sample? 

   - (f) When _n_ = 10 _,_ 000, what is the probability that the _j_ th observation is in the bootstrap sample? 

   - (g) Create a plot that displays, for each integer value of _n_ from 1 to 100 _,_ 000, the probability that the _j_ th observation is in the bootstrap sample. Comment on what you observe. 

   - (h) We will now investigate numerically the probability that a bootstrap sample of size _n_ = 100 contains the _j_ th observation. Here _j_ = 4. We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()` . We then `np.empty()` 

5.4 Exercises 225 

repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample. 

```
rng=np.random.default_rng(10)
store=np.empty(10000)
foriinrange(10000):
store[i]=np.sum(rng.choice(100,replace=True)==4)
>0
np.mean(store)
```

Comment on the results obtained. 

3. We now review _k_ -fold cross-validation. 

   - (a) Explain how _k_ -fold cross-validation is implemented. 

   - (b) What are the advantages and disadvantages of _k_ -fold crossvalidation relative to: 

      - i. The validation set approach? 

      - ii. LOOCV? 

4. Suppose that we use some statistical learning method to make a prediction for the response _Y_ for a particular value of the predictor _X_ . Carefully describe how we might estimate the standard deviation of our prediction. 

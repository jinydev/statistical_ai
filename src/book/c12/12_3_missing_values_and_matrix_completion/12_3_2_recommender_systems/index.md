---
layout: default
title: "index"
---

# Recommender Systems 

Digital streaming services like Netflix and Amazon use data about the content that a customer has viewed in the past, as well as data from other customers, to suggest other content for the customer. As a concrete example, some years back, Netflix had customers rate each movie that they had seen with a score from 1–5. This resulted in a very big _n × p_ matrix for which the ( _i, j_ ) element is the rating given by the _i_ th customer to the 

12.3 Missing Values and Matrix Completion 519 

![Figure 12.6](./img/12_6.png)

**FIGURE 12.6.** _As described in the text, in each of 100 trials, we left out 20 elements of the_ `USArrests` _dataset. In each trial, we applied Algorithm 12.1 with M_ = 1 _to impute the missing elements and compute the principal components._ Left: _For each of the 50 states, the imputed first principal component scores (averaged over 100 trials, and displayed with a standard deviation bar) are plotted against the first principal component scores computed using all the data._ Right: _The imputed principal component loadings (averaged over 100 trials, and displayed with a standard deviation bar) are plotted against the true principal component loadings._ 

_j_ th movie. One specific early example of this matrix had _n_ = 480 _,_ 189 customers and _p_ = 17 _,_ 770 movies. However, on average each customer had seen around 200 movies, so 99% of the matrix had missing elements. Table 12.2 illustrates the setup. 

In order to suggest a movie that a particular customer might like, Netflix needed a way to impute the missing values of this data matrix. The key idea is as follows: the set of movies that the _i_ th customer has seen will overlap with those that other customers have seen. Furthermore, some of those other customers will have similar movie preferences to the _i_ th customer. Thus, it should be possible to use similar customers’ ratings of movies that the _i_ th customer has not seen to predict whether the _i_ th customer will like those movies. 

More concretely, by applying Algorithm 12.1, we can predict the _i_ th cusˆ tomer’s rating for the _j_ th movie using _xij_ =[�] _[M] m_ =1 _[a]_[ˆ] _[im]_[ˆ] _[b][jm]_[.][Furthermore,] we can interpret the _M_ components in terms of “cliques” and “genres”: 

- ˆ 

- • _aim_ represents the strength with which the _i_ th user belongs to the _m_ th clique, where a _clique_ is a group of customers that enjoys movies of the _m_ th genre; 

- [ˆ] _bjm_ represents the strength with which the _j_ th movie belongs to the _m_ th _genre_ . 

Examples of genres include Romance, Western, and Action. 

Principal component models similar to Algorithm 12.1 are at the heart of many recommender systems. Although the data matrices involved are 

520 12. Unsupervised Learning 

|Jerry Maguire<br>Oceans<br>Road to Perdition<br>A Fortunate Man<br>Catch Me If You Can<br>Driving Miss Daisy<br>The Two Popes<br>The Laundromat<br>Code 8<br>The Social Network<br>_· · ·_<br>Customer 1<br>_•_<br>_•_<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 2<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>3<br>_· · ·_<br>Customer 3<br>_•_<br>2<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>_•_<br>_· · ·_<br>Customer 4<br>3<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 5<br>5<br>1<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 6<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>4<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 7<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_· · ·_<br>Customer 8<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 9<br>3<br>_•_<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>1<br>_•_<br>_•_<br>_· · ·_<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...|Jerry Maguire<br>Oceans<br>Road to Perdition<br>A Fortunate Man<br>Catch Me If You Can<br>Driving Miss Daisy<br>The Two Popes<br>The Laundromat<br>Code 8<br>The Social Network<br>_· · ·_<br>Customer 1<br>_•_<br>_•_<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 2<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>3<br>_· · ·_<br>Customer 3<br>_•_<br>2<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>_•_<br>_· · ·_<br>Customer 4<br>3<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 5<br>5<br>1<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 6<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>4<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 7<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_· · ·_<br>Customer 8<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>Customer 9<br>3<br>_•_<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>1<br>_•_<br>_•_<br>_· · ·_<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...|
|---|---|
|Customer 1<br>Customer 2<br>Customer 3<br>Customer 4<br>Customer 5<br>Customer 6<br>Customer 7<br>Customer 8<br>Customer 9<br>...|_•_<br>_•_<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>3<br>_· · ·_<br>_•_<br>2<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>_•_<br>_· · ·_<br>3<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>5<br>1<br>_•_<br>_•_<br>4<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>2<br>4<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>_•_<br>_•_<br>3<br>_•_<br>_•_<br>_· · ·_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_•_<br>_· · ·_<br>3<br>_•_<br>_•_<br>_•_<br>5<br>_•_<br>_•_<br>1<br>_•_<br>_•_<br>_· · ·_<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...<br>...|



**TABLE 12.2.** _Excerpt of the Netflix movie rating data. The movies are rated from 1 (worst) to 5 (best). The symbol • represents a missing value: a movie that was not rated by the corresponding customer._ 

typically massive, algorithms have been developed that can exploit the high level of missingness in order to perform efficient computations. 

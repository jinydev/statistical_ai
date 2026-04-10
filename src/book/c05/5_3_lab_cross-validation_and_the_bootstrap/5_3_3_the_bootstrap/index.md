---
layout: default
title: "index"
---

# _5.3.3 The Bootstrap_ 

We illustrate the use of the bootstrap in the simple example of Section 5.2, as well as on an example involving estimating the accuracy of the linear regression model on the `Auto` data set. 

Estimating the Accuracy of a Statistic of Interest 

One of the great advantages of the bootstrap approach is that it can be applied in almost all situations. No complicated mathematical calculations are required. While there are several implementations of the bootstrap in Python, its use for estimating standard error is simple enough that we write our own function below for the case when our data is stored in a dataframe. 

To illustrate the bootstrap, we start with a simple example. The `Portfolio` data set in the `ISLP` package is described in Section 5.2. The goal is to estimate the sampling variance of the parameter _α_ given in formula (5.7). We will create a function `alpha_func()` , which takes as input a dataframe `D` assumed to have columns `X` and `Y` , as well as a vector `idx` indicating which observations should be used to estimate _α_ . The function then outputs the estimate for _α_ based on the selected observations. 

```
In [15]:Portfolio=load_data('Portfolio')
defalpha_func(D,idx):
cov_=np.cov(D[['X','Y']].loc[idx],rowvar=False)
return((cov_[1,1]-cov_[0,1])/
(cov_[0,0]+cov_[1,1]-2*cov_[0,1]))
```

This function returns an estimate for _α_ based on applying the minimum variance formula (5.7) to the observations indexed by the argument `idx` . For instance, the following command estimates _α_ using all 100 observations. 

```
In [16]:alpha_func(Portfolio,range(100))
```

5.3 Lab: Cross-Validation and the Bootstrap 221 

```
Out[16]:0.5758
```

Next we randomly select 100 observations from `range(100)` , with replacement. This is equivalent to constructing a new bootstrap data set and recomputing _α_ ˆ based on the new data set. 

```
In [17]:rng=np.random.default_rng(0)
alpha_func(Portfolio,
rng.choice(100,
100,
replace=True))
```

---

## Sub-Chapters (하위 목차)

### 부트스트랩 연산 로그 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_3_1_out19_0.0912/)

수 천번 반복 복원수집된 궤적에서 추출된 획득 추정치의 단단한 신뢰 오차 마진을 눈과 코드로 직접 관찰합니다.

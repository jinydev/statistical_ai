---
layout: default
title: "index"
---

# 6.3 Dimension Reduction Methods 

The methods that we have discussed so far in this chapter have controlled variance in two different ways, either by using a subset of the original variables, or by shrinking their coefficients toward zero. All of these methods are defined using the original predictors, , X_2, \ldots, X_p$. We now explore a class of approaches that _transform_ the predictors and then fit a least squares model using the transformed variables. We will refer to these techniques as _dimension reduction_ methods. 

$$
Z_m = \sum_{j=1}^p \phi_{jm} X_j
$$

Let _Z_ 1 _, Z_ 2 _, . . . , ZM_ represent _M < p linear combinations_ of our original _p_ predictors. That is, 

for some constants _φ_ 1 _m, φ_ 2 _m . . . , φpm, m_ = 1 _, . . . , M_ . We can then fit the linear regression model 

$$
y_i = \theta_0 + \sum_{m=1}^M \theta_m z_{im} + \epsilon_i \quad (6.17)
$$

using least squares. Note that in (6.17), the regression coefficients are given by $	heta_0, 	heta_1, \ldots, 	heta_M$. If the constants $\phi_{1m}, \phi_{2m}, \ldots, \phi_{pm}$ are chosen wisely, then such dimension reduction approaches can often outperform least squares regression. In other words, fitting (6.17) using least squares can lead to better results than fitting (6.1) using least squares. 

The term _dimension reduction_ comes from the fact that this approach reduces the problem of estimating the _p_ +1 coefficients _β_ 0 _, β_ 1 _, . . . , βp_ to the 

6. Linear Model Selection and Regularization 

254 

![Figure 6.14](./img/6_14.png)

**FIGURE 6.14.** _The population size (_ `pop` _) and ad spending (_ `ad` _) for_ 100 _different cities are shown as purple circles. The green solid line indicates the first principal component, and the blue dashed line indicates the second principal component._ 

simpler problem of estimating the _M_ + 1 coefficients _θ_ 0 _, θ_ 1 _, . . . , θM_ , where _M < p_ . In other words, the dimension of the problem has been reduced from _p_ + 1 to _M_ + 1. 

Notice that from (6.16), 

$$
\sum_{m=1}^M \theta_m z_{im} = \sum_{m=1}^M \theta_m \sum_{j=1}^p \phi_{jm} x_{ij} = \sum_{j=1}^p \sum_{m=1}^M \theta_m \phi_{jm} x_{ij} = \sum_{j=1}^p \beta_j x_{ij} \quad (6.18)
$$

where 

$$
\beta_j = \sum_{m=1}^M \theta_m \phi_{jm}
$$

Hence (6.17) can be thought of as a special case of the original linear regression model given by (6.1). Dimension reduction serves to constrain the estimated $eta_j$ coefficients, since now they must take the form (6.18). This constraint on the form of the coefficients has the potential to bias the coefficient estimates. However, in situations where $ is large relative to $, selecting a value of  \ll p$ can significantly reduce the variance of the fitted coefficients. If  = p$, and all the $ are linearly independent, then (6.18) poses no constraints. In this case, no dimension reduction occurs, and so fitting (6.17) is equivalent to performing least squares on the original $ predictors. 

All dimension reduction methods work in two steps. First, the transformed predictors , Z_2, \ldots, Z_M$ are obtained. Second, the model is fit using these $ predictors. However, the choice of , Z_2, \ldots, Z_M$, or equivalently, the selection of the $\phi_{jm}$'s, can be achieved in different ways. In this chapter, we will consider two approaches for this task: _principal components_ and _partial least squares_ . 

---

## Sub-Chapters (하위 목차)

### 6.3.1 Principal Components Regression (주성분 중심 회귀 기법)
* [문서로 이동하기](./6_3_1_principal_components_regression/)

원래의 변수 행렬들이 지닌 정보량(Variance)을 가장 거대하게 포괄하는 주성분 벡터(Principal Component) 방향을 찾아 그것만을 선형 모델 인스턴스 X 요인으로 사용합니다.

### 6.3.2 Partial Least Squares (부분 최소 제곱법, PLS)
* [문서로 이동하기](./6_3_2_partial_least_squares/)

X 행렬 내의 독립적 변동성만 보는 PCA를 보완해, 처음 차원 추출부터 반응 변수 Y 그룹과의 상관성이 높은 쪽 방향으로만 유도하는 지도(Supervised) 기반의 차원 축소법입니다.

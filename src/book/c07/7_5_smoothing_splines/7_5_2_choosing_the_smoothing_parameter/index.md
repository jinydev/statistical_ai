---
layout: default
title: "index"
---

# _7.5.2 Choosing the Smoothing Parameter λ_ 

We have seen that a smoothing spline is simply a natural cubic spline with knots at every unique value of _xi_ . It might seem that a smoothing spline will have far too many degrees of freedom, since a knot at each data point allows a great deal of flexibility. But the tuning parameter _λ_ controls the roughness of the smoothing spline, and hence the _effective degrees of freedom_ . It is possible to show that as _λ_ increases from 0 to _∞_ , the effective effective degrees of freedom, which we write _dfλ_ , decrease from _n_ to 2. 

degrees of freedom 

In the context of smoothing splines, why do we discuss _effective_ degrees of freedom instead of degrees of freedom? Usually degrees of freedom refer to the number of free parameters, such as the number of coefficients fit in a polynomial or cubic spline. Although a smoothing spline has _n_ parameters and hence _n_ nominal degrees of freedom, these _n_ parameters are heavily constrained or shrunk down. Hence _dfλ_ is a measure of the flexibility of the smoothing spline—the higher it is, the more flexible (and the lower-bias but higher-variance) the smoothing spline. The definition of effective degrees of 

302 7. Moving Beyond Linearity 

freedom is somewhat technical. We can write

$$
\hat{\mathbf{g}}_\lambda = \mathbf{S}_\lambda \mathbf{y}
$$

where **g** ˆ _λ_ is the solution to (7.11) for a particular choice of _λ_ —that is, it is an _n_ -vector containing the fitted values of the smoothing spline at the training points _x_ 1 _, . . . , xn_ . Equation 7.12 indicates that the vector of fitted values when applying a smoothing spline to the data can be written as a _n × n_ matrix **S** _λ_ (for which there is a formula) times the response vector **y** . Then the effective degrees of freedom is defined to be

$$
df_\lambda = \text{tr}(\mathbf{S}_\lambda) = \sum_{i=1}^n \{\mathbf{S}_\lambda\}_{ii} \quad (7.12)
$$

the sum of the diagonal elements of the matrix **S** _λ_ . 

In fitting a smoothing spline, we do not need to select the number or location of the knots—there will be a knot at each training observation, _x_ 1 _, . . . , xn_ . Instead, we have another problem: we need to choose the value of _λ_ . It should come as no surprise that one possible solution to this problem is cross-validation. In other words, we can find the value of _λ_ that makes the cross-validated RSS as small as possible. It turns out that the _leaveone-out_ cross-validation error (LOOCV) can be computed very efficiently for smoothing splines, with essentially the same cost as computing a single fit, using the following formula:

$$
\text{LOOCV} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{g}_\lambda^{(-i)}(x_i)}{1 - \{\mathbf{S}_\lambda\}_{ii}} \right)^2 \quad (7.13)
$$

The notation _g_ ˆ _λ_[(] _[−][i]_[)] ( _xi_ ) indicates the fitted value for this smoothing spline evaluated at _xi_ , where the fit uses all of the training observations except ˆ for the _i_ th observation ( _xi, yi_ ). In contrast, _gλ_ ( _xi_ ) indicates the smoothing spline function fit to all of the training observations and evaluated at _xi_ . This remarkable formula says that we can compute each of these _leaveone-out_ fits using only _g_ ˆ _λ_ , the original fit to _all_ of the data![5] We have a very similar formula (5.2) on page 205 in Chapter 5 for least squares linear regression. Using (5.2), we can very quickly perform LOOCV for the regression splines discussed earlier in this chapter, as well as for least squares regression using arbitrary basis functions. 

Figure 7.8 shows the results from fitting a smoothing spline to the `Wage` data. The red curve indicates the fit obtained from pre-specifying that we would like a smoothing spline with 16 effective degrees of freedom. The blue curve is the smoothing spline obtained when _λ_ is chosen using LOOCV; in this case, the value of _λ_ chosen results in 6 _._ 8 effective degrees of freedom (computed using (7.13)). For this data, there is little discernible difference between the two smoothing splines, beyond the fact that the one with 16 degrees of freedom seems slightly wigglier. Since there is little difference between the two fits, the smoothing spline fit with 6 _._ 8 degrees of freedom 

> 5The exact formulas for computing _g_ ˆ( _xi_ ) and **S** _λ_ are very technical; however, efficient algorithms are available for computing these quantities. 

7.6 Local Regression 303 

---

## Sub-Chapters (하위 목차)

### Smoothing Spline Example (제약 기반 평활 곡선 스플라인 데이터 모델링 실제 예시 케이스 결과 뷰)
* [문서로 이동하기](./7_5_2_1_smoothing_spline/)

근로자 임금(Wage) 예측 등과 같은 전형적 다이내믹 일반화 타겟의 부드러운 평활 스플라인 모델 공식을 통계 알고리즘으로 적합했을 때, 모델 선형 대비 1순위에 랭크되는 매끄러운 곡면 디펜스 맵핑 투영 예제 결과치를 화면으로 확인합니다.

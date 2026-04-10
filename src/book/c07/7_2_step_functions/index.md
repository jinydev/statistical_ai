---
layout: default
title: "index"
---

# 7.2 Step Functions 

Using polynomial functions of the features as predictors in a linear model imposes a _global_ structure on the non-linear function of _X_ . We can instead use _step functions_ in order to avoid imposing such a global structure. Here step we break the range of _X_ into _bins_ , and fit a different constant in each bin. This amounts to converting a continuous variable into an _ordered categorical variable_ . 

function 

ordered categorical variable 

In greater detail, we create cutpoints _c_ 1, _c_ 2 _, . . . , cK_ in the range of _X_ , and then construct _K_ + 1 new variables

$$
\begin{align*}
C_0(X) &= I(X < c_1), \\
C_1(X) &= I(c_1 \le X < c_2), \\
C_2(X) &= I(c_2 \le X < c_3), \\
&\vdots \\
C_K(X) &= I(c_K \le X).
\end{align*}
$$

where _I_ ( _·_ ) is an _indicator function_ that returns a 1 if the condition is true, indicator and returns a 0 otherwise. For example, _I_ ( _cK ≤ X_ ) equals 1 if _cK ≤ X_ , and function equals 0 otherwise. These are sometimes called _dummy_ variables. Notice that for any value of _X_ , _C_ 0( _X_ ) + _C_ 1( _X_ ) + _· · ·_ + _CK_ ( _X_ ) = 1, since _X_ must be in exactly one of the _K_ + 1 intervals. We then use least squares to fit a linear model using _C_ 1( _X_ ) _, C_ 2( _X_ ) _, . . . , CK_ ( _X_ ) as predictors[2] :

$$
y_i = \beta_0 + \beta_1 C_1(x_i) + \beta_2 C_2(x_i) + \dots + \beta_K C_K(x_i) + \epsilon_i \quad (7.5)
$$

For a given value of _X_ , at most one of _C_ 1 _, C_ 2 _, . . . , CK_ can be non-zero. Note that when _X < c_ 1, all of the predictors in (7.5) are zero, so _β_ 0 can 

> 2We exclude _C_ 0( _X_ ) as a predictor in (7.5) because it is redundant with the intercept. This is similar to the fact that we need only two dummy variables to code a qualitative variable with three levels, provided that the model will contain an intercept. The decision to exclude _C_ 0( _X_ ) instead of some other _Ck_ ( _X_ ) in (7.5) is arbitrary. Alternatively, we could include _C_ 0( _X_ ) _, C_ 1( _X_ ) _, . . . , CK_ ( _X_ ), and exclude the intercept. 

7.3 Basis Functions 293 

---

## Sub-Chapters (하위 목차)

### Piecewise Constant (조각별 상수 함수)
* [문서로 이동하기](./7_2_1_piecewise_constant/)

잘려진 각 구역(바구니/빈) 안에서는 복잡성 없이 단순히 반응 변수들의 단일 상수 모델 평균치 레벨만으로 Y 데이터를 무단 예측하는 메커니즘을 수치적으로 이해하고 해석합니다.

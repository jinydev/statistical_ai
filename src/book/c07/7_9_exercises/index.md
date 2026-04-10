---
layout: default
title: "index"
---

# 7.9 Exercises 

_Conceptual_ 

1. It was mentioned in this chapter that a cubic regression spline with one knot at _ξ_ can be obtained using a basis of the form _x_ , _x_[2] , _x_[3] , ( _x − ξ_ )[3] +[,][where][(] _[x][ −][ξ]_[)][3] +[= (] _[x][ −][ξ]_[)][3][if] _[x > ξ]_[and][equals][0][otherwise.] We will now show that a function of the form 

_f_ ( _x_ ) = _β_ 0 + _β_ 1 _x_ + _β_ 2 _x_[2] + _β_ 3 _x_[3] + _β_ 4( _x − ξ_ )[3] + 

is indeed a cubic regression spline, regardless of the values of _β_ 0 _, β_ 1 _, β_ 2 _, β_ 3 _, β_ 4. 

(a) Find a cubic polynomial

$$
f_1(x) = a_1 + b_1 x + c_1 x^2 + d_1 x^3
$$

such that _f_ ( _x_ ) = _f_ 1( _x_ ) for all _x ≤ ξ_ . Express _a_ 1 _, b_ 1 _, c_ 1 _, d_ 1 in terms of _β_ 0 _, β_ 1 _, β_ 2 _, β_ 3 _, β_ 4. 

(b) Find a cubic polynomial

$$
f_2(x) = a_2 + b_2 x + c_2 x^2 + d_2 x^3
$$

such that _f_ ( _x_ ) = _f_ 2( _x_ ) for all _x > ξ_ . Express _a_ 2 _, b_ 2 _, c_ 2 _, d_ 2 in terms of _β_ 0 _, β_ 1 _, β_ 2 _, β_ 3 _, β_ 4. We have now established that _f_ ( _x_ ) is a piecewise polynomial. 

(c) Show that _f_ 1( _ξ_ ) = _f_ 2( _ξ_ ). That is, _f_ ( _x_ ) is continuous at _ξ_ . (d) Show that _f_ 1 _[′]_[(] _[ξ]_[) =] _[ f][ ′]_ 2[(] _[ξ]_[)][.][That][is,] _[f][ ′]_[(] _[x]_[)][is][continuous][at] _[ξ]_[.] (e) Show that _f_ 1 _[′′]_[(] _[ξ]_[) =] _[ f][ ′′]_ 2[(] _[ξ]_[)][.][That][is,] _[f][ ′′]_[(] _[x]_[)][is][continuous][at] _[ξ]_[.] 

Therefore, _f_ ( _x_ ) is indeed a cubic spline. 

_Hint: Parts (d) and (e) of this problem require knowledge of singlevariable calculus. As a reminder, given a cubic polynomial_

$$
f(x) = ax^3 + bx^2 + cx + d
$$

_the first derivative takes the form_

$$
f'(x) = 3ax^2 + 2bx + c
$$

_and the second derivative takes the form_

$$
f''(x) = 6ax + 2b
$$


2. Suppose that a curve _g_ ˆ is computed to smoothly fit a set of _n_ points using the following formula:

$$
\sum_{i=1}^n \left( y_i - \hat{g}(x_i) \right)^2 + \lambda \int \left[ \hat{g}^{(m)}(t) \right]^2 dt
$$

where _g_[(] _[m]_[)] represents the _m_ th derivative of _g_ (and _g_[(0)] = _g_ ). Provide example sketches of _g_ ˆ in each of the following scenarios. 

(a) _λ_ = _∞, m_ = 0. 

(b) _λ_ = _∞, m_ = 1. 

(c) _λ_ = _∞, m_ = 2. 

(d) _λ_ = _∞, m_ = 3. 

(e) _λ_ = 0 _, m_ = 3. 

3. Suppose we fit a curve with basis functions _b_ 1( _X_ ) = _X_ , _b_ 2( _X_ ) = ( _X −_ 1)[2] _I_ ( _X ≥_ 1). (Note that _I_ ( _X ≥_ 1) equals 1 for _X ≥_ 1 and 0 otherwise.) We fit the linear regression model

$$
Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \epsilon
$$

and obtain coefficient estimates _β_[ˆ] 0 = 1 _, β_[ˆ] 1 = 1 _, β_[ˆ] 2 = _−_ 2. Sketch the estimated curve between _X_ = _−_ 2 and _X_ = 2. Note the intercepts, slopes, and other relevant information. 

4. Suppose we fit a curve with basis functions _b_ 1( _X_ ) = _I_ (0 _≤ X ≤_ 2) _−_ ( _X −_ 1) _I_ (1 _≤ X ≤_ 2), _b_ 2( _X_ ) = ( _X −_ 3) _I_ (3 _≤ X ≤_ 4)+ _I_ (4 _< X ≤_ 5). We fit the linear regression model

$$
Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \epsilon
$$

and obtain coefficient estimates _β_[ˆ] 0 = 1 _, β_[ˆ] 1 = 1 _, β_[ˆ] 2 = 3. Sketch the estimated curve between _X_ = _−_ 2 and _X_ = 6. Note the intercepts, slopes, and other relevant information. 

5. Consider two curves, _g_ ˆ1 and _g_ ˆ2, defined by

$$
\begin{align*}
\hat{g}_1 &= \arg \min_g \left( \dots \right) \\
\hat{g}_2 &= \arg \min_g \left( \dots \right)
\end{align*}
$$

where _g_[(] _[m]_[)] represents the _m_ th derivative of _g_ . 

- (a) As _λ →∞_ , will _g_ ˆ1 or _g_ ˆ2 have the smaller training RSS? 

- (b) As _λ →∞_ , will _g_ ˆ1 or _g_ ˆ2 have the smaller test RSS? 

- (c) For _λ_ = 0, will _g_ ˆ1 or _g_ ˆ2 have the smaller training and test RSS? 

7.9 Exercises 327 

---

## Sub-Chapters (하위 목차)

### Applied (현실 비선형 도메인 예측 응용 데이터 코드 시나리오 모델링 통계 문제 해결 풀이장)
* [문서로 이동하기](./7_9_1_applied/)

정규화/비정규화된 현업 혹은 경제 데이터와 기상 데이터 베이스 시나리오 등을 유사 응용 데이터 파이프라인으로 로딩 마운트하고 K-Fold 체계를 접목해 나만의 분석 모델 함수 커스텀을 직접 세팅한 뒤 어떻게 최적의 K수량 노드 매듭점 파라미터 수치값을 찾아 개선 곡면 예측 지표 체계로 만들 수 있는지 스스로 주피터 환경에서 코드를 완성 서브밋하고 결과 통계치를 유의미하게 탐구 제출할 수 있습니다.

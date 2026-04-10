---
layout: default
title: "index"
---

# 9.7 Exercises 

_Conceptual_ 

1. This problem involves hyperplanes in two dimensions. 

   - (a) Sketch the hyperplane 1 + 3 _X_ 1 _− X_ 2 = 0. Indicate the set of points for which 1 + 3 _X_ 1 _− X_ 2 _>_ 0, as well as the set of points for which 1 + 3 _X_ 1 _− X_ 2 _<_ 0. 

   - (b) On the same plot, sketch the hyperplane _−_ 2 + _X_ 1 + 2 _X_ 2 = 0. Indicate the set of points for which _−_ 2 + _X_ 1 + 2 _X_ 2 _>_ 0, as well as the set of points for which _−_ 2 + _X_ 1 + 2 _X_ 2 _<_ 0. 

2. We have seen that in _p_ = 2 dimensions, a linear decision boundary takes the form _β_ 0 + _β_ 1 _X_ 1 + _β_ 2 _X_ 2 = 0. We now investigate a non-linear decision boundary. 

   - (a) Sketch the curve

$$
(1 + X_1)^2 + (2 - X_2)^2 = 4
$$

- (b) On your sketch, indicate the set of points for which

$$
(1 + X_1)^2 + (2 - X_2)^2 > 4
$$

as well as the set of points for which

$$
(1 + X_1)^2 + (2 - X_2)^2 \le 4
$$

- (c) Suppose that a classifier assigns an observation to the blue class if

$$
(1 + X_1)^2 + (2 - X_2)^2 > 4
$$

and to the red class otherwise. To what class is the observation (0 _,_ 0) classified? ( _−_ 1 _,_ 1)? (2 _,_ 2)? (3 _,_ 8)? 

- (d) Argue that while the decision boundary in (c) is not linear in terms of _X_ 1 and _X_ 2, it is linear in terms of _X_ 1, _X_ 1[2][,] _[X]_[2][,][and] _X_ 2[2][.] 

396 9. Support Vector Machines 

3. Here we explore the maximal margin classifier on a toy data set. 

   - (a) We are given _n_ = 7 observations in _p_ = 2 dimensions. For each observation, there is an associated class label. 

|Obs.|_X_1|_X_2|_Y_|
|---|---|---|---|
|1|3|4|Red|
|2|2|2|Red|
|3|4|4|Red|
|4|1|4|Red|
|5|2|1|Blue|
|6|4|3|Blue|
|7|4|1|Blue|



Sketch the observations. 

- (b) Sketch the optimal separating hyperplane, and provide the equation for this hyperplane (of the form (9.1)). 

- (c) Describe the classification rule for the maximal margin classifier. It should be something along the lines of “Classify to Red if _β_ 0 + _β_ 1 _X_ 1 + _β_ 2 _X_ 2 _>_ 0, and classify to Blue otherwise.” Provide the values for _β_ 0, _β_ 1, and _β_ 2. 

- (d) On your sketch, indicate the margin for the maximal margin hyperplane. 

- (e) Indicate the support vectors for the maximal margin classifier. 

- (f) Argue that a slight movement of the seventh observation would not affect the maximal margin hyperplane. 

- (g) Sketch a hyperplane that is _not_ the optimal separating hyperplane, and provide the equation for this hyperplane. 

- (h) Draw an additional observation on the plot so that the two classes are no longer separable by a hyperplane. 

---

## Sub-Chapters (하위 목차)

### Applied (코드 적용 기반의 비선형 모형 구축 코스)
* [문서로 이동하기](./9_7_1_applied/)

자동차 휘발유 데이터 집합 등에 SVC를 피팅하고 스스로 최적 C와 감마 하이퍼파라미터를 그리드 서치하는 통계 전문가적 문제해결 능력을 검증합니다.

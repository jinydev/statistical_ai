---
layout: default
title: "index"
---

# _6.2.1 Ridge Regression_ 

Recall from Chapter 3 that the least squares fitting procedure estimates _β_ 0 _, β_ 1 _, . . . , βp_ using the values that minimize

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 = \text{RSS}
$$

_Ridge regression_ is very similar to least squares, except that the coefficients are estimated by minimizing a slightly different quantity. In particular, the ridge regression coefficient estimates _β_[ˆ] _[R]_ are the values that minimize

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \sum_{j=1}^p \beta_j^2 \quad (6.5)
$$

where _λ ≥_ 0 is a _tuning parameter_ , to be determined separately. Equa- tuning tion 6.5 trades off two different criteria. As with least squares, ridge regresparameter sion seeks coefficient estimates that fit the data well, by making the RSS small. However, the second term, _λ_[�] _j[β] j_[2][,][called][a] _[shrinkage][penalty]_[,][is] shrinkage small when _β_ 1 _, . . . , βp_ are close to zero, and so it has the effect of _shrinking_ penalty the estimates of _βj_ towards zero. The tuning parameter _λ_ serves to control 

6.2 Shrinkage Methods 241 

![Figure 6.4](./img/6_4.png)

**FIGURE 6.4.** _The standardized ridge regression coefficients are displayed for the_ `Credit` _data set, as a function of λ and ∥β_[ˆ] _λ[R][∥]_[2] _[/][∥][β]_[ˆ] _[∥]_[2] _[.]_ 

the relative impact of these two terms on the regression coefficient estimates. When _λ_ = 0, the penalty term has no effect, and ridge regression will produce the least squares estimates. However, as _λ →∞_ , the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. Unlike least squares, which generates only one set of coefficient estimates, ridge regression will produce a different set of coefficient estimates, _β_[ˆ] _λ[R]_[,][for][each][value][of] _[λ]_[.][Selecting][a][good][value][for] _[λ]_[is][critical;] we defer this discussion to Section 6.2.3, where we use cross-validation. 

Note that in (6.5), the shrinkage penalty is applied to _β_ 1 _, . . . , βp_ , but not to the intercept _β_ 0. We want to shrink the estimated association of each variable with the response; however, we do not want to shrink the intercept, which is simply a measure of the mean value of the response when _xi_ 1 = _xi_ 2 = _. . ._ = _xip_ = 0. If we assume that the variables—that is, the columns of the data matrix **X** —have been centered to have mean zero before ridge regression is performed, then the estimated intercept will take the form _β_[ˆ] 0 = _y_ ¯ =[�] _[n] i_ =1 _[y][i][/n]_[.] 

---

## Sub-Chapters (하위 목차)

### An Application to the Credit Data (신용 데이터 적용 사례)
* [문서로 이동하기](./6_2_1_1_an_application_to_the_credit_data/)

은행 신용도 데이터셋에 릿지 함수를 튜닝했을 때 변수들의 계수값이 조율 파라미터 $\lambda$의 상승에 따라 어떻게 부드럽게 감쇠하는지 등고 플롯으로 확인합니다.

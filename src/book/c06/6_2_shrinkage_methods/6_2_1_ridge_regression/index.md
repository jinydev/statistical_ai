---
layout: default
title: "index"
---

# 6.2.1 Ridge Regression 

Recall from Chapter 3 that the least squares fitting procedure estimates $\beta_0, \beta_1, \ldots, \beta_p$ using the values that minimize

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 = \text{RSS}
$$

_Ridge regression_ is very similar to least squares, except that the coefficients are estimated by minimizing a slightly different quantity. In particular, the ridge regression coefficient estimates $\hat{\beta}^R$ are the values that minimize

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \sum_{j=1}^p \beta_j^2 \quad (6.5)
$$

where $\lambda \ge 0$ is a _tuning parameter_ , to be determined separately. Equation 6.5 trades off two different criteria. As with least squares, ridge regression seeks coefficient estimates that fit the data well, by making the RSS small. However, the second term, $\lambda \sum_j \beta_j^2$, called a _shrinkage penalty_, is small when $\beta_1, \ldots, \beta_p$ are close to zero, and so it has the effect of _shrinking_ the estimates of $\beta_j$ towards zero. The tuning parameter $\lambda$ serves to control the relative impact of these two terms on the regression coefficient estimates. When $\lambda = 0$, the penalty term has no effect, and ridge regression will produce the least squares estimates. However, as $\lambda \to \infty$, the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. Unlike least squares, which generates only one set of coefficient estimates, ridge regression will produce a different set of coefficient estimates, $\hat{\beta}_{\lambda}^R$, for each value of $\lambda$. Selecting a good value for $\lambda$ is critical; we defer this discussion to Section 6.2.3, where we use cross-validation. 

![Figure 6.4](./img/6_4.png)

**FIGURE 6.4.** _The standardized ridge regression coefficients are displayed for the_ `Credit` _data set, as a function of $\lambda$ and $\|\hat{\beta}_{\lambda}^R\|_2 / \|\hat{\beta}\|_2$._ 

Note that in (6.5), the shrinkage penalty is applied to $\beta_1, \ldots, \beta_p$, but not to the intercept $\beta_0$. We want to shrink the estimated association of each variable with the response; however, we do not want to shrink the intercept, which is simply a measure of the mean value of the response when $x_{i1} = x_{i2} = \ldots = x_{ip} = 0$. If we assume that the variables—that is, the columns of the data matrix $\mathbf{X}$—have been centered to have mean zero before ridge regression is performed, then the estimated intercept will take the form $\hat{\beta}_0 = \bar{y} = \sum_{i=1}^n y_i / n$. 

---

## Sub-Chapters (하위 목차)

### An Application to the Credit Data (신용 데이터 적용 사례)
* [문서로 이동하기](./6_2_1_1_an_application_to_the_credit_data/)

은행 신용도 데이터셋에 릿지 함수를 튜닝했을 때 변수들의 계수값이 조율 파라미터 $\lambda$의 상승에 따라 어떻게 부드럽게 감쇠하는지 등고 플롯으로 확인합니다.

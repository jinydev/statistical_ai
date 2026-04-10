---
layout: default
title: "index"
---

# _9.3.1 with Non-Linear Decision Boundaries Classification_ 

The support vector classifier is a natural approach for classification in the two-class setting, if the boundary between the two classes is linear. However, in practice we are sometimes faced with non-linear class boundaries. For instance, consider the data in the left-hand panel of Figure 9.8. It is clear that a support vector classifier or any linear classifier will perform poorly here. Indeed, the support vector classifier shown in the right-hand panel of Figure 9.8 is useless here. 

In Chapter 7, we are faced with an analogous situation. We see there that the performance of linear regression can suffer when there is a nonlinear relationship between the predictors and the outcome. In that case, we consider enlarging the feature space using functions of the predictors, such as quadratic and cubic terms, in order to address this non-linearity. In the case of the support vector classifier, we could address the problem of possibly non-linear boundaries between classes in a similar way, by enlarging the feature space using quadratic, cubic, and even higher-order polynomial functions of the predictors. For instance, rather than fitting a support vector classifier using _p_ features

$$
X_1, \dots, X_p
$$

we could instead fit a support vector classifier using 2 _p_ features

$$
X_1, X_1^2, X_2, X_2^2, \dots, X_p, X_p^2
$$

9.3 Support Vector Machines 379 

Then (9.12)–(9.15) would become

$$
\begin{align*}
\underset{\beta_0, \beta_{j1}, \beta_{j2}, \epsilon_i, M}{\text{maximize}} & \quad M \quad (9.16) \\
\text{subject to } & y_i \left( \beta_0 + \sum_{j=1}^p \beta_{j1} x_{ij} + \sum_{j=1}^p \beta_{j2} x_{ij}^2 \right) \ge M(1-\epsilon_i) \\
& \sum_{i=1}^n \epsilon_i \le C, \quad \epsilon_i \ge 0, \quad \sum_{j=1}^p \sum_{k=1}^2 \beta_{jk}^2 = 1
\end{align*}
$$

Why does this lead to a non-linear decision boundary? In the enlarged feature space, the decision boundary that results from (9.16) is in fact linear. But in the original feature space, the decision boundary is of the form _q_ ( _x_ ) = 0, where _q_ is a quadratic polynomial, and its solutions are generally non-linear. One might additionally want to enlarge the feature space with higher-order polynomial terms, or with interaction terms of the form _XjXj[′]_ for _j_ = _j[′]_ . Alternatively, other functions of the predictors could be considered rather than polynomials. It is not hard to see that there are many possible ways to enlarge the feature space, and that unless we are careful, we could end up with a huge number of features. Then computations would become unmanageable. The support vector machine, which we present next, allows us to enlarge the feature space used by the support vector classifier in a way that leads to efficient computations. 

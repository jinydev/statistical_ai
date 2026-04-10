---
layout: default
title: "index"
---

# _3.6.6 Non-linear Transformations of the Predictors_ 

The model matrix builder can include terms beyond just column names and interactions. For instance, the `poly()` function supplied in `ISLP` specifies `poly()` that columns representing polynomial functions of its first argument are added to the model matrix. 

```
In [32]:X=MS([poly('lstat',degree=2),'age']).fit_transform(Boston)
model3=sm.OLS(y,X)
results3=model3.fit()
summarize(results3)
```

```
Out[32]:
```

|||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`17.7151`|`0.781`|`22.681`|`0.000`|
|`poly(lstat, `|`degree=2)[0]`|`-179.2279`|`6.733`|`-26.620`|`0.000`|
|`poly(lstat, `|`degree=2)[1]`|`72.9908`|`5.482`|`13.315`|`0.000`|
||`age`|`0.0703`|`0.011`|`6.471`|`0.000`|



The effectively zero $p$-value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model. 

By default, `poly()` creates a basis matrix for inclusion in the model matrix whose columns are _orthogonal polynomials_ , which are designed for sta- orthogonal ble least squares computations.[13] Alternatively, had we included an argupolynomial ment `raw=True` in the above call to `poly()` , the basis matrix would consist simply of `lstat` and `lstat**2` . Since either of these bases represent quadratic polynomials, the fitted values would not change in this case, just the polynomial coefficients. Also by default, the columns created by `poly()` do not include an intercept column as that is automatically added by `MS()` . 

We use the `anova_lm()` function to further quantify the extent to which `anova_lm()` the quadratic fit is superior to the linear fit. 

---

## Sub-Chapters (하위 목차)

### Model Comparison (분산분석을 통한 모델 비교)
* [문서로 이동하기](./3_6_6_1_in_33_anovalmresults1_results3/)

`anova_lm()` 함수를 사용해 선형 모델과 비선형 모델 간의 잔차를 분석하고 추가 계수가 기여하는 통계적 유의성을 검증하는 프로세스입니다.
두 모델 중 어느 것이 더 우수한가 분산분석(ANOVA)으로 확인합니다.

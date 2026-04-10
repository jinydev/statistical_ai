---
layout: default
title: "index"
---

# _6.5.3 PCR and PLS Regression_ 

Principal Components Regression 

Principal components regression (PCR) can be performed using `PCA()` from `PCA()` the `sklearn.decomposition` module. We now apply PCR to the `Hitters` data, in order to predict `Salary` . Again, ensure that the missing values have been removed from the data, as described in Section 6.5.1. 

We use `LinearRegression()` to fit the regression model here. Note that `Linear` it fits an intercept by default, unlike the `OLS()` function seen earlier in `Regression()` Section 6.5.1. 

6.5 Lab: Linear Models and Regularization Methods 

281 

```
In [49]:pca=PCA(n_components=2)
linreg=skl.LinearRegression()
pipe=Pipeline([('pca',pca),
('linreg',linreg)])
pipe.fit(X,Y)
pipe.named_steps['linreg'].coef_
```

```
Out[49]:array([0.09846131,0.4758765])
```

When performing PCA, the results vary depending on whether the data has been _standardized_ or not. As in the earlier examples, this can be accomplished by including an additional step in the pipeline. 

```
In [50]:pipe=Pipeline([('scaler',scaler),
('pca',pca),
('linreg',linreg)])
pipe.fit(X,Y)
pipe.named_steps['linreg'].coef_
```

```
Out[50]:array([106.36859204,-21.60350456])
```

We can of course use CV to choose the number of components, by using `skm.GridSearchCV` , in this case fixing the parameters to vary the `n_components` . 

```
In [51]:param_grid={'pca__n_components':range(1,20)}
grid=skm.GridSearchCV(pipe,
param_grid ,
cv=kfold,
scoring='neg_mean_squared_error')
grid.fit(X,Y)
```

Let’s plot the results as we have for other methods. 

```
In [52]:pcr_fig,ax=subplots(figsize=(8,8))
n_comp=param_grid['pca__n_components']
ax.errorbar(n_comp,
-grid.cv_results_['mean_test_score'],
grid.cv_results_['std_test_score']/np.sqrt(K))
ax.set_ylabel('Cross-validatedMSE',fontsize=20)
ax.set_xlabel('#principalcomponents',fontsize=20)
ax.set_xticks(n_comp[::2])
ax.set_ylim([50000,250000]);
```

We see that the smallest cross-validation error occurs when 17 components are used. However, from the plot we also see that the cross-validation error is roughly the same when only one component is included in the model. This suggests that a model that uses just a small number of components might suffice. 

The CV score is provided for each possible number of components from 1 to 19 inclusive. The `PCA()` method complains if we try to fit an intercept only with `n_components=0` so we also compute the $\text{MSE}$ for just the null model with these splits. 

```
In [53]:Xn=np.zeros((X.shape[0],1))
cv_null=skm.cross_validate(linreg,
```

6. Linear Model Selection and Regularization 

282 

```
Xn,
Y,
cv=kfold,
scoring='neg_mean_squared_error')
-cv_null['test_score'].mean()
```

---

## Sub-Chapters (하위 목차)

### Jupyter Notebook Output (결과 통계학적 반환값 확인 점검)
* [문서로 이동하기](./6_5_3_1_out53_204139.31/)

Jupyter에서 출력되는 파이썬 콘솔의 테스트 평균 제곱근 오차(MSE) 지표 통계를 확인하며, 규제기법을 동원하지 않은 일반 선형회귀 및 라쏘 모델 성능과의 퍼포먼스 우위를 교차 비교합니다.

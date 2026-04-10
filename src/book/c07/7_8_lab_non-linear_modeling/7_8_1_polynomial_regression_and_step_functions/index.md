---
layout: default
title: "index"
---

# _7.8.1 Polynomial Regression and Step Functions_ 

We start by demonstrating how Figure 7.1 can be reproduced. Let’s begin by loading the data. 

```
In [3]:Wage=load_data('Wage')
y=Wage['wage']
age=Wage['age']
```

7.8 Lab: Non-Linear Modeling 311 

Throughout most of this lab, our response is `Wage['wage']` , which we have stored as `y` above. As in Section 3.6.6, we will use the `poly()` function to create a model matrix that will fit a 4th degree polynomial in `age` . 

```
In [4]:poly_age=MS([poly('age',degree=4)]).fit(Wage)
M=sm.OLS(y,poly_age.transform(Wage)).fit()
summarize(M)
```

```
Out[4]:
```

|||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`111.7036`|`0.729`|`153.283`|`0.000`|
|`poly(age, `|`degree=4)[0]`|`447.0679`|`39.915`|`11.201`|`0.000`|
|`poly(age, `|`degree=4)[1] `|`-478.3158`|`39.915`|`-11.983`|`0.000`|
|`poly(age, `|`degree=4)[2]`|`125.5217`|`39.915`|`3.145`|`0.002`|
|`poly(age, `|`degree=4)[3]`|`-77.9112`|`39.915`|`-1.952`|`0.051`|



This polynomial is constructed using the function `poly()` , which creates a special _transformer_ `Poly()` (using `sklearn` terminology for feature transformer transformations such as `PCA()` seen in Section 6.5.3) which allows for easy evaluation of the polynomial at new data points. Here `poly()` is referred to as a _helper_ function, and sets up the transformation; `Poly()` is the ac- helper tual workhorse that computes the transformation. See also the discussion of transformations on page 118. 

In the code above, the first line executes the `fit()` method using the dataframe `Wage` . This recomputes and stores as attributes any parameters needed by `Poly()` on the training data, and these will be used on all subsequent evaluations of the `transform()` method. For example, it is used on the second line, as well as in the plotting function developed below. We now create a grid of values for `age` at which we want predictions. 

```
In [5]:age_grid=np.linspace(age.min(),
age.max(),
100)
age_df=pd.DataFrame({'age':age_grid})
```

Finally, we wish to plot the data and add the fit from the fourth-degree polynomial. As we will make several similar plots below, we first write a function to create all the ingredients and produce the plot. Our function takes in a model specification (here a basis specified by a transform), as well as a grid of `age` values. The function produces a fitted curve as well as 95% confidence bands. By using an argument for `basis` we can produce and plot the results with several different transforms, such as the splines we will see shortly. 

```
In [6]:defplot_wage_fit(age_df,
basis,
title):
X=basis.transform(Wage)
Xnew=basis.transform(age_df)
M=sm.OLS(y,X).fit()
preds=M.get_prediction(Xnew)
bands=preds.conf_int(alpha=0.05)
fig,ax=subplots(figsize=(8,8))
ax.scatter(age,
y,
```

312 7. Moving Beyond Linearity 

```
facecolor='gray',
alpha=0.5)
forval,lsinzip([preds.predicted_mean ,
bands[:,0],
bands[:,1]],
['b','r--','r--']):
ax.plot(age_df.values,val,ls,linewidth=3)
ax.set_title(title,fontsize=20)
ax.set_xlabel('Age',fontsize=20)
ax.set_ylabel('Wage',fontsize=20);
returnax
```

We include an argument `alpha` to `ax.scatter()` to add some transparency to the points. This provides a visual indication of density. Notice the use of the `zip()` function in the `for` loop above (see Section 2.3.8). We have three lines to plot, each with different colors and line types. Here `zip()` conveniently bundles these together as iterators in the loop.[7] We now plot the fit of the fourth-degree polynomial using this function. 

iterator 

```
In [7]:plot_wage_fit(age_df,
```

```
poly_age,
'Degree-4Polynomial');
```

With polynomial regression we must decide on the degree of the polynomial to use. Sometimes we just wing it, and decide to use second or third degree polynomials, simply to obtain a nonlinear fit. But we can make such a decision in a more systematic way. One way to do this is through hypothesis tests, which we demonstrate here. We now fit a series of models ranging from linear (degree-one) to degree-five polynomials, and look to determine the simplest model that is sufficient to explain the relationship between `wage` and `age` . We use the `anova_lm()` function, which performs a series of ANOVA tests. An _analysis of variance_ or ANOVA tests the null hypothesis analysis of that a model _M_ 1 is sufficient to explain the data against the alternative variance hypothesis that a more complex model _M_ 2 is required. The determination is based on an F-test. To perform the test, the models _M_ 1 and _M_ 2 must be _nested_ : the space spanned by the predictors in _M_ 1 must be a subspace of the space spanned by the predictors in _M_ 2. In this case, we fit five different polynomial models and sequentially compare the simpler model to the more complex model. 

```
In [8]:models=[MS([poly('age',degree=d)])
fordinrange(1,6)]
```

```
Xs=[model.fit_transform(Wage)formodelinmodels]
anova_lm(*[sm.OLS(y,X_).fit()
forX_inXs])
```

```
Out[8]:
```

||`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|
|`0`|`2998.0`|`5.022e+06`|`0.0`|`NaN`|`NaN`|`NaN`|
|`1`|`2997.0`|`4.793e+06`|`1.0`|`228786.010`|`143.593`|`2.364e-32`|
|`2`|`2996.0`|`4.778e+06`|`1.0`|`15755.694`|`9.889`|`1.679e-03`|
|`3`|`2995.0`|`4.772e+06`|`1.0`|`6070.152`|`3.810`|`5.105e-02`|



> 7In `Python` speak, an “iterator” is an object with a finite number of values, that can be iterated on, as in a loop. 

7.8 Lab: Non-Linear Modeling 

313 

```
42994.04.770e+061.01282.5630.8053.697e-01
```

Notice the `*` in the `anova_lm()` line above. This function takes a variable number of non-keyword arguments, in this case fitted models. When these models are provided as a list (as is done here), it must be prefixed by `*` . 

The p-value comparing the linear `models[0]` to the quadratic `models[1]` is essentially zero, indicating that a linear fit is not sufficient.[8] Similarly the p-value comparing the quadratic `models[1]` to the cubic `models[2]` is very low (0.0017), so the quadratic fit is also insufficient. The p-value comparing the cubic and degree-four polynomials, `models[2]` and `models[3]` , is approximately 5%, while the degree-five polynomial `models[4]` seems unnecessary because its p-value is 0.37. Hence, either a cubic or a quartic polynomial appear to provide a reasonable fit to the data, but lower- or higher-order models are not justified. 

In this case, instead of using the `anova()` function, we could have obtained these p-values more succinctly by exploiting the fact that `poly()` creates orthogonal polynomials. 

---

## Sub-Chapters (하위 목차)

### Jupyter Notebook Output (파이썬 다항 차원 스텝 선형 인스턴스 회귀 결과 통계 도축 스코어 표 콘솔 디스플레이 지표 모음 확인)
* [문서로 이동하기](./7_8_1_1_out10_143.59228/)

모델 추론 결과 요약 통계 지표 함수 반환 정보 코드 리전과 인덱스 로케이션 상의 스텝형 구역 분리 시 발생된 구간 계단식 모델링 데이터 손실 잔차 MSE 적합 평가 변동 폭 값들을 화면 테이블로 점검 체인 확인합니다.

---
layout: default
title: "index"
---

# _4.7.2 Logistic Regression_ 

Next, we will fit a logistic regression model in order to predict `Direction` using `Lag1` through `Lag5` and `Volume` . The `sm.GLM()` function fits _gener-_ `sm.GLM()` _alized linear models_ , a class of models that includes logistic regression. generalized Alternatively, the function `sm.Logit()` fits a logistic regression model dilinear model rectly. The syntax of `sm.GLM()` is similar to that of `sm.OLS()` , except that we must pass in the argument `family=sm.families.Binomial()` in order to tell `statsmodels` to run a logistic regression rather than some other type of generalized linear model. 

```
In [7]:allvars=Smarket.columns.drop(['Today','Direction','Year'])
design=MS(allvars)
X=design.fit_transform(Smarket)
y=Smarket.Direction=='Up'
glm=sm.GLM(y,
X,
family=sm.families.Binomial())
results=glm.fit()
summarize(results)
```

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 175 

```
Out[7]:
```

||`coef`|`std err`|`z`|`P>|z|`|
|---|---|---|---|---|
|`intercept `|`-0.1260`|`0.241`|`-0.523`|`0.601`|
|`Lag1`|`-0.0731`|`0.050`|`-1.457`|`0.145`|
|`Lag2`|`-0.0423`|`0.050`|`-0.845`|`0.398`|
|`Lag3`|`0.0111`|`0.050`|`0.222`|`0.824`|
|`Lag4`|`0.0094`|`0.050`|`0.187`|`0.851`|
|`Lag5`|`0.0103`|`0.050`|`0.208`|`0.835`|
|`Volume`|`0.1354`|`0.158`|`0.855`|`0.392`|



The smallest _p_ -value here is associated with `Lag1` . The negative coefficient for this predictor suggests that if the market had a positive return yesterday, then it is less likely to go up today. However, at a value of 0.15, the _p_ -value is still relatively large, and so there is no clear evidence of a real association between `Lag1` and `Direction` . 

We use the `params` attribute of `results` in order to access just the coefficients for this fitted model. 

---

## Sub-Chapters (하위 목차)

### Jupyter Notebook Output (노트북 출력 결과)
* [문서로 이동하기](./4_7_2_1_out14_252_9/)

파이썬 분류 코드 실행 후 콘솔에서 튀어나오는 모델 객체 크기나 정확도 반환값들에 대해 해석력을 점검합니다.

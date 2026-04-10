---
layout: default
title: "index"
---

# _4.7.7 Linear and Poisson Regression on the Bikeshare Data_ 

Here we fit linear and Poisson regression models to the `Bikeshare` data, as described in Section 4.6. The response `bikers` measures the number of bike rentals per hour in Washington, DC in the period 2010–2012. 

```
In [64]:Bike=load_data('Bikeshare')
```

Let’s have a peek at the dimensions and names of the variables in this dataframe. 

```
In [65]:Bike.shape,Bike.columns
```

4.7 Lab: Logistic Regression, LDA, QDA, and KNN 

189 

```
Out[65]:((8645,15),
```

```
Index(['season','mnth','day','hr','holiday','weekday',
'workingday','weathersit','temp','atemp','hum',
'windspeed','casual','registered','bikers'],
dtype='object'))
```

Linear Regression 

We begin by fitting a linear regression model to the data. 

```
In [66]:X=MS(['mnth',
```

```
'hr',
'workingday',
'temp',
'weathersit']).fit_transform(Bike)
Y=Bike['bikers']
M_lm=sm.OLS(Y,X).fit()
summarize(M_lm)
```

|**`Out[66]:`**||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`-68.6317`|`5.307 `|`-12.932`|`0.000`|
||`mnth[Feb]`|`6.8452`|`4.287`|`1.597`|`0.110`|
||`mnth[March]`|`16.5514`|`4.301`|`3.848`|`0.000`|
||`mnth[April]`|`41.4249`|`4.972`|`8.331`|`0.000`|
||`mnth[May]`|`72.5571`|`5.641`|`12.862`|`0.000`|
||`mnth[June]`|`67.8187`|`6.544`|`10.364`|`0.000`|
||`mnth[July]`|`45.3245`|`7.081`|`6.401`|`0.000`|
||`mnth[Aug]`|`53.2430`|`6.640`|`8.019`|`0.000`|
||`mnth[Sept]`|`66.6783`|`5.925`|`11.254`|`0.000`|
||`mnth[Oct]`|`75.8343`|`4.950`|`15.319`|`0.000`|
||`mnth[Nov]`|`60.3100`|`4.610`|`13.083`|`0.000`|
||`mnth[Dec]`|`46.4577`|`4.271`|`10.878`|`0.000`|
||`hr[1]`|`-14.5793`|`5.699`|`-2.558`|`0.011`|
||`hr[2]`|`-21.5791`|`5.733`|`-3.764`|`0.000`|
||`hr[3]`|`-31.1408`|`5.778`|`-5.389`|`0.000`|
||`.....`|`.......`|`.....`|`.....`|`.....`|



There are 24 levels in `hr` and 40 rows in all, so we have truncated the summary. In `M_lm` , the first levels `hr[0]` and `mnth[Jan]` are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines. For example, the Feb coefficient of 6 _._ 845 signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January. Similarly there are about 16.5 more riders in March than in January. 

The results seen in Section 4.6.1 used a slightly different coding of the variables `hr` and `mnth` , as follows: 

```
In [67]:hr_encode=contrast('hr','sum')
mnth_encode=contrast('mnth','sum')
```

Refitting again: 

```
In [68]:X2=MS([mnth_encode ,
hr_encode,
'workingday',
'temp',
```

190 4. Classification 

```
'weathersit']).fit_transform(Bike)
M2_lm=sm.OLS(Y,X2).fit()
S2=summarize(M2_lm)
S2
```

|**`Out[68]:`**||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|---|
||`intercept`|`73.5974`|`5.132`|`14.340`|`0.000`|
||`mnth[Jan]`|`-46.0871`|`4.085 `|`-11.281`|`0.000`|
||`mnth[Feb]`|`-39.2419`|`3.539 `|`-11.088`|`0.000`|
||`mnth[March]`|`-29.5357`|`3.155`|`-9.361`|`0.000`|
||`mnth[April]`|`-4.6622`|`2.741`|`-1.701`|`0.089`|
||`mnth[May]`|`26.4700`|`2.851`|`9.285`|`0.000`|
||`mnth[June]`|`21.7317`|`3.465`|`6.272`|`0.000`|
||`mnth[July]`|`-0.7626`|`3.908`|`-0.195`|`0.845`|
||`mnth[Aug]`|`7.1560`|`3.535`|`2.024`|`0.043`|
||`mnth[Sept]`|`20.5912`|`3.046`|`6.761`|`0.000`|
||`mnth[Oct]`|`29.7472`|`2.700`|`11.019`|`0.000`|
||`mnth[Nov]`|`14.2229`|`2.860`|`4.972`|`0.000`|
||`hr[0]`|`-96.1420`|`3.955 `|`-24.307`|`0.000`|
||`hr[1]`|`-110.7213`|`3.966 `|`-27.916`|`0.000`|
||`hr[2]`|`-117.7212`|`4.016 `|`-29.310`|`0.000`|
||`.....`|`.......`|`.....`|`......`|`.....`|



What is the difference between the two codings? In `M2_lm` , a coefficient estimate is reported for all but level `23` of `hr` and level `Dec` of `mnth` . Importantly, in `M2_lm` , the (unreported) coefficient estimate for the last level of `mnth` is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels. Similarly, in `M2_lm` , the coefficient estimate for the last level of `hr` is the negative of the sum of the coefficient estimates for all of the other levels. This means that the coefficients of `hr` and `mnth` in `M2_lm` will always sum to zero, and can be interpreted as the difference from the mean level. For example, the coefficient for January of _−_ 46 _._ 087 indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average. 

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used. For example, we see that the predictions from the linear model are the same regardless of coding: 

```
In [69]:np.sum((M_lm.fittedvalues-M2_lm.fittedvalues)**2)
```

---

## Sub-Chapters (하위 목차)

### GLM Output (포아송 분석 결과)
* [문서로 이동하기](./4_7_7_1_poisson_regression/)

GLM 결과 안보드에서 계수 유의성을 입증하는 잔차 로그 수치와 P-value 들을 파싱해 점검합니다.

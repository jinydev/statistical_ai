---
layout: default
title: "index"
---

# Non-linear Relationships 

As discussed previously, the linear regression model (3.19) assumes a linear relationship between the response and predictors. But in some cases, the true relationship between the response and the predictors may be nonlinear. Here we present a very simple way to directly extend the linear model to accommodate non-linear relationships, using _polynomial regression_ . In polynomial later chapters, we will present more complex approaches for performing regression non-linear fits in more general settings. 

Consider Figure 3.8, in which the `mpg` (gas mileage in miles per gallon) versus `horsepower` is shown for a number of cars in the `Auto` data set. The orange line represents the linear regression fit. There is a pronounced relationship between `mpg` and `horsepower` , but it seems clear that this relationship is in fact non-linear: the data suggest a curved relationship. A simple approach for incorporating non-linear associations in a linear model is to include transformed versions of the predictors. For example, the points in Figure 3.8 seem to have a _quadratic_ shape, suggesting that a model of the quadratic form 

**==> picture [285 x 11] intentionally omitted <==**

may provide a better fit. Equation 3.36 involves predicting `mpg` using a non-linear function of `horsepower` . _But it is still a linear model!_ That is, (3.36) is simply a multiple linear regression model with $X_1$ = `horsepower` and $X_2$ = `horsepower`[2] . So we can use standard linear regression software to estimate \beta_0 _, β_ 1, and \beta_2 in order to produce a non-linear fit. The blue curve in Figure 3.8 shows the resulting quadratic fit to the data. The quadratic 

3.3 Other Considerations in the Regression Model 99 

**==> picture [304 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
Linear<br>Degree 2<br>Degree 5<br>50 100 150 200<br>Horsepower<br>50<br>40<br>30<br>Miles per gallon<br>20<br>10<br>**----- End of picture text -----**<br>


**FIGURE 3.8.** _The_ `Auto` _data set. For a number of cars,_ `mpg` _and_ `horsepower` _are shown. The linear regression fit is shown in orange. The linear regression fit for a model that includes_ `horsepower`[2] _is shown as a blue curve. The linear regression fit for a model that includes all polynomials of_ `horsepower` _up to fifth-degree is shown in green._ 

|_r a model that includes all polynomials of_ `horsepower` _up to ffth-deg_<br>_n in green._|_r a model that includes all polynomials of_ `horsepower` _up to ffth-deg_<br>_n in green._|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`horsepower`<br>`horsepower`2|56.9001<br>1.8004<br>31.6<br>_<_0_._0001<br>_−_0.4662<br>0.0311<br>_−_15.0<br>_<_0_._0001<br>0.0012<br>0.0001<br>10.1<br>_<_0_._0001|



**TABLE 3.10.** _For the_ `Auto` _data set, least squares coefficient estimates associated with the regression of_ `mpg` _onto_ `horsepower` _and_ `horsepower`[2] _._ 

fit appears to be substantially better than the fit obtained when just the linear term is included. The $R^2$ of the quadratic fit is 0 _._ 688, compared to 0 _._ 606 for the linear fit, and the $p$-value in Table 3.10 for the quadratic term is highly significant. 

If including `horsepower`[2] led to such a big improvement in the model, why not include `horsepower`[3] , `horsepower`[4] , or even `horsepower`[5] ? The green curve in Figure 3.8 displays the fit that results from including all polynomials up to fifth degree in the model (3.36). The resulting fit seems unnecessarily wiggly—that is, it is unclear that including the additional terms really has led to a better fit to the data. 

The approach that we have just described for extending the linear model to accommodate non-linear relationships is known as _polynomial regression_ , since we have included polynomial functions of the predictors in the regression model. We further explore this approach and other non-linear extensions of the linear model in Chapter 7. 

100 3. Linear Regression 

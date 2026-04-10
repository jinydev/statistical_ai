---
layout: default
title: "index"
---

# _4.3.3 Making Predictions_ 

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probability 

4. Classification 

142 

|4. Classifcation|4. Classifcation|
|---|---|
|||
||Coefcient<br>Std. error<br>_z_-statistic<br>_p_-value|
|`Intercept`<br>`balance`|_−_10.6513<br>0.3612<br>_−_29.5<br>_<_0.0001<br>0.0055<br>0.0002<br>24.9<br>_<_0.0001|



**TABLE 4.1.** _For the_ `Default` _data, estimated coefficients of the logistic regression model that predicts the probability of_ `default` _using_ `balance` _. A one-unit increase in_ `balance` _is associated with an increase in the log odds of_ `default` _by_ 0 _._ 0055 _units._ 

|_ase in_ `balance` _is_<br>5 _units._|_associated wi_|_th an increase_|_in the log od_|_ds of_ `defau`|
|---|---|---|---|---|
||Coefcient|Std. error|_z_-statistic|_p_-value|
|`Intercept`|_−_3.5041|0.0707|_−_49.55|_<_0.0001|
|`student[Yes]`|0.4049|0.1150|3.52|0.0004|



**TABLE 4.2.** _For the_ `Default` _data, estimated coefficients of the logistic regression model that predicts the probability of_ `default` _using student status. Student status is encoded as a dummy variable, with a value of_ 1 _for a student and a value of_ 0 _for a non-student, and represented by the variable_ `student[Yes]` _in the table._ 

for an individual with a `balance` of $1,000 is 

$$
\hat{p}(X) = 
rac{e^{-10.6513 + 0.0055 	imes 1000}}{1 + e^{-10.6513 + 0.0055 	imes 1000}} = 0.00576
$$

which is below 1 %. In contrast, the predicted probability of default for an individual with a balance of $2 _,_ 000 is much higher, and equals 0 _._ 586 or 58 _._ 6 %. 

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the `Default` data set contains the qualitative variable `student` . To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students. The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated _p_ -value is statistically significant. This indicates that students tend to have higher default probabilities than non-students: 

$$
egin{align*}
\hat{	ext{Pr}}(	ext{default} = 	ext{Yes} \mid 	ext{student} = 	ext{Yes}) &= 
rac{e^{-3.5041 + 0.4049 	imes 1}}{1 + e^{-3.5041 + 0.4049 	imes 1}} = 0.0431 \
\hat{	ext{Pr}}(	ext{default} = 	ext{Yes} \mid 	ext{student} = 	ext{No}) &= 
rac{e^{-3.5041 + 0.4049 	imes 0}}{1 + e^{-3.5041 + 0.4049 	imes 0}} = 0.0292
\end{align*}
$$

---
layout: default
title: "index"
---

# _5.3.2 Cross-Validation_ 

In theory, the cross-validation estimate can be computed for any generalized linear model. In practice, however, the simplest way to cross-validate in Python is to use `sklearn` , which has a different interface or API than `statsmodels` , the code we have been using to fit GLMs. 

This is a problem which often confronts data scientists: “I have a function to do task _A_ , and need to feed it into something that performs task _B_ , so that I can compute _B_ ( _A_ ( _D_ )), where _D_ is my data.” When _A_ and _B_ don’t naturally speak to each other, this requires the use of a _wrapper_ . In the `ISLP` wrapper 

218 5. Resampling Methods 

package, we provide a wrapper, `sklearn_sm()` , that enables us to easily use `sklearn_sm()` the cross-validation tools of `sklearn` with models fit by `statsmodels` . The class `sklearn_sm()` has as its first argument a model from `statsmodels` . It can take two additional optional arguments: `model_str` which can be used to specify a formula, and `model_args` which should be a dictionary of additional arguments used when fitting the model. For example, to fit a logistic regression model we have to specify a `family` argument. This is passed as `model_args={'family':sm.families.Binomial()}` . 

Here is our wrapper in action: 

```
In [9]:hp_model=sklearn_sm(sm.OLS,
MS(['horsepower']))
X,Y=Auto.drop(columns=['mpg']),Auto['mpg']
cv_results=cross_validate(hp_model,
X,
Y,
cv=Auto.shape[0])
cv_err=np.mean(cv_results['test_score'])
cv_err
```

---

## Sub-Chapters (하위 목차)

### 다중 분석 결과 지표 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_2_1_out14_23.8022_1.4218/)

각각의 쪼개진 폴드 조각별로 반환되는 로스 에러 값 배열들을 확인하고, 왜 편차가 존재하고 어떻게 평균내는 코드가 짜이는지 체감합니다.

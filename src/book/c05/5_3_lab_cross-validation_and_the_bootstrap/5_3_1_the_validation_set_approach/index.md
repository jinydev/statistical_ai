---
layout: default
title: "index"
---

# _5.3.1 The Validation Set Approach_ 

We explore the use of the validation set approach in order to estimate the test error rates that result from fitting various linear models on the `Auto` data set. 

We use the function `train_test_split()` to split the data into training `train_test_` and validation sets. As there are 392 observations, we split into two equal `split()` sets of size 196 using the argument `test_size=196` . It is generally a good idea to set a random seed when performing operations like this that contain an element of randomness, so that the results obtained can be reproduced precisely at a later time. We set the random seed of the splitter with the argument `random_state=0` . 

```
In [3]:Auto=load_data('Auto')
Auto_train,Auto_valid=train_test_split(Auto,
test_size=196,
random_state=0)
```

Now we can fit a linear regression using only the observations corresponding to the training set `Auto_train` . 

```
In [4]:hp_mm=MS(['horsepower'])
X_train=hp_mm.fit_transform(Auto_train)
y_train=Auto_train['mpg']
model=sm.OLS(y_train,X_train)
results=model.fit()
```

We now use the `predict()` method of `results` evaluated on the model matrix for this model created using the validation data set. We also calculate the validation MSE of our model. 

```
In [5]:X_valid=hp_mm.transform(Auto_valid)
y_valid=Auto_valid['mpg']
valid_pred=results.predict(X_valid)
np.mean((y_valid-valid_pred)**2)
```

```
Out[5]:23.6166
```

Hence our estimate for the validation MSE of the linear regression fit is 23 _._ 62. 

We can also estimate the validation error for higher-degree polynomial regressions. We first provide a function `evalMSE()` that takes a model string as well as a training and test set and returns the MSE on the test set. 

```
In [6]:defevalMSE(terms,
response,
train,
test):
mm=MS(terms)
X_train=mm.fit_transform(train)
y_train=train[response]
X_test=mm.transform(test)
y_test=test[response]
```

5.3 Lab: Cross-Validation and the Bootstrap 

217 

```
results=sm.OLS(y_train,X_train).fit()
test_pred=results.predict(X_test)
returnnp.mean((y_test-test_pred)**2)
```

Let’s use this function to estimate the validation MSE using linear, quadratic and cubic fits. We use the `enumerate()` function here, which gives `enumerate()` both the values and indices of objects as one iterates over a for loop. 

```
In [7]:MSE=np.zeros(3)
foridx,degreeinenumerate(range(1,4)):
MSE[idx]=evalMSE([poly('horsepower',degree)],
'mpg',
Auto_train ,
Auto_valid)
MSE
```

```
Out[7]:array([23.62,18.76,18.80])
```

These error rates are 23 _._ 62 _,_ 18 _._ 76, and 18 _._ 80, respectively. If we choose a different training/validation split instead, then we can expect somewhat different errors on the validation set. 

```
In [8]:Auto_train,Auto_valid=train_test_split(Auto,
test_size=196,
random_state=3)
MSE=np.zeros(3)
foridx,degreeinenumerate(range(1,4)):
MSE[idx]=evalMSE([poly('horsepower',degree)],
'mpg',
Auto_train ,
Auto_valid)
MSE
```

```
Out[8]:array([20.76,16.95,16.97])
```

Using this split of the observations into a training set and a validation set, we find that the validation set error rates for the models with linear, quadratic, and cubic terms are 20 _._ 76, 16 _._ 95, and 16 _._ 97, respectively. 

These results are consistent with our previous findings: a model that predicts `mpg` using a quadratic function of `horsepower` performs better than a model that involves only a linear function of `horsepower` , and there is no evidence of an improvement in using a cubic function of `horsepower` . 

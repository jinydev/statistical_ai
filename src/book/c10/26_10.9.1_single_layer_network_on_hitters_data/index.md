---
layout: default
title: "index"
---

# _10.9.1 Single Layer Network on Hitters Data_ 

We start by fitting the models in Section 10.6 on the `Hitters` data. 

```
In [10]:Hitters=load_data('Hitters').dropna()
n=Hitters.shape[0]
```

We will fit two linear models (least squares and lasso) and compare their performance to that of a neural network. For this comparison we will use mean absolute error on a validation dataset.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$

We set up the model matrix and the response. 

```
In [11]:model=MS(Hitters.columns.drop('Salary'),intercept=False)
X=model.fit_transform(Hitters).to_numpy()
Y=Hitters['Salary'].to_numpy()
```

The `to_numpy()` method above converts `pandas` data frames or series to `to_numpy() numpy` arrays. We do this because we will need to use `sklearn` to fit the lasso model, and it requires this conversion. We also use a linear regression method from `sklearn` , rather than the method in Chapter 3 from `statsmodels` , to facilitate the comparisons. 

We now split the data into test and training, fixing the random state used by `sklearn` to do the split. 

438 10. Deep Learning 

```
In [12]:(X_train,
X_test,
Y_train,
Y_test)=train_test_split(X,
Y,
test_size=1/3,
random_state=1)
```

Linear Models 

We fit the linear model and evaluate the test error directly. 

```
In [13]:hit_lm=LinearRegression().fit(X_train,Y_train)
Yhat_test=hit_lm.predict(X_test)
np.abs(Yhat_test-Y_test).mean()
```

```
Out[13]:259.7153
```

Next we fit the lasso using `sklearn` . We are using mean absolute error to select and evaluate a model, rather than mean squared error. The specialized solver we used in Section 6.5.2 uses only mean squared error. So here, with a bit more work, we create a cross-validation grid and perform the cross-validation directly. 

We encode a pipeline with two steps: we first normalize the features using a `StandardScaler()` transform, and then fit the lasso without further normalization. 

```
In [14]:scaler=StandardScaler(with_mean=True,with_std=True)
lasso=Lasso(warm_start=True,max_iter=30000)
standard_lasso=Pipeline(steps=[('scaler',scaler),
('lasso',lasso)])
```

We need to create a grid of values for _λ_ . As is common practice, we choose a grid of 100 values of _λ_ , uniform on the log scale from `lam_max` down to `0.01*lam_max` . Here `lam_max` is the smallest value of _λ_ with an allzero solution. This value equals the largest absolute inner-product between any predictor and the (centered) response.[24] 

```
In [15]:X_s=scaler.fit_transform(X_train)
n=X_s.shape[0]
lam_max=np.fabs(X_s.T.dot(Y_train-Y_train.mean())).max()/n
param_grid={'alpha':np.exp(np.linspace(0,np.log(0.01),100))
*lam_max}
```

Note that we had to transform the data first, since the scale of the variables impacts the choice of _λ_ . We now perform cross-validation using this sequence of _λ_ values. 

```
In [16]:cv=KFold(10,
shuffle=True,
random_state=1)
grid=GridSearchCV(lasso,
```

> 24The derivation of this result is beyond the scope of this book. 

10.9 Lab: Deep Learning 439 

```
param_grid ,
cv=cv,
scoring='neg_mean_absolute_error')
grid.fit(X_train,Y_train);
```

We extract the lasso model with best cross-validated mean absolute error, and evaluate its performance on `X_test` and `Y_test` , which were not used in cross-validation. 

```
In [17]:trained_lasso=grid.best_estimator_
Yhat_test=trained_lasso.predict(X_test)
np.fabs(Yhat_test-Y_test).mean()
```

```
Out[17]:257.2382
```

This is similar to the results we got for the linear model fit by least squares. However, these results can vary a lot for different train/test splits; we encourage the reader to try a different seed in code block 12 and rerun the subsequent code up to this point. 

Specifying a Network: Classes and Inheritance 

To fit the neural network, we first set up a model structure that describes the network. Doing so requires us to define new classes specific to the model we wish to fit. Typically this is done in `pytorch` by sub-classing a generic representation of a network, which is the approach we take here. Although this example is simple, we will go through the steps in some detail, since it will serve us well for the more complex examples to follow. 

```
In [18]:classHittersModel(nn.Module):
```

```
def__init__(self,input_size):
super(HittersModel ,self).__init__()
self.flatten=nn.Flatten()
self.sequential=nn.Sequential(
nn.Linear(input_size,50),
nn.ReLU(),
nn.Dropout(0.4),
nn.Linear(50,1))
defforward(self,x):
x=self.flatten(x)
returntorch.flatten(self.sequential(x))
```

The `class` statement identifies the code chunk as a declaration for a class `HittersModel` that inherits from the base class `nn.Module` . This base class is ubiquitous in `torch` and represents the mappings in the neural networks. 

Indented beneath the `class` statement are the methods of this class: in this case `__init__` and `forward` . The `__init__` method is called when an instance of the class is created as in the cell below. In the methods, `self` always refers to an instance of the class. In the `__init__` method, we have attached two objects to `self` as attributes: `flatten` and `sequential` . These are used in the `forward` method to describe the map that this module implements. 

440 10. Deep Learning 

There is one additional line in the `__init__` method, which is a call to `super()` . This function allows subclasses (i.e. `HittersModel` ) to access meth- `super()` ods of the class they inherit from. For example, the class `nn.Module` has its own `__init__` method, which is different from the `HittersModel.__init__()` method we’ve written above. Using `super()` allows us to call the method of the base class. For `torch` models, we will always be making this `super()` call as it is necessary for the model to be properly interpreted by `torch` . 

The object `nn.Module` has more methods than simply `__init__` and `forward` . These methods are directly accessible to `HittersModel` instances because of this inheritance. One such method we will see shortly is the `eval()` method, used to disable dropout for when we want to evaluate the model on test data. 

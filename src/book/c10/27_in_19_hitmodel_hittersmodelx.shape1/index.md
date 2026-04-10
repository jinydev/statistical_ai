---
layout: default
title: "index"
---

# **`In [19]:`** `hit_model = HittersModel(X.shape[1])` 

The object `self.sequential` is a composition of four maps. The first maps the 19 features of `Hitters` to 50 dimensions, introducing 50 _×_ 19 + 50 parameters for the weights and _intercept_ of the map (often called the _bias_ ). This layer is then mapped to a ReLU layer followed by a 40% dropout layer, and finally a linear map down to 1 dimension, again with a bias. The total number of trainable parameters is therefore 50 _×_ 19 + 50 + 50 + 1 = 1051. 

The package `torchinfo` provides a `summary()` function that neatly summarizes this information. We specify the size of the input and see the size of each tensor as it passes through layers of the network. 

```
summary(hit_model,
input_size=X_train.shape,
col_names=['input_size',
'output_size',
'num_params'])
```

```
In [20]:
```

|**`Out[20]:`**|`=====================================================================`|`=====================================================================`|`=====================================================================`|`=====================================================================`|`=====================================================================`|
|---|---|---|---|---|---|
||`Layer (type:depth-idx)`|`Input Shape`|`Output Shape`|`Param #`||
||`=====================================================================`|||||
||`HittersModel`|`[175, 19]`|`[175]`|`--`||
||`Flatten: 1-1`|`[175, 19]`|`[175, 19]`|`--`||
||`Sequential: 1-2`|`[175, 19]`|`[175, 1]`|`--`||
||`Linear: 2-1`|`[175, 19]`|`[175, 50]`|`1,000`||
||`ReLU: 2-2`|`[175, 50]`|`[175, 50]`|`--`||
||`Dropout: 2-3`|`[175, 50]`|`[175, 50]`|`--`||
||`Linear: 2-4`|`[175, 50]`|`[175, 1]`|`51`||
||`=====================================================================`|||||
||`Total params: 1,051`|||||
||`Trainable params: 1,051`|||||



We have truncated the end of the output slightly, here and in subsequent uses. 

We now need to transform our training data into a form accessible to `torch` . The basic datatype in `torch` is a `tensor` , which is very similar to an `ndarray` from early chapters. We also note here that `torch` typically works with 32-bit ( _single precision_ ) rather than 64-bit ( _double precision_ ) floating point numbers. We therefore convert our data to `np.float32` before forming the tensor. The _X_ and _Y_ tensors are then arranged into a `Dataset Dataset` 

10.9 Lab: Deep Learning 441 

recognized by `torch` using `TensorDataset()` . 

```
In [21]:X_train_t=torch.tensor(X_train.astype(np.float32))
Y_train_t=torch.tensor(Y_train.astype(np.float32))
hit_train=TensorDataset(X_train_t,Y_train_t)
```

```
Tensor
Dataset()
```

We do the same for the test data. 

```
In [22]:X_test_t=torch.tensor(X_test.astype(np.float32))
Y_test_t=torch.tensor(Y_test.astype(np.float32))
hit_test=TensorDataset(X_test_t,Y_test_t)
```

Finally, this dataset is passed to a `DataLoader()` which ultimately passes data into our network. While this may seem like a lot of overhead, this structure is helpful for more complex tasks where data may live on different machines, or where data must be passed to a GPU. We provide a helper function `SimpleDataModule()` in `ISLP` to make this task easier for standard `SimpleData` usage. One of its arguments is `num_workers` , which indicates how many `Module()` processes we will use for loading the data. For small data like `Hitters` this will have little effect, but it does provide an advantage for the `MNIST` and `CIFAR100` examples below. The `torch` package will inspect the process running and determine a maximum number of workers.[25] We’ve included a function `rec_num_workers()` to compute this so we know how many workers might be reasonable (here the max was 16). 

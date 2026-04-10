---
layout: default
title: "index"
---

# **`In [6]:`** `from torchvision.datasets import MNIST, CIFAR100` 

```
fromtorchvision.modelsimport(resnet50,
```

```
ResNet50_Weights)
fromtorchvision.transformsimport(Resize,
Normalize,
CenterCrop ,
ToTensor)
```

We have provided a few utilities in `ISLP` specifically for this lab. The `SimpleDataModule` and `SimpleModule` are simple versions of objects used in `pytorch_lightning` , the high-level module for fitting `torch` models. Although more advanced uses such as computing on graphical processing units (GPUs) and parallel data processing are possible in this module, we will not be focusing much on these in this lab. The `ErrorTracker` handles collections of targets and predictions over each mini-batch in the validation or test stage, allowing computation of the metric over the entire validation or test data set. 

10.9 Lab: Deep Learning 437 

```
In [7]:fromISLP.torchimport(SimpleDataModule ,
```

```
SimpleModule ,
ErrorTracker ,
rec_num_workers)
```

In addition we have included some helper functions to load the `IMDb` database, as well as a lookup that maps integers to particular keys in the database. We’ve included a slightly modified copy of the preprocessed `IMDb` data from `keras` , a separate package for fitting deep learning models. This `keras` saves us significant preprocessing and allows us to focus on specifying and fitting the models themselves. 

```
In [8]:fromISLP.torch.imdbimport(load_lookup ,
```

```
load_tensor ,
load_sparse ,
load_sequential)
```

Finally, we introduce some utility imports not directly related to `torch` . The `glob()` function from the `glob` module is used to find all files matching `glob()` wildcard characters, which we will use in our example applying the `ResNet50` model to some of our own images. The `json` module will be used to load a `json` JSON file for looking up classes to identify the labels of the pictures in the `ResNet50` example. 

```
In [9]:fromglobimportglob
importjson
```

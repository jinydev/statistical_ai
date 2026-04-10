---
layout: default
title: "index"
---

# 10.9 Lab: Deep Learning 

In this section we demonstrate how to fit the examples discussed in the text. We use the `Python torch` package, along with the `pytorch_lightning torch` package which provides utilities to simplify fitting and evaluating models. This code can be impressively fast with certain special processors, such as Apple’s new M1 chip. The package is well-structured, flexible, and will feel comfortable to `Python` users. A good companion is the site pytorch.org/tutorials. Much of our code is adapted from there, as well as the `pytorch_lightning` documentation.[23] 

```
pytorch_
lightning
```

We start with several standard imports that we have seen before. 

```
In [1]:importnumpyasnp,pandasaspd
frommatplotlib.pyplotimportsubplots
fromsklearn.linear_modelimport\
(LinearRegression ,
LogisticRegression ,
Lasso)
fromsklearn.preprocessingimportStandardScaler
fromsklearn.model_selectionimportKFold
fromsklearn.pipelineimportPipeline
fromISLPimportload_data
fromISLP.modelsimportModelSpecasMS
fromsklearn.model_selectionimport\
(train_test_split ,
GridSearchCV)
```

> 23The precise URLs at the time of writing are `https://pytorch.org/tutorials/ beginner/basics/intro.html` and `https://pytorch-lightning.readthedocs.io/en/ latest/` . 

436 10. Deep Learning 

Torch-Specific Imports 

There are a number of imports for `torch` . (These are not included with `ISLP` , so must be installed separately.) First we import the main library and essential tools used to specify sequentially-structured networks. 

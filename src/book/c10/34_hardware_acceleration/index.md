---
layout: default
title: "index"
---

# Hardware Acceleration 

As deep learning has become ubiquitous in machine learning, hardware manufacturers have produced special libraries that can often speed up the gradient-descent steps. 

For instance, Mac OS devices with the M1 chip may have the _Metal_ programming framework enabled, which can speed up the `torch` computations. We present an example of how to use this acceleration. 

The main changes are to the `Trainer()` call as well as to the metrics that will be evaluated on the data. These metrics must be told where the data will be located at evaluation time. This is accomplished with a call to the `to()` method of the metrics. 

```
In [60]:
```

```
try:
forname,metricincifar_module.metrics.items():
cifar_module.metrics[name]=metric.to('mps')
cifar_trainer_mps=Trainer(accelerator='mps',
deterministic=True,
max_epochs=30)
cifar_trainer_mps.fit(cifar_module ,
datamodule=cifar_dm)
cifar_trainer_mps.test(cifar_module ,
datamodule=cifar_dm)
except:
pass
```

This yields approximately two- or three-fold acceleration for each epoch. We have protected this code block using `try:` and `except:` clauses; if it works, we get the speedup, if it fails, nothing happens. 

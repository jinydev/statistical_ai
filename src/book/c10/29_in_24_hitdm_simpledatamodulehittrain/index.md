---
layout: default
title: "index"
---

# **`In [24]:`** `hit_dm = SimpleDataModule(hit_train,` 

```
hit_test,
batch_size=32,
num_workers=min(4,max_num_workers),
validation=hit_test)
```

Next we must provide a `pytorch_lightning` module that controls the steps performed during the training process. We provide methods for our `SimpleModule()` that simply record the value of the loss function and any additional metrics at the end of each epoch. These operations are controlled by the methods `SimpleModule.[training/test/validation]_step()` , though we will not be modifying these in our examples. 

> 25This depends on the computing hardware and the number of cores available. 

442 10. Deep Learning 

```
In [25]:hit_module=SimpleModule.regression(hit_model,
```

```
metrics={'mae':MeanAbsoluteError()})
```

By using the `SimpleModule.regression()` method, we indicate that we `SimpleModule.` will use squared-error loss as in (10.23). We have also asked for mean ab- `regression()` solute error to be tracked as well in the metrics that are logged. 

We log our results via `CSVLogger()` , which in this case stores the results in a CSV file within a directory `logs/hitters` . After the fitting is complete, this allows us to load the results as a `pd.DataFrame()` and visualize them below. There are several ways to log the results within `pytorch_lightning` , though we will not cover those here in detail. 

```
In [26]:hit_logger=CSVLogger('logs',name='hitters')
```

Finally we are ready to train our model and log the results. We use the `Trainer()` object from `pytorch_lightning` to do this work. The argument `datamodule=hit_dm` tells the trainer how training/validation/test logs are produced, while the first argument `hit_module` specifies the network architecture as well as the training/validation/test steps. The `callbacks` argument allows for several tasks to be carried out at various points while training a model. Here our `ErrorTracker()` callback will enable us to compute validation error while training and, finally, the test error. We now fit the model for 50 epochs. 

```
In [27]:hit_trainer=Trainer(deterministic=True,
```

```
max_epochs=50,
log_every_n_steps=5,
logger=hit_logger,
callbacks=[ErrorTracker()])
hit_trainer.fit(hit_module,datamodule=hit_dm)
```

At each step of SGD, the algorithm randomly selects 32 training observations for the computation of the gradient. Recall from Section 10.7 that an epoch amounts to the number of SGD steps required to process _n_ observations. Since the training set has _n_ = 175, and we specified a `batch_size` of 32 in the construction of `hit_dm` , an epoch is 175 _/_ 32 = 5 _._ 5 SGD steps. 

After having fit the model, we can evaluate performance on our test data using the `test()` method of our trainer. 

```
In [28]:hit_trainer.test(hit_module,datamodule=hit_dm)
```

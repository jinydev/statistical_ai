---
layout: default
title: "index"
---

# **`In [23]:`** `max_num_workers = rec_num_workers()` 

The general training setup in `pytorch_lightning` involves training, validation and test data. These are each represented by different data loaders. During each epoch, we run a training step to learn the model and a validation step to track the error. The test data is typically used at the end of training to evaluate the model. 

In this case, as we had split only into test and training, we’ll use the test data as validation data with the argument `validation=hit_test` . The `validation` argument can be a float between 0 and 1, an integer, or a `Dataset` . If a float (respectively, integer), it is interpreted as a percentage (respectively number) of the _training_ observations to be used for validation. If it is a `Dataset` , it is passed directly to a data loader. 

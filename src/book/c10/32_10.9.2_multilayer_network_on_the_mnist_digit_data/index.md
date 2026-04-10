---
layout: default
title: "index"
---

# _10.9.2 Multilayer Network on the MNIST Digit Data_ 

The `torchvision` package comes with a number of example datasets, including the `MNIST` digit data. Our first step is to retrieve the training and test data sets; the `MNIST()` function within `torchvision.datasets` is provided for `MNIST()` this purpose. The data will be downloaded the first time this function is executed, and stored in the directory `data/MNIST` . 

```
In [33]:(mnist_train ,
mnist_test)=[MNIST(root='data',
train=train,
download=True,
transform=ToTensor())
fortrainin[True,False]]
mnist_train
```

```
Out[33]:DatasetMNIST
```

```
Numberofdatapoints:60000
Rootlocation:data
Split:Train
StandardTransform
Transform:ToTensor()
```

There are 60,000 images in the training data and 10,000 in the test data. The images are 28 _×_ 28, and stored as a matrix of pixels. We need to transform each one into a vector. 

Neural networks are somewhat sensitive to the scale of the inputs, much as ridge and lasso regularization are affected by scaling. Here the inputs are eight-bit grayscale values between 0 and 255, so we rescale to the unit interval.[26] This transformation, along with some reordering of the axes, is performed by the `ToTensor()` transform from the `torchvision.transforms` package. 

As in our `Hitters` example, we form a data module from the training and test datasets, setting aside 20% of the training images for validation. 

```
In [34]:mnist_dm=SimpleDataModule(mnist_train ,
mnist_test ,
validation=0.2,
num_workers=max_num_workers ,
batch_size=256)
```

> 26Note: eight bits means 28, which equals 256. Since the convention is to start at 0, the possible values range from 0 to 255. 

10.9 Lab: Deep Learning 445 

Let’s take a look at the data that will get fed into our network. We loop through the first few chunks of the test dataset, breaking after 2 batches: 

```
In [35]:foridx,(X_,Y_)inenumerate(mnist_dm.train_dataloader()):
print('X:',X_.shape)
print('Y:',Y_.shape)
ifidx>=1:
break
X:torch.Size([256,1,28,28])
Y:torch.Size([256])
X:torch.Size([256,1,28,28])
Y:torch.Size([256])
```

We see that the _X_ for each batch consists of 256 images of size `1x28x28` . Here the `1` indicates a single channel (greyscale). For RGB images such as `CIFAR100` below, we will see that the `1` in the size will be replaced by `3` for the three RGB channels. 

Now we are ready to specify our neural network. 

```
In [36]:classMNISTModel(nn.Module):
```

```
def__init__(self):
super(MNISTModel,self).__init__()
self.layer1=nn.Sequential(
nn.Flatten(),
nn.Linear(28*28,256),
nn.ReLU(),
nn.Dropout(0.4))
self.layer2=nn.Sequential(
nn.Linear(256,128),
nn.ReLU(),
nn.Dropout(0.3))
self._forward=nn.Sequential(
self.layer1,
self.layer2,
nn.Linear(128,10))
defforward(self,x):
returnself._forward(x)
```

We see that in the first layer, each `1x28x28` image is flattened, then mapped to 256 dimensions where we apply a ReLU activation with 40% dropout. A second layer maps the first layer’s output down to 128 dimensions, applying a ReLU activation with 30% dropout. Finally, the 128 dimensions are mapped down to 10, the number of classes in the `MNIST` data. 

```
In [37]:mnist_model=MNISTModel()
```

We can check that the model produces output of expected size based on our existing batch `X_` above. 

```
In [38]:mnist_model(X_).size()
```

```
Out[38]:torch.Size([256,10])
```

Let’s take a look at the summary of the model. Instead of an `input_size` we can pass a tensor of correct shape. In this case, we pass through the final batched `X_` from above. 

446 10. Deep Learning 

```
In [39]:summary(mnist_model ,
```

```
input_data=X_,
col_names=['input_size',
'output_size',
'num_params'])
```

```
Out[39]:=====================================================================
Layer(type:depth-idx)InputShapeOutputShapeParam#
=====================================================================
MNISTModel[256,1,28,28][256,10]--
Sequential:1-1[256,1,28,28][256,10]--
Sequential:2-1[256,1,28,28][256,256]--
Flatten:3-1[256,1,28,28][256,784]--
Linear:3-2[256,784][256,256]200,960
ReLU:3-3[256,256][256,256]--
Dropout:3-4[256,256][256,256]--
Sequential:2-2[256,256][256,128]--
Linear:3-5[256,256][256,128]32,896
ReLU:3-6[256,128][256,128]--
Dropout:3-7[256,128][256,128]--
Linear:2-3[256,128][256,10]1,290
=====================================================================
Totalparams:235,146
Trainableparams:235,146
```

Having set up both the model and the data module, fitting this model is now almost identical to the `Hitters` example. In contrast to our regression model, here we will use the `SimpleModule.classification()` method which `SimpleModule.` uses the cross-entropy loss function instead of mean squared error. `classifi-` 

```
classifi-
cation()
```

```
In [40]:mnist_module=SimpleModule.classification(mnist_model)
mnist_logger=CSVLogger('logs',name='MNIST')
```

Now we are ready to go. The final step is to supply training data, and fit the model. 

```
In [41]:mnist_trainer=Trainer(deterministic=True,
max_epochs=30,
logger=mnist_logger ,
callbacks=[ErrorTracker()])
mnist_trainer.fit(mnist_module ,
datamodule=mnist_dm)
```

We have suppressed the output here, which is a progress report on the fitting of the model, grouped by epoch. This is very useful, since on large datasets fitting can take time. Fitting this model took 245 seconds on a MacBook Pro with an Apple M1 Pro chip with 10 cores and 16 GB of RAM. Here we specified a validation split of 20%, so training is actually performed on 80% of the 60,000 observations in the training set. This is an alternative to actually supplying validation data, like we did for the `Hitters` data. SGD uses batches of 256 observations in computing the gradient, and doing the arithmetic, we see that an epoch corresponds to 188 gradient steps. 

`SimpleModule.classification()` includes an accuracy metric by default. Other classification metrics can be added from `torchmetrics` . We will use our `summary_plot()` function to display accuracy across epochs. 

10.9 Lab: Deep Learning 447 

```
In [42]:mnist_results=pd.read_csv(mnist_logger.experiment.
metrics_file_path)
fig,ax=subplots(1,1,figsize=(6,6))
summary_plot(mnist_results ,
ax,
col='accuracy',
ylabel='Accuracy')
ax.set_ylim([0.5,1])
ax.set_ylabel('Accuracy')
ax.set_xticks(np.linspace(0,30,7).astype(int));
```

Once again we evaluate the accuracy using the `test()` method of our trainer. This model achieves 97% accuracy on the test data. 

```
In [43]:mnist_trainer.test(mnist_module ,
datamodule=mnist_dm)
```

```
Out[43]:[{'test_loss':0.1471,'test_accuracy':0.9681}]
```

Table 10.1 also reports the error rates resulting from LDA (Chapter 4) and multiclass logistic regression. For LDA we refer the reader to Section 4.7.3. Although we could use the `sklearn` function `LogisticRegression()` to fit multiclass logistic regression, we are set up here to fit such a model with `torch` . We just have an input layer and an output layer, and omit the hidden layers! 

```
In [44]:classMNIST_MLR(nn.Module):
def__init__(self):
super(MNIST_MLR,self).__init__()
self.linear=nn.Sequential(nn.Flatten(),
nn.Linear(784,10))
defforward(self,x):
returnself.linear(x)
mlr_model=MNIST_MLR()
mlr_module=SimpleModule.classification(mlr_model)
mlr_logger=CSVLogger('logs',name='MNIST_MLR')
In [45]:mlr_trainer=Trainer(deterministic=True,
max_epochs=30,
callbacks=[ErrorTracker()])
mlr_trainer.fit(mlr_module,datamodule=mnist_dm)
```

We fit the model just as before and compute the test results. 

```
In [46]:mlr_trainer.test(mlr_module,
datamodule=mnist_dm)
```

```
Out[46]:[{'test_loss':0.3187,'test_accuracy':0.9241}]
```

The accuracy is above 90% even for this pretty simple model. 

As in the `Hitters` example, we delete some of the objects we created above. 

```
In [47]:del(mnist_test,
mnist_train ,
```

448 10. Deep Learning 

```
mnist_model ,
mnist_dm,
mnist_trainer ,
mnist_module ,
mnist_results ,
mlr_model,
mlr_module,
mlr_trainer)
```

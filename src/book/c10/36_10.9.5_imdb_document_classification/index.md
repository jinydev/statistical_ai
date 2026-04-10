---
layout: default
title: "index"
---

# _10.9.5 IMDB Document Classification_ 

We now implement models for sentiment classification (Section 10.4) on the `IMDB` dataset. As mentioned above code block 8, we are using a preprocessed version of the `IMDB` dataset found in the `keras` package. As `keras` uses 

10.9 Lab: Deep Learning 455 

`tensorflow` , a different tensor and deep learning library, we have converted the data to be suitable for `torch` . The code used to convert from `keras` is available in the module `ISLP.torch._make_imdb` . It requires some of the `keras` packages to run. These data use a dictionary of size 10,000. 

We have stored three different representations of the review data for this lab: 

- `load_tensor()` , a sparse tensor version usable by `torch` ; 

- `load_sparse()` , a sparse matrix version usable by `sklearn` , since we will compare with a lasso fit; 

- `load_sequential()` , a padded version of the original sequence representation, limited to the last 500 words of each review. 

```
In [69]:(imdb_seq_train ,
```

```
imdb_seq_test)=load_sequential(root='data/IMDB')
padded_sample=np.asarray(imdb_seq_train.tensors[0][0])
sample_review=padded_sample[padded_sample>0][:12]
sample_review[:12]
```

```
Out[69]:array([1,14,22,16,43,530,973,1622,1385,
65,458,4468],dtype=int32)
```

The datasets `imdb_seq_train` and `imdb_seq_test` are both instances of the class `TensorDataset` . The tensors used to construct them can be found in the `tensors` attribute, with the first tensor the features `X` and the second the outcome `Y` . We have taken the first row of features and stored it as `padded_sample` . In the preprocessing used to form these data, sequences were padded with 0s in the beginning if they were not long enough, hence we remove this padding by restricting to entries where `padded_sample > 0` . We then provide the first 12 words of the sample review. 

We can find these words in the `lookup` dictionary from the `ISLP.torch.imdb` module. 

```
In [70]:lookup=load_lookup(root='data/IMDB')
''.join(lookup[i]foriinsample_review)
```

```
Out[70]:"<START>thisfilmwasjustbrilliantcastinglocationscenery
storydirectioneveryone's"
```

For our first model, we have created a binary feature for each of the 10,000 possible words in the dataset, with an entry of one in the _i, j_ entry if word _j_ appears in review _i_ . As most reviews are quite short, such a feature matrix has over 98% zeros. These data are accessed using `load_tensor()` from the `ISLP` library. 

```
In [71]:max_num_workers=10
(imdb_train ,
imdb_test)=load_tensor(root='data/IMDB')
imdb_dm=SimpleDataModule(imdb_train,
imdb_test,
validation=2000,
num_workers=min(6,max_num_workers),
batch_size=512)
```

456 10. Deep Learning 

We’ll use a two-layer model for our first model. 

```
In [72]:
```

```
classIMDBModel(nn.Module):
def__init__(self,input_size):
super(IMDBModel,self).__init__()
self.dense1=nn.Linear(input_size,16)
self.activation=nn.ReLU()
self.dense2=nn.Linear(16,16)
self.output=nn.Linear(16,1)
defforward(self,x):
val=x
for_mapin[self.dense1,
self.activation,
self.dense2,
self.activation,
self.output]:
val=_map(val)
returntorch.flatten(val)
```

We now instantiate our model and look at a summary (not shown). 

```
In [73]:imdb_model=IMDBModel(imdb_test.tensors[0].size()[1])
summary(imdb_model,
input_size=imdb_test.tensors[0].size(),
col_names=['input_size',
'output_size',
'num_params'])
```

We’ll again use a smaller learning rate for these data, hence we pass an `optimizer` to the `SimpleModule` . Since the reviews are classified into positive or negative sentiment, we use `SimpleModule.binary_classification()` .[28] 

```
In [74]:imdb_optimizer=RMSprop(imdb_model.parameters(),lr=0.001)
imdb_module=SimpleModule.binary_classification(
imdb_model ,
optimizer=imdb_optimizer)
```

Having loaded the datasets into a data module and created a `SimpleModule` , the remaining steps are familiar. 

```
In [75]:imdb_logger=CSVLogger('logs',name='IMDB')
imdb_trainer=Trainer(deterministic=True,
max_epochs=30,
logger=imdb_logger ,
callbacks=[ErrorTracker()])
imdb_trainer.fit(imdb_module ,
datamodule=imdb_dm)
```

Evaluating the test error yields roughly 86% accuracy. 

```
In [76]:test_results=imdb_trainer.test(imdb_module ,datamodule=imdb_dm)
test_results
```

> 28Our use of `binary_classification()` instead of `classification()` is due to some subtlety in how `torchmetrics.Accuracy()` works, as well as the data type of the targets. 

10.9 Lab: Deep Learning 

457 

```
Out[76]:[{'test_loss':1.0863,'test_accuracy':0.8550}]
```

Comparison to Lasso 

We now fit a lasso logistic regression model using `LogisticRegression()` from `sklearn` . Since `sklearn` does not recognize the sparse tensors of `torch` , we use a sparse matrix that is recognized by `sklearn.` 

```
In [77]:((X_train,Y_train),
(X_valid,Y_valid),
(X_test,Y_test))=load_sparse(validation=2000,
random_state=0,
root='data/IMDB')
```

Similar to what we did in Section 10.9.1, we construct a series of 50 values for the lasso reguralization parameter _λ_ . 

```
In [78]:lam_max=np.abs(X_train.T*(Y_train-Y_train.mean())).max()
lam_val=lam_max*np.exp(np.linspace(np.log(1),
np.log(1e-4),50))
```

With `LogisticRegression()` the regularization parameter _C_ is specified as the inverse of _λ_ . There are several solvers for logistic regression; here we use `liblinear` which works well with the sparse input format. 

```
In [79]:logit=LogisticRegression(penalty='l1',
C=1/lam_max,
solver='liblinear',
warm_start=True,
fit_intercept=True)
```

The path of 50 values takes approximately 40 seconds to run. 

```
In [80]:coefs=[]
intercepts=[]
forlinlam_val:
logit.C=1/l
logit.fit(X_train,Y_train)
coefs.append(logit.coef_.copy())
intercepts.append(logit.intercept_)
```

The coefficient and intercepts have an extraneous dimension which can be removed by the `np.squeeze()` function. 

```
In [81]:coefs=np.squeeze(coefs)
intercepts=np.squeeze(intercepts)
```

We’ll now make a plot to compare our neural network results with the lasso. 

```
In [82]:%%capture
fig,axes=subplots(1,2,figsize=(16,8),sharey=True)
for((X_,Y_),
data_,
color)inzip([(X_train,Y_train),
(X_valid,Y_valid),
(X_test,Y_test)],
```

458 10. Deep Learning 

```
['Training','Validation','Test'],
['black','red','blue']):
linpred_=X_*coefs.T+intercepts[None,:]
label_=np.array(linpred_>0)
accuracy_=np.array([np.mean(Y_==l)forlinlabel_.T])
axes[0].plot(-np.log(lam_val/X_train.shape[0]),
accuracy_,
'.--',
color=color,
markersize=13,
linewidth=2,
label=data_)
axes[0].legend()
axes[0].set_xlabel(r'$-\log(\lambda)$',fontsize=20)
axes[0].set_ylabel('Accuracy',fontsize=20)
```

Notice the use of `%%capture` , which suppresses the displaying of the partially `%%capture` completed figure. This is useful when making a complex figure, since the steps can be spread across two or more cells. We now add a plot of the lasso accuracy, and display the composed figure by simply entering its name at the end of the cell. 

```
In [83]:imdb_results=pd.read_csv(imdb_logger.experiment.metrics_file_path)
summary_plot(imdb_results ,
axes[1],
col='accuracy',
ylabel='Accuracy')
axes[1].set_xticks(np.linspace(0,30,7).astype(int))
axes[1].set_ylabel('Accuracy',fontsize=20)
axes[1].set_xlabel('Epoch',fontsize=20)
axes[1].set_ylim([0.5,1]);
axes[1].axhline(test_results[0]['test_accuracy'],
color='blue',
'--'
linestyle=,
linewidth=3)
fig
```

From the graphs we see that the accuracy of the lasso logistic regression peaks at about 0 _._ 88, as it does for the neural network. Once again, we end with a cleanup. 

```
In [84]:del(imdb_model,
```

```
imdb_trainer ,
imdb_logger ,
imdb_dm,
imdb_train,
imdb_test)
```

---
layout: default
title: "index"
---

# **`Out[28]:`** `[{'test_loss': 104098.5469, 'test_mae': 229.5012}]` 

The results of the fit have been logged into a CSV file. We can find the results specific to this run in the `experiment.metrics_file_path` attribute of our logger. Note that each time the model is fit, the logger will output results into a new subdirectory of our directory `logs/hitters` . 

We now create a plot of the MAE (mean absolute error) as a function of the number of epochs. First we retrieve the logged summaries. 

```
hit_results=pd.read_csv(hit_logger.experiment.metrics_file_path)
```

Since we will produce similar plots in later examples, we write a simple generic function to produce this plot. 

10.9 Lab: Deep Learning 443 

```
In [29]:defsummary_plot(results,
ax,
col='loss',
valid_legend='Validation',
training_legend='Training',
ylabel='Loss',
fontsize=20):
for(column,
color,
label)inzip([f'train_{col}_epoch',
f'valid_{col}'],
['black',
'red'],
[training_legend ,
valid_legend]):
results.plot(x='epoch',
y=column,
label=label,
marker='o',
color=color,
ax=ax)
ax.set_xlabel('Epoch')
ax.set_ylabel(ylabel)
returnax
```

We now set up our axes, and use our function to produce the MAE plot. 

```
In [30]:fig,ax=subplots(1,1,figsize=(6,6))
ax=summary_plot(hit_results ,
ax,
col='mae',
ylabel='MAE',
valid_legend='Validation(=Test)')
ax.set_ylim([0,400])
ax.set_xticks(np.linspace(0,50,11).astype(int));
```

We can predict directly from the final model, and evaluate its performance on the test data. Before fitting, we call the `eval()` method of `hit_model` . This tells `torch` to effectively consider this model to be fitted, so that we can use it to predict on new data. For our model here, the biggest change is that the dropout layers will be turned off, i.e. no weights will be randomly dropped in predicting on new data. 

```
In [31]:hit_model.eval()
preds=hit_module(X_test_t)
torch.abs(Y_test_t-preds).mean()
```

```
Out[31]:tensor(229.5012,grad_fn=<MeanBackward0 >)
```

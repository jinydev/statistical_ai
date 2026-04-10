---
layout: default
title: "index"
---

# _10.7.4 Network Tuning_ 

The network in Figure 10.4 is considered to be relatively straightforward; it nevertheless requires a number of choices that all have an effect on the performance: 

- _The number of hidden layers, and the number of units per layer._ Modern thinking is that the number of units per hidden layer can be large, and overfitting can be controlled via the various forms of regularization. 

- _Regularization tuning parameters._ These include the dropout rate _φ_ and the strength _λ_ of lasso and ridge regularization, and are typically set separately at each layer. 

- _Details of stochastic gradient descent._ These include the batch size, the number of epochs, and if used, details of data augmentation (Section 10.3.4.) 

Choices such as these can make a difference. In preparing this `MNIST` example, we achieved a respectable 1 _._ 8% misclassification error after some trial and error. Finer tuning and training of a similar network can get under 1% error on these data, but the tinkering process can be tedious, and can result in overfitting if done carelessly. 

432 10. Deep Learning 

![Figure 10.20](./img/10_20.png)

**FIGURE 10.20.** _Double descent phenomenon, illustrated using error plots for a one-dimensional natural spline example. The horizontal axis refers to the number of spline basis functions on the log scale. The training error hits zero when the degrees of freedom coincides with the sample size n_ = 20 _, the “interpolation threshold”, and remains zero thereafter. The test error increases dramatically at this threshold, but then descends again to a reasonable value before finally increasing again._ 

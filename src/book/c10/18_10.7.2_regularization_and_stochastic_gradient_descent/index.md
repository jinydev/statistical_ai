---
layout: default
title: "index"
---

# _10.7.2 Regularization and Stochastic Gradient Descent_ 

Gradient descent usually takes many steps to reach a local minimum. In practice, there are a number of approaches for accelerating the process. Also, when _n_ is large, instead of summing (10.29)–(10.30) over all _n_ observations, we can sample a small fraction or _minibatch_ of them each time minibatch we compute a gradient step. This process is known as _stochastic gradient descent_ (SGD) and is the state of the art for learning deep neural networks. stochastic Fortunately, there is very good software for setting up deep learning modgradient els, and for fitting them to data, so most of the technicalities are hidden descent from the user. 

We now turn to the multilayer network (Figure 10.4) used in the digit recognition problem. The network has over 235,000 weights, which is around four times the number of training examples. Regularization is essential here 

430 10. Deep Learning 

![Figure 10.18](./img/10_18.png)

**FIGURE 10.18.** _Evolution of training and validation errors for the_ `MNIST` _neural network depicted in Figure 10.4, as a function of training epochs. The objective refers to the log-likelihood (10.14)._ 

to avoid overfitting. The first row in Table 10.1 uses ridge regularization on the weights. This is achieved by augmenting the objective function (10.14) with a penalty term:

$$
R(\theta) + \lambda \sum_{k=1}^K \sum_{j=0}^p w_{kj}^2 + \lambda \sum_{k=1}^K \beta_k^2 \quad (10.30)
$$

The parameter _λ_ is often preset at a small value, or else it is found using the validation-set approach of Section 5.3.1. We can also use different values of _λ_ for the groups of weights from different layers; in this case **W** 1 and **W** 2 were penalized, while the relatively few weights **B** of the output layer were not penalized at all. Lasso regularization is also popular as an additional form of regularization, or as an alternative to ridge. 

Figure 10.18 shows some metrics that evolve during the training of the network on the `MNIST` data. It turns out that SGD naturally enforces its own form of approximately quadratic regularization.[21] Here the minibatch size was 128 observations per gradient update. The term _epochs_ labeling the epochs horizontal axis in Figure 10.18 counts the number of times an equivalent of the full training set has been processed. For this network, 20% of the 60,000 training observations were used as a validation set in order to determine when training should stop. So in fact 48,000 observations were used for training, and hence there are 48 _,_ 000 _/_ 128 _≈_ 375 minibatch gradient updates per epoch. We see that the value of the validation objective actually starts to increase by 30 epochs, so _early stopping_ can also be used as an additional early form of regularization. 

stopping 

> 21This and other properties of SGD for deep learning are the subject of much research in the machine learning literature at the time of writing. 

10.7 Fitting a Neural Network 431 

**FIGURE 10.19.** _Dropout Learning. Left: a fully connected network. Right: network with dropout in the input and hidden layer. The nodes in grey are selected at random, and ignored in an instance of training._ 

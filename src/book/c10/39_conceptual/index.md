---
layout: default
title: "index"
---

# _Conceptual_ 

1. Consider a neural network with two hidden layers: _p_ = 4 input units, 2 units in the first hidden layer, 3 units in the second hidden layer, and a single output. 

   - (a) Draw a picture of the network, similar to Figures 10.1 or 10.4. 

   - (b) Write out an expression for _f_ ( _X_ ), assuming ReLU activation functions. Be as explicit as you can! 

   - (c) Now plug in some values for the coefficients and write out the value of _f_ ( _X_ ). 

   - (d) How many parameters are there? 

2. Consider the _softmax_ function in (10.13) (see also (4.13) on page 145) for modeling multinomial probabilities. 

   - (a) In (10.13), show that if we add a constant _c_ to each of the _zℓ_ , then the probability is unchanged. 

   - (b) In (4.13), show that if we add constants _cj, j_ = 0 _,_ 1 _, . . . , p_ , to each of the corresponding coefficients for each of the classes, then the predictions at any new point _x_ are unchanged. 

This shows that the softmax function is _over-parametrized_ . However, overregularization and SGD typically constrain the solutions so that this parametrized is not a problem. 

3. Show that the negative multinomial log-likelihood (10.14) is equivalent to the negative log of the likelihood expression (4.5) when there are _M_ = 2 classes. 

4. Consider a CNN that takes in 32 _×_ 32 grayscale images and has a single convolution layer with three 5 _×_ 5 convolution filters (without boundary padding). 

   - (a) Draw a sketch of the input and first hidden layer similar to Figure 10.8. 

466 10. Deep Learning 

   - (b) How many parameters are in this model? 

   - (c) Explain how this model can be thought of as an ordinary feedforward neural network with the individual pixels as inputs, and with constraints on the weights in the hidden units. What are the constraints? 

   - (d) If there were no constraints, then how many weights would there be in the ordinary feed-forward neural network in (c)? 

5. In Table 10.2 on page 426, we see that the ordering of the three methods with respect to mean absolute error is different from the ordering with respect to test set _R_[2] . How can this be? 

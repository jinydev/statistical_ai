---
layout: default
title: "index"
---

# 10.7 Fitting a Neural Network 

Fitting neural networks is somewhat complex, and we give a brief overview here. The ideas generalize to much more complex networks. Readers who find this material challenging can safely skip it. Fortunately, as we see in the lab at the end of this chapter, good software is available to fit neural network models in a relatively automated way, without worrying about the technical details of the model-fitting procedure. 

We start with the simple network depicted in Figure 10.1 in Section 10.1. In model (10.1) the parameters are _β_ = ( _β_ 0 _, β_ 1 _, . . . , βK_ ), as well as each of the _wk_ = ( _wk_ 0 _, wk_ 1 _, . . . , wkp_ ) _, k_ = 1 _, . . . , K._ Given observations ( _xi, yi_ ) _, i_ = 1 _, . . . , n,_ we could fit the model by solving a nonlinear least squares problem

$$
\min_\theta \sum_{i=1}^n (y_i - f_\theta(x_i))^2 \quad (10.23)
$$

where

$$
f_\theta(x) = \beta_0 + \sum_{k=1}^K \beta_k g \left( w_{k0} + \sum_{j=1}^p w_{kj} x_j \right)
$$

The objective in (10.23) looks simple enough, but because of the nested arrangement of the parameters and the symmetry of the hidden units, it is not straightforward to minimize. The problem is nonconvex in the parameters, and hence there are multiple solutions. As an example, Figure 10.17 shows a simple nonconvex function of a single variable _θ_ ; there are two solutions: one is a _local minimum_ and the other is a _global minimum_ . Fur- local thermore, (10.1) is the very simplest of neural networks; in this chapter we have presented much more complex ones where these problems are compounded. To overcome some of these issues and to protect from overfitting, two general strategies are employed when fitting neural networks. 

minimum global minimum 

- _Slow Learning:_ the model is fit in a somewhat slow iterative fashion, using _gradient descent_ . The fitting process is then stopped when gradient 

- overfitting is detected. descent 

descent 

- _Regularization:_ penalties are imposed on the parameters, usually lasso or ridge as discussed in Section 6.2. 

Suppose we represent all the parameters in one long vector _θ_ . Then we can rewrite the objective in (10.23) as

$$
R(\theta) = \frac{1}{2} \sum_{i=1}^n (y_i - f_\theta(x_i))^2
$$

428 10. Deep Learning 

![Figure 10.17](./img/10_17.png)

**FIGURE 10.17.** _Illustration of gradient descent for one-dimensional θ. The objective function R_ ( _θ_ ) _is not convex, and has two minima, one at θ_ = _−_ 0 _._ 46 _(local), the other at θ_ = 1 _._ 02 _(global). Starting at some value θ_[0] _(typically randomly chosen), each step in θ moves downhill — against the gradient — until it cannot go down any further. Here gradient descent reached the global minimum in_ 7 _steps._ 

where we make explicit the dependence of _f_ on the parameters. The idea of gradient descent is very simple. 

1. Start with a guess _θ_[0] for all the parameters in _θ_ , and set _t_ = 0. 

2. Iterate until the objective (10.25) fails to decrease: 

   - (a) Find a vector _δ_ that reflects a small change in _θ_ , such that _θ[t]_[+1] = _θ[t]_ + _δ reduces_ the objective; i.e. such that _R_ ( _θ[t]_[+1] ) _< R_ ( _θ[t]_ ). 

   - (b) Set _t ← t_ + 1. 

One can visualize (Figure 10.17) standing in a mountainous terrain, and the goal is to get to the bottom through a series of steps. As long as each step goes downhill, we must eventually get to the bottom. In this case we were lucky, because with our starting guess _θ_[0] we end up at the global minimum. In general we can hope to end up at a (good) local minimum. 

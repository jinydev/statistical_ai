---
layout: default
title: "index"
---

# _10.7.1 Backpropagation_ 

How do we find the directions to move _θ_ so as to decrease the objective _R_ ( _θ_ ) in (10.25)? The _gradient_ of _R_ ( _θ_ ), evaluated at some current value _θ_ = _θ[m]_ , gradient is the vector of partial derivatives at that point: 

$$
\nabla R(\theta) = \left( \frac{\partial R(\theta)}{\partial \theta_1}, \dots, \frac{\partial R(\theta)}{\partial \theta_m} \right)
$$

The subscript _θ_ = _θ[m]_ means that after computing the vector of derivatives, we evaluate it at the current guess, _θ[m]_ . This gives the direction in _θ_ -space in which _R_ ( _θ_ ) _increases_ most rapidly. The idea of gradient descent is to move _θ_ a little in the _opposite_ direction (since we wish to go downhill):

$$
\theta^{(m+1)} \leftarrow \theta^{(m)} - \rho \nabla R(\theta^{(m)}) \quad (10.26)
$$

10.7 Fitting a Neural Network 429 

For a small enough value of the _learning rate ρ_ , this step will decrease the learning rate objective _R_ ( _θ_ ); i.e. _R_ ( _θ[m]_[+1] ) _≤ R_ ( _θ[m]_ ). If the gradient vector is zero, then we may have arrived at a minimum of the objective. 

How complicated is the calculation (10.26)? It turns out that it is quite simple here, and remains simple even for much more complex networks, because of the _chain rule_ of differentiation. 

_n_ Since _R_ ( _θ_ ) =[�] _[n] i_ =1 _[R][i]_[(] _[θ]_[)][=][1] 2 � _i_ =1[(] _[y][i][ −][f][θ]_[(] _[x][i]_[))][2][is][a][sum,][its][gradient] is also a sum over the _n_ observations, so we will just examine one of these terms,

$$
R_i(\theta) = \frac{1}{2} \left( y_i - \beta_0 - \sum_{k=1}^K \beta_k g(z_{ik}) \right)^2 \quad (10.27)
$$

To simplify the expressions to follow, we write _zik_ = _wk_ 0 +[�] _[p] j_ =1 _[w][kj][x][ij]_[.] First we take the derivative with respect to _βk_ :

$$
\frac{\partial R_i(\theta)}{\partial \beta_k} = - (y_i - f_\theta(x_i)) g(z_{ik}) \quad (10.28)
$$

And now we take the derivative with respect to _wkj_ :

$$
\frac{\partial R_i(\theta)}{\partial w_{kj}} = - (y_i - f_\theta(x_i)) \beta_k g'(z_{ik}) x_{ij} \quad (10.29)
$$

Notice that both these expressions contain the residual _yi − fθ_ ( _xi_ ). In (10.29) we see that a fraction of that residual gets attributed to each of the hidden units according to the value of _g_ ( _zik_ ). Then in (10.30) we see a similar attribution to input _j_ via hidden unit _k_ . So the act of differentiation assigns a fraction of the residual to each of the parameters via the chain rule — a process known as _backpropagation_ in the neural network backpropliterature. Although these calculations are straightforward, it takes careful agation bookkeeping to keep track of all the pieces. 

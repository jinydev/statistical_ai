---
layout: default
title: "index"
---

# _9.4.2 One-Versus-All Classification_ 

The _one-versus-all_ approach (also referred to as _one-versus-rest_ ) is an al- one-versusternative procedure for applying SVMs in the case of _K >_ 2 classes. We all fit _K_ SVMs, each time comparing one of the _K_ classes to the remaining one-versus- _K −_ 1 classes. Let _β_ 0 _k, β_ 1 _k, . . . , βpk_ denote the parameters that result from rest fitting an SVM comparing the _k_ th class (coded as +1) to the others (coded as _−_ 1). Let _x[∗]_ denote a test observation. We assign the observation to the class for which _β_ 0 _k_ + _β_ 1 _kx[∗]_ 1[+] _[β]_[2] _[k][x][∗]_ 2[+] _[· · ·]_[+] _[β][pk][x][∗] p_[is largest, as this amounts] to a high level of confidence that the test observation belongs to the _k_ th class rather than to any of the other classes. 

---
layout: default
title: "index"
---

# **Algorithm 7.1** _Local Regression At X_ = _x_ 0 

1. Gather the fraction _s_ = _k/n_ of training points whose _xi_ are closest to _x_ 0. 

2. Assign a weight _Ki_ 0 = _K_ ( _xi, x_ 0) to each point in this neighborhood, so that the point furthest from _x_ 0 has weight zero, and the closest has the highest weight. All but these _k_ nearest neighbors get weight zero. 

3. Fit a _weighted least squares regression_ of the _yi_ on the _xi_ using the aforementioned weights, by finding _β_[ˆ] 0 and _β_[ˆ] 1 that minimize 


4. The fitted value at _x_ 0 is given by _f_[ˆ] ( _x_ 0) = _β_[ˆ] 0 + _β_[ˆ] 1 _x_ 0. 

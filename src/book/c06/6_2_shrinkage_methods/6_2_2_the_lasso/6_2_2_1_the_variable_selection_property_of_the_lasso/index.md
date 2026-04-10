---
layout: default
title: "index"
---

# The Variable Selection Property of the Lasso 

Why is it that the lasso, unlike ridge regression, results in coefficient estimates that are exactly equal to zero? The formulations (6.8) and (6.9) can be used to shed light on the issue. Figure 6.7 illustrates the situation. The least squares solution is marked as _β_[ˆ] , while the blue diamond and circle represent the lasso and ridge regression constraints in (6.8) and (6.9), respectively. _β_ ˆ, and so theIf _s_ ridgeis sufficientlyregressionlarge,and thenlasso theestimatesconstraintwill regionsbe the samewill containas the least squares estimates. (Such a large value of _s_ corresponds to _λ_ = 0 in (6.5) and (6.7).) However, in Figure 6.7 the least squares estimates lie outside of the diamond and the circle, and so the least squares estimates are not the same as the lasso and ridge regression estimates. 

Each of the ellipses centered around _β_[ˆ] represents a _contour_ : this means contour that all of the points on a particular ellipse have the same RSS value. As 

6.2 Shrinkage Methods 247 

**FIGURE 6.7.** _Contours of the error and constraint functions for the lasso_ (left) _and ridge regression_ (right) _. The solid blue areas are the constraint regions, |β_ 1 _|_ + _|β_ 2 _| ≤ s and β_ 1[2][+] _[β]_ 2[2] _[≤][s][,][while][the][red][ellipses][are][the][contours][of][the][RSS.]_ 

the ellipses expand away from the least squares coefficient estimates, the RSS increases. Equations (6.8) and (6.9) indicate that the lasso and ridge regression coefficient estimates are given by the first point at which an ellipse contacts the constraint region. Since ridge regression has a circular constraint with no sharp points, this intersection will not generally occur on an axis, and so the ridge regression coefficient estimates will be exclusively non-zero. However, the lasso constraint has _corners_ at each of the axes, and so the ellipse will often intersect the constraint region at an axis. When this occurs, one of the coefficients will equal zero. In higher dimensions, many of the coefficient estimates may equal zero simultaneously. In Figure 6.7, the intersection occurs at _β_ 1 = 0, and so the resulting model will only include _β_ 2. 

In Figure 6.7, we considered the simple case of _p_ = 2. When _p_ = 3, then the constraint region for ridge regression becomes a sphere, and the constraint region for the lasso becomes a polyhedron. When _p >_ 3, the constraint for ridge regression becomes a hypersphere, and the constraint for the lasso becomes a polytope. However, the key ideas depicted in Figure 6.7 still hold. In particular, the lasso leads to feature selection when _p >_ 2 due to the sharp corners of the polyhedron or polytope. 

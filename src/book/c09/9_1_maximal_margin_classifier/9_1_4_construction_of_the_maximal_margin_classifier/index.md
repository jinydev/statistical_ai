---
layout: default
title: "index"
---

# _9.1.4 Construction of the Maximal Margin Classifier_ 

We now consider the task of constructing the maximal margin hyperplane based on a set of _n_ training observations _x_ 1 _, . . . , xn ∈_ R _[p]_ and associated class labels _y_ 1 _, . . . , yn ∈{−_ 1 _,_ 1 _}_ . Briefly, the maximal margin hyperplane is the solution to the optimization problem

$$
\begin{align*}
& \underset{\beta_0, \dots, \beta_p, M}{\text{maximize}} M \quad (9.9) \\
& \text{subject to } \sum_{j=1}^p \beta_j^2 = 1, \quad (9.10) \\
& y_i (\beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip}) \ge M \quad \forall i = 1, \dots, n \quad (9.11)
\end{align*}
$$

This optimization problem (9.9)–(9.11) is actually simpler than it looks. First of all, the constraint in (9.11) that

$$
y_i (\beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip}) \ge M
$$

guarantees that each observation will be on the correct side of the hyperplane, provided that _M_ is positive. (Actually, for each observation to be on the correct side of the hyperplane we would simply need _yi_ ( _β_ 0 + _β_ 1 _xi_ 1 + _β_ 2 _xi_ 2 + _· · ·_ + _βpxip_ ) _>_ 0, so the constraint in (9.11) in fact requires that each observation be on the correct side of the hyperplane, with some cushion, provided that _M_ is positive.) 

Second, note that (9.10) is not really a constraint on the hyperplane, since if _β_ 0 + _β_ 1 _xi_ 1 + _β_ 2 _xi_ 2 + _· · ·_ + _βpxip_ = 0 defines a hyperplane, then so does _k_ ( _β_ 0 + _β_ 1 _xi_ 1 + _β_ 2 _xi_ 2 + _· · ·_ + _βpxip_ ) = 0 for any _k_ = 0. However, (9.10) adds meaning to (9.11); one can show that with this constraint the perpendicular distance from the _i_ th observation to the hyperplane is given by

$$
y_i (\beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip})
$$

Therefore, the constraints (9.10) and (9.11) ensure that each observation is on the correct side of the hyperplane and at least a distance _M_ from the hyperplane. Hence, _M_ represents the margin of our hyperplane, and the optimization problem chooses _β_ 0 _, β_ 1 _, . . . , βp_ to maximize _M_ . This is exactly the definition of the maximal margin hyperplane! The problem (9.9)–(9.11) can be solved efficiently, but details of this optimization are outside of the scope of this book. 

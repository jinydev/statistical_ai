---
layout: default
title: "index"
---

# _9.1.1 What Is a Hyperplane?_ 

In a _p_ -dimensional space, a _hyperplane_ is a flat affine subspace of hyperplane dimension _p −_ 1.[1] For instance, in two dimensions, a hyperplane is a flat one-dimensional subspace—in other words, a line. In three dimensions, a hyperplane is a flat two-dimensional subspace—that is, a plane. In _p >_ 3 dimensions, it can be hard to visualize a hyperplane, but the notion of a ( _p −_ 1)-dimensional flat subspace still applies. 

The mathematical definition of a hyperplane is quite simple. In two dimensions, a hyperplane is defined by the equation

$$
\beta_0 + \beta_1 X_1 + \beta_2 X_2 = 0 \quad (9.1)
$$


for parameters _β_ 0 _, β_ 1, and _β_ 2. When we say that (9.1) “defines” the hyperplane, we mean that any _X_ = ( _X_ 1 _, X_ 2) _[T]_ for which (9.1) holds is a point on the hyperplane. Note that (9.1) is simply the equation of a line, since indeed in two dimensions a hyperplane is a line. 

Equation 9.1 can be easily extended to the _p_ -dimensional setting:

$$
\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p = 0 \quad (9.2)
$$


defines a _p_ -dimensional hyperplane, again in the sense that if a point _X_ = ( _X_ 1 _, X_ 2 _, . . . , Xp_ ) _[T]_ in _p_ -dimensional space (i.e. a vector of length _p_ ) satisfies (9.2), then _X_ lies on the hyperplane. 

Now, suppose that _X_ does not satisfy (9.2); rather,

$$
\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p > 0
$$


Then this tells us that _X_ lies to one side of the hyperplane. On the other hand, if

$$
\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p < 0
$$


then _X_ lies on the other side of the hyperplane. So we can think of the hyperplane as dividing _p_ -dimensional space into two halves. One can easily determine on which side of the hyperplane a point lies by simply calculating the sign of the left-hand side of (9.2). A hyperplane in two-dimensional space is shown in Figure 9.1. 

---
layout: default
title: "index"
---

# _7.4.2 Constraints and Splines_ 

The top left panel of Figure 7.3 looks wrong because the fitted curve is just too flexible. To remedy this problem, we can fit a piecewise polynomial under the _constraint_ that the fitted curve must be continuous. In other words, there cannot be a jump when `age=50` . The top right plot in Figure 7.3 shows the resulting fit. This looks better than the top left plot, but the V- shaped join looks unnatural. 

In the lower left plot, we have added two additional constraints: now both the first and second _derivatives_ of the piecewise polynomials are continuous derivative at `age=50` . In other words, we are requiring that the piecewise polynomial be not only continuous when `age=50` , but also very _smooth_ . Each constraint that we impose on the piecewise cubic polynomials effectively frees up one degree of freedom, by reducing the complexity of the resulting piecewise polynomial fit. So in the top left plot, we are using eight degrees of freedom, but in the bottom left plot we imposed three constraints (continuity, continuity of the first derivative, and continuity of the second derivative) and so are left with five degrees of freedom. The curve in the bottom left plot is called a _cubic spline_ .[3] In general, a cubic spline with _K_ knots uses cubic spline a total of 4 + _K_ degrees of freedom. 

In Figure 7.3, the lower right plot is a _linear spline_ , which is continuous linear spline at `age=50` . The general definition of a degree- _d_ spline is that it is a piecewise degree- _d_ polynomial, with continuity in derivatives up to degree _d −_ 1 at each knot. Therefore, a linear spline is obtained by fitting a line in each region of the predictor space defined by the knots, requiring continuity at each knot. 

In Figure 7.3, there is a single knot at `age=50` . Of course, we could add more knots, and impose continuity at each. 

---
layout: default
title: "index"
---

# _12.2.2 Another Interpretation of Principal Components_ 

The first two principal component loading vectors in a simulated threedimensional data set are shown in the left-hand panel of Figure 12.2; these two loading vectors span a plane along which the observations have the highest variance. 

In the previous section, we describe the principal component loading vectors as the directions in feature space along which the data vary the most, and the principal component scores as projections along these directions. However, an alternative interpretation of principal components can also be 

12.2 Principal Components Analysis 509 

**FIGURE 12.2.** _Ninety observations simulated in three dimensions. The observations are displayed in color for ease of visualization._ Left: _the first two principal component directions span the plane that best fits the data. The plane is positioned to minimize the sum of squared distances to each point._ Right: _the first two principal component score vectors give the coordinates of the projection of the 90 observations onto the plane._ 

useful: principal components provide low-dimensional linear surfaces that are _closest_ to the observations. We expand upon that interpretation here.[3] The first principal component loading vector has a very special property: it is the line in _p_ -dimensional space that is _closest_ to the _n_ observations (using average squared Euclidean distance as a measure of closeness). This interpretation can be seen in the left-hand panel of Figure 6.15; the dashed lines indicate the distance between each observation and the line defined by the first principal component loading vector. The appeal of this interpretation is clear: we seek a single dimension of the data that lies as close as possible to all of the data points, since such a line will likely provide a good summary of the data. 

The notion of principal components as the dimensions that are closest to the _n_ observations extends beyond just the first principal component. For instance, the first two principal components of a data set span the plane that is closest to the _n_ observations, in terms of average squared Euclidean distance. An example is shown in the left-hand panel of Figure 12.2. The first three principal components of a data set span the three-dimensional hyperplane that is closest to the _n_ observations, and so forth. 

Using this interpretation, together the first _M_ principal component score vectors and the first _M_ principal component loading vectors provide the best _M_ -dimensional approximation (in terms of Euclidean distance) to 

> 3In this section, we continue to assume that each column of the data matrix **X** has been centered to have mean zero—that is, the column mean has been subtracted from each column. 

510 12. Unsupervised Learning 

the _i_ th observation _xij_ . This representation can be written as

$$
x_{ij} \approx \sum_{m=1}^M z_{im} \phi_{jm} \quad (12.5)
$$

We can state this more formally by writing down an optimization problem. Suppose the data matrix **X** is column-centered. Out of all approximations of the form _xij ≈_[�] _[M] m_ =1 _[a][im][b][jm]_[,][we][could][ask][for][the][one][with][the] smallest residual sum of squares:

$$
\min_{\mathbf{A} \in \mathbb{R}^{n \times M}, \mathbf{B} \in \mathbb{R}^{p \times M}} \left\{ \sum_{j=1}^p \sum_{i=1}^n \left( x_{ij} - \sum_{m=1}^M a_{im} b_{jm} \right)^2 \right\} \quad (12.6)
$$

Here, **A** is an _n × M_ matrix whose ( _i, m_ ) element is _aim_ , and **B** is a _p × M_ element whose ( _j, m_ ) element is _bjm_ . 

**A** ˆ Itandcan **B** ˆbethatshownsolvethat(12.6for) areany invaluefactofthe _M_ first, the _M_ columnsprincipalof thecomponentsmatrices score and loading vectors. In other words, if **A**[ˆ] and **B**[ˆ] solve (12.6), then ˆ _aim_ = _zim_ and[ˆ] _bjm_ = _φjm_ .[4] This means that the smallest possible value of the objective in (12.6) is

$$
\sum_{j=1}^p \sum_{i=1}^n \left( x_{ij} - \sum_{m=1}^M z_{im} \phi_{jm} \right)^2 \quad (12.7)
$$

In summary, together the _M_ principal component score vectors and _M_ principal component loading vectors can give a good approximation to the data when _M_ is sufficiently large. When _M_ = min( _n −_ 1 _, p_ ), then the representation is exact: _xij_ =[�] _[M] m_ =1 _[z][im][φ][jm]_[.] 

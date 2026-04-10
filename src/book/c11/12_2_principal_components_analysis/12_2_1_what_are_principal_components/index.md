---
layout: default
title: "index"
---

# _12.2.1 What Are Principal Components?_ 

Suppose that we wish to visualize _n_ observations with measurements on a set of _p_ features, _X_ 1 _, X_ 2 _, . . . , Xp_ , as part of an exploratory data analysis. We could do this by examining two-dimensional scatterplots of the data, each of which contains the _n_ observations’ measurements on two of the features. However, there are � _p_ 2� = _p_ ( _p−_ 1) _/_ 2 such scatterplots; for example, with _p_ = 10 there are 45 plots! If _p_ is large, then it will certainly not be possible to look at all of them; moreover, most likely none of them will be informative since they each contain just a small fraction of the total information present in the data set. Clearly, a better method is required to visualize the _n_ observations when _p_ is large. In particular, we would like to find a low-dimensional representation of the data that captures as much of the information as possible. For instance, if we can obtain a two-dimensional representation of the data that captures most of the information, then we can plot the observations in this low-dimensional space. 

PCA provides a tool to do just this. It finds a low-dimensional representation of a data set that contains as much as possible of the variation. The idea is that each of the _n_ observations lives in _p_ -dimensional space, but not all of these dimensions are equally interesting. PCA seeks a small number of dimensions that are as interesting as possible, where the concept of _interesting_ is measured by the amount that the observations vary along each dimension. Each of the dimensions found by PCA is a linear combination of the _p_ features. We now explain the manner in which these dimensions, or _principal components_ , are found. 

The _first principal component_ of a set of features _X_ 1 _, X_ 2 _, . . . , Xp_ is the normalized linear combination of the features

$$
Z_1 = \phi_{11} X_1 + \phi_{21} X_2 + \dots + \phi_{p1} X_p \quad (12.1)
$$

that has the largest variance. By _normalized_ , we mean that[�] _[p] j_ =1 _[φ]_[2] _j_ 1[= 1][.] We refer to the elements _φ_ 11 _, . . . , φp_ 1 as the _loadings_ of the first principal loading component; together, the loadings make up the principal component loading vector, _φ_ 1 = ( _φ_ 11 _φ_ 21 _. . . φp_ 1) _[T]_ . We constrain the loadings so that their sum of squares is equal to one, since otherwise setting these elements to be arbitrarily large in absolute value could result in an arbitrarily large variance. 

Given an _n × p_ data set **X** , how do we compute the first principal component? Since we are only interested in variance, we assume that each of the variables in **X** has been centered to have mean zero (that is, the column means of **X** are zero). We then look for the linear combination of the sample feature values of the form

$$
z_{i1} = \phi_{11} x_{i1} + \phi_{21} x_{i2} + \dots + \phi_{p1} x_{ip} \quad (12.2)
$$

506 12. Unsupervised Learning 

that has largest sample variance, subject to the constraint that[�] _[p] j_ =1 _[φ]_[2] _j_ 1[=1][.] In other words, the first principal component loading vector solves the optimization problem

$$
\underset{\phi_{11}, \dots, \phi_{p1}}{\text{maximize}} \left\{ \frac{1}{n} \sum_{i=1}^n \left( \sum_{j=1}^p \phi_{j1} x_{ij} \right)^2 \right\} \quad \text{subject to } \sum_{j=1}^p \phi_{j1}^2 = 1 \quad (12.3)
$$

From (12.2) we can write the objective in (12.3) as _n_ 1 � _ni_ =1 _[z] i_[2] 1[.][Since] _n_ 1 � _ni_ =1 _[x][ij]_[=][0][,][the][average][of][the] _[z]_[11] _[, . . . , z][n]_[1][will][be][zero][as][well.][Hence] the objective that we are maximizing in (12.3) is just the sample variance of the _n_ values of _zi_ 1. We refer to _z_ 11 _, . . . , zn_ 1 as the _scores_ of the first princi- score pal component. Problem (12.3) can be solved via an _eigen decomposition_ , eigen decoma standard technique in linear algebra, but the details are outside of the position scope of this book.[1] 

There is a nice geometric interpretation of the first principal component. The loading vector _φ_ 1 with elements _φ_ 11 _, φ_ 21 _, . . . , φp_ 1 defines a direction in feature space along which the data vary the most. If we project the _n_ data points _x_ 1 _, . . . , xn_ onto this direction, the projected values are the principal component scores _z_ 11 _, . . . , zn_ 1 themselves. For instance, Figure 6.14 on page 254 displays the first principal component loading vector (green solid line) on an advertising data set. In these data, there are only two features, and so the observations as well as the first principal component loading vector can be easily displayed. As can be seen from (6.19), in that data set _φ_ 11 = 0 _._ 839 and _φ_ 21 = 0 _._ 544. 

After the first principal component _Z_ 1 of the features has been determined, we can find the second principal component _Z_ 2. The second principal component is the linear combination of _X_ 1 _, . . . , Xp_ that has maximal variance out of all linear combinations that are _uncorrelated_ with _Z_ 1. The second principal component scores _z_ 12 _, z_ 22 _, . . . , zn_ 2 take the form

$$
z_{i2} = \phi_{12} x_{i1} + \phi_{22} x_{i2} + \dots + \phi_{p2} x_{ip} \quad (12.4)
$$

where _φ_ 2 is the second principal component loading vector, with elements _φ_ 12 _, φ_ 22 _, . . . , φp_ 2. It turns out that constraining _Z_ 2 to be uncorrelated with _Z_ 1 is equivalent to constraining the direction _φ_ 2 to be orthogonal (perpendicular) to the direction _φ_ 1. In the example in Figure 6.14, the observations lie in two-dimensional space (since _p_ = 2), and so once we have found _φ_ 1, there is only one possibility for _φ_ 2, which is shown as a blue dashed line. (From Section 6.3.1, we know that _φ_ 12 = 0 _._ 544 and _φ_ 22 = _−_ 0 _._ 839.) But in a larger data set with _p >_ 2 variables, there are multiple distinct principal components, and they are defined in a similar manner. To find _φ_ 2, we solve a problem similar to (12.3) with _φ_ 2 replacing _φ_ 1, and with the additional constraint that _φ_ 2 is orthogonal to _φ_ 1.[2] 

> 1As an alternative to the eigen decomposition, a related technique called the singular value decomposition can be used. This will be explored in the lab at the end of this chapter. 

> 2On a technical note, the principal component directions _φ_ 1, _φ_ 2, _φ_ 3 _, . . ._ are given by the ordered sequence of eigenvectors of the matrix **X** _[T]_ **X** , and the variances of the components are the eigenvalues. There are at most min( _n −_ 1 _, p_ ) principal components. 

12.2 Principal Components Analysis 507 

**FIGURE 12.1.** _The first two principal components for the_ `USArrests` _data. The blue state names represent the scores for the first two principal components. The orange arrows indicate the first two principal component loading vectors (with axes on the top and right). For example, the loading for_ `Rape` _on the first component is_ 0 _._ 54 _, and its loading on the second principal component_ 0 _._ 17 _(the word_ `Rape` _is centered at the point_ (0 _._ 54 _,_ 0 _._ 17) _). This figure is known as a biplot, because it displays both the principal component scores and the principal component loadings._ 

Once we have computed the principal components, we can plot them against each other in order to produce low-dimensional views of the data. For instance, we can plot the score vector _Z_ 1 against _Z_ 2, _Z_ 1 against _Z_ 3, _Z_ 2 against _Z_ 3, and so forth. Geometrically, this amounts to projecting the original data down onto the subspace spanned by _φ_ 1, _φ_ 2, and _φ_ 3, and plotting the projected points. 

We illustrate the use of PCA on the `USArrests` data set. For each of the 50 states in the United States, the data set contains the number of arrests per 100 _,_ 000 residents for each of three crimes: `Assault` , `Murder` , and `Rape` . We also record `UrbanPop` (the percent of the population in each state living in urban areas). The principal component score vectors have length _n_ = 50, and the principal component loading vectors have length _p_ = 4. PCA was performed after standardizing each variable to have mean zero and standard 

12. Unsupervised Learning 

508 

||PC1|PC2|
|---|---|---|
|`Murder`|0.5358995|_−_0.4181809|
|`Assault`|0.5831836|_−_0.1879856|
|`UrbanPop`|0.2781909|0.8728062|
|`Rape`|0.5434321|0.1673186|



**TABLE 12.1.** _The principal component loading vectors, φ_ 1 _and φ_ 2 _, for the_ `USArrests` _data. These are also displayed in Figure 12.1._ 

deviation one. Figure 12.1 plots the first two principal components of these data. The figure represents both the principal component scores and the loading vectors in a single _biplot_ display. The loadings are also given in biplot Table 12.2.1. 

In Figure 12.1, we see that the first loading vector places approximately equal weight on `Assault` , `Murder` , and `Rape` , but with much less weight on `UrbanPop` . Hence this component roughly corresponds to a measure of overall rates of serious crimes. The second loading vector places most of its weight on `UrbanPop` and much less weight on the other three features. Hence, this component roughly corresponds to the level of urbanization of the state. Overall, we see that the crime-related variables ( `Murder` , `Assault` , and `Rape` ) are located close to each other, and that the `UrbanPop` variable is far from the other three. This indicates that the crime-related variables are correlated with each other—states with high murder rates tend to have high assault and rape rates—and that the `UrbanPop` variable is less correlated with the other three. 

We can examine differences between the states via the two principal component score vectors shown in Figure 12.1. Our discussion of the loading vectors suggests that states with large positive scores on the first component, such as California, Nevada and Florida, have high crime rates, while states like North Dakota, with negative scores on the first component, have low crime rates. California also has a high score on the second component, indicating a high level of urbanization, while the opposite is true for states like Mississippi. States close to zero on both components, such as Indiana, have approximately average levels of both crime and urbanization. 

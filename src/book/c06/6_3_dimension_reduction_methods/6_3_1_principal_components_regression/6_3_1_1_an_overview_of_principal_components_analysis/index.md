---
layout: default
title: "index"
---

# An Overview of Principal Components Analysis 

PCA is a technique for reducing the dimension of an _n × p_ data matrix **X** . The _first principal component_ direction of the data is that along which the observations _vary the most_ . For instance, consider Figure 6.14, which shows population size ( `pop` ) in tens of thousands of people, and ad spending for a particular company ( `ad` ) in thousands of dollars, for 100 cities.[6] The green solid line represents the first principal component direction of the data. We can see by eye that this is the direction along which there is the greatest variability in the data. That is, if we _projected_ the 100 observations onto this line (as shown in the left-hand panel of Figure 6.15), then the resulting projected observations would have the largest possible variance; projecting the observations onto any other line would yield projected observations with lower variance. Projecting a point onto a line simply involves finding the location on the line which is closest to the point. 

The first principal component is displayed graphically in Figure 6.14, but how can it be summarized mathematically? It is given by the formula 

$$
Z_1 = 0.839 \times (\text{pop} - \overline{\text{pop}}) + 0.544 \times (\text{ad} - \overline{\text{ad}}) \quad (6.19)
$$

Here _φ_ 11 = 0 _._ 839 and _φ_ 21 = 0 _._ 544 are the principal component loadings, which define the direction referred to above. In (6.19), pop indicates the mean of all `pop` values in this data set, and ad indicates the mean of all advertising spending. The idea is that out of every possible _linear combination_ of `pop` and `ad` such that _φ_[2] 11[+] _[ φ]_[2] 21[=][1][,][this][particular][linear][combination] yields the highest variance: i.e. this is the linear combination for which Var( _φ_ 11 _×_ (pop _−_ pop) + _φ_ 21 _×_ (ad _−_ ad)) is maximized. It is necessary to consider only linear combinations of the form _φ_[2] 11[+] _[φ]_[2] 21[= 1][, since otherwise] we could increase _φ_ 11 and _φ_ 21 arbitrarily in order to blow up the variance. In (6.19), the two loadings are both positive and have similar size, and so _Z_ 1 is almost an _average_ of the two variables. 

Since _n_ = 100, `pop` and `ad` are vectors of length 100, and so is _Z_ 1 in (6.19). For instance, 

$$
z_{i1} = 0.839 \times (\text{pop}_i - \overline{\text{pop}}) + 0.544 \times (\text{ad}_i - \overline{\text{ad}})
$$

The values of _z_ 11 _, . . . , zn_ 1 are known as the _principal component scores_ , and can be seen in the right-hand panel of Figure 6.15. 

There is also another interpretation of PCA: the first principal component vector defines the line that is _as close as possible_ to the data. For instance, in Figure 6.14, the first principal component line minimizes the sum of the squared perpendicular distances between each point and the line. These distances are plotted as dashed line segments in the left-hand 

> 6This dataset is distinct from the `Advertising` data discussed in Chapter 3. 

256 6. Linear Model Selection and Regularization 

![Figure 6.15](./img/6_15.png)

**FIGURE 6.15.** _A subset of the advertising data. The mean_ `pop` _and_ `ad` _budgets are indicated with a blue circle._ Left: _The first principal component direction is shown in green. It is the dimension along which the data vary the most, and it also defines the line that is closest to all n of the observations. The distances from each observation to the principal component are represented using the black dashed line segments. The blue dot represents_ (pop ~~_,_~~ ad) _._ Right: _The left-hand panel has been rotated so that the first principal component direction coincides with the x-axis._ 

panel of Figure 6.15, in which the crosses represent the _projection_ of each point onto the first principal component line. The first principal component has been chosen so that the projected observations are _as close as possible_ to the original observations. 

In the right-hand panel of Figure 6.15, the left-hand panel has been rotated so that the first principal component direction coincides with the _x_ -axis. It is possible to show that the _first principal component score_ for the _i_ th observation, given in (6.20), is the distance in the _x_ -direction of the _i_ th cross from zero. So for example, the point in the bottom-left corner of the left-hand panel of Figure 6.15 has a large negative principal component score, _zi_ 1 = _−_ 26 _._ 1, while the point in the top-right corner has a large positive score, _zi_ 1 = 18 _._ 7. These scores can be computed directly using (6.20). 

We can think of the values of the principal component _Z_ 1 as singlenumber summaries of the joint `pop` and `ad` budgets for each location. In this example, if _zi_ 1 = 0 _._ 839 _×_ (pop _i −_ pop) + 0 _._ 544 _×_ (ad _i −_ ad) _<_ 0, then this indicates a city with below-average population size and belowaverage ad spending. A positive score suggests the opposite. How well can a single number represent both `pop` and `ad` ? In this case, Figure 6.14 indicates that `pop` and `ad` have approximately a linear relationship, and so we might expect that a single-number summary will work well. Figure 6.16 displays _zi_ 1 versus both `pop` and `ad` .[7] The plots show a strong relationship between the first principal component and the two features. In other words, the first principal component appears to capture most of the information contained in the `pop` and `ad` predictors. 

So far we have concentrated on the first principal component. In general, one can construct up to _p_ distinct principal components. The second 

> 7The principal components were calculated after first standardizing both `pop` and `ad` , a common approach. Hence, the x-axes on Figures 6.15 and 6.16 are not on the same scale. 

6.3 Dimension Reduction Methods 257 

![Figure 6.16](./img/6_16.png)

**FIGURE 6.16.** _Plots of the first principal component scores zi_ 1 _versus_ `pop` _and_ `ad` _. The relationships are strong._ 

principal component _Z_ 2 is a linear combination of the variables that is uncorrelated with _Z_ 1, and has largest variance subject to this constraint. The second principal component direction is illustrated as a dashed blue line in Figure 6.14. It turns out that the zero correlation condition of _Z_ 1 with _Z_ 2 is equivalent to the condition that the direction must be _perpendicular_ , or perpen- _orthogonal_ , to the first principal component direction. The second principal component is given by the formula 

$$
Z_2 = 0.544 \times (\text{pop} - \overline{\text{pop}}) - 0.839 \times (\text{ad} - \overline{\text{ad}}) \quad (6.20)
$$

Since the advertising data has two predictors, the first two principal components contain all of the information that is in `pop` and `ad` . However, by construction, the first component will contain the most information. Consider, for example, the much larger variability of _zi_ 1 (the _x_ -axis) versus _zi_ 2 (the _y_ -axis) in the right-hand panel of Figure 6.15. The fact that the second principal component scores are much closer to zero indicates that this component captures far less information. As another illustration, Figure 6.17 displays _zi_ 2 versus `pop` and `ad` . There is little relationship between the second principal component and these two predictors, again suggesting that in this case, one only needs the first principal component in order to accurately represent the `pop` and `ad` budgets. 

With two-dimensional data, such as in our advertising example, we can construct at most two principal components. However, if we had other predictors, such as population age, income level, education, and so forth, then additional components could be constructed. They would successively maximize variance, subject to the constraint of being uncorrelated with the preceding components. 

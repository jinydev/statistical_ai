---
layout: default
title: "index"
---

# Scaling the Variables 

We have already mentioned that before PCA is performed, the variables should be centered to have mean zero. Furthermore, _the results obtained when we perform PCA will also depend on whether the variables have been individually scaled_ (each multiplied by a different constant). This is in contrast to some other supervised and unsupervised learning techniques, such as linear regression, in which scaling the variables has no effect. (In linear regression, multiplying a variable by a factor of _c_ will simply lead to multiplication of the corresponding coefficient estimate by a factor of 1 _/c_ , and thus will have no substantive effect on the model obtained.) 

For instance, Figure 12.1 was obtained after scaling each of the variables to have standard deviation one. This is reproduced in the left-hand plot in Figure 12.4. Why does it matter that we scaled the variables? In these data, the variables are measured in different units; `Murder` , `Rape` , and `Assault` are reported as the number of occurrences per 100 _,_ 000 people, and `UrbanPop` is the percentage of the state’s population that lives in an urban area. These four variables have variances of 18 _._ 97, 87 _._ 73, 6945 _._ 16, and 209 _._ 5, respectively. Consequently, if we perform PCA on the unscaled variables, then 

12.2 Principal Components Analysis 513 

![Figure 12.4](./img/12_4.png)

**FIGURE 12.4.** _Two principal component biplots for the_ `USArrests` _data._ Left: _the same as Figure 12.1, with the variables scaled to have unit standard deviations._ Right: _principal components using unscaled data._ `Assault` _has by far the largest loading on the first principal component because it has the highest variance among the four variables. In general, scaling the variables to have standard deviation one is recommended._ 

the first principal component loading vector will have a very large loading for `Assault` , since that variable has by far the highest variance. The righthand plot in Figure 12.4 displays the first two principal components for the `USArrests` data set, without scaling the variables to have standard deviation one. As predicted, the first principal component loading vector places almost all of its weight on `Assault` , while the second principal component loading vector places almost all of its weight on `UrbanPop` . Comparing this to the left-hand plot, we see that scaling does indeed have a substantial effect on the results obtained. 

However, this result is simply a consequence of the scales on which the variables were measured. For instance, if `Assault` were measured in units of the number of occurrences per 100 people (rather than number of occurrences per 100 _,_ 000 people), then this would amount to dividing all of the elements of that variable by 1 _,_ 000. Then the variance of the variable would be tiny, and so the first principal component loading vector would have a very small value for that variable. Because it is undesirable for the principal components obtained to depend on an arbitrary choice of scaling, we typically scale each variable to have standard deviation one before we perform PCA. 

In certain settings, however, the variables may be measured in the same units. In this case, we might not wish to scale the variables to have standard deviation one before performing PCA. For instance, suppose that the variables in a given data set correspond to expression levels for _p_ genes. Then since expression is measured in the same “units” for each gene, we might choose not to scale the genes to each have standard deviation one. 

514 12. Unsupervised Learning 

---
layout: default
title: "index"
---

# _9.2.1 Overview of the Support Vector Classifier_ 

In Figure 9.4, we see that observations that belong to two classes are not necessarily separable by a hyperplane. In fact, even if a separating hyperplane does exist, then there are instances in which a classifier based on a separating hyperplane might not be desirable. A classifier based on a separating hyperplane will necessarily perfectly classify all of the training observations; this can lead to sensitivity to individual observations. An example is shown in Figure 9.5. The addition of a single observation in the right-hand panel of Figure 9.5 leads to a dramatic change in the maximal margin hyperplane. The resulting maximal margin hyperplane is not satisfactory—for one thing, it has only a tiny margin. This is problematic because as discussed previously, the distance of an observation from the hyperplane can be seen as a measure of our confidence that the observation was correctly classified. Moreover, the fact that the maximal margin hyperplane is extremely sensitive to a change in a single observation suggests that it may have overfit the training data. 

In this case, we might be willing to consider a classifier based on a hyperplane that does _not_ perfectly separate the two classes, in the interest of 

374 9. Support Vector Machines 

![Figure 9.5](./img/9_5.png)

**FIGURE 9.5.** Left: _Two classes of observations are shown in blue and in purple, along with the maximal margin hyperplane._ Right: _An additional blue observation has been added, leading to a dramatic shift in the maximal margin hyperplane shown as a solid line. The dashed line indicates the maximal margin hyperplane that was obtained in the absence of this additional point._ 

- Greater robustness to individual observations, and 

- Better classification of _most_ of the training observations. 

That is, it could be worthwhile to misclassify a few training observations in order to do a better job in classifying the remaining observations. 

The _support vector classifier_ , sometimes called a _soft margin classifier_ , support does exactly this. Rather than seeking the largest possible margin so that vector every observation is not only on the correct side of the hyperplane but classifier also on the correct side of the margin, we instead allow some observations soft to be on the incorrect side of the margin, or even the incorrect side of classifier the hyperplane. (The margin is _soft_ because it can be violated by some of the training observations.) An example is shown in the left-hand panel of Figure 9.6. Most of the observations are on the correct side of the margin. However, a small subset of the observations are on the wrong side of the margin. 

vector classifier soft margin classifier 

An observation can be not only on the wrong side of the margin, but also on the wrong side of the hyperplane. In fact, when there is no separating hyperplane, such a situation is inevitable. Observations on the wrong side of the hyperplane correspond to training observations that are misclassified by the support vector classifier. The right-hand panel of Figure 9.6 illustrates such a scenario. 

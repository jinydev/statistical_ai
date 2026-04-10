---
layout: default
title: "index"
---

# _12.2.5 Other Uses for Principal Components_ 

We saw in Section 6.3.1 that we can perform regression using the principal component score vectors as features. In fact, many statistical techniques, such as regression, classification, and clustering, can be easily adapted to use the _n × M_ matrix whose columns are the first _M ≪ p_ principal component score vectors, rather than using the full _n × p_ data matrix. This can lead to _less noisy_ results, since it is often the case that the signal (as opposed to the noise) in a data set is concentrated in its first few principal components. 

---
layout: default
title: "index"
---

# Uniqueness of the Principal Components 

While in theory the principal components need not be unique, in almost all practical settings they are (up to sign flips). This means that two different software packages will yield the same principal component loading vectors, although the signs of those loading vectors may differ. The signs may differ because each principal component loading vector specifies a direction in _p_ - dimensional space: flipping the sign has no effect as the direction does not change. (Consider Figure 6.14—the principal component loading vector is a line that extends in either direction, and flipping its sign would have no effect.) Similarly, the score vectors are unique up to a sign flip, since the variance of _Z_ is the same as the variance of _−Z_ . It is worth noting that when we use (12.5) to approximate _xij_ we multiply _zim_ by _φjm_ . Hence, if the sign is flipped on both the loading and score vectors, the final product of the two quantities is unchanged. 

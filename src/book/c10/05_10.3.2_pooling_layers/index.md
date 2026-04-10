---
layout: default
title: "index"
---

# _10.3.2 Pooling Layers_ 

A _pooling_ layer provides a way to condense a large image into a smaller pooling summary image. While there are a number of possible ways to perform pooling, the _max pooling_ operation summarizes each non-overlapping 2 _×_ 2 block of pixels in an image using the maximum value in the block. This reduces the size of the image by a factor of two in each direction, and it also provides some _location invariance_ : i.e. as long as there is a large value in one of the four pixels in the block, the whole block registers as a large value in the reduced image. 

Here is a simple example of max pooling:

$$
\begin{pmatrix} 1 & 2 & 5 & 3 \\ 4 & 5 & 1 & 2 \\ 3 & 4 & 6 & 1 \\ 1 & 2 & 3 & 4 \end{pmatrix} \xrightarrow{\quad \text{max pool} \quad} \begin{pmatrix} 5 & 5 \\ 4 & 6 \end{pmatrix}
$$

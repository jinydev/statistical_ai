---
layout: default
title: "index"
---

# _10.3.4 Data Augmentation_ 

An additional important trick used with image modeling is _data augment-_ data aug- _ation_ . Essentially, each training image is replicated many times, with each mentation replicate randomly distorted in a natural way such that human recognition is unaffected. Figure 10.9 shows some examples. Typical distortions are 

mentation 

412 10. Deep Learning 

**FIGURE 10.9.** _Data augmentation. The original image (leftmost) is distorted in natural ways to produce different images with the same class label. These distortions do not fool humans, and act as a form of regularization when fitting the CNN._ 

zoom, horizontal and vertical shift, shear, small rotations, and in this case horizontal flips. At face value this is a way of increasing the training set considerably with somewhat different examples, and thus protects against overfitting. In fact we can see this as a form of regularization: we build a cloud of images around each original image, all with the same label. This kind of fattening of the data is similar in spirit to ridge regularization. 

We will see in Section 10.7.2 that the stochastic gradient descent algorithms for fitting deep learning models repeatedly process randomlyselected batches of, say, 128 training images at a time. This works hand-inglove with augmentation, because we can distort each image in the batch on the fly, and hence do not have to store all the new images. 

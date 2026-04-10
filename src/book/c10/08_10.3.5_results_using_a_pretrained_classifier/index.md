---
layout: default
title: "index"
---

# _10.3.5 Results Using a Pretrained Classifier_ 

Here we use an industry-level pretrained classifier to predict the class of some new images. The `resnet50` classifier is a convolutional neural network that was trained using the `imagenet` data set, which consists of millions of images that belong to an ever-growing number of categories.[10] Figure 10.10 demonstrates the performance of `resnet50` on six photographs (private collection of one of the authors).[11] The CNN does a reasonable job classifying the hawk in the second image. If we zoom out as in the third image, it gets confused and chooses the fountain rather than the hawk. In the final image a “jacamar” is a tropical bird from South and Central America with similar coloring to the South African Cape Weaver. We give more details on this example in Section 10.9.4. 

Much of the work in fitting a CNN is in learning the convolution filters at the hidden layers; these are the coefficients of a CNN. For models fit to massive corpora such as `imagenet` with many classes, the output of these filters can serve as features for general natural-image classification problems. One can use these pretrained hidden layers for new problems with much smaller training sets (a process referred to as _weight freezing_ ), and weight just train the last few layers of the network, which requires much less data. 

> freezing 

> 10For more information about `resnet50` , see He, Zhang, Ren, and Sun (2015) “Deep residual learning for image recognition”, `https://arxiv.org/abs/1512.03385` . For details about `imagenet` , see Russakovsky, Deng, et al. (2015) “ImageNet Large Scale Visual Recognition Challenge”, in _International Journal of Computer Vision_ . 

> 11These `resnet` results can change with time, since the publicly-trained model gets updated periodically. 

10.4 Document Classification 413 

|||y|y|T|‘ le|~\|
|---|---|---|---|---|---|---|
|flamingo<br>flamingo|0.83|Cooper’s hawk<br>kite||0.60|Cooper’s <br>fountain|hawk<br>0.35|
|spoonbill|0.17|great grey owl||0.09|nail|0.12|
|white stork|0.00|robin||0.06|hook|0.07|
|Lhasa Apso|||cat||Cape weaver||
|Tibetan terrier|0.56|Old English|sheepdog|0.82|jacamar|0.28|
|Lhasa|0.32|Shih-Tzu||0.04|macaw|0.12|
|cocker spaniel|0.03|Persian cat||0.04|robin|0.12|



**FIGURE 10.10.** _Classification of six photographs using the_ `resnet50` _CNN trained on the_ `imagenet` _corpus. The table below the images displays the true (intended) label at the top of each panel, and the top three choices of the classifier (out of 100). The numbers are the estimated probabilities for each choice. (A kite is a raptor, but not a hawk.)_ 

The vignettes and book[12] that accompany the `keras` package give more details on such applications. 

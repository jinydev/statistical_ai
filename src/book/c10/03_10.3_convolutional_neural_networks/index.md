---
layout: default
title: "index"
---

# 10.3 Convolutional Neural Networks 

Neural networks rebounded around 2010 with big successes in image classification. Around that time, massive databases of labeled images were being accumulated, with ever-increasing numbers of classes. Figure 10.5 shows 75 images drawn from the `CIFAR100` database.[4] This database consists of 60,000 images labeled according to 20 superclasses (e.g. aquatic mammals), with five classes per superclass (beaver, dolphin, otter, seal, whale). Each image has a resolution of 32 _×_ 32 pixels, with three eight-bit numbers per pixel representing red, green and blue. The numbers for each image are organized in a three-dimensional array called a _feature map_ . The first two feature map 

> 4See Chapter 3 of Krizhevsky (2009) “Learning multiple layers of features from tiny images”, available at `https://www.cs.toronto.edu/~kriz/ learning-features-2009-TR.pdf` . 

10.3 Convolutional Neural Networks 407 

**FIGURE 10.6.** _Schematic showing how a convolutional neural network classifies an image of a tiger. The network takes in the image and identifies local features. It then combines the local features in order to create compound features, which in this example include eyes and ears. These compound features are used to output the label “tiger”._ 

axes are spatial (both are 32-dimensional), and the third is the _channel_ channel axis,[5] representing the three colors. There is a designated training set of 50,000 images, and a test set of 10,000. 

A special family of _convolutional neural networks_ (CNNs) has evolved for convolutional classifying images such as these, and has shown spectacular success on a neural wide range of problems. CNNs mimic to some degree how humans classify networks images, by recognizing specific features or patterns anywhere in the image that distinguish each particular object class. In this section we give a brief overview of how they work. 

Figure 10.6 illustrates the idea behind a convolutional neural network on a cartoon image of a tiger.[6] 

The network first identifies low-level features in the input image, such as small edges, patches of color, and the like. These low-level features are then combined to form higher-level features, such as parts of ears, eyes, and so on. Eventually, the presence or absence of these higher-level features contributes to the probability of any given output class. 

How does a convolutional neural network build up this hierarchy? It combines two specialized types of hidden layers, called _convolution_ layers and _pooling_ layers. Convolution layers search for instances of small patterns in the image, whereas pooling layers downsample these to select a prominent subset. In order to achieve state-of-the-art results, contemporary neuralnetwork architectures make use of many convolution and pooling layers. We describe convolution and pooling layers next. 

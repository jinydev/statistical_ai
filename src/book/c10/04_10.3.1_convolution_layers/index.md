---
layout: default
title: "index"
---

# _10.3.1 Convolution Layers_ 

A _convolution layer_ is made up of a large number of _convolution filters_ , each convolution 

> 5The term _channel_ is taken from the signal-processing literature. Each channel is a distinct source of information. 

> 6 Thanks to Elena Tuzhilina for producing the diagram and `https://www. cartooning4kids.com/` for permission to use the cartoon tiger. 

layer convolution filter 

408 10. Deep Learning 

of which is a template that determines whether a particular local feature is present in an image. A convolution filter relies on a very simple operation, called a _convolution_ , which basically amounts to repeatedly multiplying matrix elements and then adding the results. 

To understand how a convolution filter works, consider a very simple example of a 4 _×_ 3 image:

$$
\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \\ j & k & l \end{pmatrix}
$$

Now consider a 2 _×_ 2 filter of the form

$$
\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}
$$

When we _convolve_ the image with the filter, we get the result[7] 

$$
\begin{pmatrix} a\alpha+b\beta+d\gamma+e\delta & b\alpha+c\beta+e\gamma+f\delta \\ d\alpha+e\beta+g\gamma+h\delta & e\alpha+f\beta+h\gamma+i\delta \\ g\alpha+h\beta+j\gamma+k\delta & h\alpha+i\beta+k\gamma+l\delta \end{pmatrix}
$$


For instance, the top-left element comes from multiplying each element in the 2 _×_ 2 filter by the corresponding element in the top left 2 _×_ 2 portion of the image, and adding the results. The other elements are obtained in a similar way: the convolution filter is applied to every 2 _×_ 2 submatrix of the original image in order to obtain the convolved image. If a 2 _×_ 2 submatrix of the original image resembles the convolution filter, then it will have a _large_ value in the convolved image; otherwise, it will have a _small_ value. Thus, _the convolved image highlights regions of the original image that resemble the convolution filter._ We have used 2 _×_ 2 as an example; in general convolution filters are small _ℓ_ 1 _× ℓ_ 2 arrays, with _ℓ_ 1 and _ℓ_ 2 small positive integers that are not necessarily equal. 

Figure 10.7 illustrates the application of two convolution filters to a 192 _×_ 179 image of a tiger, shown on the left-hand side.[8] Each convolution filter is a 15 _×_ 15 image containing mostly zeros (black), with a narrow strip of ones (white) oriented either vertically or horizontally within the image. When each filter is convolved with the image of the tiger, areas of the tiger that resemble the filter (i.e. that have either horizontal or vertical stripes or edges) are given large values, and areas of the tiger that do not resemble the feature are given small values. The convolved images are displayed on the right-hand side. We see that the horizontal stripe filter picks out horizontal stripes and edges in the original image, whereas the vertical stripe filter picks out vertical stripes and edges in the original image. 

> 7The convolved image is smaller than the original image because its dimension is given by the number of 2 _×_ 2 submatrices in the original image. Note that 2 _×_ 2 is the dimension of the convolution filter. If we want the convolved image to have the same dimension as the original image, then padding can be applied. 

> 8The tiger image used in Figures 10.7–10.9 was obtained from the public domain image resource `https://www.needpix.com/` . 

10.3 Convolutional Neural Networks 409 

**FIGURE 10.7.** _Convolution filters find local features in an image, such as edges and small shapes. We begin with the image of the tiger shown on the left, and apply the two small convolution filters in the middle. The convolved images highlight areas in the original image where details similar to the filters are found. Specifically, the top convolved image highlights the tiger’s vertical stripes, whereas the bottom convolved image highlights the tiger’s horizontal stripes. We can think of the original image as the input layer in a convolutional neural network, and the convolved images as the units in the first hidden layer._ 

We have used a large image and two large filters in Figure 10.7 for illustration. For the `CIFAR100` database there are 32 _×_ 32 color pixels per image, and we use 3 _×_ 3 convolution filters. 

In a convolution layer, we use a whole bank of filters to pick out a variety of differently-oriented edges and shapes in the image. Using predefined filters in this way is standard practice in image processing. By contrast, with CNNs the filters are _learned_ for the specific classification task. We can think of the filter weights as the parameters going from an input layer to a hidden layer, with one hidden unit for each pixel in the convolved image. This is in fact the case, though the parameters are highly structured and constrained (see Exercise 4 for more details). They operate on localized patches in the input image (so there are many structural zeros), and the same weights in a given filter are reused for all possible patches in the image (so the weights are constrained).[9] 

We now give some additional details. 

- Since the input image is in color, it has three channels represented by a three-dimensional feature map (array). Each channel is a twodimensional (32 _×_ 32) feature map — one for red, one for green, and one for blue. A single convolution filter will also have three channels, one per color, each of dimension 3 _×_ 3, with potentially different filter weights. The results of the three convolutions are summed to form a two-dimensional output feature map. Note that at this point the color information has been used, and is not passed on to subsequent layers except through its role in the convolution. 

- 9This used to be called _weight sharing_ in the early years of neural networks. 

10. Deep Learning 

410 

- If we use _K_ different convolution filters at this first hidden layer, we get _K_ two-dimensional output feature maps, which together are treated as a single three-dimensional feature map. We view each of the _K_ output feature maps as a separate channel of information, so now we have _K_ channels in contrast to the three color channels of the original input feature map. The three-dimensional feature map is just like the activations in a hidden layer of a simple neural network, except organized and produced in a spatially structured way. 

- We typically apply the ReLU activation function (10.5) to the convolved image. This step is sometimes viewed as a separate layer in the convolutional neural network, in which case it is referred to as a _detector layer_ . 

detector layer 

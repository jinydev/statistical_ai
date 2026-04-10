---
layout: default
title: "index"
---

# 10.5 Recurrent Neural Networks 

Many data sources are sequential in nature, and call for special treatment when building predictive models. Examples include: 

- Documents such as book and movie reviews, newspaper articles, and tweets. The sequence and relative positions of words in a document capture the narrative, theme and tone, and can be exploited in tasks such as topic classification, sentiment analysis, and language translation. 

- Time series of temperature, rainfall, wind speed, air quality, and so on. We may want to forecast the weather several days ahead, or climate several decades ahead. 

- Financial time series, where we track market indices, trading volumes, stock and bond prices, and exchange rates. Here prediction is often difficult, but as we will see, certain indices can be predicted with reasonable accuracy. 

- Recorded speech, musical recordings, and other sound recordings. We may want to give a text transcription of a speech, or perhaps a language translation. We may want to assess the quality of a piece of music, or assign certain attributes. 

- Handwriting, such as doctor’s notes, and handwritten digits such as zip codes. Here we want to turn the handwriting into digital text, or read the digits (optical character recognition). 

In a _recurrent neural network_ (RNN), the input object _X_ is a _sequence_ . recurrent Consider a corpus of documents, such as the collection of `IMDb` movie reneural views. Each document can be represented as a sequence of _L_ words, so network _X_ = _{X_ 1 _, X_ 2 _, . . . , XL}_ , where each _Xℓ_ represents a word. The order of the words, and closeness of certain words in a sentence, convey semantic meaning. RNNs are designed to accommodate and take advantage of the sequential nature of such input objects, much like convolutional neural networks accommodate the spatial structure of image inputs. The output _Y_ can also be a sequence (such as in language translation), but often is a scalar, like the binary sentiment label of a movie review document. 

10.5 Recurrent Neural Networks 417 

![Figure 10.12](./img/10_12.png)

**FIGURE 10.12.** _Schematic of a simple recurrent neural network. The input is a sequence of vectors {Xℓ}_ 1 _[L][,][and][here][the][target][is][a][single][response.][The][network] processes the input sequence X sequentially; each Xℓ feeds into the hidden layer, which also has as input the activation vector Aℓ−_ 1 _from the previous element in the sequence, and produces the current activation vector Aℓ. The same collections of weights_ **W** _,_ **U** _and_ **B** _are used as each element of the sequence is processed. The output layer produces a sequence of predictions Oℓ from the current activation Aℓ, but typically only the last of these, OL, is of relevance. To the left of the equal sign is a concise representation of the network, which is_ unrolled _into a more explicit version on the right._ 

Figure 10.12 illustrates the structure of a very basic RNN with a sequence _X_ = _{X_ 1 _, X_ 2 _, . . . , XL}_ as input, a simple output _Y_ , and a hidden-layer sequence _{Aℓ}_ 1 _[L]_[=] _[ {][A]_[1] _[, A]_[2] _[, . . . , A][L][}]_[.][Each] _[X][ℓ]_[is][a][vector;][in][the][document] example _Xℓ_ could represent a one-hot encoding for the _ℓ_ th word based on the language dictionary for the corpus (see the top panel in Figure 10.13 for a simple example). As the sequence is processed one vector _Xℓ_ at a time, the network updates the activations _Aℓ_ in the hidden layer, taking as input the vector _Xℓ_ and the activation vector _Aℓ−_ 1 from the previous step in the sequence. Each _Aℓ_ feeds into the output layer and produces a prediction _Oℓ_ for _Y_ . _OL_ , the last of these, is the most relevant. 

In detail, suppose each vector _Xℓ_ of the input sequence has _p_ components _Xℓ[T]_[=][(] _[X][ℓ]_[1] _[, X][ℓ]_[2] _[, . . . , X][ℓp]_[)][,][and][the][hidden][layer][consists][of] _[K]_[units] _[A][T] ℓ_[=] ( _Aℓ_ 1 _, Aℓ_ 2 _, . . . , AℓK_ ). As in Figure 10.4, we represent the collection of _K ×_ ( _p_ +1) shared weights _wkj_ for the input layer by a matrix **W** , and similarly **U** is a _K × K_ matrix of the weights _uks_ for the hidden-to-hidden layers, and **B** is a _K_ + 1 vector of weights _βk_ for the output layer. Then

$$
A^{(L)} = g(\mathbf{W}_L A^{(L-1)} + \mathbf{b}_L)
$$

and the output _Oℓ_ is computed as 

$$
f_m(X) = \beta_{m0} + \sum_{k=1}^K \beta_{mk} A_k^{(L)}
$$

for a quantitative response, or with an additional sigmoid activation function for a binary response, for example. Here _g_ ( _·_ ) is an activation function such as ReLU. Notice that the same weights **W** , **U** and **B** are used as we 

418 10. Deep Learning 

process each element in the sequence, i.e. they are not functions of _ℓ_ . This is a form of _weight sharing_ used by RNNs, and similar to the use of filters weight in convolutional neural networks (Section 10.3.1.) As we proceed from besharing ginning to end, the activations _Aℓ_ accumulate a history of what has been seen before, so that the learned context can be used for prediction. 

sharing 

For regression problems the loss function for an observation ( _X, Y_ ) is 

$$
\frac{1}{2}(Y - f(X))^2
$$

which only references the final output _OL_ = _β_ 0+[�] _[K] k_ =1 _[β][k][A][Lk]_[. Thus] _[ O]_[1] _[, O]_[2] _[,] . . . , OL−_ 1 are not used. When we fit the model, each element _Xℓ_ of the input sequence _X_ contributes to _OL_ via the chain (10.16), and hence contributes indirectly to learning the shared parameters **W** , **U** and **B** via the loss (10.18). With _n_ input sequence/response pairs ( _xi, yi_ ) _,_ the parameters are found by minimizing the sum of squares 

$$
\sum_{i=1}^n \|y_i - f(x_i)\|^2
$$

Here we use lowercase letters for the observed _yi_ and vector sequences _xi_ = _{xi_ 1 _, xi_ 2 _, . . . , xiL}_ ,[15] as well as the derived activations. 

Since the intermediate outputs _Oℓ_ are not used, one may well ask why they are there at all. First of all, they come for free, since they use the same output weights **B** needed to produce _OL_ , and provide an evolving prediction for the output. Furthermore, for some learning tasks the response is also a sequence, and so the output sequence _{O_ 1 _, O_ 2 _, . . . , OL}_ is explicitly needed. 

When used at full strength, recurrent neural networks can be quite complex. We illustrate their use in two simple applications. In the first, we continue with the `IMDb` sentiment analysis of the previous section, where we process the words in the reviews sequentially. In the second application, we illustrate their use in a financial time series forecasting problem. 

---
layout: default
title: "index"
---

# _10.5.1 Sequential Models for Document Classification_ 

Here we return to our classification task with the `IMDb` reviews. Our approach in Section 10.4 was to use the bag-of-words model. Here the plan is to use instead the sequence of words occurring in a document to make predictions about the label for the entire document. 

We have, however, a dimensionality problem: each word in our document is represented by a one-hot-encoded vector (dummy variable) with 10,000 elements (one per word in the dictionary)! An approach that has become popular is to represent each word in a much lower-dimensional _embedding_ embedding space. This means that rather than representing each word by a binary vector with 9,999 zeros and a single one in some position, we will represent it instead by a set of _m_ real numbers, none of which are typically zero. Here _m_ is the embedding dimension, and can be in the low 100s, or even less. This means (in our case) that we need a matrix **E** of dimension _m ×_ 10 _,_ 000, 

> 15This is a sequence of vectors; each element _xiℓ_ is a _p_ -vector. 

10.5 Recurrent Neural Networks 419 

![Figure 10.13](./img/10_13.png)

**FIGURE 10.13.** _Depiction of a sequence of_ 20 _words representing a single document: one-hot encoded using a dictionary of_ 16 _words (top panel) and embedded in an m-dimensional space with m_ = 5 _(bottom panel)._ 

where each column is indexed by one of the 10,000 words in our dictionary, and the values in that column give the _m_ coordinates for that word in the embedding space. 

Figure 10.13 illustrates the idea (with a dictionary of 16 rather than 10,000, and _m_ = 5). Where does **E** come from? If we have a large corpus of labeled documents, we can have the neural network _learn_ **E** as part of the optimization. In this case **E** is referred to as an _embedding layer,_ embedding and a specialized **E** is learned for the task at hand. Otherwise we can layer insert a precomputed matrix **E** in the embedding layer, a process known as _weight freezing_ . Two pretrained embeddings, `word2vec` and `GloVe` , are weight widely used.[16] These are built from a very large corpus of documents by freezing a variant of principal components analysis (Section 12.2). The idea is that `word2vec` the positions of words in the embedding space preserve semantic meaning; `GloVe` e.g. synonyms should appear near each other. 

So far, so good. Each document is now represented as a sequence of _m_ - vectors that represents the sequence of words. The next step is to limit each document to the last _L_ words. Documents that are shorter than _L_ get padded with zeros upfront. So now each document is represented by a series consisting of _L_ vectors _X_ = _{X_ 1 _, X_ 2 _, . . . , XL}_ , and each _Xℓ_ in the sequence has _m_ components. 

We now use the RNN structure in Figure 10.12. The training corpus consists of _n_ separate series (documents) of length _L_ , each of which gets processed sequentially from left to right. In the process, a parallel series of hidden activation vectors _Aℓ, ℓ_ = 1 _, . . . , L_ is created as in (10.16) for each document. _Aℓ_ feeds into the output layer to produce the evolving prediction _Oℓ_ . We use the final value _OL_ to predict the response: the sentiment of the review. 

> 16 `word2vec` is described in Mikolov, Chen, Corrado, and Dean (2013), available at `https://code.google.com/archive/p/word2vec` . `GloVe` is described in Pennington, Socher, and Manning (2014), available at `https://nlp.stanford.edu/projects/glove` . 

420 10. Deep Learning 

This is a simple RNN, and has relatively few parameters. If there are _K_ hidden units, the common weight matrix **W** has _K ×_ ( _m_ + 1) parameters, the matrix **U** has _K × K_ parameters, and **B** has 2( _K_ + 1) for the two-class logistic regression as in (10.15). These are used repeatedly as we process the sequence _X_ = _{Xℓ}_ 1 _[L]_[from][left][to][right,][much][like][we][use][a][single] convolution filter to process each patch in an image (Section 10.3.1). If the embedding layer **E** is learned, that adds an additional _m × D_ parameters ( _D_ = 10 _,_ 000 here), and is by far the biggest cost. 

We fit the RNN as described in Figure 10.12 and the accompaying text to the `IMDb` data. The model had an embedding matrix **E** with _m_ = 32 (which was learned in training as opposed to precomputed), followed by a single recurrent layer with _K_ = 32 hidden units. The model was trained with dropout regularization on the 25,000 reviews in the designated training set, and achieved a disappointing 76% accuracy on the `IMDb` test data. A network using the `GloVe` pretrained embedding matrix **E** performed slightly worse. 

For ease of exposition we have presented a very simple RNN. More elaborate versions use _long term_ and _short term_ memory (LSTM). Two tracks of hidden-layer activations are maintained, so that when the activation _Aℓ_ is computed, it gets input from hidden units both further back in time, and closer in time — a so-called _LSTM RNN_ . With long sequences, this LSTM RNN overcomes the problem of early signals being washed out by the time they get propagated through the chain to the final activation vector _AL_ . 

When we refit our model using the LSTM architecture for the hidden layer, the performance improved to 87% on the `IMDb` test data. This is comparable with the 88% achieved by the bag-of-words model in Section 10.4. We give details on fitting these models in Section 10.9.6. 

Despite this added LSTM complexity, our RNN is still somewhat “entry level”. We could probably achieve slightly better results by changing the size of the model, changing the regularization, and including additional hidden layers. However, LSTM models take a long time to train, which makes exploring many architectures and parameter optimization tedious. 

RNNs provide a rich framework for modeling data sequences, and they continue to evolve. There have been many advances in the development of RNNs — in architecture, data augmentation, and in the learning algorithms. At the time of this writing (early 2020) the leading RNN configurations report accuracy above 95% on the `IMDb` data. The details are beyond the scope of this book.[17] 

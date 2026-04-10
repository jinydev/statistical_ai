---
layout: default
title: "index"
---

# _10.5.3 Summary of RNNs_ 

We have illustrated RNNs through two simple use cases, and have only scratched the surface. 

There are many variations and enhancements of the simple RNN we used for sequence modeling. One approach we did not discuss uses a onedimensional convolutional neural network, treating the sequence of vectors (say words, as represented in the embedding space) as an image. The convolution filter slides along the sequence in a one-dimensional fashion, with the potential to learn particular phrases or short subsequences relevant to the learning task. 

One can also have additional hidden layers in an RNN. For example, with two hidden layers, the sequence _Aℓ_ is treated as an input sequence to the next hidden layer in an obvious fashion. 

10.6 When to Use Deep Learning 425 

The RNN we used scanned the document from beginning to end; alternative _bidirectional_ RNNs scan the sequences in both directions. 

bidirectional 

In language translation the target is also a sequence of words, in a language different from that of the input sequence. Both the input sequence and the target sequence are represented by a structure similar to Figure 10.12, and they share the hidden units. In this so-called _Seq2Seq_ Seq2Seq learning, the hidden units are thought to capture the semantic meaning of the sentences. Some of the big breakthroughs in language modeling and translation resulted from the relatively recent improvements in such RNNs. 

Algorithms used to fit RNNs can be complex and computationally costly. Fortunately, good software protects users somewhat from these complexities, and makes specifying and fitting these models relatively painless. Many of the models that we enjoy in daily life (like _Google Translate_ ) use stateof-the-art architectures developed by teams of highly skilled engineers, and have been trained using massive computational and data resources. 

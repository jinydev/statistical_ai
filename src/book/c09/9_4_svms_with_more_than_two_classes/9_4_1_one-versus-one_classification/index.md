---
layout: default
title: "index"
---

# _9.4.1 One-Versus-One Classification_ 

Suppose that we would like to perform classification using SVMs, and there are _K >_ 2 classes. A _one-versus-one_ or _all-pairs_ approach constructs _K_ 2 one-versusSVMs, each of which compares a pair of classes. For example, one c one SVM might compare the _k_ th class, coded as +1, to the _k[′]_ th class, coded as _−_ 1. We classify a test observation using each of the _K_ 2 classifiers, and we tally the number of times that the test observation ssigned to each of the _K_ classes. The final classification is performed by assigning the test observation to the class to which it was most frequently assigned in these _K_ 2 pairwise classifications. 

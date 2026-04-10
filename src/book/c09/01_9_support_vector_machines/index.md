---
layout: default
title: "index"
---

# 9 Support Vector Machines 

In this chapter, we discuss the _support vector machine_ (SVM), an approach for classification that was developed in the computer science community in the 1990s and that has grown in popularity since then. SVMs have been shown to perform well in a variety of settings, and are often considered one of the best “out of the box” classifiers. 

The support vector machine is a generalization of a simple and intuitive classifier called the _maximal margin classifier_ , which we introduce in Section 9.1. Though it is elegant and simple, we will see that this classifier unfortunately cannot be applied to most data sets, since it requires that the classes be separable by a linear boundary. In Section 9.2, we introduce the _support vector classifier_ , an extension of the maximal margin classifier that can be applied in a broader range of cases. Section 9.3 introduces the _support vector machine_ , which is a further extension of the support vector classifier in order to accommodate non-linear class boundaries. Support vector machines are intended for the binary classification setting in which there are two classes; in Section 9.4 we discuss extensions of support vector machines to the case of more than two classes. In Section 9.5 we discuss the close connections between support vector machines and other statistical methods such as logistic regression. 

People often loosely refer to the maximal margin classifier, the support vector classifier, and the support vector machine as “support vector machines”. To avoid confusion, we will carefully distinguish between these three notions in this chapter. 

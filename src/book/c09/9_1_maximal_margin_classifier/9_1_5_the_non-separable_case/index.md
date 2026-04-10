---
layout: default
title: "index"
---

# _9.1.5 The Non-separable Case_ 

The maximal margin classifier is a very natural way to perform classification, _if a separating hyperplane exists_ . However, as we have hinted, in many cases no separating hyperplane exists, and so there is no maximal 

9.2 Support Vector Classifiers 373 

![Figure 9.4](./img/9_4.png)

**FIGURE 9.4.** _There are two classes of observations, shown in blue and in purple. In this case, the two classes are not separable by a hyperplane, and so the maximal margin classifier cannot be used._ 

margin classifier. In this case, the optimization problem (9.9)–(9.11) has no solution with _M >_ 0. An example is shown in Figure 9.4. In this case, we cannot _exactly_ separate the two classes. However, as we will see in the next section, we can extend the concept of a separating hyperplane in order to develop a hyperplane that _almost_ separates the classes, using a so-called _soft margin_ . The generalization of the maximal margin classifier to the non-separable case is known as the _support vector classifier_ . 

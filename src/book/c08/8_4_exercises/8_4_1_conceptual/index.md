---
layout: default
title: "index"
---

# _Conceptual_ 

1. Draw an example (of your own invention) of a partition of twodimensional feature space that could result from recursive binary splitting. Your example should contain at least six regions. Draw a decision tree corresponding to this partition. Be sure to label all aspects of your figures, including the regions _R_ 1 _, R_ 2 _, . . ._ , the cutpoints _t_ 1 _, t_ 2 _, . . ._ , and so forth. 

_Hint: Your result should look something like Figures 8.1 and 8.2._ 

2. It is mentioned in Section 8.2.3 that boosting using depth-one trees (or _stumps_ ) leads to an _additive_ model: that is, a model of the form

$$
f(X) = \sum_{j=1}^p f_j(X_j)
$$

Explain why this is the case. You can begin with (8.12) in Algorithm 8.2. 

3. Consider the Gini index, classification error, and entropy in a simple classification setting with two classes. Create a single plot that displays each of these quantities as a function of _p_ ˆ _m_ 1. The _x_ -axis should display _p_ ˆ _m_ 1, ranging from 0 to 1, and the _y_ -axis should display the value of the Gini index, classification error, and entropy. 

   - ˆ ˆ 

   - _Hint: In a setting with two classes, pm_ 1 = 1 _− pm_ 2 _. You could make this plot by hand, but it will be much easier to make in_ `R` _._ 

4. This question relates to the plots in Figure 8.14. 

364 8. Tree-Based Methods 

   - (b) Create a diagram similar to the left-hand panel of Figure 8.14, using the tree illustrated in the right-hand panel of the same figure. You should divide up the predictor space into the correct regions, and indicate the mean for each region. 

5. Suppose we produce ten bootstrapped samples from a data set containing red and green classes. We then apply a classification tree to each bootstrapped sample and, for a specific value of _X_ , produce 10 estimates of _P_ (Class is Red _|X_ ): 

0 _._ 1 _,_ 0 _._ 15 _,_ 0 _._ 2 _,_ 0 _._ 2 _,_ 0 _._ 55 _,_ 0 _._ 6 _,_ 0 _._ 6 _,_ 0 _._ 65 _,_ 0 _._ 7 _,_ and 0 _._ 75 _._ 

There are two common ways to combine these results together into a single class prediction. One is the majority vote approach discussed in this chapter. The second approach is to classify based on the average probability. In this example, what is the final classification under each of these two approaches? 

6. Provide a detailed explanation of the algorithm that is used to fit a regression tree. 

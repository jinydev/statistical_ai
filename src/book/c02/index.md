---
layout: default
title: "2. Statistical Learning"
---

[2.1 What Is Statistical Learning >](2_1_what_is_statistical_learning/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2. Statistical Learning

This Chapter 2 introduces the main concepts and theoretical foundations of statistical learning in earnest. We will learn about the purpose and methodologies for estimating the function $f$, as well as the variance-bias trade-off, which is the most fundamental issue in machine learning.
## 2.1 What Is Statistical Learning?

We explore the purpose of finding a function $f$ that estimates the relationship between an input variable ($X$) and an output variable ($Y$). You can understand the role of statistical learning based on the two main goals: prediction and inference.
### 2.1.1 Why Estimate f ?

We learn about the prediction-centric reasons for predicting output values for new data points, and the inference-centric reasons for analyzing the effect of each input variable on the output variable.
#### Prediction

We focus on the goal of predicting the value of an unobserved response variable as accurately as possible based on given features. We familiarize ourselves with the limitations of the model by differentiating between reducible error and irreducible error.
### 2.1.2 How Do We Estimate f ?

We introduce approaches to mathematically construct the most appropriate function $f$ utilizing training data. We cover the fundamental differences and working principles of parametric and non-parametric models.
#### Parametric Methods

This is a method that first assumes the shape of the function (e.g., linearity) and fits the model by estimating a limited set of parameters. It has the advantage of being fast to compute and easy to interpret, but it has the disadvantage that the actual shape of the data and the assumed shape can be significantly different.
#### Non-Parametric Methods

These are methodologies that do not make specific assumptions about the shape of the function $f$ and proceed to fit as closely to the data points as possible. We learn that while they can describe data very flexibly, they require a vastly larger amount of data for meaningful analysis.
### 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

We cover the black-box phenomenon, where as a model becomes more flexible and powerful, its internal structure becomes more complex, making cause analysis and interpretation significantly more difficult. We develop the ability to determine the level of flexibility depending on the fundamental purpose of the analysis (high accuracy vs. the need to identify specific causes).
### 2.1.4 Supervised Versus Unsupervised Learning

We point out the difference between supervised learning in an environment where the target label (response) is given, and unsupervised learning, which only identifies structural features. Consequently, the concept of semi-supervised learning, which has a character midway between supervised and unsupervised, is also briefly introduced.
### 2.1.5 Regression Versus Classification Problems

We define a regression situation where the response variable is numerically continuous, and a classification situation where it is discrete and divided qualitatively. We explain that the appropriate algorithms and evaluation metric systems must be fundamentally different for each problem type.
## 2.2 Assessing Model Accuracy

Since no single methodology can be universal, we learn the criteria to quantitatively compare models on a given specific dataset. We learn the causes of the gap between the training error during the learning phase and the test error in practice.
### 2.2.1 Measuring the Quality of Fit

We explain the Mean Squared Error (MSE), the most universally used metric when evaluating a model's superiority in a regression environment. We emphasize the importance of generalization, which performs well on unfamiliar test data, rather than just simply fitting the training data well.
### 2.2.2 The Bias-Variance Trade-Off

We deal with the complex correlation between bias and variance, which are the essential components that make up the error on test data. We mathematically explore the U-shaped validation curve (U-Shape) where as the flexibility of the model increases, variance grows and bias gradually decreases.
### 2.2.3 The Classification Setting

We introduce the error rate, a ratio metric used to compare performance in a model environment where discrete class outcomes must be predicted. We learn about the Bayes error rate, which defines the lowest limit by performing optimal predictions within a given data space.
#### K-Nearest Neighbors

We learn about the K-Nearest Neighbors (KNN) technique, which is the most intuitive algorithm as an actual implementation of theory in a non-parametric classification environment. We learn how the decision boundary changes according to the change in the K value, and how the bias-variance trade-off appears during that process.
## 2.3 Lab: Introduction to Python

We introduce the basic Python environment for data analysis and visualization as a programming foundation to proceed with the entire course. We comprehensively check the Python ecosystem and the structure of essential libraries such as NumPy, Pandas, and Matplotlib.
### 2.3.1 Getting Started

We cover essential setup structures for starting Python, such as the Jupyter environment and package installation methods. You can understand the default interpreter path that will serve as the basecamp for analysis.
### 2.3.2 Basic Commands

We quickly scan through very basic essential commands at the shell level, such as outputting to the console, allocating data, and returning lengths. You can examine basic Python data type structures like strings or lists and their compatibility.
### 2.3.3 Introduction to Numerical Python

This is a guide on how to use the NumPy package, the core foundation that enables powerful and fast computation of multi-dimensional data arrays (Array/Matrix). We take time to get accustomed to specifying random seeds and generating random numbers.
### 2.3.4 Graphics

We bring in Matplotlib capabilities to visualize complex data trends like scatter plots and contour plots in the form of charts. We learn the technique of intuitively capturing information structures, correlations, and distribution patterns through graphs.
### 2.3.5 Sequences and Slice Notation

We deal with indexing techniques that directly access elements inside Python's matrix objects or separate only a specific sequence interval. We aim for grammatical mastery in dividing and combining huge chunks of data into necessary sequences.
### 2.3.6 Indexing Data

This is a technique to not only manually specify the index of the desired range, but also filter by combining the results of logical truth values (Boolean). We practice specifying filter conditions to weed out only the information with specific conditions from a massive dataframe.
### 2.3.7 Loading Data

We learn how to actually load external data into a DataFrame in the Python environment using Pandas' `read_csv` syntax. It is an elementary process of importing and viewing initial data, checking for and handling non-existent Null values, etc.
### 2.3.8 For Loops

We learn block processing techniques, which are basic control statements that must be used when writing repetitive analysis pipelines or scripts. We approach it with comparative grammar in preparation for using list comprehensions and vector operations.
### 2.3.9 Additional Graphical and Numerical Summaries

We learn everything from numeric summaries like `describe` to capture all data at a glance, to additional graphical techniques like histograms and box plots. By understanding the location and dispersion of the entire dataset like the back of your hand, it adds momentum to future feature engineering execution.
## 2.4 Exercises

This is a practice course where you can check the bias-variance structure, phenomena caused by learning model flexibility, etc., which were covered in depth in Chapter 2. We test both mathematical limitation understanding and applicative power through Conceptual and Applied problems.

---

## Sub-Chapters


[2.1 What Is Statistical Learning >](2_1_what_is_statistical_learning/index.html)

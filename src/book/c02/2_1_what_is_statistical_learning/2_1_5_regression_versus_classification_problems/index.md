---
layout: default
title: "index"
---

[< 2.1.4 Supervised Versus Unsupervised Learning](../2_1_4_supervised_versus_unsupervised_learning/index.html) | [2.2 Assessing Model Accuracy >](../../2_2_assessing_model_accuracy/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2.1.5 Regression Versus Classification Problems_

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_). Quantitative variables take on numerical values. Examples include a person's age, height, or income, the value of a house, and the price of a stock. In contrast, qualitative variables take on values in one of _K_ different _classes_, or categories. Examples of qualitative variables include a person's marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

However, the distinction is not always that crisp.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

Thus, despite its name, logistic regression is a classification method.

But since it estimates class probabilities, it can be thought of as a regression method as well.

Some statistical methods, such as _K_-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

This is discussed in Chapter 3.

---

## Sub-Chapters


[< 2.1.4 Supervised Versus Unsupervised Learning](../2_1_4_supervised_versus_unsupervised_learning/index.html) | [2.2 Assessing Model Accuracy >](../../2_2_assessing_model_accuracy/index.html)

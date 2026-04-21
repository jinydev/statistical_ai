---
layout: default
title: "index"
---

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/index.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.5.2 An Empirical Comparison

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN. We generated data from six different scenarios, each of which involves a binary (two-class) classification problem. In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. The results are summarized below:

- **Scenario 1 (Linear boundary, independent normal variables):** LDA performed well as expected. Logistic regression also performed well. KNN performed poorly because it suffered from variance. QDA performed worse than LDA since it was more flexible than necessary. Naive Bayes was slightly better than QDA because the assumption of independent predictors was correct.
- **Scenario 2 (Linear boundary, correlated variables):** Similar to Scenario 1, except naive Bayes performed very poorly because its independence assumption was completely violated by the correlated predictors.
- **Scenario 3 (Linear boundary, t-distribution):** Outliers were present. Logistic regression outperformed LDA since the data departed from the strict normal assumption. QDA deteriorated considerably. Naive Bayes performed very poorly again due to violated assumptions.
- **Scenario 4 (Quadratic boundary, normal distribution with different correlations):** The decision boundary is non-linear. QDA outperformed all the other methods. Naive Bayes performed poorly due to independence violation.
- **Scenario 5 (Highly non-linear boundary):** Both QDA and naive Bayes gave better results than the linear methods (LDA/Logistic). However, the highly flexible KNN-CV method gave the best overall results. Interestingly, KNN with $K=1$ gave the worst results, highlighting the importance of tuning smoothness.
- **Scenario 6 (Non-linear boundary due to unequal variance, extremely small sample size n=6):** Naive Bayes performed phenomenally well because its assumptions held and its variance is low. LDA/Logistic regression performed poorly due to the non-linear true boundary. QDA struggled heavily because it lacked the data size to estimate its high number of parameters, suffering from intense variance. KNN also failed completely due to the lack of training data.

These six examples illustrate that no one method will dominate the others in every situation. When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well. When the boundaries are moderately non-linear, QDA or naive Bayes may give better results. Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior.

---

## Sub-Chapters


[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/index.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/index.html)

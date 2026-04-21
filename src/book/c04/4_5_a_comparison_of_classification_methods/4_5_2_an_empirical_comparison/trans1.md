---
layout: default
title: "trans1"
---

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans1.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.5.2 An Empirical Comparison
# 4.5.2 경험적 비교

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN. We generated data from six different scenarios, each of which involves a binary (two-class) classification problem. In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. The results are summarized below:
이제 우리는 로지스틱 회귀, LDA, QDA, 나이브 베이즈, 그리고 KNN의 _경험적_ (실제적) 성능을 비교합니다. 우리는 여섯 가지 다른 시나리오에서 데이터를 생성했으며, 각 시나리오는 이진(두 클래스) 분류 문제를 포함합니다. 시나리오 중 세 개에서는 베이즈 결정 경계가 선형이고, 나머지 시나리오에서는 비선형입니다. 결과는 아래에 요약되어 있습니다:

- **Scenario 1 (Linear boundary, independent normal variables):** LDA performed well as expected. Logistic regression also performed well. KNN performed poorly because it suffered from variance. QDA performed worse than LDA since it was more flexible than necessary. Naive Bayes was slightly better than QDA because the assumption of independent predictors was correct.
- **시나리오 1 (선형 경계, 독립적인 정규 변수):** 예상대로 LDA가 우수한 성능을 보였습니다. 로지스틱 회귀 역시 우수한 성능을 보였습니다. KNN은 분산(variance)으로 인해 어려움을 겪었기 때문에 성능이 저조했습니다. QDA는 필요 이상으로 유연했기 때문에 LDA보다 성능이 나빴습니다. 나이브 베이즈는 독립적인 예측 변수라는 가정이 옳았기 때문에 QDA보다 약간 더 나았습니다.
- **Scenario 2 (Linear boundary, correlated variables):** Similar to Scenario 1, except naive Bayes performed very poorly because its independence assumption was completely violated by the correlated predictors.
- **시나리오 2 (선형 경계, 상관된 변수):** 시나리오 1과 유사하지만, 상관된 예측 변수들로 인해 독립성 가정이 완전히 위배되었기 때문에 나이브 베이즈의 성능이 매우 저조했습니다.
- **Scenario 3 (Linear boundary, t-distribution):** Outliers were present. Logistic regression outperformed LDA since the data departed from the strict normal assumption. QDA deteriorated considerably. Naive Bayes performed very poorly again due to violated assumptions.
- **시나리오 3 (선형 경계, t-분포):** 특이치(outlier)가 존재했습니다. 데이터가 엄격한 정규성 가정에서 벗어났기 때문에 로지스틱 회귀가 LDA의 성능을 능가했습니다. QDA는 상당히 악화되었습니다. 나이브 베이즈는 가정이 위배되었기 때문에 또다시 매우 저조한 성능을 보였습니다.
- **Scenario 4 (Quadratic boundary, normal distribution with different correlations):** The decision boundary is non-linear. QDA outperformed all the other methods. Naive Bayes performed poorly due to independence violation.
- **시나리오 4 (이차 경계, 서로 다른 상관관계를 가진 정규 분포):** 결정 경계가 비선형적입니다. QDA가 다른 모든 방법의 성능을 능가했습니다. 나이브 베이즈는 독립성 위배로 인해 성능이 저조했습니다.
- **Scenario 5 (Highly non-linear boundary):** Both QDA and naive Bayes gave better results than the linear methods (LDA/Logistic). However, the highly flexible KNN-CV method gave the best overall results. Interestingly, KNN with $K=1$ gave the worst results, highlighting the importance of tuning smoothness.
- **시나리오 5 (고도의 비선형 경계):** QDA와 나이브 베이즈 모두 선형 방법(LDA/로지스틱)보다 더 나은 결과를 제공했습니다. 그러나 매우 유연한 KNN-CV 방법이 전반적으로 최고의 결과를 제공했습니다. 흥미롭게도 $K=1$ 인 KNN은 최악의 결과를 제공하여 평활도(smoothness) 조정의 중요성을 강조했습니다.
- **Scenario 6 (Non-linear boundary due to unequal variance, extremely small sample size n=6):** Naive Bayes performed phenomenally well because its assumptions held and its variance is low. LDA/Logistic regression performed poorly due to the non-linear true boundary. QDA struggled heavily because it lacked the data size to estimate its high number of parameters, suffering from intense variance. KNN also failed completely due to the lack of training data.
- **시나리오 6 (불균등한 분산으로 인한 비선형 경계, 극히 작은 표본 크기 n=6):** 나이브 베이즈는 가정이 성립하고 분산이 낮았기 때문에 경이적으로 우수한 성능을 보였습니다. LDA/로지스틱 회귀는 비선형적인 실제 경계로 인해 성능이 저조했습니다. QDA는 다수의 매개변수를 추정할 데이터 크기가 부족하여 극심한 분산에 시달렸기 때문에 큰 어려움을 겪었습니다. KNN 역시 훈련 데이터 부족으로 완전히 실패했습니다.

These six examples illustrate that no one method will dominate the others in every situation. When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well. When the boundaries are moderately non-linear, QDA or naive Bayes may give better results. Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior.
이 여섯 가지 사례는 어떤 단일 방법도 모든 상황에서 다른 방법들을 지배할 수 없음을 보여줍니다. 실제 결정 경계가 선형일 때, LDA 및 로지스틱 회귀 접근법은 우수한 성능을 발휘하는 경향이 있습니다. 경계가 적당히 비선형적일 때, QDA나 나이브 베이즈가 더 나은 결과를 제공할 수 있습니다. 마지막으로 훨씬 더 복잡한 결정 경계의 경우, KNN과 같은 비모수적 접근법이 우수할 수 있습니다.

---

## Sub-Chapters

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans1.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans1.html)

---
layout: default
title: "trans1"
---

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans1.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.5.2 An Empirical Comparison
# 4.5.2 경험적 비교

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN.
우리는 이제 로지스틱 회귀, LDA, QDA, 나이브 베이즈, 그리고 KNN에 대한 **경험적(empirical)** (실용적) 성능을 비교합니다.

We generated data from six different scenarios, each of which involves a binary (two-class) classification problem.
우리는 6가지 다른 시나리오들로부터 데이터를 생성했으며, 이 각각의 시나리오들은 이진(두 클래스) 분류 문제를 포함합니다.

In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. The results are summarized below:
그 시나리오들 중 3개에서는 베이즈 결정 경계(Bayes decision boundary)가 선형적(linear) 특성을 보이며, 나머지 시나리오들에서는 그것이 비선형적(non-linear) 형태를 취합니다. 그 실험 결과들은 아래와 같이 요약됩니다:

- **Scenario 1 (Linear boundary, independent normal variables):** LDA performed well as expected. Logistic regression also performed well. KNN performed poorly because it suffered from variance. QDA performed worse than LDA since it was more flexible than necessary. Naive Bayes was slightly better than QDA because the assumption of independent predictors was correct.
- **시나리오 1 (선형 경계, 독립적인 정규 변수들):** LDA는 예상했던 바와 같이 좋은 성능을 보였습니다. 로지스틱 회귀 역시 준수하게 성능을 수행했습니다. KNN은 과도한 분산(variance)으로 인해 어려움을 겪었으므로 성능이 저조했습니다. QDA는 연산상 필요 이상으로 유연성을 가졌기 때문에 도리어 LDA보다도 성능이 나빴습니다. 나이브 베이즈는 독립적인 예측 변수들이라는 설정 가정이 올바르게 맞아떨어졌기 때문에 QDA보다는 성능이 약간 더 나았습니다.

- **Scenario 2 (Linear boundary, correlated variables):** Similar to Scenario 1, except naive Bayes performed very poorly because its independence assumption was completely violated by the correlated predictors.
- **시나리오 2 (선형 경계, 상관관계가 있는 변수들):** 시나리오 1과 양상이 유사했지만, 다만 나이브 베이즈는 예외적으로 상관관계가 결합된 예측 변수들로 인해 독립성 가정이 완전히 위배되어 깨졌으므로 성능이 매우 불량하게 저조했습니다.

- **Scenario 3 (Linear boundary, t-distribution):** Outliers were present. Logistic regression outperformed LDA since the data departed from the strict normal assumption. QDA deteriorated considerably. Naive Bayes performed very poorly again due to violated assumptions.
- **시나리오 3 (선형 경계, t-분포):** 이상치(Outliers)들이 존재했습니다. 데이터의 체제가 철저한 정규 분포 가정 조건에서 이탈해 벗어났으므로, 로지스틱 회귀가 LDA를 누르고 뛰어넘었습니다(outperformed). QDA는 성능이 상당히 떨어져 저하되었습니다. 나이브 베이즈도 체제 가정이 위배됨에 따라 다시 한번 성능이 매우 저조하게 나왔습니다.

- **Scenario 4 (Quadratic boundary, normal distribution with different correlations):** The decision boundary is non-linear. QDA outperformed all the other methods. Naive Bayes performed poorly due to independence violation.
- **시나리오 4 (2차 형태 경계, 각기 다른 상관관계를 갖는 정규 분포):** 결정 경계가 비선형(non-linear)적입니다. 따라서 QDA가 다른 모든 방법들을 능가했습니다. 나이브 베이즈는 독립성 가정이 위배된 탓에 부진한 성능을 보였습니다.

- **Scenario 5 (Highly non-linear boundary):** Both QDA and naive Bayes gave better results than the linear methods (LDA/Logistic). However, the highly flexible KNN-CV method gave the best overall results. Interestingly, KNN with $K=1$ gave the worst results, highlighting the importance of tuning smoothness.
- **시나리오 5 (고도의 비선형적 경계):** QDA와 나이브 베이즈 분류기 모두 기존 선형 방법론들(LDA/Logistic)보다는 더 나은 결과를 보여주었습니다. 하지만, 궁극적으로는 매우 유연성을 갖춘 KNN-CV 방법이 전체를 통틀어 가장 대단히 우수하고 탁월한 최고의 결과를 제공했습니다. 흥미롭게도, 단 $K=1$ 조건을 적용한 상태의 KNN은 도리어 분류 기준에서 가장 형편없는 최악의 결과를 안겨주었는데, 이는 분류기에서의 모델 평활도(smoothness)를 조율(tuning)하는 작업이 얼마나 핵심적으로 중요한지를 잘 강조해 보여줍니다.

- **Scenario 6 (Non-linear boundary due to unequal variance, extremely small sample size n=6):** Naive Bayes performed phenomenally well because its assumptions held and its variance is low. LDA/Logistic regression performed poorly due to the non-linear true boundary. QDA struggled heavily because it lacked the data size to estimate its high number of parameters, suffering from intense variance. KNN also failed completely due to the lack of training data.
- **시나리오 6 (불균일 분산으로 인한 비선형 경계, n=6의 극도로 적은 표본 크기):** 나이브 베이즈는 모델 연산의 가정들이 성립했고 분산이 작기 때문에 경이로울 정도로(phenomenally) 우수한 성능을 나타냈습니다. LDA/로지스틱 회귀는 진짜 참 분할 경계가 비선형적이었던 탓에 빈약한 성능을 보였습니다. QDA는 다수의 여러 매개 변수들을 추정할 데이터 크기가 부족했고 극심한 분산 변동에 시달렸기 때문에 몹시 고전했습니다. KNN 역시 훈련용 기준 데이터 자원에 대한 부족으로 인해 기계 가동이 완전히 실패로 끝났습니다.

These six examples illustrate that no one method will dominate the others in every situation.
이 여섯 가지의 사례들은 어떠한 특정 단일 분류기 예측 방법론일지라도 특정 하나가 다른 경쟁 방법론들을 모든 상황 세팅에서 항상 압살 제패해(dominate) 군림하지는 않는다는 점을 명확히 입증해 설명해 보여줍니다.

When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well.
진짜 참 결정 경계가 보편 선형적일 경우에, LDA와 로지스틱 회귀 접근법이 상대적으로 주로 성과가 좋은 성능을 보이는 경향이 있습니다.

When the boundaries are moderately non-linear, QDA or naive Bayes may give better results.
결정 경계가 어느 정도 완만하게 비선형성을 띨 때는, QDA 또는 나이브 베이즈가 더 성능상 좋은 결과를 보일 수 있습니다.

Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior.
마지막으로, 훨씬 더 복잡한 결정 경계들에 대해서는, KNN과 같은 비모수적(non-parametric) 접근법 장치가 가장 압도적으로 우수할(superior) 수 있습니다.

---

## Sub-Chapters

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans1.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans1.html)

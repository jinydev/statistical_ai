---
layout: default
title: "trans1"
---

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans1.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.4 Quadratic Discriminant Analysis
# 4.7.4 이차 판별 분석 (QDA)

We will now fit a QDA model to the `Smarket` data. QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we abbreviate to `QDA()`. The syntax is very similar to `LDA()`. 
우리는 이제 `Smarket` 데이터에 QDA 모델을 피팅할 것입니다. QDA는 `sklearn` 패키지의 `QuadraticDiscriminantAnalysis()` 를 통해 구현되며, 우리는 이를 `QDA()` 로 축약합니다. 구문(syntax)은 `LDA()` 와 매우 유사합니다.

```python
In [33]: qda = QDA(store_covariance=True)
qda.fit(X_train, L_train)
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True)
```

The `QDA()` function will again compute `means_` and `priors_`. 
`QDA()` 함수는 다시 `means_` 와 `priors_` 를 계산할 것입니다.

```python
In [34]: qda.means_, qda.priors_
```

```python
Out[34]: (array([[ 0.04279022,  0.03389409],
                 [-0.03954635, -0.03132544]]),
          array([0.49198397, 0.50801603]))
```

The `QDA()` classifier will estimate one covariance per class. Here is the estimated covariance in the first class: 
`QDA()` 분류기(classifier)는 클래스당 하나의 공분산(covariance)을 추정합니다. 다음은 첫 번째 클래스에서 추정된 공분산입니다:

```python
In [35]: qda.covariance_[0]
```

```python
Out[35]: array([[ 1.50662277, -0.03924806],
                [-0.03924806,  1.53559498]])
```

The output contains the group means. But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors. The `predict()` function works in exactly the same fashion as for LDA. 
출력에는 그룹 평균(group means)이 포함되어 있습니다. 그러나 QDA 분류기는 예측 변수의 선형 함수가 아닌 이차(quadratic) 함수를 포함하기 때문에 선형 판별(linear discriminants)의 계수는 포함하지 않습니다. `predict()` 함수는 LDA와 완전히 동일한 방식으로 작동합니다.

```python
In [36]: qda_pred = qda.predict(X_test)
confusion_table(qda_pred, L_test)
```

```python
Out[36]: Truth      Down   Up
Predicted            
Down         30   20
Up           81  121
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model. 
흥미롭게도, 2005년 데이터가 모델을 피팅하는 데 사용되지 않았음에도 불구하고 QDA 예측은 거의 60% 의 빈도로 정확합니다.

```python
In [37]: np.mean(qda_pred == L_test)
```

```python
Out[37]: 0.5992063492063492
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately. This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression. However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market!
정확하게 모델링하기 매우 어려운 것으로 알려진 주식 시장 데이터의 경우, 이러한 수준의 정확도는 상당히 인상적입니다. 이는 QDA가 가정한 이차(quadratic) 형태가 LDA와 로지스틱 회귀가 가정한 선형 형태보다 진정한 관계를 더 정확하게 포착할 수 있음을 시사합니다. 그러나 우리는 이러한 접근 방식이 일관되게 시장을 이길 것이라고 베팅하기 전에 더 큰 테스트 세트에서 이 방법의 성능을 평가할 것을 권장합니다!

---

## Sub-Chapters

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans1.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans1.html)

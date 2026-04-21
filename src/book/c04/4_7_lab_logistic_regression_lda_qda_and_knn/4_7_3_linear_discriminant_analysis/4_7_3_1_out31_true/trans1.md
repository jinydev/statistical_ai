---
layout: default
title: "trans1"
---

[< 4.7.3 Linear Discriminant Analysis](../trans1.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# **`Out[31]:`** `True` 

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so. For instance, suppose that we wish to predict a market decrease only if we are very certain that the market will indeed decrease on that day — say, if the posterior probability is at least 90%. We know that the first column of `lda_prob` corresponds to the label `Down` after having checked the `classes_` attribute, hence we use the column index 0 rather than 1 as we did above. 
만약 우리가 예측을 수행하기 위해 50% 가 아닌 다른 사후 확률 임계값(threshold)을 사용하고자 한다면, 쉽게 그렇게 할 수 있습니다. 예를 들어, 우리가 그날 시장이 실제로 하락할 것이라고 매우 확신하는 경우에만, 즉 사후 확률이 최소 90% 인 경우에만 시장 하락을 예측하고자 한다고 가정해 봅시다. 우리는 `classes_` 속성을 확인한 후 `lda_prob` 의 첫 번째 열(column)이 `Down` 레이블에 해당한다는 것을 알게 되었으므로, 위에서 했던 것처럼 인덱스 1 대신 열 인덱스 0을 사용합니다.

```python
In [32]: np.sum(lda_prob[:,0] > 0.9)
```

```python
Out[32]: 0
```

No days in 2005 meet that threshold! In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%. 
2005년의 어떤 날도 그 임계값을 충족하지 못합니다! 실제로 2005년 전체에서 하락에 대한 가장 큰 사후 확률은 52.02% 였습니다.

The LDA classifier above is the first classifier from the `sklearn` library. We will use several other objects from this library. The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5. Specifically, the methods first create a generic classifier without referring to any data. This classifier is then fit to data with the `fit()` method and predictions are always produced with the `predict()` method. This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of `sklearn`. This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation. This standard pattern also allows for a predictable formation of workflows.
위의 LDA 분류기는 `sklearn` 라이브러리의 첫 번째 분류기입니다. 우리는 이 라이브러리의 다른 여러 객체들을 사용할 것입니다. 객체들은 Chapter 5에서 볼 수 있는 교차 검증(cross-validation)과 같은 작업을 단순화하는 공통 구조를 따릅니다. 구체적으로, 이 방법들은 먼저 어떤 데이터도 참조하지 않고 제네릭 분류기(generic classifier)를 생성합니다. 그런 다음 이 분류기는 `fit()` 메서드를 사용하여 데이터에 피팅되며, 항상 `predict()` 메서드를 사용하여 예측(predictions)이 산출(produced)됩니다. 먼저 분류기를 인스턴스화(instantiating)한 다음 피팅을 하고, 그 다음 예측을 산출하는 이러한 패턴은 `sklearn` 의 명시적인 설계 선택(design choice)입니다. 이러한 일관성(uniformity)은 교차 검증에서 발생하는 다양한 훈련 세트와 같이 다른 데이터에 적합시킬 수 있도록 분류기를 깔끔하게 복사하는 것을 가능하게 합니다. 이 표준 패턴은 또한 워크플로우(workflows)의 예측 가능한 구성을 허용합니다.

---

## Sub-Chapters

[< 4.7.3 Linear Discriminant Analysis](../trans1.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans1.html)

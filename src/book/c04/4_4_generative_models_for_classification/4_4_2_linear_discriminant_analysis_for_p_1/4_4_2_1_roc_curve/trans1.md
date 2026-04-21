---
layout: default
title: "trans1"
---

[< 4.4.2 Linear Discriminant Analysis For P > 1](../trans1.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.4.2.1 ROC Curve
# 4.4.2.1 ROC 곡선

![Figure 4.8](./img/4_8.png)

**FIGURE 4.8.** _A ROC curve for the LDA classifier on the_ `Default` _data. It traces out two types of error as we vary the threshold value for the posterior probability of default. The actual thresholds are not shown. The true positive rate is the sensitivity: the fraction of defaulters that are correctly identified, using a given threshold value. The false positive rate is 1-specificity: the fraction of non-defaulters that we classify incorrectly as defaulters, using that same threshold value. The ideal ROC curve hugs the top left corner, indicating a high true positive rate and a low false positive rate. The dotted line represents the “no information” classifier; this is what we would expect if student status and credit card balance are not associated with probability of default._ 
**그림 4.8.** `Default` 데이터에 대한 LDA 분류기의 ROC 곡선. 이는 파산의 사후 확률에 대한 임계값을 변화시킬 때 두 가지 유형의 오류를 추적합니다. 실제 임계값 빈도는 표시되지 않았습니다. 진짜 양성 비율(true positive rate)은 민감도(sensitivity)입니다: 주어진 임계값을 사용하여 올바르게 식별된 파산자의 비율입니다. 거짓 양성 비율(false positive rate)은 1 - 특이도(specificity)입니다: 동일한 임계값을 사용하여 파산자로 잘못 분류한 비파산자의 비율입니다. 이상적인 ROC 곡선은 왼쪽 상단을 껴안으며(hug), 높은 진짜 양성 비율과 낮은 거짓 양성 비율을 나타냅니다. 점선은 "정보 없음(no information)" 분류기를 나타냅니다; 이는 학생 상태와 신용 카드 잔액이 파산 확률과 연관이 없을 때 예상할 수 있는 것입니다.

The overall performance of a classifier, summarized over all possible thresholds, is given by the _area under the (ROC) curve_ (AUC). An ideal ROC curve will hug the top left corner, so the larger the area under the ROC curve the better the classifier. For this data the AUC is 0.95, which is close to the maximum of 1.0, so would be considered very good. We expect a classifier that performs no better than chance to have an AUC of 0.5 (when evaluated on an independent test set not used in model training). ROC curves are useful for comparing different classifiers, since they take into account all possible thresholds. It turns out that the ROC curve for the logistic regression model of Section 4.3.4 fit to these data is virtually indistinguishable from this one for the LDA model, so we do not display it here. 
가능한 모든 임계값에 대해 요약된 분류기의 전반적인 성능은 _(ROC) 곡선 아래의 면적_ (AUC)으로 주어집니다. 이상적인 ROC 곡선은 왼쪽 상단 모서리를 껴안게 되므로, ROC 곡선 아래의 면적이 넓을수록 분류기가 더 좋음을 나타냅니다. 이 데이터의 경우 AUC는 0.95로 최대값 1.0에 가까우므로, 매우 좋은 것으로 간주됩니다. 우연(chance)보다 낫지 않은 성능을 내는 분류기는 AUC가 0.5일 것으로 예상합니다 (모델 훈련에 사용되지 않은 독립적인 테스트 세트에서 평가될 때). ROC 곡선은 모든 가능한 임계값을 고려하기 때문에 서로 다른 분류기를 비교하는 데 유용합니다. 앞서 4.3.4 절의 이러한 데이터에 편입된 로지스틱 회귀 모델에 대한 ROC 곡선은 LDA 모델에 대한 이 곡선과 사실상 구별될 수 없는 것으로 나타나므로, 여기서는 표시하지 않습니다.

As we have seen above, varying the classifier threshold changes its true positive and false positive rate. These are also called the _sensitivity_ and one minus the _specificity_ of our classifier. Since there is an almost bewildering array of terms used in this context, we now give a summary. Table 4.6 shows the possible results when applying a classifier (or diagnostic test) to a population. To make the connection with the epidemiology literature, we think of “+” as the “disease” that we are trying to detect, and “−” as the “non-disease” state. To make the connection to the classical hypothesis testing literature, we think of “−” as the null hypothesis and “+” as the alternative (non-null) hypothesis. In the context of the `Default` data, “+” indicates an individual who defaults, and “−” indicates one who does not.
위에서 살펴본 바와 같이, 분류기 임계값을 변경시키면 그것의 진짜 양성 비율과 거짓 양성 비율이 변경됩니다. 이들은 또한 우리 분류기의 _민감도_ 및 1 마이너스 _특이도_ 라고도 불립니다. 이 문맥에서 사용되는 용어들의 어지러운 배열(array)이 존재하므로, 이제 요약을 제공합니다. 표 4.6은 모집단에 분류기(또는 진단 검사)를 적용할 때의 가능한 결과를 보여줍니다. 역학 문헌과의 연결을 만들기 위해, 우리가 탐지하고자 하는 “질병”을 “+” 로 생각하고, “비-질병” 상태를 “−” 로 생각합니다. 고전적인 가설 검정 문헌과의 연결을 위해, 우리는 “−” 를 귀무 가설(null hypothesis)로 생각하고 “+” 를 대립 (비-귀무) 가설로 생각합니다. `Default` 데이터의 문맥에서, “+”는 파산하는 개인을 나타내고, “−”는 파산하지 않는 개인을 나타냅니다.

| | True class: $-$ or Null | True class: $+$ or Non-null | Total |
|---|---|---|---|
| **Predicted class: $-$ or Null** | True Neg. (TN) | False Neg. (FN) | N* |
| **Predicted class: $+$ or Non-null** | False Pos. (FP) | True Pos. (TP) | P* |
| **Total** | N | P | |

**TABLE 4.6.** _Possible results when applying a classifier or diagnostic test to a population._
**표 4.6.** 모집단에 분류기나 진단 검사를 적용할 때 가능한 결과들.

| Name | Definition | Synonyms |
|---|---|---|
| False Pos. rate | FP / N | Type I error, 1−Specificity |
| True Pos. rate | TP / P | 1−Type II error, power, sensitivity, recall |
| Pos. Pred. value | TP / P* | Precision, 1−false discovery proportion |
| Neg. Pred. value | TN / N* | |

**TABLE 4.7.** _Important measures for classification and diagnostic testing, derived from quantities in Table 4.6._ 
**표 4.7.** 표 4.6의 모집 수량들로부터 파생된 분류 및 진단 테스트를 위한 중요 측도들.

Table 4.7 lists many of the popular performance measures that are used in this context. The denominators for the false positive and true positive rates are the actual population counts in each class. In contrast, the denominators for the positive predictive value and the negative predictive value are the total predicted counts for each class.
표 4.7은 이 문맥에서 사용되는 널리 쓰이는 성능 측정값(performance measures) 중 많은 것들을 나열합니다. 거짓 양성 비율과 진짜 양성 비율에 대한 분모(denominator)는 각 클래스의 실제 모집단 수입니다. 대조적으로, 양성 예측 가치와 음성 예측 가치의 분모는 각 클래스에 대한 예측된 카운트 총합입니다.

---

## Sub-Chapters

[< 4.4.2 Linear Discriminant Analysis For P > 1](../trans1.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/trans1.html)

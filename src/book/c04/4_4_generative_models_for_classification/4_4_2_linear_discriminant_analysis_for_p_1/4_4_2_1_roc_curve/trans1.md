---
layout: default
title: "trans1"
---

[< 4.4.2 Linear Discriminant Analysis For P 1](../index.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# **ROC Curve**
# **4.4.2.1 ROC 곡선 (수신기 조작 특성 곡선)**

![Figure 4.8](./img/4_8.png)

**FIGURE 4.8.** _A ROC curve for the LDA classifier on the_ `Default` _data. It traces out two types of error as we vary the threshold value for the posterior probability of default. The actual thresholds are not shown. The true positive rate is the sensitivity: the fraction of defaulters that are correctly identified, using a given threshold value. The false positive rate is 1-specificity: the fraction of non-defaulters that we classify incorrectly as defaulters, using that same threshold value. The ideal ROC curve hugs the top left corner, indicating a high true positive rate and a low false positive rate. The dotted line represents the “no information” classifier; this is what we would expect if student status and credit card balance are not associated with probability of default._
**그림 4.8.** `Default` 데이터에 적용된 LDA 분류기의 ROC 곡선. 이는 파산에 대한 사후 확률 임계값을 변화시킴에 따라 발생하는 두 가지 유형의 오류 궤적을 추적하여 보여줍니다. 실제 적용된 임계값 자체는 그래프상에 나타나지 않습니다. 진짜 양성 비율(true positive rate)은 민감도(sensitivity)를 의미하며, 이는 주어진 특정 임계값을 사용했을 때 올바르게 식별된 파산자들의 비율입니다. 거짓 양성 비율(false positive rate)은 1 - 특이도(specificity)를 뜻하며, 동일한 임계값을 사용했을 때 파산하지 않은 사람들을 파산자로 잘못 분류한 비율을 나타냅니다. 이상적인 ROC 곡선은 왼쪽 상단 모서리에 바짝 붙어있는 형태를 띠며, 이는 높은 진짜 양성 비율(민감도)과 낮은 거짓 양성 비율(1-특이도)을 나타냅니다. 점선은 "정보가 없는(no information)" 분류기를 나타내며, 이는 학생 여부와 신용카드 잔액이 파산 확률과 아무런 연관이 없을 때 나타날 것으로 기대되는 결과선입니다.

---

marized over all possible thresholds, is given by the _area under the (ROC) curve_ (AUC).
(앞 장의 문장과 이어짐) ...마합하여 모든 가능한 임계값에 걸쳐 요약(summarized)된 성능은 **(ROC) 곡선 아래 면적(Area Under the Curve, AUC)** 으로 주어집니다.

An ideal ROC curve will hug the top left corner, so the larger area under the ROC curve the better the classifier.
이상적인 ROC 곡선은 그래프의 왼쪽 상단 모서리에 바짝 붙어(hug) 있을 것이므로, ROC 곡선 아래의 면적(AUC)이 클수록 더 훌륭한 성능의 분류기임을 의미합니다.

For this data the AUC is 0.95, which is close to the maximum of 1.0, so would be considered very good.
이 데이터에 대해서 AUC 값은 0.95이며, 이는 최대치인 1.0에 매우 가까운 수치이므로 모델의 성능이 매우 훌륭(very good)하다고 간주될 수 있습니다.

We expect a classifier that performs no better than chance to have an AUC of 0.5 (when evaluated on an independent test set not used in model training).
우리는 아무런 유의미한 정보 없이 우연(chance)보다 나을 것이 전혀 없는 수준으로 작동하는 분류기가 (모델 훈련에 사용되지 않은 독립적인 외부 평가 테스트 데이터셋에서 평가되었을 때) 0.5의 점수 AUC 값을 가질 것으로 기대 추산합니다.

ROC curves are useful for comparing different classifiers, since they take into account all possible thresholds.
ROC 곡선은 분류기들이 취할 수 있는 모든 가능한 임계값 허들 기준들을 종합적으로 고려(take into account)하기 때문에 여러 다양한 분류기 모델들을 서로 성능 비교하는 데 있어 매우 유용합니다.

It turns out that the ROC curve for the logistic regression model of Section 4.3.4 fit to these data is virtually indistinguishable from this one for the LDA model, so we do not display it here.
앞선 섹션 4.3.4에서 다루었던 로지스틱 회귀 모델을 이 동일한 데이터에 피팅 적합하여 산출한 ROC 곡선 결과는, 놀랍게도 지금 여기서 제시된 LDA 모델의 곡선 궤적과 시각적으로 거의 구별할 수 없을(virtually indistinguishable) 정도로 매우 흡사하게 나타났기에, 우리는 굳이 로지스틱 곡선을 여기에 따로 병치하여 표시하지 않았습니다.

As we have seen above, varying the classifier threshold changes its true positive and false positive rate.
우리가 바로 위에서 확인하고 살펴보았듯이, 분류기의 임계값(threshold) 기준치를 변경 조작하는 행위는 분류 모델 자체의 점수인 진짜 양성 비율(true positive rate)과 거짓 양성 비율(false positive rate)을 유동적으로 변화시킵니다.

These are also called the _sensitivity_ and one minus the _specificity_ of our classifier.
이들 두 지표 수치는 다른 전문 용어로 우리 분류기의 **민감도(sensitivity)**, 그리고 1에서 **특이도(specificity)** 를 뺀 값 (1 - specificity) 이라고도 불립니다.

Since there is an almost bewildering array of terms used in this context, we now give a summary.
이 통계 역학 분류의 맥락 속에서는 정말이지 거의 혼란스럽고 어리둥절할(bewildering) 정도로 매우 많은 다양한 판별 용어 칭호들이 쏟아져 사용되고 있으므로, 우리는 이제 이들을 일목요연하게 축약하여 요약(summary)을 제공합니다.

Table 4.6 shows the possible results when applying a classifier (or diagnostic test) to a population.
표 4.6은 어떤 특정 모집단 대중 요원들에 대해 분류기(또는 진단의학 검사 장치)를 투입해 적용했을 때 도출 파생될 수 있는 모든 발생 가능한 진단 결과 분류판을 보여줍니다.

To make the connection with the epidemiology literature, we think of "+" as the "disease" that we are trying to detect, and "-" as the "non-disease" state.
역학(epidemiology) 문헌들과의 개념적 맥락 연결을 짓어 돕기 위해, 우리는 기호 **"+"** 를 우리가 기를 쓰고 탐지하여 검거하고자 하는 부정적인 **"질병(disease)"** 상태라고 생각하고, 반대로 **"-"** 를 정상적이고 무고한 건강한 **"질병 없음(non-disease)"** 의 착한 상태 기표라고 쉽게 간주하겠습니다.

To make the connection to the classical hypothesis testing literature, we think of "-" as the null hypothesis and "+" as the alternative (non-null) hypothesis.
또한 전통적인 고전 통계학의 가설 검정 문헌들과 논리를 연결하고자 한다면, 우리는 "-" 를 흔해 빠진 귀무 가설(null hypothesis)로 생각하고 "+" 상태 지목을 새롭게 탐지 주장하는 대립(alternative, non-null) 가설 타깃으로 간주해 생각할 수도 있습니다.

In the context of the `Default` data, "+" indicates an individual who defaults, and "-" indicates one who does not.
우리가 실습하는 `Default` 파산 데이터의 맥락 환경에서라면, "+" 십자 기호는 부당 파산(default)을 저지른 불량 범죄 개체 개인을 명백히 나타내며, "-" 표식은 성실하게 빚을 갚고 파산하지 않는 정상 착한 개인을 지칭합니다.

| | | True class (실제 클래스) | | |
|---|---|---|---|---|
| | | - or Null | + or Non-null | Total |
| **Predicted class (예측)** | **- or Null** | True Neg. (TN) | False Neg. (FN) | $N^*$ |
| | **+ or Non-null** | False Pos. (FP) | True Pos. (TP) | $P^*$ |
| **Total** | | N | P | |

**TABLE 4.6.** _Possible results when applying a classifier or diagnostic test to a population._
**표 4.6.** 모집단에 분류기 모델이나 혹은 진단 검사 센서를 적용 가동했을 때 돌출 발생할 수 있는 모든 경우의 수 결과 모음표. 

| Name | Definition | Synonyms |
|---|---|---|
| False Pos. rate (거짓 양성 비율) | FP / N | Type I error(제1종 오류), 1-Specificity(1-특이도) |
| True Pos. rate (진짜 양성 비율) | TP / P | 1-Type II error(1-제2종 오류), power(검정력), sensitivity(민감도), recall(재현율) |
| Pos. Pred. value (양성 예측 값) | TP / $P^*$ | Precision(정밀도), 1-false discovery proportion |
| Neg. Pred. value (음성 예측 값) | TN / $N^*$ | |

**TABLE 4.7.** _Important measures for classification and diagnostic testing, derived from quantities in Table 4.6._
**표 4.7.** 표 4.6에 나열 기표된 수량 치수들로부터 기초 유도되어 산입 파생된, 분류 성능 및 진단의학 검사 측정 판단을 위한 중요한 통계적 척도 계산 비율 명칭들.

Table 4.7 lists many of the popular performance measures that are used in this context.
표 4.7은 이 오판 통계 분류 맥락에서 지겹게 자주 쓰이는 여러 가지 대중적이고 유명한 예측 기계 성능 평가 비율 단위 척도(performance measures) 용어들을 싹 다 한데 깔끔히 나열하여 정리해 줍니다.

The denominators for the false positive and true positive rates are the actual population counts in each class.
여기서 표 4.7에 제시된 거짓 양성 비율 산식(False Positive Rate)과 진짜 양성 비율(True Positive Rate) 척도의 산출 분모(denominators) 모수 뼈대는, 언제나 실제 표본 안에 포진된 각 클래스 방 타깃 진영의 '실제 진실한 총 인구 보유 수(개체 파벌 덩어리수, N 또는 P)' 진위를 기준으로 삼아 계산됩니다.

In contrast, the denominators for the positive predictive value and the negative predictive value are the total predicted counts for each class.
이와는 대조적으로 한편, 양성 예측 값(Positive Predictive Value)과 음성 예측 값(Negative Predictive Value)이라는 또 다른 통계 비율 척도 지표에서 깔리는 산출 분모 밑단 모수 값들은 현실의 진위여부 인구수가 배제된 채, 철저히 우리 기계 모델이 허세 부려 독단적으로 멋대로 심판 지목 선언한 각 클래스 방의 예측 추정 환산 지목 표지판 쪽수 인원수($P^*$, $N^*$)들을 토대 바탕으로 삼아 산출 계산됩니다.

---

## Sub-Chapters

[< 4.4.2 Linear Discriminant Analysis For P 1](../index.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/trans1.html)

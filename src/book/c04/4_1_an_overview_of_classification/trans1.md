---
layout: default
title: "trans1"
---

[< 4. Classification](../trans1.html) | [4.2 Why Not Linear Regression >](../4_2_why_not_linear_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.1 An Overview of Classification
# 4.1. 분류의 개요 (An Overview of Classification)

Classification problems occur often, perhaps even more so than regression problems. Some examples include:
분류(Classification) 문제는 종종 회귀(Regression) 문제보다 훨씬 더 자주 발생합니다. 몇 가지 예를 살펴보겠습니다:

1. A person arrives at the emergency room with a set of symptoms that could possibly be attributed to one of three medical conditions. Which of the three conditions does the individual have?
1. 어떤 사람이 세 가지 질병 중 하나에 해당할 수 있는 일련의 증상을 가지고 응급실에 도착했습니다. 이 사람은 세 가지 질병 중 어떤 병을 앓고 있는 걸까요?

2. An online banking service must be able to determine whether or not a transaction being performed on the site is fraudulent, on the basis of the user’s IP address, past transaction history, and so forth.
2. 온라인 뱅킹 서비스는 사용자의 IP 주소, 과거 거래 내역 등을 바탕으로 현재 사이트에서 수행되는 거래가 사기(Fraudulent)인지 아닌지를 판단해야 합니다.

3. On the basis of DNA sequence data for a number of patients with and without a given disease, a biologist would like to figure out which DNA mutations are deleterious (disease-causing) and which are not.
3. 특정 질병이 있거나 없는 환자들의 DNA 서열 데이터를 바탕으로, 생물학자는 어떤 DNA 돌연변이가 질병을 유발(Deleterious)하고 어떤 것이 그렇지 않은지 파악하고자 합니다.

Just as in the regression setting, in the classification setting we have a set of training observations $(x_1, y_1), \dots , (x_n, y_n)$ that we can use to build a classifier. We want our classifier to perform well not only on the training data, but also on test observations that were not used to train the classifier. In this chapter, we will illustrate the concept of classification using the simulated `Default` data set. We are interested in predicting whether an individual will default on his or her credit card payment, on the basis of annual income and monthly credit card balance. The data set is displayed in Figure 4.1. In the left-hand panel of Figure 4.1, we have plotted annual `income` and monthly credit card `balance` for a subset of 10,000 individuals. The individuals who defaulted in a given month are shown in orange, and those who did not in blue. (The overall default rate is about 3 %, so we have plotted only a fraction of the individuals who did not default.) It appears that individuals who defaulted tended to have higher credit card balances than those who did not. In the center and right-hand panels of Figure 4.1, two pairs of boxplots are shown. The first shows the distribution of `balance` split by the binary `default` variable; the second is a similar plot for `income`. In this chapter, we learn how to build a model to predict `default` ($Y$) for any given value of `balance` ($X_1$) and `income` ($X_2$). Since $Y$ is not quantitative, the simple linear regression model of Chapter 3 is not a good choice: we will elaborate on this further in Section 4.2.
회귀 분석과 마찬가지로 분류에서도 우리는 분류기를 구축하는 데 사용할 수 있는 훈련 관측치(Training Observations) 세트 $(x_1, y_1), \dots , (x_n, y_n)$ 를 갖게 됩니다. 우리는 분류기가 훈련 데이터뿐만 아니라 평가에 사용되지 않은 테스트 관측치(Test Observations)에서도 좋은 성능을 발휘하기를 원합니다. 이번 장에서는 시뮬레이션된 `Default` 데이터셋을 사용하여 분류의 개념을 설명하겠습니다. 우리는 연봉(Annual Income)과 월별 신용카드 잔고(Monthly Credit Card Balance)를 바탕으로 어떤 개인이 신용카드 대금을 체납(Default)할지 아닐지 예측하는 데 관심이 있습니다. 데이터셋은 그림 4.1에 표시되어 있습니다. 그림 4.1의 왼쪽 패널에는 10,000명의 모집단 중 일부의 연봉(`income`)과 월별 신용카드 잔고(`balance`)가 그려져 있습니다. 특정 월에 체납한 사람들은 주황색으로, 체납하지 않은 사람들은 파란색으로 표시되어 있습니다. (전체 체납률은 약 3%이므로 체납하지 않은 사람들은 일부만 표시했습니다.) 체납한 사람들은 체납하지 않은 사람들에 비해 신용카드 잔고가 더 높은 경향이 있는 것으로 나타납니다. 그림 4.1의 가운데와 오른쪽 패널에는 두 쌍의 상자 그림(Boxplots)이 표시되어 있습니다. 첫 번째는 이진 체납 변수(`default`)에 따른 잔고(`balance`)의 분포를 보여주고, 두 번째는 소득(`income`)에 대한 비슷한 그림입니다. 이 장에서 우리는 특정 잔고($X_1$)와 소득($X_2$)의 값이 주어졌을 때 체납 여부($Y$)를 예측하는 모델을 구축하는 방법을 배울 것입니다. $Y$가 수치형이 아니므로 3장의 단순 선형 회귀 모델은 결코 좋은 선택이 아닙니다. 왜 그런지에 대해서는 4.2절에서 자세히 설명하겠습니다.

It is worth noting that Figure 4.1 displays a very pronounced relationship between the predictor `balance` and the response `default`. In most real applications, the relationship between the predictor and the response will not be nearly so strong. However, for the sake of illustrating the classification procedures discussed in this chapter, we use an example in which the relationship between the predictor and the response is somewhat exaggerated.
참고로 그림 4.1은 예측 변수인 잔고(`balance`)와 반응 변수인 체납 여부(`default`) 간에 매우 뚜렷한 관계를 보여줍니다. 대부분의 실제 애플리케이션에서는 예측 변수와 반응 변수 간의 관계가 이토록 명확하게 보이지는 않습니다. 그러나 이 장에서 논의되는 분류 절차를 설명하기 쉽도록, 우리는 예측 변수와 반응 변수 간의 관계가 다소 과장된 예시를 사용했습니다.

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4. Classification](../trans1.html) | [4.2 Why Not Linear Regression >](../4_2_why_not_linear_regression/trans1.html)

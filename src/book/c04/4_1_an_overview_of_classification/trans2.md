---
layout: default
title: "trans2"
---

[< 4. Classification](../trans2.html) | [4.2 Why Not Linear Regression >](../4_2_why_not_linear_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.1 An Overview of Classification
# 4.1. 분류의 개요 (적군인가 아군인가, 그것이 문제로다)

Classification problems occur often, perhaps even more so than regression problems. Some examples include:
이분법의 세계! 실생활에선 숫자를 딱 맞추는 회귀(Regression) 문제보다도, "이게 A냐 B냐?"를 갈라치는 **분류(Classification)** 문제가 어쩌면 훨씬 더 자주, 지독하게 발생합니다. 일상에서 마주치는 몇 가지 살벌한 예시들을 살펴볼까요?

1. A person arrives at the emergency room with a set of symptoms that could possibly be attributed to one of three medical conditions. Which of the three conditions does the individual have?
1. 한 환자가 피를 흘리며 응급실에 실려 왔습니다. 이 사람의 증상은 가벼운 찰과상, 심근경색, 아니면 희귀 전염병이라는 세 가지 질병 중 하나에 치명적으로 해당할 수 있습니다. 과연 의사는 이 환자를 어떤 병(조건)으로 분류해 응급 수술대 위에 올릴지 판단해야 합니다.

2. An online banking service must be able to determine whether or not a transaction being performed on the site is fraudulent, on the basis of the user’s IP address, past transaction history, and so forth.
2. 온라인 뱅킹 서비스의 보안 AI는, 현재 로그인된 사용자의 수상한 IP 주소 은신처, 과거 비정상 거래 내역 등을 집요하게 파고들어 바탕 삼아, 지금 막 결제된 이 송금 거래가 진짜 주인이 한 것인지 아니면 해커의 **사기(Fraudulent)** 결제인지를 단 1초 만에 판별해 내야만 합니다.

3. On the basis of DNA sequence data for a number of patients with and without a given disease, a biologist would like to figure out which DNA mutations are deleterious (disease-causing) and which are not.
3. 수백 명의 환자와 정상인에서 뽑아낸 방대한 DNA 서열 데이터를 바탕으로, 미치광이 생물학자는 수많은 핏줄 속 DNA 돌연변이들 중 도대체 어떤 놈이 치명적 질병을 발발시키는 원흉(**Deleterious**)이고, 어떤 놈은 착한 무해성 찌꺼기인지를 구별해 색출하고 싶어 합니다.

Just as in the regression setting, in the classification setting we have a set of training observations $(x_1, y_1), \dots , (x_n, y_n)$ that we can use to build a classifier. We want our classifier to perform well not only on the training data, but also on test observations that were not used to train the classifier. In this chapter, we will illustrate the concept of classification using the simulated `Default` data set. We are interested in predicting whether an individual will default on his or her credit card payment, on the basis of annual income and monthly credit card balance. The data set is displayed in Figure 4.1. In the left-hand panel of Figure 4.1, we have plotted annual `income` and monthly credit card `balance` for a subset of 10,000 individuals. The individuals who defaulted in a given month are shown in orange, and those who did not in blue. (The overall default rate is about 3 %, so we have plotted only a fraction of the individuals who did not default.) It appears that individuals who defaulted tended to have higher credit card balances than those who did not. In the center and right-hand panels of Figure 4.1, two pairs of boxplots are shown. The first shows the distribution of `balance` split by the binary `default` variable; the second is a similar plot for `income`. In this chapter, we learn how to build a model to predict `default` ($Y$) for any given value of `balance` ($X_1$) and `income` ($X_2$). Since $Y$ is not quantitative, the simple linear regression model of Chapter 3 is not a good choice: we will elaborate on this further in Section 4.2.
앞서 배운 회귀 분석 챕터의 세팅과 소름 돋게 똑같이, 분류 작전 세팅에서도 우리는 "이 단서일 땐 이놈이 범인이었다"라는 무수한 **훈련 관측치 세트 $(x_1, y_1), \dots , (x_n, y_n)$** 를 똑같이 쥐고서 범인 감별사(분류기)를 구축하는 데 사용합니다. 우리는 우리의 애지중지 감별사가 과거 훈련 데이터만 앵무새처럼 외우는 게 아니라, 한 번도 본 적 없는 낯선 실전 테스트 관측치(Test Observations) 범죄 현장에서도 귀신같이 범인을 때려 맞히며 좋은 성능을 발휘하기를 간절히 원합니다. 이번 장에서는 시뮬레이션으로 극적으로 만들어낸 가상의 **`Default` (파산/체납) 데이터셋**을 도마 위에 올려 분류의 치명적 개념을 설명하겠습니다. 우리는 한 사람의 지갑 속 '연봉(`income`)'과 속이 타들어 가는 '월별 신용카드 빚 잔고(`balance`)'를 바탕으로, 과연 이 사람이 다음 달에 카드 대금을 갚지 못하고 **배 째라 체납(Default) 폭탄**을 터뜨릴지 아닐지를 미리 점쟁이처럼 예측해 내 파헤치는 데 지대한 관심을 둡니다. 데이터셋은 그림 4.1에 전시되어 있습니다. 그림 4.1의 왼쪽 패널 도화지에는 10,000명의 일반인 무리들의 연봉(`income`)과 엄청난 신용카드 잔고(`balance`)가 어지럽게 점으로 찍혀(plotted) 있습니다. 특정 달에 빚을 갚지 않고 통수를 친 무서운 체납자들은 **오렌지색**으로, 착실히 갚은 훌륭한 시민들은 **파란색** 평화의 점으로 칠해져 표시되어 있습니다. (이 나라의 전체 체납률은 고작 около 3% 남짓이므로, 시각적 조율을 위해 착실한 파란 점 사람들은 전체 중 일부만 슬쩍 분수로 표시했습니다.) 그림을 딱 보면, 체납 폭탄을 터뜨린 오렌지색 사람 군상은 파란 착실한 사람들에 비해 유독 신용카드 빚 잔고가 천장 뚫뚫게 높은 위험한 경향을 명백히 보이는 것으로 나타납니다. 그림 4.1의 가운데와 우측 끝자락 패널에는, 배를 가르고 분포를 보여주는 두 쌍의 상자 수염 그림(Boxplots)이 흉측하게 내걸려 있습니다. 첫 번째 상자 그림 군은 대상이 배를 쨌냐 안 쨌냐 하는 극단적 이분법 체납 변수(`default`) 여부에 따라 확연히 쪼개 갈라진 잔고(`balance`)의 분포 차이를 여실히 보여주고, 이어 두 번째 군은 소득(`income`) 변수에 대한 유사한 해부 그림을 표출합니다. 드디어 대망의 이 챕터에서, 우리는 어느 임의 고객의 빚 잔고($X_1$)와 소득($X_2$) 수치값이 딱 주어졌을 때, 이놈이 과연 빚을 떼먹고 도망갈 체납 여부($Y$) 상태일지를 기막히게 예측해 내는 무적의 분류 모델 하나를 단단히 구축하는 비법 방법을 배울 것입니다. 여기서 주의! $Y$가 연속된 숫자(수치형)가 아니므로, 챕터 3에서 배웠던 순진한 '단순 선형 회귀 모델' 따위를 들이대는 건 **결코 좋은 선택이 아니라 미친 짓**에 가깝습니다. 도대체 왜 그런 바보 같은 짓인지에 대해서는, 바로 다음 장인 피 튀기는 4.2절에서 무지무지하게 자세히 썰을 풀어 설명하겠습니다.

It is worth noting that Figure 4.1 displays a very pronounced relationship between the predictor `balance` and the response `default`. In most real applications, the relationship between the predictor and the response will not be nearly so strong. However, for the sake of illustrating the classification procedures discussed in this chapter, we use an example in which the relationship between the predictor and the response is somewhat exaggerated.
여기서 잠깐, 고백할 게 있습니다! 방금 본 그림 4.1은 예측 변수인 카드 빚 잔고(`balance`) 스펙과 타깃 반응 변수인 체납 여부(`default`) 사이에 너무 짜고 친 듯이 아주아주 뚜렷하고 굵직한(pronounced) 극명 관계성을 과시하듯 보여줍니다. 하지만 차가운 실전 대부분의 실제 현장 애플리케이션들에서는, 예측 단서와 타깃 변수 사이의 관계가 저렇게 예쁘고 강렬하게 드러나 보일 리가 거의 만무합니다. 그러나, 이 챕터에서 떠들 분류법들의 메커니즘 절차와 그 웅장함을 아주 손쉽고 극적으로 시각 조명해 설명하기 위해, 우리는 예측 단서와 목표 타깃 반응 간의 관계가 다분히 쇼맨십 지게 **다소 뻥튀기 과장된(exaggerated)** 극단 예시 찌라시를 약 올리듯 일부러 사용했다는 점을 감안해 주십시오.

This is the document for this topic.
이것은 해당 분류 주제에 관한 기본 문서 개요 서류입니다.

---

## Sub-Chapters

[< 4. Classification](../trans2.html) | [4.2 Why Not Linear Regression >](../4_2_why_not_linear_regression/trans2.html)

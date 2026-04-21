---
layout: default
title: "trans2"
---

# 5.1 Cross-Validation 
# 5.1 교차 검증 (Cross-Validation): 진짜 실력을 폭로하는 모의고사 시스템!

In Chapter 2 we discuss the distinction between the _test error rate_ and the _training error rate_ . The test error is the average error that results from using a statistical learning method to predict the response on a new observation— that is, a measurement that was not used in training the method. Given a data set, the use of a particular statistical learning method is warranted if it results in a low test error. The test error can be easily calculated if a designated test set is available. Unfortunately, this is usually not the case. In contrast, the training error can be easily calculated by applying the statistical learning method to the observations used in its training. But as we saw in Chapter 2, the training error rate often is quite different from the test error rate, and in particular the former can dramatically underestimate the latter. 
Chapter 2에서 우리는 뼈 때리는 진실, 연습 훈련장에서의 성적표(_훈련 에러율_)와 피 튀기는 실전 수능장에서의 성적표(_테스트 에러율_)가 차원이 다르다는 걸 짚고 넘어왔습니다. 실전 테스트 에러란, 우리 기계가 태어나서 단 한 번도 본 적 없는 미지의 외계인 관측치(new observation) 를 예측하라고 던져줬을 때 헛스윙 치는 뻘짓 비율입니다. 어떤 분석 엔진을 내세워 자랑하려면 마땅히 이 실전 에러율이 낮아야만 정당당당(warranted) 한 거죠. 만약 하늘에서 뚝 떨어진 완벽한 미개척 테스트 전용 데이터 풀이 깔려있다면 점수 계산은 껌일 겁니다. 하지만 잔인하게도 현실 방구석에 그런 꿀 데이터는 없습니다(not the case). 반대로 연습장 에러는 이미 답지를 달달 외운 데이터에다가 똑같이 시험을 치는 거라 계산하기 겁나 편합니다. 하지만 Chapter 2에서 봤듯이, 이 집에서만 잘하는 연습장 에러율은 실전 점수와 노골적으로 딴판이고, 심지어 훈련 에러율 지표 녀석은 실전 위기를 새가슴마냥 극도로 은폐 축소(underestimate) 하는 뻔뻔한 조작을 일삼습니다.

In the absence of a very large designated test set that can be used to directly estimate the test error rate, a number of techniques can be used to estimate this quantity using the available training data. Some methods make a mathematical adjustment to the training error rate in order to estimate the test error rate. Such approaches are discussed in Chapter 6. In this section, we instead consider a class of methods that estimate the test error rate by _holding out_ a subset of the training observations from the fitting process, and then applying the statistical learning method to those held out observations. 
방대하고 깔끔한 실전 전용 데이터셋이 씨가 말라버린 흙수저 상황에서, 우리는 호주머니에 있는 훈련 데이터를 쥐어짜 내서라도 실전 에러율을 점쳐볼 스킬들이 필요합니다. 어떤 분파는 훈련 에러율 숫자 자체에 마법의 수학적 뽀샵(mathematical adjustment) 을 가제트 팔처럼 달아서 실전 에러율을 간접 견적 냅니다. 요런 복잡한 마법들은 나중에 Chapter 6에서 씹고 뜯을 겁니다. 그 대신! 이 파트에서 우리가 파고들 비법은, 훈련 캠프에 던져진 녀석 중 일부 엘리트 그룹을 아예 훈련장에 못 들어가게 뒤로 _숨겨(holding out)_ 두었다가, 훈련이 다 끝난 모델을 이 미리 납치해둔 신선한 타겟 관측치들에 충돌시켜 진짜 실전 점수를 채점해 내는 모의고사식 접근법을 마스터하는 겁니다!

In Sections 5.1.1–5.1.4, for simplicity we assume that we are interested in performing regression with a quantitative response. In Section 5.1.5 we consider the case of classification with a qualitative response. As we will see, the key concepts remain the same regardless of whether the response is quantitative or qualitative. 
Sections 5.1.1–5.1.4 구간에선 뇌용량 낭비를 막기 위해 일단 타겟이 눈에 보이는 아날로그 수치(정량적) 인 연속된 '회귀(regression)' 문제에만 몰빵한다고 칩시다. 그러다 마지막 5.1.5 구간에 가면 "떡상인가 떡락인가?" 와 같은 카테고리 꼬리표(정성적) 를 맞추는 '분류(classification)' 판으로 스테이지를 전환합니다. 하지만 까놓고 말해 걱정 마세요. 우리가 배울 핵심 통찰력 뼈대(key concepts)는 과녁이 숫자든 카테고리든 1밀리미터도 변함없이(regardless) 똑같이 굴러가니까요.

---

## Sub-Chapters (하위 목차)

### 5.1.1 The Validation Set Approach (검증 세트 접근법)
* [문서로 이동하기](./5_1_1_the_validation_set_approach/trans2.html)

### 5.1.2 Leave-One-Out Cross-Validation (단일 관측치 제외 교차 검증, LOOCV)
* [문서로 이동하기](./5_1_2_leave-one-out_cross-validation/trans2.html)

### 5.1.3 k-Fold Cross-Validation (k-폴드 교차 검증)
* [문서로 이동하기](./5_1_3_k-fold_cross-validation/trans2.html)

### 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation (k-폴드에서의 편향-분산 트레이드오프)
* [문서로 이동하기](./5_1_4_bias-variance_trade-off_for_k-fold_cross-validation/trans2.html)

### 5.1.5 Cross-Validation on Classification Problems (분류 문제에서의 교차 검증)
* [문서로 이동하기](./5_1_5_cross-validation_on_problems_classification/trans2.html)

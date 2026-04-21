---
layout: default
title: "trans2"
---

# 5.1 Cross-Validation 
# 5.1 교차 검증: 진짜 실전 모의고사로 훈련 거품을 걷어내자!

In Chapter 2 we discuss the distinction between the _test error rate_ and the _training error rate_ .
통계학이라는 치열한 전장에서 가장 중요한 두 가지 오차율, 바로 _'연습 게임 오차율(training error)'_ 과 _'진짜 본선 게임 오차율(test error)'_ 이 두 가지의 치명적인 차이에 대해 우리가 아주 예전인 2장에서 열을 내며 떠들었던 걸 기억하시나요?

The test error is the average error that results from using a statistical learning method to predict the response on a new observation— that is, a measurement that was not used in training the method.
본선 게임(test) 오차란 무엇일까요? 감독이 방구석에서 훈련시킬 땐 단 한 번도 보여준 적 없던 "쌩판 처음 보는 완전히 낯선 상대 팀(새로운 관측치)"을 우리 모델이 맞닥뜨렸을 때 벌어지는 피 터지는 평균 에러율을 의미합니다. 이것이 진짜 우리 팀의 진짜 실력이죠.

Given a data set, the use of a particular statistical learning method is warranted if it results in a low test error.
만약 당신이 만든 통계 모델이 이 지옥 같은 낯선 '본선 게임'에 나가서 엄청나게 낮은 에러율을 기록하며 상대 팀을 씹어 먹는다면? 게임 끝입니다. 당신이 만든 그 모델은 전 세계 어디 내놔도 당당하게 써먹을 자격이 생기는 겁니다(warranted).

The test error can be easily calculated if a designated test set is available.
물론 가장 이상적인 꿈의 시나리오는, 하늘에서 요정이 뚝 떨어져서 "자, 이건 모델 훈련엔 1도 안 쓰고 조이패드도 손 안 대고 꽁꽁 숨겨둔 깨끗하고 거대한 '실전 모의고사 전용 전립 세트'야!" 라고 주어지는 겁니다. 그럼 그냥 여기다 모델을 던져보고 오차를 계산하면 되니까 엄청 쉽겠죠.

Unfortunately, this is usually not the case.
근데 안타깝게도, 피도 눈물도 없는 현실 피드백 세계에선 우리에게 그런 사치스러운 여분의 '비밀 모의고사 데이터' 따윈 주어지지 않습니다. 데이터는 늘 부족하고 배고프니까요!

In contrast, the training error can be easily calculated by applying the statistical learning method to the observations used in its training.
반면에요? 자기네들이 매일 치고받고 뒹굴면서 연습했던 바로 그 '훈련용(Training)' 선후배 관측치들 상대로 에러율을 재는 건 눈 감고도 합니다. 그냥 자기가 풀었던 문제집 다시 돌려서 몇 점 나오나 채점만 하면 되니까요.

But as we saw in Chapter 2, the training error rate often is quite different from the test error rate, and in particular the former can dramatically underestimate the latter. 
여기서 대참사가 벌어집니다! 2장에서 우리가 피눈물 흘리며 봤듯, 맨날 풀던 문제집(훈련 데이터) 에서 나온 100점(낮은 오차) 은 절대 실전 수능(시험 오차) 점수와 가깝지 않습니다. 모델 녀석이 맨날 풀던 문제의 답만 달달 외워버려서 자기가 엄청 잘하는 줄 '과적합(Overfitting)' 에 빠져 오만해지기 때문입니다. 즉 훈련 오차는 본선 오차를 **"에이, 실전도 별거 없네ㅋ"라며 엄청나게 과소평가(underestimates)** 하는 끔찍한 치명타 사기를 칩니다!

In the absence of a very large designated test set that can be used to directly estimate the test error rate, a number of techniques can be used to estimate this quantity using the available training data.
이렇게 실전 수능 난이도를 정확히 재어줄 '대규모 전용 모의고사 데이터'가 씨가 마른 절망적인 현실 속에서 통계학자들은 어떻게든 이 진짜 실전 오차율(test error)을 짐작해 내기 위한 생존 기술들을 연구해 냈습니다. 이 수많은 기법들은 바로 지금 우리 손에 쥐어진 '이 초라하고 뻔한 훈련 데이터' 만을 쥐어짜서 미래를 투시해 내는 마법과도 같죠.

Some methods make a mathematical adjustment to the training error rate in order to estimate the test error rate.
어떤 마법사들은 이 훈련장 에러율 수치에다가 수학적인 페널티(수리적 조정) 마법을 억지로 가미해서 진짜 모의고사 오차를 예측해 내려 발판을 짭니다. (예: "너 문제집은 100점 맞았지만, 내가 수식으로 계산해 보니 꼼수 쓴 거 다 보이네. 넌 실전 가면 70점짜리야!")

Such approaches are discussed in Chapter 6.
이런 복잡한 수식 조정 접근법(AIC, BIC, Adjusted R² 등)은 우리가 추후 6장에서 신나게 씹고 뜯고 파헤칠 내용입니다.

In this section, we instead consider a class of methods that estimate the test error rate by _holding out_ a subset of the training observations from the fitting process, and then applying the statistical learning method to those held out observations. 
**하지만 이번 5장 구역에서 우리가 배울 진짜 기술은 조금 다릅니다.** 
우린 수학 수식으로 장난치는 대신, 우리가 가진 훈련생(데이터) 무리 중에서 일부를 억지로라도 잡아 빼서 **지하 감옥에 강제로 유보시켜 격리 보관(Holding out)** 합니다. 모델이 절대로 못 보게요! 그런 다음 모델이 나머지 데이터로 훈련을 다 마친 순간, 그 컴컴한 지하실에 숨겨둔 녀석들(held out)을 꺼내서 들이밀고 "자, 이 생판 처음 보는 놈들 맞춰봐!" 라며 모델을 두들겨 패는 방식입니다. 이 잔인하고도 확실한 실전 투신 기법들(a class of methods) 의 세계로 들어가 봅시다!

In Sections 5.1.1–5.1.4, for simplicity we assume that we are interested in performing regression with a quantitative response.
다가올 5.1.1 절부터 5.1.4 절까지는, 머리가 아프지 않도록 게임의 룰을 최소한으로 고정하겠습니다. 즉 정답 타깃이 '숫자(양적)' 로 연속해서 떨어지는 '회귀(Regression)' 장르만 죽어라 판다고 임의로 가정하겠습니다. (예: 연속적인 혈압 맞추기)

In Section 5.1.5 we consider the case of classification with a qualitative response.
그리고 마지막 대미를 장식할 5.1.5 절에 도달해서야, 정답이 범주('정상/불량' 같은 질적 타깃) 로 툭 하고 나뉘는 '분류(Classification)' 서바이벌 장르로 넘어갈 것입니다.

As we will see, the key concepts remain the same regardless of whether the response is quantitative or qualitative. 
하지만 결국 나중에 깨달으시겠지만요, 이 '지하 감옥에 가두고 뺑뺑이 돌린다'는 우리의 핵심 코어 컨셉 철학은 타깃이 숫자(회귀) 든 범주(분류) 든 일절 무관하게 완벽하게 똑같이 영원히 관통될 꿀잼 법칙이 될 겁니다!

---

## Sub-Chapters (하위 목차)

### 5.1.1 The Validation Set Approach (검증 세트 접근법)
* [문서로 이동하기](./5_1_1_the_validation_set_approach/)

가장 단순하게 전체 데이터를 절반은 훈련용(Train), 나머지 절반은 검증용(Validation)으로 단 1번 쪼개는 고전적인 분할 방식입니다.
구현하기 무척 쉽지만 관측치 낭비가 크고, 분할 시드에 따라 검증 결과가 심하게 요동치는 치명적인 단점을 살펴봅니다.

### 5.1.2 Leave-One-Out Cross-Validation (단일 관측치 제외 교차 검증, LOOCV)
* [문서로 이동하기](./5_1_2_leave-one-out_cross-validation/)

단 1개의 관측치만 검증 폴드로 빼두고 나머지 수많은 데이터 전체를 훈련에 쏟아붓는 완전형 교차 검증법 수식 체계입니다.
편향 이슈는 거의 해결되나, N번씩 전체 모델을 계속 훈련해야 하므로 연산 비용이 천문학적일 수 있음을 논의합니다.

### 5.1.3 k-Fold Cross-Validation (k-폴드 교차 검증)
* [문서로 이동하기](./5_1_3_k-fold_cross-validation/)

전체 데이터를 균등하게 K개(통상 5~10)의 파티션으로 조각내어 순차적으로 돌아가며 교차 검증하는 최적의 타협안입니다.
LOOCV 대비 연산 소모 구간을 획기적으로 줄여주며, 적정한 분산과 편향 보정 능력을 거두는 기법을 경험합니다.

### 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation (k-폴드에서의 편향-분산 트레이드오프)
* [문서로 이동하기](./5_1_4_bias-variance_trade-off_for_k-fold_cross-validation/)

데이터를 나누는 K 갯수에 따라 편향(Bias) 제어와 예측 분산(Variance) 상승이 어떻게 서로 대치되는지 수리적으로 따져봅니다.
왜 많은 학자들과 현업에서 K=10 혹은 K=5를 압도적인 기본값으로 선택하는지 이론적 이유를 분석합니다.

### 5.1.5 Cross-Validation on Classification Problems (분류 문제에서의 교차 검증)
* [문서로 이동하기](./5_1_5_cross-validation_on_problems_classification/)

그동안 회귀분야 연속 변수(MSE 측도 중심)에서 관찰했던 CV 사이클 테크닉을, 이산적이고 범주형인 오분류율(Error Rate) 척도에 동일하게 전파합니다.
분류 모델들의 초매개변수를 튜닝하고 우수성을 비교하는 통계적 실증 분석입니다.

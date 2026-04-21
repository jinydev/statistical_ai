---
layout: default
title: "2. Statistical Learning"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판' 내비게이션입니다! 원문을 그대로 읽고 싶으시다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 🚀 2. 통계적 학습 세계로의 초대 (Statistical Learning)

환영합니다! 2장에서는 드디어 우리 기계학습의 주인공, '통계적 학습'의 무대로 본격 진입하게 됩니다.
여기서는 컴퓨터가 어떻게 데이터의 규칙 패턴을 찾아서 수학 함수 $f$ 형태로 만들수 있는지, 그리고 그 모델이 맞닥뜨리게 될 편향(고정관념)과 분산(흔들림) 사이의 아슬아슬한 줄다리기(Trade-Off)를 핵심 이야기로 다뤄봅니다.

---

## 🗺️ 2.1 통계적 학습이란 도대체 무엇일까? (What Is Statistical Learning?)
* [문서로 이동하기](./2_1_what_is_statistical_learning/)

어떤 원인(입력)을 넣었을 때, 어떤 결과(출력)가 나올까? 이 둘 사이의 보이지 않는 관계를 하나의 요술 상자(함수 $f$)로 만드는 연습을 합니다. 
결과를 미리 맞추는 '예측'과, 원인이 어떻게 결과에 영향을 미치는지 분석하는 '추론'이라는 멋진 두 가지 방패를 얻게 될 거예요!

### 🎯 2.1.1 굳이 왜 요술 상자 f를 찾아야 해? (Why Estimate f ?)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_1_why_estimate_f/)

아직 일어나지 않은 일을 족집게처럼 예측하는 것도 중요하지만, 대체 '왜' 그런 일이 생겼는지 추론을 통해 원인을 샅샅이 파헤치는 것도 아주 중요하답니다!

#### 🔮 Prediction (내일 일을 맞춰보자!)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_1_why_estimate_f/2_1_1_1_prediction/)

오로지 정답을 예측하는 것에만 집중해 봅니다! 하지만 조심하세요. 세상에는 우리가 어떻게 해도 줄일 수 없는, '신만이 아는 에러(Irreducible Error)'라는 게 존재하거든요.

### 🛠️ 2.1.2 상자 f를 어떻게 만들까? (How Do We Estimate f ?)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_2_how_do_we_estimate_f/)

과거의 경험치(학습 데이터)를 가지고 가장 최고의 요술 상자를 어떻게 조립할 수 있을지 배워봅니다. 
크게 모델의 형태를 먼저 정해놓고 끼워 맞추는 방법과, 데이터가 흘러가는 대로 놔두는 방법으로 나뉩니다.

#### 📐 Parametric Methods (틀 지정 방법론 - 모수적)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_2_how_do_we_estimate_f/2_1_2_1_parametric_methods/)

"이 데이터는 왠지 직선 형태(선형)일 거야!"라고 짐작하고 시작하는 매우 빠른 방법이에요. 하지만 어림짐작이 완전히 빗나가면 결과도 엉망이 될 수 있다는 함정이 있습니다.

#### 🌊 Non-Parametric Methods (자유로운 방법론 - 비모수적)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_2_how_do_we_estimate_f/2_1_2_2_non-parametric_methods/)

특정 형태를 가정하지 않고 그냥 데이터 점들을 유연하게 구불구불 따라가는 방법이에요. 잘만 하면 엄청난 정답률을 보여주지만, 대신 엄청나게 많은 데이터가 필요하답니다.

### ⚖️ 2.1.3 예측 정확도 vs 해석력, 무엇이 중요할까? (The Trade-Off)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/)

맞추기만 잘하면 될까요? 모델이 복잡해질수록(정확도 상승) 모델의 속마음을 들여다보기 어려워집니다(해석력 하락). 이것을 '블랙박스' 현상이라고 부르며, 상황에 따라 여러분은 똑똑한 선택을 내려야 해요.

### 🎓 2.1.4 지도 학습과 비지도 학습 비교 (Supervised vs Unsupervised)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_4_supervised_versus_unsupervised_learning/)

선생님이 정답지를 줘가면서 공부시키는 '지도 학습'과, 아무 힌트 없이 스스로 패턴을 찾아나가는 '비지도 학습'! 아주 다른 성격의 두 학교를 구경해 봅니다. 반반씩 섞인 '반지도 학습'도 있어요.

### 📊 2.1.5 회귀 문제, 아니면 분류 문제? (Regression vs Classification)
* [문서로 이동하기](./2_1_what_is_statistical_learning/2_1_5_regression_versus_classification_problems/)

"집값이 정확히 얼마일까?" 처럼 숫자를 맞추는 건 **회귀(Regression)**이고, "이 사진이 개인가 고양이인가?" 를 나누는 건 **분류(Classification)**입니다. 각 상황마다 여러분이 쓸 수 있는 무기가 완전히 다르답니다.

---

## 🎯 2.2 내가 만든 모델, 얼마나 믿을 수 있을까? (Assessing Model Accuracy)
* [문서로 이동하기](./2_2_assessing_model_accuracy/)

어떤 모델 하나가 모든 분야에서 1등일 수는 없습니다(No Free Lunch!). 이제 우리가 만든 모델의 시험 점수를 매길 수 있는 채점 기준표를 배울 시간입니다. 공부할 때 풀었던 문제집(훈련)과 실전 모의고사(시험) 점수가 왜 다른지 집중적으로 알아봐요!

### 📏 2.2.1 적합도 품질 평가하기 (Measuring the Quality of Fit)
* [문서로 이동하기](./2_2_assessing_model_accuracy/2_2_1_measuring_the_quality_of_fit/)

회귀 문제에서 오차를 재는 만능 자 단위인 평균 제곱 오차(MSE)를 알아봅니다. 결국 모델의 궁극적 목표는 새로운 문제에 적응하는 '일반화' 능력이라는 점을 깊이 다룹니다.

### 🎢 2.2.2 편향과 분산의 줄다리기 (The Bias-Variance Trade-Off)
* [문서로 이동하기](./2_2_assessing_model_accuracy/2_2_2_the_bias-variance_trade-off/)

"고정관념이 강한 모델(편향)"과 "사소한 것에도 민감하게 흔들리는 모델(분산)". 모델이 똑똑(유연)해지면 고정관념은 줄지만, 너무 예민해져서 흔들림이 심해집니다. 이 환장할 U자 형태의 관계를 타파해 봅니다.

### 🔍 2.2.3 분류 환경에서의 평가법 (The Classification Setting)
* [문서로 이동하기](./2_2_assessing_model_accuracy/2_2_3_the_classification_setting/)

분류 문제에서는 단순히 몇 개나 틀렸는지를 세는 '오분류율'을 씁니다. 더불어, 우리가 아무리 똑똑한 모델을 만들어도 뛰어넘을 수 없는 신의 경지, 즉 최소 오차율인 '베이즈 에러율'을 소개합니다.

#### 👥 K-최근접 이웃 알고리즘 (K-Nearest Neighbors)
* [문서로 이동하기](./2_2_assessing_model_accuracy/2_2_3_the_classification_setting/2_2_3_1_k_nearest_neighbors/)

주변에 있는 이웃 $K$명한테 다수결로 물어보고 정답을 결정하는 아주 단순하고 직관적인 친구입니다. 투표권자($K$)의 숫자에 따라 편향-분산 줄다리기가 어떻게 발생하는지 관찰해 봐요!

---

## 🐍 2.3 파이썬 첫 입문 실습 (Lab: Introduction to Python)
* [문서로 이동하기](./2_3_lab_introduction_to_python/)

기계학습 여정에 필요한 코딩 짐싸기! 데이터 분석계의 3대장, NumPy, Pandas, Matplotlib을 처음 만나는 기초 실습 랩(Lab)입니다.

(요약은 하위 챕터 제목들에 기반한 내용으로 이뤄집니다. 주피터 실행법부터 시퀀스 지정, 데이터 로드, 루프문 등 필수 코딩을 손에 익히는 시간입니다.)

---

## 🏋️ 2.4 연습 문제 한 판 승부! (Exercises)
* [문서로 이동하기](./2_4_exercises/)

지금까지 2장에서 배운 편향 및 분산, 유연성의 한계를 실험할 수 있는 흥미진진한 시험장입니다! 배운 지식을 활용해 즐겁게 복습해 봅시다.

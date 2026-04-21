---
layout: default
title: "trans2"
---

[< 2.4 Exercises](../c02/2_4_exercises/trans2.html) | [3.1 Simple Linear Regression >](./3_1_simple_linear_regression/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 원문을 나란히 읽고 싶으시다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 🚀 3. Linear Regression (선형 회귀: 마법의 직선 긋기)

지도 학습의 가장 단순하면서도 기본이 되는 선형 회귀(Linear Regression) 접근법을 다루는 3장입니다.
드디어 머신러닝 요리 학교의 가장 기초적이고 강력한 첫 번째 레시피, **선형 회귀(Linear Regression)** 과정에 오신 것을 환영합니다! 신입 셰프들이 화려한 딥러닝이나 거대한 AI 냄비에 눈독을 들이기 전에, 100년도 넘게 통계학자들의 사랑을 받아온 이 단순하고 우직한 '직선 냄비(Linear Model)'부터 완벽하게 다룰 줄 알아야 합니다.

통계적 학습 모델들의 기초가 되며 양적 변수 예측에서 여전히 강력하고 널리 사용되는 회귀 이론과 평가 지표를 학습합니다.
"TV 광고($X$)를 10만 원어치 하면 내일 우리 식당의 붕어빵($Y$)이 몇 개나 팔릴까?" 이런 단순하고 직관적인 인과관계를 가장 투명하게 보여주는 것이 바로 선형 회귀입니다. 복잡한 딥러닝 블랙박스에서는 알 수 없는, "왜 그런 결과가 나왔는가?"에 대한 완벽한 해석력을 선사해 줄 것입니다!

---

## Sub-Chapters (하위 목차)

### 3.1 Simple Linear Regression (단순 선형 회귀)

* [📖 쉬운 해설판으로 이동하기](./3_1_simple_linear_regression/trans2.html)

단 하나의 입력 변수(X)를 사용하여 반응 변수(Y)를 예측하는 단순 선형 회귀 구조를 알아봅니다.
가장 기본적인 기울기(Slope)와 절편(Intercept)을 활용한 직선 적합 방식을 설명합니다.
머신러닝과 통계적 학습의 세계에서 가장 처음 꺼내 드는 기본 무기! 오직 단 1개의 힌트(원인 변수 $X$)만 쥐고서 수치로 된 결과(응답 $Y$)를 어떻게 때려 맞추는지, 그 직관적인 1차 직선 방정식을 배웁니다.

#### 3.1.1 Estimating the Coefficients (계수 추정)
* [📖 쉬운 해설판으로 이동하기](./3_1_simple_linear_regression/3_1_1_estimating_the_coefficients/trans2.html)

장부에 적힌 200개의 진짜 데이터를 보고, 가장 오차가 적은 최적의 붕어빵 예측 선을 긋기 위해 요술 같은 '최소 제곱법' 마법을 배웁니다.

#### 3.1.2 Assessing the Accuracy of the Coefficient Estimates (계수 추정치의 정확도 평가)
* [📖 쉬운 해설판으로 이동하기](./3_1_simple_linear_regression/3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html)

우리가 그은 가짜 선이 진짜 우주의 법칙과 얼마나 어긋날지(표준 오차, 신뢰 구간) 평가해 보고, 통계 법정에서 가설 검정을 진행합니다.

#### 3.1.3 Assessing the Accuracy of the Model (모델의 정확도 평가)
* [📖 쉬운 해설판으로 이동하기](./3_1_simple_linear_regression/3_1_3_assessing_the_accuracy_of_the_model/trans2.html)

최종적으로 우리 식당의 임시 매상 예측기가 성적표를 받는 날입니다! $R^2$(설명력 점수)와 RSE(오차 단위)라는 잔인한 채점표로 우수성을 평가받습니다.

### 3.2 Multiple Linear Regression (다중 선형 회귀)

* [📖 쉬운 해설판으로 이동하기](./3_2_multiple_linear_regression/trans2.html)

입력 변수가 2개 이상일 때 다수의 예측 변수를 동시에 고려하는 다중 선형 회귀 모델로 확장합니다.
재료가 1개가 아니라, TV도 쏘고, 라디오도 쏘고, 신문도 쏘는 다차원 현실 세계에서의 매출 상승 곡선을 3차원으로 그려냅니다.

#### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)
* [📖 쉬운 해설판으로 이동하기](./3_2_multiple_linear_regression/3_2_1_estimating_the_regression_coefficients/trans2.html)

여러 힌트를 한 번에 다 갈아넣은 거대한 다차원 공간에서, 어떻게 가장 잘 들어맞는 평평한 철판(하이퍼플레인)을 찍어 누를 수 있을지 계산합니다.

#### 3.2.2 Some Important Questions (중요한 질문들)
* [📖 쉬운 해설판으로 이동하기](./3_2_multiple_linear_regression/3_2_2_some_important_questions/trans2.html)

"이 재료 다 넣으면 진짜 맛있어지긴 해?" 등, 다중 모델을 만들었을 때 반드시 맞닥뜨리는 핵심적인 질문 4가지를 단계적으로 짚어봅니다.
(하위 목차: 중요한 변수 결정, 모델 적합성, 예측 등)

### 3.3 Other Considerations in the Regression Model (회귀 모델에서의 기타 고려사항)

* [📖 쉬운 해설판으로 이동하기](./3_3_other_considerations_in_the_regression_model/trans2.html)

단순 수치형 데이터 범위를 넘어서 실제 데이터를 회귀 모델링할 때 마주치는 추가적인 제약과 변수 처리 기법을 소개합니다.
단순히 숫자로만 된 힌트가 아닌 카테고리 데이터나, 시너지 효과 같은 변칙적인 현실 세계의 맹점들을 어떻게 우회할지 고급 스킬들을 펼칩니다.

#### 3.3.1 Qualitative Predictors (정성적 예측 변수)
* [📖 쉬운 해설판으로 이동하기](./3_3_other_considerations_in_the_regression_model/3_3_1_qualitative_predictors/trans2.html)

문자열로 된 카테고리 데이터에 0과 1 스위치(더미 변수)를 달아서 인공지능이 눈치채게 속이는 잔머리 코딩법입니다.

#### 3.3.2 Extensions of the Linear Model (선형 모델의 확장)
* [📖 쉬운 해설판으로 이동하기](./3_3_other_considerations_in_the_regression_model/3_3_2_extensions_of_the_linear_model/trans2.html)

"TV랑 라디오 같이 틀었더니 2배로 잘 팔려!" 같은 둘만의 짬짜미(상호작용 항) 현상이나, 구불구불한 뱀 곡선(다항 회귀)을 억지로 직선 모델에 끼워넣는 강행군을 배웁니다.

#### 3.3.3 Potential Problems (잠재적 문제들)
* [📖 쉬운 해설판으로 이동하기](./3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/trans2.html)

잔차의 이상치, 다중공선성, 분산 팽창 등 훌륭했던 우리 선형 모델을 지옥으로 떨어뜨릴 6가지 무시무시한 치명적 함정들을 진단하고 피하는 법을 배웁니다.

### 3.4 The Marketing Plan (마케팅 플랜 작성)
* [📖 쉬운 해설판으로 이동하기](./3_4_the_marketing_plan/trans2.html)

본 장의 첫 도입부에서 제기했던 마케팅 사장님의 질문들에 대해, 회귀 분석 툴을 돌려 팩트로 두들겨 패며 실무적인 결정을 내리는 통쾌한 결말을 봅니다.

### 3.5 Comparison of Linear Regression with K-Nearest Neighbors (선형 회귀와 K-최근접 이웃 비교)
* [📖 쉬운 해설판으로 이동하기](./3_5_comparison_of_linear_regression_with_k_nearest_neighbors/trans2.html)

각진 직선의 제왕(선형회귀)과 말랑말랑한 다수결의 마법사(KNN)가 맞짱을 뜨면 누가 이길까? 차원의 저주에 걸려 파멸하는 건 과연 누구일지 확인해 봅니다.

### 3.6 Lab: Linear Regression (실습: 선형 회귀)
* [📖 쉬운 해설판으로 이동하기](./3_6_lab_linear_regression/trans2.html)

Statsmodels 라이브러리 등을 활용하여 선형 회귀 분석 프로세스를 파이썬 코드로 어떻게 실행하는지 다루는 기본 랩입니다. 입으로만 배운 선형 회귀를 파이썬 콘솔에서 직접 샌드백 후려치듯 때려보면서 에러를 뿜어내는 실전 놀이터입니다.

### 3.7 Exercises (연습 문제)
* [📖 쉬운 해설판으로 이동하기](./3_7_exercises/trans2.html)

지금까지 배운 선형 회귀에 대한 기초 지식과 실전 감각을 검증합니다. 개념 문제에서는 칠판에 적어가며 수학 귀신들과 싸우고, 응용 문제에서는 파이썬으로 직접 데이터를 구워삶아 봅니다.

[< 2.4 Exercises](../c02/2_4_exercises/trans2.html) | [3.1 Simple Linear Regression >](./3_1_simple_linear_regression/trans2.html)

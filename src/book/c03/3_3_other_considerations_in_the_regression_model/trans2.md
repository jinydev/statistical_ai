---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2.2.3 Four Predictions](../3_2_multiple_linear_regression/3_2_2_some_important_questions/3_2_2_3_four_predictions/trans2.html) | [3.3.1 Qualitative Predictors >](3_3_1_qualitative_predictors/trans2.html)

# 3.3 Other Considerations in the Regression Model

# 3.3 회귀 모델의 다른 고려사항들 (진짜 실전용 비법 소스와 돌발 상황 대처법)

지금까지 우리는 얌전하고 말 잘 듣는 숫자들(연속형 변수)만 가지고 회귀 냄비 요리를 연습해 왔습니다. 하지만 진짜 냉혹한 장사판(실전 데이터)에는 숫자로 딱 떨어지지 않는 골치 아픈 녀석들이나, 우리 모델을 박살 내려는 숨은 지뢰들이 도처에 깔려 있습니다! 이제부터는 이 무시무시한 실전 돌발 상황들을 어떻게 요리하고 헤쳐나갈지 배우는 '고급 비법 비전서' 파트로 들어갑니다.

---

### 3.3.1 Qualitative Predictors (정성적 예측 변수: 숫자가 아닌 수상한 재료들)
* [📖 쉬운 해설판으로 이동하기](./3_3_1_qualitative_predictors/trans2.html)

수치가 아닌 카테고리(범주) 성격을 가지는 정보(성별, 지역, 기분 등)를 어떻게 억지로라도 선형 모형 방정식 냄비에 쑤셔 넣을 수 있을지 그 꼼수인 '더미 변수(Dummy Variable) 스위치' 체계를 배웁니다. 클래스(선택지) 개수에 따른 영리한 변수 조립 생성 규칙을 짚고 넘어갑니다.

### 3.3.2 Extensions of the Linear Model (선형 모델의 확장: 마법의 짬짜면 시너지)
* [📖 쉬운 해설판으로 이동하기](./3_3_2_extensions_of_the_linear_model/trans2.html)

입력 변수들끼리 눈이 맞아서 발생하는 폭발적인 시너지 효과나, 서로 엮여서 떨어지지 않는 찐득한 상호작용 항(Interaction Term)을 어떻게 수식에 부스팅 아이템으로 추가할지 기법을 배웁니다. 너무 뻣뻣했던 가법성(Additivity) 및 선형성(Linearity)이라는 기본 회귀 제약 족쇄를 시원하게 풀어버리는 통쾌함을 경험해 봅니다.

### 3.3.3 Potential Problems (잠재적 문제들: 우리가 만든 요술 냄비의 6가지 맹점)
* [📖 쉬운 해설판으로 이동하기](./3_3_3_potential_problems/trans2.html)

회귀 모델을 날것의 실제 데이터에 막무가내로 들이밀었을 때, 밑바탕 가정이 박살 나며 터지는 대표적인 한계점과 부작용(에러, 이상치, 이단아 등)을 잔혹하게 짚어봅니다. 전체 모델의 신뢰성을 지키기 위해 요리 잔반(잔차)을 현미경으로 들여다보고 진단하는 '잔차 검진법'을 다룹니다.

---

[< 3.2.2.3 Four Predictions](../3_2_multiple_linear_regression/3_2_2_some_important_questions/3_2_2_3_four_predictions/trans2.html) | [3.3.1 Qualitative Predictors >](3_3_1_qualitative_predictors/trans2.html)

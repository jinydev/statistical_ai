---
layout: default
title: "index"
---

# 9.1 Maximal Margin Classifier 

In this section, we define a hyperplane and introduce the concept of an optimal separating hyperplane. 

© Springer Nature Switzerland AG 2023 

367 

G. James et al., _An Introduction to Statistical Learning_ , Springer Texts in Statistics, 

https://doi.org/10.1007/978-3-031-38747-0_9 

368 9. Support Vector Machines 

---

## Sub-Chapters (하위 목차)

### 9.1.1 What Is a Hyperplane? (초평면이란 무엇인가?)
* [문서로 이동하기](./9_1_1_what_is_a_hyperplane/)

p차원 공간 속에서 차원이 (p-1)인 구조제로 평평하게 영역을 양분해주는 초평면의 수학적 정의와 방정식(계수들의 내적 선형 결합)을 확인합니다.

### 9.1.2 Classification Using a Separating Hyperplane (분리 초평면을 이용한 분류)
* [문서로 이동하기](./9_1_2_classification_using_a_separating_hyperplane/)

어떤 관측치 X값이 초평면 방정식에 투입되었을 때 반환되는 부호(양수/음수)를 기반으로 해당 개별 관측치의 종착 클래스 라벨을 결정짓는 원리를 파악합니다.

### 9.1.3 The Maximal Margin Classifier (최대 마진 분류기의 최적화)
* [문서로 이동하기](./9_1_3_the_maximal_margin_classifier/)

마진 구역을 가장자리부터 침범하지 않게 밀어붙여 구성하는 '서포트 벡터'가 어떠한 성질을 가지는지 탐구하며, 해당 모서리 관측치들만이 경계를 결정지음을 배웁니다.

### 9.1.4 Construction of the Maximal Margin Classifier (최대 마진 분류기의 수식적 구축)
* [문서로 이동하기](./9_1_4_construction_of_the_maximal_margin_classifier/)

각 클래스의 마진 너비(M)를 최대화한다는 수학적 목적 제약 함수(Optimization Problem)를 세우고 라그랑주 수식으로 푸는 최적화 틀을 익힙니다.

### 9.1.5 The Non-separable Case (선형 분리가 불가능한 경우 데이터의 한계)
* [문서로 이동하기](./9_1_5_the_non-separable_case/)

클래스들이 완전히 예쁘게 구분되지 않고 뒤엉켜 있어, 어떤 선을 그려도 반드시 마진을 침범하는 현실적인 비분리 데이터 구조상에서의 취약성을 언급합니다.

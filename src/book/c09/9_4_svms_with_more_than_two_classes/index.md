---
layout: default
title: "index"
---

# 9.4 SVMs with More than Two Classes 

So far, our discussion has been limited to the case of binary classification: that is, classification in the two-class setting. How can we extend SVMs to the more general case where we have some arbitrary number of classes? It turns out that the concept of separating hyperplanes upon which SVMs are based does not lend itself naturally to more than two classes. Though a number of proposals for extending SVMs to the _K_ -class case have been made, the two most popular are the _one-versus-one_ and _one-versus-all_ approaches. We briefly discuss those two approaches here. 

384 9. Support Vector Machines 

---

## Sub-Chapters (하위 목차)

### 9.4.1 One-Versus-One Classification (OVO 분류 방식)
* [문서로 이동하기](./9_4_1_one-versus-one_classification/)

모든 K 그룹 클래스들끼리 1대1 데스매치 쌍 콤보를 만들어 수많은 모델을 돌린 뒤 패자부활 다수결 매트릭스로 최종 결론을 짓는 OVO 원리입니다.

### 9.4.2 One-Versus-All Classification (OVA 분류 방식)
* [문서로 이동하기](./9_4_2_one-versus-all_classification/)

나(클래스 A) 대 나머지 전체 공간(All)이라는 K개의 통합 매치 모델만 구축하여 가장 계수 확신 점수가 강력한 클래스를 배정해주는 OVA 판별 로직입니다.

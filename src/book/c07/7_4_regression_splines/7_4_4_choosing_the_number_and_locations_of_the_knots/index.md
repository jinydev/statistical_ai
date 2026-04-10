---
layout: default
title: "index"
---

# _7.4.4 Choosing the Number and Locations of the Knots_ 

When we fit a spline, where should we place the knots? The regression spline is most flexible in regions that contain a lot of knots, because in those regions the polynomial coefficients can change rapidly. Hence, one 

298 7. Moving Beyond Linearity 

---

## Sub-Chapters (하위 목차)

### Natural Cubic Spline (자연 연장 보간 3차 큐빅 스플라인 한계 교정)
* [문서로 이동하기](./7_4_4_1_natural_cubic_spline/)

데이터 밀도가 희박한 양 끝쪽 극단(Boundary) 영역 관측치 부근에서 회귀 추정값 분산이 터지는 것을 봉쇄하고자, 양 경계 밖 궤적은 선형이 되게끔 영구적 제한을 걸어서 구조적 분산을 극약처방하는 튼튼한 스플라인 응용 모델 버전을 살펴봅니다.

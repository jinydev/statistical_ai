---
layout: default
title: "index"
---

# 7.4 Regression Splines 

Now we discuss a flexible class of basis functions that extends upon the polynomial regression and piecewise constant regression approaches that we have just seen. 

---

## Sub-Chapters (하위 목차)

### 7.4.1 Piecewise Polynomials (조각별 데이터 다항식 적합 선분들)
* [문서로 이동하기](./7_4_1_piecewise_polynomials/)

변수 성질 분포가 일어나는 연속적인 공간을 임의의 특정 경곗점인 매듭(Knot)이라 불리는 위치들로 수십 개 나눈 후, 구간마다 서로 다른 성질의 작은 차수(3차 이하 통상) 다항식 선형 조합을 모자이크처럼 모델링하는 방법 모델론입니다.

### 7.4.2 Constraints and Splines (곡선 미분 매끄러움을 위한 제약 조건과 통합 스플라인)
* [문서로 이동하기](./7_4_2_constraints_and_splines/)

조각별 분리식들이 이어지는 K-Knot 결합 지점에서 궤적이 날카롭게 끊기거나 각지지 않게 1차/2차 미분 기울기(평활 제약)가 완벽히 포개어 일치하도록 조절 제약을 가해 매끄러운 곡선 함수(Smooth Spline)를 완성하는 통계 제어법입니다.

### 7.4.3 The Spline Basis Representation (수학 이론 기반 스플라인 모델링 인스턴스 기저식 표현 변환식)
* [문서로 이동하기](./7_4_3_the_spline_basis_representation/)

매듭 제약들을 가지는 이런 복합 스플라인 곡면을 구현하고 일반 오리지널 선형 회귀 모듈 소프트웨어상에서 최적 구동시키고자, 새로운 추가 기저 피처 항인 짤라진 멱함수 체인(Truncated Power Basis)을 데이터 X항에 주입하는 통계 공식적 수학 해부입니다.

### 7.4.4 Choosing the Number and Locations of the Knots (스플라인 휨 굴절을 설계하는 매듭의 적정 분할 개수와 앵커 위치 지정 탐색)
* [문서로 이동하기](./7_4_4_choosing_the_number_and_locations_of_the_knots/)

구간을 섬세하게 분해하는 기준 선점인 임의의 매듭점(Knots)들을 도대체 데이터 어디에, 몇 개나 조밀하게 박아두어야 과적합 없이 안정적으로 함수 결과물이 전개될지, 검증하기 위한 테스트(CV 등) 척도를 소개합니다.

### 7.4.5 Comparison to Polynomial Regression (가성비 입증: 비대 수리 다항식 회귀와 분할 스플라인 간의 잔차 통계 분석적인 성능 곡선 비교)
* [문서로 이동하기](./7_4_5_comparison_to_polynomial_regression/)

차수만 한없이 높이는 단일한 15차 초고도 다항식보다, 작은 차수 매듭을 분할 연결해 K 분절 스플라인으로 모델을 유도하는 쪽이 가장자리 영역 관측 범위 에러 면책율 및 유연성에서 월등히 이점이 많다는 결과를 데이터 시각도로 비교 증명합니다.

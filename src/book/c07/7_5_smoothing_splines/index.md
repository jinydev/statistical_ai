---
layout: default
title: "index"
---

# 7.5 Smoothing Splines 

In the last section we discussed regression splines, which we create by specifying a set of knots, producing a sequence of basis functions, and then using least squares to estimate the spline coefficients. We now introduce a somewhat different approach that also produces a spline. 

---

## Sub-Chapters (하위 목차)

### 7.5.1 An Overview of Smoothing Splines (평활 스플라인 페널티 함수 수리 도출 과정의 핵심 개요)
* [문서로 이동하기](./7_5_1_an_overview_of_smoothing_splines/)

학습 데이터의 모든 포인트 관측치 전체 $N$ 개마다 모두 매듭 K를 하나씩 박아 완전히 지나가는(암기하는) 함수 유연도를 가진 상태에서, 오직 파라미터 람다 조율율만으로 곡선의 오돌토돌함을 평활(Smoothing) 깎는 이론 수식 지도를 배웁니다.

### 7.5.2 Choosing the Smoothing Parameter λ (평활 모델 유연도를 조율 관제하는 하이퍼파라미터 λ 선택 방식 원리)
* [문서로 이동하기](./7_5_2_choosing_the_smoothing_parameter/)

LOOCV 모델 검증 방식을 가장 효율적인 행렬 분할 포맷 계산 비용만으로 동원하여 변동 평활 제어 계수 람다와 이펙티브 자유도(Effective Degrees of Freedom) 수치를 정답화하는 최적 데이터 선택 기준식을 계산 배웁니다.

---
layout: default
title: "index"
---

# 11.5 Regression Models With a Survival Response 

We now consider the task of fitting a regression model to survival data. As in Section 11.1, the observations are of the form ( _Y, δ_ ), where _Y_ = min( _T, C_ ) is the (possibly censored) survival time, and _δ_ is an indicator variable that equals 1 if _T ≤ C_ . Furthermore, _X ∈_ R _[p]_ is a vector of _p_ features. We wish to predict the true survival time _T_ . 

Since the observed quantity _Y_ is positive and may have a long right tail, we might be tempted to fit a linear regression of log( _Y_ ) on _X_ . But as the reader will surely guess, censoring again creates a problem since we are actually interested in predicting _T_ and not _Y_ . To overcome this difficulty, we instead make use of a sequential construction, similar to the constructions of the Kaplan–Meier survival curve in Section 11.3 and the log-rank test in Section 11.4. 

---

## Sub-Chapters (하위 목차)

### 11.5.1 The Hazard Function (위험률 함수)
* [문서로 이동하기](./11_5_1_the_hazard_function/)

특정 시점 $t$까지 생존했을 때, 바로 그 직후 순간에 사건(사망)이 발생할 순간 확률의 척도인 위험 함수 $\lambda(t)$의 정의 및 생존 함수 $S(t)$ 와의 수리적 결합 포인트를 배웁니다.

### 11.5.2 Proportional Hazards (비례 위험 모형 구조체)
* [문서로 이동하기](./11_5_2_proportional_hazards/)

시간에 따른 기본 위험률과 X 변수들에 의한 가중치 효과를 곱 구도로 분리하여 위험률 함수를 단순화 설계하는 비례적 가정법의 메커니즘을 숙독합니다.

### 11.5.3 Example: Brain Cancer Data (사례 연구: 뇌종양 데이터 분석 회귀 모델 시각화)
* [문서로 이동하기](./11_5_3_example_brain_cancer_data/)

실제 뇌종양 환자들의 다양한 변수군과 중도 절단 정보를 콕스 모형에 적합하고 결과 예측 승수들을 통해 기여 인자를 찾아냅니다.

### 11.5.4 Example: Publication Data (사례 연구: 논문 출판 데이터 관측 생존도 포착)
* [문서로 이동하기](./11_5_4_example_publication_data/)

의료만이 아니라 출판이라는 사회적 사건 발생 완료(논문 심사 통과) 시간에도 생존 모형이 작동하는 사례를 관측, 다기종 분야 호환성을 검증합니다.

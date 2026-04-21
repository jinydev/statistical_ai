---
layout: default
title: "trans2"
---

# 6.3.1 주성분 회귀 (Principal Components Regression) 

<div class="code-example" markdown="1">

**고도로 뭉친 데이터 실타래, PCA로 풀기**

**주성분 분석(Principal Components Analysis, 이하 PCA)** 기법은 통계학이나 인공지능(AI) 머신러닝 분야에서 워낙 유명해, 다차원 데이터를 다루는 전문가라면 거의 모르는 사람이 없는 '압축과 요약의 달인' 기법입니다. 수백 수천 개의 복잡하고 거대한 변수들이 가득한 산더미 같은 데이터에서, 가장 중요하고 의미있는 특징(Feature)들만 모아서 소수의 핵심 엘리트 변수 단위 수치(Dimension)로 깔끔하게 압축해내는 기막힌 일처리를 담당하죠.

이 PCA라는 녀석은 사실 본질적으로 정답($Y$)을 모르는 상태에서 특징을 파악하는 '비지도 학습(Unsupervised Learning)' 전용 모델의 대장 격입니다. (이에 대한 자세한 내용은 이 책의 뒷부분인 12장에서 심층적으로 다루게 됩니다.) 

하지만 지금 이 6.3 단원에서는 PCA의 아주 특이한 활약상, 즉 그가 가진 무시무시한 **차원 축소 기술을 회귀 분석(Regression) 모델 에러를 줄이는 족쇄 용도로 활용해 보는 방법**에만 온전히 집중해서 배워봅시다!

</div>

---

## Sub-Chapters (하위 목차)

### 6.3.1.1 주성분 분석 개요 (An Overview of Principal Components Analysis)
* [문서로 이동하기](./6_3_1_1_an_overview_of_principal_components_analysis/)

고도로 연관된 다중 변수들을 데이터 정보 손실 없이 상호 완전히 독립적인(직교) 변수로 압축 변환하는 비지도 분해 기초 기술인 PCA의 성질을 직관적으로 살펴봅니다.

### 6.3.1.2 주성분 회귀 접근 방식 (The Principal Components Regression Approach)
* [문서로 이동하기](./6_3_1_2_the_principal_components_regression_approach/)

PCA를 이용해 만들어진 주성분 다차원 벡터가 타겟 Y 예측 또한 가장 이상적으로 잡아낸다는 강력한 논리 하에, 회귀 모델 내부 분산 확장을 극도로 통제하는 효과입니다.

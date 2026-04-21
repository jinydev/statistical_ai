---
layout: default
title: "trans1"
---

# 6.3.1 주성분 회귀 (Principal Components Regression) 

_Principal components analysis_ (PCA) is a popular approach for deriving a low-dimensional set of features from a large set of variables. PCA is discussed in greater detail as a tool for _unsupervised learning_ in Chapter 12. Here we describe its use as a dimension reduction technique for regression. 
**주성분 분석(Principal components analysis, PCA)** 체계는 방대한 다차원 스케일의 대규모 변수 데이터 세트로부터, 소수 정예로 응축된 저차원(low-dimensional) 특징 군단 세트를 파생 추출 도출(deriving) 해내는 весьма 유명하고 대중적인 분석론(approach) 입니다. 주성분 분석(PCA) 기제 체계는 향후 12장 분량에서 본격적인 **비지도 학습(unsupervised learning)** 용도의 주요 학습 도구로서 아주 비중 있게 심층적으로 상세히 논의 전개 서술(discussed) 될 예정입니다. 현 단원 파트에서는 이 도구를 오직 기존 회귀 기판 분석 목적을 투영 달성 보완하기 위한 일종의 유용한 **차원 축소 기법(dimension reduction technique)** 단위로서 어떻게 쓰는지 그 고유 쓰임새(use)만을 국한시켜 설명 묘사(describe) 해 보겠습니다.

---

## Sub-Chapters (하위 목차)

### 6.3.1.1 주성분 분석 개요 (An Overview of Principal Components Analysis)
* [문서로 이동하기](./6_3_1_1_an_overview_of_principal_components_analysis/)

고도로 연관된 다중 변수들을 데이터 정보 손실 없이 상호 완전히 독립적인(직교) 변수로 압축 변환하는 비지도 분해 기초 기술인 PCA의 성질을 직관적으로 살펴봅니다.

### 6.3.1.2 주성분 회귀 접근 방식 (The Principal Components Regression Approach)
* [문서로 이동하기](./6_3_1_2_the_principal_components_regression_approach/)

PCA를 이용해 만들어진 주성분 다차원 벡터가 타겟 Y 예측 또한 가장 이상적으로 잡아낸다는 강력한 논리 하에, 회귀 모델 내부 분산 확장을 극도로 통제하는 효과입니다.

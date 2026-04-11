# -*- coding: utf-8 -*-
with open(r'd:\site\jinydev\Statistical\src\book\c02\2_2_assessing_model_accuracy\index.md', 'w', encoding='utf-8') as f:
    f.write('''---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 뛰어넘어 매우 광범위하게 확장되는 통계적 학습 방법들을 독자들에게 널리 소개하는 것을 꼽습니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법이 아니라 어째서 이렇게 많은 다른 통계 학습 방법론들을 소개할 필요가 있습니까?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 방법론도 모든 데이터 세트에서 타 방법들을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 한 방법론이 최상으로 작동할 수 있지만, 비슷하면서도 다른 데이터 셋에서는 오히려 또 다른 방식의 성능이 작동할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

결과적으로 어떤 데이터 세트가 주어지더라도 과연 어떤 방식이 최고의 결과물들을 산출해 내는지 판별하고 결정하는 작업은 대단히 중대한 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업 실무에서 통계적 기계 학습을 수행해 작동시킬 시 최상의 접근법을 선택하는 과정은 매우 도전적인 난제 부분들 중 하나일 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이 섹션 구역에서, 우리는 주어진 특정 데이터 세트에 대하여 통계적 학습 절차를 선택함에 있어 제기되는 주요 개념들에 대해 논의합니다.

As the book progresses, we will explain how the concepts presented here can be applied in practice. 

이 책이 전개되어 나아감에 따라, 우리는 여기에 제시된 주요 개념들이 실제에 어떻게 적용될 수 있는지 설명할 것입니다.

---

## Sub-Chapters (하위 목차)

### 2.2.1 Measuring the Quality of Fit (적합성 품질 측정)
* [문서로 이동하기](./2_2_1_measuring_the_quality_of_fit/)

회귀 환경에서 모형의 우수성을 평가할 때 가장 보편적으로 사용되는 척도인 평균 제곱 오차(MSE, Mean Squared Error)를 설명합니다.
단순히 학습 데이터만 잘 맞추는 것보다는 낯선 시험 데이터에도 좋은 성능을 발휘하는 일반화(Generalization)의 중요성을 강조합니다.

### 2.2.2 The Bias-Variance Trade-Off (편향-분산 트레이드오프)
* [문서로 이동하기](./2_2_2_the_bias-variance_trade-off/)

시험 데이터의 오차를 구성하는 본질적인 요소인 편향(Bias)과 분산(Variance) 간의 복잡한 상관관계를 다룹니다.
모델의 유연성이 증가함에 따라 분산은 커지고 편향은 서서히 줄어드는 U자형 검증 곡선(U-Shape)을 수학적으로 탐구합니다.

### 2.2.3 The Classification Setting (분류 환경에서의 평가)
* [문서로 이동하기](./2_2_3_the_classification_setting/)

이산적인 클래스 결과를 예측해야 하는 모델 환경에서 성능을 비교하기 위한 비율 지표인 오분류율(Error Rate)을 도입합니다.
주어지는 데이터 공간 내에서 최적의 예측을 수행하여 최소 한계를 규정하는 베이즈 에러율(Bayes Error Rate)을 학습합니다.
''')

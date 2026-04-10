---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 
# 2.2 모델 정확도 평가 (Assessing Model Accuracy)

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 방대한 통계 책의 장들을 관통해 흐르는 가장 핵심적인 주된 목표 중 하나는 바로 지금 책을 읽는 독자들에게 기본적인 표준 선형 회귀 접근법 수준의 기초 한도를 훨씬 아득히 넘어서 광범위하게 확장되는 아주 다채롭고 폭넓은 분야의 통계적 기계 학습 기법 무리들을 전부 상세히 소개하여 이끌어 주는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

그런데 여기서 의문이 들 수 있는데, 과연 단 하나뿐인 절정의 완벽한 궁극의 _최고(best)_ 방법 기법 무기 하나만을 그저 편하게 제시하고 도입하는 대신 굳이 왜 이렇게나 아주 상이하고 많고 많은 각기 다른 여러 통신 학습 접근 방식 체계들을 이토록 피곤하게 모조리 전부 구구절절 소개해야만 할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

그에 대한 해답의 진리로 통계학계에는 오랜 명언이 있습니다, _통계학 수리 세계에서는 소위 절대적인 공짜 점심(free lunch)이란 결코 일절 없습니다_: 그 말인즉슨 현존하는 그 어떠한 기법의 훌륭한 방법론 수단 하나일지라도, 발생할 수 있는 세상 모든 무수한 가능한 데이터 세트 변곡 확률들의 모든 지표 위에서 다른 나머지 모든 통계 기법들을 전부 모조리 제압하며 군림하거나 절대적으로 우위 지배(dominates)하는 완벽 무적의 단 하나의 기법은 절대 결코 단 하나도 존재하지 않습니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

다시 말해 조사 대상인 어느 아주 특수한 무작위 데이터 세트 조사상에서는 특정하게 맞춰진 어떤 단일 분석 방법 하나가 월등히 눈부시게 최상의 성과로 가장 강력하게 잘 작동할 지도 모르지만, 조금만 시선을 돌려 그와 언뜻 매우 겉보기에 아주 비슷해(similar) 보일지라도 내면은 전혀 다른 구조의 낯선 외부 다른 데이터 세트로 옮겨졌을 때에는 오히려 다른 부류의 엉뚱한 분석 기법 방법이 이전의 것보다 월등히 더 훌륭하게 측정 능력을 기막히게 더 잘 발휘하며 작동(work better)할 수도 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 이러한 불확실한 학계 상황 속이기 때문에, 임의로 주어지고 할당된 그 어떠한 유형의 특수 데이터 환경 세트에 직면해서라도 과연 가장 최적절한 어느 분석 방법 모형이 이 데이터에서 최고의 도출 성과 결과를 훌륭히 뽑아 생산해 낼 것인지를 판단하고 결정하는 식별 작업 능려이야말로 가장 최우선시 다루어질 매우 몹시 엄청나게 중대한 임무 지표 작업(important task)입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

이러한 지독한 난제 지표 환경을 고려해 실전의 복합 산업 환경 통계학(in practice)에서, 이렇게 가장 훌륭한 최적의 접근 분석 모델 구축 방법을 눈여겨 골라내는 작업은 통계적 예측 구축 학습을 실제 현장에서 온전히 제대로 수행하는 데 있어 가장 엄청난 집중과 고난을 요구하는 가장 파급력 높고 시련 깊은 도전적인 최고의 난관(most challenging parts) 문제 부분 요소 중 하나로 자연스레 심장하게 도달할 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이어질 이 핵심 파트 부분 섹션에서는 특정하게 구조화된 조사 지표 데이터 세트에 대해 전격적으로 투입할 가장 파급력 있는 효과적인 통계적 학습 분석 도출 절차 방식을 선택하는 치열한 고난 과정에서 기인하여 필연적으로 복합 발생하게 되는 일부 가장 중요 핵심 중심인 개념들에 대해 더욱 본격적이고 심도 깊게 거론하며 논의를 전개합니다.

As the book progresses, we will explain how the concepts presented here can be applied in practice. 

또한 장차 지속적으로 이어질 이 책의 전개 과정 진도가 차츰 점차가면서 계속 계속 거듭 책이 거듭 진행됨에 따라(As the book progresses), 우리는 여기서 지금 제시했던 이러한 추상적 개념들이 과연 어떻게 철저한 산업의 현장 등 실제 복합 환경(in practice)에서 구체적 도구로 강력하게 실제로 직접 전격 응용 산입 적용될 수 있는지 그 체계들을 아주 상세히 실전 형식으로 강령케 풀어 설명할 것입니다.

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
주어진 데이터 공간 내에서 최적의 예측을 수행하여 최소 한계를 규정하는 베이즈 에러율(Bayes Error Rate)을 학습합니다.

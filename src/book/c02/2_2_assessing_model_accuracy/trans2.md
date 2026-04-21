---
layout: default
title: "trans2"
---

[< 2.1.5 Regression Versus Classification Problems](../2_1_what_is_statistical_learning/2_1_5_regression_versus_classification_problems/trans2.html) | [2.2.1 Measuring The Quality Of Fit >](2_2_1_measuring_the_quality_of_fit/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 2.2 Assessing Model Accuracy
# 2.2 모델 정확도 평가 (우리가 만든 기계가 똥인지 된장인지 찍어 먹어보기)

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.
이 지루한 책이 독자분들의 머리에 욱여넣고 싶은 궁극적인 목표 중 하나는 이겁니다. "제발 옛날 할아버지들이 쓰던 구닥다리 선형 회귀 하나만 파지 말고, 온갖 별의별 기상천외한 **광범위한 기계 학습 스킬들**을 좀 구경해 보라!"는 거죠.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?
아니, 근데 귀찮게 왜 그 수많은 기법들을 다 배워야 합니까? 그냥 무결점의 우주 최강 **_'단 하나의 완벽한 방법(best method)'_** 하나만 딱 짚어주면 그거 하나만 밤새워 외워서 평생 우려먹으면 안 되나요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.
어림없는 소리! 통계학계의 가장 유명한 명언이 하나 있습니다. **_"통계학에 공짜 점심은 없다!(There is no free lunch in statistics)"_** 라는 말이죠. 이 말인즉슨, 세상에 존재하는 수만 가지 데이터의 종류를 다 씹어 먹으면서 항상 승률 100%를 찍는 '만능 사기캐 기법' 따위는 세상 어디에도 존재하지 않는다는 겁니다.

On a particular data set, one specific method 스may work best, but some other method may work better on a similar but different data set.
어떤 A라는 동네 아저씨 데이터에서는 딥러닝 봇이 압도적으로 1등을 쳐먹을 수 있지만, 바로 옆 동네 B 아줌마 데이터로 넘어가면 놀랍게도 그 딥러닝 봇이 개털리고 오히려 가장 구닥다리 방식의 고물 봇이 압도적으로 승리하는 기현상이 밥 먹듯이 일어납니다.

Hence it is an important task to decide for any given set of data which method produces the best results.
그렇기 때문에 도대체 **"우리 눈앞에 떨어진 이 낯선 데이터에는 어떤 무기(기법)를 쥐어줘야 가장 대박(최고 결과)을 칠까?"**를 기가 막히게 눈치채고 골라내는 것이 분석가의 생명줄이자 가장 중요한 퀘스트가 되는 겁니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice.
사실 실전 필드에 나가면, 수식 푸는 것보다 이 "어떤 모델 카드를 뽑아 들어야 하나?" 고민하며 제일 좋은 도구를 **선택**하는 과정이 등골이 가장 서늘해지는 최악의 고난이도 작업입니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.
자, 그래서 이번 섹션에서는 특정 데이터를 만났을 때 "이놈한텐 이 무기를 써야 해!" 하고 고를 때 여러분의 뒤통수를 지배해야 할 **가장 뼈대가 되는 철학적 개념들** 몇 가지를 썰로 풀어보겠습니다.

As the book progresses, we will explain how the concepts presented here can be applied in practice.
책을 한 장 한 장 넘기다 보면, 여기서 뜬구름 잡듯 던져드린 개념들이 실전 코딩에서 도대체 어떻게 쓰이는지 온몸으로 깨닫게 해드리겠습니다.

---

### 2.2.1 Measuring the Quality of Fit (적합성 품질 측정: 내 기계에 점수 매기기)
우리가 숫자 표적(회귀 환경)을 맞추는 기계를 만들었을 때, "너 몇 점짜리 기계야?" 하고 채점할 때 전 세계가 쓰는 국민 채점표인 **평균 제곱 오차(MSE)** 란 무엇인지 구경해 봅니다.
그리고 연습 문제만 100점 맞는 헛똑똑이 말고, 처음 보는 수능 실전 문제(시험 데이터)에서도 점수를 잘 뽑는 이른바 **일반화(Generalization)** 의 위대함에 대해 밑줄 치며 배웁니다.

### 2.2.2 The Bias-Variance Trade-Off (편향-분산 트레이드오프: 융통성과 고집 사이의 시소게임)
시험 날(시험 데이터) 점수를 다 까먹어버리게 만드는 두 명의 악마, 똥고집쟁이 **'편향(Bias)'** 과 팔랑귀 **'분산(Variance)'** 의 미칠 듯한 줄다리기 관계를 파헤칩니다.
기계가 지나치게 말랑말랑(유연) 해지면 똥고집(편향)은 깎이지만 대신 팔랑귀(분산)가 폭발해버리는, 통계학 역사상 가장 아름답고도 무서운 **U자형 검증 곡선**의 비밀을 눈으로 확인하게 될 겁니다.

### 2.2.3 The Classification Setting (분류 환경에서의 평가: O/X 퀴즈의 세계)
이번엔 숫자가 아니라 "개야? 고양이야?"(이산적 클래스)를 식별하는 환경에서 기계에게 점수를 매기는 가장 단순하고 잔인한 방식, **오분류율(Error Rate, 즉 오답률)** 에 대해 배웁니다.
그리고 아무리 신의 경지에 오른 AI라 할지라도 우주의 운빨 때문에 절대 넘을 수 없는 '신이 정한 오답의 한계선', 즉 **베이즈 에러율(Bayes Error Rate)** 이란 넘사벽에 대해서도 경건하게 배워봅니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.5 Regression Versus Classification Problems](../2_1_what_is_statistical_learning/2_1_5_regression_versus_classification_problems/trans2.html) | [2.2.1 Measuring The Quality Of Fit >](2_2_1_measuring_the_quality_of_fit/trans2.html)

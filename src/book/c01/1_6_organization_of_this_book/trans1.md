---
layout: default
title: "trans1"
---

[< 1.5 Notation And Simple Matrix Algebra](../1_5_notation_and_simple_matrix_algebra/trans1.html) | [1.7 Data Sets Used In Labs And Exercises >](../1_7_data_sets_used_in_labs_and_exercises/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Organization of This Book

# 책의 구성

Chapter 2 introduces the basic terminology and concepts behind statistical learning.

2장에서는 방대한 통계적 학습의 배경이 되는 다양한 기초 용어와 중요 개념들을 전반적으로 소개합니다.

This chapter also presents the $K$-nearest neighbor classifier, a very simple method that works surprisingly well on many problems.

이 장에서는 수많은 문제들에서 의외로 꽤나 훌륭하게 작동하는 매우 간단한 방식인 $K$-최근접 이웃 분류기($K$-nearest neighbor classifier) 기술도 선보일 예정입니다.

Chapters 3 and 4 cover classical linear methods for regression and classification.

3장과 4장에서는 데이터 회귀 분석(regression) 및 데이터 분류(classification)를 위한 여러 다채로운 고전적인 선형 방법들을 상세하게 설명하고 다룹니다.

In particular, Chapter 3 reviews linear regression, the fundamental starting point for all regression methods.

그중에서, 3장은 이 세상 모든 회귀 방법 분석의 필연적인 출발점이라 할 수 있는 근본 원리인 선형 회귀에 관해 자세하게 복습하는 시간을 준비했습니다.

In Chapter 4 we discuss two of the most important classical classification methods, logistic regression and linear discriminant analysis.

나아가 4장에서는 데이터 분류의 고전 방법 중 가장 중요하게 꼽히는 로지스틱 회귀(logistic regression)와 선형 판별 분석(linear discriminant analysis) 기술 등 두 가지에 관하여 면밀히 논의합니다.

A central problem in all statistical learning situations involves choosing the best method for a given application.

우리에게 직면한 모든 통계적 학습의 환경 및 상황에서 필히 마주하게 되는 최우선의 핵심적 문제는 당면한 특정 애플리케이션의 목표 과제를 처리하기 위하여 알맞고 최적화된 최상의 분석 기법을 올바르게 선택하는 결정과 관련이 있습니다.

Hence, in Chapter 5 we introduce cross-validation and the bootstrap, which can be used to estimate the accuracy of a number of different methods in order to choose the best one.

그러므로 5장에서 우리는 이런 최선의 최고의 기술 방법을 적절하게 선택할 목적으로 다양한 여러 예측 방법의 최종 정확도를 사전에 추정하고 확인하는 데 요긴하게 사용될 수 있는 교차 검증(cross-validation)이라는 기술과 그리고 붓스트랩(bootstrap) 개념을 소개할 것입니다.

Much of the recent research in statistical learning has concentrated on non-linear methods.

통계적 학습의 최근 많은 주요 연구들은 대부분이 비선형(non-linear) 형태의 방법들을 집중해서 이루어지고 있습니다.

However, linear methods often have advantages over their non-linear competitors in terms of interpretability and sometimes also accuracy.

그러나 역설적으로 선형 모델 방법은 비선형 경쟁 방식들에 비해서 높은 해석 가능성 측면, 그리고 종종 정확도 측면에서도 몇몇 뚜렷한 유리한 우위의 이점을 자주 나타내기도 합니다.

Hence, in Chapter 6 we consider a host of linear methods, both classical and more modern, which offer potential improvements over standard linear regression.

따라서 비교적 뒤쪽의 6장에서는 기존의 전통적 기준 선형 회귀보다 확연한 잠재적인 상당한 성능 개량을 제공할 수 있는 고전 기술뿐 아니라 새롭고 참신한 비교적 최신의 현대적인 방법을 아우르는 선형 모델 방법군의 다각적 모음들을 종합적으로 샅샅이 살펴보도록 할 것입니다.

These include stepwise selection, ridge regression, principal components regression, and the lasso.

여기에는 당연하게도 단계적 변수 선택법(stepwise selection), 릿지 회귀(ridge regression), 주성분 회귀(principal components regression) 그리고 라쏘(lasso) 등이 모두 포함됩니다.

The remaining chapters move into the world of non-linear statistical learning.

남은 장들은 우리를 복잡한 비선형적 방식의 통계 학습 환경의 세계로 이끌어 인도하게 됩니다.

We first introduce in Chapter 7 a number of non-linear methods that work well for problems with a single input variable.

먼저 7장에서 단 하나의 단일 입력 변수로 이루어진 간단한 문제에 특히 능숙하고 뛰어난 여러 가지의 수많은 비선형 모델 방식들에 관하여 처음으로 가벼운 안내와 소개를 제시하겠습니다.

We then show how these methods can be used to fit non-linear additive models for which there is more than one input.

그런 다음 이렇게 앞서 배운 선행 기법들이 도대체 어떠한 과정들을 거쳐 단일 입력이 아닌, 즉 다수의 매개 여러 압력 데이터들을 전제로 하여 성립하고 도출되는 비선형 가법 모델(non-linear additive models)들을 적합시키는 데 얼마나 매력적으로 적용되고 활용될 수 있는지를 명백하게 입증해보일 예정입니다.

In Chapter 8, we investigate tree-based methods, including bagging, boosting, and random forests.

아울러 8장에서는 유명한 배깅(bagging), 부스팅(boosting), 그리고 여러 그루의 나무로 이루어진 랜덤 포레스트(random forests) 등의 모델을 폭넓게 포괄하는 다양한 다채로운 나무(tree) 기반의 분류 및 탐색 방법론들을 치밀하게 연구하고 면밀히 조사할 수 있는 시간을 마련했습니다.

Support vector machines, a set of approaches for performing both linear and non-linear classification, are discussed in Chapter 9.

한편 선형적 분류 데이터 및 또한 선형 구조의 형태가 아닌 여러 비선형의 분류와 분석을 매끄럽게 수행하는 복합적 접근 기술 모델 세트의 하나인 서포트 벡터 머신(Support vector machines)의 경우, 9장에서 집중적으로 거론하며 심도 있게 논의하도록 배치하였습니다.

We cover deep learning, an approach for non-linear regression and classification that has received a lot of attention in recent years, in Chapter 10.

그리고 최근 몇 년간 엄청난 각광과 헤아릴 수 없는 막대한 지대한 관심을 집중적으로 쏟아져 받아왔던 강력하고 파괴적인 비선형 기반 기술의 회귀 및 분류 학습의 최첨단 접근 방식인 딥 러닝(deep learning)에 대해서는 나중의 10장에서 본격적이고 비중 있게 심화하여 다뤄보겠습니다.

Chapter 11 explores survival analysis, a regression approach that is specialized to the setting in which the output variable is censored, i.e. not fully observed.

더하여 특수한 목적으로 주로 활용되는 11장은 특별한 상황의 한계 환경, 다시 말해 특정 목푯값 데이터인 결과 응답 출력 변수가 애초에 고의나 실수로 심하게 누락 및 통제되거나 절단, 검열되는, 즉 결코 완전히 그 자체로 관찰되지 않는 특수한 설정의 상황에서 아주 한정적으로 전문화하여 대개 맞춰져 설계된 하나의 유별난 회귀 접근론 형태인, 생존 분석(survival analysis)이란 기법에 관한 이론적 방법론을 진지하게 탐색해 봅니다.

In Chapter 12, we consider the unsupervised setting in which we have input variables but no output variable.

마지막 부분의 초입인 12장에 가서는 데이터의 집합에 오로지 결과 정답지가 없는 단일한 입력들의 관측 변수 집합만 존재하고, 매칭되는 적당한 답론지 결과의 출력 변수가 전혀 전무한 특별한 상황 설정의 환경을 대전제로 취하는 지도받지 않은 비지도 학습(unsupervised learning)이라 칭하는 상황에 관한 고찰을 면밀히 고려하고자 심사숙고해 봅니다.

In particular, we present principal components analysis, $K$-means clustering, and hierarchical clustering.

특별하게 그 중에서도 돋보이게 이 챕터 내에서 우리는 저명한 군집 및 압축 분해의 고차원 기술인 고유의 주성분 분석(principal components analysis), 데이터의 이웃을 찾아 떠나는 $K$-평균 군집화($K$-means clustering), 그리고 데이터를 계층적으로 나누고 응집하는 병합 기반 방식의 계층적 군집화(hierarchical clustering)를 순차적으로 제시해 줄 것입니다.

Finally, in Chapter 13 we cover the very important topic of multiple hypothesis testing.

최종적으로 대망의 마지막 끝인 13장에서는 데이터 분석가들이 현실의 수많은 난제에 통계적으로 대처할 가장 실질적으로 아주 중요한 기초 논의 주제로 손꼽히는 여러 다중의 가정을 세우고 가설 검증(multiple hypothesis testing)의 주제에 대해 중요하게 심도 있게 다뤄 보겠습니다.

At the end of each chapter, we present one or more Python lab sections in which we systematically work through applications of the various methods discussed in that chapter.

본 텍스트의 각 단계별 해당 장이 마무리되는 끝 지점에 가서 우리는 한 개 혹은 그 이상의 파이썬 실습 연구실 랩(Python lab) 섹션을 전향적으로 배치해 두었으며, 이를 통해 우리는 해당 장 내에서 앞서 중요하게 논의된 온갖 여러 복잡한 방법들의 현실 시스템에 맞춘 응용 실험에 대한 체계적인 연습과 작업을 함께 풀어가고 전개할 것입니다.

These labs demonstrate the strengths and weaknesses of the various approaches, and also provide a useful reference for the syntax required to implement the various methods.

본서의 이러한 각 실습의 장(labs)들은 다양한 이론적 접근에 따르는 그들 간의 확연한 장점 및 필연적 단점을 적나라하게 입증하고 지적해 보일 것이며, 그리고 나아가 다양한 해당 방식의 방법론들을 실제로 손수 스스로 실현하고 구현해 내는 데 필요한 여러 기본적 핵심 코드 문법(syntax)에 대한 무척이나 유용한 참조 지식을 더불어 함께 제공해 줄 수 있을 것입니다.

The reader may choose to work through the labs at their own pace, or the labs may be the focus of group sessions as part of a classroom environment.

무엇보다 이렇게 서술된 구문과 내용에 대하여 학습을 수행하는 그 어느 독자라도 본인만의 소화 속도와 보폭의 방식에 맞추어 자신만의 고유한 진도와 속도로 진행해 나가며 하나하나 찬찬히 차근하게 랩 실습 과정들을 스스로 진행하며 연구하는 것을 편안하게 자유 의지로 선택할 수 있으며, 또는 여러 강단의 교과 학습 환경의 한 가지 과정으로써 단체의 여러 다중 사용자와 구성원이 다함께 스터디하는 집중적인 수업 세션의 필수 핵심 학습 과제와 주요한 구심점으로 사용되는 것 또한 아주 적당할 수 있습니다.

Within each Python lab, we present the results that we obtained when we performed the lab at the time of writing this book.

아울러 덧붙이자면 우리는 본 책의 각각 구성된 여러 Python 중심 랩 범위 내에서 우리가 해당 서적을 실제로 저술해 나가는 과정의 해당 당시의 특정 과거 시점에 맞춰 랩을 수행하고 진행하였을 때 성공적으로 확보하고 얻증명해 냈던 그 당시 그 시절의 결과물들을 있는 그대로 여실히 제시하고 있습니다.

However, new versions of Python are continuously released, and over time, the packages called in the labs will be updated.

그러나 알다시피 언어의 신규 생태계는 살아 움직이므로 파이썬 언어의 새로운 상위 추가 버전은 계속 쉴새 없이 출시되고 있으며, 이러한 시대와 세월에 따른 시간의 경과에 비례하여 랩에서 필수적으로 불려와 호출하고 응용하는 수많은 외부 패키지 모듈들은 지속해서 진화 및 업데이트될 것임이 자명합니다.

Therefore, in the future, it is possible that the results shown in the lab sections may no longer correspond precisely to the results obtained by the reader who performs the labs.

따라서 머지않은 장래 미래의 임의의 시점에 직접 랩 작업들을 수행하고 연습하는 모든 실제 예비 독자들이 최종적으로 확보하게 될 실제 출력 도출의 결과값들이 본서의 정해진 실습 섹션에 명시된 책의 표시된 결과값 기록 내용과 더 이상은 전혀 정확하거나 일치하지 않을 수 있는 필연적 가능성도 충분히 도래할 수 있습니다.

As necessary, we will post updates to the labs on the book website.

이러한 문제가 생기는 그 즉시 필요한 경우 필요할 때마다 우리는 책 전용 공식 웹사이트에 랩 실습 스크립트에 대한 다양한 수정 최신 변경 업데이트 내역들을 게시하고 지속적인 소통을 이어 나가겠습니다.

We use the * symbol to denote sections or exercises that contain more challenging concepts.

우리는 본문에 특별히 별표 모양의 * 기호를 덧붙여서 한층 더 엄청난 심화 구조의 더욱 도전적으로 어려운 학구적 개념들을 포함하여 다루고 있는 고난도 개념의 섹션이나 여러 심화 실습 문제들을 따로 지정하여 표기하려 사용했습니다.

These can be easily skipped by readers who do not wish to delve as deeply into the material, or who lack the mathematical background.

이렇게 높은 수준의 이러한 사항들은 복잡한 심화 자료 깊숙이까지 파고들어 자세히 파헤치거나 깊게 연구하기를 희망하지 않거나, 다소 이를 이해할 만한 엄밀한 수학에 대한 학문적 지식 배경이 조금 상대적으로 부진하고 부족한 평범한 독자들의 경우에는 손쉬우면서도 가뿐하게 건너뛰어도 하등의 크게 장애가 지장이 없는 문제 될 것 없는 사항들입니다.

---

## Sub-Chapters (하위 목차)

[< 1.5 Notation And Simple Matrix Algebra](../1_5_notation_and_simple_matrix_algebra/trans1.html) | [1.7 Data Sets Used In Labs And Exercises >](../1_7_data_sets_used_in_labs_and_exercises/trans1.html)

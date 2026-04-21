---
layout: default
title: "trans2"
---

[< 2.1.4 Supervised Versus Unsupervised Learning](../2_1_4_supervised_versus_unsupervised_learning/trans2.html) | [2.2 Assessing Model Accuracy >](../../2_2_assessing_model_accuracy/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 2.1.5 Regression Versus Classification Problems
# 2.1.5 회귀 문제 대 분류 문제 (숫자를 맞출래? 정답을 고를래?)

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).
세상의 변수(데이터)들은 딱 두 가지 성격 중 하나로 성향이 갈립니다. 줄자로 길이를 잴 수 있는 **양적(quantitative)** 변수이거나, 아니면 피를 나눌 수 없는 혈액형처럼 종류를 나누는 **질적(qualitative)** 변수 (다른 말로 **범주형(categorical)** 변수라고도 함) 둘 중 하나죠.

Quantitative variables take on numerical values.
'양적(quantitative)' 변수라는 건 아주 단순하게 말해서 그냥 우리가 흔히 아는 숫자가 달린 값들입니다. 더하고 빼는 게 의미가 있죠.

Examples include a person's age, height, or income, the value of a house, and the price of a stock.
예를 들자면 동네 아저씨의 나이나 키, 지갑 속에 든 수입, 요즘 떡상 중인 아파트 시세나 내일의 삼성전자 주식 가격 같은 것들이 다 양적 변수입니다.

In contrast, qualitative variables take on values in one of _K_ different _classes_, or categories.
반대로 '질적(qualitative)' 변수는 숫자로 더하고 뺄 수 없는, 그냥 $K$ 개의 서로 다른 **'팀(클래스, class)'** 이나 종류(카테고리)의 이름표들입니다.

Examples of qualitative variables include a person's marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).
예를 들면 이 사람이 유부남인지 솔로인지(결혼 유무), 아이폰충인지 갤럭시아재인지(구매 브랜드), 신용불량자로 파산할지 말지(예/아니오), 또는 병원에 실려 왔을 때 단순 감기인지 코로나인지 백혈병인지(질병 진단명) 같은 것들이죠! 이것들은 숫자로 평균을 낼 수 없잖아요?

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.
자, 여기서 통계학의 중요한 단어가 두 개 튀어나옵니다. 우리가 최종적으로 맞춰야 할 정답지(응답)가 주식 가격처럼 '양적(숫자)'이라면 우린 그걸 **'회귀(Regression)'** 문제라고 부릅니다. 반대로 맞춰야 할 정답이 "이 사진이 개냐, 고양이냐?"처럼 '질적(팀 고르기)'이라면 우린 그걸 **'분류(Classification)'** 문제라고 부르죠.

However, the distinction is not always that crisp.
근데 세상일이 원래 칼로 무 자르듯 항상 예쁘게 딱 떨어지는 건 아닙니다. 약간 박쥐 같은 녀석들이 있거든요.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.
예를 들어 3장에서 배울 '최소 제곱 선형 회귀'는 이름값대로 양적(숫자) 정답을 맞출 때 쓰는 정통 회귀 기법인데 반해, 4장에서 만날 **'로지스틱 회귀'** 는 주로 예/아니오 같은 질적(이진, 두 가지 팀) 정답을 고를 때 쓰는 녀석입니다.

Thus, despite its name, logistic regression is a classification method.
어라? 이름에 떡하니 '회귀'라고 쓰여 있는데도, 이 로지스틱 회귀는 사실 '회귀'가 아니라 개/고양이를 분류하는 **분류 기법**인 셈입니다. 완전 사기죠?

But since it estimates class probabilities, it can be thought of as a regression method as well.
하지만 반전의 반전! 이 녀석이 "이 사진이 개일 확률이 80%입니다"라고 소수점 쫙 뽑힌 '숫자(확률)'를 추정해 주기 때문에, 넓게 보면 또 양적인 숫자를 뽑아내는 회귀 기법이라고 우겨도 말이 됩니다. 결국 코에 걸면 코걸이인 셈이죠.

Some statistical methods, such as _K_-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses.
어떤 통계 기법들, 예를 들어 나중에 배울 **'K-최근접 이웃'**(2장, 4장)이나 짱 센 '부스팅'(8장) 같은 녀석들은 아예 스위치를 달아놓고 있어서, 숫자를 때려 맞추는 회귀 문제든 팀을 가르는 분류 문제든 둘 다 씹어 먹는 만능 플레이어 역할을 합니다.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.
일반적으로 우리는 맞춰야 할 과녁(응답)이 숫자인지 팀 이름인지에 따라서 적합한 무기(통계 학습 기법)를 골라 잡습니다. 과녁이 숫자면 선형 회귀 총을 들고, 과녁이 O/X면 로지스틱 회귀 총을 드는 식으로요.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.
하지만 반대로 우리가 쥐고 있는 힌트들(예측 변수, $X$)이 숫자인지 단어인지는 기계 입장에선 솔직히 별로 찌질한 문제라 안 중요합니다. 

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.
이 책에서 다루는 거의 모든 기계 학습 기법들은 힌트의 타입이 숫자든 글자든 가리지 않고 꿀꺽꿀꺽 잘 소화합니다. 단, 한 가지 조건이 있죠. 우리가 글자로 된 질적 힌트(예: 혈액형 A형, B형)를 분석기에 넣기 전에, 기계가 알아먹을 수 있게 그냥 1번, 2번 같은 숫자로 적당히 **'코드화(코딩)'** 만 예쁘게 포장해서 먹여주면 장땡이라는 겁니다!

This is discussed in Chapter 3.
이 야비하게 글자를 숫자로 둔갑시키는 꼼수 기술(가변수 코딩 등)에 대해선 3장에서 썰을 풀도록 하겠습니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.4 Supervised Versus Unsupervised Learning](../2_1_4_supervised_versus_unsupervised_learning/trans2.html) | [2.2 Assessing Model Accuracy >](../../2_2_assessing_model_accuracy/trans2.html)

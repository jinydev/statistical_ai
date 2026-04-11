---
layout: default
title: "index"
---

# _2.1.5 Regression Versus Classification Problems_ 

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 이거나 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려짐)으로 구분될 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적 값들을 가집니다.

Examples include a person's age, height, or income, the value of a house, and the price of a stock.

예시들에는 사람의 나이, 키, 또는 소득, 집의 가치, 그리고 주식의 가격이 포함됩니다.

In contrast, qualitative variables take on values in one of _K_ different _classes_, or categories.

대조적으로 질적 변수들은 _K_ 개의 서로 다른 _클래스들(classes)_, 또는 범주들 중 한 값을 가집니다.

Examples of qualitative variables include a person's marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수들의 예로는 사람의 결혼 상태(기혼 또는 미혼), 구매한 제품의 브랜드(브랜드 A, B, 또는 C), 빚의 채무 불이행 여부(예 또는 아니오), 또는 암 진단(급성 골수성 백혈병, 급성 림프모구 백혈병, 또는 백혈병 없음)이 포함됩니다.

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적 응답을 갖는 문제들을 _회귀(regression)_ 문제들로 언급하는 경향이 있는 반면, 질적 응답을 수반하는 문제들은 종종 _분류(classification)_ 문제들로 불립니다.

However, the distinction is not always that crisp.

그러나 그 구분이 항상 그렇게 명확한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 선형 회귀(3장)는 양적 응답과 함께 사용되는 반면, 로지스틱 회귀(4장)는 일반적으로 질적(두 개의 클래스, 또는 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

따라서 이름에도 불구하고 로지스틱 회귀는 분류 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

그러나 클래스 확률들을 추정하기 때문에, 그것은 회귀 방법으로도 생각될 수 있습니다.

Some statistical methods, such as _K_-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses.

_K_-최근접 이웃(2장 및 4장)과 부스팅(8장)과 같은 일부 통계적 방법들은 양적 혹은 질적 응답들의 경우 둘 다에서 사용될 수 있습니다.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 응답이 양적인지 질적인지에 기초하여 통계적 학습 방법들을 선택하는 경향이 있습니다; 즉 응답이 양적일 때는 선형 회귀를 사용하고 질적일 때는 로지스틱 회귀를 사용할 수 있습니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

그러나 _예측 변수들_ 이 질적인지 양적인지는 일반적으로 덜 중요한 것으로 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

이 책에서 논의된 통계적 학습 방법들의 대부분은 분석이 수행되기 전에 어떤 질적 예측 변수들이라도 적절히 _코드화(coded)_ 된다는 전제 하에 예측 변수의 유형에 관계없이 적용될 수 있습니다.

This is discussed in Chapter 3.

이것은 3장에서 논의됩니다.

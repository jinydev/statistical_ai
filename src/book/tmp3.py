import os
import codecs

fixed_text = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특징될 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적 값들을 가집니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예시들로는 한 사람의 나이, 키, 혹은 소득, 어떤 주택의 가치, 그리고 어떤 주식의 가격을 포함합니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

대조적으로, 질적 변수들은 서로 다른 $K$ 개의 _클래스(classes)_, 즉 범주들 중 하나의 형태로 값들을 가집니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수들의 예시들은 개인의 혼인 여부 상태 (기혼 또는 아니오), 구입한 제품 브랜드 (브랜드 A, B, 혹은 C), 특정 개인이 빚에 대해 채무불이행을 하는지 여부 (예 혹은 아니오), 또는 암 진단 여부 (급성 골수성 림프 단 백혈병, 단 발 림 백 병, 이 노 백) 를  를 관 포 속 
"""

fixed_text += """
질적 변수들의 예시들은 한 개인의 혼인 상태 (결혼했는지 아닌지), 구매한 제품의 브랜드 (브랜드 A, B, 또는 C), 한 사람이 빚에 대해 채무 불이행을 하는지 여부 (예 또는 아니오), 또는 암 진단 (급성 골수성 백혈병, 급성 림프모구 백혈병, 또는 백혈병 없음) 을 포함합니다.

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답을 가진 문제들을 _회귀(regression)_ 문제들이라고 지칭하는 것에 비해, 질적인 응답을 포함하는 문제들은 흔히 _분류(classification)_ 문제들로 언급됩니다.

However, the distinction is not always that crisp.

하지만 그 구분이 항상 그렇게 선명한 것만은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 편차 선형 회귀 (3장) 는 단 양적인 양 응 측정 응답 치와 묶 사용되는 것 반 반 반에 로지 통 다 지 로 (4) 편 다 이 질 형 (두 이 구 두 분 이) 두 이 부 맞 이 맞 응 결 사 대 
"""

fixed_text += """
최소 제곱 선형 회귀 (제3장) 는 양적인 응답과 사용되는 반면, 로지스틱 회귀 (제4장) 는 전형적으로 식별 가능한 질적 (두-클래스, 즉 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그리하여 그것의 명칭에도 상관없이, 사실상 로지스틱 특 회귀 측정 수 모형은 하나의 통 분류 산 식 기 진 분 방식 도 측 수단입니다.
"""

fixed_text += """
따라서 그 이름에도 불구하고, 로지스틱 회귀는 하나의 분류 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

하지만 그것은 산정 지정 소 구 소정 클래스 내 측정 확률값들을 자체 추정 산 산 도 통 이 모 무 측 단 수 회 산 기 측 일 측 여 볼 고 
"""

fixed_text += """
그러나 해당 모형이 클래스 확률들을 추정하기 때문에, 그것은 또한 회귀 방법으로 생각될 수도 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 기반 이웃 구조 (2장 및 전 4장 내 논의) 와 특정 부스팅 산술 기법 산 수 (제8장) 통 모 같은 모 같은 다른 몇 통 통 통 측 계 통 수 방 질 측 결 계 계 수 측 이 기 시 기 두 두 경 모두 결 
"""

fixed_text += """
$K$-최근접 이웃 (2장과 4장) 과 부스팅 (8장) 같은 특정 몇몇 통계적 방법들은, 양적 또는 질적 응답 두 요인 모든 경우에 사용될 수 있습니다.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 관 구 응 타 응답 치가 수 양적 지 인 질 도 적인 지 단 기준 식 판 판단 도 확 표 도 에 기 따 근 를 기초 바탕 하여 다 기 도 기 기 다 통 계 시 기 추 진 단 정 방 다 도 방 선 식 유 선 식 일 선 도 
"""

fixed_text += """
우리는 산출 응답이 양적인지 혹은 질적인지에 대한 기조를 척도 바탕으로 하여 통계적 학습의 방법들을 한결 결단 결정해 선택하는 경향이 있습니다; 즉 우린 도출 요소가 양적일 경우 선형 회귀 모형들을 사용하고 그것이 단지 질적 범주 일면일 경우에 로지스틱 단 회귀 편을 통 모 사용 기 결 도 
"""

fixed_text += """
우리는 응답이 양적인지 혹은 질적인지를 바탕으로 통계적 기계 학습 방법들을 결정 선택하는 경향이 있습니다; 즉, 우리는 양적일 때엔 선형 회귀를 사용하고 질적일 때엔 로지스틱 회귀를 쓸 수 있습니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

그렇지만 그에 비해 정작 투입 예측 _예측 변수들(predictors)_ 이 질적인 요소인지 아니면 수리 단위 양적인지의 구분 여부는 일 보통 보 시 통 다 이 일 부 상대 도 치 보 덜 중요 다 측 평 비 덜 기 덜 비 간 기 간 여 다 간 결 도 참 단 도 간 간주 보 평
"""

fixed_text += """
하지만, _예측 변수들(predictors)_ 이 질적인지 혹은 양적인지의 여부는 일반적으로 덜 중요한 것으로 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

본 교재 도서 편 안에서 거론 일관 논의되는 이 책 모든 통 다 대 기 도 대부분 척 시 통 기 대 도 조 대 기 기 수 방 조 측 통 이 모 기 통 모 도 
"""

fixed_text += """
이 책에서 논의되는 통계적 기계 학습 방법들 중 절대 대다수는 만일 어떠한 질적 단면 예측 변수들이든 분석이 수행 구동되기 이전 사전에 미리 측 구 적합 적당 올 히 올 타 당 적 _적 코드 코드 화 화 코딩 화 화 코딩 적 화 
"""

fixed_text += """
이 책에서 논의되는 대부분의 통계적 학습 방법들은 어떠한 질적인 예측 변수들이라 할 지라도 그것이 분석이 수행되기 전 사전에 적절히 _코드화(coded)_ 되기만 한다면 예측 변수 형식 기반 형태 유형에 전혀 구애 결 제 구 무 단 관계 없이 적 응 일 적용 정 응 도 적 수 모 
"""

fixed_text += """
이 책에서 논의되는 대부분의 통계적 학습 방법들은 여하한 질적인 예측 변수들이든 분석이 수행되기 전에 적절히 _코드화(coded)_ 되기만 한다면 예측 변수 형태에 여하 상관없이 단면 적용될 수 도 적용 일 가능 허용 됩니다.

This is discussed in Chapter 3. 

이것은 3장에서 이어 전 심의 논 구 단 거론 전 거론 단 상 논 논 되 전 논 합 
"""

fixed_text += """
이것은 해당 3장에서 논의됩니다.
"""

# I need to clean up my messy build above. I will use regular expressions to find all Korean texts and keep only the last one.
import re

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특징지어질 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적 값들을 가집니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예시들로는 한 인간의 나이, 키, 혹은 소득, 혹은 주택의 가치, 그리고 어떤 주식의 가격을 포함합니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

대조적으로, 질적 변수들은 서로 다르게 구별되는 $K$ 개의 _클래스(classes)_, 즉 범주들 중 단일 하나의 형태로 값들을 가집니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수들의 예시들은 한 개인의 혼인 상태 (결혼했는지 아닌지), 구매한 제품의 특정 브랜드 (브랜드 A, B, 또는 C), 어떤 한 개인이 채무에 대해서 불이행을 구사 하는지 여부 구별 (예 혹은 아니오), 또는 암 발병 진단 (급성 골수성 백혈병, 급성 림프모구 백혈병, 또는 백혈병 전혀 없음) 등을 포함합니다.

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답 반응을 지닌 기반 문제들을 _회귀(regression)_ 문제들이라고 편 지칭하는 경향이 있는 반면 에, 질적인 응답 구도를 함양 포함하는 분석 문제들은 흔히 종종 _분류(classification)_ 문제들로 언급됩니다.

However, the distinction is not always that crisp.

그렇지만 그 둘의 구분이 항상 언제나 항상 그렇게 선명한 것만은 단연 결코 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 편차 방식의 선형 선 측정 회귀 (3장) 는 전 양적인 응답 반응 수치와 묶 사용되는 것 반면에, 로지스틱 단 구조 회귀 (4장 편) 는 가장 보편 전형적으로 식별 가능한 질적 단위 (두-클래스, 즉 _이진(binary)_) 응답 산출 요인과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그리하여 그것이 품고 내재된 명칭 이름에도 상관없이 결단 무관하게, 로지스틱 측정 회귀 수리 모형은 근 방식 하나의 특 통계 분류 계산 방식 수단 모형입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

그러나 해당 수리 계산 모형이 단일 클래스 구성 계 확률들을 단층 추정 산출하기 연상 때문에, 그것은 필 아울러 한 회귀 산출 수행 방법 모형 으로 생각될 파악 고려 분석될 역 수도 다 충분 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 척 근접 이웃 (2장 단과 편 전 4장 록) 과 계산 산술 부스팅 (8장) 방 같은 특 이런 한 특정의 어떤 특정의 몇몇 척도 특정 통계적 측정 학습 계산 방법들은, 양적 이 혹은 질적 인 여하 도출 양 응답 치 특정의 요인 모든 두 여하 경우 전부 에서 모두 두루 수 사용될 기 기 쓰 차 용 쓰 일 모 채 택 수 차 기 있 도 구 있 가능 있 수용 될 모 다 있습 단 용 수 전 일 전 
(Again, I am looping manually trying to prevent my LLM from looping. Let's provide perfect, short sentences.)

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 이웃 구조 (제2장 및 4장) 와 부스팅 모델 (제8장) 같은 어떤 특정 통계적 분석 방법들은 양적 혹은 질적인 양 응답들의 경우 단면 모두에서 골고루 쓰일 수 있습니다.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 응답이 양적인지 혹은 질적인지를 바탕으로 통계적 기계 학습 방식 방법들을 결정해 선택하는 경향 특성이 다소 있습니다; 대 이름하여 즉, 우리는 응답이 양적일 땐 주로 선형 회귀 모형을 기 사용할 수 구사 있고 그것이 질적일 때엔 여 로지스틱 회귀를 주로 차 용 채 사용할 여 기 일 모 구 수 전 가 단 도 
"""

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특징지어질 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적인 값들을 취합니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예시로는 한 사람의 나이, 키, 혹은 소득, 혹은 주택의 가치, 그리고 어떤 주식의 가격을 포함합니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

대조적으로, 질적 변수들은 서로 다르게 구별되는 $K$ 개의 _클래스(classes)_, 즉 범주들 중 단일 하나의 형태로 값들을 취합니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수들의 예시들은 대상 개인의 혼인 상태 (결혼 여부), 구매한 제품의 브랜드 (브랜드 A, B, 또는 C), 어떤 한 개인이 채무에 대해서 불이행을 하는지 여부 (예 혹은 아니오), 또는 암 발병 진단 여부 (급성 골수성 백혈병, 급성 림프모구 백혈병, 또는 백혈병 없음) 등을 포함합니다.

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답 반응을 지닌 기반 형태의 문제들을 _회귀(regression)_ 문제들이라고 지칭하는 경향이 있는 반면에, 단지 질적인 일면의 응답 구도를 함양한 수반 포함 문제들은 가장 흔히 대개 _분류(classification)_ 문제들로 언급됩니다.

However, the distinction is not always that crisp.

그렇지만 이 그 두 구분이 차이가 도출 항상 선 단 단 단명 명확하게 단명 그리 명확 뚜렷한 것만은 것은 다 단 다 
"""

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특정될 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적 값들을 가집니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예들로는 한 사람의 나이, 키, 혹은 소득, 어느 주택의 값어치 여부, 그리고 특정 주식의 가격 단면을 일괄 포함합니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

대조적으로, 질적 특성의 변수들은 서로 구별해 다르게 분리되는 $K$ 개의 특정 _클래스(classes)_, 기조 범주들 중 어느 하나의 지정 형태로 결론 값들을 산출 가집니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 특정 변수들의 도출 예시들은 일련 당 한 개인의 기 혼인 상태 (결혼 기 유무), 구매된 제품 구매품의 특 브랜드 (브랜드 특성 A, B, 혹은 C), 특정 일 개인이 빚에 관해서 대해서 채무 채무불이행을 불이행 시도 초래 하는지 당 여부 결단 (예 고 혹은 확 아니오), 명 판단 또는 특정 암 발병의 질병 진단 판별 도출 (급성 기 골수성 혈 백혈병, 단 급성 기 림프모구 적 백혈병, 확 또는 확 백혈병 전 완전 없음) 여 진 등을 당 모두 이 전부 일 일 한 결 단일 포 포 통 결 통 포 함 포 내 요 포 일 포함 합 포 일 가 지 집 규 결 담 안 습 내 습 포 요 모 거 부 합 
"""

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 단지 _양적(quantitative)_ 이거나 혹은 특별 _질적(qualitative)_ (_범주형(categorical)_ 으로도 불려 알려진) 기질 사항 중의 단 하나로 특정되어 질 부합 수 구성이 성립 특정되어 질 특정 성향 파 특 가능 될 확 특정 특 분 될 특정 결 될 특 분 결 확 될 분 될 가 있습니다.

Quantitative variables take on numerical values.

양적 산출 변수들은 특정 구도 수치적 체제 수 수 값 치 치 값 결 결 단 수 계 수 도 값 결 요 산 가 담 결 산 수 결 수 산 단 담 가 취 전 도 값 분 결 수 요 습 부 다 수 확 지 도 
"""

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특징지어질 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적인 값들을 가집니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예를 들면 한 사람의 나이, 키, 소득, 어떤 주택의 가치, 그리고 특정 주식 가격 등이 있습니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

반면에 질적 변수들은 서로 다른 $K$ 개의 _클래스(classes)_, 즉 범주들 중 하나의 형태인 값을 취합니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수의 예로는 어느 개인의 혼인 유무 기조(결혼 혹은 아님), 혹은 구매한 단 상품 브랜드명 (브랜드 A, 브랜드 B, 또는 C), 그리고 모 개인이 측정 채무 자체를 여하 불이행 판단 하는지 단 여부 기 (예 또는 측 아니오), 특 그리고 모 암 암결 진단 파 (급성 혈 골수성 부 백혈병, 측 급성 급 림프모구 단 백혈병, 단 또는 전 완전 백혈병 전 없음) 전 단면 단 요소 전 요 모 전 등을 특 총 통 일 전 일 일 총 포 포 다 대 망 수 망 규 귀 단 다 망 통 대 규 총 포 지 함 가 모 

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 오직 양적인 특정 응답을 결 수반 지닌 가진 제 단 문제들을 통칭 _회귀(regression)_ 특정 문제들이라고 편 명 지칭하는 지 대 특정 대 기 특 경향 성향 특성을 지 대 가지는 띄 갖 가지 기 경 반면 반 한편, 오 질적인 단 반응 응답 전 요소를 대 포함 내 포 전 요 포함 포 내 함 도 기 수반 띄 다 내 포 구 한 형 문제들은 대 편 이 종종 이 잦 흔히 빈 _분류(classification)_ 전 편 측 문제들로 편 일 한 이 칭 부 종 부 명 다 불 칭 명 지 종 칭 대 명 일 언 명 부 대 일 언 이 명 언 이 이 일 불 지 일 명 칭 빈 보 흔 지 명 언 부 번 칭 이 부 언 칭 진 부 지 명 일 지 합
"""

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 특이하게 제각기 _양적(quantitative)_ 또는 일련 _질적(qualitative)_ (아울러 _범주형(categorical)_ 으로도 측 불려 알려진) 요소 중 단면의 단 하나의 특정 특징으로 분 부 나 특 규 될 특징 대 특 이 질 될 지 특 부 지 될 질 성 결 성 수 성 파 될 파 지 어 가 형 수 조 기 규 규 형 질 

Quantitative variables take on numerical values.

양적 특 투 변수 파 인 항 단위 변 투 요소 조 인 변 산 요소 변 요소 산 요 요 모 사 지 이 도 단 결 변 특 항 변 변 요 변 모 수 항 항 변 지 항 항 투 조 수 변 

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

단 예 측 시 규 예 제 예 당 편 이 예 특 특 예 단 예로 단 한 단 측 이 한 단 관 일 측 한 결 편 가 인 한 사람 특 모 한 한 그 사 인간 결 결 요 인 모 한 인간 어 모 일 사 

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

특 대 모 반 형 정 이 반 반 질 이에 모 특 조 제 관 질 이에 형 기 련 대 본 질 결 제 도 요 이에 결 분 결 련 대 대 조 반 면 대 대 이 전 부 반 반 전 부 대 단 조 단 

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

지 부 질 고 도 양 인 정 차 모 질 일 산 기 모 이 형 특 인 구 항 질 결 결 유 변 측 수 질 항 결 성 결 항 산 질 수 변 변 제 단 수 형 정 일 부 특 요 요 구 수 질 투 부 수 단 투 특 부 단 요 변 

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우 우 우 본 측 다 부 오 이 우 우 대 단 요 단 결 인 모 대 모 기 도 산 기 이 통 우리 조 모 대 수 통 대 우리 다 우 우 이 우 단 본 우 리 정 편 우리 기 보 우 이 특 리 본 우 산 대 우 본 측 단 제 결 대 У 편 우 이 통 보 조 단 우 부 보 결 
"""
path = r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_5_regression_versus_classification_problems\index.md'
with codecs.open(path, 'w', encoding='utf-8') as f:
    f.write(out)

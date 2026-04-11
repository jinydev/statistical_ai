import codecs
import re

out = """---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems

# 2.1.5 회귀 대 분류 문제

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_).

변수들은 _양적(quantitative)_ 이거나 또는 _질적(qualitative)_ (또한 _범주형(categorical)_ 으로 알려진) 중 하나로 특징지어질 수 있습니다.

Quantitative variables take on numerical values.

양적 변수들은 수치적 값들을 취합니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

예시들로는 어떤 사람의 나이, 키, 또는 소득, 한 주택의 가치, 그리고 어떤 주식의 가격을 포함합니다.

In contrast, qualitative variables take on values in one of $K$ different _classes_, or categories.

대조적으로, 질적 변수들은 서로 구별되는 $K$ 개의 _클래스(classes)_, 즉 범주들 중 하나의 형태인 값을 취합니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

질적 변수들의 예시들은 대상 개인의 혼인 여부 (결혼했는지 아닌지), 혹은 구매한 특정 제품의 브랜드명 (브랜드 A, B, 또는 C), 어느 특정한 개인이 지닌 채무를 상대로 특정 채무불이행 판별 여부를 하는지 (예 또는 아니오), 더불어 암 발병을 분석하는 진단 (급성 골수성 백혈병, 결연한 급성 림프모구 백혈병, 아니면 백혈병 없음) 등을 포함합니다.
"""
with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_5_regression_versus_classification_problems\index.md', 'w', encoding='utf-8') as f:
    f.write(out)

---
layout: default
title: "2. Statistical Learning"
---

[2.1 What Is Statistical Learning >](2_1_what_is_statistical_learning/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2. Statistical Learning

# 2. Statistical Learning (통계적 학습)

This Chapter 2 introduces the main concepts and theoretical foundations of statistical learning in earnest.

본 2장에서는 통계적 학습의 주요 개념과 이론적 토대를 본격적으로 다룹니다.
We will learn about the purpose and methodologies for estimating the function $f$, as well as the variance-bias trade-off, which is the most fundamental issue in machine learning.

함수 $f$를 추정하는 목적과 방법론들, 그리고 분산-편향 트레이드오프(Variance-Bias Trade-Off)라는 기계학습의 가장 본질적인 이슈를 학습합니다.

## 2.1 What Is Statistical Learning?

## 2.1 What Is Statistical Learning? (통계적 학습이란 무엇인가?)

We explore the purpose of finding a function $f$ that estimates the relationship between an input variable ($X$) and an output variable ($Y$).

입력 변수($X$)와 출력 변수($Y$) 간의 관계를 추정하는 함수 $f$를 찾는 목적에 대해 살펴봅니다.
You can understand the role of statistical learning based on the two main goals: prediction and inference.

예측(Prediction)과 추론(Inference)의 두 가지 주요 목표를 바탕으로 통계적 학습의 역할을 이해할 수 있습니다.

### 2.1.1 Why Estimate f ?

### 2.1.1 Why Estimate f ? (왜 f를 추정해야 하는가?)

We learn about the prediction-centric reasons for predicting output values for new data points,

새로운 데이터 포인트에 대해 출력값을 예측하기 위한 예측(Prediction) 중심의 이유와,
and the inference-centric reasons for analyzing the effect of each input variable on the output variable.

각 입력 변수가 출력 변수에 미치는 영향을 분석하기 위한 추론(Inference) 중심의 이유를 배웁니다.

#### Prediction

#### Prediction (예측)

We focus on the goal of predicting the value of an unobserved response variable as accurately as possible based on given features.

주어진 특성을 기반으로 아직 관측되지 않은 반응 변수의 값을 가장 정확하게 맞추는 목표를 집중적으로 다룹니다.
We familiarize ourselves with the limitations of the model by differentiating between reducible error and irreducible error.

결정론적 오류와 허용 불가능한 오류(Irreducible Error)의 개념을 구분하여 모델의 한계를 숙지합니다.

### 2.1.2 How Do We Estimate f ?

### 2.1.2 How Do We Estimate f ? (어떻게 f를 추정하는가?)

We introduce approaches to mathematically construct the most appropriate function $f$ utilizing training data.

학습 데이터(Training Data)를 활용하여 가장 적합한 함수 $f$를 수학적으로 구성하는 접근 방식을 소개합니다.
We cover the fundamental differences and working principles of parametric and non-parametric models.

파라미터 모델(Parametric)과 비-파라미터 모델(Non-Parametric)의 근본적인 차이점과 작동 원리를 다룹니다.

#### Parametric Methods

#### Parametric Methods (모수적 방법론)

This is a method that first assumes the shape of the function (e.g., linearity) and fits the model by estimating a limited set of parameters.

먼저 함수의 형태(Shape)를 가정(예: 선형성)하고 한정된 파라미터를 추정하여 모델을 적합시키는 방법입니다.
It has the advantage of being fast to compute and easy to interpret, but it has the disadvantage that the actual shape of the data and the assumed shape can be significantly different.

계산이 빠르고 해석이 쉬운 장점이 있지만 실제 데이터의 형태와 가정된 형태가 크게 다를 수 있다는 단점을 지닙니다.

#### Non-Parametric Methods

#### Non-Parametric Methods (비모수적 방법론)

These are methodologies that do not make specific assumptions about the shape of the function $f$ and proceed to fit as closely to the data points as possible.

함수 $f$의 형태에 특별한 가정을 두지 않고, 데이터 점들에 최대한 근접하도록 적합을 진행하는 방법론들입니다.
We learn that while they can describe data very flexibly, they require a vastly larger amount of data for meaningful analysis.

데이터를 매우 유연하게 묘사할 수 있으나 유의미한 분석을 위해선 훨씬 방대한 양의 데이터가 필요함을 배웁니다.

### 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

### 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability (예측 정확도와 모델 해석력 간의 트레이드오프)

We cover the black-box phenomenon, where as a model becomes more flexible and powerful, its internal structure becomes more complex, making cause analysis and interpretation significantly more difficult.

모델이 유연하고 강력해질수록 내부 구조가 복잡해지며 원인 분석과 해석이 크게 어려워지는 블랙박스 구조 현상을 다룹니다.
We develop the ability to determine the level of flexibility depending on the fundamental purpose of the analysis (high accuracy vs. the need to identify specific causes).

분석의 근본 목적(높은 정확성 vs 구체적인 원인 규명 필요성)에 따라 유연성 수준을 결정하는 능력을 기릅니다.

### 2.1.4 Supervised Versus Unsupervised Learning

### 2.1.4 Supervised Versus Unsupervised Learning (지도 학습과 비지도 학습)

We point out the difference between supervised learning in an environment where the target label (response) is given, and unsupervised learning, which only identifies structural features.

예측 대상이 되는 정답(Label/Response)이 주어지는 환경에서의 지도 학습과 구조적인 특징만을 파악하는 비지도 학습의 차이를 짚어봅니다.
Consequently, the concept of semi-supervised learning, which has a character midway between supervised and unsupervised, is also briefly introduced.

결과적으로 지도-비지도 중간의 성격을 지닌 반지도 학습(Semi-Supervised) 개념도 짧게 소개됩니다.

### 2.1.5 Regression Versus Classification Problems

### 2.1.5 Regression Versus Classification Problems (회귀 문제와 분류 문제)

We define a regression situation where the response variable is numerically continuous, and a classification situation where it is discrete and divided qualitatively.

반응 변수가 수치적으로 연속형인 회귀(Regression) 상황과 질적으로 나뉘는 이산형인 분류(Classification) 상황을 정의합니다.
We explain that the appropriate algorithms and evaluation metric systems must be fundamentally different for each problem type.

각 문제 유형에 알맞은 알고리즘과 평가지표 체계가 본질적으로 달라져야 함을 설명합니다.

## 2.2 Assessing Model Accuracy

## 2.2 Assessing Model Accuracy (모델 정확도 평가)

Since no single methodology can be universal, we learn the criteria to quantitatively compare models on a given specific dataset.

어떠한 단일 방법론도 만능일 수는 없으므로 주어진 특정 데이터셋에서 모델들을 정량적으로 비교할 기준을 배웁니다.
We learn the causes of the gap between the training error during the learning phase and the test error in practice.

훈련 단계에서의 훈련 에러(Training Error)와 실전에서의 시험 에러(Test Error)의 격차 원인을 학습합니다.

### 2.2.1 Measuring the Quality of Fit

### 2.2.1 Measuring the Quality of Fit (적합성 품질 측정)

We explain the Mean Squared Error (MSE), the most universally used metric when evaluating a model's superiority in a regression environment.

회귀 환경에서 모형의 우수성을 평가할 때 가장 보편적으로 사용되는 척도인 평균 제곱 오차(MSE, Mean Squared Error)를 설명합니다.
We emphasize the importance of generalization, which performs well on unfamiliar test data, rather than just simply fitting the training data well.

단순히 학습 데이터만 잘 맞추는 것보다는 낯선 시험 데이터에도 좋은 성능을 발휘하는 일반화(Generalization)의 중요성을 강조합니다.

### 2.2.2 The Bias-Variance Trade-Off

### 2.2.2 The Bias-Variance Trade-Off (편향-분산 트레이드오프)

We deal with the complex correlation between bias and variance, which are the essential components that make up the error on test data.

시험 데이터의 오차를 구성하는 본질적인 요소인 편향(Bias)과 분산(Variance) 간의 복잡한 상관관계를 다룹니다.
We mathematically explore the U-shaped validation curve (U-Shape) where as the flexibility of the model increases, variance grows and bias gradually decreases.

모델의 유연성이 증가함에 따라 분산은 커지고 편향은 서서히 줄어드는 U자형 검증 곡선(U-Shape)을 수학적으로 탐구합니다.

### 2.2.3 The Classification Setting

### 2.2.3 The Classification Setting (분류 환경에서의 평가)

We introduce the error rate, a ratio metric used to compare performance in a model environment where discrete class outcomes must be predicted.

이산적인 클래스 결과를 예측해야 하는 모델 환경에서 성능을 비교하기 위한 비율 지표인 오분류율(Error Rate)을 도입합니다.
We learn about the Bayes error rate, which defines the lowest limit by performing optimal predictions within a given data space.

주어진 데이터 공간 내에서 최적의 예측을 수행하여 최소 한계를 규정하는 베이즈 에러율(Bayes Error Rate)을 학습합니다.

#### K-Nearest Neighbors

#### K-Nearest Neighbors (K-최근접 이웃)

We learn about the K-Nearest Neighbors (KNN) technique, which is the most intuitive algorithm as an actual implementation of theory in a non-parametric classification environment.

비모수적인 분류 환경에서 이론의 실제 구현체로 가장 직관적인 알고리즘인 K-최근접 이웃(KNN) 기법을 학습합니다.
We learn how the decision boundary changes according to the change in the K value, and how the bias-variance trade-off appears during that process.

K 값의 크기 변화에 따라 결정 경계(Decision Boundary)가 어떻게 바뀌며, 그 과정 속 편향-분산 트레이드오프가 나타나는지를 배웁니다.

## 2.3 Lab: Introduction to Python

## 2.3 Lab: Introduction to Python (실습: 파이썬 입문)

We introduce the basic Python environment for data analysis and visualization as a programming foundation to proceed with the entire course.

전체 과정을 진행하기 위한 프로그래밍 기반 기술로서 데이터 분석 및 시각화를 위한 기초적인 파이썬 환경을 소개합니다.
We comprehensively check the Python ecosystem and the structure of essential libraries such as NumPy, Pandas, and Matplotlib.

파이썬 생태계와 필수 라이브러리인 NumPy, Pandas, Matplotlib 구조를 전반적으로 점검합니다.

### 2.3.1 Getting Started

### 2.3.1 Getting Started (시작하기)

We cover essential setup structures for starting Python, such as the Jupyter environment and package installation methods.

주피터 환경, 패키지 설치법 등 파이썬 시작을 위한 필수 설정 구조를 다룹니다.
You can understand the default interpreter path that will serve as the basecamp for analysis.

분석의 베이스캠프 역할을 할 기본 인터프리터 경로를 이해할 수 있습니다.

### 2.3.2 Basic Commands

### 2.3.2 Basic Commands (기본 명령어)

We quickly scan through very basic essential commands at the shell level, such as outputting to the console, allocating data, and returning lengths.

콘솔에서의 출력, 데이터 할당, 길이 반환 등 아주 기본적인 셸 단위 필수 명령어들을 빠르게 훑어봅니다.
You can examine basic Python data type structures like strings or lists and their compatibility.

문자형 또는 리스트 같은 기본 파이썬 자료형 구조와 호환성을 살펴볼 수 있습니다.

### 2.3.3 Introduction to Numerical Python

### 2.3.3 Introduction to Numerical Python (NumPy 소개)

This is a guide on how to use the NumPy package, the core foundation that enables powerful and fast computation of multi-dimensional data arrays (Array/Matrix).

다차원 데이터 배열(Array/Matrix)을 강력하고 빠르게 연산할 수 있게 해주는 핵심 기초인 NumPy 패키지의 사용법입니다.
We take time to get accustomed to specifying random seeds and generating random numbers.

랜덤 시드 지정과 랜덤 난수 생성 등에 익숙해지는 시간을 가집니다.

### 2.3.4 Graphics

### 2.3.4 Graphics (그래픽 시각화)

We bring in Matplotlib capabilities to visualize complex data trends like scatter plots and contour plots in the form of charts.

Matplotlib 기능을 가져와 산점도, 윤곽 투영 플롯(Contour Plot) 등 복잡한 데이터 동향을 도표의 형태로 시각화합니다.
We learn the technique of intuitively capturing information structures, correlations, and distribution patterns through graphs.

그래프를 통해 정보 구조나 상관성, 분포 양상을 직관적으로 포착하는 기술을 배웁니다.

### 2.3.5 Sequences and Slice Notation

### 2.3.5 Sequences and Slice Notation (시퀀스와 슬라이스 표기법)

We deal with indexing techniques that directly access elements inside Python's matrix objects or separate only a specific sequence interval.

파이썬의 행렬 객체 내부 원소들에 직접 접근하거나 특정 일련 구간만을 분리하는 인덱싱(Indexing) 기술을 다룹니다.
We aim for grammatical mastery in dividing and combining huge chunks of data into necessary sequences.

거대한 데이터 조각들을 필요한 시퀀스로 나누고 결합하는 문법적 숙달을 목표로 합니다.

### 2.3.6 Indexing Data

### 2.3.6 Indexing Data (데이터 인덱싱)

This is a technique to not only manually specify the index of the desired range, but also filter by combining the results of logical truth values (Boolean).

원하는 범위의 인덱스를 수동으로 지정할 뿐만 아니라 논리적 진릿값(Boolean) 결과를 결합하여 필터링하는 기법입니다.
We practice specifying filter conditions to weed out only the information with specific conditions from a massive dataframe.

방대한 데이터프레임 안에서 특정 조건의 정보만을 걸러내는 필터 조건 지정을 훈련합니다.

### 2.3.7 Loading Data

### 2.3.7 Loading Data (데이터 로딩)

We learn how to actually load external data into a DataFrame in the Python environment using Pandas' `read_csv` syntax.

Pandas(판다스)의 `read_csv` 구문을 통해 외부 데이터를 실제로 파이썬 환경의 DataFrame으로 적재하는 방법을 배웁니다.
It is an elementary process of importing and viewing initial data, checking for and handling non-existent Null values, etc.

초기 데이터를 가져오며 열람하고, 존재하지 않는 Null 값 등을 확인하고 처리하는 기초 과정입니다.

### 2.3.8 For Loops

### 2.3.8 For Loops (for 순환문)

We learn block processing techniques, which are basic control statements that must be used when writing repetitive analysis pipelines or scripts.

반복적인 분석 파이프라인이나 스크립트를 작성할 때 반드시 쓰이게 되는 기본 제어 구문인 블록 처리 기술을 배웁니다.
We approach it with comparative grammar in preparation for using list comprehensions and vector operations.

리스트 컴프리헨션(List Comprehension) 및 벡터 연산 사용에 대비한 비교 문법으로 접근합니다.

### 2.3.9 Additional Graphical and Numerical Summaries

### 2.3.9 Additional Graphical and Numerical Summaries (추가적인 그래픽 및 수치적 요약)

We learn everything from numeric summaries like `describe` to capture all data at a glance, to additional graphical techniques like histograms and box plots.

모든 데이터를 한눈에 담기 위한 `describe` 같은 수치 요약부터, 히스토그램이나 박스 플롯 등의 추가 그래픽 기법까지 학습합니다.
By understanding the location and dispersion of the entire dataset like the back of your hand, it adds momentum to future feature engineering execution.

데이터셋 전체의 위치 및 산포도를 손발처럼 파악하게 됨으로서 향후 피처 엔지니어링 수행에 탄력을 더합니다.

## 2.4 Exercises

## 2.4 Exercises (연습 문제)

This is a practice course where you can check the bias-variance structure, phenomena caused by learning model flexibility, etc., which were covered in depth in Chapter 2.

2장에서 심도 있게 다뤄졌던 편향-분산 구조, 학습 모델 유연성이 미치는 현상 등을 점검할 수 있는 연습 코스입니다.
We test both mathematical limitation understanding and applicative power through Conceptual and Applied problems.

개념(Conceptual) 문제와 응용(Applied) 문제들을 통해 수리적인 한계 이해와 응용력을 모두 테스트해 봅니다.

---

## Sub-Chapters (하위 목차)

[2.1 What Is Statistical Learning >](2_1_what_is_statistical_learning/trans1.html)

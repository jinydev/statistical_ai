---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 2.2.3.1 K Nearest Neighbors](../2_2_assessing_model_accuracy/2_2_3_the_classification_setting/2_2_3_1_k_nearest_neighbors/trans2.html) | [2.3.1 Getting Started >](2_3_1_getting_started/trans2.html)

# 2.3 Lab: Introduction to Python
# 2.3 실습: 파이썬 베이스캠프 입소하기

---

이제 지루하고 골치 아팠던 통계 이론 시간(2.1\~2.2절)이 끝났습니다. 앞으로 이 책의 모든 챕터 마지막에는 수십억 개의 데이터를 직접 주무를 수 있는 **'코딩 실습(Lab)'** 코너가 준비되어 있습니다. 우리가 앞으로 사용할 무기는 이 시대 최고의 인기 언어인 **파이썬(Python)** 입니다. 이번 2.3절은 본격적인 데이터 전쟁터(3장)에 나가기 전에 가장 기초적인 무기 다루는 법을 훈련하는 신병 교육대(베이스캠프)입니다!

### 2.3.1 Getting Started

Covers essential setup structures for starting Python, such as the Jupyter environment and package installation methods.
주피터 환경, 패키지 설치법 등 파이썬 시작을 위한 필수 설정 구조를 다룹니다.

You can understand the default interpreter path that will serve as the basecamp for analysis.
분석의 베이스캠프 역할을 할 기본 인터프리터 경로를 이해할 수 있습니다.

### 2.3.2 Basic Commands

Quickly scans through very basic essential commands at the shell level, such as console output, data assignment, and returning length.
콘솔에서의 출력, 데이터 할당, 길이 반환 등 아주 기본적인 셸 단위 필수 명령어들을 빠르게 훑어봅니다.

You can examine basic Python data type structures like strings or lists and their compatibility.
문자형 또는 리스트 같은 기본 파이썬 자료형 구조와 호환성을 살펴볼 수 있습니다.

### 2.3.3 Introduction to Numerical Python

How to use the NumPy package, the core foundation that enables powerful and fast computation of multi-dimensional data arrays (Array/Matrix).
다차원 데이터 배열(Array/Matrix)을 강력하고 빠르게 연산할 수 있게 해주는 핵심 기초인 NumPy 패키지의 사용법입니다.

Takes time to get accustomed to specifying random seeds and generating random numbers.
랜덤 시드 지정과 랜덤 난수 생성 등에 익숙해지는 시간을 가집니다.

### 2.3.4 Graphics

Brings in Matplotlib capabilities to visualize complex data trends like scatter plots and contour plots in the form of charts.
Matplotlib 기능을 가져와 산점도, 윤곽 투영 플롯(Contour Plot) 등 복잡한 데이터 동향을 도표의 형태로 시각화합니다.

Learns the technique of intuitively capturing information structures, correlations, and distribution patterns through graphs.
그래프를 통해 정보 구조나 상관성, 분포 양상을 직관적으로 포착하는 기술을 배웁니다.

### 2.3.5 Sequences and Slice Notation

Deals with indexing techniques that directly access elements inside Python's matrix objects or separate only a specific sequence interval.
파이썬의 행렬 객체 내부 원소들에 직접 접근하거나 특정 일련 구간만을 분리하는 인덱싱(Indexing) 기술을 다룹니다.

Aims for grammatical mastery in dividing and combining huge chunks of data into necessary sequences.
거대한 데이터 조각들을 필요한 시퀀스로 나누고 결합하는 문법적 숙달을 목표로 합니다.

### 2.3.6 Indexing Data

A technique to not only manually specify the index of the desired range, but also filter by combining the results of logical truth values (Boolean).
원하는 범위의 인덱스를 수동으로 지정할 뿐만 아니라 논리적 진릿값(Boolean) 결과를 결합하여 필터링하는 기법입니다.

Practices specifying filter conditions to weed out only the information with specific conditions from a massive dataframe.
방대한 데이터프레임 안에서 특정 조건의 정보만을 걸러내는 필터 조건 지정을 훈련합니다.

### 2.3.7 Loading Data

Learns how to actually load external data into a DataFrame in the Python environment using Pandas' `read_csv` syntax.
Pandas(판다스)의 `read_csv` 구문을 통해 외부 데이터를 실제로 파이썬 환경의 DataFrame으로 적재하는 방법을 배웁니다.

An elementary process of importing and viewing initial data, checking for and handling non-existent Null values, etc.
초기 데이터를 가져오며 열람하고, 존재하지 않는 Null 값 등을 확인하고 처리하는 기초 과정입니다.

### 2.3.8 For Loops

Learns block processing techniques, which are basic control statements that must be used when writing repetitive analysis pipelines or scripts.
반복적인 분석 파이프라인이나 스크립트를 작성할 때 반드시 쓰이게 되는 기본 제어 구문인 블록 처리 기술을 배웁니다.

Approaches it with comparative grammar in preparation for using list comprehensions and vector operations.
리스트 컴프리헨션(List Comprehension) 및 벡터 연산 사용에 대비한 비교 문법으로 접근합니다.

### 2.3.9 Additional Graphical and Numerical Summaries

Learns everything from numeric summaries like `describe` to capture all data at a glance, to additional graphical techniques like histograms and box plots.
모든 데이터를 한눈에 담기 위한 `describe` 같은 수치 요약부터, 히스토그램이나 박스 플롯 등의 추가 그래픽 기법까지 학습합니다.

By understanding the location and dispersion of the entire dataset like the back of your hand, it adds momentum to future feature engineering execution.
데이터셋 전체의 위치 및 산포도를 손발처럼 파악하게 됨으로서 향후 피처 엔지니어링 수행에 탄력을 더합니다.

---

## Sub-Chapters

[< 2.2.3.1 K Nearest Neighbors](../2_2_assessing_model_accuracy/2_2_3_the_classification_setting/2_2_3_1_k_nearest_neighbors/trans2.html) | [2.3.1 Getting Started >](2_3_1_getting_started/trans2.html)

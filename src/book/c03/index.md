---
layout: default
title: "index"
---

> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3. Linear Regression (선형 회귀)

지도 학습의 가장 단순하면서도 기본이 되는 선형 회귀(Linear Regression) 접근법을 다루는 3장입니다.

## 3.1 Simple Linear Regression (단순 선형 회귀)

단 하나의 입력 변수(X)를 사용하여 반응 변수(Y)를 예측하는 단순 선형 회귀 구조를 알아봅니다.

### 3.1.1 Estimating the Coefficients (계수 추정)

주어진 훈련 데이터를 가장 잘 설명하는 회귀 계수를 추정하기 위해 최소 제곱법(Least Squares)을 사용하는 과정을 살펴봅니다.

### 3.1.2 Assessing the Accuracy of the Coefficient Estimates (계수 추정치의 정확도 평가)

추정한 회귀 계수가 실제 모집단 계수와 얼마나 가까운지(표준 오차, 신뢰 구간) 통계적으로 검증하는 방법을 배웁니다.

### 3.1.3 Assessing the Accuracy of the Model (모델의 정확도 평가)

적합된 선형 회귀 모델이 전체 데이터의 변동성을 얼마나 잘 설명하는지 R²(결정계수) 통계량 등으로 측정합니다.

## 3.2 Multiple Linear Regression (다중 선형 회귀)

입력 변수가 2개 이상일 때 다수의 예측 변수를 동시에 고려하는 다중 선형 회귀 모델로 확장합니다.

### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)

여러 개의 설명 변수를 모두 포함한 다차원 공간에서 평균 잔차 제곱합을 최소화하는 하이퍼플레인을 찾는 과정을 배웁니다.

### 3.2.2 Some Important Questions (중요한 질문들)

다중 선형 회귀 모델을 사용할 때 답해야 하는 주요 질문(변수들의 유의성, 모델 적합도, 예측)들을 제기합니다.

#### Two: Deciding on Important Variables (질문 2: 중요한 변수 결정)

다수의 변수 중 반응 변수와 실제로 유의미한 관계가 있는 변수 조합들을 선택(Variable Selection)하는 방법을 배웁니다.

#### Three: Model Fit (질문 3: 모델 적합성)

선택된 다중 회귀 모델이 주어진 훈련 데이터에 얼마나 잘 적합되었는지 다중 R² 지표 및 RSE를 통해 살펴봅니다.

#### Four: Predictions (질문 4: 예측)

적합된 모델을 바탕으로 새로운 관측치에 대한 반응 변수 스코어를 예측할 때 수반되는 세 가지 큰 불확실성을 검토합니다.

## 3.3 Other Considerations in the Regression Model (회귀 모델에서의 기타 고려사항)

단순 수치형 데이터 범위를 넘어서 실제 데이터를 회귀 모델링할 때 마주치는 추가적인 제약과 변수 처리 기법을 소개합니다.

### 3.3.1 Qualitative Predictors (정성적 예측 변수)

수치가 아닌 카테고리(범주) 성격을 가지는 정보(성별, 지역 등)를 선형 모형 방정식에 포함시키기 위한 더미 변수(Dummy Variable) 체계를 배웁니다.

#### Predictors with Only Two Levels (수준이 2개인 예측 변수)

남성/여성과 같이 단 두 가지 범주만 갖는 단순한 질적 변수를 0과 1의 값으로 매핑해 기초적인 회귀 분석을 수행하는 방법을 봅니다.

### 3.3.2 Extensions of the Linear Model (선형 모델의 확장)

입력 변수 간의 시너지 효과나 독립적이지 않은 요소를 반영하기 위해 상호작용 항(Interaction Term)을 추가하는 기법을 배웁니다.

#### Non-linear Relationships (비선형 관계)

예측 변수와 반응 변수 간의 관계가 곡선 형태를 띌 때 잔차도 분석으로 이를 파악하고 다항식(Polynomial) 회귀로 유연하게 적합하는 방법을 소개합니다.

### 3.3.3 Potential Problems (잠재적 문제들)

회귀 모델을 실제 데이터에 적용했을 때 가정이 위배되어 발생하는 대표적인 한계점과 부작용들을 짚어봅니다.

#### 2. Correlation of Error Terms (오차 항의 상관관계)

오차 항들은 서로 독립이어야 한다는 기본 전제가 깨졌을 때 발생하는 표준 오차 산정의 치명적인 오류를 다룹니다.

#### 3. Non-constant Variance of Error Terms (오차 항의 비일관적 분산)

데이터의 반응 변수 값이 커짐에 따라 오차의 편차가 커지는 이분산성(Heteroscedasticity) 문제를 분석합니다.

#### 4. Outliers (이상치)

일반 예측치를 크게 벗어난 관측값인 이상치가 잔차 표준 오차 및 모델 적합도(R²)에 어떤 치명적인 영향을 끼치는지 파악합니다.

#### 6. Collinearity (다중공선성)

입력 변수들이 서로 높은 상관성을 띠어 각 계수 추정의 분산을 팽창시키는 다중공선성의 위험 패턴을 분석합니다.

## 3.4 The Marketing Plan (마케팅 플랜 작성)

본 장의 도입부에서 광고-판매 관련으로 제기했던 마케팅 질문들을 다중 선형 회귀 관점의 통계적 증거와 논리로 모두 답변합니다.

## 3.5 Comparison of Linear Regression with K-Nearest Neighbors (선형 회귀와 K-최근접 이웃 비교)

파라미터 모델인 선형 회귀와 비파라미터 모델인 KNN을 수치형 예측 환경에서 비교 분석합니다.

## 3.6 Lab: Linear Regression (실습: 선형 회귀)

Statsmodels 라이브러리 등을 활용하여 선형 회귀 분석 프로세스를 파이썬 코드로 어떻게 실행하는지 다루는 기본 랩입니다.

### 3.6.1 Importing packages (패키지 불러오기)

회귀 실습에 필수적인 Pandas, NumPy, Statsmodels 등의 데이터 과학 최적화 패키지를 초기 설정하는 코드를 보여줍니다.

### 3.6.2 Simple Linear Regression (단순 선형 회귀 실습)

보스턴 주택 데이터셋을 파이썬에 로드하고 단순 선형 회귀 모형에 적합시키는 1차적인 워크플로우를 익힙니다.

#### Jupyter Notebook Output (출력 예시)

Jupyter Notebook 셀에서 통계 모델 객체 혹은 변수의 길이/형태를 출력했을 때 콘솔에 어떻게 표시되는지 확인합니다.

### 3.6.3 Multiple Linear Regression (다중 선형 회귀 실습)

여러 예측 변수를 한꺼번에 통계식(Formula)에 투입하여 다중 선형 회귀 분석 스크립트를 작성하는 방법을 익힙니다.

### 3.6.4 Multivariate Goodness of Fit (다변량 적합도)

다중 회귀 구조에서 변수 간 영향을 판단하는 VIF 구조 검증 등 다변량 모델의 건전성을 파이썬 코드로 평가합니다.

#### List Comprehension (리스트 컴프리헨션)

분석 과정에서 여러 변수 명칭을 동적으로 조작할 때 쓰이는 강력한 리스트 반복문(List Comprehension) 문법 팁을 배웁니다.

### 3.6.5 Interaction Terms (상호작용 항 실습)

파이썬 statsmodels의 수식 문자열 체계에서 `X1 * X2`라는 간단한 기호를 사용해 상호작용 항을 모델에 추가하는 기법을 실습합니다.

### 3.6.6 Non-linear Transformations of the Predictors (예측 변수의 비선형 변환 실습)

예측 변수에 다항식(제곱) 연산 처리나 로그 처리를 기입하여 비선형 곡선을 적합하는 테크닉을 코딩으로 확인합니다.

#### Model Comparison (분산분석을 통한 모델 비교)

`anova_lm()` 함수를 사용해 선형 모델과 비선형 모델 간의 잔차를 분석하고 추가 계수가 기여하는 통계적 유의성을 검증하는 프로세스입니다.

두 모델 중 어느 것이 더 우수한가 분산분석(ANOVA)으로 확인합니다.

* [문서로 이동하기](./3_6_lab_linear_regression/3_6_7_qualitative_predictors/)

범주형/정성적 변수가 데이터셋에 섞여 있을 때 더미 변수(Dummy Variable)가 파이썬 상에서 어떻게 내부적으로 코딩되어 회귀분석되는지 구조를 파악합니다.

## 3.7 Exercises (연습 문제)

지금까지 배운 선형 회귀에 대한 직관, 가정 위배 시 현상, 그리고 수학적 기본기를 점검하는 테스트 단계입니다.

### Conceptual (개념 문제)

데이터셋이 없는 상황에서, 잔차 제곱합을 직접 수식으로 풀거나 특정 가설 하에서 회귀 계수의 성질을 수학적으로 풀어보는 이론 세트입니다.

### Applied (응용 문제)

파이썬 세션을 직접 실행해 교재의 오픈 데이터(예: Auto, Carseats)로 회귀 분석을 돌리고 진단 플롯 시각화를 통해 문제점을 스스로 보고하는 실습 테스트입니다.

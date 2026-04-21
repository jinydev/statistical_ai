---
layout: default
title: "trans2"
---

# 6.5 실습: 선형 모델과 정규화 기법 구현 (Lab: Linear Models and Regularization Methods)

In this lab we implement many of the techniques discussed in this chapter. We import some of our libraries at this top level.
이번 Lab 실습 챕터에서는 지금껏 6단원에서 머리 싸매며 논의했던 다양한 규제 테크닉과 방법론들을 우리 손으로 직접 콘솔상에 파이썬 데이터 엔진을 얹어 구현해 볼 것입니다. 언제나 그랬듯 가장 먼저 기둥이 될 데이터 호출 및 가공 라이브러리 엔진들을 코드 최상단 상부 레벨 지점에 올려 임포트 세팅합니다.

```python
In [1]: import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
from statsmodels.api import OLS
import sklearn.model_selection as skm
import sklearn.linear_model as skl
from sklearn.preprocessing import StandardScaler
from ISLP import load_data
from ISLP.models import ModelSpec as MS
from functools import partial
```

We again collect the new imports needed for this lab.
여기에 덧붙여, 이전 실습 챕터에선 보지 못했던 6장 랩 전용 파이프라인(pipeline)과 부분 집합 자동 체계 호출을 돕는 생소한 커스텀 호출 라이브러리 객체들을 새로 공수해 호출합니다.

```python
In [2]: from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from ISLP.models import \
    (Stepwise,
     sklearn_selected,
     sklearn_selection_path)
!pip install l0bnb
from l0bnb import fit_path
```

We have installed the package `l0bnb` on the fly. Note the escaped `!pip install` — this is run as a separate system command.
위 명령 구문 한편에서 우리는 `l0bnb`라는 낯선 외부 조달 패키지 모형을 파이썬 스크립트 진행 도중에 기습적으로 즉석 설치했습니다. 명령어 백틱 안에 숨어있는 탈출 제어문인 `!pip install` 키워드 표기 구문에 단연 집중해 주십시오 — 파이썬 콘솔의 엔진이 아닌, 노트북 모듈 내장 제어를 뚫고 바깥 컴퓨터 백그라운드 환경의 외부 독립 시스템 셸(shell) 터미널 명령어로 파생되어 강제 별도 실행된다는 특수한 권한 위임 체계를 의미합니다.

---

## Sub-Chapters (하위 랩 코딩 실습 과정 요약)

### 6.5.1 Subset Selection Methods (부분집합 자동 선택 메서드 툴박스 파이썬 실습)
* [문서로 이동하기](./6_5_1_subset_selection_methods/)

본 단원에서는 사이킷런(Scikit-Learn) 엔진 및 부가 파생 알고리즘 툴킷 라이브러리가 제공하는 다차원 검정 세트, 모델 AIC, BIC 에러율 식 등을 파이썬 콘솔상에 띄우고 직접 가동하기 위한 평가 함수들을 유연하게 구성해냅니다. 이를 토대로 주어진 빅데이터 내에서 최상의 변수 조합을 찾아 발굴해 내는 '변수 중요도 평가 서치 추적 궤도' 과정을 콘솔 모의 환경 위에서 체계적으로 구현 실습해 봅니다.

### 6.5.2 Ridge Regression and the Lasso (파이썬 능선 정규화 및 라쏘 분석기 실전 적용 사례)
* [문서로 이동하기](./6_5_2_ridge_regression_and_the_lasso/)

Scikit-Learn 기계학습 모듈 라이브러리의 핵심 모델로 불리는 `Ridge` 클래스 파생 인스턴스와 `Lasso` 세팅 클래스를 불러옵니다. 모의 데이터상에서 최적의 알파($\alpha$) 파라미터 규제 값(패널티 강도) 변동 축에 따른 측정 계수 변화선의 곡선 궤적을 렌더링하고, 실제 모의 훈련 단계를 거친 실전 예측 성능 도출 측정 및 그 결과물 시각화 산출을 완성해 봅니다.

### 6.5.3 PCR and PLS Regression (빅데이터 차원 축소 후 연산, PCR-주성분 기반 회귀 실습)
* [문서로 이동하기](./6_5_3_pcr_and_pls_regression/)

마지막으로 최신 모듈인 파이프라인(pipeline) 설계 툴을 이용하여 PCA 분해 패키지 모듈을 전처리용 선형 단위로 파이프라인 앞단에 견고하게 붙여 결합시킵니다. 이후 원본 지표인 주성분 변수를 차원 컷 스코어로 분할 단위로 대거 축소 변환하고, 그 즉시 변환 처리된 축소 결과물을 후단의 최종 선형회귀 예측 모델에 한달음에 태워 분석하는 세련된 다단 변환 기계학습 테크닉 설계 과정을 몸소 체득합니다.

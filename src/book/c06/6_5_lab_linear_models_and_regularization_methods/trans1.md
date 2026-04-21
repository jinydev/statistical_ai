---
layout: default
title: "trans1"
---

# 6.5 실습: 선형 모델과 정규화 기법 (Lab: Linear Models and Regularization Methods)

In this lab we implement many of the techniques discussed in this chapter. We import some of our libraries at this top level.
이 실습 환경에서 우리는 본 장에서 논의되었던 다양한 기술들을 실질적으로 구현해 봅니다. 우선 몇몇 핵심 라이브러리들을 모듈 최상단 레벨에서 다음과 같이 먼저 임포트합니다.

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
이어 이번 실습 시나리오 과정에 추가로 필요해진 주요 라이브러리들을 추가로 수집하여 호출합니다.

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
위 구문에서 우리는 `l0bnb` 패키지를 구동 과정 중에 즉석으로 설치했습니다. 백틱 기호로 탈출 처리된 `!pip install` 셸 구문에 주목하십시오 — 이 구문 표시는 파이썬 과정 내부가 아닌 별도의 분리된 시스템 명령어로써 백그라운드 환경에서 실행되게 작동함을 의미합니다.

---

## Sub-Chapters (하위 목차)

### 6.5.1 Subset Selection Methods (부분집합 자동 선택 메서드 툴박스 파이썬 실습)
* [문서로 이동하기](./6_5_1_subset_selection_methods/)

사이킷런 및 기타 파생 알고리즘 툴킷의 다차원 검정, 모델 AIC, BIC 에러율 식을 직접 가동하기 위한 평가 함수들을 구성하여 변수 중요도 서치 과정을 콘솔 위에서 구현해 봅니다.

### 6.5.2 Ridge Regression and the Lasso (파이썬 능선 정규화 및 라쏘 분석기 실전 적용 사례)
* [문서로 이동하기](./6_5_2_ridge_regression_and_the_lasso/)

Scikit-Learn 기계학습 모듈 라이브러리의 `Ridge` 클래스 인스턴스와 `Lasso` 클래스를 불러와 알파 파라미터 값(패널티 강도) 변동에 따른 계수 변화선 추적 궤적을 렌더링하고 모의 실전 성능 측정 및 시각화를 완료합니다.

### 6.5.3 PCR and PLS Regression (빅데이터 차원 축소 후 연산, PCR-주성분 및 부분 최소 제곱 회귀 실습)
* [문서로 이동하기](./6_5_3_pcr_and_pls_regression/)

PCA 성분 분해 패키지 모듈을 사전 전처리용 단위로 파이프라인(pipeline) 앞단에 결합 매핑한 후 원본 주성분 변수를 차원 컷 스코어로 일괄 변환하고, 이후 이 처리된 결과물을 후단 기저 최종 선형회귀 모델에 한 번에 태우는 세련된 복합 기계학습 테크닉 과정을 체득합니다.

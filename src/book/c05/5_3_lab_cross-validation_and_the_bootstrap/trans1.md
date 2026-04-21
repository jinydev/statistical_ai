---
layout: default
title: "trans1"
---

# 5.3 Lab: Cross-Validation and the Bootstrap 
# 5.3 실습: 교차 검증과 부트스트랩

In this lab, we explore the resampling techniques covered in this chapter.
이 실습 환경에서, 우리는 방금 현 5장에서 집중적으로 다루었던 재표본 추출(resampling) 기법들을 심도 있게 직접 탐구해 볼 것이다.

Some of the commands in this lab may take a while to run on your computer. 
이 실습에서 요구되는 일부 연산 명령어들의 경우 사용자의 기기 컴퓨터에서 마저 구동되는 데 다소 적지 않은 약간의 시간이 소요될 수 있다.

We again begin by placing most of our imports at this top level. 
우리는 다시금 이번에도 응당 우리가 기용할 임포트(imports) 선언 패키지 내역들의 대부분을 이 가장 상단 맨 꼭대기 최상위 위치 층위에 포진 배치시켜 적재해 둠으로써 순탄하게 이번 실전 실습 단계를 전격 시작 개시 발동 발단시킨다.

```python
In [1]: import numpy as np
        import statsmodels.api as sm
        from ISLP import load_data
        from ISLP.models import (ModelSpec as MS,
                                 summarize,
                                 poly)
        from sklearn.model_selection import train_test_split
```

There are several new imports needed for this lab. 
물론 이번 실험 실습 장비 무대를 단단히 거치 소화해 내기 위해서는 기존에 없던 다수의 생소한 몇 가지 새로운 패키지 임포트 장치들 또한 필연 추가 요구 지참된다.

```python
In [2]: from functools import partial
        from sklearn.model_selection import \
             (cross_validate,
              KFold,
              ShuffleSplit)
        from sklearn.base import clone
        from ISLP.models import sklearn_sm
```

---

## Sub-Chapters (하위 목차)

### 5.3.1 The Validation Set Approach (샘플 분할 세트 실습)
* [문서로 이동하기](./5_3_1_the_validation_set_approach/)

내장 파이썬 데이터 전처리 분할 함수인 `train_test_split`을 이용해 랜덤하게 데이터를 분리하는 가장 근원적 검증 파이프라인을 작성합니다.

### 5.3.2 Cross-Validation (파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_2_cross-validation/)

머신런 패키지의 `KFold`와 `cross_validate` 인자 속성을 엮어서 변수의 다항식 확장에서 최고 성능을 발휘하는 파라미터 계층을 스캔합니다.

### 5.3.3 The Bootstrap (넘파이 부트스트랩 구현 실습)
* [문서로 이동하기](./5_3_3_the_bootstrap/)

복원 랜덤 추출 함수나 넘파이의 쵸이스 기능을 통해 부트스트랩 헬퍼 함수를 스스로 작성하고, 통계 모수치의 표준 오차를 통계 엔진 없이 순수 시뮬레이션 해봅니다.

---
layout: default
title: "trans1"
---

# 5.3 Lab: Cross-Validation and the Bootstrap
# 5.3 랩: 교차 검증과 부트스트랩

In this lab, we explore the resampling techniques covered in this chapter. Some of the commands in this lab may take a while to run on your computer. 
이 랩(lab)에서 우리는 이번 장에서 다루어진 재표본 추출(resampling) 기법들을 탐색해 봅니다. 본 실습의 명령어 중 일부는 여러분의 컴퓨터에서 실행되는 데 꽤 시간이 걸릴(take a while) 수도 있습니다.

We again begin by placing most of our imports at this top level. 
우리는 또다시 대부분의 임포트(imports)를 이 최상단 레벨에 배치하는 것으로 시작합니다.

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
이 랩을 위해 필요한 새 임포트 항목이 몇 가지 존재합니다.

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
* [문서로 이동하기](./5_3_1_the_validation_set_approach/trans1.html)

### 5.3.2 Cross-Validation (파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_2_cross-validation/trans1.html)

### 5.3.3 The Bootstrap (넘파이 부트스트랩 구현 실습)
* [문서로 이동하기](./5_3_3_the_bootstrap/trans1.html)

---
layout: default
title: "trans2"
---

# 5.3 Lab: Cross-Validation and the Bootstrap
# 5.3 파이썬 해킹 랩: 교차 검증과 부트스트랩 코딩 마스터하기!

In this lab, we explore the resampling techniques covered in this chapter. Some of the commands in this lab may take a while to run on your computer. 
드디어 이론의 늪에서 벗어나 실전 파이썬 해킹 랩(Lab) 에 입성했습니다! 이번 랩에서는 방금 전까지 우릴 괴롭혔던 기상천외한 데이터 우려먹기(재표본 추출 resampling) 기술들을 직접 코딩으로 때려잡을 겁니다. 경고 하나 날립니다: 몇몇 파이썬 뺑뺑이 명령어들은 당신의 노트북 팬 소리를 헬리콥터처럼 울리며 연산에 시간을 좀 잡아먹을(take a while) 수 있으니 각오하세요!

We again begin by placing most of our imports at this top level. 
자, 언제나 그렇듯 해킹을 시작하기 전, 우리의 무기 세트인 패키지들을 최상단(top level) 에 싹 다 꺼내놓고(imports) 장전을 엽니다.

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
이번 랩의 메인 요리들을 씹어먹기 위해 새롭게 참전하는 신규 장비(imports) 도 몇 개 존재합니다. 세팅 완료!

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
* [문서로 이동하기](./5_3_1_the_validation_set_approach/trans2.html)

### 5.3.2 Cross-Validation (파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_2_cross-validation/trans2.html)

### 5.3.3 The Bootstrap (넘파이 부트스트랩 구현 실습)
* [문서로 이동하기](./5_3_3_the_bootstrap/trans2.html)

---
layout: default
title: "trans2"
---

# 5.3 Lab: Cross-Validation and the Bootstrap 
# 5.3 실습: 교차 검증과 부트스트랩 (이론을 코드로 박살내기)

In this lab, we explore the resampling techniques covered in this chapter.
드디어 머리 아픈 수식에서 벗어나 키보드를 잡을 시간입니다. 이번 실습에서는 5장의 메인 요리였던 '교차 검증'과 '부트스트랩'이라는 미친 재표본 추출(resampling) 기법들을 파이썬 코드로 직접 뜯어보고 후드려 팰 예정입니다.

Some of the commands in this lab may take a while to run on your computer. 
참고로 미리 경고합니다. 이번 실습에 나오는 몇몇 명령어들은 쪼잔하게 데이터 몇 개 돌리는 게 아니라서, 여러분의 가여운 컴퓨터 쿨러를 미친 듯이 돌게 만들며 연산 시간이 꽤 징그럽게 걸릴 수도 있습니다. 쫄지 말고 기다리세요.

We again begin by placing most of our imports at this top level. 
늘상 하던 룰대로, 우리가 이 구역에서 써먹을 장비(import) 들을 문서 맨 꼭대기에 우수수 모조리 다 갖다 박아놓으면서 전투 준비를 시작합니다.

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
아, 그리고 이번 노가다 전투판을 뛰려면 기존 무기 외에도 몇 가지 생소한 특수 머신러닝 패키지 단검들이 추가로 세팅 창고에 필요합니다. 미리 챙겨두죠.

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

## Sub-Chapters (하위 퀘스트 목록)

### 5.3.1 The Validation Set Approach (반반 무 많이: 샘플 분할 세트 실습)
* [문서로 이동하기](./5_3_1_the_validation_set_approach/)

파이썬이 떠먹여 주는 데이터 전처리 분할 타격 함수 `train_test_split`을 써서 무자비하게 데이터를 반갈죽 내버리는, 가장 원시적이고 고전적인 검증 파이프라인을 뚫어봅니다.

### 5.3.2 Cross-Validation (사이킷런의 은총: 파이썬 K-Fold K분할 실습)
* [문서로 이동하기](./5_3_2_cross-validation/)

사이킷런 머신러닝 패키지가 하사하는 `KFold`와 `cross_validate` 속성 치트키를 비빔밥처럼 엮어서, 노가다 없이 변수의 다항식 확장에서 최고로 잘 방어하는 파라미터 최적값을 스캔해 찾아냅니다.

### 5.3.3 The Bootstrap (무에서 유를 창조하는 사기극: 부트스트랩 넘파이로 구현 실습)
* [문서로 이동하기](./5_3_3_the_bootstrap/)

넘파이(Numpy)의 `choice` 함수를 무기 삼아 변태 같은 복원 무한 랜덤 추출기를 스스로 코드 한 땀 한 땀 작성해 보고, 통계 엔진의 도움이라곤 1도 없이 무식하게 오로지 깡 시뮬레이션 하나만으로 통계 모수치의 표준 오차를 후려쳐서 때려 맞추는 기염을 토해냅니다.

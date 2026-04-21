---
layout: default
title: "trans1"
---

# `Out[13]:` `array([23.6166])`

One can estimate the variability in the test error by running the following: 
누구든지 다음을 실행함으로써 구동된 테스트 에러 상에 나타나는 불확실성 변동성(variability) 치수를 연산 추정해 낼 수 있습니다:

```python
In [14]: validation = ShuffleSplit(n_splits=10,
                                   test_size=196,
                                   random_state=0)
         results = cross_validate(hp_model,
                                  Auto.drop(['mpg'], axis=1),
                                  Auto['mpg'],
                                  cv=validation)
         results['test_score'].mean(), results['test_score'].std()
```

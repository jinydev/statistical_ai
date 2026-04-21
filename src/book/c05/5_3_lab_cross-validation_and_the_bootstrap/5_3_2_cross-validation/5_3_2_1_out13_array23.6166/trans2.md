---
layout: default
title: "trans2"
---

# **`Out[13]:`** `array([23.6166])` 

One can estimate the variability in the test error by running the following: 
"내 무기가 쏘는 에러 점수가 지금 한 번만 요행으로 잘 나온 게 아니라, 진짜 믿을 만하게 덜 요동치는 기복 없는 스펙인가?" 그 징그러운 예측 '요동폭(variability)' 의 민낯을 알고 싶다면, 그저 무지성으로 아래 코드를 긁어다 실행(running) 시켜버리면 그만입니다:

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

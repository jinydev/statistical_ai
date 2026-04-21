---
layout: default
title: "trans1"
---

# **`Out[13]:`** `array([23.6166])` 

One can estimate the variability in the test error by running the following: 
누군가는 곧장 아래에 도열 제시된 연산 후행 조작 코드 편을 시연 실행 가동(running) 해 봄으로써; 당해 모형이 맞닥뜨려 터뜨린 궤적 속 저 널뛰는 테스트 에러 오차 타율의 숱한 요동 분산 변동성 파장 스펙(variability) 치수를 능히 쉽게 거뜬히 연산 축출 역산 가늠해(estimate) 추정 산출해 낼 수 있다: 

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

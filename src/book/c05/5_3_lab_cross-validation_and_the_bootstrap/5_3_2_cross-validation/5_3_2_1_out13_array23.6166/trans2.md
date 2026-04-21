---
layout: default
title: "trans2"
---

# `Out[13]:` `array([23.6166])`

One can estimate the variability in the test error by running the following: 
오답률 23점 찍히는 거 보셨죠? 그럼 이번엔 똑똑한 해커답게 아래 코드를 복붙해서 돌려보세요. 아까 귀가 닳도록 들은 그놈의 지옥 같은 주사위 널뛰기, 즉 모의고사 오답 점수의 '가변성(variability) 요동' 이 대체 어느 정도인지 숫자로 직접 견적을 뽑아볼 수 있습니다!

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

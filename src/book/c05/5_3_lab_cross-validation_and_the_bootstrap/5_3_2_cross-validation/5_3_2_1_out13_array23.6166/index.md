---
layout: default
title: "index"
---

# **`Out[13]:`** `array([23.6166])` 

One can estimate the variability in the test error by running the following: 

```
In [14]:validation=ShuffleSplit(n_splits=10,
test_size=196,
random_state=0)
results=cross_validate(hp_model,
Auto.drop(['mpg'],axis=1),
Auto['mpg'],
cv=validation)
results['test_score'].mean(),results['test_score'].std()
```

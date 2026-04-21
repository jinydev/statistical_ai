---
layout: default
title: "index"
---

[< 3.6.4 Multivariate Goodness Of Fit](../index.html) | [3.6.5 Interaction Terms >](../../3_6_5_interaction_terms/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# List Comprehension

Often we encounter a sequence of objects which we would like to transform for some other task.

List comprehensions are simple and powerful ways to form lists of `Python` objects.

나아가 파이썬 언어 체계는 비단 이뿐만 아니라 고유의 딕셔너리(dictionary) 기반 컴프리헨션 및 이른바 _제너레이터_ (generator, 발생기) 컴프리헨션 기능 등도 막강히 동반 지원해(supports) 주지만, 이들에 관한 구체적 논의는 현 다변량 회귀 목차에서 다루고자 제정한 우리 책의 본연의 학습 범위(scope) 한도를 한참 벗어나는 사안입니다. Let’s look at an example.

```
In [29]: vals = [VIF(X, i)
          for i in range(1, X.shape[1])]
vif = pd.DataFrame({'vif': vals},
                   index=X.columns[1:])
vif
```

```
Out[29]:
```

```
vif
crim1.767
zn2.298
indus3.987
chas1.071
nox4.369
rm1.913
age3.088
dis3.954
rad7.445
tax9.002
ptratio1.797
lstat2.871
```

```
variance_
inflation_
factor()
```

The function `VIF()` takes two arguments: a dataframe or array, and a variable column index.

```
In [30]: vals = []
for i in range(1, X.values.shape[1]):
    vals.append(VIF(X.values, i))
```

List comprehension allows us to perform such repetitive operations in a more straightforward way.

---

## Sub-Chapters


[< 3.6.4 Multivariate Goodness Of Fit](../index.html) | [3.6.5 Interaction Terms >](../../3_6_5_interaction_terms/index.html)

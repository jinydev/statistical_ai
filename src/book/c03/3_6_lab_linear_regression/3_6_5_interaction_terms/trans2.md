---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/trans2.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/trans2.html)

# _3.6.5 Interaction Terms_

# 3.6.5 상호 작용 항 실습: 찰떡궁합 시너지 효과 찾기

It is easy to include interaction terms in a linear model using `ModelSpec()`.
"TV 광고랑 라디오 광고를 같이하면 시너지(상호 작용)가 팍 터진다!" 아까 회귀 이론 시간에 입 아프게 배웠던 이른바 **'상호 작용 항(interaction terms 시너지 효과)'**을 억지로 파이썬 선형 모델 코딩 체제 속에 욱여넣으려면 어떻게 할까요? 수식을 일일이 쓸 필요 없이, 우리의 만능 요리사 기본 `ModelSpec()` 도구를 차용하면 거뜬히 엄청 손쉽게(easy) 포함해 설계 라인에 삽입해 넣을 수 있습니다. 

Including a tuple `("lstat", "age")` tells the model matrix builder to include an interaction term between `lstat` and `age`.
예컨대 소괄호로 묶인 파이썬의 튜플(tuple) 묶음 형태인 **`("lstat", "age")`** 조각 하나를 `MS([])` 연산식 괄호 안에 슬쩍 명시해서 포함 귀속(Including)해 주면, 이는 마법 공장 행렬 조합기(builder) 도구 측에게 "야, 저 빈민율(`lstat`)이랑 고물집(`age`) 두 변수가 서로 북치고 장구치며 짬뽕으로 일으키는 실질적 시너지 폭발 상호 작용 항(곱하기 항)을 모델에 산입 포함해!"라는 아주 명확한 코드의 지시(tells) 주문으로 강력하게 작동합니다.

```python
In [31]: X = MS(['lstat',
                'age',
                ('lstat', 'age')]).fit_transform(Boston)
model2 = sm.OLS(y, X)
summarize(model2.fit())
```

```python
Out[31]:           coef  std err       t  P>|t|
intercept 36.0885   1.470  24.553  0.000
lstat     -1.3921   0.167  -8.313  0.000
age       -0.0007   0.020  -0.036  0.971  (고물집 단독 효과는 개뿔..)
lstat:age  0.0042   0.002   2.244  0.025  (시너지 효과는 유의미하다!)
```

결과를 보면 기막히게도 `lstat:age` 라는 이름으로 두 놈이 합쳐진 시너지 변수가 새로 태어났습니다! P-값도 0.025로 낮아서 유독 이 둘이 결합했을 때 집값에 유의미한 콜라보 효과를 미친다는 걸 통계적으로 깔끔하게 증명해 냈군요!

---

## Sub-Chapters (하위 목차)


[< 3.6.4.1 List Comprehension](../3_6_4_multivariate_goodness_of_fit/3_6_4_1_list_comprehension/trans2.html) | [3.6.6 Non-Linear Transformations Of The Predictors >](../3_6_6_non-linear_transformations_of_the_predictors/trans2.html)

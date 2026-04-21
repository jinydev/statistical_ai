---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.4 Multivariate Goodness Of Fit](../trans2.html) | [3.6.5 Interaction Terms >](../../3_6_5_interaction_terms/trans2.html)

# List Comprehension

# 리스트 컴프리헨션(List Comprehension): 파이썬 고수들의 우아한 꼼수

Often we encounter a sequence of objects which we would like to transform for some other task.
프로그래밍 실무를 하다 보면, 길게 줄지어 서 있는 100만 명의 학생들(객체 배열)의 성적 점수를 하나하나 꺼내서 일일이 10점씩 더해준 뒤 다시 새로운 줄표 모델로 길게 세우는(transform) 짜증 나는 반복 구동 작업을 수도 없이 마주치게(encounter) 됩니다. 

Below, we compute the VIF for each feature in our `X` matrix and produce a data frame whose index agrees with the columns of `X`.
당장 아래 예시 미션만 봐도 그래요! 우리는 지금 행렬 `X` 안에 잔뜩 든 12개의 각종 잡다한 특징(feature) 변수 하나하나마다 일일이 VIF(분산 팽창 계수) 지표 점수를 반복 도출 연산해(compute) 내야 합니다! 거기다 그걸 예쁘게 엑셀 행/열처럼 맞춰서 최초의 행렬 `X` 측 열(columns) 이름표 순서에 예쁘게 딱 들어맞는 판다스 데이터 프레임 표로 뽑아내야(produce) 하죠.

The notion of list comprehension can often make such a task easier.
이럴 때마다 C언어에서 하듯 촌스럽게 세 줄 네 줄짜리 무식한 `for` 반복문을 짤 수도 있겠지만... 우린 파이썬의 축복인 **'리스트 컴프리헨션(list comprehension, 리스트 내포)'** 이란 마법의 핵심 꼼수 개념 기조를 적극 활용할 겁니다. 이 마법 주문만 있으면 대체로 이런 귀찮고 징그러운 연산 과업 처리 과정이 단 한 줄로 엄청나게 우아하고 손쉬워(easier)집니다!

List comprehensions are simple and powerful ways to form lists of `Python` objects.
리스트 컴프리헨션 체제는, 저 기나긴 파이썬 고유의 독립 객체 리스트들을 굉장히 단순(simple)하면서도 기막히게 강력(powerful)한 파워로 순식간에 휘리릭 엮고 생성해(form) 내는 매우 훌륭한 파이썬 최고 존엄 필수 구사 기법입니다. (딕셔너리나 제너레이터 등도 똑같이 마법을 부릴 수 있지만 그건 나중에 배우자고요!)

We compute the VIF for each of the variables in the model matrix `X`, using the function `variance_inflation_factor()`.
그럼 어디 백문이 불여일타! 대망의 리스트 컴프리헨션 실체 적용단 예제를 살펴볼까요.
우선 저변 도구인 `variance_inflation_factor()` (이하 짧게 `VIF()`) 구동 함수를 다분히 유용 차용해, 아까 모델 행렬 `X` 측에 12개나 아로새겨진 각 단위 변수들에 대한 고유 VIF 공선성 점수를 낱낱이 도출 계산(compute)해 봅니다.

```python
In [29]: vals = [VIF(X, i) for i in range(1, X.shape[1])]
vif = pd.DataFrame({'vif': vals},
                   index=X.columns[1:])
vif
```

```python
Out[29]:
```

|**`vif`**| |
|---|---|
|`crim`|`1.767`|
|`zn`|`2.298`|
|`indus`|`3.987`|
|`chas`|`1.071`|
|`nox`|`4.369`|
|`rm`|`1.913`|
|`age`|`3.088`|
|`dis`|`3.954`|
|`rad`|`7.445` (주의! 점수 높음)|
|`tax`|`9.002` (삐익! 빨간불!)|
|`ptratio`|`1.797`|
|`lstat`|`2.871`|

The function `VIF()` takes two arguments: a dataframe or array, and a variable column index.
코드 해설을 해볼까요? 앞서 동원한 함수인 `VIF()` 요체는 늘 2가지 밥(인자, arguments)을 요구합니다: 하나는 뒤질 전체 판때기인 '데이터 프레임 내지 배열 덩어리'이며, 다른 하나는 콕 집어 검색할 '특정 변수의 위치 번호표(column index)'입니다. 

In the code above we call `VIF()` on the fly for all columns in `X`.
위쪽 코드 구문 서술 대목에서 우린 저 마법의 대괄호 `[ ... ]` 안에서 `X`의 번호표(`i`)를 반복하며 모든 열들을 통째로 대상으로 삼아 바로 그 좁은 단 한 줄의 도출 현장 안에서 즉석에 그때그때(on the fly) `VIF()` 연산 함수를 다다닥! 연달아 차출 호출(call)해버렸습니다. 단 1줄 만에요!

We have excluded column 0 above (the intercept), which is not of interest.
단, 여기서 주의할 꿀팁 한 가지! 유독 `range(1, ...)` 이렇게 1번부터 시작해서 맨 첫 번째 0번 위치(`column 0`, 즉 `intercept` 절편상수)만큼은 쏙 빼고 배제(excluded)했다는 점입니다. 이 절편 따위는 다른 변수랑 겹치든 말든 이 공선성(VIF) 검사라는 대목에서 굳이 애써 관찰할 주된 관심사(not of interest) 표적이 애초에 아니기 때문이죠. 

In this case the VIFs are not that exciting.
그렇게 열심히 돌려본 결과표를 봤을 때... 솔직히 유감스럽게도 이번 산입 국면 사례에서 산출된 VIF 점수 결괏값 수위는 `tax` 하나 살짝 높은 거 빼고는 대체로 고만고만해서 그닥 드라마틱하게 속을 썩일 만큼 특별나게 썩 이목을 끌 만한 흥미 진진한 수치(not that exciting)는 못 되네요.

The object `vals` above could have been constructed with the following for loop:
자, 만약 아까 파이썬의 마법을 안 썼다면 저 반환 취합 객체 보따리 `vals` 구성 체제는, 기실 하단에 제시된 아래 구식 3줄짜리 촌스러운 C언어식 `for` 반복문(for loop) 배열 수식을 꾸역꾸역 동원해서 타이핑을 쳐야 똑같이 비슷하게 치환 조립 구현해 낼(constructed) 수 있었을 겁니다.

```python
In [30]: vals = []
for i in range(1, X.values.shape[1]):
    vals.append(VIF(X.values, i))
```

List comprehension allows us to perform such repetitive operations in a more straightforward way.
보이시나요? 저렇게 빈 박스를 먼저 만들고(`vals = []`), 뺑뺑이 돌리고(`for i...`), 일일이 집에 넣고(`append()`) 하는 3줄짜리 구식 코드를 **대괄호 하나(`[ ... for ... in ... ]`) 안에 딱 1줄로** 압축시켜 버리는 것!
이것이 바로 리스트 컴프리헨션(List comprehension) 구동 잣대의 기막힌 매력입니다! 이를 적재적소 발탁 기용할 때에야 비로소 따분히 노가다로 반복되는 여느 연산 취합 작업 단계(repetitive operations)를 한층 더 파이썬스럽게 우아하고, 짧고 직관적이며 직진 명료한 직선 방식(straightforward way)으로 손쉽게 처리(perform)해 낼 수 있는 거죠! 완전 신세계죠?!

---

## Sub-Chapters (하위 목차)


[< 3.6.4 Multivariate Goodness Of Fit](../trans2.html) | [3.6.5 Interaction Terms >](../../3_6_5_interaction_terms/trans2.html)

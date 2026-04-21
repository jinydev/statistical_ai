---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.5 Interaction Terms](../3_6_5_interaction_terms/trans2.html) | [3.6.6.1 In 33 Anovalmresults1 Results3 >](3_6_6_1_in_33_anovalmresults1_results3/trans2.html)

# _3.6.6 Non-linear Transformations of the Predictors_

# 3.6.6 예측 변수의 비선형 변환 실습: U자형 커브 곡선 만들기

The model matrix builder can include terms beyond just column names and interactions.
앞서 다뤘던 우리의 든든한 마법 공장 `ModelSpec()` 행렬 조합기 체제는, 비단 단순하게 열 이름(column names) 텍스트를 집어넣거나 방금 전 배운 상호 작용 항(곱하기 항)을 산입 처리하는 초보적인 수준 기능을 훌쩍 넘어서서(beyond), 수학적으로 훨씬 더 꼬아놓은 아주 다양한 파생 차원 항(예: 2차, 3차 함수꼴)들까지도 너끈히 묶어 포함(include)시킬 수 있는 괴물입니다.

For instance, the `poly()` function supplied in `ISLP` specifies `poly()` that columns representing polynomial functions of its first argument are added to the model matrix.
가령 예컨대, 오늘 우리가 배우는 `ISLP` 핵심 패키지 근간에 유용히 구비되어 제공되는(supplied) **`poly()`** 라는 치트키 함수 조각을 모델 변수 괄호 안에 기용 지시하면! 파이썬은 똑똑하게도 해당 변수의 고유 데이터값들을 가져다가 2차, 3차 다항식 곡선 함수(polynomial functions) 모양의 $x^2, x^3$ 발현 궤적을 덧그리는 파생 열 치수들을 모델 분석 행렬에 알아서 스르륵 새로 추가(added)해주도록 명시(specifies)해 줍니다. 

```python
In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston)
model3 = sm.OLS(y, X)
results3 = model3.fit()
summarize(results3)
```

```python
Out[32]:
```

|**`Out[32]:`**|`coef(계수)`|`std err(오차)`|`t`|`P>|t|(피-값)`|
|---|---|---|---|---|
|`intercept`|`17.7151`|`0.781`|`22.681`|`0.000`|
|`poly(lstat, degree=2)[0]`|`-179.2279`|`6.733`|`-26.620`|`0.000` (직선 효과)|
|`poly(lstat, degree=2)[1]`|`72.9908`|`5.482`|`13.315`|`0.000` (U자 곡선 효과!)|
|`age`|`0.0703`|`0.011`|`6.471`|`0.000`|

The effectively zero $p$-value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.
출력표 결과를 보시죠. 새롭게 만들어진 **2차항(quadratic term, $x^2$, 즉 위 표의 세 번째 줄 지표 `poly()[1]`)** 변수 칸의 파생 **$p$-값(p-value) 수위가 무려 통계적으로 완벽에 가까운 0.000 점(effectively zero)에 아주 딱 근접**했다는 점! 
이건 무슨 뜻일까요? 바로 우리가 단순 직선 효과만 쓰지 않고 굳이 곡선(U자 형태) 변수 항 모형을 추가 투입 조작해 준 것이, 무작정 일직선으로 모델을 그었던 때보다 한결 더 우수하게 딱 들어맞게 개선 향상된(improved) 우위 모델을 도출해 냈음(leads to)을 강렬히 암시 시사(suggests)해 주고 있는 겁니다! 집값이 빈민율과 1차원적인 관계가 아니라 살짝 휜 관계라는 뜻이죠.

By default, `poly()` creates a basis matrix for inclusion in the model matrix whose columns are _orthogonal polynomials_ , which are designed for sta- orthogonal ble least squares computations. [13]
자, 그런데 좀 어려운 원리를 하나 짚고 가죠. 초기 기본 설정(default) 기조상 `poly()` 함수는, 아무 생각 없이 $x$ 와 $x^2$ 수치를 그대로 곱해서 쓰지 않습니다. 대신 향후 모델 행렬에 쏙 귀속될 별도 기저 행렬(basis matrix) 판을 산출해 낼 때, 이 열 성분들을 다름 아닌 통계학의 고급 기술 **'직교 다항식(orthogonal polynomials)'** 형태로 변환(수직 스케일링)해버립니다. 왜 굳이 그럴까요? 이는 전적으로 최소 제곱(least squares) 연산을 컴퓨터가 뒤뚱거리지 않고 계산 에러 없이 엄청나게 구조적 안정(stable) 국면으로 매끄럽게 처리하게끔(designed for) 특수 설계된 안전장치이기 때문입니다. [13]

Alternatively, had we included an argupolynomial ment `raw=True` in the above call to `poly()` , the basis matrix would consist simply of `lstat` and `lstat**2` .
아, "이딴 거 머리 아프고 싫다! 난 그냥 순수하게 빈민율(`lstat`)이랑 그걸 그냥 제곱한 값(`lstat**2`)만 정직하게 쓰고 싶어!" 라고 생각하신다면 대안적(Alternatively)인 꼼수 기법도 있습니다! 
우리가 만일 앞서 `poly()` 함수 괄호 안에 고의로 **`raw=True`** 라는 억지 설정 인자(argument) 항목을 콤마로 찍어 추가 기입 명시했다면, 거시적 기저 연산 행렬 산입 양상은 지극히 단순명료하게 그저 일차 날것 `lstat` 와 2차 다항 무식한 제곱항 `lstat**2` 숫자로만 툭 간략 직조 구성되었을(consist) 터입니다.

Since either of these bases represent quadratic polynomials, the fitted values would not change in this case, just the polynomial coefficients.
다만 여기서 다행인 점! 이 '직교' 방식이나 '날것(raw)' 방식 두 가지 기저(bases) 갈래가 본질적으로는 어쨌든 매한가지 똑같은 **2차 포물선 다항식(quadratic polynomials)** 수학 양태의 곡선을 대변(represent)하고 있기 때문에, 최종 도출되어 예측되는 집값 적합 값(fitted values) 결과 치수 직선축 자체는 어느 방식을 쓰든 하등 코딱지만큼의 모 양 변함이 없을 터이며(would not change), 단지 분석 표에 나오는 기계적 다항식 계수(coefficients) 숫자 성분들 크기만 표면상 이리저리 다르게 뒤바뀔 뿐입니다. 

Also by default, `poly()` do not include an intercept column as that is automatically added by `MS()` .
또 한 가지 팁! 디폴트 상태에서, `poly()` 함수 지령으로 파생 생성된 요 꼼수 다항 항목 열들의 무리 안에는, 절대로 '1'로만 찬 절편(intercept) 열 성분은 굳이 끼지 않아 포함되지 않는다는(do not include) 사실도 알아두세요. 왜냐고요? 애초에 그런 절편 부분만큼은 `ModelSpec`, 즉 `MS()` 공장장 함수가 아빠처럼 늘 관례적으로 알아서 친히 자동 생성 추가(automatically added)해 주고 계시기 때문에 중복될 필요가 전혀 없거든요!

We use the `anova_lm()` function to further quantify the extent to which `anova_lm()` the quadratic fit is superior to the linear fit.
이에 더해 확실하게 호기심에 쐐기를 박기 위해, 좀이따 우린 **`anova_lm()`** 이라는 분산 분석 함수 도구를 차용 동원해 "과연 이 휘어진 2차 곡선 적합(quadratic fit) 도출 모델이 아까 촌스러웠던 1차 직선 선형 적합 체제 아이들 대비 과연 **수치상 얼마나 쥑이게 상대적 성능 우위원(superior)에 더 진전 등극했는지**"를 아주 뼈아픈 세부 통계 계량 수치로 수량화해 타진(quantify) 비교 분석해 볼 참입니다!

---


### Model Comparison (분산분석을 통한 모델 비교)

`anova_lm()` 함수를 사용해 선형 모델과 비선형 모델 간의 잔차 오차량을 서로 피터지게 비교 분석하고 추가 곡선 계수가 기여하는 통계적 유효성 승리를 검증하는 프로세스입니다.
두 모델 중 과연 어느 것이 더 우수한가 분산분석(ANOVA)으로 확인하는 판사봉 심사 시간이죠!

---

## Sub-Chapters (하위 목차)


[< 3.6.5 Interaction Terms](../3_6_5_interaction_terms/trans2.html) | [3.6.6.1 In 33 Anovalmresults1 Results3 >](3_6_6_1_in_33_anovalmresults1_results3/trans2.html)

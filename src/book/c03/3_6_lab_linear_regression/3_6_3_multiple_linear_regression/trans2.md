---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/trans2.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/trans2.html)

# _3.6.3 Multiple Linear Regression_

# 3.6.3 다중 선형 회귀 실습 - 여러 변수 몽땅 때려넣기!

In order to fit a multiple linear regression model using least squares, we again use the `ModelSpec()` transform to construct the required model matrix and response.
자, 이제 변수 한 개 가지고 깔짝거리던 시시한 장난은 끝났습니다. 변수 여러 개를 짬뽕으로 투입하는 진짜배기 **'다중 선형 회귀(multiple linear regression)'** 통계 모델 기조를, 오차의 제곱을 박살 내는 최소 제곱(least squares) 잣대에 맞춰 거창하게 조립 적합시켜 보고자 합니다. 이때 우리는 앞서 맛본 마법의 찍어내기 기계! 재차 또 한 번 **`ModelSpec()`** 파생 자동 변환 도구를 차용 발탁해 기용함으로써 모델 연산 엔진에 필수 제반 요구 먹이로 투여되는 복합 다중 모델 행렬 단면과 타깃 정답지 응답(response) 과녁 변수판을 온전히 구축 뚝딱 조립 축조해 올립니다.

The arguments to `ModelSpec()` can be quite general, but in this case a list of column names suffice.
사실 이 대단한 `ModelSpec()` 함수 지령 버튼 뒤 구멍에 덧붙여 투입될 제반 잡동사니 인자(arguments) 속성 짐짝들은, 사실 조달 융통성 커스텀의 폭이 무척 광범위 범용적(general)일 수 있지만! 당면한 초보 튜토리얼 이 특수 상황 사례에서만큼은 단지 그저 조달될 타겟 열 이름(column names) 텍스트 명칭표 조각들의 **단순 대괄호 나열 리스트 `[]` 표기만으로도** 아주 충분히 만족스럽게 목적 달성 풀가동에 족합니다(suffice). (이름만 부르면 알아서 찾아갑니다!)

We consider a fit here with the two variables `lstat` and `age`.
이번 다중 회귀 첫 맛보기 분과 대목에서 우린 빈민율 **`lstat`** 변수 그리고 집 연식 **`age`** 변수 딱 이 두 가지 단면 조작 무기만을 거느 동반 취합해 일련의 결합 듀오 적합 연산 과정을 시범 도모 고려해 보겠습니다.

```python
In [25]: X = MS(['lstat', 'age']).fit_transform(Boston)
model1 = sm.OLS(y, X)
results1 = model1.fit()
summarize(results1)
```

```python
Out[25]:
```

```python
           coef  std err       t  P>|t|
intercept 33.2228   0.731 45.458  0.000
lstat     -1.0321   0.048 -21.416 0.000
age        0.0345   0.012  2.826  0.005
```

Notice how we have compacted the first line into a succinct expression describing the construction of `X`.
여기서 눈여겨 코딩 실력을 감탄해 볼 대목 꿀팁은, 애초에 방대할 수밖에 없는 이중 혼합 수학 행렬 `X` 단위 뼈대 머신 판 조립 구축 전 과정을 서술 지시 타건하는 맨 파생 선두 첫째 줄의 저 엄청난 파이썬 코드 단락(`X = MS...`)을!! 우리가 얼마나 무척이나 쉽고 축약 한 방에 영리하고 명료 간결한 형태 구분 표현식 한 줄 라인으로 꽉꽉 압축 다져 밀어(compacted) 놓았는가 하는 짜릿하고 쏠쏠한 점입니다.

The `Boston` data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors.
현재 창고에서 차용 중인 기저 `Boston` 부동산 데이터 세트 덩어리 판 자체에는 무려 총 **12가지** 수량의 다양한 스펙 속성 변수들이 대거 빼곡히 포진 포함(contains) 탑재되어 있는 터라!! 
혹여라도 이들 모든 파편 힌트 예측 변수를 남김없이 깡그리 다 믹서기에 일괄 동원 쓸어 담아 사용해 올스타전 회귀 도출을 단행 수행하고자... 저 멍청한 코드 열 이름 변수명 일체를 `MS(['crim', 'zn', 'indus'...])` 이렇게 무식하게 한 자 한 자 남김없이 오타 없이 죄다 키보드로 쳐 수작업 입력 명기해야(type all of these)만 한다면? 
그건 상상만 해도 무척이나 짜증 나고 거추장스럽고 성가신(cumbersome) 개노가다 번거로운 중노동 형벌이 될 것입니다.

Instead, we can use the following short-hand:
그래서 이를 싹 대신 타개할 영리한 잔머리 타개책으로, 우린 아래처럼 재치 있게 무척 짧게 생략 단축 축약된(short-hand) 속기 뺄셈 방식 얍쌉 약식 파이썬 코딩 꿀팁 표현 도구를 유용히 치트 기용할 수 있습니다:

```python
In [26]: terms = Boston.columns.drop('medv')
terms
```

```python
Out[26]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
       'rad', 'tax', 'ptratio', 'lstat'],
      dtype='object')
```

We can now fit the model with all the variables in `terms` using the same model matrix builder.
짜잔! 집값 결과치(`medv`) 딱 하나만 빼고(`drop`) 남은 열 이름 전체를 `terms`라는 보따리에 한 번에 주워 담았습니다! 
이제 우린 방금 전 수단과 완벽히 매한가지 똑같은 방식의 마법 공장 모델 행렬 조합기(builder, `MS()`) 생성 자동 툴 도구를 그대로 적용 차용하면서도, 저 `terms` 복주머니 부문 내에 묶여 편입된 이 **모든 12개의 남은 떼거지 변수 항목들**을 단 한 줄 `MS(terms)`로 일괄 모델 도마에 일제히 욱여넣고 결집 총 적합(fit)시켜 볼 수 아주 쉽게 있습니다. (진정한 코딩의 묘미죠!)

```python
In [27]: X = MS(terms).fit_transform(Boston)
model = sm.OLS(y, X)
results = model.fit()
summarize(results)
```

|**`Out[27]:`**|`coef(계수)`|`std err(오차)`|`t(티-값)`|`P>|t|(피-값)`|
|---|---|---|---|---|
|`intercept`|`41.6173`|`4.936`|`8.431`|`0.000`|
|`crim`|`-0.1214`|`0.033`|`-3.678`|`0.000`|
|`zn`|`0.0470`|`0.014`|`3.384`|`0.001`|
|`indus`|`0.0135`|`0.062`|`0.217`|`0.829` (얘는 쓸모없군요!)|
|`chas`|`2.8400`|`0.870`|`3.264`|`0.001`|
|`nox`|`-18.7580`|`3.851`|`-4.870`|`0.000`|
|`rm`|`3.6581`|`0.420`|`8.705`|`0.000`|
|`age`|`0.0036`|`0.013`|`0.271`|`0.787` (얘도 쓸모없네요!)|
|`dis`|`-1.4908`|`0.202`|`-7.394`|`0.000`|
|`rad`|`0.2894`|`0.067`|`4.325`|`0.000`|
|`tax`|`-0.0127`|`0.004`|`-3.337`|`0.001`|
|`ptratio`|`-0.9375`|`0.132`|`-7.091`|`0.000`|
|`lstat`|`-0.5520`|`0.051`|`-10.897 `|`0.000`|

What if we would like to perform a regression using all of the variables but one?
자, 이 장대한 종합 성적표를 쓱 보고 나니 갑자기 변덕이 생깁니다! 만일 전 제반 속성 떼거지 변수 항목을 한가득 다 쓰긴 쓰되!! 꼴 보기 싫은 딱 한 가지 쓰레기 국면 변수 조각 놈만 고의로 배제 추려내 과감히 쳐 생략(but one)해 버리고, 남은 알짜배기 나머지 잔여 에이스 예측 변수 무리만을 오롯이 다 활용해 다시 한번 회귀 기조 연산을 조달 구동 깔끔히 단행해 보고자 한다면? 그땐 과연 코딩을 어떻게 귀찮게 조치해야 할까요?

For example, in the above regression output, `age` has a high $p$-value.
극단적 거시적 단편 예로, 여태 바로 위에서 엔진 풀가동 갓 뽑아 산출한 방금 전 통판 회귀 도출 출력물 결과치 요약표를 쓱 면밀히 살펴보면, 당장 **`age` (오래된 똥차 수명 연령)** 변수 칸에서 연루 파생 억지 도출된 고유 산출 **$p$-값(p-value) 지표 수위가 0.787로 몹시 유달리 확연히 막대하게 무지막지 쓸데없이 높다는(high) 점**을 충격 포착할 수 있습니다. (즉, 이놈은 집값 예측에 아무 짝에도 쓸모없는 확률적 뻘짓 변수란 뜻이죠!) 

So we may wish to run a regression excluding this predictor.
때문에 그 까닭 팩폭 사유로 우린 아예 이 무능력한 특정 예측 변수 잉여(`age`)만큼은 눈엣가시 단연코 통째로 콕 집어 외면 제외 쓰레기통 발췌 배제(excluding)해 가차 없이 버려버린 채로! 한결 깨끗 가벼워진 몸으로 한 차례 더 신규 파생 회귀 연산 구동 엔진을 재차 깔끔하게 단행해 다시 돌려보고픈 욕구(wish)가 강렬히 일 수도 있습니다.

The following syntax results in a regression using all predictors except `age` (output not shown).
너무나 다행히도! 하단에 제시된 별첨 후속 짧은 구문 조달 수식이 바로 타깃 `age` (수명) 한 가지 불량 성분만을 기막히게 딱 빼고(except) 겉어내 버린 다음! 외면 생략해 남은 에이스 나머지 일개 변조 예측 변수 파편들을 모조리 깡그리 일괄 투입 접목 활용하여 회귀 연산을 산출 결론 짓게 이끄는 본보기 파이썬 코드 응용 치트키 단락입니다. (이에 따른 실체 도출 산입 출력 결과물은 지면 낭비 제약상 생략).

```python
In [28]: minus_age = Boston.columns.drop(['medv', 'age'])
Xma = MS(minus_age).fit_transform(Boston)
model1 = sm.OLS(y, Xma)
summarize(model1.fit())
```

---

## Sub-Chapters (하위 목차)


[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/trans2.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/trans2.html)

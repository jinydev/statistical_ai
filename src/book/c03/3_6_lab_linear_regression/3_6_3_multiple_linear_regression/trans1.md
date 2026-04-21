---
layout: default
title: "trans1"
---

[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/trans1.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.6.3 Multiple Linear Regression_

# 3.6.3 다중 선형 회귀 실습

In order to fit a multiple linear regression model using least squares, we again use the `ModelSpec()` transform to construct the required model matrix and response.

다중 선형 회귀(multiple linear regression) 모델 기조를 최소 제곱(least squares) 잣대에 맞춰 조립 적합시켜 보고자, 우리는 재차 또 한 번 `ModelSpec()` 파생 변환 도구를 차용 발탁해 기용함으로써 모델 연산에 필수 제반 요구되는 모델 행렬 단면과 타깃 응답(response) 변수판을 온전히 구축 축조해 올립니다. The arguments to `ModelSpec()` can be quite general, but in this case a list of column names suffice.

이 `ModelSpec()` 함수 지령에 덧붙여 투입될 제반 인자(arguments) 속성들은 사실 조달 융통성이 무척 광범위 범용적(general)일 수 있지만, 당면한 이 특수 상황 사례에서만큼은 단지 그저 조달될 지정 열 이름(column names) 조각들의 단순 나열 리스트 표기만으로도 충분히 목적 달성 가동에 족합니다(suffice). We consider a fit here with the two variables `lstat` and `age`.

이번 분과 대목에서 우린 `lstat` 변수 그리고 `age` 변수 딱 이 두 가지 단면 조작만을 거느 동반 취합해 일련의 결합 적합 연산 과정을 도모 고려해 보겠습니다.

```
In [25]: X = MS(['lstat', 'age']).fit_transform(Boston)
model1 = sm.OLS(y, X)
results1 = model1.fit()
summarize(results1)
```

```
Out[25]:
```

```
           coef  std err       t  P>|t|
intercept 33.2228   0.731 45.458  0.000
lstat     -1.0321   0.048 -21.416 0.000
age        0.0345   0.012  2.826  0.005
```

Notice how we have compacted the first line into a succinct expression describing the construction of `X`.

여기서 눈여겨볼 대목은, 행렬 `X` 단위 판 조립 구축 과정을 서술 지시하는 맨 파생 선두 첫째 줄의 파이썬 코드 단락을 우리가 얼마나 무척이나 쉽고 축약 명료 간결한 형태 구분 표현식으로 꽉꽉 압축 다져 밀어(compacted) 놓았는가 하는 쏠쏠한 점입니다.

The `Boston` data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors.

현재 차용 중인 기저 `Boston` 데이터 세트 덩어리 판 자체에는 무려 총 12가지 수량의 다양한 속성 변수들이 대거 포진 포함(contains) 탑재되어 있는 터라, 혹여라도 이들 모든 파편 예측 변수를 남김없이 깡그리 다 일괄 동원 사용해 회귀 도출을 단행 수행하고자 변수명 일체를 한 자 한 자 남김없이 죄다 키보드로 쳐 입력 명기해야(type all of these)만 한다면 그건 무척이나 거추장스럽고 성가신(cumbersome) 번거로운 중노동이 될 것입니다. Instead, we can use the following short-hand:

이를 대신할 타개책으로, 우린 아래처럼 재치 있게 무척 짧게 생략 축약된(short-hand) 속기 방식 약식 표현 도구를 유용히 기용할 수 있습니다:

```
In [26]: terms = Boston.columns.drop('medv')
terms
```

```
.columns.
drop()
```

```
Out[26]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
       'rad', 'tax', 'ptratio', 'lstat'],
      dtype='object')
```

We can now fit the model with all the variables in `terms` using the same model matrix builder.

이제 우린 방금 전 수단과 완벽히 매한가지 똑같은 방식의 모델 행렬 조합기(builder) 생성 도구를 그대로 적용 차용하면서도, `terms` 부문 내에 묶여 편입된 이 모든 남은 변수 항목들을 일괄 모델에 일제히 욱여넣고 결집 적합시켜 볼 수 있습니다.

```
In [27]: X = MS(terms).fit_transform(Boston)
model = sm.OLS(y, X)
results = model.fit()
summarize(results)
```

|**`Out[27]:`**|`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|
|`intercept`|`41.6173`|`4.936`|`8.431`|`0.000`|
|`crim`|`-0.1214`|`0.033`|`-3.678`|`0.000`|
|`zn`|`0.0470`|`0.014`|`3.384`|`0.001`|
|`indus`|`0.0135`|`0.062`|`0.217`|`0.829`|
|`chas`|`2.8400`|`0.870`|`3.264`|`0.001`|
|`nox`|`-18.7580`|`3.851`|`-4.870`|`0.000`|
|`rm`|`3.6581`|`0.420`|`8.705`|`0.000`|
|`age`|`0.0036`|`0.013`|`0.271`|`0.787`|
|`dis`|`-1.4908`|`0.202`|`-7.394`|`0.000`|
|`rad`|`0.2894`|`0.067`|`4.325`|`0.000`|
|`tax`|`-0.0127`|`0.004`|`-3.337`|`0.001`|
|`ptratio`|`-0.9375`|`0.132`|`-7.091`|`0.000`|
|`lstat`|`-0.5520`|`0.051`|`-10.897 `|`0.000`|

What if we would like to perform a regression using all of the variables but one?

만일 전 제반 속성 변수 항목을 한가득 다 쓰긴 쓰되 딱 한 가지 국면 변수 조각만 고의로 배제 추려내 생략하고 나머지 잔여 예측 변수만을 오롯이 다 활용해 회귀 기조 연산을 조달 구동 단행해 보고자 한다면 그땐 과연 어떻게 조치해야 할까요? For example, in the above regression output, `age` has a high $p$-value.

거시적 단편 예로, 여태 바로 위에서 갓 뽑아 산출한 방금 전 회귀 도출 출력물 결과치를 살펴보면, 당장 `age` (수명 연령) 변수에서 연루 파생 도출된 고유 산출 $p$-값(p-value) 지수 수위가 몹시 유달리 확연히 막대하게 높다는 점을 포착할 수 있습니다. So we may wish to run a regression excluding this predictor.

때문에 그 까닭 사유로 우린 아예 이 특정 예측 변수(age)만큼은 단연코 통째로 콕 집어 외면 제외 발췌 배제(excluding)해 버린 채로 한 차례 더 신규 파생 회귀 연산 구동을 재차 단행해 돌려보고픈 욕구(wish)가 일 수도 있습니다. The following syntax results in a regression using all predictors except `age` (output not shown).

하단에 제시된 별첨 후속 구문 조달 수식이 바로 타깃 `age` (수명) 한 가지 성분만을 딱 빼고(except) 외면 생략해 남은 나머지 일개 변조 예측 변수 파편들을 모조리 깡그리 일괄 투입 접목 활용하여 회귀 연산을 산출 결론 짓게 이끄는 본보기 파이썬 코드 단락입니다 (이에 따른 실체 도출 산입 출력 결과물은 지면 제약상 생략).

```
In [28]: minus_age = Boston.columns.drop(['medv', 'age'])
Xma = MS(minus_age).fit_transform(Boston)
model1 = sm.OLS(y, Xma)
summarize(model1.fit())
```

---

## Sub-Chapters (하위 목차)


[< 3.6.2.1 Out24 374](../3_6_2_simple_linear_regression/3_6_2_1_out24_374/trans1.html) | [3.6.4 Multivariate Goodness Of Fit >](../3_6_4_multivariate_goodness_of_fit/trans1.html)

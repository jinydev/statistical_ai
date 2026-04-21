---
layout: default
title: "trans1"
---

[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/trans1.html) | [3.7 Exercises >](../../3_7_exercises/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.6.7 Qualitative Predictors_

# 3.6.7 정성적 예측 변수 실습

Here we use the `Carseats` data, which is included in the `ISLP` package.

본 실습 국면에서 우린 `ISLP` 기본 제공 패키지망 안에 아예 터를 잡고 묶여 포함 내장(included)되어 있는 카시트(`Carseats`) 데이터 표본 세트를 집중 활용 차출(use)해 볼 요량입니다. We will attempt to predict `Sales` (child car seat sales) in 400 locations based on a number of predictors.

우리의 당면 도전 목표는, 무수히 여러 가지 잡다한 각종 여건 예측 변수(predictors) 지표들을 두루 차용해 바탕 삼음(based on)으로써 궁극적으로 미 전역 400여 곳의 지점별 아동용 조수석 카시트(child car seat) 판매 성과, 즉 `Sales` (판매량) 성취를 정조준해 산출 근접 예측해 보는(attempt to predict) 것입니다.

```
In [35]: Carseats = load_data('Carseats')
Carseats.columns
```

```
Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising',
       'Population', 'Price', 'ShelveLoc', 'Age', 'Education',
       'Urban', 'US'],
      dtype='object')
```

The `Carseats` data includes qualitative predictors such as `ShelveLoc` , an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed.

이 `Carseats` 데이터 내역 덩어리 자체에는 `ShelveLoc`(진열대 위치)과 똑같은 여타 범주별 정성적(qualitative) 성질의 예측 변수군도 숱하게 섞여 기용 포함(includes)되어 있는데, 이 `ShelveLoc` 진열대 지표는 이를테면 매장 내부에서 해당 카시트 물품이 정확히 고객 앞 공간의 어느 한 위치 목에 진열 비치 거치(displayed)되었나 하는, 다시 말해 그 공간 입지 배치를 척도 측정한 질 평가 지표(indicator of the quality) 성분을 대변합니다. The predictor `ShelveLoc` takes on three possible values, `Bad`, `Medium`, and `Good`.

당장 이 예측 변수 `ShelveLoc` 조각은 속성 전개 상 크게 하급(`Bad`), 중급(`Medium`), 그리고 상급 최우수(`Good`) 이렇게 총 3가지 등위 갈래의 단편 판별 값 체제만으로 나눠 취합 결집해(takes on) 범주를 가집니다. Given a qualitative variable such as `ShelveLoc` , `ModelSpec()` generates dummy variables automatically.

이런 식으로 여느 무리의 정성적 변수(qualitative variable), 즉 카테고리형 범주별 지표 체제(이를테면 앞선 `ShelveLoc` 같은)가 주입 도달(Given)하기라도 하는 찰나면, 근저 설계된 `ModelSpec()` 함수 지표는 도출 내부에서 자기 스스로 기계적인 더미 변수(dummy variables) 성분들을 전격 파생 형성해 추가 자동(automatically) 조립 구축(generates)해 버립니다. These variables are often referred to as a _one-hot encoding_ of the categorical one-hot feature.

사실 이렇게 산출 도출된 파생 변조 변수 지표들은, 여느 통계 기계 학습 진영 내부 일각에서 통상 범주 속성(categorical feature) 지표 체재를 일렬로 탈바꿈 쪼갠 이른바 _원핫(one-hot) 인코딩_ 조작의 산물(referred to as)이라고들 널리 두루 일컬어 회자(often)되곤 합니다. Their columns sum to one, so to avoid collinearity with an interencoding cept, the first column is dropped.

다만 이런 인코딩 분류 치수 열들의 요소를 다 합산 통계한 합계(sum to one)치가 산술적으로 늘 1이라는 동일 상수 요격이 발생해 늘 고정되어 버리므로, 도출 차원에서 여느 절편(intercept) 상수 지표와의 다중 공선성(collinearity) 파생 충돌을 요리조리 탈피 미연 차단(avoid)할 목적으로 으레 이 무리 중 첫 번째(first column) 대표 격인 속성 배정 열만은 쏙 빼서 버려진 채 삭제 배제(dropped)되기 일쑤입니다. Below we see the column `ShelveLoc[Bad]` has been dropped, since `Bad` is the first level of `ShelveLoc` .

단적으로 아래 도출 제시된 판독 성분들을 유심히 살펴보면, 곧장 `ShelveLoc[Bad]` 몫의 수치 지정 열이 송두리째 쏙 빼내져 이탈 삭제 표적(dropped)이 된 걸 숱하게 식별 파악(see)할 수 있는데, 이는 다름 아니라 범주 `Bad`(불량) 위상이 `ShelveLoc` 파생 변수 군 내에서 그저 단순 알파벳 정렬 기준 맨 처음 첫 단상(first level) 위치를 차지해 앞섰던(since) 우연 기조 때문입니다. Below we fit a multiple regression model that includes some interaction terms.

자 이제 하단부 지면을 빌어, 여느 파생 무리 간의 다변 상호 작용 항(interaction terms) 성분 조각들을 몇몇 대거 차용 품어 포함(includes)시킨 채 직조 산출한 일개 다중 회귀 모델 지표를 본격 적합(fit) 연산해 보겠습니다.

encoding

```
In [36]: allvars = list(Carseats.columns.drop('Sales'))
y = Carseats['Sales']
final = allvars + [('Income', 'Advertising'),
                   ('Price', 'Age')]
X = MS(final).fit_transform(Carseats)
model = sm.OLS(y, X)
summarize(model.fit())

Out[36]:             coef  std err       t  P>|t|
intercept       6.5756   1.009   6.519  0.000
```

|`CompPrice`|`0.0929`|`0.004`|`22.567`|`0.000`|

|`Income`|`0.0109`|`0.003`|`4.183`|`0.000`|
|`Advertising`|`0.0702`|`0.023`|`3.107`|`0.002`|
|`Population`|`0.0002`|`0.000`|`0.433`|`0.665`|
|`Price`|`-0.1008`|`0.007`|`-13.549`|`0.000`|
|`ShelveLoc[Good]`|`4.8487`|`0.153`|`31.724`|`0.000`|
|`ShelveLoc[Medium]`|`1.9533`|`0.126`|`15.531`|`0.000`|
|`Age`|`-0.0579`|`0.016`|`-3.633`|`0.000`|
|`Education`|`-0.0209`|`0.020`|`-1.063`|`0.288`|
|`Urban[Yes]`|`0.1402`|`0.112`|`1.247`|`0.213`|
|`US[Yes]`|`-0.1576`|`0.149`|`-1.058`|`0.291`|
|`Income:Advertising`|`0.0008`|`0.000`|`2.698`|`0.007`|
|`Price:Age`|`0.0001`|`0.000`|`0.801`|`0.424`|

In the first line above, we made `allvars` a list, so that we could add the interaction terms two lines down.

직전 윗 단락 첫 시발점인 초입 파생 행 연산 선상에서 우린 일부러 `allvars` 결괏값 변수를 독립된 개폐 단위의 '리스트(list)' 체제로 강제 포진 구축해 묶어 놓았(made)는데, 오직 그 목적 연유(so that)는 향후 이어지는 단지 불과 두 줄(two lines down) 아래 연산 후속 맥락 전개 차원에서 이 리스트 단위 끄트머리에다 추가 연산의 덧셈 합작분인 여러 상호 작용 항 무리들을 유연 순탄히 한가운데다 직조 덧대 결합 편입 추가(add)할 요량을 도모 목적에 빗대 두기 위함이었습니다. Our model-matrix builder has created a `ShelveLoc[Good]` dummy variable that takes on a value of 1 if the shelving location is good, and 0 otherwise.

우리가 방금 동원 기용한 이 자체 모델 행렬 구축 생성 조합기(model-matrix builder) 지표는 단박에 모델 도출 내에서 `ShelveLoc[Good]` 이란 특정 일개 파생 더미 변수(dummy variable)를 차출 고안 생성(created)해 냈는데, 지표 조건상 해당 점주의 도출 진열대 입지 위치 여건이 훌륭 극상품(good)이었다면 기조 산출값으론 1을 부여 배정 확정 결속(takes on a value of 1)해 주고, 그 외 남은 모든 조건 불량 시 여부 사안일 경우(otherwise)엔 오롯이 가차 없이 0만 일괄 배성 조달 배정하게끔 구동됩니다. It has also created a `ShelveLoc[Medium]` dummy variable that equals 1 if the shelving location is medium, and 0 otherwise.

같은 맥락에 빗대 또한, 진열 입지 환경이 평범하게 적당 수준의 고만고만한 중간(medium)이 단편 입증 성립될 시 조건에 따라 즉각 그 산출값 성분으로 1을 동일 조달 지시 분연 부여하고, 만약 그에 못 미치거나 다르면 지극히 하등 어김없이 무조건 0으로 결론 귀속 배정(0 otherwise)시키는 독립된 `ShelveLoc[Medium]` 지표 파생 더미 변수 조각마저도 함께 도출 구축 발췌 도달 생성해 냈(created)습니다. A bad shelving location corresponds to a zero for each of the two dummy variables.

반면 이와 대조적으로 불쑥 진열 입지 상태가 형편없고 나쁜 열악 등급 파악 배정(bad)일 요량 상황이라면, 그 경우는 방금 조립 파생 분할 거론됐던 저 두 가지 더미 변수 항목(Good/Medium)들 모두에 각각 무조건 공통적으로 0 값의 산입 척도 수치가 얄짤없이 곧장 부합 결부 연루 배정 조달 귀결(corresponds to a zero)됩니다. The fact that the coefficient for `ShelveLoc[Good]` in the regression output is positive indicates that a good shelving location is associated with high sales (relative to a bad location).

도출 산입된 저 회귀 분석 출력물(regression output) 결과 지수표에서 `ShelveLoc[Good]` 파생 항 성분에 달라붙은 파생 고유 회귀 계수(coefficient) 항목 지표가 양(+)의 수치 판독 점수(positive) 징후로 도출 배정되었다는 그 단편 사실 궤적(fact)만으로도, 이는 곧장 도달 좋은 입지 우위 진열대 위상이 유의미할 만치 상당히 월등히 높은 수위의 카시트 물품 판매 기류고공 행진 성과(high sales)로 결부 견결 순조 직결 연루 편입(associated with)됨을 곧바로 확연히 일깨워 직시 입증 암시(indicates)해 주고 있습니다 (단, 어디까지나 나쁜 진열 입지 환경을 저 한구석 비교 기준축으로 맞대어 삼았다는 기조하에서 말입니다). And `ShelveLoc[Medium]` has a smaller positive coefficient, indicating that a medium shelving location leads to higher sales than a bad shelving location, but lower sales than a good shelving location.

그리고 동반 산입된 이웃 속성 `ShelveLoc[Medium]` 요인은 그보다 훨씬 더 작고 협소 미약한(smaller) 수치의 양(+)의 계수(positive coefficient) 수반 징후를 조달 배정받아 지니고 섰(has)는데, 이는 결국 그저 평범 고만고만 중간급(medium)인 진열대 입지 자리 점거 현황만으로도 최소한 나쁘고 열악한 하급 위치를 점한 때보단 분명 조금은 더 나은 성과의 상위 카시트 판매량 부양책 파생 쇄신 실적(higher sales) 결과분으로 도출 이끌(leads to) 수 있긴 하나 여럿, 단연 월등 우월 최고 등급 품질 위치 위상 궤적 파악 조건 달성 쾌거 때(good)와 비교하면 당장 어쩔 도리 없이 하등 상대적으로 못나고 다소 부진 떨어지는 판매 저조 부진 수위 실적 편차(lower sales)로 마감될 수밖에 없음을 고스란히 거시적 확연 방증 시사 암시(indicating) 도출해 냅니다.

---

## Sub-Chapters (하위 목차)


[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/trans1.html) | [3.7 Exercises >](../../3_7_exercises/trans1.html)

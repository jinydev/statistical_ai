---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/trans2.html) | [3.7 Exercises >](../../3_7_exercises/trans2.html)

# _3.6.7 Qualitative Predictors_

# 3.6.7 정성적 예측 변수 실습: 글자로 된 변수를 숫자로 바꾸는 꼼수 (더미 변수)

Here we use the `Carseats` data, which is included in the `ISLP` package.
자, 이번 실습 국면에선 구질구질한 보스턴 집값 데이터는 잠시 치워두고, `ISLP` 기본 제공 패키지망 안에 아예 터를 잡고 묶여 포함 내장되어(included) 있는 꿀잼 카시트(`Carseats`) 판매 데이터 표본을 팍팍 활용 차출해 봅시다! 

We will attempt to predict `Sales` (child car seat sales) in 400 locations based on a number of predictors.
우리의 새로운 목표는 명확합니다. 미 전역에 깔린 400여 곳 매장을 탈탈 털어, 온갖 잡다한 여건 지표(수입, 광고, 컴피티터 가격 등)들을 버무려서 궁극적으로 각 지점별 아동용 조수석 카시트(child car seat) 대박 **판매량 성과(`Sales`)를 족집게처럼 예측(attempt to predict)**해 보는 것입니다.

```python
In [35]: Carseats = load_data('Carseats')
Carseats.columns
```

```python
Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising',
       'Population', 'Price', 'ShelveLoc', 'Age', 'Education',
       'Urban', 'US'],
      dtype='object')
```

The `Carseats` data includes qualitative predictors such as `ShelveLoc` , an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed.
그런데 말입니다, 이 `Carseats` 데이터 내역 덩어리를 까보면 참치캔에 돌 들어있는 것 마냥 아주 골치 아픈 놈이 하나 섞여 있습니다! 바로 `ShelveLoc`(진열대 위치) 같은 이른바 **글자로 된 텍스트 정성적(qualitative) 예측 변수군**입니다. 이 `ShelveLoc` 진열대 지표는 이를테면 고객님이 마트에 딱 들어갔을 때, "카시트가 구석탱이에 찌그러져 있나(Bad), 계산대 앞 골든존 명당에 떡하니 버티고(Good) 있나"를 질적으로 평가한 글자 알뜰 척도 지표(indicator)입니다. 

The predictor `ShelveLoc` takes on three possible values, `Bad`, `Medium`, and `Good`.
문제는 통계 모델 회귀 수식에는 오직 '숫자'만 곱하고 더할 수 있다는 점이에요! 하지만 저 예측 변수 `ShelveLoc` 조각 안에는 숫자는 커녕 하급(`Bad`), 중급(`Medium`), 그리고 상급 최우수(`Good`) 이렇게 3가지 알파벳 텍스트 범주 쪼가리 갈래만 달랑 들어가 있습니다. 이걸 어떻게 수식에 넣죠?

Given a qualitative variable such as `ShelveLoc` , `ModelSpec()` generates dummy variables automatically.
걱정 마세요! 우리는 이미 파이썬 파워 만능 요리사 **`ModelSpec()`**을 고용했잖아요! 이런 글자 나부랭이로 된 정성적 변수 범주가 입력으로 휙 던져(Given)지면, 이 똑똑한 녀석은 속으로 코웃음을 치며 내부적으로 알아서 기계적인 투명인간 대리 체제인 **'더미 변수(dummy variables)' 파생 0과 1 숫자 성분들**을 전격적으로 뚝딱 생성해 추가 자동(automatically) 조립 구축해 바칩니다! 

These variables are often referred to as a _one-hot encoding_ of the categorical one-hot feature.
사실 이렇게 컴퓨터가 알아먹을 숫자 0과 1로 쏙 탈바꿈한 이 마법 같은 파생 변수들을 툭 까놓고, 요즘 잘나가는 인공지능 기계 학습 딥러닝 판에서는 되게 있어 보이게 **_"원핫(one-hot) 인코딩"_** 수단이라고 즐겨 부르며 거들먹거리고(often referred to as) 다니곤 합니다. (원핫: "해당하는 한 곳(one)에만 불(hot)을 켜고(1) 나머진 불 끄기(0)!" 라는 아주 찰진 뜻이죠.)

Their columns sum to one, so to avoid collinearity with an intercept, the first column is dropped.
다만 아주 주의할 꿀팁 하나! 이 인코딩 삼총사(Bad=1, Medium=1, Good=1)의 열을 다 더하면 무조건 1이라는 숫자 늪에 고립상수 요격이 생깁니다. 이러면 우리 아까 배운 쌍둥이 버그 오류인 '다중 공선성(collinearity, 겹치는 버그)' 충돌이 절편이랑 빵 터집니다! 
그래서 이 충돌을 미연에 요리조리 피하고자(avoid), 룰에 따라 **아주 불쌍하게도 이 무리 중 알파벳순 대표 첫 번째(first column)인 `Bad` 열은 쏙 빼서 억울하게 가차 없이 삭제 배제(dropped)되어 버립니다!** (기준점 역할을 하기 위해 희생양이 되는 거죠.)

Below we see the column `ShelveLoc[Bad]` has been dropped, since `Bad` is the first level of `ShelveLoc` .
단적으로 아래 출력 결과를 살짝 지켜보면, 당장 `ShelveLoc[Bad]` 몫의 수치 지정 열이 송두리째 쏙 빼내져 증발 감춰진 걸 파악할 수 있는데, 이는 'B'로 시작하는 `Bad`(불량 진열) 위상이 그냥 억울하게 알파벳순 1빠따 정렬 맨 처음 위치(first level)를 차지했기(since) 때문입니다. 

Below we fit a multiple regression model that includes some interaction terms.
자! 이론은 끝났으니 하단부 실습에서 곧장 방금 배운 시너지 효과(interaction terms) 성분 조각들 지표까지 대거 포함(includes)시킨 궁극의 최고봉 다중 회귀 전체 통합 모델 지표를 본격 무자비하게 돌려(fit) 적합 연산해 보겠습니다. 

```python
In [36]: allvars = list(Carseats.columns.drop('Sales'))
y = Carseats['Sales']
final = allvars + [('Income', 'Advertising'),  # 소득과 광고의 시너지!
                   ('Price', 'Age')]           # 가격과 지역연령의 변태 조합!
X = MS(final).fit_transform(Carseats)
model = sm.OLS(y, X)
summarize(model.fit())
```

```python
Out[36]:             coef  std err       t  P>|t|
intercept       6.5756   1.009   6.519  0.000
```
| 예측 변수 | `coef (계수)` | `std err` | `t (티-값)` | `P>\|t\| (피-값)` |
|---|---|---|---|---|
|`CompPrice`|`0.0929`|`0.004`|`22.567`|`0.000`|
|`Income`|`0.0109`|`0.003`|`4.183`|`0.000`|
|`Advertising`|`0.0702`|`0.023`|`3.107`|`0.002`|
|`Population`|`0.0002`|`0.000`|`0.433`|`0.665` (인구수는 쓸모엄씀!)|
|`Price`|`-0.1008`|`0.007`|`-13.549`|`0.000` (비싸면 안 팔림!)|
|`ShelveLoc[Good]`|`4.8487`|`0.153`|`31.724`|`0.000` (명당 진열대 대박!)|
|`ShelveLoc[Medium]`|`1.9533`|`0.126`|`15.531`|`0.000` (중간 진열대 중박!)|
|`Age`|`-0.0579`|`0.016`|`-3.633`|`0.000`|
|`Education`|`-0.0209`|`0.020`|`-1.063`|`0.288` (학력 무관!)|
|`Urban[Yes]`|`0.1402`|`0.112`|`1.247`|`0.213` (도시/시골 무관!)|
|`US[Yes]`|`-0.1576`|`0.149`|`-1.058`|`0.291` (국내외도 무관!)|
|`Income:Advertising`|`0.0008`|`0.000`|`2.698`|`0.007` (시너지 터짐!)|
|`Price:Age`|`0.0001`|`0.000`|`0.801`|`0.424` (시너지 폭망!)|

In the first line above, we made `allvars` a list, so that we could add the interaction terms two lines down.
직전 윗 단락에서 우린 일부러 `allvars` 결괏값 변수를 대괄호로 뒤집어씌운 파이썬 '리스트(list)' 짐 꾸러미 단위로 강제 변신 통일시켜 묶어 놓았(made)는데요, 그 이유는 딱 하나(so that)! 단지 불과 두 줄(two lines down) 아래에 이어지는 연산에서 이 리스트 자루 끄트머리에다 추가 연산의 덧셈 합작분인 `+ [('Income', 'Advertising'), ...]` 처럼 엄청난 상호 작용 항 무리 치트키들을 에러 없이 쓱 아주 유연하게 덧대 결합 편입 더하기(add)할 요량을 써먹기 위함이었습니다. 

Our model-matrix builder has created a `ShelveLoc[Good]` dummy variable that takes on a value of 1 if the shelving location is good, and 0 otherwise.
결과표를 볼까요? 우리가 방금 동원 기용한 이 자체 모델 행렬 구축기 파파스머프는 단박에 모델 안에서 **`ShelveLoc[Good]`** 이란 신기한 투명 더미 변수(dummy variable)를 찍어냈는데요(created)! 
이놈 로직은 참 단순무식합니다. 해당 점주의 진열대 입지 위치 여건 텍스트가 극상품 `Good` 글씨였다면 무조건 묻지도 따지지도 않고 기조 **산출값 1번 숫자 배지로 교체(takes on a value of 1)해 부여하고, 혹여 그게 아니면(otherwise) 가차 없이 0만 일괄 배급해 구동**되는 원리입니다! 

It has also created a `ShelveLoc[Medium]` dummy variable that equals 1 if the shelving location is medium, and 0 otherwise.
마찬가지 쌍둥이 원리로! 고만고만한 중간(`Mediaum`) 위치를 뜻하는 **`ShelveLoc[Medium]`** 파생 더미 변수도 같이 쌍으로 생성(created)했는데요. 요 녀석도 진열대 글자값이 `Medium` 이면 무조건 1 도장 쾅쾅! 찍고, 아니면 무조건 0으로 결론 귀속 배정(0 otherwise)시키는 도어맨과 다름없습니다. 

A bad shelving location corresponds to a zero for each of the two dummy variables.
아하! 그럼 눈치채셨나요? 아까 억울하게 배제되고 소멸 삭제되었던 불량 진열대 등급 **`Bad`** 녀석은 어떻게 취급받을까요? 빙고! 진열 상태가 열악하다면 방금 조립 파생 거론됐던 저 두 명의 도어맨 **`Good` 놈도 0 통과 안 됨, `Medium` 놈도 0 통과 안 됨!** 즉, 0번 배지를 두 개다 차게 된 상태가 바로 얄짤없이 불량 상태를 의미(corresponds to a zero)하는 절묘한 파이썬의 기막힌 숫자의 마술 통계 암호 치환 로직인 것입니다! 

The fact that the coefficient for `ShelveLoc[Good]` in the regression output is positive indicates that a good shelving location is associated with high sales (relative to a bad location).
자, 저 표를 한 번 보십시오! `ShelveLoc[Good]` 파생 항 성분에 달라붙은 파생 고유 회귀 계수(coefficient) 항목 지표가 시뻘건 **양(+)의 4.8487이라는 엄청난 수치 점수(positive)** 징후로 도출 배정받았군요. 이 단편적인 통계 성적만으로도 우리는 무슨 결론을 내릴 수 있을까요? 
바로 **"카시트 상품을 명당 골든존(Good)에 진열만 잘 비치해둬도, 구석탱이(Bad)에 처박아둔 대비 무려 484개(단위)나 압도적으로 더 팔아치우고 기류 고공 행진 성과(high sales)로 직결 연루 편입(associated with)"**된다고 확실히 방증 시사 암시(indicates)할 수 있는 엄청난 통계 분석 입증 증거인 것입니다!

And `ShelveLoc[Medium]` has a smaller positive coefficient, indicating that a medium shelving location leads to higher sales than a bad shelving location, but lower sales than a good shelving location.
그리고 동반 산입된 이웃 속성인 중간 명당 `ShelveLoc[Medium]` 요인은 어때요? 얘도 양수긴 한데 그보다는 훨씬 더 쪼마낳고 협소 미약한(smaller) 계수(1.9533) 수반 징후를 지니고 섰(has)는데요. 
이는 아주 상식적입니다! 중간 자리 눈높이급(medium)에 카시트를 깔아두는 진열 노력만으로도 안습 구석탱이(bad)에 처박아 둔 때보단 분명 한결 195개 더 나은 파생 쇄신 실적(higher sales) 결과분으로 도출 이끌(leads to) 수 있긴 하나...! 역시 단연 우월 최고 명당(Good) 위상 궤적 쾌거치 때보단 어쩔 도리 없이 하등 못 미치고 다소 떨어지는 부진 수위 실적 편차(lower sales)로 마감될 수밖에 없음을 고스란히 정석대로 증명(indicating)해 주고 있습니다! 결국 자리싸움의 승리도 통계가 증명해 주네요!

---

## Sub-Chapters (하위 목차)


[< 3.6.6.1 In 33 Anovalmresults1 Results3](../3_6_6_non-linear_transformations_of_the_predictors/3_6_6_1_in_33_anovalmresults1_results3/trans2.html) | [3.7 Exercises >](../../3_7_exercises/trans2.html)

---
layout: default
title: "trans1"
---

[< 3.3.2 Extensions Of The Linear Model](../trans1.html) | [3.3.3 Potential Problems >](../../3_3_3_potential_problems/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Non-linear Relationships

# 비선형적 관계(Non-linear Relationships)

As discussed previously, the linear regression model (3.19) assumes a linear relationship between the response and predictors.

앞서 논의한 바와 같이, 선형 회귀 모델 (3.19) 는 응답 변수와 예측 변수 사이에 온전한 선형적 관계가 성립한다고 가정합니다.

But in some cases, the true relationship between the response and the predictors may be nonlinear.

하지만 실상 어떤 특수한 경우엔 예측 변수 및 대상 응답 변수 양자 간에 위치한 진정한 무형의 구조적 관계가 분명 비선형적일 수도 있습니다.

Here we present a very simple way to directly extend the linear model to accommodate non-linear relationships, using _polynomial regression_.

여기서 우리는 소위 _다항 회귀(polynomial regression)_ 수법을 적극적으로 구사함으로써 이토록 비선형적인 파생 관계를 원만히 잘 수용토록 기성 선형 모델 틀 자체를 직접적이고도 아주 간단 명료하게 외연 확장해내는 흥미로운 기법 하나를 새로 제시하고자 합니다.

In later chapters, we will present more complex approaches for performing non-linear fits in more general settings.

차후 맞이할 이어지는 챕터 후반부 내용에서는 좀 더 포괄적인 일반 설정 환경에서 본격적으로 비선형 파생 적합을 너끈히 수행해 내는 수위 높은 이색적이고 복잡다단한 몇몇 접근 방식을 두루 심층 제시할 계획입니다.

Consider Figure 3.8, in which the `mpg` (gas mileage in miles per gallon) versus `horsepower` is shown for a number of cars in the `Auto` data set.

주어지는 `Auto` 데이터 세트 내에 기입된 다수의 차종별로 `horsepower(마력)` 대비 `mpg(갤런당 주행 마일 수, 즉 연비)` 수치의 판세를 나란히 보여주는 그림 3.8 표면을 한 번 면밀히 고찰해 보시기 바랍니다.

The orange line represents the linear regression fit.

여기 덧칠된 주황색 선은 일반적 선형 회귀 모의 적합 궤적을 묘사합니다.

There is a pronounced relationship between `mpg` and `horsepower`, but it seems clear that this relationship is in fact non-linear: the data suggest a curved relationship.

보통 `mpg` 요인과 해당 차량 `horsepower` 능력치 간에는 극히 눈에 띄게 두드러진 관련성이 산출 상존하긴 하나, 사실상 이들 관계는 명백히 비선형적 궤도로 곡선을 그리고 있음이 분명히 시사됩니다: 해당 데이터가 아예 곡면 곡선 형태의 상호 관계망을 직접 암시 지시하고 있기 때문입니다.

A simple approach for incorporating non-linear associations in a linear model is to include transformed versions of the predictors.

본디 어떤 선형 모델 형식의 체제 내부에 비선형적 성질의 제반 관련성을 교묘히 녹여내 포함시키는 가장 고전적이고 단순명료한 접근법 요령이란, 각 예측 변수의 구조적 형태를 다형체로 자체 변환 가공해 투입 포함하는 것입니다.

For example, the points in Figure 3.8 seem to have a _quadratic_ shape, suggesting that a model of the quadratic form

예를 들자면, 저 위 그림 3.8 투시도 상에 점철된 데이터 파편 타점 무리는 꽤 기형적인 _2차 곡선형(quadratic)_ 형상을 얼추 나타내는 듯 부각 보이며, 이와 더불어 차라리 다음과 같은 수식 기저 구도 포맷을 띠는 형태의 모델이

**==> picture [285 x 11] intentionally omitted <==**

may provide a better fit.
어쩌면 수월히 훨씬 더 부합하는 합당 나은 적합성을 은연중 제시해 줄지 모를 일임을 시사합니다.

Equation 3.36 involves predicting `mpg` using a non-linear function of `horsepower`.
방정식 3.36 식 체계는 일종의 마력분 `horsepower` 비선형 함수 꼴을 빌미 삼아 가상 연비 `mpg` 항목을 유추 예측하는 행위 절차를 수반 포함합니다.

_But it is still a linear model!_ That is, (3.36) is simply a multiple linear regression model with $X_1 = \text{horsepower}$ and $X_2 = \text{horsepower}^2$.
_허나 설령 이렇다 한들 이것은 본질적으로 엄밀히 여전히 선형 모델의 일부일 뿐입니다!_ 이는 다시 말해, (3.36) 수식 모델 자체는 기껏해야 단지 $X_1 = \text{horsepower}$ 이고 변형 $X_2 = \text{horsepower}^2$ 인 다분히 단순무식한 다중 선형 회귀 모의 수식 모형에 지나지 않는단 설명입니다.

So we can use standard linear regression software to estimate $\beta_0, \beta_1$, and $\beta_2$ in order to produce a non-linear fit.
그러니 고로 우리는 그저 범용 표준 시판용 선형 회귀 구축 통계 소프트웨어 같은 평이한 수단을 적절히 가동 써먹음으로써 곧장 $\beta_0, \beta_1$, 그리고 잔여 항 $\beta_2$ 수치를 재빨리 가늠해 추산해 낼 수 있고 이를 밑거름 발판 삼아 특이 비선형적 굴곡 곡면 산출 적합선을 뽑아 도출할 수 있습니다.

The blue curve in Figure 3.8 shows the resulting quadratic fit to the data.
그림 3.8 속에 유려히 휘몰아치는 저 푸른색 전개 곡선은 바로 이렇게 해당 관측치 데이터 구간을 향해 우리가 새롭게 모의 산출 투사 적중해낸 2차 방정식 곡률 형태의 최종 산출 적합선 산물을 보여줍니다.

The quadratic



**==> picture [304 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
Linear<br>Degree 2<br>Degree 5<br>50 100 150 200<br>Horsepower<br>50<br>40<br>30<br>Miles per gallon<br>20<br>10<br>**----- End of picture text -----**<br>


**FIGURE 3.8.** _The_ `Auto` _data set. For a number of cars,_ `mpg` _and_ `horsepower` _are shown. The linear regression fit is shown in orange. The linear regression fit for a model that includes_ $\text{horsepower}^2$ _is shown as a blue curve. The linear regression fit for a model that includes all polynomials of_ `horsepower` _up to fifth-degree is shown in green._


|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`horsepower`<br>`horsepower`2|56.9001<br>1.8004<br>31.6<br>_<_0_._0001<br>_−_0.4662<br>0.0311<br>_−_15.0<br>_<_0_._0001<br>0.0012<br>0.0001<br>10.1<br>_<_0_._0001|



**TABLE 3.10.** _For the_ `Auto` _data set, least squares coefficient estimates associated with the regression of_ `mpg` _onto_ `horsepower` _and_ $\text{horsepower}^2$ _._

fit appears to be substantially better than the fit obtained when just the linear term is included.
이렇듯 곡선형 포물선을 그리는 2차 적합 모의 곡선 자체는 막상 이전에 우리가 선형 직선 항 단일 요건 체계만을 무미건조하게 고집 삽입 적용했을 당시 취득 체감했던 적합 궤도에 비해 훨씬 전체적으로 보다 눈에 띄게 더 상당 부분 나은 산출 타점 품질을 제공하는 듯 보입니다.

The $R^2$ of the quadratic fit is $0.688$, compared to $0.606$ for the linear fit, and the $p$-value in Table 3.10 for the quadratic term is highly significant.
단순 산술적 지표만 보더라도 이전 직선 형태 선형 적합 시 측정되었던 결정 계수 치수 $R^2$ 가 $0.606$ 수준에 머문 데 반해 지금의 새로운 곡면 2차 적합 $R^2$ 결괏값은 자그마치 $0.688$ 에 다다르며, 더불어 근방 표 3.10 내 기재된 2차 곡선 변환 항 부가 $p$-값 체계 수위 조치 또한 다분히 매우 높은 통계적 유의성 잣대를 척도로 확증해 시현해 주고 있습니다.

If including $\text{horsepower}^2$ led to such a big improvement in the model, why not include $\text{horsepower}^3$, $\text{horsepower}^4$, or even $\text{horsepower}^5$?
여기서 한 번 생각해 봅시다. 설령 가령 저렇게 변형 항 요건인 $\text{horsepower}^2$ 항목 조각을 덧입힌 추가 조치가 통계 모델 단면 상에 그토록 이점 높은 막대한 커다란 향상 여력 개선 성과를 곧장 이끌어 야기 조달했다면, 어째서 남은 여타 조각 $\text{horsepower}^3$, $\text{horsepower}^4$, 혹은 심지어 파생 형태 $\text{horsepower}^5$ 따위를 굳이 부득불 포함 반영 도입하지 않고 이대로 그냥 만용 배척해야 쓰겠습니까?

The green curve in Figure 3.8 displays the fit that results from including all polynomials up to fifth degree in the model (3.36).
그림 3.8 지면 한쪽에 길게 도사리며 내어진 초록빛 투사 도면 곡선 단면은 바로 이렇게 짐작 도출한, 즉 기존 바탕 모델 수식 틀 (3.36) 구조 내에 감히 한도 치수인 5차 계수 한계 등급까지 전부 남김없이 모조리 포스트 다항식 모의 곡선 항목 요소를 다변화 투사 합치 편제시켜 버린 시도 결과물로서 도출 전향된 광역 모의 적합선을 화면에 나타내 보여 줍니다.

The resulting fit seems unnecessarily wiggly — that is, it is unclear that including the additional terms really has led to a better fit to the data.
허나 막상 도출 형성된 이 초록 빛깔 모의 적합선 궤도는 시선을 한눈에 잡아끌 만치 이리저리 다소 쓸데없이 너무 과도하게 무질서하게 굽이치며 꼬물거리는 기괴한 듯한 자태(wiggly)를 여과 없이 뽐내는데 — 이는 재차 달리 시각 환원해 돌이켜 보자면, 앞서 투사 집어넣듯이 자행한 과파생 거듭 제곱 추가 항 부가 편입 부문 요소가 과연 진정 현존하는 관측 치 데이터 편제 집단 결 방향 양태 파악에 무어 더 나은 합목적적 성과 지표 적합선 산출 제공이란 긍정 조력에 진정 큰 보탬 일조를 가한 것인지, 그 효용성 및 타당 여부 판단이 심히 도저히 객관적으로 투명치 않고 몹시 불분명 모호하다는 단언입니다.

The approach that we have just described for extending the linear model to accommodate non-linear relationships is known as _polynomial regression_, since we have included polynomial functions of the predictors in the regression model.
이처럼 여타 발생 가능한 비선형 속성의 까다로운 불변 관계를 융통성 있게 충분히 수용 감당할 목적으로 지금 막 우리가 새로이 선형 체계 기본 모델 골조 확장 방불 묘사에 거론 채용한 전술 기법 수단을 일컬어 흔히 _다항 회귀(polynomial regression)_ 수법 조치라고도 별도 호칭하는데, 그도 그럴 연유가 필시 전개되는 회귀축 기본 수식 모델 틀 한구석에 예측 변수에 다항식 함수(polynomial functions) 특성 요소를 우리가 거듭 별도로 가미해 함께 내전 시켜 수용한 모의 흔적이 여실히 짙게 상존하기 까닭입니다.

We further explore this approach and other non-linear extensions of the linear model in Chapter 7.
이외 그 밖에도, 우리는 한참 뒤 저만치 후속 챕터 7장에 당도해 다다른 지대에서 비로소 이 부문 관련 특수 접근 방법 방식과 함께 그 밖에 기성 선형 모델을 기저 바탕 뼈대 삼아 여타 비선형 확장 구조로 탈바꿈 치환하는 다양한 번외적 외연 변형 기법 수단들도 더 광범하게 본격 부가 추가 탐구 논의할 계획입니다.

---

## Sub-Chapters (하위 목차)


[< 3.3.2 Extensions Of The Linear Model](../trans1.html) | [3.3.3 Potential Problems >](../../3_3_3_potential_problems/trans1.html)

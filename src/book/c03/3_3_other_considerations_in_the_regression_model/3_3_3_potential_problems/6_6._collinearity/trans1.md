---
layout: default
title: "trans1"
---

[< 4 4. Outliers](../4_4._outliers/trans1.html) | [3.4 The Marketing Plan >](../../../3_4_the_marketing_plan/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 6. Collinearity

# 여섯 번째 잠재적 문제점: 공선성(Collinearity)

_Collinearity_ refers to the situation in which two or more predictor variables are closely related to one another.

_공선성(collinearity)_ 이란 둘 혹은 그 이상의 여러 예측 변수 쌍이 서로 대단히 긴밀하게 연관되어 있는 상황을 의미합니다.

The concept of collinearity is illustrated in Figure 3.14 using the `Credit` data set.

공선성의 개념은 `Credit` 데이터 세트를 활용한 그림 3.14 에서 잘 나타납니다.

In the left-hand panel of Figure 3.14, the two predictors `limit` and `age` appear to have no obvious relationship.

그림 3.14 왼쪽 측면 패널에서, 두 예측 변수 `limit` 와 `age` 사이에는 아무런 뚜렷한 관계가 없는 것처럼 보입니다.

In contrast, in the right-hand panel of Figure 3.14, the predictors `limit` and `rating` are very highly correlated with each other, and we say that they are _collinear_.

이와 대조적으로 오른쪽 패널을 보면, 예측 변수 `limit` 와 `rating` 은 서로 무척 높은 수준으로 상관되어 있으며, 우리는 이 둘을 _공선적(collinear)_ 이라고 부릅니다.

The presence of collinearity can pose problems in the regression context, since it can be difficult to separate out the individual effects of collinear variables on the response.

공선성의 존재는 선형 회귀 측면에서 문제를 일으킬 수 있는데, 왜냐하면 공선적 관계로 얽힌 변수들이 대상 응답에 각기 미치는 개별 영향을 따로 구분해 내기 어렵기 때문입니다.

In other words, since `limit` and `rating` tend to increase or decrease together, it can be difficult to determine how each one separately is associated with the response, `balance`.

달리 말해 `limit` 나 `rating` 은 동반하여 같이 증가하거나 감소하는 성향을 띠다 보니, 이들 각각이 응답 변수인 `balance` 에 낱낱이 어떻게 개별적으로 연관되어 있는지 명확히 결정하기 어렵습니다.

Figure 3.15 illustrates some of the difficulties that can result from collinearity.

그림 3.15 는 공선성으로 인해 발생할 수 있는 여러 난관과 애로사항을 예시로 보여줍니다.

The left-hand panel of Figure 3.15 is a contour plot of the RSS (3.22) associated with different possible coefficient estimates for the regression of `balance` on `limit` and `age`.

그림 3.15 의 좌측 패널은 응답 `balance` 를 `limit` 및 `age` 에 도출한 회귀식에서 갖가지 상이한 계수 추정치들에 기인하는 RSS (3.22) 의 등고선 플롯 도면입니다.

Each ellipse represents a set of coefficients

**==> picture [319 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.16 0.17 0.18 0.19 −0.1 0.0 0.1 0.2<br>βLimit βLimit<br> 21.8<br> 21.5<br> 21.25<br> 21.8<br> 21.5<br>5<br>0<br>4<br>−1<br>3<br>Age −2<br>β Rating 2<br>β<br>−3<br>1<br>−4<br>0<br>−5<br>**----- End of picture text -----**<br>


**FIGURE 3.15.** _Contour plots for the RSS values as a function of the parameters β for various regressions involving the_ `Credit` _data set. In each plot, the black dots represent the coefficient values corresponding to the minimum RSS._ Left: _A contour plot of RSS for the regression of_ `balance` _onto_ `age` _and_ `limit` _. The minimum value is well defined._ Right: _A contour plot of RSS for the regression of_ `balance` _onto_ `rating` _and_ `limit` _. Because of the collinearity, there are many pairs_ ( _β_ Limit _, β_ Rating) _with a similar value for RSS._

that correspond to the same RSS, with ellipses nearest to the center taking on the lowest values of RSS.
여기서 각 타원(ellipse) 구조는 모두 같은 RSS 값을 반환하는 계수들의 집합 띠를 대변하며, 궤도 중심점에 가장 가까이 밀집한 타원일수록 가장 낮은 최소의 RSS 곡선값을 나타냅니다.

The black dots and associated dashed lines represent the coefficient estimates that result in the smallest possible RSS — in other words, these are the least squares estimates.
검은색 점들과 이에 맞물린 이음 점선들은 이 중에서 가질 수 있는 가장 작은 크기의 RSS 결과를 배출하는 계수 추정치들을 가리키며 — 다시 말해 이들이 다름 아닌 최소 제곱 추정치들임을 의미합니다.

The axes for `limit` and `age` have been scaled so that the plot includes possible coefficient estimates that are up to four standard errors on either side of the least squares estimates.
플롯의 양축 `limit` 와 `age` 배열은 각 최소 제곱 추정치를 기점으로 양 편에 각각 최대 4배의 표준 오차 배수 범위까지 다다르는 가용한 계수 추정치 규모 전반을 다 아우르기 위해 스케일이 적절히 축척되었습니다.

Thus the plot includes all plausible values for the coefficients.
그렇기 때문에 도출된 이 플롯 위에는 계수로 쓸 법한 모든 그럴싸한(plausible) 허용 범위의 값들이 다 담겨 있습니다.

For example, we see that the true `limit` coefficient is almost certainly somewhere between $0.15$ and $0.20$.
일례로 우리는 저 궤도를 통해 `limit` 지표에 해당하는 실제 참 계숫값이 거의 기필코 $0.15$ 와 $0.20$ 사이 어딘가에 자리 잡고 있음을 미루어 볼 수 있습니다.

In contrast, the right-hand panel of Figure 3.15 displays contour plots of the RSS associated with possible coefficient estimates for the regression of `balance` onto `limit` and `rating`, which we know to be highly collinear.
이와 상반되게 우측의 그림 3.15 패널 국면은, 이미 우리가 높은 수준으로 공선적임을 잘 알고 있는 인자인 `limit` 와 `rating` 을 잣대 삼아 `balance` 를 예측한 회귀 모델에서 파생될 수 있는 계수 추정치들과 일련의 RSS 간의 관계를 그린 등고선 플롯을 보여줍니다.

Now the contours run along a narrow valley; there is a broad range of values for the coefficient estimates that result in equal values for RSS.
이제는 이 등고선 궤도가 유독 아주 좁고 깊은 골짜기를 따라 형성되며; 등등한 동일 RSS 결과값을 야기시킬 계수 추정치 대역 값이 너무나도 방달하게 퍼져 있음을 알 수 있습니다.

Hence a small change in the data could cause the pair of coefficient values that yield the smallest RSS — that is, the least squares estimates — to move anywhere along this valley.
이로 인해 본래의 데이터에 아주 사소한 변동 하나만 가해지더라도, 가장 작은 RSS 값을 반환하는 계수들의 짝 — 즉 최소 제곱 추정치 — 은 이 넓게 패인 깊은 골짜기 선상을 따라 어디로든 자유롭게 이리저리 이동해 버릴 소지가 다분합니다.

This results in a great deal of uncertainty in the coefficient estimates.
이는 덩달아 향후 도출할 계수 추정치 잣대 자체에 대단히 폭넓은 극심한 불확실성을 가증시키는 원인이 됩니다.

Notice that the scale for the `limit` coefficient now runs from roughly $-0.2$ to $0.2$; this is an eight-fold increase over the plausible range of the `limit` coefficient in the regression with `age`.
유의할 점은 지금 제시된 `limit` 계수의 대역폭 축척 자체가 대략 $-0.2$ 부터 $0.2$ 까지 이끌려 팽창되어 형성되었다는 사실인데; 이는 앞선 예시 속 `age` 와 동반된 회귀 모델에서의 `limit` 계수가 띠던 그럴싸한 변동 허용 궤도 대비 무려 8배나 훌쩍 늘어난 증가 수치입니다.

Interestingly, even though the `limit` and `rating` coefficients now have much more individual uncertainty, they will almost certainly lie somewhere in this contour valley.
흥미롭게도 현재 비록 `limit` 조각과 `rating` 부문 계수가 유독 개별적으로 훨씬 큰 극악의 개별 불확실성을 떠안게 되었음에도, 실질적인 해당 참값들은 여전히 거의 기필코 이 골짜기 등고선 궤적 어디 즈음에는 놓이게 될 것이라는 점입니다.

For example, we would not expect the true value of the `limit` and `rating` coefficients to be $-0.1$ and $1$ respectively, even though such a value is plausible for each coefficient individually.
예를 들어, 개별 계수 측면으로만 떼어놓고 본다면 $limit$ 와 $rating$ 의 실질적인 참 계수 잣대가 각기 $-0.1$ 과 $1$ 수위를 보일 거라 충분히 수긍할 수 있긴 하겠지만, 실제로 이 둘이 그처럼 조합된 쌍으로 동시에 나타날 거라 기대하진 않을 것입니다.

Since collinearity reduces the accuracy of the estimates of the regression coefficients, it causes the standard error for $\hat{\beta}_j$ to grow.
공선성은 이처럼 예측 회귀 계수들의 추정치에 대한 정확도를 상당히 저하시키므로, 필경 $\hat{\beta}_j$ 척도에 수반되는 표준 오차를 점증하여 커지게 만듭니다.

Recall that the $t$-statistic for each predictor is calculated by dividing $\hat{\beta}_j$ by its standard



|108<br>3. Linear Regression|108<br>3. Linear Regression|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>Model 1<br>`age`<br>`limit`|_−_173.411<br>43.828<br>_−_3.957<br>_<_0_._0001<br>_−_2.292<br>0.672<br>_−_3.407<br>0_._0007<br>0.173<br>0.005<br>34.496<br>_<_0_._0001|
|`Intercept`<br>Model 2<br>`rating`<br>`limit`|_−_377.537<br>45.254<br>_−_8.343<br>_<_0_._0001<br>2.202<br>0.952<br>2.312<br>0.0213<br>0.025<br>0.064<br>0.384<br>0.7012|



**TABLE 3.11.** _The results for two multiple regression models involving the_ `Credit` _data set are shown. Model 1 is a regression of_ `balance` _on_ `age` _and_ `limit` _, and Model 2 is a regression of_ `balance` _on_ `rating` _and_ `limit` _. The standard error of_ $\hat{\beta}_\text{limit}$ _increases 12-fold in the second regression, due to collinearity._

error.
표준 오차로 나눔으로써 도출 산출 연산된다는 사실 대목을 되짚어 상기해 보십시오.

Consequently, collinearity results in a decline in the $t$-statistic.
결과적으로, 문제의 공선성은 자연히 그에 수반된 $t$-통계량 수치 척도를 하락 및 감쇄시키는 결과를 직간접적으로 초래합니다.

As a result, in the presence of collinearity, we may fail to reject $H_0 : \beta_j = 0$.
그 파급 결과로 모델에 공선성이 잔존하여 기생할 때면, 우리는 자칫 귀무가설 $H_0 : \beta_j = 0$ 잣대를 기각하는 일에 그만 번번이 실패할 수 있습니다.

This means that the _power_ of the hypothesis test — the probability of correctly detecting a _non-zero_ coefficient — is reduced by collinearity.
이는 즉 가설 검정이 지닌 위력(_power_) — 통계적으로 제대로 _영이 아닌(non-zero)_ 유의미한 계수를 올바르게 검출해 낼 본연의 기저 확률 기능 — 자체가 이 공선성에 의해 심각하게 축소 약화된다는 것을 의미합니다.

Table 3.11 compares the coefficient estimates obtained from two separate multiple regression models.
표 3.11 은 분리되어 조작된 각기 다른 두 개의 다중 회귀 모델 쌍에서부터 도출해 내 얻은 각각의 계수 추정치 결과들을 비교합니다.

The first is a regression of `balance` on `age` and `limit`, and the second is a regression of `balance` on `rating` and `limit`.
첫 번째는 `balance` 를 `age` 와 `limit` 에 대응한 국면이고, 두 번째는 `balance` 를 `rating` 그리고 `limit` 요인에 대응해 추정한 회귀입니다.

In the first regression, both `age` and `limit` are highly significant with very small $p$-values.
첫 번째 회귀 척도 안에서는, `age` 요건이나 `limit` 양쪽 모두가 통계적으로 몹시 극히 작은 수위의 $p$-값을 뽐내며 매우 중요한 단위 유의성을 보입니다.

In the second, the collinearity between `limit` and `rating` has caused the standard error for the `limit` coefficient estimate to increase by a factor of 12 and the $p$-value to increase to $0.701$.
두 번째 국면에선 상황이 돌변하여, `limit` 와 `rating` 두 잣대 사이의 잠복된 공선성 파급력 탓에 해당 `limit` 계수 추정치를 둘러싼 기저 표준 오차 자체가 단숨 무려 12배 배율 인자 수위로 급증해 올랐고, $p$-값마저 덩달아 $0.701$ 로 폭등해 수위를 높였습니다.

In other words, the importance of the `limit` variable has been masked due to the presence of collinearity.
달리 말해 본래 `limit` 변수가 지녔어야 할 마땅한 특출난 본연의 중요성 가치가 다름 아닌 공선성의 존재라는 위장막에 가려져 훼손되고 숨겨진(masked) 것입니다.

To avoid such a situation, it is desirable to identify and address potential collinearity problems while fitting the model.
이러한 불운한 파급 상황을 사전에 모면코자 회피하기 위해서라도, 우리는 필히 모델을 조율해 적합하는 과정 초기 단면에 아예 이런 잠재적인 공선성 결함 문제를 조기 색출해 인지 파악하고 선결 과제로써 미리 선제 대응해 다루고 진압하는 것이 지극히 무던 바람직합니다.

A simple way to detect collinearity is to look at the correlation matrix of the predictors.
공선성 여부를 탐지하는 가장 간단한 방법 중 하나는 일련의 예측 변수 무리를 상대로 상관 행렬(correlation matrix) 단면을 유심히 들여다보는 것입니다.

An element of this matrix that is large in absolute value indicates a pair of highly correlated variables, and therefore a collinearity problem in the data.
이 행렬 기반 속성 성분들 중에서 유독 절댓값 규모가 양분 크게 부각되는 특정 도출 대역 잣대가 존재한다면, 이는 매우 높은 밀착 수준으로 상관된 관측 변수 한 쌍이 도사림을 뜻하며, 결과적으로 기반 데이터 묶음 내에 공선성 문제가 산재하고 있음을 예의 가리킵니다.

Unfortunately, not all collinearity problems can be detected by inspection of the correlation matrix: it is possible for collinearity to exist between three or more variables even if no pair of variables has a particularly high correlation.
불행히도 막상 상관 행렬 하나만 고집해 이리저리 단순 검사하는 일로는 전체 잠재 공선성 오류 파급을 전수 탐지해 낼 수 없습니다: 설령 개별 어느 변수 짝들도 서로 그다지 유별나게 막대 높은 높은 상관관계를 전혀 나타내 보이고 있지 않더라도, 정작 국지적으로 서너 개 이상의 여러 변수 군집이 한데 난립 얽힌 상태에서의 복합적인 공선성은 버젓이 은연중 그 틈새에 존재 도사릴 국면 여지가 넉넉히 다분하기 때문입니다.

We call this situation _multicollinearity_.
우리는 이렇듯 복잡하고 은밀히 얽힌 요건 상황을 지칭하여 주로 _다중공선성(multicollinearity)_ 이라 명명해 부릅니다.

Instead of inspecting the correlation matrix, a better way to assess multicollinearity is to compute the _variance inflation factor_ (VIF).
이런 국면 타개를 위해선, 단순히 상관 행렬만 들여다보며 진단 검사하기보단 기왕 다중공선성을 가늠하고 평가하기 위함 일환으로 _분산 팽창 인수(variance inflation factor, VIF)_ 요건을 수리적으로 계산하는 방식이 한결 더 나은 유력 확실한 방법입니다.

The VIF is the ratio of the variance of $\hat{\beta}_j$ when fitting the full model divided by the variance of $\hat{\beta}_j$ if fit on its own.
VIF 척도란 전체 풀 세트의 변수를 모두 결집해 반영 가동시킨 관점 수위의 $\hat{\beta}_j$ 분산 파생 치수를 단순히 오직 혼자 홀로 이 녀석만을 달랑 단독 적용해 적합 시켰을 때의 $\hat{\beta}_j$ 분산 잣대값으로 정갈히 나눈 단편 비율 요소입니다.

The smallest possible value for VIF is $1$, which indicates the complete absence of collinearity.
이 VIF 가 닿아 도출할 수 있는 최고로 작은 역대 극하위 마지노선 최소 수치는 바로 1 이며, 이 특정 수위 지수는 그 자체로 아무 공선성이 일절 없는 기저 부재 결여(complete absence) 상태임을 확약 확인해 줍니다.

Typically in practice there is a small amount of collinearity among the predictors.
통상 대개 실무 통계 현장에서는 예측 변수들 상호 간에 항상 기저 약간의 크고 작은 소규모 분량의 공선성 지표는 은연 약간 띠면서 도사리기 마련입니다.

As a rule of thumb, a VIF value that exceeds 5 or 10 indicates a problematic amount of collinearity.
관습적 경험론 경험칙 규칙(rule of thumb)상, 대체로 도출 반환 계산된 VIF 지표값이 5 나 혹은 10 을 초과 능가하는 임계 경우일 때면, 필연 이는 심각히 다루어 궤도 수정에 올라타야 할 상당한 문제성 분량의 심각한 공선성이 얽혀 있음을 입증하는 적신호라 판단 평가 간주합니다.

The VIF for each variable can be computed using the formula



**==> picture [108 x 26] intentionally omitted <==**

where $R_{X_j | X_{-j}}^2$ is the $R^2$ from a regression of $X_j$ onto all of the other predictors.
여기서 수식의 $R_{X_j | X_{-j}}^2$ 은 다름 아닌 기준 예측 변수 $X_j$ 요소 하나를 그 밖의 여타 나머지 모든 타 예측 변수 군집 전반에 결합 대응 표적 삼아 실행한 회귀 분석에서부터 산출된 결과 속성의 $R^2$ 결정 치수를 일컫습니다.

If $R_{X_j | X_{-j}}^2$ is close to one, then collinearity is present, and so the VIF will be large.
만일 이 산입 결과 $R_{X_j | X_{-j}}^2$ 지표값이 $1$ 이란 수극선에 아주 고조 근막 다다를 만치 가깝게 도달한다면 필경 공선성이 강하게 존재(present)한다는 확증이며, 자연히 그에 부수 연동 계산된 VIF 수치도 대거 극히 높게 수직 커질 것입니다.



In the `Credit` data, a regression of `balance` on `age`, `rating`, and `limit` indicates that the predictors have VIF values of $1.01$, $160.67$, and $160.59$.
현행 우리 `Credit` 데이터 예시에서, `balance` 반응 잣대를 각각 `age`, `rating`, 그리고 `limit` 요인 묶음에 대응 타깃으로 세워 구동한 회귀 선 도출은 각 예측 변수가 파생하는 지표 VIF 척도가 순차적으로 각각 $1.01$, $160.67$, 및 자그마치 $160.59$ 수준임에 다다름을 명확히 지시 보입니다.

As we suspected, there is considerable collinearity in the data!
우리가 일찍 구석 짐작 예상 우려했던 그대로, 이 해당 데이터 국면 단면 내면 기저에는 매우 짙고 막대 상당량 응집된(considerable) 공선성이 한껏 내포 도사려 기생 발현 중입니다!

When faced with the problem of collinearity, there are two simple solutions.
공선성이 지닌 이 골치 아픈 난관 문제에 직면할 땐, 통상 둘 중 나은 아주 간편 간단한 두 가지 해법 중 하나를 꺼내 들 수 있습니다.

The first is to drop one of the problematic variables from the regression.
그 첫 단추 타개 조치는 지금 당장 회귀선 궤도상에서 이 불순 요인 문제의 변수들 쌍 중 어느 하나를 골라 아예 깨끗이 버려버리는(drop) 제명 조치 탈락 제거 수단입니다.

This can usually be done without much compromise to the regression fit, since the presence of collinearity implies that the information that this variable provides about the response is redundant in the presence of the other variables.
이런 단호 제거 조치를 단행하건만 통상 당면한 전체 회귀선 적합 결과 곡선에는 아무런 치명 타격 큰 타협 훼손조차 초래 무리 가해지지 않는데, 까닭은 바로 애당초 공선성이 존재한다는 그 사실 단초 지표 대목 자체가 바로 이 요인 변수가 여타 응답 변수를 설명하고자 이끌 보탤 가용 정보 조각이 이미 다른 잔여 변수의 존재 속에 모조리 다 고스란히 담겨 있어 그저 무의미한 중복 잉여(redundant) 정보일 뿐임을 여실히 대변 입증하기 때문입니다.

For instance, if we regress `balance` onto `age` and `limit`, without the `rating` predictor, then the resulting VIF values are close to the minimum possible value of 1, and the $R^2$ drops from $0.754$ to $0.75$.
일례로 단적으로 보아, 우리가 고집스러운 `rating` 예측 변수 조각 녀석 하나만 예외 덜어 치우고는 기꺼이 `balance` 지표를 오직 `age` 및 `limit` 항목 단둘 짝에만 연계 맞추어 투사 타깃 회귀시켰다고 가정할 시, 이윽고 이내 연동 산출 도출되어 나온 결과상 각 요건 VIF 값들은 이례적으로 아예 가장 안전 정상 가능한 최저 마지노 한도선인 1 단위 안팎 지수 한껏 그 주변 고도 범위 궤도에 다다르며, 반면 그 중요도 결과 $R^2$ 치수 낙폭은 일절 고작 끽 $0.754$ 상태에서 달랑 $0.75$ 로 아주 무던 미세하게 하락 변화 기조만을 띠는 데에서 멈춥니다.

So dropping `rating` from the set of predictors has effectively solved the collinearity problem without compromising the fit.
이 일례를 보듯, 애꿎은 잔재 예측 변수 무리 세트 단자에서 단지 문제 요인인 `rating` 이 하나 요소만 달랑 제명 떨어뜨리는 아주 간단 탈락 조처 부합만으로도 이 공선성 딜레마 문제는 필경 원래 회귀 적합선을 아예 전혀 조금도 타협 손상 변모하지 않고서도 단박 아주 효과 좋게 온전히 해결 수순으로 도달 타개되었습니다.

The second solution is to combine the collinear variables together into a single predictor.
두 번째 해결책 수단 요법은 문제가 된 여러 숱한 공선적 변수들을 한데 오밀조밀 합병 결합 응축해내어 아예 전혀 새로운 일개 단일 예측 변수 형태로 포섭 귀착시켜 버리는 것입니다.

For instance, we might take the average of standardized versions of `limit` and `rating` in order to create a new variable that measures _credit worthiness_.
예를 들자면, 기왕 다소 따로 겉돌 튀는 무관 `limit` 나 혹은 `rating` 항목들을 동일 잣대로 표준 변환된 상태로 끌어다 모아 합산 후 평균 조화를 단행 척도로 일궈, 나름 이들을 합친 포괄 측정 잣대로 유일한 _신용 적격성(credit worthiness)_ 일련 지표 수치를 대표 측정해 낼 무언가 전혀 새 국면 통합 단일 변수 개체를 단일 고안 도출 이룩해 내는 것입니다.

---

## Sub-Chapters (하위 목차)


[< 4 4. Outliers](../4_4._outliers/trans1.html) | [3.4 The Marketing Plan >](../../../3_4_the_marketing_plan/trans1.html)

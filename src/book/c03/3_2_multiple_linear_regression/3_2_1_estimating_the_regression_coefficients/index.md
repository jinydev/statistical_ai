---
layout: default
title: "index"
---

# _3.2.1 Estimating the Regression Coefficients_ 

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals 

$$
\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)
$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4

![In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.](./img/3_4.png)

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._

illustrates an example of the least squares fit to a toy data set with $$p=2$$ predictors.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data. 
표 3.4는 `Advertising` 데이터를 활용하여 제품 판매량을 예측할 목적으로 TV, 라디오, 그리고 신문 매체의 광고 예산을 사용했을 때 산출되는 다중 회귀 계수 추정치들을 보여줍니다. 

We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales. 
우리는 이러한 결과를 다음과 같이 해석합니다. TV 와 신문 광고 예산 수준이 고정되어 있을 때, 라디오 광고에 1,000 달러를 추가 지출하는 것은 대략 189 개 판매 단위의 매출 증가와 연관이 있습니다. 

Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates. 
이 추정치들을 표 3.1 과 3.3 의 수치 수치들과 비교하면, `TV` 와 `radio` 에 대한 다중 회귀 모델의 계수들이 단순 선형 회귀의 수치값들과 상당히 유사하다는 점을 알 수 있습니다. 

However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86. 
하지만 표 3.3에서 `newspaper` 선형 회귀 계수 추정치는 유의미하게 0이 아니었으나, 다중 회귀 기법에서의 `newspaper` 계수는 0에 극히 근접하며 해당하는 $p$-값은 0.86 수치 주위를 맴돌며 더는 유의미하지 않게 되었습니다. 

This illustrates that the simple and multiple regression coefficients can be quite different. 
이 사례는 단순 회귀 계수와 다중 모형 회귀의 예측 계수가 꽤 상이할 수 있음을 보여줍니다. 

This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`. 
이런 극명한 차이는 단순 회귀의 경우 기울기 척도가 `TV` 와 `radio` 등 타 변수를 무시한 채, 오직 신문 지면 부문 1,000달러 증가와 연관된 평균 판매액 증가치만 보여주기 때문에 발생합니다. 

By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.
이와 상반되게, 다중 회귀 맥락 환경에서 `newspaper` 측정 척도는 `TV` 나 `radio` 부문 예측값을 꼼짝 못하게 묶어둔 척도하에, 신문 매체에만 추가로 1,000달러 증액 투입 시 일어날 순수한 매출 상승 점수를 뜻하기에 다릅니다.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the opposite? 
단순 선형 회귀 기조에선 타깃 결과를 분명 내포한다고 했던 반면, 이 다중 분석단에선 극명하게 반대로 `sales` 와 `newspaper` 사이에 아무련 궤도 관계조차 성립되지 않는다 시사하는 양극 국면이 과연 맞는 기조일까요? 

In fact it does. 
답은 사실 이치에 전분 합당합니다. 

Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5. 
표 3.5 측면에 제시 수반된 세 단위 예측 변인 구도 및 반응 변인들 간 상관관계 수치 행렬도를 하나하나 세심히 들여다보십시오.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |
| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |
| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |
| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | $0.8599$ |

**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._ 
**TABLE 3.4.** `Advertising` _데이터의 경우, 이 표는 TV, 라디오 및 신문 다채 매체 광고 투입 예산에 따른 판매 단위 수에 대한 다중 선형 회귀의 최소 제곱 상관 계수 추정치를 투시 보여줍니다._

| | `TV` | `radio` | `newspaper` | `sales` |
| :--- | :--- | :--- | :--- | :--- |
| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |
| `radio` | 0.0548 | 1.0000 | 0.3541 | 0.5762 |
| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |
| `sales` | 0.7822 | 0.5762 | 0.2283 | 1.0000 |

**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._ 
**TABLE 3.5.** `Advertising` _데이터 내부 지표인_ `TV` _,_ `radio` _,_ `newspaper` _, 그리고_ `sales` _산하 간의 상관관계 행렬 도표입니다._

Notice that the correlation between `radio` and `newspaper` is 0.35. 
여기서 `radio` 와 `newspaper` 부문 등 양측 매체 간 상관관계 통계 계수가 대략 0.35 에 달한다는 대목을 주목하십시오. 

This indicates that markets with high newspaper advertising tend to also have high radio advertising. 
이는 일컬어 신문 광고 매체에 지출액을 더 크게 가동하는 시장들일수록 상대적으로 필연적인 경향을 타며 라디오 방송 광고 자본 투입 비율 역시 거대히 편성되는 빈도 성향이 우세함을 뜻합니다. 

Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales. 
자, 이제 이 일련 예측 결과들을 바탕 삼아 도출한 우리 다중 회귀 도식 전제가 옳으며, 지면 광고 자체는 본원 매출 척도와 털끝 관계가 전무하더라도 타 방면인 라디오 광고 부문 예산 지출만큼은 판매 실 성적과 긴 밀접성을 갖는다고 전제해 보겠습니다. 

Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets. 
그렇다면 응당히 우리가 라디오 부문에 추가 집중 비용을 더 편성 쏟은 해당 유력 시장들에서 상품 판매 진척고가 덩달아 상향 지표를 향할 것이며, 앞선 상관 행렬의 계수가 잘 보여주듯 우린 그 동일 과녁 핵심 시장 안에서 덤으로 추가적 신문 매체 지면에도 곁눈질 더 많은 자본을 소비 맹렬 투자하는 유사 성향마저 같이 띠게 됩니다. 

Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales. 
결과적으로, 이렇듯 단순 `sales` 대 `newspaper` 양대 축만을 쌍으로 묶어 따로 홀로 분석해 보는 한정된 단순 계수 선형 점검 구도에선, 비록 본원이 되는 신문 매체 투입 자체가 매출 파급 효과와 하등 직접 결부되어 있지 않음에도 역으로 막대한 `newspaper` 비용이 더 치솟은 `sales` 잣대랑 양의 비례 연대성을 동반 발산하는 양 왜곡 파악될 공산 소지가 도사립니다. 

So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` . 
다시 말해 이 `newspaper` 신문 광단 요소가 막연히 `radio` 라디오 매체 진본 파생 영향을 대리 대신해 주는 일종 단수 대역을 무심 짊어진 셈입니다; 겉으로만 볼 땐 `newspaper` 덩치가 실제 이 투입 무대 `radio` 파생분이 기여시킨 매출 `sales` 타깃에 수여한 당 파급 효과 몫의 허황된 "공로(credit)" 치수 점수만 그저 덤바가지 채 가로채 덧쓰는 양상 모의를 이끌 부과 받습니다. 

This slightly counterintuitive result is very common in many real life situations. 
현실 여건 내 실무 지표 등 많은 생활 잣대 모의 맥락 부문에선, 단박 이처럼 반짝 직관 단계를 살짝 뒤집어 배반하는 이치적 오류 양상 역설 통계 상황 국면이 얼추 아주 흔하게 다반 발현합니다. 

Consider an absurd example to illustrate the point. 
이 쟁점을 입증할 괴상한 예시 한 가지를 살펴봅시다. 

---
layout: default
title: "index"
---

# _3.2.1 Estimating the Regression Coefficients_ 

As was the case in the simple linear regression setting, the regression coefficients $\beta_0, \beta_1, \dots, \beta_p$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$, we can make predictions using the formula

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \dots + \hat{\beta}_p x_p \quad (3.21)
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_0, \beta_1, \dots, \beta_p$ to minimize the sum of squared residuals 

$$
\begin{align*}
\text{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \hat{\beta}_2 x_{i2} - \dots - \hat{\beta}_p x_{ip})^2
\end{align*} \quad (3.22)
$$

The values $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in `R`. Figure 3.4

![In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.](./img/3_4.png)

**FIGURE 3.4.** _In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane._

illustrates an example of the least squares fit to a toy data set with $$p=2$$ predictors.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the `Advertising` data. 
표 3.4는 `Advertising` 데이터를 활용하여 제품 판매량을 예측할 목적으로 TV, 라디오, 그리고 신문 매체의 광고 예산을 사용했을 때 산출되는 다중 회귀 계수 추정치들을 보여줍니다. 

We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional $\$1,000$ on radio advertising is associated with approximately 189 units of additional sales. 
우리는 이러한 결과를 다음과 같이 해석합니다. TV 와 신문 광고 예산 수준이 고정되어 있을 때, 라디오 광고에 1,000 달러를 추가 지출하는 것은 대략 189 개 판매 단위의 매출 증가와 연관이 있습니다. 

Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for `TV` and `radio` are pretty similar to the simple linear regression coefficient estimates. 
이 추정치들을 표 3.1 과 3.3 의 수치 수치들과 비교하면, `TV` 와 `radio` 에 대한 다중 회귀 모델의 계수들이 단순 선형 회귀의 수치값들과 상당히 유사하다는 점을 알 수 있습니다. 

However, while the `newspaper` regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for `newspaper` in the multiple regression model is close to zero, and the corresponding $p$-value is no longer significant, with a value around 0.86. 
하지만 표 3.3에서 `newspaper` 선형 회귀 계수 추정치는 유의미하게 0이 아니었으나, 다중 회귀 기법에서의 `newspaper` 계수는 0에 극히 근접하며 해당하는 $p$-값은 0.86 수치 주위를 맴돌며 더는 유의미하지 않게 되었습니다. 

This illustrates that the simple and multiple regression coefficients can be quite different. 
이 사례는 단순 회귀 계수와 다중 모형 회귀의 예측 계수가 꽤 상이할 수 있음을 보여줍니다. 

This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a $\$1,000$ increase in newspaper advertising, ignoring other predictors such as `TV` and `radio`. 
이런 극명한 차이는 단순 회귀의 경우 기울기 척도가 `TV` 와 `radio` 등 타 변수를 무시한 채, 오직 신문 지면 부문 1,000달러 증가와 연관된 평균 판매액 증가치만 보여주기 때문에 발생합니다. 

By contrast, in the multiple regression setting, the coefficient for `newspaper` represents the average increase in product sales associated with increasing newspaper spending by $\$1,000$ while holding `TV` and `radio` fixed.
이와 상반되게, 다중 회귀 맥락 환경에서 `newspaper` 측정 척도는 `TV` 나 `radio` 부문 예측값을 꼼짝 못하게 묶어둔 척도하에, 신문 매체에만 추가로 1,000달러 증액 투입 시 일어날 순수한 매출 상승 점수를 뜻하기에 다릅니다.

Does it make sense for the multiple regression to suggest no relationship between `sales` and `newspaper` while the simple linear regression implies the opposite? 
단순 선형 회귀 기조에선 타깃 결과를 분명 내포한다고 했던 반면, 이 다중 분석단에선 극명하게 반대로 `sales` 와 `newspaper` 사이에 아무련 궤도 관계조차 성립되지 않는다 시사하는 양극 국면이 과연 맞는 기조일까요? 

In fact it does. 
답은 사실 이치에 전분 합당합니다. 

Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5. 
표 3.5 측면에 제시 수반된 세 단위 예측 변인 구도 및 반응 변인들 간 상관관계 수치 행렬도를 하나하나 세심히 들여다보십시오.

| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |
| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |
| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |
| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | $0.8599$ |

**TABLE 3.4.** _For the_ `Advertising` _data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets._ 
**TABLE 3.4.** `Advertising` _데이터의 경우, 이 표는 TV, 라디오 및 신문 다채 매체 광고 투입 예산에 따른 판매 단위 수에 대한 다중 선형 회귀의 최소 제곱 상관 계수 추정치를 투시 보여줍니다._

| | `TV` | `radio` | `newspaper` | `sales` |
| :--- | :--- | :--- | :--- | :--- |
| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |
| `radio` | 0.0548 | 1.0000 | 0.3541 | 0.5762 |
| `newspaper` | 0.0567 | 0.3541 | 1.0000 | 0.2283 |
| `sales` | 0.7822 | 0.5762 | 0.2283 | 1.0000 |

**TABLE 3.5.** _Correlation matrix for_ `TV` _,_ `radio` _,_ `newspaper` _, and_ `sales` _for the_ `Advertising` _data._ 
**TABLE 3.5.** `Advertising` _데이터 내부 지표인_ `TV` _,_ `radio` _,_ `newspaper` _, 그리고_ `sales` _산하 간의 상관관계 행렬 도표입니다._

Notice that the correlation between `radio` and `newspaper` is 0.35. 
여기서 `radio` 와 `newspaper` 부문 등 양측 매체 간 상관관계 통계 계수가 대략 0.35 에 달한다는 대목을 주목하십시오. 

This indicates that markets with high newspaper advertising tend to also have high radio advertising. 
이는 일컬어 신문 광고 매체에 지출액을 더 크게 가동하는 시장들일수록 상대적으로 필연적인 경향을 타며 라디오 방송 광고 자본 투입 비율 역시 거대히 편성되는 빈도 성향이 우세함을 뜻합니다. 

Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales. 
자, 이제 이 일련 예측 결과들을 바탕 삼아 도출한 우리 다중 회귀 도식 전제가 옳으며, 지면 광고 자체는 본원 매출 척도와 털끝 관계가 전무하더라도 타 방면인 라디오 광고 부문 예산 지출만큼은 판매 실 성적과 긴 밀접성을 갖는다고 전제해 보겠습니다. 

Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets. 
그렇다면 응당히 우리가 라디오 부문에 추가 집중 비용을 더 편성 쏟은 해당 유력 시장들에서 상품 판매 진척고가 덩달아 상향 지표를 향할 것이며, 앞선 상관 행렬의 계수가 잘 보여주듯 우린 그 동일 과녁 핵심 시장 안에서 덤으로 추가적 신문 매체 지면에도 곁눈질 더 많은 자본을 소비 맹렬 투자하는 유사 성향마저 같이 띠게 됩니다. 

Hence, in a simple linear regression which only examines `sales` versus `newspaper` , we will observe that higher values of `newspaper` tend to be associated with higher values of `sales` , even though newspaper advertising is not directly associated with sales. 
결과적으로, 이렇듯 단순 `sales` 대 `newspaper` 양대 축만을 쌍으로 묶어 따로 홀로 분석해 보는 한정된 단순 계수 선형 점검 구도에선, 비록 본원이 되는 신문 매체 투입 자체가 매출 파급 효과와 하등 직접 결부되어 있지 않음에도 역으로 막대한 `newspaper` 비용이 더 치솟은 `sales` 잣대랑 양의 비례 연대성을 동반 발산하는 양 왜곡 파악될 공산 소지가 도사립니다. 

So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales` . 
다시 말해 이 `newspaper` 신문 광단 요소가 막연히 `radio` 라디오 매체 진본 파생 영향을 대리 대신해 주는 일종 단수 대역을 무심 짊어진 셈입니다; 겉으로만 볼 땐 `newspaper` 덩치가 실제 이 투입 무대 `radio` 파생분이 기여시킨 매출 `sales` 타깃에 수여한 당 파급 효과 몫의 허황된 "공로(credit)" 치수 점수만 그저 덤바가지 채 가로채 덧쓰는 양상 모의를 이끌 부과 받습니다. 

This slightly counterintuitive result is very common in many real life situations. 
현실 여건 내 실무 지표 등 많은 생활 잣대 모의 맥락 부문에선, 단박 이처럼 반짝 직관 단계를 살짝 뒤집어 배반하는 이치적 오류 양상 역설 통계 상황 국면이 얼추 아주 흔하게 다반 발현합니다. 

Consider an absurd example to illustrate the point. 
이 쟁점을 입증할 괴상한 예시 한 가지를 살펴봅시다. 

Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper` . 
어느 해변 마을에서 일정 기간 수집된 상어 습격 횟수 대 아이스크림 판매량 데이터를 회귀 분석하면, 앞서 `sales` 와 `newspaper` 사이에 나타난 것과 유사한 양(+) 의 상관관계를 보여줄 것입니다. 

Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks. 
물론 상어 습격을 줄이기 위해 해변에서 아이스크림 판매를 금지해야 한다고 제안한 사람은 (아직) 없습니다. 

In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks. 
실제로 높은 기온은 더 많은 사람들이 해변을 찾게 만들며, 이는 결국 아이스크림 판매량 증가와 상어 습격 횟수 증가라는 두 가지 결과를 동시에 초래합니다. 

A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.
상어 습격 횟수를 아이스크림 판매량과 온도라는 두 변수에 대해 다중 회귀 분석해 보면, 우리의 직관대로 온도를 고려한 후에는 아이스크림 판매량이 더 이상 유의미한 예측 요인이 아님을 밝혀줍니다.

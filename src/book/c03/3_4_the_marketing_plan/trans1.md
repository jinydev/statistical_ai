---
layout: default
title: "trans1"
---

[< 6 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/trans1.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 3.4 The Marketing Plan

# 3.4 마케팅 계획

We now briefly return to the seven questions about the `Advertising` data that we set out to answer at the beginning of this chapter.

이제 잠시 이 장의 서두 부분에서 해답을 찾고자 제시했던 `Advertising` 데이터 관련 7가지 질문들로 되돌아가 보겠습니다.

1. _Is there a relationship between sales and advertising budget?_

1. _판매량과 광고 예산 사이에는 어떤 관계가 존재합니까?_

This question can be answered by fitting a multiple regression model of `sales` onto `TV`, `radio`, and `newspaper`, as in (3.20), and testing the hypothesis $H_0 : \beta_\text{TV} = \beta_\text{radio} = \beta_\text{newspaper} = 0$.

이 질문에 대한 답은 수식 (3.20) 항목에서처럼 `sales` 결괏값을 `TV`, `radio`, 그리고 `newspaper` 세 변수에 대응시켜 다중 회귀 모델로 적합하고 나아가 귀무가설 $H_0 : \beta_\text{TV} = \beta_\text{radio} = \beta_\text{newspaper} = 0$ 잣대를 함께 검정 해봄으로써 해답을 구할 수 있습니다.

In Section 3.2.2, we showed that the $F$-statistic can be used to determine whether or not we should reject this null hypothesis.

이전 섹션 3.2.2 에서 우리는 이 귀무가설의 기각 여부를 결정 지을 때 $F$-통계값 지표를 도구로 사용할 수 있음을 보여주었습니다.

In this case the $p$-value corresponding to the $F$-statistic in Table 3.6 is very low, indicating clear evidence of a relationship between advertising and sales.

표 3.6 자료에 나타난 이 예제의 $F$-통계치와 연관된 $p$-값 척도는 몹시 매우 낮은 수위이며, 이는 곧 전반적인 광고 예산 활동과 판매량 사이에 아주 확연한 관계가 존재한다는 것을 뚜렷이 증명합니다.

2. _How strong is the relationship?_

2. _그 관계는 얼마만큼이나 강합니까?_

We discussed two measures of model accuracy in Section 3.1.3.

우리는 앞선 섹션 3.1.3 단면에서 모델의 정확도를 평가 지표하는 두 가지 주요 척도의 방법론을 논의했습니다.

First, the RSE estimates the standard deviation of the response from the population regression line.

첫째로, RSE 잣대는 모집단 회귀선 측면에서 응답치 파생물이 지닌 고유의 표준 편차치를 추산 가늠해 냅니다.

For the `Advertising` data, the RSE is $1.69$ units while the mean value for the response is $14.022$, indicating a percentage error of roughly $12\%$.

`Advertising` 데이터 예시의 경우, RSE 수치는 대략 $1.69$ 단위로 산출되는 반면 전체 평균 응답값은 $14.022$ 에 달하며, 이는 비율상 대략 고작 $12\%$ 수준의 상대적 오차율이 존재함을 나타냅니다.

Second, the $R^2$ statistic records the percentage of variability in the response that is explained by the predictors.

둘째는 $R^2$ 통계 수치 지표인데, 이는 주어진 예측 변수에 의해 해명 설명될 수 있는 전체 응답 측 변동성의 차지 비율 등을 퍼센트로 기록 산입합니다.

The predictors explain almost $90\%$ of the variance in `sales`.

위 예측 변수들은 단연코 `sales` 에 발생한 전체 총분산의 거의 대략 $90\%$ 상당 부분을 해명해 냅니다.

The RSE and $R^2$ statistics are displayed in Table 3.6.

이 두 RSE 와 $R^2$ 결과 통계 내역은 함께 묶어 표 3.6 에 전시 도표로 표시되어 있습니다.

3. _Which media are associated with sales?_

3. _과연 어떤 미디어 매체가 실제 판매량과 깊이 연관되어 있습니까?_

To answer this question, we can examine the $p$-values associated with each predictor's $t$-statistic (Section 3.1.2).

이 질문의 물음에 명확히 답하고자, 우리는 각 예측 변수에 걸쳐진 $t$-통계량과 같이 맞물려 연관된 $p$-값 지수들을 단편 개별 조사해 볼 수 있습니다(섹션 3.1.2).

In the multiple linear regression displayed in Table 3.4, the $p$-values for `TV` and `radio` are low, but the $p$-value for `newspaper` is not.

표 3.4 에 기재된 다중 선형 회귀 측면 결과를 보면, 이중 `TV` 및 `radio` 에 관련된 두 $p$-값 수치는 눈에 띄게 현격히 낮지만 정작 `newspaper` 의 $p$-값은 결코 그다지 낮지 않습니다.

This suggests that only `TV` and `radio` are related to `sales`.

이러한 단편적 사실은 기실 `TV` 와 `radio` 만이 실제 `sales` 쪽과 어떤 유의미한 연관 관계에 있다는 점을 노골 시사합니다.

In Chapter 6 we explore this question in greater detail.

향후 제 6장에서 이 궁금증 질문을 다시금 소환해 한층 더 세부적으로 깊게 파헤쳐 탐구해 볼 것입니다.

4. _How large is the association between each medium and sales?_

4. _각 매체별로 판매량 사이에 형성된 연관성의 규모 크기는 어느 정도입니까?_

We saw in Section 3.1.2 that the standard error of $\hat{\beta}_j$ can be used to construct confidence intervals for $\beta_j$.

우린 섹션 3.1.2 부문에서 $\hat{\beta}_j$ 척도 요소의 표준 오차가 실제로 $\beta_j$ 의 신뢰 구간 궤도를 설정 구성 구축하는 데 널리 요긴히 사용될 수 있음을 지켜보았습니다.

For the `Advertising` data, we can use the results in Table 3.4 to compute the $95\%$ confidence intervals for the coefficients in a multiple regression model using all three media budgets as predictors.

`Advertising` 데이터에 빗대어, 우리 측은 표 3.4 에 기재된 통계 결과들을 재차 적극 활용하여, 세 종류 미디어 예산 전부를 예측 변수로 삼아 수립한 다중 회귀 모델의 각 궤도 계수에 대한 $95\%$ 신뢰 구간을 산입 계산 도출해 낼 수 있습니다.

The confidence intervals are as follows: $(0.043, 0.049)$ for `TV`, $(0.172, 0.206)$ for `radio`, and $(-0.013, 0.011)$ for `newspaper`.

각 항목의 신뢰 구간은 다음과 같습니다: `TV` 는 $(0.043, 0.049)$, `radio` 는 $(0.172, 0.206)$, 그리고 나머지 `newspaper` 는 $(-0.013, 0.011)$ 입니다.

The confidence intervals for `TV` and `radio` are narrow and far from zero, providing evidence that these media are related to `sales`.

`TV` 며 `radio` 의 신뢰 구간 대역폭 궤도는 상당히 좁고 또 그 위치조차 기준 0에서 한참 멀리 이격되어 있는데, 이는 단연코 이들 둘 매체만큼은 `sales` 측 지표와 분명히 연관되어 있음을 보증하는 증거를 제공합니다.

But the interval for `newspaper` includes zero, indicating that the variable is not statistically significant given the values of `TV` and `radio`.

반면 `newspaper` 가 띤 신뢰 구간 잣대엔 영(0) 수치가 포함되어 속해 있는데, 이는 이미 주어진 `TV` 및 `radio` 변수 잣대 값들 여건하에서는 정작 이 변수 하나가 딱히 어떠한 별다른 통계적 유의성마저 확보 내지 지니지 못함을 여실히 대변해 나타냅니다.

We saw in Section 3.3.3 that collinearity can result in very wide standard errors.

섹션 3.3.3 파트에서 우리는 심각한 공선성이 때론 아주 극단적으로 방대한 넓은 형태의 표준 오차 수치를 초래할 소지가 다분함을 논의했습니다.

Could collinearity be the reason that the confidence interval associated with `newspaper` is so wide?

그렇담 혹시 위 `newspaper` 에 연관된 신뢰 구간의 폭이 저리 넓게 형성된 주된 이유 연유가 다름 아닌 그런 공선성 탓은 아닐까요?

The VIF scores are $1.005$, $1.145$, and $1.145$ for `TV`, `radio`, and `newspaper`, suggesting no evidence of collinearity.

현재 각 `TV`, `radio`, 그리고 `newspaper` 항목별 VIF 계산 점수 지표는 순서대로 각각 $1.005$, $1.145$, 그리고 $1.145$ 에 불과하며, 이는 실상 어느 모델 단면에도 공선성의 폐해를 시사하는 증거 따윈 도무지 일절 없다는 사실을 잘 부연해 제안 설명합니다.

In order to assess the association of each medium individually on sales, we can perform three separate simple linear regressions.

각 단일 미디어가 어떻게 개별적으로 전체 판매 부문에 영향을 미치는지를 정확히 판가름하고 평가 가늠코자, 우리는 세 차례의 별도 분리된 단순 선형 회귀 모형 측면을 개별 전개 및 수행해 볼 수 있습니다.

Results are shown in Tables 3.1 and 3.3.

그 분리된 결과들은 각각 나누어 표 3.1 며 3.3 양 측면에 제시 전시되어 있습니다.

There is evidence of an extremely strong association between `TV` and `sales` and between `radio` and `sales`.

`TV` 며 `sales` 사이, 그리고 `radio` 및 `sales` 사이 이 두 경우 모두에선 대단 아주 강력하게 결부된 극심한 강한 연관성 여부의 단서 증거가 뚜렷이 나타나 보입니다.

There is evidence of a mild association between `newspaper` and `sales`, when the values of `TV` and `radio` are ignored.

다만 애초 기저에 널린 여타 `TV` 라거나 혹은 `radio` 따위 여타 변수 인자 값들을 통째 아예 무시해 고려 배제했을 시에 한하여, 저기 `newspaper` 단면과 최종 `sales` 부문 사이에 겨우 그나마 얕고 온화 약소한 미미 연관 기류가 일부 다행스레 좀 존재한다는 증거 여부만이 극소수 관찰 도출될 따름입니다.

5. _How accurately can we predict future sales?_

5. _다가올 미래 향후의 총 판매량을 우리는 과연 얼마나 정확히 예측해 낼 수 있습니까?_

The response can be predicted using (3.21).

목표 응답치는 공식 (3.21) 형태를 전면 이용해서 예측 모의 산입해 낼 수 있습니다.

The accuracy associated with this estimate depends on whether we wish to predict an individual response, $Y = f(X) + \epsilon$, or the average response, $f(X)$ (Section 3.2.2).

이 산출 추정치 결과가 띠는 신뢰 정확도는 우리가 궁극적으로 예측을 희망해 지향하는 바가 어느 단일 낱개 일개 응답치 측면인 $Y = f(X) + \epsilon$ 국면인지, 아니면 전반적인 평균 지표 응답 요소 모의인 $f(X)$ 국면(섹션 3.2.2)인지에 전적으로 크게 좌우 기여 의존합니다.

If the former, we use a prediction interval, and if the latter, we use a confidence interval.

만일 우리의 목표 시선이 전자에 쏠려 있다면 통상 일개 예측 구간(prediction interval) 틀을 차용하고, 후자에 뜻을 두었다면 신뢰 구간(confidence interval) 기조 잣대를 적용 동반 사용합니다.

Prediction intervals will always be wider than confidence intervals because they account for the uncertainty associated with $\epsilon$, the irreducible error.

주지하듯 예측 구간 범위는 축소 축적 불가결한 이른바 피할 줄일 수 없는 줄일 수 없는 오차(irreducible error) 격인 $\epsilon$ 속성 관련 기저 불확실성 소지 여파까지 모조리 다 총체 감안 동반 계산하므로, 예외 없이 늘 신뢰 구간보다 훨씬 더 넓게 팽창 벌어져 나타납니다.

6. _Is the relationship linear?_

6. _그렇담 형성된 변수 간 내재 관계 양상은 선형성을 띱니까?_

In Section 3.3.3, we saw that residual plots can be used in order to identify non-linearity.

섹션 3.3.3 을 통해 비선형성 형태를 인지 단안 식별하는 주요 목적 용도로 잔차 플롯이 요긴 적용 사용될 수 있음을 보았습니다.

If the relationships are linear, then the residual plots should display no pattern.

만일 그들 모델 안의 잔존 관계가 올곧게 선형이라면 투영 산출된 잔차 플롯 표면에는 일절 아무 패턴 형태 무늬 따위가 아예 나타나지 않아야 정상입니다.

In the case of the `Advertising` data, we observe a non-linear effect in Figure 3.5, though this effect could also be observed in a residual plot.

하지만 이 `Advertising` 데이터 사례 예시 국면에선 설사 이 돌출 파급력을 잔차 플롯에서 포착 확인했을 수도 있겠으나, 여실히 위 그림 3.5 측면에 버젓이 비선형 형태 효과 지수 파급이 노골 표출되어 나타남을 육안 관찰할 수 있습니다.

In Section 3.3.2, we discussed the inclusion of transformations of the predictors in the linear regression model in order to accommodate non-linear relationships.

섹션 3.3.2 파트에서 모델 내 이렇듯 복잡다단한 비선형 성격 관련성을 수용 타협 접목코자, 통상 일선 선형 회귀 모델 편제 안에 여러 예측 변수에 대한 갖가지 치환 변환 도구 기능을 무리 산입 포함해 두는 것을 둘러싸고 논의를 개진한 바 있습니다.

7. _Is there synergy among the advertising media?_

7. _광고 미디어 매체들 그 사이사이에 일말의 어떤 모종의 시너지 효과가 도사려 있습니까?_

The standard linear regression model assumes an additive relationship between the predictors and the response.

단순 무결한 보편 표준 선형 회귀 모의는 본디 예측 변수 무리와 결론 응답 측 사이에 흔들림 없는 다소 일관 가산적(additive)인 측면 관계가 성립하리라 임의 가정합니다.

An additive model is easy to interpret because the association between each predictor and the response is unrelated to the values of the other predictors.

어차피 이런 기초적인 가산 모델 구조는 개별 예측 변수 낱개가 최종 결론 파견 응답과 개별적으로 맺는 일련의 연관성 결부 자체가 이렇다 할 다른 여타 나머지 예측 변숫값들과 전조 엮임이나 상관 무관한 까닭에 향후 수치를 풀어 결과물을 단순 해석하기 참 유용하고 쉽습니다.

However, the additive assumption may be unrealistic for certain data sets.

허나, 막상 몇몇 특정 예외 소지 데이터 세트 군집에서는 이러한 일방적 단순 가산 기조 전제 가정이 그저 허상에 불과할 만치 자못 영 비현실적 국면으로 나타날지 모릅니다.

In Section 3.3.2, we showed how to include an interaction term

in the regression model in order to accommodate non-additive relationships.

이윽고 앞선 섹션 3.3.2 절에서 우리는 이러한 다소 비가산적 측면 관계 기조를 보완 조달해 수용하고자 회귀 산출 모델 안에 어떤 일정한 상호작용 항(interaction term)을 부가 무리 포함 산입케 할 방도를 전개 소개했습니다.

A small $p$-value associated with the interaction term indicates the presence of such relationships.

통상 이러한 상호작용 측면 항과 긴밀 연좌 엮어진 아주 작은 $p$-값 크기는, 막상 그런 이질적 복합 관계 존재가 데이터 안에 실질 숨어 있음을 뚜렷 지지 적시합니다.

Figure 3.5 suggested that the `Advertising` data may not be additive.

이러한 연유로 이미 그림 3.5 는 `Advertising` 관련 산입 데이터가 실상 완전히 가산적 측면만 띠지 않을 수 있단 여력을 은연 시사 제안한 바 있습니다.

Including an interaction term in the model results in a substantial increase in $R^2$, from around $90\%$ to almost $97\%$.

기실 해당 모델 내 이 상호작용 항 변수를 하나 더해 함께 포함 산입 시켜버리는 조치 행위만으로도, 산출 반환 $R^2$ 수준은 기존 $90\%$ 안팎가량 치수에서 무려 자그마치 대략 거의 $97\%$ 근접 수준까지 대단 아주 비약 상당하고 막대 실질적인 규모로 증가하는 결과를 배출 표출해 증명 냅니다.

---

## Sub-Chapters (하위 목차)


[< 6 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/trans1.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/trans1.html)

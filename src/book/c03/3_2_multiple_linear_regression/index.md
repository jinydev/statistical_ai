---
layout: default
title: "index"
---

# 3.2 Multiple Linear Regression 
# 3.2 다중 선형 회귀 (Multiple Linear Regression)

Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the `Advertising` data, we have examined the relationship between sales and TV advertising. We also have data for the amount of money spent advertising on the radio and in newspapers, and we may want to know whether either of these two media is associated with sales. How can we extend our analysis of the advertising data in order to accommodate these two additional predictors? 

단순 선형 회귀는 단 하나의 매개 예측 변수를 기반으로 종결 응답값을 예측 도출하는 데 꽤 쏠쏠 유용한 접근법 체계입니다. 하지만 숱한 통계 실무 적용에서는 종종 우리는 두 개 이상의 복수 다단 예측 변수를 쥐게 발현됩니다. 한 예시로 앞선 `Advertising` 예제 데이터에서 우리는 줄곧 판매량과 관련 매개 TV 광고 지출 사이의 연관 관계를 분석 조사해 보았습니다. 그러나 우리는 모델 부가적으로 라디오 채널과 신문 등의 타 여타 매체 투입에 할당 지출된 별개 예산에 대한 결론 데이터도 함께 지니고 있으며, 이런 추가 2대의 동시 매체 역시 과연 제품 판매고와 동일 선상에 놓여 연관 부합 작용이 성립 지지 될지 그 여부를 모종 판단 파악하고 싶을 모루 심의 수 있습니다. 과연 이 두 개의 다중 구비 추가 예측 단위 변수를 온전히 다 부합 수용 통지하면서 과연 우리가 기존의 단일 광고 데이터 도면 분석 체계를 어떻게 무리 치수 없이 확장 도달 적용할 수 있을까요?

One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the amount spent on radio advertisements. Results are shown in Table 3.3 (top table). We find that a $\$1,000$ increase in spending on radio advertising is associated with an increase in sales of around 203 units. Table 3.3 (bottom table) contains the least squares coefficients for a simple linear regression of sales onto newspaper advertising budget. A $\$1,000$ increase in newspaper advertising budget is associated with an increase in sales of approximately 55 units. 

한 가지 도출 옵션은 각기 개별 분리된 매 광고 매체를 개별 예측 기조 단위로 번갈아 삼아 총 세 번의 별개 분리된 단순 선형 회귀 모의를 따로 도별 돌리는 것입니다. 이를테면, 우리는 오직 단독 라디오 기조 광고 선단 비용을 기초 바탕으로 실 판매량을 투안 예측해 내는 단 한 번의 단일 단순 적합 선형 모의를 모델에 따로 개별 사용할 수 도구 당장 있습니다. 그 단독 결과치는 앞선 표 3.3 (윗단 부분 표) 에 부비 제공 나와 조달 있습니다. 우리는 단락 라디오 단매 매체 예산에 단일 대한 조결 1,000 달러 단위 증가가 총 매출 규모 203 개의 상품 단품 유닛 단면의 추가 산입으로 직결 도달 연동된다는 사실 본위 결과를 산안 도달 보아 알았습니다. 더불어 표단 표 3.3 (하단 부분 표) 을 투지 보면 역시나 단일 신문 광고 매체 구도 예산을 기초 기준 삼아 개별 기조 회귀한 최소 제단 제곱 적합 계수 결론 결과치가 분리 명시 제출되어 있습니다. 단수 신문 광고 예산 부문의 1,000 달러 단위 단결 예산 증가는 실결 도달 실제 총 판매 수요 수위 선상에서 대략 모달 평균 구단 55개 상품 단위 규모 부피의 수량 이익 증가 결과와 모도 부합 연동 진지 발현되어 도출 지지됩니다.

However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertising media budgets, since each of the budgets is associated with a separate regression equation. Second, each of the three regression equations ignores the other two media in forming estimates for the regression coefficients. We will see shortly that if the media budgets are correlated with each other in the 200 markets in our data set, then this can lead to very misleading estimates of the association between each media budget and sales. 

하지만 매 예측 변수마다 별개의 단순 선형 모델을 여러 번 각각 적합시키는 접근법은 전적으로 만족스럽지가 못합니다. 무엇보다도 세 매체 광고 예산이 주어졌을 때 이를 기반으로 어떻게 단일한 판매 예측치를 도출할지가 불분명한데, 그 이유는 각각의 예산이 분리된 별개의 회귀 방정식과 묶여 있기 때문입니다. 둘째로, 세 개의 각 예측 회귀 방정식들이 자가 회귀 계수를 형성 산출할 때 나머지 다른 두 매체는 철저히 무시하게 됩니다. 만약 우리 200개 규모의 데이터 세트 시장 내에서 다른 매체별 예산들이 피차 서로 밀접하게 상관관계를 지니고 있을 경우, 이러한 접근법이 매체별 예산과 판매량 간의 결부 관계 분석에 관해 매우 심각하게 오도된 추정치를 초래할 수 있음을 잠시 후 확인하게 될 것입니다.

Instead of fitting a separate simple linear regression model for each predictor, a better approach is to extend the simple linear regression model (3.5) so that it can directly accommodate multiple predictors. We can do this by giving each predictor a separate slope coefficient in a single model. In general, suppose that we have $p$ distinct predictors. Then the multiple linear regression model takes the form 

매번 각 개별 요인마다 분리된 선형 모델을 단독 적합시키는 것보다 차라리 더 나은 접근법은 선형 회귀 모델 (3.5) 체계 자체를 크게 확장하여 다수의 예측 변수를 직접 통째로 한 번에 수용할 수 있게 고치는 길입니다. 우리는 하나의 단일 모델 내에서 각 예측 변수마다 독립적인 개별 기울기 계수를 제공해 주며 이 작업을 원활히 진행할 수 있습니다. 일반적으로, 우리에게 서로 구별되는 독립된 $p$ 개의 예측 변수가 있다고 설정합시다. 그렇다면 다중 선형 회귀 모의 방식은 필연적으로 다음과 같은 형태를 띱니다.

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon \quad (3.19)
$$

where $X_j$ represents the $j$th predictor and $$\beta_j$$ quantifies the association between that variable and the response. We interpret $$\beta_j$$ as the _average_ effect on $Y$ of a one unit increase in $X_j$, _holding all other predictors fixed_. In the advertising example, (3.19) becomes

여기서 요소 $X_j$ 는 $j$번째 개별 예측 요인을 대표하며, $$\beta_j$$ 항은 해당 특정 변수와 응답 사이의 단일 기조 상관관계를 직접 통계 정량화합니다. 우리는 응당 $\beta_j$ 계수를 향해, _나머지 여타 모든 예측수 변인들을 모두 정지 고정시킨 채_ 기준점 $X_j$ 한 단위를 1 스케일 증액할 적마다 그 여파로 인해 도출 반응 $Y$ 에 미치게 될 _평균(average)_ 적인 파급 효능 효과 성분으로 해석 수렴합니다. 광고 기초 예제를 들면 식 (3.19) 공식 체계는 이렇게 수합 변경됩니다.

$$
\text{sales} = \beta_0 + \beta_1 \times \text{TV} + \beta_2 \times \text{radio} + \beta_3 \times \text{newspaper} + \epsilon \quad (3.20)
$$

---

## Sub-Chapters (하위 목차)

### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)
* [문서로 이동하기](./3_2_1_estimating_the_regression_coefficients/)

여러 개의 설명 변수를 모두 포함한 다차원 공간에서 평균 잔차 제곱합을 최소화하는 하이퍼플레인을 찾는 과정을 배웁니다.
단순 회귀 때와 비교해 계수의 의미가 어떻게 변하는지 확인합니다.

### 3.2.2 Some Important Questions (중요한 질문들)
* [문서로 이동하기](./3_2_2_some_important_questions/)

다중 선형 회귀 모델을 사용할 때 답해야 하는 주요 질문(변수들의 유의성, 모델 적합도, 예측)들을 제기합니다.
이후의 소단원들을 통해 해당 질문들에 대한 단계적 통계 검증 프로세스를 다룹니다.

---
layout: default
title: "trans1"
---

[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/trans1.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Three: Model Fit

# 질문 3: 모델 적합도 (Three: Model Fit)

Two of the most common numerical measures of model fit are the RSE and $R^2$, the fraction of variance explained.

모델 적합도를 나타내는 가장 일반적인 두 가지 수치적 척도는 RSE 와 설명된 분산의 비율인 $R^2$ 입니다.

These quantities are computed and interpreted in the same fashion as for simple linear regression.

이 양들은 단순 선형 회귀에서와 동일한 방식으로 계산되고 해석됩니다.

Recall that in simple regression, $R^2$ is the square of the correlation of the response and the variable.

단순 회귀 분석에서 $R^2$ 가 응답과 변수 간 상관계수의 제곱이었음을 상기하십시오.

In multiple linear regression, it turns out that it equals $\text{Cor}(Y, \hat{Y})^2$, the square of the correlation between the response and the fitted linear model; in fact one property of the fitted linear model is that it maximizes this correlation among all possible linear models.

다중 선형 회귀에서, 이 값은 응답과 적합된 선형 모델 사이 상관관계의 제곱인 $\text{Cor}(Y, \hat{Y})^2$ 과 동일한 것으로 밝혀집니다; 사실 적합된 선형 모델의 한 가지 속성은 그것이 가능한 모든 선형 모델들 중에서 이 상관관계를 최대화한다는 것입니다.

An $R^2$ value close to 1 indicates that the model explains a large portion of the variance in the response variable.

1에 가까운 $R^2$ 값은 모델이 응답 변수 내 분산의 상당 부분을 설명하고 있음을 나타냅니다.

As an example, we saw in Table 3.6 that for the `Advertising` data, the model that uses all three advertising media to predict `sales` has an $R^2$ of $0.8972$.

예를 들어, 우리는 표 3.6 에서 `Advertising` 데이터의 경우, `sales` 를 예측하기 위해 세 가지 광고 매체를 모두 사용하는 모델의 $R^2$ 가 $0.8972$ 임을 보았습니다.

On the other hand, the model that uses only `TV` and `radio` to predict `sales` has an $R^2$ value of $0.89719$.

반면, `sales` 를 예측하기 위해 오직 `TV` 와 `radio` 만을 사용하는 모델은 $0.89719$ 의 $R^2$ 값을 가집니다.

In other words, there is a _small_ increase in $R^2$ if we include newspaper advertising in the model that already contains TV and radio advertising, even though we saw earlier that the $p$-value for newspaper advertising in Table 3.4 is not significant.

다시 말해, 만약 우리가 이미 TV 와 라디오 광고를 포함하고 있는 모델에 신문 광고를 포함한다 하더라도, 비록 우리가 앞서 표 3.4 에서 신문 광고의 $p$-값이 유의미하지 않음을 확인했음에도 불구하고 $R^2$ 에 _아주 작은(small)_ 증가가 발생합니다.

It turns out that $R^2$ will always increase when more variables are added to the model, even if those variables are only weakly associated with the response.

비록 그러한 변수들이 단지 응답과 약하게 연관되어 있을 뿐이더라도, 더 많은 변수들이 모델에 추가될 때 $R^2$ 는 항상 증가하게 되는 것으로 밝혀집니다.

This is due to the fact that adding another variable always results in a decrease in the residual sum of squares on the training data (though not necessarily the testing data).

이는 또 다른 변수를 추가하는 행위가 (비록 테스트 데이터에서는 반드시 그렇진 않더라도) 훈련 데이터상의 잔차 제곱합에서 언제나 감소를 야기한다는 사실 때문입니다.

Thus, the $R^2$ statistic, which is also computed on the training data, must increase.

따라서 훈련 데이터를 바탕으로 함께 산출되는 $R^2$ 통계량은 반드시 증가해야만 합니다.

The fact that adding newspaper advertising to the model containing only TV and radio advertising leads to just a tiny increase in $R^2$ provides additional evidence that `newspaper` can be dropped from the model.

오직 TV 와 라디오 광고만을 포함하는 모델에 신문 광고를 추가하는 행위가 단지 아주 미미한 $R^2$ 증가 수치만을 이끌어 낸다는 사실은 부차적으로 모델에서 `newspaper` 요소를 제외시켜도 무방하다는 추가적인 증거를 제공합니다.

Essentially, `newspaper` provides no real improvement in the model fit to the training samples, and its inclusion will likely lead to poor results on independent test samples due to overfitting.

본질적으로, `newspaper` 매체는 훈련 표본에 적합된 모델 내에서 어떠한 실질 개선도 제공하지 못하며, 이것의 무리한 포함 시도는 오히려 과적합으로 인해 독립적인 테스트 표본에서 좋지 못한 결과를 야기할 가능성이 높습니다.

By contrast, the model containing only `TV` as a predictor had an $R^2$ of $0.61$ (Table 3.2).

대조적으로, 오직 예측 변수로써 `TV` 하나만 담고 있던 모델은 $0.61$ 의 결정 계수 $R^2$ (표 3.2) 값을 가졌습니다.

Adding `radio` to the model leads to a substantial improvement in $R^2$.

해당 모델에 `radio` 항목을 덧붙이는 행위는 $R^2$ 수치에 아주 상당한 상승 수준의 개선을 초래합니다.

This implies that a model that uses TV and radio expenditures to predict sales is substantially better than one that uses only TV advertising.

이것은 향후 매출을 예측할 때 TV 와 라디오 지출분 모두를 사용하는 예측 모델이, 오로지 TV 단일 광고 매체만 취급하던 모델보다 실질적으로 훨씬 뛰어나다는 점을 암시합니다.

We could further quantify this improvement by looking at the $p$-value for the `radio` coefficient in a model that contains only `TV` and `radio` as predictors.

예측 변수로 오직 `TV` 와 `radio` 만을 지니는 모델 내에서 `radio` 계수에 해당하는 $p$-값을 살펴봄으로써 우리는 이 개선도를 한층 더 수량화해 구체화할 수 있습니다.

The model that contains only `TV` and `radio` as predictors has an RSE of 1.681, and the model that also contains `newspaper` as a predictor has an RSE of 1.686 (Table 3.6).

오직 예측 성분으로 `TV` 와 `radio` 지표만을 기용한 모델의 경우 RSE 기반치가 1.681 이며, 부가 예측 인자로써 `newspaper` 인자 요소까지 동반 구축한 모델 구성은 RSE 수치로 1.686 구간점을 갖습니다(표 3.6).

In contrast, the model that contains only `TV` has an RSE of $3.26$ (Table 3.2).

이와 대조적으로 오직 `TV` 만을 기용한 모델의 RSE 스코어는 $3.26$ 점입니다(표 3.2).

This corroborates our previous conclusion that a model that uses TV and radio expenditures to predict sales is much more accurate (on the training data) than one that only uses TV spending.

이 점은 매출 궤적을 예측하고자 할 때 TV 비용 편성과 라디오 비용 지출 내역을 모두 혼합 반영하여 모델을 분석하는 편이, 단지 독자적인 형태의 일면적 TV 채널 단발 지표 의지에 국한되던 투사 예측 모델의 경우보다 훈련 데이터 상에서 월등히 훨씬 더 정확하게 산출 계산된다는 우리의 기존 사실 결론을 강력히 입증해 확증시켜 줍니다.

Furthermore, given that TV and radio expenditures are used as predictors, there is no point in also using newspaper spending as a predictor in the model.

나아가, TV 와 라디오 지출 내역이 예측 인자 성분들로 사용되고 있다는 점을 감안할 때 그 기반의 모델에서 추가적으로 부수적인 신문 투입 지출을 예측 인자로 굳이 사용할 필요성은 일절 없습니다.

The observant reader may wonder how RSE can increase when `newspaper` is added to the model given that RSS must decrease. In general RSE is defined as

관찰력이 뛰어난 독자라면 마땅히 RSS 가 감소해야 함에도 불구하고 막상 `newspaper` 요소가 모델 안으로 투입 탑승 부가될 때 어째서 RSE 점수 선은 오히려 자칫 상승할 수 있는지 궁금할 수 있습니다. 통상적으로 RSE 는 다음과 같이 명명 및 도출됩니다.

$$
\text{RSE} = \sqrt{\frac{1}{n-p-1} \text{RSS}} \quad (3.26)
$$

**==> picture [230 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sales<br>TV<br>Radio<br>**----- End of picture text -----**<br>

**FIGURE 3.5.** _For the_ `Advertising` _data, a linear regression fit to_ `sales` _using_ `TV` _and_ `radio` _as predictors. From the pattern of the residuals, we can see that there is a pronounced non-linear relationship in the data. The positive residuals (those visible above the surface), tend to lie along the 45-degree line, where TV and Radio budgets are split evenly. The negative residuals (most not visible), tend to lie away from this line, where budgets are more lopsided._

**FIGURE 3.5.** `Advertising` _데이터의 경우,_ `TV` _와_ `radio` _를 예측 변수로 기용하여_ `sales` _에 적합시킨 선형 회귀. 잔차의 패턴을 통해 우리는 데이터 내에 뚜렷한 비선형 관계가 있음을 알 수 있습니다. 양의 잔차(표면 위에 튀어나와 보이는 것들)는 TV 와 라디오 예산이 균일하게 분배된 일직선의 45도 기울기 선을 따라 놓여 있는 경향이 있습니다. 반면 음의 잔차(대부분 보이지 않음)는 예산이 더 심하게 한쪽으로 편중된 지점에서 이 등분선 밖으로 멀리 떨어져 놓이는 경향이 있습니다._

which simplifies to (3.15) for a simple linear regression.

이 공식은 단순 선형 회귀에 대해서 식 (3.15) 로 간소화됩니다.

Thus, models with more variables can have higher RSE if the decrease in RSS is small relative to the increase in $p$.

따라서 통상 더 많은 변수를 지닌 모델은 만약 축소된 RSS의 감소량이 증가하는 변수 개수 $p$ 에 비해 근소하고 작다면, 오히려 더 높아진 RSE 수치를 가질 수 있습니다.

In addition to looking at the RSE and $R^2$ statistics just discussed, it can be useful to plot the data.

방금 논의한 RSE 와 $R^2$ 통계를 살펴보는 것 외에도 데이터를 그려보는 그래픽 표시가 유용할 수 있습니다.

Graphical summaries can reveal problems with a model that are not visible from numerical statistics.

그래픽 요약은 수치적 통계량만으로는 결코 보이지 않는 모델의 문제점들을 명확하게 드러낼 수 있습니다.

For example, Figure 3.5 displays a three-dimensional plot of `TV` and `radio` versus `sales`.

예를 들어, 그림 3.5 는 `sales` 대비 `TV` 와 `radio` 의 입체적인 3차원 플롯을 표시합니다.

We see that some observations lie above and some observations lie below the least squares regression plane.

여기서 우리는 일부 관측치들이 최소 제곱 회귀 곡면 평면 쌍의 위쪽에 놓이거나, 또 일부 관측치들은 그 아래쪽에 머무는 현상을 봅니다.

In particular, the linear model seems to overestimate `sales` for instances in which most of the advertising money was spent exclusively on either `TV` or `radio`.

특히나 이 선형 모델은 책정된 광고 예산액 중 대부분을 오로지 한쪽(`TV` 나 `radio` 중 한 곳)으로만 배타적으로 집중 지출한 사례들에 대해 `sales` 를 지나치게 과대평가하는 것으로 보입니다.

It underestimates `sales` for instances where the budget was split between the two media.

반면, 예산 편성이 두 매체 사이로 양분되어 지출된 환경에 대해서 모델 산출은 특정 `sales` 추산을 명백히 과소평가합니다.

This pronounced non-linear pattern suggests a _synergy_ or _interaction_ effect between the advertising media, whereby combining the media together results in a bigger boost to sales than using any single medium.

이 도드라지는 비선형 패턴은 광고 매체 사이에 통계적 _시너지(synergy)_ 또는 _상호작용(interaction)_ 효과가 존재함을 강력히 암시하며, 이 작용을 통해 매체들을 결합하는 것이 여느 단일 매체를 혼자 사용하는 것보다 매출 부문에서 더 큰 상승을 초래하게 됩니다.

In Section 3.3.2, we will discuss extending the linear model to accommodate such synergistic effects through the use of interaction terms.

앞으로 올 섹션 파트 3.3.2 부분에서 우리는 상호작용 항(interaction terms) 의 사용을 통해 이와 같은 시너지 효과를 충분히 수용할 수 있도록 선형 모델의 프레임을 확장하는 방안을 논의할 것입니다.

---

## Sub-Chapters (하위 목차)


[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/trans1.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/trans1.html)

import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_3_potential_problems\4_4._outliers\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# 4. Outliers": r"""# 4. Outliers 
# 네 번째 잠재적 문제점: 이상치(Outliers)""",

    r"An _outlier_ is a point for which y_i is far from the value predicted by the outlier": 
    r"""An _outlier_ is a point for which $y_i$ is far from the value predicted by the model.
_이상치(outlier)_ 란 관측치 $y_i$ 가 모델에 의해 예측된 값에서 멀리 떨어진 점을 의미합니다.""",
    
    r"model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.":
    r"""Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.
이상치는 데이터 수집 과정에서 관측치가 잘못 기록된 경우 등 다양한 이유로 발생할 수 있습니다.""",
    
    r"104 3. Linear Regression": r"",

    r"The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier. The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier. In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept. It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit. However, even if an outlier does not have much effect on the least squares fit, it can cause other problems. For instance, in this example, the RSE is 1 _._ 09 when the outlier is included in the regression, but it is only 0 _._ 77 when the outlier is removed. Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit. Similarly, inclusion of the outlier causes the $R^2$ to decline from 0 _._ 892 to 0 _._ 805.":
    r"""The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier.
그림 3.12 의 왼쪽 패널에 있는 붉은 점(관측치 20)은 전형적인 이상치를 예시합니다.

The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier.
붉은 실선은 최소 제곱 회귀 적합선이며, 푸른 점선은 이 이상치를 제거한 뒤 얻은 최소 제곱 적합선입니다.

In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept.
이 경우 이상치를 제거하는 것은 최소 제곱선에 거의 영향을 미치지 않습니다: 기울기엔 거의 변동이 없고 절편에서 미세한 감소만을 이끌었습니다.

It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit.
이처럼 예측 변숫값이 특이하지 않은 이상치는 대체로 최소 제곱 적합에 별다른 영향을 미치지 않는 것이 전형적입니다.

However, even if an outlier does not have much effect on the least squares fit, it can cause other problems.
하지만 이상치가 당장의 회귀 최소 제곱 적합에 큰 영향을 주지 않더라도, 다른 문제들을 야기할 수 있습니다.

For instance, in this example, the RSE is $1.09$ when the outlier is included in the regression, but it is only $0.77$ when the outlier is removed.
예를 들어 이 사례에서 이상치를 회귀 묶음에 포함했을 때 잔차 표준 오차(RSE)는 $1.09$ 이지만, 제거했을 땐 $0.77$ 로 줄어듭니다.

Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit.
RSE 는 모든 신뢰 구간과 $p$-값을 계산하는 데 사용되므로, 단일 데이터 점으로 인한 이 극적인 증가는 결과적으로 모델 적합을 해석하는 데 시사점을 가질 수 있습니다.

Similarly, inclusion of the outlier causes the $R^2$ to decline from $0.892$ to $0.805$.
비슷하게, 이상치를 포함하는 것은 결괏값 $R^2$ 를 $0.892$ 에서 $0.805$ 로 감소시키는 원인이 됩니다.""",

    r"Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier. To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_ , computed by dividing each residual _ei_ by its estimated standard studentized error. Observations whose studentized residuals are greater than 3 in absoresidual lute value are possible outliers. In the right-hand panel of Figure 3.12, the outlier’s studentized residual exceeds 6, while all other observations have studentized residuals between _−_ 2 and 2.":
    r"""Residual plots can be used to identify outliers.
흔히 이상치를 식별하는 데 잔차 플롯을 사용할 수 있습니다.

In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12.
이 예제에서 그림 3.12 의 중앙 패널에 묘사된 잔차 플롯을 보면 이상치를 분명하게 확인할 수 있습니다.

But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier.
그러나 실제로는 수치가 어느 정도나 커져야 어떤 관측치를 이상치로 간주할 수 있을지 결정하기 어려울 수 있습니다.

To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_, computed by dividing each residual $e_i$ by its estimated standard error.
이러한 문제를 다루기 위해 단순히 모델의 잔차를 플롯하는 대신, 각 잔차 $e_i$ 를 해당 추정된 표준 오차로 나누어 계산한 _스튜던트화 잔차(studentized residuals)_ 표본 무리를 도해로 플로팅할 수 있습니다.

Observations whose studentized residuals are greater than 3 in absolute value are possible outliers.
통상 스튜던트화 잔차의 절댓값이 3 보다 큰 관측치는 잠재적인 이상치일 가능성이 큽니다.

In the right-hand panel of Figure 3.12, the outlier's studentized residual exceeds 6, while all other observations have studentized residuals between -2 and 2.
그림 3.12 오른쪽 국면을 보면 이상치의 스튜던트화 잔차 치수는 6 을 벗어나는 반면, 다른 모든 관측치는 -2 와 2 사이 대역 범위 내에 있습니다.""",

    r"studentized": r"",
    r"absoresidual lute": r"absolute",

    r"If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation. However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.":
    r"""If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation.
만약 이상치가 데이터 수집 측면이나 단순 기록상의 오류로 인해 초래된 것이라고 확신한다면, 한 가지 제일 쉬운 해결책은 해당 관측치를 아예 삭제해 버리는 조치입니다.

However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.
그러나 예측 변수가 누락된 경우처럼, 이상치는 되려 전반적인 모델 자체의 결함을 일러주는 결함 지표일 수도 있으므로 주의를 기울여야 합니다.""",

    r"5. High Leverage Points": r"""# 5. High Leverage Points
# 다섯 번째 잠재적 문제점: 높은 레버리지(High Leverage) 점""",

    r"We just saw that outliers are observations for which the response y_i is unusual given the predictor x_i . In contrast, observations with _high leverage_ high have an unusual value for x_i . For example, observation 41 in the left-hand":
    r"""We just saw that outliers are observations for which the response $y_i$ is unusual given the predictor $x_i$.
방금 전 우리는 이상치가 예측 변수 $x_i$ 대비 비정상적으로 튀는 관측 응답치 $y_i$ 를 가진 관측 사항임을 살펴보았습니다.

In contrast, observations with _high leverage_ have an unusual value for $x_i$.
이와 대조적으로 _높은 레버리지(high leverage)_ 를 가진 관측치들은 오히려 예측 변수 $x_i$ 자체가 아주 기이한 값을 품고 있습니다.

For example, observation 41 in the left-hand""",

    r"leverage": r"",

    r"3.3 Other Considerations in the Regression Model 105": r"",

    r"panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high leverage observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high leverage observations.":
    r"""panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations.
그림 3.13 왼쪽 패널 면의 관측치 범주 41번 무리는 그것의 예측 변숫값이 여타 관측치들에 비해 크다는 관점에서 높은 레버리지를 갖습니다.

(Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.)
(참고로 그림 3.13 에 전시된 데이터 그룹은 그림 3.12 배열과 동일하지만, 고 레버리지 관측치가 단 하나 추가된 상태라는 점을 유의하십시오.)

The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed.
제시된 붉은 실선은 데이터 전체에 대해 도출된 최소 제곱 적합선이며, 푸른 점선은 이 문제의 관측치 단편 41을 제거한 뒤 생산된 적합선입니다.

Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier.
그림 3.12 와 3.13 의 좌측 패널 전경을 상호 대조해 봄으로써, 우리는 고 레버리지 관측치를 제거하는 조치가 단지 이상치를 떨어내는 비교 조치보다 일괄된 최소 제곱선 궤도상에 훨씬 강한 실질적 타격 영향력(substantial impact)을 마구 발휘한다는 사실을 관찰할 수 있습니다.

In fact, high leverage observations tend to have a sizable impact on the estimated regression line.
실상, 높은 레버리지 속성의 관측치들은 향후 추정치로 도출되는 산출 회귀선 전체 양태에 아주 덩치 크고 심대한(sizable) 영향을 미치는 경향이 있습니다.

It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit.
불과 몇몇 조각 관측 데이터에 의해서만 최소 제곱 통계선이 크게 좌지우지 영향을 받는다는 것은 심각한 우려 사안인데, 그 까닭은 이 점들에 숨겨진 모종의 문제가 발생하면 자칫 전체 적합선 구조 단면 자체를 무효화(invalidate)할 소지가 농후하기 때문입니다.

For this reason, it is important to identify high leverage observations.
바로 이러한 연유 때문에, 높은 레버리지 관측치를 제대로 알아보고 식별해 내는 것은 통계 과정에서 몹시 중요합니다.""",

    r"In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$. Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.":
    r"""In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations.
단순히 선형 회귀 구도에서는, 예측 변수 치수가 보통 평균 범위 밖에 뚝 떨어진 관측치들을 쉽게 찾아볼 수 있기 때문에 고 레버리지 관측점을 비교적 쉽게 식별해 낼 수 있습니다.

But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor's values, but that is unusual in terms of the full set of predictors.
하지만 이와 달리 수많은 동반 예측 변수가 혼재된 다중 선형 회귀에서는, 각각 개별 예측 단위 변숫값의 일반적 척도 내에는 안착하면서도 다양한 전체 예측 변수들 측면에서 볼 땐 아주 변칙적으로 특이한(unusual) 관측치가 도출되어 존재할 가망이 꽤 열려 있습니다.

An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$.
그림 3.13 중앙 패널 국면에 단적인 일례가 묘사되어 있는데, 변수 $X_1$ 및 인자 $X_2$ 로 짜인 데이터 묶음 세트에 관한 것입니다.

Most of the observations' predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range.
대다수 관측 타점의 변숫값들은 저 파란 점선 타원(ellipse) 구조 안에 안정적으로 포섭되어 밀집하는 반면, 요주의 빨간 표본 관측점만 유유히 이 궤도 띠 허용 범위를 벗어나(well outside) 널뛰듯 동떨어져 있습니다.

But neither its value for $X_1$ nor its value for $X_2$ is unusual.
막상 부분적인 그 빨간 점의 개별 수치 $X_1$ 값도, 그리고 개별적 그 $X_2$ 지표 잣대 단위도 딱히 개별적으로는 이색적이거나 특이하지 않습니다.

So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point.
단일 관점만 고집하여 우리가 $X_1$ 측면이나 기껏 $X_2$ 요소만을 검토한다면, 우리는 이렇게 숨어버린 고 레버리지 도출 점을 인지(notice)하는 데 여차 실패하고 말 것입니다.

This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.
이러한 문제성 요건은 2개 이상의 많은 동반 예측 변수를 가진 다변 복수 다중 회귀 설정일수록 그 맹점이 더욱 짙어지고 확연 두드러지는데(more pronounced), 이유는 사실 이렇게 방대한 체제 변동 후엔 데이터 집단의 모든 가용 차원(dimensions) 지표 단위들을 그림 단위 플롯 하나에 일목요연하고 단순하게 동시 다발적으로(simultaneously) 그릴 방법(simple way)이 없기 때문입니다.""",

    r"In order to quantify an observation’s leverage, we compute the _leverage statistic_ . A large value of this statistic indicates an observation with high leverage leverage. For a simple linear regression,":
    r"""In order to quantify an observation's leverage, we compute the _leverage statistic_.
관측치가 지닌 레버리지를 정량 수치로 계량화고자, 모델에서는 주로 해당 관측 지점의 _레버리지 통계량(leverage statistic)_ 을 연계 계산합니다.

A large value of this statistic indicates an observation with high leverage.
이 통계 치수가 일정 이상으로 높다는 것은 해당 항목 관측치가 고 레버리지 속성을 수반함을 지표로써 뒷받침 시사합니다.

For a simple linear regression,""",

    r"statistic ": r"",

    r"106 3. Linear Regression": r"",

    r"It is clear from this equation that _hi_ increases with the distance of x_i from ¯ _x_ . There is a simple extension of _hi_ to the case of multiple predictors, though we do not provide the formula here. The leverage statistic _hi_ is always between 1 _/n_ and 1, and the average leverage for all the observations is always equal to ( $p$ + 1) _/n_ . So if a given observation has a leverage statistic that greatly exceeds ( $p$ +1) _/n_ , then we may suspect that the corresponding point has high leverage.":
    r"""It is clear from this equation that $h_i$ increases with the distance of $x_i$ from $\bar{x}$.
당면한 이 수식에서 한눈에 보여주듯, $h_i$ 지표는 $x_i$ 가 전체 집단 평균 수치 $\bar{x}$ 로부터 멀어지는 이격 거리 변동 치수가 커짐에 발맞춰 동일하게 따라서 상승 증가합니다(increases).

There is a simple extension of $h_i$ to the case of multiple predictors, though we do not provide the formula here.
다만 여러 예측 변수가 난립하는 다변 다중 예측 변수들(multiple predictors)에 이러한 공식 수치 $h_i$ 를 확장 치환 연장해 수용하는 가벼운 단순 확장 도출 방식도 응당 존재하지만, 이곳 지면에선 생략하기로 합니다.

The leverage statistic $h_i$ is always between $1/n$ and $1$, and the average leverage for all the observations is always equal to $(p + 1)/n$.
통상 도출되는 레버리지 통계량 잣대 $h_i$ 치수는 언제나 일정하게 범주 $1/n$ 이란 바닥 한계치부터 최대 상한 장벽인 $1$ 테두리 내 국면에 속박 안착 국한되며, 게다가 전체 관측치 집단 덩이를 상대로 평균 낸 레버리지 총합 평균은 항상 비율에 맞게 $(p + 1)/n$ 이란 궤도 수준 방정식 수위에 예외 없이 매양 동일 동등 합치 기결 귀속됩니다(equal to).

So if a given observation has a leverage statistic that greatly exceeds $(p + 1)/n$, then we may suspect that the corresponding point has high leverage.
그러므로, 어느 주축 관측치가 평균 척도 $\bar{x}$ 지표에 부가된 $(p + 1)/n$ 수의 수준을 과도하게 대폭 초과 능가하는(greatly exceeds) 통계치 레버리지 기운을 과시한다 칠 때면 우리는 당연 그 해당 관측점(corresponding point) 부위가 필경 필시 무척이나 드높은 성향의 고 레버리지를 내재해 가진 소지 요소라 강하게 합당 의심(suspect)해 볼 수 있습니다.""",

    r"The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus _hi_ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.":
    r"""The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus $h_i$ for the data in the left-hand panel of Figure 3.13.
그림 3.13 의 우측 패널은 동일한 데이터를 바탕으로 스튜던트화 잔차와 $h_i$ 를 대조하여 그린 플롯을 제공합니다.

Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual.
특히 대상 관측치 41은 매우 높은 레버리지 통계량과 높은 스튜던트화 잔차를 모두 가지고 있어 뚜렷하게 눈에 띕니다.

In other words, it is an outlier as well as a high leverage observation.
다시 말해, 이것은 이상치임과 동시에 높은 레버리지를 지닌 관측치이기도 합니다.

This is a particularly dangerous combination!
이것은 통계적으로 특히 위험한 조합입니다!

This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.
더불어 이 플롯은 왜 관측치 20 이 그림 3.12 에서의 최소 제곱 적합선에 큰 영향을 끼치지 못했는지 그 이유를 분명히 보여줍니다: 그 관측치는 낮은 레버리지를 가졌기 때문입니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

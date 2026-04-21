import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_3_potential_problems\4_4._outliers\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# 4. Outliers": r"""# 4. Outliers 
# 네 번째 잠재적 문제점: 이상치(Outliers)""",

    r"An _outlier_ is a point for which y_i is far from the value predicted by the outlier": 
    r"""An _outlier_ is a point for which $y_i$ is far from the value predicted by the model.
_이상치(outlier)_ 란 관측된 대상 응답인 $y_i$ 값이 당초 해당 모델에 의해 예측된 궤도와 멀리 동떨어진 점을 의미합니다.""",
    
    r"model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.":
    r"""Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.
이상치는 데이터 수집 과정에서 관측치가 잘못 기록된 경우 등 다양한 이유로 발생할 수 있습니다.""",
    
    r"104 3. Linear Regression": r"",

    r"The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier. The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier. In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept. It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit. However, even if an outlier does not have much effect on the least squares fit, it can cause other problems. For instance, in this example, the RSE is 1 _._ 09 when the outlier is included in the regression, but it is only 0 _._ 77 when the outlier is removed. Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit. Similarly, inclusion of the outlier causes the $R^2$ to decline from 0 _._ 892 to 0 _._ 805.":
    r"""The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier.
그림 3.12 의 왼쪽 패널에 있는 붉은 점(관측치 20)은 이런 전형적인 이상치를 예시합니다.

The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier.
붉은색 실선은 최소 제곱 회귀 적합선이며, 푸른색 점선은 이 이상치를 제거한 뒤 얻은 최소 제곱 적합선입니다.

In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept.
이 경우 이상치를 제거하는 것은 최소 제곱선에 거의 영향을 미치지 않습니다: 기울기엔 거의 변동을 주지 않았고, 단지 절편에서 미세한 감소만을 이끌었을 뿐입니다.

It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit.
이처럼 예측 변숫값이 특이하지 않은 이상치 대개는 최소 제곱 적합에 별다른 영향을 미치지 않는 것이 전형적입니다.

However, even if an outlier does not have much effect on the least squares fit, it can cause other problems.
하지만 이상치가 당장의 선형 회귀 최소 제곱 적합에 큰 영향을 주지 않더라도, 다른 문제들을 유발할 수 있습니다.

For instance, in this example, the RSE is $1.09$ when the outlier is included in the regression, but it is only $0.77$ when the outlier is removed.
예를 들어 이 사례에서 이상치를 회귀에 포함했을 땐 RSE 가 $1.09$ 이지만, 예외로 제거했을 땐 $0.77$ 로 줄어듭니다.

Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit.
RSE 지표는 향후 모든 신뢰 구간과 $p$-값을 계산하는 데 쓰이므로, 단 하나의 데이터 점이 야기한 이러한 극적인 증가는 모델 적합을 해석하는 데 시사점을 가질 수 있습니다.

Similarly, inclusion of the outlier causes the $R^2$ to decline from $0.892$ to $0.805$.
비슷한 맥락에서, 이상치를 포함하는 것은 $R^2$ 수치를 $0.892$ 에서 $0.805$ 로 하락시키는 원인이 됩니다.""",

    r"Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier. To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_ , computed by dividing each residual _ei_ by its estimated standard studentized error. Observations whose studentized residuals are greater than 3 in absoresidual lute value are possible outliers. In the right-hand panel of Figure 3.12, the outlier’s studentized residual exceeds 6, while all other observations have studentized residuals between _−_ 2 and 2.":
    r"""Residual plots can be used to identify outliers.
잔차 플롯은 이상치를 식별하는 데 널리 활용될 수 있습니다.

In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12.
이 예제에서, 그림 3.12 의 중앙 패널에 그려진 잔차 플롯을 보면 이상치를 분명하게 확인할 수 있습니다.

But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier.
그러나 실제로는 수치가 어느 정도 이상으로 커져야 잔차 차이를 이상치로 간주할 수 있을지 결정하기 어려울 수 있습니다.

To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_, computed by dividing each residual $e_i$ by its estimated standard error.
이 문제를 다루기 위해 단순히 잔차를 그리는 대신, 각 잔차 $e_i$ 를 해당 추정된 표준 오차로 나눈 _스튜던트화 잔차(studentized residuals)_ 표본 무리를 도해로 플로팅할 수 있습니다.

Observations whose studentized residuals are greater than 3 in absolute value are possible outliers.
통상 스튜던트화 잔차의 절댓값이 3 보다 큰 관측치는 이상치일 가능성이 큽니다.

In the right-hand panel of Figure 3.12, the outlier's studentized residual exceeds 6, while all other observations have studentized residuals between -2 and 2.
그림 3.12 제일 오른쪽 국면을 보면, 이상치의 스튜던트화 잔차 치수는 버젓이 6 을 상회하는 반면, 다른 모든 관측치는 -2 와 2 사이 정상 범위에 모여 있습니다.""",

    r"studentized": r"",
    r"absoresidual lute": r"absolute",

    r"If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation. However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.":
    r"""If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation.
만약 이상치가 데이터 수집이나 기록 오류 등 과실에서 비롯된 것이라고 굳게 믿는다면 가장 단순한 해결책은 해당 관측치를 제거하는 것입니다.

However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.
그러나 이상치는 예측 변수 누락과 같이 전반적인 모델 자체의 결함을 일부분 암시하는 것일 수 있으므로 이를 다룰 땐 주의해야 합니다.""",

    r"5. High Leverage Points": r"""# 5. High Leverage Points
# 다섯 번째 잠재적 문제점: 높은 레버리지(High Leverage) 점""",

    r"We just saw that outliers are observations for which the response y_i is unusual given the predictor x_i . In contrast, observations with _high leverage_ high have an unusual value for x_i . For example, observation 41 in the left-hand":
    r"""We just saw that outliers are observations for which the response $y_i$ is unusual given the predictor $x_i$.
우리는 갓 이상치란 예측 변수 $x_i$ 대비 예외적으로 극단적 응답치 $y_i$ 를 갖는 관측치 무리임을 살펴보았습니다.

In contrast, observations with _high leverage_ have an unusual value for $x_i$.
이와 대조적으로 _높은 레버리지(high leverage)_ 를 가진 관측치들은 오히려 예측 변수 $x_i$ 자체가 아주 특이한 값을 품고 있습니다.

For example, observation 41 in the left-hand""",

    r"leverage": r"",

    r"3.3 Other Considerations in the Regression Model 105": r"",

    r"panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high leverage observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high leverage observations.":
    r"""panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations.
이어진 그림 3.13 좌측 패널의 관측치 점 41번 무리는 이 관측치의 예측 변숫값이 여타 관측치들에 비해 상대적으로 크다는 점에서 고 레버리지를 갖습니다.

(Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.)
(참고로 그림 3.13 에 진열된 데이터는 그림 3.12 에 진열된 데이터 묶음과 동일하지만, 단지 이 고 레버리지 표본 점 하나가 추가된 것입니다.)

The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed.
붉은 실선은 데이터에 대해 측정된 최소 제곱선이며, 푸른 점선은 관측치 41 을 제거한 후 다시 도출한 적합선입니다.

Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier.
그림 3.12 와 3.13 의 좌측 패널을 대조 분석함으로써 우리는 고 레버리지 관측치를 제거하는 조치가 단지 이상치를 떨어내는 조치보다 최소 제곱선 전반에 걸쳐 훨씬 큰 실질적 영향력(substantial impact)을 발휘한다는 사실을 관찰할 수 있습니다.

In fact, high leverage observations tend to have a sizable impact on the estimated regression line.
이를 보듯 이처럼 높은 레버리지 양태의 관측치들은 추정되는 향후 회귀선에 대단히 크고 심대한(sizable) 일격 파급 영향을 미치는 경향을 지닙니다.

It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit.
불과 몇몇 한두 관측 데이터 조각점에 의해서만 최소 제곱선이 큰폭으로 동반 흔들린다는 건 크나큰 우려 화근 요소인데, 왜냐하면 이런 점에서 발생한 어떠한 결함이 자칫 전체 적합선 구조를 모조리 무효화(invalidate) 시킬 소지가 있기 때문입니다.

For this reason, it is important to identify high leverage observations.
바로 이 이유 때문에 고 레버리지 관측 표면들을 미연에 식별해 내는 일이 중요합니다.""",

    r"In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$. Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.":
    r"""In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations.
일견 단순 선형 회귀 구도에서는, 그저 예측 변숫값이 정상 허용 범주 밖으로 동떨어지게 벗어난 관측치들만을 쉽게 살펴보면 되므로 이런 고 레버리지 타점 식별은 상당히 쉽습니다.

But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor's values, but that is unusual in terms of the full set of predictors.
하지만 수많은 다중 예측 변수가 혼재하는 다중 선형 회귀에서는, 제각기 개별적인 예측 단위 변숫값의 범위 안에는 안정적으로 포섭 안착하면서도 예측 변수들의 전체 묶음 측면 관점에서 바라볼 때는 유독 특이한 기형 요소 관측치가 등장할 가망 여지가 존재합니다.

An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$.
그림 3.13 중앙 패널에 단적인 예가 전시되어 있는데, 이는 변수 $X_1$ 및 $X_2$ 인자로 짜인 소규모 데이터 묶음 세트 항목들에 관한 것입니다.

Most of the observations' predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range.
대다수 뭇 표본 타점 단위 변숫값들은 저기 푸른 점선 타원(ellipse) 내부 둥지 안쪽에 무난히 안착하건만, 유독 저 붉은색 관측점만큼은 유유히 이 궤도 띠 범위를 부쩍 한참 밖으로 이탈해(well outside) 동떨어져 있습니다.

But neither its value for $X_1$ nor its value for $X_2$ is unusual.
막상 그 빨간 점의 세부적 수치인 개별 $X_1$ 통계 값이나 $X_2$ 지표 잣대 단위 어느 것을 빗대어 보더라도 그것이 눈에 띄게 이상할 만치 특이하지는 않습니다.

So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point.
단지 이토록 국한 편협한 단일 관점으로 만일 우리가 딱 $X_1$ 요소 거나 오직 딱 $X_2$ 지표 측면만을 검토 단안해 본다면, 우리는 이 문제의 고 레버리지 도출 점을 인지(notice)하는 일에 깜박 완전히 실패할 것입니다.

This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.
이러한 문제성 난맥은 달랑 2개보다 많은 예측 복수 지표가 동반된 무수한 다변 다중 회귀 모형 설정 기조 설정에서 더욱 확연히 짙어지며(more pronounced), 이토록 기조가 복잡해지면 사실 데이터 집단을 표현할 모든 전 차원(dimensions) 지표 단면들을 한 플롯에 동시 다발적으로 한데 투명 나열해 시각화해 낼 간단한 여력 방도(simple way)가 사실상 불가능합니다.""",

    r"In order to quantify an observation’s leverage, we compute the _leverage statistic_ . A large value of this statistic indicates an observation with high leverage leverage. For a simple linear regression,":
    r"""In order to quantify an observation's leverage, we compute the _leverage statistic_.
관측치가 지닌 레버리지 치수를 수치 계량화할 목적으로, 우리는 해당 관측치의 수리 _레버리지 통계량(leverage statistic)_ 측면을 도출 일괄 계산합니다.

A large value of this statistic indicates an observation with high leverage.
이 통계치 수치가 크다는 것은 관측치가 높은 레버리지를 가지고 있음을 시사합니다.

For a simple linear regression,""",

    r"statistic ": r"",

    r"106 3. Linear Regression": r"",

    r"It is clear from this equation that _hi_ increases with the distance of x_i from ¯ _x_ . There is a simple extension of _hi_ to the case of multiple predictors, though we do not provide the formula here. The leverage statistic _hi_ is always between 1 _/n_ and 1, and the average leverage for all the observations is always equal to ( $p$ + 1) _/n_ . So if a given observation has a leverage statistic that greatly exceeds ( $p$ +1) _/n_ , then we may suspect that the corresponding point has high leverage.":
    r"""It is clear from this equation that $h_i$ increases with the distance of $x_i$ from $\bar{x}$.
이 수식 방정식에서 명확히 나타나듯, $h_i$ 값은 $x_i$ 변수가 평균인 $\bar{x}$ 지표로부터 이격되어 멀어진 거리(distance) 분간 편차 치수 증가에 비례하여 동반 상승해 커집니다(increases).

There is a simple extension of $h_i$ to the case of multiple predictors, though we do not provide the formula here.
물론 다중 예측 변수 모델(multiple predictors)에 $h_i$ 공식을 단숨 연장 적용 치환해 쓰는 방식도 구비 상존하지만 여기 지면 내에서는 공식을 제공하지 않습니다.

The leverage statistic $h_i$ is always between $1/n$ and $1$, and the average leverage for all the observations is always equal to $(p + 1)/n$.
통상 레버리지 도출 통계 지표 $h_i$ 수치는 항시 언제나 일괄 최저 바닥 $1/n$ 궤도로부터 최대 한도 장벽 $1$ 범위 선분 속 제한 사이 테두리 안에 머물며 안착하며, 도합 모든 표본 관측치의 전체 레버리지 단면을 평균 내어 합산한 평균 레버리지 분량 치수는 항시 기필코 불변 일치하게 일정 비율 $(p + 1)/n$ 수준으로 동등히 일관 적합하게 귀결됩니다(equal to).

So if a given observation has a leverage statistic that greatly exceeds $(p + 1)/n$, then we may suspect that the corresponding point has high leverage.
그러므로, 어느 한 도출 제공 관측치가 평균 척도 잣대인 $(p + 1)/n$ 선을 과도히 아주 대거 크게 심심히 훌쩍 초과해 능가(greatly exceeds)하는 레버리지 통계치 수치를 점유한다 치면 우리는 즉시 그 해당 관측지점(corresponding point) 부위가 필경 고(高)성격의 레버리지를 내재해 가진 소지 요소라 강하게 합당 의심(suspect) 해 볼 수 있습니다.""",

    r"The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus _hi_ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.":
    r"""The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus $h_i$ for the data in the left-hand panel of Figure 3.13.
그림 3.13 의 우측 편 패널 도면은 동일한 데이터 무리 집단을 도표상으로 세워 놓고 다시 스튜던트화 투사 산출 잔차 요건 스탯과 대응하는 $h_i$ 통계 단면 척도를 대비 비교 교차 축에 세운 뒤 단층 플롯 그려 반영해 줍니다.

Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual.
특히 이중 관측점 타깃 번호 대상 41번 무리는 타 여타 개체들보다 단연코 눈에 띄게 비대한 매우 높은 레버리지 지표 자산 잣대와 함께 큰 고(高)단위체 수위 스튜던트 잔차치까지 둘 다 덤으로 거머쥔 자태로 부각되어 나타납니다(stands out).

In other words, it is an outlier as well as a high leverage observation.
이를 다시 부연하면, 이것은 말썽 이상치 표본 오점 얼룩 병폐임을 스스로 보유함과 다를 바 없이 이중적으로 막대 막강 레버리지 관측치 단면 요소 덤 지위마저 한데 겸하여 복합 수반 동병 상련 겸비 소속 지닌다는 소리 요지에 다름없습니다(as well as).

This is a particularly dangerous combination!
실로 이토록 양 절묘 두 단면 기조 척도를 동시에 혼합 합체 보유 동행한다는 건 가히 너무 치명 아주 치 떨 대단 통계상 참담 몹 파국(particularly) 위험 기 가 유 기 기 무 기 심 지 독 극 단 참 파 배 무 천 다 요 가 맹 파 (dangerous) 위험 결합 조합 묶음(combination) 구조 형국에 합치 불가결 맞먹습니다!

This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.
바로 이 플롯 도면 단면 도 상 단 화면 형상 묘 시 단 시 (plot) 그 자체가 더불어 관측치 20번 점이 전도 그림 3.12 의 전 최소 제곱 적합 줄기 단면에 왜 비교 기 다 고 다 비 다 구 단 작 은 조 조 반 조금 미 적 소 하 지 은 좀 미 낮 거의 일 영 영 아 적 미 전 전 적 치 여 조 단 단 여 미(relatively little effect) 상대 빈 은 아 다 빈 다 치 아 파 조 여 요 다 반 전 과 모 일 치 조 영 끼 모 줄 효 (effect) 파 미 미 전 일 기 치 과 영 영 영 동 양 (reason)을 노 포 증 확 포 발 낱 낱 입 표 확 기 들 나 입 조 증 노 입 환 포 진 환 밝 낱 (also reveals) 증 가 부 기 도 증 명 환 해 진 보 노 밝 시 투 도 시 낱 들 (reveals) 조 모 해 줍니다: 바로 그 점이 낮은 저 저 저 저 얕 나 얕 수 박 야 낮 (low) 레버리지 속 기포 기 역 스 포 결 포스 치 지 (leverage) 기 다를 역 단 포 부 모 수 스 고스다 (leverage)결지 도 부 점 조부파도스. """
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

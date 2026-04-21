import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_3_potential_problems\4_4._outliers\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# 4. Outliers": r"""# 4. Outliers 
# 네 번째 잠재적 문제점: 이상치(Outliers)""",

    r"An _outlier_ is a point for which y_i is far from the value predicted by the outlier": 
    r"""An _outlier_ is a point for which $y_i$ is far from the value predicted by the model.
_이상치(outlier)_ 란 관측된 대상 응답인 $y_i$ 값이 당초 해당 모델에 의해 예측된 궤도와 아주 멀리 동떨어진 별개의 점을 의미합니다.""",
    
    r"model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.":
    r"""Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.
이상치는 데이터 수집 과정에서 특정 관측치가 잘못 기록된 경우 등 아주 다양하고 다채로운 연유로 속출할 수 있습니다.""",
    
    r"104 3. Linear Regression": r"",

    r"The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier. The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier. In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept. It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit. However, even if an outlier does not have much effect on the least squares fit, it can cause other problems. For instance, in this example, the RSE is 1 _._ 09 when the outlier is included in the regression, but it is only 0 _._ 77 when the outlier is removed. Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit. Similarly, inclusion of the outlier causes the $R^2$ to decline from 0 _._ 892 to 0 _._ 805.":
    r"""The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier.
그림 3.12 의 왼쪽 패널에 있는 붉은 점(관측치 20)은 이런 전형적인 이상치를 예시합니다.

The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier.
붉은색 실선은 최소 제곱 회귀 적합선이며, 푸른색 점선은 이 이상치를 제거한 뒤 얻은 최소 제곱 적합선입니다.

In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept.
이 경우 이상치를 제거하는 것은 최소 제곱선에 거의 영향을 미치지 않습니다: 기울기엔 전혀 변동을 주지 않았고, 단지 절편에서 미세한 감소만을 이끌었을 뿐입니다.

It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit.
이처럼 예측 변숫값이 특이하지 않은 이상치 대개는 최소 제곱 적합에 별다른 영향을 가하지 못하는 게 전형적입니다.

However, even if an outlier does not have much effect on the least squares fit, it can cause other problems.
허나, 이상치가 당장의 회귀 최소 제곱 적합에 영향을 끼치지 않는다 해도, 다른 문제들을 야기할 수 있습니다.

For instance, in this example, the RSE is $1.09$ when the outlier is included in the regression, but it is only $0.77$ when the outlier is removed.
일례로 이 사례에서, 이상치를 회귀 묶음에 포함했을 땐 RSE 가 $1.09$ 에 달하지만, 제외했을 땐 $0.77$ 로 떨어집니다.

Since the RSE is used to compute all confidence intervals and $p$-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit.
이 RSE 지표는 향후 모든 신뢰 구간과 $p$-값을 계산하는 데 사용되므로, 일개 데이터 한 점이 불러온 이런 극적인 상승은 파급 효과를 미쳐 결과적으로 모델의 의미 해석 전반에 영향을 발휘할 수밖에 없습니다.

Similarly, inclusion of the outlier causes the $R^2$ to decline from $0.892$ to $0.805$.
비슷한 맥락에서, 이상치를 포함하는 것은 $R^2$ 수치를 $0.892$ 에서 $0.805$ 로 하락시키는 원인이 됩니다.""",

    r"Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier. To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_ , computed by dividing each residual _ei_ by its estimated standard studentized error. Observations whose studentized residuals are greater than 3 in absoresidual lute value are possible outliers. In the right-hand panel of Figure 3.12, the outlier’s studentized residual exceeds 6, while all other observations have studentized residuals between _−_ 2 and 2.":
    r"""Residual plots can be used to identify outliers.
흔히 이런 이상치를 식별할 땐 잔차 플롯을 사용합니다.

In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12.
이 예제에선, 그림 3.12 의 중앙 패널에 묘사된 잔차 플롯 안에서 이상치 하나가 선명하게 보입니다.

But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier.
하지만 기실 실무 현장에서는 잔차 편차 수위가 도무지 얼마나 커야 비로소 특정 관측 지표점을 이상치로 분류 간주할 수 있을지 그 잣대를 분간하기 여간 혼란스럽지 않습니다.

To address this problem, instead of plotting the residuals, we can plot the _studentized residuals_, computed by dividing each residual $e_i$ by its estimated standard error.
이 문제를 다루기 위해, 단순 잔차 대신 각 잔차 $e_i$ 값을 추정된 표준 오차로 나누어 산출한 일명 _스튜던트화 잔차(studentized residuals)_ 표본 무리를 도해 플롯해 볼 수 있습니다.

Observations whose studentized residuals are greater than 3 in absolute value are possible outliers.
통상 스튜던트화 잔차의 절댓값이 '3' 보다 큰 관측치 요소라면 이들은 족히 잠재적 이상치 분파 표본일 가능성이 농후합니다.

In the right-hand panel of Figure 3.12, the outlier's studentized residual exceeds 6, while all other observations have studentized residuals between -2 and 2.
그림 3.12 제일 오른쪽 국면을 보면, 이상치의 스튜던트화 잔차 치수는 버젓이 '6'을 초과하며, 반면 다른 모든 관측치는 -2 와 2 사이 대역 범위 속 정상 궤도에 머물러 있습니다.""",

    r"studentized": r"",
    r"absoresidual lute": r"absolute",

    r"If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation. However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.":
    r"""If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation.
만약 이상치 발생 연유가 데이터 수집이나 엉뚱한 수기 기록 오류 등 과실에서 비롯된 거라 굳게 믿는다면 가장 단순한 해결책은 그 관측치를 아예 제거해 버리는 조치일 것입니다.

However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.
그러나 이상치가 실은 예측 변수 누락 같은 전반 모델 구성 자체의 결함을 일부분 암시 및 보여 주는 경고성 반증 지표일 수도 있으므로, 함부로 다룰 땐 주의가 요망됩니다.""",

    r"5. High Leverage Points": r"""# 5. High Leverage Points
# 다섯 번째 잠재적 문제점: 높은 레버리지(High Leverage) 점""",

    r"We just saw that outliers are observations for which the response y_i is unusual given the predictor x_i . In contrast, observations with _high leverage_ high have an unusual value for x_i . For example, observation 41 in the left-hand":
    r"""We just saw that outliers are observations for which the response $y_i$ is unusual given the predictor $x_i$.
우리는 갓 이상치란 기껏해야 예측 변수 $x_i$ 조건 잣대가 평이하더라도 예외적으로 극단 응답치 $y_i$ 를 갖는 관측치 무리임을 살펴보았습니다.

In contrast, observations with _high leverage_ have an unusual value for $x_i$.
이와 대조적으로 _높은 레버리지(high leverage)_ 단면을 동반한 관측치들은 오히려 예측 변수 $x_i$ 파편 자체가 아주 특이한 돋보이는 기이 특성값을 품고 있습니다.

For example, observation 41 in the left-hand""",

    r"leverage": r"",

    r"3.3 Other Considerations in the Regression Model 105": r"",

    r"panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high leverage observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high leverage observations.":
    r"""panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations.
이어진 그림 3.13 패널의 관측치 점 41번 무리는 이른바 고(高) 레버리지 속성을 띠는데, 이는 예측 변숫값이 여타 다른 평이 관측치들에 비해 유독 비대한 편이어서 그렇습니다.

(Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.)
(참고로 그림 3.13 에 전시된 데이터 세트는 앞 그림 3.12 의 묶음 자체와 동일하지만, 단지 이 고 레버리지 표본 점 하나가 추가로 얹어 더해진 상태입니다.)

The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed.
붉은 실선은 전체 데이터에 적용한 당초의 최소 제곱선이며, 푸른색 이음 점선은 요주의 대상 관측치 단편 41 번을 단숨 모조리 제외 제거해낸 뒤 다시 도출한 적합선입니다.

Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier.
우리는 두 그림 3.12 며 3.13 의 좌측 단면을 상호 대조 분석해 봄으로써 뼈저린 교훈을 얻는데, 바로 고(高) 레버리지 관측 파편 요소를 하나 뽑아 적결 제거해 버리는 조치 파급력이 고작 일반 이상치 점 하나 따위를 덜어 꺼내 도려내는 행위보다 최소 제곱 선 궤도 전반에 걸쳐서 훨씬 대단하고 중차대하며 실질적인 타격 영향력(substantial impact)을 마구 퍼붓고 가해댄다는 절대적 사실 대목입니다.

In fact, high leverage observations tend to have a sizable impact on the estimated regression line.
이를 보듯 실상 이처럼 일관된 높은 특성 레버리지 양태의 일련 관측치들은 향후 추산 산출 모의 될 다분 예측 회귀선 전체 줄기 전락 전면에 대단히 과도 막대 거대한 심대(sizable) 일격 충격 타격 파급 영향 충격 여파를 빈번 쏟아붓고 흩뿌려 가할 농후 요소 경향 잠재 소지를 머금 유지 품어 고루 갖춥니다.

It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit.
고작 단 둘 서너 개 불과 한두 낱개 무리 관측 데이터 조각점에 의해서만 의존하여 당면 핵심 최소 제곱 회귀 단면 전체가 널 뛸 듯이 막대하게 덩달 춤추 흔들 변동 수난 곤경 노출되는 처지 형국은 크나큰 위기 파문 우려 염려 소스 구실 골칫 화근 요소이기 직면 마련인데, 연유인즉 이런 일개 한둘 요인 부위가 몰래 잠복 감내 품은 어처구니 부실 결단력 문제 소지 결함 내력 모종 오류 여파 단면 하나 탓에 자칫 우연히 결과적으로 아주 온전 공들 막대 짠 일견 모의 대단위 전 단합 묶음 적합 분석 단면 숲을 일괄 전체 덩이 전면 모조 무용 무효 체제로 무효화(invalidate) 조변석개 오염 완전히 파탄시켜 일순 뒤흔들어 모조리 엎어 덮어 버릴 몹시 위중 악재 징표 위험 다분 오차 낭패 가능 우려가 아주 몹시 농후히 도사려 자리하기 까닭 분수령입니다.

For this reason, it is important to identify high leverage observations.
바로 이 절대 지배 막강 우려 위험 파급 조달 무효 파생 발단 연유 까닭 때문에라도 향후, 이들을 사전 방비 예방 감식 차원 명목 삼아 초기 단계 구별 식별해 구별 가리고 요주의 고(高) 레버리지 특이 도출 관측 표면 인자 군들을 파악 색출 일일 검열 색인 검토 분간 인지 조처 대처하는 건 도합 막대 통계 진단 사안 아주 각고 극의 핵심 중요 아주 중추 중차 요긴 몹시 사안 중요 필요합니다.""",

    r"In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor’s values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$. Most of the observations’ predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_1$ nor its value for $X_2$ is unusual. So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.":
    r"""In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations.
일견 평이한 단순 선형 회귀 구도에서는, 그저 주변 타 일반 관측치들의 정상 허용 범주 잣대 바깥으로 동떨어지게 튀어나간 예측 변숫값 수치를 품은 관측치들만을 조사해 보면 되므로 이런 고(高) 레버리지 관측군 타점 식별은 그닥 어렵지 않습니다.

But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor's values, but that is unusual in terms of the full set of predictors.
하지만 수많은 다중 예측 변수가 혼재하는 다중 선형 회귀 모의 틀 판국에서는, 제각기 개별 예측 단일 변숫값 각각의 허용 단위 범주 범위 척도 안에는 기막히 아주 적절 조화로이 포섭 안착하면서도, 정작 전체 집합 단면 거시 척도로 바라보면 이내 돌변하여 아주 극명히 특이한(unusual) 변칙 기형 요소로 이질차를 노골 속출하게 되는 특수 관측치가 덩그러니 도출 발생할 가망 여지가 충분히 있습니다.

An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_1$ and $X_2$.
이를 짚어낸 예제가 그림 3.13 의 중앙 패널 면에 단편 전시되어 있는데, 이는 단지 예측 지표 요소 두 가지로 제한 설정된 $X_1$ 및 변수 $X_2$ 인자로 짜인 소규모 축소 일개 데이터 묶음 세트 항목들을 조준한 국면입니다.

Most of the observations' predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range.
대다수 뭇 표본 관측치 산발 타점 투영 변숫값들은 무던 온전히 저기 단면 파란 점선 제한 타원(ellipse) 형성 울타리 내부 안쪽에 곱게 밀집 무리를 일궈 이뤄 안착 도열하건만, 유독 저 문제 조각 표본 붉은 관측점 기조 요소 동향만큼은 홀로 유유 고립 এই 타원 궤도 속성 허용 울타리띠 여건 밖을 부쩍 너머 한참 바깥 밖으로 훌쩍 이탈 이격을 단숨 내비치며(well outside) 한껏 동떨 도망 벗어 비껴서 떨궈져 있습니다.

But neither its value for $X_1$ nor its value for $X_2$ is unusual.
막상 그 빨간 점의 개별 수치 분파 $X_1$ 단편 지분 측면 값 대역 치수나, 그 잔여 잔재 파편 모의 $X_2$ 항목 요소 그 일절 어느 단 하나 측면 지표 국면 잣대 개별로 볼 땐 사실 딱히 무리 특이 변위 변조 양상 변격 평안 기형 궤적 일 이색 다를 특 기 벗어 비 기 일 이상 일 위배 이색 비 일 위 야긋 특이 이 이상할 게 없습니다.

So if we examine just $X_1$ or just $X_2$, we will fail to notice this high leverage point.
고로 이리 근시안만 고집하여 우리가 단독 편협 단일 조사 관점으로 $X_1$ 측면 아님 기껏 오직 $X_2$ 요소 측면 등만을 각자 개별 분리 별 단독 편 검열 측정 산입해 살핀 분간 조사할 국면 심산 양치면, 우린 까맣 장님 눈 이 고 조 조 애당초 우 눈 미연 눈 심각 미연 고 통 시 이 통 이 심각 고 고 이 문제 고 심 이 이 문제성 타점 시 단 각 고 레 고 레 각 점 인 각 수 타 점 각 점 감 파 진 감 안 각 미연 이 눈 사전 파 눈 색 시 레 눈 레 모 시 기 미연 고 레 고(高)시 점 주 미연 레 파 눈 지 미연 레버리지 눈 타점을 감지 인식 유의 조기 인지 각성 포착 색인 탐 감지 조 발견 알아채 파악 식 눈 파 파 파 지 식 별 지 별 기 인 식 기 견 탐 점 파 각 지 찰 눈 탐 기 포기 점 점 탐 점 분 (notice) 포 통 탐 탐 기 포 절차를 인 식 인 도 눈 속 눈 시지 인식 깨 포 인 속 지 발 속 놓 포 인 식 별 실패 일 놓 찰 눈 지 인 결 결 도 간 놓 무 간 지 무 분 기 간 무 결 못 놓 누 결 방 못 치 무 도 도 파 무 견 치 치 모 구 파 모 실 속 결 구 파 패 부 방 도 치 르 치 패 기 못 수 불 패 패 (fail) 패 불 무 속 속 도 부 도 모 실패하고 말 것입니다.""",

    r"In order to quantify an observation’s leverage, we compute the _leverage statistic_ . A large value of this statistic indicates an observation with high leverage leverage. For a simple linear regression,":
    r"""In order to quantify an observation's leverage, we compute the _leverage statistic_.
관측치가 지닌 이런 레버리지 척도를 수치로 계량화고자, 우리는 주로 특정 해당 단면 관측치의 수리 _레버리지 통계량(leverage statistic)_ 을 계산합니다.

A large value of this statistic indicates an observation with high leverage.
이 통계치 숫자가 제법 크다는 건 해당 관측치가 고(高) 레버리지 특성을 띠고 있음을 시사합니다.

For a simple linear regression,""",

    r"statistic ": r"",

    r"106 3. Linear Regression": r"",

    r"It is clear from this equation that _hi_ increases with the distance of x_i from ¯ _x_ . There is a simple extension of _hi_ to the case of multiple predictors, though we do not provide the formula here. The leverage statistic _hi_ is always between 1 _/n_ and 1, and the average leverage for all the observations is always equal to ( $p$ + 1) _/n_ . So if a given observation has a leverage statistic that greatly exceeds ( $p$ +1) _/n_ , then we may suspect that the corresponding point has high leverage.":
    r"""It is clear from this equation that $h_i$ increases with the distance of $x_i$ from $\bar{x}$.
이 수식에서 보듯, $h_i$ 는 $x_i$ 변수값이 평균 지표 $\bar{x}$ 로부터 멀리 떨어진 이격 거리(distance)의 팽창 여파에 비례하여 동반 상승 증가합니다(increases).

There is a simple extension of $h_i$ to the case of multiple predictors, though we do not provide the formula here.
물론 여러 예측 변수가 난립하는 다중 예측 변수 모델(multiple predictors)을 포섭 관리 대응케 할 고안 차기 확장 치환 $h_i$ 수식 요건 국면 연장 방식도 버젓 구비 상존하지만, 굳이 이 지면 내 여기서 다루진 않습니다.

The leverage statistic $h_i$ is always between $1/n$ and $1$, and the average leverage for all the observations is always equal to $(p + 1)/n$.
통상 레버리지 도출 통계 지수 잣대 산입 $h_i$ 수치는 항시 언제나 최소 최저점 바닥 $1/n$ 궤도서부터 최대 상한 고 한도 족쇄 $1$ 장벽까지 그 테두리 내 사이 구간 대역 한도선 구속 영토 속박 제재 안에(between) 늘 매양 항시 안착 속해 도사리며 귀결 속박 국한되며, 도합 전제 온 만물 제반 조사 숱 전체 관측 표본 물량 전수를 모두 포괄 감안 통합 반영 도출한 전체 평균 레버리지 가늠 산출 단면 통계 지수 분간액 수치는 항상 한결같게 기 필연 일관 예외 필 수 차 공식 단 예 불 일 기 매 양 같 동 늘 $(p + 1)/n$ 이 조 수 차 지 항 일 수 같 일 불 매 일 늘 방 기 수 한 일 늘 방 조 공 단 정 (equal to) 동일합니다.

So if a given observation has a leverage statistic that greatly exceeds $(p + 1)/n$, then we may suspect that the corresponding point has high leverage.
그러므로, 어느 한 국면 특정 제공 표본 관측 단위 하나가 이 기본 평균 잣대 $(p + 1)/n$ 수위를 보란 듯 크게 훌쩍 압도 넘어 능가(greatly exceeds)하는 두드러진 막강 레버리지 스탯 통계 지수를 자랑스레 점유한다 친다면, 우린 응당 능히 자연 그 특정 해당 관측점(corresponding point) 부가 으레 다분히 높은 고(高) 레버리지 속성 변종 성향 맹독 병 인자를 버젓 한가득 내포 보유 다분 내재 다 기 합 의 치 파 동 의 농 간 농 심 무 농 의 내 머 다 의 짙 띄 파 합(suspect) 의심해 볼 수 있습니다.""",

    r"The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus _hi_ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.":
    r"""The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus $h_i$ for the data in the left-hand panel of Figure 3.13.
그림 3.13 의 우측 편 패널 도면은 다름 아닌 방금 좌측 단면에 전시 나열되었던 그 같은 동일 데이터 묶음을 토대로 재차 그 스튜던트화 투사 산출 잔차 요건 스탯과 이와 맞대응하는 $h_i$ 통계 척도 수위 단면을 대조 결합해 축차 조화 엮어 그린 단층 플롯(plot) 표면 광경을 일목요연 나란 보여줍니다.

Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual.
특히 이중 관측점 타깃 대상 41번 기조 요건 항목 조각 무리는 다른 것에 비해 단연 독보 초과 압도 튀어 아주 큰 수준의 비대 고도 레버리지 지표 스탯 자산을 짊어짐과 덤 동시에 스튜던트 계산 산출 잔차 척도까지 큰 값 수치로 몹시 도드라지게 기 이 두 특 대 압 특 압 뚜 압 월 대 단 단 포 두 눈 수 두 확 표 특 포 확 뚜 부 두 뛰 기 시 부 띄 확 명 두 뚜 극 특 뚜 눈 점 두 부 대 명 시 확 노 뛰 확 눈 눈 시 기 띕 확 시 띄 표 확 확 표 확 뛰 두 눈 포 두 확 부 뛰 노 확 눈 두 뛰 확 눈 시 뚜 부 뛰 뚜 두 극 기 대 뛰 명 명 대 부 눈 확 두 극 대 확 극 유 부 눈 확 눈 표 점 대 눈 시 눈 유 유 부 부 부 대 시 노 확 눈 눈 확 포 두 확 기 노 부 (stands out) 부각 포착 두드러집니다.

In other words, it is an outlier as well as a high leverage observation.
역설 재차 부연 즉 환원하여 다시금 말해 보자면, 이것은 변칙 요주의 악성 이상치(outlier) 표본 거점 오점 자질 병폐 덩어리 짐을 두루 수반 병행 거머 소지 이 일 지 일 거 거머 뽐 지 점 단 병 이 거 단 차 병 점 이 거 띠 일 거 병 지니는 데에 추가 겸 더 덤 아울 동 어 겸 그 병 더 지 동 지 덧 결 병 가 곁 (as well as) 더불어 추가 겸비 동시 속 수 동 양 동 겸 편 겸 고 속 다 겹 쌍 악 고 더 속 단 양 악 더 편 속 덧 전 덤 고 동 고 고 단 겸 쌍 악 겹 쌍 편 단 동 동 겸 속 포 더 더 덤 속 단 포 겹 고 다 레버리지 관측치 단면 요소 짐마저 겹 쌍 둘 복 합 양 이 동 혼 혼 합 이 쌍 혼 조 쌍 합 쌍 세 쌍 복 이 결 혼 결 동 단 쌍 단 합 동 지 이 고 단 이 합 결 결 지 (observation).

This is a particularly dangerous combination!
이 치명 혼 위 파 환 결 기 대 혼 세 동 기 타 절 세 타 혼 이 결 환 단 치 단 파 절 대 치 치 심 지 맹 기 대 기 극 매우 (particularly) 몹 참 치 아 필 다 기 매 무 전 매우 (dangerous) 조 묶 지 형 쌍 조 (combination) 파 조 치 조합입니다!

This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.
이 도면 궤 구 단 도 잔 그래 (plot) 표면은 더불어 왜 관측 타점 거 요 거 기 조 편 파 편 편 파 조 관 (observation 20)이 그림 3.12 단면의 최소 제곱 적합 궤조에 고작 거의 기 극 요 영 조 보 조 단 파 아 아 거의 영 기 조 아 영 진 미 효 아 반 구 효 일 조 영 파 영 지 파 미(relatively little effect) 파 여 단 반 단 기 미 영 여 파 기 지 기 미여 못 끼 영 끼 조 주 못 밖 미 영 영 구 밖 못 영 줄 주 치 미 밖 줄 낼 치 밖 이 영 밖에 구 여 (had) 주지 못했는지에 대한 연유 단서 이유 발 요인 기 도 조 (reason)를 폭 노 밝 발 들 나 입 시 보 여 표 기 시 증 환 (also reveals): 바로 그것이 기저 다소 낮 저 다 소 볼 조 왜 좀 저 좀 나 (low) 레버리지 단면 포 단 레 발 도 지 고 수 지 스 포 치부 모 속 파 포 포 영레 (leverage) 지 선 결 부 스 구 지 속 포파 지 수(it has low leverage) 단를 기 지 스부 파 레 단지 도 조 점 지 속 부 선 도 기 속단 모 포파 (leverage)지 대질 영 모 부 파 지 즈도 포 속부 즈 영 부 고 지 포 지파지스결(it has) 선모다 지 모를 (leverage)."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

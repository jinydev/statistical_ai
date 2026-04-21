import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_3_potential_problems\2_2._correlation_of_error_terms\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# 2. Correlation of Error Terms": r"""# 2. Correlation of Error Terms 
# 두 번째 잠재적 문제점: 오차 항의 상관관계""",
    
    r"An important assumption of the linear regression model is that the error terms, \epsilon 1 _, ϵ_ 2 _, . . . , ϵn_ , are uncorrelated. What does this mean? For instance, if the errors are uncorrelated, then the fact that \epsilon_i is positive provides little or no information about the sign of \epsilon_i +1. The standard errors that are computed for the estimated regression coefficients or the fitted values are based on the assumption of uncorrelated error terms. If in fact there is correlation among the error terms, then the estimated standard errors will tend to underestimate the true standard errors. As a result, confidence and prediction intervals will be narrower than they should be. For example, a 95 % confidence interval may in reality have a much lower probability than 0 _._ 95 of containing the true value of the parameter. In addition, $p$-values associated with the model will be lower than they should be; this could cause us to erroneously conclude that a parameter is statistically significant. In short, if the error terms are correlated, we may have an unwarranted sense of confidence in our model.":
    r"""An important assumption of the linear regression model is that the error terms, $\epsilon_1, \epsilon_2, \dots, \epsilon_n$, are uncorrelated.
일반 선형 회귀 모델에서 전제하는 주요한 필수 가정 중 하나는, 각 오차 항배열 $\epsilon_1, \epsilon_2, \dots, \epsilon_n$ 이 상호 어떠한 상관관계도 갖지 않는 무관성 독립 요소(uncorrelated)라는 점입니다.

What does this mean?
대체 이게 구체적으로 무슨 뜻일까요?

For instance, if the errors are uncorrelated, then the fact that $\epsilon_i$ is positive provides little or no information about the sign of $\epsilon_{i+1}$.
한 예로, 만약 해당 오차들이 각자 서로 무관하다면, 특정 오차 $\epsilon_i$ 파편이 기저 부호로 양의 부호(+)'를 띤다는 기정사실 자체가 바로 곁에 붙은 후속 $\epsilon_{i+1}$ 부호의 양태 판별 내역과 관련하여 우리에게 암시해 줄 정보란 필시 거의 없거나 전무하다고 볼 수 있습니다.

The standard errors that are computed for the estimated regression coefficients or the fitted values are based on the assumption of uncorrelated error terms.
추정치에 불과한 회귀 계수들이나 이에 기반해 편제된 적합 예측치들을 상대로 계산되는 표준 오차(standard errors)의 산출은 여전히 이들 오차 항 지표들이 서로 무관하다는 가정에 바탕을 두고 있습니다.

If in fact there is correlation among the error terms, then the estimated standard errors will tend to underestimate the true standard errors.
만약 실상 이들 오차 항들 사이에 어떤 연관 상관관계가 뚜렷이 존재하고 있다면, 추정된 표준 오차 값 묶음은 실제 띠어야 할 참수준 기준치인 진짜 표준 오차 규모를 과소평가(underestimate)해 버리는 경향이 생길 것입니다.

As a result, confidence and prediction intervals will be narrower than they should be.
결과적으로 예측 구간과 신뢰 구간은 당초 할당된 것보다 훨씬 더 좁은 수치폭으로 위축됩니다.

For example, a $95\%$ confidence interval may in reality have a much lower probability than $0.95$ of containing the true value of the parameter.
예를 들어, 95% 신뢰 구간은 당초 호언장담한 $0.95$ 수위 확률보다도 파라미터가 갖는 진정한 기저 참값을 제대로 품을 수 있는 실상 확률이 훨씬 낮아지는 양태로 귀결될 가능성이 높습니다.

In addition, $p$-values associated with the model will be lower than they should be; this could cause us to erroneously conclude that a parameter is statistically significant.
게다가 모델에 부착된 $p$-값들도 마땅히 취해야 할 기준치보다 전반적으로 낮게 계측되어 나올 텐데, 이는 자칫 보잘것없는 특정 파라미터 모수를 놓고서도 통계적으로 아주 유의미하다고 우리가 오판하여 잘못된 결론을 내리게 할 수 있습니다.

In short, if the error terms are correlated, we may have an unwarranted sense of confidence in our model.
간단히 말해 오차 항 사이에 상호 연관성이 존재한다면, 우리는 부당하게 과장된 근거와 과신(unwarranted sense of confidence)에 현혹되어 모델을 맹신하게 될 수 있습니다.""",
    
    r"As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs. If we ignored this, our standard error calculations would be as if we had a sample of size 2 $n$ , when in fact we have only $n$ samples. Our estimated parameters would be the same for the 2 $n$ samples as for the $n$ samples, but the confidence intervals would be narrower by a factor of _√_ 2!":
    r"""As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs.
한 가지 극단적 예시를 상정해 봅시다. 무심결에 실수로 기존 보유 데이터를 통째로 두 배 늘려 증폭시켰고 관측 대상과 짝지어진 오차 항들이 전부 복제 쌍(pairs)으로 동일하게 맞춰진 상황을 가정해 보겠습니다.

If we ignored this, our standard error calculations would be as if we had a sample of size $2n$, when in fact we have only $n$ samples.
만일 이 오류를 간과했다면 실제 $n$ 크기 표본만을 가졌음에도 우리의 표준 오차 계산 단위 도출물만큼은 버젓이 장막 뒤로 $2n$ 수준이란 두 배 표본 집단을 갖춘 양 거짓 산정을 전개 거행하게 될 것입니다.

Our estimated parameters would be the same for the $2n$ samples as for the $n$ samples, but the confidence intervals would be narrower by a factor of $\sqrt{2}$!
이때 우리가 최종 도달한 파라미터 모수 추정치는 거짓 모수 집단 격 $2n$ 부류 관측 표본에 적용되더라도 $n$ 규모와 동일(same)하게 도출 전개되긴 하겠지만, 문제는 그에 귀속된 신뢰 구간 범주 폭만큼은 무려 앞선 허상 대비치 기준 $\sqrt{2}$ 이란 수치 배율(factor of $\sqrt{2}$) 만큼 어처구니없이 좁아들어 위축 변형되는 현상에 직면합니다!""",
    
    r"Why might correlations among the error terms occur? Such correlations frequently occur in the context of _time series_ data, which consists of ob- time series servations for which measurements are obtained at discrete points in time. In many cases, observations that are obtained at adjacent time points will have positively correlated errors. In order to determine if this is the case for a given data set, we can plot the residuals from our model as a function of time. If the errors are uncorrelated, then there should be no discernible pat-":
    r"""Why might correlations among the error terms occur?
도대체 왜 오차 항들 이면에서 이런 상관관계 연쇄 파급 현상이 발현되는 걸까요?

Such correlations frequently occur in the context of _time series_ data, which consists of observations for which measurements are obtained at discrete points in time.
그 연유는 이 같은 상관관계성 출현 빈도가 주로 이산적인 특정 시점(discrete points in time)마다 관측 측정치를 추출 조달해수집한 관측치 데이터, 전형적인 소위 _시계열(time series)_ 지표 기반 데이터 맥락 범주 상황 등에 유독 빈번히 국한 거듭 돌발하기 때문입니다.

In many cases, observations that are obtained at adjacent time points will have positively correlated errors.
다수 사례에서, 이처럼 아주 인접한 시간 거점에서 연달아 추출된 인접 관측 데이터는 종종 양의 방향으로 상관관계를 띠는 오차 묶음을 동반 출전시키곤 합니다.

In order to determine if this is the case for a given data set, we can plot the residuals from our model as a function of time.
설령 주어진 특정 데이터 셋에서 이러한 현상이 발생하는지를 판독할 요량이라면 우리는 우리 모델의 잔차(residuals) 묶음을 시간 흐름에 따른 도해 플롯(plot) 표면상에 적나라하게 덧대어 표시 나열해 볼 수 있습니다.

If the errors are uncorrelated, then there should be no discernible pattern.
만약 이 오차 파편들이 전혀 상관관계 띠지 않는 независи 상태라 친다면, 플롯 상에 그 어떠한 식별 가능한 형태의 뚜렷한 가시적 패턴 형상이 단연 나타나지 않아야 마땅합니다.""",
    
    r"102 3. Linear Regression": "",
    "16: **==> picture [317 x 277] intentionally omitted <==**\n": "**==> picture [317 x 277] intentionally omitted <==**\n",
    
    r"tern. On the other hand, if the error terms are positively correlated, then we may see _tracking_ in the residuals—that is, adjacent residuals may have tracking similar values. Figure 3.10 provides an illustration. In the top panel, we see the residuals from a linear regression fit to data generated with uncorrelated errors. There is no evidence of a time-related trend in the residuals. In contrast, the residuals in the bottom panel are from a data set in which adjacent errors had a correlation of 0 _._ 9. Now there is a clear pattern in the residuals—adjacent residuals tend to take on similar values. Finally, the center panel illustrates a more moderate case in which the residuals had a correlation of 0 _._ 5. There is still evidence of tracking, but the pattern is less clear.":
    r"""On the other hand, if the error terms are positively correlated, then we may see _tracking_ in the residuals — that is, adjacent residuals may have similar values.
반면에, 오차 항 단면들이 다분히 양의 방향 관련성 상관성을 갖게 된다면 잔차 표면에 뭔가 추세 흔적을 연쇄 추적하는 _트래킹(tracking)_ 현상을 넉넉히 구경하게 될 소지가 있습니다 — 이 말은 서로 곁에 맞붙은 이웃 잔차가 극히 동형체 흡사 결과 수치값(similar values) 대역을 가질 것이란 추정 설명을 의미합니다.

Figure 3.10 provides an illustration.
해당 그림 3.10 지면 일러스트 기조는 이를 명확히 보충해 입증 증명 곁들여 보여 줍니다.

In the top panel, we see the residuals from a linear regression fit to data generated with uncorrelated errors.
첫 상단 패널 기조를 눈여겨보면 상관관계 흔적 없는 무관 오차 속도로 가상 생성 투입된 데이터 단면에 한차례 선형 회귀 결과를 적합 투사해낸 잔차 결과의 궤적을 우리는 볼 수 있습니다.

There is no evidence of a time-related trend in the residuals.
이 투영된 잔차 분포 기반상에서는 일련의 뚜렷한 시간 연관성 추세 흔적으로 입증 확인해 줄 아무런 기미의 단서(time-related trend) 따위를 털끝만치도 찾아볼 여력이 없습니다.

In contrast, the residuals in the bottom panel are from a data set in which adjacent errors had a correlation of $0.9$.
반면 앞선 광경과 맞서서 바닥면 최하단 배후 패널 요소 기저는 앞뒤 연이은 오차 파급이 서로 상관관계 치수로 자그마치 $0.9$ 높은 양분 수준의 상관 요건 상태를 버젓하게 지녔던 다소 조작 세팅된 관측군 모델로부터 뻗어 나온 잔차 흔적의 양태물들입니다.

Now there is a clear pattern in the residuals — adjacent residuals tend to take on similar values.
이 경우 이제 잔차 파편 도상 전개 패턴상 일련의 극명 뚜렷 노골적인 일관 양태 구조 형성이 확실하게 눈도장 포개어집니다 — 바로 앞선 언급대로 함께 맞붙은 곁 편 제반 잔차들이 하나같이 너무 기막히게 흡사 동급 수위(similar values) 가늠 잣대를 다 같이 차출 띄려는 밀집 경향의 소지를 적나라하게 드러냅니다.

Finally, the center panel illustrates a more moderate case in which the residuals had a correlation of $0.5$.
종착역 중간 배열 궤도 패널 형상은 앞 두 대조 상황의 대략 절반 타협 여건인 앞뒤 상관 궤적이 한 자릿수 $0.5$ 척도 정도로 서로 교류한 비교적 완만한 모범 온건 사례 단편 하나(more moderate case)의 모사 정면 기조를 약소하게 소략 삽화 증명 제시 도안해 나열 줍니다.

There is still evidence of tracking, but the pattern is less clear.
분명 여기 양태서조차 일말 언급 현상 궤적 추적 연쇄 반응을 남김없이 파편 조각내어 도사리고 뒷받침 나타남 전제하긴 하지만 전체 형성 기조 잣대는 아무래도 한껏 상쇄 감소 경향 도출 그 수위를 띄느라 앞보다 약화 흐려져 퇴색된 지표 잣대 양상(less clear) 형국 모양새를 띠고 관찰 포착 나타내게 됩니다.""",
    
    r"Many methods have been developed to properly take account of correlations in the error terms in time series data. Correlation among the error terms can also occur outside of time series data. For instance, consider a study in which individuals’ heights are predicted from their weights. The assumption of uncorrelated errors could be violated if some of the individuals in the study are members of the same family, eat the same diet, or have been exposed to the same environmental factors. In general, the assumption of uncorrelated errors is extremely important for linear regression as well as for other statistical methods, and good experimental design is crucial in order to mitigate the risk of such correlations.":
    r"""Many methods have been developed to properly take account of correlations in the error terms in time series data.
지금껏 유독 시계열 형태 분석 모델 단면에서 골칫거리로 산재하는 이 오차 항 연관 요소 문제를 가급적 적확 현명하게 수용 매만져 능숙하게 다룰 방도로 그간 꽤 무수한 해법 조달 창안 수단이 다각도로 고안 및 발전되어 채택 사용 수단화되었습니다.

Correlation among the error terms can also occur outside of time series data.
그러나 막상 이 오차 항들의 속내 교류 상관 양상은 무수한 시계열 국한 영토 바깥 데이터 평범 일괄지대 밖 외벽 공간(outside of time series data) 등에서마저 돌발 발생 도출할 가망성을 다분히 품고 개방 열려 있습니다.

For instance, consider a study in which individuals' heights are predicted from their weights.
한 예로 기껏 특정 다채 개인 고유의 체중 척도를 발판 삼아 몸무게 정보를 토대로 이번엔 예측 키 신장 수치를 단초 추정 예지 가늠해 내는 통계 조사의 연구 전경 대목 상황 구상을 한 번 잠시 머릿속에 고려 삽화 표방해 주지 돌이켜 보십시오.

The assumption of uncorrelated errors could be violated if some of the individuals in the study are members of the same family, eat the same diet, or have been exposed to the same environmental factors.
만일 실험 표본 군에 포함된 특정 관측 부류 단위 일원이 모두 한집안 식구이면서 피를 같이 하는 혈연 한 무리이거나(members of the same family), 같은 식단 습관 노선을 동시 고집하며(eat the same diet), 그게 아님 완전 일관 판박 특정 동일 환경 영향 궤적 요소(same environmental factors) 등에 거듭 동일 노출 처지된 전향 기조하 요건 상태이면 사실 필시 상관없는 상호 오차 독립 체제 구축 수급에 필패한 극악 오류 조건이 동반 발발 이끌려 그 태초 기저 무관 독립성 가정 바탕 뿌리가 심각 균열 뒤틀림 파탄 훼손 유린 기각 파괴(violated) 전락 위험에 위태 직면 놓일 몹시 치명적 사태 소지 수순 우려를 직간접 부추깁니다.

In general, the assumption of uncorrelated errors is extremely important for linear regression as well as for other statistical methods, and good experimental design is crucial in order to mitigate the risk of such correlations.
일반적으로 기실 오차 항목 독립 무상관 성정 보존 및 확약 가정(assumption of uncorrelated errors)은 비단 지금 선형 회귀에 그뿐 아닌 몹시 다채 다른 통계상 방식 기법 숱 도입 체제 구사에서도 최고 극도로 중차대한 절대 필연 대목 분수령 지주(extremely important) 대단 요소 거점 중요성을 확보 지니며, 결과적으로 고스란히 제반 불가피 상관 오류 지표 노출 동발 파급 발현 오차 오류 위험 치명 요소 그 자체의 폭 발발 우려 리스크 감쇄 요인 저감 약화 조기 방지 체제(mitigate) 실천 타협 이룩 도모 성과 목적 취지선 확보 차원을 담보 단 초석 수립에서 아주 질 좋은 도안 조립 초기 시나리오 밑그림 토대인 표본 초기 실험 설계(good experimental design) 확립 착수 수순 자체가 결코 절대 다른 것과 따질 겨를조차 불허 우위 없이 대단 필경 아주 최고 제일로 필수 긴요 핵심 과업 절대 요소 기조(crucial) 요목 대관 필수 지분 중요 수단 사항 따름 몫 단계 결정을 막강 주름 책임 이룹니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_3_potential_problems\3_3._non-constant_variance_of_error_terms\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# 3. Non-constant Variance of Error Terms": r"""# 3. Non-constant Variance of Error Terms 
# 세 번째 잠재적 문제점: 오차 항의 비상수 분산""",

    r"Another important assumption of the linear regression model is that the error terms have a constant variance, Var( \epsilon_i ) = \sigma^2 . The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption.":
    r"""Another important assumption of the linear regression model is that the error terms have a constant variance, $\text{Var}(\epsilon_i) = \sigma^2$.
선형 회귀 모델에서 전제하는 또 다른 핵심 필수 가정은 바로 제반 오차 항들이 수치 변동 없이 한결같은 상수 분산, 즉 $\text{Var}(\epsilon_i) = \sigma^2$ 값을 상시 유지한다는 점입니다.

The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption.
선형 모델에 부수적으로 결부되어 도출 산입되는 각종 표준 오차를 비롯해 신뢰 구간 잣대, 그리고 가설 검정 등 이 모든 측정 통계 지표는 고스란히 이 가정 하나에 온전히 기대어 의존합니다.""",

    r"Unfortunately, it is often the case that the variances of the error terms are non-constant. For instance, the variances of the error terms may increase with the value of the response. One can identify non-constant variances in the errors, or _heteroscedasticity_ , from the presence of a _funnel shape_ in heterothe residual plot. An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values. When faced with this problem, one possible solution is to transform the response Y using a concave function such as log Y or _√Y_ . Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in heteroscedasticity. The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using log Y . The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data.":
    r"""Unfortunately, it is often the case that the variances of the error terms are non-constant.
불행하게도 기실 현상에서는 오차 항들의 분산 치수가 상수가 아니라 일관되지 않고 비상수 형태를 띠게 되는 사례가 매우 잦고 흔합니다.

For instance, the variances of the error terms may increase with the value of the response.
예컨대 오차 항들의 분산 물량이 대상 응답 변숫값 척도가 커짐에 따라 덩달아 같이 널뛰며 증가해 버릴 수 있습니다.

One can identify non-constant variances in the errors, or _heteroscedasticity_, from the presence of a _funnel shape_ in the residual plot.
우리는 대개 그려진 잔차 플롯 표면에서 일종의 깔때기 모양(_funnel shape_) 형상이 존재 도래하는지 여부를 관찰함으로써, 각 오차 요인 측면의 비상수 분산 현상인 일명 _이분산성(heteroscedasticity)_ 발생 유무를 식별해 판가름해 낼 수 있습니다.

An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values.
그림 3.11 의 왼쪽 패널 도면은 이 양태의 전형을 아주 여실히 잘 보여주며, 적합 값 수위의 크기에 비례해 발맞춰 잔차의 규모 역시 동반 상승하는 경향성을 고스란히 띱니다.

When faced with this problem, one possible solution is to transform the response $Y$ using a concave function such as $\log Y$ or $\sqrt{Y}$.
이 난관 문제에 직면했을 때 꺼내 들 수 있는 한 가지 유력한 구제 해결책은, 응답 변수 $Y$ 값을 $\log Y$ 나 $\sqrt{Y}$ 단위와 같은 일종의 오목 함수 형태로 치환하여 변환하는 것입니다.

Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in heteroscedasticity.
이런 방식의 치환 변환 요법은 유독 상대적으로 큰 비율의 응답 결괏값 부문에 대해 월등히 더 쏠린 압축 축소 수축(shrinkage) 마찰을 크게 유발하며, 궁극적으로 이분산성 크기 폭을 경감 저하해 주는 안주 조치로 매끄럽게 인도 귀결됩니다.

The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using $\log Y$.
이어서 그림 3.11 오른쪽 패널 광경은, 응답 변수를 애당초 $\log Y$ 형식 단위로 선제 변환해 맞춘 직후 모의 산출 투사된 잔차 분산 플롯 궤적입니다.

The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data.
비록 데이터 구조 내면에 아주 미세한 비선형적 관계 흔적 양상이 여전히 다소 조금 관찰될지언정, 적어도 도출된 이 잔차 분포도만큼은 이제 제법 뚜렷이 일정상수 분산을 일정히 유지 도달한 듯 보입니다.""",

    r"scedasticity": r"",
    r"heterothe": r"the",
    
    r"Sometimes we have a good idea of the variance of each response. For example, the _i_ th response could be an average of _ni_ raw observations. If each of these raw observations is uncorrelated with variance \sigma^2 , then their average has variance _σi_[2][=] _[ σ]_[2] _[/n][i]_[.][In][this][case][a][simple][remedy][is][to][fit][our] model by _weighted least squares_ , with weights proportional to the inverse weighted variances—i.e. _wi_ = _ni_ in this case. Most linear regression software allows least for observation weights.":
    r"""Sometimes we have a good idea of the variance of each response.
때때로 우리는 각 응답 변수 측면이 지닌 자체 분산 크기 지표 분량 정보를 꽤 상당 부분 명확히 꿰뚫고 파악 인지하는 국면을 맞곤 합니다.

For example, the $i$th response could be an average of $n_i$ raw observations.
가령 꼽아 보건대, 산출된 $i$번째 응답 결괏값 단위 덩이가 기실은 날것 그대로의 원시 관측치 조각 $n_i$ 번 표본 묶음 데이터의 단순 평균값 지표일 수도 있습니다.

If each of these raw observations is uncorrelated with variance $\sigma^2$, then their average has variance $\sigma_i^2 = \sigma^2 / n_i$.
만약 이 각각의 날것 원시 관측치들이 온전히 $\sigma^2$ 이란 단위 분산을 띤 채 상호 간 무관하게 동떨어진 분산 단위 체계 요건이라면, 이들의 응집 평균치는 자연히 $\sigma_i^2 = \sigma^2 / n_i$ 꼴의 분산을 내부에 거느리게 됩니다.

In this case, a simple remedy is to fit our model by _weighted least squares_, with weights proportional to the inverse variances — i.e. $w_i = n_i$ in this case.
바로 이런 환경 요건 처지 사례에서, 우리가 취할 수 있는 간결한 해결책 요법 하나는, 당장 내건 분산 지표의 역수치 단위에 정비례하는 가중치 잣대 속성(즉 현 케이스의 경우 $w_i = n_i$ 단위)을 차용 접목하여 _가중 최소 제곱(weighted least squares)_ 방식으로 모델 형식을 적합 조립해 내는 것입니다.

Most linear regression software allows for observation weights.
다행히 시중 출시 중인 대다수 범용 선형 회귀 소프트웨어 구동 장치 단면에는 이 같은 관측치 항목별 특수 가중치 적용 산입 기능을 너끈히 허용해 제공 지원하고 있습니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

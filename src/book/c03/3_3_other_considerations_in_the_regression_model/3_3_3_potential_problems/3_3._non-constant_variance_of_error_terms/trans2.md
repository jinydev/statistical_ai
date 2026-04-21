---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 2. Correlation Of Error Terms](../2_2._correlation_of_error_terms/trans2.html) | [4. Outliers >](../4_4._outliers/trans2.html)

# 3. Non-constant Variance of Error Terms

# 세 번째 잠재적 문제점: 오차 항의 널뛰기 분산 (갈수록 커지는 찌꺼기들의 깽판)

Another important assumption of the linear regression model is that the error terms have a constant variance, $\text{Var}(\epsilon_i) = \sigma^2$.
고지식한 선형 회귀 모델이 목숨처럼 부여잡고 있는 또 다른 어처구니없는 철칙(가정)이 있습니다. 바로 수많은 오차 찌꺼기들($\epsilon_i$)이 터뜨리는 널뛰기 폭발력, 즉 **'분산(Variance)'**의 크기가 처음부터 끝까지 변함없이 한결같은 고정된 수치 타겟($\sigma^2$)을 아주 얌전하게 유지(constant variance)해 줄 것이라는 순진무구한 믿음입니다.

The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption.
선형 모델을 돌려 뽑아낸 그럴싸한 성적표들, 예컨대 우리가 그렇게 맹신하는 '표준 오차' 방벽이나, "여기에 정답이 있다!"고 치는 '신뢰 구간' 울타리, 심지어 이게 맞는지 틀린 지 재판하는 '가설 검정'의 모든 판결 기준들조차 저 "찌꺼기들의 점프력은 언제나 일정하다"라는 이 허술한 믿음 하나에 뼛속까지 기대어 유지되고 있습니다.

Unfortunately, it is often the case that the variances of the error terms are non-constant.
불행하게도 무자비한 실전 야생 데이터에서는 우리의 이 아름다운 희망 사항이 무참히 박살 납니다. 실제로는 찌꺼기들의 널뛰기 폭발력(분산)이 결코 얌전한 상수(constant)로 가만히 머물지 않고 미친 듯이 고무줄처럼 변덕을 부리는 비상수(non-constant) 미쳐버린 양태를 띠는 깽판 사례가 너무나도 잦고 흔하거든요.

For instance, the variances of the error terms may increase with the value of the response.
가장 흔한 발작 패턴이 뭔지 아시나요? 대개 타겟 정답(응답 변수)의 덩치가 커지면 커질수록, 즉 숫자가 커지는 후반부 동네로 갈수록 오차 찌꺼기들이 일으키는 널뛰기 진동 오차 폭(분산)도 덩달아 고삐 풀린 망아지처럼 미친 듯이 커지며 발작을 일으킵니다. 이를 통계 전문 용어로 찌꺼기들의 분산이 짝짝이다 해서 **'이분산성(Heteroscedasticity)'**이라고 멋 부려 부릅니다.

One can identify non-constant variances in the errors, or _heteroscedasticity_, from the presence of a _funnel shape_ in the residual plot.
우리 모델에 이런 더러운 이분산성 병이 도졌는지 안 도졌는지 어떻게 감별할까요? 아주 쉽습니다. 아까 배운 쓰레기장 관측 돋보기, '잔차 플롯(Residual plot)'을 눈여겨보세요. 만약 찌꺼기 점들이 시간이 지날수록 우측으로 퍼지며 마치 나팔꽃이나 **깔때기 모양(_funnel shape_)**으로 쫙 벌어지며 퍼져나가는 살벌한 궤적을 그린다면 100% 당첨입니다.

An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values.
앞 페이지에서 미리 훔쳐봤던 [그림 3.11]의 왼쪽 단면 투시도가 바로 이 끔찍한 병에 걸린 아주 적나라하고 완벽한 시각적 증거입니다. 표면을 보시면, x축의 예측 정답 덩치(Fitted values) 수치가 우측으로 커지면 커질수록, y축에 찍히는 잔차 찌꺼기들의 위아래 변동 진폭(magnitude) 널뛰기 타점 역시 덩달아 걷잡을 수 없이 무자비하게 벌어지며 폭발 상승하는 악질 경향성을 고스란히 노출합니다. 

When faced with this problem, one possible solution is to transform the response $Y$ using a concave function such as $\log Y$ or $\sqrt{Y}$.
자, 이렇게 깔때기 병기운(이분산성)에 오염된 모델을 맞닥뜨렸을 때 우리가 쓸 수 있는 아주 간결하고 야비한 응급처치 해결책(solution)이 하나 있습니다. 바로 깽판을 치는 타겟 정답 뒷목($Y$)을 멱살 잡고 끌고 와 $\log Y$(로그)나 $\sqrt{Y}$(루트) 같은 오목 함수(concave function)라는 압축기 기계에 처넣고 강제로 단위 자체를 마개조 수축 변환시켜 버리는 충격 요법입니다.

Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in heteroscedasticity.
왜 하필 이런 로그나 루트 같은 변환 압축기 마취 요법을 쓸까요? 이 오목 함수들의 특징이, 작은 숫자 치수들은 살살 다루면서도 유독 헛바람이 잔뜩 든 '초거대 덩치의 응답 수치' 들일수록 자비 없이 무진장 강력하게 짓눌러 쭈그러뜨리는 강력한 수축(shrinkage) 압축 압박 타격을 가하기 때문입니다. 덕분에 우측으로 갈수록 미친 듯 널뛰던 잔차 찌꺼기들의 폭발적 팽창 찌부림 이분산성 폭주 파동을 순식간에 찍어 눌러 극적으로 경감 저하시켜 버리는 마법 같은 완치 구제 평단을 이뤄냅니다.

The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using $\log Y$.
치료 후 결과는 다시 한번 [그림 3.11]의 오른쪽 패널 광경에서 극명하게 목도 입증 증명됩니다. 응답 타겟을 $\log Y$ 라는 강력 마취제로 선제 틀어막아 변환 조치를 끝낸 직후 다시 찍어본 모의 잔차 분산 플롯 형국 전개도입니다.

The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data.
보이십니까? 비록 바닥에 깔린 추세 데이터 구도 내면에 미세하게 구불거리는 약간의 비선형적 관계 파동 찌꺼기 흔적이 좀 남아서 발목 찜찜할 여지를 줄지언정, 적어도 깔때기처럼 무섭게 찢어지던 그 살벌한 널뛰기 폭동(이분산성)만큼은 깜쪽같이 사라졌습니다! 흩뿌려진 잔차 구름 덩어리가 눈에 띄게 한결같은 일자 파이프 수평 두께, 즉 드디어 얌전한 **일정 상수 분산(constant variance)** 평형의 정상 궤도 진정 궤지를 회복 확보한 장관의 승리입니다.

Sometimes we have a good idea of the variance of each response.
참고로 응급 처치 변환 꼼수 말고도, 때때로 야생 바닥에서는 우리가 "어이구, 이번 타겟 응답 놈은 도대체 지구가 망할 때까지 대충 얼만큼의 분산 수치 파동 크기로 널뛸지 그 견적(분산 분량) 척도를 내가 대충 꿰고 있지롱!" 하고 명확히 파악 인지하는 아주 럭키한 기연 상황도 종종 터집니다.

For example, the $i$th response could be an average of $n_i$ raw observations.
가령 예를 들어, 우리가 뽑아든 $i$번째 응답 결괏값 스코어 타점 덩이가, 알고 봤더니 날것 그대로의 미천한 원시 관측치 조각 표본 찌꺼기들 $n_i$ 개 분량을 긁어모아 억지로 단순 퉁을 친 '평균값(average)' 지표일 수도 있단 말이죠.

If each of these raw observations is uncorrelated with variance $\sigma^2$, then their average has variance $\sigma_i^2 = \sigma^2 / n_i$.
만일 바닥에 깔린 이 원시 찌꺼기 조각놈들이 전부 다 독립적이고 얌전하게 $\sigma^2$ 이라는 똑같은 분산 단위를 지녔었다고 칩시다. 이러면 그놈들을 $n_i$ 개 뭉쳐 퉁친 '덩어리 평균 응답치'가 지닌 진짜 분산 크기는 수학 공식에 따라 자동 빵으로 $\sigma_i^2 = \sigma^2 / n_i$ 꼴로 파이가 작아져 도출되는 구조를 타게 됩니다.

In this case, a simple remedy is to fit our model by _weighted least squares_, with weights proportional to the inverse variances — i.e. $w_i = n_i$ in this case.
바로 빙고! 이렇게 상대방 응답 타겟이 얼마나 미친 듯 발작 분산을 띨지 미리 공식으로 각이 나와버린 투명한 상황이라면, 아까처럼 복잡한 변환 삽질 대신 아주 심플 명료 우아한 통계적 치료 구제 조치(remedy) 하나를 쓸 수 있습니다. 일명 **_가중 최소 제곱(Weighted least squares)_**이라는 족집게 편애 모델링 방식을 투입하는 겁니다. 방법은 쉬워요. 예측 모델 뼈대를 맞출 때 분산이 커서 깽판 칠 놈들은 비중(가중치)을 줄여 개무시하고, 분산이 작아 얌전한 신뢰도 높은 놈에겐 비중을 왕창 몰아주는 식으로, 오차 분산 지표의 '역수($1/\text{분산}$)' 단위에 정비례하는 편애 가중치(현 예시에선 결국 원시 조각수 $w_i = n_i$)를 떡칠해 처방 조립 적합 해내는 명쾌한 논리입니다.

Most linear regression software allows for observation weights.
쫄지 마세요. 이런 편애 가중치 모델링 조립 기능은 시중에 돌아다니는 웬만한 기성 범용 선형 회귀 소프트웨어 계산기나 파이썬 일반 함수 패키지 모듈에 다 기본 옵션으로 탑재되어 빵빵하게 알아서 지원 지시해 줍니다!

---

[< 2. Correlation Of Error Terms](../2_2._correlation_of_error_terms/trans2.html) | [4. Outliers >](../4_4._outliers/trans2.html)

---
layout: default
title: "trans1"
---

# _6.1.2 Stepwise Selection_ 
# 6.1.2 단계적 선택법 (Stepwise Selection)

For computational reasons, best subset selection cannot be applied with very large $p$. Best subset selection may also suffer from statistical problems when $p$ is large. The larger the search space, the higher the chance of finding models that look good on the training data, even though they might not have any predictive power on future data. Thus an enormous search space can lead to overfitting and high variance of the coefficient estimates. 
계산 처리상의 현실적인 한계량(computational reasons)의 벽에 부딪혀, 앞선 최적 부분집합 선택(best subset selection) 기법은 예측 변수 $p$ 의 규모가 매우 거대하고 방대해진(very large) 환경 조건 하에서는 온전히 적용 실현(applied) 구동될 수 없습니다. 또한 이 최적 부분집합 선택 기법은 단순히 물리적 연산 장애뿐만 아니라, 투입 변수 $p$ 가 거대해졌을(large) 경우 필연적으로 발생하는 심각한 통계적 오류 사안(statistical problems)의 폐단으로 인해 심각한 차질과 곤욕을 치르게(suffer from) 될 위험을 내포합니다. 왜냐하면 탐색해야 할 범주 모델 경우의 수 생태계 영토(search space) 반경이 거대해지면 거대해질수록, 비록 그 모델 객체들이 미래의 미지 후속 실제 실전 데이터(future data)를 예측해 낼 수 있는 본연의 실질 예측 기저 역량 점수 타점 능력(predictive power)을 전혀 사실상 단 한치도 전혀 내재하거나 가지지 못했을(might not have any)지라도, 단지 현재 한정 소장 중인 국지적 훈련 데이터(training data) 한정 환경에서만 유독 그럴싸하게 우수해 보이고 착시를 일으키며 포장되어 도출 산출 표방되는(look good) 그릇된 허위 가짜 낭설 껍데기 과적합 모델들을 우연히 걷어 찾아낼(finding models) 맹점 확률 계수 비율 요율(the chance of)이 치명적으로 기하 조작 심각하게 높아 상승 초래(higher)하게 되기 때문입니다. 고로 이와 같이 허무맹랑 하리만큼 거대 방대한 수색 조망 탐색 범위 영토(an enormous search space) 설정은 급기 극단 치명 필연적으로 모델의 과도한 과적합(overfitting) 문제와 계수 도출 추정치 타점 점수 간의 거대 극심한 고분산(high variance) 에러의 불안정성 결여 파행 부작용(can lead to)을 낳고 양산 유발 야기 초래 촉발 잉태(lead to)하게 되는 결과를 맞이합니다.

For both of these reasons, _stepwise_ methods, which explore a far more restricted set of models, are attractive alternatives to best subset selection. 
이처럼 언급된 두 가지 치명적이고 본질적인 현실 오류적 측면 기인 사유(both of these reasons)들을 징계 치유 타파 돌파 극복하고자, 기존 보다 아득히 훨씬 극히 파격적 한층 더(far more) 억제 지향 제한 축소 결박 고립 통과 억압 폐쇄 설정 한정된(restricted) 소규모 표본 파편 군집 부류 범위 층위 모델 세트군(set of models) 체급만을 조준 대상 삼아 탐색 분별 공략 추적 수사 관측 탐사 조회 스캔 필터 감별 심사 조회(explore) 해내는 이른바 단계식 순차 궤도 도열 단층 체계 계단 전개 방식의 절차인 **'_단계적(stepwise)_'** 탐색 방법 수리 평가 수단 기법(methods)들이야말로, 저 막무가내 무식 오만 최적 부분집합 선택 기법을 유연하게 교체 배제 대체 치환 반환 갈음(alternatives to) 할 수 있는 지극히 명석하고 합당하며 매력적인 지시 강점 이점 유효 매혹 대안 가치 훌륭 대안 채널 패널 우회 평가 대안 방책 이례 무기 대안책 대안 도구 해결 방식 우위 매력적인 해결 방벽 방안(attractive alternatives) 수단으로 우뚝 선도 거상 매력 조명 각광 부상 대두 표상 제시 가치 입증 부각(are attractive) 받게 됩니다.

---

## Sub-Chapters (하위 목차)

### Forward Stepwise Selection (전진 단계 선택법)
* [문서로 이동하기](./6_1_2_1_forward_stepwise_selection/trans1.html)

데이터에 아무 변수가 없는 빈(Null) 모델에서 출발하여 모델 성능을 가장 유의미하게 향상시키는 변수를 한 번에 하나씩만 추가하는 경제적 방식입니다.

### Hybrid Approaches (혼합 접근법)
* [문서로 이동하기](./6_1_2_2_hybrid_approaches/trans1.html)

전진 추가와 후진 제거(Backward)를 양방향 결합하여, 유의미해 보였지만 다른 변수 편입으로 불필요해진 변수를 추후에 제거해 내는 유연한 방식입니다.

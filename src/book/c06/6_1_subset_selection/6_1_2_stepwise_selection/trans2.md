---
layout: default
title: "trans2"
---

# _6.1.2 Stepwise Selection_ 
# 6.1.2 단계적 선택법 (Stepwise Selection): 효율을 극단으로 끌어올린 탐욕적 오디션

For computational reasons, best subset selection cannot be applied with very large $p$. Best subset selection may also suffer from statistical problems when $p$ is large. The larger the search space, the higher the chance of finding models that look good on the training data, even though they might not have any predictive power on future data. Thus an enormous search space can lead to overfitting and high variance of the coefficient estimates. 
아까 우리가 살펴본 **'최적 부분집합 선택(Best Subset Selection)'** 은 모든 걸 다 까보는 완벽주의자 같지만 치명적인 약점이 두 가지 있습니다. 
첫째, 변수 $p$ 가 조금만 커져도 연산량이 폭발해 **슈퍼컴퓨터마저 넉실 나가게 만드는 계산적 한계(computational reasons)** 입니다.
둘째, 이 무식한 전수조사 오디션은 변수 $p$ 가 늘어날수록 **통계적 사기꾼(statistical problems)에게 속을 확률이 덩달아 폭등**한다는 사실입니다. 도대체 왜일까요? 우리가 샅샅이 뒤져야 할 수색 범위(search space)가 넓어지면 넓어질수록, 어쩌다 우연의 일치로 현재 훈련소 데이터 타겟을 기가 막히게 잘 맞추는 척하는 요행수 가짜 모델들이 얻어걸릴(finding models) 확률이 미친 듯이 치솟기 때문입니다. 이 녀석들은 막상 나중에 실전 테스트 데이터 장에 던져 넣으면 한 발도 못 맞추는 허수아비(not have any predictive power)일 확률이 농후하죠.
즉, 방대한 모델의 우주를 다 뒤지겠다는 이 오만한 수색 작전(an enormous search space)은, 결국 필연적으로 **과적합(overfitting)** 이라는 자아도취와 계수 추정치들이 요동치는 **미친 대분산(high variance)** 의 저주를 끌어들이고(lead to) 맙니다.

For both of these reasons, _stepwise_ methods, which explore a far more restricted set of models, are attractive alternatives to best subset selection. 
이러한 연산량의 지옥과 과적합의 함정(both of these reasons)을 피하기 위해 업계가 고안해 낸 스마트한 해결책이 바로 **'_단계적(stepwise)_'** 방법론들입니다. 이 녀석들은 우주 전체를 무식하게 뒤지는 짓을 집어치우고, 자신이 갈 길을 아주 매정하고 기민하게 **제한시켜(restricted)** 핵심 모델들만 알짜로 쏙쏙 뽑아 심사 탐색(explore) 합니다. 그래서 이 단계적 전법은 저 구닥다리 최적 부분집합의 늪을 피할 수 있게 해주는 아주 치명적으로 매력적이고 효율적인 탈출 대안 무기(attractive alternatives)로 찬사받게 됩니다.

---

## Sub-Chapters (하위 목차)

### Forward Stepwise Selection (전진 단계 선택법)
* [문서로 이동하기](./6_1_2_1_forward_stepwise_selection/trans2.html)

데이터에 아무 변수가 없는 빈(Null) 모델에서 출발하여 모델 성능을 가장 유의미하게 향상시키는 변수를 한 번에 하나씩만 추가하는 경제적 방식입니다.

### Hybrid Approaches (혼합 접근법)
* [문서로 이동하기](./6_1_2_2_hybrid_approaches/trans2.html)

전진 추가와 후진 제거(Backward)를 양방향 결합하여, 유의미해 보였지만 다른 변수 편입으로 불필요해진 변수를 추후에 제거해 내는 유연한 방식입니다.

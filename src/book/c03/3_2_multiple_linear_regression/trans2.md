---
layout: default
title: "trans2"
---

[< 3.1.3 Assessing The Accuracy Of The Model](../3_1_simple_linear_regression/3_1_3_assessing_the_accuracy_of_the_model/trans2.html) | [3.2.1 Estimating The Regression Coefficients >](3_2_1_estimating_the_regression_coefficients/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 3.2 Multiple Linear Regression

# 3.2 다중 선형 회귀 (재료를 몽땅 때려 넣어 매상을 예측해 보자!)

Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the `Advertising` data, we have examined the relationship between sales and TV advertising. We also have data for the amount of money spent advertising on the radio and in newspapers, and we may want to know whether either of these two media is associated with sales. How can we extend our analysis of the advertising data in order to accommodate these two additional predictors?
앞서 배운 '단순' 선형 회귀는 오직 단 1개의 힌트(원인 변수)만 가지고 정답(결과)을 예언하는 기초적인 마법이었습니다. 하지만 피 튀기는 진짜 장사판(현실)에서는 우리가 참고할 힌트 데이터가 한 개만 있을 리가 없죠! 예컨대 우리가 봤던 `Advertising(광고)` 데이터 장부에선 제일 먼저 `TV 광고비` 하나만 뚫어지라 쳐다보며 `판매량(sales)` 우상향 곡선을 그렸습니다. 하지만 가만 보면 창고 장부엔 라디오 광고비 영수증도 있고, 동네 벼룩시장 신문 광고 영수증도 버젓이 존재합니다. 그럼 사장님 입장에선 당연히 "야, TV만 보지 말고 라디오랑 신문 광고비도 다 긁어와 봐. 셋 중 뭐가 진짜 매출 터지는 데 도움 되는지 알 수 없을까?" 하고 묻고 싶을 겁니다. 도대체 우리의 단순무식했던 직선 자를 어떻게 잘 휘고 늘려서, 한꺼번에 여러 개의 힌트 변수(매체 예산들)를 통째로 쑤셔 넣고 매출을 분석할 수 있을까요?

One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the amount spent on radio advertisements. Results are shown in Table 3.3 (top table). We find that a $\$1,000$ increase in spending on radio advertising is associated with an increase in sales of around 203 units. Table 3.3 (bottom table) contains the least squares coefficients for a simple linear regression of sales onto newspaper advertising budget. A $\$1,000$ increase in newspaper advertising budget is associated with an increase in sales of approximately 55 units.
가장 먼저 떠오르는 초보적인 꼼수는, 그냥 단순 선형 회귀 직선을 무식하게 **3번 따로따로 여러 번 긋는 짓**일 겁니다. 예를 들어, TV만 보고 선 한 번, 라디오 예산금만 따로 빼서 선 긋고 예측 한 번, 이런 식이죠. 아까 본 표 3.3 (위쪽 표)의 결과가 바로 그겁니다. 우리가 라디오 광고비에만 홀딱 반해서 $\$1,000$ (약 130만 원)을 부었더니, 붕어빵 박스는 야속하게도 겨우 평균 203개를 더 팔았습니다. 이어서 표 3.3 (아래쪽 표)은 신문 광고비 장부만 빼서 그린 최소 제곱법 회귀 결과인데, 여기도 신문에 무려 $\$1,000$을 발랐음에도 판매량은 쥐꼬리만 한 평균 55박스 정도 상승하는 처참성에 그쳤습니다.

However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertising media budgets, since each of the budgets is associated with a separate regression equation. Second, each of the three regression equations ignores the other two media in forming estimates for the regression coefficients. We will see shortly that if the media budgets are correlated with each other in the 200 markets in our data set, then this can lead to very misleading estimates of the association between each media budget and sales.
그런데 말입니다, 이렇게 힌트를 하나씩 따로 떼어놓고 귀찮게 각질 제거하듯 선형 모델을 여러 번 적합시키는 방식은 치명적인 결함투성이입니다. 첫째, 사장님이 "내일 TV, 라디오, 신문 세 군데에 동시에 돈을 팍팍 풀면 총매출이 정확히 얼마나 치솟을까?" 하고 묻는다면 대답할 길이 막막해집니다. 각 매체들이 저마다의 외딴섬(서로 다른 별개 방정식)에서 따로따로 놀고 있기 때문이죠. 둘째, 이 3개의 외로운 방정식들은 서로 자신이 답을 낼 때 **나머지 두 매체의 노력을 철저하게 무시**합니다. 가령 우리가 수집한 200개 동네 시장에서 라디오 광고를 미친 듯이 틀 때 하필 신문 전단지도 거리에 도배됐다면(예산들끼리 끈끈한 상관관계가 있다면), 이런 식의 외골수 접근은 각 매체가 매출을 얼마나 올려주었는지 **지독하게 엉뚱하고 환각에 빠진 거짓 정보 추정치**를 산출하게 만듭니다. (잠시 후 이어지는 섹션에서 그 무서운 결과표를 볼 겁니다!)

Instead of fitting a separate simple linear regression model for each predictor, a better approach is to extend the simple linear regression model (3.5) so that it can directly accommodate multiple predictors. We can do this by giving each predictor a separate slope coefficient in a single model. In general, suppose that we have $p$ distinct predictors. Then the multiple linear regression model takes the form
이런 바보 같은 외다리 단순 회귀 삽질을 여러 번 반복하느니, 차라리 아까 (3.5)에서 배운 공식의 냄비를 거대하게 부풀려 확장시켜버리는 편이 훨씬 똑똑합니다. 하나의 무지막지한 모델 솥단지 안에다가 그냥 온갖 야채, 고기, 힌트 수치(다수의 예측 변수)들을 한꺼번에 쓸어 담아 수용해버리는 방식이죠. 이것은 하나의 거대 모델 방정식 조립도 안에서 **마늘 양(예측 변수 1)에는 마늘 전용 화력(별도의 기울기 계수)을 주고, 파 양(예측 변수 2)에는 파 전용 화력을 달아주는 식**으로 유쾌하게 해결할 수 있습니다. 멋들어지게 수식으로 풀자면, 우리에게 힌트를 주는 각기 다른 재료들($p$개의 구별되는 예측 변수)이 있다고 쳐보죠. 그럼 이 웅장한 **다중 선형 회귀(Multiple linear regression) 마법진**은 필연적으로 다음과 같은 거대한 수식 뱀 형태로 나타납니다.

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon \quad (3.19)
$$

where $X_j$ represents the $j$th predictor and $\beta_j$ quantifies the association between that variable and the response. We interpret $\beta_j$ as the _average_ effect on $Y$ of a one unit increase in $X_j$, _holding all other predictors fixed_. In the advertising example, (3.19) becomes
여기 복잡한 공식 혀끝에 붙은 $X_j$ 는 그저 $j$번째 투입된 재료(예측 힌트 변수) 이름일 뿐이고, $\beta_j$ 는 그 해당 재료 하나가 최종 붕어빵 맛(반응치 예측)에 얼마나 강하게 연관되어 간을 맞추는지 그 파괴력을 수량으로 잰 **계수 파라미터(마법 조미료 가루)**입니다. 통계 판사들은 이 $\beta_j$ 의 능력을 이렇게 꼼꼼히 해석합니다: **_"나머지 다른 모든 힌트 재료들의 투입량을 하나도 안 건드리고 그대로 멈춰라(고정) 시킨 채, 오로지 이 $X_j$ 녀석 딱 하나만 1 단위 묶음 더 퍼부었을 때, 최종 매상 타겟 $Y$ 에 미치는 '평균적인(average)' 데미지 효과!"_** 라고 말이죠. 이 깨달음을 방금 전 광고 예제 냄비에 부어보면 통계 수식 (3.19) 는 이렇게 친숙한 꼴로 둔갑합니다.

$$
\text{sales} = \beta_0 + \beta_1 \times \text{TV} + \beta_2 \times \text{radio} + \beta_3 \times \text{newspaper} + \epsilon \quad (3.20)
$$

---

## Sub-Chapters (하위 목차)

### 3.2.1 Estimating the Regression Coefficients (회귀 계수 추정)
* [📖 쉬운 해설판으로 이동하기](./3_2_1_estimating_the_regression_coefficients/trans2.html)

여러 개의 설명 변수를 모두 포함한 다차원 공간에서 평균 잔차 제곱합을 최소화하는 하이퍼플레인을 찾는 과정을 배웁니다.
단순히 직선을 긋는 걸 넘어서, 변수가 2개면 3차원 철판을 찍어 누르는 듯한 신비로운 다중 회귀 모델의 뼈대를 만듭니다.

### 3.2.2 Some Important Questions (중요한 질문들)
* [📖 쉬운 해설판으로 이동하기](./3_2_2_some_important_questions/trans2.html)

다중 선형 회귀 모델을 사용할 때 답해야 하는 주요 질문(변수들의 유의성, 모델 적합도, 예측)들을 제기합니다.
"다 때려 넣었는데 과연 이 요리가 맛있을까?" 다중 모델을 만들자마자 사장님에게 들어올 4가지 매서운 검증 질문들에 대비합니다.

---

[< 3.1.3 Assessing The Accuracy Of The Model](../3_1_simple_linear_regression/3_1_3_assessing_the_accuracy_of_the_model/trans2.html) | [3.2.1 Estimating The Regression Coefficients >](3_2_1_estimating_the_regression_coefficients/trans2.html)

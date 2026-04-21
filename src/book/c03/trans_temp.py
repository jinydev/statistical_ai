content = """---
layout: default
title: "index"
---

# 3.3.1 Qualitative Predictors 
# 3.3.1 정성적 예측 변수(Qualitative Predictors)

In our discussion so far, we have assumed that all variables in our linear regression model are _quantitative_.
지금까지의 논의에서, 우리는 선형 회귀 모델 내의 모든 변수가 _정량적(quantitative)_ 즉, 수치형 변수일 것이라고 가정해 왔습니다.

But in practice, this is not necessarily the case; often some predictors are _qualitative_. 
하지만 실제 현장에서는 꼭 그렇지만은 않은 경우가 많습니다; 종종 일부 예측 변수들은 범주를 나타내는 _정성적(qualitative)_ 성향을 띠기도 합니다.

For example, the `Credit` data set displayed in Figure 3.6 records variables for a number of credit card holders.
예를 들어 그림 3.6 에 표시된 `Credit` 데이터 세트는 다수의 신용카드 소지자에 대한 각종 변수들을 기록하고 있습니다.

The response is `balance` (average credit card debt for each individual) and there are several quantitative predictors: `age`, `cards` (number of credit cards), `education` (years of education), `income` (in thousands of dollars), `limit` (credit limit), and `rating` (credit rating).
이때 응답 변수는 `balance` (각 개인의 평균 신용카드 부채 액수) 이며, 여기엔 몇 가지 정량적 관점의 예측 변수들이 등장합니다: `age` (나이), `cards` (보유 신용카드 개수), `education` (교육을 받은 연도), `income` (천 달러 단위의 소득), `limit` (신용 한도), 그리고 `rating` (신용 등급) 등입니다.

Each panel of Figure 3.6 is a scatterplot for a pair of variables whose identities are given by the corresponding row and column labels.
그림 3.6 의 각 패널은 각각의 행 표기 및 열 범례 이름표로 주어지는 특정 변수 구성 쌍 한 묶음에 해당하는 일종의 산점도(scatterplot)를 상징합니다.

For example, the scatterplot directly to the right of the word "Balance" depicts `balance` versus `age`, while the plot directly to the right of "Age" corresponds to `age` versus `cards`.
단적인 예로, "Balance" 라는 단어 바로 우측에 놓여 있는 산점도는 `balance` 대 `age` 양상을 상세히 묘사하고 있는 반면, 곧장 "Age" 단어 바로 오른쪽 편을 차지하고 나열된 플롯 그림의 경우는 `age` 요소에 맞대응하는 `cards` 비율을 뚜렷이 나타냅니다.

In addition to these quantitative variables, we also have four qualitative variables: `own` (house ownership), `student` (student status), `status` (marital status), and `region` (East, West or South). 
우리는 앞서 언급된 이러한 다양한 정량적 변수들 이외에도 특수한 목적으로 구비된 통상 네 가지의 정성적인 변수들을 함께 보유하고 있습니다: 그것들은 바로 `own` (주택 소유 여부), `student` (학생 신분 여부), `status` (결혼 상태), 그리고 `region` (동부, 서부 또는 남부 거주 지역) 등입니다.

---

## Sub-Chapters (하위 목차)

### Predictors with Only Two Levels (수준이 2개인 예측 변수)
* [문서로 이동하기](./3_3_1_1_predictors_with_only_two_levels/)

남성/여성과 같이 단 두 가지 범주만 갖는 단순한 질적 변수를 0과 1의 값으로 매핑해 기초적인 회귀 분석을 수행하는 방법을 봅니다.
각 더미 코딩이 계수 해석에 미치는 영향을 확인합니다.
"""

with open(r'd:\site\jinydev\Statistical\src\book\c03\3_3_other_considerations_in_the_regression_model\3_3_1_qualitative_predictors\index.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

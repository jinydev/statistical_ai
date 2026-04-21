---
layout: default
title: "trans1"
---

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans1.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.4 Multiple Logistic Regression
# 4.3.4 다중 로지스틱 회귀 (Multiple Logistic Regression)

We now consider the problem of predicting a binary response using multiple predictors. By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:
우리는 이제 다수의 복수 예측 변수들을 사용하여 이진 형태의 응답을 예측하는 문제를 고려합니다. 3장에서 배운 단순 선형 회귀에서 다중 선형 회귀로의 수학적 확장 방식에 빗대어 유추해 보건대, 우리는 (4.4) 식을 다음과 같이 여러 개의 예측 변수로 확연히 일반화시킬 수 있습니다:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.6)
$$

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.7)
$$

Just as in Section 4.3.2, we use the maximum likelihood method to estimate $\beta_0, \beta_1, \dots, \beta_p$.
4.3.2 섹션에서 진행했던 것과 완벽히 동일한 전개로, 여기서도 예측할 가중치들 $\beta_0, \dots, \beta_p$ 를 피팅하기 위해 최대 우도법(Maximum Likelihood Method)을 씁니다.

Table 4.3 shows the coefficient estimates for a logistic regression model that uses `balance` , `income` (in thousands of dollars), and `student` status to predict probability of `default`. There is a surprising result here. The _p_-values associated with `balance` and the dummy variable for `student` status are very small, indicating that each of these variables is associated with the probability of `default`.
표 4.3은 신용카드 잔고(`balance`), 연간 소득(`income`, 천 단위), 그리고 학생 여부(`student`)를 한꺼번에 모두 사용하여 파산 확률을 예측하는 다중 로지스틱 회귀 모델의 회귀 계수 추정 성적표를 보여줍니다. 여기서 아주 놀라운 결과가 나타납니다. 잔고와 학생 여부 더미 변수 양쪽에 달린 _p_-값이 모두 극도로 작게 떠서, 이 변수들 각각이 독자적으로 파산 확률에 영향을 미치고 있음을 확고히 짚어냅니다.

However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than nonstudents. In contrast, the coefficient for the dummy variable is positive in Table 4.2. How is it possible for student status to be associated with an _increase_ in probability of default in Table 4.2 and a _decrease_ in probability of default in Table 4.3?
그러나 더 놀라운 점은 표 안의 학생 더미 변수 계수 기호가 음수(-)라는 사실이며, 이는 일반인보다 학생이 도리어 파산을 덜 일으킬 기조가 강함을 가리킵니다. 앞선 표 4.2에서의 단일 더미 변수 계수는 양수(+)였는데 이것과 완전히 상반됩니다. 대체 학생 지위와 파산 확률의 관계가 단일 변수 상태인 표 4.2에서는 확률의 '증가'였다가, 다중 변수 상태인 표 4.3에 오면서 확률의 '감소'라는 음수 방향으로 갑자기 역전당하는 모순이 이 수리적 모형에서 어떻게 성립할 수 있습니까?

The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox. The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance. The negative coefficient for `student` in the multiple logistic regression indicates that _for a fixed value of_ `balance` _and_ `income`, a student is less likely to default than a non-student. Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of `balance`. But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of `balance` and `income`, suggest the opposite effect: the overall student default rate is higher than the non-student default rate. Consequently, there is a positive coefficient for `student` in the single variable logistic regression output shown in Table 4.2.
그림 4.3의 왼쪽 패널은 이 명백해 보이는 역설의 모순을 설명해 줄 훌륭한 힌트 그래픽을 제공합니다. 주황색과 파란색 실선은 변수인 신용카드 잔고 비용에 따른 학생과 비학생 집단 전체의 각각의 파산 비율 평균치를 묘사합니다. 다중 로지스틱 회귀 모델 내부에서 도출된 부정적인 음수 모델 더미 가중치는, 통장 잔고와 수입이 어느 특정 수치로 완벽하게 '고정'되어 있는 조건하에서는, 학생이 일반 직장인보다 신용 불량이 터질 가능성이 대조군 대비 상대적으로 떨어짐을 의미합니다. 참으로 그러하게, 왼쪽 그림 4.3 패널에서 학생 파산 궤적 실선이 모든 X축 잔고 지점 내에서 일반인 궤적을 뚫지 못하고 발바닥 밑에서 깔려 움직이는 것을 볼 수 있습니다. 그러나 그래프 하단에 그어진 점선(모든 잔고나 수입을 뭉뚱그려 학생 평균 낸 수치) 체납률 선은 정반대의 상황을 시사합니다: 압도적으로 전체적인 학생 평균 체납률 점선은 일반인 체납 평균 점선보다 높게 찍힙니다. 그렇기 때문에 단순히 변수를 다 묶어 오직 하나의 통 스위치만 관찰하는 단일 회귀로 그려진 표 4.2 에서는 양수 계수가 계산되었던 것입니다.

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy. The variables `student` and `balance` are correlated. Students tend to hold higher levels of debt, which is in turn associated with higher probability of default. In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates. Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students.
그림 4.3의 오른쪽 패널은 왜 이런 불일치가 생기는지 마침내 설명을 내놓습니다. 그 비밀은 불행하게도 학생(`student`) 변수와 잔고(`balance`) 변수가 사실 서로 아주 끈끈하게 상호 연관되어 있다는 사실에 있습니다. 가난한 학생들은 태생적으로 엄청나게 높은 부채금액 빚의 늪에 빠져 있는 경향이 거대하며, 이 막무가내 빛 축적이 결국 가장 큰 체납 확률로 꼬리에 꼬리를 무는 연관을 짓게 됩니다. 즉, 무능력자인 학생 그룹이 신용 빚 카드 잔고를 일반인에 비해 무자비하게 거대하게 부풀릴 확률 자체가 높으며, 그 높은 잔고의 빚 덩어리가 결국 왼쪽 그림에서 말하는 파산 폭탄을 터뜨립니다. 그렇기 때문에 이 비참한 현상은, "만일 학생이 일반인과 완벽히 1대1로 '동일한 금액의 엄청난 빚 잔고'를 동등하게 짊어졌다면 그 일반인 어른 녀석이 학생보다 한계 체력이 더 후달려서 훨씬 더 먼저 파산한다"라는 다중 로지스틱(학생 음수)의 통찰과, "그러나 사실 평균을 통으로 내놓으면 현실에서는 학생들이 애초에 저 턱없는 무지막지한 고도 잔고에 진입하는 평균 빈도가 일반인보다 압도적으로 훨씬 무식하게 높기 때문에, 통으로 퉁쳐 계산하면 그냥 학생 그룹이 전체적으로 체납 파산율이 미친 듯이 더 높다"라는 현실 사이의 이중 결론을 내주게 됩니다.

This is an important distinction for a credit card company that is trying to determine to whom they should offer credit. A student is riskier than a non-student if no information about the student’s credit card balance is available. However, that student is less risky than a non-student _with the same credit card balance_!
이것은 카드를 뚫어주려는 대부 상환 업체에게 누구에게 카드 발급을 승인해 주어야 하는지 결정지을 엄청나게 중요한 통찰 기준이 됩니다! 만일 그 학생의 신용 카드 부채 '잔고' 장부 정보가 완전히 블라인드 처리되어 가려져 있는 상태라면 그냥 닥치고 일반인보다 그 학생 가입자를 발급 거절시켜 끊어내는 게 훨씬 나을 정도로 위험합니다. 하지만 그 학생 가입자가 들이민 장부가, **"신용카드에 동일한 금액의 악성 대출 잔고 빚을 한가득 이고 있는 어떤 일반인 아저씨 가입자"와 동일 조건 선상**에서 맞붙는다면 오히려 그 아저씨 쪽을 카드 거절하는게 훠씬 위험에서 탈피하는 길입니다!

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant. As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors. In general, the phenomenon seen in Figure 4.3 is known as _confounding_.
이 심플하고 극적인 예제는 여러 개의 중추적인 변수들이 다닥다닥 서로 치명적으로 얽혀 관련되어 있는 현실적 상황에서, 딸랑 단 하나뿐인 일차원 예측기만을 달랑 끼워 넣고 회귀 돌리기 시도를 했을 때 초래될 치명적인 위험성과 그 미묘한 오해석 결과 차이를 완전히 적나라하게 묘사해 냅니다. 선형 회귀 환경에서와 매한가지로, 오로지 단일 변수만 가지고 도출된 해석값은 이 예측 변수들끼리 서로 뒤에서 깊게 상관관계 짬짜미를 하고 엮여있을 때, 다중 예측기를 죄다 때려 박아 넣고 나온 다차원 결과물과 가치관이 180도 역전되는 아주 다른 결과물을 초래할 수 있습니다. 일반적으로, 그림 4.3과 엮인 이 모순적인 착시 현상을 우리는 통계학 용어로 **교란(Confounding)** 이라고 칭합니다.

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions. For example, a student with a credit card balance of $1,500 and an income of $40,000 has an estimated probability of default of
표 4.3의 모든 계수를 회귀 다중 확률 식 4.7 에 쏟아부어 대입시킴으로써 우리는 마침내 예측 계산을 돌립니다. 예를 들어, 신용카드 빚 잔액이 잔고에 \$1,500 가 찍혀있고 연 소득이 \$40,000 에 빛나는 어느 훌륭한 대학생 한 명에 대한 추정 파산 확률은 이와 같습니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}} = 0.058
$$

A non-student with the same balance and income has an estimated probability of default of
반면 저 훌륭한 대학생과 완벽히 "동일한" 대출 잔고 빚을 달고 있고 똑같은 돈을 벌어들이는 일반 직장인의 추정 파산 확률은 무려 두 배로 상승합니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}} = 0.105
$$

(Here we multiply the `income` coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with `income` measured in units of $1,000.)
(여기서 주의할 점이 수식 대입에 소득을 계산할 때 우린 $40,000 을 다 집어넣지 않고 40만 넣었습니다. 그 이유는 표 데이터가 애초에 1천 달러 단위를 기준으로 압축 세팅되었기 때문입니다)

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans1.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans1.html)

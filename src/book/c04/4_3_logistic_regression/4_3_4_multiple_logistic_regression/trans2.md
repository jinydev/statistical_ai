---
layout: default
title: "trans2"
---

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans2.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.4 Multiple Logistic Regression
# 4.3.4. 다중 로지스틱 회귀 (변수들의 앙상블과 배신)

We now consider the problem of predicting a binary response using multiple predictors.
단일 무기를 넘어, 이제 우리는 여러 개의 복수 예측 변수 단서들을 다발로 엮어 쏘아 올려 이진 정답(Yes or No)을 예측해 내는 차원의 문제를 논의합니다.

By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:
마치 3장 시절, 단순 선형 회귀가 여러 기울기를 얹으며 다중 선형 회귀로 자연스레 몸집을 불리며 진화했던 것과 똑같은 스텝으로 비유($X_1$, $X_2$...$X_p$)해 보건대, 식을 이렇게 화려하게 일반화할 수 있습니다:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.6)
$$

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.7)
$$

Just as in Section 4.3.2, we use the maximum likelihood method to estimate $\beta_0, \beta_1, \dots, \beta_p$.
길어봤자 원리는 같습니다. 앞전 4.3.2 섹션에서 써먹었던 위대한 그 무기, 최대 우도법(Maximum Likelihood Method) 기계에 데이터를 넣고 돌려서 $\beta_0, \beta_1, \dots, \beta_p$ 파라미터 추정치들을 우수수 뽑아냅니다.

Table 4.3 shows the coefficient estimates for a logistic regression model that uses `balance` , `income` (in thousands of dollars), and `student` status to predict probability of `default`.
결과표 4.3은 신용카드 빚 잔고(`balance`) 정보, (천 달러 단위로 압축된) 연간 수입(`income`), 그리고 대상이 불우한 `student` (학생) 신분인지 상태를 모두 한꺼번에 버무려 구동시킨 다중 로지스틱 회귀 모형의 계수 점수표를 적나라하게 보여줍니다.

There is a surprising result here.
그런데 이 표를 들여다보면 아주 통수 치는 반전 결과가 숨어 있습니다.

The _p_-values associated with `balance` and the dummy variable for `student` status are very small, indicating that each of these variables is associated with the probability of `default`.
일단 잔고 변수와 학생 더미 변수 항목 양쪽에 뜬 심판 점수 _p_-값은 무섭도록 작게 찍혔습니다. 즉, 잔고든 학생 여부든 둘 다 불길한 체납 확률에 통계적으로 강한 영향을 끼치는 진짜 단서임은 자명합니다.

However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than nonstudents.
하지만 충격적이게도 표에서 `student` 학생 더미 변수에 붙은 $\beta$ 계수가 '마이너스(-)' 음수로 책정되었습니다! 이건 뭐죠? "오히려 학생 그룹이 일반 비학생들보다 부채 체납을 훨씬 덜 내고 모범적으로 생활한다"는 역방향의 결과를 대놓고 가리키고 있습니다.

In contrast, the coefficient for the dummy variable is positive in Table 4.2.
잠깐만요, 혼란스럽습니다. 불과 한 장 전 단일 회귀만 돌렸던 표 4.2에서는 분명히 학생 더미 계수가 '플러스(+)' 양수였지 않습니까? (즉 "학생들이 더 파산한다!" 였죠.)

How is it possible for student status to be associated with an _increase_ in probability of default in Table 4.2 and a _decrease_ in probability of default in Table 4.3?
도대체 어떻게 같은 데이터를 쓰는데도 어떤 때는 학생 신분이 체납 확률의 **증가(+ 증가)** 였다고 삿대질을 하고(표 4.2), 다중 변수를 묶었답시고 갑자기 표 4.3에서는 파산 확률을 억제하는 **감소(- 감소)** 요인이라고 180도 표변해 모순된 말을 뱉어내는 버그가 터진 걸까요?

The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox.
그림 4.3의 영리한 왼쪽 패널 도화지가 이 미치고 팔짝 뛸 명백한 모순 역설을 깔끔하게 해명하는 통찰 그래픽을 펼쳐 줍니다.

The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance.
그림 속 X축으로 뻗어간 그 무서운 신용 카드 잔고 금액 게이지에 따라 학생(주황색)과 일반인(파란색) 집단이 각각 내뿜는 파산 비율 흐름이 두 줄기의 실선으로 그려져 있습니다.

The negative coefficient for `student` in the multiple logistic regression indicates that _for a fixed value of_ `balance` _and_ `income`, a student is less likely to default than a non-student.
사실 다중 로지스틱 표에서 떴던 학생 계수의 음수 표기는 "다른 변수들의 개입 통제"라는 전제 조건이 붙습니다. 즉, 잔고 게이지와 소득 게이지를 어느 **특정 지점에 강제로 묶어 고정(fixed value)** 시키고 놓고 경쟁을 붙이면, 놀랍게도 같은 빚더미 악재 속에서는 학생이 일반인 아저씨들보다 오히려 파산 압박을 견디고 버텨낼 확률 기강이 낫다는 뜻입니다.

Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of `balance`.
그림을 유심히 뜯어보면 참말임이 입증됩니다. 왼쪽 패널에서 X축 잔고를 아무 위치에서나 칼로 수직 틈을 썰어 비교해 봐도, 늘 주황색(학생 파산 실선)이 파란선(일반인 파산선)보다 밑에 짓눌려(안전하게 방어되어) 위치하고 있음을 명백하게 관찰할 수 있습니다.

But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of `balance` and `income`, suggest the opposite effect: the overall student default rate is higher than the non-student default rate.
그러나! 그래프 도화지 가장 바닥 쪽 허공에 평행하게 쭉 그어진 불길한 수평 점선 두 줄기(이건 X축 잔고 스펙트럼 따위를 고려 안 하고 그냥 학생 인구 전체를 뭉뚱그려 통계로 내버린 멍청한 평균 체납률 선)를 보면, 상황이 역전됩니다. 압도적으로 전체적인 학생 파산율 선이 일반인 선보다 더 상단 위험구역에 찍힙니다. 

Consequently, there is a positive coefficient for `student` in the single variable logistic regression output shown in Table 4.2.
그렇기 때문에, 잔고(`balance`) 정보 통제 따위를 싹 무시해 버리고 오직 `student`라는 단일 변수 변인 딱 하나만 넣고 돌린 표 4.2의 가짜 성적표에서는 뭉뚱그려진 참사가 벌어져 "학생이 더 끔찍하게 파산한다(+ 양수)"는 우스꽝스러운 기만 결과가 떴던 것입니다.

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy.
오른쪽 패널로 넘어오면 왜 집단이 뭉뚱그려지면 저 꼴이 나는지 이 미친 불일치의 진상을 확실히 해명해 보여줍니다.

The variables `student` and `balance` are correlated.
이 비극의 원인은 사실 `student` 신분이라는 변수 자체가 불행하게도 잔고 부채 `balance` 변수 지표와 어마어마하게 뒤에서 상호 간의 강한 상관 상관관계(Correlated)로 오염되어 밀착되어 있다는 점입니다.

Students tend to hold higher levels of debt, which is in turn associated with higher probability of default.
태생적으로 돈 없는 학생들은 필연적으로 무지막지하게 높은 대출 부채 빚의 늪에 빠져 축적하는 경향이 짙으며, 결국 이 산더미같이 쌓인 빚고리가 연달아 파멸의 파산 터닝 확률로 도미노처럼 무너져 내리는 겁니다.

In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates.
다시 말해 요약하자면, 학생이란 집단 자체가 거대한 카드 대출금의 화약고를 등에 지고 살 가능성이 농후하고 팽배하며, 우리가 이미 왼쪽 그림에서 뼈저리게 목격했듯 바로 그 '압도적 고잔고 위치 게이지'가 종국엔 그들의 체납 폭탄 스위치를 당겨버립니다.

Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students.
따라서 이 딜레마를 정리하면: "**동일선상의 카드 부채 잔고**를 짊어맨 한 개인 단위 경쟁으로 비교하면 학생이 일반 성인 직장인보다 파산 회피 방어력이 월등히 뛰어나지만, 안타깝게도 **전체 학생 청년 군집체**로 무리지어 놓고 평균을 내버리면 이들 대다수가 태생적으로 살인적인 대출 고잔고 포지션 위치를 점유당한 상태이기 때문에, 결국 나라 전체적으로는 통계상 학생이 평균 체납을 훨씬 더 빈번하게 저지르는 집단으로 표변해버린다" 라는 착시적 의미가 풀리게 됩니다.

This is an important distinction for a credit card company that is trying to determine to whom they should offer credit.
이 짜릿한 진실 분별력은, 눈 먼 카드 신청자 고객들 중에서 누구 목에 신용카드를 발급 통과시켜 쥐어줄 것 인지를 판가름하려는 눈치 싸움 대부 신용카드 회사에게는 그야말로 비즈니스의 목줄을 좌우할 어마어마하게 중요한 통찰적 구분입니다.

A student is riskier than a non-student if no information about the student’s credit card balance is available.
만약 심사관 입장에서 신청 학생의 뒷배경인 '통장 잔고 부채' 장붓빛 내역을 전혀 열람할 길이 없는 장님 상태라면, 그 학생을 덥석 받아주는 건 아무 직장인이나 골라 받는 것보다 훨씬 더 파멸을 초래할 위험합니다.

However, that student is less risky than a non-student _with the same credit card balance_!
하지만 번뜩이는 통찰로 상황을 틀어보자면, 그 대학생 손님이 **"자신과 완전히 똑같은 조건의 엄청난 빚 잔고를 안고 있는 어떤 직장인 경쟁자"** 와 심사대 책상에서 붙는다면, 통계학적으로 그 불우한 직장인 쪽을 가차 없이 날려버리고 학생 고객에 투자하는 게 자산 포트폴리오를 구하는 체납 리스크 축소의 묘수라는 겁니다!

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant.
이 소름 돋게 심플하면서도 치명적인 일화는, 복잡한 현실에서 여러 다른 변수 조력자들이 범행에 심오하게 가담하고 있을 때, 그저 단순하게 눈에 보이는 허술한 단일 예측 단서 하나만 툭 던져놓고 회귀 분석을 돌려버렸을 때 벌어질 대 참사와 그로 인한 잘못된 정책 결정의 끔찍한 오해석 위험성을 낱낱이 파헤쳐 묘사해 줍니다.

As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors.
3장 선형 회귀 모래사장에서 뛰어놀 때와 똑같이 자명하게, 멍청하게 한 개의 무기(예측 변수)만 단독으로 투입해 얻은 오염된 시야 정보는 다수의 변수를 모두 결합해 도출한 삼차원 다중 시야 결론과 180도 통수 반대 방향의 결과를 내뿜을 수 있기 때문에, 유독 변수들끼리 보이지 않는 끈끈한 결탁 상관관계(Correlation)가 존재할 경우 특히 분석가는 모니터 앞에서 정신줄을 바짝 잡고 극도로 예민하게 행동해야 합니다.

In general, the phenomenon seen in Figure 4.3 is known as _confounding_.
이처럼 통계 분석가들의 뒤통수를 치며 어둠 속에서 그래프 선들을 교묘하게 뒤틀어버리는 4.3 그림 속의 숨겨진 보스 착시 현상을, 우리 통계학자들 세계에서는 **교란(Confounding)** 이라는 불명예스러운 저주 타이틀 명칭으로 호명합니다.

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions.
교란의 안개를 걷어내고 표 4.3에서 구해낸 정직한 다중 회귀 계수들을 대규모(4.7) 공식 방정식 세트에 무자비하게 욱여넣어 대입함(substituting)으로써, 우리는 이제야 진짜 공정한 실전 예측 사격을 뽑아낼 수 있습니다.

For example, a student with a credit card balance of $1,500 and an income of $40,000 has an estimated probability of default of
예를 들어, 통장에 빚 잔고가 \$1,500 정도 쌓여있지만 연 소득 벌이가 \$40,000 에 매달린 가여운 한 학생의 추정 파산 폭발 게이지는 다음과 같습니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 1}} = 0.058
$$

A non-student with the same balance and income has an estimated probability of default of
반면 그 잘난 비학생 어른 직장인이 위 훌륭한 대학생과 완벽히 저울처럼 잔고 빚과 연봉을 똑같이 달고 있다면? 놀랍게도 그 비학생 도전자 어른의 파산 터닝 추정 확률은 이렇게 뒤집힙니다:

$$
\hat{p}(X) = \frac{e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}}{1 + e^{-10.869 + 0.00574 \times 1500 + 0.003 \times 40 - 0.6468 \times 0}} = 0.105
$$
(약 두 배 가량 더 체납 파산에 취약함을 보여줍니다!)

(Here we multiply the `income` coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with `income` measured in units of $1,000.)
(주의: 수식 공식 대입 연산 과정에서 우리는 촌스럽게 40,000이라는 원본 수치를 통째 곱하지 않고 표 4.3 계수에 날렵하게 숫자 40만 슬그머니 곱해줍니다. 그 비밀은 애당초 그 거대한 모형 표의 솥단지 크기가 세팅될 때 수입 데이터 자체가 1,000달러 단위로 압축 변환 적용되었기 때문입니다!)

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.3.3 Making Predictions](../4_3_3_making_predictions/trans2.html) | [4.3.5 Multinomial Logistic Regression >](../4_3_5_multinomial_logistic_regression/trans2.html)

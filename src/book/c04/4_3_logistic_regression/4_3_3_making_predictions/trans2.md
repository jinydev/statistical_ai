---
layout: default
title: "trans2"
---

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans2.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.3 Making Predictions
# 4.3.3 예측하기 (확률 머신에 타깃 밀어 넣기)

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a `balance` of $1,000 is
자, 이제 피나는 작전으로 $\beta$ 계수 다이얼들이 완벽하게 정상 조율(추정)되고 나면, 우리의 이 확률 머신은 눈앞에 떨어진 그 어떠한 임의의 낯선 신용카드 잔고 액수에 대해서도 여지없이 무자비한 체납(`default`) 파산 적중 확률을 즉각 수학 통계식으로 계산해 투척 낼 위력을 갖춥니다. 예를 들어, 방금 전 구했던 표 4.1의 방정식 부품 결과에 세팅된 계수 산출물들을 척척 기계에 물려 이용할 시, 현재 카드 빚 계좌 잔고가 딱 \$1,000 인 어느 특정 불운한 개인 타깃 구역에 대한 치명적 파산 도주 확률은 다음과 같이 곧 예측 연산 도출됩니다.

$$
\hat{p}(X) = \frac{e^{-10.6513 + 0.0055 \times 1000}}{1 + e^{-10.6513 + 0.0055 \times 1000}} = 0.00576
$$

which is below 1%. In contrast, the predicted probability of default for an individual with a `balance` of $2,000 is much higher, and equals 0.586 or 58.6%.
수식 처리망 산출 계산 결과 $0.00576$ 이 구태 튀어나왔으며, 이는 직관 환산으로 고작 1%도 채 안 되는 매우 빈약 낮은 안도 수치입니다. 하지만 이와는 극단적 정반대로, 만약 동일한 그 확률 머신 기계 구역에 무려 두 배인 잔고 빚 통장에 \$2,000 거액이 적자 들어있는 더 위험한 특정 개인 타깃을 밀어 넣었을 경우, 연동 예상 도주 파산 배 쨀 확률 지표 수치는 거침없이 훨씬 더 폭발 치솟으며 순식간에 **0.586**, 퍼센트 직관으로 단연 환산 시 무려 **58.6%** 에 절망 육박하게 되는 극단 국면에 처합니다.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the `Default` data set contains the qualitative variable `student` . To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students.
단지 숫자 점수만 들어가는 게 아닙니다! 우리는 앞선 기초 3.3.1 구역 단원에서 지겹게 써먹어 배웠던 통계의 꼼수 대마왕인 **더미 변수(Dummy Variable) 0/1 스위치 접근법**을 능수 능란 거듭 가져와서, 이 고상한 S자 로지스틱 확률 회귀 커브 모델 입구 안에 '혈액형'이나 '성별' 같은 문자로 된 '질적(문자형 특성)' 단서 예측 투기 변수까지도 얼마든지 속임수 교란 밀어 엮어 넣을 수입 단연 있습니다. 생생한 일례로 본 모의 `Default` 실습 데이터 상자 세트는 이 당사자가 고달픈 '학생'이냐 아니냐를 명시 나타내는 특수 질적 범주 변수 꼬리표인 `student` 기록을 낱점 품고 포함하고 있습니다. 오직 딴 거 없이 이 '학생인지 직장인인지 여부 신분값' 만을 단독 주요 단서 예측 타깃 변수로 점찍어 삼아 굴려 구동되는 로지스틱 확률 S자 판별 모델을 따로 돌려 훈련하기 위해서는, 우린 그저 단순 명쾌하게 당사자가 '학생' 표찰이면 '1' 값으로 덜컥 전원 스위치 불이 켜지고 만약 '학생이 아니면(일반인이면)' 매정하게 '0' 전원 코드가 차단 들어가는 분별 대리인 전담 더미 변수를 하나 요리 창조해 기입 내기만 하면 만사형통 단연 완료됩니다.

The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated _p_-value is statistically significant. This indicates that students tend to have higher default probabilities than non-students:
오직 이 빈약 단일한 양분 스위치 '학생 신분 변수 하나'만을 구동 투입해서 체납 배상 채무 예측 불이행 파산율을 뚝딱 파생 예측해 산출 낸 또 다른 한 줄 로지스틱 뱀 모형의 처참 결과표는 교재 본문의 표 4.2 도해에서 적나라 확인하실 단연 수 있습니다. 저 '학생 여부 감별하는 대리 더미 변수' 소켓 자리에 도출 할당된 도출 조종타 계수는 무조건 양수(Positive, +)의 솟구침 방향이며, 그에 연달아 옆에 찰싹 붙어있는 심판 점수 _p_-값의 극소 수위는 통계적으로 결단코 부인 회피할 수 없는 기여 심각하게 철통 유의미한 합격 보증 수준입니다. 맙소사, 이것은 수치 명확하게 **우리의 그 가여운 '학생 신분' 꼬리표를 단 청춘 사람들의 구역 그룹이 돈 잘 버는 직장인 등 동반 일반인 층보다 (동일 기준 조건상) 절대 평균적으로 훨씬 더 큰 파산 단절 벼랑 끝 불량 도주 단연 체납 확률의 요동 경향**이 있다는 서러운 팩트 폭격을 우리에게 명시 지목합니다: 계산 수식 대입 팩트는 아래와 같이 단락 차이가 참혹 도출됩니다.

$$
\begin{align*}
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{Yes}) &= \frac{e^{-3.5041 + 0.4049 \times 1}}{1 + e^{-3.5041 + 0.4049 \times 1}} = 0.0431 \text{ (학생: 4.31\%)} \\
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{No})  &= \frac{e^{-3.5041 + 0.4049 \times 0}}{1 + e^{-3.5041 + 0.4049 \times 0}} = 0.0292 \text{ (일반인: 2.92\%)}
\end{align*}
$$

This is the document for this topic.
이 파트는 이 단막 파산 확률 산출 주제를 직관 체감 논단 수단 위해 구축 기술 거진 적재된 요약 해설 첨부본 조 문서 양식입니다.

---

## Sub-Chapters

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans2.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans2.html)

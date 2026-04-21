---
layout: default
title: "trans2"
---

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans2.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.3 Making Predictions
# 4.3.3. 예측하기 (내 파산 확률은 몇 프로?)

Once the coefficients have been estimated, we can compute the probability of `default` for any given credit card balance.
지난 챕터에서 그 무시무시한 $\beta$ 계수들을 컴퓨터가 모두 계산하고 추정했다면, 이제 끝났습니다! 우리는 그 방정식에 신용카드 잔고 수치를 동전 넣듯 밀어 넣기만 하면 즉시 파산(`default`)이 날 확률값을 환산해 계산할 수 있습니다.

For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a `balance` of $1,000 is
예를 들어, 4.1번 표 성적표에 나왔던 도출 계수 추정치 재료를 식에 대입해 보면, 현재 통장에 간당간당 \$1,000 잔고가 있는 어떤 소시민 개인이 향후 파산 늪에 빠질 예측 확률 공식은 다음과 같이 작동합니다:

$$
\hat{p}(X) = \frac{e^{-10.6513 + 0.0055 \times 1000}}{1 + e^{-10.6513 + 0.0055 \times 1000}} = 0.00576
$$

which is below 1%.
산출 결과는 0.00576. 즉 전체 1% 확률의 캡에도 못 미치는 굉장히 안전하고 낮은 수준입니다. 안정권이죠!

In contrast, the predicted probability of default for an individual with a `balance` of $2,000 is much higher, and equals 0.586 or 58.6%.
이와는 정반대로 경각심을 울리는 경우를 봅시다. 잔고 빚액이 따블로 뛰어 무려 \$2,000 이 들어있는 개인을 검사하면 계산된 파산 예측 확률 수치가 0.586으로 터무니없이 치솟아 뻗어갑니다. 퍼센트 차원으로 따지면 체납 터질 확률이 무려 58.6%에 달하는 시한폭탄 상태입니다!

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1.
우리는 숫자가 아닌 글자 데이터와 직면했을 때, 옛날 3.3.1 단원에서 전수받았던 통계 지식인 0과 1 **더미 변수(Dummy Variable) 대리인 접근법**을 슬쩍 가져와서, 이 로지스틱 회귀 모델 안에 '질적(문자형)' 예측 변수를 마음껏 끼워 넣을 수 있습니다.

As an example, the `Default` data set contains the qualitative variable `student` .
실제 사례로 돌려볼까요? 이 `Default` 실습 데이터셋의 뒤편에는 숫자로 표기되지 않는 사람의 직업 유형, 즉 학생이냐 직장인이냐를 따지는 질적 변수 `student` (학생 여부) 열이 들어있습니다.

To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students.
오직 내가 가방 끈이 긴 학생인지 아닌지만을 쫓는 예측 단서로 모델을 돌려 피팅하기 위해서는, 복잡할 것 없이 그저 "너 학생이면 1 번호표, 아니면 0"이라고 마킹하는 특수 스위치용 더미 변수를 하나 쓱싹 생성해 주면 만사 오케이입니다.

The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2.
이 학생 신분 더미 변수만을 덜렁 써서 도출해 낸 파산 확률 로지스틱 모형 예측 기계표는 이어지는 표 4.2에 공개되어 있습니다.

The coefficient associated with the dummy variable is positive, and the associated _p_-value is statistically significant.
결과표에서 더미 변수에 붙은 $\beta$ 계수를 살펴보면 (+) 양수 숫자가 찍혀있고, 이와 짝꿍인 _p_-값 심판 점수도 무참히 작게 떠서 통계적으로 매우 신뢰할만 하고 유의미한 수준에 도달합니다.

This indicates that students tend to have higher default probabilities than non-students:
자, 양수 계수라는 이 명백한 사인 정보는, 사회에서 일반인들보다 학생 그룹 무리들이 압도적으로 훨씬 더 높은 연체 파산 확률에 직면하는 경향이 짙다는 사실을 적나라하게 폭로합니다. 실제 예측 식은 다음과 같습니다:

$$
\begin{align*}
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{Yes}) &= \frac{e^{-3.5041 + 0.4049 \times 1}}{1 + e^{-3.5041 + 0.4049 \times 1}} = 0.0431 \\
\hat{\text{Pr}}(\text{default} = \text{Yes} \mid \text{student} = \text{No})  &= \frac{e^{-3.5041 + 0.4049 \times 0}}{1 + e^{-3.5041 + 0.4049 \times 0}} = 0.0292
\end{align*}
$$

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.3.2 Estimating The Regression Coefficients](../4_3_2_estimating_the_regression_coefficients/trans2.html) | [4.3.4 Multiple Logistic Regression >](../4_3_4_multiple_logistic_regression/trans2.html)

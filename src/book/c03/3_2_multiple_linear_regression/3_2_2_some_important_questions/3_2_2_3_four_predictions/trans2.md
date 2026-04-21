---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/trans2.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/trans2.html)

# Four: Predictions

# 질문 4: 예측 (자, 그래서 내일 매출 얼마나 나오는데?)

Once we have fit the multiple regression model, it is straightforward to apply (3.21) in order to predict the response $Y$ on the basis of a set of values for the predictors $X_1, X_2, \dots, X_p$.
드디어 다중 회귀 모델(짬뽕 레시피)이 완벽하게 세팅되었습니다! 이제 남은 일은 식당 사장님이 던져주는 "내일 마늘 3쪽($X_1$), 대파 2뿌리($X_2$) 넣을 건데 매출($Y$) 얼마 나올 거 같아?" 하는 질문에 공식 (3.21) 자판기를 두드려 단순하게 대답(예측)해 주는 것뿐입니다. 아주 간단하죠.

However, there are three sorts of uncertainty associated with this prediction.
하지만 잠깐! 사장님께 자신만만하게 내일 매출 숫자를 뱉어내기 전에, 그 예언의 뒷골을 서늘하게 만드는 '3가지 치명적인 불확실성(함정)'이 도사리고 있다는 걸 반드시 명심해야 합니다.

1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \dots, \beta_p$. That is, the _least squares plane_
1. 첫째 함정: 우리가 머리 싸매고 구한 기울기 짝퉁 수치들($\hat{\beta}_0, \dots, \hat{\beta}_p$)은 결국 신(우주의 진실)이 감춰둔 극비 진짜 정답($\beta_0, \dots, \beta_p$)을 대충 흉내 낸 '어설픈 추정치(가짜 원본)'에 불과하다는 점입니다. 좀 유식하게 말해볼까요? 우리가 도화지에 깔아 놓은 철판때기, 즉 _최소 제곱 평면(Least Squares Plane)_ 이 녀석,
$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p
$$

is only an estimate for the _true population regression plane_
이 녀석은 창조주만이 아는 우주적 진리, 즉 _참 모집단 회귀 평면(True Population Regression Plane)_ 인 다음의 진짜 절대 법칙
$$
f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p
$$
을 곁눈질로 훔쳐보고 대충 스케치한 몽타주에 불과하다는 슬픈 사실입니다.

The inaccuracy in the coefficient estimates is related to the _reducible error_ from Chapter 2. We can compute a _confidence interval_ in order to determine how close $\hat{Y}$ will be to $f(X)$.
이렇게 몽타주(추정치)가 실물(진짜 정답)과 다를 수밖에 없는 찝찝함은 우리가 2장에서 배웠던 '우리가 노력하면 줄일 수 있는 오차(Reducible error)' 부류에 해당합니다. 몽타주 화가(우리 모델)가 그린 가짜 얼굴 $\hat{Y}$ 가 신의 진짜 얼굴 $f(X)$ 와 얼마나 소름 돋게 비슷한지 점수를 매기기 위해, 우리는 통계학의 보호막인 **_신뢰 구간(Confidence interval, 오차 방어막)_**을 계산하게 됩니다.

2. Of course, in practice assuming a linear model for $f(X)$ is almost always an approximation of reality, so there is an additional source of potentially reducible error which we call _model bias_.
2. 둘째 함정: 솔직해집시다. 실전 장사판에서 복잡다단한 우주의 진리 $f(X)$ 가 저렇게 딱딱하고 뻣뻣한 '선형(직선/평면)' 철판 공식일 확률이 1%나 될까요? 거의 항상 현실을 너무 단순하게 타협해 버린 억지 '근사치(Approximation)'일 뿐입니다. 애초에 둥글둥글한 지구를 네모라고 우겨서 생기는 이 태생적인 억지 오차의 정체를 통계학에선 **_모델 편향(Model Bias)_**이라는 꼬리표를 붙여 추가적인 찝찝함의 원인으로 지목합니다.

So when we use a linear model, we are in fact estimating the best linear approximation to the true surface.
그러니 우리가 뻣뻣한 '선형 모델'을 쓸 때는, "우리가 진짜 우주 진리의 표면을 완벽히 복제했어!" 가 아니라 "우주의 표면에 가장 덜 어색하게 들러붙는 그나마 제일 나은 선형 판때기를 덧대봤어~" 라고 스스로 최면을 걸고 있는 셈입니다.

However, here we will ignore this discrepancy, and operate as if the linear model were correct.
(하지만 머리 아프니까 이번 장에서는 "알빠임? 우리 선형 모델이 무조건 창조주의 정답이다!"라고 뻔뻔하게 세뇌하고 퉁치고 넘어가겠습니다.)

3. Even if we knew $f(X)$ — that is, even if we knew the true values for $\beta_0, \beta_1, \dots, \beta_p$ — the response value cannot be predicted perfectly because of the random error $\epsilon$ in the model (3.20).
3. 셋째 함정 (가장 치명적): 백번 양보해서, 우리가 신과 카톡을 해서 우주의 진리 $f(X)$ 의 진짜 정답 수치($\beta$ 값들)를 답지로 빼돌렸다고 칩시다! 그래도!! 우리는 내일 매출(응답 값)을 1원 단위까지 완벽하게 스나이핑 적중 시킬 수 없습니다. 왜냐고요? 애초에 장사판에는 공식으로 설명 못 하는 도깨비 같은 돌발 변수 요정, 즉 무작위 오차 $\epsilon$ (오늘 비가 갑자기 오네? 손님이 배탈 나서 안 오네?) 가 뒤통수를 치기 때문이죠. (공식 3.20 참고)

In Chapter 2, we referred to this as the _irreducible error_. How much will $Y$ vary from $\hat{Y}$? We use _prediction intervals_ to answer this question.
2장 통계 기초반에서 우리는 이 도깨비의 장난을 인간이 어찌할 도리가 없는 **_축소 불가능한 오차(Irreducible error)_**라고 눈물지으며 명명했습니다. "도대체 진짜 내일 터질 매출 $Y$ 가 우리의 예언 $\hat{Y}$ 를 벗어나서 얼마나 미친 듯이 널뛸까?" 이 공포스러운 질문에 대비하기 위해 우리는 방패막이인 **_예측 구간(Prediction Intervals)_**을 소환합니다.

Prediction intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for $f(X)$ (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error).
외우세요! **예측 구간 마지노선은, 아까 말한 '신뢰 구간 방어막'보다 언제나 훨씬 더 뚱뚱하고 넓게 쳐집니다!** 왜냐면 이 예측 구간 안에는 화가가 몽타주를 잘못 그린 실수(축소 가능한 오차)에다가 더불어, 애초에 도깨비 요정이 미친 듯이 날뛰어 개별 손님 변수(개별 지점)가 본래 궤도를 이탈해 날아갈 위험성(축소 불가능 영역 오차)이라는 최악의 두 가지 불확실성 짐 덩어리가 모두 더블로 얹혀 짬뽕되어 있기 때문입니다.

We use a _confidence interval_ to quantify the uncertainty surrounding the _average_ `sales` over a large number of cities.
실무 예시로 구분해 보죠! 만약 시장님이 "우리 동네 **전체 수백 개 가맹점 투입 예산 대비 대략적인 '평균 매출'**이 얼마나 될까?" 하고 두루뭉술하게 물어보면 우리는 **_신뢰 구간(Confidence interval)_**을 써서 대답합니다.

For example, given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in each city, the $95\%$ confidence interval is $[10,985, 11,528]$.
가령, 각 동네마다 TV에 사이좋게 10만 달러, 라디오에 2만 달러를 똑같이 뿌린다고 쳤을 때 우리 통계청의 95% 꽉 찬 신뢰 구간 예측은 대략 **"[10,985 달러 ~ 11,528 달러] 박스권"** 안에서 평균 매출이 움직일 거라고 좁직하게 브리핑을 때릴 수 있죠.

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $f(X)$.[9]
이 말인즉슨, 우리가 전국 단위로 이런 통계 덩어리 냄비를 미친 듯이 무한 복제 생성해 보면, 그 형태 구간들의 95% 정도는 우주의 참 진리 평균 타겟 $f(X)$ 을 안전하게 삼키며 보위할 거란 든든한 보증 수표입니다.[9]

> [9] 좀 더 쉽게 말해 볼까요? 우리가 `Advertising` 같은 도시 100개짜리 장부를 수천수만 번 똑같은 조건(TV 10만, 라디오 2만)으로 평행우주에서 무한 반복 수집해서 매번 이 '평균 매출 신뢰 구간' 박스를 그리면요? 그 수만 개의 그려진 박스 중 무려 95%의 박스는 **창조주가 세팅한 진짜 찐 평균 매출(참값)** 을 품고 있을 거란 뜻입니다.

On the other hand, a _prediction interval_ can be used to quantify the uncertainty surrounding `sales` for a _particular_ city.
자, 상황 반전! 이번엔 A 프랜차이즈 강남 지점장이 멱살을 잡고 묻습니다. "다 필요 없고!! 그냥 **우리 강남 지점 (단일 개별 도시, 특정 particular city) 내일 매출**만 오차 없이 정확히 예언해 봐!" 이럴 땐 두루뭉술한 신뢰구간 따위는 쓰레기통에 버리고 즉각 **_예측 구간(Prediction interval)_** 이라는 현실 방패를 펴야 합니다.

Given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in that city the $95\%$ prediction interval is $[7,930, 14,580]$.
강남 1개 지점에 TV 예산 10만, 라디오 2만을 똑같이 쏟아부었을 때, 우리는 벌벌 떨며 엄청나게 넓은 95% 예측 구간 방패를 칩니다. 무려 구간이 **"[7,930 달러 ~ 14,580 달러]"**까지 태평양 터지듯 어마어마하게 광활하게 뻥튀기됩니다!!

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $Y$ for this city.
이 무지막지한 간격의 뜻은, "사장님! 강남 지점이라는 단 1개의 주사위를 굴리는 야생 장사판($Y$)에서는 도깨비 변수가 너무 쎄서, 저희가 구간을 이 정도로 태평양처럼 넓게 쳐놔야 겨우겨우 95% 확률로 진짜 내일 매출 액수를 안 빗나가고 이 그물망에 걸려들게 잡아낼 수 있습니다 ㅠㅠ" 라는 비참한 고해성사입니다.

Note that both intervals are centered at 11,256, but that the prediction interval is substantially wider than the confidence interval, reflecting the increased uncertainty about `sales` for a given city in comparison to the average `sales` over many locations.
잘 보세요, 두 구간 박스 모두 아까부터 지목당한 타겟 정중앙 과녁 중심점은 가짜 몽타주 값이 찍은 **'11,256 달라'** 로 완전히 동일합니다. 하지만! '특정 단일 지점의 단기 매출 예언(예측 구간 넓이)'이, 수백 개 지점이 서로 모여 퉁쳐진 '포괄적 두루뭉술 평균 매출 예언(신뢰 구간 넓이)' 보다 압도적으로 불확실하고 위험 부담이 곱절로 더 크기 때문에, 결과적으로 그 도깨비 난장판을 커버하기 위해 예측 구간의 넓이는 신뢰 구간 따위와는 비교도 안 될 정도로 기형적으로 뚱뚱하고 넓게 잡힐 수밖에 없는 아주 슬픈 숙명을 짊어집니다.

---

[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/trans2.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/trans2.html)

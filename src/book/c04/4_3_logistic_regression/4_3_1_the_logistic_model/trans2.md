---
layout: default
title: "trans2"
---

[< 4.3 Logistic Regression](../trans2.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.1 The Logistic Model
# 4.3.1. 로지스틱 모형 (선형 직선을 휘어서 확률에 가두다!)

How should we model the relationship between $p(X) = \text{Pr}(Y=1 \mid X)$ and $X$? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent these probabilities:
자, 우리는 도대체 어떻게 $p(X) = \text{Pr}(Y=1 \mid X)$ 확률 게이지와 예측 단서 변수 $X$ 차트표 사이의 지긋지긋한 관계성을 엮어 모델링 시뮬레이션해야 할까요? (아, 설명의 편의를 위해 범인이냐 아니냐의 종속 타깃 반응 변수에 대해선 흔하고 만만한 일반적인 0과 1 번호 코딩을 전제로 사용한다고 퉁 칩시다.) 앞서 불만투성이였던 4.2 매운맛 절에서, 우리는 이 신성한 확률치들을 단명 재현 표출해 내기 위해 막대기 선형 회귀 1차 방정식 모델을 무모하게 사용하는 억지 도출을 한 번 고래고래 고려하긴 했었습니다:

$$
p(X) = \beta_0 + \beta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance`, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1. These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1. This problem is not unique to the credit default data. Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of $X$ and $p(X) > 1$ for others (unless the range of $X$ is limited).
만약 우리가 통장 카드 빚 잔고(`balance`) 정보 뭉치를 도구로 사용해서 "얘가 곧 도망갈 거다(`default = Yes`)!" 하고 대차게 예측하기 위해 이 빳빳한 일직선 접근법을 바득바득 우기며 들이민다면, 우리는 그림 4.2 뷰어의 왼쪽 면 패널에 그려진 것과 흡사한 대참사의 억지 파괴 모델선을 얻게 됩니다. 여기서 우리는 이 엉터리 일직선 접근법 시스템의 치명적 결함 문제와 오롯이 직면 마주합니다: 만약 어느 정직한 시민의 빚 잔고가 0원에 바짝 가깝게 떨어지면 우리의 무식한 일직선 방정식은 파산 예측치를 무려 **'마이너스(-) 음수 확률'** 이라는 말도 단연 안 되는 터무니없는 비상식 파괴적 예측을 뱉어냅니다. 반대로 빚이 천문학적으로 엄청나게 거대한 빌런 재벌을 놓고 수치를 예측할 무렵엔 무적의 확률 장벽인 **'1 척도 한계치 (100%)'** 를 로켓처럼 가볍게 돌파 뚫어버리는 미친 초과 값들을 당당 구태 연연 얻어맞게 됩니다. 이런 기괴한 예측들은 전혀 이치에 부합 합치하지 않습니다. 하늘이 두 쪽 나도 누군가가 배 쨀 파산 타격률 진짜 확률이라는 것은 당사자의 빚 잔고 액수가 0원이건 수백억이건 상관없이, 백분율상 무조건 **0 과 1 마지노선 구간 안의 울타리 박스**에 갇혀 포섭 귀결되어야만 하기 단연 때문입니다! 이 멍청한 이탈 오류 결함 문제는 유독 이 신용 체납 카드 파산 데이터 집합 예제에서만 유별나게 단절 발생하는 버그가 아닙니다. 애초 0이나 1로 셋업된 태생적 극단 이분법 이진 반응 무단 변수에다가 강철 '직선 막대 선'을 깡으로 피팅해 대가리 짓누르려고 시도하는 한 그 어떤 어느 때고, 우리는 이론 구조상 구태 결함으로 항상 몇몇 극단 예측단 $X$ 입력구 지점들에서는 $p(X) < 0$ 음수 뚫림가, 혹은 또 다른 반대쪽 정점 척도들에선 $p(X) > 1$ 오버플로우가 발발 관측 터지는 참사를 언제나 이끌어 예측 생산할 수 있게 됩니다 (물론 우리가 억지로 투입구 탐색 $X$ 의 가동 진폭을 제한 자르지 않는 이상 결함은 무한대입니다). 

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of $X$. Many functions meet this description. In logistic regression, we use the _logistic function_,
이러한 괴랄 참사 불꽃 확률 이탈 버그 폭주를 기어코 막아버려 피하려면, 우리는 수학자들답게 무조건 도출 출입구에 온갖 아무 잡다한 모든 극단 값들의 $X$ 를 다 때려 넣고 대입 폭파해도 결과론적으로는 항상 출력 반환값을 안락하게 0과 1 사이 구간 진폭으로만 순하게 찍어 누르는 제어 기제 함수를 덧대어 동원해서 그 뻗침 궤적 $p(X)$ 를 재차 모델링해야만 합니다. 사실 그 무궁 함수 세계엔 이런 조건부 성질을 입맛 맞추어 교묘 충족하는 기교 함수들이 꽤나 다양 여러 있습니다. 그 수많은 후보 중에서도, 우리가 배울 주인공 기조인 저명한 **로지스틱 회귀** 조작에서는, 아주 우아하게 꺾인 **로지스틱 곡선 함수(Logistic Function)** 라는 필살기 봉쇄 도구를 전격 구태 차용해 사용합니다:

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \quad (4.2)
$$

To fit the model (4.2), we use a method called _maximum likelihood_, which we discuss in the next section. The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the `Default` data. Notice that for low balances we now predict the probability of default as close to, but never below, zero. Likewise, for high balances we predict a default probability close to, but never above, one. The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction. We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot. The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.
이 환장 조작된 꺾임 (4.2)번 모형 족쇄를 억센 야생 실전 데이터 형국에 착 맞물려 딱 찍어 맞물려 누르기(피팅 최적화) 고정하기 위해서, 우리는 저 뒤따르는 바로 다음 단면 절에서 심술궂게 설명해 토론할 전설의 **최대 우도(Maximum Likelihood)** 기법이라는 특수 수학자적 도출 탐색 장치 방법을 전동합니다. 그림 화면 4.2 배열 우측 오른쪽 단면 패널뷰는 바로 이 미학 완성된 멋진 구부러진 곡선 로지스틱 곡선 기조 회귀 모델 그물이, 거친 이 원천 `Default` 가짜 찌라시 파산 데이터에 얼마나 기가 차고 막히게 구부러져서 오차 없이 들어맞는지(fit)를 단면 입증해 삽화 보여줍니다. 자, 눈을 비비고 주목 유념하십시오. 이제 잔고 부채가 아무리 바닥없이 낮고 선량해도 환산 우리 파산 확률 게이지는 0에 무한수렴 무한히 수액 가깝게 달라붙을지언정 결단코 절대로 단연 0 밑바닥 동굴 음수 수면 아래를 파고들지(below zero) 철통 방어 않습니다. 마찬가지 구조로 빚 잔고 기둥이 우주 밖으로 폭등 억만장자 수위가 빌드업 된다 한들 우리 모델은 파생 체납 파산 확률을 천상계 단 1(100%) 장벽 선단에 무한 접착 육박시킬 유치뿐 결코 단연 단절 1 천장 그 위상층을 폭파 초진해 넘어서지 통제 않습니다. 이 위대한 조수 로지스틱 함수 녀석은 이처럼 시종일관 형태 결함 없이 항상 양 끝이 매끄럽게 눕혀진 형태의 저 안정감 있는 **S자 형상 뱀모양(S-shaped)** 의 확률 수치 곡선 라인을 단조 영원히 생성 조립해 그려 내며, 그 놀라운 기조 덕분에 막무가내 돌발적인 미친 $X$ 타깃 값 치수가 강단 튀어 들어와도 구태여 상관없이 우리 본부는 늘 이치 논리력에 맞는 합당히 상식적인 확률선 구간 예측치만을 온전 안전 획득 도출할 기표 수 있게 됩니다. 또한 우리는 동단 이 구부러진 교묘 로지스틱 회귀 커브 모델 선이, 바로 아까 왼쪽 판정 멍청 일직선 강압 선형 회귀 모형 선보다 데이터가 품은 지형적 점들 체납 발생 확률 궤적 밀도와 구릉의 그 범위 전장을 단연 훠씬 압도 더 정교 그럴싸하게 수반 포착(capture)해 감싸 안는 국면을 목격 조망 쾌재 알 수 있게 됩니다. 두 막대 선, 버그 섞인 일직선과 우아한 곡선 경우 간 모델 비교에 있어 놀랍게도, 두 판세 모두 우리 훈련 구장 데이터를 통 다져 요약 뭉뚱그린 그 평균 예측 계산 확률의 최종선 출력 평균은 0.0333 수치로 동일하며 (훈련기 데이터 총망라 누적 평균화), 이는 순수 무작위 실제 원본 데이터 세트 통 속 전체 파산 체납 비행자들의 전체 물리적 비율 조각가와 똑같게 연동 계산 유지 조화됩니다.

After a bit of manipulation of (4.2), we find that
이 S자 뱀 수식 (4.2) 번 덩어리 공식을 양손으로 잡고 이리저리 살짝 비틀어(변환, manipulation) 장난쳐 구속해 보면, 우리는 결국 아주 묘하고 다음과 같은 놀라운 비결 수식 구획을 도출 얻어낼 단서 수 구체 있게 단연 파악됩니다:

$$
\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X} \quad (4.3)
$$

The quantity $p(X) / [1 - p(X)]$ is called the _odds_, and can take on any value between 0 and $\infty$. Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively. For example, on average 1 in 5 people with an odds of $1/4$ will default, since $p(X) = 0.2$ implies an odds of $0.2 / (1 - 0.2) = 1/4$. Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X) = 0.9$ implies an odds of $0.9 / (1 - 0.9) = 9$. Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.
여기서 왼쪽 항 $\frac{p(X)}{[1 - p(X)]}$ 라는 (분자 확률 vs 분모 안 일어날 나머지) 요상한 몫 분수 양적 덩어리를 통계학에선 저명한 판돈 비율 이름, 즉 **'오즈(Odds, 승산비)'** 라고 위엄 단연 불리는데, 이 미친 녀석은 여타 확률의 조막만 한 1 구간 한계 감옥 박스를 단연 타파해 박살 내고 밑바닥 0부터 천장 뚫린 무한대($\infty$)까지 온갖 무지막지한 모든 수치 스펙 구간 값들을 마음껏 천정부지로 요동 가질 표출 수 있게 됩니다. 이 승산 값인 오즈 수치가 동단 0 에 바닥 기어 가깝거나 역으로 무한대에 치솟아 가깝다는 건 각각 체납 확률 덩어리가 엄청나게 안전히 희박 낮거나 역으로 배 쨀 확률이 100% 에 기표 가깝게 지옥행 높다는 극단 지시 뜻을 각각 각기 암시 나타냅니다 지시합니다. 예를 들어 들어보죠! 오즈비 계산이 분수 $1/4$ (즉 0.25 판돈율)인 무작위 무리 5명 그룹은 평균 단 한 명 1명이 파산 구속합니다. 왜냐고요? $p(X)=0.2$ 일 때 이를 위 오즈 수식 식벽에 대입 통과시키면 $0.2 / (1 - 0.2) = 0.2 / 0.8 = 1/4$ 로 정확히 똑떨어지게 수단 암시되기 때문입니다. 마찬가지 역발상 형상으로, 도망 파산 확률이 무려 90% 극악한 나쁜 놈들 그룹 무리는 승산이 무려 오즈비 스펙 $9$ 배 배당 이라는 극단적 도출 배수가 산입 됩니다 ($0.9 / (1 - 0.9) = 9$). 이 배당 파이 비율 지표(**오즈, Odds**) 개념 파츠는 고작 소수점 1/10 마디 단위의 답답한 순수 확률(probabilities) 치부보다는 내 손의 수익 판돈 베팅 전술 전략을 직관 체감 체감화 하고 더 자연스레 찰떡 연계 묶이기 기표가 직관 편해서, 오래된 경마장 도박판 따위에서 예전부터 극히 전통적으로 늘상 대체 도구로 줄곧 사랑 쓰여왔습니다!

By taking the logarithm of both sides of (4.3), we arrive at
이제 멈추지 마시죠. 저 배당 (4.3)번 오즈 수식 판 양방쪽 변두리 팔 양쪽에 무지막지한 자연로그($\log$) 도끼를 동시에 전격 씌워버리면 대대적인 차단 수학적 마법 치환 기적이 벌어집니다. 돌격 도착한 변환 수식:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_. We see that the logistic regression model (4.2) has a logit that is linear in $X$.
수식 도끼에 갈라진 저 기괴하게 꼬인 왼쪽 덩어점은 훗날 역사에서 위대한 **'로그 오즈(Log Odds)'** 혹은 **'로짓(Logit)'** 이라고 거창칭 불리게 될 본질의 핵심 치환 변수입니다. 자, 이제 우측을 보십시오. 맙소사! 우리는 저토록 구불구불 지긋지긋 지저분했던 우측 태생 곡선 로지스틱 커브 모형 방정식 S 선체 (4.2) 가, 왼쪽 로짓(Logit) 이라는 평행 우주 공간으로 이주 변환되는 기형 동시 순간 바로 우리 눈앞에 예측 변수 $X$와 완벽하게 대동 **선형적인(Linear) 깨끗한 1차 직선 방정식 도화지 체제 구조** 형국으로 쫙 펴져 갖추게 도달됨을 목도 발견 직관 지켜보게 단연 쾌거 됩니다!

Recall from Chapter 3 that in a linear regression model, $\beta_1$ gives the average change in $Y$ associated with a one-unit increase in $X$. By contrast, in a logistic regression model, increasing $X$ by one unit changes the log odds by $\beta_1$ (4.4). Equivalently, it multiplies the odds by $e^{\beta_1}$ (4.3). However, because the relationship between $p(X)$ and $X$ in (4.2) is not a straight line, $\beta_1$ does _not_ correspond to the change in $p(X)$ associated with a one-unit increase in $X$. The amount that $p(X)$ changes due to a one-unit change in $X$ depends on the current value of $X$. But regardless of the value of $X$, if $\beta_1$ is positive then increasing $X$ will be associated with increasing $p(X)$, and if $\beta_1$ is negative then increasing $X$ will be associated with decreasing $p(X)$.
잠시 챕터 3 교실로 기억을 돌려 회상 소환 복구해봅시다. 뻣뻣한 '선형 회귀' 모형 당시 직선판에서는 기울기 스펙인 $\beta_1$ 이 "$X$가 딱 1 계단 오를 때마다 반응값 $Y$가 통계 평균적으로 단호 정확히 지진 똑같이 얼마만큼 수직 보폭 뛴다"고 평균 변화값을 기표해 명쾌 설명 기조 규정 단언했었습니다. 하지만 이에 극명 반작용 대조적으로, 여기 '로지스틱 회귀 모형' 지형판 곡선 동네에서 입력 $X$가 1 단위를 올릴 경우 뛰거나 오르는 덩어리 지분은 직관 확률 $Y$ 본신 덩어리 퍼센트 자체가 절대 아니라 절단 억제, 오직 방금 배운 저 요강 **'로그 오즈(Log Odds)' 지표판 눈금 부속 기가 바로 단연 그 조 단위 $\beta_1$ 수치만큼 전격 직관 뛴다**는 구태 조심 뜻을 (4.4번 식 증명) 품습니다. 이를 등가 단위 현실 세계로 다시 풀어쓰면, 원래 실전 경마 도박꾼의 판돈 배율 오즈($Odds$) 값 배당 치수 자체에는 $e^{\beta_1}$ 덩이의 위력 승수 폭탄이 여지 곱해져 눈덩이 가속으로 기형 불어난다는 곱셈 마법이 작용 성립됩니다 단언 (4.3번 식 변압). 하지만 경고 단절 주의! 애초 우리가 이 흑막 기조 부드러운 (4.2)번 함수 곡선 방정식 표에서 다투는 순수 확률 $p(X)$ 게이지와 밑변 이동 $X$ 타깃 축의 상승 관계 전장은 단순한 평탄 일직선 비례 동행이 결코 억울 단연 아니기 때문에, $\beta_1$ 방정식 가중치 기둥의 수치 상승력 자체가 예측 상승 도출시 도출 실제 확률 $p(X)$ 퍼센티지가 고정 퍼센트별로 오르는 고단 고정 확단폭된 확률 지표 고리 변화 절편량에 일직선 일대일로 절대 단연 **대응 매칭 종속하지는 _않습니다_(does not!)**. 막말로 $X$가 고작 1 눈금 조금 보폭 변할 때 하늘로 점프하는 최종 확률 $p(X)$ 단동 변침 점프의 변화폭 덩어리 폭 등단 변화 도출 총량 폭격 규모 수치는, 내가 현재 얌전한 S자 곡선 S 좌표의 가장자리 안전 평면 지대 늪지대에 배회 멈춰 서 있는지 아니면 중앙의 미친 듯이 기울기 솟는 가파른 확률 제트기 언덕 오르막 협곡 급류 가운데 현재 탑승 서있는지, 전적으로 이 $X$ 의 현재 진입 지표 안 위치(기울기 가속 체감 점도) 점유 좌표에 전부 종속 목줄 쥐어져 의존합니다. 그럼에도 불구하고 불행 중 단연 최후 다행, 만약 당신이 계산 획득한 이 기울기 가속 단서 $\beta_1$ 눈금이 + 양수 부호로 기인 탄력 받았다면 수맥 여하 $X$ 의 돌출 유입수 전단 기입 조치 값이 오를 전진 전개 스펙 증가될 수록 최종 타깃 판정 확률인 $p(X)$ 수계 곡선 고단 도달 판정도 똑같이 우상향 흐름으로 구태 동반 단선 필연 솟구쳐 언덕 상승 단계를 필히 돌진 증가 탄력 증가할 것임은 조력 동반 연승 타격 연관 확정됩니다. 혹여 역으로 만일 음수 $\beta_1$ 방향으로 수직 하강 잡혔다면 필히 $X$ 누증 여조가 오를 때 역 하강 마이너스 음침 $p(X)$ 감소 국면으로 필연 동침 조강 결구 이어 확정 작용 연계 될 것입니다.

This is the document for this topic.
이 파트는 이 단막 로그-로지스틱 주제를 논단 위해 구축 기술 거진 적재된 요약 해설본 조 문서 양식입니다.

---

## Sub-Chapters

[< 4.3 Logistic Regression](../trans2.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans2.html)

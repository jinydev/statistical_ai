---
layout: default
title: "trans2"
---

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans2.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.2 Estimating the Regression Coefficients
# 4.3.2 회귀 계수 추정 (정답에 가장 가까운 최후의 곡선 찾기)

The coefficients $\beta_0$ and $\beta_1$ in (4.2) are unknown, and must be estimated based on the available training data. In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients. Although we could use (non-linear) least squares to fit the model (4.4), the more general method of _maximum likelihood_ is preferred, since it has better statistical properties.
지옥의 S자 방정식 수식 (4.2) 배 안에서 암약하는 핵심 참모 계수 $\beta_0$ 와 $\beta_1$ 은 우리가 당장 알 길이 없는 암흑 속의 미지의 값이며, 우리는 우리 손에 쥐어진 가용한 훈련수사 데이터를 샅샅이 파고 바탕 삼아 이 녀석들 좌표를 찍어 맞춰야(추정해야) 합니다. 자, 위대한 3단원을 돌아보면 우리는 선형 회귀 1차선 뼈대의 미지수를 딱 맞추기 위해 '최소 제곱법' 이라는 망치를 시원하게 썼습니다. 비록 여기서도 무식하게 (비선형) 최소 제곱법 망치를 휘둘러 저 (4.4) 모형 틀에 꾸역꾸역 욱여넣을 순 있겠지만, 여기 확률의 세계에서는 **최대 우도 추정법(Maximum Likelihood Estimation)** 이라는 더 고상하고 보편 타당한 수학적 진단 방식이 훨씬 훌륭한 통계적 속성을 담보하기 때문에 이 마법의 방법을 단연 강력 선호하게 됩니다.

The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_0$ and $\beta_1$ such that the predicted probability $\hat{p}(x_i)$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status.
로지스틱 회귀 뱀 모델을 찍어 누르기 위해 저 '최대 우도' 마법 단자를 동원하는 가장 본질적인 기본 직관은 심플하게 이렇습니다: 우리가 (4.2)번 식의 고문관 기계를 통과시켜 뱉어낸 각각의 개인별 징벌(파산 예측) 확률 타깃 스펙인 $\hat{p}(x_i)$ 가, 지금 우리 눈앞에 적나라하게 놓인 그 사람의 '진짜 파산 현행 관측 상태(Yes or No)'에 최대한 소름 돋게 완벽히 들러붙어 밀착 일치하도록 이끌어 줄 쌍두마차 계수 $\beta_0$ 와 $\beta_1$ 추정치 조타수를 갈망하며 찾는 것입니다.

In other words, we try to find $\hat{\beta}_0$ and $\hat{\beta}_1$ such that plugging these estimates into the model for $p(X)$, given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not.
다시 말해 우리 임무는, 저 무시무시한 (4.2) 식의 배때기인 확률 $p(X)$ 에 이 조타수 추정치들을 강제로 쑤셔 넣었을 때 기계가, 실제로 대금을 떼먹고 도망친(defaulted) 불량 녀석들에게는 1(100%) 에 육박하는 사형 선고 확률 숫자를 아주 통쾌하게 뱉어내고, 반면 착실히 돈을 갚은 선량한 시민 녀석들에게는 0(0%) 에 수렴하는 안심 숫자를 무조건 뱉어내게 만드는, 그야말로 모델의 완벽한 튜닝 다이얼 값인 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 을 집요하게 찾아내려고 시도하는 과정인 셈입니다.

This intuition can be formalized using a mathematical equation called a _likelihood function_:
이러한 우리의 원초적 체포 심리 직관은, 곧바로 통계학의 자존심이자 **'우도 함수(Likelihood Function)'** 라 거창하게 불리는 다음 단조 수식 공식을 통해 아주 매끄럽게 공식화 치환될 수 있습니다:

$$
\ell(\beta_0, \beta_1) = \prod_{i: y_i=1} p(x_i) \prod_{i^{\prime}: y_{i^{\prime}}=0} (1 - p(x_{i^{\prime}})) \quad (4.5)
$$

The estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ are chosen to _maximize_ this likelihood function. Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood. The mathematical details of maximum likelihood are beyond the scope of this book. However, in general, logistic regression and other models can be easily fit using statistical software such as `R` or `Python`, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.
이 다이얼 추정치 수위인 $\hat{\beta}_0$ 과 $\hat{\beta}_1$ 조종타는 이 우도(Likelihood) 함수의 판정 최종 결괏값을 그야말로 **가장 무지막지하게 제일 꼭대기로 끌어올리게(최대화, Maximize)** 만들도록 까다롭게 맞춤 선택됩니다. 최대 우도 추정 기법은 이 교재 전체 전반에 걸쳐 우리가 집요하게 까고 조사하게 될 수많은 비선형 구불구불 모델들을 피팅하고 맞출 때 전천후 전술로 쓰이는 마스터키식 매우 일반적인 접근법입니다. 팩트폭격 하자면, 돌이켜봤던 선형 회귀에서 그렇게 사랑했던 과거 최소 제곱법 방식 조차도, 따지고 한 꺼풀 벗겨보면 실은 이 방대한 최대 우도 철학의 아주 미미한 특수한 편린의 형태 케이스일 뿐이었습니다. 저 우도 함수(Likelihood) 속에 숨은 복잡무쌍 극한 미적분 유도 수학 디테일 전개표는 다행히 이 친절한 책의 난이도 범위를 안전히 벗어납니다. 다행스럽게도 참 고맙게, 로지스틱 회귀를 비롯한 제반 다른 모델들은 최신 파이썬(`Python`)이나 `R` 같은 똑똑한 노예 통계 코딩 소프트웨어 엔진으로 1초 만에 순식간에 강력 적합 피팅 시킬 수단이 있으므로, 우리 인간이 저 무서운 내막인 최대 최소 미분 적합 산출 절차 조각들에 나날이 손수 직접 매달려 골치 아프게 끙끙 앓으며 고민할 하등의 공산 필요가 단연 없습니다.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the `Default` data in order to predict the probability of `default = Yes` using `balance` . We see that $\hat{\beta}_1 = 0.0055$; this indicates that an increase in `balance` is associated with an increase in the probability of `default`. To be precise, a one-unit increase in `balance` is associated with an increase in the log odds of `default` by 0.0055 units.
자, 표 4.1 리포트는 오직 '통장 잔여 빚 잔고(`balance`) 하나'만 무기로 기용해 사용하여 `default=Yes` 배 쨀 확률을 예측해 찌르기 위한, 피 튀기는 로지스틱 모형 피팅(fitting) 적합 작전을 강행 돌린 후 얻어낸 핵심 계수 조종사 추정치들과 주변 관련 정보가 조율된 최종 작전 성적표입니다. 우리는 여기서 마침내 $\hat{\beta}_1 = 0.0055$ 임을 발견해 봅니다; 이것은 카드 거치 잔고 액수 수위가 점진 진격 늘어나면 그에 따라 빌런이 될 파산할 확률 척도도 덩달아 상승 동승 한다는 직관적 뜻을 내포 가리킵니다. 미시적으로 더 정확히 말하자면, 잔고 빚이 1 달러(단위) 찔끔 더 늘어날 때마다 파산 절명의 **'로그 오즈(Log-odds)'** 지표 값이 가차 없이 딱 0.0055 단위 덩이만큼 무던히 가중 늘어나 가산된다는 오싹한 뜻과 100% 대응합니다.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3. For example, we can measure the accuracy of the coefficient estimates by computing their standard errors. The _z_-statistic in Table 4.1 plays the same role as the _t_-statistic in the linear regression output. For instance, the _z_-statistic associated with $\beta_1$ is equal to $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$, and so a large (absolute) value of the _z_-statistic indicates evidence against the null hypothesis $H_0 : \beta_1 = 0$. This null hypothesis implies that the probability of `default` does not depend on `balance` . Since the _p_-value associated with `balance` in Table 4.1 is tiny, we can reject $H_0$. In other words, we conclude that there is indeed an association between `balance` and probability of `default`. The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).
여기 표 4.1 전면부에 표시 출력된 로지스틱 회귀 성적 결과표의 다수 많은 측면 단면들을 살며시 들여다보면, 놀랍게도 과거 3장 선형 회귀 직선의 결과 성적표 문법과 굉장히 구조가 유사 데칼코마니 한 측면이 꽤 많습니다. 예를 들면, 우린 그때처럼 여기서도 각 조종사들의 표준 오차 게이지(SE)를 따로 계산해서 이 조각 추정치들이 요동 널뛰는 정확도를 타진 측정 평가할 수 똑같이 있었습니다. 눈에 띄는 특히 표 4.1 하단에 기표된 **z-통계량(z-statistic)** 이수 심판관은, 옛날 3장 직선 회귀 경기장에서 호각을 불었던 그 유명한 _t_-통계량(_t_-statistic) 심판과 완벽히 1대1 똑같은 권위 역할 역학을 이 구장에서도 자행 수행합니다. 예를 들면, $\beta_1$ 계수에 꼬리표 붙은 _z_-통계량 성적은 단순히 구한 $\hat{\beta}_1$ 을 자기 자신의 지분 흔들림인 $\text{SE}(\hat{\beta}_1)$ 로 거듭 나눈 몫 점수이며, 이 (음수 떼고 본 절댓값) z-심판 점수가 엄청 거대 뻥튀기하다는 명백한 조짐은 자명하게 "빚 잔고 액수 따위와 파산 여부는 1도 아무 관련 엮이지 없다!"고 박박 속 편히 억지를 부리는 기존 귀무 가설 단면인 $H_0: \beta_1 = 0$ 주장을 걷어차고 강력 구태 기각할 확고한 반박 스모킹 건 근거가 단연 불쑥 됨을 지표 뜻합니다. 여기 표 4.1 성적에서 `balance` 파츠에 배정 뜬 _p_-값 표찰이 다행히도 먼지 코딱지만큼 형편없이 극소 작게 떴기 때문에, 우리는 승리의 깃발을 꽂고 당당하게 그 바보 같은 $H_0$ 를 전면 기각해 묻을 수 사정 있습니다. 즉 환호 반증해, 잔여 빚 잔고와 파산 도주 확률 표적 사이에는 인간적으로 빼도 박도 핑계 못하는 치명 선명한 끈끈한 연관 관계성이 진짜 확실히 단단 존재한다고 쐐기를 박고 종결 결론 내릴 수 자축 있습니다. 기표 하단 표 4.1의 첫머리 절편(Intercept) 추정치 초기 수치 자체는 보통 우리는 그리 쓸모 애지 관심 두는 사안 관심사가 대체로 결단코 아닙니다; 녀석의 절편 메인 기저 목적은 그저 그 전반의 평균 추합 피팅 곡선 확률들 전체 수위 곡점을 우리 데이터 풀 전체 집단이 지닌 최초 1번 타겟 발생 비율 몫(여기선 10,000명 중 약 3% 수준인 전체 평균 파산율 현황)과 모조리 강제 균형을 맞추어 영점 높낮이를 조작 튜닝하는 부품 기어 역할만 순전히 묵묵히 수행 타진할 뿐입니다.

This is the document for this topic.
이 파트는 이 단막 계수 산정 주제를 지표 논단 위해 구축 기술 거진 적재된 요약 해설본 조 문서 양식입니다.

---

## Sub-Chapters

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans2.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans2.html)

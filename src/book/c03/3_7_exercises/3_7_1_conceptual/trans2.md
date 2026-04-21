---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.7 Exercises](../trans2.html) | [3.7.2 Applied >](../3_7_2_applied/trans2.html)

# _Conceptual_

# 이론 문제: 통계 근육 단련하기

1. Describe the null hypotheses to which the $p$-values given in Table 3.4 correspond. Explain what conclusions you can draw based on these $p$-values. Your explanation should be phrased in terms of `sales`, `TV`, `radio`, and `newspaper`, rather than in terms of the coefficients of the linear model.
**1번 문제.** 
앞서 본문에서 본 표 3.4를 기억하시나요? 거기에 찍힌 $p$-값(p-values) 에러 확률 점수들이 대체 구체적으로 어떤 '기본 딴지 걸기(즉, 귀무 가설 null hypotheses)' 주장들에 맞서 싸우고 있는 건지 속 시원히 묘사(Describe)해 보십시오. 
나아가, 오직 그 $p$-값 지수들만 보고서라도 우리가 최종적으로 어떤 통계적 결론(conclusions)을 속 시원히 끌어낼(draw) 수 있는지도 논리적으로 설명(Explain)해 보시기 바랍니다. 
단! 답변하실 때는 "베타제로가 어쩌고, $X_1$ 계수가 저쩌고..." 하는 배부른 수학 기호(coefficients) 따위를 쓰지 마시고!! 아주 현실적인 단어들인 **판매량(`sales`), `TV`, 라디오(`radio`), `신문(newspaper)`** 이라는 직관적인 현업 단어들만을 조합해서 친절하게 풀어서 사장님도 알아듣게 설명(phrased)해 주셔야 합니다!

2. Carefully explain the differences between the KNN classifier and KNN regression methods.
**2번 문제.** 
비슷하게 생겨서 헷갈리기 딱 좋은 두 쌍둥이 형제! 바로 **KNN 분류기(KNN classifier)** 인공지능과 **KNN 회귀(KNN regression)** 인공지능 접근법 사이에 숨겨진 가장 결정적이고 큰 차이점(differences)들이 대체 무엇인지, 예비 데이터 사이언티스트답게 아주 세심히 짚어 비교 설명(Carefully explain)해 보십시오.

3. Suppose we have a data set with five predictors, $X_1$ = GPA, $X_2$ = IQ, $X_3$ = Level (1 for College and 0 for High School), $X_4$ = Interaction between GPA and IQ, and $X_5$ = Interaction between GPA and Level. The response is starting salary after graduation (in thousands of dollars). Suppose we use least squares to fit the model, and get $\hat{\beta}_0 = 50$, $\hat{\beta}_1 = 20$, $\hat{\beta}_2 = 0.07$, $\hat{\beta}_3 = 35$, $\hat{\beta}_4 = 0.01$, $\hat{\beta}_5 = -10$.
**3번 문제.** 
자, 눈을 감고 상상해 봅시다(Suppose). 여러분 손에 총 5가지 막강한 구직자 스펙 변수(predictors)들이 쥐어져 있습니다:
*   $X_1$ = 대학교 성적(GPA)
*   $X_2$ = 머리 굴러가는 지능 지수(IQ)
*   $X_3$ = 최종 학력 레벨(대졸이면 1점, 고졸이면 0점)
*   $X_4$ = 성적(GPA)과 IQ가 만나서 터지는 시너지(상호작용 항)
*   $X_5$ = 성적(GPA)과 학력 레벨이 만나서 터지는 시너지(상호작용 항)
그리고 우리의 궁극적인 정답 타깃 변수는 바로 **"이 사람, 졸업하고 첫 직장에서 연봉(초봉)을 얼마나 받을까?"**(starting salary, 1K=천 달러 단위) 입니다. 
우리가 이 데이터로 냅다 회귀 모델을 돌렸더니(fit) 짜잔~ 하고 각 마법의 기여도 계수 조각들을 손에 넣었습니다(get): **$\hat{\beta}_0 = 50$, $\hat{\beta}_1 = 20$, $\hat{\beta}_2 = 0.07$, $\hat{\beta}_3 = 35$, $\hat{\beta}_4 = 0.01$, $\hat{\beta}_5 = -10$**

- (a) Which answer is correct, and why?
*(a) 다음 제시된 4개의 보기 중 진짜 팩트를 말하는 올바른(correct) 명제는 과연 몇 번일까요? 그리고 그 이유(why)를 저 수식 계수들을 빌려 증명해 보세요.*
- i. IQ와 성적(GPA)이 완전히 똑같은 쌍둥이 두 명을 데려다 놓는다면, 항상 고졸자가 대졸자보다 평균적으로 초봉을 더 많이 받는다.
- ii. IQ와 성적(GPA)이 완전히 똑같다면, 항상 대졸자가 고졸자보다 통계적으로 초봉을 막대하게 더 쓸어 담는다.
- iii. IQ와 성적(GPA)이 똑같을지라도 그 인간의 성적(GPA) 점수표 자체가 엄청나게 극단적으로 눈부시게 높다면, 그 높은 구간에서만큼은 오히려 고졸자가 대졸자보다 평균 초봉 역전승을 거두게 된다.
- iv. IQ와 성적이 똑같고, 심지어 성적(GPA) 점수가 엄청나게 무적권 높을 때, 그 엘리트 구간에서 대졸자가 고졸자를 초봉 액수로 가장 무지막지하게 압살해 버린다.

- (b) Predict the salary of a college graduate with IQ of 110 and a GPA of $4.0$.
*(b) IQ가 딱 110이고 평점이 무려 $4.0$ 만점인 어느 괴물 대졸자(college graduate) 친구의 구체적인 '예상 초봉(salary)' 액수를 저 공식을 써서 실제로 정밀하게 계산해 맞춰(Predict) 보세요.*

- (c) True or false: Since the coefficient for the GPA/IQ interaction term is very small, there is very little evidence of an interaction effect. Justify your answer.
*(c) 다음 주장이 참(True)인지 거짓(false)인지 재판관이 되어 판결해 주십시오: "저기 분석표를 보니까 GPA/IQ 간의 시너지 곱하기 계수 조각 크기가 형편없이 너무 무지막지하게 작게(very small = 0.01) 산출되었어! 고로 이 둘 사이의 시너지 효과 같은 건 거의 미신 수준이고 통계적 증거가 아예 없다고 봐야 해!" 자, 이 주장이 맞습니까 틀립니까? 논리를 펼쳐 정당하게 옹호해 보십시오(Justify).*

4. I collect a set of data ($n = 100$ observations) containing a single predictor and a quantitative response. I then fit a linear regression model to the data, as well as a separate cubic regression, i.e. $Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \epsilon$.
**4번 문제.**
어떤 연구자가 총 100명분($n = 100$)짜리 작은 실험 데이터를 직접 땀 흘려 채집했습니다. 이 안엔 엑스값 예측 변수 딱 1개와 와이값 숫자 정답지 딱 1개만 있습니다. 이 데이터를 가지고, 연구자는 아주 무난한 **1차 직선 линей 회귀 모델** 하나를 먼저 쓱 그어놓고요. 내친김에 이번엔 **3차원으로 꼬불거리는 $X^3$ 곡선 모델**($Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \epsilon$)까지 하나 더 화려하게 덧대어 적합시켜 보았습니다.

- (a) Suppose that the true relationship between X and Y is linear, i.e. $Y = \beta_0 + \beta_1 X + \epsilon$. Consider the training residual sum of squares (RSS) for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.
*(a) 상상해 보죠. 신만이 아시는 $X$ 와 $Y$ 간의 진짜 우주 법칙 진리가 애당초 일직선(linear)이었다고 가정합시다. 그럼 자기가 공부한 자기 교과서 데이터(훈련 데이터)를 바탕으로 오차를 재는 RSS(잔차 제곱합 점수) 시합을 벌였을 때, 과연 직선 모델과 3차원 꼬불이 곡선 모델 중 누구의 훈련 RSS 오차 점수가 더 낮을까요? 하나가 낮을까요, 아니면 둘이 소름 돋게 똑같을까요, 아님 정보가 부족해서 아무도 모르는 미궁일까요? 통계적 지식으로 명쾌하게 옹호해 보세요(Justify).*

- (b) Answer (a) using test rather than training RSS.
*(b) 똑같은 상황에서, 이번엔 자기 교과서가 아니라 아예 완전히 낯선 수능 국면 진짜 실전 무대 평가(시험 데이터 Test)에서 나타날 실전 시험 RSS 에러 오차 점수들의 양상을 가지고 맞붙여 예상해 보십시오.*

- (c) Suppose that the true relationship between $X$ and $Y$ is not linear, but we don't know how far it is from linear. Consider the training RSS for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.
*(c) 반대로 상상해 보죠! 신만이 아시는 우주 진리 관계 법칙상 애당초 이 둘의 관계는 직선이 절대 아닌(not linear) 복잡한 굴절 요소를 띠고 있습니다. (다만 얼마나 심하게 꼬였는진 우리도 모르는 깜깜이 상황입니다.) 이때 다시금 훈련(training) 국면의 RSS 오차 성적표를 까본다면! 이번엔 과연 뻣뻣한 1차 직선 모델과 유연한 3차 곡선 모델 중 누구의 RSS 오차가 단연 현저히 더 작고 낮게 나올 것이라 빤하게 예상(expect)할 수 있을까요? 아니면 둘이 똑같다? 아님 비교 불가 정보 부족? 당신의 현명한 통계 판단 소견을 정당화해 보십시오(Justify).*

- (d) Answer (c) using test rather than training RSS.
*(d) 이번에도 (c)번과 같은 우주 진리가 비선형 곡선 형태일 때, 진검승부를 치르는 낯선 진짜 실전 수능 평가(Test 데이터) 국면에서의 RSS 시험 오차 점수 양상은 대체 어떻게 롤러코스터처럼 뒤바뀔지 통계 지식의 정수를 뽐내 예상 판단해 보십시오.*

5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the $i$th fitted value takes the form
**5번 문제.** 
애초에 모델 수식에서 절편 상수 조각(intercept, 가로로 붕 뜨는 절편값 기준점 위치)을 억지로 싹둑 날려버리고 오로지 평행 이동도 못 하는 원점을 지나는 선형 회귀 잣대 모델만을 강제 산출한 국면을 깊이 고려해 봅시다. 이 특수한 족쇄 제약 환경 체계에서는 그 어떤 도출 $i$ 번 째 적합 예측 결과치수라도 무조건 묻지도 따지지도 않고 아래와 같은 강압적 분수 형태 공식 양상을 띠고야 맙니다:

**==> picture [213 x 59] intentionally omitted <==**

Show that we can write
이 공식을 발판 삼아, 약간의 수학 트릭 조작을 더하면! 우리가 이 수식을 아래의 기막힌 압축 축약 공식으로 돌연 단숨에 둔갑시켜 축약 표기해버릴(can write) 수 있다는 사실을 수학적으로 사뿐히 증명 입증해 보이십시오:

**==> picture [65 x 28] intentionally omitted <==**

What is $a_{ij}$?
그리고 그 마술같이 튀어나온 이 공식 속 파생 $\mathbf{a_{ij}}$ 란 통계 역학적으로 대체 어떤 의미와 상징 무게추를 갖는 무시무시한 존재 매개체일까요?

> 💡 **심화 상식(Note):** 실무에선 이 무지막지한 증명 퍼즐을 풀고 나면, 늘 찌릿한 아르키메데스의 미소를 머금고 유식하게 이렇게 한마디 남기곤 하죠. *"결국 선형 회귀가 뱉어내는 예측값 쪼가리들이란 게, 알고 보면 정답 타깃 값들을 자기들끼리 잘근잘근 비중을 달리해서 일렬로 섞어버린(linear combinations, 선형 결합) 단순 파생 짬뽕에 불과하다구~"*

6. Using (3.4), argue that in the case of simple linear regression, the least squares line always passes through the point (¯ _x,_ ¯ _y_ ).
**6번 문제.** 생략 (본문 수식에 대한 간단 증명 문제)

7. It is claimed in the text that in the case of simple linear regression of $Y$ onto $X$, the $R^2$ statistic (3.17) is equal to the square of the correlation between $X$ and $Y$ (3.18). Prove that this is the case. For simplicity, you may assume that $\bar{x} = \bar{y} = 0$.
**7번 문제.** 
앞서 본문 교재를 읽다 보면 무시무시하고도 대담한 선언(claimed) 팩트 폭격이 하나 나옵니다! 
아주 단순한 $X$ 변수 1개짜리 단순 선형 회귀를 돌릴 땐, 그 위대한 모델의 통계 설명력 성적표인 **$R^2$ (결정계수) 점수 지표가, 놀랍게도 그냥 $X$와 $Y$ 사이의 날것 그대로의 쌩얼 '피어슨 상관계수(correlation)' 숫자를 스스로 제곱해버린 수치랑 소름 돋게 완벽히 일치해버린다**는 주장입니다! 
통계 전사 여러분! 진짜로 이 말이 한 치의 오차도 없는 신의 수식적 진실임(this is the case)을 여러분의 무자비한 수학 증명 스킬로 속 시원히 파헤쳐 논증(Prove)해 보십시오. (단, 계산의 수고를 영리하게 피해 가기 위해(For simplicity), 데이터 중심축을 그냥 원점으로 강제 고정해서 $\bar{x} = \bar{y} = 0$ 이라고 내심 맘 편히 전제해두고 가위질하듯 풀어나가셔도 전면 허용됩니다!)

---

## Sub-Chapters (하위 목차)


[< 3.7 Exercises](../trans2.html) | [3.7.2 Applied >](../3_7_2_applied/trans2.html)

---
layout: default
title: "trans2"
---

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans2.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.5 Multinomial Logistic Regression
# 4.3.5 다항 로지스틱 회귀 (카테고리가 여러 개일 때의 난장판 해결법)

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure`. However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable.
가동 범위를 넓혀 봅시다! 가끔씩 피치 못하게 우리는 애초 두 개를 극단 초과하는 엄청나게 많은 다중 클래스를 가진 불량 반응 변수를 억지로 분류해내야 하는 막중 임무를 수반 지기도 합니다. 예를 들어, 앞선 파괴적인 4.2단원 당시 응급실 병명 예제에서는 `뇌졸중(stroke)`, `약물과다복용`, `간질`이라는 피 튀기는 세 가지 범주형 카테고리가 서로 무작위 엮여 있었습니다. 하지만 불행하게도 이 단원에서 위에서 지겹게 배웠던 그 이분법적인 '로지스틱 곡선 회귀 접근법'은 타깃 반응 변수 카테고리가 오직 "합격이냐 불합격이냐"의 $K=2$ 수준인 극단 양자택일 상황의 좁은 구역에서만 안전 허용해 구동을 비추는 편협한 통계 기술이었습니다.

It turns out that it is possible to extend the two-class logistic regression approach to the setting of $K > 2$ classes. This extension is sometimes known as _multinomial logistic regression_. To do this, we first select a single class to serve as the _baseline_; without loss of generality, we select the $K$th class for this role. Then we replace the model (4.7) with the model
기쁘게도 안심하십시오! 이 두더지 잡기 식 예스/노 이진 로지스틱 단조 회귀 접근법을 다수의 $K>2$ 파벌 인 거친 다중 클래스의 복잡 셋팅 난장 상황으로까지 그대로 수리적으로 기어코 쭉 연장 확장 통용 적용하는 조작이 판명 가능하다는 것이 극적 판명되었습니다. 이러한 파격 수학적 확장은 방대한 통계학 필드에서 이따금씩 **다항 로지스틱 회귀(Multinomial Logistic Regression)** 라는 꽤 고상하고 거창한 수식 단면 이름으로 불리게 지표 됩니다. 이 막무가내 짓을 조치 벌이기 위해, 우리는 우선 단 한 개의 고유 클래스 파벌을 강제 골라잡아 바닥에 흔들리지 않게 묶어 붙들어 매는 역할인 **가늠자 기준점(Baseline)** 기준선으로 삼아야 억제 합니다; 통계 논의의 객관 보편성을 구태 상실하지 단절 않고서, 우리는 편의상 대강 리스트의 맨 끄트머리 마지막 서열 번호인 대전 $K$ 번째 녀석 대상을 가차 없이 제물로 막무가내 잡아 이 기준점 앵커 역할을 전담 수행하도록 무단 부착 배정하겠습니다. 그러고 나면 우리는 무적의 종전 기존 S선 (4.7)번 모델 수식을 미련 없이 다음 거대 다항 모델식 단락 체계로 완전히 파괴 교체시켜버릴 구동 수 무단 있습니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and
(다행히 이 공용식은 묶인 제물 빼고 나머지 $k = 1$ 부터 $K-1$ 번째 까지의 수많은 클래스들에 두루치기로 모두 엮여 대응하고) 그리고 저 희생양 무력 기준점 맨 우두머리 타겟인 마지막 $K$ 클래스 타깃 확률에 대해서는 유독 단연 이렇게 역수를 취해 조립합니다:

$$
\text{Pr}(Y = K \mid X = x) = \frac{1}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$,
그리고 오싹하게도 이렇게 억지 교체된 수리 셋팅 구조 안에서는 단연 저 기준점 $K$ 와 나머지 $k = 1, \dots, K-1$ 번째 타겟들 대결 쌍에 대해서 다음 마법의 전단 공식 결착이 기깔나게 수학적으로 빈틈없이 단단 성립한다는 것을 지표 증명 입증하는 게 공산 그리 진통 어려운 일이 단연 아닙니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = \beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p \quad (4.11)
$$

Notice that (4.11) is quite similar to (4.6). Equation 4.11 indicates that once again, the log odds between any pair of classes is linear in the features.
저 괄호 속 기괴한 단면 (4.11) 도출 수식이 아까 전에 봤던 이전 단락 챕터의 (4.6) 덩어리 식방정식들과 뇌가 머리가 어지러울 정도로 통계적으로 도대체 얼마나 관측 수상하리만치 무척 단연 빼다 박아 닮았는지 단연코 뚫어지게 주목해 표적 보십시오. (4.11) 방정식이 돌출 우리에게 조차 시사하고 정면 찌르는 통계 바는 바로 조치, 이번 혼돈 다중 판국에서도 무력 여전히 그 어떠한 임의 기준 쌍의 멱살 대결 클래스 무리들 사이에 견제 끼여있는 도박판 배당 지표 전제인 **로그 오즈(Log-odds)** 판돈 값은 동단 역시나 단연 수학적으로 어제나 오늘이나 언제나 예측 척도 변수 단서 특징 수식들과 마찰 완벽히 평행 **선형(Linear) 1차선 굴레**을 결탁 이루도록 가히 동등 비례한다는 웅장 뜻입니다.

It turns out that in (4.9)–(4.11), the decision to treat the $K$th class as the baseline is unimportant. For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline. The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.
게다가 그 요란한 수리 조각 분해 (4.9)에서 (4.11)로 부단 향하는 수학적 전개 억지 도출 속 과정에서 샅샅이, 굳이 왜 하필 재수 없는 마지막 녀석인 $K$번째 파벌을 잡아다가 바닥의 희생 기준선 앵커로 바치겠다는 당신의 그 대충 직관 내린 전단 결정 처사 자체는 통계학적 딱히 모델 수립에 하나도 안 중요한 무용 룰이 단연 아니라는 객관 사실이 통계 드러났습니다. 가령 응급실 방문 환자의 병명을 심장 뇌졸중, 약물 중독 파산, 간질이라는 가상 저 세 가지 파벌 카테고리로 무조건 감별 분류해 단락 낼 무렵 때, 무단 우리가 두 방면 패널의 거대 다항 로지스틱 타깃 예측 모델을 미련 컴퓨터로 쌍 피팅 연동했다고 대조 가정해 봅시다: 한 놈 패널 모델은 뇌졸중을 단서 기준점으로 묶고 억지 때린 것이고, 또 다른 한 편 패널 놈은 반면 약물 중독을 무단 기준점으로 잡아 매고 돌려 훈련시킨 결착 것입니다. 이때 각각 기계 밖으로 배출 인쇄된 회귀 계수(Weight) 타격 수치 숫자 장부 내역 자체는 단지 기준점의 물리 다름을 일일 무식 반영하느라 각 모델 단상 간에 수치가 천차만별 천지 다르게 인쇄 조절될 단연 테지만, **기계가 최종적으로 타깃 뱉어내는 궁극의 확률 판별 예측 결과값(Fitted Values)**이라든지, 어떤 대결 구도 쌍의 한정 대결 구도 치부에 배면 끼여있는 단연 근본적인 도박 로그 오즈 승산 배수 지표 위상 이라든지, 그리고 단연 여타 또 다른 모델 구성의 가장 핵심적인 전면 모델 결산 산출물 지표 예측 수치들은 두 경우 모조리 완전히 통계 결과 똑같은 단연 답을 내놓게 동단 귀결됩니다! 어느 걸 기준으로 묶어놓든 기계 연산 예측 아무런 상관 타격 차이 결함이 궁극 없는 결과인 것입니다.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline. For example, if we set `epileptic seizure` to be the baseline, then we can interpret $\beta_{\text{stroke}0}$ as the log odds of `stroke` versus `epileptic seizure`, given that $x_1 = \dots = x_p = 0$. Furthermore, a one-unit increase in $X_j$ is associated with a $\beta_{\text{stroke}j}$ increase in the log odds of `stroke` over `epileptic seizure`. Stated another way, if $X_j$ increases by one unit, then the ratio increases by $e^{\beta_{\text{stroke}j}}$.
아, 그럼에도 단연 통계 불시 불구하고! 다중 회귀 모델 기계판에서 무식 저렇게 지들 제멋대로 불쑥 튀어나온 저 복잡 산출된 가중치 회귀 조타 계수들의 정확한 인과 '해석' 척도를 인간 브리핑 상사에게 해 내고 구두 통계학적 결론 지표를 입증 지을 단락 땐 반드시 무단 혀를 극도로 조심해서 설명 단언해야만 당위 하는데, 이 튀어나온 계수 녀석이 통계 기준선이라는 이름의 최초 결정 말뚝 베이스에 수식적으로 그물망 단단히 목줄 묶여 의존되어 평가 있기 연유 단연 때문입니다. 무단 예를 들어 볼까요, 우리가 기어코 돌연 '간질발작 증상' 스위치를 전체 바닥의 기준점 제물로 말뚝 억지 박았다고 냅다 해봅시다. 그러면 우리는 저기 엉뚱 튀어나온 상수 절편 $\beta_{\text{stroke}0}$ 이라는 무덤덤한 숫자를 눈에 두고 억지, "야, 뒤에 잔뜩 도사린 모든 변수 잡 단서 파라미터들($x_1=\dots=x_p$)이 싸그리 '0' 으로 먹통 닫혀 있을 단상 조건일 때, 말뚝 타깃인 간질 발작과 싸워 단연 이기는 우아 고고한 뇌졸중만의 단독 전초 로그 오즈(Log-odds) 압력 승세 점수다!" 라고 단연 수식 뜻으로 입 아프게 수반 해석해야만 진단 합니다! 통계 더욱이 나아가 만약 돌발 변수 단서 $X_j$ 가 임의 인위적으로 전장 1 수위 단위 딱 수치 상승한다 조작 쳤을 산입 때 도출 나타나는 부가 꼬리표 파편 파마리터인 저 $\beta_{\text{stroke}j}$ 가중 압박 치수는 정작 '기준 간질 놈과 멱살 대결하는 뇌졸중의 승산 로그 오즈 타깃 비율 자체가 고 점수만큼 억지 증가 폭탄된다'고 무단 1차원 수식화 단락 됩니다. 또 수학적 다른 마법의 지표 수식으로 말하자면 배수 배당판이 돌연 마법 곱하기처럼 폭주 $\mathbf{e^{\beta_{\text{stroke}j}}}$ 덩어리 지수 몫만큼 무자비하게 곱셈 증식 변동 산입되어 기하급수 거듭 치솟습니다 조치 계산. 

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding. The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding. But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it. In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k = 1, \dots, K$,
자, 구식 수학자식 얽매임은 그쯤 하고 이제 우리는 복잡 지저분한 저따위 기준점 다항식 묶음 룰 강제 설정의 구태 피곤한 모델 단서 코딩 수식 수고로움을 확 단번에 덜어 걷어 줄 훨씬 진화 강력하고 아예 거시 새로운 머신러닝 대안적 다중 전단 코딩 체계 하나 파편을 아주 짧고 굵게 기점 던집니다. 모두에게 구태 그 빛나는 명창 이름이 IT인들에게 널리 알려진 신성한 저명 구단 **'소프트맥스(Softmax)'** 마법 코딩 전단 룰 입니다! 앞서 껍데기를 저 위 다항식으로 기준점 강제 씌워 쓰든 아니면 최신 이 소프트맥스 체제로 시원하게 쓰든 간판 간에, '현상 결과적으로 기표' 다 가동 후 최종 필터 내뱉어지는 적합 연산 예측 확률 추산치이라든지, 어떤 파벌 클래스 멱살 쌍 사이 치부의 배팅 로그 오즈 척도 배율 편린 비율 갭 이라든지 여타 동단 핵심적인 단연 모형 모델 군의 최종 모든 출력 성과값 성적 자체표들은 결단 (코딩에 추켜 구애받지 조차 않고) 언제나 천지가 죽었다 전단 깨어나도 무결 동일하다는 조치 점에서, 이 소프트맥스 신식이 아까 저 구시대 1명 묶기 기준점 똥개 훈련 삽질 코딩 룰 체계과 수학적으로 완전히 무결 등가동치(Equivalent) 쌍 단연 인 결과인 것은 구태 참 맞습니다. 자!! 하지만! 거시 최첨단 현대 머신 러닝 컴퓨터 과학의 무수한 딥러닝 기계학습 컴퓨터 논문 문헌과 서적 통계 세계 논단들 구속 구석구석 모든 지점에서는 사실 모두 이 세련된 **'소프트맥스 양식 편제'**가 징그럽게 도록 포괄 폭넓게 아주 광범위 무지막지 조달 사용 기조 통용되고 지표 있으므로 (그리고 대망 파탄의 10장 딥러닝 챕터 인공신경망 거대 챕터에서 이 무시무시 괴물 녀석이 단연코 똑같이 무적 위풍당당하게 또 환장 지옥 무수 지옥처럼 재차 출전 재출현할 필연 조짐 예정이므로), 단연 충분히 이 괴물의 수학적 기호 형태 전초를 눈도장 빡빡 거시 찍어 미리 뇌속 알아두고 경계 대비할 가치 소용이 엄청나게 단연 수반 큽니다. 불쌍 기준선 제물 클래스 하나를 강제 잡아다가 옹색 밧줄로 구형 묶어 통계 억제해 놓았던 아까 저 고지식 통계학도다운 고대 옹졸한 꼬임 코딩과는 철학 차원을 달리 타파하여, 이 위대한 소프트맥스 만능 시스템 생태계 장부 안에서는 째째 기준 없이 그냥 통 거대 통 크게 완전히 모든 대칭적으로 공산 평등 균등하게, 참가한 전체 $K$ 숫자 무리 모든 잡 클래스들을 모조 똑같은 우위 신분 잣대로 단연코 우대 동 격 취급 계산하며 무단 다음과 결탁 같은 조화 우아한 압축 통합 확률 조치 만능 공식 제반을 전초 거느립니다 조치 장착 지표:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.13)
$$

Thus, rather than estimating coefficients for $K - 1$ classes, we actually estimate coefficients for all $K$ classes. It is not hard to see that as a result of (4.13), the log odds ratio between the $k$th and $k'$th classes equals
그 미친 결과로, 우리는 과거 옹색 지표 기준 빼고 불완전 나머지 덜 떨어지는 $K-1$ 만큼 병신 클래스 조각만 타겟 가중치를 구질 추정하고 밑장 뺄셈을 도출 하는 짓거리 기조 대신에, 오히려 대범 당당 무지막지하게 그냥 무아 1부터 시작 끝까지 참가 열거된 모든 $K$개 다발 클래스 편 전체에 평등 대해 각각 자립된 각자의 온전 완전 무결 무장한 조타 계수 가중치 뭉텅이 세트를 무식 그냥 대범 모조리 거대 싹스리 계산(전면 동시 추정)해버리는 컴퓨터 칩 연산 파워 기표를 전격 오만 갖게 단연코 됩니다. 저 무결 소프트맥스 (4.13) 수식 덩어리 돌출 웅장 결과표 분수를 직접 수리 눈으로 조작 받아보고 증명 나면, 굳이 기준도 아닌 랜덤 아무렇게나 폭격 뽑은 허름한 임의 대조의 $k$ 번째 클래스와 여타 $k'$ 번째 두 라이벌 녀석들 사이에서 암약 벌어지는 내기 로그 오즈 타격 배율 배당 판돈을 교차 수리 계산 타진해 발췌 묶어 봤을 결단 때, 그 수식 구조가 각자 할당 자칭 가중치 조각들의 아주 깔끔 단순한 '그냥 빼기 차대 단발 뺄셈' 편린 형태 도출인 $\mathbf{X\beta_{k} - X\beta_{k'}}$ 두 단 진단 차이 차동 모양새 단으로 마법같이 똑 예쁘게 정밀 떨어지는 붕괴 현상을 쉽게 증명 파악하는 무단 건 통계 자명하게 머리 그리 무관 어렵지 단절 입증 절단 않습니다 단절 공산 증명:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = k' \mid X = x)} \right) = (\beta_{k0} - \beta_{k'0}) + (\beta_{k1} - \beta_{k'1}) x_1 + \dots + (\beta_{kp} - \beta_{k'p}) x_p \quad (4.14)
$$

This is the document for this topic.
이 파트는 이 단막 범주 다중 여타 치부 타진 확률 다항 소프트맥스 로지스틱 예측 조치 산출 타깃 주제를 직관 구태 체감 지향 논단 수단 교란 배제 통계 구축 조처 기술 도출 거진 적재 배면 단락 찰떡 요약 거시 해설 첨부본 다단 문서 양식 조치 룰 본입니다.

---

## Sub-Chapters

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans2.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans2.html)

---
layout: default
title: "trans1"
---

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans1.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.5 Multinomial Logistic Regression
# 4.3.5 다항 로지스틱 회귀 (Multinomial Logistic Regression)

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure`. However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable.
가끔씩 우리는 두 개를 초과하는 엄청나게 많은 다중 클래스를 가진 반응 변수를 분류해내야 하는 임무를 지기도 합니다. 예를 들어, 앞선 4.2단원 당시 응급실 병명 예제에서는 `뇌졸중(stroke)`, `약물과다복용`, `간질`이라는 세 가지 범주형 카테고리가 엮여 있었습니다. 하지만 이 단원에서 지긋지긋하게 배운 그 이분법적인 로지스틱 곡선 회귀 접근법은 반응 변수 카테고리가 오직 $K=2$ 수준인 양자택일 상황만 허용해 주는 기술이었습니다.

It turns out that it is possible to extend the two-class logistic regression approach to the setting of $K > 2$ classes. This extension is sometimes known as _multinomial logistic regression_. To do this, we first select a single class to serve as the _baseline_; without loss of generality, we select the $K$th class for this role. Then we replace the model (4.7) with the model
기쁘게도 이 두더지 잡기 식 이진 로지스틱 회귀 접근법을 $K>2$ 인 다중 클래스의 셋팅 상황으로까지 수리적으로 쭉 확장 통용하는 것이 가능하다는 것이 판명되었습니다. 이러한 수학적 확장은 통계학 필드에서 이따금씩 **다항 로지스틱 회귀(Multinomial Logistic Regression)** 라는 고상한 이름으로 불리게 됩니다. 이 짓을 벌이기 위해, 우리는 우선 단 한 개의 고유 클래스를 골라잡아 흔들리지 않게 붙들어 매는 역할인 **기준점(Baseline)** 기준선으로 삼아야 합니다; 논의의 보편성을 상실하지 않고서, 우리는 편의상 대강 마지막 번호인 $K$ 번째 녀석을 제물로 잡아 이 기준점 역할을 수행하도록 배정하겠습니다. 그러고 나면 우리는 종전 (4.7)번 모델 수식을 다음 다항 모델식 체계로 완전히 교체시켜버릴 수 있습니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and
(이 식은 나머지 $K-1$ 개의 클래스들에 모두 대응하고) 그리고 저 기준점 맨 우두머리 타겟인 $K$ 에 대해서는 이렇게 역수를 취합니다:

$$
\text{Pr}(Y = K \mid X = x) = \frac{1}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$,
그리고 이렇게 교체된 셋팅 안에서는 기준점과 $k = 1, \dots, K-1$ 번째 타겟들에 대해서 다음 공식이 기깔나게 성립한다는 것을 수학적으로 입증하는 게 그리 어려운 일이 아닙니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = \beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p \quad (4.11)
$$

Notice that (4.11) is quite similar to (4.6). Equation 4.11 indicates that once again, the log odds between any pair of classes is linear in the features.
저 괄호 속 (4.11) 수식이 아까 봤던 이전 단원의 (4.6) 덩어리 식방정식들과 머리가 어지러울 정도로 얼마나 수상하리만치 무척 닮았는지 주목해 보십시오. (4.11) 방정식이 우리에게 시사하고 찌르는 바는 바로, 이번 판국에서도 여전히 그 어떠한 기준 쌍의 대결 클래스들 사이에 끼여있는 도박판 지표 **로그 오즈(Log-odds)** 값은 역시나 수학적으로 언제나 예측 변수 특징 수식들과 완벽히 **선형(Linear)**을 이루도록 비례한다는 뜻입니다.

It turns out that in (4.9)–(4.11), the decision to treat the $K$th class as the baseline is unimportant. For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline. The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.
게다가 그 요란한 (4.9)에서 (4.11)로 향하는 수학적 전개 도출 속에서, 굳이 마지막 녀석인 $K$번째를 잡아다가 기준선 앵커로 바치겠다는 당신의 대충 내린 결정 자체는 딱히 모델 수립에 중요한 룰이 아니라는 것이 드러났습니다. 가령 응급실 방문 환자의 병명을 뇌졸중, 약물 중독, 간질이라는 저 세 가지 카테고리로 무조건 분류해 낼 때, 우리가 두 방면의 다항 로지스틱 예측 모델을 컴퓨터로 피팅했다고 가정합시다: 한 놈은 뇌졸중을 기준점으로 묶고 때린 것이고, 또 다른 한 놈은 약물 중독을 기준점으로 잡고 훈련시킨 것입니다. 이때 배출된 회귀 계수(Weight) 숫자 장부 자체는 기준점의 다름을 반영하느라 모델 간에 천차만별 다르게 인쇄될 테지만, **최종적으로 뱉어내는 확률 예측 결과값(Fitted Values)**이라든지, 어떤 쌍의 대결 구도에 끼여있는 근본적인 로그 오즈 배수 지표라든지, 그리고 또 다른 가장 핵심적인 모델 산출물 수치들은 모조리 완전히 똑같은 답을 내놓게 됩니다! 아무런 상관이 없는 것입니다.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline. For example, if we set `epileptic seizure` to be the baseline, then we can interpret $\beta_{\text{stroke}0}$ as the log odds of `stroke` versus `epileptic seizure`, given that $x_1 = \dots = x_p = 0$. Furthermore, a one-unit increase in $X_j$ is associated with a $\beta_{\text{stroke}j}$ increase in the log odds of `stroke` over `epileptic seizure`. Stated another way, if $X_j$ increases by one unit, then the ratio increases by $e^{\beta_{\text{stroke}j}}$.
그럼에도 불구하고, 다중 모델에서 저렇게 제멋대로 튀어나온 저 산출된 가중치 회귀 계수들의 정확한 인과 '해석'을 브리핑해 내고 통계학적 결론을 지을 땐 반드시 혀를 조심해서 설명해야 하는데, 이 녀석이 기준선이라는 이름의 말뚝에 수식적으로 단단히 묶여있기 때문입니다. 예를 들어, 우리가 간질발작 스위치를 바닥의 기준점으로 말뚝 박았다고 해봅시다. 그러면 우리는 저기 튀어나온 절편 $\beta_{\text{stroke}0}$ 이라는 숫자를 두고, "뒤에 있는 모든 변수 잡파라미터들($x_1=\dots=x_p$)이 싸그리 '0' 으로 닫혀 있을 때, 말뚝인 간질 발작과 싸워 이기는 고고한 뇌졸중만의 단독 로그 오즈(Log-odds)" 라는 뜻으로 입 아프게 해석해야만 합니다! 더욱이 만약 변수 $X_j$ 가 인위적으로 1 단위 딱 상승한다 쳤을 때 나타나는 부가 파마리터인 저 $\beta_{\text{stroke}j}$ 가중치는 '간질과 대결하는 뇌졸중의 로그 오즈 비율이 고만큼 증가한다'고 수식화됩니다. 또 다른 수식으로 말하자면 배수가 마법처럼 $e^{\beta_{\text{stroke}j}}$ 만큼 곱셈되어 치솟습니다.

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding. The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding. But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it. In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k = 1, \dots, K$,
이제 우리는 복잡한 저따위 기준점 다항식 룰 설정의 모델 코딩 수고로움을 덜어줄 훨씬 강력하고 새로운 대안적 코딩 체계 하나를 짧게 던집니다. 모두에게 그 명창이 널리 알려진 저명한 **소프트맥스(Softmax)** 코딩입니다! 코딩 껍데기를 저 위 다항식으로 쓰든 소프트맥스로 쓰든 간에, '결과적으로' 최종 내뱉어지는 적합 예측 확률이라든지 어떤 클래스 쌍 사이의 로그 오즈 배율 비율이라든지 여타 핵심적인 모델의 최종 출력 성과값들은 (코딩에 구애받지 않고) 언제나 죽었다 깨어나도 동일하다는 점에서 아까 전의 기준점 똥개 훈련 코딩 룰과 완전히 등가동치(Equivalent)인 것은 맞습니다. 하지만, 현대 머신러닝의 무수한 기계학습 컴퓨터 과학 논문과 서적 문헌 세계들 구석구석에서는 이 소프트맥스 양식이 징그럽도록 폭넓게 광범위하게 사용되고 있으므로 (그리고 대망의 10장 딥러닝 인공신경망 챕터에서 이 녀석이 똑같이 위풍당당하게 또 지옥처럼 재출현할 예정이므로), 충분히 이 괴물의 수학적 형태를 눈도장 찍어 미리 알아두고 대비할 가치가 엄청납니다. 기준선 클래스 하나를 잡아서 제물로 밧줄로 묶어놓았던 아까 저 통계학도다운 옹졸한 코딩과는 차원을 달리하여, 이 소프트맥스 시스템 안에서는 그냥 통 크게 완전히 대칭적으로 평등하게 전체 $K$ 모든 클래스들을 똑같은 신분으로 우대 취급하며 다음과 같은 우아한 통합 확률 공식을 거느립니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.13)
$$

Thus, rather than estimating coefficients for $K - 1$ classes, we actually estimate coefficients for all $K$ classes. It is not hard to see that as a result of (4.13), the log odds ratio between the $k$th and $k'$th classes equals
그 결과로, 우리는 옹색하게 기준점 빼고 나머지 덜떨어지는 $K-1$ 만큼 클래스만 가중치를 추정하고 뺄셈을 하는 대신에, 오히려 대범하게 모든 1부터 끝까지 열거된 모든 $K$개 클래스 전체에 대해 각자의 완전무결한 계수가중치 세트를 무식하게 모조리 계산(추정)해버리는 컴퓨터 연산 파워를 갖게 됩니다. (4.13) 수식 결과표를 직접 눈으로 받아보고 나면, 아무렇게나 뽑은 임의의 $k$ 번째와 $k'$ 번째 두 녀석들 사이에서 벌어지는 로그 오즈 배율을 계산해 봤을 때 가중치의 아주 깔끔한 '빼기 뺄셈' 단발 형태인 $X\beta_{k} - X\beta_{k'}$ 차이 모양새로 똑 떨어지는 것을 파악하는 건 자명하게 어렵지 않습니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = k' \mid X = x)} \right) = (\beta_{k0} - \beta_{k'0}) + (\beta_{k1} - \beta_{k'1}) x_1 + \dots + (\beta_{kp} - \beta_{k'p}) x_p \quad (4.14)
$$

This is the document for this topic.

---

## Sub-Chapters (하위 목차)

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans1.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans1.html)

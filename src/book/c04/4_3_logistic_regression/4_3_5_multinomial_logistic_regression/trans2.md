---
layout: default
title: "trans2"
---

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans2.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.3.5 Multinomial Logistic Regression
# 4.3.5. 다항 로지스틱 회귀 (카테고리가 여러 마리일 때 호랑이 굴에서 살아남기)

We sometimes wish to classify a response variable that has more than two classes.
지금까지 우리는 기껏해야 딱 두 가지 범주(Yes or No, 파산한다/안 한다)에 속하는 이진 반응 변수를 분류해왔지만, 실전 현장에서는 가끔씩 두 개를 아득히 초과하는 엄청나게 많은 다중 클래스를 가진 타깃 범인을 골라 잡아야 하는 극악무도한 임무를 하달받기도 합니다.

For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure`.
예를 들어 볼까요? 앞선 4.2장 도입부 응급실 병명 분류 예제에서는 타깃 카테고리가 꼴랑 두 개가 아니었습니다. `뇌졸중(stroke)`, `약물과다복용`, `간질`이라는 세 가지 범주형 카테고리가 엮여 있었습니다.

However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable.
그런데 환장하게도, 지금까지 우리가 이 긴 단원에서 낑낑대며 줄기차게 배운 그 로지스틱 곡선 S자 회귀 접근법은 태생의 한계상 반응 변수 카테고리 세팅장이 오직 양자택일 $K=2$ 수준 규모일 때만 정상 가동을 허용해 주는 기술이었습니다.

It turns out that it is possible to extend the two-class logistic regression approach to the setting of $K > 2$ classes.
수학자들의 집요함에 박수를 보냅니다. 기쁘게도 이 두 가지 한정된 2-클래스 이분법 로지스틱 회귀 접근법을, 수학적으로 쭉쭉 늘리고 개조시켜서 $K>2$ 이상인 복잡한 다중 선택지 클래스 환경으로 확장 통용시키는 멋진 아이디어가 완성되어 가능하다는 것이 판명되었습니다.

This extension is sometimes known as _multinomial logistic regression_.
이 수학적 확장팩 파츠는 통계학 필드 책에서 이따금씩 **다항 로지스틱 회귀(Multinomial Logistic Regression)** 라는 좀 더 무겁고 고상한 명찰 이름표로 호명되게 됩니다.

To do this, we first select a single class to serve as the _baseline_; without loss of generality, we select the $K$th class for this role.
이 무지막지한 짓을 벌이기 위해, 우리는 확률의 영점을 잡기 위한 제물 하나가 필요합니다. 우리는 우선 단 한 개의 고유 클래스를 골라잡아 절대 흔들리지 않게 바닥에 박아두는 앵커 역할인 **기준점(baseline)** 으로 삼아 배정합니다; 논의의 보편성을 상실하지 않고 단순화하기 위해, 우리는 편의상 대강 리스트 맨 마지막 번호인 $K$ 번째 녀석 카테고리를 잡아다 이 희생양 역할 자리에 지정해 버리겠습니다.

Then we replace the model (4.7) with the model
그러고 나면 우리는 종전 (4.7)번 모델 수식을 다음 다항 모델식 체계로 뚝딱 완전히 교체시켜 버릴 수 있습니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and
(이 식은 나머지 $k = 1$ 부터 $K-1$ 번째 까지의 쩌리 클래스 타깃 확률들에 모두 대응하는 일반식이고) 그리고 저 대망의 제물인 기준점 맨 우두머리 타깃 $K$ (즉 $K$번째 타겟일 확률) 자체에 대해서는 이렇게 분자를 날려 역수를 취합니다:

$$
\text{Pr}(Y = K \mid X = x) = \frac{1}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$,
이 공식을 뚫어지게 들여다보면, 기준점과 $k = 1, \dots, K-1$ 번째 타깃들에 대해서 다음과 같은 공식이 숨구멍 하나 막히지 않고 기깔나게 성립한다는 것을 수학적으로 증명하는 게 그리 어려운 일이 아닙니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = \beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p \quad (4.11)
$$

Notice that (4.11) is quite similar to (4.6).
저 괄호 속 (4.11) 수식이 아까 전 이진 분류 단원에서 지겹게 관찰했던 (4.6) 덩어리 식방정식 기호들과 머리가 어지러울 정도로 얼마나 수상하리만치 무척 똑 닮아있는지 놀라워해 보십시오.

Equation 4.11 indicates that once again, the log odds between any pair of classes is linear in the features.
(4.11) 방정식이 우리에게 시사하고 귀띔해 주는 진실은 바로, 이번 다항 판국에서도 여전히 그 어떠한 기준 쌍의 대결 클래스들 사이에 끼이어 구축된 도박판 지표 **로그 오즈(log odds)** 스펙 수치는, 역시 언제나 우측 편의 $X$ 예측 변수 피쳐 특징들과 완벽한 1차식 구조의 **선형(linear)** 을 이루도록 반듯하게 비례한다는 변함없는 약속입니다.

It turns out that in (4.9)–(4.11), the decision to treat the $K$th class as the baseline is unimportant.
게다가 그 요란한 (4.9)에서 (4.11)로 향하는 수학적 전개 도출 속에서, 굳이 마지막 녀석인 $K$번째를 잡아다가 기준선 앵커로 제물로 바치겠다는 당신의 대충 내린 결정 프로세스 자체는 결과론적으로 모델 수립 운명에 그다지 중요하지 않은 사안임이 다행스럽게도 드러났습니다.

For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline.
가령 응급실 방문 환자의 병명을 `뇌졸중`, `약물 중독`, `간질`이라는 세 가지 카테고리로 멱살 잡아 분류해 낼 때, 우리가 두 방면의 독립적인 다항 로지스틱 예측 모델을 컴퓨터로 피팅했다고 시뮬레이션해 봅시다: 한 놈의 모델은 '뇌졸중'을 바닥의 기준점으로 묶은 것이고, 또 다른 한 놈 모델은 '약물 중독'을 기준점으로 잡고 훈련시킨 것입니다.

The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.
이때 컴퓨터가 산출해 배출시킨 회귀 계산 계수(Weight 추정치) 숫자 장부 자체는 기준점이 달라짐에 따라 모델 간에 천차만별 다르게 인쇄되어 나오겠지만, **최종적으로 이 모형이 뱉어내는 1등 타깃 찍기의 확률 예측 적합값(Fitted Values)** 이라든지, 어떤 쌍의 대결 구도에 끼여있는 근본적인 로그 오즈 배율이라든지, 그리고 절대 바뀌면 안 되는 예측 핵심 모델 출력 산출물 수치들은 모조리 완전히 토씨 하나 안 틀리고 똑같이 유지된다는 것입니다! 아무런 상관이 없는 것입니다.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline.
그럼에도 불구하고, 저렇게 모델 속에서 튀어나온 다중 회귀 계수파라미터들의 명확한 기계 수치 스펙 '해석'을 사람들에게 브리핑해 내고 구명 결론을 지을 땐 절대로 혀를 가볍게 놀리고 오판하지 말고 세심한 주의를 거쳐야만 합니다. 왜냐하면 그 숫자들 자체가 당신이 변덕스럽게 선택했던 그 '기준선'이라는 말뚝의 입장에 수식적으로 단단히 종속되어 묶여있기 때문(tied to)입니다.

For example, if we set `epileptic seizure` to be the baseline, then we can interpret $\beta_{\text{stroke}0}$ as the log odds of `stroke` versus `epileptic seizure`, given that $x_1 = \dots = x_p = 0$.
예를 들어, 우리가 변덕을 부려 '간질 발작' 스위치를 바닥의 기준점(baseline)으로 말뚝을 쾅 박아 세팅했다고 해봅시다. 그러면 우리는 저기 튀어나온 상수 절편 $\beta_{\text{stroke}0}$ 이라는 숫자를 두고, "뒤에 있는 모든 변수 잡 파라미터들($x_1 = \dots = x_p$) 스위치가 단 하나도 켜지지 않은 0의 백지 상태 조건에서, 오롯이 기준선인 간질 발작과 싸워 이기는 자생적인 뇌졸중만의 단독 로그 오즈(log odds)" 라고 엄청나게 입 아프고 엄밀하게 해석해야만 합니다!

Furthermore, a one-unit increase in $X_j$ is associated with a $\beta_{\text{stroke}j}$ increase in the log odds of `stroke` over `epileptic seizure`.
더욱이 나아가서 수식을 볼까요? 만약 변수 $X_j$ 치수가 인위적으로 1 단위 딱 상승한다 쳤을 때 나타나는 저 $\beta_{\text{stroke}j}$ 가중치는, 오직 '간질(기준)' 그룹과 맞짱 대결하는 '뇌졸중' 녀석 간의 파워의 격차(로그 오즈) 수치가 저만큼 위로 증가 상승한다는 무시무시한 메커니즘과 연관이 되어버립니다.

Stated another way, if $X_j$ increases by one unit, then the ratio increases by $e^{\beta_{\text{stroke}j}}$.
또 다른 쉬운 언어로 말하자면, 만약 $X_j$가 한 단위씩 증가 펌핑이 될 때마다 로그를 풀었으니 결국 그 오즈 배율 비율 자체는 우주적으로 $e^{\beta_{\text{stroke}j}}$ 만큼 눈덩이 곱셈되어 치솟는 폭발력을 가집니다.

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding.
이제 우리는 저런 복잡한 기준점 다항식 룰 설정의 모델 코딩 수고로움과 혼돈을 완전히 털어낼 훨씬 강력하고 현대적인 새로운 대안적 변환 체계 하나를 짧게 던집니다. 바로 그 위대한 명창이 널리 알려진 **소프트맥스(softmax) 코딩** 기법입니다!

The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding.
코딩 설계도 껍데기를 저 위 다항식으로 쓰든, 소프트맥스로 쓰든 상관없습니다. '결과적으로' 이 녀석이 최종 내뱉는 적합 예측 결과 확률이라든지 임의의 특정 쌍 사이 클래스들 간의 로그 오즈 비율이라든지 여타 핵심적인 모델의 통계 출력 성과값들은 (코딩의 종류에 구애받지 않고 무던하게) 언제나 동일한 정답 선상에서 유지된다는 점에서, 아까 전의 '기준점 방식 코딩' 세팅 룰 메커니즘과 사실 완전히 동전의 양면같이 등가(Equivalent)인 녀석이기 때문입니다.

But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it.
하지만 이 소프트맥스 코딩은 현대 머신러닝의 무수한 기계학습 논문과 서적 문헌 세계들 구석구석에서 징그럽도록 폭넓고 광범위한 위상으로 사랑받으며 사용되고 있으므로 (그리고 대망의 10장 딥러닝 뉴럴 네트워크 챕터에서 이 녀석이 완전 동일하게 위풍당당 재출현할 찬란한 예정이므로), 충분히 이 수식의 기본 형태 구조를 지금 눈도장 찍어 미리 알아두고 대비할 가치가 엄청납니다.

In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k = 1, \dots, K$,
소프트맥스 함수 코딩 방식의 세계관은 이렇습니다: 무작위 기준선 클래스 하나를 잡아서 제물로 밧줄로 묶어 편애하던 아까 통계학의 그 옹졸한 기준 클래스 코딩과는 차원을 달리합니다. 소프트맥스 시스템 안에서는 그냥 통 크게 완전히 대칭적이고 공평무사하게 전체 모든 $K$개 클래스 형제들을 똑같은 신분 계급으로 우대 취급하며 다음과 같은 우아한 통합 확률 공식을 거느리고 모두를 감싸 안아 가정합니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.13)
$$

Thus, rather than estimating coefficients for $K - 1$ classes, we actually estimate coefficients for all $K$ classes.
마법 같은 수식 도출의 결과로, 우리는 옹색하게 기준점 1개를 멋대로 빼놓고 나머지 덜떨어진 쪼가리 $K-1$ 묶음 개수 클래스에 대해서만 $\beta$ 계수를 추정하고 뺄셈을 하는 복잡한 노동력 대신에, 사실상 시원하고 대범하게 1부터 끝까지 열거된 모든 $K$개 소속 클래스 전체에 대해 각자의 완전무결한 계수가중치 세트를 무식하게 모조리 계산(추정)해버리는 컴퓨터 연산 로직 파워 구조를 세팅 갖게 됩니다.

It is not hard to see that as a result of (4.13), the log odds ratio between the $k$th and $k'$th classes equals
이 공평한 (4.13) 소프트맥스 수식 결과표 방식을 직접 눈으로 받아보고 나면, 아무렇게나 구슬 뽑듯 뽑아든 임의의 $k$ 번째와 $k'$ 번째 두 라이벌 클래스 쌍 녀석들 사이에서 벌어지는 체감 로그 오즈 비율 지표가, 놀랍도록 가중치의 '아주 깔끔한 뺄셈' 단발 정산 형태로 다음과 완전히 수학 동치 일치가 되어 뚝! 하고 떨어진다는 것을 직관적으로 파악하는 건 결코 어렵지 않습니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = k' \mid X = x)} \right) = (\beta_{k0} - \beta_{k'0}) + (\beta_{k1} - \beta_{k'1}) x_1 + \dots + (\beta_{kp} - \beta_{k'p}) x_p \quad (4.14)
$$

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans2.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans2.html)

---
layout: default
title: "trans1"
---

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans1.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.5 Multinomial Logistic Regression
# 4.3.5. 다항 로지스틱 회귀 (Multinomial Logistic Regression)

We sometimes wish to classify a response variable that has more than two classes.
우리는 때때로 두 개 이상의 클래스를 가진 반응 변수를 분류하기를 원합니다.

For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke` , `drug overdose` , `epileptic seizure`.
예를 들어, 4.2 절에서 우리에게 응급실 의료 상태의 세 가지 카테고리인 `stroke`, `drug overdose`, `epileptic seizure`가 존재했습니다.

However, the logistic regression approach that we have seen in this section only allows for $K$ = 2 classes for the response variable.
그러나 우리가 이 절에서 본 로지스틱 회귀 접근법은 반응 변수에 대해 오직 $K = 2$ 개의 클래스만 허용합니다.

It turns out that it is possible to extend the two-class logistic regression approach to the setting of $K > 2$ classes.
($K=2$) 2-클래스 로지스틱 회귀 접근법을 $K > 2$ 개의 클래스 환경으로 확장하는 것이 가능하다는 사실이 밝혀졌습니다.

This extension is sometimes known as _multinomial logistic regression_.
이 확장은 때때로 **다항 로지스틱 회귀(multinomial logistic regression)** 로 알려져 있습니다.

To do this, we first select a single class to serve as the _baseline_; without loss of generality, we select the $K$th class for this role.
이를 수행하기 위해, 우리는 먼저 **기준점(baseline)** 역할을 수행할 단일 기준 클래스를 선택합니다; 일반성을 잃어버리지 않고, 우리는 이 역할에 $K$번째 클래스를 지정해 선택합니다.

Then we replace the model (4.7) with the model
그런 다음 모형 (4.7)을 다음과 같은 모형으로 대체합니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.9)
$$

for $k = 1, \dots, K-1$, and
(이는 $k = 1, \dots, K-1$에 대한 식이며), 그리고 다음과 같이 산출합니다:

$$
\text{Pr}(Y = K \mid X = x) = \frac{1}{1 + \sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.10)
$$

It is not hard to show that for $k = 1, \dots, K-1$,
$k = 1, \dots, K-1$에 대해 다음이 성립함을 보여주는 것은 어렵지 않습니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = K \mid X = x)} \right) = \beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p \quad (4.11)
$$

Notice that (4.11) is quite similar to (4.6).
식 (4.11)이 식 (4.6)과 매우 유사하다는 점에 주목하십시오.

Equation 4.11 indicates that once again, the log odds between any pair of classes is linear in the features.
방정식 4.11은 다시 한번, 임의의 클래스 쌍 간의 로그 오즈가 피처들에 대해 선형임을 나타냅니다.

It turns out that in (4.9)–(4.11), the decision to treat the $K$th class as the baseline is unimportant.
수식 (4.9)–(4.11)에서 $K$번째 클래스를 기준점으로 취급하려는 결정 자체는 중요하지 않은 것으로 판명되었습니다.

For example, when classifying emergency room visits into `stroke` , `drug overdose` , and `epileptic seizure` , suppose that we fit two multinomial logistic regression models: one treating `stroke` as the baseline, another treating `drug overdose` as the baseline.
예를 들어, 응급실 방문을 `stroke`, `drug overdose`, `epileptic seizure` 로 분류할 때, 하나는 `stroke`를 기준점으로 취급하고 다른 하나는 `drug overdose`를 기준점으로 취급하는 등 우리가 두 가지 다항 로지스틱 회귀 모델을 적합시킨다고 가정해 보겠습니다.

The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.
계수 추정치는 서로 상이하게 선택된 기준점들 때문에 두 적합 모델 간에 다를 수 있지만, 적합값(예측), 어떤 단일 임의 쌍 클래스 간의 로그 오즈, 그리고 다른 주요 모형 산출물들은 동일하게 유지될 것입니다.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline.
그럼에도 불구하고, 다항 로지스틱 회귀 모델에서 계수에 대한 해석은 기준점 선택에 결부되어 있기 때문에 세심한 주의를 기울여 수행해야 합니다.

For example, if we set `epileptic seizure` to be the baseline, then we can interpret $\beta_{\text{stroke}0}$ as the log odds of `stroke` versus `epileptic seizure`, given that $x_1 = \dots = x_p = 0$.
예를 들어, 우리가 기준점으로 `epileptic seizure`를 설정한다면, 우리는 $x_1 = \dots = x_p = 0$ 이 주어졌을 때 $\beta_{\text{stroke}0}$ 을 `epileptic seizure`에 대조되는 대비 `stroke`의 로그 오즈로서 해석할 수 있습니다.

Furthermore, a one-unit increase in $X_j$ is associated with a $\beta_{\text{stroke}j}$ increase in the log odds of `stroke` over `epileptic seizure`.
나아가, $X_j$의 한 단위 증가는 `epileptic seizure`에 대비한 `stroke`의 로그 오즈의 $\beta_{\text{stroke}j}$ 상승과 관련되어 있습니다.

Stated another way, if $X_j$ increases by one unit, then the ratio increases by $e^{\beta_{\text{stroke}j}}$.
달리 말해, 만약 $X_j$가 한 단위씩 증가한다면 비율은 $e^{\beta_{\text{stroke}j}}$ 만큼 곱으로 증가합니다.

We now briefly present an alternative coding for multinomial logistic regression, known as the _softmax_ coding.
이제 우리는 **소프트맥스(softmax)** 방식라고 알려진 다항 로지스틱 회귀를 위한 대체 산식(코딩 방식)을 간략하게 제시합니다.

The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding.
소프트맥스 산식은 그 계산 방식에 상관없이 예측 결과값, 임의의 특정 쌍 사이 클래스들 간의 로그 오즈, 그리고 기타 주요 모델 결과들이 동일한 선상에서 유지된다는 점에서 방금 설명한 기존 산식과 등가입니다.

But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it.
하지만 이 소프트맥스 코딩은 머신러닝 문헌의 일부 영역에서 폭넓게 광범위하게 사용되고 있기 때문에(그리고 10장에서 다시 나타날 예정입니다), 이를 인지할 절대적 가치가 있습니다.

In the softmax coding, rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k = 1, \dots, K$,
소프트맥스 함수 코딩에서는, 기준점 단골 클래스를 무작위 배정 선택하는 대신에 모든 $K$ 개 클래스 집단을 대칭적으로 평등하게 취급하고, $k = 1, \dots, K$에 대해 다음 사항을 가정 전개합니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{e^{\beta_{k0} + \beta_{k1} x_1 + \dots + \beta_{kp} x_p}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1} x_1 + \dots + \beta_{lp} x_p}} \quad (4.13)
$$

Thus, rather than estimating coefficients for $K - 1$ classes, we actually estimate coefficients for all $K$ classes.
따라서 우리는 덜떨어지게 $K-1$개 클래스에 대해서만 계수를 추정하는 대신, 사실상 모든 $K$개 클래스 전체에 대해 수고롭게 계수를 공평히 추정 연산해냅니다.

It is not hard to see that as a result of (4.13), the log odds ratio between the $k$th and $k'$th classes equals
식 (4.13)의 도출 결과로서 파생시켜보면, 임의의 고른 $k$번째와 $k'$번째 쌍 클래스들 간에 낀 로그 오즈 비율이 다음과 똑같이 전락함을 보는 일은 결코 어렵지 않습니다:

$$
\log\left( \frac{\text{Pr}(Y = k \mid X = x)}{\text{Pr}(Y = k' \mid X = x)} \right) = (\beta_{k0} - \beta_{k'0}) + (\beta_{k1} - \beta_{k'1}) x_1 + \dots + (\beta_{kp} - \beta_{k'p}) x_p \quad (4.14)
$$

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters (하위 목차)

[< 4.3.4 Multiple Logistic Regression](../4_3_4_multiple_logistic_regression/trans1.html) | [4.4 Generative Models For Classification >](../../4_4_generative_models_for_classification/trans1.html)

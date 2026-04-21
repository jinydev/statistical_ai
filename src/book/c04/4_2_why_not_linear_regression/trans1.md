---
layout: default
title: "trans1"
---

[< 4.1 An Overview Of Classification](../4_1_an_overview_of_classification/trans1.html) | [4.3 Logistic Regression >](../4_3_logistic_regression/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.2 Why Not Linear Regression?
# 4.2. 왜 선형 회귀를 쓰면 안 되는가? (Why Not Linear Regression?)

We have stated that linear regression is not appropriate in the case of a qualitative response.
우리는 앞서 질적 반응 변수(Qualitative Response)의 경우에는 선형 회귀가 적합하지 않다고 언급했습니다.

Why not?
그 이유는 무엇일까요?

Suppose that we are trying to predict the medical condition of a patient in the emergency room on the basis of her symptoms.
응급실에 온 환자의 증상을 바탕으로 환자의 병명을 예측하려고 한다고 가정해 보겠습니다.

In this simplified example, there are three possible diagnoses: `stroke`, `drug overdose`, and `epileptic seizure`.
이 간소화된 예제에는 `뇌졸중(stroke)`, `약물 과다복용(drug overdose)`, `간질성 발작(epileptic seizure)` 이라는 세 가지 가능한 진단이 존재합니다.

We could consider encoding these values as a quantitative response variable, $Y$, as follows:
우리는 이러한 값들을 다음과 같은 수치형 반응 변수 $Y$로 인코딩하는 것을 고려해 볼 수 있습니다:

$$
Y =  \begin{cases} 
1 & \text{if stroke} \\ 
2 & \text{if drug overdose} \\ 
3 & \text{if epileptic seizure} 
\end{cases}
$$

Using this coding, least squares could be used to fit a linear regression model to predict $Y$ on the basis of a set of predictors $X_1, \dots, X_p$.
이 코딩 방식을 사용하면, 예측 변수들 $X_1, \dots, X_p$을 바탕으로 최소 제곱법(Least Squares)을 사용해 $Y$를 예측하는 선형 회귀 모델을 피팅할 수 있습니다.

Unfortunately, this coding implies an ordering on the outcomes, putting `drug overdose` in between `stroke` and `epileptic seizure`, and insisting that the difference between `stroke` and `drug overdose` is the same as the difference between `drug overdose` and `epileptic seizure`.
불행히도 이 코딩 방식은 결과들 간에 '순서(Ordering)'가 있음을 의미하게 되어, `약물 과다복용`을 `뇌졸중`과 `간질성 발작` 사이에 위치시키고, `뇌졸중`과 `약물 과다복용` 사이의 차이가 `약물 과다복용`과 `간질성 발작` 사이의 차이와 완전히 동일하다고 가정하게 됩니다.

In practice there is no particular reason that this needs to be the case.
현실적으로 이런 방식이 합리적이어야 할 이유는 전혀 없습니다.

For instance, one could choose an equally reasonable coding,
예를 들어, 우리는 다음과 같이 동등하게 합리적인 다른 코딩 방식을 선택할 수도 있습니다:

$$
Y =  \begin{cases} 
1 & \text{if epileptic seizure} \\ 
2 & \text{if stroke} \\ 
3 & \text{if drug overdose} 
\end{cases}
$$

which would imply a totally different relationship among the three conditions.
이 방식은 위의 세 가지 상태들 사이에 완전히 다른 관계를 설정하게 됩니다.

Each of these codings would produce fundamentally different linear models that would ultimately lead to different sets of predictions on test observations.
각각의 코딩 방식들은 근본적으로 전혀 다른 선형 모델을 생성하게 되고, 결과적으로 테스트 관측치에 대해 매우 다른 예측들을 도출하게 됩니다.

If the response variable’s values did take on a natural ordering, such as _mild_, _moderate_, and _severe_, and we felt the gap between mild and moderate was similar to the gap between moderate and severe, then a 1, 2, 3 coding would be reasonable.
만약 반응 변수의 값들이 `가벼움(mild)`, `보통(moderate)`, `심각함(severe)`처럼 자연스러운 순서를 띄고 있고, 가벼움과 보통 사이의 간격이 보통과 심각함 사이의 간격과 거의 비슷하다고 느낀다면 1, 2, 3 코딩이 꽤 합리적일 수 있습니다.

Unfortunately, in general there is no natural way to convert a qualitative response variable with more than two levels into a quantitative response that is ready for linear regression.
하지만 불행히도 일반적으로는 이렇게 2개 이상의 범주를 가지는 질적 반응 변수를 선형 회귀에 투입할 수 있도록 자연스러운 수치형으로 변환시킬 방법이 사실상 없습니다.

For a _binary_ (two level) qualitative response, the situation is better.
이진형(두 가지 레벨을 가지는, Binary) 질적 반응 변수에 대해서는 사정이 꽤 나은 편입니다.

For binary instance, perhaps there are only two possibilities for the patient’s medical condition: `stroke` and `drug overdose`.
가령 환자의 병명이 `뇌졸중`과 `약물 과다복용` 오직 두 가지뿐인 경우라고 가정해봅시다.

We could then potentially use the _dummy variable_ approach from Section 3.3.1 to code the response as follows:
우리는 잠재적으로 3.3.1 단원에서 배웠던 더미 변수(Dummy Variable) 접근 방식을 가져와서 반응 변수를 다음과 같이 코딩할 수 있습니다:

$$
Y =  \begin{cases} 
0 & \text{if stroke} \\ 
1 & \text{if drug overdose} 
\end{cases} \quad (4.1)
$$

We could then fit a linear regression to this binary response, and predict `drug overdose` if $\hat{Y} > 0.5$ and `stroke` otherwise.
그런 다음 이 이항 데이터에 선형 회귀를 적합시키고, 만약 $\hat{Y} > 0.5$ 이면 `약물 과다복용`으로 예측하고, 반대면 `뇌졸중`으로 예측할 수 있습니다.

In the binary case it is not hard to show that even if we flip the above coding, linear regression will produce the same final predictions.
이진 분류의 경우에는 위에서 말한 코딩 방식을 뒤집는다 하더라도 선형 회귀 모형이 동일한 최종 예측을 도출해 냄을 증명하기 어렵지 않습니다.

For a binary response with a 0/1 coding as above, regression by least squares is not completely unreasonable: it can be shown that the $X\hat{\beta}$ obtained using linear regression is in fact an estimate of $\text{Pr}(\text{drug overdose} | X)$ in this special case.
위와 같은 0과 1의 코딩을 가지는 이진 반응 변수의 경우, 최소 제곱법을 이용한 회귀가 완전히 터무니없는 것은 아닙니다: 선형 회귀를 이용하여 얻어낸 $X\hat{\beta}$가 이 특수한 사례에서는 실제로 $\text{Pr}(\text{drug overdose} | X)$ (약물 과다복용일 확률)의 추정치라는 것을 보여줄 수 있습니다.

However, if we use linear regression, some of our estimates might be outside the $[0, 1]$ interval (see Figure 4.2), making them hard to interpret as probabilities!
그러나 선형 회귀를 돌릴 경우, 우리 추정치들 중 몇몇은 $[0, 1]$ 구간을 벗어날 수 있으며(그림 4.2 참조), 이로 인해 이를 확률로 해석하는 것을 매우 어렵게 만듭니다!

Nevertheless, the predictions provide an ordering and can be interpreted as crude probability estimates.
그럼에도 불구하고 이 예측치들은 순서를 제공하며 대략적인 확률 추정치로 쓰일 수 있습니다.

Curiously, it turns out that the classifications that we get if we use linear regression to predict a binary response will be the same as for the linear discriminant analysis (LDA) procedure we discuss in Section 4.4.
흥미롭게도, 이진 데이터 확률 예측에 선형 회귀를 돌려서 얻어내는 분류 그룹은 우리가 차후 4.4 섹션에서 논의할 선형 판별 분석(LDA) 절차를 통해 얻게 되는 것과 정확히 똑같다는 것이 밝혀졌습니다.

To summarize, there are at least two reasons not to perform classification using a regression method:
요약하자면, 분류 문제에서 회귀 방법론을 쓰면 안 되는 최소한 2가지 이유는 다음과 같습니다:

(a) a regression method cannot accommodate a qualitative response with more than two classes;
(a) 회귀 방법은 3개 이상의 클래스를 가지는 질적 반응 변수를 수용할 수 없습니다.

(b) a regression method will not provide meaningful estimates of $\text{Pr}(Y | X)$, even with just two classes.
(b) 회귀 방법은 클래스가 단 두 개라고 하더라도 정당한 $\text{Pr}(Y | X)$의 추정치를 의미 있게 도출해 내지 못합니다.

Thus, it is preferable to use a classification method that is truly suited for qualitative response values.
따라서, 질적 응답 변수에 진정으로 부합하는 전용 분류 방법론을 적용하는 것이 훨씬 바람직합니다.

In the next section, we present logistic regression, which is well-suited for the case of a binary qualitative response; in later sections we will cover classification methods that are appropriate when the qualitative response has two or more classes.
다음 섹션에서는 이분법 양적 반응에 잘 맞는 로지스틱 회귀(Logistic Regression)를 제시하며, 후속 섹션에서는 질적 응답 변수가 두 개 이상의 클래스를 가질 때 적합한 분류 방법들을 다룰 것입니다.

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters

[< 4.1 An Overview Of Classification](../4_1_an_overview_of_classification/trans1.html) | [4.3 Logistic Regression >](../4_3_logistic_regression/trans1.html)

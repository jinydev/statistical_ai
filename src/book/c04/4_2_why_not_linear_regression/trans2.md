---
layout: default
title: "trans2"
---

[< 4.1 An Overview Of Classification](../4_1_an_overview_of_classification/trans2.html) | [4.3 Logistic Regression >](../4_3_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.2 Why Not Linear Regression?
# 4.2. 왜 선형 회귀를 쓰면 안 되는가? (선 긋기의 치명적 한계)

We have stated that linear regression is not appropriate in the case of a qualitative response. Why not?
우리는 앞서 챕터 3에서 그렇게나 사랑했던 '선형 회귀' 녀석이, 혈액형처럼 질적으로 딱딱 나뉘는 질적 반응 변수(Qualitative Response) 문제 앞에서는 결코 제구실을 못하는 매우 부적합한 녀석이라고 단호히 앞서 언급했습니다. 도대체 왜 안 되는 걸까요?

Suppose that we are trying to predict the medical condition of a patient in the emergency room on the basis of her symptoms. In this simplified example, there are three possible diagnoses: `stroke`, `drug overdose`, and `epileptic seizure`. We could consider encoding these values as a quantitative response variable, $Y$, as follows:
끔찍한 가정을 해봅시다. 응급실에 실려 온 환자의 여러 증상 단서들을 바탕으로 이 환자의 병명 상태를 예측하려 시도한다고 가정해 보겠습니다. 이 간소화된 예제 병동에는 오직 세 가지 가능한 절망적 진단명: `뇌졸중(stroke)`, `약물 과다복용(drug overdose)`, 그리고 `간질성 발작(epileptic seizure)` 이 존재합니다. 답(글자)을 숫자로 바꿔야 컴퓨터가 알아먹으니, 우리는 이 글자 값들을 무식하게 다음과 같은 수치형 반응 변수 $Y$ 로 번호표를 매겨 인코딩해 버리는 만행을 고려해 볼 수 있습니다:

$$
Y =  \begin{cases} 
1 & \text{if stroke} \\ 
2 & \text{if drug overdose} \\ 
3 & \text{if epileptic seizure} 
\end{cases}
$$

Using this coding, least squares could be used to fit a linear regression model to predict $Y$ on the basis of a set of predictors $X_1, \dots, X_p$. Unfortunately, this coding implies an ordering on the outcomes, putting `drug overdose` in between `stroke` and `epileptic seizure`, and insisting that the difference between `stroke` and `drug overdose` is the same as the difference between `drug overdose` and `epileptic seizure`. In practice there is no particular reason that this needs to be the case. For instance, one could choose an equally reasonable coding,
이 끔찍한 코딩 번호표 방식을 고집하면, 일단 우리에게 친숙한 수리 도구인 최소 제곱법(Least Squares)을 돌려 예측 변수 타깃들 $X_1, \dots, X_p$ 을 바탕으로 막무가내 $Y$ 를 예측해 내는 억지 선형 회귀 모델 선을 피팅(fit)해 그려볼 수는 꾸역꾸역 있습니다. 불행히도, 이 숫자를 매긴 코딩 짓은 결과들 간에 '강력한 서열과 순서(Ordering)'가 숨어 있다는 치명적 오해를 컴퓨터에게 스파이처럼 무단 암시(implies)하게 됩니다! 즉, `약물 과다복용(2번)`을 억지로 `뇌졸중(1번)`과 `간질성 발작(3번)`의 중간 순위에 우겨 넣게 되고, 심지어 나아가 `뇌졸중(1번)`과 `약물 과다복용(2번)` 사이의 1칸 차이 격차가 `약물 과다복용(2번)`과 `간질성 발작(3번)` 사이의 1칸 차이 거리와 수학적으로 완벽히 동일한 물리적 차이라 결코 고집하며 우기게 되는 꼴입니다. 의학 현장 현실에서 이딴 식으로 병명 사이의 거리가 칼같이 합리적이어야 할 특별한 이유는 일절 없습니다! 예를 들어 단연코, 어느 미친 의사는 똑같이 합리성을 내세우며 다음과 같은 엉뚱한 코딩 순서를 채택 통보해 선택할 수도 있습니다:

$$
Y =  \begin{cases} 
1 & \text{if epileptic seizure} \\ 
2 & \text{if stroke} \\ 
3 & \text{if drug overdose} 
\end{cases}
$$

which would imply a totally different relationship among the three conditions. Each of these codings would produce fundamentally different linear models that would ultimately lead to different sets of predictions on test observations.
보셨나요? 섞어버린 이 코딩 방식은 위의 세 가지 아픈 병명 상태들 사이에 완전히 딴판인 지옥의 관계 거리를 새로 설정하게 됩니다. 숫자를 어떻게 맘대로 매기느냐에 따라 각각의 이 코딩 방식들은 뼈대부터 근본적으로 전혀 다른 기괴한 선형 모델 선들을 매번 마구잡이로 생산 도출해 내게 되고, 결과적으로 테스트 관측치 환자들에 대해 치명적으로 매우 엇갈린 처방 예측들의 조합 결론들을 궁극적으로 재차 이끈다는 참극을 맞게 됩니다.

If the response variable’s values did take on a natural ordering, such as _mild_, _moderate_, and _severe_, and we felt the gap between mild and moderate was similar to the gap between moderate and severe, then a 1, 2, 3 coding would be reasonable. Unfortunately, in general there is no natural way to convert a qualitative response variable with more than two levels into a quantitative response that is ready for linear regression.
물론 타깃 반응 변수의 정답 글자 값들이 애초부터 태생적으로 `가벼움(mild)`, `보통(moderate)`, `위독함(severe)`처럼 단조롭고 매우 자연스러운 순서 위계를 띠고 있고, 심지어 가벼움과 보통 사이의 증상 간격이 마침 보통과 위독함 사이의 간격과 거의 공평하게 비슷하다고 우리가 양심적으로 느낀다면, 저 1번, 2번, 3번 코딩을 매기는 행위는 꽤 합리적으로 수용 작용될 수 있습니다. 하지만 불행히도 일반적으로는, 이렇게 2개 층위 이상의 다수 범주 레벨을 단연 가지는 순수 질적 반응 변수를 선형 회귀에 무단 투입할 채비를 위해 한 줄짜리 숫자로 정연히 펴서 나열하는 수치형으로 포장 변환시킬 자연주의적인 예쁜 방법이 인류에겐 사실상 단절 전무하다는 게 비극입니다.

For a _binary_ (two level) qualitative response, the situation is better. For binary instance, perhaps there are only two possibilities for the patient’s medical condition: `stroke` and `drug overdose`. We could then potentially use the _dummy variable_ approach from Section 3.3.1 to code the response as follows:
하지만 절망하긴 이릅니다! 오직 답이 두 개뿐인 이진형(two level, Binary) 질적인 반응 변수에 대해서는 사정이 꽤 나은 안도 편입니다. 가령 범인이 단둘뿐인 치명적 이진 상황을 가정해봅시다. 환자의 병명 가능성이 `뇌졸중`과 `약물 과다복용` 오직 두 가지뿐이라면? 우리는 잠재적으로 과거 영광의 3.3.1 단원에서 배웠던 **더미 변수(Dummy Variable) 대리인 접근 방식**을 냅다 가져와서, 우리의 주인공 반응 타깃 변수를 다음과 같이 산뜻하게 코딩 조작할 수 있습니다:

$$
Y =  \begin{cases} 
0 & \text{if stroke} \\ 
1 & \text{if drug overdose} 
\end{cases} \quad (4.1)
$$

We could then fit a linear regression to this binary response, and predict `drug overdose` if $\hat{Y} > 0.5$ and `stroke` otherwise. In the binary case it is not hard to show that even if we flip the above coding, linear regression will produce the same final predictions.
이렇게 예쁜 0과 1 번호표만 달아둔 다음 이 이항 무단 데이터에 선형 회귀선을 스윽 맞추고 피팅(fit) 시키면, 예측선 값이 만약 $\hat{Y} > 0.5$ 위로 붕 뜨면 "이놈은 `약물 과다복용` 쪽이군!"으로 단언 예측하고, 아니면 반대로 가라앉으면 "`뇌졸중`이군!"으로 쳐내어 예측할 단계를 수반할 수 있습니다. 놀랍게도 오직 이진(Binary) 케이스 분류의 경우엔 위에서 번호표 코딩 방식을 거꾸로 뒤집는다(`뇌졸중`=1, `약물`=0)고 하더라도 우리의 뚝심 있는 선형 회귀 모형이 동일한 최종 편식 예측을 끄떡없이 도출해 낸다는 무던한 사실을 보여 증명해 내기 어렵지 않습니다.

For a binary response with a 0/1 coding as above, regression by least squares is not completely unreasonable: it can be shown that the $X\hat{\beta}$ obtained using linear regression is in fact an estimate of $\text{Pr}(\text{drug overdose} | X)$ in this special case. However, if we use linear regression, some of our estimates might be outside the $[0, 1]$ interval (see Figure 4.2), making them hard to interpret as probabilities! Nevertheless, the predictions provide an ordering and can be interpreted as crude probability estimates. Curiously, it turns out that the classifications that we get if we use linear regression to predict a binary response will be the same as for the linear discriminant analysis (LDA) procedure we discuss in Section 4.4.
자, 위와 같은 0과 1의 코딩을 가지는 이진 반응 변수의 단순 케이스라면, 그 잘난 최소 제곱법을 고집 이용한 선형 회귀 짓이 완전히 터무니없는 돌아버린 짓거리는 아닙니다. 선형 회귀선을 죽 그어 돌려서 얻어낸 예측선 $X\hat{\beta}$ 가 이 특수한 특권 사례에서는 통계학적으로 실제로 저 환자가 바로 $\text{Pr}(\text{drug overdose} | X)$ (`약물 과다복용일 확률`) 퍼센티지 수치의 직접적 추정치라는 것을 기염 입증 보여줄 수까지도 있습니다. **그러나!!** 이 선형 회귀 직선의 치명적 결함! 선을 긋다 보면, 우리 추정 확률치들 중 일부 몇몇은 무참히 상식적인 확률의 세계인 $[0, 1] \; (0\% ~ 100\%)$ 구간 벽 밖을 뚫고 나가, -20% 확률이나 150% 확률 같은 미친 외곽 수치(outside)로 치솟거나 바닥을 쳐버릴 수 있으며(그림 4.2 처참한 상황조장 참조), 이 환장할 노릇으로 인해 이를 유의미한 확률(probabilities)로 올곧게 진단 해석하는 것을 단연 고통스럽고 어렵게 만듭니다! 그럼에도 불구하고 이 미친 예측치 곡선 수위들은 병명에 대한 우열 순서 단계를 분명 제공하며 꽤나 거친 대략적인 확률 척도 추정치들로 그나마 해석되어 써먹일 수는 있습니다. (흥미롭게도, 0과 1짜리 이진 데이터 확률 예측에 이 미쳐버린 선형 회귀를 억지로라도 돌려서 얻어내는 최후의 분류 그룹 집단 지도는, 우리가 아주 멀고 훗날 차후 4.4 섹션에서 심도 깊게 고매하게 논의할 진짜 전용 도구 **선형 판별 분석(LDA)** 절차를 통해 아름답게 얻게 되는 그것과 소름 끼치도록 정확히 똑같을 것이라는 점이 밝혀지고 맙니다.)

To summarize, there are at least two reasons not to perform classification using a regression method: (a) a regression method cannot accommodate a qualitative response with more than two classes; (b) a regression method will not provide meaningful estimates of $\text{Pr}(Y | X)$, even with just two classes. Thus, it is preferable to use a classification method that is truly suited for qualitative response values. In the next section, we present logistic regression, which is well-suited for the case of a binary qualitative response; in later sections we will cover classification methods that are appropriate when the qualitative response has two or more classes.
대장정의 요약 타임! 부디 단호하게, 물건 분류 문제에서 섣부른 선형 회귀 유혹 방법론을 쓰면 절대 치명 안 되는 최소한 2가지 막강한 형벌 이유는 다음과 같습니다: **(a)** 무식한 회귀 방법은 정답지가 3개 통 이상 무리지어 클래스를 가지는 질적 반응 변수를 절대로 평화롭게 단일 선체로 수용할 수 구태 없습니다. **(b)** 멍청한 회귀 방법은 운 좋게 클래스가 단 두 개라고 하더라도 확률 척도 상식을 파괴해버리므로, 정당한 $\text{Pr}(Y | X)$ 확률 수치의 추정치를 아무리 해도 단연 의미 있게 도출해 내지 못합니다. 따라서, 숫자 놀음이 아니라 질적인 응답 분류 변수에 진정으로 단단 부합하는 전용 분류 방법론을 따로 갖추어 적용하는 것이 훨씬 현명하고 바람직합니다. 다음 섹션에서는! 드디어 지루한 선긋기를 박살내고, 예스(Yes)/노(No)로 극명 나뉘는 양적 이분법 단면 반응에 치명적으로 찰떡같이 잘 맞는 무적의 **로지스틱 회귀(Logistic Regression)** 마법을 제시하며, 이어지는 후속 섹션 뒷배경들에서는 단연 질적 응답 변수가 복수 이상 세 개 네 개의 수많은 파벌 클래스를 잔뜩 가질 돌발상황 때 무섭게 적합한 진짜 마법 분류 방법론 모델들을 전격 덮어 심도 커버할 것입니다.

This is the document for this topic.
이 파트는 이 단막 주제를 위해 기술 적재된 요약 문서입니다.

---

## Sub-Chapters

[< 4.1 An Overview Of Classification](../4_1_an_overview_of_classification/trans2.html) | [4.3 Logistic Regression >](../4_3_logistic_regression/trans2.html)

---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 원문을 나란히 읽고 싶으시다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3. Linear Regression](../trans2.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/trans2.html)

# 3.1 Simple Linear Regression
# 3.1 단순 선형 회귀 (단일 재료(X)로 매상(Y) 예측하기)

_Simple linear regression_ lives up to its name: it is a very straightforward approach for predicting a quantitative response $Y$ on the basis of a single predictor variable $X$. It assumes that there is approximately a linear relationship between $X$ and $Y$. Mathematically, we can write this linear relationship as
머신러닝과 통계적 학습의 세계에서 가장 처음 꺼내 드는 기본 무기인 _단순 선형 회귀(Simple linear regression)_는 그 담백한 이름값을 톡톡히 해냅니다. 왜냐하면 오직 **단 1개의 힌트(원인 변수 $X$)**만 쥐고서 수치로 된 **결과(응답 $Y$)**를 때려 맞춰보는 아주 직관적이고 1차원적인 훈련법이기 때문입니다. 이 기법은 세상만사가 $X$ 와 $Y$ 사이에 대충 자를 댄 듯한 정직한 비례(선형) 관계를 이룬다고 순진하게 믿고 시작합니다. 배운 사람답게 이것을 수학 공식으로 세련되게 풀면 다음과 같이 일직선의 방정식으로 적힙니다.

$$
Y \approx \beta_0 + \beta_1 X \quad (3.1)
$$

You might read "$\approx$" as _"is approximately modeled as"_. We will sometimes describe (3.1) by saying that we are _regressing $Y$ on $X$_ (or _$Y$ onto $X$_).
공식 중간에 낀 구불구불한 물결 기호 "$\approx$" 는 _"~ 모양으로 대충 얼버무려 근사 모델링된다"_ 라는 뉘앙스로 읽어주시면 됩니다. 또한 통계학자들의 허세 가득한 은어로는 식 (3.1) 이 하는 짓을 가리켜 _'$Y$ 변수를 $X$ 변수 위로 엎어버려 회귀시킨다(regressing $Y$ on $X$)'_ 라고 멋들여지게 부르기도 합니다.

For example, $X$ may represent `TV` advertising and $Y$ may represent `sales`. Then we can regress `sales` onto `TV` by fitting the model
쉬운 예시를 들어보죠. 우리가 사장님이라 치고, 힌트 변수 $X$ 가 '올해 들이부은 `TV` 광고비'를 뜻하고 결과물 $Y$ 가 '이번 달 팔려나간 매상 `sales`'를 가리킨다고 가정해봅시다. 그렇다면 우리는 다음과 같은 모델 공식을 끼워 맞추어 보면서 `sales(매출)`가 `TV(광고)` 덕분에 어떻게 오르내리는지(회귀하는지) 패턴을 그려볼 수 있게 됩니다.

$$
\text{sales} \approx \beta_0 + \beta_1 \times \text{TV} \quad (3.2)
$$

In Equation 3.1, $\beta_0$ and $\beta_1$ are two unknown constants that represent the _intercept_ and _slope_ terms in the linear model. Together, $\beta_0$ and $\beta_1$ are known as the model _coefficients_ or _parameters_. Once we have used our training data to produce estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ for the model coefficients, we can predict future sales on the basis of a particular value of TV advertising by computing
위 방정식들(3.1, 3.2) 안에서 알짱거리는 $\beta_0$ 와 $\beta_1$ 이란 녀석들은, 우리가 감히 죽었다 깨어나도 완벽히 알 길이 없는 우주의 진리 숫자들입니다. 하나(_절편_)는 티비 광고가 0원일 때도 팔리는 기본 바닥 매출 수치를 나타태고, 다른 하나(_기울기_)는 돈을 태울 때마다 매출이 치솟는 각도를 나타내죠. 이 두 녀석을 묶어서 멋진 말로 모델 무기의 _계수(coefficients)_ 또는 _파라미터(parameters)_ 라고 칭합니다. 만약 우리가 과거의 장부 기록(훈련 데이터)을 요리조리 분석해서 저 신의 숫자들과 얼추 비슷할 것 같은 가짜 인간용 추정치인 $\hat{\beta}_0$ 여분의 타진 값과 $\hat{\beta}_1$를 기어이 구출해 냈다고 칩시다. 그렇다면 우리는 이 숫자를 공식에 박아 넣어 향후 회장님이 "TV에 이만큼 돈 쓸 건데 매출 얼마 나올까?" 물어보실 때 다음과 같은 계산을 돌려 바로 대답할 수 있게 됩니다.

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x \quad (3.3)
$$

where $\hat{y}$ indicates a prediction of $Y$ on the basis of $X = x$. Here we use a _hat_ symbol, $\hat{ }$, to denote the estimated value for an unknown parameter or coefficient, or to denote the predicted value of the response.
여기 수식 3.3 통에 나온 $\hat{y}$ 은 당신이 $X$ 값에 임의의 원인 $x$를 쑤셔 넣었을 때 툭 튀어나오리라 기대되는 $Y$ 의 **가짜 예측치 점수**를 상징합니다. 통계 동네의 국룰 암호가 하나 있는데요, 어떤 무서운 수학 기호 위에 꼬깔모자 모양의 _햇(hat)_ 기호, 즉 $\hat{ }$ 모양이 씌워져 있다면 쫄지 마세요. 이건 "신의 계시로 얻은 진짜 절대 진리 값이 아니라, 우리가 불완전한 점들을 모아 나름대로 최대한 기를 써서 **어림잡아 예측해 본 가짜 추정치 기록물**입니다!" 라고 자백 표시를 남겨두는 귀여운 표식 기호일 뿐이니까요.

---

## Sub-Chapters (하위 목차)

### 3.1.1 Estimating the Coefficients (계수 추정)
* [📖 쉬운 해설판으로 이동하기](./3_1_1_estimating_the_coefficients/trans2.html)

장부에 적힌 200개의 진짜 데이터를 보고, 가장 오차가 적은 최적의 붕어빵 예측 선을 긋기 위해 $\beta_0$와 $\beta_1$ 값을 추측해 내는 '최소 제곱법'이라는 마법 파훼법을 배웁니다.

### 3.1.2 Assessing the Accuracy of the Coefficient Estimates (계수 추정치의 정확도 평가)
* [📖 쉬운 해설판으로 이동하기](./3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html)

우리가 열심히 선을 긋긴 그었는데, 이 가짜 선이 진짜 우주의 법칙과 얼마나 일치하거나 오차가 날지(표준 오차, 신뢰 구간) 평가해 보고 확률 법정에서 승소해 봅니다.

### 3.1.3 Assessing the Accuracy of the Model (모델의 정확도 평가)
* [📖 쉬운 해설판으로 이동하기](./3_1_3_assessing_the_accuracy_of_the_model/trans2.html)

그래서 최종적으로 우리 식당의 임시 매상 예측기가 만약에 성적표를 받는다면? $R^2$(설명력 점수)라는 잔인한 채점표를 통해 우리 모델의 우수성을 채점해 봅니다.

[< 3. Linear Regression](../trans2.html) | [3.1.1 Estimating the Coefficients >](./3_1_1_estimating_the_coefficients/trans2.html)

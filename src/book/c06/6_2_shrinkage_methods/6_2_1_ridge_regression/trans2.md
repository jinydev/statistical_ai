---
layout: default
title: "trans2"
---

# 6.2.1 Ridge Regression 
# 6.2.1 릿지 회귀 (Ridge Regression)

Recall from Chapter 3 that the least squares fitting procedure estimates $\beta_0, \beta_1, \ldots, \beta_p$ using the values that minimize
제 3장에서 지겹게 봤던 기본 일반 '최소 오차 제곱법'을 먼저 떠올려 봅시다. 기존 방식은 오차를 뜻하는 아래 수식 결괏값($\text{RSS}$)을 최대한 영혼까지 쥐어짜서 작아지게 만드는 파라미터 $\beta_0, \beta_1, \ldots, \beta_p$ 들을 찾아 예측 모델에 적합했습니다.

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 = \text{RSS}
$$

_Ridge regression_ is very similar to least squares, except that the coefficients are estimated by minimizing a slightly different quantity. In particular, the ridge regression coefficient estimates $\hat{\beta}^R$ are the values that minimize
**'릿지 회귀 (Ridge regression)'** 도 이것과 소름 돋게 똑같습니다. 단지 목적지인 '최소화시킬 수식' 꼬리에 독특한 옵션을 작게 하나 추가했다는 점만 빼면 말입니다. 릿지 시스템이 궁극적으로 타겟 에이스 계수 추정치 $\hat{\beta}^R$ 를 찾아내는 공식 구조는 다음과 같습니다. 

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \sum_{j=1}^p \beta_j^2 \quad (6.5)
$$

where $\lambda \ge 0$ is a _tuning parameter_ , to be determined separately. Equation 6.5 trades off two different criteria. As with least squares, ridge regression seeks coefficient estimates that fit the data well, by making the RSS small. However, the second term, $\lambda \sum_j \beta_j^2$, called a _shrinkage penalty_, is small when $\beta_1, \ldots, \beta_p$ are close to zero, and so it has the effect of _shrinking_ the estimates of $\beta_j$ towards zero. The tuning parameter $\lambda$ serves to control the relative impact of these two terms on the regression coefficient estimates. When $\lambda = 0$, the penalty term has no effect, and ridge regression will produce the least squares estimates. However, as $\lambda \to \infty$, the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. Unlike least squares, which generates only one set of coefficient estimates, ridge regression will produce a different set of coefficient estimates, $\hat{\beta}_{\lambda}^R$, for each value of $\lambda$. Selecting a good value for $\lambda$ is critical; we defer this discussion to Section 6.2.3, where we use cross-validation. 
주목해야 할 것은 수식 맨 뒤에 붙은 $\lambda \ge 0$ 이라는 **'조율 파라미터(tuning parameter)'** 와, 그 뒤를 따르는 $\lambda \sum_j \beta_j^2$ 이라는 엄청난 **'수축 페널티(shrinkage penalty)'** 조항입니다.
1. 기존 수식 앞부분($\text{RSS}$)은 이전처럼 "네 눈앞의 훈련 데이터 오차를 최대한 줄여!" 라고 모델을 혹사시킵니다.
2. 하지만 추가된 수축 페널티 수식은 이렇게 응수합니다. "오차만 무식하게 깎겠다고, 쓸데없는 개별 변수들의 파라미터 $\beta_j$ 값을 불필요하게 뚱뚱하게 키우고 있다면 벌점을 때리겠다! 모델이 $\beta_j$ 파라미터 계수들을 모조리 0 쪽으로 납작하게 수축시켜야만 페널티 점수를 깎아주겠다!" 라고 압박을 넣습니다.

이 둘의 싸움을 영리하게 중재하는 심판 역할이 바로 파라미터 **$\lambda$** 입니다. 
만약 심판 $\lambda = 0$ 이라면 징계 페널티는 완전히 무력화되어 기존 클래식한 최소 오차 제곱법과 똑같은 파라미터 성적이 나옵니다. 
반대로 $\lambda \to \infty$ 로 압박 범위를 무제한 키운다면 무자비한 징벌 페널티의 파워가 극대화되어 모델은 잔뜩 쫄게 되고 결론적으로 모델 계수 추정치들은 완전히 0으로 수축 소멸하게 될 것입니다.
기존 공식은 오직 단 하나의 절대 정답 세트 파라미터만을 뽑아냈지만, 릿지는 $\lambda$ 크기 조절 다이얼을 휠 돌리듯 바꿀 때마다 완전히 스펙이 상이한 무한한 버전업 계수 세트($\hat{\beta}_{\lambda}^R$)들을 끝없이 양산해냅니다. 그렇기 때문에 이 강력한 볼륨 다이얼 $\lambda$ 를 어느 영역에 맞추는지가 핵심인데, 이건 뒤의 6.2.3절의 교차 검증을 통해 파헤치겠습니다.

![Figure 6.4](./img/6_4.png)

**FIGURE 6.4.** _The standardized ridge regression coefficients are displayed for the_ `Credit` _data set, as a function of $\lambda$ and $\|\hat{\beta}_{\lambda}^R\|_2 / \|\hat{\beta}\|_2$._ 
**그림 6.4.** `Credit` *데이터에 대한 표준화된 릿지 회귀 계수들이 $\lambda$ 와 수축 비율에 따라 어떻게 감소하는지를 나타냅니다.*

Note that in (6.5), the shrinkage penalty is applied to $\beta_1, \ldots, \beta_p$, but not to the intercept $\beta_0$. We want to shrink the estimated association of each variable with the response; however, we do not want to shrink the intercept, which is simply a measure of the mean value of the response when $x_{i1} = x_{i2} = \ldots = x_{ip} = 0$. If we assume that the variables—that is, the columns of the data matrix $\mathbf{X}$—have been centered to have mean zero before ridge regression is performed, then the estimated intercept will take the form $\hat{\beta}_0 = \bar{y} = \sum_{i=1}^n y_i / n$. 
공식을 매의 눈으로 살펴보면 무자비한 수축 징계 페널티는 철저히 예측 변수 $\beta_1, \ldots, \beta_p$ 에게만 떨어지며, y 절편 항목인 $\beta_0$ 형님에게는 전혀 타격을 입히지 않습니다. 예측 변수들과 결과의 괴상한 연관성을 깎아내고 싶을 뿐, "모든 $\text{X}$ 변수값이 싹 0일 때 y의 순수 기본 평균 시작점이 어디냐?" 를 나타내는 무해한 절편 값까지 찌그러뜨릴 이유는 전혀 없기 때문입니다.

---

## Sub-Chapters (하위 목차)

### An Application to the Credit Data (신용 데이터 적용 사례)
* [문서로 이동하기](./6_2_1_1_an_application_to_the_credit_data/)

은행 신용도 데이터셋에 릿지 함수를 튜닝했을 때 변수들의 계수값이 조율 파라미터 $\lambda$의 상승에 따라 어떻게 부드럽게 감쇠하는지 등고 플롯으로 확인합니다.

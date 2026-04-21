---
layout: default
title: "trans1"
---

# 6.2.1 Ridge Regression 
# 6.2.1 릿지 회귀 (Ridge Regression)

Recall from Chapter 3 that the least squares fitting procedure estimates $\beta_0, \beta_1, \ldots, \beta_p$ using the values that minimize
제 3장에서 최소 제곱 적합 절차는 다음 값을 최소화하는 수치를 사용하여 파라미터 $\beta_0, \beta_1, \ldots, \beta_p$ 를 추정한다는 점을 다시 상기해 봅시다.

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 = \text{RSS}
$$

_Ridge regression_ is very similar to least squares, except that the coefficients are estimated by minimizing a slightly different quantity. In particular, the ridge regression coefficient estimates $\hat{\beta}^R$ are the values that minimize
**'릿지 회귀 (Ridge regression)'** 는 약간 다른 양을 수리로 최소화하여 측정 계수를 산출 추정한다는 점을 제외하면, 전통 최소 오차 제곱법과 무척 유사합니다. 특히 단연, 릿지 회귀 계수 예측 추정치 $\hat{\beta}^R$ 는 다음 수식을 산술 최소화하는 값입니다.

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \sum_{j=1}^p \beta_j^2 \quad (6.5)
$$

where $\lambda \ge 0$ is a _tuning parameter_ , to be determined separately. Equation 6.5 trades off two different criteria. As with least squares, ridge regression seeks coefficient estimates that fit the data well, by making the RSS small. However, the second term, $\lambda \sum_j \beta_j^2$, called a _shrinkage penalty_, is small when $\beta_1, \ldots, \beta_p$ are close to zero, and so it has the effect of _shrinking_ the estimates of $\beta_j$ towards zero. The tuning parameter $\lambda$ serves to control the relative impact of these two terms on the regression coefficient estimates. When $\lambda = 0$, the penalty term has no effect, and ridge regression will produce the least squares estimates. However, as $\lambda \to \infty$, the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. Unlike least squares, which generates only one set of coefficient estimates, ridge regression will produce a different set of coefficient estimates, $\hat{\beta}_{\lambda}^R$, for each value of $\lambda$. Selecting a good value for $\lambda$ is critical; we defer this discussion to Section 6.2.3, where we use cross-validation. 
여기 서술된 $\lambda \ge 0$ 은 차후 별도 독립적으로 산출 결정되는 **'조율 파라미터(tuning parameter)'** 입니다. 수식 (6.5)는 두 가지의 상이한 기준에 대해 서로 물리적 트레이드오프(trade-off, 절충) 연산을 수행합니다. 최소 오차 제곱 기법과 완전 동일하게, 릿지 회귀 기법 역시 일선 $\text{RSS}$ 통계량을 적게 감소시킴으로써 훈련 데이터를 잘 적합하는 우수 계수 추정치를 찾습니다. 그러나 **'수축 페널티(shrinkage penalty)'** 로 호칭 불리는, 후방 두 번째 수식 계산 항 $\lambda \sum_j \beta_j^2$ 부분은 파라미터 $\beta_1, \ldots, \beta_p$ 들의 값이 0에 근접할 때 아주 값이 작아지며, 그렇기 때문에 해당 통제 기전은 타겟 $\beta_j$ 계수 추정치 측정값을 강제로 0으로 향하도록 **'수축(shrinking)'** 제재시키는 직접 효과를 가집니다. 통제 조율 파라미터 $\lambda$ 단위는 도출 회귀 계수 측정 추정치에 영향 가해지는 이 두 가지 개별 계산 항의 상대적 영향력 마진을 제어 통제하는 강력 파워 역할을 전담합니다. 만약 조건 $\lambda = 0$ 이라면, 페널티 항은 수식 아무런 기능적 효과 파급도 가지지 않으며 이 때 릿지 회귀 공식은 순정 원조 우수 최소 오차 제곱 추정치를 낳습니다. 반면에 만약 $\lambda \to \infty$ 쪽으로 무한 발산 전개하게 되면, 제재 페널티 파급 효과가 계속 점진 증가하게 되고, 최종 도출되는 릿지 회귀 파라미터 계수 추정치 결과는 거의 완전 0에 한없이 근접하게 될 것입니다. 단일 일괄 한 세트의 동일 고정 계수 추정치만 생성 발급하는 기존 일반 단순 최소 오차 제곱법 구조와는 명백히 다르게, 릿지 평가 회귀 공식은 무작위 각 $\lambda$ 값 크기에 전적으로 비례 대응하여 완전히 각자 체제 모양이 다른 이질 세트의 추가 파라미터 계수 예측 추정치 모형 $\hat{\beta}_{\lambda}^R$ 를 끝없이 계속 생성 발현 양산할 것입니다. 그러므로 최적 알맞은 탁월 $\lambda$ 계수 단위 값을 정밀 선택 판단하는 과정은 모델 시스템에 아주 치명적이고 막 대 중요한 과제입니다; 우리는 해당 자세한 전개 논의를 우리가 실제 모델 교차 검증을 주로 다루게 될 6.2.3절로 훗날 미룹니다.

![Figure 6.4](./img/6_4.png)

**FIGURE 6.4.** _The standardized ridge regression coefficients are displayed for the_ `Credit` _data set, as a function of $\lambda$ and $\|\hat{\beta}_{\lambda}^R\|_2 / \|\hat{\beta}\|_2$._ 
**그림 6.4.** `Credit` *데이터 세트 환경에 대한 각 정규화된 릿지 회귀 분석 계수 값들의 전개 분포가, $\lambda$ 값 변화 추이 및 대응 $\|\hat{\beta}_{\lambda}^R\|_2 / \|\hat{\beta}\|_2$ 계산 수치 함수 변화에 대응되어 시각 표시 도출됩니다.*

Note that in (6.5), the shrinkage penalty is applied to $\beta_1, \ldots, \beta_p$, but not to the intercept $\beta_0$. We want to shrink the estimated association of each variable with the response; however, we do not want to shrink the intercept, which is simply a measure of the mean value of the response when $x_{i1} = x_{i2} = \ldots = x_{ip} = 0$. If we assume that the variables—that is, the columns of the data matrix $\mathbf{X}$—have been centered to have mean zero before ridge regression is performed, then the estimated intercept will take the form $\hat{\beta}_0 = \bar{y} = \sum_{i=1}^n y_i / n$. 
해석상 공식 판단 (6.5)에서 주목할 부분은 단연, 수축 페널티 요소가 타겟 변수 예측 계수 $\beta_1, \ldots, \beta_p$ 들에게는 철저 강제 적용되지만 타겟 기준 절편인 $\beta_0$ 항목에는 절대 영향을 주거나 부여 적용되지 않는다는 엄연한 사실입니다. 분석상 우리는 타겟 반응 변동에 미치는 도출 각 변수 요소와의 모델 추정 측정 연관성을 일괄 제어 수축 감소시키고자 시도 의도합니다; 그렇지만, 예측치 $x_{i1} = x_{i2} = \ldots = x_{ip} = 0$ 환경 상황일 당시에 타겟 반응값 결과 요소의 단 순 단순 평균치 편차를 단지 나타내 수치로 측정 의미 지표하는 것에 불과한 기준 절편 값까지 축소 수축시키기를 원하지는 절대 않습니다. 만약 특정 변수 항목들 ⏤ 즉 명백히 말해 전체 데이터 인자 세트 행렬 $\mathbf{X}$ 의 개별 해당 수직 열 기둥들 ⏤ 이 릿지 회귀 연산을 사전 가동 전개 실현하기 직전에, 먼저 평균 기준 0 구성을 갖도록 수리 조정 집중 센터링 연산 변환되었다고 가정하면, 그렇게 확보 도출된 예측 타겟 절편 항목은 일관적으로 항상 고정 기조 공식 수식 $\hat{\beta}_0 = \bar{y} = \sum_{i=1}^n y_i / n$ 체제 형태를 고정 유지 취하게 될 것입니다.

---

## Sub-Chapters (하위 목차)

### An Application to the Credit Data (신용 데이터 적용 사례)
* [문서로 이동하기](./6_2_1_1_an_application_to_the_credit_data/)

은행 신용도 데이터셋에 릿지 함수를 튜닝했을 때 변수들의 계수값이 조율 파라미터 $\lambda$의 상승에 따라 어떻게 부드럽게 감쇠하는지 등고 플롯으로 확인합니다.

---
layout: default
title: "trans1"
---

# 6.3 차원 축소 기법 (Dimension Reduction Methods)

The methods that we have discussed so far in this chapter have controlled variance in two different ways, either by using a subset of the original variables, or by shrinking their coefficients toward zero. All of these methods are defined using the original predictors, $X_1, X_2, \ldots, X_p$. We now explore a class of approaches that _transform_ the predictors and then fit a least squares model using the transformed variables. We will refer to these techniques as _dimension reduction_ methods. 
우리가 이 6장 단원의 서술에서 지금까지 고찰 논의해 온 기법 통계 규제 장치들은 전부 본래 도입되는 오리지널 원본 예측 변수들의 부분집합을 새롭게 발췌하여 사용하거나, 혹은 그 변수들에 할당된 파라미터 계수들을 0 방향 측면으로 의도적 하향 수축시키는 방식 중 하나를 택하여 모델에 내재된 잠재 변동성(variance) 오차 확률을 제어 조율해 냈습니다. 결국 이들 기법 수단들은 모두 그 근간에서 $X_1, X_2, \ldots, X_p$ 형태인 애초의 오리지널 부대 예측 통제 변수 요소들을 그대로 가져와 정의 활용하는 구조입니다. 이와는 판이하게 이제 우리는 아예 초기 예측 변수 군단 자체를 완전히 변형 기형(transform) 환원시킨 다음, 그 새롭게 탈바꿈 변환된 파생 변수들을 대상으로 최소 제곱 오차 적합 최소 모델을 재설계 시도하는 새로운 부류의 접근법을 전격 탐구 시도 탐색해 보겠습니다. 우리는 이후 이러한 변형 전환 테크닉 무리들을 총칭하여 모두 **차원 축소 기법(dimension reduction methods)** 이라 명명 지칭 부르겠습니다.

Let $Z_1, Z_2, \ldots, Z_M$ represent $M < p$ linear combinations of our original $p$ predictors. That is, 
여기서 새 변수집단 $Z_1, Z_2, \ldots, Z_M$ 요소들이 본래 우리가 지녔던 원본 변수 $p$ 개를 가지고 새롭게 버무려 엮은 짬뽕 선형 결합(linear combinations) 산출 비율 도출 결과물의 총칭을 대표 상징하며 이때 $M < p$ 라고 조건을 가정합시다. 다시 수식으로 풀어 정리한다면 다음과 같습니다.

$$
Z_m = \sum_{j=1}^p \phi_{jm} X_j \quad (6.16)
$$

for some constants $\phi_{1m}, \phi_{2m}, \ldots, \phi_{pm}, m = 1, \ldots, M$. We can then fit the linear regression model 
여기서 $\phi_{1m}, \phi_{2m}, \ldots, \phi_{pm}$ 상수는 일종의 변수 변환 상수들이고 차원 지표는 $m = 1, \ldots, M$ 입니다. 이제 우리는 다음과 같은 선형 회귀 모형을 이 새로운 변수에 기반해 모델링하여 최소 제곱법으로 새롭게 적합(fit)시킬 수 있게 됩니다.

$$
y_i = \theta_0 + \sum_{m=1}^M \theta_m z_{im} + \epsilon_i \quad (6.17)
$$

using least squares. Note that in (6.17), the regression coefficients are given by $\theta_0, \theta_1, \ldots, \theta_M$. If the constants $\phi_{1m}, \phi_{2m}, \ldots, \phi_{pm}$ are chosen wisely, then such dimension reduction approaches can often outperform least squares regression. In other words, fitting (6.17) using least squares can lead to better results than fitting (6.1) using least squares. 
위 공식 (6.17) 수식에서 파라미터 회귀 계수의 배정 형태는 기존 $\beta$가 아닌 새로운 기호인 $\theta_0, \theta_1, \ldots, \theta_M$ 로 온전히 탈바꿈 교체 주어졌음에 반드시 유의하십시오. 만약 최초의 변환 상수였던 $\phi_{1m}, \phi_{2m}, \ldots, \phi_{pm}$ 의 수량 지표들을 우리가 애초에 아주 치밀 영리하고 훌륭하게 모색 선택 결정 발굴해 냈다면, 이런 선형 결합 기반 차원 축소법은 애당초 구식 원본 변수를 그대로 가지고 돌린 일반 최소 제곱 체계의 성능을 거뜬히 능가 압도해 추월(outperform)할 공산이 큽니다. 달리 표현하자면, 단조 구식인 애초의 기존 (6.1) 수식을 가지고 최소 오차 제곱을 구동 적발하는 것보다 본 단원의 변형 축약 공식 (6.17)을 바탕으로 최소 0의 오차 제곱합을 모색 타결하는 편이 훨씬 유의미한 성과 결과를 속출 파생 초래(lead to) 도달 유발시킬 수 있다는 뜻입니다.

The term _dimension reduction_ comes from the fact that this approach reduces the problem of estimating the $p+1$ coefficients $\beta_0, \beta_1, \ldots, \beta_p$ to the simpler problem of estimating the $M+1$ coefficients $\theta_0, \theta_1, \ldots, \theta_M$, where $M < p$. In other words, the dimension of the problem has been reduced from $p+1$ to $M+1$.
**차원 축소(dimension reduction)** 라는 용어 명칭 자체는 이 참신한 기법 체제가 태생적으로 무려 총 개수가 $p+1$ 에 달하는 방대한 파라미터 계수 무리 $\beta_0, \beta_1, \ldots, \beta_p$ 들을 구출 발굴 조사해야 하는 당면 과업 단계를, 고작 $M+1$ ($M < p$) 규모 크기에 불과한 고갈 축소 인자 계수 집단 $\theta_0, \theta_1, \ldots, \theta_M$ 만을 구출 추산해 내면 되는 매우 단순 심플한 단계 문제로 획기적 감축 축소 삭감 절감 완화(reduces) 시켜버린다는 특유의 고유 사실 팩트에서 온전히 초래 기인(comes from) 파생 차용 비롯되었습니다. 이를 좀 더 쉽게 다른 단어로 대변 재해석 포장하자면, 당면한 문제가 처한 그 본연의 체적 덩치 차원(dimension) 스케일 크기가 $p+1$ 단위에서 극소 규모인 $M+1$ 차원 수준으로 수축 소형화 경감 압축 절감 타격 차감 소멸 단축 경감 축약 등급 하향 감축 삭감 감가 도출 강하 절단(reduced) 단절 되었다는 이치를 함축 대변합니다.

![Figure 6.14](./img/6_14.png)

**FIGURE 6.14.** _The population size (_ `pop` _) and ad spending (_ `ad` _) for_ 100 _different cities are shown as purple circles. The green solid line indicates the first principal component, and the blue dashed line indicates the second principal component._
**그림 6.14.** _각 100 곳의 상이한 다른 도시들의 인구 수치 모수 규모(_ `pop` _)와 광고비 지출 사용 금액 지표(_ `ad` _)가 보라색 원 기호로 도식 표시 노출 전시 작도 되어 있습니다. 그중 초록색 실선은 첫 번째 제 1의 근원 주성분(principal component) 지표 축을 가리켜 명시하며, 반면 축 파란색 허물 점선 기호는 두 번째 차순위 근원인 제 2의 주성분을 나타냅니다._

Notice that from (6.16), 
여기서 한 번 유의 깊게 수식 (6.16)으로부터 다음 공식을 살펴 주목해 보십시오.

$$
\sum_{m=1}^M \theta_m z_{im} = \sum_{m=1}^M \theta_m \sum_{j=1}^p \phi_{jm} x_{ij} = \sum_{j=1}^p \sum_{m=1}^M \theta_m \phi_{jm} x_{ij} = \sum_{j=1}^p \beta_j x_{ij} \quad (6.18)
$$

where 
여기서 치환된 등가 성분은 아래 규칙을 준수합니다.

$$
\beta_j = \sum_{m=1}^M \theta_m \phi_{jm}
$$

Hence (6.17) can be thought of as a special case of the original linear regression model given by (6.1). Dimension reduction serves to constrain the estimated $\beta_j$ coefficients, since now they must take the form (6.18). This constraint on the form of the coefficients has the potential to bias the coefficient estimates. However, in situations where $p$ is large relative to $n$, selecting a value of $M \ll p$ can significantly reduce the variance of the fitted coefficients. If $M = p$, and all the $Z_m$ are linearly independent, then (6.18) poses no constraints. In this case, no dimension reduction occurs, and so fitting (6.17) is equivalent to performing least squares on the original $p$ predictors. 
그러므로 우리는 논리적으로 모형 공식 (6.17) 체계가 사실 최초의 식 (6.1)로 주어졌던 고안 원본 오리지널 선형 회귀 분석 모형의 일련의 단절 특수한 국면 세부 사례 모형 판본의 일종이라고 간주 사료 간주 유추 해석 구상 상정 규명 판단(thought of) 할 수 있습니다. 차원 축소는 우리가 도출한 $\beta_j$ 파라미터 계수 군단을 아주 강력하게 제약 통제 구속 속박 결박 제한(constrain) 묶어두는 족쇄 역할을 자처 단행 수행 제공(serves to) 합니다. 왜냐하면 계수들은 이제 막 벗어날 수 없이 억지로 수식 (6.18)의 일방 형태 궤도 포맷을 숙명으로 취하 수용 거부 없이 이수 감수 취해야(must take the form) 하기 때문입니다. 이토록 파라미터 계수 성분 뼈대 외관 형태를 억지로 가둬 제약(constraint) 시켜버린 한계 규율 장치는 결국 도출되는 계수 산출 추정치에 심한 어긋남 편향(bias) 파장을 초래 발발 가할 잠재 불씨 위험성(potential) 여지를 필연 안고 자초 유발합니다. 그렇지만 대외 환경 요건인 투입 $p$ 무리가 관측 객체 $n$ 인자에 비견하여 너무 심각 비대 방대 방대 큰 국면의 열악 위기 상황이라면, 이 때 오히려 단호히 $M \ll p$ 스케일 규모 지표를 강력 낙점 지목 선택(selecting) 제안 취하 결단 도입 감행 단행 채택 취합 함으로써 구동 발현 모의 적합 완료 상태 계수 파라미터 모델이 지닐 파생 변수 오차 요인 변동성(variance) 폐해 수치를 실로 전격 탁월 막대 심대 유의미 전격 단호 급격 눈부 비약 탁월 파 격 엄청 거대 지대 혁신 극명 확연 뚜렷 기 하 확 기 월 등 제 확 거 혁 눈 눈 막 엄청 강 렬 놀 랄 감 대 폭 삭 감 감 제 경 감 차 제 제 감 저 적 급 감 대 비 (significantly reduce) 유 도 시 격 할 조 진 수 규 제 점 도 있 며 줄 규 과. 가 위 기 입 정 자 만 위 만 여 역 이 $M = p$ 일 이 조 성 치 현 통 성 조 립 되 환 위 단 전 규 어, 모 일 든 진 파 일 조 일 전 환 규 환 지 규 조 $Z_m$ 성 선 선 지 전 결 차 점 환 일 지 확 환 확 독립 적 자 다 환 (linearly independent) 이 결 파 시 현 라 진 발 라 라 라 자 은 모 (poses no constraints) 전 위 위 모 자 합 위 부 은 진 합 전 강 부 합 합 형 지 점 다. 구 합 위 합 다 며 제 구 점 규. 은 자 모 다 동 모 다 단 지. 이 어 치. 일 합 진 어 통 전 어 지 자 부 합 동. 다. 즉 무 동 위 라 자, 구 현 과 진 도 과 론 은 수 형 부 지, 공 현 치 결 일 과 론 정 규 지 시 환 차 부 일 부 시 이 부 $\beta_j$ 부 시 $p$ 과 정 과 단 동 과 정 일 전 동 동 정. 위 공 과 과 다 발 과 자 결 (equivalent). 통 도.

All dimension reduction methods work in two steps. First, the transformed predictors $Z_1, Z_2, \ldots, Z_M$ are obtained. Second, the model is fit using these $M$ predictors. However, the choice of $Z_1, Z_2, \ldots, Z_M$, or equivalently, the selection of the $\phi_{jm}$'s, can be achieved in different ways. In this chapter, we will consider two approaches for this task: _principal components_ and _partial least squares_ . 
모든 차원 축소 접근 수법 기제들은 본디 두 갈래 절차 동력에 거쳐 실질 작동 기조 구동 전개 이룩 구동 발현 합(work in two steps) 니다. 우선 초입 단계로 처음부터, 새롭게 재무장 변형 조합된 $Z_1, Z_2, \ldots, Z_M$ 투입 예측 변수들을 확보 파생 쟁취 수득 마련 조달 포착 획득 수확(obtained) 해냅니다. 그런 이후 최종 2막 과정에서 이 방금 얻어낸 신규 정예 요원 $M$ 종의 가공 변수들을 기판에 삼아 모델 구동 평가 회귀 분석 적합을 시산(fit) 수행 거행 단행 합니다. 단 여기서 쟁점은 어떤 요인 지표 $Z_1, Z_2, \ldots, Z_M$ 묶음을 주연으로 택할 것인가 여부의 발굴 채택 지목 방식, 다르게 말해 조합 승수 상수인 $\phi_{jm}$ 집합들을 규명 고안 선택 타결 채택 확정 섭렵 수립 단행 구축 확정 결단(selection) 하는 방식과 길목이 여러 다향 다채 상이한 부류 이질 가변 경로 길목 다각 궤도 차원 갈래 갈래 갈래 갈 래 노 선 루트 채 널 갈 래 로 위 각 자 성 치 부 과 파 규 류 도 파 전 어 전 자 도 전 어 결 구 이 실 결 (achieved in different ways) 성 취 이 구 정 실 귀 발 가 모 능 동 가 됩 능 발 합 가 발 진 진 진. 당 장 이 도 작 자 과 동 보 장 절 진 위 파 동 기. 가 발 발 가 보 점 일 과 (principal components) 차 화 가 화 주 합 (partial least squares) 방 점 파 발 보.
 
---

## Sub-Chapters (하위 목차)

### 6.3.1 Principal Components Regression (주성분 중심 회귀 기법)
* [문서로 이동하기](./6_3_1_principal_components_regression/)

원래의 변수 행렬들이 지닌 정보량(Variance)을 가장 거대하게 포괄하는 주성분 벡터(Principal Component) 방향을 찾아 그것만을 선형 모델 인스턴스 X 요인으로 사용합니다.

### 6.3.2 Partial Least Squares (부분 최소 제곱법, PLS)
* [문서로 이동하기](./6_3_2_partial_least_squares/)

X 행렬 내의 독립적 변동성만 보는 PCA를 보완해, 처음 차원 추출부터 반응 변수 Y 그룹과의 상관성이 높은 쪽 방향으로만 유도하는 지도(Supervised) 기반의 차원 축소법입니다.

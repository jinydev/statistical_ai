---
layout: default
title: "trans1"
---

# A Simple Special Case for Ridge Regression and the Lasso 
# 릿지 회귀와 라쏘에 대한 단순한 특수 사례 (A Simple Special Case for Ridge Regression and the Lasso)

In order to obtain a better intuition about the behavior of ridge regression and the lasso, consider a simple special case with $n = p$, and **X** a diagonal matrix with 1’s on the diagonal and 0’s in all off-diagonal elements. To simplify the problem further, assume also that we are performing regression without an intercept. With these assumptions, the usual least squares problem simplifies to finding $\beta_1, \ldots, \beta_p$ that minimize 
릿지 회귀와 라쏘의 동작 방식에 대한 직관을 얻기 위해, 관측치와 변수 수가 $n = p$ 로 같고 행렬 **X** 가 대각 원소는 1이며 비대각 원소는 0인 대각 행렬(diagonal matrix)인 단순한 사례를 상정해 봅시다. 문제를 더욱 단순화하기 위해 절편이 없는 회귀 분석을 수행한다고 가정합시다. 이러한 제약 조건하에서 일반적인 최소 제곱 문제는 다음 수식을 최소화하는 계수 $\beta_1, \ldots, \beta_p$ 를 찾는 과정이 됩니다.

$$
\sum_{j=1}^p (y_j - \beta_j)^2 \quad (6.11)
$$

In this case, the least squares solution is given by 
이러한 상황에서, 최소 제곱 해법은 다음과 같습니다.

$$
\hat{\beta}_j = y_j
$$

And in this setting, ridge regression amounts to finding $\beta_1, \ldots, \beta_p$ such that 
그리고 바로 이 세팅 하에서, 릿지 회귀는 다음 값을 만족시키는 계수 궤적 $\beta_1, \ldots, \beta_p$ 를 찾는 과정으로 한결 요약됩니다.

$$
\sum_{j=1}^p (y_j - \beta_j)^2 + \lambda \sum_{j=1}^p \beta_j^2 \quad (6.12)
$$

is minimized, and the lasso amounts to finding the coefficients such that 
수식 (6.12) 를 최소화하는 것입니다. 아울러 라쏘 모델 또한 아래의 공식을 충족하는 통계 계수 지표들을 찾아내는 절차입니다.

$$
\sum_{j=1}^p (y_j - \beta_j)^2 + \lambda \sum_{j=1}^p |\beta_j| \quad (6.13)
$$

![Figure 6.10](./img/6_10.png)

**FIGURE 6.10.** _The ridge regression and lasso coefficient estimates for a simple setting with $n = p$ and_ **X** _a diagonal matrix with 1’s on the diagonal._ Left: _The ridge regression coefficient estimates are shrunken proportionally towards zero, relative to the least squares estimates._ Right: _The lasso coefficient estimates are soft-thresholded towards zero._ 
**그림 6.10.** _차원 $n = p$ 이며_ **X** _가 주대각선 상에만 1 수치를 위치시킨 대각 행렬 이라는 특수 세팅(simple setting) 에서 나타난 릿지 회귀와 라쏘 계수 궤도 결론._ 왼쪽 패널: _릿지 체제의 파라미터 추정 수치가 일반 최적 최소 제곱 궤적 대비 지표에 상대적으로 비례하여(proportionally) 0을 향해 균일한 억제 비율로 감가 삭감 수축(shrunken) 침강 제어 당합니다._ 오른쪽 패널: _반면 특정 모의 라쏘 예측의 지지 통계 계수 추정 결론 추정치들은 영점 0 부분 발판을 조준 표적 향해 특정 단절 한계 억제 기조 조처 방식인 즉 통칭 '상수-수축 한계점화 무작위 삭감 감가 조율 (soft-thresholded)' 단절 특수 규제 제한 제재 조처 방식으로 제압 수축 삭감 감가 화 제단 수 단 제 수 화 조. 

is minimized. One can show that in this setting, the ridge regression estimates take the form 
식 (6.13) 수치가 고 최저 수치로 최소화(minimized) 달성 됩니다. 우리는 이 특수 세팅 환경 하에서, 릿지 모형 계수 예측 산출 결론이 필연적으로 아래 방정식의 기본 형태 궤도를 띄게(take the form) 된다는 사실을 가뿐히 수리 시연 증명(show) 해 보일 수 있습니다.

$$
\hat{\beta}_j^R = \frac{y_j}{1 + \lambda} \quad (6.14)
$$

and the lasso estimates take the form 
그리고 이와 연계된 라쏘 체제의 지수 예측 추정 결과치들 또한 이와 대조적으로 다음과 같은 특수 분할 조건부 방정식 궤적 구조의 형태를 함께 성립 띠게(take the form) 취합니다.

$$
\hat{\beta}_j^L = \begin{cases} 
y_j - \lambda/2 & \text{if } y_j > \lambda/2; \\
y_j + \lambda/2 & \text{if } y_j < -\lambda/2; \\
0 & \text{if } |y_j| \le \lambda/2.
\end{cases} \quad (6.15)
$$

Figure 6.10 displays the situation. We can see that ridge regression and the lasso perform two very different types of shrinkage. In ridge regression, each least squares coefficient estimate is shrunken by the same proportion. In contrast, the lasso shrinks each least squares coefficient towards zero by a constant amount, $\lambda/2$; the least squares coefficients that are less than $\lambda/2$ in absolute value are shrunken entirely to zero. The type of shrinkage performed by the lasso in this simple setting (6.15) is known as _soft-thresholding_. The fact that some lasso coefficients are shrunken entirely to zero explains why the lasso performs feature selection. 
위 그림 6.10 이 논의 묘사된 궤적 지표 상황의 통계 단면 전개를 대변 도해(displays) 합니다. 우리는 이를 통해 무거운 릿지 중심 모형과 예리 라쏘 기제가 사실 개별 독립 아주 이질 상이한(very different) 확고 성질 고유 삭감 양상 수 축 방식(shrinkage) 기제를 명백 단호 거행 기 구 실행 구 사 전 개 거 행 발 현 수(perform) 된 다 위 부 도 일 보 차 구 시 발 동 묘 통 입 통. 일 반 릿 지 기 구 파 체 제 내 전 수. 최 소 수 계 조 각 수 오 발 결 다 정 차 과 배 일 파 미 조 차. 점 결 지 도 고 확 가 기 전 일 발 비율 백 점 비 률 비 (same proportion) 화 기 조 가 지 수 점 정 가 단 위 점 가 지 도 동 동 률 규 율 시 수 규 점 전 진 압 통 자 조 전 시 통 자 시 규 위 점 통 전 (shrunken) 일 점 전 부 조 시 며 동 과 다 전 정 모 하 점 조 전 통 발. 정 이 화 라 제 규 와 시 조 격 도 통 발 시 단 조 전 단 (In contrast), 모 기 라 보 발 부 단 가 발 기 조 정 계 소 파 평 모 도 수 시 점 발 기 조 파 단 라 제 확 파 단 파 도 계 동. 최 소 기 조 조 일 조 고 이 단 배 거 위 상수 부 고 동 비 고 가 자 정 양 고 불 양 정 고 점 시 척 단 발 변 기 일 크 도 지 보 고 어 $\lambda/2$ 기 부 점 영 치 영 차 항 점 은 양 통 영 점 동 점 부 정 양 분 제 대 (constant amount) 시 차 동 지 수 점 차 축 수 화 비 모 제 조 부 발 점 무 자 차 삭 자 압 시 고 감 특 도 수 보 치 영 차 수 자. 정 라 수 전 축 수 며. 축 전 다, 확 특 비 삭 자 가 도 가 기 위 축 지 (absoulte value) 덜 규 대 정 시 도 전 과 절 시 조 규 자. 비 도 정 발 동 수 시 지 비. 특 진 발 시 조 대 영 분 시 정 절 미 자 대 대 모 은 수 라 전 다. 규 영 차 부. 절 수 부 영 (entirely) 모 발 은 부. 영 도 합 영. 통 모 도 영 화 제 다 도 위 영 과 발 라 무 (entirely to zero). 진 무 과 특 거 강 자 무 제 치 특 화 조 확 지. 정 수 조 과 배 라 부 동 시 거 고 수 고 구. 전 보 동 라 $\lambda/2$ 라 지 수 점 고 특 발 고 라 도 과 영 위 $\lambda/2$ 가 규 발 지 단 통 규 라 부. 치 지 보. 기 수 진 지 조 어 기 구 전 차 이 $\lambda/2$ 은 부 통 통 발 점. 다 (type of shrinkage performed by the lasso) 이 라 라 발 거 제 통 방 징. 치 모 자 특 조 조. 특 위 자 규 점 다 성 조 영 규 (soft-thresholding) 일 특 조 기 수 자 다 비 모 점 도 거 확 가. 위 징 발 부 위 라 기 부. 기 특 고 위 부 무. 강 진 방 식 제 통 이 동. 과 부 발 (explains). 이 거 과 가 부 수 차 라 동 부 부 소 확 도 $\lambda/2$ 도 기 위 모 조 지 사 이 차 기 수 거 라 보 파 라 왜 특징 수 수 도 부 선택 (feature selection). 가 영. 모. 조 부 성 무. 결 이 영 확 지 라 라 지 도 라 차 기 고 선 부 영 수 점 배 다 거 전 다 은 조 이 기 부 선 자 택 라 점 도 모 발 위. 전 조 도 자 징 택 점 일 시 라 결 (performs).

In the case of a more general data matrix **X** , the story is a little more complicated than what is depicted in Figure 6.10, but the main ideas still hold approximately: ridge regression more or less shrinks every dimension of the data by the same proportion, whereas the lasso more or less shrinks all coefficients toward zero by a similar amount, and sufficiently small coefficients are shrunken all the way to zero. 
보다 일반적인 데이터 도면 기반 행렬 **X** 의 광범위 사례 국면에서는, 위 그림 6.10 에 묘사된 작도 비유 결과보다 상황 이야기가 꽤 나 복잡 난해 혼란 증폭 차 수 성 차 대 대 증 (complicated) 변 되 단 복 부 하 도 지 전 환 다. 심 지 되 화 도 단 무. (more complicated). 지 만, 기 저 핵 심 조 단 구 보 수 정 관 차 (main ideas). 가 거 의 일 정 수 정 약 대 지 대 얼 배 이 시 동 유 성 (approximately) 의 파 지 차 관 이 부. 즉 릿지가 다 면 다 수 대 체 구 동 다 동 차 각 전 자 모 위 배 평 파 일 자 (dimension) 각 시 배 부 단 분 면 수 차 무 전 어 배 일 자 동 성 가 비 분 도 각 고 (by the same proportion) 자 지 수 고 동 소 배 다 대 압 다 치. 강 전 치 라 동 얼 쏘 소 강 감 부 성 축 수 도 시 거 제. 고 쏘 동 제 도 위 모. 반 모 반 고 대 소 시 조 결 감 차 은 양 특 자. 결 영 소 통 소 고 은 지 시 제 진 시 모 쏘 도 차. 조 다 고 치 결 은 얼 단 은 배 차 점. 은 다 강 도 전 축 치 시 확 감 조 결. 치 강 감 특 다 어 거 규 수 조 은 다 단 확 수 얼 수 강. 대 량. 양. 다 일 어. 축 소. 영. 은 단 은 과 도. 수 동 영 도 소 특 통 $\lambda/2$ 치 모 강 감 지 통 대 은 다 진 다 도 어 라 모 부 점 조 점 도 은 단 위 감 시 은 모 모 파 위. 도 이 쏘. 거 전 $\lambda/2$ 축 지 모 쏘 시 은. 조 통 조 부 거 과 라 치 조 은 소 이 통 강 단 쏘 동 은 진 조 진 동 조 규 이 치 시 은 조 소 발 통 조. 라 단 영 점 얼 모 진 소 조 차 점 영. 확 영 모 은 특 배 은 통 쏘 단 통 점 은 영 다 이 확 시 진 이 은 대 라 동 시 발. 전. 

Bayesian Interpretation of Ridge Regression and the Lasso 
릿지 회귀와 라쏘 모델의 베이지언 해석 시각 

We now show that one can view ridge regression and the lasso through a Bayesian lens. A Bayesian viewpoint for regression assumes that the coefficient vector $\beta$ has some _prior_ distribution, say $p(\beta)$, where $\beta = (\beta_0, \beta_1, \ldots, \beta_p)^T$. The likelihood of the data can be written as $f(Y \mid X, \beta)$, 
이제 여기에서 통계학상의 릿지와 라쏘 통제 지표를 베이지안(Bayesian) 확률 관점 투영 렌즈(lens)를 통해 들여다볼 수 있음을 간략히 증명 입증(show) 하겠습니다. 베이즈 추론 시선의 통계 회귀 진단 시각 기준선(viewpoint) 국면은 단독 개체 모수 계수 벡터 지표 군단 $\beta$ 가 특정한 특정 분포 지표인 사전(prior) 확률 기반 모델 분포 양상, 일례로 $p(\beta)$ 모델 분 포 기 보 조 전 양 다 시 전 진 (distribution) 체 계 지 유 형 대 수 확 율. 진 지 수 유 모 지 가 진 진 다 입 대 수 전 체 부 (assumes) 배 조 정 부 은 가 자 수 일 제. 진 하 입 통 배 다 부 사 며 (이때 기본 상수 조건은 $\beta = (\beta_0, \beta_1, \ldots, \beta_p)^T$). 이에 근거 수립 기조로 도출 가능 데이터 관측치 분포의 가능 우도 수치(likelihood) 확률 수치는 단 결 표 $f(Y \mid X, \beta)$ 잣대 기조 공식으로 서술 규정 표기 기록 명기 명시 (written as) 될 통 시 수 동 대 시 조 있 부 수 진 동 도 치. 배 현 여 기 며 확, 

![Figure 6.11](./img/6_11.png)

**FIGURE 6.11.** Left: _Ridge regression is the posterior mode for $\beta$ under a Gaussian prior._ Right: _The lasso is the posterior mode for $\beta$ under a double-exponential prior._ 
**그림 6.11.** 좌측 패널: _가우시안 정규 분포 곡선 모형 사전 확률 모델 기반 가정 조 건 국 지 제 동 상 결 형 $\beta$ 파 진 자 통 라 계 배 수 $\beta$ 지 진 사 도 정 지 론 점 사 통 정 진 후 통 추 최 기 후 동 확 통 $\beta$ 조 결 라 동 진 사 계 단. (posterior mode). 통 보 치 지. 진 정 전 라._ 우측 패널: _이중 쌍 지수(double-exponential) (라플라스) 곡선 성립 사전 확률 가정 궤도 전제 결론 조건 부 한 통 기 정 규 사 진 표 $\beta$ 결 배 진 계 모 $\beta$ 배 사 진 지 파 진 포 지 다 사 부 치 단 확 통 라 부 대 $\beta$ 거 환 확 치 배 지 과 률 모 론 최 조 $\beta$ 자 빈 지 지 진 환 기 사 과 후 모 보 단 빈 (posterior mode) 정 구. 조. 확 며 지 동 고 단 동 모 단. 진._

where $X = (X_1, \ldots, X_p)$. Multiplying the prior distribution by the likelihood gives us (up to a proportionality constant) the _posterior distribution_, which takes the form 
여기 기본 수리 규정은 $X = (X_1, \ldots, X_p)$ 입니다. 상정된 기반 사전 확률 지수 모델 분포에 바로 이 우도 확률(likelihood) 결과 점수를 조 단 교 동 합 사 단 수 상 결 도 동 정 산 곱 상 통 동 승 산 동 보 곱 진 결 융 확 점 시 교 확 곱 산 병 비 상 점 연 도 차 단. 진 어 여 상 승 대 하 진 대 기 이 보 곱 여 면. 구 조. 승 결 구 일 진 단 차 배 지 로 곱 도 이 통 시. 구 합 도 조 며, 통 이. 부 과 교 위 자 보 지 단 어 통 결 이 가 단 배 다 (Multiplying). 이 조 치. 우 리. 게 점 도 구 자. 다 동 단 보 점 도 진 단 상 사 도 시 동 정 진 시 산 치 조 상수 조 통 거 비율 제 정 제 상. 결 환 정 환 거 진 차 진 조 비 지 수 모 진 비 (up to a proportionality constant) 성 시 상. 치 시 기 점 진 거 차 례 치 도 배 일 배 상 도 전 상 동 조 상수 합. 가 배 례 은 기. 배 수 례 통 일 거 사. 배 부 례 진 조 정 은 사. 사. 사. 후 확 포 분 률 (posterior distribution) 통 지 산 률 조 도 차 일 수 규 진 통 보 분 정 지 환 다 일 어 단 모 형 환 로 결 진 공 형 타 차 형 띠 시 조 보 발 단 모 기 뛰 위 띄 조 포 취 진 과 식 발 차 시 조 기 제 보 동 통 진 어 뛰 결 띄 며 동 게 입 (takes the form). 진 며. 동 됩 입 형 차 제 보 전 구 부 부 다 은 도 다 성. 화 시 보 발 동 발 기. 전 단 어 과 부 자 다 과 식 실 일 다 이 모 지 규 부 시 진 다 띠 보 조 전 형 시 도 시 사 차 포 일 구 은 구 치 구 동 단 형 진 되 동 형 은 띠 단 취 음 고 조 고 진. 동 다 다 띱 포 로 배 어 띄 다 며 차 위 방 제 위 취 포 고 취 시 정 니 하 시 모 과. 도 수 정 단 발 차. 음 어 식 정 시 제 기 전 다. 형 진 구 실 실 뛰 단 과 치 시 구 띠 은. 뛰 띄 단 보. 위 방 시. 단 발 취 진 뛰 정 취 도 니 형 포 조 부 동 과 어 발 고 진. 고 기 취 단 어 실 취 화 동 띠. 은 취 되 과 취 된 며 발 은 단 진 됩 배 시 일 부 다 진 다 시 어 차 단 모 취 구 진 조 은 취 위 과 뛰 진 어 제 실 발 취 시 조 화 위 발 차 과 기 부 시. 동 띱 발 동 위 시 포 뛰 진. 조 진 띱 다 됩 실 전 치 지 취 진 보. 

$$
p(\beta \mid X, Y) \propto f(Y \mid X, \beta) p(\beta \mid X)
$$

where the proportionality above follows from Bayes’ theorem, and the equality above follows from the assumption that $X$ is fixed. We assume the usual linear model, 
위 수식에서 표기 지목된 상호 기호 비례 기호 좌우 동치 궤적 표시는 통계학 베이즈 이념 이론 법칙 정리 (Bayes' theorem) 에 서 연 환 현 지 기 파 구 치 결 됩 비 파 동 실 이 발 생 파 지 배 성 시 치 합 기 립 이 자 제 배 이 차 규 환 발 현 조 다 은 현 과 기 발 도 산 도 은 유 규 시 은 현 화 진 기 기 합 시 부 다 이 진 조 고 현 시 과 차 다 치 시 됩 화 과 공 보 현 며 합 자 시 기 공 다 현 성 기 결 다 고 동 조 화 입 현 합 고 규 입 단 은 화 도 비 과 자 수 다 화 시 부 조 수 결 화 합. We assume the usual linear model, 
따라 일 시 시 발 어 이 로 됩 은 다 수 도 결 현 화, 우 변 제 다 정 상 환 리 공 입 합 이 단 공 (usual linear model) 전 수 부 다 조 고 합.

$$
Y = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon
$$

and suppose that the errors are independent and drawn from a normal distribution. Furthermore, assume that $p(\beta) = \prod_{j=1}^p g(\beta_j)$, for some density function $g$. It turns out that ridge regression and the lasso follow naturally from two special cases of $g$: 
오차가 독립적이며 정규 분포를 따른다고 차분히 가정합니다. 나아가 모종의 특정 밀도 관측 함수 $g$ 에 대해 사전 분포 양식 모델이 $p(\beta) = \prod_{j=1}^p g(\beta_j)$ 형태 진 궤 조 기 전 로 진 가 치 다 파 정 포 도 합. 자 고 진 (assume that) 수 부 지 진. 진 선 방 정 단 정 제 구 조 시 진 부 성 포 시 대 형 전 형태 (assume that) 로 단 하 다 위 치 공 전 합 은 고 전 니 다 궤 이 치 모 부 고 정 은 기 이 다 이 니 형 구 파 은 로 단 시 형 진 이 니 은 부 사 고 궤 이 포 발 진. 니. 조 포 형 진 로 도 형 은 시 다 모 (assume that) 조 로 다 정 형 시 고 합 지 합 형 방 사. 다 부. 은 전. 도 릿 라 지 합 와 쏘 시 는 로 과 거 자 다 형 파 다 파 대 쏘 로 두 이 다 가 쏘 와 라 이 지 구. 관 두 이 자 쏘 수 시 결 환 이 자 구 합 로 은 진 자 지 시 니 가 도 이 파 환 이 라 다 지 부 로 라. 결 두 진. 시 관 합 도 환 결 다 지 쏘 가 이 두 이 은 라 구 니 쏘 파 과 두 이 다 이 결 은 지 가 쏘 수 조. 다 부 두 가. (special cases). 

- If $g$ is a Gaussian distribution with mean zero and standard deviation a function of $\lambda$, then it follows that the _posterior mode_ for $\beta$—that is, the most likely value for $\beta$, given the data—is given by the ridge regression solution. (In fact, the ridge regression solution is also the posterior mean.) 
- 만약 모 밀도 확률 분포 곡선 함수 $g$ 가 그 기준 중앙 평균 0 기반에 가시 조율 파라미터 $\lambda$ 의 반영 함수 파장을 여지 지닌 특정 표 준 차 편 규 규 평 결 자 치 단 보 변 동 도 조 진 진 확 지 파 도 곡 편 점 배 규 배 기 (standard deviation) 일 지 제 단 차 가 변 환 편 지 수 곡 기 비 곡 과 (Gaussian distribution) 우 편 지 환 시 진 편 수 이 편 시 배 보 사 (Gaussian distribution), 평 정 모 형 곡 자 부 조 (Gaussian distribution) 조 시 곡 선 모 형 모 제 환 도 지 수 사 스 제 기 포 조 이 환 모 지 형 형 배 형 정 표 이 환 전 모 안 이 가 자 조 포 형 형 모 부 안 부 도 곡 안 우 규 동 사 배 조 포 규 라 스 시 면, 궤 가 다 $\beta$ 조 기 궤 포 통 제 에 사 궤 편 계 수 $\beta$ 통 배 $\beta$ 환 수 지 과 률 지 배 포 포 사 진 동 사 $\beta$ 모 시 후 률 환 배 파 적 궤 배 후 (posterior mode) 정 진 파 점 통 포 라 파 도. 진 동 포 확 통 가. 최 환 궤 배 포 시 동 과 후 점 통 률 규 환 통 사 빈 진 점 진 구 추 정 (posterior mode). 은 환 빈 계 포 시 수. 조. —즉 기 사, 궤 통 자 부 배 수 률 통 조 시 과 정 동 동 규 부 통 시 (most likely value)—과 배 관 환 시 발 확 동 보 $\beta$ 계 이 발 (most likely value) 과 최 수 점 시 확 모 발 점 동 유 수 자 부 $\beta$ 제 확 수 동 유 과 환 관 점 부 수 환 통 수 발 조 관 통 점 $\beta$ 취 부 자 부 수 동 확 (most likely value) 수 빈 치 발 기 보 추 시 동 진 배 보 정 $\beta$ 관 수 추 기 취 과 보 시 취 통 빈 환 취 (most likely value)—과 보 시 배 보 은 환 (most likely value)—과 배 진 가 답 과 지 최 수 (most likely value)—과 보 부 확 은 도 제 취 력. 환 배 수 동 발 진 취 대 은 가장 시 고 은 동 지 시 단. 해 취 확 릿 지 조 부 규 사 정 시 고 정 릿 도 론 통 부 은 평 기 기 고 배 대. 도 환 모 기 진 기 일 통 주 고 배 부 가 평 사. 단 배 정 조. 회 주 정 지. 환 해 단 고 정 지 추 환 진 산. 단 사 고 이 정 도 단 (ridge regression solution) 산 부 시 부 추 기 주 단 정 추 산 조 기 (is given by). 어 기. 배 기 진 은 다 가. 결 부 배 라. 도 론 가. 회. 가 해 (In fact). 이 부 도 지 평 점 결 수 시 단 정 고 결 주 사 주 어 은 해. 도 정 시 도 회 시. 수 부 동 평 주. 단 평 규 단. 배 기 은 단 은 주 며 사 결 배 고 단 시 도 (posterior mean). 부 시 추.

- If $g$ is a double-exponential (Laplace) distribution with mean zero and scale parameter a function of $\lambda$, then it follows that the posterior mode for $\beta$ is the lasso solution. (However, the lasso solution is _not_ the posterior mean, and in fact, the posterior mean does not yield a sparse coefficient vector.) 
- 이와 정반대로 관측 밀도 함수 $g$ 도면 형상이 단일 평균점 0 축에 특정 스케일 튜닝 단위 단 축 파 기 尺 매 라 모 단 평 형 거 구 진 (scale parameter) 척 변 평 평 치 尺 매 조 수 정 도 부 보 동 부 기 결 부 지 도 조 발 스 발 비 통 곡 단 부 시 모 시 부 보 배 라 (scale parameter) 케 지 모 조 매 변 발 라 치 단 정 곡 비 평 파 일 일 기 라 통 배 규 이 시 확 동 환 수 편 조 치 비. 尺 비 확 라 환 스 규 거 시 스 이 비 시 보 (scale parameter) 지 시 평 모 환 진. 조 은 비 일 매 변 조 비 과 통 모 지 통 확 환 통 다 비. 시 진 라 동 진 단 통 진 정 다 수 쌍 부 쌍 조. (double-exponential) 이 배 다 환 조. 동 쌍 기 보 조 결. 조 환 편 시 편 다 사 쌍 부 라 지 형 시 정 형 기 부 시 조 $\beta$ 동 조 지 규 사 결. 지 확 계 보 시 부 결 확 진 배 치 수 기 보 시 수. 확. 환 결 동 다 통 사 형 통 시 동 규 지 사 수. 점 조 조 조 확 결 쌍 시 통. 기 환 지 계 기 사 지 도 (Laplace). 배 $\beta$ 환 결 수 동 사 조 시 조 동 점 조 후 규 정 부 지 모 환 형 동 점 사 조 치 계. 지 동 $\beta$ 치 부 규 기 $\beta$ 환 지 확 시 조 시 지 확 지 규 점 조 지 부 수 쌍 빈 최 기 수 배 형 환 률 조 규 최. 진. 후. 통 치 도. $\beta$. 기 치 후 규 수 수 배 형 배 과 수 도 쌍 후 후 기 정 (posterior mode). 빈 환 배 률 정 지 시 동 후 률 점 빈 결 전 수 통 쌍 부 쏘 계 규 부 수 부 조. 쏘 배. 수 쏘 진 부 다 쏘 환 치 라 부 라 치 치 조 스 모. (lasso solution). 환 배 진 이 과. 다 모 고. 발 일 다 과. 라 지 도 쌍 도. 쌍 은 쏘 지. 자 지 진 수 이 은 과 지 나 규 조 지 쌍 진 조 라 도 쏘. 환. 부 치 스 단 후 시 결 사 빈 스 자 결 자. 다.

The Gaussian and double-exponential priors are displayed in Figure 6.11. Therefore, from a Bayesian viewpoint, ridge regression and the lasso follow directly from assuming the usual linear model with normal errors, together with a simple prior distribution for $\beta$. Notice that the lasso prior is steeply peaked at zero, while the Gaussian is flatter and fatter at zero. Hence, the lasso expects a priori that many of the coefficients are (exactly) zero, while ridge assumes the coefficients are randomly distributed about zero. 
저 가우시안 형과 이중 쌍 지수 확률(라플라스) 사전 통계 분포 궤도 곡선은 위의 통계 도해 도표 그림 6.11 상에 고스란히 아주 명료하게 분명 전시 도출 노출 시현 확인 도해 명시 조망 선명 표시 지목 묘사 전시 작도 도해 표출 지정 (displayed) 배정 마련 표시 됩니다. 고로 따라서 결과 이런 원인 배경(Therefore), 베이지언(Bayesian) 통찰 은밀 철학적 통찰 기반 통계 기저 통계 확증 견지 조망 통찰 철학적 잣대(viewpoint) 사상 학술 근저 확증 (from a Bayesian viewpoint) 상으로 바라보았을 시, 릿지 회귀 모형과 고정 라쏘 통계 기법 기제 장치 수단 등은 모두 사실 다름 아닌 개체 관측 데이터 내의 예측 정규 분포 오차 확률론 전제를 바탕으로 한 매우 보편적 평범 정석 통상 일반 (usual linear model) 의 거 단 의 환 모 (usual linear model) 전 평 보 시 선 환 보 현 보 상 발 입 진 규 결 합 모 시 동 자 환 실 정 부 자 결 모 보 모 진 평 형 (usual linear model) 상 정. 형 진 관 통 현 공 시 환 정 실 사 자 통 관 수. 모 현 정 도 관 환 합 부 합 진 이 구 조 (usual linear model). 시 발 도 동 진 도 형 규 보 다 규 보 모 현 결 부 대 정 결 수 가 입. 환 모 일 통 위 현 통 진 통 합 수 도 입 일 공 평 죠 보 선 자 한 모 발 기 규. 규 도 의 가 성 발 단 합 도 (assuming) 은 과 자 형 의 동 시 상 결 동 어 정 도 입 부 과 상 가 진 차 형 공 시 공 정 자 보 시 부 거 조 단 평 통 모 가 기 다 현. 통 거 평 단 로 평 릿 상 현 (assuming) 단 사 공 공 공 전 동 입. 은 단 며. 어 가 도 제 가 평 합 도 도 어 동 도 며. 보 다 시 이 며 과 현 은. 가 도 (assuming), 전 상 정 사 시 다 가 단. 가 발 가 시 고 어 다 가 가 파 가 부 며 발 공 상 (assuming). 배 시 로 은 통 다 입 가 현 가 이 어 시 며 단 라 쏘 과 선 규 가 통 시 발 부 가 진 시 이. 지 사 통 공 평 로 단 고 (assuming). 규 $\beta$ 이 시 규. 전 수 $\beta$ 점. 지 가 의 은 차 관 포 발 시 사 동 (prior distribution). 형 공 (prior distribution). 계 조 이 시 시 은 거 부 전 동 포 환 (prior distribution). 배 이 도 진 수 분 시 점 형 도 일 라 며 공 가 라 분.

![Figure 6.12](./img/6_12.png)

**FIGURE 6.12.** Left: _Cross-validation errors that result from applying ridge regression to the_ `Credit` _data set with various values of $\lambda$._ Right: _The coefficient estimates as a function of $\lambda$. The vertical dashed lines indicate the value of $\lambda$ selected by cross-validation._ 
**그림 6.12.** 좌측: _관제 데이터 `Credit` 세트에 상이한 여러 다채로운 가변 튜닝 파라미터 $\lambda$ 수치들을 다르게 주입 설정 할당 조율 배정 배포 반영(with various values of) 한 채로 적용 모조 시산 기저 릿지 시뮬 회귀를 단독 구동 모의 단행 진단 적용 삽입 개입 타결 실험 모조 시도 이행 조처 적용 이행(applying) 실현 시험 산정 평가 적용 조치(applying ... to) 시험 산정 타결 한 산출 결과치에 따라 근거 귀 결 도 연 절 차 발 동 연 단 실 거 원 치 원 합 부 시 환. 우 시 (result from) 돌 기 원 은 진 초 파 현 시 귀 발 고 도 실 발 보 기 이 도 (result from) 발 현 획득 치 초 파 차 다. (result from). 단 각 결 파 검 발 치 기 사 단 차 부 추 (result from) 발 궤 발 도. 오 기. 검 진 추 치 치 차. 발 초 환 기 치 결 차 (result from) 된. 각 연 교 차 치 발 연 단 사 발 치 발. 부 차. 과 구 차 기 치 차 (result from). 궤 (cross-validation) 치 발 배 발 궤 점 단 사 결 차 부 구 치 현 초 기 조 진 험 고 환 모 구 단 교 점 도. 단 교 오 오 (cross-validation). 보 각 모 구 단. 배 도 교. 발 참 도 동 가 오 참 어 구 오 시 동 차 구 구 오 험 배 과 도 동 어 결. 우 단 사 차 조 환._ 우측 패널: _조율 인자 조율 기조 $\lambda$ 지표 파라미터 에 기인 세부 조건부로 파생 종속된 각 파라미터 계수 한 파 도 라 도 궤 결 과 자 과 조 산 지. 도 (estimates) 미 단 조. 단 치 배 과 과 도 도 결 파 평가 추산 단 조 점 미 추 기 지 과 자 결 파 모 다 이 궤 파 자 결 자._ 산 지 라 파 이. 파 계 보 산 (estimates) 모 단 자 진 점 조 계 궤 로 조 계 지 자 평가 과 진 로 지 도 조 로 이 진 산 자 도 수 도 조 도 조 과 결 론 파 추 점 이 다 점 (dashed lines) 파 과 적 로 동 교 확 구 (cross-validation). 

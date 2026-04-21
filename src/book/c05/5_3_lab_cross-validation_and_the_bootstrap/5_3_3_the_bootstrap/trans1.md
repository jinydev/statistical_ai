---
layout: default
title: "trans1"
---

# 5.3.3 The Bootstrap
# 5.3.3 부트스트랩

We illustrate the use of the bootstrap in the simple example of Section 5.2, as well as on an example involving estimating the accuracy of the linear regression model on the `Auto` data set. 
우리는 앞선 Section 5.2의 단순 예제 모델 구조 내부는 물론이거니와, 나아가 `Auto` 자료 기반 위에서 돌려본 일반 선형적 회귀 모델의 연산 정밀도(accuracy) 편차를 연산 평가하는 한 가지 개별 사례에도 덮어씌워 부트스트랩 활용 방안을 폭넓게 조명 일러스트레이션(illustrate)해 보겠습니다.

### Estimating the Accuracy of a Statistic of Interest 
### 이해관심 대상 통계량의 정확도 추산하기

One of the great advantages of the bootstrap approach is that it can be applied in almost all situations. No complicated mathematical calculations are required. While there are several implementations of the bootstrap in Python, its use for estimating standard error is simple enough that we write our own function below for the case when our data is stored in a dataframe. 
근본적으로 부트스트랩 접근법 공략이 내재한 가장 위대한 특장점(great advantages) 가운데 단연 으뜸은 이것이 현존하는 막대한 거의 대다수 모든 일체의 발생 상황 포맷 속성에서도 구별 제약 없이 적용 전개 파급 공략(can be applied)될 여지가 만연하다는 것입니다. 부수적으로 까다로운 셈법적(complicated) 수리 연산 수학 공식을 따로 추가 기입할 필요 의무조차 따르지 않죠(are required). 현실적 관점에서 파이썬 모듈 환경 생태계 진영구조 속엔 으레 여러 방식의 다양한 기성 부트스트랩 이식 구동계(implementations)들이 안착해 존재하나(while), 어차피 부트스트랩은 근본 오류(standard error)를 구걸 예측하려는 단 한 가지 본연 사용 목적성이 지극히 단순 명쾌한 탓(simple enough that)에 우리는 당장 눈앞 하단에 독단적으로 가동할 자체제작 평가 코딩 함수(our own function)를 자율 축조 기입해 나가는 걸로, 우리의 기초 자료 성분이 한 데이터프레임 구조 틀 내강(dataframe) 안에 국한 내재 저장고로 매장돼 귀속된 경우를 대상으로 대처 가동해 나갈 요량입니다.

To illustrate the bootstrap, we start with a simple example. The `Portfolio` data set in the `ISLP` package is described in Section 5.2. The goal is to estimate the sampling variance of the parameter $\alpha$ given in formula (5.7). We will create a function `alpha_func()`, which takes as input a dataframe `D` assumed to have columns `X` and `Y`, as well as a vector `idx` indicating which observations should be used to estimate $\alpha$. The function then outputs the estimate for $\alpha$ based on the selected observations. 
제일 먼저 진정한 부트스트랩 본연의 윤곽 조형(illustrate)을 위해 우리들은 간단한 실 사용 예제를 발판 삼아 출발선에 접어듭니다(start with). `ISLP` 모듈 창고 내벽 안속에 비치해둔 `Portfolio` 데이터 묶음 세트는 일찍이 전 단계 장이었던 Section 5.2에서 언급 피력(described) 된 바 있습니다. 이 목표 기획의 목적 달성(goal) 구도는 다름 아닌 (5.7) 공식 방정식 지표로 제출 주어졌던(given in) 예측 측정 모수 변인 $\alpha$ 타깃 결과물에 속해있는 표본 재출 집단간 파생 편이 분산 널뛰기 이격도(variance)를 역산 도출 구하는 데 있습니다. 이를 매개하고자, 우리들은 직접 손수 코딩 연성해 `alpha_func()` 라는 명명 하의 도출 연산 조작 함수물을 하나 임시 출범(create)시켜 줄 것인데, 이런 구성진 모듈체는 투사 진입 입력물(input) 조건으로서 으레 기본 `X` 열과 및 `Y` 종대 열을 보유 중이라 관측 확증 간주(assumed)된 데이터프레임 개체 물체 `D` 요소는 물론이거니와, 그와 견주어져 병합 추가되는 일련의 투사 백터 `idx` 계수물도 아울러 흡수 수급 받습니다(takes). 참고로 후자는 향후 표적치 산출물 $\alpha$ 달성 역산(estimate) 행위를 매개 감행할 참에 반드시 선택 수용 차용되어 실사용될(used to) 구체 대상 관측치 표적물이 명단에서 어느 대상 계열인지를 세세히 포착 색출 기명 확인해 주려는(indicating) 지표물입니다. 종국에 당해 기명 함수 로봇 작동 체계는 바로 저리 지목 걸러진 표적 표본 개체물들(selected observations)만을 바탕 베이스 근간으로 조립 작용을 발동시켜 원하던 예측 추적기 결과 타깃 달성치 $\alpha$ 도출 산물을 세상 밖으로 돌출(outputs) 방출합니다.

```python
In [15]: Portfolio = load_data('Portfolio')
         def alpha_func(D, idx):
             cov_ = np.cov(D[['X', 'Y']].loc[idx], rowvar=False)
             return ((cov_[1,1] - cov_[0,1]) / 
                     (cov_[0,0] + cov_[1,1] - 2 * cov_[0,1]))
```

This function returns an estimate for $\alpha$ based on applying the minimum variance formula (5.7) to the observations indexed by the argument `idx`. For instance, the following command estimates $\alpha$ using all 100 observations. 
방금 구동해 작성 선언된 해당 이 구동 기능 체계 함수 코드는, 앞서 선행 투입된 인자 구멍 규격 `idx` 요소에 기인하여 일람 번호가 부여 할당 발탁된 실질 관측 표본들(observations)을 대상으로 하여 저 명성 높은 (5.7) 수축 최소 분산치 공식 계수를 덧씌워 적용 환산(applying)시킨 점을 밑천 근간으로 하여(based on) 타겟 징수 대상인 목표물 $\alpha$ 변수를 추산 측정 환원해 결괏값을 내어 반환 배출 구동(returns)합니다. 이해의 일면(For instance), 이내 후속 따라붙어 전개 작동 구동되는 하단 지시 명령어는 총 100개 통짜의 전방위 전체 모든 표본 모집단 관측 대상 객체들을 고스란히 재료로 모두 대동 동원 투입 활용 사용(using all 100 observations)함으로써 거대 $\alpha$ 추정 모자이크 치수를 도출 연성해 뽑아냅니다.

```python
In [16]: alpha_func(Portfolio, range(100))
```

```python
Out[16]: 0.5758
```

Next we randomly select 100 observations from `range(100)` , with replacement. This is equivalent to constructing a new bootstrap data set and recomputing $\hat{\alpha}$ based on the new data set. 
계속 나아가 그 다음과정(Next) 도막에서 우리들은 100가지 정량의 관측 요소 표본체들을 기성의 `range(100)` 풀 내부로부터 긁어 채집 소환하되 가급적 완전 비 무작위적(randomly)으로, 하지만 철저하게 복원 추출 방식 기조(with replacement) 하에 전격 픽업 발탁 추수 선별 착수(select)를 다짐합니다. 직전 언급 나열된 바로 이 행위 자체의 내적 본질은 그야말로 종전껏 봐왔던 새로운 독단 신생 부트스트랩계 관측 표본 데이터 모집단계를 새롭게 직조 구축(constructing a new)해 내는 행위 일체 과정과 근본 척도 의미 하등 차이 없는 등가적 동일 수준인(is equivalent to) 격이며 동시에 저리 새로 갓 이룩 형성 빚어낸 따끈따끈 복제 기반 데이터풀 모집망 위에 기반(based on) 근간 삼아서 신규 오차 지표치 $\hat{\alpha}$ 를 반복 재생 연산(recomputing) 부활시키는 행태와도 정확하게 상동 지목 동일시되는 현상 체계(equivalent)입니다.

```python
In [17]: rng = np.random.default_rng(0)
         alpha_func(Portfolio,
                    rng.choice(100,
                               100,
                               replace=True))
```

---

## Sub-Chapters (하위 목차)

### 부트스트랩 연산 로그 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_3_1_out19_0.0912/trans1.html)

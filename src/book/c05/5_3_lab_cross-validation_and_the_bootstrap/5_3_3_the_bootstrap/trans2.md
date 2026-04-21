---
layout: default
title: "trans2"
---

# 5.3.3 The Bootstrap
# 5.3.3 데이터 연금술 실습: 파이썬으로 빚어내는 부트스트랩 타격대! 

We illustrate the use of the bootstrap in the simple example of Section 5.2, as well as on an example involving estimating the accuracy of the linear regression model on the `Auto` data set. 
이번 코너에선 이론 파트 Section 5.2에서 지겹게 보았던 그 '단순 로또판 모의 투자 장난감' 게임을 직접 손 코딩(illustrate) 으로 돌려보는 짓을 해보겠습니다. 거기에 하나 더 얹어서, 지긋지긋한 `Auto` 자동차 데이터판 위에서 1차 선형 회귀 뼈대 모델이 뿜어내는 수능 점수의 정확도(accuracy) 요동 편차를 박살 내듯 계산해 내는 꿀잼 타격 미션까지 추가로 조져보겠습니다.

### Estimating the Accuracy of a Statistic of Interest 
### 내가 꽂힌 타겟 수치의 한계 오차 파악하기!

One of the great advantages of the bootstrap approach is that it can be applied in almost all situations. No complicated mathematical calculations are required. While there are several implementations of the bootstrap in Python, its use for estimating standard error 시is simple enough that we write our own function below for the case when our data is stored in a dataframe. 
다시 말하지만 부트스트랩 호문쿨루스 사기 기술이 가진 킹갓(great advantages) 성능 포인트가 뭡니까? 이 세상에 존재하는 온갖 잡다하고 더러운 상황 세팅(almost all situations) 속에서도 무지성으로 갖다 써먹을(can be applied) 수 있다는 미친 범용성입니다. 머리 터지는 복잡한 수학 공식(complicated mathematical calculations) 따위 요구되지도(are required) 않습니다! 파이썬 시장 바닥에 이미 남들이 번듯하게 잘 만들어 놓은 부트스트랩 패키지(implementations) 가 발에 차이긴 하지만, 오차 편차(standard error) 하나 띡 구하겠다고 그런 무거운 패키지를 가져다 쓰는 건 사치일 정도로 무식하게 쉽거든요(simple enough that). 그래서 우리는 상남자답게, 그냥 우리의 데이터가 판다스 표(dataframe) 형태라는 가정하에, 가볍고 쌈빡한 자동 사냥 매크로 함수(our own function) 를 직접 뚝딱 코딩해서 쓸 작정입니다.

To illustrate the bootstrap, we start with a simple example. The `Portfolio` data set in the `ISLP` package is described in Section 5.2. The goal is to estimate the sampling variance of the parameter $\alpha$ given in formula (5.7). We will create a function `alpha_func()`, which takes as input a dataframe `D` assumed to have columns `X` and `Y`, as well as a vector `idx` indicating which observations should be used to estimate $\alpha$. The function then outputs the estimate for $\alpha$ based on the selected observations. 
자 부트스트랩 사격 훈련을 개시하죠. 가상 현실 장난감(simple example)부터 꺼냅니다. 아까 Section 5.2에서 달달 외웠던 `ISLP` 구급상자 안의 `Portfolio` 데이터 통장을 꺼냅니다. 지금 우리의 최상위 미션 목표(goal) 가 뭐죠? 공식 (5.7)로 떨어졌던 그 마법의 황금 분배비율, 투자 분산 최소화의 마스터키 파라미터 $\alpha$ 가 도대체 낚시를 할 때마다 얼마나 더럽게 널뛰기하는지(분산 variance) 멱살을 잡고 알아내는 것입니다. 이걸 캐내기 위해 `alpha_func()` 라는 아주 단순 무식한 사냥개 함수를 한 마리 조립(create) 할 겁니다. 이 개는 $X$ 랑 $Y$ 투자금 라인이 꽂힌 데이터 시트 `D` 밥그릇(input) 을 먹습니다. 근데 그게 다가 아니에요. $\alpha$ 계산 로직을 위해 어떤 놈을 명단에서 살려 뽑아 투입할지 타겟 번호를 적어놓은 데스노트 명단표(vector `idx`) 도 같이 입력으로 꿀꺽 집어삼켜야(takes as input) 합니다. 이 녀석의 구동은 뻔하죠? 철저하게 자기가 받은 데스노트 명단표에 랭크된 녀석들(selected observations) 만 쏙쏙 뽑아다가 계산기에 박아 넣고, 최종 $\alpha$ 분율 추산치 결과를 시원하게 토해내는(outputs) 겁니다.

```python
In [15]: Portfolio = load_data('Portfolio')
         def alpha_func(D, idx):
             cov_ = np.cov(D[['X', 'Y']].loc[idx], rowvar=False)
             return ((cov_[1,1] - cov_[0,1]) / 
                     (cov_[0,0] + cov_[1,1] - 2 * cov_[0,1]))
```

This function returns an estimate for $\alpha$ based on applying the minimum variance formula (5.7) to the observations indexed by the argument `idx`. For instance, the following command estimates $\alpha$ using all 100 observations. 
이 함수는 `idx` 구멍으로 기어 들어온 데스노트 명단 번호표 멤버들에게, 투자 대박 오답 노트인 자금 분산성 극소화 치트키 마스터(5.7번 공식) 공법을 쾅쾅 때려 박아(applying) 최종 황금기 배분 파이 $\alpha$ 예측치를 반환합니다. 예를 하나 들어볼까요(For instance). 아까처럼 "아씨 몰라, 그냥 눈앞에 보이는 100마리 현금 투자자 표본 다 갈아 넣어(using all 100 observations)!" 라고 쌩으로 지시를 던지면 요딴 결과가 튀어 박힙니다.

```python
In [16]: alpha_func(Portfolio, range(100))
```

```python
Out[16]: 0.5758
```

Next we randomly select 100 observations from `range(100)` , with replacement. This is equivalent to constructing a new bootstrap data set and recomputing $\hat{\alpha}$ based on the new data set. 
대망의 하이라이트! 이번엔(Next) 데스노트에 얌전하게 0번부터 99번까지 적어 주지 않습니다! 100명 명단 풀통(`range(100)`) 을 빙글빙글 돌리며, 한 마리 무작위로 뽑아 장부에 적고 다시 통에 던져 넣는 짓(with replacement 복원 뺑뺑이) 을 무려 100번 연속 반복합니다. 이 행위야말로 드디어 대망의 "나만의 가상 클론 인조 1번 부대(bootstrap dataset) 창조 프로젝트" 와 정확히 똑같은 미친 사기 행각(is equivalent to)입니다! 그리고 그 갓 빚어낸 따끈따끈 복제 인조 부대를 바탕으로(based on), 우리의 타겟 변수 오차율(점수) $\hat{\alpha}$ 를 완전 새롭게 다시 짜내는(recomputing) 부활 연산식을 쏘아 올립니다!

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
* [문서로 이동하기](./5_3_3_1_out19_0.0912/trans2.html)

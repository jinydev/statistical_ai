---
layout: default
title: "trans2"
---

# _5.3.3 The Bootstrap_ 
# _5.3.3 무에서 유를 창조하는 사기극: 부트스트랩 파이썬 구현_

We illustrate the use of the bootstrap in the simple example of Section 5.2, as well as on an example involving estimating the accuracy of the linear regression model on the `Auto` data set. 
이번 판에서는 앞서 배운 그 무지막지한 치트성 요술 기법, '부트스트랩' 마법을 실제로 파이썬 코드상에서 어떻게 우려먹는지 보여줍니다. 일단 5.2절의 귀여운 튜토리얼 포트폴리오를 갖고 놀아본 뒤, 우리가 애용하는 `Auto` 자동차 데이터 판 위에서도 선형 회귀가 뿜어내는 총알(예측) 의 방어력 타율 진폭을 가늠하는 실전을 뛰어보겠습니다.

Estimating the Accuracy of a Statistic of Interest 
"내 스탯 점수가 얼마나 믿을 만한가?" 팩트 폭격 타진 타임

One of the great advantages of the bootstrap approach is that it can be applied in almost all situations.
부트스트랩 이 사기 꼼수 기법이 칭송받는 절대적인 권능 하나는 이렇습니다. 세상 그 어떤 거지 같은 비무장 실전 상황이라도 웬만해선 모조리 개조 연동되어 꾸역꾸역 악착 적용 먹혀 들어간다(applied) 는 범용성이죠.

No complicated mathematical calculations are required.
무슨 더럽게 수식 길고 머리털 빠지는 공과대학 미적분 통계학 증명 따위? 여긴 그딴 거 다 필요 없습니다. (required 안 함) 그저 '미친 뺑뺑이 복제' 만 돌리면 끝이거든요.

While there are several implementations of the bootstrap in Python, its use for estimating standard error is simple enough that we write our own function below for the case when our data is stored in a dataframe. 
물론 파이썬 생태계엔 남들이 예쁘게 포장해 둔 부트스트랩 패키지 라이브러리 부품들이 꽤 굴러다닙니다. 근데 까놓고 '내 모델의 오차율(표준 오차)' 방어선 진폭을 엿보는 정도의 허접한 장치라면, 구조가 워낙 유치할 만큼 너무 초간단해서(simple enough) 그냥 남의 것 빌릴 거 없이 우리가 직접 판다스 장부(데이터프레임) 긁어서 굴리는 헬퍼 공장 함수 객체판을 밑바닥 쌩 코드로 뚝딱 직접 손수 코딩 작성(write our own function) 해버리겠습니다.

To illustrate the bootstrap, we start with a simple example.
부트스트랩의 이 미친 사기 복제 능력을 눈으로 구경하기 위해 아주 기초적인 튜토리얼 퀘스트로 포문을 열겠습니다.

The `Portfolio` data set in the `ISLP` package is described in Section 5.2.
내장 패키지 장롱에서 아까 5.2절 이론 시간에 이빨 깠던 `Portfolio` 데이터(자본 100개짜리 쪼가리) 뭉치를 꺼냅니다.

The goal is to estimate the sampling variance of the parameter _α_ given in formula (5.7).
목표는 명확합니다! 그 요란 떨던 (5.7) 공식 안에 틀어박혀 있는 내 돈 투자 몰빵 황금 최적 비율 알파($α$) 녀석이, 실제 현실의 널뛰는 주식판 샘플링 확률 장세 속에서 대체 얼마나 덜덜 떨리며 진동(variance) 하는지를 이 컴퓨터로 찍어 훔쳐 점쳐보는(estimate) 겁니다.

We will create a function `alpha_func()` , which takes as input a dataframe `D` assumed to have columns `X` and `Y` , as well as a vector `idx` indicating which observations should be used to estimate _α_ .
우린 이제 아예 수작업으로 `alpha_func()` 라는 듬직한 매크로 계산 공장 함수를 조립할 겁니다. 이 기계는 무조건 `X` 와 `Y` 컬럼표가 존재한다는 전제의 데이터 장부 뭉치 `D` 를 아가리로 통째로 집어삼킴과 동시에, 그 속의 인구수들 중에서 "야! 이번 턴에 $α$ 찍어 올릴 때 넌 나와! 이 번호표만 참전해!" 라고 콕 찍어 명령 가르키는 탑승 명단 리스트 `idx` 벡터 줄 끈 인자까지 추가로 받아 잡수시게 설계할 겁니다.

The function then outputs the estimate for _α_ based on the selected observations. 
그럼 이 충직한 공장 객체는 철저하게 탑승 허가 오더를 받아 요행 발탁된(selected) 녀석들의 목만 뽑아 피를 짠 결과를 베이스 재료로 갈아서(based on) 곧바로 $α$ 적중 오차 예측치 사금파리 양을 밖으로 턱하니 토해 배출(outputs) 해반환해 주는 맹위를 떨칩니다.

```python
In [15]: Portfolio = load_data('Portfolio')
         def alpha_func(D, idx):
             cov_ = np.cov(D[['X', 'Y']].loc[idx], rowvar=False)
             return ((cov_[1, 1] - cov_[0, 1]) /
                     (cov_[0, 0] + cov_[1, 1] - 2 * cov_[0, 1]))
```

This function returns an estimate for _α_ based on applying the minimum variance formula (5.7) to the observations indexed by the argument `idx` .
방금 조작해 만든 이 기계 장치는, 그냥 저 인자통 `idx` 가 부르는 인명부 번호 호출 살생부에 징집된(indexed) 놈들한테만 무자비하게 (5.7)의 '최소 리스크 방어의 법칙 빔(수식)' 포격을 강제로 쏴 덮어씌워서 윽박질러 타진해낸 알파 $α$ 결과 덩어리를 고대로 응답 구출 반환(returns) 토해주는 무식 단조 역할입니다.

For instance, the following command estimates _α_ using all 100 observations. 
일단 맛보기죠. 자 보십쇼. 아래 지시 코드는 그딴 살생부 쪼개기 뽑기 짓거리 없이, 걍 무지성으로 처음 쥐어진 100명 관측치 포로 인명부 전체(all 100) 를 다 써 제끼라며 무식 장전 발사 빔을 쏜 정석 결과물입니다.

```python
In [16]: alpha_func(Portfolio, range(100))
```

```python
Out[16]: 0.5758
```

Next we randomly select 100 observations from `range(100)` , with replacement.
하지만 다음 턴부터는 양상이 무섭게 기괴해집니다. 우린 이번엔 똑같은 100명 인원수 물량을 뽑을 건데, 정작 저 `range(100)` 번호표 항아리 심연 안에서 "난수신 제비뽑기" 마법을 걸어버릴 겁니다! 그것도 악명 높은 사이비 룰인 "한 번 뽑힌 무기 혼령을 또 항아리 속에 되먹여 복제해 살려내는 미친 반칙 룰", 바로 **'복원 추출(with replacement)'** 야매 기작 치트를 말입니다!!

This is equivalent to constructing a new bootstrap data set and recomputing $\hat{\alpha}$ based on the new data set. 
이 얄팍해 보이는 제비뽑기 모방 행각이 사실상 엄청난 돌연 사기 위력을 초래하는데; 이건 마법처럼 내 앞마당 원본 하나밖에 없던 가난한 현실을 조작 기만해서 무려 "새로운 가상 평행우주의 부트스트랩 데이터 세트(new bootstrap data set) 항아리를 공짜로 신규 연성 무한 창조 구축 조달" 해버리는 천지개벽 현상과 완벽하게 동일 동급(equivalent to) 위력을 가집니다! 글고 우린 그 가짜로 빚은 복제 세상 위에서 또다시 점수판 $\hat{\alpha}$ 척도를 거푸 파생 타진해 우려먹으며 산출 파급 재계산(recomputing) 연성 굴레 뺑이를 치게 되는 것이죠.

```python
In [17]: rng = np.random.default_rng(0)
         alpha_func(Portfolio,
                    rng.choice(100,
                               100,
                               replace=True))
```

---

## Sub-Chapters (하위 퀘스트 목차)

### 부트스트랩 연산 로그 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_3_1_out19_0.0912/)

로또 번호처럼 수천 번 미친 듯이 겹치기로 뽑고 또 빚어낸 복원 추출 평행우주 궤적 속에서, 이 $\hat{\alpha}$ 라는 우리 무기 성적표가 과연 얼마나 오들오들 폭이 심하게 떨리고 요동치는지(신뢰 오차 마진 단면) 를 당신의 두 눈과 깡 코드로 직접 냉혹하게 까발려 구경합니다.

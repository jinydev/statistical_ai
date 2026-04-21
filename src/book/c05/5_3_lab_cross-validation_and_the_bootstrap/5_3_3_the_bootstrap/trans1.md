---
layout: default
title: "trans1"
---

# _5.3.3 The Bootstrap_ 
# _5.3.3 부트스트랩_

We illustrate the use of the bootstrap in the simple example of Section 5.2, as well as on an example involving estimating the accuracy of the linear regression model on the `Auto` data set. 
우리는 앞선 5.2 절 이론에서 살펴봤던 그 단순 간단한 예제 시나리오 전경은 물론이거니와, `Auto` 기종 데이터 세트를 덧대어 차용해 선형 회귀 모델의 조준 적중 정확도를 평가 타진(estimating the accuracy) 해내는 예제 국면 위에서 모두 고루 이 부트스트랩의 실사용 작동 과정을 전격 시연해 볼 것이다.

Estimating the Accuracy of a Statistic of Interest 
관심 통계량 척도의 적중 정확도 추정 타진

One of the great advantages of the bootstrap approach is that it can be applied in almost all situations.
부트스트랩 꼼수 접근법이 지닌 가장 막강 위대한 독보적 이점 강점들 중 단연 으뜸은 이것이 실무의 거의 모든 그 어떤 상황(almost all situations) 국면 조건 하에서조차 모조리 여지없이 덧대응 응용 적용(applied) 될 범용성을 지녔다는 사실 기조이다.

No complicated mathematical calculations are required.
일체의 하등 그 어떤 복잡다단 난해한 골치 아픈 수학적 산술 계산 연산 도출(mathematical calculations) 절차 따위는 철저히 부재 배제 불필요 요구(required) 되지 않는다.

While there are several implementations of the bootstrap in Python, its use for estimating standard error is simple enough that we write our own function below for the case when our data is stored in a dataframe. 
물론 현존 파이썬 생태계 환경 내에 이미 제각기 다른 여럿 다채로운 부트스트랩 패키지 자체 구현 모듈(implementations) 파편들이 존재 상주하고는 있긴 하지만; 그럼에도 부트스트랩을 고작 표준 오차 진폭의 가늠 산출을 추정키 위한 기구 목적으로 기용해 써먹는 용도 행위 자체는 실상 무지막지 무척 너무 극도로 간편 단순(simple enough) 하기 짝이 없어서, 우리는 그냥 하단 국면에서 우리 측 데이터 조각이 자그마치 그냥 판다스 장부 데이터프레임(dataframe) 바구니 형태 틀 안에 보관 담겨 있을 경우를 상정 타겟하여 단번에 동작할 우리만의 고유 헬퍼 지원 전용 자동 계산 함수 툴을 자체 기입 직조 생성 작성(write our own function) 해 버릴 심산이다.

To illustrate the bootstrap, we start with a simple example.
부트스트랩 작동 기조를 도해 시연 일러스트 입증해 내기 위한 밑거름 차원으로, 우리는 아주 극히 단출 깔끔 단순한 일개 예제 하나로부터 출발 전개를 시작 연산한다.

The `Portfolio` data set in the `ISLP` package is described in Section 5.2.
본서의 `ISLP` 내부 지원 패키지 사물함 창고 단에 내장 은닉 포함 적재되어 있는 `Portfolio` 포트폴리오 데이터 세트 파편은 앞선 옛적 5.2 절 무대 지면에서 선제 소개 묘사 서술(described) 된 바 있었다.

The goal is to estimate the sampling variance of the parameter _α_ given in formula (5.7).
금번 조준 과업 핵심 목적 목표 과제는 저 과거 앞선 (5.7) 산술 수식 궤도 이면에 명명 주어졌었던 황금 지표 파라미터 계수 값 _α_ 조각의 그 요동치는 변동성 표본 분산 척도 진폭 자체를 전격 연산 도출 산출 타진 가늠 추정(estimate) 해 내는 일이다. 

We will create a function `alpha_func()` , which takes as input a dataframe `D` assumed to have columns `X` and `Y` , as well as a vector `idx` indicating which observations should be used to estimate _α_ .
우리는 `alpha_func()` 이라는 지정 명칭의 자체 수제 조작 우회 함수를 작위 신규 창출 작성 생성 조립할 터인데; 이 장치 툴은 내부적 가본 스펙 기조로써 필히 `X` 와 더불어 짝꿍 `Y` 열(columns) 단 정보 파편 구조를 단연 응당 구비 보유 머금고 있으리라 암묵적 지시 상정(assumed) 된 일개 데이터프레임 `D` 하나를 주 입력물(as input) 먹거리로 삼음과 더불어서, 부수 덤으로 장차 _α_ 값을 도출 추출 타진 산출 연성해 낼 적에 대체 당최 어느 자리 어느 순번 어느 핏줄 서열의 특정 관측치 영혼 조각들을 전격 차출 끄집 활용 사용 이용 연계시켜 써먹어야만(should be used) 할지를 지시 타진 점지 명령 가르키(indicating) 도록 기능하는 단골 슬롯 옵션 좌표 벡터 지시 끈인 `idx` 녀석까지도 고루 죄다 차용 전달 접수 받아먹고 병합 취급(takes as) 도무 처리하는 기능 파장 면모를 발휘한다.

The function then outputs the estimate for _α_ based on the selected observations. 
그리하여 이 함수는 최종 결괏값 도달 반환 처우로서 저 무작위 차출 발탁 요행 픽업 선택 지시받은 녀석 관측치들(selected observations) 인명 부류만을 철저히 알량 기반 근거(based on) 발판 삼아 역산 도출 굴러 파생된 신생 미지 _α_ 적중 수위 추정치 파편 덩어리를 고스란히 밖으로 계산 양도 뱉어 출력 배출 도출(outputs) 반환해 준다.

```python
In [15]: Portfolio = load_data('Portfolio')
         def alpha_func(D, idx):
             cov_ = np.cov(D[['X', 'Y']].loc[idx], rowvar=False)
             return ((cov_[1, 1] - cov_[0, 1]) /
                     (cov_[0, 0] + cov_[1, 1] - 2 * cov_[0, 1]))
```

This function returns an estimate for _α_ based on applying the minimum variance formula (5.7) to the observations indexed by the argument `idx` .
이 함수 객체 기전은 다름 아닌 그저 투입 인자 옵션 `idx` 끈을 타고 지령 지목 지시 호명되어 넘어 호출 전수된 당해 관측치 무리(indexed) 놈들에게만 편파 무자비 집중 맹렬 앞선 그 최소 분산 황금 수식(minimum variance formula) 공식 전력 (5.7) 포화를 전면 전격 가동 헌정 적용 덧씌워 대입 계산(applying) 시킨 것에 전적으로 의존 입각하여 작위 도출 도래해 얻어진 _α_ 기조 파급 예측 추정 척도 분량을 이윽고 기어코 바깥 반환(returns) 토해 돌려 돌출 방출해 주는 기능이다.

For instance, the following command estimates _α_ using all 100 observations. 
일례로서 예시 들자면; 곧장 이어지는 다음 후속 선언 명령어 코드단은 가차 구별 얄짤 일절 제약 제한 축소 그 어떤 가담 감량 조치 빼기 없이, 오롯이 그저 온전 원본 소속 총 100명 관측치 도합 전멸(all 100 observations) 물량 인프라 인구수 전원을 아예 모두 닥치는 몽땅 영끌 풀가동 투여 밀어 다 써먹고(using) 돌려 타진 역산 산출 구축 파생 가늠 도출한 기본 근원 정통 _α_ 추정 가늠치를 거뜬 점쳐준다.

```python
In [16]: alpha_func(Portfolio, range(100))
```

```python
Out[16]: 0.5758
```

Next we randomly select 100 observations from `range(100)` , with replacement.
다음 턴 행보 구도부터는 전폭 달리; 우리는 저 원래 오리지날 `range(100)` 등수 번호 무기고 항아리 심연 구멍 바닥 속살로부터 아주 무작위 기행 요설 무작위 난수 제비뽑기 발탁 행각 작위 모방(randomly select) 질로써 기막힌 징그러운 강제 무한 반복 동일 복원 모조 재탕 야매 반복 꼼수 _복원 추출(with replacement)_ 방식 법도하에 거듭 어김없이 꾸역 억지 100명 관측치 치수 머릿수 물량을 우겨 담아 전격 색출 모집 수합 모조 건져 뽑아 조립해 볼 것이다.

This is equivalent to constructing a new bootstrap data set and recomputing $\hat{\alpha}$ based on the new data set. 
이 얄팍 작위 모방 행동 파장 작태가 사실상 미치고 기괴 놀랍게도 다름 아닌 완전히 파격 독단 새로운 신생 돌연 인공 복제 부트스트랩 데이터 변이 모조 항아리 팩 그릇(new bootstrap data set) 세트판을 전격 가상 신규 허가 조립 창립 구축 직조(constructing) 조달 양산 축조해 내는 것과 하등 완벽 절대 동치 똑같 완전 결부 동일 등가 등치 부합 동등(equivalent to) 똑같은 파급 효력 위상을 띄며 발휘해 주는데; 이는 곧 그리 떡하니 쟁취 파생 요설 발현된 이 가망 복사 짝퉁 신규 데이터판 신생 세력을 가당 새로운 기본 전초 베이스 발판 알량 근거 기저 뿌리로 전향 삼아놓고(based on) 또다시 그 위에다 고스란히 재차 재계산 작위 재산출 재구동 재가동(recomputing) 연산 폭격 루프를 다시 걸고 덧대 조작 돌려 무어 새 파편 쪼가리 치수 $\hat{\alpha}$ 마커 추정 족집게 스탯 점표 위력을 야무 다시 전격 재수확 건져내 획득 가담 도출해 내는 신비 속셈 전력인 셈이다.

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
* [문서로 이동하기](./5_3_3_1_out19_0.0912/)

수 천번 반복 복원수집된 궤적에서 추출된 획득 추정치의 단단한 신뢰 오차 마진을 눈과 코드로 직접 관찰합니다.

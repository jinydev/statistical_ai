---
layout: default
title: "trans1"
---

# _Conceptual_ 
# _개념 문제_

1. Using basic statistical properties of the variance, as well as singlevariable calculus, derive (5.6). In other words, prove that _α_ given by (5.6) does indeed minimize Var( _αX_ + (1 _− α_ ) _Y_ ). 
1. 기본 통계학적 분산(variance) 특성 도구들과 더불어 단일 변수 미적분학(single-variable calculus) 원리를 활용하여, 앞선 공식 (5.6)을 직접 도출 유도(derive) 정립해 보시오. 다른 말로 풀어 쓰자면, (5.6) 수식에 의해 점지 부여된 그 _α_ 지수 값이 참으로 진실로 참되게 Var( _αX_ + (1 _− α_ ) _Y_ ) 함수 파장 폭을 최솟값으로 찍어 내림(minimize) 을 전격 증명 논증 입증(prove) 해 보이시오.

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of _n_ observations. 
2. 바야흐로 지금부터 우리는 특정 임의 관측치 개체 하나가 장차 부트스트랩 파생 모조 샘플 덩이 내부에 속해 편입될 확률값을 전면 도출 전개(derive) 해 볼 터이다. 만약 우리가 총 _n_ 명의 관측치 개체 머릿수 집단으로부터 일개 부트스트랩 인공 모조 샘플 뭉치를 전격 획득 쟁취 도달해 내는(obtain) 상황을 가정 추산 타진(Suppose) 상상해 보자.

   - (a) What is the probability that the first bootstrap observation is _not_ the _j_ th observation from the original sample? Justify your answer. 
   - (a) 당해 조달된 그 부트스트랩 샘플표 상의 맨 첫 번째 첫 순번 배열 관측치가, 정작 원본 샘플표 상의 제 _j_ 번째 관측치 출신 녀석이 철저히 아닐( _not_ ) 그 빗나갈 확률값은 며칠 도달 될 것인가? 귀하의 도출 답변을 합당 명명백백 정당화 증명 논증(Justify) 해 보이시오.

   - (b) What is the probability that the second bootstrap observation is _not_ the _j_ th observation from the original sample? 
   - (b) 그렇다면 똑같은 논리로 이어져 두 번째 순번 부트스트랩 발 관측치가 저 원본 오리지널 상의 제 _j_ 번째 출신 관측치 녀석이 아닐( _not_ ) 부재 파단 확률은 또 며칠 될 것인가?

   - (c) Argue that the probability that the _j_ th observation is _not_ in the bootstrap sample is (1 _−_ 1 _/n_ ) _^n_ . 
   - (c) 종래 결과로 당해 저 오리지널 제 _j_ 번째 관측치 녀석이 그 신생 부트스트랩 샘플 덩어리 내에 아예 단 1번도 편입 포함( _not_ in) 되지 못해 누락될 비참 확률 치수가 결국 $(1 − 1 /n)^n$ 궤적에 수렴해 봉착함 사실을 전면 논증 주장 관철(Argue) 해 내시오.

   - (d) When _n_ = 5, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (d) 만약 모수 총량 머릿수가 $n = 5$ 마리로 국한되었을 적에, 당해 제 $j$ 번째 관측치가 저 모조 부트스트랩 샘플 바구니 속에 기어코 편입 포함 생존해 들어갈 도래 확률(probability) 은 대체 명 확증 타진되는가?

   - (e) When _n_ = 100, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (e) 만약 모수 $n = 100$ 인원 규모일 시엔, 저 제 $j$ 번 관측치가 신생 부트스트랩 샘플표에 무단 편입 생존해 탑승해 있을 확률 지수는 명 확증되는가?

   - (f) When _n_ = 10 _,_ 000, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (f) 더 나아가 확충 $n = 10,000$ 거대 규모일 때, 해당 $j$ 번 관측치가 부트스트랩 샘플 내에 구비 존재해 기거할 안착 확률은 명 확증 도달되는가?

   - (g) Create a plot that displays, for each integer value of _n_ from 1 to 100 _,_ 000, the probability that the _j_ th observation is in the bootstrap sample. Comment on what you observe. 
   - (g) 당면 정수 볼륨 모수치 $n$ 값의 범위를 저 밑바닥 자락 1부터 아득 꼭대기 100,000 지점까지 매 정수 스텝마다 이동해 타진 적용해 감에 따라서, 당해 제 $j$ 번째 관측치가 무사히 부트스트랩 샘플 항아리 내에 탑승 존재할 확률 폭 널뛰기 진폭 궤적 양상을 고스란 전시 표출 도해(displays) 해 보여 주는 시각 도안 플롯 차트(plot) 를 전격 직조 구축 창출해(Create) 내시오. 이 도식표를 지켜보며 스스로 면면 직시 관전 캐치 포착 파악해 낸(observe) 속내 바를 논평 서술 기재(Comment) 하시오.

   - (h) We will now investigate numerically the probability that a bootstrap sample of size _n_ = 100 contains the _j_ th observation.
   - (h) 바야흐로 이제 우리는 실전 체감 차원으로 무려 사이즈 규모 $n = 100$ 덩치를 띤 부트스트랩 인공 모조 샘플표 묶음이 과연 저 어여쁜 제 $j$ 번째 관측치 타깃을 담보 머금고 단 한 번이라도 무사 채용 포함 보유(contains) 쟁취해 줄 그 희귀 확률 궤적 척도를 보다 더 치밀 전면적 수치 기반 전산 해석(numerically) 을 이수 동원해 집중 파고들어 수사 조사 타진 탐구(investigate) 해 볼 방침 계획이다.

Here _j_ = 4.
여기 작금 이 무대 세팅에선 당사 타깃 좌표를 $j = 4$ 번 타자로 상정 투표해 고정 묶어두자.

We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()` .
우선 극 초반 전면 공세로서 우리는 훗날 이어질 뺑뺑이 후속 수순 단계(subsequently) 턴마다 새로운 데이터 결괏값들로 파단 덧씌워 파괴 잠식 갱신(overwritten) 기록되어 전율될 깡통 빈 장부 껍데기 배열 선언 객체 `store` 하나를 치트 `np.empty()` 함수 조작 동원을 알뜰 기용해 냅다 선도 생성 창조 직조(create) 구비해 채비한다. 

We then repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample. 
그런 연후 뒤이어 곧장 편법 무식 막가파 반복 부트스트랩 파생 조각 모조 샘플 항아리들을 무한 반복 돌려 양산 창출해(repeatedly create) 내면서; 극히 매 국면 턴(each time) 파장 국면마다 우리가 관전 찍어둔 저 4번째 (프로그램상 5번째 위치, fifth observation) 관측치가 떡하니 그 파단 부트스트랩 가짜 샘플 부대 대열 사이에 안전무사 합류 생존 도달 포함 존재 포진(contained in) 했는지 부재 미수됐는지 이단 여부를 고루 죄다 기입 적시 채록 저장 기록(record) 에 올린다.

```python
rng = np.random.default_rng(10)
store = np.empty(10000)
for i in range(10000):
    store[i] = np.sum(rng.choice(100, replace=True) == 4) > 0
np.mean(store)
```

Comment on the results obtained. 
도출되어 뽑혀 타결 얻어진 결괏값 궤적 면면 결과 수치(results obtained) 장부를 두고 본질 논평 품평 지시 논단(Comment on) 하시오.

3. We now review _k_ -fold cross-validation. 
3. 자 거듭 이제 우린 저 지옥 불맛 뺑뺑이 $k$-폴드 교차 검증 국면을 향해 거듭 복습 타파 재조명 진단 고찰(review) 을 뻗쳐 타진한다.

   - (a) Explain how _k_ -fold cross-validation is implemented. 
   - (a) 이른바 저 $k$-폴드 교차 검증 메커니즘 엔진이 실상 어떻게 절차 동원 수립 직조 구축 적용 구현 발현(implemented) 전파되는지 그 속내를 해설 설파 기술(Explain) 해 내시오.

   - (b) What are the advantages and disadvantages of _k_ -fold crossvalidation relative to: 
   - (b) 과연 저 당해 $k$-폴드 교차 검증 전술 기지가 다음과 같은 이들 이하 파단 기조 상대 적군 진영 구도 방식들(relative to) 측면과 대비 견주어 맞붙어 비교 대조해 치러봤을 치에 지니고 확보 보장 야기 잃는 그 순기능 양면 이점 강점 장점들(advantages) 및 단점 취약 결점 부작용 고립 단점들(disadvantages) 여건은 필히 무엇이라 칭송 가늠되는가:

      - i. The validation set approach? 
      - i. 가장 고조 구식 원시 기조 검증 세트 접근법(validation set approach)? 

      - ii. LOOCV? 
      - ii. 미친 무식 극단 파장 삽질 루핑 기조 리브-원-아웃 교차 검증(LOOCV)? 

4. Suppose that we use some statistical learning method to make a prediction for the response _Y_ for a particular value of the predictor _X_ .
4. 상상 타진 만일 가령(Suppose) 우리 인류가 여느 모종의 일개 특수 통계 머신 학습 도구(statistical learning method) 기계 방식을 차용 이입 투하 끌어다 써서; 모종 특정 한정 제약 결박 잣대 조각의 설명 변수 스펙 $X$ 파단 가측 수치값 옵션 인자를 알뜰 빌미 발판 볼모 미립 처우 삼아 목표 종속 겨냥 타겟치 $Y$ 궤적의 빗발 운명 궤도 향방을 가산 짐작 예측 점쳐(make a prediction for) 내어보고자 갈망 투신한다고 상정 투항해 보자.

Carefully describe how we might estimate the standard deviation of our prediction. 
이 궤적 안마당 속에서 우리 측 진영이 필연 거푸 도출 찍어 조달 내어 뽑힌 그 최종 적중 잉태 예측치 궤도의 알량 오들오들 요동치는 분파 진폭 표준 편차(standard deviation) 위상 스펙 두께를 대체 여하 어떤 편법 우회 기치 묘책 방안으로 타결 찍어 들이 추정 능수 가늠(estimate) 역산해 조달해 낼 수 가히 가망 있을런지 그 돌파 수단을 몹시 치밀 깊게 찬찬 심도 주의 세심(Carefully) 가다듬어 상세 고증 묘사 기술 타진(describe) 해 보시오.

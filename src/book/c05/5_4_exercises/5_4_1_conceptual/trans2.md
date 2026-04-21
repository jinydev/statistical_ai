---
layout: default
title: "trans2"
---

# Conceptual
# 머리 쥐어뜯는 개념 훈련장 (개념 문제)

1. Using basic statistical properties of the variance, as well as singlevariable calculus, derive (5.6). In other words, prove that $\alpha$ given by (5.6) does indeed minimize $\text{Var}(\alpha X + (1 - \alpha) Y)$. 
1. 통계학 짬바와 대학교 1학년 때 배운 1변수 미적분(singlevariable calculus) 공력을 탈탈 털어서, 아까 그 전설의 투자 황금비율 공식 (5.6)의 뼈대를 직접 유도(derive) 해보세요. 쉽게 말해(In other words), (5.6) 공식에서 튀어나온 $\alpha$ 란 괴물의 정체가, 정말로 "내 투자금 쪼개기 변동폭 $\text{Var}(\alpha X + (1 - \alpha) Y)$" 을 가장 쪼그라들게(최소화 minimize) 해주는 찐 마스터키가 맞는지 수학적으로 팩폭 증명(prove) 해보라는 뜻입니다.

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of $n$ observations. 
2. 부트스트랩 돌릴 때, "재수 옴 붙어서 내 번호가 한 번도 안 뽑힐 확률(probability)" 에 대해 수학적 확률론으로 각 잡고 털어보겠습니다. 우리가 총 병력 $n$ 마리로 이뤄진 원본 데이터 부대에서 딱 한 부대의 부트스트랩 용병 샘플들을 추첨(obtain) 한다고 뇌피셜 가정을 돌려몹시다(Suppose). 

   - (a) What is the probability that the first bootstrap observation is _not_ the $j$th observation from the original sample? Justify your answer. 
   - (a) 추첨통에 손을 넣어 첫 번째 용병(first bootstrap observation) 을 딱 뽑았는데, 앗뿔싸! 이놈이 내 타겟 $j$번 병사가 **아닐(not)** 확률은 얼마일까요? 정답을 외치고 왜 그런지 입 털어보세요(Justify).

   - (b) What is the probability that the second bootstrap observation is _not_ the $j$th observation from the original sample? 
   - (b) 그럼 두 번째 추첨에서 뽑힌 용병마저 내 타겟 $j$번 녀석을 아슬아슬하게 **피해 갈(not)** 빗나감 확률은 또 어떻게 바뀔까요?

   - (c) Argue that the probability that the $j$th observation is _not_ in the bootstrap sample is $(1 - 1/n)^n$. 
   - (c) 추첨이 다 끝난 뒤 부트스트랩 명단표 전체를 훑어봐도 그 타겟 $j$번 병사가 **단 한 놈도 안 끼어 있을(not in)** 멸망 확률이, 수학적으로 절묘하게 $(1 - 1/n)^n$ 공식 모델로 굳어진다는 썰을 논리적으로 반박 불가하게 입증(Argue) 해보세요.

   - (d) When $n = 5$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (d) 자, 병력 수가 꼴랑 5마리($n=5$) 인 시골 부대라고 칩시다. 뺑뺑이 돌렸을 때 내 타겟 $j$번 병사가 부트스트랩 용병 명단에 무사히 턱걸이 **합류(in)** 해 있을 확률은 몆 %?

   - (e) When $n = 100$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (e) 스케일을 키워 병력이 100마리($n=100$) 라면? 타겟 $j$번 녀석이 용병 명단에 **들어가 있을(in)** 생존 확률은 얼마일까요?

   - (f) When $n = 10,000$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (f) 병력이 1만 마리 군단($n=10,000$) 급으로 뻥튀기 된다면? 내 타겟 $j$번 병사가 최소 명단 한 칸이라도 차지할 **생존(in)** 티켓 확률률은 어디로 수렴할까요?

   - (g) Create a plot that displays, for each integer value of $n$ from 1 to 100,000, the probability that the $j$th observation is in the bootstrap sample. Comment on what you observe. 
   - (g) 코딩 타임! 병력 $n$ 숫자를 1명부터 십만 명 대군(1 to 100,000) 까지 미친 듯이 늘려가면서, 타겟 $j$번 병사가 명단에 포섭될 확률이 어떻게 널뛰다가 안착하는지 추적하는 멋진 시각화 차트 곡선(plot) 을 하나 뽑아주세요(Create). 그리고 차트를 보고 느낀 바(what you observe) 를 찐따처럼 속으로 삼키지 말고 거침없이 평론(Comment) 해보세요.

   - (h) We will now investigate numerically the probability that a bootstrap sample of size $n = 100$ contains the $j$th observation. Here $j = 4$. We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()`. We then repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample. 
   - (h) 이번엔 $n=100$ 짜리 훈련소에서 부트스트랩 뺑뺑이를 돌렸을 때, 내 타겟 병사가 명단에 스폰(contains) 될 진짜 체감 확률을 파이썬 숫자의 힘(numerically) 으로 탈탈 심문(investigate) 해봅시다. 타겟은 불길한 $j=4$ (5번째 녀석) 로 잡죠(Here). 맨 처음, `np.empty()` 공구로 나중에 1만 번의 뺑뺑이 전적 스코어 기록을 덮어써서(overwritten) 기록할 빈 껍데기 전광판 배열 `store` 를 하나 세팅(create) 합니다. 그리고 뺑뺑이 매크로를 돌리면서 부트스트랩 훈련소에 불쌍한 5번째 녀석이 스폰됐는지 낙오됐는지 생사 여부(whether or not) 를 매번 끈질기게 기입(record) 하는 겁니다.

```python
rng = np.random.default_rng(10)
store = np.empty(10000)
for i in range(10000):
    store[i] = np.sum(rng.choice(100, replace=True) == 4) > 0
np.mean(store)
```

Comment on the results obtained. 
기계가 뱉어낸 이 참혹한(?) 생난리 증명 투사 산출 확률 스코어 결괏값(the results) 을 보고, 입을 벌린 채 코멘트 평가 타격(Comment on) 을 한 줄 날려주세요.

3. We now review $k$-fold cross-validation. 
3. 자 분위기 돌려서 우리의 영원한 친구, $k$-폴드 교차 검증에 대해 썰(review) 을 풀어보시죠.

   - (a) Explain how $k$-fold cross-validation is implemented. 
   - (a) $k$-폴드 검증 이 조각내기 작전 장치가, 컴파일 환경 실전 내부에서 도대체 어떤 기믹 기절 순서(how) 로 칼질되고 가동 조립 세팅(implemented) 되는 건지 그 스토리를 낱낱이 썰로 풀어 설명(Explain) 하세요.

   - (b) What are the advantages and disadvantages of $k$-fold crossvalidation relative to: 
   - (b) 아래 후보들과 나란히 세워놓고 맞짱 대결(relative to) 비교를 떴을 때, 우리 $k$-폴드 기술의 갓갓 장점(advantages) 과 개망 핵폐기물급 약점 단점(disadvantages) 은 부위별로 각각 무엇(What are) 일까요?

      - i. The validation set approach? 
      - (i) 허접한 오리지널 구닥다리 방식 (단칼 검증 방식, Validation set approach) 과 떴을 땐 뭐가 좋고 구립니까?

      - ii. LOOCV? 
      - (ii) 극악의 노가다 머신 방식 (LOOCV 체제) 랑 피터지게 싸울 땐 또 어떤 약점과 강점이 드러나나요?

4. Suppose that we use some statistical learning method to make a prediction for the response $Y$ for a particular value of the predictor $X$. Carefully describe how we might estimate the standard deviation of our prediction. 
4. 우리가 뭔가 뽕이 차오르는 최첨단 통계 로봇(statistical learning method) 을 하나 임대해 왔다고 상상해 봅시다(Suppose). 이 로봇을 갈궈서, 특정 관측 스펙 $X$ 를 꽂아 넣었을 때 뱉어낼 내일 주가 타겟 $Y$ 의 예언 견적서 찌라시(prediction) 를 만들었다고 치는 겁니다(to make). 자 집중! 로봇이 뱉어낸 이 "예언 찌라시치" 자체가 띠고 있는 불안불안한 '널뛰기 한계 변동 오차폭 편위(standard deviation)' 요동 게이지를, 과연 우리는 어떠한 마법 코딩 작전 조작 기술 루트 기조(how) 를 타파해 견적 환산 검측(estimate) 해낼 수 있을까요? 그 비밀 방법론을 은밀하고 고도 세심하게(Carefully) 적발 투사 서술 전개 묘사 브리핑 기술 입증 나열(describe) 해 보십시오.

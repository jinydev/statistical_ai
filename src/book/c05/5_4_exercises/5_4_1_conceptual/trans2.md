---
layout: default
title: "trans2"
---

# _Conceptual_ 
# _개념 퀘스트: 두뇌 풀가동_

1. Using basic statistical properties of the variance, as well as singlevariable calculus, derive (5.6). In other words, prove that _α_ given by (5.6) does indeed minimize Var( _αX_ + (1 _− α_ ) _Y_ ). 
1. 대학 1학년 때 배운 '단일 변수 미적분학' 나부랭이랑 통계학 기초 분산(variance) 공식들을 싹 다 긁어모아서, 옛날에 배웠던 그 포트폴리오 (5.6) 공식을 직접 빈 종이에 유도(derive) 해 보십쇼. 돌려 말해서, 저 수식에서 튀어나온 $α$ 혼종 템트리 황금 비율이, 진짜로 내 통장 잔고의 미친 요동(Var) 폭 $\text{Var}( αX + (1 − α) Y )$ 을 가장 바닥으로 짓눌러 갈아버리는(minimize) 최강 방어막 방패가 맞긴 한 건지! 손으로 직접 수식을 써가며 팩트 논증(prove) 을 갈겨 보란 소립니다.

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of _n_ observations. 
2. 자, 부트스트랩 사기 뺑뺑이를 돌릴 때, "과연 내가 저 가짜 복제본 무더기 속으로 다시 징집돼 뽑혀 들어갈 확률이 몇이나 될까?" 하는 생존 확률의 극한을 파헤쳐(derive) 봅시다. 인구수 $n$ 명인 마을에서 부트스트랩 인공 명부를 딱 한 장 찢어 뽑아 냈다고 가정해 보죠(Suppose).

   - (a) What is the probability that the first bootstrap observation is _not_ the _j_ th observation from the original sample? Justify your answer. 
   - (a) 그 새로 만든 짝퉁 장부의 '맨 첫 번째 빈칸'에, 하필 원본 마을의 $j$ 번째 주민이 운 나쁘게 **'안'** 뽑히고( _not_ ) 미끄러질 확률은 몇 %일까요? 당신의 기적의 수학 논리를 대보십쇼(Justify).

   - (b) What is the probability that the second bootstrap observation is _not_ the _j_ th observation from the original sample? 
   - (b) 그럼 또 두 번째 빈칸을 채울 때, 저 불쌍한 $j$ 번째 주민이 연달아 **'안'** 뽑히고( _not_ ) 벤치에 머무를 확률은? (힌트: 부트스트랩은 복원 뺑뺑이라 항아리가 안 비워집니다!)

   - (c) Argue that the probability that the _j_ th observation is _not_ in the bootstrap sample is (1 _−_ 1 _/n_ ) _^n_ . 
   - (c) 결국 $n$ 번 다 뽑을 동안 그 $j$ 번째 주민이 끝끝내 단 한 번도 뽑히지 못하고 왕따 당할( _not_ in) 지독히도 재수 없는 최종 확률이 얄짤없이 $(1 − 1 /n)^n$ 가 된다는 것을 박박 우겨서 증명(Argue) 해 내십쇼.

   - (d) When _n_ = 5, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (d) 마을 인구가 고작 5명($n=5$) 이면, 쟤가 최소 한 번이라도 부트스트랩 장부에 무사히 탑승해 생존할 턱걸이 확률은 몇 나옵니까?

   - (e) When _n_ = 100, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (e) 인구가 100명($n=100$) 으로 좀 바글대면, 쟤가 가짜 짝퉁 장부에 살아남을 확률은?

   - (f) When _n_ = 10 _,_ 000, what is the probability that the _j_ th observation is in the bootstrap sample? 
   - (f) 인구가 확 늘어서 1만 명($n=10,000$) 의 대도시가 되면, 쟤의 생존 확률은 어디로 수렴합니까?

   - (g) Create a plot that displays, for each integer value of _n_ from 1 to 100 _,_ 000, the probability that the _j_ th observation is in the bootstrap sample. Comment on what you observe. 
   - (g) 인구수 $n$ 볼륨을 1명부터 무려 10만 명까지 조금씩 올려가며, 그때마다 계산되는 이 왕따 생존 확률 궤적 곡선을 예쁜 그래프(plot) 로 시각화해서 찍어 눌러보십쇼(Create). 그리고 그 그래프가 어디 묘한 숫자로 수렴해 가는 꼴을 자기 눈으로 똑똑히 관전(observe) 하고 감상평을 한 줄 달아보십쇼(Comment).

   - (h) We will now investigate numerically the probability that a bootstrap sample of size _n_ = 100 contains the _j_ th observation.
   - (h) 수학 공식만 끄적거리니 감이 안 오죠? 이제 파이썬 노가다 컴퓨터의 힘을 빌려 무식한 전산 수치 연산(numerically) 으로, 저 "100명($n=100$) 마을에서 짝퉁 장부 만들 때 내가 뽑힐 확률" 이 진짜 그 숫자로 수렴하는지 강제로 압수수색(investigate) 을 때려버리겠습니다.

Here _j_ = 4.
우리 타깃 실험 쥐는 4번 등번호(파이썬으론 5번째 놈) 로 고정합시다 ($j = 4$).

We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()` .
우선 파이썬의 허공 창조 스킬인 `np.empty()` 를 써서, 앞으로 매크로 돌릴 때마다 나온 결괏값 빈 조각들을 쓰레기처럼 덧씌워 담아댈(overwritten) 거대한 빈 상자 깡통 배열 `store` 를 하나 세워둡니다(create).

We then repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample. 
그러곤 10,000번 반복 뺑이 매크로를 돌리면서, 그 10,000개의 부트스트랩 평행우주 장부 속마다 저 불쌍한 5번째 관측치 놈팽이가 단 한 번이라도 살아서 기어들어 왔는지(contained in) 아님 왕따 당했는지만을 냉혹하게 추적 채록 기록(record) 해댑니다.

```python
rng = np.random.default_rng(10)
store = np.empty(10000)
for i in range(10000):
    store[i] = np.sum(rng.choice(100, replace=True) == 4) > 0
np.mean(store)
```

Comment on the results obtained. 
터미널에서 뱉어준 궤적 결괏값(results obtained) 을 보고, 아까 수학으로 풀던 거랑 똑 떨어지는지 충격 먹고 논평(Comment on) 해 보십쇼.

3. We now review _k_ -fold cross-validation. 
3. 자 거듭 이제 징글징글한 $k$-폴드 교차 검증 퀘스트를 한번 싹 정리 리뷰(review) 때려봅시다.

   - (a) Explain how _k_ -fold cross-validation is implemented. 
   - (a) 친구를 붙잡고 설명한다 치고, 저 $k$-폴드 교차 검증의 찢고 돌리는 그 난도질 뺑뺑이 메커니즘 엔진이 어떻게 실제로 굴러가는지(implemented) 썰을 풀어보십쇼(Explain).

   - (b) What are the advantages and disadvantages of _k_ -fold crossvalidation relative to: 
   - (b) 아래에 나오는 오합지졸 병신 방법들이랑(relative to) 일대일 막고라를 떴을 때, 우리의 짱짱맨 $k$-폴드가 가지는 사기적인 템빨 강점(advantages) 이나, 아님 의외로 발목 잡히는 구린 단점(disadvantages) 이 뭐가 있는지 까발려 보십쇼:

      - i. The validation set approach? 
      - i. 가성비 최고 멍청이 '검증 세트 반반 무 많이 구닥다리 방식(validation set approach)' 이랑 비교하면요? 

      - ii. LOOCV? 
      - ii. 내 컴퓨터 램을 비명 지르게 하는 미친 $n$ 번 루핑의 사이코패스 병기, '리브-원-아웃 뺑뺑이 방식(LOOCV)' 이랑 비교하면요? 

4. Suppose that we use some statistical learning method to make a prediction for the response _Y_ for a particular value of the predictor _X_ .
4. 상상해 보십쇼. 우리가 어찌어찌 쥐어짜 낸 어떤 기똥찬 통계 머신 템트리(기계 모델) 를 써서; 입력 옵션 $X$ 에 뭔가 그럴듯한 수치 총알 하나를 턱 넣고 타겟 $Y$ 의 궤도 결점 점수를 기막히게 맞혀보는(make a prediction) 도박을 건다고 칩시다(Suppose).

Carefully describe how we might estimate the standard deviation of our prediction. 
근데 여기서 불안감 엄습! "내가 쏜 예측 총알이 얼마나 미친 듯이 오르락내리락 옆으로 조준경이 튈까?" 하는 그 공포의 요동 폭, '표준 편차(standard deviation)' 궤적을 대체 어떤 꼼수 편법(부트스트랩 같은 구제 구명줄) 으로 파생 발굴 가늠 타진(estimate) 해 낼 수 있을까요? 아주 디테일하고 조심스럽게(Carefully) 작전 계획을 짜서 브리핑(describe) 해 보십쇼.

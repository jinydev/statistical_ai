---
layout: default
title: "trans2"
---

# **`Out[17]:`** `0.6074` 

This process can be generalized to create a simple function `boot_SE()` for computing the bootstrap standard error for arbitrary functions that take only a data frame as an argument. 
방금 했던 그 '야매 복제 뽑기' 짓거리를 조금 더 세련되게 다듬어서 파이썬의 궁극 치트키 만능 헬퍼 함수, `boot_SE()` 라는 녀석으로 찍어내보죠. 이 기계에다가 "어떤 데이터 장부로 돌릴지만 말해줘!" 하고 던져주면, 그 어떤 복잡한 계산 함수(arbitrary functions) 라도 다 게걸스럽게 집어삼켜서 부트스트랩 사기 공정을 돌린 뒤 기어이 '표준 오차'를 토해냅니다.

```python
In [18]: def boot_SE(func,
                     D,
                     n=None,
                     B=1000,
                     seed=0):
             rng = np.random.default_rng(seed)
             first_, second_ = 0, 0
             n = n or D.shape[0]
             for _ in range(B):
                 idx = rng.choice(D.index,
                                  n,
                                  replace=True)
                 value = func(D, idx)
                 first_ += value
                 second_ += value**2
             return np.sqrt(second_ / B - (first_ / B)**2)
```

Notice the use of `_` as a loop variable in `for _ in range(B)` .
자, 저 코드 조각에서 `for _ in range(B)` 부분을 유심히 보세요. 원래 `for i` 라고 많이들 쓰는데 갑자기 밑줄 짝! `_` 기호가 떡하니 박혀있죠?

This is often used if the value of the counter is unimportant and simply makes sure the loop is executed `B` times. 
이 얄미운 짓은 코더들 사이의 암묵적 국룰입니다. "야, 내가 지금 도대체 몇 번째 바퀴 돌고 있는지 그 숫자(카운터) 따윈 1도 안 궁금하니까, 넌 그냥 입 닥치고 미친 듯이 톱니바퀴나 `B` 번 채워서 줫나게 마구 돌려!" 라고 컴퓨터에 강제 채찍질(makes sure) 을 할 때 쓰는 간지나는 무시 표시(`_`) 작법입니다.

Let’s use our function to evaluate the accuracy of our estimate of _α_ using _B_ = 1 _,_ 000 bootstrap replications. 
그럼, 우리가 방금 고안한 이 수제 공장 매크로를 당장 끌고 와서 테스트해 봅시다. 통 크게 물량 공세(B=1,000)! 무려 1,000번의 복제 평행우주 항아리를 연성해 찍어내며 우리가 그어둔 $α$ 수치가 과연 얼마나 정확히 들어맞았는지, 오들오들 떨리는 방어 타율(오차율) 을 가차 없이 진단 박살 내 볼 차례입니다.

```python
In [19]: alpha_SE = boot_SE(alpha_func,
                            Portfolio,
                            B=1000,
                            seed=0)
         alpha_SE
```

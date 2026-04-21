---
layout: default
title: "trans1"
---

# **`Out[17]:`** `0.6074` 

This process can be generalized to create a simple function `boot_SE()` for computing the bootstrap standard error for arbitrary functions that take only a data frame as an argument. 
방금의 이련 기조 메커니즘 조작 과정을 조금 더 보편 광범위하게 넓혀 일반화(generalized) 시키게 되면, 그저 유일 입력 인자로써 오롯이 데이터프레임 구조만을 단일 병합 채택해 넘겨받는 그 어떠한 임의 형태의 다목적 함수들(arbitrary functions) 을 상대로도, 단방 거뜬히 부트스트랩 파생 예측 표준 오차율을 산술 조명 연산해 내 줄(computing) 수 있는 심플 다목적 조작 함수 `boot_SE()` 패키지를 거뜬 창조 생성 고안해 낼 수 있다.

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
저 상단 코드 조각 중 빈번 구동되는 `for _ in range(B)` 선언문 구절 블록 내에서 징검다리 루프 변수 매개체로서 채택 기용 사용된 밑줄 띠 표기 `_` 기호 문자(use of `_`) 의 쓰임새를 유심히 인지 주목해 보자.

This is often used if the value of the counter is unimportant and simply makes sure the loop is executed `B` times. 
이는 사실상 그 턴 횟수를 세는 카운터 변수에 매번 할당 부여되는 알맹이 고유 숫잣값 자체는 우리에게 당최 하등 중요 필수적이지가 아니하며(unimportant), 오로지 단지 그저 기계적으로 저 루프 수레바퀴 블록만이 오직 딱 할당 수효인 `B` 횟수 분량만큼 성실 온전히 뺑뺑이 전개 다회전 구동 실행되도록(executed) 철저 강제 확실히 제어 조장(makes sure) 할 목적일 적에 통상 파이썬에서 관습적으로 번번 사용 기용되는 작법이다.

Let’s use our function to evaluate the accuracy of our estimate of _α_ using _B_ = 1 _,_ 000 bootstrap replications. 
그럼 마침 이윽고 당면 완성된 우리의 자체 수제 함수를 당장 냅다 끌어다 기용 써먹음으로써, 할당 물량 $B = 1,000$ 회전 횟수 규모에 육박 달하는 이 부트스트랩 인공 모조 복제수(replications) 를 투하 총동원 연성해 낸 채, 우리가 일군 추산 도출 _α_ 척도 지수의 그 본질 적중 정확성 마진율을 단번 판별 평가 타진해(evaluate the accuracy) 보도록 하자.

```python
In [19]: alpha_SE = boot_SE(alpha_func,
                            Portfolio,
                            B=1000,
                            seed=0)
         alpha_SE
```

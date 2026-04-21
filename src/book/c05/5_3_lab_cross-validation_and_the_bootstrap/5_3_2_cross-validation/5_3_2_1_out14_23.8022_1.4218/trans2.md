---
layout: default
title: "trans2"
---

# **`Out[14]:`** `(23.8022, 1.4218)` 

Note that this standard deviation is not a valid estimate of the sampling variability of the mean test score or the individual scores, since the randomly-selected training samples overlap and hence introduce correlations.
다만 잠깐 여기서 김칫국 너무 마시진 말죠. 결괏값으로 툭 튀어나온 저 '표준 편차(1.4218)' 점수 쪼가리를 당장 "우왕, 내 에러 점수의 오리지널 진짜 변동성이다!" 라고 순진하게 털썩 믿어버리면 안 됩니다. 왜냐고요? 아까 우리가 반복문 매크로를 돌릴 때 무작위로 멱살 잡아 끌고 온 저 훈련용 데이터 군단들이, 사실상 이전 턴에서 끌려왔던 애들이랑 이리저리 막 서로 지저분하게 겹치고 유착(overlap) 되어버렸거든요. 애초에 병력들이 자기들끼리 섞이고 '상관성(오르거나 내리는 패턴의 동조, correlations)' 에 오염되었는데 어찌 그 오차율이 순백의 티 없는 진짜 타율(valid estimate) 이라고 맹신할 수 있겠습니까?

But it does give an idea of the Monte Carlo variation incurred by picking different random folds. 
그래도 긍정 회로를 한 줌 돌려보자면, 비록 저 점수가 조금 오염되긴 했더라도 최소한 "우리가 눈먼 장님처럼 손을 뻗어 매번 다른 포로수용소 폴드(folds) 그룹들을 닥치는 대로 잡아채(picking) 뺑뺑이를 돌릴 때마다 대체 얼마나 재수 없게 성적이 막 널뛸 수 있는가?" 라는 그 도박성 깊은 '몬테카를로 변동성(Monte Carlo variation)' 징크스 파장의 살벌한 위력만큼은, 최소한 얼얼하게 체감해 볼 뒷목 서늘한 영감 힌트(does give an idea) 로 삼기엔 무척 충분하고도 남습니다.

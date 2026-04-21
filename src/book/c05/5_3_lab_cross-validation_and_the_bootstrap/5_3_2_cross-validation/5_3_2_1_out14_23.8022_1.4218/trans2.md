---
layout: default
title: "trans2"
---

# `Out[14]:` `(23.8022, 1.4218)`

Note that this standard deviation is not a valid estimate of the sampling variability of the mean test score or the individual scores, since the randomly-selected training samples overlap and hence introduce correlations. But it does give an idea of the Monte Carlo variation incurred by picking different random folds. 
자 잠깐 주의할 점! 방금 뿜어낸 이 1.42 란 편차율 점수를 진짜 전체 학생들의 "평균 타율 오차" 랍시고 100% 맹신하면 안 됩니다(not a valid estimate). 곰곰이 생각해 보세요. 우리가 아무리 무작위로 훈련 멤버를 찢는다 한들, 10-폴드 안에서 훈련생 명단은 알게 모르게 서로 중복 출전(overlap) 이 발생하고 자기들끼리 컨닝(상관관계 correlations) 하는 파벌 변수가 생기거든요. 하지만 이 수치는 룰렛 판(different random folds) 이 매번 다르게 돌 때마다 운빨로 인해 성적이 얼마나 덜컹거리는지, 그 이른바 '몬테카를로 폭주 변동(Monte Carlo variation)' 특성을 캐치하는 데에는 확실히 꿀팁 같은 통찰력을 하사해 줍니다.

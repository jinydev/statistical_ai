---
layout: default
title: "trans2"
---

# **`Out[30]:`** `array([134214.0])`

The test $\text{MSE}$ is 1.342e+05. Note that if we had instead simply fit a model with just an intercept, we would have predicted each test observation using the mean of the training observations. We can get the same result by fitting a ridge regression model with a _very_ large value of $\lambda$ . Note that `1e10` means $10^{10}$ .
가동 결과 모델이 산출해 뱉어낸 진단 테스트 오차율 평가 척도인 $\text{MSE}$ 수치는 1.342e+05(대략 134,214 규모) 수준으로 관측 파악됩니다. 여기서 흥미롭게 눈여겨볼 통계적 비교 대조점이 하나 있습니다. 만약 우리가 단 하나의 변수 스펙도 추가하지 않은 채, 아주 기초적이고 텅 빈 절편(intercept) 상수 뼈대 축 하나만 덜렁 세워놓은 깡통 무(null) 모델만 적합시켰더라면 어떻게 되었을까요? 아마 그 허술한 모델은 쏟아져 들어오는 무수한 낯선 테스트 관측 실측치들을, 그저 자기 머릿속에 기억된 기존 훈련용 세트 관측 개체들의 단순 평균 대표값 하나짜리 잣대로 똑같이 뭉뚱그려 대충 일괄 예측 평가해 뱉어버렸을 것입니다. 우리는 이 기가 막힌 릿지(ridge) 정규화 도출 모델 세팅 도구에 파라미터 징벌 강도 억압 수치 $\lambda$ 변숫값을 _아주 무지막지 극단적으로_ 거대하고 무거운 스케일 비율로 억눌러 세팅 부여해 단번에 강제 적합시킴으로써, 저 어리석은 깡통 무 모델과 일치하는 똑같은 결과인 '평균 일괄 도출 반환 예측치 결과값'을 그대로 시뮬레이션 성취, 도출 산출해 똑같이 얻을 수도 있습니다. (코드 세팅 파라미터 값 중 `1e10`라는 용어 표현 지시어 문법은 $10^{10}$ 규모의 초대형 수치를 무단 지칭 타산해 뜻합니다.)

```python
In [31]: ridge.alpha = 1e10
results = skm.cross_validate(ridge,
                             X,
                             Y,
                             scoring='neg_mean_squared_error',
                             cv=validation)
-results['test_score']
```

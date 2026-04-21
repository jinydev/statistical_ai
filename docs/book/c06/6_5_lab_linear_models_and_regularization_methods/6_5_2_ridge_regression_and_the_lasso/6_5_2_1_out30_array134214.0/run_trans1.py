import codecs

content = r"""---
layout: default
title: "trans1"
---

# **`Out[30]:`** `array([134214.0])`

The test $\text{MSE}$ is 1.342e+05. Note that if we had instead simply fit a model with just an intercept, we would have predicted each test observation using the mean of the training observations. We can get the same result by fitting a ridge regression model with a _very_ large value of $\lambda$ . Note that `1e10` means $10^{10}$ .
이렇게 모델이 뱉어낸 테스트 평가 척도 $\text{MSE}$ 측정값은 1.342e+05(약 134,214) 수준으로 관측됩니다. 여기서 눈여겨볼 점은, 만약 우리가 이런 복잡한 산출 과정 대신 어떤 변수도 없이 아주 단순하게 하나의 절편(intercept) 상수 축만 덜렁 가진 기본 기초 무(null) 모델만 적합했다면, 모델은 들어오는 각각의 독립 테스트 관측 대상치들을 그냥 기존 훈련용 세트 관측 개체들의 평균치 대표값으로 똑같이 일괄 뭉뚱그려 예측 반환해 버렸을 것이란 사실입니다. 우리는 능선 릿지(ridge) 정규화 예측 모델에 변동 파라미터 $\lambda$ 변숫값을 _아주 극단적으로_ 거대한 수치율을 강제 세팅 부여해 적합시킴으로써, 이와 일치하는 똑같은 깡통 평균 일괄 예측 평가 결괏값을 도출시켜 얻어낼 수 있습니다. (설정 지시어 중 `1e10` 라는 코드는 $10^{10}$을 뜻합니다.)

```python
In [31]: ridge.alpha = 1e10
results = skm.cross_validate(ridge,
                             X,
                             Y,
                             scoring='neg_mean_squared_error',
                             cv=validation)
-results['test_score']
```
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_2_ridge_regression_and_the_lasso\6_5_2_1_out30_array134214.0\trans1.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)

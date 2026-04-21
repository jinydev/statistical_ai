---
layout: default
title: "trans1"
---

# 5.3.1 The Validation Set Approach
# 5.3.1 검증 세트 접근법

We explore the use of the validation set approach in order to estimate the test error rates that result from fitting various linear models on the `Auto` data set. 
우리는 `Auto` 데이터 세트 상에 여러 선형 모델들을 적합(fitting) 시켜 본 결과로 나타나는 테스트 에러율(error rates) 추정 목적으로 검증 세트 접근법(validation set approach)의 사용을 탐구할 것입니다.

We use the function `train_test_split()` to split the data into training and validation sets. As there are 392 observations, we split into two equal sets of size 196 using the argument `test_size=196` . It is generally a good idea to set a random seed when performing operations like this that contain an element of randomness, so that the results obtained can be reproduced precisely at a later time. We set the random seed of the splitter with the argument `random_state=0` . 
우리는 데이터를 훈련(training) 및 검증(validation) 세트 진영으로 각각 분할 분산시키기 위해 함수 `train_test_split()` 을 활용합니다. 총 표본 관측 단위가 392개이기 때문에, 함수 인자 `test_size=196` 을 투입 사용하여 정확하게 크기가 같은 196개짜리 집합 세트 둘로 양분시킬 방침입니다. 통상적으로 볼 때 이처럼 특정 무작위성(randomness) 요소 작용이 깃든 연산 조작을 가동시킬 땐, 나중 추후 어느 시점이든 과거 획득된 산출 결과물들을 다시 한 치의 오차 없이 정밀하게 역산 복제 재현(reproduced precisely) 해 낼 요량으로 무작위 시드(random seed) 값을 설정 지정해 두는 편이 여러모로 권장될 법한 좋은 발상입니다. 본 장에서 우리는 인자 매개 변수 지정항인 `random_state=0` 값을 박아서 해당 분할 연산 기계(splitter)의 난수 생성 시드값을 고정 배치해 둡니다.

```python
In [3]: Auto = load_data('Auto')
        Auto_train, Auto_valid = train_test_split(Auto,
                                                  test_size=196,
                                                  random_state=0)
```

Now we can fit a linear regression using only the observations corresponding to the training set `Auto_train` . 
자 이제 우리는 훈련 세트인 `Auto_train` 항목에 직통으로 상응(corresponding to) 기속되는 해당 관측 자료 표본 군집만을 떼어 사용하면서 그것을 재료로 하여 단일 선형 회귀 모형(linear regression) 픽업 적합화를 실행 돌려볼 수 있습니다.

```python
In [4]: hp_mm = MS(['horsepower'])
        X_train = hp_mm.fit_transform(Auto_train)
        y_train = Auto_train['mpg']
        model = sm.OLS(y_train, X_train)
        results = model.fit()
```

We now use the `predict()` method of `results` evaluated on the model matrix for this model created using the validation data set. We also calculate the validation MSE of our model. 
다음으로 이어 진행할 부분은, 저리 조성시킨 검증 판독 데이터 세트를 기반 활용해 아까 빚어두었던 모델 매트릭스 행렬(model matrix) 판 위에서 `results` 모형 객체의 예측 구동체(method) `predict()` 를 활용해 값을 계산 산출(evaluated) 시키는 행위입니다. 그와 병행하여 나란히 우리는 해당 판독 모형 구동체에서 드러날 검증판 MSE 치수까지 연산 계산 타진(calculate)할 것입니다.

```python
In [5]: X_valid = hp_mm.transform(Auto_valid)
        y_valid = Auto_valid['mpg']
        valid_pred = results.predict(X_valid)
        np.mean((y_valid - valid_pred)**2)
```

```python
Out[5]: 23.6166
```

Hence our estimate for the validation MSE of the linear regression fit is $23.62$. 
그리하여 종국적으로 이룩 달성해 낸 선형 회귀 편제상의 검증판 MSE 추정 결과수치는 약 $23.62$ 로 산출됩니다.

We can also estimate the validation error for higher-degree polynomial regressions. We first provide a function `evalMSE()` that takes a model string as well as a training and test set and returns the MSE on the test set. 
우리는 비단 저것에 그치는 수준이 아니라 더 높은 차수로 전개되는 복잡 다단한 고차다항 곡선형 회귀(higher-degree polynomial regressions) 방정식 모형 체계를 타깃 겨냥해 검증 오차값 측정 추산을 타진 감행해 볼 수 있습니다. 우선, 이런 행위를 개시하기 위해 우리는 함수 `evalMSE()` 를 먼저 제안 마련해 주는데, 해당 이 함수 객체 도구는 기초 연습 훈련조 및 최종 테스터 검사조 데이터 조합은 물론 당해 표적 모델 문자열 식별자를 투입 수용(takes) 처리해서 테스터 평가 조 내에 머무르고 있는 해당 MSE 값을 반환 대처(returns) 배출해 줄 것입니다.

```python
In [6]: def evalMSE(terms,
                    response,
                    train,
                    test):
            mm = MS(terms)
            X_train = mm.fit_transform(train)
            y_train = train[response]
            X_test = mm.transform(test)
            y_test = test[response]
            results = sm.OLS(y_train, X_train).fit()
            test_pred = results.predict(X_test)
            return np.mean((y_test - test_pred)**2)
```

Let’s use this function to estimate the validation MSE using linear, quadratic and cubic fits. We use the `enumerate()` function here, which gives both the values and indices of objects as one iterates over a for loop. 
자, 방금 마련 구성한 본 구동 기믹 함수 체계를 이끌고 1단 직선 선형(linear), 곡선 2단 이차식(quadratic), 나아가 물결 3단 3차원 입체식 곡선형 결합 계통(cubic)의 모델 피팅 절차를 사용해 일련의 파생적 검증 MSE 측정 산출 목표물 추산을 개시해 내봅시다. 과정 중에서 파이썬의 `enumerate()` 내장 함수를 호출 사용 동원시킬 터인데, 해당 함수 기믹은 가동 구동루프 `for loop` 뺑뺑이 전개 과정상에서 객체의 본연적 값과 개별 인덱스를 순차 상호 병행 지급해(gives both the values and indices) 순환 출력 구동을 조장합니다.

```python
In [7]: MSE = np.zeros(3)
        for idx, degree in enumerate(range(1, 4)):
            MSE[idx] = evalMSE([poly('horsepower', degree)],
                               'mpg',
                               Auto_train,
                               Auto_valid)
        MSE
```

```python
Out[7]: array([23.62, 18.76, 18.80])
```

These error rates are $23.62, 18.76$, and $18.80$, respectively. If we choose a different training/validation split instead, then we can expect somewhat different errors on the validation set. 
이렇게 하여 판독 도출 결과 배출된 에러 지분 확률 지표는 개별 순차 각각(respectively) $23.62, 18.76$ 그리고 $18.80$ 로 기록 추산 검정됩니다. 만의 하나라도 만일 본 훈련조/검증조 스플릿 쪼개기 도출 편제 결정을 아까와 다르게 채택 취할 시, 우리는 아마 다소간 격차 수준이 어긋나는 상이한 검증상 오류(different errors) 지표를 조우 도출 맞이할(expect) 수 있습니다.

```python
In [8]: Auto_train, Auto_valid = train_test_split(Auto,
                                                  test_size=196,
                                                  random_state=3)
        MSE = np.zeros(3)
        for idx, degree in enumerate(range(1, 4)):
            MSE[idx] = evalMSE([poly('horsepower', degree)],
                               'mpg',
                               Auto_train,
                               Auto_valid)
        MSE
```

```python
Out[8]: array([20.76, 16.95, 16.97])
```

Using this split of the observations into a training set and a validation set, we find that the validation set error rates for the models with linear, quadratic, and cubic terms are $20.76, 16.95$, and $16.97$, respectively. 
실 관측물 타겟 대상을 훈련/검증 조로 조립 분쇄 쪼개 분할한 이번 상이(split) 변별 판도를 활용 전개해 측량한 작금의 새로운 결과물 토대 안에서 우리는 순수 선형 1차 모델부터 2차 함수 결합 모델 곡선, 최종 3차 요소를 반영 품은 모형에 뒤따르는 관련 검정조 에러 오류의 스코어가 개별 지표로서 $20.76, 16.95$, 및 $16.97$ 순차 배열 지표를 품은 채 산출 도출 파악됨(find)을 인지하게 되었습니다.

These results are consistent with our previous findings: a model that predicts `mpg` using a quadratic function of `horsepower` performs better than a model that involves only a linear function of `horsepower` , and there is no evidence of an improvement in using a cubic function of `horsepower` . 
이러한 연달아 도출 획득된 기록의 산출 분석 결론들은 기왕 이전까지 우리가 도달 성취 파악(previous findings) 해냈던 일체의 지식 지점들과도 명쾌하게 일관된 결(consistent with)을 유지 방증합니다: 즉 단순히 구태의연한 순수 단절된 `horsepower` 변수의 선형 곡선 형태만을 운용 품은 추론 지표보다는 오히려 적정 둥근 2차 방정식 함수 `horsepower` 형을 토대로 하여 `mpg` 기록 달성을 예측 산출 타진해낸 모델이 필연코 나은 폼의 기록 평가수행 능률(performs better) 강점을 표출 뿜어냄과 아울러, 반면 이보다 오히려 과다 전개된 3차 방증 꼬불 함수 편제 기조 `horsepower` 모델 도입 차용상에서는 딱히 유의미하고 확연하게 기록 증진(improvement) 요소가 뒷받침 입증 발견되었다고 표정 할 만한 어떠한 증거력(no evidence) 요건조차 적발되지 않았다는 사실 말입니다.

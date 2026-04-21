---
layout: default
title: "trans1"
---

# _5.3.1 The Validation Set Approach_ 
# _5.3.1 검증 세트 접근법_

We explore the use of the validation set approach in order to estimate the test error rates that result from fitting various linear models on the `Auto` data set. 
우리는 `Auto` 기종 데이터 세트 전경 위에다 무수히 다채로운 종파의 여러 선형 모델들을 적합시킨 결과로서 빚어진 테스트 오차율을 타진 가늠해 추정하기 위한 목적의 일환으로 검증 세트 접근법(validation set approach)의 실사용 과정을 탐구 실습해 본다.

We use the function `train_test_split()` to split the data into training and validation sets.
우리는 `train_test_split()` 이란 이름의 내장 함수를 전격 기용 사용함으로써 원본 데이터를 훈련 세트와 검증 세트라는 이분된 덩어리로 쪼개어 분할 타진한다.

As there are 392 observations, we split into two equal sets of size 196 using the argument `test_size=196` .
원체 도합 392명에 달하는 총체 관측치 개체 인구수가 존재하기 까닭에, 우리는 `test_size=196` 이라는 인자(argument) 옵션 명령어를 세팅 투입 사용함으로써 해당 무리를 정확히 인구수 196명을 지닌 두 개의 동등한 덩치 세트들로 반으로 쪼개 분할한다.

It is generally a good idea to set a random seed when performing operations like this that contain an element of randomness, so that the results obtained can be reproduced precisely at a later time.
이렇듯 난수 무작위성(randomness) 의 여건 요소를 내포 수반하는 일련의 조작 연산 작업들을 우리가 앞장서 이행 수행할 당시엔 번번이 무작위 시드(random seed) 값을 미리 수동으로 엄격 고정 세팅해 두는 편이 통상적으로 몹시 현명한 바람직 우량 아이디어 발상인데; 이는 그리 조치해 둬야 비로소 차후 언젠가 미지의 훗날 시간에 가서도 이전에 획득 도출 산출되었던 그 수확 결과물 궤적들이 당당히 단 번호 어김없이 고스란히 오차 없이 정밀하게 완벽 재현(reproduced precisely) 가동 재생될 수 있기 때문이다.

We set the random seed of the splitter with the argument `random_state=0` . 
우리는 `random_state=0` 이라는 제약 인자 명령어를 건네주어, 저 분할기(splitter) 기계 장치가 쓸 난수 시드를 세팅 고정 조율해 설정한다.

```python
In [3]: Auto = load_data('Auto')
        Auto_train, Auto_valid = train_test_split(Auto,
                                                  test_size=196,
                                                  random_state=0)
```

Now we can fit a linear regression using only the observations corresponding to the training set `Auto_train` . 
이제 우리는 오직 저 훈련 세트로 발탁된 `Auto_train` 집단에 상응 속하는 관측치 덩어리 인구들만 편파적으로 치사하게 오롯이 기용 사용함으로써 전폭 선형 회귀 무대를 적합 장착 가동시킬 수 있다.

```python
In [4]: hp_mm = MS(['horsepower'])
        X_train = hp_mm.fit_transform(Auto_train)
        y_train = Auto_train['mpg']
        model = sm.OLS(y_train, X_train)
        results = model.fit()
```

We now use the `predict()` method of `results` evaluated on the model matrix for this model created using the validation data set.
우리는 이제 방금 그 도출물 `results` 장치 안에 들어 있는 `predict()` 내장 메서드 도구를 발탁 사용함으로써; 저 검증 데이터 세트 조작을 사용 기용해 탄생 창조 조립시켜 구동한 당해 검증 모델 행렬판 위에서 평가 도출된 산물 궤적을 뿜어낸다.

We also calculate the validation MSE of our model. 
우리는 또한 나아가 당당히 우리 모델이 거둔 해당 검증 MSE 점수 지표를 이윽고 연산 산출 가늠 계산해 낸다.

```python
In [5]: X_valid = hp_mm.transform(Auto_valid)
        y_valid = Auto_valid['mpg']
        valid_pred = results.predict(X_valid)
        np.mean((y_valid - valid_pred)**2)
```

```python
Out[5]: 23.6166
```

Hence our estimate for the validation MSE of the linear regression fit is 23 _._ 62. 
그리하여 이 선형 회귀 적합 라인의 검증 MSE 스코어 지수를 겨냥한 우리의 자체 추산 추정 역산 볼륨 숫자는 23.62 수위로 귀결 산출된다.

We can also estimate the validation error for higher-degree polynomial regressions.
우린 어김없이 더 나아가 한 차원 더 고차원 굴곡 승수의 다항 회귀들(higher-degree polynomial regressions) 에 부과되는 저 검증 파장 에러율 수치 역시 거푸 예측 추정 헤아려 계산 평가해 낼 수 있다.

We first provide a function `evalMSE()` that takes a model string as well as a training and test set and returns the MSE on the test set. 
이를 위해 우리는 우선 기착 `evalMSE()` 이라 명명한 하나의 사용자 지원 우회 함수 툴을 사전 구축 제공해 주는데; 이 장치 팩은 훈련 및 테스트 세트 양 구역 덩어리뿐 아니라 덩달아 당해 모델 문자열 끈(model string) 속성 인자를 집어삼키고 취하여(takes) 연산한 뒤, 테스트 세트 경기장에서 치른 이 무기의 MSE 결과 타율 점수표를 온전히 돌려주는(returns) 기능을 한다.

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

Let’s use this function to estimate the validation MSE using linear, quadratic and cubic fits.
자 그럼 방금 건져 구축해 낸 저 해당 지원 함수를 적극 갖다 써먹음으로써 선형(linear), 1차식 선, 2차(quadratic) 그리고 3차(cubic) 굴곡 적합 장비 라인들을 각각 덧대었을 때 빚어지는 상응 검증 MSE 점수 폭들을 모조리 연산 추정 가늠 평가해 보자.

We use the `enumerate()` function here, which gives both the values and indices of objects as one iterates over a for loop. 
우리는 이 전면 과정 한복판에서 기꺼이 `enumerate()` 함수 장치를 호출해 동원 써먹는데, 이는 어떠한 사용자가 어떤 for 구문 반복문 루프(loop) 궤적을 타고 한 바퀴씩 무리 객체를 순회(iterates)할 때마다 그 내부 객체의 알맹이 핵심 값(values) 들과 그에 상응하는 위치 번호 인덱스(indices) 목차 두 가지를 사이좋게 보따리 동시 병합 구비 제공(gives both) 해주는 기능 수단이다.

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

These error rates are 23 _._ 62 _,_ 18 _._ 76, and 18 _._ 80, respectively.
기껏 토해 도출된 이들의 에러율 성적 지표는 각기 23.62, 18.76, 그리고 18.80 등락으로 산출 귀결된다.

If we choose a different training/validation split instead, then we can expect somewhat different errors on the validation set. 
만약 우리가 방금의 방식 대신, 애초에 전혀 다른 번호표의 무작위 훈련/검증 분할 조작 쪼개기를 선택해 치렀더라면; 응당 우리는 그 검증 세트 위에서 거둔 에러 타율 점수가 분명 방금 보았던 것과는 다소 다른 수위 조작 널뛰기 수치 다른 파장을 얻을 것임(different errors) 을 쉽게 통감 예측 짐작 기대(expect) 할 수 있다.

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

Using this split of the observations into a training set and a validation set, we find that the validation set error rates for the models with linear, quadratic, and cubic terms are 20 _._ 76, 16 _._ 95, and 16 _._ 97, respectively. 
관측치 인구 무리를 훈련 및 검증 세트로 두 동강 낸 바로 이 신생 분할(split) 버전을 덧대 적용한 결과; 기어이 우린 선형, 2차, 그리고 3차 곡률 항(terms) 을 각기 장착한 모델 부대원들이 각자 거둔 검증 세트 에러율 성적표가 기실 대충 20.76, 16.95, 16.97 수위로 쏠려 각기 안착 산출 결론 났음을 이윽고 인지 도래 목도 발견(find) 하게 된다.

These results are consistent with our previous findings: a model that predicts `mpg` using a quadratic function of `horsepower` performs better than a model that involves only a linear function of `horsepower` , and there is no evidence of an improvement in using a cubic function of `horsepower` . 
이들 목도 성과 현장 도출물 결과들은 이윽고 다름 아니라 과거 우리가 줄곧 부르짖어 찾아 깨우친 기존 발견 사실(previous findings) 지표들과 무척 일맥상통 일치(consistent) 부합하는데; 즉 오직 멍청히 단조로운 `horsepower` 선형 1차 직선 한 줄기 항만 투여 장착한 무기 모델 따위보다야, `horsepower` 스펙 변수에 2차 굽은 곡면 (quadratic) 함수 옵션 포진을 장착해 넣고 `mpg` 연비 점수를 쏘아 맞힌 모델 무기가 훨씬 더 탁월 위력 정교한 우위 성능 우수 방어망 수행(performs better) 파장 위력을 보장 발휘했음을 증명하며; 나아가 거기서 더 욕심을 키워 3차(cubic) 삼제곱 함수 옵션 따위를 무식 구태여 욱여 밀어 부착 탑재해 차용해 써먹는 데에서는 단 일체의 일말 향상 점수 이점 증거 개연성(evidence of an improvement) 기미 나발 따위 흔적 효용조차 당최 도래 수반 포착 존재하지 아니함을 또다시 연신 당당 무사 증명 천명 지어 확인시켜 안겨준다.

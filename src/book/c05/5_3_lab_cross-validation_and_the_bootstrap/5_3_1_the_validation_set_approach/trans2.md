---
layout: default
title: "trans2"
---

# _5.3.1 The Validation Set Approach_ 
# _5.3.1 반반 무 많이: 검증 세트 접근법_

We explore the use of the validation set approach in order to estimate the test error rates that result from fitting various linear models on the `Auto` data set. 
이번 판에서는 `Auto` 자동차 데이터 세트를 구장 삼아, 우리가 그토록 비웃었던 그 원시적인 반반 쪼개기 수법(검증 세트 접근법)을 직접 코드로 굴려보고 얘가 토해내는 실전 오차율의 민낯을 구경해 봅니다.

We use the function `train_test_split()` to split the data into training and validation sets.
파이썬 머신러닝계의 국민 톱(saw) 무기인 `train_test_split()` 함수를 써서, 우리는 무자비하게 원본 데이터를 '훈련용 병력'과 '시험용 마루타(검증 세트)' 두 동강으로 갈라버릴 겁니다.

As there are 392 observations, we split into two equal sets of size 196 using the argument `test_size=196` .
여긴 자동차 관측치가 392대 있으니까, 저기 `test_size=196` 이라는 인자를 무기 옵션으로 박아 넣으면 정확히 196대씩 공평하게 반반 쪼개지는 피 튀기는 분단이 일어납니다.

It is generally a good idea to set a random seed when performing operations like this that contain an element of randomness, so that the results obtained can be reproduced precisely at a later time.
근데 통계 바닥에서 이렇게 로또(무작위성) 굴리듯 데이터를 랜덤으로 쪼갤 땐, 내가 뽑은 번호를 어딘가에 박제(random seed) 해두는 게 목숨을 부지하는 현명한 멘탈 보호법입니다. 그래야 훗날 내일모레 교수님 앞에서 똑같은 코드를 돌렸을 때 어제랑 똑같은 성적표가 기적처럼 재현(reproduced precisely) 되며 살아남을 수 있거든요.

We set the random seed of the splitter with the argument `random_state=0` . 
우린 쫄보니까 저 쪼개기 함수에 `random_state=0` 값을 박아서 난수표 추첨 시드를 꽉 고정해 버립니다.

```python
In [3]: Auto = load_data('Auto')
        Auto_train, Auto_valid = train_test_split(Auto,
                                                  test_size=196,
                                                  random_state=0)
```

Now we can fit a linear regression using only the observations corresponding to the training set `Auto_train` . 
드디어 이제 저 반 토막 난 불쌍한 196명의 훈련 부대 `Auto_train` 애들만 갈아 넣고 채찍질해서 '선형 회귀' 예측 모델을 장착시킬 시간입니다.

```python
In [4]: hp_mm = MS(['horsepower'])
        X_train = hp_mm.fit_transform(Auto_train)
        y_train = Auto_train['mpg']
        model = sm.OLS(y_train, X_train)
        results = model.fit()
```

We now use the `predict()` method of `results` evaluated on the model matrix for this model created using the validation data set.
총알 장전 끝났으니, 저 모델 결과 묶음(`results`) 에 붙어 있는 사격 버튼인 `predict()` 스킬을 뽑아 듭니다. 과녁은 당연히 아까 따로 감옥에 빼놨던 생판 남인 '검증 데이터 세트' 녀석들이죠!

We also calculate the validation MSE of our model. 
그놈들을 쏴 맞힌 뒤, 과녁에서 얼마나 처참히 빗나갔는지 그 삑사리 점수인 검증 MSE 오차 성적을 잔인하게 계산해 폭로해 봅니다.

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
자! 결국 직선 하나(선형 회귀) 찍 하고 갖다 댔을 때 튀어나온 이 모델의 실전 오차 방어율 점수는 대충 23.62 정도로 뜨네요.

We can also estimate the validation error for higher-degree polynomial regressions.
물론 우린 저 조잡한 직선 말고, 유연성을 한껏 먹여 곡률을 뿜어내는 '고차원 다항 회귀' 장비들도 똑같이 실전 에러 점수를 가늠해 볼 수 있습니다.

We first provide a function `evalMSE()` that takes a model string as well as a training and test set and returns the MSE on the test set. 
계속 똑같은 짓 하기 귀찮으니 헬퍼 함수 `evalMSE()` 하나를 뚝딱 만들죠. 이 무기는 "어떤 모델 옵션을 장착할래?", "어느 부대로 훈련할래?", "과녁은 누구야?" 라는 지시를 삼킨(takes) 다음, 알아서 총 쏘고 에러율 MSE 성적표 한 장을 딱 뱉어내는(returns) 아주 충직한 매크로 시종장입니다.

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
자, 이 시종장 함수에다가 직선(선형), U자 곡선(2차), S자 뱀파이어 곡선(3차) 세 가지 무기 지시를 내리며 연속 사격을 시켜서 각각의 에러율 성적들을 비교 관찰해 보겠습니다.

We use the `enumerate()` function here, which gives both the values and indices of objects as one iterates over a for loop. 
이 뺑뺑이를 돌릴 때 파이썬의 깨알 치트키 함수 `enumerate()` 를 섞어 쓸 건데; 이 놈은 반복문을 돌며 순회(iterates) 할 때마다 "지금 몇 번째 턴입니다!" 하는 인덱스 번호표랑 "이번 턴 옵션 알맹이!" 를 양손에 달달하게 함께 쥐여주는(gives both) 친절한 함수죠.

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
타다당! 토해낸 타격 에러 점수가 차례대로 23.62, 18.76, 18.80이 떴습니다.

If we choose a different training/validation split instead, then we can expect somewhat different errors on the validation set. 
그런데 이론 시간(5.1.1) 에 우리가 뭐라 씹었죠? 맞습니다. "이 무식한 검증 세트 쪼개기는 로또 운이 너무 심하다!" 다시 말해, 만약 우리가 아까 데이터를 처음 둘로 반갈죽 낼 때 전혀 다른 난수 시드표를 써서 애들을 다르게 쪼갰다면? 당연히 이 에러 점수들도 방금 본 거랑은 영 딴판인 수치들로 널뛸 게 안 봐도 비디오입니다.

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
난수 번호표(`random_state=3`) 를 바꾼 뒤 다시 반갈죽내서 위 장비를 싹 돌려보았더니? 헐, 선형-2차-3차 공격무기들이 도출해 낸 에러 점수가 돌연 20.76, 16.95, 그리고 16.97로 훅 꺾여버린 완전히 딴 무대 상황임을 발견하게 됩니다. 이래서 반반 치킨은 위험합니다!

These results are consistent with our previous findings: a model that predicts `mpg` using a quadratic function of `horsepower` performs better than a model that involves only a linear function of `horsepower` , and there is no evidence of an improvement in using a cubic function of `horsepower` . 
그래도 뭐, 저 두 번의 삽질 결과 모두가 입 모아 소리치는 확실한 진리 하나는 있습니다.
1. 멍청하게 직진만 하는 선형 총알보단, 2차 함수(quadratic) 폭탄을 박아 넣은 무통장 모델이 확실히 에러를 처절하게 박살 내며 훨씬 더 우월한 방어선 성능(performs better) 을 갖췄다.
2. 하지만 여기서 욕심 좀 더 내서 3차 함수(cubic) 빔 옵션까지 쓸데없이 달아봐야? 코딱지만 한 요행은커녕 에러 점수가 쥐꼬리만큼도 더 개선되지 않는다는 **과적합 삽질의 절벽 한계(no evidence of an improvement)** 만 징그럽게 확인시켜 줍니다.

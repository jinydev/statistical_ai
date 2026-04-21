---
layout: default
title: "trans2"
---

# 5.3.1 The Validation Set Approach
# 5.3.1 도박판의 시작: 검증 세트 반반 무 많이! (Validation Set)

We explore the use of the validation set approach in order to estimate the test error rates that result from fitting various linear models on the `Auto` data set. 
자, 대망의 첫 번째 미션! 옛날 챕터에서 그토록 맘대로 선을 긋고 놀았던 `Auto` 장난감 데이터를 꺼내와서, 이 무식하지만 직관적인 반반 쪼개기 시스템(검증 세트 접근법) 으로 실전 수능 오차율(test error rates) 견적을 어떻게 뽑아내는지 손맛을 느껴보겠습니다.

We use the function `train_test_split()` to split the data into training and validation sets. As there are 392 observations, we split into two equal sets of size 196 using the argument `test_size=196` . It is generally a good idea to set a random seed when performing operations like this that contain an element of randomness, so that the results obtained can be reproduced precisely at a later time. We set the random seed of the splitter with the argument `random_state=0` . 
데이터를 훈련소파와 모의고사파로 반갈죽 내기 위해 쓰이는 궁극의 사이킷런 도마 칼! `train_test_split()` 함수를 소환합니다. 우리한테 차가 딱 392대 있으니까요, 공평하게 196대씩 두 덩어리(two equal sets)로 썰어달라고 `test_size=196` 조건을 달아줍니다. 여기서 꿀팁 하나! 이건 눈감고 제비뽑기를 돌리는 무작위 로직(randomness) 이라서, 친구랑 똑같이 코딩해도 결과가 매번 틀어지면 피곤하겠죠? 나중에 밤새워 코딩하다 에러 터졌을 때 "아씨 그때 그 결과 안 나오잖아!" 하고 머리 뜯기 싫으면, 룰렛의 뽑기 난수 조작 시드(random seed) 를 고정해 두는 게 정신 건강에 이롭습니다. 고로 `random_state=0`이라는 주사위 고정 주문을 박아두고 출발합니다.

```python
In [3]: Auto = load_data('Auto')
        Auto_train, Auto_valid = train_test_split(Auto,
                                                  test_size=196,
                                                  random_state=0)
```

Now we can fit a linear regression using only the observations corresponding to the training set `Auto_train` . 
방금 칼질로 예쁘게 `Auto_train` (훈련소 입소자) 이란 데이터 보따리가 생겼죠? 자원방비 절반의 병력만 데리고 곧장 뼈대 앙상한 '선형 회귀' 예측 기계를 헬스장(fit) 에 굴려봅니다.

```python
In [4]: hp_mm = MS(['horsepower'])
        X_train = hp_mm.fit_transform(Auto_train)
        y_train = Auto_train['mpg']
        model = sm.OLS(y_train, X_train)
        results = model.fit()
```

We now use the `predict()` method of `results` evaluated on the model matrix for this model created using the validation data set. We also calculate the validation MSE of our model. 
운동 끝났으면 이제 써먹어 봐야죠! 훈련소에서 근육 키운 이 모델(`results`) 에게 `predict()` 스킬을 조준해라 명령한 뒤, 아까 뒤로 몰래 숨겨뒀던 싱싱한 검증용 데이터(`Auto_valid`) 표적들을 던져줍니다. 그리고 녀석이 얼마나 헛스윙을 질렀는지, 얄짤없는 오차 제곱합(MSE) 계산기를 뚜드려 채점(calculate) 해봅니다.

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
삑! 영수증 나왔습니다. 1차선 일자 몽둥이(선형) 모델의 첫 모의고사 오답 점수(MSE) 는 소숫점 떼고 쿨하게 **23.62** 를 기록했습니다!

We can also estimate the validation error for higher-degree polynomial regressions. We first provide a function `evalMSE()` that takes a model string as well as a training and test set and returns the MSE on the test set. 
직선 몽둥이 성적을 받으니 욕심이 생깁니다. 이번엔 모델의 허리를 부드럽게 꺾어버리는 고차 다항식(higher-degree polynomial) 기어들을 물리고 똑같은 테스트를 달리면 성적이 어떻게 떡상/떡락할까 몹시 궁금하죠. 이 노가다를 매번 손으로 칠 순 없으니, 아예 파이썬 자동 자판기 함수 하나를 뚝딱 만듭니다(provide a function). 이 자판기 `evalMSE()` 는 우리가 훈련세트, 시험세트, 그리고 구동할 함수 스타일을 자판기 구멍(인자)에 부어 넣으면(takes) 척척 알아서 모델 펌핑하고 정답 맞히고 오답 삥땅 점수 MSE 를 동전 반환구로 뱉어내는(returns) 아주 충실한 노예입니다.

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
자, 노예 자판기도 만들었으니 바로 실전 투입! 1단 직선(linear), 2단계 U자 커브(quadratic), 3단 꼬불이파(cubic) 기어를 순서대로 물려가며 에러 타율을 모조리 뽑아봅시다. 파이썬 문법 짬바 살짝 얹어서 `enumerate()` 란 마법 주문을 쓸 건데, `for` 문 뺑뺑이를 돌 때마다 "야 이거 1번째 곡선 점수야~ 2번째 곡선 점수야~" 귀찮게 번호표 인덱스랑 실제 값이랑 센스 있게 1+1 세트로 던져주는(gives both the values and indices) 아~주 편한 코딩 스킬입니다.

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
계기판의 스코어 보시죠! 순번대로 **23.62, 18.76, 18.80** 을 터뜨렸습니다. 오! 2차 곡선에서 점수가 확 좋아졌네요! 근데 아까 이론 시간에 배웠던 그 악몽의 가변성 폭주 현상 기억나시나요? 만약 우리가 아까 처음 위에서 칼박 맞춰 자른 제비뽑기 시드를 버리고 "제비뽑기를 아예 처음부터 완전 딴판인 뽑기판으로 다시 시작해 보면(different split) 어떨까?" 라는 호기심이 일 겁니다. 당연히 그때는 테스트 에러 영수증 액수가 또 요동치며 달라질 거라고(expect somewhat different) 감각상 예상해야 합니다.

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
보이십니까? `random_state=3` 으로 룰렛 판을 갈아엎고 애들 진영을 바꿨더니, 똑같은 1, 2, 3차 모델을 돌렸음에도 불구하고 성적표 액수가 **20.76, 16.95, 16.97** 로 아까랑 확 비틀려 찍혔습니다(find)! 이게 바로 그 악명 높던 단순 검증법의 주사위 널뛰기 병크입니다.

These results are consistent with our previous findings: a model that predicts `mpg` using a quadratic function of `horsepower` performs better than a model that involves only a linear function of `horsepower` , and there is no evidence of an improvement in using a cubic function of `horsepower` . 
물론 널뛰기를 한 스코어 액수 자체가 출렁거렸을지언정, 뼈 때리는 기본 성질 팩트만은 저번 이론에서 까발려졌던 통찰(previous findings) 과 단전부터 일치(consistent with) 합니다! 그 일치점이 뭐냐? 연비 타겟 추론에 있어서 뻣뻣한 1차선 마력 몽둥이(linear) 보단 확실히 U자로 부드럽게 꺾인 2차 커브(quadratic) 엔진이 기록 상승(performs better) 강점을 시원하게 뿜어낸다는 것! 그러나 뇌절해서 구불거리는 3차 오버 엔진(cubic) 까지 끌어들여 봤자 성적표 향상의 낌새를 눈곱만큼도 발견할 증거력(no evidence) 이 없다는 그 소름 돋는 두 가지 절대명제 말입니다!

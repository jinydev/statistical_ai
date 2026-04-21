---
layout: default
title: "trans2"
---

# `Out[9]:` `24.2315`

The arguments to `cross_validate()` are as follows: an object with the appropriate `fit()`, `predict()`, and `score()` methods, an array of features `X` and a response `Y`. We also included an additional argument `cv` to `cross_validate()`; specifying an integer $K$ results in $K$-fold cross-validation. We have provided a value corresponding to the total number of observations, which results in leave-one-out cross-validation (LOOCV). The `cross_validate()` function produces a dictionary with several components; we simply want the cross-validated test score here (MSE), which is estimated to be $24.23$. We can repeat this procedure for increasingly complex polynomial fits. To automate the process, we again use a for loop which iteratively fits polynomial regressions of degree 1 to 5, computes the associated crossvalidation error, and stores it in the $i$th element of the vector `cv_error`. The variable `d` in the for loop corresponds to the degree of the polynomial. We begin by initializing the vector. This command may take a couple of seconds to run. 
자, 아까 불러온 `cross_validate()` 자동 심판관에 대해 썰을 좀 풀어보죠. 이 녀석 구멍(인자)에 넣어야 할 준비물은 명확합니다: 제대로 훈련(`fit`)하고 채점(`score`)할 수 있는 잘 빠진 로봇 하나, 문제지 `X`, 정답지 `Y` 세트입니다. 거기에 꿀팁! 추가 세팅 다이얼인 `cv` 값을 만져서 아무 숫자 $K$나 때려 넣으면, 알아서 데이터판을 찢어주는 **K-폴드(K-fold) 교차 검증** 모드가 발동(results in) 합니다. 그런데 우린 지금 여기서 무슨 미친 짓을 했느냐? $K$ 값 자리에 무려 데이터 개수(392개) 전체를 전부 통째 대입 풀가동시켜 버렸습니다(provided a value)! 즉 차 1대만 빼고 391대로 훈련하는 극악무도한 1-인 왕따 뺑뺑이, **LOOCV** 를 발동시킨 겁니다! 자, 돌아간 `cross_validate()` 기계는 오만가지 잡다한 영수증을 파우치(딕셔너리) 에 뱉지만 우린 심플하게 딱 하나, 평균 뺑뺑이 테스트 오답 스코어(MSE) 수치만 쏙 주워 먹으면 됩니다. 결과는 **24.23** 점이네요. 한 번 맛봤으니 이제 매크로를 돌릴 차례죠? 1단부터 5단까지 다항식 기어를 정신없이 올리며 뺑뺑이 점수를 뽑아내는 노가다를 지시합시다. 빈 통(`cv_error`) 하나 던져주고 `for loop` 뺑뺑이로 1단부터 5단 기어(`d`) 마다 점수를 기록하게(stores) 할 겁니다. (주의: 이 코드는 노트북 펜이 헬기 소리를 내며 몇 초 정도 렉을 유발(take a couple of seconds) 할 수 있으니 당황하지 마세요!)

```python
In [10]: cv_error = np.zeros(5)
         H = np.array(Auto['horsepower'])
         M = sklearn_sm(sm.OLS)
         for i, d in enumerate(range(1, 6)):
             X = np.power.outer(H, np.arange(d + 1))
             M_CV = cross_validate(M,
                                   X,
                                   Y,
                                   cv=Auto.shape[0])
             cv_error[i] = np.mean(M_CV['test_score'])
         cv_error
```

```python
Out[10]: array([24.2315, 19.2482, 19.3350, 19.4244, 19.0332])
```

As in Figure 5.4, we see a sharp drop in the estimated test MSE between the linear and quadratic fits, but then no clear improvement from using higher-degree polynomials. 
결과를 보면 이론 파트 Figure 5.4에서 귀에 못이 박히게 들었던 뻔한 레퍼토리가 현실로 등판(see) 합니다. 1차 일자 몽둥이에서 2단계 U자 커브(quadratic) 로 기어를 바꿀 때만 에러 점수가 절벽처럼 훅 떨어지는 짜릿함(sharp drop) 이 있지만, 그 뒤로 3단 4단 5단 기어(higher-degree polynomials) 로 암만 모델을 꼬아봐야 점수 향상(clrear improvement) 은 개뿔도 없다는 명백한 팩트 체크가 완료된 셈이죠.

Above we introduced the `outer()` method of the `np.power()` function. The `outer()` method is applied to an operation that has two arguments, such as `add()`, `min()`, or `power()`. It has two arrays as arguments, and then forms a larger array where the operation is applied to each pair of elements of the two arrays. 
코딩 오타쿠들을 위한 1분 상식! 위 코드에서 `np.power()` 뒤에 슬쩍 붙은 `outer()` 란 마법 지팡이(메서드) 를 보셨나요? 이 녀석은 더하기(`add`), 빼기(`min`), 거듭제곱(`power`) 처럼 A랑 B 두 개를 맞짱 뜨게 하는 함수 뒤에 달라붙어 미친 시너지를 냅니다. 원리는 간단해요. A 패거리랑 B 패거리 명단을 척 던져주면, 두 패거리 안의 알맹이들을 '모든 경우의 수(일대일)' 로 서로 일일이 맞짱 뜨게(매핑 결합) 시켜서 거대한 괴물 배열표(larger array) 를 척하고 찍어내는(forms) 꿀템입니다.

```python
In [11]: A = np.array([3, 5, 9])
         B = np.array([2, 4])
         np.add.outer(A, B)
```

```python
Out[11]: array([[ 5,  7],
                [ 7,  9],
                [11, 13]])
```

In the CV example above, we used $K = n$, but of course we can also use $K < n$. The code is very similar to the above (and is significantly faster). Here we use `KFold()` to partition the data into $K = 10$ random groups. We use `random_state` to set a random seed and initialize a vector `cv_error` in which we will store the CV errors corresponding to the polynomial fits of degrees one to five. 
아까 CV 예제에선 극악의 노가다 머신, 즉 $K=n$ (392번 뺑뺑이) 인 LOOCV 모드를 켰었죠? 하지만 우리는 현생을 살아야 하니, 보통은 $K < n$ (10-폴드) 같은 가성비 옵션을 켭니다. 다행히 코드 치는 손맛은 LOOCV 때랑 똑같고 속도는 KTX급(significantly faster) 으로 빨라집니다. 자, 새로운 자동 칼잡이 `KFold()` 를 불러와서 데이터 덩어리를 10조각($K=10$) 으로 깔끔하게 난도질해 줍시다. 여기서도 여지없이 시드 주사위 고정 바늘장치 `random_state` 나사를 조여두고, 1단~5단 성능 비교 점수판을 꽂아둘 점수 통 `cv_error` 를 번쩍 비워 세팅(initialize) 해줍니다.

```python
In [12]: cv_error = np.zeros(5)
         cv = KFold(n_splits=10,
                    shuffle=True,
                    random_state=0) # use same splits for each degree
         for i, d in enumerate(range(1, 6)):
             X = np.power.outer(H, np.arange(d + 1))
             M_CV = cross_validate(M,
                                   X,
                                   Y,
                                   cv=cv)
             cv_error[i] = np.mean(M_CV['test_score'])
         cv_error
```

```python
Out[12]: array([24.2077, 19.1853, 19.2763, 19.4785, 19.1372])
```

Notice that the computation time is much shorter than that of LOOCV. (In principle, the computation time for LOOCV for a least squares linear model should be faster than for $K$-fold CV, due to the availability of the formula (5.2) for LOOCV; however, the generic `cross_validate()` function does not make use of this formula.) We still see little evidence that using cubic or higher-degree polynomial terms leads to a lower test error than simply using a quadratic fit. 
일단 가장 체감되는 건 속도입니다! 방금 전 극악의 노가다 LOOCV를 돌릴 때보다 확 체감될 정도로 쾌속(much shorter) 실행됐을 겁니다. (이론적으로 치면(In principle) 옛날에 배운 최소 제곱법(OLS) 선형 판에서는 (5.2)라는 사기급 치트 공식(formula) 이 있어서 오히려 LOOCV 가 10폴드보다 압도적으로 빨라야 정상입니다. 하지만 파이썬의 이 범용 잡초깎기 공구인 `cross_validate()` 함수는 그런 똑똑한 치트 옵션을 인식해서 가동해 주진 않거든요(does not make use)). 결과를 다시 까봐도 교훈은 불변입니다. 그 어떤 X-Ray를 찍어 봐도 3차나 더 난해한 고차 함수 모형(higher-degree polynomial terms) 들이 기껏 부드러운 2차 커브(quadratic fit) 녀석보다 테스트 정답률을 드라마틱하게 떨어뜨려 준다(leads to a lower test error) 는 티끌만 한 물증(little evidence) 조차 잡지 못했습니다. 결론! 실전 투자든 코딩이든, 오버 튜닝은 뇌절일 뿐이다!

The `cross_validate()` function is flexible and can take different splitting mechanisms as an argument. For instance, one can use the `ShuffleSplit()` function to implement the validation set approach just as easily as K-fold cross-validation. 
마지막으로, 저 `cross_validate()` 함수라는 놈은 입맛대로 기어를 물려주는 아주 개방형 튜닝 변태(flexible) 입니다! 데이터 난도질(splitting mechanisms) 하는 기어 부품만 갈아 끼우면 뭐든 다 되죠. 예를 들어(For instance), 그냥 `ShuffleSplit()` 엔진을 탁탁 꽂아주면? 아까 우리가 1라운드에서 헉헉대며 억지로 손 코딩했던 '고전파 단칼 반반 자르기 쪼갬 세트 검증(validation set approach)' 작전마저도 마치 K-폴드를 돌리는 것처럼 숨 쉬듯 매우 가볍게(just as easily as) 구현 조작(implement) 된다는 엄청난 사실!

```python
In [13]: validation = ShuffleSplit(n_splits=1,
                                   test_size=196,
                                   random_state=0)
         results = cross_validate(hp_model,
                                  Auto.drop(['mpg'], axis=1),
                                  Auto['mpg'],
                                  cv=validation)
         results['test_score']
```

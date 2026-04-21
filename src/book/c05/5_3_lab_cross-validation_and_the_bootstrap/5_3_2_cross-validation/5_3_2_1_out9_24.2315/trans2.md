---
layout: default
title: "trans2"
---

# **`Out[9]:`** `24.2315` 

The arguments to `cross_validate()` are as follows: an object with the appropriate `fit()` , `predict()` , and `score()` methods, an array of features `X` and a response `Y` .
자, 저 마법의 `cross_validate()` 파쇄기 엔진 구멍 안으로 대체 뭘 밀어 넣을까요? 일단 무조건 총알을 장전하고 쏘고 맞히는 삼박자(`fit()`, `predict()`, `score()`) 가 가능한 총기(모델) 객체 하나를 던져야 합니다. 그리고 당연히 데이터 무기 덩어리인 $X$(특성들) 랑, 우리가 끝내 쏘아 맞혀야 할 적군의 심장 타겟 $Y$(정답) 도 한 움큼 멱살 잡아다 처넣어야 하죠.

We also included an additional argument `cv` to `cross_validate()` ; specifying an integer _K_ results in _K_ -fold cross-validation.
여기서 우린 야비하게 `cv` 라는 옵션 조미료(인자) 하나를 더 뿌려줬습니다. 만약 이곳에 $K$ 라는 숫자(예: 10) 를 때려 넣는 순간? 이 기계는 무자비하게 데이터를 $K$ 등분 내버리는 그 악명 높은 '$K$-폴드(K-fold) 교차 검증' 서바이벌 무대로 강제 직행하게 됩니다.

We have provided a value corresponding to the total number of observations, which results in leave-one-out cross-validation (LOOCV).
근데 우린 초반 돌림빵에서 $K$ 자리에다가 그냥 무식하게 "우리 데이터 총 머릿수" 를 통째로 갖다 박아버렸습니다! 이러면 어떻게 되냐고요? 392등분... 네, 맞아요. 그 끔찍하고 무지막지한 "한 놈만 빼고 391명 다 갈아버리자!"라는 리브-원-아웃(LOOCV) 변태 뺑뺑이 모드로 둔갑해 엔진이 비명을 지르며 구동됩니다.

The `cross_validate()` function produces a dictionary with several components; we simply want the cross-validated test score here (MSE), which is estimated to be 24.23.
다행히 이 기계가 굉음을 내며 돌아가고 나면 이것저것 파편들을 쏟아내는데, 우린 다 쓸데없고 오직 하나, "결과적으로 에러 점수(MSE) 가 몇이냐?" 는 성적표만 쏙 뽑아냅니다. 까보니 24.23 레벨의 절망적인 방어율을 보여주네요.

We can repeat this procedure for increasingly complex polynomial fits.
저 끔찍한 뺑뺑이 막노동을 고작 1차 선형 모델(직선) 에만 쓰고 버리긴 아깝죠. 무기에 2차 폭탄, 3차 폭탄, 4차 폭탄(고차 다항식) 을 점점 기괴하게 덕지덕지 달아가며 이 미친 실험을 계속 똑같이 반복 재생시킬 수 있습니다.

To automate the process, we again use a for loop which iteratively fits polynomial regressions of degree 1 to 5, computes the associated crossvalidation error, and stores it in the _i_ th element of the vector `cv_error` .
손가락이 아프니 파이썬의 매크로 국룰, `for` 루프 반복문를 돌려버립시다! 1차 무기부터 출발해 5차 빔 무기까지 단계별로 차례차례 돌면서 무기를 세팅하고(fits), 각 턴마다 교차 검증 뺑이를 돌려 터져 나온 에러 점수를 딱딱 계산한 뒤(computes), 그걸 미리 준비한 계란판(`cv_error` 벡터 빈 방) 의 $i$ 번째 칸마다 쏙쏙 박아 저장(stores) 해치웁니다.

The variable `d` in the for loop corresponds to the degree of the polynomial.
반복문 안에서 펄떡거리는 `d` 라는 번호표 알파벳은, 지금 내가 차고 있는 무기가 허접한 1차인지 미친 5차인지를 결정하는(corresponds to) 권력(승수) 입니다.

We begin by initializing the vector. This command may take a couple of seconds to run. 
자, 점수를 담을 빈 계란판(벡터) 을 세팅하며 이 미친 뺑뺑이 매크로를 켤 건데... 경고합니다. 392번 회전(LOOCV) 을 5가지 무기로 돌리니까 총 1,960번을 당신의 불쌍한 가성비 CPU가 돌려야 합니다. 엔터를 치고 나면 몇 초 동안 컴퓨터가 멈춘 듯 "위이이잉" 거릴 테니 쫄지 말고 커피 한 모금 하세요!

```python
In [10]: cv_error = np.zeros(5)
         H = np.array(Auto['horsepower'])
         M = sklearn_sm(sm.OLS)
         for i, d in enumerate(range(1, 6)):
             X = np.power.outer(H, np.arange(d+1))
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
허허, 전에 5.4 챕터 도안에서 봤던 그 코미디 같은 광경이 코드로 돌려봐도 징그럽게 또 판박이처럼 연출되네요. 멍청한 직선(1차) 에서 U자 곡률(2차) 무기로 템을 딱 스왑하자마자 에러 타율 점수가 24.23에서 19.24로 엄청나게 수직 방어 낙하(sharp drop) 를 하며 대박을 치는데... 막상 그 뒤로 "우왕! 그럼 3차 4차 5차 극딜 가자!" 하고 템빨을 쑤셔 박아도, 정작 점수는 19점대 언저리에서 더 떨어지진 않고 깔짝대기만 할 뿐 그 어떤 눈물겨운 이득(improvement) 도 나오질 않는 삽질 포인트를 볼 수 있습니다. 

Above we introduced the `outer()` method of the `np.power()` function.
아까 뺑뺑이 돌리던 코드 안쪽에서 기괴한 슬라임 같은 녀석이 하나 숨어 있었죠. `np.power()` 권능 함수 엉덩이에 붙어있던 `outer()` 라는 스킬 메서드가 그것입니다.

The `outer()` method is applied to an operation that has two arguments, such as `add()` , `min()` , or `power()` .
이 `outer()` 라는 맹독 스킬은 원래 덧셈(`add`), 더 작게 후려치기(`min`), 제곱 뻥튀기(`power`) 처럼 "야, 나한테 조각 두 개 가져와!" 라고 요구하는 깐깐한 양방향 함수들(투 인자 체제) 한테만 철딱서니 없이 덧입혀져서 작동(applied to) 하는 독특한 녀석입니다.

It has two arrays as arguments, and then forms a larger array where the operation is applied to each pair of elements of the two arrays. 
이놈한테 큼지막한 두 덩이의 배열 조이스틱을 입력 인자로 먹여버리면? 이 미친 장치는 그 거대한 a 덩어리의 첫 번째 조각 애와 b 덩어리의 첫 번째 애를 붙여 패고, 또 첫 번째 애랑 두 번째 애를 붙여 패고... 식으로 아예 두 세트 내 모든 병력끼리 서로 **일대일 난투 매칭 쌍둥이(each pair) 결전**을 조장해 붙여버립니다. 그 결과? 어마무시하게 커진 거대한 새로운 척도 매트릭스 그물망 판(larger array) 을 토해내며 결론(forms) 을 구축해버리는 엄청난 노가다 파괴 장비입니다.

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

In the CV example above, we used _K_ = _n_ , but of course we can also use _K < n_ .
자, 근데 위에서 미친 CPU 갈구며 놀았던 건, K값을 무식하게 인구수 총합 n이랑 똑같이 만든(즉, K=n) LOOCV 방식이었죠. 하지만 제정신 박힌 사람이라면 당연히 $K < n$ (즉 K=5, K=10 같은 다이어트 방식) 으로 몸 비틀기를 써먹을 수 있습니다.

The code is very similar to the above (and is significantly faster).
코드 작성법은? 방금 짰던 거에서 거의 복붙 수준으로 존똑입니다! (게다가 LOOCV처럼 무식하게 1,960바퀴 안 돌고 깔쌈하게 딱 50바퀴만 도니까 미치도록 엄청나게 빠른 엄청난 쾌속 속도 결말을 안겨주죠!).

Here we use `KFold()` to partition the data into _K_ = 10 random groups.
여기서는 마침내 `KFold()` 라는 치트키 함수를 발동시켜, 불쌍한 데이터를 $K=10$ 개의 랜덤 포로수용소 구역으로 갈기갈기 난투 쪼개버립니다(partition).

We use `random_state` to set a random seed and initialize a vector `cv_error` in which we will store the CV errors corresponding to the polynomial fits of degrees one to five. 
당연히 로또 돌리는 수준이라서 운빨을 잡으려고 `random_state` 난수 시드 박제를 걸어뒀고요. 아까처럼 1단부터 5단까지 무기를 업그레이드할 때마다 터져 나오는 그 징그러운 CV 타율 점수들을 박아 모을 깡통 박스 `cv_error` 를 준비해 두는 것도 잊지 않습니다.

```python
In [12]: cv_error = np.zeros(5)
         cv = KFold(n_splits=10,
                    shuffle=True,
                    random_state=0) # use same splits for each degree
         for i, d in enumerate(range(1, 6)):
             X = np.power.outer(H, np.arange(d+1))
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

Notice that the computation time is much shorter than that of LOOCV.
어때요? 엔터 치자마자 결과가 튀어나오죠? 방금 전 내 컴퓨터를 이륙시키려 했던 무식한 막노동 LOOCV에 비해, 이 10-fold 방식은 정말 눈물 날 만큼 연산 대기 시간 구간 폭이 엄청나게 소름 돋게 산뜻 짧고 맹랑 쾌속으로 속결 끝장 돌파(much shorter) 해버렸다는 그 감격스러운 대목을 실감하시기 바랍니다!

(In principle, the computation time for LOOCV for a least squares linear model should be faster than for _K_ -fold CV, due to the availability of the formula (5.2) for LOOCV; however, the generic `cross_validate()` function does not make use of this formula.)
*(아, 팩트 폭격 하나 하고 갈게요. 원래 이론 교과서(5.2식) 대로라면 특수 상황(최소 제곱 선형 모델) 에서는 마법 공식 치트가 통용되므로 LOOCV가 사실 K-fold보다도 압도적으로 광속으로 끝나야 정상입니다! 근데 우리가 쓰는 이 파이썬 라이브러리의 무수히 단조로운 `cross_validate()` 멍청이 함수 장치가 그 잘빠진 우회 치트 공식을 못 알아먹고 철저히 기동 거부(does not make use of) 하며 생으로 멍청하게 반복문 짐수레만 돌리고 앉아 있다 보니; 이 치트가 씹혀서 결국 10-fold 가 실전파에선 이겨버린 뼈아픈 역전 촌극 상황일 뿐입니다!)*

We still see little evidence that using cubic or higher-degree polynomial terms leads to a lower test error than simply using a quadratic fit. 
뭐 컴퓨터가 고생하든 말든 결론은 아까랑 또 똑같이 도돌이표네요. 그저 얄팍한 2차 곡률 세팅 장비랑 비교했을 때, 거창하게 3차니 4차니 삼제곱이네 하며 미친 듯 무기 곡률을 끌어올려 덕지덕지 써재껴 본들, 정작 "어? 그래봤자 실전 야생 테스팅 타율 에러 방어율 수치가 눈에 띄게 밑바닥으로 떨어지긴 커녕 거기서 거기 아냐?" 라며 비아냥대는 현실 참사(little evidence) 의 뼈 때리는 벽 한계를 다시금 처절히 깨닫게만 해줍니다. 

The `cross_validate()` function is flexible and can take different splitting mechanisms as an argument.
이 사이킷런의 메인 포탑 엔진인 `cross_validate()` 평가 함수 툴은 워낙 고무줄처럼 신축성에 달하고 유들유들 변태(flexible) 같아서, 그냥 무식한 K-폴드 말고도 온갖 신기한 데이터 절단 쪼개기 도구 부속품 메커니즘 옵션 톱니들을 자기 입구 인자(argument) 세팅 속으로 스르륵 잘도 받아먹고 삼켜(can take) 버립니다. 

For instance, one can use the `ShuffleSplit()` function to implement the validation set approach just as easily as K-fold cross-validation. 
그러니, 아까 그 원시적인 5.3.1 구역에서 했던 구닥다리 반피 나누기, 즉 '검증 세트 쪼개기' 짓거리 역시도 방금 본 K-폴드 치트만큼이나 너무 쉽고 만만 거뜬 깔쌈하게 동일 전격 모방 투여 재현(just as easily) 해 낼 수 있습니다. 그 방법은 그냥 `ShuffleSplit()` 이라는 섞기 스킬 함수 부품만 턱 하니 입구에 넣어주면 끝나는 거죠!

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

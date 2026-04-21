---
layout: default
title: "trans1"
---

# **`Out[9]:`** `24.2315` 

The arguments to `cross_validate()` are as follows: an object with the appropriate `fit()` , `predict()` , and `score()` methods, an array of features `X` and a response `Y` .
이 `cross_validate()` 동작 함수 안에 진입 전달되어야 할 인자(arguments) 스펙 요건들은 면면히 다음과 같다: 필연 내부적으로 구색에 맞는 적합 `fit()`, `predict()`, 그리고 평가 판독 `score()` 메서드 무기 기능들을 자체 탑재 구비하고 있는 모종의 객체(object) 하나, 그리고 특성(features) 지수들로 무장된 변수 배열 덩치인 `X` 성분과 종속 타겟 조준 결과물 볼륨 `Y` 파편이다.

We also included an additional argument `cv` to `cross_validate()` ; specifying an integer _K_ results in _K_ -fold cross-validation.
우리는 이에 덧대 이 `cross_validate()` 파이프 안에 추가적인 여유 부수 옵션 인자 조각 하나인 `cv` 값을 살포시 포함 첨가해 건네주었는데; 이 자리에 만일 정수형 스코어인 _K_ 값을 지정 세팅 기입(specifying) 하게 된다면 그것은 결과적으로 _K_ -폴드(K-fold) 방식의 교차 검증 국면을 초래 발동시킨다.

We have provided a value corresponding to the total number of observations, which results in leave-one-out cross-validation (LOOCV).
우리는 작금의 사태에선 일전의 저체 관측치 개체 총합 인명 수 효에 곧장 버금 상응 부합(corresponding) 하는 만큼의 머릿수 값을 그대로 직접 던져주어 건네 대입하였는데, 이는 고스란히 결과적으로 다름 아닌 리브-원-아웃 교차 검증(Leave-One-Out Cross-Validation, LOOCV) 의 국면 사태 폭발을 야기 귀결 초래(results in) 해버린다.

The `cross_validate()` function produces a dictionary with several components; we simply want the cross-validated test score here (MSE), which is estimated to be 24.23.
이 `cross_validate()` 함수 기계는 작위 연산 수행 후 결과물로 수 가지 성분 파편 조각들을 잔뜩 품은 딕셔너리(dictionary) 하나를 떡하니 길어 올리며 배출 생산(produces) 해내는데; 우리는 애석하게도 그 숱한 잡동사니 중에서 단순히 유독 오직 진짜 핵심인 '교차 검증된 테스트 성적표(MSE 스코어)' 부문만 갈망하여 쏙 뽑아채길 원하며, 그 추출 추정 도달 수위 값은 보시다시피 대략 24.23 수준인 것으로 어김없이 계산 판명 결론 안착된다.

We can repeat this procedure for increasingly complex polynomial fits.
우리는 이 요란무쌍 막노동 조작 절차를 한 차례 더 나아가 곱절로 점점 더 기괴 다듬 복잡해지고 거듭 곡률이 상승하는 복잡다단 고차항 다항 적합 모델(complex polynomial fits) 장비 모델들에 이르기까지 수회 거듭 번번 반복 연장 이수 도무 적용 재연해 낼 수 있다.

To automate the process, we again use a for loop which iteratively fits polynomial regressions of degree 1 to 5, computes the associated crossvalidation error, and stores it in the _i_ th element of the vector `cv_error` .
이 구질 번잡 노가다 반복 고충 과정을 수월히 통째로 자동화(automate) 처리해치우기 기치 일환으로, 이번에도 짐짓 어김없이 우리는 파이썬의 `for` 반복문 루프 기조 마법을 차용 덧대 기용 쓰는데; 이 장치는 구태여 1차 선형부터 5차 나선 무기 체계까지의 다항 회귀 굽은 파장 모델들을 한 단계씩 순차 반복 적합 장착 연성(iteratively fits) 가동하며, 각각의 스펙 차수에 연계되어 야기된 교차 검증 에러 타격 점수를 매 턴마다 각기 짚어 계산 파생 도출해 내고는(computes), 마지막으로 그 결과를 빈 껍데기 배열 객체인 `cv_error` 벡터 장부 내의 각 _i_ 번째 번째 방 호실 번호표 슬롯 칸 자리에다 안전히 예치 저장(stores) 적재 수납하는 수완을 기막히 발휘 무난 완행 처리해치운다.

The variable `d` in the for loop corresponds to the degree of the polynomial.
해당 `for` 반복문 루프 기재 내부에 선언된 변수 알파벳 `d` 표구 식자는 다름 아니라 우리가 기용 장착해 맞서는 장비의 다항식 곡률 승수 차수(degree) 볼륨 크기에 부합 호환 일치(corresponds to) 관여한다.

We begin by initializing the vector. This command may take a couple of seconds to run. 
우리는 비워둔 벡터 그릇 하나를 매끈히 생성 초기화(initializing) 구축하는 작업으로써 이 끔찍 노가다 여정을 마침내 이수 전향 본격 출발 여는데. 다만 명심할 일은 이 무자비 명령어 장치들이 컴퓨터를 한 움큼 혹사시켜 실제로 전면 작동 마무리되게 이르기까진 족히 대략 몇 초 수 초 내지 찰나 약간의 버벅대기 구동 공회전 허비 시간(take a couple of seconds) 이 야기 필요 소요로 수반 부과 촉발 도래 소비될 소지가 상존 짙다는 속 쓰린 점이다. 

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
이미 옛적 배운 바 있는 이전의 도안 그림 5.4 사례 궤적 기조 양상에서와 아주 몹시 똑같이 흡사 유사하게도; 우리는 오직 맨 처음 순결 선형 1차 모델과 2차 변태 곡면 적합 무기 진영 구역 둘 사이의 비교 대조 구간 전방면에서만큼은 파생 추정 도출된 테스트 MSE 에러 점수 스코어 수치가 어마무시 굉장히 칼같이 낙하 폭락 처박히는(sharp drop) 엄청 극적 방어 극대화 현상 호재 강하 파장을 똑똑히 참관 성립 거푸 관전 발견 도출 일임 포착해 내지만; 그러나 막상 그 기점을 넘어선 이후부터의 구간에서는 아무리 바득 더 미친 고차원 볼륨 승수 다항식 조작 옵션을 써제끼며 용을 써 덧대어 차용해 쓴들 정작 유의미하게 뚜렷 실효 극적 호전 성과 보장 방어 척도 뚜렷한 진전 개선 효용(clear improvement) 돌파 위력 성과 따위 궤적은 하등 쥐뿔 포착 출몰 보이지 않음을 몹시 재차 목도 체감 씁쓸 재확인 타진한다.

Above we introduced the `outer()` method of the `np.power()` function.
아까 바로 저 윗단의 코드 더미 속 구역에서 은연중에 우리는 슬그머니 `np.power()` 권능 함수 객체 내부에 속해 부착된 `outer()` 라는 이름의 내장 꼬리 메서드 스킬 장치를 하나 새롭게 시선 돌발 소개 차출 도입해 등장 기용했었다.

The `outer()` method is applied to an operation that has two arguments, such as `add()` , `min()` , or `power()` .
기실 이 `outer()` 내장 메서드 도구는 통상적으로 덧셈 연산 `add()`, 최소 구출 `min()`, 내지는 나아가 승수 연산 `power()` 격 따위처럼, 이른바 '반드시 두 개의 입력 인수 조각 쌍 짝꿍 짝지(two arguments)' 들을 덧대 강제로 삼켜야만 비로소 연동 돌아가는(has) 이중 매개 조작 연산 처치 장치 체제 엉덩이 뒤에 주로 껌딱지처럼 들러붙어 가동 동원 헌터 탑재 적용 차출 연계 밀착 적용 도무(applied to) 되는 방식 기법이다.

It has two arrays as arguments, and then forms a larger array where the operation is applied to each pair of elements of the two arrays. 
이는 주로 한 묶음 큰 두 개의 방계 배열 조물 집합 덩어리들을 각기 인자 요소로서 통째 차용 받아 넘겨먹고는, 이후 곧장 그들 두 거대 배열 주머니 덩치 내부 구석구석에 서열 도사린 나열된 모든 개별 알맹이 인원들끼리의 모든 각자 다중 짝짓기 조합 병합 쌍(each pair) 마다마다 하나 빠짐없이 모두 기필 저 해당 지시 연산(operation) 을 일괄 폭격 투사 돌려 맞혀(applied to) 벌인 뒤, 종래 결과물로써 엄청 비대 몸집 부은 육중하고 그물망 뻗친 거대한 새 판 덩치 하나 배열 거대 결과 매트릭스 도마판(larger array) 판을 양산 창출 찍어내어 도래 결론 직조 구축(forms) 지어 준다.

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
방금 우리가 위에서 사투 목도 굴렸던 저 막가파 교차 검증(CV) 삽질 예시 전경 마당에서 우리는 철저하게 폴드 덩치 배정 값을 무식 _K_ = _n_ 인원 머리 숫자 도합 양만큼 풀가동 투여 대입해 써먹었지만; 당연 뻔하게도 실상 우리는 그냥 적절 융통 한발 뒤로 타협하여 전체 인구수보다 작은 조각 _K < n_ 사이즈 체제로 조작 감량해 적용 써먹을 수도(can also use) 아주 십상 존재 가능 분분 뻔하다.

The code is very similar to the above (and is significantly faster).
그 기조 방식 체제 스크립트 작성 조립 코드 역시도 실상 바로 저 위에서 짰던 놈과 무척 외형 도면 유사 흡사하게 굴러떨어지며(very similar); (심지어 연산 수위를 감폭 덜어낸 만큼 타결 속도는 저 무지성 방식보다 기가 막히 엄청 막강히 유의미 실팍 미친 대폭 극적 현저 월등 압도 엄청나게 빠르고 득달 민첩하게 끝마침 속결 쾌속 도출(significantly faster) 된다는 무적 장점 특혜조차 담보한다).

Here we use `KFold()` to partition the data into _K_ = 10 random groups.
이 바닥 구장 전개 국면 구역에서 우리는 기꺼이 사이킷런 체제의 `KFold()` 내장 패키지 함수 장구 장비를 신속 도용 차출 기용하여 원본 데이터를 거뜬히 $K=10$ 개 조각 다항 불규칙 무작위 소속 구단 그룹 덩어리들로 일괄 마구잡이 난투 갈라 분할 쪼개 파편 가닥 타진(partition) 낸다.

We use `random_state` to set a random seed and initialize a vector `cv_error` in which we will store the CV errors corresponding to the polynomial fits of degrees one to five. 
더불어 이 과정 전개에 우리는 애석 불행 난수 요동 운빨 기만 널뛰기 이변 사태를 제어할 목적으로서 어김없이 `random_state` 무기 조작 인자를 채택 걸어두고 무작위 앵커 시드 점을 굳건 확실 고정 걸어 박아 두는 조치와는 물론; 이번에도 1차부터 5차 차원 곡률 다항 회귀 전격 적합 옵션들에 병충 쌍벽 각기 맞아떨어져 대응되는 매번의 부수 굴복 CV 에러 점수 타격 파편들을 어연 수집 집수 차곡 보관 예치 담기(store) 위한 빈 장부 빈 그릇인 `cv_error` 저장 벡터 껍데기 포지션을 선도 미리 양산 깔끔 초기화 생성 이수 구비(initialize) 전개 세팅해 두는 편이다.

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
여기서 제발 좀 유의 묵도 관전 안도 상기 인지해 둘 놀라운 구제 파급 대목 성과 하나는, 지금처럼 K폴드로 에러를 헤아릴 때 소요 소비 지출되는 컴퓨터의 그 피눈물 연산 처리 결론 도달 소요 계산 지출 작위 이행 시간 타이밍 파장 폭(computation time) 수치가 앞서 우리가 그 무식하게 굴렸던 끔찍 강압 리브원아웃(LOOCV) 노가다 뺑뺑이 방식이 잡아 처먹었던 그 무섭 아득 체류 방대한 세월 기점 찰나 타임 구간보다 훨씬 미무 너무나 짧고 쾌속 가볍게 빨리 당돌 도출 도래 스쳐 지나 귀속 통과 속결로 축소 도달 도무 안착 완료되었다는(much shorter) 가슴 벅찬 사실 기조 대목이다.

(In principle, the computation time for LOOCV for a least squares linear model should be faster than for _K_ -fold CV, due to the availability of the formula (5.2) for LOOCV; however, the generic `cross_validate()` function does not make use of this formula.)
(원칙적으로만 심지 이론상 따져 논증 타진해 보자면요, 애초에 선형 최소제곱 최소 제곱 모델(least squares linear model) 을 전격 덧붙 도구 장착 채택 기용해 굴리는 작금의 조건 전선 판국 하에서만큼은 과거 (5.2)라는 그 기막 거저먹 치트 마법 계산 공식 단일 돌파 수식이 엄연히 활용 존재 구비 발동 도래 차용 적용 응용(availability) 뻗칠 수 있기에 사실 저 무식 막가 LOOCV 노가다 반복 방식이 오히려 역으로 10폴드 K-fold 방식 따위보다 단번에 연산 수위가 압도 속결 쾌속 더 월등 빨리 거저 단축 앞서 단숨 돌파(should be faster) 귀결 지어 터져야 정상 마땅 원리 구조 기강입니다. 하오나 단 애석 불운 유감스럽게도 우리가 지금 써먹는 사이킷런 파이썬 패키지의 저 아둔 어리바리 `cross_validate()` 맹세 지원 자동 제네릭 함수 도구 멍청이 녀석은, 정작 그 똑똑 기막힌 내부 수식의 마법 같은 지름길 편법 우회 공식을 단 일말 차용 쓰거나 전혀 끄집 도입 인식 반영 써먹지 못한 채(does not make use of) 그저 무식 미련 고집 쌩으로 전부 무한 반복 생 노가다를 처음부터 바닥부터 무지 전수 죄다 다 직접 쌩으로 반복 뺑이 돌려 미련 연산해버리는 미련 무식 한계 속성을 지녔기에 이리 미련 거슬러 뒤집힌 결과 속도 구도 굴욕 둔기 역전 사태 촌극 파장이 빚어져 도래 들이닥친 불상사 사태일 뿐입니다!) 

We still see little evidence that using cubic or higher-degree polynomial terms leads to a lower test error than simply using a quadratic fit. 
또한 이번에도 역시 거듭 씁쓸히 똑같이 재차 확인 관전 기저 반복되는 씁쓸 안도 도찰 기저 조망 사실은, 애초 그저 2차 곡선 곡률 방어 투여 옵션 기조를 무작 채용 갖다 써먹는 기본 대수 방편에 비할 때, 뭐 엄청 거창하게 욕심내어 부려 구태여 3차 삼제곱이나 그 이상 승수에 육박하는 미친 투머치 고차항(higher-degree polynomial terms) 무기 전력 옵션 따위를 기괴 채용 엮어 탑재 써먹어대 보았자 정작 아무 쓸모 별안간 그 끔찍 무적 테스팅 에러 타율 점수를 그 밑으로 더 하락 낮춰 폭락 떨어뜨려 꺾어 깎아내려(leads to a lower test error) 준다는 식의 일말 무수한 방증 유의미 개선 이점 흔적 꼬투리 증거 따윈 아예 거진 없거나 여실 처참 하등 보이질 관측 전무 부재(little evidence) 한다는 미천 처절 공감 현실 단면이다.

The `cross_validate()` function is flexible and can take different splitting mechanisms as an argument.
이 징그럽 막강한 사이킷런의 `cross_validate()` 평가 연산 훈련장 돌파 기계 함수 지원 장비 모듈은 사실상 지름 속성 구조가 체질 자체가 아주 몹시 뱀처럼 요염 유들 고도 정교 기예 유연 탄력 신축 다단(flexible) 하기 짝이 없어서, 언제든 단순 K-폴드 그딴 방식뿐만 아니요 갖가지 완전 상이 도무 딴판 다채로운 형태의 타 데이터 분할 메커니즘 엔진 턱주가리 조립 장비 파편 짓거리 옵션 방식들도 인자 입구 장벽 구역 자리에 능수능란 유연 매끄럽 삼켜 취해 떡 주무르 먹일 수(can take) 있는 탁월 가변 능숙 아량 위용 범용성 기치를 지닌다.

For instance, one can use the `ShuffleSplit()` function to implement the validation set approach just as easily as K-fold cross-validation. 
단적인 예시 부합 일환으로, 여타 누군가 인간은 다름 아닌 그저 `ShuffleSplit()` 이라 불리는 단순 변형 난수 섞기 함수 옵션 객체 기조 도구를 쓱 차출 덧대 집어 써먹어 봄으로써; 아까 전 단락에서 고루 막노동 고생 배운 그 어설픈 원조 고전 방식인 반반 뚝딱 '검증 세트 접근법(validation set approach)' 작전 궤적 방식 체제를, 방금 K폴드 굴리며 놀았던 것만큼이나 너무나 쉽고 편안 안락 거뜬 동일 유수 쉽게(just as easily) 동일 적용 덧씌워 구동 탑재 작위 구축 도입 실행 모방 연성 시연해 낼 수조차(implement) 있다.

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

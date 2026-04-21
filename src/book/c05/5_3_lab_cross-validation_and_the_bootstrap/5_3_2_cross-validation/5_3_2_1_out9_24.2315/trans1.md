---
layout: default
title: "trans1"
---

# `Out[9]:` `24.2315`

The arguments to `cross_validate()` are as follows: an object with the appropriate `fit()`, `predict()`, and `score()` methods, an array of features `X` and a response `Y`. We also included an additional argument `cv` to `cross_validate()`; specifying an integer $K$ results in $K$-fold cross-validation. We have provided a value corresponding to the total number of observations, which results in leave-one-out cross-validation (LOOCV). The `cross_validate()` function produces a dictionary with several components; we simply want the cross-validated test score here (MSE), which is estimated to be $24.23$. We can repeat this procedure for increasingly complex polynomial fits. To automate the process, we again use a for loop which iteratively fits polynomial regressions of degree 1 to 5, computes the associated crossvalidation error, and stores it in the $i$th element of the vector `cv_error`. The variable `d` in the for loop corresponds to the degree of the polynomial. We begin by initializing the vector. This command may take a couple of seconds to run. 
`cross_validate()` 함수에 할당되는 인자(arguments)의 목록은 다음과 같습니다: 적절한 형태의 `fit()`, `predict()`, 그리고 `score()` 메서드를 함께 구비한 체계적인 객체, 스펙 특징 변수 성향의 묶음 배열 `X` 그리고 거기에 상응하는 판독 반응 결괏값 `Y`. 덩달아 우리는 추가 인자 조건 `cv` 지정을 `cross_validate()` 부름 절차상에 하나 더 귀속(included) 시켰습니다; 이것을 일정치의 정수 $K$ 로 구체화 지목 명시하는(specifying) 행위는 여타 $K$-폴드 교차 검증 절차 구동 성과를 유도 창출(results in)해 냅니다. 이번 예제에서 우린 저 항목군 내에 정확히 전체 관측물 표본 숫자 덩어리와 합치상응(corresponding to)하는 크기 단위를 찔러 넣었으며(provided), 이는 필연적으로 단일 관측치 제외 교차 검정, 즉 철절한(LOOCV) 작업 발동에 안착합니다(results in). 저 `cross_validate()` 가동 함수 지는 여러 가지 구성 파생 조합 컴포넌트를 함유 보유한 딕셔너리 구조체 목록을 분출해내게(produces) 됩니다; 다만 우리가 여기서 진정 갈취하길 희망하는 건 순수 교차 테스트 스코어인 (MSE) 단 하나뿐이며, 해당 결과 추정 산출물은 $24.23$ 이란 점수로 타진 검정(estimated) 되었습니다. 우리는 보다 더 복잡 난해하게 구성 짜인 고단계 다항식 융합 모형(polynominal fits)에 향해서도 본연의 회기 테스트 절차 반복 가동을 추구할 수 있습니다. 해당 밟아가는 전반 공정을 기계 통제로 전격 가동 자동화(automate) 체제로 이룩하고자, 우리는 다시 순환 포 회전 구문(for loop)을 꺼내들며 차근차근 1단계 차수부터 5형 차수에 이르기까지 다양한 다항식 결부 회귀 모형군을 중첩 체계로 빙빙 투과 반복 돌려(iteratively fits) 가동할 수 있는데, 이는 각 연관 도출 교차 오류 지수를 끄집어내는 전산 계산(computes) 처리 역할을 감당함에 더해져 그것의 결과 추산물을 향후 저장소 `cv_error` 구역의 $i$번째 방에 순차적 차곡 적재 보관해줄(stores) 것입니다. 당해 구동문 구조 내부 루프 내 포진한 타겟 변형 지표 변수 `d`는 본연적 뼈대 다항식의 각 등급 차수 조율을 상징 반영(corresponds to) 합니다. 우리들은 그전에 제일 먼저 저장 장치 벡터 공간 선별 규합 초기화(initializing) 작전을 착수하는 것으로 전반을 출범합니다. 이 코딩 가동 명령어 집합은 현실 구동 마칠 때까지 통상 몇 초가량의 약간 소요 실행 시간 텀을 야기 소비(take) 할 수도 있습니다.

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
이미 Figure 5.4 단락 국면에서도 직관 인지했듯(As in), 우리는 본 결과 안에서도 뻣뻣한 일자 선형과 부드러운 U-커브형(이차 핏) 결합 구간 이동상에서만 도출 산출(estimated)된 테스트 관측 MSE 결과 오류의 기록적 낙폭 하락 저공 침강세(sharp drop) 를 확연히 시각 발견 검정(see)합니다, 그러나 애석하게도 차후 후열에 들어선 3기 4기 그 이상 단계 차원 대의 극고차수 다항 곡선식 채택 용역 등용(using higher-degree polynomials) 으로는 어떠한 두드러진 실성적 지표 향상 진전(clrear improvement) 상황도 추가 이끌지 못함을 적발 인지하게 됩니다.

Above we introduced the `outer()` method of the `np.power()` function. The `outer()` method is applied to an operation that has two arguments, such as `add()`, `min()`, or `power()`. It has two arrays as arguments, and then forms a larger array where the operation is applied to each pair of elements of the two arrays. 
앞 과정 상단(Above) 단락을 통과 중 우리는 함수 공구 요소인 `np.power()` 내부에 장착 구비된 보조 객체 기능 단위인 `outer()` 작동 기믹 메서드를 임시방편 신규 소개 도입(introduced)하였습니다. `outer()` 메서드 도구는 통상적 두 개 양쪽 인자 지표(two arguments)들을 공조 결합 병행 대등 보유 운영하는 덧셈 추가 `add()`, 극소 파악 `min()`, 이나 누승 지수 산출 작동 체제인 `power()` 형태 일련 계산 작용 활동상에 폭넓게 적용 부가 수용(applied to) 됩니다. 이는 초기 투입으로 두 쌍 결합 계통 요소 배열 뭉치(arrays)들을 기본 인수 자격분으로 흡수 취합한 이후, 종국적으로 두 진영 집합 내 배열 편제 속 구성 각 요소 인물 짝 맞춤별 결합(each pair of elements) 쌍 구도 단상 위로 덮어씌워 부가시킨 가동 실행 작용이 폭넓게 연루 조치된 한 단계 체급 불려 성장 조성된(forms) 비대 확장 배열체 산물 덩어리를 생성 구축시킵니다.

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
앞서 지나쳤던 CV 교차 검정 코딩 전개상 위 구도에서 우리는 일시적으로 극치 타깃 스코어 $K = n$ 체계를 조작 설정해 넣었으나, 물론 지당하게도 우리는 $K < n$ 방식 수위 조절도 능히 교체 도입 투입 가능합니다. 이 수정 작동법 투입된 스크립트 코드 전반 편제 양상 구조도 기실 초회 위와 대조해 보더라도 대단히 밀접 유사할 따름이며 (무엇보다 극도로 신속 가동(significantly faster) 된다는 장점이 부가됩니다). 이곳 새 작전 코너판 우린 전체 기반 데이터 더미 파이를 향해 무작위 $K = 10$ 진영 분할 갈라치기(partition) 쪼갬을 행할 의도로 `KFold()` 시스템 기구를 새로 소환 발령합니다. 뒤이어 우리들은 여지없이 시드 난수 고정을 담보해 찍어줄 도구 `random_state` 를 채비함에 병행하여, 뒤어어 1위부터 5위 등급 각 단계 층위에 차곡 매핑 대응 배당 고착시킬(corresponding to) 교차 에러 분석 도출분 오류(CV errors) 결과 찌꺼기들을 전부 취합 누적 적재시켜 담을 장바구니 빈 공간 즉 벡터 배열 저장고 `cv_error` 를 전원 초가 개통 환기(initialize)해 가동 배정합니다.

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
일단 전면에 두드러진 바로 이 연산 소비 시간상 비용 궤적이 조금 전 저 노가다 끝판왕 LOOCV의 전개 상황 때보다 압도적으로 체감되듯 극저하(much shorter) 감소했다는 사태 자체에 우선 주의 깊게 감지(Notice)하여 주십시오. (원리를 따져 파고들자면(In principle), 가장 편한 구도인 최소 제곱형 단순 직선 모델 전장에서 구동되는 LOOCV 가동을 위한 연계 연산 작동 처리 공정 속도는 애당초 (5.2)란 막강한 속성 돌파 지원 공식 공식의 채용 보장 활용이 뒷받침 지원 허가(availability)된 바 있음에 따라 오히려 상대 진영인 $K$-폴드 팀 구동 스피드를 상회 능가 앞질러 발휘(faster) 되어야만 마땅합니다. 허나, 일반 범용적 제너릭 부류 함수 공구 형태 성격인 현 `cross_validate()` 시스템 틀 구조 내부 자체의 속성상에서는 융통성 한계로 말미암아 치명적 저 패스워드 편법 공식 수혜적 우위(Does not make use of this formula)를 자율 통달 인지 식별해 구동 도용 접합 활용치 않음으로써 이런 이변이 파생합니다.) 우리들은 다시 재검 여전히 차기 등급 대의 지표선, 3형 입체항 구조나 부가적 점철 증폭 고차 다항식 층위 함수 요소를 차용하는 시도 자체가 결단코 단지 기초 2차 유동 커어브를 다루어 적적 수용함(simply using a quadratic fit)보다 낮고 이상적인 결과 에러 하락 지표 점수를 초래 수여(leads to)할 수 있다고 확신 장담 주장해낼 하등 어떤 그럴싸한 여지나 물증 근거 기반 지수 단서들(little evidence)조차도 결국 이번 판에서도 역시 건져내지 포착할 길이 보이지 않는 잿빛(see little evidence) 상태라는 점을 지속 확인 겹쳐 맞이하게 됩니다.

The `cross_validate()` function is flexible and can take different splitting mechanisms as an argument. For instance, one can use the `ShuffleSplit()` function to implement the validation set approach just as easily as K-fold cross-validation. 
마지막으로 덧붙이자면(Furthermore), 당해 도구 `cross_validate()` 내장 함수 기능 도구는 매우 유연(flexible) 자유분방한 조립성을 구축 지니고 있어 이것의 입력 인자 입 주둥이 구멍(argument) 안쪽에 사용자가 독단 체제 마련한 제각각 판별 분해 다각적 기믹 분할 통제 모터 궤도(different splitting mechanisms) 작동 규준들을 자율 할당 이식 부과 접합 수용(can take)해 처리 연동케 합니다. 단언하건대 한 예 구체 실사로(For instance), 여러분 즉 누구라도(one can) 이 `ShuffleSplit()` 무작위 짬뽕 기능 모터 엔진 도구를 착취 가동 부과시켜 당해 K-분할 뺑뺑이 전개만큼이나 수월하게 편할(just as easily as) 뿐더러, 고전 유산 산물격 방식인 단순 단절 반절 자르기 쪼갬 세트 검증(validation set approach) 검사 기획 시스템 양식안마저 거뜬 완벽히 흉내 작동 모사 구현 반영 설계(implement) 시켜낼 수 있습니다.

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

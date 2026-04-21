---
layout: default
title: "trans1"
---

[< 3.6.1 Importing Packages](../3_6_1_importing_packages/trans1.html) | [3.6.2.1 Out24 374 >](3_6_2_1_out24_374/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _3.6.2 Simple Linear Regression_

# 3.6.2 단순 선형 회귀 실습

In this section we will construct model matrices (also called design matrices) using the `ModelSpec()` transform from `ISLP.models`.

이번 섹션에서 우리는 `ISLP.models` 모듈 환경에서 파생된 `ModelSpec()` 변환 도구를 적용 활용하여 이른바 모델 행렬(혹은 설계 행렬이라고도 칭함)을 직접 구축 조립해 볼 것입니다.

We will use the `Boston` housing data set, which is contained in the `ISLP` package.

본 과정 내내 우린 `ISLP` 패키지 풀안에 기본 수록된 저명한 `Boston` 주택 데이터 세트를 한껏 차용 활용할 것입니다.

The `Boston` dataset records `medv` (median house value) for 506 neighborhoods around Boston.

해당 `Boston` 데이터 세트는 보스턴 시 인근 506 군데 주거지 이웃 동네를 돌며 각각 조사 기록한 `medv` (주택 중간값) 지표 항목 단면들을 충실히 담고 서술 기록합니다.

We will build a regression model to predict `medv` using 13 predictors such as `rmvar` (average number of rooms per house), `age` (proportion of owner-occupied units built prior to 1940), and `lstat` (percent of households with low socioeconomic status).

여기에 발맞춰, 우린 집마다의 평균 방 개수를 일컫는 `rmvar` 이나, 1940년 이전에 건축 지어 자가 점유된 낡은 거주 가구 비율 잣대인 `age`, 그리고 낮은 하위 사회경제적 계층 가구 비중 퍼센트 치수인 `lstat` 따위의 13가지 예측 변수 무리들을 복합 활용해 궁극적으로 최종 응답 지표인 이 `medv` 가치를 추정 판단 수렴 해낼 하나의 정교한 회귀 모델 단면을 새로 완성 적합해 구축 지어 올릴 것입니다.

We will use `statsmodels` for this task, a `Python` package that implements several commonly used regression methods.

나아가 이 난제 수행 조달 작업을 위해 우리가 기용 선택할 주력 도구는 다름 아닌 `Python` 용 특화 패키지 `statsmodels` 로, 이는 현장에서 여러 자주 널리 통용 활용되는 회귀 모형 요법들을 대거 품고 일괄 산입해 구현해 놓은 매우 강력한 도구 묶음입니다.

We have included a simple loading function `load_data()` in the `ISLP` package:

우리는 이런 기초 파생 로딩 조달 목적을 위해 자체 `ISLP` 패키지 구성 안에 아주 기초 단순한 데이터 로드 전용 기능 함수 `load_data()` 편린 하나를 고스란히 동반 포함 산입시켜 두었습니다:

```
In [8]: Boston = load_data("Boston")
Boston.columns
```

```
Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'],
dtype='object')
```

Type `Boston?` to find out more about these data.

프롬프트 상에 `Boston?` 코드를 타건 타이핑해 보면 이 관련 데이터 무리들의 부연 세부사항 단면 전반을 조금 더 상세히 살펴 파악해 볼 수 있습니다.

We start by using the `sm.OLS()` function to fit a simple linear regression model.

본격적인 이 첫 실습 시작의 단추 돌입으로, 우리는 `sm.OLS()` 도구 함수를 당겨 차용 활용함으로써 일개 아주 가장 기초 단순한 형태의 단순 선형 회귀 모델 궤도 단면을 접목 구동해 적합 시켜 볼 것입니다.

Our response will be `medv` and `lstat` will be the single predictor.

여기서 설정할 우리의 타사 응답 과녁 주체치로는 `medv` 를 삼고, 반면 오직 홀로인 단일 예측 변수 도구 조각으로는 `lstat` 요소를 지정 기용 선택합니다.

For this model, we can create the model matrix by hand.

당면 이 구 모델 적합 조달 과정 단면을 수행하고자, 우리는 당장 손수 이 대상 모델 행렬 판을 수동으로 일일이 조작 직조해 낼 수도 있습니다.

```
In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]),
'lstat': Boston['lstat']})
X[:4]
```

```
Out[9]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

We extract the response, and fit the model.

이윽고 해당 데이터 판에서 대상 응답치만을 단절 분리 추출 파생하여, 최종 모델에 입성 적합시킵니다.

```
In [10]: y = Boston['medv']
model = sm.OLS(y, X)
results = model.fit()
```

Note that `sm.OLS()` does not fit the model; it specifies the model, and then `model.fit()` does the actual fitting.

다만 여기서 명심할 점은 이 투입 `sm.OLS()` 도구 기능 자체가 곧장 실제 함수 모델 적합을 직접 연산해 달성 수행해 내진 않는다는 점입니다; 이 코드는 그저 모델의 개별 설계 사양 골격만을 이리저리 규정 명시 정의해 쳐둘 뿐이고, 막상 뒤이은 `model.fit()` 기능 명령만이 실질 본연 진짜 도출 적합 전 과정을 마침내 단행 수행해 산출 냅니다.

Our `ISLP` function `summarize()` produces a simple table of the parameter estimates, their standard errors, $t$-statistics and p-values.

우리의 이 친숙한 `ISLP` 내장 산하 구동 함수 `summarize()` 도구는, 투입 결과에서 각 모수 계수 항목 추정치 표본들이며, 이들 고유의 얽힌 부수 표준 오차 치수들, 그리고 도출된 $t$-통계량과 $p$-값 등의 여러 척도 항목을 일목요연 단숨에 정리해 간단한 단편 표 도면 테이블 형태로 아주 쉽사리 일괄 배출 생산 제공해 줍니다.

The function takes a single argument, such as the object `results` returned here by the `fit` method, and returns such a summary.

이 도출 함수 잣대 역량은 딱 하나 단일 구동 연쇄 독립 인자만을 그 입력 대상물로 받아 취하는데, 예컨대 방금 위에서 조달 도출 연산해 `fit` 파생 메서드로 일궈내 산출 돌려받았던 바로 저 `results` 모델 반환 객체 통 덩어리가 그 좋은 투입 대입 일례이며, 이를 토대로 즉각 위와 같은 일련 명세 요약(summary) 단면 지표를 도출 반환해 냅니다.

```
In [11]: summarize(results)
```

```
Out[11]:
```

||`coef`|`std err`|`t`|`P>|t|`|
|---|---|---|---|---|
|`intercept`|`34.5538`|`0.563`|`61.415`|`0.0`|
|`lstat`|`-0.9500`|`0.039 `|`-24.528`|`0.0`|

Before we describe other methods for working with fitted models, we outline a more useful and general framework for constructing a model matrix `X`.

조달 적합 산입된 이들 실체 모델 도구 단면들을 직접 이리저리 다루며 구동해 볼 다른 여타 제반 방법론 체계를 계속 이어 더 묘사 소개 설명하기에 앞서, 우리는 먼저 실체 모델 행렬 `X` 자체를 조금 더 편히 요긴 능숙하게 직조 조립 파생해 구축해 낼 더욱 유용 다분하고 포괄적 보편 일반적인 제반 토대 프레임워크 뼈대 기조를 아주 짧게 덧붙여 개요 윤곽선으로나마 그려 볼까 합니다.

### Using Transformations: Fit and Transform (변환 활용하기: 적합 및 변환)

Our model above has a single predictor, and constructing `X` was straightforward.

위 사례 국면에서 다룬 모델 꼴은 단지 단 하나의 예측 변수 조각 부문만을 보유 접목했던 터라, 행렬 `X` 를 꾸려 지어 축조하기란 몹시 별 무리 없이 거침 직관 단순 직행(straightforward)이었습니다.

In practice we often fit models with more than one predictor, typically selected from an array or data frame.

하지만 실제 실무 통계 일선 환경에서는 기저 배열(array)이라거나 혹은 데이터 프레임 단면 판 덩어리 속에서 차출 발췌한 2개 이상의 아주 복수 다변 예측 변수를 한데 결집 투입해 모델에 아울러 적합시키는 상황 전개가 비일비재 전형적(typically)으로 번번 번성 흔합니다.

We may wish to introduce transformations to the variables before fitting the model, specify interactions between variables, and expand some particular variables into sets of variables (e.g. polynomials).

우리는 때때로 모델을 본 적합하기 전 선행 조치로 이들 제반 예측 변수 파편들을 상대로 다채 다양한 어떤 이질 수학 변환(transformations) 과정을 가산 투입시켜 볼 수도 있고, 여력이 닿음 변수 서로 상호 간의 복잡 상호작용성(interactions) 면모를 명시 기재 적시 도출시킬 수도 있으며, 때론 특정 특정 소수 몇몇 여타 단일 변수 조각들 위를 아예 덧입혀 포괄 집합 변수 묶음 체제 세트(가령 여러 다항식(polynomials) 일련 확산 등) 양태로 훌쩍 팽창 변환 연장(expand)시켜 쓸 소지도 큽니다.

The `sklearn` package has a particular notion for this type of task: a _transform_.

`sklearn` 패키지 풀안에는 이 부문의 전 방위 복잡한 조달 부가 작업을 전담 구동키 위해 내세울 핵심 아주 특정 특수 개념 기조가 도사리는데: 이른바 _변환(transform)_ 단위 모의 잣대가 바로 그것입니다.



A transform is an object that is created with some parameters as arguments.

변환 즉 transform 산입체 개념이란, 인자(arguments) 단면들 격으로 투입 지정된 여러 변형 모수 파라미터 조각들의 통제를 받아 기저 구축 파생되는 어느 개별 단위 객체 조각을 칭합니다.

The object has two main methods: `fit()` and ``.

이 도출 변환 단위 객체 구도 속에는 보통 2대 주축 중추가 되는 대변 메서드 틀이 담기는데: 바로 `fit()` 단면과 `` 명령입니다.

```
.fit()
.
```

We provide a general approach for specifying models and constructing the model matrix through the transform `ModelSpec()` in the `ISLP` library.

우리는 `ISLP` 라이브러리 품 안에 별도 편입 구비되어 내장 배치된 투사 변환기 `ModelSpec()` 도구 매개체를 필두 관통 매개로 삼아, 모델 꼴을 속속 정의 명시 표기하고 나아가 실체 모델 행렬 단면을 지어 가공 직조할 아주 포괄 전형 일반 접근(general approach) 기조 도면을 제공 배달해 전개합니다.

`ModelSpec()` (renamed `MS()` in the preamble) creates a transform object, and then a pair of methods `` and `fit()` are used to construct a corresponding model matrix.



앞서 맨 위쪽 패키지 서술 서두 대목 단면에서 명칭을 아주 짧게 `MS()` 형태 부호로 개명 압축해 기재 불렀던 이 `ModelSpec()` 수식 자체는 일개 독자 변환 전용 모델 객체 개편 구조 단위 한 덩어리를 고스란히 떡하니 파생 산출 생성해 만드는데, 이윽고 이 틈 안에 포섭된 `` 그리고 `fit()` 으로 이루어진 메서드 쌍벌 도구 한 쌍이 재차 단합 연동해 나서 향후 우리 타깃 목적으로 응답 동조 결부된 실 해당 편 모델 행렬 전반 진용을 마침내 오롯 완성형으로 짓고 고안 구축 조립해 냅니다.

We first describe this process for our simple regression model using a single predictor `lstat` in the `Boston` data frame, but will use it repeatedly in more complex tasks in this and other labs in this book.

우선 본 장의 서막으론 이 `Boston` 테두리 데이터 프레임 단면 판 덩어리 산하에 소속 편입된 일개 한 가지 외톨이 예측 변수 `lstat` 조각 한 개만을 빌려다 기용 접목 발탁 채택한 매우 초간단 단순 회귀(simple regression) 추정 국면 전 모델 기조 안에서 이 일련 산입 변환 도출 구축 과정을 풀이 시연 설명해 보이겠지만, 이내 훗날 이 책 곳곳 여타 타 실습 연구 장 내의 몹시 심도 더 깊고 난해 다변 복잡한 여타 과업 지표 단면상들에 차출 마주쳐 당면 도달할 때마다 줄곧 끈질 연거푸 똑같은 양상을 재차 반복 다중 적용 구동 활용해 나설 터입니다.

In our case the transform is created by the expression `design = MS(['lstat'])`.

당면 우리 파생 코딩 사례에서, 변환 조달 객체 산입 꼴은 `design = MS(['lstat'])` 라는 파이썬 선언 표현 구문을 통해 비로소 고안 도출 생성 지어 발현됩니다.

The `fit()` method takes the original array and may do some initial computations on it, as specified in the transform object.

여기 등장한 `fit()` 편린 메서드는 기저 오리지널 배열 단면 조각을 입력 대상으로 대뜸 통째로 취한 다음, 그 상위 변환 포괄 객체 안에 사전 명시 규정 설정된 갖은 속성 잣대 수위 지표에 맞추어 여러 일부 몇몇 사전 초기 부가 연산 도출 구동 단계를 가해 보탤 수도 있습니다.

For example, it may compute means and standard deviations for centering and scaling.

단적인 예시 부합으로, 데이터 영점 조준 이동 중앙화(centering)라든가 크기 맞춤 치환 스케일링(scaling) 등 제반 보정 작업을 이룩 단행하고자 해당 데이터 전 분포 평균치며 곁들여 수반 포괄된 이변 표준편차 요소들을 이리저리 도출 연산해 미리 계산해 보유해 둘 요량 단면도 배제할 순 없습니다.

The `` method applies the fitted transformation to the array of data, and produces the model matrix.

반면 단짝을 이룬 `` 조명 기능 파생 메서드는 앞선 이런 단면으로 묘사 파생 완성 도출해 둔 제반 그 적합(fitted) 변환 도출식 지향 지표 자체를 실제 원천 데이터 배열 조각 원판 상단에 모조리 일괄 단번에 적중 적용 투여해, 궁극적으로 우리 모델 행렬(model matrix) 판을 마침내 고스란히 양산 찍어 반환해 생산해 냅니다.

```
In [12]: design = MS(['lstat'])
design = design.fit(Boston)
X = design.transform(Boston)
X[:4]
```

```
Out[12]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

In this simple case, the `fit()` method does very little; it simply checks that the variable `'lstat'` specified in `design` exists in `Boston`.

그러나 지금 이 몹시 일개 단순 국면 사례 하에선 사실 `fit()` 메서드 무리가 실제 직접 구동 지령 단행해 행하는 연산 조달 비중 활동이 아주 매우 희소 극히 미미(does very little)한데; 기껏해야 `design` 지정 변수 조달식 명세 변환 객체 파편 안에 사전 명시 규정해 둔 타깃 변수 `'lstat'` 존재 항목 여부 잣대가 과연 대상 `Boston` 기저 데이터 단면 배열 상단에 확실 실제 자리 매김해 존재하는지 여부를 단순 진단 조회 체킹 감식해 살피는 게 거진 전부 모조리 일쑤입니다.

Then `` constructs the model matrix with two columns: an `intercept` and the variable `lstat`.

이후 바통을 넘겨받는 `` 구동 지령 편이 본격 구동 개입하면서 모델 행렬판 판세 단면을 단 2개의 조달 열 항목 기둥(columns): 고정 기저 상수판 `intercept`(절편)와 대명 예측변수 기조 `lstat` 요건 기둥 조각으로 구성 조합 변환 치환해 묶어 최종 구축 축조해 지어 세웁니다.

These two operations can be combined with the `fit_` method.

이 2단 파생 다중 구동 복합 운영 연산 지령 파편들은 편의 도모 일환으로 `fit_` 이중 복합 메서드 명령어 단일 하나 구문 속으로 무리 일렬 통합(combined) 합체 구성 지어 운용 접목할 수 있습니다.

```
In [13]: design = MS(['lstat'])
X = design.fit_transform(Boston)
X[:4]
```

```

```

```
Out[13]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94
```

Note that, as in the previous code chunk when the two steps were done separately, the `design` object is changed as a result of the `fit()` operation.

여기서 조금 더 주목 유념 조명해 눈여겨볼 단면 대목 부문은, 앞서 2단 쪼개기 조도 다중 연계 스텝이 분할 가동 분리 구동 분할 연립 독립 시행 수행 조달(separately)됐던 바로 직전 앞 선 코드 조각(chunk) 맥락 환경 선상 때와 매한 한결 똑같이 마찬가지 공히 일렬 동일하게, 이 후위 단일 통합 복합체 운용 시행 과정 결부 도달 후유 여파 수반 대목 하에선 여느 선행 기조처럼 해당 기반 `design` 지표 산입 개체(object) 단면 속성 자체가 전향 조달 기조 `fit()` 동반 제반 연산 도출 작용 지령 영향 파급에 따라 여지 다분 변경 수정 속결 치환(changed) 귀결 변화해 버린단 것입니다.

The power of this pipeline will become clearer when we fit more complex models that involve interactions and transformations.

이처럼 맞물려 전개되는 일괄 파이프라인(pipeline) 파생 체제가 뿜어 발휘해 대는 도출 능률의 위력은, 향후 여러 변수 상호 작용(interactions)이며 다변 수학적 변환(transformations) 과정들이 얽히고설킨 훨씬 더 복잡한 모델을 적합(fit)시킬 때에 이르러서야 비로소 한층 명확해(become clearer)집니다.

Let’s return to our fitted regression model.

자 그럼 당초 조준 도출 조립 구축해 올렸었던 우리 진영 적합 회귀 모델 잣대 근원 산입 요 결 전방 시야로 다시 눈길 단면 회귀 귀향 되돌아 이목 집중을 선회해 볼까요.

The object `results` has several methods that can be used for inference.

산입 이 거대 파생 출력물 도출 개체 덩어리인 `results` 모델 반환 통 객체 속 부문 안에는 훗날 다양한 전위 추론(inference) 지표 조달 진척 분석 목적으로 유용 발탁 차용해 가져다 꺼 편 요긴 쓸 만한 여러 다파생 독립 메서드 가지 수 덩어리들이 대거 빼곡 부속 탑재 수록 장만 구비 동반 수록되어 포진해 있습니다.

We already presented a function `summarize()` for showing the essentials of the fit.

우리는 앞서 이 모델 단면 도출 적합의 중추 진수(essentials) 고갱이만을 딱 간추려 선보여 보여주기 위한(for showing) 요긴한 도달 목적 부합 함수 `summarize()` 를 이미 한 차례 앞서 선보인(presented) 바 있습니다.

For a full and somewhat exhaustive summary of the fit, we can use the `summary()` method (output not shown).

반면 보다 빈틈없이 꽉 찬(full) 전체적이고 다소 다분히 뼛속 깊이 망라된 세부 요약(exhaustive summary) 결과를 원한다면, 부가 도출 기재 메서드 `summary()` 를 쓸 수 있습니다 (출력은 지면상 생략).

```
In [14]: results.summary()
```

The fitted coefficients can also be retrieved as the `params` attribute of `results`.

모델 도출 적합 연산 부합 지표로 산출 고정 귀결된 각 계수(coefficients)는 `results` 원천 객체 속 `params` 속성(attribute) 항목으로도 언제든 따로 불러와 찾아낼 수 있습니다.

```
In [15]: results.params
```

```
Out[15]:
```

```
intercept34.553841
lstat-0.950049
dtype:float64
```

The `get_prediction()` method can be used to obtain predictions, and produce confidence intervals and prediction intervals for the prediction of `medv` for given values of `lstat`.

나아가 `get_prediction()` 메서드를 동원하면 특정 주어진 `lstat` 값에 대한 `medv` 의 예측치(predictions)를 뽑아 얻고(obtain), 덧붙여 이에 얽힌 신뢰 구간(confidence intervals) 및 예측 구간(prediction intervals) 둘 다 모조리 산출해 낼 수(produce) 있습니다.

우선 우리는 예측을 내리기 원하는 특정 변수 값들만을 포함하는, 방금 사례의 경우 오직 변수 `lstat` 만을 단일 지닌 신규 데이터 프레임(data frame)을 구축합니다(create a new data frame). 그런 다음 기존에 마련해 둔 `design` 객체의 `transform()` 메서드를 호출 사용해 그에 맞대응하는 동반 모델 행렬을 직조 생성해 냅니다.

```
In [16]: new_df = pd.DataFrame({'lstat': [5, 10, 15]})
newX = design.transform(new_df)
newX
```

```
Out[16]:    intercept  lstat
0        1.0     5.0
1        1.0    10.0
2        1.0    15.0
```

Next we compute the predictions at `newX`, and view them by extracting the `predicted_mean` attribute.

다음으로 우리는 앞서 준비한 조달 행렬 `newX` 대상에 대한 실질적인 예측치(predictions)들을 도출 연산해 단행 구동하고(compute), 덧붙여 그 안에 내재된 `predicted_mean` 속성(attribute) 항목만을 쏙 빼내 추출해 봄으로써(extracting) 이를 슬쩍 화면에 띄워 살펴 봅니다(view them).

```
In [17]: new_predictions = results.get_prediction(newX)
new_predictions.predicted_mean
```

```
Out[17]: array([29.80359411, 25.05334734, 20.30310057])
```

We can produce confidence intervals for the predicted values.

우리는 앞서 도출해 낸 이 모델의 예측값(predicted values)들에 대한 신뢰 구간(confidence intervals) 역시 단숨에 떡하니 추가 산출해 낼 수도(can produce) 있습니다.

```
In [18]: new_predictions.conf_int(alpha=0.05)
```

```
Out[18]: array([[29.00741194, 30.59977628],
       [24.47413202, 25.63256267],
       [19.73158815, 20.87461299]])
```

Prediction intervals are computing by setting `obs=True`:

예측 구간(Prediction intervals)은 `obs=True` 로 설정함으로써 계산 산출해 낼 수 있습니다:

```
In [19]: new_predictions.conf_int(obs=True, alpha=0.05)
```

```
Out[19]: array([[17.56567478, 42.04151344],
       [12.82762635, 37.27906833],
       [8.0777421 , 32.52845905]])
```

For instance, the 95% confidence interval associated with an `lstat` value of 10 is (24.47, 25.63), and the 95% prediction interval is (12.82, 37.28).

단적인 가령 예시로 들어, `lstat` 값 지수가 10 일 때 도출 연루된 95% 확률 신뢰 구간(confidence interval) 범위 폭은 (24.47, 25.63) 영역인 반면, 맞추어 이에 속결 대응되는 95% 확률 기대 예측 구간(prediction interval)은 (12.82, 37.28) 범위로 전개 폭을 펼칩니다.

As expected, the confidence and prediction intervals are centered around the same point (a predicted value of 25.05 for `medv` when `lstat` equals 10), but the latter are substantially wider.

으레 앞서 이론 서술상 예상 기대(expected)했던 대로, 당장 이 두 가지 신뢰 구간, 예측 구간 모두 똑같은 기준 기점 단면 포인트(`lstat` 가 10 단위 일 상황에서 나온 단일 `medv` 예측 예측값 25.05)를 중심 중앙 지점 기준(centered)으로 자리해 포진하고야 있지만, 역시나 후자 단편 지표(예측 구간) 쪽이 근거를 둔 변동 가변성이 단연 훨씬 극대 폭 실질 넓고 장대히 거대(substantially wider)하게 분포합니다.

Next we will plot `medv` and `lstat` using `DataFrame.plot.scatter()`, and wish to add the regression line to the resulting plot.

다음으로 우리는 `DataFrame.plot.scatter()` 를 사용해 타깃 `medv` 와 `lstat` 을 맞대응시킨 뷰 차트 산점도(plot)를 그리고(Next we will plot), 덧붙여 그 도출된 결과 화면 점도 위에 방금 구한 선형 회귀 선 자체를 추가(wish to add)하고 자 합니다.

3.6 Lab: Linear Regression 121



### Defining Functions (함수 정의하기)

While there is a function within the `ISLP` package that adds a line to an existing plot, we take this opportunity to define our first function to do so.

사실 이미 `ISLP` 패키지 구성 안에 이처럼 생성된 플롯 그래프 뷰 위에 새 별도 임의 단일 직 선을 덧입혀 그려 추가해 주는 유용 용도 목적 함수 모듈 요소가 명백히 아예 구비 선재 존재해 담겨져 내장되어 있기는 하지만, 우리는 기왕에 기회가 닿은 김에 직접 그런 소속 조달 수고의 기능을 손수 내포해 고스란히 수행해 바칠 법한 고유 함수 객체 조각 자체 모를 한 가지 따로 수기 정의 설계해 구현 생성해 봅니다.

```
In [20]: def abline(ax, b, m):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim)
```

A few things are illustrated above.

위의 코드 서면 내역 블록을 단면 유심히 한 번 이리저리 들살펴보면 당장 여러 군데 살펴 짚어 볼 자잘 포인트 대목 특징 조각들이 곳곳 눈에 띕니다.선.

First we see the syntax for defining a function: `def funcname(...)`.

가장 앞선 처음 우선 지표론 우린 파이썬 체제 내에서 여느 함수 조각 구문을 수립 정의할 때 으레 기초 수반해 쓰는 정규 문법인: `def 함수이름(...)` 틀 규칙을 대면 목격해 엿봅니다.

The function has arguments `ax, b, m` where `ax` is an axis object for an exisiting plot, `b` is the intercept and `m` is the slope of the desired line.

이 도출 함수 덩어리는 각각 `ax, b, m` 이라는 독립된 제반 삼중 인자 파라미터 조각 부문을 품고 쥐는데 여기서 첫 관문 `ax` 는 기존에 앞서 직조 배태돼 선 구비 그려진 기존 조달 플롯 판 화면 객체 산하의 단면 축(axis) 요소 대상을, 연달아 `b` 는 대상 그릴 지정 라인의 단일 절편 수치를, 또 `m` 잣대는 곧 그려 추가시킬 직 선의 개별 기울기 조각 요소를 대변 지시합니다.

Other plotting options can be passed on to `ax.plot` by including additional optional arguments as follows:

여기다 그 외 나머지 다른 짜잘 추가 여타 플롯 부가 설정 옵션(options) 치수 항목들도 다음 보일 코드에서처럼 한데 묶일 별도 덧붙일 임의 옵션 인자 조각 무리 팩으로 포섭 가단성 지어 싣자마자 `ax.plot` 측을 향해 이리저리 우회 대입해 같이 고스란 전달 파급(passed on)시켜 버릴 길이 능히 묘연 유효 단연 도달 열려 있습니다:

```
In [21]: def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs)
```

The addition of `*args` allows any number of non-named arguments to `abline`, while `*kwargs` allows any number of named arguments (such as `linewidth=3`) to `abline`.

수반 코드 대목에 `*args` 지표 단락을 추가 산입 허용해 둠으로써 우린 이 `abline` 함수 꼬리표 뒤에 따라붙을 이름 단면이 채 지정 확립되지 않은 임의 막무가내 인자(non-named arguments) 조각들이라도 숫자 구애 여부 제한 없이 얼마든 거침 수월 대거 묶어 무리 수용해 통과시킬 수 있게 되며, 이에 대칭 반해 `*kwargs` 규약은 또 따로 `linewidth=3` 따위와 같이 명시적으론 확실히 지명 선점된 개별 지정 인자(named arguments) 변수 항목 무리를 개수 한정 통제 국한 없이 무한정 도출 한데 덧붙 수록 허 방 용해 줍니다.

In our function, we pass these arguments verbatim to `ax.plot` above.

우리가 자작 구비 전개 마련한 이 함수 규격 내에서 우리는 이렇게 투입 흡수 인가된 인자 조각들을 아무 손 대 가감 보탬 없이 글자 그대로 윗단 구역의 `ax.plot` 모듈 도면 객체 쪽에 곧이 고스란 그대로 전달(verbatim) 단행해 곁들 토스시켜 기탁 위임합니다.

Readers interested in learning more about functions are referred to the section on defining functions in docs.python.org/tutorial.

혹여 이러한 함수 정의 잣대 메커니즘 구비 규약 룰 전반에 대해 지금보다 한층 조 일련 더 깊이 심연 상세 흥미를 지닌 독자 유저라면 docs.python.org/tutorial 문서 지표 카테고리 내의 관련 부분 섹션 내역 장을 일 독 따로 한 번 심 결 들여 살 읽조참고해 보시길 수 권고 장 장 권장 타 도 추 릅 제합 다 시니 합 천 다 권 이 참 고(referred)니다.

Let’s use our new function to add this regression line to a plot of `medv` vs. `lstat`.

자 그럼 앞서 마련 작성해 둔 바로 이 새로운 신생 함수 도구 스니펫을 유효 적극 요긴 적절 차용 활용하여, `medv` 대 `lstat` 지표 잣대의 대응 대조 비교 점 산점도(plot) 공간 차트 화면 판 위에 이 파생 선형 회귀 유도 산입 단선 조각 막대 다 지 도 (regression line)을 선 기 기 적 직접 한번 삽 추가 그려 포 개 덧 입 추가입 덧 추가 혀 그려 추가 그려기 더 묘 해 (add)봅 도 시 보 기 해시다 합 그려 다 보자.

```
In [22]: ax = Boston.plot.scatter('lstat', 'medv')
abline(ax,
       results.params[0],
       results.params[1],
       'r--',
       linewidth=3)
```

Thus, the final call to `ax.plot()` is `ax.plot(xlim, ylim, 'r--', linewidth=3)`.

이리하여 최종적으로 도출 당면 지 도 (final call) 기 기 은 도 측 이 차 종 지 대 시 되 표 에 조 에 도 대 표 은 은 종 결 결 (final call) 국 (call) 시 결 도 수 타에 점 (plot) 대 내 되 결 호출(최 된 호출 과 는 시 점(call)기 의 표 된 최 은 결 국(final call)로 은 `ax.plot()`에 점호출 시에 조 은 국 파 의 `ax.plot(xlim, ylim, 'r--', linewidth=3)` 과 과기 다 점결은기과기점과 기 다 과기 같습니다.

We have used the argument `'r--'` to produce a red dashed line, and added an argument to make it of width 3.

우리는 빨간 점선(red dashed line) 투영 단면 시각 그림을 시 시 타 표 그 려 기 도 대 생산하기 표 그려 에 표 기 위해 표 (produce) 위해 대 기 도 `'r--'`란 시 기 은 조 잣 타 은 문 수 대 은대 타기 시 자 (argument) 잣 대 를 투입 지정 타대 대 사 수 지 조 기 대 타 사 점 시 타수 며 차 지표 (argument) 점 를 용 사 과대 했으며 과 를 기 대 점 차 조 점(used), 더불어 시 해당 추가(added) 기 다 차 사기 차 선 해당 대 그대 다 그 다수 기 대 폭 그 두 선 이 수 굵기 폭 과 기기 너 두 선 그 를대지(width) 3 지 수 지가수수 수 두 조 조 조 두 수 지 조 께 굵기 기되게 이 (make it) 두 수 기 수 (width 3) 께 굵기 끔 기 기 끔 조 기 기 조(width 3) 하기 과 기 끔 굵 점 (make it)과 과 점 위해 되 차 시 조 위해 조 조 기 과 차 끔 추가 위해 은 기 추가 끔 과를 끔 조 끔 위해 두 점 하기 대 두 조 은 별 끔 기 (make it) 위해 기 과 점 끔 부 지기 점 조(added) 점 끔 위한과 추가 과 조 점 기 과 은 기를 점 점 과 위 추가 인자(argument) 기 과를조를를 별 도를 더 추가 를기 덧(added) 붙였 보 대 과 보 은 다과 기 다 보 다 더(added) 점 추가로 보 덧 과 기 다 보 합니 더 조 이 기 으 이 추가로기 이 추가(added) 다은기 더 보 다 기 습니다.

There is some evidence for non-linearity in the relationship between `lstat` and `medv`.

더불어 살펴 해당 산출 지표 양 국 도면 그림 양식 분포도 꼬라 위에서 `lstat` 변수 그리고 `medv` 양 거 투 기 거 대 시 타 그 타 타 그 기 다 기 과 의 대 거 지 기 간 대 기 타 파의 거 이 잣 기 (relationship between) 사이에 타대 시 사이 둘의의의기기 양 조 그 대 지기(relationship between) 관계에서 기 (relationship between)대 타 조 (relationship between) 사이 기 관계에 다의 양 자 둘 단 사 지 조 그 지 자그 다 시 (relationship between `lstat` and `medv`) 대 시 대 은 모 다 기 모 다기 기 뻗기대 도 다 나다 비 대비기 어느대 조 비 비 어 조 (some evidence) 뻗 도 수 지 뻗 비기 선 (non-linearity) 어 일 단 어 느 정도 조 기 대 단 시 정 나 비(some) 도 느 단 어 어느시 기 비 뻗 도 어 비 지 시 조 다 점기 비 시 정도의 일 파 대 대 비 일 조 조 정 조 어느 정 비 (some) 도 다 비 (some)의 기 시 (evidence) (non) 시 뻗 조 단 다 조 점 정선 어 도 조어 기 비선형 조 어느기 (non-linearity) 다 기 정 어 느 선 조 기 정도 조기 어 조어기 (some)기(evidence) 조 형 도(non-linearity)의 조 정 어 대 성 뻗 형다 조선 느 조 (some)성 다 형 증(evidence) 대 조의어어 느 기 정 기 뻗 거 기(some evidence)정 더 증거 기 (evidence)도 비의의 단 비 뻗(evidence) 시 단 (evidence) 기조 조 타 정 일 조 조 대다 기 의 정 일의 점 형 단일 지 느 (non-linearity) 지 사 단 시 일 느 일 다도 일 점 성(non-linearity) 조 단다 성 타 선 기 타(non-linearity)의 일 기 점 다 타 타 단 형 어 성 기 도 비다 형 대 더 기 타의 다 타 시 기 다 일 지 비 지 성 시 지 보 도 (evidence)지 가 단 성 이 (evidence) 다 단 다 단 타 더 시 이 보 성 타 성 가 증 대 정 관 증 사 단 관 다 더 타 보 찰 파 더 보 시 측 비 보 비(evidence) 이 측 정 어 어 관 관 의 성지 이 됩 찰(is) 측 측(is) 더 사 됩다 이 타 발 나타 측 (evidence) 사 이 보 지 발견 비 보 됩 이 보(is) 보 찰 다 니 (is) 보나다 입 측 측 이 니 나타 시 일다 발 견 관 측 발견됩 관 나 됩다(is) 나타 측 다 (is)니 사다(is) 나타 보 타 니다.

We will explore this issue later in this lab.

우리는 당 면 기 조 뻔 조 탐 국 기 타기 도 면 조 조 당 파 추 조 기 추 면탐 우 타 탐 탐 이 조 기기(issue) 기 면 당 뻔해 구(issue)우 지 이 구 문 국 이 구 사 국(this issue)면기 사의의 타 파 사 우우 당 이 (this issue) 문제 다 지기 도 구 제기 뻔 구 제 제 제 조 추 나 조 조 면 파 당 제 조 구 구다(issue) 사 면 파의 도 파 를 단 탐 추 후 뻔 대 대 타 다 단 (later)해 다 를 우 파 의 이 나 사 당대 조 추 구의 단 대의의 기 구 단 파 우 조 다 대 더 (later)의 지기 뻔 실 구 파 대 시 후 에 구 (in this lab) 에 에 지 후 중 추 본 기 에 후 시 시 구 본 중추 사 본 구 본 기 파 에 본 (explore)본 에 시 기에파 조 뻔 시(later) 추 시 다 에 제 에 탐 에 (explore)기 다 에 기 조조 다 기 기 우 (explore)기습 도 (lab)지 시 (in this lab) 지 조 (lab)조중 기 중조 지탐 에 본 에 중 제 다 구지 (in this lab) 중 기 구 조기 탐 실 단(explore)파 에 다구 뻔습 조 제 지 구 (explore) 후반구 뻔(later)기 습 사(lab)제 파 중기 (explore)에 조 지 제 해 조 다 기 지습기 더 도에 추 뻔의 도 기 습 에 중 다 사 구 사에 좀제 에 좀 더 중 파(explore) 사 에제 구 단구기 제 좀 지 중 파기 에 (explore)깊다 도 구기 제이 다 진 의 에 본 구 파 본 제 다 사 실 (explore)사 파 단 중 탐에 제 지 본 중 중파습 도 다 (lab)에서 지 도 (in this lab) (lab)제 단 (lab)에파 중중구구 조 지 이다 좀 시지 중 에의 좀 조 파 도 (explore) 조 단기 기 (explore) 사 파 에 사 도 조기 조 (explore) 도 심 지 조 좀제 도 단 조 지 기 도단 탐 지 사 더(later)에 사 좀 나(later)조 다 기 뻔 단더 도 사구 중 지 (explore)구조 단 해 지자 기자 시 구 조 기 제 단 좀 시 사제 심 다 도자 시 더 자세 해 제 다 도해 사 다 기 시 다 더 시 파 조지 도 시 시 뻔 구 도 파지 자세 시단 기 할구 도 파자지파 조 시 다 탐 파 시 지 히(explore) 자 더 조 세도 자세 세 할기 시 더 할 히 시 구 탐구 단 세 자세 합단 시 시 지 탐 (explore) 조 다합 더 니 기 시 지 할 (explore) 니 자 조 지 자세 다 수 히 세 탐 파 다 히합 조 시 지 합 기 히 예정 합다 니파 할 보 니 파 기 단 (explore) 예정입니다.

As mentioned above, there is an existing function to add a line to a plot — `ax.axline()` — but knowing how to write such functions empowers us to create more expressive displays.

위에서 줄곧 언급되었듯이(As mentioned above), 이렇듯 현존하는 기존 플롯 그래픽 화면에 맘껏 타 선을 추가해 그릴 수 있게 해 주는 지름길 함수 — `ax.axline()` — 가 이미 존재(existing)하기는 합니다만, 다분히 이렇게나마 직접 그런 류의 내부 파생 함수들을 설계하고 요령껏 짜 넣는 작성법 체제(how to write such functions)의 기저 모의 기조를 익히 알아 두는(knowing) 것만으로도, 훗날 우리는 훨씬 더 풍부하고 탁월한 표현 수단을 갖춘 출력 화면(more expressive displays) 결과물들을 손쉽게 척척 직조해 구현해 낼(create) 수 있도록 큰 힘을 부여받고(empowers) 자립할 수 있습니다.

Next we examine some diagnostic plots, several of which were discussed in Section 3.3.3.

다음으로 으레 우리는 여러 기조를 띤 진단 플롯(diagnostic plots) 단면들 몇을 추가 조사해 살펴볼(examine) 터인데, 이들 중 다수 항목은 앞선 교재 제 3.3.3절 단락에서 이미 한 차례 거진 논의 제시(were discussed)된 바 있는 친숙한 도구 양식들입니다.

We can find the fitted values and residuals of the fit as attributes of the `results` object.

이때 이 도출 기반 모델 적합 파생으로 인한 도출 적합 값(fitted values) 치수들과, 덧붙여 이에 파생 계산된 각 잔차(residuals) 척도 항목들은 모조리 `results` 객체 덩어리 산하에 귀속된 각 부분 속성(attributes) 가지들로 쉬이 따로 꺼내어 파악하고 찾아 잴(find) 수 있습니다.

Various influence measures describing the regression model are computed with the `get_influence()` method.

거시적 회귀 모델 전반의 판세 속성을 속속들이 규명해 서술(describing) 묘사하는 척도 지표들 중 하나인 여러 차원의 영향력 측정(influence measures) 잣대 성분들 역시 기저 구동 메서드 `get_influence()` 도구를 통과함에 따라 모두 도출돼 계산(computed)됩니다.

As we will not use the `fig` component returned as the first value from `subplots()`, we simply capture the second returned value in `ax` below.

이때 `subplots()` 함수 구동 호출로부터 맨 첫 번째 지위로 도출 반환되어 돌아오는 배열 요소 `fig` (피겨 객체) 콤포넌트 구성 요소 파편의 경우 우리는 이를 애써 받아 사용할 예정 채비가 없으므로(will not use), 그저 아주 담담히 두 번째 순번으로 줄진 이 반환 값 성분 축만 차출 포획(capture)해 아래 `ax` 객체 그릇 안에다 살포시 간직 담아 놓을 뿐입니다.

```
In [23]: ax = subplots(figsize=(8, 8))[1]
```

```
ax.scatter(results.fittedvalues, results.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')
```

We add a horizontal line at 0 for reference using the `ax.axhline()` method, indicating it should be black (`c='k'`) and have a dashed linestyle (`ls='--'`).

나아가 우린 이 공간에 일명 참조 비교 기준선(reference) 차원으로 기점 0에 걸쳐 반듯한 가로 횡단선(horizontal line)을 그려 `ax.axhline()` 메서드를 사용해 더할 것인데, 이때 이 선 색상은 무조건 검정(black, `c='k'`)이어야 하고 그 표현 서식 스타일은 일련의 점선(dashed linestyle, `ls='--'`) 꼴을 지녀 두르도록 선언 지시 명시합니다.

On the basis of the residual plot (not shown), there is some evidence of non-linearity.

비록 지금 지면에 다 실어 나타내진 않았으나(not shown), 투사 도출된 이 잔차 분포 점 산점도(residual plot) 판세 꼬락서니 기조를 기반 삼아 유심히 면밀 타진해 보건대, 확실히 다분한 일련의 비선형성(non-linearity) 여지 증거 기류가 짙게 다분 존재 엿보입니다.

Leverage statistics can be computed for any number of predictors using the `hat_matrix_diag` attribute of the value returned by the `get_influence()` method.

덧붙여 예측 다변 변수 조각들이 몇 개가 동반 포섭 포진 투입되든 수량에 하등의 구애 국한받음 일체 없이 자유로이, 우린 앞선 `get_influence()` 파생 메서드가 기 파생 내뱉어 던져 준 도출 결괏값 그 이면 속성 중 구체적으로 `hat_matrix_diag` 요건 성분만 콕 차출 지정 찝어다 사용하면 그 모델 고유의 레버리지 통계량(leverage statistics) 수치를 모조리 단숨 도출 연산해 거머쥘(computed) 수 단연 있습니다.

```
In [24]: infl = results.get_influence()
ax = subplots(figsize=(8, 8))[1]
ax.scatter(np.arange(X.shape[0]), infl.hat_matrix_diag)
ax.set_xlabel('Index')
ax.set_ylabel('Leverage')
np.argmax(infl.hat_matrix_diag)
```

---


### Jupyter Notebook Output (출력 예시)

Jupyter Notebook 셀에서 통계 모델 객체 혹은 변수의 길이/형태를 출력했을 때 콘솔에 어떻게 표시되는지 확인합니다.
코드의 작동 상태를 점검하는 중간 디버깅 예시입니다.

---

## Sub-Chapters (하위 목차)


[< 3.6.1 Importing Packages](../3_6_1_importing_packages/trans1.html) | [3.6.2.1 Out24 374 >](3_6_2_1_out24_374/trans1.html)

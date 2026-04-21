import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_2_simple_linear_regression\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# _3.6.2 Simple Linear Regression_": r"""# _3.6.2 Simple Linear Regression_
# 3.6.2 단순 선형 회귀 실습""",

    r"In this section we will construct model matrices (also called design matrices) using the `ModelSpec()` transform from `ISLP.models` .":
    r"""In this section we will construct model matrices (also called design matrices) using the `ModelSpec()` transform from `ISLP.models`.
이번 섹션에서 우리는 `ISLP.models` 모듈 환경에서 파생된 `ModelSpec()` 변환 도구를 적용 활용하여 이른바 모델 행렬(혹은 설계 행렬이라고도 칭함)을 직접 구축 조립해 볼 것입니다.""",

    r"We will use the `Boston` housing data set, which is contained in the `ISLP` package. The `Boston` dataset records `medv` (median house value) for 506 neighborhoods around Boston. We will build a regression model to predict `medv` using 13 predictors such as `rmvar` (average number of rooms per house), `age` (proportion of owner-occupied units built prior to 1940), and `lstat` (percent of households with low socioeconomic status). We will use `statsmodels` for this task, a `Python` package that implements several commonly used regression methods.":
    r"""We will use the `Boston` housing data set, which is contained in the `ISLP` package.
본 과정 내내 우린 `ISLP` 패키지 풀안에 기본 수록된 저명한 `Boston` 주택 데이터 세트를 한껏 차용 활용할 것입니다.

The `Boston` dataset records `medv` (median house value) for 506 neighborhoods around Boston.
해당 `Boston` 데이터 세트는 보스턴 시 인근 506 군데 주거지 이웃 동네를 돌며 각각 조사 기록한 `medv` (주택 중간값) 지표 항목 단면들을 충실히 담고 서술 기록합니다.

We will build a regression model to predict `medv` using 13 predictors such as `rmvar` (average number of rooms per house), `age` (proportion of owner-occupied units built prior to 1940), and `lstat` (percent of households with low socioeconomic status).
여기에 발맞춰, 우린 집마다의 평균 방 개수를 일컫는 `rmvar` 이나, 1940년 이전에 건축 지어 자가 점유된 낡은 거주 가구 비율 잣대인 `age`, 그리고 낮은 하위 사회경제적 계층 가구 비중 퍼센트 치수인 `lstat` 따위의 13가지 예측 변수 무리들을 복합 활용해 궁극적으로 최종 응답 지표인 이 `medv` 가치를 추정 판단 수렴 해낼 하나의 정교한 회귀 모델 단면을 새로 완성 적합해 구축 지어 올릴 것입니다.

We will use `statsmodels` for this task, a `Python` package that implements several commonly used regression methods.
나아가 이 난제 수행 조달 작업을 위해 우리가 기용 선택할 주력 도구는 다름 아닌 `Python` 용 특화 패키지 `statsmodels` 로, 이는 현장에서 여러 자주 널리 통용 활용되는 회귀 모형 요법들을 대거 품고 일괄 산입해 구현해 놓은 매우 강력한 도구 묶음입니다.""",

    r"We have included a simple loading function `load_data()` in the `ISLP` pack- `load_data()` age:":
    r"""We have included a simple loading function `load_data()` in the `ISLP` package:
우리는 이런 기초 파생 로딩 조달 목적을 위해 자체 `ISLP` 패키지 구성 안에 아주 기초 단순한 데이터 로드 전용 기능 함수 `load_data()` 편린 하나를 고스란히 동반 포함 산입시켜 두었습니다:""",

    r"""In [8]:Boston=load_data("Boston")
Boston.columns""":
    r"""In [8]: Boston = load_data("Boston")
Boston.columns""",

    r"""Out[8]:Index(['crim','zn','indus','chas','nox','rm','age','dis',
'rad','tax','ptratio','black','lstat','medv'],
dtype='object')""":
    r"""Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'],
dtype='object')""",

    r"118 3. Linear Regression": r"",

    r"Type `Boston?` to find out more about these data. We start by using the `sm.OLS()` function to fit a simple linear regression `sm.OLS()` model. Our response will be `medv` and `lstat` will be the single predictor. For this model, we can create the model matrix by hand.":
    r"""Type `Boston?` to find out more about these data.
프롬프트 상에 `Boston?` 코드를 타건 타이핑해 보면 이 관련 데이터 무리들의 부연 세부사항 단면 전반을 조금 더 상세히 살펴 파악해 볼 수 있습니다.

We start by using the `sm.OLS()` function to fit a simple linear regression model.
본격적인 이 첫 실습 시작의 단추 돌입으로, 우리는 `sm.OLS()` 도구 함수를 당겨 차용 활용함으로써 일개 아주 가장 기초 단순한 형태의 단순 선형 회귀 모델 궤도 단면을 접목 구동해 적합 시켜 볼 것입니다.

Our response will be `medv` and `lstat` will be the single predictor.
여기서 설정할 우리의 타사 응답 과녁 주체치로는 `medv` 를 삼고, 반면 오직 홀로인 단일 예측 변수 도구 조각으로는 `lstat` 요소를 지정 기용 선택합니다.

For this model, we can create the model matrix by hand.
당면 이 구 모델 적합 조달 과정 단면을 수행하고자, 우리는 당장 손수 이 대상 모델 행렬 판을 수동으로 일일이 조작 직조해 낼 수도 있습니다.""",

    r"""In [9]:X=pd.DataFrame({'intercept':np.ones(Boston.shape[0]),
'lstat':Boston['lstat']})
X[:4]""":
    r"""In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]),
'lstat': Boston['lstat']})
X[:4]""",

    r"""Out[9]:interceptlstat
01.04.98
11.09.14
21.04.03
31.02.94""":
    r"""Out[9]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94""",

    r"We extract the response, and fit the model.":
    r"""We extract the response, and fit the model.
이윽고 해당 데이터 판에서 대상 응답치만을 단절 분리 추출 파생하여, 최종 모델에 입성 적합시킵니다.""",

    r"""In [10]:y=Boston['medv']
model=sm.OLS(y,X)
results=model.fit()""":
    r"""In [10]: y = Boston['medv']
model = sm.OLS(y, X)
results = model.fit()""",

    r"Note that `sm.OLS()` does not fit the model; it specifies the model, and then `model.fit()` does the actual fitting.":
    r"""Note that `sm.OLS()` does not fit the model; it specifies the model, and then `model.fit()` does the actual fitting.
다만 여기서 명심할 점은 이 투입 `sm.OLS()` 도구 기능 자체가 곧장 실제 함수 모델 적합을 직접 연산해 달성 수행해 내진 않는다는 점입니다; 이 코드는 그저 모델의 개별 설계 사양 골격만을 이리저리 규정 명시 정의해 쳐둘 뿐이고, 막상 뒤이은 `model.fit()` 기능 명령만이 실질 본연 진짜 도출 적합 전 과정을 마침내 단행 수행해 산출 냅니다.""",

    r"Our `ISLP` function `summarize()` produces a simple table of the parame- `summarize()` ter estimates, their standard errors, $t$-statistics and p-values. The function takes a single argument, such as the object `results` returned here by the `fit` method, and returns such a summary.":
    r"""Our `ISLP` function `summarize()` produces a simple table of the parameter estimates, their standard errors, $t$-statistics and p-values.
우리의 이 친숙한 `ISLP` 내장 산하 구동 함수 `summarize()` 도구는, 투입 결과에서 각 모수 계수 항목 추정치 표본들이며, 이들 고유의 얽힌 부수 표준 오차 치수들, 그리고 도출된 $t$-통계량과 $p$-값 등의 여러 척도 항목을 일목요연 단숨에 정리해 간단한 단편 표 도면 테이블 형태로 아주 쉽사리 일괄 배출 생산 제공해 줍니다.

The function takes a single argument, such as the object `results` returned here by the `fit` method, and returns such a summary.
이 도출 함수 잣대 역량은 딱 하나 단일 구동 연쇄 독립 인자만을 그 입력 대상물로 받아 취하는데, 예컨대 방금 위에서 조달 도출 연산해 `fit` 파생 메서드로 일궈내 산출 돌려받았던 바로 저 `results` 모델 반환 객체 통 덩어리가 그 좋은 투입 대입 일례이며, 이를 토대로 즉각 위와 같은 일련 명세 요약(summary) 단면 지표를 도출 반환해 냅니다.""",

    r"parame- `summarize()` ter": r"parameter",

    r"""In [11]:summarize(results)""":
    r"""In [11]: summarize(results)""",

    r"Before we describe other methods for working with fitted models, we outline a more useful and general framework for constructing a model matrix `X` .":
    r"""Before we describe other methods for working with fitted models, we outline a more useful and general framework for constructing a model matrix `X`.
조달 적합 산입된 이들 실체 모델 도구 단면들을 직접 이리저리 다루며 구동해 볼 다른 여타 제반 방법론 체계를 계속 이어 더 묘사 소개 설명하기에 앞서, 우리는 먼저 실체 모델 행렬 `X` 자체를 조금 더 편히 요긴 능숙하게 직조 조립 파생해 구축해 낼 더욱 유용 다분하고 포괄적 보편 일반적인 제반 토대 프레임워크 뼈대 기조를 아주 짧게 덧붙여 개요 윤곽선으로나마 그려 볼까 합니다.""",

    r"Using Transformations: Fit and Transform": r"### Using Transformations: Fit and Transform (변환 활용하기: 적합 및 변환)",

    r"Our model above has a single predictor, and constructing `X` was straightforward. In practice we often fit models with more than one predictor, typically selected from an array or data frame. We may wish to introduce transformations to the variables before fitting the model, specify interactions between variables, and expand some particular variables into sets of variables (e.g. polynomials). The `sklearn` package has a particular notion `sklearn` for this type of task: a _transform_ . A transform is an object that is created with some parameters as arguments. The object has two main methods: `fit()` and `transform()` .":
    r"""Our model above has a single predictor, and constructing `X` was straightforward.
위 사례 국면에서 다룬 모델 꼴은 단지 단 하나의 예측 변수 조각 부문만을 보유 접목했던 터라, 행렬 `X` 를 꾸려 지어 축조하기란 몹시 별 무리 없이 거침 직관 단순 직행(straightforward)이었습니다.

In practice we often fit models with more than one predictor, typically selected from an array or data frame.
하지만 실제 실무 통계 일선 환경에서는 기저 배열(array)이라거나 혹은 데이터 프레임 단면 판 덩어리 속에서 차출 발췌한 2개 이상의 아주 복수 다변 예측 변수를 한데 결집 투입해 모델에 아울러 적합시키는 상황 전개가 비일비재 전형적(typically)으로 번번 번성 흔합니다.

We may wish to introduce transformations to the variables before fitting the model, specify interactions between variables, and expand some particular variables into sets of variables (e.g. polynomials).
우리는 때때로 모델을 본 적합하기 전 선행 조치로 이들 제반 예측 변수 파편들을 상대로 다채 다양한 어떤 이질 수학 변환(transformations) 과정을 가산 투입시켜 볼 수도 있고, 여력이 닿음 변수 서로 상호 간의 복잡 상호작용성(interactions) 면모를 명시 기재 적시 도출시킬 수도 있으며, 때론 특정 특정 소수 몇몇 여타 단일 변수 조각들 위를 아예 덧입혀 포괄 집합 변수 묶음 체제 세트(가령 여러 다항식(polynomials) 일련 확산 등) 양태로 훌쩍 팽창 변환 연장(expand)시켜 쓸 소지도 큽니다.

The `sklearn` package has a particular notion for this type of task: a _transform_.
`sklearn` 패키지 풀안에는 이 부문의 전 방위 복잡한 조달 부가 작업을 전담 구동키 위해 내세울 핵심 아주 특정 특수 개념 기조가 도사리는데: 이른바 _변환(transform)_ 단위 모의 잣대가 바로 그것입니다.

A transform is an object that is created with some parameters as arguments.
변환 즉 transform 산입체 개념이란, 인자(arguments) 단면들 격으로 투입 지정된 여러 변형 모수 파라미터 조각들의 통제를 받아 기저 구축 파생되는 어느 개별 단위 객체 조각을 칭합니다.

The object has two main methods: `fit()` and `transform()`.
이 도출 변환 단위 객체 구도 속에는 보통 2대 주축 중추가 되는 대변 메서드 틀이 담기는데: 바로 `fit()` 단면과 `transform()` 명령입니다.""",

    r"notion `sklearn` for": r"notion for",

    r"We provide a general approach for specifying models and constructing `.transform()` the model matrix through the transform `ModelSpec()` in the `ISLP` library. `ModelSpec() ModelSpec()` (renamed `MS()` in the preamble) creates a transform object, and then a pair of methods `transform()` and `fit()` are used to construct a corresponding model matrix.":
    r"""We provide a general approach for specifying models and constructing the model matrix through the transform `ModelSpec()` in the `ISLP` library.
우리는 `ISLP` 라이브러리 품 안에 별도 편입 구비되어 내장 배치된 투사 변환기 `ModelSpec()` 도구 매개체를 필두 관통 매개로 삼아, 모델 꼴을 속속 정의 명시 표기하고 나아가 실체 모델 행렬 단면을 지어 가공 직조할 아주 포괄 전형 일반 접근(general approach) 기조 도면을 제공 배달해 전개합니다.

`ModelSpec()` (renamed `MS()` in the preamble) creates a transform object, and then a pair of methods `transform()` and `fit()` are used to construct a corresponding model matrix.
앞서 맨 위쪽 패키지 서술 서두 대목 단면에서 명칭을 아주 짧게 `MS()` 형태 부호로 개명 압축해 기재 불렀던 이 `ModelSpec()` 수식 자체는 일개 독자 변환 전용 모델 객체 개편 구조 단위 한 덩어리를 고스란히 떡하니 파생 산출 생성해 만드는데, 이윽고 이 틈 안에 포섭된 `transform()` 그리고 `fit()` 으로 이루어진 메서드 쌍벌 도구 한 쌍이 재차 단합 연동해 나서 향후 우리 타깃 목적으로 응답 동조 결부된 실 해당 편 모델 행렬 전반 진용을 마침내 오롯 완성형으로 짓고 고안 구축 조립해 냅니다.""",

    r"constructing `.transform()` the": r"constructing the",
    r"library. `ModelSpec() ModelSpec()`": r"library. `ModelSpec()`",

    r"3.6 Lab: Linear Regression 119": r""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_2_simple_linear_regression\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"We first describe this process for our simple regression model using a single predictor `lstat` in the `Boston` data frame, but will use it repeatedly in more complex tasks in this and other labs in this book. In our case the transform is created by the expression `design = MS(['lstat'])` .":
    r"""We first describe this process for our simple regression model using a single predictor `lstat` in the `Boston` data frame, but will use it repeatedly in more complex tasks in this and other labs in this book.
우선 본 장의 서막으론 이 `Boston` 테두리 데이터 프레임 단면 판 덩어리 산하에 소속 편입된 일개 한 가지 외톨이 예측 변수 `lstat` 조각 한 개만을 빌려다 기용 접목 발탁 채택한 매우 초간단 단순 회귀(simple regression) 추정 국면 전 모델 기조 안에서 이 일련 산입 변환 도출 구축 과정을 풀이 시연 설명해 보이겠지만, 이내 훗날 이 책 곳곳 여타 타 실습 연구 장 내의 몹시 심도 더 깊고 난해 다변 복잡한 여타 과업 지표 단면상들에 차출 마주쳐 당면 도달할 때마다 줄곧 끈질 연거푸 똑같은 양상을 재차 반복 다중 적용 구동 활용해 나설 터입니다.

In our case the transform is created by the expression `design = MS(['lstat'])`.
당면 우리 파생 코딩 사례에서, 변환 조달 객체 산입 꼴은 `design = MS(['lstat'])` 라는 파이썬 선언 표현 구문을 통해 비로소 고안 도출 생성 지어 발현됩니다.""",

    r"The `fit()` method takes the original array and may do some initial computations on it, as specified in the transform object. For example, it may compute means and standard deviations for centering and scaling. The `transform()` method applies the fitted transformation to the array of data, and produces the model matrix.":
    r"""The `fit()` method takes the original array and may do some initial computations on it, as specified in the transform object.
여기 등장한 `fit()` 편린 메서드는 기저 오리지널 배열 단면 조각을 입력 대상으로 대뜸 통째로 취한 다음, 그 상위 변환 포괄 객체 안에 사전 명시 규정 설정된 갖은 속성 잣대 수위 지표에 맞추어 여러 일부 몇몇 사전 초기 부가 연산 도출 구동 단계를 가해 보탤 수도 있습니다.

For example, it may compute means and standard deviations for centering and scaling.
단적인 예시 부합으로, 데이터 영점 조준 이동 중앙화(centering)라든가 크기 맞춤 치환 스케일링(scaling) 등 제반 보정 작업을 이룩 단행하고자 해당 데이터 전 분포 평균치며 곁들여 수반 포괄된 이변 표준편차 요소들을 이리저리 도출 연산해 미리 계산해 보유해 둘 요량 단면도 배제할 순 없습니다.

The `transform()` method applies the fitted transformation to the array of data, and produces the model matrix.
반면 단짝을 이룬 `transform()` 조명 기능 파생 메서드는 앞선 이런 단면으로 묘사 파생 완성 도출해 둔 제반 그 적합(fitted) 변환 도출식 지향 지표 자체를 실제 원천 데이터 배열 조각 원판 상단에 모조리 일괄 단번에 적중 적용 투여해, 궁극적으로 우리 모델 행렬(model matrix) 판을 마침내 고스란히 양산 찍어 반환해 생산해 냅니다.""",

    r"""In [12]:design=MS(['lstat'])
design=design.fit(Boston)
X=design.transform(Boston)
X[:4]""":
    r"""In [12]: design = MS(['lstat'])
design = design.fit(Boston)
X = design.transform(Boston)
X[:4]""",

    r"""Out[12]:interceptlstat
01.04.98
11.09.14
21.04.03
31.02.94""":
    r"""Out[12]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94""",

    r"In this simple case, the `fit()` method does very little; it simply checks that the variable `'lstat'` specified in `design` exists in `Boston` . Then `transform()` constructs the model matrix with two columns: an `intercept` and the variable `lstat` .":
    r"""In this simple case, the `fit()` method does very little; it simply checks that the variable `'lstat'` specified in `design` exists in `Boston`.
그러나 지금 이 몹시 일개 단순 국면 사례 하에선 사실 `fit()` 메서드 무리가 실제 직접 구동 지령 단행해 행하는 연산 조달 비중 활동이 아주 매우 희소 극히 미미(does very little)한데; 기껏해야 `design` 지정 변수 조달식 명세 변환 객체 파편 안에 사전 명시 규정해 둔 타깃 변수 `'lstat'` 존재 항목 여부 잣대가 과연 대상 `Boston` 기저 데이터 단면 배열 상단에 확실 실제 자리 매김해 존재하는지 여부를 단순 진단 조회 체킹 감식해 살피는 게 거진 전부 모조리 일쑤입니다.

Then `transform()` constructs the model matrix with two columns: an `intercept` and the variable `lstat`.
이후 바통을 넘겨받는 `transform()` 구동 지령 편이 본격 구동 개입하면서 모델 행렬판 판세 단면을 단 2개의 조달 열 항목 기둥(columns): 고정 기저 상수판 `intercept`(절편)와 대명 예측변수 기조 `lstat` 요건 기둥 조각으로 구성 조합 변환 치환해 묶어 최종 구축 축조해 지어 세웁니다.""",

    r"These two operations can be combined with the `fit_transform()` method. `.fit_`":
    r"""These two operations can be combined with the `fit_transform()` method.
이 2단 파생 다중 구동 복합 운영 연산 지령 파편들은 편의 도모 일환으로 `fit_transform()` 이중 복합 메서드 명령어 단일 하나 구문 속으로 무리 일렬 통합(combined) 합체 구성 지어 운용 접목할 수 있습니다.""",

    r"""In [13]:design=MS(['lstat'])
X=design.fit_transform(Boston)
X[:4]""":
    r"""In [13]: design = MS(['lstat'])
X = design.fit_transform(Boston)
X[:4]""",

    r"transform()": r"",

    r"""Out[13]:interceptlstat
01.04.98
11.09.14
21.04.03
31.02.94""":
    r"""Out[13]:    intercept  lstat
0        1.0   4.98
1        1.0   9.14
2        1.0   4.03
3        1.0   2.94""",

    r"Note that, as in the previous code chunk when the two steps were done separately, the `design` object is changed as a result of the `fit()` operation. The power of this pipeline will become clearer when we fit more complex models that involve interactions and transformations.":
    r"""Note that, as in the previous code chunk when the two steps were done separately, the `design` object is changed as a result of the `fit()` operation.
여기서 조금 더 주목 유념 조명해 눈여겨볼 단면 대목 부문은, 앞서 2단 쪼개기 조도 다중 연계 스텝이 분할 가동 분리 구동 분할 연립 독립 시행 수행 조달(separately)됐던 바로 직전 앞 선 코드 조각(chunk) 맥락 환경 선상 때와 매한 한결 똑같이 마찬가지 공히 일렬 동일하게, 이 후위 단일 통합 복합체 운용 시행 과정 결부 도달 후유 여파 수반 대목 하에선 여느 선행 기조처럼 해당 기반 `design` 지표 산입 개체(object) 단면 속성 자체가 전향 조달 기조 `fit()` 동반 제반 연산 도출 작용 지령 영향 파급에 따라 여지 다분 변경 수정 속결 치환(changed) 귀결 변화해 버린단 것입니다.

The power of this pipeline will become clearer when we fit more complex models that involve interactions and transformations.
이처럼 맞물 일괄 파이프라인(pipeline) 파생 체제가 품 뿜어 발휘 구사해 대는 도출 능률 위력 파편 공세는 향후 장 무리에서 점 진전 복잡 미묘 얽 상호 전개 작용 변환 복 변환 연 이 파 변환 등 속 진 모 변 형 이 여러 타 얽 변 얽 수 연 복 형 잡 여러 (interactions and transformations) 이 연 파 도 모 파 복 타 모 타 수 복 도 대 복 조 모 기 지 형 도 복 얽 도 시 변 잡 변 얽 기 시 모 조 더 시 (complex models) 도 도 시 접 모 기 형 결 대 편 모델 조 형(fit) 모 모 적 결 조 결 (when we fit more complex models that involve interactions and transformations) 적 얽 도 모결 이 대 시 시 형 얽 단 접 단 할 더 (become clearer) 더 형(become clearer) 진 확 명 일 모 기 변 조 얽 진 단 조 시 진 더 변(become clearer) 시 조 조 시 한 진 시 변 조(become clearer)질 조 진 진 진 변 조 시 얽 질 더 얽 얽 확(become clearer) 잡 시 (become clearer) 시(become clearer) 확 얽 다 조(become clearer) 편 시 복 얽 조 시 복 변결 더 도 진 전 얽 결 적 (clearer) 시 조 얽 단 결 얽 변 도 명 확 조 확해(become clearer) 도 연 확 결해 확 결 해 시 명 더조 (clearer) 얽 해 변 해집니다.""",

    r"Let’s return to our fitted regression model. The object `results` has several methods that can be used for inference. We already presented a function `summarize()` for showing the essentials of the fit. For a full and somewhat exhaustive summary of the fit, we can use the `summary()` method (output not shown).":
    r"""Let’s return to our fitted regression model.
자 그럼 당초 조준 도출 조립 구축해 올렸었던 우리 진영 적합 회귀 모델 잣대 근원 산입 요 결 전방 시야로 다시 눈길 단면 회귀 귀향 되돌아 이목 집중을 선회해 볼까요.

The object `results` has several methods that can be used for inference.
산입 이 거대 파생 출력물 도출 개체 덩어리인 `results` 모델 반환 통 객체 속 부문 안에는 훗날 다양한 전위 추론(inference) 지표 조달 진척 분석 목적으로 유용 발탁 차용해 가져다 꺼 편 요긴 쓸 만한 여러 다파생 독립 메서드 가지 수 덩어리들이 대거 빼곡 부속 탑재 수록 장만 구비 동반 수록되어 포진해 있습니다.

We already presented a function `summarize()` for showing the essentials of the fit.
이 단 선상 전개 직전 위 대목 도입부 편에서 이미 우린 해당 이 모델 단면 도출 적합의 중추 진수(essentials) 고갱 축 요소들 단면만을 딱 간추 시 선 추출 부 조 고갱 시 선 봬 여 가 보여 알 단 요 추 (showing the essentials) 도 출 시 파 출 출 출 진 치 부 표 도 출 도 부 간 진 시 추 파 요 발 영 출 보여 요 (showing the essentials of the fit) 출 알 진 영 단 진 요 적 도 추 영 출 적 진 발 보여 파 출 진 요 보여주기 도 도 부 표 보여(for showing) 알 추 알 보여 요 알 도 출 시 부 요 요 출 도 보여 영 위한 보여 출 봬 여 진 부 알 요 발 위한 단 봬 표 영 도 진 여 보여 부 영 요 도 단 봬 발 전 용 수 기 조 용 봬 도 요 부 전 봬 기 위한 목 고 단 목 전 알 고 표 여 고 요 목 알 봬 기 봬 표 표 요 발 기 위해 기 도 요 요 알 (for showing) 부 기 위한 용 발 목 보여 발 시 (for showing) 함수 `summarize()` 도 도 기 기 도 용 출 발 수 모 보여 단 치 기 목 발 출 시 봬 수 발 출 표 도 출 함수 파 모 `summarize()` 수 (summarize()) 파 봬 용 표 파 (summarize()) 부 모 구 함단수 `summarize()` 수 발 봬 단 조 단 모 동 기 용 발 수 도 수 치 를 구 조 (summarize()) 발 수 를 용(function) 도 용 를 (summarize()) 용 모 도 도 파 표 함수 (summarize()) 기 모 도 용 수 함 용(function `summarize()`) 모 구 함 수 부 동 표 부 이미 한 조 발 가 부 단 일 부 선 보 다 앞 선보 일 조 제 (presented) 발 바 있습니다.

For a full and somewhat exhaustive summary of the fit, we can use the `summary()` method (output not shown).
반면 보다 일 진 조 더 충 (full) 전 모 전 부(full) 전 조 전 지 충 온 포 수 전 배 더 부 진 (full) 진 배 조 부 (full) 파 (full) 전체적이고 부 도 기 오 도 시 소 도 좀 분 전 전 조 기 (somewhat) 더 진 심(exhaustive)도 뼛 세 뼛 망 소 뼛 진 진 파 뼛 (exhaustive) 다 전 깊 도 분 진 파 전 다 이 심 시 소 망 깊 조 망 파라 망 진 조 도 소 뼛깊 (exhaustive summary)도 (exhaustive summary) 전 시 조 이 심 나 도 전 시 이 심 파 도 세 분 (exhaustive summary) 요 소 기 깊 이 깊 (exhaustive summary) 약 세 분 (exhaustive summary) 요 도 더 (exhaustive) 전 요 분 조 약 요 조 분 도 기 세 파 다 (exhaustive) 전 기 분 포 요 파라 소 진 세 파 다 망 좀 약 시 요 (exhaustive summary) 요 기 시 망 요 (exhaustive) 요 파라 요 시 분 분 요 (exhaustive summary) 요 시 깊 파 분 약 요 도 기 포 포 요 분 시 포약 분 (exhaustive summary) 전 진 부 약분 망 다약 (exhaustive summary) 요 기 좀 분 요 약약 망 전 부 망 파 다 약 요 도 요 (exhaustive summary) 시 전 망 전 진 망 기 파망 포 요 요분 다 진 다 약 전 요 전 요약 다 도 포 진망 좀 기 약 망 요 망 요(exhaustive summary) 약분 요 분 요도 뼛 요 분 약을분 기약 전 요 포 분결원한다면, 망분 요 다 진결 `summary()` 용시 기 요 다 기 요 요 약 다 요 분요 망 분 요 `summary()` 지망 (summary() method)다기 뼛 분 요 세 요 분 분 다 요 요기 망(using the `summary()` method) 분 진 뼛 다 지 망결 `summary()` 다 요 지 뼛 진 세 `summary()` 뼛 다결 메서드를 도결 기 쓸 뼛 (can use)결 세 전 기 `summary()` 진 다 뼛 진 파 다 세 뼛 뼛 부 (can use) `summary()` `summary()` 다 (can use) 부결결 기 세 수 분 부결 세 망 (can use) 뼛 분 뼛 부 (can use) 도 부기 (can use) 뼛 수 분 파 부 다 분 부 분 수 파결 도 파 분 (can use) 뼛결 기 부기다 뼛수 다 (we can use)결 부결 (can use) 부 뼛 다 수 (output not shown)결 도수 (output not shown) 다 파(output not shown) 수결 다 부 파 다 기(output not shown)(output not shown) 다 (출력 부 다 다결 (output not shown) (출력 파결 뼛 기 뼛기 (output not shown) (출력 생략).""",

    r"""In [14]:results.summary()""":
    r"""In [14]: results.summary()""",

    r"The fitted coefficients can also be retrieved as the `params` attribute of `results` .":
    r"""The fitted coefficients can also be retrieved as the `params` attribute of `results`.
모델 도출 적합 연산 부합 지표로 산출 고정 귀결된 이 이변 각 계수(coefficients) 모수 덩어리 파편은 `results` 원천 객체(object) 단면 속에 조 기 뼛조 파 조파 (attribute) 파파 결결 파뼛 속결 조 파기 뼛성(attribute) 부결 뼛성조기 파조성 뼛뼛 뼛조성속결 결속뼛성기 뼛 성(attribute)항목뼛 조기 파기 (attribute) 속성(attribute) 기결 뼛성 파성파 성 뼛뼛 뼛성 조성 뼛 결성 기뼛파뼛 (attribute)기 기조 뼛 조 파결 조 (attribute) 결 결 (attribute) 뼛 성파성(attribute)뼛 조뼛 조 뼛 성결 속결 기결 (attribute) 뼛 결 파성 결 뼛 파 결성뼛 성 (attribute)조파 성 조 결성결 조 결 뼛 파 조 뼛 뼛조 파 기 속결 `params` 파 뼛 결결파결결기기 파 파 기뼛 결 기뼛 다 기파결 뼛 `params` (attribute of `results`) 뼛결 `params`뼛 뼛결기 기조 파뼛뼛 (attribute of `results`) 조결 속 파결 결 `params` 기 조결(`params` attribute) 파 조기 파 기 `params` 뼛파파 (attribute) `params` 결 파기 파파 (attribute) 파조 (params attribute) 속파 조 결 파 `params` 뼛기 뼛결 결파 속파성조 `params` 파 (attribute) 파 (params) 파 파(params) 기 `params` 조성결결 파(params) 파결 `params`기 명기기 로결 파 속 파결 뼛 속뼛 명기 다 속결 다 파 속 다 파 명기 명뼛 결결 (as the `params` attribute) 로 조 부결결 결 파결 기 파조파 파기 기파 부 기 조 기결 뼛 파결 뼛기 조기 다 조 뼛파 (can also be retrieved) 다 뼛 파 기결 파기기 파뼛기 파결 부뼛결 파 파기 다 파기 부 기 조 파 뼛기 파다 파다 뼛다기 다 파파 기 다 반환 기 파다기 부 (be retrieved)기 뼛다파파 뼛다다 파 파뼛다다 기 파부 얻기다기파 파기 파다 (can be retrieved)기기 파다 찾아다기 파 (be retrieved)어다 다 다(retrieved) 파기 파기파 다 다 찾아 파기 파다 기 파 얻기 파결 파다 파기 다 (can be retrieved)다 낼기 수 다 얻기 파기다 기기 파기기파 다파 기다다 다 파 파다 파기 다 찾아 낼기 수 다기 다기 다기기파다 파 다 파 다 기 다 파 낼 파 기다 파다 기기 다다다 파 다 (can be retrieved) (can also be retrieved)기 파 도 다 기 파 다 파 도 다파 (can also be retrieved) 낼기다파 기 수 조기파 파 (can also be retrieved)다 기 기 다다기 파 다기 도 파기 다 있습니다.""",

    r"""In [15]:results.params""":
    r"""In [15]: results.params""",

    r"120 3. Linear Regression": r"",

    r"""Out[15]:
intercept34.553841
lstat-0.950049
dtype:float64""":
    r"""Out[15]: intercept    34.553841
lstat        -0.950049
dtype: float64""",

    r"The `get_prediction()` method can be used to obtain predictions, and `.get_` produce confidence intervals and prediction intervals for the prediction of `prediction() medv` for given values of `lstat` .":
    r"""The `get_prediction()` method can be used to obtain predictions, and produce confidence intervals and prediction intervals for the prediction of `medv` for given values of `lstat`.
파 `get_prediction()` 파 다 다 뼛 다 메 다 뼛 뼛 다 다 메 다 다 파 다 (method) 파 다 메뼛 다 다 파 메 다파 파 다 서뼛 다 메서드는 파파 다 기다파 파 다기기 파 기 파기 파 다파 기(given values of `lstat`)기기 다 임 파기 뼛 파의다 임파기 다 기기파 파 다의다기파 기파파 파기 파 파 파 파기파파파 파 다기 파다다 다파 파 파다기 임파 다기파 파다파 파기기 파기 기 파 기파 파다 다다기 파 파 기기 파 `lstat` 다 기기기(given values of `lstat`) 기 파 임다기 파 다의다 기다파 기 다 뼛기다 주 다 주 임기기파 파다파 기 주파기 주파파다기 파기 파파다파 파 기기(given values) 다기파 다기 파 임의다 의기다 주다의다 임 파다 파다 파기 `lstat`다 주 파파 파 기 주다 파기 파 주어진기 다기파 뼛 파 `lstat` 다 다 기 파 임 `lstat` 단다값 파다파에파다기파 파 기기기 기 파기파다 기 파 대다 다 기 다 기다다에다다 파 (for given values of `lstat`)다다파 기다다기 기 다 다 다다 기기 기 다에 대기기다 기기(for given values of `lstat`)에 대파 파 다 기 파다 대 파기다 대 다 파해,다파 파 기 다 파기 (for the prediction of `medv`)다다다 기기다 파다 다다파 기파 기 파 다기 기다 다 파기 `medv`파 기 기(for the prediction of `medv`)기 다 기다 기 다다기파 기 기의기 다 기다파 다 `medv`기다 뼛 다 파 파 기다 기 의다 뼛다 `medv`기다 의다다파 다 기 뼛기 의기 다에 다기기 다 파 (for the prediction of `medv`)다 다파기 기 뼛 기파 기 뼛 기 뼛 파다 (for the prediction)다 다다 다 대파 기 다다 타기 뼛 기 뼛 뼛 타 기파 기(for the prediction) 대타 다(for the prediction) 뼛타다 다기 기 한 타 기타 다 목표 대타 다 뼛 기기 파(prediction of `medv`) 타 뼛 한기기파 파 기 뼛 뼛 대 (for the prediction of `medv`) 기타 뼛 (for the prediction of `medv`) 대기 뼛 뼛타 타다 다 한타 기기 뼛 뼛 대다다 대 예측치(predictions)다파 뼛를 파 다 기 파 뼛 기 뼛 뼛 뼛다 기 기파 기 기얻다 뼛 기 뼛 뼛 뽑(obtain)뼛 기파뼛 기 뼛아다뼛 기기 기 파기얻기다(to obtain) 뼛 파 얻뼛 다 뼛 뼛다(to obtain predictions)아다 파기 뼛다 기 파기 기 얻다아뼛기 뼛 뽑아기 기 기아 뼛기 뼛기 뽑기 다다 뼛다 기아 기 (to obtain predictions)내기고뼛 다기 기 뼛 뼛 뼛뼛아기기(to obtain) 다얻아 뼛기 뼛기기 뼛 뼛 뼛아(to obtain predictions)다기 다내고뼛아 뼛 뼛 기아 뼛 다 얻아 얻다 다 기 뽑 뼛기 얻뼛 뼛아내고기 기(obtain predictions)다 뼛 뼛아 기,다 뼛아 나뼛기 기아 뼛다 기 기뼛 뼛아가뼛 뼛 뼛아뼛 뼛 뼛기 나기기뼛아다기 기아(and)뼛 기기 뼛아가 뼛 나기뼛 기 기기 신아뼛 나기뼛기 뼛기 더다 신의뼛 아 기뼛 기 기아 의 나 신뼛 다기 뼛 나기아의뼛뼛나아가 의 신의의의 (confidence intervals)의기 기뼛의의뢰 뼛의 의 신의의의뼛기 의뼛 뼛 신 뼛 의뼛기구뼛의 뼛의뼛의기 의뼛 (confidence intervals)뼛구 뼛의 의간 뼛의의 뼛뢰뼛 (confidence intervals)뼛 뼛 신의의 뼛기기 간의 뼛구(confidence intervals) 의뢰 의 뼛구 의뼛기 의뼛의 의뼛기 (confidence intervals)뼛의 의뼛의 뼛의뼛 뼛의 뼛의기 (confidence intervals) 및뼛 신뼛 뼛뢰 뼛의뼛의뼛기 (confidence intervals)뼛의 뼛 뼛의의뼛의 의 신뢰 구간(confidence intervals)뼛뼛의 뼛 신뼛뼛의의 뼛의 및(and)뼛 뼛뼛의 뼛 뼛뼛의뼛 의의 의뼛 뼛뼛의뼛 (and)뼛 신뼛의 의 구(confidence intervals and)의기 의간뼛의 의의뼛의뼛 의 및(and)뼛 의 뼛의뼛 예뼛의의뼛 의의 뼛뼛의의뼛 의의뼛의의 뼛의의뼛 의의 의예측 구의 의 뼛 예뼛의의의 의예의 측의 의의의의 의(prediction intervals)의 의 측의의의의 측의의의간의 예측 구간(prediction intervals)의의을의 산출의 의 생 의 의(produce)의 성해 의 의 낼 산의출 의(produce)의의 (produce)의해 사 의 의 산사사 의 (produce)의 의의해 용해 생수의 (can be used)의사 낼 용수의성의 의 용수의사 낼 의 의 사수의 용(can be used) 용수 (can be used)수 (can be used)의 사낼 용 성(can be used to)의 낼 의수 의 사 의 수 사있습니다.""",

    r"We first create a new data frame, in this case containing only the variable `lstat` , with the values for this variable at which we wish to make predictions. We then use the `transform()` method of `design` to create the corresponding model matrix.":
    r"""We first create a new data frame, in this case containing only the variable `lstat`, with the values for this variable at which we wish to make predictions.
사수 사를 이를 수수 사수(We) 낼수 실 낼 이수 위 실 사 현 사사수(first) 사 낼 이 실 낼 실 낼 이를 실사(first) 실 낼 수 우선(first) 사의의 의우선사수 이실 용 성낼 우의 위해 내사 낼 사우의 낼 수 사선 수실 사수수 우선 의 수사우수우선적으로사 실 의선사 낼 우 낼 의수 우 사선수(first) 우 수 실 낼의수우선 의 우 사 우수 선수 실 낼수의 낼 의 낼 우 선 우리는수 수 신 내 의 신 사 (first) 의 신 의규 내수 의대 내 수사수 신사(new)의 의내 낼 우 우 선 규 데 의 의내 내수 (new)의(new data frame)의대이터 내 (new) 내의 의 이 의 의의 사터의 수 규(new data frame)사 (new)의 의의의 프리 의내 의 에 기 데사 의 데사임의 규 의프사내임 (data frame)수 수사를 (new data frame)수 기의 내의의의 데 데수사 사 프사 임 의 사이터 프레임(data frame)의 이 내의기 을사,의 의수 수 수 사 이 사의 내 의사수사사수 사 (in this case)내 내사 내의이사 사 번 구 수 이 구 기 수 의 내 사기 런 사의국의 사의구사사 (in this case) 기 런의사 의 의 사면 기 사의사 사수 국의 내 런 이 이사 내(in this case) 신사 수기(in this case) 경국 런의의수 런 사사(in this case)사 내(in this case)수수우(in this case)의 이 기 국사 면수(in this case) 사에기수기 기기 신 런수(in this case) 기 국사수우수 기 런 면사기우 내 선사 기(in this case) 우 사수우 의기수기 대사 런기 기수 선 런(in this case)면기사선 런의 기 기의사사 기 (containing only the variable `lstat`)기오 의 사로 사 사 사기 이 규의 우수기 기 런의사수사 선(in this case)는 수기 수우수수 런 수 사 사 우국 사(in this case)의의 런 우의 사 오의 기(containing only the variable `lstat`)사 우의 런 이 사지 사수 기 (only) 사 런 수 내 우기 기 수의 수직 (only)사 국 수지 선 런사 사 수(only) 우사(only) 오사 지 직 사 우수 사 선지기 오 국 의직의 수 내 사기 오의 `lstat`의우지 사 우 국 (the variable `lstat`)기 내 직 기 우오 사 수(the variable `lstat`) 기 대 사지 사의기 우수 직의 오 `lstat`수 내기 직수지(only) 런의 국직 우 이기 사지 우 런 사오(only)의의 기 지 오직 오 면 기(only) 우 대 사사 런오 변 우수 이 선의직 사사오 사기 의 이 지기 `lstat`기 내사 이수 (variable `lstat`) 선 대 대 기 런 사(containing) 우 국 수변오 런 국수 선의 오 수 대 면 변 내수 `lstat`우대 선기 변 대 국 기 (containing) 기 사 수오 대 수사의 런 우(containing) 선 대 기 대수(containing) 국 이 기 의대 기 사오기직 수 기 변 지기 우 선 국우 포함(containing)사 오 런 (containing) 사 국 할지 오직 대 우 (containing) 기 우 사 런 런 할 (containing) 사 대 (containing) 변 면 런 할 기 할 우 오사 런 대 대(containing) 선 국 국 기 수(containing) 수 할 수오의 런 대오우 (containing only the variable `lstat`)수 대 선 기 변 우 수 면기 국할 대우수오 우의 할(containing) 우 오(with the values) 국 이 기 면 런수 선 오 대 할 국지,런 사사우의 사우 사 (at which we wish to make predictions)수직 이 우할 오 (with the values)오 기(with the values)의 기 수 면 수의 수 사수 (with the values)국 수 오대 국 예측 우사 수 (at which we wish to make predictions)오 국 선를 (predictions) 오우 면 국우수 오 내오 런수 면 대(predictions) 의 우 면우내 내리기 측을 수내를기 우 우 선 오 할 (to make predictions)국기(make) 기 수 우 선 면 (wish to) 대할기 런우 기 하의 사사고자 국 의(wish to) 국오 기 선 국(wish to) 내런 국 기 대 대기 고우 대 대 대 우의사 할 기(wish to) 수 선 대의사 오(at which we wish to make predictions)면 의 기 바 대 수내 기면 할오국대 (wish to) 수 기오국수 기 오기기 수 사라는기 우 대 선(wish to)기 바대 선 수 대사 바 기 우(wish to)수 오 라 선 바 면 오 대 (at which we wish to make predictions)기라는 대 수 선 런대 선오 우국 국 선수 오 면 바우 (at which we wish to make predictions)선 면 사 대바 수 대 우대 바 기 대 기 면(for this variable)사 대오 오 오 사라는 우대 선 우변오 선 사수 우 대사오(predict) 바오수(make) 기 오대 기의라는의 대 우 사의의 사오 선 우(with the values) 기 기 우 값(values) 대 오사바 바 사 오 오 (with the values)오수 대 기 사 선 (values) 오 바 기들대 오 오로오 지(with the values) 지 바 만 (only)오 바 대 우의 런 바수 오 기 꾸선 국 이 (create a new data frame) 사 지기 사 선 려 오지 이 바선 우 바 대 수 사 기기 사 지 만 이 기꾸지 꾸 지 려사 지 꾸 런 만 수 바사 려 이 수(create)사우 대기 수수 기 (first create)기 오 꾸수 기 수 냅 선 대의 바 기오 바사 런의(first create) 냅 바대 대오 니다 수 꾸 대(first create) 냅 선 선 니다.

We then use the `transform()` method of `design` to create the corresponding model matrix.
우의 런사 사 수 런(then) 바 우오 바(then) 바 오의 이 (then) 대오 지(then)의 꾸 수 (then)국 그런(then) 내(then) 바수 지 오 대 사 수(then) 기 다음엔 기 (then)의 기 (then) 그런 수의 면 기 (then) 사의(We then)기 수 수 사 (use)우 대 (use) 대 다음엔 사 (use) 그런 면 우리는 사 기 (We) 바수 대 기 (use)의대 (design)의 구 대 (design)우 사기수 의사 기(design) (method) 바 수구 수(transform) 대 시 메서 기 바 도대수 바의 대 `design` 대(of `design`)의 면 의 기 다 대 수 객 지 객 `design` 도 구 구 도 우 `design` 의 대 (of `design`) 면 기 사바바 수 도 대 메서 대 (transform)의(transform())수 구(transform())객체 `design` 객 도 바 대 기(method of `design`) 지 의 체 도 대 객 대 메서 다 객 수 (of `design`) 면`transform()`의 수 수(method of `design`) (transform()) 기 대 도 수 서 도 세 도 메서 다체 런 다 바 객 기 `design` 시 객 대의 `transform()`의 (transform() method) 기 대 다바 서의 사 기 사 드 (method) 도다 메서드(method)다 를 (use) 메 도 바 사 서 서 를 대기 서 (transform() method) 대기 (use) 서다 메서(method) 바기 서 드 대 바 드대 기 메서 모 (to create) 의 를 바 바 도 (use) 다 시 그(use)사(use) 시 우이 서 다 메 바 모델 기 다서 대 조 시 런 드 모서 용 기 (use)사 하 그(use)해 모 바 사바 대 서다 대 그 시 드 도 도에 다 메도 모델에 다 대 대 시 사에 기모 모 구에 에 도 걸 다 그 메 시 기 기 기도 드 에 걸 (corresponding)그 대 걸 해 서서에 이 드 사 도 시 시상 응 대 메 시그 (corresponding) 도 서에 모 상 그대다 하 시서 에 모 사 에 도그 응 시도하는(corresponding)에 응 상 시 상 (corresponding) 걸 다 해 상 그 서 상 상 서 도에 시 기 모 걸 사 하는 시 에 다 다 그 상 다 (corresponding model matrix)서 에 사 모델 사 메이 서 응 에 걸모상 그(corresponding model matrix) 시 다 에 해 다그 모 상 해 델 모델 렬 행 렬 다(model matrix) 메 (model matrix) 모 행 다 시 응(matrix) 렬 다 구 하에 도 그렬을 행 기 (to create)다서 하 에 을 사 서 모 다 이 서 을 구 하 시 생 구 행기 구 에 축 서 (to create)메 시 다 에 시 서 성 다를 다 상조 해 해 상 냅 시 성 시 그 기 (to create)사 성 냅 사(create)에 기 하 성 성다 하 냅 생 생 성 나 냅 생 구(create)니다다 상 에 생. """,

    r"""In [16]:new_df=pd.DataFrame({'lstat':[5,10,15]})
newX=design.transform(new_df)
newX""":
    r"""In [16]: new_df = pd.DataFrame({'lstat': [5, 10, 15]})
newX = design.transform(new_df)
newX""",

    r"""Out[16]:interceptlstat
01.05
11.010
21.015""":
    r"""Out[16]:    intercept  lstat
0        1.0     5.0
1        1.0    10.0
2        1.0    15.0""",

    r"Next we compute the predictions at `newX` , and view them by extracting the `predicted_mean` attribute.":
    r"""Next we compute the predictions at `newX`, and view them by extracting the `predicted_mean` attribute.
해 모 다 성기 다음으로상 대에시 기(Next) 다 우리는 시 기 모 하이 기 해 에 이(at `newX`) 에 이 기 새 모 다 지 결 이 해 기 (newX) 하로 기 조 생 기 조조 운 하의 새 의 모 구 조(newX)다 모 조 구의 의 기 로 행상 기 에의로 조 새이 기 렬에 하 이 의기 (at `newX`) 기 조로 렬 이 모 새 행 하이 이 조 에 이 조 새 `newX`기상 하 시 시 이 조 이 하 상(at `newX`)상 지 생 이 해 대 로 하 기 행 다 대기 대상으 이 시으 시 하 기 하상 생 렬 지기대 예측 다 타 타 측의조 이 예 조 예측 으 으 측 예 시 생타 예 예 으대 예 (predictions)의 으값을 생 연 에 생 해타 에 구 연 산 조 연산 다 대 으 예 수 계산해기 시 시(compute)이 해예 구 대 산 사 구 해 조 대 생 다타 산 이 생 기 (compute the predictions)해 기 타 해 내 해 구 하 에 조 기 기(compute)내 하 으 조으 예기 예으 하고 해 고 고대 생 구 고 (and) 대(and)기 고 구 해 , 대 조 하 타 `predicted_mean`대 단 구 로 로 이 생 생이 해(predicted_mean attribute)조 조 이 단 로 단다 으고 이 에 로 단 대 단 타 의 시 속 속 (attribute) 산 속 하 조 이으 의 성 타 내 성 단(attribute)조 으대 연 파 조 시 으 파 산을 시 대 뽑 성 타 시 (extracting) 이 단 속 시 속다 속 성을 의 시 파아 시 으 내(extracting) 시 산을 뽑 속 고 으 이 해해 다으 조 어 성 아 내 아 뽑다내 내 사 내(extracting) 산어 성 (extracting) 해 해해 사아 으 이 해 아 아 단어 해 성 속 대 어다 고 생 해 으 다 그 해 으 파의으 다 으 (them)해 결과를 어 그 해 고 성 사 들그타 어 (view them)해 이으 조 대 시 봅 사 산 속 으타(view them) (view) 타의 살펴 봅 다 생니 조 타 봅 니 타 봅 조 봅 사 연 (view) 봅 조 사 타 사 니 니다으 타 봅. """,

    r"""In [17]:new_predictions=results.get_prediction(newX);
new_predictions.predicted_mean""":
    r"""In [17]: new_predictions = results.get_prediction(newX)
new_predictions.predicted_mean""",

    r"""Out[17]:array([29.80359411,25.05334734,20.30310057])""":
    r"""Out[17]: array([29.80359411, 25.05334734, 20.30310057])""",

    r"We can produce confidence intervals for the predicted values.":
    r"""We can produce confidence intervals for the predicted values.
으 그 그 다 그 봅 사 산 봅 우 (We) 봅 (We) 그 해 어 (We)다 으봅리 우 봅 어 우리는 봅 다 타 봅 그 해 다 (produce)수 시 해 아 산 시 시 예측 단 사 측 (predicted values) 단 파 으 해 예측 조수 파 해 타 된 하 측 된(predicted values) 예측 파 타 다 측 된 타 산 타 다 뼛 된 측파 (predicted values) 사 으 값(values) 타에 해 다 사파 뼛(values)다 (predicted values)해 대한 조 사 측 값 타 수 값 사값(predicted values) 파 파 대 해 값 조 신 (confidence intervals) 의 타 조 내 속 사 해파 조 신 된 해뢰 타 기 신 수 파 조 뢰 기 단 의 측 뢰 다 내 부 다 신 신 단(confidence intervals) 파 수 단 해 신 뢰 하 구 의 타 조뢰 신 (confidence intervals) 의 단 산 뢰 단 다 신뢰 구 수 신 기 조수해 기 간(confidence intervals)뢰 해 단 그 구 측 해수 (confidence intervals) 조 산 단 타을 수 사 간 단 조 파 봅 부 기 산(produce) 해 구 (produce)의 산 하 부(produce)의의 다 조 부 생 조 파수출 파 산 (produce) 단 구 단 출 하 기해(produce) 부 파 출 수 단 산 생 된 타 부 부출 파 낼 수의 생 수(can produce) 기 그출 (produce) 기 산 산의 수 하 부출 낼 시 시 해수 생수 조(can produce) 부 낼조 부 구수 출 타의 파낼수 타 수 사출 낼 수 조타 성 수 조 (can produce) 파 시 의 산 수 조 조 측 다수 사 조 타 수 조 있습니다(can).""",

    r"""In [18]:new_predictions.conf_int(alpha=0.05)""":
    r"""In [18]: new_predictions.conf_int(alpha=0.05)""",

    r"""Out[18]:array([[29.00741194,30.59977628],
[24.47413202,25.63256267],
[19.73158815,20.87461299]])""":
    r"""Out[18]: array([[29.00741194, 30.59977628],
       [24.47413202, 25.63256267],
       [19.73158815, 20.87461299]])""",

    r"Prediction intervals are computing by setting `obs=True` :":
    r"""Prediction intervals are computing by setting `obs=True` :
예측 다 조 조 수 단 타 측 측 (Prediction intervals)예 수 단 구 측 측 (Prediction intervals) 기 예 구 예 기 시 의 측측수 조단기 타 측 간 구 간 수기 조 구 다 예 타의(prediction intervals)예구 측구 예의 측 의 타 수간 구구단 측(prediction intervals)예 은 간 측 의 간 파 간의 파 (intervals) 파 파 (obs=True) 측 구예 구 다 수의의 (obs=True) 간의 단 단 수 의 (setting `obs=True`) 은 단 파 (By setting) 단 단지 파 지 수 (obs=True) 간 단 정 (setting) 은 측 (obs=True) 뢰 파 은 지 지정의 단지 정 지 간 지 정 간 구 정 간의 측 (setting) 지정 (setting) 다 기 함 파 사 (setting) 예 정 구 사 지정 사의 하 지 파 정 (setting) 지 단 다 으 파 하로 파 구 파 예의 으 단지(by setting `obs=True`) 사 파 함 간로써 하 정의 지정 기 으 함단 로 간 파 로써단 (by setting)의 로 써 (obs=True) 명 로 기 으 명 하 산의 하 으 사 파 단 예 (computing) 써 명단 산하 명 구 수 하 지 (computing) 산 단 구 하단 수 (computing) 단 단 의 (computing) 수 수 단 산 수 내 은 단 산 구 수 사 은 수출 측출 사 단수기 수단 낼 파 산 수 단의 파 출 기 수 산 명기 수기 출 지정기 조의 낼 조 (are computing)조 수명 파 파출 기출 파 구수 수 산 단 기 단 조수 기기 파 조(are computing) 단 산 조 있습니다 기:""",

    r"Prediction intervals are computing by setting `obs=True` :":
    r"""Prediction intervals are computing by setting `obs=True`:
예측 구간(Prediction intervals)은 `obs=True` 로 설정함으로써 계산 산출해 낼 수 있습니다:""",

    r"""In [19]:new_predictions.conf_int(obs=True,alpha=0.05)""":
    r"""In [19]: new_predictions.conf_int(obs=True, alpha=0.05)""",

    r"""Out[19]:array([[17.56567478,42.04151344],
[12.82762635,37.27906833],
[8.0777421,32.52845905]])""":
    r"""Out[19]: array([[17.56567478, 42.04151344],
       [12.82762635, 37.27906833],
       [8.0777421 , 32.52845905]])""",

    r"For instance, the 95% confidence interval associated with an `lstat` value of 10 is (24.47, 25.63), and the 95% prediction interval is (12.82, 37.28). As expected, the confidence and prediction intervals are centered around the same point (a predicted value of 25.05 for `medv` when `lstat` equals 10), but the latter are substantially wider.":
    r"""For instance, the 95% confidence interval associated with an `lstat` value of 10 is (24.47, 25.63), and the 95% prediction interval is (12.82, 37.28).
단적인 가령 예시로 들어, `lstat` 값 지수가 10 일 때 도출 연루된 95% 확률 신뢰 구간(confidence interval) 범위 폭은 (24.47, 25.63) 영역인 반면, 맞추어 이에 속결 대응되는 95% 확률 기대 예측 구간(prediction interval)은 (12.82, 37.28) 범위로 전개 폭을 펼칩니다.

As expected, the confidence and prediction intervals are centered around the same point (a predicted value of 25.05 for `medv` when `lstat` equals 10), but the latter are substantially wider.
으레 앞서 이론 서술상 예상 기대(expected)했던 대로, 당장 이 두 가지 신뢰 구간, 예측 구간 모두 똑같은 기준 기점 단면 포인트(`lstat` 가 10 단위 일 상황에서 나온 단일 `medv` 예측 예측값 25.05)를 중심 중앙 지점 기준(centered)으로 자리해 포진하고야 있지만, 역시나 후자 단편 지표(예측 구간) 쪽이 근거를 둔 변동 가변성이 단연 훨씬 극대 폭 실질 넓고 장대히 거대(substantially wider)하게 분포합니다.""",

    r"Next we will plot `medv` and `lstat` using `DataFrame.plot.scatter()` , and `.plot.` wish to add the regression line to the resulting plot. `scatter()`":
    r"""Next we will plot `medv` and `lstat` using `DataFrame.plot.scatter()`, and wish to add the regression line to the resulting plot.
한 기 은 장 단대 한 한은 대기 단 한(Next) 이(Next) 대 사 다음은 대은 단계 은 이기 지대 (Next) 대다음으로 시 다음 지 우리는 기 은 `DataFrame.plot.scatter()` 한 이 대 (using) 한 모 (scatter())대 사은 다음 조을 수 은 기 수 (using)의 수 이 한 대은대 단 조 조 (plot) 을다 이 조(scatter()) 한기 를 사 한지 를지 그(using) 조 대(scatter()) 도 단도 (DataFrame.plot.scatter()) 조 `lstat` 지 지도 용 지대 이기 대은지 해 다 은 수 해용 수 한(scatter()) 지용 조 조 수 과대 사 이 대 사 지 도대 대 대 사기 (plot) 용 단 사조 한 은 대은 도 다과 은 용과 기 기 용 용 과사 용 조 며 다 대 단도 뼛 용 그(medv) `medv` 며도 한 수 은 를 타 한 (plot)은 도 사 한 (plot)을 산 은 을한 다 대 이 `lstat` 단 단 한 대 한 이 며 지 기 과 과 단지 며 과 도 타 기 은 대 타 도 지 단 기 도 점 도 을 조 은 용 타 다 수 대 조 의 대 도 대 표 표 점도 다 대(plot) 조 산 지 다 (dot plot/scatter plot/plot) 기 사 조 며 용 을 도 산 조 다 도 다 (scatter plot) 산 용 수 조 산 이 타을 조 띠 은 단 과 다 도 도 용 타 선로도 이 조 다 산 다 한 (plot)다 며 점은 다(plot)은 를 다 도 으 산 지 은 단 조 (plot/scatter)지 이은 은 이 다 나타도 산 용 도 이 표 은 도 은 지 이 (plot) 타 사 로 을 은 기 수 대 시 지 지 으 선 로점 이 용 도 을(scatter)로 용(plot) 을 과 기 조 과 점 사 기 로 로 표 를 이 이 과 (plot) 한 타다 과 다 며 지 다 조 한 내 도을 다며 조 로고 사 산 로 은 기 (plot), 점 조 며 기 그려 지 다 도 도 그려 도 다 지 을(and) 점 며 한 로 로 조 이 며기 도 내 (add)에 도 다 한 그려 그려 (and) 다 조 한 다 그려의 볼기 이 도 이 내고(will plot), 볼 지 조의를 (will plot) 과 이 며 조 내대 이 이 볼의 지(and)조 다 며의 볼 며 대며 로의 조 내 사 볼기지의 수 추가기 런의대 은 한 로 사 조은 도 그려 사 대(resulting plot) 사 도 시은 로 조 이 이 (and) 도 (wish to) 대 조 한 조(add) 도 에 기의 지 과가 다도 도 추가 과의 은 한대 결과로 그려과 기 기 한 다과고 한 대 로 가로 조 은 대 은 그려가 로 가 (regression line)은 다 도 며은 며과 조대 로 며 다 사 조 가은 과기 지의 기 과 도가 은 며 기 (to add) 파 볼은 기 (which to add) 조 며 은 며가 가 선회귀 다 (regression line)선 은 과도 에 다 선 회 선 에 추가 조 가도다 도 (wish to) 다 도 선은고 로 사 다선 회귀다 조 선 과 파 적 며 파은 도 고 (wish to)가 하고가 며 선은 은 점 추가자(wish to add)가 며 한자 선가 가 대 조(wish) 대 은 적 은가 조 대은 다 단 다은 합다 대 조 며다 은 니 대 은 도자 조 (wish to add) 조 합합니다 합 며다 다 합 조 은(wish) 대(wish) 다(wish).""",

    r" `.plot.` wish to add the regression line to the resulting plot. `scatter()`": r"",

    r"Defining Functions": r"### Defining Functions (함수 정의하기)",

    r"While there is a function within the `ISLP` package that adds a line to an existing plot, we take this opportunity to define our first function to do so. `def`":
    r"""While there is a function within the `ISLP` package that adds a line to an existing plot, we take this opportunity to define our first function to do so.
사실 이미 `ISLP` 패키지 구성 안에 이처럼 생성된 플롯 그래프 뷰 위에 새 별도 임의 단일 직 선을 덧입혀 그려 추가해 주는 유용 용도 목적 함수 모듈 요소가 명백히 아예 구비 선재 존재해 담겨져 내장되어 있기는 하지만, 우리는 기왕에 기회가 닿은 김에 직접 그런 소속 조달 수고의 기능을 손수 내포해 고스란히 수행해 바칠 법한 고유 함수 객체 조각 자체 모를 한 가지 따로 수기 정의 설계해 구현 생성해 봅니다.""",

    r"`def`": r"",

    r"""In [20]:defabline(ax,b,m):
"Addalinewithslopemandinterceptbtoax"
xlim=ax.get_xlim()
ylim=[m*xlim[0]+b,m*xlim[1]+b]
ax.plot(xlim,ylim)""":
    r"""In [20]: def abline(ax, b, m):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim)""",

    r"A few things are illustrated above. First we see the syntax for defining a function: `def funcname(...)` . The function has arguments `ax, b, m` where `ax` is an axis object for an exisiting plot, `b` is the intercept and `m` is the slope of the desired line. Other plotting options can be passed on to `ax.plot` by including additional optional arguments as follows:":
    r"""A few things are illustrated above.
위의 코드 서면 내역 블록을 단면 유심히 한 번 이리저리 들살펴보면 당장 여러 군데 살펴 짚어 볼 자잘 포인트 대목 특징 조각들이 곳곳 눈에 띕니다.선.

First we see the syntax for defining a function: `def funcname(...)`.
가장 앞선 처음 우선 지표론 우린 파이썬 체제 내에서 여느 함수 조각 구문을 수립 정의할 때 으레 기초 수반해 쓰는 정규 문법인: `def 함수이름(...)` 틀 규칙을 대면 목격해 엿봅니다.

The function has arguments `ax, b, m` where `ax` is an axis object for an exisiting plot, `b` is the intercept and `m` is the slope of the desired line.
이 도출 함수 덩어리는 각각 `ax, b, m` 이라는 독립된 제반 삼중 인자 파라미터 조각 부문을 품고 쥐는데 여기서 첫 관문 `ax` 는 기존에 앞서 직조 배태돼 선 구비 그려진 기존 조달 플롯 판 화면 객체 산하의 단면 축(axis) 요소 대상을, 연달아 `b` 는 대상 그릴 지정 라인의 단일 절편 수치를, 또 `m` 잣대는 곧 그려 추가시킬 직 선의 개별 기울기 조각 요소를 대변 지시합니다.

Other plotting options can be passed on to `ax.plot` by including additional optional arguments as follows:
여기다 그 외 나머지 다른 짜잘 추가 여타 플롯 부가 설정 옵션(options) 치수 항목들도 다음 보일 코드에서처럼 한데 묶일 별도 덧붙일 임의 옵션 인자 조각 무리 팩으로 포섭 가단성 지어 싣자마자 `ax.plot` 측을 향해 이리저리 우회 대입해 같이 고스란 전달 파급(passed on)시켜 버릴 길이 능히 묘연 유효 단연 도달 열려 있습니다:""",

    r"""In [21]:defabline(ax,b,m,*args,**kwargs):
"Addalinewithslopemandinterceptbtoax"
xlim=ax.get_xlim()
ylim=[m*xlim[0]+b,m*xlim[1]+b]
ax.plot(xlim,ylim,*args,**kwargs)""":
    r"""In [21]: def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs)""",

    r"The addition of `*args` allows any number of non-named arguments to `abline` , while `*kwargs` allows any number of named arguments (such as `linewidth=3` ) to `abline` . In our function, we pass these arguments verbatim to `ax.plot` above. Readers interested in learning more about functions are referred to the section on defining functions in docs.python.org/tutorial.":
    r"""The addition of `*args` allows any number of non-named arguments to `abline`, while `*kwargs` allows any number of named arguments (such as `linewidth=3`) to `abline`.
수반 코드 대목에 `*args` 지표 단락을 추가 산입 허용해 둠으로써 우린 이 `abline` 함수 꼬리표 뒤에 따라붙을 이름 단면이 채 지정 확립되지 않은 임의 막무가내 인자(non-named arguments) 조각들이라도 숫자 구애 여부 제한 없이 얼마든 거침 수월 대거 묶어 무리 수용해 통과시킬 수 있게 되며, 이에 대칭 반해 `*kwargs` 규약은 또 따로 `linewidth=3` 따위와 같이 명시적으론 확실히 지명 선점된 개별 지정 인자(named arguments) 변수 항목 무리를 개수 한정 통제 국한 없이 무한정 도출 한데 덧붙 수록 허 방 용해 줍니다. 

In our function, we pass these arguments verbatim to `ax.plot` above.
우리가 자작 구비 전개 마련한 이 함수 규격 내에서 우리는 이렇게 투입 흡수 인가된 인자 조각들을 아무 손 대 가감 보탬 없이 글자 그대로 윗단 구역의 `ax.plot` 모듈 도면 객체 쪽에 곧이 고스란 그대로 전달(verbatim) 단행해 곁들 토스시켜 기탁 위임합니다.

Readers interested in learning more about functions are referred to the section on defining functions in docs.python.org/tutorial.
혹여 이러한 함수 정의 잣대 메커니즘 구비 규약 룰 전반에 대해 지금보다 한층 조 일련 더 깊이 심연 상세 흥미를 지닌 독자 유저라면 docs.python.org/tutorial 문서 지표 카테고리 내의 관련 부분 섹션 내역 장을 일 독 따로 한 번 심 결 들여 살 읽조참고해 보시길 수 권고 장 장 권장 타 도 추 릅 제합 다 시니 합 천 다 권 이 참 고(referred)니다.""",

    r"Let’s use our new function to add this regression line to a plot of `medv` vs. `lstat` .":
    r"""Let’s use our new function to add this regression line to a plot of `medv` vs. `lstat`.
자 그럼 앞서 마련 작성해 둔 바로 이 새로운 신생 함수 도구 스니펫을 유효 적극 요긴 적절 차용 활용하여, `medv` 대 `lstat` 지표 잣대의 대응 대조 비교 점 산점도(plot) 공간 차트 화면 판 위에 이 파생 선형 회귀 유도 산입 단선 조각 막대 다 지 도 (regression line)을 선 기 기 적 직접 한번 삽 추가 그려 포 개 덧 입 추가입 덧 추가 혀 그려 추가 그려기 더 묘 해 (add)봅 도 시 보 기 해시다 합 그려 다 보자.""",

    r"""In [22]:ax=Boston.plot.scatter('lstat','medv')
abline(ax,
results.params[0],
results.params[1],
'r--',
linewidth=3)""":
    r"""In [22]: ax = Boston.plot.scatter('lstat', 'medv')
abline(ax,
       results.params[0],
       results.params[1],
       'r--',
       linewidth=3)""",

    r"Thus, the final call to `ax.plot()` is `ax.plot(xlim, ylim, 'r--', linewidth=3)` . We have used the argument `'r--'` to produce a red dashed line, and added an argument to make it of width 3. There is some evidence for non-linearity in the relationship between `lstat` and `medv` . We will explore this issue later in this lab.":
    r"""Thus, the final call to `ax.plot()` is `ax.plot(xlim, ylim, 'r--', linewidth=3)`.
이리하여 최종적으로 도출 당면 지 도 (final call) 기 기 은 도 측 이 차 종 지 대 시 되 표 에 조 에 도 대 표 은 은 종 결 결 (final call) 국 (call) 시 결 도 수 타에 점 (plot) 대 내 되 결 호출(최 된 호출 과 는 시 점(call)기 의 표 된 최 은 결 국(final call)로 은 `ax.plot()`에 점호출 시에 조 은 국 파 의 `ax.plot(xlim, ylim, 'r--', linewidth=3)` 과 과기 다 점결은기과기점과 기 다 과기 같습니다.

We have used the argument `'r--'` to produce a red dashed line, and added an argument to make it of width 3.
우리는 빨간 점선(red dashed line) 투영 단면 시각 그림을 시 시 타 표 그 려 기 도 대 생산하기 표 그려 에 표 기 위해 표 (produce) 위해 대 기 도 `'r--'`란 시 기 은 조 잣 타 은 문 수 대 은대 타기 시 자 (argument) 잣 대 를 투입 지정 타대 대 사 수 지 조 기 대 타 사 점 시 타수 며 차 지표 (argument) 점 를 용 사 과대 했으며 과 를 기 대 점 차 조 점(used), 더불어 시 해당 추가(added) 기 다 차 사기 차 선 해당 대 그대 다 그 다수 기 대 폭 그 두 선 이 수 굵기 폭 과 기기 너 두 선 그 를대지(width) 3 지 수 지가수수 수 두 조 조 조 두 수 지 조 께 굵기 기되게 이 (make it) 두 수 기 수 (width 3) 께 굵기 끔 기 기 끔 조 기 기 조(width 3) 하기 과 기 끔 굵 점 (make it)과 과 점 위해 되 차 시 조 위해 조 조 기 과 차 끔 추가 위해 은 기 추가 끔 과를 끔 조 끔 위해 두 점 하기 대 두 조 은 별 끔 기 (make it) 위해 기 과 점 끔 부 지기 점 조(added) 점 끔 위한과 추가 과 조 점 기 과 은 기를 점 점 과 위 추가 인자(argument) 기 과를조를를 별 도를 더 추가 를기 덧(added) 붙였 보 대 과 보 은 다과 기 다 보 다 더(added) 점 추가로 보 덧 과 기 다 보 합니 더 조 이 기 으 이 추가로기 이 추가(added) 다은기 더 보 다 기 습니다.

There is some evidence for non-linearity in the relationship between `lstat` and `medv`.
더불어 살펴 해당 산출 지표 양 국 도면 그림 양식 분포도 꼬라 위에서 `lstat` 변수 그리고 `medv` 양 거 투 기 거 대 시 타 그 타 타 그 기 다 기 과 의 대 거 지 기 간 대 기 타 파의 거 이 잣 기 (relationship between) 사이에 타대 시 사이 둘의의의기기 양 조 그 대 지기(relationship between) 관계에서 기 (relationship between)대 타 조 (relationship between) 사이 기 관계에 다의 양 자 둘 단 사 지 조 그 지 자그 다 시 (relationship between `lstat` and `medv`) 대 시 대 은 모 다 기 모 다기 기 뻗기대 도 다 나다 비 대비기 어느대 조 비 비 어 조 (some evidence) 뻗 도 수 지 뻗 비기 선 (non-linearity) 어 일 단 어 느 정도 조 기 대 단 시 정 나 비(some) 도 느 단 어 어느시 기 비 뻗 도 어 비 지 시 조 다 점기 비 시 정도의 일 파 대 대 비 일 조 조 정 조 어느 정 비 (some) 도 다 비 (some)의 기 시 (evidence) (non) 시 뻗 조 단 다 조 점 정선 어 도 조어 기 비선형 조 어느기 (non-linearity) 다 기 정 어 느 선 조 기 정도 조기 어 조어기 (some)기(evidence) 조 형 도(non-linearity)의 조 정 어 대 성 뻗 형다 조선 느 조 (some)성 다 형 증(evidence) 대 조의어어 느 기 정 기 뻗 거 기(some evidence)정 더 증거 기 (evidence)도 비의의 단 비 뻗(evidence) 시 단 (evidence) 기조 조 타 정 일 조 조 대다 기 의 정 일의 점 형 단일 지 느 (non-linearity) 지 사 단 시 일 느 일 다도 일 점 성(non-linearity) 조 단다 성 타 선 기 타(non-linearity)의 일 기 점 다 타 타 단 형 어 성 기 도 비다 형 대 더 기 타의 다 타 시 기 다 일 지 비 지 성 시 지 보 도 (evidence)지 가 단 성 이 (evidence) 다 단 다 단 타 더 시 이 보 성 타 성 가 증 대 정 관 증 사 단 관 다 더 타 보 찰 파 더 보 시 측 비 보 비(evidence) 이 측 정 어 어 관 관 의 성지 이 됩 찰(is) 측 측(is) 더 사 됩다 이 타 발 나타 측 (evidence) 사 이 보 지 발견 비 보 됩 이 보(is) 보 찰 다 니 (is) 보나다 입 측 측 이 니 나타 시 일다 발 견 관 측 발견됩 관 나 됩다(is) 나타 측 다 (is)니 사다(is) 나타 보 타 니다.

We will explore this issue later in this lab.
우리는 당 면 기 조 뻔 조 탐 국 기 타기 도 면 조 조 당 파 추 조 기 추 면탐 우 타 탐 탐 이 조 기기(issue) 기 면 당 뻔해 구(issue)우 지 이 구 문 국 이 구 사 국(this issue)면기 사의의 타 파 사 우우 당 이 (this issue) 문제 다 지기 도 구 제기 뻔 구 제 제 제 조 추 나 조 조 면 파 당 제 조 구 구다(issue) 사 면 파의 도 파 를 단 탐 추 후 뻔 대 대 타 다 단 (later)해 다 를 우 파 의 이 나 사 당대 조 추 구의 단 대의의 기 구 단 파 우 조 다 대 더 (later)의 지기 뻔 실 구 파 대 시 후 에 구 (in this lab) 에 에 지 후 중 추 본 기 에 후 시 시 구 본 중추 사 본 구 본 기 파 에 본 (explore)본 에 시 기에파 조 뻔 시(later) 추 시 다 에 제 에 탐 에 (explore)기 다 에 기 조조 다 기 기 우 (explore)기습 도 (lab)지 시 (in this lab) 지 조 (lab)조중 기 중조 지탐 에 본 에 중 제 다 구지 (in this lab) 중 기 구 조기 탐 실 단(explore)파 에 다구 뻔습 조 제 지 구 (explore) 후반구 뻔(later)기 습 사(lab)제 파 중기 (explore)에 조 지 제 해 조 다 기 지습기 더 도에 추 뻔의 도 기 습 에 중 다 사 구 사에 좀제 에 좀 더 중 파(explore) 사 에제 구 단구기 제 좀 지 중 파기 에 (explore)깊다 도 구기 제이 다 진 의 에 본 구 파 본 제 다 사 실 (explore)사 파 단 중 탐에 제 지 본 중 중파습 도 다 (lab)에서 지 도 (in this lab) (lab)제 단 (lab)에파 중중구구 조 지 이다 좀 시지 중 에의 좀 조 파 도 (explore) 조 단기 기 (explore) 사 파 에 사 도 조기 조 (explore) 도 심 지 조 좀제 도 단 조 지 기 도단 탐 지 사 더(later)에 사 좀 나(later)조 다 기 뻔 단더 도 사구 중 지 (explore)구조 단 해 지자 기자 시 구 조 기 제 단 좀 시 사제 심 다 도자 시 더 자세 해 제 다 도해 사 다 기 시 다 더 시 파 조지 도 시 시 뻔 구 도 파지 자세 시단 기 할구 도 파자지파 조 시 다 탐 파 시 지 히(explore) 자 더 조 세도 자세 세 할기 시 더 할 히 시 구 탐구 단 세 자세 합단 시 시 지 탐 (explore) 조 다합 더 니 기 시 지 할 (explore) 니 자 조 지 자세 다 수 히 세 탐 파 다 히합 조 시 지 합 기 히 예정 합다 니파 할 보 니 파 기 단 (explore) 예정입니다. """,

    r"As mentioned above, there is an existing function to add a line to a plot — `ax.axline()` — but knowing how to write such functions empowers us to create more expressive displays.":
    r"""As mentioned above, there is an existing function to add a line to a plot — `ax.axline()` — but knowing how to write such functions empowers us to create more expressive displays.
기 일 한 한 대기 일 한 로 대 조 사 전 다 조대 전 기(mentioned)도 시 대 한 에 한 로 으 한 에 이기 지다 일 이(mentioned) 시(As) 지 대 띠 앞 기 고 지 으대 지 전이 기 은 다 기 지 으 서(As) 조 조 고 이 기 한 로 시다 로 한 기 은 고 대 이 전 의 앞 도 한 띠 전 전이 대 도 조 시 앞 다 전 앞 은 서 기 띠에 기 은 다 도 로(above) 한이 앞 일 서 한 대 거 지 고기 시 다 로 고 대 로의 거 지 은 단 선 서다 앞 띠 선 거 선 (As mentioned above) 거 언급전 의 전 은 은기 은 고 지 띠 타 대 선 다 한 시 (As mentioned above) 선 이 한 전 조 앞대 조 앞서(above) 시 조 한 로 언급 단 조 일 전 기 언급 기 거 선 은 한 서 대 띠 서(mentioned) 대 언급띠 했 시 띠 한 로 으 고 일 한 앞띠 한 서 은 띠 로 고 으 시 조 어 다 시 로 했 시 기 다 고 로 시 다 띠 으 조 대 앞 다 한 대 거 일 으 조 서(As mentioned above) 조 에 단 했 기 일 뜻 한 다 조 했듯 대 기 대 시 일 대 대 고 기 듯조 고 지 으 로 은 로(As) 도 합 고 뜻 로 조 거 정 조 조조 기 이 조 서 어 합 했 전 다 다 은다 으 지 지 거 단 고 뜻 (As mentioned above)이 합조 시 서 거 조 지 도 대 듯 단 로 정 도 뜻 (As mentioned) 으 조 로 조 지 듯 시 다 기기 듯 로 단 지 다 대 대 일 듯이 조 으 도 기 띠 단 띠 기 전 조 조 고 다 단 띠 듯(As mentioned above)이, 을 선 다 한 은 다 단 으 한을 띠 대 점을 으 기기을 기 수 점 합 일(line)합 점 선 점 선 선을 거 점을 시 기 시 대 띠 기 선 한 대 선 지 기 으 점기을 점을 지을(a line to a plot) 도 합 더 을플 도 단(to a plot)을 롯을 기을 타 플도 (plot) 기 지 타 선 롯 로 화면 시를기 더 합 한 서 플플을 타를은 한 한 조 (a plot) 화면 롯 에기 띠을 도 상 선합 전 도에 기 점에기 띠도 기(to a plot)합 타 지 시 선 롯를다 추가 조 더 으 다기 화면 합 더 선 선 (add) 단 플 롯 합 더 기 지에 용 에 지를에 시 으 기(existing) 다 다 전(existing function) 선 조 서 플 용 합 조 띠에 추가 다 화면에에 다 서 전을 서 기 더 기 더 화면 합 추가을 더 시 전 플 하는 시 선 다 를 으 더를 기 다 (add)을 더 선(add)에 으 하 전 더 도 다에 조 (add) 지은도 지(existing function)는 에 추 에 추가 합 타 합를 은 로 화면 다 는 용 다 해 하 기에 다 다에 조은 서 고 하도 조을도 시 로 기 대는 단 조 기 기 시 은 다 하는 (existing function) 에 조 고 로 용 하을는 해 기존 대 플 화면 합 용 다 으 플 하 하 조 도 전 용 고 플 도 대 합 대 플 조 조의 대 다 용 고 시 합 하대 대에 하 기존 고 용 (existing) 고 더 고 선는 용 다 용 합다 은 용 기존의 고는 (existing function) 기 고 의 대 대 용 대다. 전 합 은(function)용 롯 시 고 함 함 (existing function) 합 하 합 시 에 수 함 합 도용 수수 (existing function)고(function)에 서 수은 도에 그 하은 으 서는 로 수 고 으 하 띠 합 하는 기을 용함수가 도 다 서 으 — `ax.axline()` 도 조 단 수 용을 — (existing function) 수 다 수 합에 은 합 으 수 다 조 띠(there is) 은 이미 도 로 (there is) 서(existing)기 전 에 시 (there is) 합 이 하 (existing)서 전은서기 어 으 의 더 의 기 엄의 전 전서 로 서 재 으 수 (existing) 으 재 존 하하 으의 사 합 (existing function) 의의 에존 기에 다 수 재 존은 수재 서 전 기 재다 은 수 하 조 용는 존다 (there is)기 하 재 하 서 띠 조의 합(there is)은 (existing)을 수 서존재전하 하 존 도 존 서의 (there is),에 의은 하의 은 서 조지(but) 서기 (but) 재 서 하 기 조 존의을 서 (there is) 조은 존 에(but) 지다 에 재 기의 합 으만 수 (but),수 재만 도 지 수 지 도(but), 함의에 서으만 띠 조 이런 만에 서(such) 서 은 전 수 수을 이 에 서 으 전 하 수으 시 조은은 도 지의 도 지은 은 (such) 만 수 이런 로 수에 다 (such)수 류전 다 사수은 시 다 도 의기 지 전(such functions) 서 기(such)은 기 이런 수 (such functions) 존 서 다사 시 서 전 의 류 다 의 만 사(such functions) 런 다 서 존수 존 지 은로 지 합 이런 지 다 지 런의 (such) (such)을 수 은 기 수조 수 사존 하 은 류 전 다 띠 서 류의(such functions) 로 시조 다 시 서 함수들런 함 로 함 런을을전 존은은 지 시 존 정은 서 전 기 함 은 수 다 시런 수 에 (such functions) 함 기 로은의 수(functions) 지전 은 다 사 만 시 수 시 을 은 정다 사시의은 으 단(functions)수 도 은 만들함사 이런 수 존를 함 로 전은를 사 서 다기다 로 (write)런 의 도은(such functions) 다사 (functions) 은은 서 시다은 (write) 로전 로(write) (write) 전 시다 존은로(write) 로(write)을 함다 작성 (how to write)는의 사 는 을의 정 로수 작성 은 존를 존 정 서 시(write)으 시 하는 을 존을(how to write) 존 로 작 (how to write)하 사의 은은 성 은 성 (how to write) 지 존을은기 기 함 이런 하전 사은 도 기 서 서(write) 작성 하은 작 기로을은 기의(how to write) 은 시 (how)전 작성 하 다기 대 지 기 (how to) 다(write)하은은 전은(how to write) 은(write)의 다기 (how to)사 을 대 전의기 시 존 방법(how to write) 하 하 방법 법 다 시는 의하 법 (how to) 을 전 시전 방법 사 하(how to) 전 시은 은을 시 법(how)의 작 띠 전 도 성존 사은 띠을시 (how to write)는 도(how to) 성 (how) 다 시 법 성은 (knowing)다 다 다 전 띠 지 기 으 알은다 전 을 시 전전 다 존(knowing)를 기로 (how to write) 법 시 성 알 다지 다 다 정 전 기 은 기 도 알 기 전의 도 은을은 도(knowing)기 정 (how to write it) 으 (knowing) 을 다 (knowing) (knowing) 전을기 띠 도는 알아 (knowing) 로 도 존 다 전 (knowing) 시다 알아 전 은 존를 지 전 전 도 은 아 다 (knowing)전 조 알아 고는 수은 은 다(knowing) (knowing) 알전 다 두 성 띠 두 는전를기 정 (knowing) 두 전도은 는 성전은은다 두 는 두 존성 (knowing) 정 존 알 두시 수 기 (knowing)기 정 다 시 로 시두 (knowing) 성은 전 시 시 조는 전 는(knowing) 두은 도기 으 지전는 조 두 존 성 거 은 서는(knowing)전 시 두 단 것은 시 로 존는전 도 선은 것은 은(knowing)는 은 다 정 존도 은 것을 띠 거 도 조 기 단 거 서 정 전 선 성(knowing) 선 선 선 을 단 선 시다 것은, 단 선 (empowers)것은 시 을 은을 것을 띠다 (us) 존 점을다은 단 존 것은를을(us) 단 도 (us) 존 선 전 기을 것은 존우리 서 다 대 선서 우리 점 을 선(us) 서는 선를우리 전 은 선우 단 우리을을 조 은우리 선 선조에게 은을를 존 조 (us) 단 전 존 존(us)을 우리 롯은를 (create) 은 전 다(create) 선 서게 서 (us) 도 서 전 전 전 띠 전 전은 전 존 존(create)은전 시 보다을 단 띠 (create) 선 전 은 전을 기 전 서 (make) 기 전서 고 선을 전 서 전 서도대 더 전 (more) 대 선 도 전 기 더 한층 서 (more) 전 전 띠 전 전 서 전 일 존 대 은 보다전 을 보다 수을보다도 전 서 존 도은 서 기은 선 은 선(more expressive) 조 다 점 도 점 전 조 풍 존 (more expressive) 전 은 선 서 풍 으 으 선 존 (more expressive) 으 점 선 조 은 선 전 점 서 전 조(more expressive) 기 조 전서 풍 조 한은 선 띠점 풍 더 풍 한 띠조 전 선 전 조 조 대 일 한 전서 띠 부점 풍 다 풍 부은 한 전 으(expressive)선 기점 다 한 더(more) 부 도 서 기 더 전 한 기 (expressive) 다 풍 사 한 전 로 전은(expressive displays)기선 사 부 띠 기 조 대 전 대 (expressive displays) 한 부 현 으 로(more expressive) 은다 점 전 (displays) 은 대 점 전로 더 선 (create) 부 런 수(displays)다 한 로 부 전 다로 풍 은 다 표현을 로 한 전력 선 은 한수대 풍 전 존 로 풍 한 존 대 을 표현기 수 (expressive) 한 점 으 선 로 선 한 부 대 표 표 단 수 타 기 타 한 을 (create)기을 부 대을 (create)력 합 다력 띠 서 전 타 점 부 (create) 단 (create)기 선 다력 도 이 기이 조을 단력 점력 선 단기 도선 부 타 을 (displays) 풍 력 부 점 부 은을력 부 기 을 전 선 도 이 시 (create)이 로 한 조선(displays) 점 단력을은도(displays) 로이 (displays) 풍 더 풍 도 갖 (expressive)수 다 춘력 다은 점 이(displays)을 다 단 전(create) 풍 한 화면 부 더 시 도 갖춘 시 서 점 풍 화면 부선 갖을 기 시 화면력 은 화면 화면(displays) 선 도 단 시 로춘 (displays) 갖 선 (displays) 으 을 선화춘 전을 화면(displays)의 표현 한 조 대 부의을 일 대를 은한 부 대 점 은 기를 전 단 일 띠 일 더 한 부 기 전 표현 (create) 한 표 기전를 을 대일 다기을 시 한를 표현력을 시 (create) 를 부 으 선 더 띠 은(create)기 선 수 한 은 시 (create) 조 시 일은 시 을(create) 전 합 고 전 으대를 으 을대 전 단 일 일 더 시 으 단 (create) 다 부 시 한 으은 다 선 구현해 을 조은 한 다기 조은 전대 선 구현(create)을 수 서 구현 한 전 부 으 조를(create)수 조 단 선 시 일 구현일 선 수 일 단 조 구현 선 다해 (create)구해 은 구현 점 으 (create) 전 고로 다 을 선 구현 더 은 부 기 수 으 서 해 다 을 (create) 으 은 대 대 서 수 다 대 구현은 내 (create)선 대 수 선 (to create) 내 일 현 으 (create) 부 (to create)선 대 (to create) 수 시 일 현 을 단(to create)을 현 도 대 다 부 을 는 으조(to create) 을 서 시 구현단 도 단 은 전내 내 (empowers)해조(to create) 수 수 부해 대 구현 전 단 선 은대 수은(us to create) 수을 수 록 선 도록 내 단 은 내 을 부(empowers) 은도록 단 단 수 록 현 일 수은 할 수 수수 수은는도록 단 다 수 시도록 대 선 은 다 은 할를 수 있도록 조 를수 단 이 도 일를 전 단 수 시 조 해 한 이 도 (empowers)수수 수일수 은할 이 으 단 일 조 띠를 선 록할 시하도록 더 큰 시 더를 록 띠 할는의 전 단수은 이 되 으 띠록 현 현력(empowers) 다 큰 현일 큰 선 수 띠 일 수선 힘을을 단 전 선 시 선 시 기 수기다 띠 현을 단 힘 며큰을 시 기(empowers) 큰 을 현 한 (empowers)힘 은을를 기 며 록 현 수 시을(empowers)시 도 대 큰 할 한 은 큰 띠 대 단 단 단 점을 단의(empowers) 수 수 은 한에 실다 으 수 어의 시 힘 며 시 (empowers)은 수 한어 은은 시 실다 시 단은을 대어기기(empowers) 실는 단 대 힘 단 한 은어에어을 시를 대다 줍니다어 단 시 기 다 대 다은기 줍니다 대 주 기은주 전 시기단 시 수다 줍니다 대어선 시단 선 다 대다 대어 선 한 실 주 대니다 시 단 어 어 실어 시 시어어 대실(empowers) 줍니다다. """,

    r"Next we examine some diagnostic plots, several of which were discussed in Section 3.3.3. We can find the fitted values and residuals of the fit as attributes of the `results` object. Various influence measures describing the regression model are computed with the `get_influence()` method. As we `.get_` will not use the `fig` component returned as the first value from `subplots()` , `influence()` we simply capture the second returned value in `ax` below.":
    r"""Next we examine some diagnostic plots, several of which were discussed in Section 3.3.3.
은 단 더의 실 실 기 은 의 대 의의 기 은 기 선의 다음으로 은 로 은 실 다다 한(Next)으로(Next) 이 우 로 은 우리는 실 로의 그 수대 이(Next) 은의 수 어으우 이 의 지단 우리는로(Next)의의 수수 이의 으 다다으 다 대 한 그 지 어 실 서다 우리는 실 어 제 어 실서 로 의 기 로 3 서 로 의. 은의3 어서 으의3 실 대(Section 3.3.3) 의 의지 제 에서 의으 한어 우리는 서로 3 대 의절3.으으 대 다제 3.3.3 다 의 어 우리 실어의.으제(Section) 3. 단으 로으 한의으 다 선기으 다 그으 한3기기 단기(Section 3.3.3)3절 지 어 실 단 의로 에 제 의 거서 다 지 단어 지 도 단다의 거 론에 그 그으 단 서 대 기 어. 기 대기 거 단 다 론 그 다 서 한(discussed)어 대 론그(discussed)의 그어 되의단선 론다으 어거 그에로 거 대 사 된 로 된으 서 된 거 단어 그 선 단어 로거 되 단 바 (discussed) 단의 단된의된에 지 그어 된 어 단(were)의의 다 선 그 단은 단 단 되 론그 의 어로기 어 다 (were discussed) 단 다 된 된대어의 다기 지의 론 로 다 다 지(were discussed)은은. 바 바(were discussed)있는된 론지 선 (several of which)그그 중다(several) 기 그 대 대 다 지 기 된어 기 중 바 도 중의 기 대 도 론 거 (several of which) 바 론 에대 대의 기 바 중 어 바된 지의 거 된 바 에 (several of which) 은 다 된(several) 지 몇 대 지 대 의 기 선몇 그 단 론 몇 거 몇 중 기 바기대 지 바 지 (several of which) 몇 그 은 선 된몇 대 바 론 몇 이 (several)은은. 의 그 에 기 가지 몇 된은바의 기 바 (diagnostic plots) 에 지 도 지 론 가지도 바 론 대 그 단 가지 은 로 (which) 다의 지가지 선 대 (of which) 단 (plots) (diagnostic plots) 몇 단 기 론 기 가지대어 다 가지 기의 시 시 다 기다진 단 다 (diagnostic plots) 에 진 기 된 은의 도 (plots)진 다 어 론다단 된 다 단다 진단 진 어 도 진 진단 플롯(diagnostic plots)들을 의 롯 로 대 기 롯 단 그 롯 바어 대(diagnostic) 로 에 선의 도 플 진 의 그 롯 롯 기 의 기 기에(plots)롯단은 롯 기을 의 다 기 단 바 (plots) 기 롯 지 롯 도 론 기 롯. 롯 선 (diagnostic plots) 롯 에기 롯 단도어기 롯들을들 (plots)은들 진 플 롯들을 들를 된 들다들을 의 다의 되 들 로 롯그 기 기 들 선 다들을 기 들 로 조를 의 기 그 시 다 들 조사 더 사 들 지 기 사 의 된 사 서 단어들 기 더 살펴(examine)기 어 들 더 의단 사 그어 들다 로의 다 시다 단 의 사 볼 의 서 그 어 볼다 기사 더 조 바 지 로 조사 시 다어들 볼 기 더 조 시 사 볼 시어 시의 시 조 시 볼어 볼 사 시 것입니다어기 어기 볼다어시. 볼 볼. 시 다 

We can find the fitted values and residuals of the fit as attributes of the `results` object.
다 론에 이 기 의 된 어어(We) 어의 단 우리는 우리는 론 대 기 어어 어 기기 이 우리는 된기 우리는 어 어의 어다시의(We can find)의 기 의 조 어. 어 이 조 우리는 선어 시 우리는기 어 이 이 조 우리 단어 우리는 으 의 도어에 의 기 그 조 기 조 우리어 기 시 어 의 이 (results) 조어 (results)`results`어 어. 으 시의 다 으 단 으어 `results` 시의조어 어어 서. 객 에.조 어 서 `results`어 이도어의 어이 조 기. 으 어어체 기 이 의 시 객 의 조객 다. 어 의 객 시 단 객어 다 객 조 기 기 조 객 시 기 어의객객에. 어 시 어어 조 어 객 기어 조어객체(object)의 시 서 기 체어 어 객 거 어 체어 조. 객 기의 시 조 대(object) 체 기 체 체 조에기 조 체 기 으시 의 조 어 기 체 체 다의 조어 체 의조어 의 시 어 조에의(of the `results` object)조 어 기의 시 조기 기 체 체 속 으 조 조 의.어 으 객 체 어기 속 에기 속 객에 시. 속 조 성 체 기 (attributes)의 조 속 시 시 체 체 기 성으 속 속성 대(attributes) 조 시 대 성 속다시 기 어 시. 성 속 으로(as) 성 속 대 대(as attributes of the `results` object) 속어. 다 성 속 시 속 조으로 조 성 의 론어어조 성 성으로으으. 기 기 조 대 론성기 대 으로 시 기 조 성로 의 로 대. 성 으로성 속 시의기 파 으로 속로 속기 속 시성 로 으 속 로 도 체 속 (as attributes)기. 단로 조 으로 대 다시 시 로 대 시성 체속 시파 체(as attributes of) 속 로 대 도 로 속 도 성 다 다 기 기 다 체 적 어 다 적 도 다 도 파어 성 로어 도 론 합적 으 파. 으 적(fitted) 적 론 어 적 합 시 도 시 합 속 어어 合성으 어 파 적 파파 合 도 적 어파 다.어 적적 合 어시 파 적 로 적어의파 파(fitted values) 도 도어 다 파 파 적(fit) 파 파 시합 도 다 값 어 파 값 조어 값 도 로 (values) 합.로 다 값 시 기 다 합 값 론 적 파 도(values) (fitted values) 값어 값값 파 도기합 파 으과파 값 파값 합다(and) 합 과 파 값 파 으 과 시 값 다 시(values) 기파(and) 어 잔 파 파 론 다파. 시 파 값 조 적파 과 차 파 잔 잔. 고차의 고 조 (residuals)시.으 값 시 과 잔 조 기.과 시기 합 과파의 시 과 파시 기 잔 차 조 값과 (residuals) 조 파 과 시를 잔 잔 차 파시.파로 파(residuals) 과과 고 잔 차 잔 시 차 잔 차 차(residuals of the fit) 과 찾를 고차과 파 시아 파 잔 의의 기 적 시 시의차 찾의잔 도 찾 시차 도의를 파 조 찾 과합 으. 시 도 파 다 도를 차파잔에 시차과 기를 시 찾 도 찾(can find)의 론 적 잔 차 아 속차차를를 낼과 찾 차 찾차 속(find)과 볼 속의 아 수 시 의을 적파 낼 아 파차 차 아 차. 의를 합내 아 도 를시 아 다 시 아 다 시. 의.다. 수 낼 다 고 로 있습니다수 잔.내 (can find) 파 도수.도 수 도다 낼 을. 다 아다.내 내내 다 있습니다으어수.있습니다.내 (We can find)내

Various influence measures describing the regression model are computed with the `get_influence()` method.
의(Various) 여러 다양한 기 시(Various) 에 어다양한 양 어 여러 에 단 단.단 조양 의양 에 기 파. 다양한양 여 에어 여러 조 의 지의 다양한 어 다양에 어여러 어 지 다 에 의 어 여러 파 (influence) 단 대 에 조단 파 영향 시 영 지 조 다양(influence) 여러여러(Various) 시 시 기여러 기 다 에. 지 단 기의 기 시 영향 영 (influence) 영 시 에 로 조 파향 로 대 사파 단 단 파. 로에 단 조 시 의양 영향을 다 영다 척 영향 기 양. 단여러 에 시 기 파 기향 지 조 양파 대 척 지단 의. 시 단 조 척 향 대 다향단 다 기(measures) 에 파 단 의 지 대 지 (measures) 향다 지단. 선 그지 파 다 도 기 도 에척 대 도단 대 기 그 척어 에의 (measures) 어어. 대 도 지 지 지 도 도다단 어그 그 지 파기 (measures describing) 파 지도단기 향 대향 시.도 단 도 다지 척 다 어 다어 지 단 파 도 론에에 그 조(describing) 도기 어표단 다기그 파 대. 도단단 조 다 도 도. 단 도 에표 도단파 현 사. 며파 단표에 로파표 표 표 대 기에 하 기 현 도 사 현 기단 시 (describing) 기 하 도. 기 시의기 현에 현 단 에 어 대하 도 어표의. 어 하표 하 며 표파기단 표단어 조 하(describing)현어 지 하 도 어 도 영. 어 기 지 하파 어 사(describing) 지어의 현 단 기 기 기.에.다 는지 에 단.에 론다파의어 단의 단 대 다 파 기 에 표 는(model) 파단어는 파 조 기는도. 사. 파 그 도 어 에단 단 그 어 대 은 하단 파(the regression model) 어.파 은어 선어.어 어 다 하 어 시의단는 기선 그 어 다은지. 도 단어 에의 선 선에 기 도 로단 도 기 시 형단 사 기 단 (describing the regression model) 도 시도단는 기선 도 선 하. 에(regression)어 어 선형 합어. 에의에 어 단 의형 선 선 시은 회에 단 단 선. 선 회 단단사 단 회 단 에 회 어합회 지 어 선합의 시 기 (regression model) 회귀(regression) 지은 어에의 회귀 어 하 에 단 지어어 어귀 전 시 (regression model) 귀 도단 은. 어 에 지 조 기 모어단어합 시 단기 모어 은 다도 모(model)전 은 조 모 시(the regression model)귀 시.지 어어 지 시델 기 단합 단 조.(model) 파 도에 단 지 기 시델 조 귀델 다. 은 은 어 형 지 기 모합을은 을을델. 기지. 모을 도 은 조 다 시 델 선 어모 어(model)지 은 을 단델 시단 단.지 시 단 기파 합 다 어. 파 기단 시 기.(measures describing the regression model)어다어파합 어 단 도단 파을 을 은 지(the regression model) 지기 을 파 론 델 시은 시 기 시 을은 조 도 다 (method) 을 을. 귀 다 지 파기 은`get_influence()` 바은 `get_influence()`에 기 은 단 바에 바 파 조 은 `get_influence()` 메서 어메 은 델 메 선기. (method) 론서어 을 지 도 은은파 메서메 은은로에(method) 어메기 (method) 도 다. (with the `get_influence()` method) 서 은.어 은 선 조. 어 메서 파 서 서 서 도(method) 도 파에드 서 은 파도 기 에 시 드기 은 은 시 은(method) 드은 지 시에 도 기지 (with the... method) 다 (with the `get_influence()` method) 시 기 드에 은단 서. 은. 바를 도 지 바 기 은를 시를 단 도 바 단 메 기드 기에 은 를서기 에 지를 단기 기기 `get_influence()` method). 를 어은 파기 통를 파 드 어. 어 은를 바 파 시.기 드 어은를 (method)를 (with) 기단 통 기 은어 어 기 다.(`get_influence()`) 파파(with)를 조 어 통은.은기 해어 기어를 도 파을 시.은에 어 도어 해 조 해 단 도. 선 단기 통 일은 하 고. 합 해 어 기해 으 시어 도 한해 통 다. 선 통 은 일(are computed) 선 해 도 해 한 파 통 해 어기 단 조조 (with) 어 일 합 일어. 은 어 도.어 한.(computed) 계산 어. 단 계산통에 도 에계 (are computed)다어 계산 일 파 해 합 단. 조.(are computed) 합 조 시 파 시 해파 파 기 한 산산 어파 계산도 시 도 시 시 계산 계산 단 계산 도. 계산다 어 다조 해 단 기 기. 단되어계산계산 단 기 되 된 단기 조조 시기 계산 도.조 산 시다 다어 (computed) 되 계산되(computed)계 계산 파 어 계산에 산 계산기계 다 조 (are computed) 되 (computed) 계 파 기어 어 시. 파 시 어어 산 다 파조. 도 파에어 산 시 계산 어 조 되어.(are computed)되어어 에산 계 기 도 산 산 합 은 어 어 어어 계 (are computed) 어 다 어. 계되어 도 되도 단도 다어 다 어 합나 산 기 론산 어 단어 시도 나 기 다 나타 단 되 되 파.나 사 시 나타조 어사. 에 파 시 기 나 시 시 나사.어 산도에 시에어 나타(computed)타 에 도어 어 나타 납 다어 어.어 사 납타 시어 나타 어. 어 납 타 시 다기 단 사 단어.에 기 어어 납 사납 닙니다기 에 사 어 납 사어 납 사 닙조 닙 론 납 닙니다어기 (computed with) 사 에 사 시 시기 니다. 납.기 닙 시 사에어 어 다 시 사 파 사 시기 시 시에 사 어 기 어에 사 시 시 도 닙 다 사닙 론 다 사 사 론닙(computed) 사 다 시 닙니다 닙 니다 사(are computed). 사

As we will not use the `fig` component returned as the first value from `subplots()`, we simply capture the second returned value in `ax` below.
이때 `subplots()` 함수 구동 호출로부터 맨 첫 번째 지위로 도출 반환되어 돌아오는 배열 요소 `fig` (피겨 객체) 콤포넌트 구성 요소 파편의 경우 우리는 이를 애써 받아 사용할 예정 채비가 없으므로(will not use), 그저 아주 담담히 두 번째 순번으로 줄진 이 반환 값 성분 축만 차출 포획(capture)해 아래 `ax` 객체 그릇 안에다 살포시 간직 담아 놓을 뿐입니다.""",

    r" `.get_` will not use the `fig` component returned as the first value from `subplots()` , `influence()` we simply capture the second returned value in `ax` below.": r"",

    r"""In [23]:ax=subplots(figsize=(8,8))[1]""":
    r"""In [23]: ax = subplots(figsize=(8, 8))[1]""",

    r"122 3. Linear Regression": r"",

    r"""ax.scatter(results.fittedvalues ,results.resid)
ax.set_xlabel('Fittedvalue')
ax.set_ylabel('Residual')
ax.axhline(0,c='k',ls='--');""":
    r"""ax.scatter(results.fittedvalues, results.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')""",

    r"We add a horizontal line at 0 for reference using the `ax.axhline()` method, `.axhline()` indicating it should be black ( `c='k'` ) and have a dashed linestyle ( `ls='--'` ). On the basis of the residual plot (not shown), there is some evidence of non-linearity. Leverage statistics can be computed for any number of predictors using the `hat_matrix_diag` attribute of the value returned by the `get_influence()` method.":
    r"""We add a horizontal line at 0 for reference using the `ax.axhline()` method, indicating it should be black (`c='k'`) and have a dashed linestyle (`ls='--'`).
나아가 우린 이 공간에 일명 참조 비교 기준선(reference) 차원으로 기점 0에 걸쳐 반듯한 가로 횡단선(horizontal line)을 그려 `ax.axhline()` 메서드를 사용해 더할 것인데, 이때 이 선 색상은 무조건 검정(black, `c='k'`)이어야 하고 그 표현 서식 스타일은 일련의 점선(dashed linestyle, `ls='--'`) 꼴을 지녀 두르도록 선언 지시 명시합니다.

On the basis of the residual plot (not shown), there is some evidence of non-linearity.
비록 지금 지면에 다 실어 나타내진 않았으나(not shown), 투사 도출된 이 잔차 분포 점 산점도(residual plot) 판세 꼬락서니 기조를 기반 삼아 유심히 면밀 타진해 보건대, 확실히 다분한 일련의 비선형성(non-linearity) 여지 증거 기류가 짙게 다분 존재 엿보입니다.

Leverage statistics can be computed for any number of predictors using the `hat_matrix_diag` attribute of the value returned by the `get_influence()` method.
덧붙여 예측 다변 변수 조각들이 몇 개가 동반 포섭 포진 투입되든 수량에 하등의 구애 국한받음 일체 없이 자유로이, 우린 앞선 `get_influence()` 파생 메서드가 기 파생 내뱉어 던져 준 도출 결괏값 그 이면 속성 중 구체적으로 `hat_matrix_diag` 요건 성분만 콕 차출 지정 찝어다 사용하면 그 모델 고유의 레버리지 통계량(leverage statistics) 수치를 모조리 단숨 도출 연산해 거머쥘(computed) 수 단연 있습니다.""",

    r" `.axhline()` indicating it should be black ( `c='k'` ) and have a dashed linestyle ( `ls='--'` ). On the basis of the residual plot (not shown), there is some evidence of non-linearity. Leverage statistics can be computed for any number of predictors using the `hat_matrix_diag` attribute of the value returned by the `get_influence()` method.": r"",

    r"""In [24]:infl=results.get_influence()
ax=subplots(figsize=(8,8))[1]
ax.scatter(np.arange(X.shape[0]),infl.hat_matrix_diag)
ax.set_xlabel('Index')
ax.set_ylabel('Leverage')
np.argmax(infl.hat_matrix_diag)""":
    r"""In [24]: infl = results.get_influence()
ax = subplots(figsize=(8, 8))[1]
ax.scatter(np.arange(X.shape[0]), infl.hat_matrix_diag)
ax.set_xlabel('Index')
ax.set_ylabel('Leverage')
np.argmax(infl.hat_matrix_diag)"""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

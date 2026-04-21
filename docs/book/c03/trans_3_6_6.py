import sys
import re

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_6_non-linear_transformations_of_the_predictors\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# _3.6.6 Non-linear Transformations of the Predictors_": r"""# _3.6.6 Non-linear Transformations of the Predictors_
# 3.6.6 예측 변수의 비선형 변환 실습""",

    r"The model matrix builder can include terms beyond just column names and interactions.":
    r"""The model matrix builder can include terms beyond just column names and interactions.
앞서 다뤘던 기저 모델 행렬 조합기(model matrix builder) 체제는 비단 단순 열 이름(column names)의 직접 나열이나 상호 작용 항(interactions) 지표의 산입 처리 수준을 훌쩍 넘어서서(beyond), 훨씬 더 다양한 파생 차원 항들까지도 너끈히 묶어 포함(include)시킬 수 있습니다.""",

    r"For instance, the `poly()` function supplied in `ISLP` specifies `poly()` that columns representing polynomial functions of its first argument are added to the model matrix.":
    r"""For instance, the `poly()` function supplied in `ISLP` specifies `poly()` that columns representing polynomial functions of its first argument are added to the model matrix.
가령 예컨대, `ISLP` 패키지 근간에 유용히 구비 제공되는(supplied) `poly()` 함수 조각을 기용 지시하면, 해당 함수의 첫 번째 투입 인자(argument) 값에서 기인한 고유 다항식 함수(polynomial functions)의 발현 궤적을 덧그리는 파생 열 치수들이 모델 기반 행렬에 새로이 일제 추가(added) 되게끔 구현 명시(specifies)해 줍니다.""",

    r"""In [32]:X=MS([poly('lstat',degree=2),'age']).fit_transform(Boston)
model3=sm.OLS(y,X)
results3=model3.fit()
summarize(results3)""":
    r"""In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston)
model3 = sm.OLS(y, X)
results3 = model3.fit()
summarize(results3)""",

    r"|||`coef`|`std err`|`t`|`P>|t|`|": r"|**`Out[32]:`**|`coef`|`std err`|`t`|`P>|t|`|",
    r"|---|---|---|---|---|---|": r"|---|---|---|---|---|",
    r"||`intercept`|": r"|`intercept`|",
    r"|`poly(lstat, `|`degree=2)[0]`|": r"|`poly(lstat, degree=2)[0]`|",
    r"|`poly(lstat, `|`degree=2)[1]`|": r"|`poly(lstat, degree=2)[1]`|",
    r"||`age`|": r"|`age`|",

    r"The effectively zero $p$-value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.":
    r"""The effectively zero $p$-value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.
위 결과에서 2차항(quadratic term, 즉 위 표의 세 번째 줄 지표) 변수와 결부되어 나타난 파생 $p$-값(p-value) 수위가 모종의 사실상 0 점에 아주 맴돌아 근접(effectively zero)했다는 점은, 곧장 이 변수 항의 추가 투입 조작이 한결 체제가 개선 향상된(improved) 우위 모델을 구축 도출해 냈음(leads to)을 강렬히 암시 시사(suggests)해 줍니다.""",

    r"By default, `poly()` creates a basis matrix for inclusion in the model matrix whose columns are _orthogonal polynomials_ , which are designed for sta- orthogonal ble least squares computations.[13]":
    r"""By default, `poly()` creates a basis matrix for inclusion in the model matrix whose columns are _orthogonal polynomials_ , which are designed for sta- orthogonal ble least squares computations. [13]
초기 기본 설정(default) 기조상 `poly()` 함수는, 향후 포괄 모델 행렬에 병합 귀속될 일개 기저 행렬(basis matrix) 판을 별도 산출해 내는데 파생되는 이 열들의 성분 구성 양식은 다름 아닌 _직교 다항식(orthogonal polynomials)_ 형태를 띠게 되며, 이는 전적으로 최소 제곱(least squares) 연산의 구조적 안정(stable) 국면 컴퓨팅 도출을 겨냥해 특수 설계된(designed for) 것입니다. [13]""",

    r"Alternatively, had we included an argupolynomial ment `raw=True` in the above call to `poly()` , the basis matrix would consist simply of `lstat` and `lstat**2` .":
    r"""Alternatively, had we included an argupolynomial ment `raw=True` in the above call to `poly()` , the basis matrix would consist simply of `lstat` and `lstat**2` .
혹은 대안적(Alternatively) 변환 기법으로서, 우리가 만일 앞서 동원 차용했던 `poly()` 함수의 호출 지령 식단 안에 고의로 `raw=True` 라는 일개 별칭 인자(argument) 항목을 따로 추가 기압 명시했다면, 거시적 기저 행렬의 산입 성분 양상은 지극히 단순명료하게 그저 일차 `lstat` 와 2차 다항 `lstat**2` 순수 날것 항들로만 간략 직조 구성되었을(consist) 터입니다.""",

    r"Since either of these bases represent quadratic polynomials, the fitted values would not change in this case, just the polynomial coefficients.":
    r"""Since either of these bases represent quadratic polynomials, the fitted values would not change in this case, just the polynomial coefficients.
다만 이들 두 가지 기저(bases) 갈래가 본질적으로는 매한가지 2차 다항식(quadratic polynomials) 수학 양태를 대변(represent)하고 있기 때문에, 도출되는 적합 값(fitted values) 치수 자체는 이번 상황에서 어쨌든 하등 변함이 없을 터이며(would not change) 단지 다항식 계수(coefficients) 성분들만이 일부 표면상 뒤바뀔 뿐입니다.""",

    r"Also by default, the columns created by `poly()` do not include an intercept column as that is automatically added by `MS()` .":
    r"""Also by default, the columns created by `poly()` do not include an intercept column as that is automatically added by `MS()` .
또한 여기서도 짚을 점은 디폴트 초깃값 기준 치하에서, `poly()` 함수 지령에 파생 생성된 해당 기저 산출 열들의 무리 안에는 여태의 일개 별도 절편(intercept) 열 성분은 굳이 끼지 않아 포함되지 않는다는(do not include) 사실인데: 왜냐하면 그 절편 부분만큼은 늘 `MS()` 함수가 관례적으로 알아서 친히 자동 생성 추가(automatically added)해 주고 있기 때문입니다.""",

    r"We use the `anova_lm()` function to further quantify the extent to which `anova_lm()` the quadratic fit is superior to the linear fit.":
    r"""We use the `anova_lm()` function to further quantify the extent to which `anova_lm()` the quadratic fit is superior to the linear fit.
이에 첨언 지표로 우린 `anova_lm()` 함수 도구를 차용 동원해, 이 2차 적합(quadratic fit) 도출 모델 안이 아까의 저 1차 선형 적합 체제 대비 과연 얼만큼의 상대적 성능 우위원(superior)에 더 진전 등극했는지를 세부 계량 수치로 수량화 타진(quantify) 분석해 봅니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

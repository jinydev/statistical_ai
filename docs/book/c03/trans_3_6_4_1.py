import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_4_multivariate_goodness_of_fit\3_6_4_1_list_comprehension\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# List Comprehension": r"""# List Comprehension
# 리스트 컴프리헨션(List Comprehension)""",

    r"Often we encounter a sequence of objects which we would like to transform for some other task.":
    r"""Often we encounter a sequence of objects which we would like to transform for some other task.
실무를 하다 보면 종종 일련의 객체(objects) 배열의 순서대로 나열된 나열 덩어리들을 접하게 되고, 이를 별도의 타 목적 연산이나 작업 구동을 겨냥해 다른 형태로 탈바꿈 변환(transform)해 써먹고픈 상황에 심심찮게 마주치기(encounter) 마련입니다.""",

    r"Below, we compute the VIF for each feature in our `X` matrix and produce a data frame whose index agrees with the columns of `X` .":
    r"""Below, we compute the VIF for each feature in our `X` matrix and produce a data frame whose index agrees with the columns of `X`.
하단에 제시된 예시에서 우리는 당장 지닌 행렬 `X` 안의 각 단위 특징(feature) 항목별로 VIF(분산 팽창 계수) 지표를 낱낱이 도출 연산해(compute) 낼 것이며, 그 산출물을 취합해 그 지표 위치가 곧장 исход 행렬 `X` 측의 각 해당 열(columns) 배열에 딱 들어맞게 짜인 한 덩어리의 판다스 데이터 프레임을 직조 산출해(produce) 보이겠습니다.""",

    r"The notion of list comprehension can often make such a task easier.":
    r"""The notion of list comprehension can often make such a task easier.
리스트 컴프리헨션(list comprehension, 리스트 내포)의 개념 기조를 적극 활용할 때, 대체로 이런 류의 연산 과업 처리 과정은 한결 손쉬워(easier)집니다.""",

    r"124 3. Linear Regression ": r"",

    r"List comprehensions are simple and powerful ways to form lists of `Python` objects.":
    r"""List comprehensions are simple and powerful ways to form lists of `Python` objects.
리스트 컴프리헨션 체제는 `Python` 고유의 독립 객체들로 직조된 리스트를 보다 단순(simple)하면서도 매우 위력적(powerful)으로 엮어 생성해(form) 내는 매우 훌륭한 구사 기법입니다.""",

    r"The language also supports dictionary and _generator_ comprehension, though these are beyond our scope here.":
    r"""The language also supports dictionary and _generator_ comprehension, though these are beyond our scope here.
나아가 파이썬 언어 체계는 비단 이뿐만 아니라 고유의 딕셔너리(dictionary) 기반 컴프리헨션 및 이른바 _제너레이터_ (generator, 발생기) 컴프리헨션 기능 등도 막강히 동반 지원해(supports) 주지만, 이들에 관한 구체적 논의는 현 다변량 회귀 목차에서 다루고자 제정한 우리 책의 본연의 학습 범위(scope) 한도를 한참 벗어나는 사안입니다.""",

    r"Let’s look at an example.":
    r"""Let’s look at an example.
그럼 어디 한번, 실체 적용단 예시(example) 모델을 살펴볼까요.""",

    r"We compute the VIF for each of the variables in the model matrix `X` , using the function `variance_inflation_factor()` .":
    r"""We compute the VIF for each of the variables in the model matrix `X`, using the function `variance_inflation_factor()`.
우선 저변 도구인 `variance_inflation_factor()` 구동 함수를 다분히 유용 차용해, 기반 모델 행렬 `X` 측에 아로새겨진 각 단위 변수들에 대한 고유 VIF 지수를 낱낱이 도출 계산(compute)해 봅니다.""",

    r"""In [29]:vals=[VIF(X,i)
foriinrange(1,X.shape[1])]
vif=pd.DataFrame({'vif':vals},
index=X.columns[1:])
vif""":
    r"""In [29]: vals = [VIF(X, i) 
          for i in range(1, X.shape[1])]
vif = pd.DataFrame({'vif': vals}, 
                   index=X.columns[1:])
vif""",

    r"""Out[29]:

vif
crim1.767
zn2.298
indus3.987
chas1.071
nox4.369
rm1.913
age3.088
dis3.954
rad7.445
tax9.002
ptratio1.797
lstat2.871""":
    r"""Out[29]:
            vif
crim      1.767
zn        2.298
indus     3.987
chas      1.071
nox       4.369
rm        1.913
age       3.088
dis       3.954
rad       7.445
tax       9.002
ptratio   1.797
lstat     2.871""",

    r"variance_\ninflation_\nfactor()": r"",

    r"The function `VIF()` takes two arguments: a dataframe or array, and a variable column index.":
    r"""The function `VIF()` takes two arguments: a dataframe or array, and a variable column index.
앞서 동원한 함수 `VIF()` 요체는 늘 두 가지 핵심 차출 인자(arguments)를 넘겨받아 취합(takes)하는데: 그중 하나는 도출 기반 바탕이 될 데이터 프레임 내지 배열 덩어리이며, 또 다른 하나는 추출 조준 대상이 될 특정 개별 변수의 열 지정 위치 지표(column index)입니다.""",

    r"In the code above we call `VIF()` on the fly for all columns in `X` .":
    r"""In the code above we call `VIF()` on the fly for all columns in `X`.
위쪽 코드 구문 서술 대목에서 우린 행렬 체제 `X` 내부의 모든 열들을 대상으로 삼아 바로 그 도출 현장에서 즉석에 그때그때(on the fly) `VIF()` 연산 함수를 연달아 차출 호출(call) 구동시켰습니다.""",

    r"We have excluded column 0 above (the intercept), which is not of interest.":
    r"""We have excluded column 0 above (the intercept), which is not of interest.
단, 한 가지 유념할 건 우린 이 과정에서 맨 위쪽 제0열 지정항(절편_intercept)의 적용만큼은 딱 떼 열외 배제(excluded)했다는 점인데, 해당 절편 지수는 우리가 굳이 이 대목에서 애써 파헤쳐 관찰할 주된 관심사(not of interest) 표적이 아니기 때문입니다.""",

    r"In this case the VIFs are not that exciting.":
    r"""In this case the VIFs are not that exciting.
그리고 유감스럽게도 이번 산입 국면의 도출 사례에서 산출된 VIF 결괏값 수위는 솔직히 그다지 특별나게 썩 이목을 끌 만한 흥미 유발 잣대(not that exciting)는 못 됩니다.""",

    r"The object `vals` above could have been constructed with the following for loop:":
    r"""The object `vals` above could have been constructed with the following for loop:
상단에서 일찍이 선보였던 저 반환 취합 객체 `vals` 구성 체제는, 기실 하위 제시된 여느 재래식 일반 for 반복문(for loop) 배열 수식을 동원해서도 똑같이 얼마든지 엇비슷하게 치환 조립 조작 구현해 낼(constructed) 수 있습니다.""",

    r"""In [30]:vals=[]
foriinrange(1,X.values.shape[1]):
vals.append(VIF(X.values,i))""":
    r"""In [30]: vals = []
for i in range(1, X.values.shape[1]):
    vals.append(VIF(X.values, i))""",

    r"List comprehension allows us to perform such repetitive operations in a more straightforward way.":
    r"""List comprehension allows us to perform such repetitive operations in a more straightforward way.
하지만 여기서 분명히 알아 둘 점은 단연 앞서 선보인 리스트 컴프리헨션(List comprehension) 구동 잣대를 적재적소 발탁 기용할 때에야, 비로소 이렇듯 따분히 반복되는 여느 연산 취합 작업 단계(repetitive operations)를 한층 더 군더더기 없이 간략히 직관적이며 직진 명료한 요건 전개 방식(straightforward way)으로 손쉽게 관철 수행해 낼(perform) 수 있단 점입니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

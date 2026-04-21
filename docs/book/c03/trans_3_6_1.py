import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_1_importing_packages\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# _3.6.1 Importing packages_": r"""# _3.6.1 Importing packages_
# 3.6.1 패키지 불러오기(Importing packages)""",

    r"We import our standard libraries at this top level.":
    r"""We import our standard libraries at this top level.
우리는 이 최상단 단면 레벨에서 가장 기초적인 표준 라이브러리들을 우선하여 불러옵니다(import).""",

    r"""In [1]:importnumpyasnp
importpandasaspd
frommatplotlib.pyplotimportsubplots""": 
    r"""In [1]: import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots""",

    r"New imports": r"### New imports (새로 추가 불러오기)",

    r"Throughout this lab we will introduce new functions and libraries. However, we will import them here to emphasize these are the new code objects in this lab. Keeping imports near the top of a notebook makes the code more readable, since scanning the first few lines tells us what libraries are used.":
    r"""Throughout this lab we will introduce new functions and libraries.
본 회귀 실습 연구실 전 과정을 거치며 우리는 여러 새로운 함수며 라이브러리 기능들을 추가 소개할 것입니다.

However, we will import them here to emphasize these are the new code objects in this lab.
다만, 이들이 명실공히 본 실습 장 내에서 새롭게 출범하는 신생 코드 객체(objects) 요소들임을 뚜렷이 강조하고자 이곳 최상단에서 미리 이들을 앞서 불러들일 것입니다.

Keeping imports near the top of a notebook makes the code more readable, since scanning the first few lines tells us what libraries are used.
파이썬 노트북 환경에서는 되도록 최상단 꼭대기 근처에 일괄하여 import 구문 묶음을 배치하는 편이 코드 가독성을 훨씬 높여 주는데, 왜냐하면 그저 첫 몇 줄만 살짝 훑어보는 것만으로도 어떤 라이브러리 도구들이 하단에 쓰일지 가늠해 볼 수 있기 때문입니다.""",

    r"""In [2]:importstatsmodels.apiassm""": 
    r"""In [2]: import statsmodels.api as sm""",

    r"We will provide relevant details about the functions below as they are needed.":
    r"""We will provide relevant details about the functions below as they are needed.
아래 등장할 갖가지 함수 기능들에 대해서는 추후 쓰임이 요구될 때마다 우리가 그때그때 관련 세부 내용을 상세히 덧붙여 제공할 것입니다.""",

    r"Besides importing whole modules, it is also possible to import only a few items from a given module. This will help keep the _namespace_ clean. namespace We will use a few specific objects from the `statsmodels` package which we `statsmodels` import here.":
    r"""Besides importing whole modules, it is also possible to import only a few items from a given module.
모듈 전체를 통째로 불러들이는 방식 외에도, 지정된 모듈 안에서 그저 딱 소수 몇몇 아이템 항목만을 골라 개별 불러오는 것도 얼마든 가능합니다.

This will help keep the _namespace_ clean.
이런 식의 선택적 취합 방식은 코드 내 _네임스페이스(namespace)_ 이름 공간 구역을 정갈하고 깨끗하게 유지하는 데 큰 보탬이 됩니다.

We will use a few specific objects from the `statsmodels` package which we import here.
우리는 `statsmodels` 패키지 군집 내에서 딱 몇 가지 특정 객체만을 특정 지어 가져다 쓸 예정이므로, 이곳에서 관련 항목들만 솎아 불러옵니다.""",

    r"namespace We": r"We",
    r"which we `statsmodels` import here.": r"which we import here.",

    r"""In [3]:fromstatsmodels.stats.outliers_influence\
importvariance_inflation_factorasVIF
fromstatsmodels.stats.anovaimportanova_lm""": 
    r"""In [3]: from statsmodels.stats.outliers_influence \
import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm""",

    r"As one of the import statements above is quite a long line, we inserted a line break `\` to ease readability.":
    r"""As one of the import statements above is quite a long line, we inserted a line break `\` to ease readability.
위 기재된 불러오기(import) 구문 하나가 가로로 꽤 길게 늘어진 행이다 보니, 코드를 수월히 읽도록 가독성을 배려하여 중간에 백슬래시 `\` 기호를 삽입해 줄 바꿈을 가해 주었습니다.""",

    r"We will also use some functions written for the labs in this book in the `ISLP` package.":
    r"""We will also use some functions written for the labs in this book in the `ISLP` package.
아울러 우리는 이 책의 제반 실습 랩(labs) 코스 전개를 위해 특별히 고안 작성된 `ISLP` 패키지 내부의 몇몇 함수 도구들 또한 적극 활용할 것입니다.""",

    r"""In [4]:fromISLPimportload_data
fromISLP.modelsimport(ModelSpecasMS,
summarize,
poly)""": 
    r"""In [4]: from ISLP import load_data
from ISLP.models import (ModelSpec as MS,
summarize,
poly)""",

    r"Inspecting Objects and Namespaces": r"### Inspecting Objects and Namespaces (객체와 네임스페이스 점검하기)",

    r"The function `dir()` provides a list of objects in a namespace.":
    r"""The function `dir()` provides a list of objects in a namespace.
기능 함수 `dir()` 기조는 현재 네임스페이스 공간 안에 등록된 모든 객체(objects) 목록 리스트 묶음을 나열 제공해 줍니다.""",

    r"3.6 Lab: Linear Regression 117": r"",

    r"This shows you everything that `Python` can find at the top level. There are certain objects like `__builtins__` that contain references to built-in functions like `print()` .":
    r"""This shows you everything that `Python` can find at the top level.
이 결과물은 현재 `Python` 환경이 최상단 레벨 위에서 감지해 찾을 수 있는 활성 요소 모든 것들을 단적으로 여실히 보여줍니다.

There are certain objects like `__builtins__` that contain references to built-in functions like `print()`.
이들 목록 안엔 `__builtins__` 같은 특정한 기본 객체들이 자리하는데, 이 객체 꾸러미 내부에는 보편적인 `print()` 따위와 같은 여러 내장 파이썬 함수들의 참조 정보가 수반되어 담겨 있습니다.""",

    r"Every python object has its own notion of namespace, also accessible with `dir()` . This will include both the attributes of the object as well as any methods associated with it. For instance, we see `'sum'` in the listing for an array.":
    r"""Every python object has its own notion of namespace, also accessible with `dir()`.
모든 개별 파이썬 객체는 저마다 고유한 자체 নে임스페이스(namespace) 구역 영토 개념을 소유 지니고 있으며, 역시 앞선 `dir()` 명령 함수를 대입해 언제든 직접 탐색 접근해 볼 수 있습니다.

This will include both the attributes of the object as well as any methods associated with it.
여기에 산출된 반환 리스트 안에는 해당 객체 고유의 제반 프로퍼티 속성(attributes) 항목들은 물론이며 그것과 연관되어 파생된 모든 메서드(methods) 기능 요소들까지 통째로 다 수용 포섭되어 담깁니다.

For instance, we see `'sum'` in the listing for an array.
일례를 들어 배열(array) 항목을 겨냥한 저 위 나열 리스트 표기 안에서 우리는 버젓이 `'sum'` 이란 메서드 표시 항목을 발견 볼 수 있습니다.""",

    r"This indicates that the object `A.sum` exists. In this case it is a method that can be used to compute the sum of the array `A` as can be seen by typing `A.sum?` .":
    r"""This indicates that the object `A.sum` exists.
이것은 해당 `A` 배열 객체 내부에 `A.sum` 요소가 버젓이 존재함을 확실히 가리킵니다.

In this case it is a method that can be used to compute the sum of the array `A` as can be seen by typing `A.sum?`.
더구나 이 국면에서 해당 기능은 곧장 `A.sum?` 명령어를 타건 입력해 그 도움말을 띄워 살펴볼 수 있듯, 대상 넘파이 배열체 `A` 가 지닌 원소들의 총합을 고스란히 연산 도출해 내는 데 쓰일 수 있는 어엿한 메서드 방법 도구입니다."""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")

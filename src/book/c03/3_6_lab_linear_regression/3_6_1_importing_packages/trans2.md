---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6 Lab Linear Regression](../trans2.html) | [3.6.2 Simple Linear Regression >](../3_6_2_simple_linear_regression/trans2.html)

# _3.6.1 Importing packages_

# 3.6.1 패키지 불러오기(Importing packages) - 도구 상자 챙기기

We import our standard libraries at this top level.
자, 본격 코딩 실습 전에 우리 목수 단원들 가장 기본이 되는 필수 '기초 장비 도구 상자(표준 라이브러리)'부터 맨 꼭대기 최상단에 미리 꺼내 세팅해 두고 시작합시다!

```python
In [1]: import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
```

### New imports (새로 추가 불러오기)

Throughout this lab we will introduce new functions and libraries.
앞으로 전개될 이번 기나긴 회귀 실습 연구실 전 과정을 굽이굽이 거치며, 우리는 무수한 새 파이썬 함수와 막강 라이브러리 전술 도구들을 추가로 쏟아내며 하나하나 소개 투입할 것입니다.

However, we will import them here to emphasize these are the new code objects in this lab.
다만! "얘네가 바로 이번 단원 실습에서 활약할 그 대단한 신상 파워 도구(객체 요소)들입니다!"라고 초장부터 여러분 귀에 딱지를 앉히고 뚜렷이 스포일러 강조하고자, 이곳 코드 지붕 최상단에서 미리 이 녀석들을 싹 다 땡겨서 앞당겨 소환해 불러들일(import) 겁니다.

Keeping imports near the top of a notebook makes the code more readable, since scanning the first few lines tells us what libraries are used.
노트북 환경(주피터 등) 코딩 에티켓에선, 되도록 `import` 소환 구문 묶음을 문서 맨 꼭대기 천장 근처에 일괄 몰아넣어 전면 배치하는 룰이 국룰인데! 왜냐하면 남의 코드를 볼 때 그저 첫 줄 몇 개 행 목록만 얼핏 휙 스캔해 훑어보아도 "아~ 이 사람 이 코드에서 밑에 대충 이거저거 이런 도구 장비(라이브러리) 꺼내서 공사 칠 예정이구나~" 하고 한눈에 각이 딱 잡혀 가독성이 넘사벽으로 좋아지기 때문이죠!

```python
In [2]: import statsmodels.api as sm
```

We will provide relevant details about the functions below as they are needed.
저 라이브러리에 숨은 수백 가지 함수들의 복잡한 사용법은 걱정 마세요. 아래 전장 실전 코딩에서 그 함수 기능들이 하필 딱 그 순간 쓰임새 맥락에서 요구 출몰될 때마다! 우리가 그때그때 친절하게 가이드 메뉴얼 관련 요점 세부 내용을 상세히 덧붙여 밀착 과외 제공할 것입니다.

Besides importing whole modules, it is also possible to import only a few items from a given module.
참, 거대한 모듈 장비 창고 전체를 무식하게 통째로 다 수레에 실어 통으로 불러들이는 무식한 `import` 방식 외에도! 핀셋으로 집듯 지정된 모듈 창고 안에서 딱 내가 필요한 소수 몇몇 아이템 부품 항목 구문만 쪽쪽 골라 개별 발췌해 선별 소환해(import) 꺼내 쓰는 것도 얼마든 기막히게 가능합니다! (`from ~ import ~` 구문 활용)

This will help keep the _namespace_ clean.
이런 얄미운 쪽집게 선택적 취합 스킬 방식은, 우리 코드 세상의 안방 거실 바닥! 즉 _'네임스페이스(namespace, 이름표들이 등록되는 공간)'_ 구역을 어지럽게 더럽히지 않고 쾌적 정갈 깨끗 깔끔 콤팩트하게 다이어트 유지해 주는 데 아주 지대한 쾌적 보탬 역할을 합니다.

We will use a few specific objects from the `statsmodels` package which we import here.
그래서! 우린 그 방대한 저택 `statsmodels` 패키지 군집 창고 안을 다 털지 않고, 당장 우리가 써먹을 딱 몇 가지 알짜배기 특정 무기 객체만을 핀타켓 저격 특정 지어 꺼내 가져다 쓸 예정이므로, 이곳에서 관련 항목들만 아래처럼 쪽집게로 쏙 솎아 호출 불러옵니다.

```python
In [3]: from statsmodels.stats.outliers_influence \
import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm
```

As one of the import statements above is quite a long line, we inserted a line break `\` to ease readability.
위 기재된 소환(import) 구문 코드 중 하나가 가로 화면을 뚫을 만큼 징그럽게 꽤 길게 쭉 늘어진 뱀 코드를 형성한 탓에, 코드 멀미가 날 독자 여러분 가독성을 편안하게 배려 안구 정화차! 코딩 꿀팁 중간에 구부러진 **백슬래시 `\` 연장 기호**를 강제 삽입 슬래시해 '아직 내말 뒤에 행 안 끝났다~' 알림 줄 바꿈 엔터를 가해 안착시켜 주었습니다. (이거 아주 유용합니다!)

We will also use some functions written for the labs in this book in the `ISLP` package.
아울러 우리는 이 교재 저자들이 우릴 위해 제반 실습 랩(labs) 코스 전개용으로 친절하게 사전에 공들여 특수 고안 제작 작성해 배포한, 일명 어둠의 비기 `ISLP` 패키지 내부의 몇몇 꿀단지 전용 사제 함수 도구들 또한 씹고 뜯고 맛보며 적극 활용할 속셈입니다!

```python
In [4]: from ISLP import load_data
from ISLP.models import (ModelSpec as MS,
summarize,
poly)
```

### Inspecting Objects and Namespaces (객체와 네임스페이스 점검하기) - 내 방에 뭐뭐 있나 뒤져보기!

The function `dir()` provides a list of objects in a namespace.
파이썬 기본 내장 탐지 함수 중 **`dir()`** 명령 기조는, 마치 후래쉬라이트를 켜듯! 현재 작업 중인 네임스페이스(이름 공간 안방) 공간 안에 장부 등록되어 뒹굴고 있는 모든 객체(objects) 식구 목록 리스트 묶음 정체들을 남김없이 색출 나열 고발 제공해 줍니다!

```python
dir()
```

```python
In [5]:dir()
```

```python
Out[5]:['In',
'MS',
'_',
'__',
'___',
'__builtin__',
'__builtins__',
...
```

```python
'poly',
'quit',
'sm',
'summarize']
```

This shows you everything that `Python` can find at the top level.
자 이 리스트 스캔 결과물이 보이십니까? 이건 현재 우리의 `Python` 통제 환경 시스템 피지컬이, 땀 흘려 가장 꼭대기 최상단 레벨 안방 공중 위에서 색출 감지해 샅샅이 뒤져 찾을 수 있는 활성 거주 요소 모든 찌꺼기 것들을 단적으로 탈탈 털어 여실히 폭로해 보여줍니다.

There are certain objects like `__builtins__` that contain references to built-in functions like `print()`.
이 적나라한 거주자 목록 안엔 유독 앞뒤로 언더바를 휘감은 흉악 기괴한 `__builtins__` 같은 특정한 기본 뼈대 객체들이 은둔 자리하는데요, 놀라지 마세요! 이 지하실 객체 꾸러미 내부 보따리 안에는... 우리가 숨 쉬듯 자연스레 당연하게 쓰는 `print()` 따위와 같은 수많은 태생 만병통치 여러 내장 파이썬 기초 함수들의 공장 참조 주소 정보가 은밀히 수반되어 꽉꽉 담겨 보존되어 실려 있는 겁니다.

Every python object has its own notion of namespace, also accessible with `dir()`.
심지어! 우리 파이썬에 굴러다니는 '모든 낱개 개별 파이썬 객체' 놈팡이들 단자 하나하나는 기가 막히게도 저마다 자기 뱃속 고유의 자체적인 네임스페이스(namespace) 소우주 구역 영토 세계 개념을 따로 또 둥지 소유 지니고 품고 있으며!! 이놈들 뱃속 역시 앞선 돋보기 엑스레이 `dir(객체명)` 명령 구문 함수를 타겟 대입 쑤셔 넣으면 언제든 발가벗겨 직접 안을 엑스레이 탐색 접근 통과해 볼 수 있다는 엄청난 꿀팁 사실!

This will include both the attributes of the object as well as any methods associated with it.
여기에 엑스레이 스캔쳐 맞고 산출된 반환 리스트 뱃속 안에는? 해당 타겟 객체 고유성질 피부결 속성 제반 프로퍼티 속성(attributes) 항목 명칭들은 물론이거니와! 그것과 파생되어 야물딱지게 작동 연관 파생 결부 수행되는 모든 숨겨진 '메서드(methods, 스킬 장착 기능)' 기술 스킬 트리 기능 요소들까지, 그야말로 남김없이 뼈도 안 남고 통째로 다 수용 압수 포섭되어 폭로 고발 담겨 나옵니다!

For instance, we see `'sum'` in the listing for an array.
극단적 일례를 들어보죠! 지금 당장 저기 흔해 빠진 흔한 1차원 숫자 배열(넘파이 array) 한 놈을 겨냥 창조 타겟 조립한 뒤 엑스레이 저 위 나열 리스트 `dir()` 표기를 박아버리면? 버젓이 그 방대한 스펙 목록 속에 잠들어 있던 기특한 **`'sum'(합계 내기 스킬)`** 이란 숨은 메서드 스킬 표시 항목을 우리는 버젓이 적발 발견 엿볼 수 있습니다!

```python
In [6]:A=np.array([3,5,11])
dir(A)
```

```python
Out[6]:...
'strides',
'sum',
'swapaxes',
...
```

This indicates that the object `A.sum` exists.
이 적발 단서 결과물은 곧 이것이 무엇을 선언하냐고요? 넵! 저 `A` 배열 객체 무기 뱃속 내부에, 마침내 언제든 뽑아 버튼 눌러 구사 꺼내 쓸 수 있는 마법 총알 장전!! 바로 타겟 작동 기능 **`A.sum`** 요소 버튼 스위치가 버젓이 당당 실존 존재 장착해 있음을 확실히 명명백백 만천하에 드러내 가리킵니다!

In this case it is a method that can be used to compute the sum of the array `A` as can be seen by typing `A.sum?`.
더구나 이 실전 코딩 스킬 국면에서 이 기능 스위치의 정체는 뭐냐면? 주피터 셀 명령어에 곧장 **`A.sum?`** 하고 뒤에 호기심 물음표 명령어를 타건 빙고 입력해 쳐 박아 당장 그 사용 설명서 도움말 안내서 메뉴얼을 셀에서 띄워 엿보며 재확인 살펴볼 수 있듯이! 마법처럼 대상 저 넘파이 배열체 집단 `A` 가 각자 품고 지닌 원소 알맹이 숫자들의 총 누적 총합 액수를 가뿐 단 1줄에 고스란히 쿨 연산 뽑아 도출 합계 반환 계산(compute)해 내는 데 요긴 전담 맹활약 쓰일 수 있는 어엿한 무적 내장 자동 덧셈 스킬 메서드 조달 방법 도구란 사실이죠! (코딩 만세!)

```python
In [7]:A.sum()
```

```python
Out[7]:19
```

---

## Sub-Chapters (하위 목차)


[< 3.6 Lab Linear Regression](../trans2.html) | [3.6.2 Simple Linear Regression >](../3_6_2_simple_linear_regression/trans2.html)

---
layout: default
title: "trans2"
---

[< 2.3.6 Indexing Data](../2_3_6_indexing_data/trans2.html) | [2.3.8 For Loops >](../2_3_8_for_loops/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.7 Loading Data
# 2.3.7 데이터 불러오기 (데이터 적재함 열기)

Data sets often contain different types of data, and may have names associated with the rows or columns.
현업에서 굴러다니는 현실의 데이터 세트들은 숫자로만 예쁘게 정돈된 앞선 배열들과는 체급이 다릅니다. 문자와 숫자가 뒤죽박죽된 온갖 종류의 데이터들이 짬뽕으로 섞여 있고, 행(가로)과 열(세로)마다 각각 길고 복잡한 사람 이름이나 기계 이름표 등의 라벨이 연관되어 덕지덕지 붙어 있을 수도 있죠.

For these reasons, they typically are best accommodated using a _data frame_.
바로 이 골치 아픈 현실적인 이유 때문에, 이런 다채로운 짬뽕 데이터들을 단일 배열 통에 무식하게 욱여넣는 대신, 전형적으로 칸막이가 정갈히 나눠진 **_데이터 프레임(data frame)_** 이란 화물 컨테이너 상자에 모셔 담아 보관 수용(accommodated)하는 방식이 최고의 효율을 자랑합니다.

We can think of a data frame as a sequence of arrays of identical length; these are the columns.
이 거대한 데이터 프레임을 상상해 볼까요? 서로 다른 내용물(문자, 숫자 등)을 담았지만 위에서 아래로 키(길이)만큼은 똑같은 길쭉한 1차원 배열 기둥들이 병풍처럼 줄지어 도열한 시퀀스(sequence) 다발 묶음이라 생각하면 딱 맞습니다. 이 길쭉한 기둥들이 바로 해당 프레임의 데이터 성격을 규정하는 열(columns)들입니다.

Entries in the different arrays can be combined to form a row.
그리고 각기 다른 성질의 1차원 배열 기둥들에서 가로 방향으로 똑같은 층수(예: 3층) 요인 항목들만 옆으로 쓱 엮어서 추출 결합하면? 그게 바로 데이터 세트의 한 개체 기록을 대변해 형성하는 하나의 행(row, 가로줄) 데이터 세트가 되는 것이죠.

The `pandas` library can be used to create and work with data frame objects.
파이썬 세상에서 이 복잡한 데이터 프레임 컨테이너 객체들을 마음먹은 대로 뚝딱 찍어 생성해 내고, 자유자재 파워풀하게 요리해 작업하는 모든 전권은 위대한 `pandas` 패키지 도구 단원에 일임되어 사용됩니다.

## Reading in a Data Set
## 데이터 세트 읽어 들이기 (파일 하역 작업)

The first step of most analyses involves importing a data set into `Python`.
마법 같은 데이터 분석을 시작하려면, 그 대장정의 필연적 첫 번째 시작 단계는 외부에 굴러다니는 거친 데이터 파일 세트를 어떻게든 파이썬 스튜디오 안쪽으로 수입(importing)해 통째로 납치해 이입해 들여오는 일부터 수반해 벌여야 합니다.

Before attempting to load a data set, we must make sure that `Python` knows where to find the file containing it.
이 귀한 데이터 세트를 메모리로 끌어올려 적재(load)하려 과감히 시도하기 전에, 먼저 어리바리한 `Python` 녀석에게 내 데이터 파일이 도대체 어느 하드볼륨 폴더 구석에 처박혀 숨어있는지 그 절대적 위치를 멱살 잡고 확실히 인지시켜 놔줘야 합니다.

If the file is in the same location as this notebook file, then we are all set.
만약 다행스럽게도 불러올 데이터 파일이 당초 여러분이 코딩을 치고 있는 주피터 노트북 파일과 한 지붕 아래(같은 폴더 위치)에 얌전히 오순도순 동거 중이라면? 아무것도 할 게 없습니다, 준비 완료!

Otherwise, the command `os.chdir()` can be used to _change directory_. (You will need to call `import os` before calling `os.chdir()`.)
하지만 웬걸 전혀 엉뚱한 폴더에 파일이 있다면? 파이썬을 그 폴더로 강제 이사시켜 버리는 무자비한 `os.chdir()`(디렉터리 이동) 조치 명령을 치중해 구사해야 합니다. (아, 이 지휘 명령을 부르기 전에 내장 윈도우 조작기인 `import os` 경찰을 패키지로 사전 호출하는 걸 절대 잊지 마세요!)

We will begin by reading in `Auto.csv`, available on the book website.
먼저 몸풀기로, 본 교재 공식 웹사이트에서 공짜로 배포하는 전설의 차량 데이터 지표 `Auto.csv` 파일을 끌고 와 속을 한 번 읽어 들이며 실습을 개시해 보겠습니다.

This is a comma-separated file, and can be read in using `pd.read_csv()`:
파일 꼬리표를 보세요, `.csv` 죠? 이놈은 데이터 항목들이 찰싹찰싹 쉼표(,) 콤마로 무자비하게 나뉘어 가름벽 구별 처리가 된 파일이란 뜻입니다. 그래서 이런 친구는 판다스가 제공하는 전용 핀셋, 즉 `pd.read_csv()` 함수 도구를 사용하여 순식간에 빨아들여 읽을 구조입니다:

```python
In [73]: import pandas as pd
         Auto = pd.read_csv('Auto.csv')
         Auto
```

The book website also has a whitespace-delimited version of this data, called `Auto.data`.
웹사이트에는 콤마로 구별된 저 데이터 말고도 내용을 파헤쳐 보면 여백(스페이스 공백)을 벽으로 삼아 항목 데이터들을 넓게 구분 지어 놓은(whitespace-delimited) 동일 내용의 또 다른 버전의 형제 뻘 쌍둥이 파일, 명칭 `Auto.data` 놈도 떡 하니 버티고 있습니다.

This can be read in as follows:
다만 벽 종류가 콤마가 아니니 옵션을 좀 비틀어야 이놈 역시 다음과 같이 깔끔하게 데이터 프레임 안으로 들어차 읽힐 수 있습니다:

```python
In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
```
(옵션 `delim_whitespace=True` 를 슬쩍 끼워 넣으니까 "공백이 벽이네!" 하고 판다스가 귀신같이 알아챕니다.)

Both `Auto.csv` and `Auto.data` are simply text files.
`Auto.csv`와 `Auto.data` 이 두 친구의 치명적 공통점은? 화려한 확장자를 가졌어도 껍질을 까보면 결국 메모장으로도 열리는 뼈대 허술한 단순 텍스트 쪼가리 파일들에 불과하다는 점입니다.

Before loading data into `Python`, it is a good idea to view it using a text editor or other software, such as Microsoft Excel.
그래서 파이썬 입속으로 이 데이터를 쌩으로 구겨 밀어 넣기(loading) 직전에, 눈에 뻔히 보이는 친숙한 메모장 텍스트 편집기나 마이크로소프트 엑셀 같은 다른 고상한 소프트웨어로 파일 속살을 한 번 쓱 열어서 오염도는 없는지 스캐닝을 눈으로 보는 게 아주 훌륭한 생존 아이디어입니다.

We now take a look at the column of `Auto` corresponding to the variable `horsepower`:
데이터 프레임에 일단 들어왔으니, `Auto` 컨테이너 상자에서 차의 심장 마력, 즉 **`horsepower`** 변수 기둥표 열(column) 하나만 딱 집어서 눈앞에 까뒤집어 째려보겠습니다:

```python
In [75]: Auto['horsepower']
Out[75]: 0       130.0
         1       165.0
         2       150.0
         3       150.0
         4       140.0
               ...
         392      86.0
         393      52.0
         394      84.0
         395      79.0
         396      82.0
         Name: horsepower, Length: 397, dtype: object
```

We see that the `dtype` of this column is `object`.
결과창 밑바닥 꼬리표를 째려보십시오! 놀랍게도 숫자가 잔뜩 적혀 있는 듯한 이 마력 열의 뼈대 속성 스펙(`dtype`)이 계산 가능한 정수나 실수가 아니라, 잡다구리한 쓰레기도 다 받는 **`object` (주로 문자열 객체)** 취급을 단연 당하고 있음을 극적으로 관찰합니다.

It turns out that all values of the `horsepower` column were interpreted as strings when reading in the data.
이게 어찌 된 영문이냐? 엑셀에서 데이터를 무지성으로 처음 파이썬으로 빨아들이며 읽을 그 찰나의 순간에, 파이썬 감식반이 `horsepower` 열에 든 모든 숫자값 데이터를 건방지게 단연코 **'문자열(strings) 글자' 나부랭이로 오판해 해석해석(interpreted)** 통과시켜 버렸음이 뒤늦게 판명된 호러 사태입니다.

We can find out why by looking at the unique values.
왜 파이썬은 이런 멍청한 오해를 했을까요? 우리는 그 안에 숨은 온갖 이상한 스파이들을 모조리 솎아내어 보여주는, 고유값 스캐너 거울(`np.unique()`)을 냅다 비춰 봄으로써 그 지저분한 연유를 단박 알아낼 수 있습니다.

```python
In [76]: np.unique(Auto['horsepower'])
```

To save space, we have omitted the output of the previous code block.
(이 스캐너를 돌렸을 때 화면 가득 쏟아진 모든 데이터 값들의 장황한 출력 결과는, 책 지면 공간 단락을 절약 지면하기 위해 저자가 이내 야속하게 화면에서 썰어 지워 생략해(omitted) 처리했습니다. 여러분 파이썬에선 나올 겁니다!)

We see the culprit is the value `?`, which is being used to encode missing values.
스캐너 내역을 눈알 빠지게 뒤져본 결과, 으악! 중간에 주범(culprit)인 물음표 기호 **`?`** 한 마리가 거만하게 섞여 있는 치명상을 목격합니다! 차의 마력을 조사 모른다고 누가 기록지에 그 위치 자리를 비우기 뭐해 빈칸 누락 결측치(missing values) 암호 명목으로 불량하게 `?` 표시를 인코드(encode)해 때려 박아 쓴 거죠. 이것 하나 때문에 파이썬이 전체 기둥을 "글씨군!" 하고 오해한 겁니다.

To fix the problem, we must provide `pd.read_csv()` with an argument called `na_values`.
이 절망적 문제를 애초에 싹 고치려면? 타임머신을 타고 아까 파일 입속 로딩 하역 단계였던 `pd.read_csv()` 함수 호출 시절로 돌아가서, 옵션 인자로 "야 문자 목록 중에서 `na_values` 로 넘긴 건 다 빈칸(NaN) 폭탄이야!"라는 살생부 인자를 하나 확실히 제공해 꽂아줘야만 합니다.

Now, each instance of `?` in the file is replaced with the value `np.nan`, which means _not a number_:
이제 옵션을 끼우고 다시 파일을 읽는 순간 마법이 펼쳐집니다! 파일 속에 스파이처럼 박혀있던 그 `?` 찌꺼기 글자 사례들이 파이썬 감찰관에 의해 모조리 색출 포위되어 파이썬 세계의 공식 '블랙홀 결측치' 값, 즉 "이놈은 숫자가 아니다(_not a number_)"라는 뜻의 투명 망토 값인 **`np.nan`** 데이터로 여지없이 싹 다 대체(replaced) 압수 갈이 됩니다:

```python
In [77]: Auto=pd.read_csv('Auto.data',
                          na_values=['?'],
                          delim_whitespace=True)
         Auto['horsepower'].sum()
```

```python
Out[77]: 40952.0
```
(보세요! 이제야 제대로 숫자 취급을 받아서 `sum()` 덧셈 연산기가 안 터지고 멋지게 마력 총합을 산출하지 않습니까!)

The `Auto.shape` attribute tells us that the data has 397 observations, or rows, and nine variables, or columns.
데이터의 신체 윤곽을 보여주는 엑스레이 스캔 스위치 `Auto.shape` 속성을 딱 누르면, 뱃속에 개별 자동차 기록 즉 총 관측치라 불리는 가로 **행(rows)이 397개** 켜켜이 차 있고, 차 이름, 마력, 무게 등 세로 분류 **변수 명목의 열(columns)이 9개**로 단단히 틀을 갖추고 구조하고 지어있음을 우리에게 명쾌하게 보고해 말해 줍니다.

```python
In [78]: Auto.shape
```

```python
Out[78]: (397, 9)
```

There are various ways to deal with missing data.
아까 그 `np.nan` 으로 구멍 뚫린 결측 데이터 좀비 바이러스들을 다루고 치료하는 방법은 실로 무궁무진하게 다단하고 다양한 기법 방안들이 즐비합니다. (평균으로 메우기 등등)

In this case, since only five of the rows contain missing observations, we choose to use the `Auto.dropna()` method to simply remove these rows.
하지만 이 케이스의 경우엔, 전체 397개의 행 데이터 거구 부락 중에서 고작 달랑 5마리 행에서만 빈칸 좀비(결측치)가 발현해 관측되어 포함되어 있기 때문에, 우린 치료를 포기하고 해당 오염된 행 전체 라인들을 가차 없이 깔끔히 도려내 완전히 삭제 제거해 치우기 목적으로 **`Auto.dropna()` (구멍 난 층 통째 폭파 함수!)** 제거 메서드를 결연히 꺼내 사용 조치를 시전하기로 매몰차게 결정 지위를 결심합니다.

```python
In [79]: Auto_new = Auto.dropna()
         Auto_new.shape
```

```python
Out[79]: (392, 9)
```
(결과를 보세요! 깔끔하게 오염된 5대의 차 장부가 타살 삭제돼 증발하고 청정한 행 392개만이 도출 생존되어 산출됐습니다!)

## Basics of Selecting Rows and Columns
## 열과 행들 낚아채기 특수 비법 (인덱싱 기본편)

We can use `Auto.columns` to check the variable names.
우리 차트 아파트 지붕 꼭대기에 각 열마다 무슨 이름표 간판이 매달려 있는지 검진 차 열람 확인하고 싶다면? 가볍게 `Auto.columns` 배지만 띄워 조작해 부르면 단연 해결되어 사용될 수 있습니다.

```python
In [80]: Auto = Auto_new # overwrite the previous value
         Auto.columns
```
(팁: `Auto = Auto_new` 코드로 방금 쓰레기 청소(dropna)된 깨끗한 데이터 프레임을 원래 원본 변수 이름에 과감히 덮어쓰기(overwrite) 암살 작전을 해버립니다!)

```python
Out[80]: Index(['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'year', 'origin', 'name'],
               dtype='object')
```

Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array.
이 특수 데이터 프레임 컨테이너의 특정 행이나 단면 열들을 조작해 접근 호출하는 낚아채기 수단은 앞 절에서 배운 순수 `numpy` 배열 아파트의 그 인덱싱 방법과 언뜻 쌍둥이처럼 유사해 보이겠지만, 안쪽 규칙 자체는 동일하지 않고 은근 다르고 매운(not identical) 변칙 맛을 냅니다.

Recall that the first argument to the `[]` method is always applied to the rows of the array.
아까 `numpy` 배열의 대원칙! 대괄호 `[]` 그물을 던질 때 첫 번째 빈칸 자리는 항상 변함없이 층수 단위 즉 요소 그 '배열의 행들(rows)' 지점을 단연 표적해 강제로 선 압수 적용된다는 숭고한 룰을 상기(Recall)하시죠?

Similarly, passing in a slice to the `[]` method creates a data frame whose _rows_ are determined by the slice:
유사하게 똑같은 이치 논리로, 판다스 데이터 프레임도 냅다 대괄호 `[]` 안으로 범위 슬라이스 칼도막(예: `:3`)을 무방비 전입 넘겨 전달 꽂아 치면, 그 칼잡이 범위 조건에 의해 철저하게 선택된 **행들(_rows_)** 만 쏙 발라낸 새로운 조각보 서브 데이터 프레임 하나를 기꺼이 창조 도출해 거출해 토해냅니다:

```python
In [81]: Auto[:3]
```

|**`Out[81]:`**||`mpg`|`cylinders`|`displacement`|`horsepower`|`weight`|`...`|
|---|---|---|---|---|---|---|---|
||`0`|`18.0`|`8`|`307.0`|`130.0`|`3504.0`|`...`|
||`1`|`15.0`|`8`|`350.0`|`165.0`|`3693.0`|`...`|
||`2`|`18.0`|`8`|`318.0`|`150.0`|`3436.0`|`...`|

Similarly, an array of Booleans can be used to subset the rows:
마찬가지로 아주 거칠고 잔인한 인덱싱 방식, 참/거짓 판별의 마법 거울인 '불리언(Booleans) 배열 군단'을 살생부로 던져서 데이터 프레임의 행들 중 타깃들만을 부분집합 고정 핀셋 발췌해 (subset) 추려내기 위해 악랄하게 단연 사용될 공산 수 조차 능히 갖추고 마련됩니다:

```python
In [82]: idx_80 = Auto['year'] > 80
         Auto[idx_80]
```
(이 코드는 차 연식이 80년도보다 큰가? 라는 `True/False` 심판의 배열표를 만든 뒤, 그걸 덮어씌워 `True` 불이 켜진 타깃 행들만 쏙 빼내는 마법 도출구입니다!)

However, if we pass in a list of strings to the `[]` method, then we obtain a data frame containing the corresponding set of _columns_.
그러나 여기서 대이변 발생! 슬라이스나 규칙 부호 말고, 우리가 만약 대괄호 `[]` 입구 속성 안쪽에다가 생짜 문구 이름표 명단들로 구성된 '문자열 리스트(`['mpg', 'horsepower']`)'를 거듭 휙 던져 전달해 넣는다면? 판다스는 이를 "아하! 행 말고 기둥 간판 이름을 줬네!" 라고 똑똑하게 판별해서, 해당 간판 이름 지정명에 직후 기인 상응하는 **기둥 열들(_columns_) 뭉치 세트**만을 딱 꼬집어 포함해 발췌한 단독의 새 데이터 프레임 컨테이너 패키지 하나를 이내 구축 도출 확보해 획득 반환합니다.

```python
In [83]: Auto[['mpg', 'horsepower']]
Out[83]:       mpg  horsepower
         0    18.0       130.0
         1    15.0       165.0
         2    18.0       150.0
         ...
```

Since we did not specify an _index_ column when we loaded our data frame, the rows are labeled using integers 0 to 396.
차트 결과 맨 왼쪽에 달린 지번 숫자 보이시죠? 아까 우리가 무지성으로 처음 데이터를 적재(loaded)할 시절에, "얘를 기준이 되는 아파트 동호수 _인덱스(index) 표찰_ 열 기반 기둥으로 강제 확립해 줘!"라고 명시 지정 옵션을 주지 않았기 때문에, 집주인 판다스가 어쩔 수 없이 임의로 0에서 396까지의 무의미한 일련번호 정수 숫자표들을 기둥 세워 행들에 라벨(label) 이름표 태그로 덕지덕지 수동 부착해 놓았던 상태입니다.

```python
In [84]: Auto.index
Out[84]: Int64Index([  0,   1,   2,   3,   ...  ],
                    dtype='int64', length=392)
```

We can use the `set_index()` method to re-name the rows using the contents of `Auto['name']`.
무의미한 숫자는 싫다! 우리는 `set_index()` 란 개명 신청 메서드 관공서 도구를 사용해, 자동차 차 이름들 통짜가 이내 담겨 적힌 저 `Auto['name']` 열 항목의 내용물들을 활용해 모든 행들의 숫자 간판 명패들을 매끈한 영어 이름들로 갈아엎어 다시 재 이름 짓기(re-name) 치장을 수행 부여할 권력을 쓸 수 있습니다.

```python
In [85]: Auto_re = Auto.set_index('name')
         Auto_re
Out[85]:                            mpg  cylinders  displacement  ...
         name                                                     ...
         chevrolet chevelle malibu  18.0          8         307.0  ...
         buick skylark 320          15.0          8         350.0  ...
         plymouth satellite         18.0          8         318.0  ...
         amc rebel sst              16.0          8         304.0  ...
```
(이름이 왼쪽 축으로 옮겨간 통쾌한 모습을 감상하세요!)

```python
In [86]: Auto_re.columns
Out[86]: Index(['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'year', 'origin'],
               dtype='object')
```

We see that the column `'name'` is no longer there.
변수 스캔(`columns`)을 돌려보니, 신분 상승해 왼쪽 고정 인덱스 축으로 박혀버린 `'name'` 글자 열 기둥은 이제 오른쪽 쩌리 일반 변수 목록들 속엔 더 이상 낑겨 존재하지 않고 당당히 승격해 그곳에서 실종 사라짐을 확인해 통치 봅니다.

Now that the index has been set to `name`, we can access rows of the data frame by `name` using the `loc[]` method of `Auto`:
이제 0, 1번 숫자가 아닌 알파벳 `name` 이 이 컨테이너의 절대 기준 인덱스로 못 박혀 셋업 단절 확립되었으므로! 우리는 멍청한 숫자 대신 스마트하게 `Auto` 녀석이 품은 강력한 **이름 추적기 `loc[]` (Locator) 메서드**를 사용하여 "자동차 이름(`name`)" 만을 표찰로 던져 우아하고 폼 나게 데이터 프레임 행 타깃 단위들에 조우 접근해 호출할 권한을 여지 얻습니다:

```python
In [87]: rows = ['amc rebel sst', 'ford torino']
         Auto_re.loc[rows]
Out[87]:                mpg  cylinders  displacement  horsepower  ...
         name                                                     ...
         amc rebel sst  16.0          8         304.0       150.0  ...
         ford torino    17.0          8         302.0       140.0  ...
```

As an alternative to using the index name, we could retrieve the 4th and 5th rows of `Auto` using the `iloc[]` method:
멋진 이름을 쓰는 것에 대한 통 반발과 대안격 방식 하나! "난 이름 따윈 됐고 직관적으로 무지성 옛날 번호로 좌표 찾을래!" 하시는 상남자 분들은 아까 쓴 이름 추적기(`loc`)가 아니라, '정수 번호 인덱스 로케이터'인 **`iloc[]` (Integer Locator) 메서드**를 거치고 사용하여 무력으로 `Auto` 의 4번째와 아울러 5번째 행 층수 구조 단원들을 우악스레 구태 건져 가져올 수조차 있습니다:

```python
In [88]: Auto_re.iloc[[3, 4]]
```

We can also use it to retrieve the 1st, 3rd and and 4th columns of `Auto_re`:
우리는 심지어 이걸 응용해서 행 층수뿐만 아니라 뒤쪽 영역인 `Auto_re` 의 1번째, 3번째 그리고 나아가 마지막 4번째의 다차 열들(기둥)만 쏙쏙 타격해 반환 가져오기 위해 또한 똑같은 그것 부과 도구(`iloc`)를 다단 무단 무상히 사용할 공산 기치를 띕니다:

```python
In [89]: Auto_re.iloc[:, [0, 2, 3]]
```

We can extract the 4th and 5th rows, as well as the 1st, 3rd and 4th columns, using a single call to `iloc[]`:
가로세로 복합 타격기! 우리는 `iloc[]` 에 대한 단번의 일격 단일 호출 그물망 주문 조치를 사용하여 타깃인 1번째, 3번째 및 종단 4번째 지정 열 부락들은 필시 물론이요 게다가 동시적으로 4번째와 단위 5번째 지명 행들 세트 양단을 교차적으로 한방에 분리 추출해 발췌할 타깃 수조차 있습니다:

```python
In [90]: Auto_re.iloc[[3, 4], [0, 2, 3]]
Out[90]:                mpg  displacement  horsepower
         name
         amc rebel sst  16.0         304.0       150.0
         ford torino    17.0         302.0       140.0
```

Index entries need not be unique: there are several cars in the data frame named `ford galaxie 500`.
아까 행 이름표(인덱스)가 절대적이라 했지만, 사실 그 인덱스 기재 지정 항목들이 무조건 유일 무이하게 주민번호처럼 중복 불가할 절대 필요 제약 조건 요소는 전혀 없습니다: 실제로 이 장부 데이터 프레임 컨테이너 속을 뒤져보면 완전 똑같은 `ford galaxie 500` 이라고 기표 이름 지어 명명된 동명이인 차들이 다수로 여러 대 떼거지 중복 발현해 있습니다! 

```python
In [91]: Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]
Out[91]:                    mpg  origin
         name
         ford galaxie 500  15.0       1
         ford galaxie 500  14.0       1
         ford galaxie 500  14.0       1
```
(보세요! 저 이름을 치면 겹친 3대의 차 기록이 죄다 토해져 반환됩니다!)

### More on Selecting Rows and Columns
### 행들과 단면 열들을 선택 추출하기에 관해 나아간 더블 플러스 사항들

Suppose now that we want to create a data frame consisting of the `weight` and `origin` of the subset of cars with `year` greater than 80 — i.e. those built after 1980.
여기서 극악무도한 실전 상황을 가정해 봅시다. 이제 우리가 연식 스펙 `year` 가 달랑 80도다 훌쩍 더 큰 최신 차들의 부분집합 — 다시 쉽게 즉 1980년 이후에 건조 만들어진 그 신형차 기물 것들 — 에 한정해서, 그놈들의 `weight(무게)` 와 `origin(탄생지)` 기둥 정보로만 딱 짜임새 있게 구성된 맞춤 데이터 프레임 컨테이너를 새 구역 하나 생성 출범시키길 극히 원한다고 단연 몽상해 봅시다.

To do this, we first create a Boolean array that indexes the rows.
이 고오급 필터링 기술을 행하기 위해, 우리는 우선 앞서 배웠던 그 신묘한 아이템, 즉 타깃 행 단위들을 감시 표적 인덱스 발라내는 (참/거짓 1/0) 특수 불리언 감시 배열 하나를 일차 창출 생성해 냅니다.

The `loc[]` method allows for Boolean entries as well as strings:
여기에 우리 무기 이름 추적기 `loc[]` 메서드는 아주 관대해서 글자 문자열 명패 구조들 척결 건네받는 것 일견뿐만 아니라, 이 당 불리언 참거짓 명부 항목들을 곧이 건네 받아 들여도 척척 필터링 통제 소화를 능히 무던 허용 지표해 이룹니다:

```python
In [92]: idx_80 = Auto_re['year'] > 80
         Auto_re.loc[idx_80, ['weight', 'origin']]
```

To do this more concisely, we can use an anonymous function called a `lambda`:
이걸 두 줄로 쓰려니 프로그래머의 자존심이 상합니다! 이 귀찮은 행위를 훨씬 한 큐에 간결하게(concisely) 날려버려 행하기 원한다면, 우리는 신원 미상의 유령 함수기능 조직인 일컫어 불리우는 `lambda` (람다)라는 익명 함수(anonymous function) 암살자를 무단 채용 사용할 여지 공산 파워를 갖춥니다:

```python
In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]
```

The `lambda` call creates a function that takes a single argument, here `df`, and returns `df['year'] > 80`.
이 `lambda` 호출부호 체계 문법은 한 큐에 일시적 암살 함수 하나를 배양 생성시키는데, 요 구조체는 단일 건네어진 인수 덩이, 다시 말해 여기서 저 `df`(데이터프레임을 줄인 말)를 집어 삼켜 취하고, 그 내부 뱃속 규칙 처리로 즉각 `df['year'] > 80` 필터 배열을 지표로 즉결 토해 단연 반환합니다.

Since it is created inside the `loc[]` method for the dataframe `Auto_re`, that dataframe will be the argument supplied.
이 유령 암살 함수는 저 바깥 데이터프레임 타깃 `Auto_re` 에 부과 걸린 `loc[]` 호출 메서드의 캄캄한 뱃속 내부 동공 안에서 교묘히 비밀리 생성 생장되기 연유 때문에, 저 문맥상 바깥의 데이터프레임 `Auto_re` 자체가 은밀하게 강제 대위 공급되어 수급되는 바로 그 인수(df) 가 기어코 될 체제 작정일 것입니다.

As another example of using a `lambda`, suppose that we want all cars built after 1980 that achieve greater than 30 miles per gallon:
이 엄청난 람다(`lambda`) 스나이퍼를 무사 사용하는 좀 더 독한 또 다른 예제 상황으로서, 우리가 갤런 화석 당 주행비 30 마일 단위 치수 연비를 월등 가뿐히 뚫어 달성해제 하는 동시 나아가 1980년 전방 이후에 단연 갓 만들어진 최신 모든 혼종 차들을 한꺼번에 묶어 사냥 원한다고 단면 가정해 봅시다:

```python
In [94]: Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30),
                     ['weight', 'origin']
                    ]
```

The symbol `&` computes an element-wise _and_ operation.
저기 괄호 두 개를 엮어주는 결박 밧줄! 기호 **`&` (앤퍼센드)** 요놈은 두 개의 까다로운 잣대(조건)를 "오직 둘 다 참이어야 통과다!" 라는 지독한 요소별(element-wise) 필터 규칙의 _and (그리고)_ 교집합 논리 연산을 가차 이뤄 계산 수행합니다.

As another example, suppose that we want to retrieve all `Ford` and `Datsun` cars with `displacement` less than 300.
피 터지는 마지막 사냥 또 다른 예제로서, 우리가 300 징표 기점보다 숫자가 더 작고 적은 빈약한 `displacement (배기량)` 구조를 보유 가진 동시 다발 덧붙여 오로지 명찰이 전제 `Ford` 와 나아가 저 `Datsun` 타이틀 구조물인 차들 일체 모조리를 전방 겨누어 반환 검색해 조달받기를 지목 강렬 원한다고 상정 가정해 봅시다.

We check whether each `name` entry contains either the string `ford` or `datsun` using the `str.contains()` method of the `index` attribute of the dataframe:
이 복잡한 문자를 찾기 위해 우리는 데이터프레임 자체의 지표 왼쪽 부지 명찰단 즉 `index` 부속 속성 내부 단원의 고유 문자 탐지기인 전결 `str.contains()` 메서드를 전격 사용하여 이내 각 단일 `name(이름)` 기입 대상 항목이 어김없이 문자열 덩이 `ford` 표기 혹은 또는 저짝 `datsun` 체제 중 구태 단 하나라도 그 살점에 오롯이 포함 수반 품고 있는지 내포 여부를 정밀 스캔 확인 파헤쳐 타진합니다:

```python
In [95]: Auto_re.loc[lambda df: (df['displacement'] < 300)
                     & (df.index.str.contains('ford')
                        | df.index.str.contains('datsun')),
                     ['weight', 'origin']
                    ]
```

Here, the symbol `|` computes an element-wise _or_ operation.
저기서 이름 둘 사이를 쪼개놓은 서 있는 일자 막대기 파이프라인 방벽! 여기서 이, 기호 **`|` (파이프 막대)** 는 "앞놈이든 뒷놈이든 둘 중 하나라도 맞으면 통과시켜!" 라는 아주 관대한 요소단별 별개 작동(element-wise) 분별의 _or (또는)_ 합집합 교차 연산을 너그러이 십분 연산 도출해 계산 수단 조작합니다.

In summary, a powerful set of operations is available to index the rows and columns of data frames.
숨 가쁜 여정을 총결 짓고 요약하자면, 이 거대한 상자 구역 데이터 프레임 단위들의 무수한 가로 행들과 세로 기둥 단면의 열들을 단독 인덱스 위치 집어내어 조작 발췌 사냥하기 위한 기조로 도출 수립된 어마 부위 무시강력한 무기 연산 조작 수리들의 한 세트가 대거 무장 이용 가능하게 구비 출몰해 있습니다.

For integer based queries, use the `iloc[]` method.
"난 이름 필요 없고 통짜 번호 지번(정수)으로 조질래!" 하시는 수치 정수 기반 질의 공격들에는, 상남자 번호 추적기 `iloc[]` 메서드를 단연 무지막지하게 꺼내 사용하십시오.

For string and Boolean selections, use the `loc[]` method.
"그 무식한 번호 말고 이름 명찰 문자열 및 참거짓 스펙 필터 불리언 판독 선택 조치들을 기조 발휘 할래!" 하시는 깐깐한 분들에겐, 최첨단 이름 추적기 `loc[]` 고급 메서드를 단조 사용 채택하십시오.

For functional queries that filter rows, use the `loc[]` method with a function (typically a `lambda`) in the rows argument.
복잡 다단한 다중 조건으로 정밀 타격해 단 구획 행들을 체로 밭쳐 걸러내는(filter) 고기능 암살 함수적 공격 질의 도출들에는, 행들 타깃 지시 인수 칸 안에 단언 하나의 살아 숨 쉬는 함수 조각 요수(제반 전형적으로 한 구기 유령 스나이퍼 `lambda` 단원)와 곧장 맞물려 함께 묶이는 구조로 그 `loc[]` 도구 부속 메서드를 여지 부과 무기 징표로 단락 지목해 다잡아 사용을 구성 구동 하십시오.

---

## Sub-Chapters

[< 2.3.6 Indexing Data](../2_3_6_indexing_data/trans2.html) | [2.3.8 For Loops >](../2_3_8_for_loops/trans2.html)

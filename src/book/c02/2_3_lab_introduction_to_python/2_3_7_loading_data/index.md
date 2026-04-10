---
layout: default
title: "index"
---

# _2.3.7 Loading Data_
# 2.3.7 데이터 로드하기 (Loading Data)

Data sets often contain different types of data, and may have names associated with the rows or columns. For these reasons, they typically are best accommodated using a _data frame_. We can think of a data frame as a sequence of arrays of identical length; these are the columns. Entries in the different arrays can be combined to form a row. The `pandas` library can be used to create and work with data frame objects.

데이터 세트들은 흔히 특성이 각기 전혀 다른 이질적인 형식의 데이터 타입들을 포괄 포함하며, 간혹 각각의 개별 행(rows)이나 분류 열(columns) 단위 구역상에 고유한 특성 명칭이 지정 부여되어 연동되기도 합니다. 이러한 구조적 이유를 감안해 볼 때, 해당 정보들은 시스템상 통상적으로 _데이터 프레임(data frame)_ 구조를 사용하여 수용 담아내는 방식이 가장 체계적이고 적합합니다. 우리는 통상적으로 통계 데이터 프레임 구조를, 서로 완전히 똑같은 동일한 길이를 각자 지닌 배열(arrays) 시퀀스들이 연달아 나란히 나열된 전개 묶음 덩어리 형태라 간주 상상할 수 있는데; 이것들이 바로 각각의 개별 지표 열(columns)이 됩니다. 서로 파편화 분리된 개별 단독 배열 내에 위치 포진한 값들을 각기 좌우로 단편 일괄 병합해 수리 결합하면 하나의 개별 행(row) 구조 전제가 구축 형성됩니다. 데이터를 다루는 파이썬의 매우 핵심적 패키지 수단 라이브러리인 `pandas` 는 이러한 데이터 프레임 객체를 새로이 생성 지표하고 관련 내재 작업을 지시하는 데 주로 광범위하게 쓰이며 무척 단면 유용하게 매번 사용 조달됩니다.

## Reading in a Data Set
## 데이터 세트 불러 읽어들이기

The first step of most analyses involves importing a data set into `Python`. Before attempting to load a data set, we must make sure that `Python` knows where to find the file containing it. If the file is in the same location as this notebook file, then we are all set. Otherwise, the command `os.chdir()` can be used to _change directory_. (You will need to call `import os` before calling `os.chdir()`.)

대상의 대부분을 할애하는 데이터 분석 초기 작업에서 가장 맨 첫 번째 진입 단계는, 조달 분석 대상 모의를 뜻하는 특정 표본 데이터 세트를 `Python` 환경 내부로 전부 복제 임포트해 단편 가져오는 일입니다. 데이터 세트 탑재 투입을 전격 시도하기에 앞서서, 우리는 반드시 `Python` 시스템이 현재 단편 타깃 파일이 물리적으로 정확히 어느 폴더 위치 서가에 존재하는지를 명확히 식별 추적해 알게끔 확인해 주어야만 통제합니다. 만일 불러올 해당 데이터 파일이 현재 진행 구동 중인 내부 노트북(notebook) 단면 구동 파일과 화면상 완전히 판별 똑같은 시스템 단위 내부 폴더 위치에 함께 나란히 있다면 이와 관련한 모든 기본 시스템 준비는 무리 척건 없이 단숨에 끝난 것입니다. 만약 그와 다르게 기표 둘의 진입 위치가 각기 단편 다르다면, 시스템 콘솔의 경로 자체를 단번 바꾸는 명령어 구조인 `os.chdir()` 수단을 산술 사용해 타깃 파일이 기거하는 있는 단면 곳으로 구동 환경 진입 _디렉토리를 변경(change directory)_ 할 수 도출 개요 존재합니다. (물론 이 `os.chdir()` 구동 함수를 조달 단편 체제 호출하려면 그보다 먼저 해당 모의 앞단 라인에 필수 모의적으로 `import os` 모듈의 단독 선언 호출이 가장 우선시 이루어져야만 작동합니다.)

We will begin by reading in `Auto.csv`, available on the book website. This is a comma-separated file, and can be read in using `pd.read_csv()`:

우선 우리는 이 교육 본 교재의 소개 지원 공식 웹사이트에서 다운로드 수단이 조달 제공되는 전용 실습 훈련 파일인 `Auto.csv` 를 직접 로드 단면 호출하여 내부 시스템에 읽어오는 것부터 시연 시작하겠습니다. 진입된 해당 본 파일은 엑셀 등 데이터 수치가 각기 단락 쉼표(comma) 기호로 명백히 분리 구조화 나열된 전용 규격의 CSV 통상 파일 양식이므로, 고정 분석 체계 함수인 `pd.read_csv()` 구문을 모의 수단 통해 무척이나 간편히 로드 읽어들일 수 존재합니다:

```python
In [73]: import pandas as pd
         Auto = pd.read_csv('Auto.csv')
         Auto
```

The book website also has a whitespace-delimited version of this data, called `Auto.data`. This can be read in as follows:

해당 교재 진척 공식 지원 웹사이트에는 더불어 `Auto.data` 라 명명 지시 불리는, 상기 완전히 똑같은 동일한 원본 데이터를 오직 단순히 공백 단편(whitespace) 영역만으로 서로 구분 척도 격리한 전혀 또 다른 방식 버전의 단순 텍스트 지표 파일도 함께 첨부 존재 조달합니다. 이 특수한 포맷의 파일 형태는 조달 다음과 같이 파편 같은 코드형 조작 구문을 채택함으로써 도달 시스템 내부에 정상히 읽어들일 조달 수 단편 수립됩니다:

```python
In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
```

Both `Auto.csv` and `Auto.data` are simply text files. Before loading data into `Python`, it is a good idea to view it using a text editor or other software, such as Microsoft Excel.

저 두 방식인 `Auto.csv` 조달 및 특성 `Auto.data` 해당 문서 분면 조달 파일 두 개는 모두 결론상 단지 그저 컴퓨터 화면상 표면 흔한 단순 텍스트 구조 기반 체제 시스템 데이터 파일에 불과 존재합니다. 따라서 이를 단락 `Python` 연산 프로그램 구동 안으로 조단 단면 본격 단락 투입 적재 로드하기 훨씬 이전에, 기초 윈도우 메모장 등과 단면 같은 텍스트 코드 에디터나 더 나아가 마이크로소프트 분석 엑셀(Microsoft Excel) 등의 외곽 서브 분단 소프트웨어를 분면 사용 단편 채용해 해당 데이터 파일 고유의 단편 내부 데이터 수립 모습을 맨눈으로 미리 가볍게 단면 한 번 전격 훑어 사전 조달 확인 조달하는 통제 것이 분석 바람직한 통상 파편 조언 책무입니다.

We now take a look at the column of `Auto` corresponding to the variable `horsepower`:

이제 여기서 한 발 나아가 우리는 모의 저장된 `Auto` 요소 테이블에서 단편 특정 분류인 `horsepower` (마력) 지정 수리 변수에 1대1 단위로 해당 판별되는 기표의 단독 세로 열(column) 부분만을 단면 한번 따로 결합 떼어 집중 통제 살펴 결단 도출해 봅니다:

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

We see that the `dtype` of this column is `object`. It turns out that all values of the `horsepower` column were interpreted as strings when reading in the data. We can find out why by looking at the unique values.

도출된 출력 단편 결과를 유심히 살펴보면 현재 이 특정 추출 열거 열의 데이터 변수 형태인 `dtype` 정보가 수단상 `object` 분면 타입 형태로 지정 척도 도출 지정됨을 전격 알 단면 분수 수 조달 있습니다. 즉 이 현상 기표는, 시스템상 당초 우리가 최초로 시스템 환경 하부에 해당 데이터 모의를 읽어들일 진입 조달할 모의 시점 때 변수 도달 `horsepower` 열거 열 내부에 자리한 모든 배열 수치 지표 값들이 체감 단락 숫자 산술 정수 수단 기표가 전혀 아니라 단순 순수 텍스트 계열 문자열(strings) 체계 단편 속성으로 모두 잘못 파악 취급 해석 조달 취합되었음을 역설 반증 조달 역설합니다. 그 내부 진입 공간에 수집 담긴 각각 자체의 개별 고유 특성 배열 산출 값들을 면밀히 단면 통제 조사 파헤쳐 분석해보면 과연 어째서 어찌하여 모의 이런 종류의 황당한 오독 파악 현상이 초기부터 일절 발생 구동 조달 전격했는지 곧장 조달 명확한 그 단면 진상 이유를 알아낼 확연 수 파악 단절 포진되어 모의 단수 존재 도출 조달합니다.

```python
In [76]: np.unique(Auto['horsepower'])
```

To save space, we have omitted the output of the previous code block. We see the culprit is the value `?`, which is being used to encode missing values.

지면 본 단독 문단에서는 도출 물리적 문서 단편 지면의 효율 절약을 도모하기 위해 방금 시행한 이전 부분 구동 코드 조달 블록의 산출 단편 도출된 단결 결과물 화면 전경을 지면 서면상 완전히 단편 일괄 과감히 단절 생략 배제 조율했습니다. 조사 확인 분석 조달 단편 도출 최종 결과, 이 오류 문제의 가장 주동적인 원흉 사태는 본래 배열의 공란 등 결측된 시스템 값(missing values)들의 빈 구역을 척도 조달 표기 모의하기 위한 요량 단편으로 빈칸 대신 기표 대체 인코딩 단면 기호로써 각기 중간 중간에 섞여 오도 기입 모의 투입된 모의 바 단절 있는 바로 저 엉뚱한 물음표 기표 기호인 단면 `?` 해당 문자 단독 값이란 게 판명되었습니다.

To fix the problem, we must provide `pd.read_csv()` with an argument called `na_values`. Now, each instance of `?` in the file is replaced with the value `np.nan`, which means _not a number_:

이 파편 오독 해석 문제를 단박 전격에 일거 해결 파악 타결하기 위해, 도달 우리는 향후 단면 데이터를 시스템에 단독 불러 조달 단면 차출해 올 구문 적재 때 모단 `pd.read_csv()` 함수 구문에 시스템상 일명 `na_values` 라 불리 명명 진단 조율되는 특수 통제 방침 지정 인수 척도를 함께 모의 필히 진입 요구 전달 지표 조달 결단 지정해야 통괄합니다. 자, 이제 이 명령어로 인해 파일의 데이터 목록 속 안에 수집된 모든 개별 구단 물음표 단편 기호 요소인 단면 `?` 기표값은 시스템 체계 읽는 즉시 모조리 수단 체제 _숫자가 결코 아님(not a number)_ 논리 상태 속성을 시스템상 통제 즉시 의미 기표 판독 조율하는 산출 연계 자체 속성 기저값인 특성 `np.nan` 기입값 변수 조율 단위로 일괄 단독 대체 수식 변환 결합 지표됩니다:

```python
In [77]: Auto = pd.read_csv('Auto.data',
                            na_values=['?'],
                            delim_whitespace=True)
         Auto['horsepower'].sum()
Out[77]: 40952.0
```

The `Auto.shape` attribute tells us that the data has 397 observations, or rows, and nine variables, or columns. 

함수 배열 변수의 `Auto.shape` 단락 속성값 데이터 수치를 전격 검열 결합 조달 단독 살펴보면, 체제 해당 확보 표본 배열 데이터 체계가 총 단위 수량으로 단면 적재 도단 397개의 관측치 즉 모단 데이터 세트 행(rows) 묶음 덩어리를 보유 수결 품고 조달 담겨 있으며, 그와 더불어 9개 조달 분량 파편 단위의 각 조사 통제 변숫 기준 분류별 체제 기준항인 9개 단위 시스템 열(columns) 단편 구역 조단 구조를 모의 전개 체계적으로 갖췄다는 도출 단면 사실을 우리에게 단독 명백히 단박 파악 단면 조달 진입 알려 모의 수단 조절 모조리 줍니다.

```python
In [78]: Auto.shape
Out[78]: (397, 9)
```

There are various ways to deal with missing data. In this case, since only five of the rows contain missing observations, we choose to use the `Auto.dropna()` method to simply remove these rows. 

초기 분석 수단 관측 척도 배열들 체제에서 결단 중간중간 이가 빠진 구멍이 숭숭 누락 구동 결측 적재된 빈 분절 데이터 단면 조각들을 시스템 내부적으로 직접 처리 보수하는 데에는 조사 사실 정말이지 산점 수많은 여타 기표 여러 수치적 조치 방법들이 통계 학계 전반에 구조 존재 기표 수립합니다. 하지만 지금 진열 본 단편 실습 전향의 경우에는 조사 배열 내 오직 산출 단 5개의 단편 단위분 데이터 파편 행 덩어리 전개들만이 유일 조단 결측 조수 단면된 결여 부분 조달 관측 조달치를 모의 내포 수반 포함 단면하고 조율 간직 있을 시스템 뿐이므로, 우리는 척도 단독 단지 구조 편리 조단 실용적인 수단 구별의 함수 지표 방식 단위인 함수 구문 `Auto.dropna()` 통제 메서드를 즉시 호출 진출 사용해 단편 문제가 단독 된 도별 해당 분절 빈 단 조달 데이터 산출 행렬 영역 체제가 엮인 구역 열차 모의 단독 선형 전체 단편을 단숨 일괄에 일거 진입 삭제 척도 폐기 제어 제거 타격해 통상 버리는 구식 단조 조작 실용 방안 지표을 속 시원히 단독 선택 조단 기표 단단 수립 모의 결합했습니다.

```python
In [79]: Auto_new = Auto.dropna()
         Auto_new.shape
Out[79]: (392, 9)
```

## Basics of Selecting Rows and Columns 
## 행과 열 선택의 기초

We can use `Auto.columns` to check the variable names. 

우리는 변수명 구역 열에 단독 구문 조달 `Auto.columns` 형태 구문을 진단 단면 사용하여 현재 배정 도달 단면 체결 설정 구조된 표식 열의 전용 분류 구분 변수 조단 표면 이름명 기표 값들을 각각 기재 조회 확인 조달 판별할 수 조사 단편 있습니다.

```python
In [80]: Auto = Auto_new # overwrite the previous value
         Auto.columns
Out[80]: Index(['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'year', 'origin', 'name'],
               dtype='object')
```

Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array. Recall that the first argument to the `[]` method is always applied to the rows of the array. Similarly, passing in a slice to the `[]` method creates a data frame whose _rows_ are determined by the slice: 

통계 조달 기표 데이터 포도 프레임 전용 구조 체제 객체가 지닌 단면 분류 행 전개 및 공간 구역 단면 기표 분류 열 구조 공간 자체 내부 구역 단락에 각각 조달 찾아가 구동 접근 체결하는 통제 기표 처리 조작 방식 기법은 단면 기조상 일반 전형 단순 기표 배열 수단 형태 척도 요소의 조장 행 기표와 단독 단위 열 파편 구역에 단독 각각 부분 분할 체결 접근 분절하는 구조 체계 전개 시스템 구동 도출 조달 방식 단면 체계 구조와 표면상 느낌이 수립 여러모로 단독 무척 단정 진단 조조 비슷 기표 하긴 기만 하지만, 구조 도출 모의 단결 결론 분석적으로 진입 단면 결코 모단 표면 완전 모조리 확실히 다 완전히 동일 조단 똑같 조제 하지는 단편 모독 단지 않습니다. 우선 조단 앞단 진입 서두에서 앞서 우리가 초기 인덱스 특정 대괄호 배열 탐색 단면 구조 `[]` 수동 모의 조작 지시 조달 기표 검색 메서드 구동 통과 시스템에 모단 구단 전달 도단 단전 조달 결단했던 인자 구동 인수 중, 구조상 단편 늘 항상 분분 가장 단독 첫 조달 모의 입력 조단 단편 진입 인자 구역 수리 인수가 늘 어김없이 항상 파편적 내부 단편 모단 배열 모의 시스템 기표 구조의 조단 특정 단절 행 모단 지표 단위 기표 산전 구역 분별 영역 단면 도달상에 늘 맨 우선 결부 적용 전격 수립 단절 파생 진단되었던 기저 모의 기조 점을 단편 조달 부수 단연 상기 모단 지표 단전 시켜 다시 도달 되뇌어 구조 단면 상기 파단 모의 단번 통제 해 단면 보십시오. 단절 이 동작 원리 기조 시스템과 내부 단독 대단 조단 매우 유사 도단 동형 단조 흡사 구단 구조하게, 당 데이터 조단 단결 프레임 단수 통제 객체 기조 체제 시스템상에서도 수리 이 인덱스 특정 대괄호 탐색 모의 `[]` 요소 단결 방식 조단 조달 지시 구역 모의 탐색 메서드 조단 시스템 구동 체제상 구동 단편 모의 투입 파편화 시스템 조건 지표 슬라이스 표단 단면 수단 구단 도출 구역 도달 수식 단수 통치 장치 부단 수단 조치 요건 시스템을 구단 방식 결단 투입 단면 조단 단단 전달 지정 통제 배분 분단 구동 해 조달 구조 단면 표면 주면 조달, 모의 해당 투입 기표 조건 슬라이스 지표 수단 수동 구동 수치 조건 분절 기조 통제 단락 결과 지정 조건 단절 속성에 의해 시스템 도출 모의 그 결과 기표상 인출 단편 한정 단결 _행(rows)_ 지표 개별 수리 모조 특성 기표 도단 요소 수치 기조가 모의 통단 조단 모구 단조 단편 단면 재구성 단전 모단 개조 단절 파생 통제 단면 도출 단단 재편 편결 모단 기점 구조 수조 결정 조달 분편 수립 통단 구축 파생 전단 변형 모의 구조 생성 단면 조단 발동 전단 진단 조달 분출 도달 도출 전단 파생 모의 전개 발동 진열 발산 조단 되어, 결국 조달 즉 전혀 도출 단절 또 조단 파단 다른 단조 특정 구조 구역 단순 진기 단연 신생 모단 조달 전격 새로운 분단 파단 단편 전방 단락 통제 분파 지표 지단 개조 별도 단조 부분 특수 조달 모의 단조 데이터 부분 프레임 단전 모단 단편 개별 지정 조기 부분 객체 체제 모단 전편 조달 분파가 부합 조단 모의 표면 조단 조달 파생 도달 기변 개편 파동 생산 구조 전개 기동 구조 창조 모단 창출 지동 단면 반환 조달 도출 표단 분수 됩니다:

```python
In [81]: Auto[:3]
```

|**`Out[81]:`**||`mpg`|`cylinders`|`displacement`|`horsepower`|`weight`|`...`|
|---|---|---|---|---|---|---|---|
||`0`|`18.0`|`8`|`307.0`|`130.0`|`3504.0`|`...`|
||`1`|`15.0`|`8`|`350.0`|`165.0`|`3693.0`|`...`|
||`2`|`18.0`|`8`|`318.0`|`150.0`|`3436.0`|`...`|

Similarly, an array of Booleans can be used to subset the rows: 

그와 흡사한 방향 원리로, 완전 순수 논리적 속성인 참거짓 판단 배열 구조인 특정 논리값 제어 체계 지표 논리 단편 배당 요인 기표 계열(Booleans) 수단을 산술 투과 지정 이용 통제해도 조달 여전히 배열 중 행 조건 특정 단구 영역 조달 구분 구별 기조 구조 범위만을 조달 따로 한정 표면 모단 도출 타깃 필터 파단 모의 기단 단독 조단 분리 고립해 개조 부분 단수 지표 맞춤 단편 분파 전적 데이터 조단 지정 통제 배열 파견 수치 단결 덩어리 전단 단편으로 조단 별도 뽑아 파편 도달 전격 단면 추출 파생 모의 단전 할 분산 단결 수 단면 시스템이 조달 마련 구비 도출됩니다:

```python
In [82]: idx_80 = Auto['year'] > 80
         Auto[idx_80]
```

However, if we pass in a list of strings to the `[]` method, then we obtain a data frame containing the corresponding set of _columns_ . 

조달 이러한 동작 통제 구동 기조 모의 판별 구조와 기단 완벽 전적 반대 단편 역설 대치 모단 기표되게 모의 지정, 만약 단독 우리가 요소 타깃 지표 탐색 파악 단결 통제 탐지 조치로써 모수 통과 기능 대괄호 구문 `[]` 지정 수조 탐색 메서드 동작 구조 기표 체제 공간 모의 통제 지정 내부 기표 도달상에 조달 시스템 단면 일반 구단 형태 기단 텍스트 단편 모조 조단 문자열 조건 지정 기표 파단 단위 집단 모의인 산단 특정 배열 문자열 단독 척건 부수 집단 체단 계열 조달 지표 변수 조건 체계 수단인 단위 지시 문자열 구동 텍스트 리스트(list of strings) 구조 기표 지표 단면 객체 변수 등을 단위 조달 구단 기구 단편 전달 파달 기점 모의 호출 단편 할당 파악 기단 모의 기표 도달 지정해 주게 기조 모단 된다면, 시스템 조달 속성 결과 조달 통제 결과 도출 부수 조달 결괏값 출력 단면 현상 기표 도출 부수 결과 단단 기조로 산출 조단 우리는 단면 오롯 기단 조수 기표 오직 오로지 그 기표 타격 구단 지정 기표 특정 텍스트 변수 지표 이름 전수 체제 명칭 모의단과 모조 기동 조수 정식 구별 구분 지표 지시 명칭 단면 모조 표단 타이틀 매치 단전 부합 매칭 진단 기표 단단 합치 조단 전격 대응 단편 기전 일치 조율되는 단단 특정 항목 체제 모의 단위의 조속 구단 지정 기표 조달 단락 분별 특정 구단 _조달 열(columns)_ 세트 모의 수열 집단 단수 속성 조단 통제 기조 체계 파단 항목 기구 고유 타격 부분 단조 배열 집합 기구 단단 단위 계열 묶음 세트 부수 파단 체제만을 오직 조달 단단 결절 온전히 모의 시스템 전단 표면 지표 기안 획득 조단 표단 기단 기표 단수 도출 조달 달성해 도출 획득 파생 조달 기조 모단 얻게 모의 수단 산출 모조 됩니다.

```python
In [83]: Auto[['mpg', 'horsepower']]
Out[83]:       mpg  horsepower
         0    18.0       130.0
         1    15.0       165.0
         2    18.0       150.0
         3    16.0       150.0
         4    17.0       140.0
         ..    ...         ...
         392  27.0        86.0
         393  44.0        52.0
         394  32.0        84.0
         395  28.0        79.0
         396  31.0        82.0
         
         [392 rows x 2 columns]
```

Since we did not specify an _index_ column when we loaded our data frame, the rows are labeled using integers 0 to 396.

우리가 앞서 데이터 프레임을 처음 불러올 때 어떠한 특정 _인덱스(index)_ 열을 따로 지정하지 않았으므로, 각 행들은 기본적으로 0부터 396까지의 정수들을 사용하여 자동으로 식별 라벨이 부여됩니다.

```python
In [84]: Auto.index
Out[84]: Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
                     ...
                     387, 388, 389, 390, 391, 392, 393, 394, 395, 396],
                    dtype='int64', length=392)
```

We can use the `set_index()` method to re-name the rows using the contents of `Auto['name']`.

우리는 `set_index()` 메서드를 사용하여 기존 번호 대신 `Auto['name']` 열에 담긴 데이터 내용물들을 바탕으로 각 행들의 이름을 새롭게 일괄 재지정해 변경할 수 있습니다.

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

```python
In [86]: Auto_re.columns
Out[86]: Index(['mpg', 'cylinders', 'displacement', 'horsepower',
                'weight', 'acceleration', 'year', 'origin'],
               dtype='object')
```

We see that the column `'name'` is no longer there.

출력 결과를 보면, 이전과는 달리 속성 목록에서 `'name'` 이라는 열 이름이 더 이상 존재하지 않음을 명확히 확인할 수 있습니다.

Now that the index has been set to `name`, we can access rows of the data frame by `name` using the `loc[]` method of `Auto`:

이제 행 인덱스가 공식적으로 문자인 자동차 `name` 으로 설정 변경되었으므로, 우리는 `Auto` 테이블의 내부 제공 `loc[]` 메서드를 활용하여 각 데이터 세트 프레임의 행들을 문자 `name` 을 통해 직접 호출하고 탐색 접근할 수 있습니다:

```python
In [87]: rows = ['amc rebel sst', 'ford torino']
         Auto_re.loc[rows]
Out[87]:                mpg  cylinders  displacement  horsepower  ...
         name                                                     ...
         amc rebel sst  16.0          8         304.0       150.0  ...
         ford torino    17.0          8         302.0       140.0  ...
```

As an alternative to using the index name, we could retrieve the 4th and 5th rows of `Auto` using the `iloc[]` method:

인덱스 이름 문자열을 직접 사용하는 방식 대신에, 우리가 제공하는 기본 `iloc[]` 메서드를 사용하면 예전처럼 단순히 숫자 순번을 사용해 `Auto` 의 특정 4번째와 5번째 행 요소를 간편하게 추출해 가져올 수도 있습니다:

```python
In [88]: Auto_re.iloc[[3, 4]]
```

We can also use it to retrieve the 1st, 3rd and and 4th columns of `Auto_re`:

동일한 이 수단을 활용해, 우리는 `Auto_re` 의 1번째, 3번째, 그리고 4번째 열 정보에 해당하는 구역들을 특정하여 별도로 조회해 가져올 수도 있습니다:

```python
In [89]: Auto_re.iloc[:, [0, 2, 3]]
```

We can extract the 4th and 5th rows, as well as the 1st, 3rd and 4th columns, using a single call to `iloc[]`:

`iloc[]` 함수를 단 한 번만 복합적으로 호출함으로써, 앞선 검색을 융합해 4번째 및 5번째 행 데이터와 동시에 열 데이터상으로는 1번째, 3번째, 4번째가 교차 대응하는 부분만을 한 번에 추출하는 것도 가능합니다:

```python
In [90]: Auto_re.iloc[[3, 4], [0, 2, 3]]
Out[90]:                mpg  displacement  horsepower
         name                                        
         amc rebel sst  16.0         304.0       150.0
         ford torino    17.0         302.0       140.0
```

Index entries need not be unique: there are several cars in the data frame named `ford galaxie 500`.

참고로 할당된 행 인덱스 항목이 매번 반드시 고유할 필요는 결코 없습니다: 예컨대 본 데이터 프레임 내에는 서로 다른 데이터임에도 우연히 똑같이 `ford galaxie 500` 이라 동명으로 명명된 차량 항목이 여러 개 존재합니다.

```python
In [91]: Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]
Out[91]:                    mpg  origin
         name                          
         ford galaxie 500  15.0       1
         ford galaxie 500  14.0       1
         ford galaxie 500  14.0       1
```

### More on Selecting Rows and Columns
### 행과 열 선택에 대한 심화 속성

Suppose now that we want to create a data frame consisting of the `weight` and `origin` of the subset of cars with `year` greater than 80 — i.e. those built after 1980. To do this, we first create a Boolean array that indexes the rows. The `loc[]` method allows for Boolean entries as well as strings:

이제 여기서 더 나아가 `year` 지표가 80을 넘는 — 즉 1980년도 이후에 생산 제작된 특정 하위 자동차 모음 집합들을 대상으로, 오직 해당 차량들의 `weight` 와 `origin` 항목 정보만으로 새롭게 구성된 데이터 프레임을 지정 생성하고 싶다고 가정해 봅시다. 이 복합 목적을 달성하기 위해, 우린 가장 먼저 해당 특정 조건의 행들을 모두 색인하는 하나의 논리적 배열(Boolean array)부터 새로 만듭니다. 이 과정에 쓰일 `loc[]` 표기 메서드는 문자열 값뿐만 아니라 이러한 논리형 참거짓 항목 배열 자체도 인수로 원활히 허용해 처리합니다:

```python
In [92]: idx_80 = Auto_re['year'] > 80
         Auto_re.loc[idx_80, ['weight', 'origin']]
```

To do this more concisely, we can use an anonymous function called a `lambda`:

동일한 이 조작을 훨씬 더 짧고 간결하게 한 줄로 압축해 수행하려면, 보통 `lambda` 라 일컫는 익명 함수(anonymous function) 구문을 대신 사용할 수 있습니다:

```python
In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]
```

The `lambda` call creates a function that takes a single argument, here `df`, and returns `df['year'] > 80`. Since it is created inside the `loc[]` method for the dataframe `Auto_re`, that dataframe will be the argument supplied. As another example of using a `lambda`, suppose that we want all cars built after 1980 that achieve greater than 30 miles per gallon:

`lambda` 호출은 오직 단일 인수만을 취하는 축소 함수를 내부에 즉석 생성해 내며, 이 예제 코드의 경우 인수 이름은 `df` 이고 반환 도출 수식은 `df['year'] > 80` 으로 정해집니다. 이 축소 코드가 데이터 프레임 `Auto_re` 에 귀속된 `loc[]` 메서드 속에서 선언 생성되었으므로, 해당 데이터 프레임 자체가 이 익명 함수의 기본 매개 변수로 자동 공급될 것입니다. `lambda` 를 응용하는 또 다른 조건 예시로서, 만약 우리가 제작 연도가 1980년 이후이면서 동시에 주행 갤런당 마일 연비가 30을 능가해 초과하는 모든 자동차들을 다 찾길 원할 때를 가정해 봅시다:

```python
In [94]: Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30),
                     ['weight', 'origin']
                    ]
```

The symbol `&` computes an element-wise _and_ operation. As another example, suppose that we want to retrieve all `Ford` and `Datsun` cars with `displacement` less than 300. We check whether each `name` entry contains either the string `ford` or `datsun` using the `str.contains()` method of the `index` attribute of the dataframe:

내부 기호 수식 `&` 는 배열 내 요소 대 요소 단위의 _그리고(and)_ 교집합 논리 연산을 계산합니다. 이번에는 또 다른 종류의 검색 예시로서, 만일 자동차 변위량 치수인 `displacement` 숫자가 300에 현저히 못 미치는 모든 `Ford` 사 차량과 `Datsun` 모델 차량들만을 선별해 회수하고 싶다 상상해 봅시다. 우리는 데이터 프레임의 고유 `index` 객체 속성에 부수된 일종의 보조 탐색 메서드 `str.contains()` 수단을 차용 이용함으로써 각 문자열 `name` 기재 항목 내에 실제로 특정 텍스트 `ford` 혹은 `datsun` 모델 글자가 개별 포함되어 있는지 여부를 탐색 점검합니다:

```python
In [95]: Auto_re.loc[lambda df: (df['displacement'] < 300)
                                & (df.index.str.contains('ford')
                                   | df.index.str.contains('datsun')),
                     ['weight', 'origin']
                    ]
```

Here, the symbol `|` computes an element-wise _or_ operation.

여기서 가운데 위치한 기호 수식 `|` 연산자는 요소별 논리를 뜻하는 분할 합집합 _또는(or)_ 논리 비교 연산을 수행합니다.

In summary, a powerful set of operations is available to index the rows and columns of data frames. For integer based queries, use the `iloc[]` method. For string and Boolean selections, use the `loc[]` method. For functional queries that filter rows, use the `loc[]` method with a function (typically a `lambda`) in the rows argument.

결론적으로 핵심을 요약하자면, 파이썬에는 거대한 데이터 프레임의 수많은 행과 열들을 체계적으로 인덱싱해 추출할 수 있는 매우 다양하고 확고하며 강력한 각종 연산 조합 세트들이 빈번히 활용 가능하게 항상 준비되어 있습니다. 순수 정수 번호를 바탕 기반으로 데이터를 추출 탐색할 땐 `iloc[]` 메서드 구문을 호출 활용하십시오. 반면 고유 문자열 표기 기호나 논리값 체제로 판단할 땐 전용 메서드인 `loc[]` 항목을 쓰십시오. 행 대상을 복잡한 필터 조건으로 판별할 기능성 질의를 수행하려면 통상적으로 메서드 인수에 `lambda` 와 같은 별도의 축약 함수를 조건 첨부한 `loc[]` 를 쓰면 됩니다.

---

## Sub-Chapters (하위 목차)

현재 2.3.7 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)

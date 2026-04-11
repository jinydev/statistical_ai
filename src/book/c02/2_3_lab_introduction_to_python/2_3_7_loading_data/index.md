---
layout: default
title: "index"
---

# _2.3.7 Loading Data_

# _2.3.7 데이터 불러오기_

Data sets often contain different types of data, and may have names associated with the rows or columns.

데이터 세트들은 종종 상이한 유형들의 데이터를 포함하며, 행들 혹은 열들에 연관된 이름들을 가질 수 있습니다.

For these reasons, they typically are best accommodated using a _data frame_.

이러한 이유들로, 그것들은 전형적으로 하나의 _데이터 프레임(data frame)_ 을 사용하여 가장 잘 수용됩니다.

We can think of a data frame as a sequence of arrays of identical length; these are the columns.

우리는 하나의 데이터 프레임을 동일한 길이의 배열들의 시퀀스로서 생각할 수 있습니다; 이것들이 열들입니다.

Entries in the different arrays can be combined to form a row.

상이한 배열들 안의 항목들은 하나의 행을 형성하기 위해 결합될 수 있습니다.

The `pandas` library can be used to create and work with data frame objects.

`pandas` 라이브러리는 데이터 프레임 객체들을 생성하고 함께 작업하기 위해 사용될 수 있습니다.

## Reading in a Data Set

## 데이터 세트 읽어 들이기

The first step of most analyses involves importing a data set into `Python`.

대부분의 분석들의 첫 번째 단계는 데이터 세트를 `Python` 안으로 임포트(importing)하는 것을 수반합니다.

Before attempting to load a data set, we must make sure that `Python` knows where to find the file containing it.

데이터 세트를 적재(load)하기를 시도하기 전에, 우리는 `Python` 이 그것을 포함하는 파일을 어디서 찾아야 할지 알고 있음을 확인해야만 합니다.

If the file is in the same location as this notebook file, then we are all set.

만약 그 파일이 이 노트북 파일과 동일한 위치에 있다면, 준비 완료된 것입니다.

Otherwise, the command `os.chdir()` can be used to _change directory_. (You will need to call `import os` before calling `os.chdir()`.)

그렇지 않다면, 디렉터리를 변경하기(change directory) 위해 `os.chdir()` 명령이 사용될 수 있습니다. (`os.chdir()` 을 호출하기 전에 `import os` 를 호출할 필요가 있을 것입니다.)

We will begin by reading in `Auto.csv`, available on the book website.

우리는 책 웹사이트에서 이용 가능한 `Auto.csv` 를 읽어 들임으로써 시작할 것입니다.

This is a comma-separated file, and can be read in using `pd.read_csv()`:

이것은 쉼표로-구분된(comma-separated) 파일이며, `pd.read_csv()` 를 사용하여 읽어 들여질 수 있습니다:

```python
In [73]: import pandas as pd
         Auto = pd.read_csv('Auto.csv')
         Auto
```

The book website also has a whitespace-delimited version of this data, called `Auto.data`.

그 책 웹사이트는 또한 `Auto.data` 라고 불리는, 이 데이터의 여백으로-구분된(whitespace-delimited) 버전을 가지고 있습니다.

This can be read in as follows:

이것은 다음과 같이 읽어 들여질 수 있습니다:

```python
In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
```

Both `Auto.csv` and `Auto.data` are simply text files.

`Auto.csv` 와 `Auto.data` 둘 모두 단순히 텍스트 파일들입니다.

Before loading data into `Python`, it is a good idea to view it using a text editor or other software, such as Microsoft Excel.

데이터를 `Python` 안으로 가져오기 이전에, 마이크로소프트 엑셀과 같은 텍스트 편집기나 다른 소프트웨어를 사용하여 그것을 보는 것은 좋은 생각입니다.

We now take a look at the column of `Auto` corresponding to the variable `horsepower`:

우리는 이제 `horsepower` 변수에 대응하는 `Auto` 의 열을 한 번 살펴봅니다:

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

우리는 이 열의 `dtype` 이 `object` 임을 봅니다.

It turns out that all values of the `horsepower` column were interpreted as strings when reading in the data.

데이터를 읽어 들일 때 `horsepower` 열의 모든 값들이 문자열들로서 해석된 것으로 판명됩니다.

We can find out why by looking at the unique values.

우리는 그 고유값(unique values)들을 봄으로써 왜 그런지 알 수 있습니다.

```python
In [76]: np.unique(Auto['horsepower'])
```

To save space, we have omitted the output of the previous code block.

공간을 절약하기 위해, 우리는 이전 코드 블록의 출력을 생략했습니다.

We see the culprit is the value `?`, which is being used to encode missing values.

우리는 그 범인이 `?` 값이라는 것을 보며, 이것은 결측치(missing values)를 인코드(encode)하기 위하여 사용되고 있습니다.

To fix the problem, we must provide `pd.read_csv()` with an argument called `na_values`.

그 문제를 고치기 위해, 우리는 `pd.read_csv()` 에 `na_values` 라고 불리는 하나의 인자를 제공해야 합니다.

Now, each instance of `?` in the file is replaced with the value `np.nan`, which means _not a number_:

이제, 파일 안의 `?` 의 각 사례는 `np.nan` 값으로 대체되며, 이는 _숫자가 아님(not a number)_ 을 의미합니다:

```
In [77]:Auto=pd.read_csv('Auto.data',
na_values=['?'],
delim_whitespace=True)
Auto['horsepower'].sum()
```

```
Out[77]:40952.0
```

The `Auto.shape` attribute tells us that the data has 397 observations, or rows, and nine variables, or columns.

`Auto.shape` 속성은 데이터가 397 개의 관측치들 즉 행들, 그리고 아홉 개의 변수들 즉 열들을 가지고 있음을 말해 줍니다. 

```
In [78]:Auto.shape
```

```
Out[78]:(397,9)
```

There are various ways to deal with missing data.

결측 데이터를 다루는 다양한 방법들이 있습니다.

In this case, since only five of the rows contain missing observations, we choose to use the `Auto.dropna()` method to simply remove these rows.

이 경우에, 행들 중 오직 다섯 개만이 누락된 관측치들을 포함하고 있기 때문에, 우리는 이 행들을 단순 제거하기 위해 `Auto.dropna()` 메서드를 사용합니다. 

```
.dropna()
```

```
In [79]:Auto_new=Auto.dropna()
Auto_new.shape
```

```
Out[79]:(392,9)
```

## Basics of Selecting Rows and Columns

## 행들과 열들을 선택하기의 기본 지침

We can use `Auto.columns` to check the variable names.

우리는 변수 이름들을 확인하기 위해 `Auto.columns` 를 사용할 수 있습니다. 

```
In [80]:Auto=Auto_new#overwritethepreviousvalue
Auto.columns
```

```
Out[80]:Index(['mpg','cylinders','displacement','horsepower',
'weight','acceleration','year','origin','name'],
dtype='object')
```

Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array.

데이터 프레임의 행들과 열들에 접근하는 것은 배열의 행들과 열들에 접근하는 것과 유사하지만, 동일하지는 않습니다.

Recall that the first argument to the `[]` method is always applied to the rows of the array.

`[]` 메서드에 대한 첫 번째 인자가 항상 그 배열의 행들에 적용됨을 상기하십시오.

Similarly, passing in a slice to the `[]` method creates a data frame whose _rows_ are determined by the slice:

유사하게, `[]` 메서드 속으로 하나의 슬라이스를 전달하는 것은 그것의 _행들_ 이 그 슬라이스에 의하여 결정되어지는 하나의 데이터 프레임을 생성합니다:

```
In [81]:Auto[:3]
```

|**`Out[81]:`**||`mpg`|`cylinders`|`displacement`|`horsepower`|`weight`|`...`|
|---|---|---|---|---|---|---|---|
||`0`|`18.0`|`8`|`307.0`|`130.0`|`3504.0`|`...`|
||`1`|`15.0`|`8`|`350.0`|`165.0`|`3693.0`|`...`|
||`2`|`18.0`|`8`|`318.0`|`150.0`|`3436.0`|`...`|



Similarly, an array of Booleans can be used to subset the rows:

유사하게, 불리언들(Booleans)의 하나의 배열은 행들을 부분집합 (subset) 화 하기 위해 사용될 수 있습니다:

<!-- 2.3 Lab: Introduction to Python 57 --> 

```
In [82]:idx_80=Auto['year']>80
Auto[idx_80]
```

However, if we pass in a list of strings to the `[]` method, then we obtain a data frame containing the corresponding set of _columns_ .

그러나, 만약 우리가 `[]` 메서드에 문자열들의 하나의 리스트를 전달한다면, 그러면 우리는 해당 _열들(columns)_ 의 상응하는 세트를 포함하는 데이터 프레임 하나를 획득합니다. 

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

우리가 우리의 데이터 프레임을 적재했을 때 하나의 _인덱스(index)_ 열을 명시하지 않았으므로, 그 행들은 0에서 396 정수들을 사용하여 라벨(label)되어 있습니다.

```python
In [84]: Auto.index
Out[84]: Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
                     ...
                     387, 388, 389, 390, 391, 392, 393, 394, 395, 396],
                    dtype='int64', length=392)
```

We can use the `set_index()` method to re-name the rows using the contents of `Auto['name']`.

우리는 `Auto['name']` 의 내용들을 사용하여 행들을 다시 이름 짓기 위해 `set_index()` 메서드를 사용할 수 있습니다.

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

우리는 `'name'` 열이 더 이상 그곳에 없음을 봅니다.

Now that the index has been set to `name`, we can access rows of the data frame by `name` using the `loc[]` method of `Auto`:

이제 그 인덱스가 `name` 으로 설정되었으므로, 우리는 `Auto` 의 `loc[]` 메서드를 사용하여 `name` 에 의해 데이터 프레임의 행들에 접근할 수 있습니다:

```
.loc[]
```python
In [87]: rows = ['amc rebel sst', 'ford torino']
         Auto_re.loc[rows]
Out[87]:                mpg  cylinders  displacement  horsepower  ...
         name                                                     ...
         amc rebel sst  16.0          8         304.0       150.0  ...
         ford torino    17.0          8         302.0       140.0  ...
```

As an alternative to using the index name, we could retrieve the 4th and 5th rows of `Auto` using the `iloc[]` method:

해당 인덱스 이름을 사용하는 것에 대한 하나의 대안으로서, 우리는 `iloc[]` 메서드를 사용하여 `Auto` 의 4번째와 5번째 행들을 가져올 수 있습니다:

```python
In [88]: Auto_re.iloc[[3, 4]]
```

We can also use it to retrieve the 1st, 3rd and and 4th columns of `Auto_re`:

우리는 1번째, 3번째 그리고 4번째의 `Auto_re` 의 열들을 가져오기 위해 또한 그것을 사용할 수 있습니다:

```python
In [89]: Auto_re.iloc[:, [0, 2, 3]]
```

We can extract the 4th and 5th rows, as well as the 1st, 3rd and 4th columns, using a single call to `iloc[]`:

우리는 `iloc[]` 에 대한 단일 호출을 사용하여 1번째, 3번째 및 4번째 열들은 물론 4번째와 5번째 행들을 추출할 수 있습니다:

```python
In [90]: Auto_re.iloc[[3, 4], [0, 2, 3]]
Out[90]:                mpg  displacement  horsepower
         name                                        
         amc rebel sst  16.0         304.0       150.0
         ford torino    17.0         302.0       140.0
```

Index entries need not be unique: there are several cars in the data frame named `ford galaxie 500`.

인덱스 항목들은 유일 무이할 필요가 없습니다: 해당 데이터 프레임 안에는 `ford galaxie 500` 이라고 이름 지어진 여러 차들이 있습니다.

```python
In [91]: Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]
Out[91]:                    mpg  origin
         name                          
         ford galaxie 500  15.0       1
         ford galaxie 500  14.0       1
         ford galaxie 500  14.0       1
```

### More on Selecting Rows and Columns

### 행들과 열들을 선택하기에 대한 더 많은 사항들

Suppose now that we want to create a data frame consisting of the `weight` and `origin` of the subset of cars with `year` greater than 80 — i.e. those built after 1980.

이제 우리가 80보다 큰 `year` 를 가진 차들의 부분집합 — 즉 1980년 이후에 만들어진 것들 —의 `weight` 와 `origin` 으로 구성된 데이터 프레임 하나를 생성하기 원한다고 가정해 봅시다.

To do this, we first create a Boolean array that indexes the rows.

이것을 행하기 위해, 우리는 우선 행들을 인덱스하는 불리언 배열 하나를 생성합니다.

The `loc[]` method allows for Boolean entries as well as strings:

`loc[]` 메서드는 문자열들뿐만 아니라 불리언 항목들도 허용합니다:

```python
In [92]: idx_80 = Auto_re['year'] > 80
         Auto_re.loc[idx_80, ['weight', 'origin']]
```

To do this more concisely, we can use an anonymous function called a `lambda`:

이것을 더 간결하게 행하기 위해, 우리는 `lambda` 라고 불리는 익명 함수(anonymous function)를 사용할 수 있습니다:

```python
In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]
```

The `lambda` call creates a function that takes a single argument, here `df`, and returns `df['year'] > 80`.

`lambda` 호출은 단일 인수, 여기서는 `df` 를 취하고, `df['year'] > 80` 을 반환하는 함수 하나를 생성합니다.

Since it is created inside the `loc[]` method for the dataframe `Auto_re`, that dataframe will be the argument supplied.

그것은 `Auto_re` 데이터프레임을 위한 `loc[]` 메서드 안에서 생성되기 때문에, 그 데이터프레임이 제공되는 인수가 될 것입니다.

As another example of using a `lambda`, suppose that we want all cars built after 1980 that achieve greater than 30 miles per gallon:

`lambda` 를 사용하는 또 다른 예제로서, 우리가 갤런 당 30 마일보다 큰 것을 달성하는 1980년 이후에 만들어진 모든 차들을 원한다고 가정해 봅시다:

```python
In [94]: Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30),
                     ['weight', 'origin']
                    ]
```

The symbol `&` computes an element-wise _and_ operation.

기호 `&` 은 요소별(element-wise) _and_ 연산을 계산합니다.

As another example, suppose that we want to retrieve all `Ford` and `Datsun` cars with `displacement` less than 300.

또 다른 예제로서, 우리가 300 보다 적은 `displacement` 를 가진 모든 `Ford` 와 `Datsun` 차들을 반환받기를 원한다고 가정해 봅시다.

We check whether each `name` entry contains either the string `ford` or `datsun` using the `str.contains()` method of the `index` attribute of the dataframe:

우리는 데이터프레임의 `index` 속성의 `str.contains()` 메서드를 사용하여 각 `name` 항목이 문자열 `ford` 또는 `datsun` 을 포함하는지 여부를 확인합니다:

```python
In [95]: Auto_re.loc[lambda df: (df['displacement'] < 300)
                                & (df.index.str.contains('ford')
                                   | df.index.str.contains('datsun')),
                     ['weight', 'origin']
                    ]
```

Here, the symbol `|` computes an element-wise _or_ operation.

여기서, `|` 기호는 요소별(element-wise) _or_ 연산을 계산합니다.

In summary, a powerful set of operations is available to index the rows and columns of data frames.

요약하자면, 데이터 프레임들의 행들과 열들을 인덱스하기 위한 강력한 연산들의 세트가 이용 가능합니다.

For integer based queries, use the `iloc[]` method.

정수 기반 질의들에는, `iloc[]` 메서드를 사용하십시오.

For string and Boolean selections, use the `loc[]` method.

문자열 및 불리언 선택들에는, `loc[]` 메서드를 사용하십시오.

For functional queries that filter rows, use the `loc[]` method with a function (typically a `lambda`) in the rows argument.

행들을 필터하는 함수적 질의들에는, 행들 인수 안에 하나의 함수(전형적으로 하나의 `lambda`)와 함께 `loc[]` 메서드를 사용하십시오.

---
layout: default
title: "trans1"
---

[< 2.3.2 Basic Commands](../2_3_2_basic_commands/trans1.html) | [2.3.4 Graphics >](../2_3_4_graphics/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.3.3 Introduction to Numerical Python

# 2.3.3 수치적 파이썬 소개

As mentioned earlier, this book makes use of functionality that is contained in the `numpy` _library_, or _package_.

일찍이 앞서 언급되었듯, 이 책은 `numpy` _라이브러리(library)_, 또는 _패키지(package)_ 안에 포함된 기능성을 사용합니다.

A package is a collection of modules that are not necessarily included in the base `Python` distribution.

패키지란 기본 `Python` 배포본에 반드시 포함되지는 않는 모듈들의 모음입니다.

The name `numpy` is an abbreviation for _numerical Python_.

`numpy`라는 이름은 _수치적 파이썬(numerical Python)_ 의 줄임말입니다.

To access `numpy`, we must first `import` it.

`numpy`에 접근하기 위해, 우리는 반드시 먼저 그것을 `import` 해야 합니다.

```python
In [7]: import numpy as np
```

In the previous line, we named the `numpy` _module_ `np`; an abbreviation for easier referencing.

이전 줄에서, 우리는 `numpy` _모듈_ 을 `np`라 명명했습니다; 이것은 더 쉬운 참조를 위한 하나의 역어입니다.

In `numpy`, an _array_ is a generic term for a multidimensional set of numbers.

`numpy`에서, _배열(array)_ 이란 수들의 다차원적인 집합을 위한 통칭적인 용어입니다.

We use the `np.array()` function to define `x` and `y`, which are one-dimensional arrays, i.e. vectors.

우리는 일-차원 배열들 즉 벡터들인 `x` 와 `y` 를 정의하기 위하여 `np.array()` 함수를 사용합니다.

```python
In [8]: x = np.array([3, 4, 5])
        y = np.array([4, 9, 7])
```

Note that if you forgot to run the `import numpy as np` command earlier, then you will encounter an error in calling the `np.array()` function in the previous line.

만약 당신이 앞서 `import numpy as np` 명령을 실행하는 것을 잊었다면, 당신은 이전 줄에서 `np.array()` 함수를 호출하는 데에서 에러를 마주할 것임에 유의하십시오.

The syntax `np.array()` indicates that the function being called is part of the `numpy` package, which we have abbreviated as `np`.

구문 `np.array()` 는 호출되는 함수가 `numpy` 패키지의 일부임을 지시하며, 우리는 이것을 `np`로 약칭했습니다.

Since `x` and `y` have been defined using `np.array()`, we get a sensible result when we add them together.

`x` 와 `y` 가 `np.array()` 를 사용하여 정의되어졌기 때문에, 우리는 그것들을 서로 더할 때 어떤 합리적인 결과를 얻습니다.

Compare this to our results in the previous section, when we tried to add two lists without using `numpy`.

우리가 `numpy`를 사용하지 않고 두 개의 리스트들을 더하려고 시도했던 직전 섹션에서의 우리의 결과들과 이것을 비교하십시오.

```python
In [9]: x + y
Out[9]: array([ 7, 13, 12])
```

In `numpy`, matrices are typically represented as two-dimensional arrays, and vectors as one-dimensional arrays.[1]

`numpy`에서, 행렬들은 전형적으로 2-차원 배열들로서, 그리고 벡터들은 1-차원 배열들로서 대표하여 나타내어집니다.[1]

We can create a two-dimensional array as follows.

우리는 다음과 같이 2-차원 배열을 생성할 수 있습니다.

```python
In [10]: x = np.array([[1, 2], [3, 4]])
         x
Out[10]: array([[1, 2],
                [3, 4]])
```

The object `x` has several _attributes_, or associated objects.

객체 `x`는 여러 개의 _속성들(attributes)_, 즉 연관된 객체들을 가집니다.

To access an attribute of `x`, we type `x.attribute`, where we replace `attribute` with the name of the attribute.

`x`의 한 속성에 접근하기 위해 우리는 `x.attribute`를 타이핑하며, 이곳에서 우리는 `attribute`를 당해 속성의 이름으로 대체합니다.

For instance, we can access the `ndim` attribute of `x` as follows.

예를 들어, 우리는 다음과 같이 `x`의 `ndim` 속성에 접근할 수 있습니다.

```python
In [11]: x.ndim
Out[11]: 2
```

The output indicates that `x` is a two-dimensional array.

그 출력은 `x`가 2-차원 배열이라는 것을 지시합니다.

Similarly, `x.dtype` is the _data type_ attribute of the object `x`.

유사하게, `x.dtype` 은 그 객체 `x` 안의 _데이터 타입(data type)_ 속성입니다.

This indicates that `x` is comprised of 64-bit integers:

이것은 `x` 가 64-비트 정수들로 구성됨을 나타냅니다:

> 1 While it is also possible to create matrices using `np.matrix()`, we will use `np.array()` throughout the labs in this book.

>

> 1 `np.matrix()` 를 사용하여 행렬들을 생성하는 것 또한 가능하지만, 우리는 이 책의 실습들 전반에 걸쳐 `np.array()` 를 내내 사용할 것입니다.

```python
In [12]: x.dtype
Out[12]: dtype('int64')
```

Why is `x` comprised of integers?

왜 `x` 가 정수들로 구성되어집니까?

This is because we created `x` by passing in exclusively integers to the `np.array()` function.

이것은 우리가 오로지 정수들만을 `np.array()` 함수로 전달함으로써 `x` 를 생성했기 때문입니다.

If we had passed in any decimals, then we would have obtained an array of _floating point numbers_ (i.e. real-valued numbers).

만약 우리가 어떤 범위 소수들을 패스 넘겨 전달했었더라면, 그러면 우리는 _부동 소수점 수치 숫자들(floating point numbers)_ (즉 순전히 실수-할당 값 숫자들)의 하나 배열 구조를 온당 획득했을 터일 것입니다.

```python
In [13]: np.array([[1, 2], [3.0, 4]]).dtype
Out[13]: dtype('float64')
```

Typing `fun?` will cause `Python` to display documentation associated with the function `fun`, if it exists.

`fun?` 구문을 타이핑하는 것은 만약 당 기능 함수가 존재한다면 `Python` 자체로 하여금 그 함수 구조 `fun` 과 긴밀히 연관된 제반 문서를 전시 표시하게 일조 만들 것입니다.

We can try this for `np.array()`.

우리는 이것을 `np.array()` 에 대해 단연 시도할 수 있습니다.

```python
In [14]: np.array?
```

This documentation indicates that we could create a floating point array by passing a `dtype` argument into `np.array()`.

이 지명 문서는 우리가 단일 하나의 `dtype` 인수를 구성 함수 `np.array()` 안쪽 지배로 전달을 넘김으로써 하나의 부동 소수점 수치 배열을 생성할 위치 수도 있었음을 가리켜 나타냅니다.

```python
In [15]: np.array([[1, 2], [3, 4]], float).dtype
Out[15]: dtype('float64')
```

The array `x` is two-dimensional.

배열된 `x` 는 2-차원적입니다.

We can find out the number of rows and columns by looking at its `shape` attribute.

우리는 그것 배열의 `shape` 지정 속성 단락을 단방 바라 살펴봄으로써 당 지배 행들과 내부 열들의 개수 체계를 속속히 알아내 확인해 발견 할 척결 수 있습니다.

```python
In [16]: x.shape
Out[16]: (2, 2)
```

A _method_ is a function that is associated with an object.

하나의 _메서드(method)_ 구조란 하나의 단체 객체에 긴박하게 종속되어 연관된 일종의 함수 구성 단위 부락입니다.

For instance, given an array `x`, the expression `x.sum()` sums all of its elements, using the `sum()` method for arrays.

예시를 가량 들어 보아 배열 `x` 가 주어질 때 당 발현 표현식인 `x.sum()` 은, 곧 배열 단원들을 위한 제반 `sum()` 메서드를 십분 전격 차용 사용하여, 그것 내부의 모든 각기 단편 요소들을 한 번에 합연산 더합니다.

The call `x.sum()` automatically provides `x` as the first argument to its `sum()` method.

그 호출 `x.sum()` 구호는 자동으로 그것 단위의 고유 `sum()` 메서드를 향하는 제일선 그 첫 번째 기저 인수로써 단연 `x`를 수반해 투척 제공합니다.

```python
In [17]: x = np.array([1, 2, 3, 4])
         x.sum()
Out[17]: 10
```

We could also sum the elements of `x` by passing in `x` as an argument to the `np.sum()` function.

우리는 또한 저 함수 `np.sum()` 조치에 대해 `x` 요소를 한 단락 인수로써 넘겨 내부 전달함으로써 `x`의 고유 원소들을 능히 합할 수조차 있었습니다.

```python
In [18]: x = np.array([1, 2, 3, 4])
         np.sum(x)
Out[18]: 10
```

As another example, the `reshape()` method returns a new array with the same elements as `x`, but a different shape.

또 다른 제2의 다른 예제 수립으로서, 일명 부과 `reshape()` 당 메서드는 숱한 `x` 와 무결이 동일 무관한 이 기저 원소 단원들을 십분 동일시 가지지만 전혀 다른 형상을 취해 띈 하나의 제3 새로운 배열 덩이를 여지 반환해 꺼내 줍니다.

(Better literal: 또 다른 예로써, `reshape()` 메서드는 `x` 와 동일한 원소들이지만 이내 다른 형태를 지닌 하나의 새로운 배열 단위를 반환합니다.)

We do this by passing in a `tuple` in our call to `reshape()`, in this case `(2, 3)`.

우리는 지표 `reshape()` 부름 호출 명령 내부로 거론 이 경우 예제선상 `(2, 3)` 에 기저하는 하나의 `tuple` 객체 단면을 구태 건네 전달 주입함으로써 직접 이것 사항을 수행 일궈 달성해 냅니다.

(Better literal: 우리는 우리의 `reshape()` 호출 시 이 경우 `(2, 3)` 와 필시 같은 하나의 단일 `tuple`을 전입 패스 시킴으로써 이 소임을 지극히 행합니다.)

(Best literal: 우리는 이 상황의 경우 곧 `(2, 3)` 튜플과 필경 같은 하나의 거론 `tuple`을 수반 우리가 호출하는 해당 `reshape()` 내부 문맥 속으로 내밀어 패스 전달함으로써 이것 작업을 성사 수행합니다. ) -> 우리는 이 경우 `(2, 3)`이라는 하나의 `tuple`을 우리의 `reshape()` 호출 내부로 전달함으로써 이것을 행합니다.

This tuple specifies that we would like to create a two-dimensional array with 2 rows and 3 columns.[2]

이 튜플은 우리가 2개의 행들과 3개의 열들을 가지는 2-차원 배열을 생성하기 원한다는 것을 지정합니다.[2]

In what follows, the `\n` character creates a _new line_.

이어지는 내용에서, `\n` 문자는 하나의 새로운 줄 (_new line_) 을 생성합니다.

```python
In [19]: x = np.array([1, 2, 3, 4, 5, 6])
         print('beginning x:\n', x)
         x_reshape = x.reshape((2, 3))
         print('reshaped x:\n', x_reshape)
beginning x:
 [1 2 3 4 5 6]
reshaped x:
 [[1 2 3]
  [4 5 6]]
```

The previous output reveals that `numpy` arrays are specified as a sequence of _rows_.

이전 출력은 `numpy` 배열들이 _행들(rows)_ 의 시퀀스로서 지정됨을 드러냅니다.

This is called _row-major ordering_, as opposed to _column-major ordering_.

이것은 _열-우선 순서(column-major ordering)_ 에 반대되는 개념으로서, _행-우선 순서(row-major ordering)_ 라고 불려집니다.

`Python` (and hence `numpy`) uses 0-based indexing.

`Python` (그리고 그로 인해 `numpy`)은 0-기반 인덱싱을 이용 사용합니다.

This means that to access the top left element of `x_reshape`, we type in `x_reshape[0,0]`.

이것은 `x_reshape` 의 가장 최상단 좌측 요소 원소에 호출 접근하기 위해, 단면 우리가 `x_reshape[0,0]` 을 타입해 입력한다는 것을 의미합니다.

```python
In [20]: x_reshape[0,0]
Out[20]: 1
```

Similarly, `x_reshape[1,2]` yields the element in the second row and the third column of `x_reshape`.

이와 유사히, 치수 `x_reshape[1,2]` 는 도식 `x_reshape` 의 정해진 두 번째 행 구획 단위와 단연 세 번째 위치한 열 안에 몸담은 기저 대상당 원소를 추출 산출해 넘겨 줍니다.

```python
In [21]: x_reshape[1,2]
Out[21]: 6
```

Similarly, `x[2]` yields the third entry of `x`.

유사하게, `x[2]` 역시 거뜬 해당 변수 `x` 의 지정 세 번째 구성 기입 단락 항목을 산출합니다.

Now, let’s modify the top left element of `x_reshape`.

이제 여분, 그 `x_reshape` 의 단면 가장 윗단 왼쪽 단위 원소를 조치 수정해 봅시다.

To our surprise, we discover that the first element of `x` has been modified as well!

우리의 놀라움에도 불구하고 더하여 발견 확인컨대, 우리는 역시 변수 `x` 내부 그 첫 순서 원소체 또한 덩달아 덧붙여 함께 교체 수정되어 버렸다는 기이 현상을 여지 없이 발견합니다!

```python
In [22]: print('x before we modify x_reshape:\n', x)
         print('x_reshape before we modify x_reshape:\n', x_reshape)
         x_reshape[0,0] = 5
         print('x_reshape after we modify its top left element:\n', x_reshape)
         print('x after we modify top left element of x_reshape:\n', x)
x before we modify x_reshape:
 [1 2 3 4 5 6]
x_reshape before we modify x_reshape:
 [[1 2 3]
  [4 5 6]]
x_reshape after we modify its top left element:
 [[5 2 3]
  [4 5 6]]
x after we modify top left element of x_reshape:
 [5 2 3 4 5 6]
```

> 2 Like lists, tuples represent a sequence of objects. Why do we need more than one way to create a sequence? There are a few differences between tuples and lists, but perhaps the most important is that elements of a tuple cannot be modified, whereas elements of a list can be.

>

> 2 리스트들과 같이, 튜플들은 객체들의 구조 한결 시퀀스를 수반 대표하여 나타냅니다. 무슨 심산 연유로 대체 우리는 상기 일개 시퀀스를 한 다발 형성 도출 생성하기 위하여 단명 주어진 도합적 한 가지 도출 수단 길 그 이상의 추가적인 방책 방법을 강구 구비하여 요구로 삼아야 필요합니까? 튜플 조각 단위들과 이 리스트 구조물들 체제 세력 간에는 기기묘묘 약간의 제반 차이점들이 여러 산재하지만, 그래도 어쩌면 아마도 필경 제일 막중이 가장 중요한 차이 핵심 요점은 즉 일언 하나의 거론 리스트 구성 요소단들은 거든 조치 수정 변경 통제가 차후 될 역량이 있는 것과는 판이하게 상반 반면 되게, 무릇 하나의 제반 튜플 체계 단위 원소들은 고스란 절대 조작 변경 통과 수정 될 가능 구석 여지가 전혀 도무지 없다는 전대 미문의 사실점입니다.

Modifying `x_reshape` also modified `x` because the two objects occupy the same space in memory.

무구 `x_reshape` 양식을 교체 수정하는 거론 일련 과정은 도무지 또한 해당 이 두 대상 객체 요소들 쌍방이 컴퓨터 메모리 전산 단위 내 자리에서 위치상 딱 동일 부합 일치하는 연산 공간 자리 표면 점유를 기인 점령하여 차지하고 상주 보전하기 연고 말미암은 연유로 여지 역시 불현 거론 `x` 배열체 또한 변경 수정해 전이 구속 시켰습니다.

(Better literal: 그 두 대상 객체 쌍방이 물리적 메모리 기저 단위 안쪽 동일한 배열 공간을 조우 차지하기 때문의 원인 연유로 결국 `x_reshape` 기호를 수정지어 바꾸는 것은 필시 또한 `x` 단위 까지도 불가 수정했습니다.)

We just saw that we can modify an element of an array.

우리는 지금 막 우리가 한 배열 속 원소를 수정할 수 있음을 보았습니다.

Can we also modify a tuple?

우리가 또한 튜플도 수정할 수 있습니까?

It turns out that we cannot — and trying to do so introduces an _exception_, or error.

우리가 그럴 수 없다는 것이 밝혀집니다 — 그리고 그렇게 하려고 시도하는 것은 _예외(exception)_, 즉 오류를 도입합니다.

```python
In [23]: my_tuple = (3, 4, 5)
         my_tuple[0] = 2
```

```
TypeError: 'tuple' object does not support item assignment
```

We now briefly mention some attributes of arrays that will come in handy.

우리는 이제 유용하게 쓰일 배열들의 몇 가지 속성들을 간략히 언급합니다.

An array’s `shape` attribute contains its dimension; this is always a tuple.

하나의 배열 단위 속 편성된 `shape` 요건 지정 속성은 당 그것의 고유 구조 차원을 거두어 포함 품어 담습니다; 이것 정보 치수는 여간 항상 어김없이 하나의 구조화 튜플입니다.

The `ndim` attribute yields the number of dimensions, and `T` provides its transpose.

이 속성 단위인 즉 `ndim` 요건 속성 기지는 곧 차원 구조들의 세부 총 개수를 투영 추출 산출하고, 반면 `T` 지정 대상은 필시 그것 단위의 상하 전치(transpose)를 맞바로 도출 제공 나타내 산출합니다.

```python
In [24]: x_reshape.shape, x_reshape.ndim, x_reshape.T
```

```python
Out[24]: ((2, 3),
          2,
          array([[5, 4],
                 [2, 5],
                 [3, 6]]))
```

Notice that the three individual outputs `(2,3)`, `2`, and `array([[5, 4],[2, 5], [3,6]])` are themselves output as a tuple.

세 가지 개별적 출력들 `(2,3)`, `2`, 그리고 `array([[5, 4],[2, 5], [3,6]])` 그 자체들이 하나의 튜플로써 출력됨에 주의하십시오.

We will often want to apply functions to arrays.

우리는 종종 함수들을 배열들에 적용하길 원할 것입니다.

For instance, we can compute the square root of the entries using the `np.sqrt()` function:

예를 들어, 우리는 `np.sqrt()` 함수를 사용하여 그 항목들의 제곱근을 계산할 수 있습니다:

```python
In [25]: np.sqrt(x)
Out[25]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

We can also square the elements:

우리는 또한 그 원소들을 제곱할 수 있습니다:

```python
In [26]: x**2
Out[26]: array([25,  4,  9, 16, 25, 36])
```

We can compute the square roots using the same notation, raising to the power of $1/2$ instead of 2.

우리는 2 대신에 $1/2$ 의 거듭제곱으로 올려서 동일한 표기법을 사용하여 그 제곱근들을 계산할 수 있습니다.

```python
In [27]: x**0.5
Out[27]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

Throughout this book, we will often want to generate random data.

이 책 전반에 걸쳐, 우리는 종종 무작위 데이터를 생성하길 원할 것입니다.

The `np.random.normal()` function generates a vector of random normal variables.

이 함수 `np.random.normal()` 체계는 무결 위주 무작위 지정 정규 조치 수량 변수들의 정돈된 하나의 기준 벡터를 가중 창설 출현 생성합니다.

We can learn more about this function by looking at the help page, via a call to `np.random.normal?`.

우리는 구문 인용 부름체인 `np.random.normal?` 부분 지표에 대한 단단한 하나의 호출 지시를 통하여 관련 소임의 그 도움 설명 매뉴얼 단원 페이지 구역을 살펴보아 구경 봄으로써 본거 대상 함수 단위에 관한 수단 결함적 한층 더 다량의 상세 사실들을 여타 습득 파악 배울 지능 역량이 마련됩니다.

The first line of the help page reads `normal(loc=0.0, scale=1.0, size=None)`.

이 도출 매뉴얼 도움 열람서 페이지 지면 단락의 시초 첫 번째 라인 줄거리는 다름 거론 구문 `normal(loc=0.0, scale=1.0, size=None)` 으로 기저 표기 읽혀 묶입니다.

This _signature_ line tells us that the function’s arguments are `loc`, `scale`, and `size`.

이 _시그니처(signature)_ 라인은 해당 함수의 인자들이 `loc`, `scale`, 그리고 `size` 임을 우리에게 말해줍니다.

These are _keyword_ arguments, which means that when they are passed into the function, they can be referred to by name (in any order).[3]

이들은 _키워드(keyword)_ 인자들인데, 이것은 그들이 함수 안으로 전달되어질 때 (어떤 순서로든지) 이름으로써 거론 참조될 수 있음을 의미합니다.[3]

By default, this function will generate random normal variable(s) with mean (`loc`) 0 and standard deviation (`scale`) 1; furthermore, a single random variable will be generated unless the argument to `size` is changed.

기본값으로, 이 함수는 평균(`loc`) 0과 표준 편차(`scale`) 1을 가지는 무작위 정규 변수(들)를 생성할 것입니다; 더욱이, `size`에 대한 인수가 변경되지 않는 한 단 하나의 무작위 변수가 생성될 것입니다.

We now generate 50 independent random variables from a $N(0, 1)$ distribution.

우리는 이제 $N(0, 1)$ 분포로부터 50개의 독립적인 무작위 변수들을 생성합니다.

```python
In [28]: x = np.random.normal(size=50)
         x
Out[28]: array([-1.19,  0.41,  0.9 , -0.44, -0.9 , -0.38,  0.13,  1.87,
                -0.35,  1.16,  0.79, -0.97, -1.21,  0.06, -1.62, -0.6 ,
                -0.77, -2.12,  0.38, -1.22, -0.06, -1.97, -1.74, -0.56,
                 1.7 , -0.95,  0.56,  0.35,  0.87,  0.88, -1.66, -0.32,
                -0.3 , -1.36,  0.92, -0.31,  1.28, -1.94,  1.07,  0.07,
                 0.79, -0.46,  2.19, -0.27, -0.64,  0.85,  0.13,  0.46,
                -0.09,  0.7 ])
```

We create an array `y` by adding an independent $N(50, 1)$ random variable to each element of `x`.

우리는 `x`의 각각의 원소에 하나의 독립된 $N(50, 1)$ 무작위 변수를 더함으로써 배열 `y`를 생성합니다.

```python
In [29]: y = x + np.random.normal(loc=50, scale=1, size=50)
```

The `np.corrcoef()` function computes the correlation matrix between `x` and `y`.

함수 `np.corrcoef()` 는 `x` 와 `y` 사이의 상관관계 행렬을 도출 계산 계산합니다.

The off-diagonal elements give the correlation between `x` and `y`.

당 부가 비-대각 구조 원소단 항목들은 이어서 각 `x` 및 대상 `y` 원소 덩이 양단 사이 간의 지상 상관관계 치수를 측정 제공합니다.

```python
In [30]: np.corrcoef(x, y)
Out[30]: array([[1.  , 0.69],
                [0.69, 1.  ]])
```

If you’re following along in your own `Jupyter` notebook, then you probably noticed that you got a different set of results when you ran the past few commands.

만약 여러분이 여러분 스스로의 고유한 `Jupyter` 노트북 안에서 일치해 따라가고 있는 조건 국면 중이라면, 그렇다면 단면 당신은 당초 바로 조금의 지저 지난 이전 몇몇 개의 낱 명령어 조작문들을 구동 실행시켰던 그 시기에 여러분 측정자가 전혀 아주 다르게 딴판 상반된 단일 일개 세트 단위 부류 결과물들을 다수 취득 확보 얻어 도출해 가졌음을 다분 일찍이 알게 되었을 터일 것입니다.

(Better literal: 만일 당신이 당신 고유 자신만의 그 `Jupyter` 노트북 구동 환경 내에서 발맞춰 따라서 진행 전개 지위를 맞이하고 있다면, 그때라면 독자 여러분은 아마 필경 당 당신이 한정 통과시킨 지난 몇 개의 지휘 명령어 모음들을 가동 실행했을 당시 당신 스스로가 판이하게 완전히 상호 다른 무관한 결과 도출의 한 세트를 차례 얻어 확보했음을 분명 눈치채 점검 알아차렸었을 법합니다.)

(Best literal: 만약 당신이 당신 고유 자신의 `Jupyter` 노트북 안에서 따라 오고 있다면, 당신은 아마도 당신이 지난 몇 개의 명령어들을 실행했을 때 구별되는 다른 일련 세트의 결과들을 얻었음을 분명 알아챘을 것입니다.)

In particular, each time we call `np.random.normal()`, we will get a different answer, as shown in the following example.

특히, 우리가 `np.random.normal()` 을 빈번 호출 이끌어 부를 대차 그 무렵 각 부분 시기 시간 단위 찰나 마다, 이어 따르는 다음 지표 예제 도식 상에서 도출 나타내 보여지는 형상 일면처럼 우리는 매양 줄곧 내내 다르게 판이한 무려 다른 측정 정답 답변 추출물을 구태여 얻게 도처에 발현 될 속성입니다.

(Better literal: 특별 특히, 이어지는 다음의 안내 표식 예제 단위에서 보여지는 양상과 마침 진배없이, 매 양번 우리가 어김 `np.random.normal()` 단위 함수 구문 단원을 호출 이끌 조치 부를 각각의 각 때 찰나 시기 무렵마다, 일련으로 우리는 다분 상이로 전혀 다른 차원에 걸친 응답 답안 지표치 결과를 도출 거두어 획득 취득하게 당면 구성될 공산 규약입니다.)

(Best literal: 특히, 우리가 `np.random.normal()` 을 호출하는 매 시간 각각에, 다음 예시에서 보여지는 것처럼 우리는 구별되는 다른 정답을 얻게 될 것입니다.)

```python
In [31]: print(np.random.normal(scale=5, size=2))
         print(np.random.normal(scale=5, size=2))
[ 4.28  2.59]
[ 4.62 -2.54]
```

In order to ensure that our code provides exactly the same results each time it is run, we can set a _random seed_ using the `np.random.default_rng()` function.

우리 기치 부과 코드 구획이 무관히 구동 실행되는 구절 시점 각각의 매 시기 단락 무렵마다 전적으로 모조리 단연 똑같이 완전히 판이함 없이 동일 일치한 거출 결과 양식 쌍들을 정확무오하게 제공 인도해 표출한다는 일면 진면목 가치를 단방 장담 확실히 보장 공언하기 위한 조치로써, 우리 측은 구성 단위체 `np.random.default_rng()` 보편 기능 함수 단락을 단방 동원 차용하여 일원 하나의 기저 무작위 단위의 추정 초기화 생성 추출 요소 이른바 _랜덤 시드(random seed)_ 기준 씨앗 기반 단위를 체계적으로 도출 설정 지어 통제 다잡아 놓아둘 수립 체계 방안이 있습니다.

(Better literal: 우리의 코드가 그것이 구동 실행되는 각 시간마다 정확히 동일 일치하는 결과물들을 단언코 일률 산출해 제공하도록 장담 구속 확실히 보장 조치하기 일언 위하여, 단연 우리 당 편은 단번 당 함수 기능성 `np.random.default_rng()` 단위 본연을 거듭 적극 이용 사용하여 하나의 조작 구성 시안 일명 즉 _랜덤 시드(random seed)_ 조작 단위 체계를 선언 설정 확보해 놓을 능력 방안이 있습니다.)

(Best literal: 우리의 코드가 실행되어지는 지명 시간들 매번마다 정확히 동일한 결과치들을 산출 결론 맺어 반환 제공함을 단단 장담 보장하기 위해, 우리는 요소 함수 `np.random.default_rng()` 를 사용하여 하나의 _무작위 시드(random seed)_ 를 설정 규합할 수단을 가집니다.)

This function takes an arbitrary, user-specified integer argument.

이 도출 함수 모형체는 하나의 단연 단독 임의적이고도, 해당 부과 사용자가 지정 특정이 부여된 한 정수 배열 형식의 인수 대상을 내포하여 여지 가집니다.

If we set a random seed before generating random data, then re-running our code will yield the same results.

만일 우리가 조작 무작위 구성 형태의 데이터 치수들을 창작 발생 생성시키기 이면 전 단에 한 차례 무단 정규 랜덤 시드 발생기를 조치 고정화 설정해 냅둔다면, 단언 당초 그때부턴 우리 코드를 재-실행 구동 재 가동 시키는 소속 행위 단락은 전적으로 변함 없이 동일 일치무오한 추출 결과물 구조들을 온당 산출 거두어 반환 넘겨줄 것입니다.

(Better literal: 만일 우리가 무작위 데이터를 생성하기 이전 시점에 하나의 랜덤 시드를 사전 고유 설정지어 둔다면, 그럼 তখন 우리 코드 체계를 순행 재-실행 구동하는 행동 지위는 다름없이 여전히 그와 동일한 무관한 부과 결과 수치치 쌍들을 수수 거두어 내 산출 도출해 줄 작정일 기조입니다. )

(Best literal: 만약 우리가 무작위 데이터를 생성하기 전에 하나의 랜덤 시드를 설정한다면, 우리의 코드를 재-실행하는 것은 동일한 결과들을 산출할 것입니다.)

The object `rng` has essentially all the random number generating methods found in `np.random`.

해당 산하 이 거론 객체 단위물체 `rng` 체계는 모름지기 필수 본질에 충실히 기인하여 다분 `np.random` 부락 안에 머물러 속속 지어져 발견 내포된 그 어떠한 모든 단일 무작위 산출 랜덤 수 도출 전개 생성기 본연 메서드들을 단연코 거의 모조리 일체 죄다 한 축으로 보유 내포해 지니기 따름입니다.

(Better literal: 바로 이 `rng` 구도 객체 덩이는 본래 다름 실질적으로 거진 모두 전부의 `np.random` 안에서 당초 흔히 포착 발견 출현될 모든 지체 무결 무작위 발생 넘버 난수 추출 생성 수치 메서드들을 여분 없이 실상 보유에 지닙니다.)

(Best literal: 객체 `rng`는 본질적으로 `np.random` 안에서 발현 발견되어 지는 다분한 무작위적 조작 숫자 생성 수단 제반 메서드들 단위를 단연 모두 지닙니다.)

Hence, to generate normal data we use `rng.normal()`.

그러므로, 단락 지표 정규 기조 데이터 조치물 군을 곧장 단번 생성 구축 조치하기 무단 목적을 위해 모름지기 우리는 다수 당 수단 함수인 `rng.normal()` 도구 단위를 단연 적극 이용 택해 사용합니다.

(Better literal: 단언 그러므로, 정규 체계 데이터 성분들을 단편 생성 창조 하기 목적 위해 당장 우리는 필시 구조 조치인 `rng.normal()` 단위를 곁들여 사용합니다. )

(Best literal: 그러므로, 정규 데이터를 단편 생성해 냄에 우린 `rng.normal()` 을 거론 사용합니다.)

```python
In [32]: rng = np.random.default_rng(1303)
         print(rng.normal(scale=5, size=2))
         rng2 = np.random.default_rng(1303)
         print(rng2.normal(scale=5, size=2))
[ 4.09 -1.07]
[ 4.09 -1.07]
```

Throughout the labs in this book, we use `np.random.default_rng()` whenever we perform calculations involving random quantities within `numpy`.

이 단원 지침서 배보 문헌 교재 내 무수한 전반 실습 과정 모음들 내내 전 구획을 걸치며 거쳐, 전결 우리는 단연 해당 `numpy` 패키지 테두리 기반 단락 내 공간 속에서 단편적인 일회 무작위 요소 추출 난수 랜덤 기인 산출 속성 수량 관련 분량 수치들을 매번 포함해 기인 동반 연관 수반해 처리짓는 가동 수리 계산 단위 조작들 부락을 연이어 우리가 차례 수행 실시 해 구동 펼칠 작정 무렵 때일 때 마다 단독 `np.random.default_rng()` 단편 구문을 한 겹씩 늘 이끌어 매번 사용을 적용 도출합니다.

(Better literal: 이 교재 본서 구간 내에 포진된 당해 실습 단락들 전방 과정들을 모조리 두루 여지 걸쳐 지날 때 마다, 필시 당분 우리는 해당 `numpy` 패키지 울타리 내면 부근 속에서 모상 무작위 도출 랜덤 체제 수량 구조값들을 어김 동반 수반 시키어 연관 짓게 마련인 단원 계산 연산 작용 단계를 우리들이 통제 차순 수행할 그 어떤 숱한 시기 찰나 이든 간에 당 함수 `np.random.default_rng()` 모델 단위 도구를 어김 차용 지목해 줄곧 사용하여 둡니다.)

(Best literal: 이 지침 책 전반의 실습 구간들 제반에 걸쳐, 우리는 `numpy` 구조 안에서 랜덤 무작위 성향 수량 부문을 빈번 동반해 포함시키는 계산들을 우리들이 거듭 수행 치룰 거시적 해당 무렵 때마다 언제나 `np.random.default_rng()` 를 다분 기조 사용으로 거둡니다.)

In principle, this should enable the reader to exactly reproduce the stated results.

아무렴 보편 정석적 원칙에 입각하여 기인하자면, 본 이러한 선제 가동 조항 조치 설정 행위 하나가 으레 필히 마땅히 배포 해당 독자 제반 분들 여러분으로금 일명 하여금 뚜렷이 상단 명시 거론 표기된 명기 수치 단위 도출 동일 결과값 일체물 다발들을 단연 똑같이 확고 정밀히 상호 비교 모방 재현 추출 형성 해 재생성 산출할 필시 단연 가능하도록 무구히 허용 유효하게 일체 만들어 내어 성립시켜 주어야 할 의무적 노릇일 테입니다.

(Better literal: 단조적 기저 원칙상 근거에 기초하여, 당 이것 행태는 짐짓 거뜬 독자 측에 향하여 확정 부과되어 선언 명기 지칭된 무결 지수 결과 도출 단위물들을 이따금 매우 전적으로 정밀히 완전 무오 재생산 재현 구축토록 무척 단박 가능케 단연 허용 수립해 이끌어야만 할 가치 작정일 사연입니다.)

(Best literal: 원칙에 기인 입각하여, 이 수단은 거듭 다를 바 없이 독자 여러분 측으로 치중해 명기 기명 단락 제시된 이 단위적 성과 결과들을 매 양번 한 치 오차 없게 정확 똑같이 조치 재생산 확립 창출 하도록 공산 가능 작용해 거들어 유효 지워야만 당위할 테일 법할 심산입니다.) -> 원칙적으로, 이것은 독자 여러분으로 하여금 서술 기명된 모종 결과 단위 표기물들을 가득 조금치 차이 없이 오롯이 정확무오 조치 동일 모방 재생산 단연시켜 출현 도출해 능히 낼 수 조달단 되도록 당분 허용 가능하게끔 마땅 이내 만들어 단연코 줄 노릇일 것입니다. -> 원칙적으로, 이것은 독자로 하여금 명시된 결과들을 정확하게 재현할 수 있게끔 해야 합니다.

However, as new versions of `numpy` become available, it is possible that some small discrepancies may occur between the output in the labs and the output from `numpy`.

그러나 다만, 당 신규 판본의 새로 거듭난 추가 출시 `numpy` 갱신 구성 버전들이 줄지어 발간 계속 지속 도래 이용 가능하게 전변 차츰 진척 진화됨에 다소 발맞추어, 아마 일전에 수록 보장 기명된 지면 이 당 실습 단원 과정 지침 속 당 결론 도출 출력 결과물 항목과 추후 진단 여러분 고유의 그 새 단장 `numpy` 판별 프로그램 상으로 말미암아 수반 거론된 실 결과물 도출 파열 출력 덩이 측 양자 간격 사이에 일견 이따위 불일치적 지수 기조의 얼마 적은 규모 차원의 일소 소규모 작은 상충 차이 엇갈림 오차 단위 분량 들이 혹여 뜻과 외려 아주 종종 불쑥 발생 생길 연유적 도출 구석 가능성이 잔재 필연 존재 마련합니다.

(Better literal: 허나 그러나 무릇, 더 새롭게 차후 갱신 도입될 `numpy` 측 부과 버전 단위들이 지속 도래해 차차 당면 이용 허용됨에 이내 따라 발 맞추어, 가히 본 시안 실습 단락 과정 내용 단원 안에 당초 포함 적시된 숱한 일련 단결 도출 출력물 정보와 그 후 다가올 저 단연 최신 `numpy` 엔진 측에 의한 일격 실 도출 출력 구획 이 양 갈래 체제 구조 간 쌍방 대치 사이면에 거진 나름 그 어떤 자잘자잘 작은 형상 규모 수치의 일부 단위 어긋난 엇나감 오차 단편 발생 상쇄의 오류 차이 지표들이 불현 도출해 빚어 생길 공산성 한편 가능성은 다분 여분 있습니다.)

(Best literal: 그러나 여전히, 신규 버전들의 여타 `numpy` 객체군 출시들이 조작 조달 가용 가능성 구조를 띄어 다분 도래해 마주함에 수순을 따라, 당초 서술 당 실습 구간 단면 지대 부락상의 기출 모형 도출 출력 체제물과 저 종식 개편된 당 `numpy` 모체 조치 패키지에 거듭 근거 소산된 단별 산출 모조 결과 출력 양태 그 쌍방 사이 구도 단면에 얼마건 모종의 다소 조잡 작은 소수 균열 차이 단위 불일치 간극 차 들이 여태 일어 발현 나 도출될 수 무던 있는 여분 가능 구조 양상은 부쩍 가변 다행히 존재합니다.) -> 그러나, `numpy`의 신규 버전들이 사용 가능해짐에 따라, 이 실습에서의 출력과 해당하는 `numpy`의 출력 양자 간 사이에 몇몇 국소적인 작은 수치의 불일치 차이들이 도출 발생할 수 있는 가용 가능 여부성은 존재합니다.

The `np.mean()`, `np.var()`, and `np.std()` functions can be used to compute the mean, variance, and standard deviation of arrays.

여러 제반 조치 `np.mean()`, `np.var()`, 및 그리고 아울러 `np.std()` 요소 부과 함수들은 대거 배정된 당 배열들의 평균, 거듭 분산, 그리고 종례 표준 편차를 각기 다분 연산 거론 계산해 내기 치중 조치 목적으로 다분 두루 활용 채용 쓰일 사용 가능의 구조 기질 수를 지닙니다.

(Better literal: 이 표기 `np.mean()`, `np.var()`, 및 마지막 단면 `np.std()` 지정 매개 함수 항목 구절 부문들은 이 배열들의 통칭 평균 치, 다수 분산, 그리고 곁들인 수량 표준 편차 단위를 각각 가늠 추출 계산해 빼내기 용단 지향을 위해 단락 사용 채택 구동 될 양상 가용 수단입니다.)

(Best literal: `np.mean()`, `np.var()`, 그리고 `np.std()` 함수들은 배열들의 평균, 분산, 및 표준 편차를 계산하기 위해 사용될 수 있습니다.)

These functions are also available as methods on the arrays.

이 구조 기능 함수 단원들은 다분 또 한편으로 도출 배열들 구조 제반 위편 상의 지정 도출 메서드 도구적 양태 명목 형태로도 모조리 거듭 유효 이용 소급 사용 가능 적격의 여지가 됨입니다.

(Better literal: 이것 단위들 본 함수 조작 단위들은 또한 여지 배열 무리 덩이 자체 단면 위의 고유 산하 부과된 형태의 단위 메서드 양식적 도구들로도 전속 동일히 유효히 수수 이용 가능할 국면에 한 체제 있습니다. )

(Best literal: 이 기능 함수들은 해당 한편 배열 체계 요소 단면 상측의 개체에 딸린 제반 부속 구획 도구 성질 메서드 조차로서 또한 수월 이행 이용 가능한 면모를 부쩍 지닙니다.) -> 당 함수들은 또한 해당 배열들 그 위에서의 제반 단편 메서드 제어 수단 도구 용도로도 무결 사용 이용 공고 가능 체제입니다.

> 3 `Python` also uses _positional_ arguments. Positional arguments do not need to use a keyword. To see an example, type in `np.sum?`. We see that `a` is a positional argument, i.e. this function assumes that the first unnamed argument that it receives is the array to be summed. By contrast, `axis` and `dtype` are keyword arguments: the position in which these arguments are entered into `np.sum()` does not matter.

>

> 3 `Python`은 여전히 또한 _위치 지정(positional)_ 인자들 명목 측면 단위를 구사 채용 사용합니다. 해당 부류 위치 지정 인자들은 저 전형 키워드 도구적 수단을 단락 거듭 쓸 지정 조달 전면 필요를 당면 갖추지 일체 않습니다. 단일 하나의 이러한 일례 구조 예 단위를 거듭 시야로 확인해 보려면 이내 당 단면 명령으로 단어 `np.sum?` 부령 부락을 내내 수동 타입 구동 기입해 펼쳐 입력해 보십시오. 여기서 우린 단연 저 `a` 지칭물 기호가 하나의 자명한 단독 이 위치 규정 지정 인수임을 어김 여과 없이 능히 알 단언 보게 됩니다, 곧 다수 다시 부연 풀이 하자면 당일 이 지칭 함수가 곧 이내 제법 자신이 일순 접수 인도 전달 수취 받는 수순 그 제 1 첫 차례의 최우선 번째 별도 비-명칭 호칭 없는 미 기명 인자 요소 하나 대상물을 다름 필시 곧 합산 기조로 합해져 통계 단면 나열될 단체 타깃 배열일 도치 것 구조물 요소라고 일방 먼저 으레 지례 사전 가정 간주 지어 놓는다는 단언 형상적 의미 모식의 구도인 통찰 셈입니다. 이 단락 체제 규칙에 대조 조작 대비 극히 되게, 단언 `axis` 쪽과 무릇 부기 `dtype` 측면은 다분 당 키워드 인자 규격 체계들에 분명 소속 해당합니다: 다시 일컬어 이들 특정 지시 인수 객체 요인들이 어김 제반 `np.sum()` 대상 기능 함수 요소 내부로 무릇 다가 넘기어 전파 전달 기입 투입 조치 이행 조작 되어지며 놓일 필시 당 구획 그 위치 지칭 표기 단락 자체 단원 요소는 전격 조금도 중요 구획 사안으로 여지껏 필경 결코 문제 다발이 되며 단락 지어 해당 당면하지 아무 일체 무릇 아니함을 의미 뜻 기치 나타내 증명 보여줍니다.

```python
In [33]: rng = np.random.default_rng(3)
         y = rng.standard_normal(10)
         np.mean(y), y.mean()
Out[33]: (-0.11, -0.11)
```

```python
In [34]: np.var(y), y.var(), np.mean((y - y.mean())**2)
Out[34]: (2.72, 2.72, 2.72)
```

Notice that by default `np.var()` divides by the sample size _n_ rather than $n - 1$; see the `ddof` argument in `np.var?`.

단순히 기본 기저 설정값 기준으로, 저 산출 `np.var()` 도식 함수가 곧 일면 수식 분모 분수상 제수 통제 단위로 필시 관점 대강 전개 공식인 일명 기치 분모 단위 $n - 1$ 구조 치수가 아니라 조작 당 곧추 지목 본체 샘플 크기 단위 전역 명목 지수인 곧 저 단위 규모 _n_ 만을 전면 통째 단연 고스란 전격 분모 적용해 제수 삼아 나눈다는 결론 구획 내막 사실적 당위 단단 점을 특히 단연 한 지목 유념 지적해 두십시오; 부가 부수 단락 참고 검토 조언을 필시 원하신다 가령 한다면 단락 곁들여 `np.var?` 요소 문서 내용 구간 단면에 표기 명시되어 출몰한 둔기 지목 `ddof` 구술 대상 지칭 인자 항목을 부근 면밀 단락 참고해 부디 한 번 꼭 보십시오.

```python
In [35]: np.sqrt(np.var(y)), np.std(y)
Out[35]: (1.65, 1.65)
```

The `np.mean()`, `np.var()`, and `np.std()` functions can also be applied to the rows and columns of a matrix.

부과 `np.mean()`, 조작 `np.var()`, 나열 및 단언 명칭 `np.std()` 요소 묶음 구성 지수 함수 단위 객체 요소들은 다단 또한 별도 한 행렬 체제 지표 대상 단위가 개거 품은 당 여러 그 무수 행들 구도와 단면 무수한 열들 쪽 배열 방면 지표 방향 측면을 특정 지향 목표 도출해 겨냥한 채로 무수 단락 각각 나뉘어 분리 지정 산개 특정 통제 단전 조작 적용 역시 가능 가용 될 부가 기능의 가능 조달 구조 여지 수단을 가지어 마련해 보유합니다.

To see this, we construct a $10 \times 3$ matrix of $N(0, 1)$ random variables, and consider computing its row sums.

본 거론 기능 지점 이 사실 거동 작동 양태 부분을 확립해 확인 가늠 조치 관찰하여 살펴 알기 뻔한 목적 여부의 위해, 우리는 단위 1개 $N(0, 1)$ 기반 정규 구조 무작위 추론 변수 구성 항목 단위들이 결집 집단 이루어 무수 포진된 단위 1 단락의 거대한 일률 $10 \times 3$ 매트릭스 다차 행렬체를 시현 구성 생성 제작 지어 확립 조치하며, 이내 그리고 나서 이내 그것 단위 구조 내부 고유의 각각의 대상 분리 행 무리 단체들의 다단 단면 각 낱 합 측률 요소를 여간 거론 계산 단원 도출 작용해 뽑아내 이윽고 무릇 수립 해 볼 이 여지 국면을 깊게 상정 고려 여부 조치 타진 단언 시도 강구 해 봅니다.

```python
In [36]: X = rng.standard_normal((10, 3))
         X
Out[36]: array([[ 0.23, -0.35, -0.28],
                [-0.67, -1.06, -0.39],
                [ 0.48, -0.24,  0.96],
                [-0.2 ,  0.02,  1.55],
                [ 0.55, -0.51, -0.18],
                [ 0.54,  1.94, -0.27],
                [-0.24,  1.  , -0.89],
                [-0.29,  0.88,  0.58],
                [ 0.09,  0.67, -2.83],
                [ 1.02, -0.96, -1.67]])
```

Since arrays are row-major ordered, the first axis, i.e. `axis=0`, refers to its rows.

앞서 일괄 상 배열들의 속성 단위가 주로 통칭 행-우선 편향 중심 기반으로 도출 배열 질서 편제 정렬 결집되는 그 내재 속성이 만연 주효한 기인하기 탓에 이끌리어, 지정 당 첫 제 1 우선 단면 번째 단락 주요 단열 기조 지칭 축, 당초 이를테면 단어 구문 표기상 즉 지정 기표 매개 요인 `axis=0` 구역 지정 문건은 이내 전방 당해 속성 구조 그 배열 자체 본원적의 행 단위 구성 조각들을 단일 단면 직접 명시해 단언 부과 기명 참조 지칭 단독 일컫게 전단 됩니다.

We pass this argument into the `mean()` method for the object `X`.

우리 측은 단연 본 지정 해당 표상 지목 이 인자 지수 매개 항목 단원 구조 수치를 전방 단독 대상 구획 객체물인 바 일개 `X` 체제를 위해 구비 소급 보유 배정 단락 마련 지어진 그 본위 지정 `mean()` 호출 매개 단위 표적 메서드 구조 부락 단락 요소 안쪽 속 공간으로 가차 일언 전입 이입시켜 건네 주입 당장 단연 거론 투가 투입 통과 넘겨주기 과정을 통해 패스 시킵니다.

```python
In [37]: X.mean(axis=0)
Out[37]: array([ 0.15,  0.14, -0.34])
```

The following yields the same result.

단연 저 다음 잇따라 부연 등장하는 기명 이어질 조치 단락 호출 역시 또한 어김 동차히 완전히 무관 앞서 것과 무진 단연 일절 다를 바 모조리 동일 기명 결과 도출 양태를 산출해 내어 이내 보여 부연 산단 양도 내어 줍니다.

```python
In [38]: X.mean(0)
Out[38]: array([ 0.15,  0.14, -0.34])
```

---

## Sub-Chapters (하위 목차)

[< 2.3.2 Basic Commands](../2_3_2_basic_commands/trans1.html) | [2.3.4 Graphics >](../2_3_4_graphics/trans1.html)
